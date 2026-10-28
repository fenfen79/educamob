from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from contextlib import asynccontextmanager
import base64
import os
import time
import asyncio
import json
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI

from supabase.client import AsyncClient, create_async_client
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.supabase import SupabaseVectorStore
from memory import get_or_create_user, get_or_create_session, save_message, get_session_history, get_user_sessions, update_session_title, add_to_transient_cache
from whatsapp import process_whatsapp_message

import os
from dotenv import load_dotenv

# Sempre carrega o .env base para garantir as credenciais da API
load_dotenv()

# Se existir o .env.lab, carrega sobrescritas específicas de laboratório
if os.path.exists(".env.lab"):
    load_dotenv(".env.lab", override=True)
elif os.path.exists("services/mobme-api/.env.lab"):
    load_dotenv("services/mobme-api/.env.lab", override=True)

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))

supabase_client: AsyncClient = None
vector_store = None
deepinfra_client: AsyncOpenAI = None
embeddings = None

from supabase.client import Client, create_client

supabase_sync_client: Client = None

AVAILABLE_SUBJECTS_CONTEXT = ""

async def load_available_subjects():
    global AVAILABLE_SUBJECTS_CONTEXT
    try:
        response = await supabase_client.table("available_subjects").select("subject_name").execute()
        subjects = [item["subject_name"].capitalize() for item in response.data]
        if subjects:
            subjects_str = ", ".join(subjects)
            AVAILABLE_SUBJECTS_CONTEXT = f"\n\n--- MATÉRIAS DISPONÍVEIS NO MATERIAL DE CONSULTA ---\nAtualmente, a sua base de dados possui conteúdo focado estritamente nestas matérias: {subjects_str}. Você SÓ TEM PERMISSÃO para ensinar conteúdos dessas matérias. Caso o aluno solicite ajuda em qualquer matéria não listada (ex: Literatura, História, Artes), você DEVE recusar educadamente explicando que a equipe de professores da Educamob ainda está escrevendo os livros dessa disciplina e que, por enquanto, você só pode ajudar com as matérias disponíveis."
        else:
            AVAILABLE_SUBJECTS_CONTEXT = ""
        print("Matérias disponíveis atualizadas com sucesso na memória da API.")
    except Exception as e:
        print(f"Aviso: Não foi possível carregar as matérias. Certifique-se de que a tabela 'available_subjects' existe. Detalhe: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    global supabase_client, supabase_sync_client, vector_store, deepinfra_client, embeddings
    
    # Initialize Async Supabase Client for our operations
    supabase_client = await create_async_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Initialize DeepInfra OpenAI-Compatible Client
    deepinfra_client = AsyncOpenAI(
        api_key=os.getenv("DEEPINFRA_API_TOKEN", ""),
        base_url="https://api.deepinfra.com/v1/openai"
    )
    
    # Initialize Sync Client specifically for Langchain's VectorStore (which doesn't support AsyncClient yet)
    supabase_sync_client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Initialize Vector Store with DeepInfra via OpenAI-Compatible API
    embeddings = OpenAIEmbeddings(
        model="BAAI/bge-m3",
        openai_api_base="https://api.deepinfra.com/v1/openai",
        openai_api_key=os.getenv("DEEPINFRA_API_TOKEN", "")
    )
    vector_store = SupabaseVectorStore(
        client=supabase_sync_client,
        embedding=embeddings,
        table_name="documents",
        query_name="match_documents"
    )
    
    # Carrega as disciplinas disponíveis do Supabase na memória
    await load_available_subjects()
    
    yield

app = FastAPI(title="Mob.me AI Tutor API", lifespan=lifespan)

from fastapi.middleware.cors import CORSMiddleware

# Configuração de CORS unificada (Permite acesso local, LAN e túneis)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    image_base64: str | None = None
    user_id: str | None = "00000000-0000-0000-0000-000000000001"  # Mock UUID para testes
    session_id: str | None = None

class TitleUpdate(BaseModel):
    title: str

import os

# Guardrail de Ambiente: O prompt muda dependendo de onde o código roda
IS_LAB_ENV = os.path.exists("services/mobme-api/.env.lab") or os.path.exists(".env.lab")

if IS_LAB_ENV:
    PROMPT_FILE = "services/mobme-api/prompts/prompt_lab.md"
    if not os.path.exists(PROMPT_FILE):
        PROMPT_FILE = "prompts/prompt_lab.md"
else:
    PROMPT_FILE = "services/mobme-api/prompts/prompt_prod.md"
    if not os.path.exists(PROMPT_FILE):
        PROMPT_FILE = "prompts/prompt_prod.md"

MODES_DIR = "services/mobme-api/prompts/modes"
if not os.path.exists(MODES_DIR):
    MODES_DIR = "prompts/modes"

BASE_PERSONA_FILE = "services/mobme-api/prompts/base_persona.md"
if not os.path.exists(BASE_PERSONA_FILE):
    BASE_PERSONA_FILE = "prompts/base_persona.md"

SESSION_STATES_FILE = "services/mobme-api/session_states.json"
if not os.path.exists("services/mobme-api"):
    SESSION_STATES_FILE = "session_states.json"

SESSION_STATES: dict[str, dict] = {}

def load_session_states():
    global SESSION_STATES
    if os.path.exists(SESSION_STATES_FILE):
        try:
            with open(SESSION_STATES_FILE, "r", encoding="utf-8") as f:
                SESSION_STATES = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar session_states: {e}")
            SESSION_STATES = {}

def save_session_states():
    try:
        with open(SESSION_STATES_FILE, "w", encoding="utf-8") as f:
            json.dump(SESSION_STATES, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar session_states: {e}")

load_session_states()

GREETINGS = {"oi", "ola", "olá", "bom dia", "boa tarde", "boa noite", "tudo bem", "tudo bem?", "ei", "hey", "opa", "fala", "e ai", "e aí"}

SUPPORTED_DISCIPLINES = {
    "ciencias", "ciências", "matematica", "matemática", "fisica", "física", 
    "quimica", "química", "calculo", "cálculo", "calculo 1", "cálculo 1"
}

ALL_DISCIPLINES = SUPPORTED_DISCIPLINES | {
    "geografia", "historia", "história", "biologia", "filosofia", "sociologia", 
    "portugues", "português", "literatura", "ingles", "inglês", "artes", "redacao", "redação"
}

INVALID_TOPIC_WORDS = {
    "outro", "outra", "outros", "outras", "outro assunto", "outra matéria", "outra materia",
    "mudar", "mudar de materia", "mudar de matéria", "mudar de assunto", "trocar", "trocar de materia",
    "trocar de matéria", "trocar de assunto", "novo assunto", "nova materia", "nova matéria",
    "nenhum", "nenhuma", "nada", "nao sei", "não sei", "sei la", "sei lá", "tanto faz",
    "qualquer", "qualquer um", "qualquer uma", "qualquer coisa", "sei nao", "sei não",
    "ajuda", "me ajuda", "escolhe", "escolha", "escolhe você", "escolha você", "escolhe ai", "escolhe aí",
    "me diz você", "me diz voce", "opcao", "opção", "menu", "duvida", "dúvida", "assunto", "materia", "matéria", "conteudo", "conteúdo"
}

CHANGE_TOPIC_TRIGGERS = {
    "outro assunto", "mudar de materia", "mudar de matéria", "mudar de assunto",
    "trocar de materia", "trocar de matéria", "trocar de assunto", "novo assunto",
    "nova materia", "nova matéria", "outro", "outra", "mudar", "trocar"
}

PAUSE_TRIGGERS = {
    "parar", "quero parar", "pausa", "dar uma pausa", "cansei", "cansei por hoje",
    "muito difícil", "muito dificil", "chega", "para", "chega por hoje", "nao quero mais", "não quero mais", "interromper", "desisto", "cancela", "cancelar"
}

def get_or_init_session_state(session_id: str, db_history: list) -> dict:
    if session_id in SESSION_STATES:
        return SESSION_STATES[session_id]
        
    state = {
        "topic": None,
        "discipline": None,
        "current_mode": None,
        "pending_track": None
    }
    
    # Tenta reconstruir caso o servidor tenha reiniciado
    for msg in db_history:
        content = msg.get("content", "").strip()
        cl = content.lower()
        if msg.get("role") == "user":
            if cl in GREETINGS:
                continue
            if cl in ALL_DISCIPLINES:
                if not state["topic"]:
                    state["discipline"] = cl.capitalize()
                continue
            if cl in {"1", "2", "3", "4", "5", "6", "7", "8"} or "bora ler" in cl:
                continue
            if len(content) < 40 and cl not in ALL_DISCIPLINES and cl not in INVALID_TOPIC_WORDS and not state["topic"]:
                state["topic"] = content.capitalize()
                
    SESSION_STATES[session_id] = state
    return state

def resolve_active_mode_and_topic(session_id: str, db_history: list, current_message: str):
    state = get_or_init_session_state(session_id, db_history)
    msg_clean = current_message.strip().lower()
    
    # 0. Interrupção/Pausa em rodadas práticas (Treino, Desafio, Flashcards)
    if state.get("current_mode") in {"modo_treino", "modo_desafio", "modo_flashcards"} and any(w in msg_clean for w in PAUSE_TRIGGERS):
        # NÃO fecha com relatório forçado. Mantém no modo para a IA acolher a pausa com empatia
        return state["current_mode"], state["topic"], state

    # 1. Opção 8: Encerrar sessão
    if msg_clean in {"8", "8️⃣"} or msg_clean.startswith("8.") or "encerrar" in msg_clean:
        state["current_mode"] = "modo_conclusao"
        save_session_states()
        return "modo_conclusao", state["topic"], state

    # 2. SESSÃO ESTRITAMENTE MONOTEMÁTICA (Se o tema já está definido, NUNCA ceder à troca de assunto):
    if state.get("topic"):
        # 2.0 Tentativa de mudar de assunto ou matéria:
        if any(trigger in msg_clean for trigger in CHANGE_TOPIC_TRIGGERS) or any(w in msg_clean for w in ["nem falei", "nem tinha falado"]) or msg_clean in ALL_DISCIPLINES:
            state["current_mode"] = "modo_novo_assunto"
            save_session_states()
            return "modo_novo_assunto", state["topic"], state

        # 2.1 Se já estava em modo_novo_assunto (recusa de troca de assunto):
        if state.get("current_mode") == "modo_novo_assunto":
            # Se confirmou continuar no tema atual ou pediu menu:
            if any(w in msg_clean for w in ["continuar", "continua", "mesmo", "fica", "ficar", "voltar", "menu", "quero o menu", "vamos"]):
                state["current_mode"] = "modo_menu"
                save_session_states()
                return "modo_menu", state["topic"], state
            # Se escolheu uma opção numérica de estudo (1 a 7), deixamos fluir para o seletor de trilhas abaixo
            elif any(msg_clean.startswith(num) for num in ["1", "2", "3", "4", "5", "6", "7"]):
                pass
            else:
                # O estudante insiste no novo tema ou recusa a regra: NUNCA ceder! Mantém a recusa e o tema intacto
                return "modo_novo_assunto", state["topic"], state

        # 2.2 Solicitação explícita do Menu (ex: "quero o menu", "menu", "perdeu a configuração"):
        if msg_clean in {"menu", "o menu", "quero o menu", "ver menu", "opcoes", "opções", "ver opções", "perdeu a configuração", "perdeu a configuracao"}:
            state["current_mode"] = "modo_menu"
            save_session_states()
            return "modo_menu", state["topic"], state

    else:
        # Se o tema ainda NÃO foi definido (início da sessão):
        if msg_clean in ALL_DISCIPLINES:
            state["discipline"] = msg_clean.capitalize()
            state["topic"] = None
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        if msg_clean in GREETINGS or msg_clean in INVALID_TOPIC_WORDS or len(msg_clean) < 3:
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

    # 4. Seleção de trilha numérica ou textual (1 a 7)
    target_mode = None
    if msg_clean in {"1", "1️⃣"} or msg_clean.startswith("1.") or "bora ler" in msg_clean or "teoria" in msg_clean:
        target_mode = "modo_teoria"
    elif msg_clean in {"2", "2️⃣"} or msg_clean.startswith("2.") or "trocando ideias" in msg_clean:
        target_mode = "modo_socratico"
    elif msg_clean in {"3", "3️⃣"} or msg_clean.startswith("3.") or "flashcard" in msg_clean:
        target_mode = "modo_flashcards"
    elif msg_clean in {"4", "4️⃣"} or msg_clean.startswith("4.") or "memorex" in msg_clean:
        target_mode = "modo_memorex"
    elif msg_clean in {"5", "5️⃣"} or msg_clean.startswith("5.") or "treino" in msg_clean:
        target_mode = "modo_treino"
    elif msg_clean in {"6", "6️⃣"} or msg_clean.startswith("6.") or "desafio" in msg_clean:
        target_mode = "modo_desafio"
    elif msg_clean in {"7", "7️⃣"} or msg_clean.startswith("7.") or "sos" in msg_clean or "me ajuda" in msg_clean:
        target_mode = "modo_sos"

    if target_mode:
        if state["topic"]:
            # Já tem tema específico! Ativa imediatamente o modo
            state["current_mode"] = target_mode
            state["pending_track"] = None
            save_session_states()
            return target_mode, state["topic"], state
        else:
            # Ainda não tem tema: anota a preferência de trilha e chama acolhida para pedir o tema
            state["pending_track"] = target_mode
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

    # 5. Se ainda NÃO definiu o tema
    if not state["topic"]:
        if msg_clean in GREETINGS or msg_clean in INVALID_TOPIC_WORDS or len(msg_clean) < 3:
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state
            
        # O estudante informou um assunto específico!
        raw_topic = current_message.strip().strip(".!?,")
        if raw_topic.lower() in INVALID_TOPIC_WORDS:
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        state["topic"] = raw_topic[:40].capitalize()
        
        # Se ele já tinha pré-selecionado uma trilha (ex: apertou 1 antes de dizer o tema)
        if state["pending_track"]:
            chosen = state["pending_track"]
            state["current_mode"] = chosen
            state["pending_track"] = None
            save_session_states()
            return chosen, state["topic"], state
        else:
            # Não escolheu trilha: mostra o menu completo com o tema real!
            state["current_mode"] = "modo_menu"
            save_session_states()
            return "modo_menu", state["topic"], state

    # 6. Se o tema já está definido e a mensagem é texto livre (conversa dentro da trilha)
    if state["current_mode"] in {"modo_teoria", "modo_socratico", "modo_flashcards", "modo_memorex", "modo_treino", "modo_desafio", "modo_sos"}:
        return state["current_mode"], state["topic"], state

    # Caso padrão
    return "modo_menu", state["topic"], state

def get_system_prompt_for_mode(mode: str) -> str:
    # Se estiver em modo laboratório e a arquitetura modular existir:
    if IS_LAB_ENV and os.path.exists(BASE_PERSONA_FILE):
        mode_file = os.path.join(MODES_DIR, f"{mode}.md")
        if os.path.exists(mode_file):
            with open(BASE_PERSONA_FILE, "r", encoding="utf-8") as f:
                base_persona = f.read()
            with open(mode_file, "r", encoding="utf-8") as f:
                mode_instructions = f.read()
            return f"{base_persona}\n\n---\n\n{mode_instructions}"
            
    # Fallback para o arquivo tradicional de prompt
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def get_system_prompt():
    return get_system_prompt_for_mode("modo_menu")

print(f"[{'[LAB] MODO LABORATORIO (MODULAR)' if IS_LAB_ENV else '[PROD] MODO PRODUCAO'}] Inicializado com sucesso.")



from tenacity import retry, stop_after_attempt, wait_exponential_jitter

# Decorator para chamadas de API externas (Google/Gemini) com Jitter Orgânico
api_retry = retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=1, max=10),
    reraise=True
)

@api_retry
async def call_with_retry_async(func, *args, **kwargs):
    """Executa uma função com retry e jitter exponencial (usando Tenacity)"""
    return await func(*args, **kwargs)

@api_retry
async def extract_text_from_image(image_base64: str) -> str:
    """Extrai informações da imagem e transcreve para texto seguindo diretrizes universais."""
    prompt = """Você é um Transcritor Visual Universal de alta precisão. Seu papel é traduzir tudo o que existe nesta imagem para texto, para que outra IA (que não tem visão) possa resolvê-la. Não responda à pergunta, apenas extraia os dados seguindo estas regras:
1. Textos: Transcreva fielmente todos os textos, enunciados e alternativas visíveis.
2. Matemática, Química e Física (e outras matérias de cálculo também): Formate qualquer fórmula, equação, composto ou grandeza usando sintaxe MathJax/LaTeX rigorosa (ex: $H_2O$ ou $x^2$).
3. Ciências da Natureza e Geografia: Se houver esquemas anatômicos, mapas, gráficos ou biomas, faça uma descrição literal e minuciosa do que está desenhado e para onde as setas apontam.
4. Humanas: Se for uma foto histórica, charge ou pintura, descreva os elementos visuais, personagens e o layout.
5. Tabelas: Converta tabelas para formato Markdown.
Lembre-se: não resolva o problema, apenas descreva visualmente e transcreva o texto."""

    model = genai.GenerativeModel("gemini-2.5-flash", generation_config={"temperature": 0.0})
    
    # Remove prefixo de data URI se existir
    if "," in image_base64:
        image_base64 = image_base64.split(",")[1]
        
    parts = [
        {"inline_data": {"mime_type": "image/jpeg", "data": image_base64}},
        {"text": prompt}
    ]
    response = await call_with_retry_async(model.generate_content_async, parts)
    return response.text.strip()

async def update_long_term_memory(user_id: str, db_history: list):
    """Roda em background para analisar o histórico e atualizar o perfil do aluno no banco."""
    try:
        # Pega apenas as últimas 10 mensagens para não gastar muitos tokens
        recent_history = db_history[-10:]
        transcript = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_history])

        prompt = f"""Analise este trecho recente de conversa entre um aluno e um tutor de IA:
{transcript}

Extraia as principais dificuldades do aluno, suas preferências de aprendizado e qualquer detalhe pessoal relevante (ex: gosta de futebol, está com dificuldade em frações, aprende melhor com exemplos práticos).
Gere um resumo em 1 ou 2 parágrafos curtos. Se não houver nada de novo, resuma o que já se sabe."""

        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Chamada com Retry!
        response = await call_with_retry_async(model.generate_content_async, prompt)
        new_memory = response.text.strip()

        # Atualiza no banco
        await supabase_client.table("users").update({"long_term_memory": new_memory}).eq("id", user_id).execute()
        print(f"Memória de longo prazo atualizada para usuário {user_id}")
    except Exception as e:
        print(f"Erro ao atualizar memória de longo prazo: {e}")

async def generate_title_bg(session_id: str, first_message: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"Crie um título extremamente curto (2 a 4 palavras no máximo) que resuma a intenção desta mensagem do aluno: '{first_message}'. Retorne APENAS o título, sem aspas, sem formatação e sem explicações."
        response = await call_with_retry_async(model.generate_content_async, prompt)
        new_title = response.text.strip().replace('"', '').replace('*', '').replace('#', '')
        await update_session_title(supabase_client, session_id, new_title)
        print(f"Título da sessão {session_id} atualizado para: {new_title}")
    except Exception as e:
        print(f"Erro ao gerar título da sessão: {e}")

@app.get("/")
async def read_root():
    return {"status": "Mob.me Backend is running (Pure Async)!"}

@app.get("/api/sessions/{user_id}")
async def get_sessions(user_id: str):
    sessions = await get_user_sessions(supabase_client, user_id)
    return {"sessions": sessions}

@app.get("/api/chat/{session_id}")
async def get_chat_history_endpoint(session_id: str):
    history = await get_session_history(supabase_client, session_id)
    for msg in history:
        msg.pop("image_base64", None)
    return {"history": history}

@app.put("/api/sessions/{session_id}/title")
async def update_title_endpoint(session_id: str, data: TitleUpdate):
    await update_session_title(supabase_client, session_id, data.title)
    return {"status": "success", "title": data.title}

@app.post("/api/admin/reload-subjects")
async def reload_subjects_endpoint():
    await load_available_subjects()
    return {"status": "success", "message": "Matérias recarregadas na memória da API."}

# Cache global de RAG para Request Coalescing (evita múltiplas requisições de embedding idênticas)
RAG_CACHE = {}

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest, background_tasks: BackgroundTasks):
    t0 = time.time()
    if not request.user_id:
        raise HTTPException(status_code=400, detail="Usuário não autenticado. Faça login no portal.")

    try:
        # 1. Recuperar Usuário, Sessão e Histórico em Paralelo
        t_supa_start = time.time()
        
        is_new_session = not bool(request.session_id)
        
        async def fetch_session_and_history():
            sess_id = await get_or_create_session(supabase_client, request.user_id, request.session_id)
            history = await get_session_history(supabase_client, sess_id)
            return sess_id, history
            
        user_task = asyncio.create_task(get_or_create_user(supabase_client, request.user_id))
        session_history_task = asyncio.create_task(fetch_session_and_history())
        
        user, (current_session_id, db_history) = await asyncio.gather(user_task, session_history_task)
        
        print(f"[{time.time()-t_supa_start:.2f}s] Supabase User/Session/History Paralelo")

        # Se for uma sessão recém criada, dispara a background task para gerar o título
        if is_new_session:
            background_tasks.add_task(generate_title_bg, current_session_id, request.message)

        has_image = bool(request.image_base64)
        extracted_text = ""
        base_user_message = request.message

        # PIPELINE HÍBRIDO: Extrai o texto da imagem ANTES de salvar no banco
        if has_image:
            print("Extrapolando imagem para texto via Gemini-2.5-Flash (Vision Frontline)...")
            try:
                extracted_text = await extract_text_from_image(request.image_base64)
                base_user_message = f"[Imagem Anexada e Descrita pela IA Visual]:\n{extracted_text}\n\n{request.message}"
            except Exception as e:
                print(f"Erro na extração visual: {e}")
                
                # Resposta de contingência elegante quando o Google bloquear a imagem por falso positivo
                
                async def fallback_stream():
                    yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                    fallback_msg = "Puxa, o meu filtro de segurança bloqueou essa imagem sem querer. Você pode me mandar outra foto ou apenas digitar a sua dúvida?"
                    yield f"data: {json.dumps({'chunk': fallback_msg})}\n\n"
                    
                    # Salva o histórico para manter a consistência da conversa
                    opt1 = add_to_transient_cache(current_session_id, "user", request.message, None)
                    asyncio.create_task(save_message(supabase_client, current_session_id, "user", request.message, None, opt1))
                    
                    opt2 = add_to_transient_cache(current_session_id, "ai", fallback_msg, None)
                    asyncio.create_task(save_message(supabase_client, current_session_id, "ai", fallback_msg, None, opt2))
                    
                    yield "data: [DONE]\n\n"
                    
                return StreamingResponse(fallback_stream(), media_type="text/event-stream")

        # 2. Salvar a mensagem (agora APENAS TEXTO, sem o base64 para evitar inchaço e amnésia)
        opt_msg_user = add_to_transient_cache(current_session_id, "user", base_user_message, None)
        background_tasks.add_task(save_message, supabase_client, current_session_id, "user", base_user_message, None, opt_msg_user)

        # 3. Detectar o Modo de Operação Ativo, Atualizar Máquina de Estados e Carregar o Prompt Especialista
        active_mode, current_topic, session_state = resolve_active_mode_and_topic(current_session_id, db_history, request.message)
        print(f"[{current_session_id[:8]}] Modo Ativo: [{active_mode}] | Tema: [{current_topic}] | Trilha Pendente: [{session_state.get('pending_track')}]")
        
        system_prompt_base = get_system_prompt_for_mode(active_mode)
        state_context = f"\n\n--- ESTADO DA SESSÃO ATUAL ---\nTema atual: {current_topic or 'NENHUM (Ainda não foi informado pelo aluno)'}\nDisciplina informada: {session_state.get('discipline') or 'Geral'}"
        if session_state.get("pending_track"):
            state_context += f"\nTrilha escolhida pelo estudante: {session_state.get('pending_track')}"
            
        subjects_ctx = AVAILABLE_SUBJECTS_CONTEXT if active_mode not in {"modo_acolhida", "modo_novo_assunto"} else ""
        
        # Perfil do Aluno com Blindagem de Sigilo (Contexto Estritamente Silencioso)
        user_name = user.get('name', 'Estudante')
        user_grade = user.get('grade_level', 'Não informada')
        
        user_memory_ctx = ""
        # NUNCA injeta memória de longo prazo durante Acolhida, Apresentação de Menu ou Transição de Assunto
        if active_mode not in {"modo_acolhida", "modo_menu", "modo_novo_assunto"}:
            long_mem = (user.get('long_term_memory') or '').strip()
            if long_mem and long_mem != "Nenhuma preferência registrada ainda.":
                user_memory_ctx = (
                    f"\nObservações Didáticas Internas (USO ESTRITAMENTE SILENCIOSO - NUNCA CITE, RECITE OU DESPEJE NO ALUNO): {long_mem}"
                )

        dynamic_system_prompt = (
            system_prompt_base 
            + state_context 
            + subjects_ctx 
            + f"\n\n--- PERFIL DO ALUNO ---\nNome: {user_name}\nSérie: {user_grade}"
            + user_memory_ctx
        )

        # Montar histórico: Ambos recebem apenas texto!
        google_contents = []
        openai_messages = [{"role": "system", "content": dynamic_system_prompt}]
        
        for msg in db_history:
            # Como as imagens antigas agora já estão descritas no msg["content"], não tem image_base64!
            google_contents.append({
                "role": "model" if msg["role"] == "ai" else "user",
                "parts": [{"text": msg["content"]}]
            })
            openai_messages.append({
                "role": "assistant" if msg["role"] == "ai" else "user",
                "content": msg["content"],
            })

        # Retrieve Context from Vector Store with Request Coalescing
        try:
            msg_lower = request.message.strip().lower()
            is_flashcard_round = len(db_history) >= 1 and ("flashcard" in db_history[-1]["content"].lower() or "🃏" in db_history[-1]["content"])

            # Se for acolhida, menu inicial, encerramento ou se o tema ainda não foi definido, pula a busca no RAG para resposta em tempo real (< 1s)
            if (active_mode in {"modo_acolhida", "modo_menu", "modo_conclusao"} or not current_topic or (active_mode == "modo_flashcards" and is_flashcard_round)) and not request.image_base64:
                print(f"Modo de alta velocidade ou sem tema definido ({active_mode}). Pulando busca no RAG para resposta em tempo real...")
                context_str = ""
            else:
                t_rag_start = time.time()
                target_subject = current_topic if current_topic else request.message
                
                # Calibrar a query e o volume de chunks conforme o modo
                if active_mode == "modo_teoria":
                    search_query = f"E-book Teoria: {target_subject}"
                    match_count = 12
                elif active_mode in {"modo_treino", "modo_desafio"}:
                    search_query = f"Lista de Exercícios: {target_subject}"
                    match_count = 6
                elif active_mode == "modo_memorex":
                    search_query = f"E-book Teoria: {target_subject}"
                    match_count = 6
                else:
                    search_query = f"{target_subject} - {request.message}"
                    match_count = 4

                cache_key = f"{search_query.strip().lower()}__mc{match_count}"
                
                if cache_key in RAG_CACHE:
                    print("Cache hit (ou aguardando co-requisição) para RAG...")
                    future_or_str = RAG_CACHE[cache_key]
                    if isinstance(future_or_str, asyncio.Future):
                        context_str = await future_or_str
                    else:
                        context_str = future_or_str
                    print(f"[{time.time()-t_rag_start:.2f}s] Recuperado do Cache Semântico")
                else:
                    # Inicia a busca original e salva um Future para as requisições concorrentes
                    future = asyncio.Future()
                    RAG_CACHE[cache_key] = future
                    
                    try:
                        # PURE ASYNC RAG: Bypass Langchain's blocking ThreadPool
                        # 1. Gerar embedding nativamente assíncrono via AsyncOpenAI com timeout de 5s
                        embed_response = await asyncio.wait_for(
                            deepinfra_client.embeddings.create(
                                input=search_query,
                                model="BAAI/bge-m3"
                            ),
                            timeout=5.0
                        )
                        query_embedding = embed_response.data[0].embedding
                        
                        # 2. Buscar no Supabase nativamente assíncrono com timeout de 5.0s (HNSW index ativo)
                        response = await asyncio.wait_for(
                            supabase_client.rpc(
                                "match_documents",
                                {"query_embedding": query_embedding, "match_count": match_count}
                            ).execute(),
                            timeout=5.0
                        )
                        
                        print(f"[{time.time()-t_rag_start:.2f}s] Supabase Vector Search ({match_count} chunks)")
                        
                        context_str = "\n\n".join([f"--- Contexto Recuperado ({d.get('metadata', {}).get('source', 'Apostila')}) ---\n{d.get('content', '')}" for d in response.data])
                        
                        future.set_result(context_str)
                        RAG_CACHE[cache_key] = context_str  # Substitui o Future pela string resolvida
                    except Exception as e:
                        future.set_exception(e)
                        if cache_key in RAG_CACHE:
                            del RAG_CACHE[cache_key]
                        raise e
        except Exception as e:
            print(f"RAG bypass ou timeout controlado: {e}")
            context_str = ""

        # Build system prompt with RAG context if available
        if context_str:
            dynamic_system_prompt += f"\n\n--- MATERIAL DE CONSULTA RELEVANTE PARA A PERGUNTA ATUAL ---\n{context_str}\n(Siga suas regras pedagógicas estritamente, use este material apenas como base de conhecimento se necessário)."
            openai_messages[0]["content"] = dynamic_system_prompt

        google_contents.append({"role": "user", "parts": [{"text": base_user_message}]})
        openai_messages.append({"role": "user", "content": base_user_message})

        async def generate_stream():
            try:
                # 1. Enviar o session_id imediatamente no primeiro chunk
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                
                # 2. Streaming Multi-LLM (DeepSeek Principal -> Gemini Fallback)
                t_start = time.time()
                full_text = ""
                
                try:
                    # Rota Principal: DeepSeek via DeepInfra (Fail-Fast)
                    max_toks = 8192 if active_mode == "modo_teoria" else 4096
                    response = await deepinfra_client.chat.completions.create(
                        model="deepseek-ai/DeepSeek-V4-Flash-0731",
                        messages=openai_messages,
                        max_tokens=max_toks,
                        stream=True
                    )
                    
                    async for chunk in response:
                        if chunk.choices and chunk.choices[0].delta.content is not None:
                            text = chunk.choices[0].delta.content
                            full_text += text
                            yield f"data: {json.dumps({'chunk': text})}\n\n"
                            await asyncio.sleep(0)
                            
                except Exception as e:
                    error_str = str(e).lower()
                    print(f"[{time.time()-t_start:.2f}s] AVISO: Falha no DeepSeek ({error_str}). Acionando Fallback para Gemini...")
                    
                    # Fallback de Resiliência usando Gemini
                    max_toks = 8192 if active_mode == "modo_teoria" else 4096
                    model = genai.GenerativeModel(
                        "gemini-2.5-flash", 
                        system_instruction=dynamic_system_prompt,
                        generation_config={"max_output_tokens": max_toks}
                    )
                    response = await call_with_retry_async(model.generate_content_async, google_contents, stream=True)
                    
                    async for chunk in response:
                        try:
                            text = chunk.text
                        except ValueError:
                            continue
                        if text:
                            full_text += text
                            yield f"data: {json.dumps({'chunk': text})}\n\n"
                            await asyncio.sleep(0)
                
                if not full_text.strip():
                    full_text = "Hmm, não consegui entender isso muito bem. Você poderia tentar explicar de outra forma? 🤔"
                    yield f"data: {json.dumps({'chunk': full_text})}\n\n"
                
                print(f"[{time.time()-t_start:.2f}s] API Streaming Completed")

                # 3. Salvar resposta final da IA no banco em background
                opt_msg_ai = add_to_transient_cache(current_session_id, "ai", full_text, None)
                background_tasks.add_task(save_message, supabase_client, current_session_id, "ai", full_text, None, opt_msg_ai)

                # 4. Atualizar Memória Longo Prazo se necessário
                if len(db_history) > 0 and len(db_history) % 5 == 0:
                    background_tasks.add_task(update_long_term_memory, request.user_id, db_history)

                yield "data: [DONE]\n\n"

            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return StreamingResponse(generate_stream(), media_type="text/event-stream")

    except Exception as e:
        return {
            "reply": f"⚠️ Desculpe, tive um problema ao processar sua pergunta. Erro: {str(e)}"
        }

@app.post("/api/webhook/whatsapp")
async def whatsapp_webhook(payload: dict, background_tasks: BackgroundTasks):
    """
    Webhook receptor para a Evolution API.
    A Evolution API exige um retorno 2xx ultrarrápido, por isso passamos o processamento para background.
    """
    background_tasks.add_task(process_whatsapp_message, supabase_client, payload)
    return {"status": "received"}
