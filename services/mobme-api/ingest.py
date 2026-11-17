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

load_dotenv()
if os.path.exists(".env.lab"):
    load_dotenv(".env.lab", override=True)
elif os.path.exists("services/mobme-api/.env.lab"):
    load_dotenv("services/mobme-api/.env.lab", override=True)

# Verificações de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DEEPINFRA_API_TOKEN = os.getenv("DEEPINFRA_API_TOKEN")

if not all([GEMINI_API_KEY, SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN]):
    print("ERRO: Faltam variáveis de ambiente no .env (GEMINI_API_KEY, SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN).")
    exit(1)

# 1. Carregar documentos Markdown
from pathlib import Path

print("Buscando arquivos Markdown de Teoria...")
base_dir = Path("../../content")
directories_to_scan = [
    base_dir / "fundamental-1",
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
    print("ERRO: Nenhum e-book atômico encontrado em content (fundamental-1, fundamental-2, medio ou superior).")
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

# -------------------------------------------------------------
# Atualizar imediatamente a tabela de matérias disponíveis e notificar a API
# -------------------------------------------------------------
print("\nAtualizando a lista de matérias dinâmicas no banco...")
try:
    KNOWN_SUBJECTS = {"matematica", "ciencias", "fisica", "quimica", "biologia", "historia", "geografia", "filosofia", "sociologia", "literatura", "ingles", "espanhol", "artes", "calculo-1", "lingua-portuguesa"}
    subjects_found = set()
    for fp in valid_files:
        for part in fp.parts:
            if part.lower() in KNOWN_SUBJECTS:
                subjects_found.add(part.lower())
    
    for subject in sorted(subjects_found):
        supabase.table("available_subjects").upsert({"subject_name": subject}).execute()
    
    import requests
    for url in ["http://localhost:8000/api/admin/reload-subjects", "https://api.educamob.com.br/api/admin/reload-subjects", "https://mobme.educamob.com.br/api/admin/reload-subjects"]:
        try:
            requests.post(url, timeout=2)
        except Exception:
            pass
        
    print(f"Matérias ativas injetadas no prompt: {', '.join([s.capitalize() for s in sorted(subjects_found)])}")
except Exception as e:
    print(f"Aviso: Erro ao atualizar as matérias dinâmicas: {e}")

file_hashes = {}
files_to_ingest = []

for file_path in valid_files:
    try:
        content_bytes = open(file_path, 'rb').read()
        file_hash = hashlib.md5(content_bytes).hexdigest()
        str_path = str(file_path).replace("\\", "/") # Normaliza barras para evitar bugs no windows/linux
        file_hashes[str_path] = file_hash
        
        # Se a hash for igual, o arquivo não mudou. PULA.
        if ingest_state.get(str_path) == file_hash:
            continue
            
        # Adiciona na lista de arquivos que precisam ser vetorizados
        files_to_ingest.append(str_path)
        
    except Exception as e:
        print(f"Erro ao verificar {file_path}: {e}")

if not files_to_ingest:
    print("Nenhum arquivo novo ou modificado. Ingestão pulada. Zero tokens gastos e nenhuma duplicata!")
else:
    print(f"{len(files_to_ingest)} arquivos novos ou modificados encontrados. Iniciando carregamento e vetorização incremental...")
    markdown_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
    embeddings = OpenAIEmbeddings(
        model="BAAI/bge-m3",
        openai_api_base="https://api.deepinfra.com/v1/openai",
        openai_api_key=DEEPINFRA_API_TOKEN,
        check_embedding_ctx_length=False
    )
    
    batch_size = 20
    total_chunks_inserted = 0
    for idx_f, str_path in enumerate(files_to_ingest, 1):
        # Só executa delete se o arquivo já constava no estado anterior (modificado)
        if str_path in ingest_state:
            try:
                supabase.table("documents").delete().eq("metadata->>source", str_path).execute()
            except Exception:
                pass
        
        try:
            loader = TextLoader(str_path, encoding='utf-8')
            file_docs = loader.load()
            splits = [s for s in markdown_splitter.split_documents(file_docs) if s.page_content.strip()]
        except Exception as e:
            print(f"Erro ao carregar/fatiar {str_path}: {e}")
            continue
            
        print(f"[{idx_f:03d}/{len(files_to_ingest):03d}] {str_path.split('/')[-1]} ({len(splits)} chunks)...")
        # Geração de embeddings em lote único por arquivo (evita múltiplas chamadas HTTP)
        tentativas_emb = 5
        embeddings_vectors = None
        while tentativas_emb > 0:
            try:
                embeddings_vectors = embeddings.embed_documents([s.page_content for s in splits])
                break
            except Exception as ee:
                tentativas_emb -= 1
                if tentativas_emb == 0:
                    print(f"  ❌ Erro fatal ao gerar embeddings para {str_path}: {ee}")
                    raise ee
                print(f"  ⚠️ Erro na API de embeddings ({str(ee)[:80]}). Retentando em 4s... ({tentativas_emb} restantes)")
                time.sleep(4)

        rows = [
            {
                "content": s.page_content,
                "metadata": s.metadata,
                "embedding": emb
            }
            for s, emb in zip(splits, embeddings_vectors)
        ]

        # Inserção direta em micro-lotes de 5 para evitar timeout do índice HNSW
        micro_batch_size = 5
        for j in range(0, len(rows), micro_batch_size):
            sub_rows = rows[j:j + micro_batch_size]
            tentativas_insert = 5
            while tentativas_insert > 0:
                try:
                    supabase.table("documents").insert(sub_rows).execute()
                    break
                except Exception as ie:
                    err_s = str(ie)
                    tentativas_insert -= 1
                    if "57014" in err_s or "timeout" in err_s.lower():
                        print(f"  ⚠️ Timeout HNSW em micro-lote de 5. Inserindo unitariamente...")
                        for single_row in sub_rows:
                            supabase.table("documents").insert([single_row]).execute()
                        break
                    elif tentativas_insert > 0:
                        print(f"  ⚠️ Erro ao inserir ({err_s[:80]}). Retentando em 4s... ({tentativas_insert} restantes)")
                        time.sleep(4)
                    else:
                        print(f"❌ Erro fatal ao inserir registros de {str_path}: {ie}. Abortando.")
                        raise ie
        
        total_chunks_inserted += len(splits)
        ingest_state[str_path] = file_hashes[str_path]
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(ingest_state, f, indent=2)
            
    print(f"SUCESSO FINAL! {len(files_to_ingest)} e-books ({total_chunks_inserted} chunks) foram vetorizados e salvos.")
