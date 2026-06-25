from supabase.client import Client
import uuid

def get_or_create_user(supabase: Client, user_id: str, name: str = "Aluno Teste"):
    response = supabase.table("users").select("*").eq("id", user_id).execute()
    if not response.data:
        # Create user
        supabase.table("users").insert({
            "id": user_id,
            "name": name,
            "long_term_memory": "Nenhuma preferência registrada ainda."
        }).execute()
        return {"id": user_id, "name": name, "long_term_memory": "Nenhuma preferência registrada ainda."}
    return response.data[0]

def get_or_create_session(supabase: Client, user_id: str, session_id: str | None = None):
    if session_id:
        response = supabase.table("chat_sessions").select("*").eq("id", session_id).execute()
        if response.data:
            return response.data[0]["id"]
    
    # Create new session
    new_session_id = str(uuid.uuid4())
    supabase.table("chat_sessions").insert({
        "id": new_session_id,
        "user_id": user_id,
        "title": "Nova Conversa"
    }).execute()
    return new_session_id

def save_message(supabase: Client, session_id: str, role: str, content: str):
    supabase.table("messages").insert({
        "session_id": session_id,
        "role": role,
        "content": content
    }).execute()

def get_session_history(supabase: Client, session_id: str):
    response = supabase.table("messages").select("*").eq("session_id", session_id).order("created_at").execute()
    return response.data

def get_user_sessions(supabase: Client, user_id: str, limit: int = 20):
    response = supabase.table("chat_sessions").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(limit).execute()
    return response.data

def update_session_title(supabase: Client, session_id: str, new_title: str):
    supabase.table("chat_sessions").update({"title": new_title}).eq("id", session_id).execute()
