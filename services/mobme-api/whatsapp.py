import os
import requests
import google.generativeai as genai
from supabase.client import Client

# Evolution API Settings
EVO_API_URL = os.getenv("EVOLUTION_API_URL", "http://localhost:8080")
EVO_API_KEY = os.getenv("EVOLUTION_API_KEY", "SUA_API_KEY_AQUI")
EVO_INSTANCE_NAME = os.getenv("EVOLUTION_INSTANCE_NAME", "EducamobBot")

def format_phone_number(remote_jid: str) -> str:
    """Extrai apenas os números do JID do WhatsApp (ex: 5511999999999@s.whatsapp.net -> +5511999999999)"""
    number = remote_jid.split("@")[0]
    return f"+{number}"

def fetch_student_data(supabase: Client, phone: str):
    """Busca o aluno no Supabase atrelado a este telefone."""
    # Como o Supabase não aceita wildcard fácil se não criarmos uma RPC, usamos match exato.
    # Pode ser necessário adaptar a formatação do número conforme salvo no BD.
    response = supabase.table("users").select("*").eq("guardian_phone", phone).execute()
    users = response.data
    
    if not users:
        # Tenta sem o '+' caso esteja salvo apenas como números
        clean_phone = phone.replace("+", "")
        response = supabase.table("users").select("*").eq("guardian_phone", clean_phone).execute()
        users = response.data

    if not users:
        return None
    
    return users[0]

def fetch_student_progress(supabase: Client, user_id: str):
    """Busca as atividades recentes do aluno."""
    response = supabase.table("student_progress").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(10).execute()
    return response.data

def generate_family_report(student, progress):
    """Usa o Gemini para formatar o boletim de forma carinhosa e clara."""
    if not progress:
        return f"Olá! Sou o assistente da Educamob. O(A) aluno(a) {student['name']} ainda não realizou nenhuma atividade na plataforma recentemente. Incentive-o(a) a acessar o Portal de Estudos!"

    # Monta um resumo das notas
    stats_text = "\n".join([f"- Matéria: {p['subject_name']} | Acertos: {p['score']}% | Data: {p['created_at'][:10]}" for p in progress])
    
    prompt = f"""Você é a assistente virtual oficial da escola Educamob.
Sua função é atender os pais no WhatsApp e enviar relatórios de desempenho dos filhos.

DADOS DO ALUNO:
Nome: {student.get('name', 'Aluno')}
Série: {student.get('grade_level', 'Não informada')}
Desempenho Recente:
{stats_text}

MENSAGEM A SER GERADA:
Escreva uma mensagem de WhatsApp para o responsável (curta, calorosa e encorajadora).
- Comece cumprimentando e dizendo que traz notícias dos estudos.
- Resuma o desempenho de forma simples. Se as notas estão altas, parabenize o esforço conjunto da família. Se estão baixas, diga de forma amigável que ele precisa focar na revisão e que o Mob.me (nosso tutor IA) está à disposição para ajudá-lo 24h.
- Use emojis moderados.
- Assine como "Equipe Pedagógica Educamob 🚀"
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        res = model.generate_content(prompt)
        return res.text.strip()
    except Exception as e:
        print(f"Erro ao gerar report: {e}")
        return f"Olá! Tivemos um pequeno erro ao gerar o relatório detalhado, mas o(a) {student['name']} já realizou {len(progress)} atividades recentes. Acesse o portal para ver os detalhes!"

def send_whatsapp_message(remote_jid: str, text: str):
    """Envia a mensagem de volta para o Evolution API."""
    url = f"{EVO_API_URL}/message/sendText/{EVO_INSTANCE_NAME}"
    headers = {
        "Content-Type": "application/json",
        "apikey": EVO_API_KEY
    }
    payload = {
        "number": remote_jid,
        "options": {
            "delay": 1200, # Simula o tempo digitando
            "presence": "composing"
        },
        "text": text
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        print(f"Mensagem enviada com sucesso para {remote_jid}")
    except requests.exceptions.RequestException as e:
        print(f"Falha ao enviar mensagem WhatsApp para {remote_jid}: {e}")

def process_whatsapp_message(supabase: Client, webhook_payload):
    """Processa o webhook recebido do Evolution API em background."""
    if isinstance(webhook_payload, list):
        for payload in webhook_payload:
            process_whatsapp_message(supabase, payload)
        return
        
    if webhook_payload.get("event") != "messages.upsert":
        return

    try:
        data = webhook_payload.get("data")
        if not data or not data.get("message"):
            return

        message_data = data["message"]
        
        # Ignora mensagens enviadas pelo próprio robô
        if webhook_payload["data"].get("key", {}).get("fromMe"):
            return
            
        remote_jid = webhook_payload["data"].get("key", {}).get("remoteJid") # O ID do WhatsApp remetente
        if not remote_jid or "@g.us" in remote_jid:
            return # Ignora grupos
            
        phone = format_phone_number(remote_jid)
        print(f"Recebida mensagem WhatsApp de: {phone}")
        
        # 1. Buscar o aluno
        student = fetch_student_data(supabase, phone)
        if not student:
            # Não achou: mensagem padrão
            reply_text = "Olá! 👋 Sou o assistente virtual da Educamob. Não encontrei nenhum aluno matriculado associado a este número de telefone. Se precisar de ajuda, por favor contate nossa secretaria."
            send_whatsapp_message(remote_jid, reply_text)
            return
            
        # 2. Buscar progresso
        progress = fetch_student_progress(supabase, student["id"])
        
        # 3. Gerar relatório IA
        reply_text = generate_family_report(student, progress)
        
        # 4. Enviar mensagem
        send_whatsapp_message(remote_jid, reply_text)
        
    except Exception as e:
        print(f"Erro no processamento do WhatsApp Webhook: {e}")
