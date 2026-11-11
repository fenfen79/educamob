import os
from dotenv import load_dotenv
from supabase.client import create_client

if os.path.exists(".env.lab"):
    load_dotenv(".env.lab", override=True)
else:
    load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

client = create_client(SUPABASE_URL, SUPABASE_KEY)
print("Deletando documentos...")
try:
    res = client.table("documents").delete().neq("content", "FAKE_DONT_EXIST_123").execute()
    print("Sucesso! Deletados:", len(res.data) if res.data else 0)
except Exception as e:
    print("Erro:", e)
