import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client
import hashlib
import json

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

print(f"Total de {len(valid_files)} e-books identificados nas pastas.")

# -------------------------------------------------------------
# INGESTÃO INTELIGENTE (Idempotente)
# -------------------------------------------------------------
STATE_FILE = "ingest_state.json"
try:
    with open(STATE_FILE, "r") as f:
        ingest_state = json.load(f)
except Exception:
    ingest_state = {}

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
docs_to_process = []
new_state = {}
files_to_ingest = []

for file_path in valid_files:
    try:
        content_bytes = open(file_path, 'rb').read()
        file_hash = hashlib.md5(content_bytes).hexdigest()
        str_path = str(file_path).replace("\\", "/") # Normaliza barras para evitar bugs no windows/linux
        
        # Mantém no estado atualizado
        new_state[str_path] = file_hash
        
        # Se a hash for igual, o arquivo não mudou. PULA.
        if ingest_state.get(str_path) == file_hash:
            continue
            
        # Adiciona na lista de arquivos que precisam ser vetorizados
        files_to_ingest.append(str_path)
        
    except Exception as e:
        print(f"Erro ao verificar {file_path}: {e}")

if not files_to_ingest:
    print("✅ Nenhum arquivo novo ou modificado. Ingestão pulada. Zero tokens gastos e nenhuma duplicata!")
else:
    print(f"🚀 {len(files_to_ingest)} arquivos novos ou modificados encontrados. Iniciando carregamento e vetorização...")
    
    # Exclui os antigos e carrega os novos
    for str_path in files_to_ingest:
        try:
            # O loader TextLoader do Langchain usa o caminho passado na variável source
            # Deletamos os chunks antigos com a source exata no Supabase antes de inserir os novos
            supabase.table("documents").delete().eq("metadata->>source", str_path).execute()
            # E por segurança, deletamos também a versão com barras antigas (Windows) se houver
            supabase.table("documents").delete().eq("metadata->>source", str_path.replace("/", "\\")).execute()
        except Exception as e:
            pass # Pode dar erro se for um arquivo novo e não existir
            
        try:
            loader = TextLoader(str_path, encoding='utf-8')
            docs_to_process.extend(loader.load())
        except Exception as e:
            print(f"Erro ao carregar texto de {str_path}: {e}")

    # Fatiar (Split) os documentos usando MarkdownTextSplitter
    print("Fatiando documentos...")
    markdown_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = markdown_splitter.split_documents(docs_to_process)
    splits = [s for s in splits if s.page_content.strip()]
    print(f"Documentos divididos em {len(splits)} pedaços (chunks).")

    # Gerar Embeddings via DeepInfra (BAAI/bge-m3)
    print("Inicializando Embeddings do DeepInfra...")
    embeddings = OpenAIEmbeddings(
        model="BAAI/bge-m3",
        openai_api_base="https://api.deepinfra.com/v1/openai",
        openai_api_key=DEEPINFRA_API_TOKEN,
        check_embedding_ctx_length=False
    )

    # Inserir no Supabase
    batch_size = 100
    for i in range(0, len(splits), batch_size):
        batch = splits[i:i + batch_size]
        print(f"Processando lote {i//batch_size + 1} de {(len(splits) + batch_size - 1)//batch_size}...")
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
                break
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    print("Limite da API atingido. Aguardando 10 segundos...")
                    time.sleep(10)
                    retries -= 1
                else:
                    raise e
                    
    # Após sucesso, salva o novo estado
    with open(STATE_FILE, "w") as f:
        json.dump(new_state, f)
        
    print("SUCESSO FINAL! Documentos novos/atualizados foram vetorizados.")

# -------------------------------------------------------------
# 5. Atualizar a tabela de matérias disponíveis e notificar a API
# (Isso ocorre sempre, pois uma pasta pode ter sido apagada ou adicionada)
# -------------------------------------------------------------
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
        requests.post("http://localhost:8000/api/admin/reload-subjects", timeout=2)
    except Exception:
        pass
        
    try:
        requests.post("https://mobme.educamob.com.br/api/admin/reload-subjects", timeout=2)
    except Exception:
        pass
        
    print(f"Matérias ativas injetadas no prompt: {', '.join([s.capitalize() for s in subjects_found])}")
except Exception as e:
    print(f"Aviso: Erro ao atualizar as matérias dinâmicas: {e}")
