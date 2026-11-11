import asyncio
import os
from dotenv import load_dotenv
from supabase.client import create_async_client
import uuid

load_dotenv("C:/Users/nepov/Documents/Pessoal/Antigravity/🚀 Educamob - DevOps e Infra/services/mobme-api/.env")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

from memory import save_message, get_session_history

async def test_image_history():
    client = await create_async_client(SUPABASE_URL, SUPABASE_KEY)
    
    session_id = str(uuid.uuid4())
    
    print("Salvando mensagem com imagem...")
    await save_message(client, session_id, "user", "resolva essa questao", "TEST_BASE_64_STRING")
    
    print("Recuperando histórico...")
    history = await get_session_history(client, session_id)
    
    for msg in history:
        print(f"Role: {msg['role']}")
        print(f"Content: {msg['content']}")
        print(f"Image Base64: {msg.get('image_base64')}")
        
    print("Limpando DB...")
    await client.table("messages").delete().eq("session_id", session_id).execute()

asyncio.run(test_image_history())
