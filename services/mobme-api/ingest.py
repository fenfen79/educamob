import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client

load_dotenv()

# Verificações de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not all([GEMINI_API_KEY, SUPABASE_URL, SUPABASE_KEY]):
    print("❌ ERRO: Faltam variáveis de ambiente no .env (GEMINI_API_KEY, SUPABASE_URL, SUPABASE_KEY).")
    exit(1)

# 1. Carregar documentos Markdown
print("Carregando arquivos Markdown...")
loader = DirectoryLoader("data", glob="**/*.md", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
docs = loader.load()

if not docs:
    print("ERRO: Nenhum arquivo Markdown encontrado na pasta 'data'.")
    exit(1)

print(f"SUCESSO: {len(docs)} arquivos carregados.")

# 2. Fatiar (Split) os documentos usando MarkdownTextSplitter
print("Fatiando documentos preservando a estrutura...")
markdown_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = markdown_splitter.split_documents(docs)
print(f"Documentos divididos em {len(splits)} pedacos (chunks).")

# 3. Gerar Embeddings via Google Gemini
print("Inicializando Embeddings do Gemini...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")

# 4. Inserir no Supabase (pgvector) em Lotes (Batches) para evitar erro 429 do Gemini (Free Tier)
print("Conectando ao Supabase e inserindo vetores (com pausas para a API Gratuita)...")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

batch_size = 5
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

    time.sleep(2) # Pausa amigável entre os lotes

print("SUCESSO FINAL! Todos os documentos foram vetorizados e salvos no Supabase.")
