from supabase.client import AsyncClient
import uuid
import re
from tenacity import retry, stop_after_attempt, wait_exponential

# Configuração global de Retry para chamadas de banco de dados
# Tenta 5 vezes, esperando 1s, 2s, 4s, 8s em caso de sobrecarga (Server disconnected / PoolTimeout)
db_retry = retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    reraise=True
)


async def get_or_create_user(supabase: AsyncClient, user_id: str, name: str = "Aluno Teste"):
    response = await supabase.table("users").select("*").eq("id", user_id).execute()
    
    # Se achou o usuário e o nome NÃO for "Aluno Teste", já podemos retornar rápido
    if response.data and response.data[0].get("name") and response.data[0].get("name") != "Aluno Teste":
        return response.data[0]
        
    real_name = name
    # Vamos tentar buscar o nome real no auth.users
    try:
        auth_resp = await supabase.auth.admin.get_user_by_id(user_id)
        if auth_resp and auth_resp.user:
            meta = auth_resp.user.user_metadata or {}
            real_name = meta.get("full_name") or meta.get("name") or real_name
            # Se ainda for "Aluno Teste", tenta extrair do email
            if real_name == "Aluno Teste" and auth_resp.user.email:
                real_name = auth_resp.user.email.split("@")[0].capitalize()
    except Exception as e:
        print(f"Erro ao buscar nome real do user_id {user_id}: {e}")
        
    if real_name == "Aluno Teste":
        real_name = "Estudante"

    if not response.data:
        # Create user
        await supabase.table("users").insert({
            "id": user_id,
            "name": real_name,
            "long_term_memory": "Nenhuma preferência registrada ainda."
        }).execute()
        return {"id": user_id, "name": real_name, "long_term_memory": "Nenhuma preferência registrada ainda."}
    
    user_data = response.data[0]
    # Atualiza retroativamente quem estava como "Aluno Teste"
    if user_data.get("name") == "Aluno Teste":
        await supabase.table("users").update({"name": real_name}).eq("id", user_id).execute()
        user_data["name"] = real_name
    return user_data


async def get_or_create_session(supabase: AsyncClient, user_id: str, session_id: str | None = None):
    if session_id:
        response = await supabase.table("chat_sessions").select("*").eq("id", session_id).execute()
        if response.data:
            return response.data[0]["id"]
    
    # Create new session
    new_session_id = str(uuid.uuid4())
    await supabase.table("chat_sessions").insert({
        "id": new_session_id,
        "user_id": user_id,
        "title": "Nova Conversa"
    }).execute()
    return new_session_id


async def save_message(supabase: AsyncClient, session_id: str, role: str, content: str, image_base64: str | None = None):
    if image_base64:
        content = f"<img_b64>{image_base64}</img_b64>{content}"
        
    await supabase.table("messages").insert({
        "session_id": session_id,
        "role": role,
        "content": content
    }).execute()


async def get_session_history(supabase: AsyncClient, session_id: str):
    response = await supabase.table("messages").select("*").eq("session_id", session_id).order("created_at").execute()
    for msg in response.data:
        if "<img_b64>" in msg["content"]:
            img_match = re.search(r"<img_b64>(.*?)</img_b64>", msg["content"])
            if img_match:
                msg["image_base64"] = img_match.group(1)
                msg["content"] = msg["content"].replace(img_match.group(0), "")
    return response.data


async def get_user_sessions(supabase: AsyncClient, user_id: str, limit: int = 20):
    response = await supabase.table("chat_sessions").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(limit).execute()
    return response.data


async def update_session_title(supabase: AsyncClient, session_id: str, new_title: str):
    await supabase.table("chat_sessions").update({"title": new_title}).eq("id", session_id).execute()
