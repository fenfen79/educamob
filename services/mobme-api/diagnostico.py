"""
Diagnóstico passo-a-passo do Mob.me Backend
Testa cada componente isoladamente para encontrar o gargalo.
"""
import os
import time
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("DIAGNÓSTICO MOB.ME - ETAPA POR ETAPA")
print("=" * 60)

# ---- ETAPA 1: Testar a chave do Gemini ----
print("\n[1/4] Testando conexão com o Gemini...")
t = time.time()
try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))
    model = genai.GenerativeModel("gemini-flash-latest")
    response = model.generate_content("Diga apenas: OK")
    print(f"  ✅ Gemini respondeu em {time.time()-t:.2f}s: {response.text.strip()[:50]}")
except Exception as e:
    print(f"  ❌ ERRO Gemini: {e}")

# ---- ETAPA 2: Testar Gemini com Streaming ----
print("\n[2/4] Testando Gemini com STREAMING...")
t = time.time()
try:
    model = genai.GenerativeModel("gemini-flash-latest")
    response = model.generate_content("Diga apenas: OK Streaming", stream=True)
    chunks = []
    for chunk in response:
        if chunk.text:
            chunks.append(chunk.text)
    full = "".join(chunks)
    print(f"  ✅ Streaming OK em {time.time()-t:.2f}s ({len(chunks)} chunks): {full.strip()[:50]}")
except Exception as e:
    print(f"  ❌ ERRO Streaming Gemini: {e}")

# ---- ETAPA 3: Testar Supabase ----
print("\n[3/4] Testando conexão com o Supabase...")
t = time.time()
try:
    from supabase.client import create_client
    SUPABASE_URL = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    result = supabase.table("users").select("id").limit(1).execute()
    print(f"  ✅ Supabase respondeu em {time.time()-t:.2f}s: {len(result.data)} registro(s)")
except Exception as e:
    print(f"  ❌ ERRO Supabase: {e}")

# ---- ETAPA 4: Testar Embeddings (RAG) ----
print("\n[4/4] Testando Embeddings (RAG Vector Search)...")
t = time.time()
try:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    from langchain_community.vectorstores.supabase import SupabaseVectorStore
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
    vector_store = SupabaseVectorStore(
        client=supabase,
        embedding=embeddings,
        table_name="documents",
        query_name="match_documents"
    )
    docs = vector_store.similarity_search("teste", k=1)
    print(f"  ✅ RAG respondeu em {time.time()-t:.2f}s: {len(docs)} documento(s)")
except Exception as e:
    print(f"  ❌ ERRO RAG: {e}")

print("\n" + "=" * 60)
print("DIAGNÓSTICO CONCLUÍDO")
print("=" * 60)
