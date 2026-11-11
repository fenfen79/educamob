import os
import sys
import time
import json
import hashlib
import re
from pathlib import Path
from dotenv import load_dotenv

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 1. Carregar variáveis de ambiente
script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"
if (script_dir / ".env.lab").exists():
    load_dotenv(script_dir / ".env.lab", override=True)
elif env_path.exists():
    load_dotenv(env_path)
else:
    load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DEEPINFRA_API_TOKEN = os.getenv("DEEPINFRA_API_TOKEN")

if not all([SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN]):
    print("❌ ERRO: Faltam variáveis de ambiente (SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN).")
    sys.exit(1)

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client

def get_math_exercise_files(base_dir: Path):
    """Localiza todos os 148 arquivos de exercícios de matemática."""
    directories = [
        base_dir / "fundamental-1" / "5-ano" / "matematica",
        base_dir / "fundamental-2" / "6-ano" / "matematica",
        base_dir / "fundamental-2" / "7-ano" / "matematica",
        base_dir / "fundamental-2" / "8-ano" / "matematica",
        base_dir / "fundamental-2" / "9-ano" / "matematica",
        base_dir / "medio" / "volume-unico" / "matematica"
    ]
    files = []
    for d in directories:
        if d.exists():
            for f in d.rglob("*.md"):
                if f.name.endswith("-exercicios.md") and not f.name.startswith("_"):
                    files.append(f)
    files.sort()
    return files

from langchain_text_splitters import RecursiveCharacterTextSplitter

sub_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=300,
    separators=["\n\n", "\n", " "]
)

def extract_chunks_from_file(file_path: Path, str_source: str):
    """Extrai chunks atômicos de cada questão preservando tags HTML e resoluções."""
    content = file_path.read_text(encoding="utf-8")
    parts = re.split(r'(?=\n<!--\s*id:\s*q\d+)', content)
    header = parts[0].strip()
    questions = parts[1:]
    
    docs = []
    # Chunk 0: cabeçalho com frontmatter e escopo
    if header:
        if len(header) > 3500:
            for sub_p in sub_splitter.split_text(header):
                docs.append(Document(
                    page_content=sub_p,
                    metadata={"source": str_source, "chunk_type": "header"}
                ))
        else:
            docs.append(Document(
                page_content=header,
                metadata={"source": str_source, "chunk_type": "header"}
            ))
        
    for idx, q_text in enumerate(questions):
        q_clean = q_text.strip()
        if q_clean:
            match_id = re.search(r'id:\s*(q\d+)', q_clean)
            q_id = match_id.group(1) if match_id else f"q{idx+1:02d}"
            
            # Se o chunk ultrapassar 3500 caracteres, divide em subchunks seguros
            if len(q_clean) > 3500:
                for sub_idx, sub_p in enumerate(sub_splitter.split_text(q_clean)):
                    docs.append(Document(
                        page_content=sub_p,
                        metadata={
                            "source": str_source,
                            "chunk_type": "exercicio",
                            "q_id": q_id,
                            "q_num": idx + 1,
                            "part": sub_idx + 1
                        }
                    ))
            else:
                docs.append(Document(
                    page_content=q_clean,
                    metadata={"source": str_source, "chunk_type": "exercicio", "q_id": q_id, "q_num": idx + 1}
                ))
            
    return docs

def main():
    print("=" * 70)
    print("🚀 INGESTÃO CANÔNICA DE LISTAS DE MATEMÁTICA NO SUPABASE (MOB.ME)")
    print("=" * 70)
    
    # Base dir aponta para a pasta content
    base_dir = script_dir.parent.parent / "content"
    if not base_dir.exists():
        base_dir = Path("content").resolve()
        
    exercise_files = get_math_exercise_files(base_dir)
    print(f"📚 Total de arquivos de exercícios de Matemática encontrados: {len(exercise_files)}")
    if len(exercise_files) != 148:
        print(f"⚠️ Aviso: Esperado 148 arquivos, encontrados {len(exercise_files)}.")
        
    # Inicializa clientes
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    embeddings = OpenAIEmbeddings(
        model="BAAI/bge-m3",
        openai_api_base="https://api.deepinfra.com/v1/openai",
        openai_api_key=DEEPINFRA_API_TOKEN,
        check_embedding_ctx_length=False
    )
    
    state_file = script_dir / "ingest_state_exercicios.json"
    if state_file.exists():
        try:
            with open(state_file, "r", encoding="utf-8") as sf:
                state = json.load(sf)
        except Exception:
            state = {}
    else:
        state = {}
        
    # Identificar quais arquivos precisam ser processados
    to_process = []
    file_hashes = {}
    
    for f in exercise_files:
        content_bytes = f.read_bytes()
        f_hash = hashlib.md5(content_bytes).hexdigest()
        # Normaliza caminho relativo consistente com ingest.py
        rel_path = "../../" + str(f.relative_to(script_dir.parent.parent)).replace("\\", "/")
        file_hashes[rel_path] = (f, f_hash)
        
        if state.get(rel_path) != f_hash:
            to_process.append(rel_path)
            
    print(f"📋 Arquivos pendentes para ingestão/atualização: {len(to_process)} de {len(exercise_files)}")
    if not to_process:
        print("✅ Todas as 148 listas já estão devidamente sincronizadas e indexadas no Supabase! Nenhuma ação pendente.")
        return

    inicio_global = time.time()
    total_docs_inseridos = 0
    batch_size = 50

    for file_idx, rel_path in enumerate(to_process, start=1):
        file_path, f_hash = file_hashes[rel_path]
        print(f"\n[{file_idx:03d}/{len(to_process):03d}] Processando: {file_path.name}...")
        
        # 1. Extrair chunks
        docs = extract_chunks_from_file(file_path, rel_path)
        print(f"   -> {len(docs)} chunks atômicos extraídos.")
        
        # 2. Limpar versões antigas deste arquivo no banco
        try:
            supabase.table("documents").delete().eq("metadata->>source", rel_path).execute()
            supabase.table("documents").delete().eq("metadata->>source", rel_path.replace("/", "\\")).execute()
        except Exception as e:
            print(f"   ⚠️ Aviso na exclusão prévia: {e}")
            
        # 3. Inserir em lotes
        total_chunks = len(docs)
        for i in range(0, total_chunks, batch_size):
            batch = docs[i:i + batch_size]
            tentativas = 5
            while tentativas > 0:
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
                    tentativas -= 1
                    print(f"   ⚠️ Erro ao inserir lote de chunks ({e}). Aguardando 6s... (Restam {tentativas} tentativas)")
                    time.sleep(6)
                    if tentativas == 0:
                        print(f"❌ Erro fatal ao inserir {rel_path}. Abortando.")
                        sys.exit(1)
                        
        total_docs_inseridos += len(docs)
        # Salva o estado incrementalmente
        state[rel_path] = f_hash
        with open(state_file, "w", encoding="utf-8") as sf:
            json.dump(state, sf, indent=2)
            
        tempo_decorrido = time.time() - inicio_global
        media_por_arquivo = tempo_decorrido / file_idx
        tempo_estimado_restante = media_por_arquivo * (len(to_process) - file_idx)
        print(f"   ✅ Arquivo indexado com sucesso! Chunks acumulados: {total_docs_inseridos} | Tempo decorrido: {tempo_decorrido/60:.1f}m | ETA restante: {tempo_estimado_restante/60:.1f}m")

    tempo_total = time.time() - inicio_global
    print("\n" + "=" * 70)
    print("🏆 INGESTÃO DE MATEMÁTICA CONCLUÍDA COM SUCESSO!")
    print(f"Total de arquivos indexados: {len(to_process)}")
    print(f"Total de fragmentos (chunks) inseridos: {total_docs_inseridos}")
    print(f"Tempo total de execução: {tempo_total/60:.2f} minutos")
    print("=" * 70)

if __name__ == "__main__":
    main()
