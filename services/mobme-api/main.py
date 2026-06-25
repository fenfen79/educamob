from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from google import genai as genai_new
import base64
import os
import time
from supabase.client import Client, create_client
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores.supabase import SupabaseVectorStore
from memory import get_or_create_user, get_or_create_session, save_message, get_session_history, get_user_sessions, update_session_title
from whatsapp import process_whatsapp_message

load_dotenv()

# Configure Gemini API (old SDK for auxiliary tasks)
genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))

# Configure new Gemini SDK (for fast streaming with thinking disabled)
gemini_client = genai_new.Client(api_key=os.getenv("GEMINI_API_KEY", ""))

# Configure Supabase & RAG
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

SYSTEM_PROMPT = r"""# PERSONA E TOM DE VOZ
Você é a **Mob.me**, a Tutora Inteligente da Educamob. 
- **Regra de Ouro:** Você é uma **facilitadora do aprendizado**, não um gabarito de respostas. O protagonista é o aluno.
- **Comunicação:** Textos curtíssimos. Máximo 2 linhas por parágrafo. Seja paciente, encorajadora e apaixonada por ensinar.
- **Visual:** Use emojis moderadamente e **negrito** para destacar conceitos-chave.
- **Nomes e Apelidos:** Se o "PERFIL DO ALUNO" fornecido no final deste prompt informar que o aluno prefere ser chamado por um apelido ou outro nome, PRIORIZE esse apelido em vez do nome de cadastro.

# PROIBIÇÕES ABSOLUTAS (NÃO NEGOCIÁVEL)
1. **NUNCA dê a resposta final:** Jamais resolva um cálculo até o fim ou entregue a teoria mastigada de cara. Se o aluno pedir a resposta pronta, responda com carinho: "Meu papel é te ajudar a chegar lá por conta própria! Vamos pensar juntos: o que você já sabe sobre isso?"
2. **NUNCA resolva a foto de imediato:** Se o aluno enviar a foto de uma questão, leia a questão, mas force-o a dar o primeiro passo: "Por onde você acha que devemos começar?"
3. **NUNCA escreva blocos de texto:** Se a resposta não couber em tópicos curtos, ela está errada.

# FLUXO SOCRÁTICO OBRIGATÓRIO (SIGA A ORDEM)
Sempre que uma nova dúvida chegar, force este ciclo:
**1. Diagnóstico:** Descubra o que o aluno já sabe ou onde ele travou ("Até onde você conseguiu entender?"). Se o aluno disser "não sei nada", dê o primeiro passo como exemplo e peça para ele tentar o segundo.
**2. Micro-passos:** Quebre o problema complexo na menor etapa possível e faça uma pergunta focada ("Qual é a fórmula que usamos aqui?").
**3. Validação:** Quando ele acertar, comemore efusivamente e passe para o próximo passo. Se errar, dê uma dica e reformule a pergunta. NUNCA corrija dando a resposta.
**4. Síntese:** Ao chegar na solução final, peça para ele explicar o que aprendeu.

# PADRÃO DE RESPOSTA (OBRIGATÓRIO)
Toda interação em que o aluno tentar resolver um passo deve seguir este layout visual:

**O que você acertou:**
- [Elogio curto sobre a tentativa ou acerto]

**Ajuste de Rota:**
- [Correção suave ou dica curta para a próxima etapa. Se ele errou, explique o 'por que' sem dar a resposta do 'como']

**Próximo Passo:**
- [A sua pergunta final que exige ação e resposta do aluno]

# REGRAS TÉCNICAS E DE SEGURANÇA
1. **Foco Estrito:** Se o aluno puxar assuntos inapropriados, perigosos ou fugir do escopo escolar (ex: fofocas, videogames não-educativos, relacionamentos), recuse polidamente e redirecione para os estudos.
2. **Restrição RAG (Anti-Alucinação):** Você DEVE basear suas explicações teóricas no "Material de consulta". Se a pergunta for sobre um assunto escolar que não consta no material fornecido, diga educadamente que aquele tópico específico não está no seu banco de dados atual e sugira que ele busque um professor da Educamob. Não use conhecimento externo para inventar a teoria.
3. **Formatação Matemática:** Toda fórmula, monômio ou equação deve OBRIGATORIAMENTE ser escrita usando formatação LaTeX delimitada por cifrões (`$formula$` para inline, `$$formula$$` para blocos isolados). NUNCA use `\(` ou `\[`. NUNCA use crases para blocos matemáticos.
4. **Contexto:** Mantenha o contexto da conversa. Nunca peça informações que o aluno já forneceu nas mensagens anteriores.
"""

app = FastAPI(title="Mob.me AI Tutor API")

# CORS – allow the Next.js dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5500", "https://educamob.com.br", "https://app.educamob.com.br"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    image_base64: str | None = None
    user_id: str | None = "00000000-0000-0000-0000-000000000001"  # Mock UUID para testes
    session_id: str | None = None

def call_with_retry(func, *args, **kwargs):
    """Executa uma função e, se tomar bloqueio 429 ou erro 503, aguarda 15s e tenta de novo (máx 6 vezes para cobrir 1 minuto)."""
    max_retries = 6
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_str = str(e).lower()
            if "429" in error_str or "quota" in error_str or "503" in error_str or "service unavailable" in error_str:
                if attempt < max_retries - 1:
                    print(f"AVISO: Instabilidade ou Limite do Google atingido. Aguardando 15 segundos (Tentativa {attempt + 1}/{max_retries})...")
                    time.sleep(15)
                else:
                    raise
            else:
                raise e

def update_long_term_memory(user_id: str, db_history: list):
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
        response = call_with_retry(model.generate_content, prompt)
        new_memory = response.text.strip()

        # Atualiza no banco
        supabase.table("users").update({"long_term_memory": new_memory}).eq("id", user_id).execute()
        print(f"Memória de longo prazo atualizada para usuário {user_id}")
    except Exception as e:
        print(f"Erro ao atualizar memória de longo prazo: {e}")


@app.get("/")
def read_root():
    return {"status": "Mob.me Backend is running!"}

@app.get("/api/sessions/{user_id}")
def get_sessions(user_id: str):
    sessions = get_user_sessions(supabase, user_id)
    return {"sessions": sessions}

@app.get("/api/chat/{session_id}")
def get_chat_history_endpoint(session_id: str):
    history = get_session_history(supabase, session_id)
    return {"history": history}

def generate_title_bg(session_id: str, first_message: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"Crie um título extremamente curto (2 a 4 palavras no máximo) que resuma a intenção desta mensagem do aluno: '{first_message}'. Retorne APENAS o título, sem aspas, sem formatação e sem explicações."
        response = call_with_retry(model.generate_content, prompt)
        new_title = response.text.strip().replace('"', '').replace('*', '').replace('#', '')
        update_session_title(supabase, session_id, new_title)
        print(f"Título da sessão {session_id} atualizado para: {new_title}")
    except Exception as e:
        print(f"Erro ao gerar título da sessão: {e}")

class TitleUpdate(BaseModel):
    title: str

@app.put("/api/sessions/{session_id}/title")
def update_title_endpoint(session_id: str, data: TitleUpdate):
    update_session_title(supabase, session_id, data.title)
    return {"status": "success", "title": data.title}


@app.post("/api/chat")
def chat_endpoint(request: ChatRequest, background_tasks: BackgroundTasks):
    t0 = time.time()
    if not request.user_id:
        raise HTTPException(status_code=400, detail="Usuário não autenticado. Faça login no portal.")

    try:
        # 1. Recuperar Usuário e Sessão
        t_supa_start = time.time()
        user = get_or_create_user(supabase, request.user_id)
        
        is_new_session = False
        if not request.session_id:
            is_new_session = True
            
        current_session_id = get_or_create_session(supabase, request.user_id, request.session_id)
        print(f"[{time.time()-t_supa_start:.2f}s] Supabase User/Session")

        # Se for uma sessão recém criada, dispara a background task para gerar o título
        if is_new_session:
            background_tasks.add_task(generate_title_bg, current_session_id, request.message)

        # 2. Salvar a mensagem do usuário no banco
        t_save_start = time.time()
        save_message(supabase, current_session_id, "user", request.message)

        # 3. Injetar a "Memória de Longo Prazo" no prompt do sistema
        dynamic_system_prompt = SYSTEM_PROMPT + f"\n\n--- PERFIL DO ALUNO ---\nNome: {user['name']}\nSérie: {user.get('grade_level', 'Não informada')}\nMemória sobre o aluno: {user.get('long_term_memory', '')}"

        # 4. Recuperar o histórico da sessão do banco de dados (ignora o frontend)
        db_history = get_session_history(supabase, current_session_id)
        print(f"[{time.time()-t_save_start:.2f}s] Supabase Save/History")
        
        # Montar histórico no formato da nova SDK
        contents = []
        for msg in db_history:
            if msg["content"] == request.message and msg == db_history[-1]:
                continue
            contents.append({
                "role": "model" if msg["role"] == "ai" else "user",
                "parts": [{"text": msg["content"]}],
            })

        # Build content parts for the current message
        current_parts = []

        if request.image_base64:
            current_parts.append({
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": request.image_base64,
                }
            })

        # Retrieve Context from Vector Store
        try:
            msg_lower = request.message.strip().lower()
            greetings = {"oi", "ola", "olá", "bom dia", "boa tarde", "boa noite", "tudo bem", "tudo bem?", "ei", "hey", "opa", "fala", "e ai", "e aí"}
            
            if msg_lower in greetings and not request.image_base64:
                print("Saudação simples detectada. Pulando busca no RAG para acelerar resposta...")
                context_str = ""
            else:
                t_rag_start = time.time()
                search_query = request.message
                if len(db_history) >= 2:
                    last_ai_msg = db_history[-2]["content"]
                    search_query = f"{last_ai_msg}\nResposta do aluno: {request.message}"

                docs = call_with_retry(vector_store.similarity_search, search_query, k=12)
                print(f"[{time.time()-t_rag_start:.2f}s] Supabase Vector Search")
                context_str = "\n\n".join([f"--- Contexto Recuperado ({d.metadata.get('source', 'Apostila')}) ---\n{d.page_content}" for d in docs])
        except Exception as e:
            print(f"Erro ao recuperar contexto: {e}")
            context_str = ""

        # Build prompt with context if available
        if context_str:
            prompt_with_context = f"""Material de consulta (use para embasar sua resposta se for relevante para a pergunta do aluno, mas não diga explicitamente "no material de consulta"):
{context_str}

Pergunta/Mensagem do aluno:
{request.message}"""
        else:
            prompt_with_context = request.message

        current_parts.append({"text": prompt_with_context})
        contents.append({"role": "user", "parts": current_parts})

        from fastapi.responses import StreamingResponse
        import json

        def generate_stream():
            try:
                # 1. Enviar o session_id imediatamente no primeiro chunk
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                
                # 2. Streaming com nova SDK + thinking desabilitado para máxima velocidade
                t_gemini_start = time.time()
                
                response = None
                max_retries = 3
                current_model = "gemini-2.5-flash"
                for attempt in range(max_retries):
                    try:
                        response = gemini_client.models.generate_content_stream(
                            model=current_model,
                            contents=contents,
                            config={
                                "system_instruction": dynamic_system_prompt,
                            },
                        )
                        break
                    except Exception as e:
                        error_str = str(e).lower()
                        if "429" in error_str or "quota" in error_str or "503" in error_str:
                            if attempt < max_retries - 1:
                                print(f"AVISO: Falha no modelo {current_model}. Mudando para fallback gemini-2.0-flash...")
                                current_model = "gemini-2.0-flash" # Fallback invisível
                            else:
                                raise e
                        else:
                            raise e

                full_text = ""
                for chunk in response:
                    try:
                        text = chunk.text
                    except ValueError:
                        # Ocasionalmente a API não retorna partes de texto (ex: bloqueio de safety silencioso)
                        continue
                    if text:
                        full_text += text
                        yield f"data: {json.dumps({'chunk': text})}\n\n"
                        # Nota: asyncio.sleep requer que esta função seja async ou rodar em thread
                
                # Fallback caso a API decida não enviar absolutamente nada (balão vazio)
                if not full_text.strip():
                    full_text = "Hmm, não consegui entender isso muito bem. Você poderia tentar explicar de outra forma? 🤔"
                    yield f"data: {json.dumps({'chunk': full_text})}\n\n"
                
                print(f"[{time.time()-t_gemini_start:.2f}s] Gemini API Streaming Completed")

                # 3. Salvar resposta final da IA no banco
                t_save_ai_start = time.time()
                save_message(supabase, current_session_id, "ai", full_text)
                print(f"[{time.time()-t_save_ai_start:.2f}s] Supabase Save AI Msg (Sync)")

                # 4. Atualizar Memória Longo Prazo se necessário
                if len(db_history) > 0 and len(db_history) % 5 == 0:
                    update_long_term_memory(request.user_id, db_history)

                yield "data: [DONE]\n\n"

            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return StreamingResponse(generate_stream(), media_type="text/event-stream")

    except Exception as e:
        return {
            "reply": f"⚠️ Desculpe, tive um problema ao processar sua pergunta. Erro: {str(e)}"
        }

@app.post("/api/webhook/whatsapp")
def whatsapp_webhook(payload: dict, background_tasks: BackgroundTasks):
    """
    Webhook receptor para a Evolution API.
    A Evolution API exige um retorno 2xx ultrarrápido, por isso passamos o processamento para background.
    """
    background_tasks.add_task(process_whatsapp_message, supabase, payload)
    return {"status": "received"}
