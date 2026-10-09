import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client

if os.path.exists(".env.lab"):
    load_dotenv(".env.lab", override=True)
else:
    load_dotenv()

# Verificações de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DEEPINFRA_API_TOKEN = os.getenv("DEEPINFRA_API_TOKEN")

if not all([GEMINI_API_KEY, SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN]):
    print("❌ ERRO: Faltam variáveis de ambiente no .env (GEMINI_API_KEY, SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN).")
    exit(1)

# 1. Carregar documentos Markdown
from pathlib import Path

print("Buscando arquivos Markdown de Matemática (Teoria)...")
base_dir = Path("../../content")
directories_to_scan = [
    base_dir / "fundamental-2",
    base_dir / "medio",
    base_dir / "superior"
]

valid_files = []
for directory in directories_to_scan:
    if directory.exists():
        for file_path in directory.rglob("*.md"):
            # Apenas arquivos dentro da pasta 'ebooks', ignorando exercícios e infra
            if "ebooks" in file_path.parts and not file_path.name.endswith("-exercicios.md") and not file_path.name.startswith("_"):
                valid_files.append(file_path)

if not valid_files:
    print("ERRO: Nenhum e-book atômico encontrado em content/fundamental-2 ou content/medio.")
    exit(1)

print(f"Encontrados {len(valid_files)} e-books para ingestão.")

docs = []
for file_path in valid_files:
    try:
        loader = TextLoader(str(file_path), encoding='utf-8')
        docs.extend(loader.load())
    except Exception as e:
        print(f"Erro ao carregar {file_path}: {e}")

print(f"SUCESSO: {len(docs)} documentos carregados.")

# 2. Fatiar (Split) os documentos usando MarkdownTextSplitter
print("Fatiando documentos preservando a estrutura...")
markdown_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = markdown_splitter.split_documents(docs)
splits = [s for s in splits if s.page_content.strip()]
print(f"Documentos divididos em {len(splits)} pedacos (chunks).")

# 3. Gerar Embeddings via DeepInfra (BAAI/bge-m3)
print("Inicializando Embeddings do DeepInfra...")
embeddings = OpenAIEmbeddings(
    model="BAAI/bge-m3",
    openai_api_base="https://api.deepinfra.com/v1/openai",
    openai_api_key=os.getenv("DEEPINFRA_API_TOKEN", ""),
    check_embedding_ctx_length=False
)

# 4. Inserir no Supabase (pgvector) em Lotes (Batches) para evitar erro 429 do Gemini (Free Tier)
print("Conectando ao Supabase e inserindo vetores (com pausas para a API Gratuita)...")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

batch_size = 100
for i in range(0, len(splits), batch_size):
    batch = splits[i:i + batch_size]
    print(f"Processando lote {i//batch_size + 1} de {(len(splits) + batch_size - 1)//batch_size}...")
    
    # Tenta inserir, se der erro de cota, espera e tenta de novo
    retries = 3
    while retries > 0:
        try:
            SupabaseVectorStore.from_documents(
                batch,
                embeddings,
                client=supabase,
                table_name="documents",
                query_name="match_documents"
            )
            break # Sucesso, sai do loop de tentativas
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print("Limite da API atingido. Aguardando 10 segundos...")
                time.sleep(10)
                retries -= 1
            else:
                raise e # Outro erro qualquer

print("SUCESSO FINAL! Todos os documentos foram vetorizados e salvos no Supabase.")

# 5. Atualizar a tabela de matérias disponíveis e notificar a API
print("\nAtualizando a lista de matérias dinâmicas no banco...")
try:
    KNOWN_SUBJECTS = {"matematica", "fisica", "quimica", "biologia", "historia", "geografia", "filosofia", "sociologia", "literatura", "ingles", "espanhol", "artes", "calculo-1"}
    subjects_found = set()
    for fp in valid_files:
        for part in fp.parts:
            if part.lower() in KNOWN_SUBJECTS:
                subjects_found.add(part.lower())
    
    for subject in subjects_found:
        supabase.table("available_subjects").upsert({"subject_name": subject}).execute()
    
    import requests
    try:
        # Notifica o backend em desenvolvimento (se estiver rodando)
        requests.post("http://localhost:8000/api/admin/reload-subjects", timeout=2)
    except Exception:
        pass
        
    try:
        # Notifica o backend em produção (substitua pela URL real se tiver domínio público direto)
        requests.post("https://mobme.educamob.com.br/api/admin/reload-subjects", timeout=2)
    except Exception:
        pass
        
    print(f"Matérias ativas identificadas e injetadas no prompt: {', '.join([s.capitalize() for s in subjects_found])}")
except Exception as e:
    print(f"Aviso: Erro ao atualizar as matérias dinâmicas: {e}")

