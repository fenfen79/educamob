import os
import sys
from dotenv import load_dotenv
from supabase.client import create_client

load_dotenv()
client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

try:
    while True:
        res = client.table("documents").select("id").limit(100).execute()
        data = res.data
        if not data:
            print("Tabela vazia!")
            break
        ids = [row["id"] for row in data]
        client.table("documents").delete().in_("id", ids).execute()
        print(f"Deletados {len(ids)} documentos...")
except Exception as e:
    print("Erro durante delecao:", e)
