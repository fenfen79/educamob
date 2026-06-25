import os
from dotenv import load_dotenv
from supabase.client import Client, create_client
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores.supabase import SupabaseVectorStore

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")

vector_store = SupabaseVectorStore(
    client=supabase,
    embedding=embeddings,
    table_name="documents",
    query_name="match_documents"
)

docs = vector_store.similarity_search("o que é um monômio?", k=4)

print(f"Encontrou {len(docs)} documentos.")
for i, d in enumerate(docs):
    print(f"\n--- Documento {i+1} ({d.metadata}) ---")
    print(d.page_content[:200] + "...")
