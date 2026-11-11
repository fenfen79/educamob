import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Carrega variáveis de ambiente
if os.path.exists(".env.lab"):
    load_dotenv(".env.lab", override=True)
else:
    load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DEEPINFRA_API_TOKEN = os.getenv("DEEPINFRA_API_TOKEN")

if not all([SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN]):
    print("❌ ERRO: Faltam variáveis de ambiente (SUPABASE_URL, SUPABASE_KEY, DEEPINFRA_API_TOKEN).")
    sys.exit(1)

def run_ingest_fisica():
    print("=" * 60)
    print("🚀 INGESTÃO DEDICADA DE FÍSICA NO SUPABASE (MOB.ME)")
    print("=" * 60)

    base_dir = Path("../../content/medio")
    if not base_dir.exists():
        print(f"❌ Diretório não encontrado: {base_dir}")
        sys.exit(1)

    # 1. Localizar e-books de Física
    fisica_files = []
    for fp in base_dir.rglob("*.md"):
        if "ebooks" in fp.parts and "fisica" in str(fp).lower() and not fp.name.endswith("-exercicios.md") and not fp.name.startswith("_"):
            fisica_files.append(fp)

    fisica_files.sort()
    print(f"📚 Total de e-books de Física encontrados: {len(fisica_files)}")
    if len(fisica_files) != 130:
        print(f"⚠️ Atenção: Esperado 130 e-books, encontrados {len(fisica_files)}.")

    # 2. Carregar documentos
    print("\nCarregando documentos...")
    docs = []
    for fp in fisica_files:
        try:
            loader = TextLoader(str(fp), encoding='utf-8')
            docs.extend(loader.load())
        except Exception as e:
            print(f"Erro ao carregar {fp}: {e}")

    print(f"✅ {len(docs)} documentos carregados com sucesso.")

    # 3. Fatiamento semântico
    print("\nFatiando documentos com MarkdownTextSplitter...")
    markdown_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = markdown_splitter.split_documents(docs)
    splits = [s for s in splits if s.page_content.strip()]
    total_chunks = len(splits)
    print(f"✅ Documentos divididos em {total_chunks} fragmentos (chunks).")

    # 4. Inicializar Embeddings e Supabase
    print("\nConectando aos serviços...")
    embeddings = OpenAIEmbeddings(
        model="BAAI/bge-m3",
        openai_api_base="https://api.deepinfra.com/v1/openai",
        openai_api_key=DEEPINFRA_API_TOKEN,
        check_embedding_ctx_length=False
    )
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # 5. Inserção em Lotes
    batch_size = 50
    total_batches = (total_chunks + batch_size - 1) // batch_size
    print(f"\nIniciando inserção em {total_batches} lotes (lotes de {batch_size} chunks)...")

    inicio = time.time()
    for i in range(0, total_chunks, batch_size):
        batch = splits[i:i + batch_size]
        lote_num = (i // batch_size) + 1
        
        tentativas = 3
        while tentativas > 0:
            try:
                SupabaseVectorStore.from_documents(
                    batch,
                    embeddings,
                    client=supabase,
                    table_name="documents",
                    query_name="match_documents"
                )
                tempo_decorrido = time.time() - inicio
                pct = (lote_num / total_batches) * 100
                print(f"[{pct:5.1f}%] Lote {lote_num:03d}/{total_batches:03d} inserido com sucesso ({len(batch)} chunks) | Tempo: {tempo_decorrido:.1f}s")
                break
            except Exception as e:
                tentativas -= 1
                print(f"⚠️ Erro no Lote {lote_num}: {e}. Tentando novamente em 5s (tentativas restantes: {tentativas})...")
                time.sleep(5)
                if tentativas == 0:
                    print(f"❌ Falha crítica no lote {lote_num}. Abortando.")
                    sys.exit(1)

    tempo_total = time.time() - inicio
    print("\n" + "=" * 60)
    print(f"🎉 INGESTÃO CONCLUÍDA COM SUCESSO!")
    print(f"Total de fragmentos vetorizados: {total_chunks}")
    print(f"Tempo total: {tempo_total:.1f} segundos ({tempo_total/60:.1f} minutos)")
    print("=" * 60)

if __name__ == "__main__":
    run_ingest_fisica()
