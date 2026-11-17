import os
import sys
import time
import json
import hashlib
import re
import argparse
import warnings
from pathlib import Path
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
    except Exception:
        pass
else:
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass

# 1. Carregar variáveis de ambiente
script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"
lab_path = script_dir / ".env.lab"

if env_path.exists():
    load_dotenv(env_path)
else:
    load_dotenv()

if lab_path.exists():
    load_dotenv(lab_path, override=True)

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
from langchain_text_splitters import RecursiveCharacterTextSplitter

sub_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=300,
    separators=["\n\n", "\n", " "]
)

def get_all_exercise_files(base_dir: Path, discipline_filter: str = None):
    """Localiza todos os arquivos de exercícios (*-exercicios.md) em content/."""
    directories = [
        base_dir / "fundamental-1",
        base_dir / "fundamental-2",
        base_dir / "medio"
    ]
    files = []
    for d in directories:
        if d.exists():
            for f in d.rglob("*.md"):
                if f.name.endswith("-exercicios.md") and not f.name.startswith("_"):
                    if discipline_filter:
                        parts = [p.lower() for p in f.parts]
                        if discipline_filter.lower() not in parts:
                            continue
                    files.append(f)
    files.sort()
    return files

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
    parser = argparse.ArgumentParser(description="Ingestão unificada de listas de exercícios no Supabase pgvector.")
    parser.add_argument("--discipline", type=str, default=None, help="Filtrar por disciplina (ciencias, historia, geografia, matematica, fisica, quimica, lingua-portuguesa)")
    parser.add_argument("--force", action="store_true", help="Forçar re-ingestão de arquivos mesmo que hash seja idêntico")
    parser.add_argument("--batch-size", type=int, default=20, help="Tamanho do lote para inserção (padrão: 20)")
    parser.add_argument("--limit", type=int, default=None, help="Número máximo de arquivos a processar")
    args = parser.parse_args()

    print("=" * 80)
    print("🚀 INGESTÃO UNIFICADA DE LISTAS DE EXERCÍCIOS NO SUPABASE PGVECTOR (MOB.ME)")
    print("=" * 80)
    
    # Base dir aponta para o repositório principal
    repo_root = script_dir.parent.parent
    base_dir = repo_root / "content"
    if not base_dir.exists():
        base_dir = Path("content").resolve()
        repo_root = base_dir.parent
        
    exercise_files = get_all_exercise_files(base_dir, args.discipline)
    print(f"📚 Total de arquivos de exercícios localizados: {len(exercise_files)}")
    
    # Contagem por disciplina
    disciplines = {}
    for f in exercise_files:
        norm_path = str(f).replace("\\", "/").lower()
        for disc in ["matematica", "ciencias", "fisica", "quimica", "historia", "geografia", "lingua-portuguesa", "biologia"]:
            if f"/{disc}/" in norm_path or f"/{disc}-" in norm_path:
                disciplines[disc] = disciplines.get(disc, 0) + 1
                break
    for d, c in sorted(disciplines.items()):
        print(f"   - {d.capitalize()}: {c} listas")
        
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
        rel_path = "../../" + str(f.resolve().relative_to(repo_root.resolve())).replace("\\", "/")
        file_hashes[rel_path] = (f, f_hash)
        
        if args.force or state.get(rel_path) != f_hash:
            to_process.append(rel_path)
            
    print(f"\n📋 Arquivos pendentes para ingestão/atualização: {len(to_process)} de {len(exercise_files)}")
    print(f"   - Já sincronizados: {len(exercise_files) - len(to_process)}")
    print(f"   - A processar: {len(to_process)}")
    
    if args.limit and args.limit < len(to_process):
        to_process = to_process[:args.limit]
        print(f"   - Limitado para teste: {len(to_process)} arquivos")
    
    if not to_process:
        print("\n✅ Todas as listas já estão 100% sincronizadas e indexadas no Supabase! Nenhuma ação pendente.")
        return

    inicio_global = time.time()
    total_docs_inseridos = 0
    batch_size = args.batch_size

    for file_idx, rel_path in enumerate(to_process, start=1):
        file_path, f_hash = file_hashes[rel_path]
        f_name = file_path.name
        parent_tag = f"{file_path.parent.parent.parent.name}/{file_path.parent.parent.name}"
        
        print(f"\n[{file_idx:03d}/{len(to_process):03d}] {f_name} ({parent_tag})...")
        
        # 1. Extrair chunks
        try:
            docs = extract_chunks_from_file(file_path, rel_path)
        except Exception as e:
            print(f"   ❌ Erro ao extrair chunks de {file_path}: {e}")
            continue
            
        print(f"   -> {len(docs)} chunks atômicos extraídos.")
        
        # 2. Limpar versões antigas deste arquivo no banco
        try:
            supabase.table("documents").delete().eq("metadata->>source", rel_path).execute()
            supabase.table("documents").delete().eq("metadata->>source", rel_path.replace("/", "\\")).execute()
        except Exception as e:
            print(f"   ⚠️ Aviso na exclusão prévia: {e}")
            
        # 3. Gerar embeddings em lote único e inserir em micro-lotes no banco
        total_chunks = len(docs)
        file_chunks_inserted = 0
        
        # 3.1 Geração de embeddings (1 única chamada para DeepInfra para todos os chunks do arquivo)
        tentativas_emb = 5
        embeddings_vectors = None
        while tentativas_emb > 0:
            try:
                embeddings_vectors = embeddings.embed_documents([d.page_content for d in docs])
                break
            except Exception as ee:
                tentativas_emb -= 1
                if tentativas_emb == 0:
                    print(f"❌ Erro fatal ao gerar embeddings para {rel_path}: {ee}")
                    sys.exit(1)
                print(f"   ⚠️ Erro na API de embeddings ({str(ee)[:80]}). Retentando em 4s... ({tentativas_emb} restantes)")
                time.sleep(4)
                
        # 3.2 Montagem dos registros
        rows = [
            {
                "content": d.page_content,
                "metadata": d.metadata,
                "embedding": emb
            }
            for d, emb in zip(docs, embeddings_vectors)
        ]
        
        # 3.3 Inserção direta em micro-lotes de 5 para evitar timeout do índice HNSW
        micro_batch_size = 5
        for j in range(0, len(rows), micro_batch_size):
            sub_rows = rows[j:j + micro_batch_size]
            tentativas_insert = 5
            while tentativas_insert > 0:
                try:
                    supabase.table("documents").insert(sub_rows).execute()
                    file_chunks_inserted += len(sub_rows)
                    break
                except Exception as ie:
                    err_s = str(ie)
                    tentativas_insert -= 1
                    if "57014" in err_s or "timeout" in err_s.lower():
                        # Se até lote de 5 der timeout, tenta inserir 1 por 1
                        print(f"   ⚠️ Timeout HNSW em micro-lote de 5. Inserindo unitariamente...")
                        for single_row in sub_rows:
                            supabase.table("documents").insert([single_row]).execute()
                            file_chunks_inserted += 1
                        break
                    elif tentativas_insert > 0:
                        print(f"   ⚠️ Erro ao inserir ({err_s[:80]}). Retentando em 4s... ({tentativas_insert} restantes)")
                        time.sleep(4)
                    else:
                        print(f"❌ Erro fatal ao inserir registros de {rel_path}: {ie}. Abortando.")
                        sys.exit(1)
                        
        total_docs_inseridos += file_chunks_inserted
        # Salva o estado incrementalmente no arquivo JSON
        state[rel_path] = f_hash
        try:
            with open(state_file, "w", encoding="utf-8") as sf:
                json.dump(state, sf, indent=2)
        except Exception as se:
            print(f"   ⚠️ Erro ao persistir estado em disco: {se}")
            
        tempo_decorrido = time.time() - inicio_global
        media_por_arquivo = tempo_decorrido / file_idx
        tempo_estimado_restante = media_por_arquivo * (len(to_process) - file_idx)
        print(f"   ✅ Indexado! Chunks acumulados: {total_docs_inseridos} | Tempo: {tempo_decorrido/60:.1f}m | ETA restante: {tempo_estimado_restante/60:.1f}m")

    tempo_total = time.time() - inicio_global
    print("\n" + "=" * 80)
    print("🏆 INGESTÃO UNIFICADA CONCLUÍDA COM SUCESSO ABSOLUTO!")
    print(f"Total de arquivos indexados: {len(to_process)}")
    print(f"Total de fragmentos (chunks) inseridos: {total_docs_inseridos}")
    print(f"Tempo total de execução: {tempo_total/60:.2f} minutos")
    print("=" * 80)

if __name__ == "__main__":
    main()
