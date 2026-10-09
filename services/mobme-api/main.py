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

# Carrega o .env.lab se existir (Laboratorio)
if os.path.exists(".env.lab"):
    load_dotenv(".env.lab", override=True)
else:
    load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# HARD GUARDRAIL: Prevenir conexão acidental com Produção
PROD_URL = "https://jaaiyectjtmlymcjzgpb.supabase.co"
if os.path.exists(".env.lab") and SUPABASE_URL == PROD_URL:
    raise RuntimeError("🚨 ALERTA CRÍTICO: Você está rodando o Laboratório com as chaves do Supabase Oficial! Servidor abortado para proteger os alunos reais.")

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
            AVAILABLE_SUBJECTS_CONTEXT = f"\n\n--- MATÉRIAS DISPONÍVEIS NO MATERIAL DE CONSULTA ---\nAtualmente, a sua base de dados possui conteúdo focado apenas nestas matérias: {subjects_str}. Para dúvidas de TODAS AS OUTRAS matérias escolares que não estão listadas aqui, você DEVE usar e ensinar a partir do seu próprio conhecimento prévio."
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

# Configuração de CORS unificada
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "https://educamob.com.br", "https://app.educamob.com.br", "https://fenfen79.github.io"],
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
if os.path.exists("services/mobme-api/.env.lab") or os.path.exists(".env.lab"):
    PROMPT_FILE = "services/mobme-api/prompts/prompt_lab.md"
    if not os.path.exists(PROMPT_FILE):
        PROMPT_FILE = "prompts/prompt_lab.md"
else:
    PROMPT_FILE = "services/mobme-api/prompts/prompt_prod.md"
    if not os.path.exists(PROMPT_FILE):
        PROMPT_FILE = "prompts/prompt_prod.md"

with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

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

        # 3. Injetar as "Matérias Disponíveis" e a "Memória de Longo Prazo" no prompt do sistema
        dynamic_system_prompt = SYSTEM_PROMPT + AVAILABLE_SUBJECTS_CONTEXT + f"\n\n--- PERFIL DO ALUNO ---\nNome: {user.get('name', 'Estudante')}\nSérie: {user.get('grade_level', 'Não informada')}\nMemória sobre o aluno: {user.get('long_term_memory', '')}"

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
            greetings = {"oi", "ola", "olá", "bom dia", "boa tarde", "boa noite", "tudo bem", "tudo bem?", "ei", "hey", "opa", "fala", "e ai", "e aí"}
            
            if msg_lower in greetings and not request.image_base64:
                print("Saudação simples detectada. Pulando busca no RAG para acelerar resposta...")
                context_str = ""
            else:
                t_rag_start = time.time()
                search_query = request.message
                if len(db_history) >= 1:
                    last_ai_msg = db_history[-1]["content"]
                    search_query = f"{last_ai_msg}\nResposta do aluno: {request.message}"

                cache_key = search_query.strip().lower()
                
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
                        # 1. Gerar embedding nativamente assíncrono via AsyncOpenAI
                        embed_response = await deepinfra_client.embeddings.create(
                            input=search_query,
                            model="BAAI/bge-m3"
                        )
                        query_embedding = embed_response.data[0].embedding
                        
                        # 2. Buscar no Supabase nativamente assíncrono
                        response = await supabase_client.rpc(
                            "match_documents",
                            {"query_embedding": query_embedding, "match_count": 12}
                        ).execute()
                        
                        print(f"[{time.time()-t_rag_start:.2f}s] Supabase Vector Search (Pure Async)")
                        
                        context_str = "\n\n".join([f"--- Contexto Recuperado ({d.get('metadata', {}).get('source', 'Apostila')}) ---\n{d.get('content', '')}" for d in response.data])
                        
                        future.set_result(context_str)
                        RAG_CACHE[cache_key] = context_str  # Substitui o Future pela string resolvida
                    except Exception as e:
                        future.set_exception(e)
                        del RAG_CACHE[cache_key]
                        raise e
        except Exception as e:
            print(f"Erro ao recuperar contexto: {e}")
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
                    response = await deepinfra_client.chat.completions.create(
                        model="deepseek-ai/DeepSeek-V4-Flash-0731",
                        messages=openai_messages,
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
                    model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=dynamic_system_prompt)
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
