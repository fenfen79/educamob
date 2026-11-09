import unicodedata
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
from fastapi.responses import StreamingResponse, Response
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
AVAILABLE_SUBJECTS_LIST = ["Ciências", "Matemática", "Física", "Química", "História", "Geografia", "Cálculo 1"]

SUBJECT_DISPLAY_MAP = {
    "ciencias": "Ciências",
    "matematica": "Matemática",
    "fisica": "Física",
    "quimica": "Química",
    "calculo-1": "Cálculo 1",
    "calculo": "Cálculo 1",
    "biologia": "Biologia",
    "historia": "História",
    "geografia": "Geografia",
    "portugues": "Língua Portuguesa",
    "literatura": "Literatura",
    "ingles": "Inglês",
    "filosofia": "Filosofia",
    "sociologia": "Sociologia",
    "artes": "Artes",
    "redacao": "Redação",
}

async def load_available_subjects():
    global AVAILABLE_SUBJECTS_CONTEXT, AVAILABLE_SUBJECTS_LIST, SUPPORTED_DISCIPLINES, ALL_DISCIPLINES
    try:
        response = await supabase_client.table("available_subjects").select("subject_name").execute()
        raw_names = [item["subject_name"].strip().lower() for item in response.data if item.get("subject_name")]
        if raw_names:
            display_subjects = []
            dynamic_supported = set()
            for rname in raw_names:
                disp = SUBJECT_DISPLAY_MAP.get(rname, rname.replace("-", " ").title())
                if disp not in display_subjects:
                    display_subjects.append(disp)
                # Adiciona variantes com e sem acento / hífen em SUPPORTED_DISCIPLINES
                dynamic_supported.add(rname)
                dynamic_supported.add(rname.replace("-", " "))
                dynamic_supported.add(disp.lower())
                norm_disp = "".join(c for c in unicodedata.normalize("NFD", disp.lower()) if unicodedata.category(c) != "Mn")
                dynamic_supported.add(norm_disp)
                if "calculo" in norm_disp:
                    dynamic_supported.update({"calculo", "cálculo", "calculo 1", "cálculo 1"})
            AVAILABLE_SUBJECTS_LIST = display_subjects
            SUPPORTED_DISCIPLINES = dynamic_supported
            NON_SUPPORTED_DISCIPLINES.difference_update(SUPPORTED_DISCIPLINES)
            ALL_DISCIPLINES = SUPPORTED_DISCIPLINES | NON_SUPPORTED_DISCIPLINES
            subjects_str = ", ".join(AVAILABLE_SUBJECTS_LIST)
            AVAILABLE_SUBJECTS_CONTEXT = f"\n\n--- MATÉRIAS DISPONÍVEIS NO MATERIAL DE CONSULTA ---\nAtualmente, a sua base de dados possui conteúdo focado estritamente nestas matérias: {subjects_str}. Você SÓ TEM PERMISSÃO para ensinar conteúdos dessas matérias. Caso o aluno solicite ajuda em qualquer matéria não listada (ex: Biologia, Literatura, Língua Portuguesa, Filosofia, Sociologia, Inglês, Artes), você DEVE recusar educadamente explicando que a equipe de professores da Educamob ainda está preparando os materiais dessa disciplina e que, por enquanto, você só pode ajudar com as matérias disponíveis ({subjects_str})."
        else:
            AVAILABLE_SUBJECTS_CONTEXT = ""
        print(f"Matérias disponíveis atualizadas dinamicamente na memória da API: {AVAILABLE_SUBJECTS_LIST}")
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

# System Prompt Oficial de Produção: v2.0.0 (Codinome: "Mob.me 6 Trilhas")
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
    "quimica", "química", "historia", "história", "geografia",
    "calculo", "cálculo", "calculo 1", "cálculo 1", "calculo-1"
}

NON_SUPPORTED_DISCIPLINES = {
    "biologia", "filosofia", "sociologia", 
    "portugues", "português", "literatura", "ingles", "inglês", "espanhol", "artes", "redacao", "redação", "gramatica", "gramática"
}

ALL_DISCIPLINES = SUPPORTED_DISCIPLINES | NON_SUPPORTED_DISCIPLINES

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


from difflib import SequenceMatcher
import re

def strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn").lower()

def is_fuzzy_word_match(w1: str, w2: str, threshold: float = 0.78) -> bool:
    w1, w2 = strip_accents(w1).strip(), strip_accents(w2).strip()
    if not w1 or not w2:
        return False
    if w1 == w2:
        return True
    # Trata singular/plural (ex: matematica vs matematicas)
    if w1.rstrip("s") == w2.rstrip("s") and len(w1.rstrip("s")) >= 4:
        return True
    if len(w1) >= 4 and len(w2) >= 4:
        if w1 in w2 or w2 in w1:
            return True
        return SequenceMatcher(None, w1, w2).ratio() >= threshold
    return False

def match_discipline_fuzzy(text: str) -> str | None:
    """Verifica se o texto digitado é apenas o nome de uma disciplina (mesmo com erro de digitação como 'matemaica')."""
    norm = strip_accents(text).strip()
    words = re.findall(r"[a-z0-9]+", norm)
    if not words or len(words) > 2:
        return None
    joined = " ".join(words)
    for d in ALL_DISCIPLINES:
        nd = strip_accents(d)
        if joined == nd or (len(joined) >= 5 and len(nd) >= 5 and SequenceMatcher(None, joined, nd).ratio() >= 0.82):
            return nd
    return None

BROAD_TOPICS_REGISTRY = {
    "bernoulli": {
        "key": "Bernoulli",
        "triggers": ["bernoulli"],
        "specific_exceptions": ["principio", "teorema", "equacao", "lei", "hidrodinamica", "fluido"],
        "options": [
            "**Princípio de Bernoulli** (Física / Hidrodinâmica - voo de aviões, fluidos e sustentação)",
            "**Equação / Teorema de Bernoulli** (Matemática / Cálculo)",
            "**Outro tópico específico** de Bernoulli"
        ],
        "clean_names": [
            "Princípio de Bernoulli",
            "Teorema de Bernoulli",
            "Bernoulli"
        ]
    },
    "newton": {
        "key": "Newton",
        "triggers": ["newton"],
        "specific_exceptions": ["lei", "leis", "1", "2", "3", "primeira", "segunda", "terceira", "gravitacao", "binomio"],
        "options": [
            "**Leis de Newton** (1ª, 2ª e 3ª Leis da Mecânica e Forças)",
            "**Lei da Gravitação Universal**",
            "**Outro tópico sobre Newton**"
        ],
        "clean_names": [
            "Leis de Newton",
            "Gravitação Universal",
            "Newton"
        ]
    },
    "cinematica": {
        "key": "Cinemática",
        "triggers": ["cinematica"],
        "specific_exceptions": ["mu", "muv", "mcu", "movimento uniforme", "queda livre", "lancamento", "velocidade media", "graficos"],
        "options": [
            "**Movimento Uniforme e MUV** (Velocidade, Aceleração e Gráficos)",
            "**Queda Livre e Lançamentos** (Vertical, Horizontal e Oblíquo)",
            "**Movimento Circular Uniforme (MCU)**"
        ],
        "clean_names": [
            "Movimento Uniforme e MUV",
            "Queda Livre e Lançamentos",
            "Movimento Circular Uniforme"
        ]
    },
    "dinamica": {
        "key": "Dinâmica",
        "triggers": ["dinamica"],
        "specific_exceptions": ["leis de newton", "atrito", "energia", "trabalho", "impulso", "quantidade de movimento"],
        "options": [
            "**Leis de Newton e Forças** (Peso, Normal, Tração e Atrito)",
            "**Trabalho, Potência e Energia Mecânica**",
            "**Impulso e Quantidade de Movimento**"
        ],
        "clean_names": [
            "Leis de Newton e Forças",
            "Trabalho e Energia Mecânica",
            "Impulso e Quantidade de Movimento"
        ]
    },
    "hidrostatica": {
        "key": "Hidrostática",
        "triggers": ["hidrostatica"],
        "specific_exceptions": ["stevin", "pascal", "arquimedes", "empuxo", "prensa", "pressao"],
        "options": [
            "**Pressão e Teorema de Stevin** (Pressão Hidrostática)",
            "**Princípio de Pascal** (Prensa Hidráulica)",
            "**Princípio de Arquimedes e Empuxo**"
        ],
        "clean_names": [
            "Pressão e Teorema de Stevin",
            "Princípio de Pascal",
            "Empuxo e Princípio de Arquimedes"
        ]
    },
    "termodinamica": {
        "key": "Termodinâmica",
        "triggers": ["termodinamica"],
        "specific_exceptions": ["1 lei", "2 lei", "primeira", "segunda", "carnot", "gases", "trabalho"],
        "options": [
            "**1ª Lei da Termodinâmica** (Calor, Trabalho e Energia Interna)",
            "**2ª Lei da Termodinâmica e Ciclo de Carnot** (Máquinas Térmicas)",
            "**Gases Perfeitos e Transformações Gasosas**"
        ],
        "clean_names": [
            "1ª Lei da Termodinâmica",
            "2ª Lei da Termodinâmica",
            "Transformações Gasosas"
        ]
    },
    "ondas": {
        "key": "Ondas e Ondulatória",
        "triggers": ["ondas", "ondulatoria"],
        "specific_exceptions": ["equacao", "fenomenos", "acustica", "interferencia", "difracao", "som", "doppler"],
        "options": [
            r"**Equação Fundamental e Tipos de Ondas** ( = \lambda \cdot f$)",
            "**Fenômenos Ondulatórios** (Reflexão, Refração, Difração e Interferência)",
            "**Acústica** (Som, Qualidades Fisiológicas e Efeito Doppler)"
        ],
        "clean_names": [
            "Equação Fundamental das Ondas",
            "Fenômenos Ondulatórios",
            "Acústica"
        ]
    },
    "optica": {
        "key": "Óptica",
        "triggers": ["optica"],
        "specific_exceptions": ["espelho", "refracao", "lente", "snell", "olho", "visao"],
        "options": [
            "**Espelhos Planos e Esféricos** (Formação de Imagens)",
            "**Refração da Luz e Lei de Snell-Descartes**",
            "**Lentes Esféricas e Instrumentos Ópticos**"
        ],
        "clean_names": [
            "Espelhos Planos e Esféricos",
            "Refração da Luz",
            "Lentes Esféricas"
        ]
    },
    "eletrostatica": {
        "key": "Eletrostática",
        "triggers": ["eletrostatica"],
        "specific_exceptions": ["coulomb", "eletrizacao", "campo eletrico", "potencial", "carga"],
        "options": [
            "**Processos de Eletrização e Carga Elétrica**",
            "**Lei de Coulomb** (Força Elétrica)",
            "**Campo Elétrico e Potencial Elétrico**"
        ],
        "clean_names": [
            "Processos de Eletrização",
            "Lei de Coulomb",
            "Campo e Potencial Elétrico"
        ]
    },
    "eletricidade": {
        "key": "Eletricidade / Eletrodinâmica",
        "triggers": ["eletricidade", "eletrodinamica"],
        "specific_exceptions": ["ohm", "resistor", "circuito", "potencia", "corrente", "gerador"],
        "options": [
            "**Corrente Elétrica e Leis de Ohm**",
            "**Associação de Resistores e Circuitos Elétricos**",
            "**Potência Elétrica e Consumo de Energia**"
        ],
        "clean_names": [
            "Leis de Ohm",
            "Associação de Resistores",
            "Potência e Energia Elétrica"
        ]
    },
    "eletromagnetismo": {
        "key": "Eletromagnetismo",
        "triggers": ["eletromagnetismo", "magnetismo"],
        "specific_exceptions": ["faraday", "lenz", "campo magnetico", "forca magnetica", "inducao"],
        "options": [
            "**Campo Magnético** (Fios, Espiras e Solenoides)",
            "**Força Magnética** (Cargas em Movimento e Regra da Mão Direita)",
            "**Indução Eletromagnética e Lei de Faraday-Lenz**"
        ],
        "clean_names": [
            "Campo Magnético",
            "Força Magnética",
            "Indução Eletromagnética"
        ]
    },
    "funcoes": {
        "key": "Funções",
        "triggers": ["funcao", "funcoes"],
        "specific_exceptions": ["afim", "quadratica", "1 grau", "2 grau", "primeiro grau", "segundo grau", "exponencial", "logaritmica", "trigonometrica", "composta", "inversa", "inorganica", "inorganicas", "organica", "organicas"],
        "options": [
            "**Funções Matemáticas** (Afim de 1º Grau ou Quadrática de 2º Grau)",
            "**Funções Inorgânicas na Química** (Ácidos, Bases, Sais e Óxidos)",
            "**Funções Orgânicas na Química** (Álcool, Cetona, Aldeído, etc.)"
        ],
        "clean_names": [
            "Funções Matemáticas (1º e 2º Grau)",
            "Funções Inorgânicas",
            "Funções Orgânicas"
        ]
    },
    "funcoes inorganicas": {
        "key": "Funções Inorgânicas",
        "triggers": ["funcoes inorganicas", "funcao inorganica", "inorganicas", "inorganica"],
        "specific_exceptions": ["reacoes", "quimica inorganica"],
        "options": [
            "**Ácidos e Bases de Arrhenius** (Ionização, dissociação e força ácida)",
            "**Sais Inorgânicos** (Neutralização total/parcial e formulação)",
            "**Óxidos e Meio Ambiente** (Classificação de óxidos e chuva ácida)",
            "**Visão Geral das 4 Funções** (Panorama condensado das 4 famílias)"
        ],
        "clean_names": [
            "Ácidos e Bases de Arrhenius",
            "Sais Inorgânicos",
            "Óxidos Inorgânicos",
            "Funções Inorgânicas"
        ]
    },
    "equacoes": {
        "key": "Equações",
        "triggers": ["equacao", "equacoes"],
        "specific_exceptions": ["1 grau", "2 grau", "primeiro grau", "segundo grau", "bhaskara", "exponencial", "logaritmica", "trigonometrica", "diferencial"],
        "options": [
            "**Equações de 1º Grau** (Fundamentos e Resolução Prática)",
            "**Equações de 2º Grau** (Fórmula de Bhaskara e Vértice)",
            "**Equações Exponenciais e Logarítmicas**"
        ],
        "clean_names": [
            "Equações de 1º Grau",
            "Equações de 2º Grau",
            "Equações Exponenciais e Logarítmicas"
        ]
    },
    "trigonometria": {
        "key": "Trigonometria",
        "triggers": ["trigonometria"],
        "specific_exceptions": ["triangulo retangulo", "ciclo", "senos", "cossenos", "arcos", "notaveis"],
        "options": [
            "**Trigonometria no Triângulo Retângulo** (Seno, Cosseno e Tangente)",
            "**Ciclo Trigonométrico e Arcos Notáveis**",
            "**Lei dos Senos e Lei dos Cossenos**"
        ],
        "clean_names": [
            "Trigonometria no Triângulo Retângulo",
            "Ciclo Trigonométrico",
            "Lei dos Senos e Cossenos"
        ]
    },
    "geometria": {
        "key": "Geometria",
        "triggers": ["geometria"],
        "specific_exceptions": ["plana", "espacial", "analitica", "pitagoras", "area", "perimetro", "volume"],
        "options": [
            "**Geometria Plana** (Áreas e Perímetros de Figuras Planas)",
            "**Geometria Espacial** (Prismas, Cilindros, Cones e Esferas)",
            "**Teorema de Pitágoras e Semelhança de Triângulos**"
        ],
        "clean_names": [
            "Geometria Plana",
            "Geometria Espacial",
            "Teorema de Pitágoras"
        ]
    },
    "matrizes": {
        "key": "Matrizes",
        "triggers": ["matriz", "matrizes"],
        "specific_exceptions": ["determinante", "sarrus", "cramer", "sistemas lineares", "multiplicacao", "inversa"],
        "options": [
            "**Operações com Matrizes** (Soma, Subtração e Multiplicação)",
            "**Determinantes** (Regra de Sarrus e Propriedades)",
            "**Sistemas Lineares** (Regra de Cramer e Escalonamento)"
        ],
        "clean_names": [
            "Operações com Matrizes",
            "Determinantes",
            "Sistemas Lineares"
        ]
    },
    "quimica organica": {
        "key": "Química Orgânica",
        "triggers": ["quimica organica"],
        "specific_exceptions": ["hidrocarboneto", "oxigenada", "nitrogenada", "isomeria", "iupac", "alcool"],
        "options": [
            "**Hidrocarbonetos e Cadeias Carbônicas** (Nomenclatura IUPAC)",
            "**Funções Orgânicas Oxigenadas e Nitrogenadas**",
            "**Isomeria Plana e Espacial**"
        ],
        "clean_names": [
            "Hidrocarbonetos",
            "Funções Orgânicas",
            "Isomeria Orgânica"
        ]
    },
    "termoquimica": {
        "key": "Termoquímica",
        "triggers": ["termoquimica"],
        "specific_exceptions": ["hess", "entalpia", "endotermica", "exotermica", "ligacao"],
        "options": [
            "**Processos Endotérmicos e Exotérmicos** (Variação de Entalpia)",
            "**Lei de Hess** (Cálculo da Variação de Entalpia)",
            "**Energia de Ligação e Entalpia de Formação**"
        ],
        "clean_names": [
            "Entalpia e Processos Térmicos",
            "Lei de Hess",
            "Energia de Ligação"
        ]
    },
    "equilibrio quimico": {
        "key": "Equilíbrio Químico",
        "triggers": ["equilibrio quimico"],
        "specific_exceptions": ["le chatelier", "kc", "kp", "ph", "poh", "deslocamento", "hidrolise"],
        "options": [
            "**Constante de Equilíbrio** ($ e $)",
            "**Deslocamento de Equilíbrio** (Princípio de Le Chatelier)",
            "**Equilíbrio Iônico da Água, pH e pOH**"
        ],
        "clean_names": [
            "Constante de Equilíbrio",
            "Princípio de Le Chatelier",
            "pH e pOH"
        ]
    },
    "eletroquimica": {
        "key": "Eletroquímica",
        "triggers": ["eletroquimica"],
        "specific_exceptions": ["pilha", "eletrolise", "nox", "redox", "daniell", "oxidacao", "reducao"],
        "options": [
            "**Pilhas e Potencial Padrão** (Pilha de Daniell e Espontaneidade)",
            "**Eletrólise Ígnea e Aquosa**",
            "**Número de Oxidação (NOX) e Reações Redox**"
        ],
        "clean_names": [
            "Pilhas Eletroquímicas",
            "Eletrólise",
            "Reações Redox e NOX"
        ]
    },
    "genetica": {
        "key": "Genética",
        "triggers": ["genetica"],
        "specific_exceptions": ["1 lei", "2 lei", "mendel", "abo", "rh", "sangue", "dna", "rna", "mutacao"],
        "options": [
            "**1ª Lei de Mendel** (Monoibridismo e Cruzamentos Genéticos)",
            "**2ª Lei de Mendel e Tipos Sanguíneos** (Sistema ABO e Fator Rh)",
            "**DNA, RNA e Síntese Proteica**"
        ],
        "clean_names": [
            "1ª Lei de Mendel",
            "2ª Lei de Mendel e Sistema ABO",
            "DNA, RNA e Síntese Proteica"
        ]
    },
    "citologia": {
        "key": "Citologia / Célula",
        "triggers": ["citologia", "celula", "celulas"],
        "specific_exceptions": ["organela", "membrana", "mitose", "meiose", "osmose", "difusao", "nucleo"],
        "options": [
            "**Organelas Celulares e suas Funções**",
            "**Membrana Plasmática e Transportes** (Osmose e Difusão)",
            "**Divisão Celular** (Mitose e Meiose)"
        ],
        "clean_names": [
            "Organelas Celulares",
            "Membrana Plasmática",
            "Divisão Celular (Mitose e Meiose)"
        ]
    },
    "ecologia": {
        "key": "Ecologia",
        "triggers": ["ecologia"],
        "specific_exceptions": ["cadeia", "trofica", "relacoes", "ciclos", "biogeoquimico", "impacto", "poluicao"],
        "options": [
            "**Cadeia Alimentar, Níveis Tróficos e Pirâmides Ecológicas**",
            "**Relações Ecológicas** (Harmônicas e Desarmônicas)",
            "**Ciclos Biogeoquímicos e Impactos Ambientais**"
        ],
        "clean_names": [
            "Cadeias Alimentares e Níveis Tróficos",
            "Relações Ecológicas",
            "Ciclos Biogeoquímicos"
        ]
    },
    "evolucao": {
        "key": "Evolução",
        "triggers": ["evolucao"],
        "specific_exceptions": ["darwin", "lamarck", "neodarwinismo", "selecao natural", "especies", "especicao"],
        "options": [
            "**Lamarckismo vs Darwinismo** (Seleção Natural)",
            "**Teoria Sintética da Evolução** (Neodarwinismo e Mutações)",
            "**Evidências da Evolução e Especiação**"
        ],
        "clean_names": [
            "Darwinismo e Seleção Natural",
            "Neodarwinismo",
            "Evidências da Evolução"
        ]
    },
    "pitagoras": {
        "key": "Pitágoras",
        "triggers": ["pitagoras"],
        "specific_exceptions": ["teorema", "triangulo", "formula", "filosofia"],
        "options": [
            r"**Teorema de Pitágoras no Triângulo Retângulo** (^2 = b^2 + c^2$)",
            "**Aplicações Práticas e Problemas com Pitágoras**",
            "**Escola Pitagórica e Filosofia Pré-Socrática**"
        ],
        "clean_names": [
            "Teorema de Pitágoras",
            "Aplicações do Teorema de Pitágoras",
            "Escola Pitagórica"
        ]
    },
    "pascal": {
        "key": "Pascal",
        "triggers": ["pascal"],
        "specific_exceptions": ["principio", "prensa", "triangulo", "binomio", "pressao"],
        "options": [
            "**Princípio de Pascal e Prensa Hidráulica** (Física / Hidrostática)",
            "**Triângulo de Pascal e Binômio de Newton** (Matemática)",
            "**Outro tópico sobre Pascal**"
        ],
        "clean_names": [
            "Princípio de Pascal",
            "Triângulo de Pascal",
            "Pascal"
        ]
    },
    "arquimedes": {
        "key": "Arquimedes",
        "triggers": ["arquimedes"],
        "specific_exceptions": ["principio", "empuxo", "flutuacao", "corpos", "hidrostatica"],
        "options": [
            "**Princípio de Arquimedes e Força de Empuxo**",
            "**Condições de Flutuação e Densidade Relativa**",
            "**Outro tópico sobre Arquimedes**"
        ],
        "clean_names": [
            "Princípio de Arquimedes e Empuxo",
            "Flutuação dos Corpos",
            "Arquimedes"
        ]
    },
    "kepler": {
        "key": "Kepler",
        "triggers": ["kepler"],
        "specific_exceptions": ["leis", "lei", "1", "2", "3", "orbitas", "areas", "periodos", "gravitacao"],
        "options": [
            "**1ª e 2ª Leis de Kepler** (Órbitas Elípticas e Lei das Áreas)",
            "**3ª Lei de Kepler** (Lei dos Períodos e Distâncias)",
            "**Gravitação Universal e Órbitas Planetárias**"
        ],
        "clean_names": [
            "Leis de Kepler",
            "3ª Lei de Kepler",
            "Gravitação e Órbitas"
        ]
    },
    "modelos atomicos": {
        "key": "Modelos Atômicos",
        "triggers": ["modelos atomicos", "atomo"],
        "specific_exceptions": ["dalton", "thomson", "rutherford", "bohr", "pauling", "distribuicao", "estrutura", "protons", "neutrons", "eletrons"],
        "options": [
            "**Evolução dos Modelos Atômicos** (Dalton, Thomson, Rutherford e Bohr)",
            "**Estrutura do Átomo** (Prótons, Nêutrons e Elétrons)",
            "**Distribuição Eletrônica e Diagrama de Linus Pauling**"
        ],
        "clean_names": [
            "Modelos Atômicos (Dalton a Bohr)",
            "Estrutura do Átomo",
            "Distribuição Eletrônica"
        ]
    },
    "tabela periodica": {
        "key": "Tabela Periódica",
        "triggers": ["tabela periodica"],
        "specific_exceptions": ["propriedades", "familias", "periodos", "metais", "raio", "eletronegatividade"],
        "options": [
            "**Organização da Tabela Periódica** (Períodos, Famílias e Grupos)",
            "**Propriedades Periódicas** (Raio Atômico, Eletronegatividade e Ionização)",
            "**Classificação dos Elementos** (Metais, Não Metais e Gases Nobres)"
        ],
        "clean_names": [
            "Organização da Tabela Periódica",
            "Propriedades Periódicas",
            "Classificação dos Elementos"
        ]
    }
}

def find_broad_topic_match(msg_clean: str):
    norm = strip_accents(msg_clean)
    # Ordena os registros com base no maior comprimento de trigger (ordem decrescente)
    # Garante que termos compostos (ex: "funcoes inorganicas") tenham precedencia sobre termos genericos ("funcoes")
    sorted_entries = sorted(
        BROAD_TOPICS_REGISTRY.values(),
        key=lambda e: max(len(t) for t in e.get("triggers", [])),
        reverse=True
    )
    for entry in sorted_entries:
        has_trigger = any(trig in norm for trig in entry["triggers"])
        if has_trigger:
            has_exception = any(exc in norm for exc in entry.get("specific_exceptions", []))
            if not has_exception:
                return entry
    return None


LEGACY_MODE_ALIASES = {
    "modo_teoria": "modo_aprender",
    "modo_microciclos": "modo_aprender",
    "modo_treino": "modo_praticar",
    "modo_desafio": "modo_praticar",
    "modo_exercicios": "modo_praticar",
    "modo_flashcards": "modo_revisar",
    "modo_memorex": "modo_resumir",
    "modo_resumo": "modo_resumir",
    "modo_socratico": "modo_menu",
    "modo_sos": "modo_resolve_questao",
    "modo_conclusao": "modo_conclusao",
}

def normalize_mode_alias(mode: str | None) -> str | None:
    if not mode:
        return mode
    return LEGACY_MODE_ALIASES.get(mode, mode)

def get_or_init_session_state(session_id: str, db_history: list) -> dict:
    if session_id in SESSION_STATES:
        st = SESSION_STATES[session_id]
        st.setdefault("pending_disambiguation", None)
        st.setdefault("disambiguation_options", None)
        st.setdefault("clean_names", None)
        st.setdefault("disambiguation_depth", 0)
        if st.get("current_mode"):
            st["current_mode"] = normalize_mode_alias(st["current_mode"])
        if st.get("pending_track"):
            st["pending_track"] = normalize_mode_alias(st["pending_track"])
        return st
        
    state = {
        "topic": None,
        "discipline": None,
        "current_mode": None,
        "pending_track": None,
        "pending_disambiguation": None,
        "disambiguation_options": None,
        "clean_names": None,
        "disambiguation_depth": 0
    }
    
    # Tenta reconstruir caso o servidor tenha reiniciado
    for msg in db_history:
        content = msg.get("content", "").strip()
        cl = content.lower()
        if msg.get("role") == "user":
            if cl in GREETINGS:
                continue
            if cl in SUPPORTED_DISCIPLINES:
                if not state["topic"]:
                    state["discipline"] = cl.capitalize()
                continue
            if cl in ALL_DISCIPLINES:
                continue
            if cl in {"1", "2", "3", "4", "5", "6", "7", "8"} or "bora ler" in cl or "aprender" in cl:
                continue
            if len(content) < 40 and cl not in ALL_DISCIPLINES and cl not in INVALID_TOPIC_WORDS and not state["topic"]:
                # Não atribui tema cegamente se não for validado
                pass
                
    SESSION_STATES[session_id] = state
    return state


# Cache em memória para o Árbitro Curricular Semântico (Solução 1 - LLM-First)
# Chaves são strings normalizadas exatas. Zero colisão de substrings!
# Cache em memória para o Árbitro Curricular Semântico (Solução 1 - LLM-First)
# Chaves são strings normalizadas exatas. Zero colisão de substrings!
SEMANTIC_TOPIC_CACHE: dict = {
    "funcoes": {
        "desambiguar": True,
        "motivo": "REGRA_1",
        "disciplina_identificada": "Interdisciplinar",
        "tema_raiz": "Funções",
        "opcoes": [
            "**Funções Matemáticas** (Álgebra: afim, quadrática, exponencial, logarítmica e gráficos)",
            "**Funções Inorgânicas** (Química: ácidos, bases, sais e óxidos de Arrhenius)",
            "**Funções Orgânicas** (Química: hidrocarbonetos, álcoois, cetonas, ácidos carboxílicos)"
        ],
        "clean_names": [
            "Funções Matemáticas",
            "Funções Inorgânicas",
            "Funções Orgânicas"
        ]
    },
    "funcoes matematicas": {
        "desambiguar": True,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Matemática",
        "tema_raiz": "Funções Matemáticas",
        "opcoes": [
            "**Função Afim / 1º Grau** (Taxa de variação, coeficientes angular e linear, gráficos de reta)",
            "**Função Quadrática / 2º Grau** (Parábolas, raízes por Bhaskara, ponto de máximo e mínimo)",
            "**Funções Exponencial e Logarítmica** (Crescimento/decaimento exponencial, propriedades e gráficos)",
            "**Introdução e Conceito de Função** (Noção de relação, domínio, contradomínio e imagem)"
        ],
        "clean_names": [
            "Função Afim",
            "Função Quadrática",
            "Função Exponencial e Logarítmica",
            "Conceito de Função"
        ]
    },
    "funcoes quimica": {
        "desambiguar": True,
        "fora_do_escopo": False,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Química",
        "tema_raiz": "Funções Químicas",
        "opcoes": [
            "**Ácidos de Arrhenius** (Ionização em água, força ácida, hidrácidos e oxiácidos)",
            "**Bases de Arrhenius** (Dissociação iônica, solubilidade, grau de dissociação e hidróxidos)",
            "**Sais Inorgânicos** (Reação de neutralização, formulação e nomenclatura)",
            "**Óxidos e Meio Ambiente** (Classificação: ácidos, básicos, neutros, anfóteros e chuva ácida)"
        ],
        "clean_names": [
            "Ácidos de Arrhenius",
            "Bases de Arrhenius",
            "Sais Inorgânicos",
            "Óxidos Inorgânicos"
        ]
    },
    "funcoes quimicas": {
        "desambiguar": True,
        "fora_do_escopo": False,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Química",
        "tema_raiz": "Funções Químicas",
        "opcoes": [
            "**Ácidos de Arrhenius** (Ionização em água, força ácida, hidrácidos e oxiácidos)",
            "**Bases de Arrhenius** (Dissociação iônica, solubilidade, grau de dissociação e hidróxidos)",
            "**Sais Inorgânicos** (Reação de neutralização, formulação e nomenclatura)",
            "**Óxidos e Meio Ambiente** (Classificação: ácidos, básicos, neutros, anfóteros e chuva ácida)"
        ],
        "clean_names": [
            "Ácidos de Arrhenius",
            "Bases de Arrhenius",
            "Sais Inorgânicos",
            "Óxidos Inorgânicos"
        ]
    },
    "funcao quimica": {
        "desambiguar": True,
        "fora_do_escopo": False,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Química",
        "tema_raiz": "Funções Químicas",
        "opcoes": [
            "**Ácidos de Arrhenius** (Ionização em água, força ácida, hidrácidos e oxiácidos)",
            "**Bases de Arrhenius** (Dissociação iônica, solubilidade, grau de dissociação e hidróxidos)",
            "**Sais Inorgânicos** (Reação de neutralização, formulação e nomenclatura)",
            "**Óxidos e Meio Ambiente** (Classificação: ácidos, básicos, neutros, anfóteros e chuva ácida)"
        ],
        "clean_names": [
            "Ácidos de Arrhenius",
            "Bases de Arrhenius",
            "Sais Inorgânicos",
            "Óxidos Inorgânicos"
        ]
    },
    "quimica inorganica": {
        "desambiguar": True,
        "fora_do_escopo": False,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Química",
        "tema_raiz": "Funções Químicas",
        "opcoes": [
            "**Ácidos de Arrhenius** (Ionização em água, força ácida, hidrácidos e oxiácidos)",
            "**Bases de Arrhenius** (Dissociação iônica, solubilidade, grau de dissociação e hidróxidos)",
            "**Sais Inorgânicos** (Reação de neutralização, formulação e nomenclatura)",
            "**Óxidos e Meio Ambiente** (Classificação: ácidos, básicos, neutros, anfóteros e chuva ácida)"
        ],
        "clean_names": [
            "Ácidos de Arrhenius",
            "Bases de Arrhenius",
            "Sais Inorgânicos",
            "Óxidos Inorgânicos"
        ]
    },
    "funcoes inorganicas": {
        "desambiguar": True,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Química",
        "tema_raiz": "Funções Inorgânicas",
        "opcoes": [
            "**Ácidos de Arrhenius** (Ionização em água, força ácida, hidrácidos e oxiácidos)",
            "**Bases de Arrhenius** (Dissociação iônica, solubilidade, grau de dissociação e hidróxidos)",
            "**Sais Inorgânicos** (Reação de neutralização, formulação e nomenclatura)",
            "**Óxidos e Meio Ambiente** (Classificação: ácidos, básicos, neutros, anfóteros e chuva ácida)"
        ],
        "clean_names": [
            "Ácidos de Arrhenius",
            "Bases de Arrhenius",
            "Sais Inorgânicos",
            "Óxidos Inorgânicos"
        ]
    },
    "cinematica": {
        "desambiguar": True,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Física",
        "tema_raiz": "Cinemática",
        "opcoes": [
            "**Movimento Uniforme (MU)** (Velocidade constante, função horária da posição e gráficos s x t)",
            "**Movimento Uniformemente Variado (MUV)** (Aceleração constante, função da velocidade e Torricelli)",
            "**Queda Livre e Lançamento Vertical** (Gravidade, tempo de queda, altura máxima e alcance)",
            "**Movimento Circular Uniforme (MCU)** (Velocidade angular, período, frequência e aceleração centrípeta)"
        ],
        "clean_names": [
            "Movimento Uniforme",
            "Movimento Uniformemente Variado",
            "Queda Livre",
            "Movimento Circular Uniforme"
        ]
    },
    "acidos de arrhenius": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Ácidos de Arrhenius"},
    "bases de arrhenius": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Bases de Arrhenius"},
    "sais inorganicos": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Sais Inorgânicos"},
    "oxidos inorganicos": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Óxidos Inorgânicos"},
    "funcao afim": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Matemática", "tema_formatado": "Função Afim (1º Grau)"},
    "funcao quadratica": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Matemática", "tema_formatado": "Função Quadrática (2º Grau)"},
    "funcao exponencial e logaritmica": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Matemática", "tema_formatado": "Funções Exponencial e Logarítmica"},
    "conceito de funcao": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Matemática", "tema_formatado": "Introdução e Conceito de Função"},
    "movimento uniforme": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Movimento Uniforme (MU)"},
    "movimento uniformemente variado": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Movimento Uniformemente Variado (MUV)"},
    "queda livre": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Queda Livre e Lançamento Vertical"},
    "movimento circular uniforme": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Movimento Circular Uniforme (MCU)"},
    "funcoes organicas": {
        "desambiguar": True,
        "fora_do_escopo": False,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Química",
        "tema_raiz": "Funções Orgânicas",
        "opcoes": [
            "**Hidrocarbonetos** (Alcanos, alcenos, alcinos, alcadienos, ciclanos e aromáticos)",
            "**Funções Oxigenadas** (Álcoois, fenóis, éteres, aldeídos, cetonas, ácidos carboxílicos e ésteres)",
            "**Funções Nitrogenadas e Outras** (Aminas, amidas, nitrilas, nitrocompostos e haletos orgânicos)"
        ],
        "clean_names": [
            "Hidrocarbonetos",
            "Funções Oxigenadas",
            "Funções Nitrogenadas"
        ]
    },
    "hidrocarbonetos": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Hidrocarbonetos"},
    "funcoes oxigenadas": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Funções Orgânicas Oxigenadas"},
    "funcoes nitrogenadas": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Química", "tema_formatado": "Funções Orgânicas Nitrogenadas"},
    "leis de newton": {
        "desambiguar": True,
        "fora_do_escopo": False,
        "motivo": "REGRA_2",
        "disciplina_identificada": "Física",
        "tema_raiz": "Leis de Newton",
        "opcoes": [
            "**Primeira Lei de Newton (Inércia)** (Conceito de inércia, referencial inercial e equilíbrio estático/dinâmico)",
            "**Segunda Lei de Newton (Princípio Fundamental da Dinâmica)** (Força resultante F = m·a, peso, normal, tração e atrito)",
            "**Terceira Lei de Newton (Ação e Reação)** (Pares de ação e reação, propriedades vetoriais e aplicações práticas)"
        ],
        "clean_names": [
            "Primeira Lei de Newton",
            "Segunda Lei de Newton",
            "Terceira Lei de Newton"
        ]
    },
    "primeira lei de newton": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Primeira Lei de Newton (Inércia)"},
    "segunda lei de newton": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Segunda Lei de Newton"},
    "terceira lei de newton": {"desambiguar": False, "fora_do_escopo": False, "motivo": "ESPECIFICO", "disciplina_identificada": "Física", "tema_formatado": "Terceira Lei de Newton (Ação e Reação)"}
}
SEMANTIC_TOPIC_CACHE["funcoes|matematica"] = SEMANTIC_TOPIC_CACHE["funcoes matematicas"]
SEMANTIC_TOPIC_CACHE["funcoes matematica"] = SEMANTIC_TOPIC_CACHE["funcoes matematicas"]
SEMANTIC_TOPIC_CACHE["funcao matematica"] = SEMANTIC_TOPIC_CACHE["funcoes matematicas"]
SEMANTIC_TOPIC_CACHE["funcoes|quimica"] = SEMANTIC_TOPIC_CACHE["funcoes quimicas"]

async def analyze_topic_curricular_rules(term: str, current_discipline: str = None) -> dict:
    """
    ÁRBITRO CURRICULAR SEMÂNTICO (Solução 1 - LLM-First):
    Analisa o termo solicitado pelo estudante sob as 2 REGRAS INDEPENDENTES de desambiguação via DeepSeek:
    - REGRA 1 (Interdisciplinar): O termo abrange disciplinas escolares diferentes (ex: Física vs Matemática).
    - REGRA 2 (Densidade Curricular): O tema abrange 3 ou mais capítulos de livro didático (>= 3 capítulos), ainda que na mesma matéria.
    """
    norm_term = strip_accents(term).strip().lower()
    norm_disc_ctx = strip_accents(current_discipline).strip().lower() if current_discipline else None
    cache_key = f"{norm_term}|{norm_disc_ctx}" if norm_disc_ctx else norm_term
    
    if cache_key in SEMANTIC_TOPIC_CACHE:
        return SEMANTIC_TOPIC_CACHE[cache_key]
    if norm_term in SEMANTIC_TOPIC_CACHE:
        return SEMANTIC_TOPIC_CACHE[norm_term]
    # Tolerância a pequenos erros de digitação nas chaves do cache (ex: "funcoes matemaica" -> "funcoes matematicas")
    if len(norm_term) >= 6:
        best_k, best_score = None, 0.0
        for k in SEMANTIC_TOPIC_CACHE:
            if "|" in k:
                continue
            score = SequenceMatcher(None, norm_term, k).ratio()
            if score > best_score:
                best_k, best_score = k, score
        if best_k and best_score >= 0.87:
            return SEMANTIC_TOPIC_CACHE[best_k]

    try:
        active_subjects_str = ", ".join(AVAILABLE_SUBJECTS_LIST)
        active_subjects_union = " | ".join(f'"{s}"' for s in AVAILABLE_SUBJECTS_LIST)
        context_discipline = f"\nContexto informado pelo estudante: A disciplina de estudo é {current_discipline} (Regra 1 interdisciplinar já delimitada nesta matéria)." if current_discipline else ""
        prompt = f"""Você é o Analista Curricular Sênior da Educamob. No momento, o acervo ativo da Educamob no banco de dados atende ESTRITAMENTE estas disciplinas: {active_subjects_str}.{context_discipline}

Sua missão é inspecionar o assunto de estudo solicitado pelo estudante e verificar o enquadramento curricular:

1. FORA DO ESCOPO (Disciplinas ainda não presentes na lista [{active_subjects_str}]):
Se o estudante pedir uma disciplina ou tema que NÃO pertença a [{active_subjects_str}] (ex: Língua Portuguesa, Gramática, Literatura, Redação, Filosofia, Sociologia, Inglês, Espanhol, Artes, ou Biologia de Ensino Médio caso "Biologia" não esteja listada acima):
- Nota importante 1: Tópicos de Ciências do Ensino Fundamental (como células, seres vivos, corpo humano, ecologia básica, astronomia e matéria/energia do 5º ao 9º ano) pertencem à disciplina "Ciências" (dentro do escopo). Porém, se o estudante pedir explicitamente a matéria "Biologia" ou um tema exclusivo de Biologia avançada não coberto em Ciências (e "Biologia" não estiver na lista ativa), classifique como fora do escopo!
- Nota importante 2: As disciplinas "História" e "Geografia" FAZEM PARTE do acervo ativo da Educamob (dentro do escopo)! Todo tema de História (Antiguidade, Idade Média, Brasil Colonial, Império, República, Revoluções, Guerras Mundiais, Guerra Fria, etc.) pertence a "História" e todo tema de Geografia (Cartografia, Clima, Relevo, Urbanização, População, Geopolítica, Globalização, etc.) pertence a "Geografia".
Retorne ESTRITAMENTE em formato JSON:
{{
  "desambiguar": false,
  "fora_do_escopo": true,
  "disciplina_identificada": "Nome real da disciplina fora do escopo (ex: Língua Portuguesa, Filosofia, Biologia, etc.)",
  "tema_formatado": "Nome do assunto"
}}

2. DENTRO DO ESCOPO ({active_subjects_str}):
Verifique se ativa o PROTOCOLO DE DESAMBIGUAÇÃO antes de apresentar o Menu de Trilhas de 6 opções:
- REGRA 1 (Interdisciplinar): O termo abrange disciplinas escolares diferentes da Educação Básica (ex: 'Bernoulli' envolve Física e Matemática; 'Newton' isolado envolve Física e Matemática; 'Funções' envolve Matemática e Química; 'Ondas' envolve Física e Ciências).
  * REGRA DE OURO SOBRE CÁLCULO 1: 'Cálculo 1' só deve ser considerado na REGRA 1 se o estudante usar termos exclusivos do ensino superior (ex: Limites, Derivadas, Integrais, Teorema Fundamental do Cálculo). Tópicos clássicos de Física, Química ou Matemática da Educação Básica (como Leis de Newton, Segunda Lei de Newton, Cinemática, Termodinâmica, Óptica) NUNCA colidem com Cálculo 1 na REGRA 1 e pertencem estritamente à sua disciplina escolar (ex: Física).
- REGRA 2 (Densidade Curricular): O tema abrange 3 OU MAIS capítulos diferentes de livro didático da BNCC, ainda que sejam da MESMA matéria (ex: 'Funções Químicas' ou 'Funções Inorgânicas' abrange Ácidos/Bases, Sais e Óxidos na Química; 'Cinemática' abrange MU, MUV, Queda Livre e Lançamentos na Física; 'Eletromagnetismo' abrange Campo, Força Magnética e Indução; 'Reações Orgânicas' abrange Substituição, Adição e Eliminação).
- DIRETRIZ DE FOLHAS ATÔMICAS PARA REGRA 2: Quando desambiguar um tema da mesma matéria (REGRA_2), as opções geradas DEVEM ser sempre capítulos finais específicos (folhas atômicas de 1 único capítulo, prontas para iniciar o estudo, como "Probabilidade de Eventos Dependentes e Independentes" ou "Ácidos de Arrhenius"), NUNCA sub-áreas amplas que precisem de outra desambiguação!

SE ATIVAR A REGRA 1 OU REGRA 2:
Retorne ESTRITAMENTE em formato JSON:
{{
  "desambiguar": true,
  "fora_do_escopo": false,
  "motivo": "REGRA_1" | "REGRA_2" | "AMBAS",
  "disciplina_identificada": {active_subjects_union} | "Interdisciplinar",
  "tema_raiz": "Nome do conceito amplo",
  "opcoes": [
    "**Opção 1** (detalhes didáticos do capítulo específico)",
    "**Opção 2** (detalhes didáticos do capítulo específico)",
    "**Opção 3** (detalhes didáticos do capítulo específico)"
  ],
  "clean_names": [
    "Nome Canônico do Capítulo 1",
    "Nome Canônico do Capítulo 2",
    "Nome Canônico do Capítulo 3"
  ]
}}

SE FOR TÓPICO ATÔMICO E ESPECÍFICO DE 1 ÚNICO CAPÍTULO:
{{
  "desambiguar": false,
  "fora_do_escopo": false,
  "motivo": "ESPECIFICO",
  "disciplina_identificada": {active_subjects_union},
  "tema_formatado": "Nome canônico corrigido do assunto específico"
}}"""

        response = await deepinfra_client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V4-Flash-0731",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f'Termo informado pelo estudante: "{term}"'}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        res_json = json.loads(response.choices[0].message.content)
        SEMANTIC_TOPIC_CACHE[cache_key] = res_json
        return res_json
    except Exception as e:
        print(f"Aviso no Analista Curricular (fallback seguro): {e}")
        return {"desambiguar": False, "motivo": "FALLBACK", "tema_formatado": term.capitalize()}

def is_holistic_selection(text: str) -> bool:
    """Detecta se o aluno respondeu querendo ver 'todos', 'tudo', 'ambos' ou pedindo para comecar do inicio na desambiguacao."""
    t = text.strip().lower()
    t_clean = re.sub(r'[^\w\s]', '', t)
    holistic_patterns = [
        r'^\s*(?:todos?|todas?|tudo|ambos|ambas|qualquer|completo|geral)\s*$',
        r'\b(?:quero|gostaria\s+de|prefiro|vamos|ver|estudar|focar|aprofundar|aprender|saber|passar\s+por)\s+(?:em\s+|de\s+)?(?:todos?|todas?|tudo|ambos|cada\s+um)\b',
        r'\b(?:todos\s+os\s+temas|todos\s+os\s+focos|todas\s+as\s+opcoes|todas\s+as\s+opções|tudo\s+junto|todos\s+eles)\b',
        r'\b(?:tanto\s+faz|voce\s+decide|qual\s+voce\s+recomenda|pode\s+ser\s+qualquer|o\s+que\s+achar\s+melhor)\b'
    ]
    return any(re.search(p, t_clean) for p in holistic_patterns)

def is_question_submission(text: str) -> bool:
    """Detecta se o aluno enviou uma questao completa (com alternativas ou dados de exercicio) para ser resolvida."""
    t = text.strip()
    has_alternatives = bool(re.search(r'[a-eA-E][\)\.][\s\S]+?[b-eB-E][\)\.]', t))
    has_question_cues = bool(re.search(
        r'\b(enem|fuvest|unicamp|vunesp|fgv|ita|ime|uerj|puc|ufmg|ufrj|mackenzie|cefet|ifsp|ifba|unb)\b|'
        r'\b(calcule|determine|assinale|encontre|resolva|obtenha|julgue|qual\s+e\s+o\s+valor|qual\s+a\s+velocidade|qual\s+a\s+fração)\b',
        t, re.IGNORECASE
    ))
    if has_alternatives:
        return True
    if has_question_cues and re.search(r'\d+\s*(?:m|cm|mm|kg|g|s|h|m/s|km/h|N|J|W|cal|Pa|V|A|\$|%|°C|mol)', t):
        return True
    return False

async def resolve_active_mode_and_topic(
    session_id: str, 
    db_history: list, 
    current_message: str,
    has_image: bool = False,
    extracted_text: str = ""
):
    state = get_or_init_session_state(session_id, db_history)
    msg_clean = current_message.strip().lower()
    
    # 0.0 Retomada de trilha pausada por envio prévio de imagem
    if state.get("paused_track") and not has_image:
        if any(w in msg_clean for w in ["voltar", "retomar", "continuar", "voltar pro treino", "voltar para o treino", "continuar o treino", "voltar para onde estavamos", "continuar exercicios", "continuar exercícios", "seguir"]):
            paused = state.pop("paused_track")
            state["current_mode"] = paused["mode"]
            state["resuming_track"] = True
            save_session_states()
            return paused["mode"], state.get("topic"), state

    # 0.05 Tratamento Inteligente para envio direto de QUESTÃO EM TEXTO (vestibular, concurso ou tarefa escolar)
    if not has_image and is_question_submission(current_message):
        current_active = state.get("current_mode", "modo_acolhida")
        # Se o aluno colou uma questão com alternativas fora de um modo ativo de questão:
        if current_active in {"modo_acolhida", "modo_menu", "modo_novo_assunto"}:
            if not state.get("topic"):
                first_line = current_message.split("\n")[0][:80].strip()
                try:
                    analysis = await analyze_topic_curricular_rules(first_line, current_discipline=state.get("discipline"))
                    disc_id = analysis.get("disciplina_identificada")
                    if disc_id and not state.get("discipline"):
                        state["discipline"] = disc_id
                    state["topic"] = analysis.get("tema_formatado") or first_line or "Questão Enviada"
                except Exception:
                    state["topic"] = "Questão Enviada"
            state["current_mode"] = "modo_resolve_questao"
            state["pending_track"] = None
            save_session_states()
            return "modo_resolve_questao", state.get("topic"), state

    # 0.1 Tratamento Híbrido Inteligente para envio de imagem em qualquer momento
    if has_image:
        current_active = state.get("current_mode", "modo_acolhida")
        
        # Se estava em modo ativo de estudo (modo_praticar, modo_aprender, modo_revisar):
        if current_active in {"modo_praticar", "modo_aprender", "modo_revisar"}:
            state["paused_track"] = {
                "mode": current_active,
                "topic": state.get("topic"),
                "discipline": state.get("discipline")
            }
            state["current_mode"] = "modo_resolve_questao"
            state["from_image_interruption"] = True
            state["pending_track"] = None
            save_session_states()
            return "modo_resolve_questao", state.get("topic"), state
            
        # Se estava fora de estudo ativo (modo_menu, modo_acolhida, modo_novo_assunto, modo_conclusao):
        else:
            # Se ainda não definiu o tema e temos texto da imagem, deduz o tema da questão!
            if not state.get("topic") and extracted_text:
                clean_snippet = extracted_text.split("\n")[0][:60].strip()
                try:
                    analysis = await analyze_topic_curricular_rules(clean_snippet, current_discipline=state.get("discipline"))
                    disc_id = analysis.get("disciplina_identificada")
                    if disc_id and not state.get("discipline"):
                        state["discipline"] = disc_id
                    state["topic"] = analysis.get("tema_formatado") or clean_snippet or "Exercício da Imagem"
                except Exception:
                    state["topic"] = clean_snippet or "Exercício da Imagem"
            
            state["current_mode"] = "modo_resolve_questao"
            state["pending_disambiguation"] = None
            state["disambiguation_options"] = None
            state["clean_names"] = None
            state["pending_track"] = None
            save_session_states()
            return "modo_resolve_questao", state.get("topic"), state

    # 0.2 Interrupção/Pausa em trilhas em andamento (Microciclos, Praticar, Revisar)
    if state.get("current_mode") in {"modo_aprender", "modo_praticar", "modo_revisar"} and any(w in msg_clean for w in PAUSE_TRIGGERS):
        # NÃO fecha com relatório parcial. Mantém no modo para a IA acolher a pausa e oferecer o Menu de Trilhas
        return state["current_mode"], state["topic"], state

    # 1. Comando explícito de finalizar/encerrar sessão (sem colidir com números de desambiguação)
    if msg_clean in {"finalizar", "encerrar", "encerrar sessao", "encerrar sessão", "finalizar sessao", "finalizar sessão"}:
        state["current_mode"] = "modo_conclusao"
        save_session_states()
        return "modo_conclusao", state["topic"], state

    # 1.5 Tratamento PRIORITÁRIO de Desambiguação de Tema Pendente (Com Desambiguação em Cascata):
    if state.get("pending_disambiguation"):
        clean_names = state.get("clean_names") or []
        selected_topic = None
        
        # 1.5.0 Desistência ou Troca de Matéria durante a desambiguação
        if any(trigger in msg_clean for trigger in CHANGE_TOPIC_TRIGGERS) or any(w in msg_clean for w in ["mudar a materia", "trocar de assunto", "outro assunto", "outra materia", "mudar de materia", "mudar materia", "mudar assunto"]):
            state["pending_disambiguation"] = None
            state["disambiguation_options"] = None
            state["clean_names"] = None
            state["topic"] = None
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state
            
        # 1.5.0b Resposta Holística / Cobrir todos os temas (ex: "todos", "todas", "tudo", "gostaria de me aprofundar em todos", "tanto faz")
        if is_holistic_selection(msg_clean):
            # O aluno deseja estudar o tema como um todo. Seleciona a opção 1 (a fundação/base do assunto) ou o tema principal
            selected_topic = clean_names[0] if clean_names else state.get("pending_disambiguation")

        # 1.5.1 Escolha numérica direta (1 a 5) com blindagem contra colisão de trilhas
        for idx in range(min(5, len(clean_names))):
            num_str = str(idx + 1)
            emoji_str = f"{idx + 1}\ufe0f\u20e3"
            if msg_clean in {num_str, emoji_str} or msg_clean == f"{num_str}." or (msg_clean.startswith(f"{num_str}.") and not any(w in msg_clean for w in ["aprender", "praticar", "flashcards", "resumo", "finalizar"])):
                selected_topic = clean_names[idx]
                break
        
        # 1.5.2 Casamento por texto e tolerância a erros de digitação (ex: "matemaica" -> "Funções Matemáticas")
        if not selected_topic:
            norm_msg_input = strip_accents(msg_clean).strip()
            parent_words = set(w for w in re.findall(r"[a-z0-9]+", strip_accents(state.get("pending_disambiguation") or "")) if len(w) > 2)
            def is_parent_word(w: str) -> bool:
                return any(is_fuzzy_word_match(w, pw, 0.72) or (len(w) >= 4 and len(pw) >= 4 and w[:4] == pw[:4]) for pw in parent_words)
            stopwords = {"quero", "estudar", "sobre", "opcao", "assunto", "materia", "tema", "foco", "caminho", "tipo", "tipos", "para", "como", "das", "dos", "nas", "nos", "uma", "uns", "por"}
            user_distinct_words = [w for w in re.findall(r"[a-z0-9]+", norm_msg_input) if len(w) > 2 and not is_parent_word(w) and w not in stopwords]

            # A) Casamento exato ou fuzzy da frase inteira contra clean_names
            for name in clean_names:
                norm_name = strip_accents(name)
                if norm_name == norm_msg_input or norm_name in norm_msg_input:
                    selected_topic = name
                    break
                if len(norm_msg_input) >= 5 and SequenceMatcher(None, norm_msg_input, norm_name).ratio() >= 0.82:
                    selected_topic = name
                    break

            # B) Casamento por palavras distintivas (com tolerância a typos como "matemaica" -> "matematicas") contra clean_names
            if not selected_topic and user_distinct_words:
                matched_clean = []
                for idx_c, name in enumerate(clean_names):
                    norm_name = strip_accents(name)
                    name_words = [w for w in re.findall(r"[a-z0-9]+", norm_name) if len(w) > 2 and not is_parent_word(w)]
                    # Todos os termos distintivos digitados pelo usuário devem bater com a opção (evita que "funções da linguagem" case com algo)
                    if name_words and all(any(is_fuzzy_word_match(uw, nw, 0.78) for nw in name_words) for uw in user_distinct_words):
                        matched_clean.append(name)
                if len(matched_clean) == 1:
                    selected_topic = matched_clean[0]

            # C) Se não casou em clean_names, verifica nas descrições completas (disambiguation_options, ex: "física", "química", "1 grau", "bhaskara")
            if not selected_topic and user_distinct_words:
                raw_opts = state.get("disambiguation_options") or []
                matched_by_opt = []
                for idx_o, opt_text in enumerate(raw_opts):
                    if idx_o >= len(clean_names):
                        break
                    opt_words = [w for w in re.findall(r"[a-z0-9]+", strip_accents(opt_text)) if len(w) > 2 and not is_parent_word(w)]
                    if opt_words and all(any(is_fuzzy_word_match(uw, ow, 0.80) for ow in opt_words) for uw in user_distinct_words):
                        matched_by_opt.append(clean_names[idx_o])
                if len(matched_by_opt) == 1:
                    selected_topic = matched_by_opt[0]
                elif len(matched_by_opt) > 1:
                    # Ex: o usuário digitou "química" em "Funções" (que aparece em Inorgânicas e Orgânicas) -> combina o tema-pai + qualificador
                    selected_topic = f"{state.get('pending_disambiguation')} {msg_clean}"


        # 1.5.3 Processamento do tema selecionado com DESAMBIGUAÇÃO EM CASCATA (Teto Máximo = 2 níveis)
        if selected_topic:
            current_depth = state.get("disambiguation_depth", 1)
            prev_reason = state.get("disambiguation_reason", "REGRA_1")
            had_discipline_in_level1 = bool(state.get("discipline"))
            analysis = await analyze_topic_curricular_rules(selected_topic, current_discipline=state.get("discipline"))
            
            disc_id = analysis.get("disciplina_identificada")
            norm_disc = strip_accents(disc_id) if disc_id else None
            norm_supported = {strip_accents(d) for d in SUPPORTED_DISCIPLINES}

            if norm_disc and norm_disc in norm_supported and not state.get("discipline"):
                state["discipline"] = disc_id

            # Guardrail contra temas fora do escopo selecionados
            norm_non_supported = {strip_accents(d) for d in NON_SUPPORTED_DISCIPLINES}
            if norm_disc and norm_disc in norm_non_supported:
                state["topic"] = None
                state["pending_disambiguation"] = None
                state["disambiguation_options"] = None
                state["clean_names"] = None
                state["disambiguation_depth"] = 0
                state["disambiguation_reason"] = None
                state["discipline"] = None
                state["out_of_scope_discipline"] = SUBJECT_DISPLAY_MAP.get(norm_disc, disc_id)
                state["current_mode"] = "modo_acolhida"
                save_session_states()
                return "modo_acolhida", None, state

            # Só permite desambiguação de Nível 2 se current_depth < 2 E se o Nível 1 foi estritamente interdisciplinar (sem disciplina definida no Nível 1)
            if analysis.get("desambiguar") and current_depth < 2 and prev_reason in {"REGRA_1", "AMBAS"} and not had_discipline_in_level1:
                state["pending_disambiguation"] = analysis.get("tema_raiz") or selected_topic.capitalize()
                state["disambiguation_options"] = analysis.get("opcoes")
                state["clean_names"] = analysis.get("clean_names")
                state["disambiguation_depth"] = current_depth + 1
                state["disambiguation_reason"] = analysis.get("motivo") or "REGRA_2"
                state["current_mode"] = "modo_acolhida"
                save_session_states()
                return "modo_acolhida", None, state
            
            # Se a opção escolhida for ATÔMICA ou atingiu o Nível 2 máximo: destrava o Super Menu!
            _raw_cname = (analysis.get("tema_formatado") or selected_topic).strip()
            canonical_name = (_raw_cname[0].upper() + _raw_cname[1:]) if _raw_cname else selected_topic
            state["topic"] = canonical_name
            state["pending_disambiguation"] = None
            state["disambiguation_options"] = None
            state["clean_names"] = None
            state["disambiguation_depth"] = 0
            state["disambiguation_reason"] = None
            
            if state.get("pending_track"):
                chosen = state["pending_track"]
                state["current_mode"] = chosen
                state["pending_track"] = None
                state["just_selected_track"] = True
                save_session_states()
                return chosen, state["topic"], state
            else:
                state["current_mode"] = "modo_menu"
                save_session_states()
                return "modo_menu", state["topic"], state
        else:
            # Verifica se o estudante clicou em uma trilha do menu (ex: "4. Resumo", "praticar") durante a desambiguação
            pre_track = None
            if msg_clean.startswith("1️⃣") or msg_clean.startswith("1.") or msg_clean in {"aprender", "microciclos", "bora ler"}:
                pre_track = "modo_aprender"
            elif msg_clean.startswith("2️⃣") or msg_clean.startswith("2.") or msg_clean in {"praticar", "exercicios", "exercícios", "treino", "desafio"}:
                pre_track = "modo_praticar"
            elif msg_clean.startswith("3️⃣") or msg_clean.startswith("3.") or msg_clean in {"revisar", "flashcards", "flashcard"}:
                pre_track = "modo_revisar"
            elif msg_clean.startswith("4️⃣") or msg_clean.startswith("4.") or msg_clean in {"resumir", "memorex", "resumo"}:
                pre_track = "modo_resumir"
            elif msg_clean.startswith("5️⃣") or msg_clean.startswith("5.") or "enviar questao" in msg_clean or "enviar questão" in msg_clean or "resolve questao" in msg_clean or "resolve questão" in msg_clean or "resolver questao" in msg_clean or "resolver questão" in msg_clean:
                pre_track = "modo_resolve_questao"
            elif msg_clean.startswith("6️⃣") or msg_clean.startswith("6.") or msg_clean in {"finalizar", "encerrar"}:
                pre_track = "modo_conclusao"

            if pre_track:
                if pre_track == "modo_conclusao":
                    state["pending_disambiguation"] = None
                    state["current_mode"] = "modo_conclusao"
                    state["just_selected_track"] = True
                    save_session_states()
                    return "modo_conclusao", state.get("topic"), state
                # Registra a trilha desejada e mantém a desambiguação ativa para o aluno escolher o subtema
                state["pending_track"] = pre_track
                state["current_mode"] = "modo_acolhida"
                save_session_states()
                return "modo_acolhida", None, state

            # O texto digitado NÃO casou com as opções da desambiguação anterior (ex: o aluno digitou um novo termo como "funções da linguagem" ou "funções quimica").
            # Limpa a desambiguação pendente e faz FALLTHROUGH para o Step 5 (Árbitro Curricular Semântico) avaliar a nova mensagem sem loop!
            state["pending_disambiguation"] = None
            state["disambiguation_options"] = None
            state["clean_names"] = None
            state["disambiguation_depth"] = 0
            save_session_states()

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
            # Se escolheu uma opção numérica de estudo (1 a 6), deixamos fluir para o seletor de trilhas abaixo
            elif any(msg_clean.startswith(num) for num in ["1", "2", "3", "4", "5", "6"]):
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
        # Detecta nome de disciplina (mesmo com erro de digitação como "matemaica", "quimca", "fisicaa")
        fuzzy_disc = match_discipline_fuzzy(msg_clean)
        if fuzzy_disc:
            norm_supported_disc = {strip_accents(d) for d in SUPPORTED_DISCIPLINES}
            state["topic"] = None
            if fuzzy_disc not in norm_supported_disc:
                state["discipline"] = None
                state["out_of_scope_discipline"] = SUBJECT_DISPLAY_MAP.get(fuzzy_disc, fuzzy_disc.capitalize())
            else:
                state["discipline"] = SUBJECT_DISPLAY_MAP.get(fuzzy_disc, fuzzy_disc.capitalize())
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        digits = {"1", "2", "3", "4", "5", "6", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"}
        if msg_clean in GREETINGS or msg_clean in INVALID_TOPIC_WORDS or (len(msg_clean) < 3 and msg_clean not in digits and not any(msg_clean.startswith(d) for d in ["1.", "2.", "3.", "4.", "5.", "6."])):
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

    # 4. Seleção do Menu Canônico de 6 Trilhas
    target_mode = None
    is_short_choice = len(msg_clean) <= 75
    current_active_mode = state.get("current_mode")
    in_active_study = current_active_mode in {"modo_aprender", "modo_praticar", "modo_revisar", "modo_resolve_questao"}

    # 4.1. Retorno explícito ao Menu Canônico de Trilhas
    if is_short_choice and msg_clean in {"menu", "ver menu", "voltar", "voltar menu", "mudar trilha", "mudar de trilha", "trilhas", "menu de trilhas", "trocar modo", "trocar de modo", "opcoes", "opções"}:
        state["current_mode"] = "modo_menu"
        state["pending_track"] = None
        state["just_selected_track"] = False
        save_session_states()
        return "modo_menu", state["topic"], state

    # 4.2. Reconhecimento de escolha de trilha
    if is_short_choice:
        if in_active_study:
            # Em modo de estudo pedagógico ativo (microciclos, questões, flashcards ou resolução de dúvidas):
            # Dígitos numéricos isolados (1, 2, 3, 4, 5, 6), letras (a, b, c, d, e) e valores de cálculo
            # são SEMPRE respostas do estudante às perguntas e NÃO escolhas de menu.
            # Apenas comandos ou nomes explícitos de trilha trocam de modo.
            if (
                msg_clean in {"1️⃣", "1️⃣ aprender", "1. aprender", "aprender", "aprender microciclos", "modo aprender", "bora ler", "teoria", "quero teoria", "ir para teoria", "ir pra teoria", "sem flashcards, teoria", "sem flash cards, teoria", "sem flashcards", "sem flash cards"}
                or msg_clean.startswith("1. aprender")
                or msg_clean.startswith("1️⃣ aprender")
                or "quero aprender" in msg_clean
                or ("teoria" in msg_clean and not any(w in msg_clean for w in ["questao", "questão", "exercicio", "exercício"]))
                or ("explicacao" in msg_clean or "explicação" in msg_clean)
            ):
                target_mode = "modo_aprender"
            elif msg_clean in {"2️⃣", "2️⃣ praticar", "2. praticar", "praticar"} or "quero praticar" in msg_clean or "modo praticar" in msg_clean or "fazer exercicios" in msg_clean or "fazer exercícios" in msg_clean or "lista de exercicios" in msg_clean or "lista de exercícios" in msg_clean:
                target_mode = "modo_praticar"
            elif msg_clean in {"3️⃣", "3️⃣ flashcards", "3️⃣ revisar", "3. flashcards", "flashcards"} or "quero flashcards" in msg_clean or "modo flashcards" in msg_clean or "quero revisar" in msg_clean or "modo revisar" in msg_clean or "flashcards" in msg_clean or "ver flashcards" in msg_clean:
                target_mode = "modo_revisar"
            elif msg_clean in {"4️⃣", "4️⃣ resumo", "4️⃣ resumir", "4. resumo", "resumo"} or "quero resumo" in msg_clean or "quero resumir" in msg_clean or "resumir memorex" in msg_clean or "modo resumir" in msg_clean or "ver memorex" in msg_clean or "fazer resumo" in msg_clean:
                target_mode = "modo_resumir"
            elif msg_clean in {"5️⃣", "5️⃣ enviar questão", "5️⃣ enviar questao", "5. enviar questão", "5. enviar questao", "5️⃣ resolve questao", "5️⃣ resolve questão"} or "enviar questao" in msg_clean or "enviar questão" in msg_clean or "resolve questao" in msg_clean or "resolve questão" in msg_clean or "resolver questao" in msg_clean or "resolver questão" in msg_clean or "tirar duvida de questao" in msg_clean or "tirar dúvida de questão" in msg_clean:
                target_mode = "modo_resolve_questao"
            elif msg_clean in {"6️⃣", "6️⃣ finalizar", "6. finalizar", "8️⃣"} or msg_clean in {"finalizar", "encerrar", "sair", "tchau", "concluir a sessao", "concluir a sessão", "encerrar sessao", "encerrar sessão"}:
                target_mode = "modo_conclusao"
        else:
            # Fora de estudo ativo (ex: em modo_menu ou modo_acolhida):
            # Dígitos numéricos 1..6 e ordinais selecionam a respectiva trilha canônica
            if state.get("topic"):
                if msg_clean in {"1", "1️⃣"} or msg_clean.startswith("1.") or "aprender" in msg_clean or "microciclo" in msg_clean or "bora ler" in msg_clean:
                    target_mode = "modo_aprender"
                elif msg_clean in {"2", "2️⃣"} or msg_clean.startswith("2.") or "praticar" in msg_clean or "exercicio" in msg_clean or "exercício" in msg_clean or "treino" in msg_clean or "desafio" in msg_clean:
                    target_mode = "modo_praticar"
                elif msg_clean in {"3", "3️⃣"} or msg_clean.startswith("3.") or "flashcard" in msg_clean or "flashcards" in msg_clean or "revisar" in msg_clean:
                    target_mode = "modo_revisar"
                elif msg_clean in {"4", "4️⃣"} or msg_clean.startswith("4.") or "resumo" in msg_clean or "resumir" in msg_clean or "memorex" in msg_clean:
                    target_mode = "modo_resumir"
                elif msg_clean in {"5", "5️⃣"} or msg_clean.startswith("5.") or "enviar questao" in msg_clean or "enviar questão" in msg_clean or "resolve questao" in msg_clean or "resolve questão" in msg_clean or "resolver questao" in msg_clean or "resolver questão" in msg_clean:
                    target_mode = "modo_resolve_questao"
                elif msg_clean in {"6", "6️⃣", "8", "8️⃣"} or msg_clean.startswith("6.") or "finalizar" in msg_clean or "encerrar" in msg_clean:
                    target_mode = "modo_conclusao"
            else:
                # Sem tema prévio
                if msg_clean in {"1", "1️⃣", "aprender", "microciclos", "bora ler"} or msg_clean.startswith("1.") or msg_clean.startswith("1️⃣"):
                    target_mode = "modo_aprender"
                elif msg_clean in {"2", "2️⃣", "praticar", "exercicios", "exercícios", "treino", "desafio"} or msg_clean.startswith("2.") or msg_clean.startswith("2️⃣"):
                    target_mode = "modo_praticar"
                elif msg_clean in {"3", "3️⃣", "flashcards", "flashcard", "revisar"} or msg_clean.startswith("3.") or msg_clean.startswith("3️⃣"):
                    target_mode = "modo_revisar"
                elif msg_clean in {"4", "4️⃣", "resumo", "resumir", "memorex"} or msg_clean.startswith("4.") or msg_clean.startswith("4️⃣"):
                    target_mode = "modo_resumir"
                elif msg_clean in {"5", "5️⃣", "enviar questao", "enviar questão", "resolve questao", "resolve questão", "resolver questao", "resolver questão"} or msg_clean.startswith("5.") or msg_clean.startswith("5️⃣"):
                    target_mode = "modo_resolve_questao"
                elif msg_clean in {"6", "6️⃣", "finalizar", "encerrar"} or msg_clean.startswith("6.") or msg_clean.startswith("6️⃣"):
                    target_mode = "modo_conclusao"

    if target_mode:
        if target_mode == "modo_conclusao":
            state["current_mode"] = "modo_conclusao"
            state["pending_track"] = None
            state["just_selected_track"] = True
            save_session_states()
            return "modo_conclusao", state["topic"], state
        elif state["topic"]:
            # Já tem tema específico! Ativa imediatamente o modo e registra gatilho de início de trilha
            state["current_mode"] = target_mode
            state["pending_track"] = None
            state["just_selected_track"] = True
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
            
        # SOLUÇÃO 1: ÁRBITRO CURRICULAR SEMÂNTICO PRIMÁRIO (LLM-First via DeepSeek)
        # Classifica sob as 2 regras independentes (Regra 1: Interdisciplinar | Regra 2: Densidade Curricular >= 3 capítulos)
        # Compreende hierarquia conceitual real sem colisões de palavras-chave ou substrings
        raw_topic = current_message.strip().strip(".!?,")
        if raw_topic.lower() in INVALID_TOPIC_WORDS:
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        analysis = await analyze_topic_curricular_rules(raw_topic, current_discipline=state.get("discipline"))
        
        # Se a LLM identificou a disciplina com clareza e o estado da sessão ainda não tem, atualiza automaticamente
        disc_id = analysis.get("disciplina_identificada")
        norm_disc = strip_accents(disc_id) if disc_id else None
        norm_supported = {strip_accents(d) for d in SUPPORTED_DISCIPLINES}

        # GUARDRAIL SISTÊMICO: Disciplina fora do acervo oficial (ex: Português, Gramática, Literatura, Filosofia)
        norm_non_supported = {strip_accents(d) for d in NON_SUPPORTED_DISCIPLINES}
        if norm_disc and norm_disc in norm_non_supported:
            state["topic"] = None
            state["pending_disambiguation"] = None
            state["disambiguation_options"] = None
            state["clean_names"] = None
            state["discipline"] = None
            state["out_of_scope_discipline"] = SUBJECT_DISPLAY_MAP.get(norm_disc, disc_id)
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state
        elif analysis.get("fora_do_escopo"):
            # Conversa informal, saudação ou texto sem tema curricular (ex: "e ai plito")
            state["topic"] = None
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        # Se a disciplina identificada for suportada:
        if disc_id and norm_disc in norm_supported and not state.get("discipline"):
            state["discipline"] = disc_id

        # Se o LLM corrigiu um typo para um tema amplo presente no cache (ex: "funcoes matemaica" -> "Funções Matemáticas"), força a desambiguação!
        norm_formatted = strip_accents(analysis.get("tema_formatado") or "").strip()
        if not analysis.get("desambiguar") and norm_formatted in SEMANTIC_TOPIC_CACHE and SEMANTIC_TOPIC_CACHE[norm_formatted].get("desambiguar"):
            analysis = SEMANTIC_TOPIC_CACHE[norm_formatted]

        if analysis.get("desambiguar"):
            state["pending_disambiguation"] = analysis.get("tema_raiz") or raw_topic.capitalize()
            state["disambiguation_options"] = analysis.get("opcoes")
            state["clean_names"] = analysis.get("clean_names")
            state["disambiguation_depth"] = 1
            state["disambiguation_reason"] = analysis.get("motivo") or "REGRA_2"
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        # GUARDRAIL INVIOLÁVEL: Nome de disciplina isolada (ex: "Matemática", "Física", "Química") NUNCA pode virar state["topic"]!
        if norm_formatted and match_discipline_fuzzy(norm_formatted):
            matched_d = match_discipline_fuzzy(norm_formatted)
            norm_supported_d = {strip_accents(d) for d in SUPPORTED_DISCIPLINES}
            state["topic"] = None
            if matched_d not in norm_supported_d:
                state["discipline"] = None
                state["out_of_scope_discipline"] = SUBJECT_DISPLAY_MAP.get(matched_d, matched_d.capitalize())
            else:
                state["discipline"] = SUBJECT_DISPLAY_MAP.get(matched_d, matched_d.capitalize())
            state["current_mode"] = "modo_acolhida"
            save_session_states()
            return "modo_acolhida", None, state

        _raw_tname = (analysis.get("tema_formatado") or raw_topic[:40]).strip()
        state["topic"] = (_raw_tname[0].upper() + _raw_tname[1:]) if _raw_tname else raw_topic[:40]
        
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
    if state["current_mode"] in {"modo_aprender", "modo_praticar", "modo_revisar", "modo_resumir", "modo_resolve_questao"}:
        return state["current_mode"], state["topic"], state

    # Caso padrão
    return "modo_menu", state["topic"], state

def get_system_prompt_for_mode(mode: str) -> str:
    # Arquitetura modular oficial homologada (Base Persona + Sub-prompt do Modo Ativo):
    if os.path.exists(BASE_PERSONA_FILE):
        mode_file = os.path.join(MODES_DIR, f"{mode}.md")
        if os.path.exists(mode_file):
            with open(BASE_PERSONA_FILE, "r", encoding="utf-8") as f:
                base_persona = f.read()
            with open(mode_file, "r", encoding="utf-8") as f:
                mode_instructions = f.read()
            return f"{base_persona}\n\n---\n\n{mode_instructions}"
            
    # Fallback para o System Prompt Oficial Consolidado v2.0.0 (prompt_prod.md)
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def get_system_prompt():
    return get_system_prompt_for_mode("modo_menu")

print("[PROD] Mob.me AI Tutor v2.0.0 (Codinome: 'Mob.me 6 Trilhas') inicializada com sucesso.")



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
    """Extrai informações da imagem e transcreve para texto seguindo diretrizes universais (com fallback DeepInfra Qwen-VL)."""
    prompt = """Você é um Transcritor Visual Universal de alta precisão. Seu papel é traduzir tudo o que existe nesta imagem para texto, para que outra IA (que não tem visão) possa resolvê-la. Não responda à pergunta, apenas extraia os dados seguindo estas regras:
1. Textos: Transcreva fielmente todos os textos, enunciados e alternativas visíveis.
2. Matemática, Química e Física (e outras matérias de cálculo também): Formate qualquer fórmula, equação, composto ou grandeza usando sintaxe MathJax/LaTeX rigorosa (ex: $H_2O$ ou $x^2$).
3. Ciências da Natureza e Geografia: Se houver esquemas anatômicos, mapas, gráficos ou biomas, faça uma descrição literal e minuciosa do que está desenhado e para onde as setas apontam.
4. Humanas: Se for uma foto histórica, charge ou pintura, descreva os elementos visuais, personagens e o layout.
5. Tabelas: Converta tabelas para formato Markdown.
Lembre-se: não resolva o problema, apenas descreva visualmente e transcreva o texto."""

    clean_b64 = image_base64.split(",", 1)[1] if "," in image_base64 else image_base64
    data_url = f"data:image/png;base64,{clean_b64}"

    # 1. Tentativa Primária com Gemini
    try:
        model = genai.GenerativeModel("gemini-2.5-flash", generation_config={"temperature": 0.0})
        parts = [
            {"inline_data": {"mime_type": "image/jpeg", "data": clean_b64}},
            {"text": prompt}
        ]
        response = await model.generate_content_async(parts)
        if response and response.text:
            return response.text.strip()
    except Exception as e_gemini:
        print(f"Aviso: Gemini Vision indisponível ({e_gemini}). Acionando fallback DeepInfra Qwen-VL...")

    # 2. Fallback Resiliente via DeepInfra Qwen-VL
    if deepinfra_client:
        try:
            resp = await deepinfra_client.chat.completions.create(
                model="Qwen/Qwen3-VL-30B-A3B-Instruct",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": data_url}}
                        ]
                    }
                ],
                max_tokens=1000,
                temperature=0.0
            )
            return resp.choices[0].message.content.strip()
        except Exception as e_di:
            print(f"Erro no fallback DeepInfra Vision: {e_di}")

    return "[Imagem Anexada: Não foi possível transcrever os dados visuais automaticamente. Por favor, envie uma foto mais nítida ou digite o enunciado da questão.]"

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
        if deepinfra_client:
            prompt = f"Crie um t?tulo extremamente curto (2 a 4 palavras no m?ximo) que resuma a inten??o desta mensagem do aluno: '{first_message}'. Retorne APENAS o t?tulo, sem aspas, sem formata??o e sem explica??es."
            resp = await deepinfra_client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V4-Flash-0731",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=20,
                temperature=0.3
            )
            new_title = resp.choices[0].message.content.strip().replace('"', '').replace('*', '').replace('#', '')
            await update_session_title(supabase_client, session_id, new_title)
            print(f"T?tulo da sess?o {session_id} atualizado para: {new_title}")
        else:
            model = genai.GenerativeModel("gemini-2.5-flash")
            prompt = f"Crie um t?tulo extremamente curto (2 a 4 palavras no m?ximo) que resuma a inten??o desta mensagem do aluno: '{first_message}'. Retorne APENAS o t?tulo, sem aspas, sem formata??o e sem explica??es."
            response = await call_with_retry_async(model.generate_content_async, prompt)
            new_title = response.text.strip().replace('"', '').replace('*', '').replace('#', '')
            await update_session_title(supabase_client, session_id, new_title)
            print(f"T?tulo da sess?o {session_id} atualizado para: {new_title}")
    except Exception as e:
        print(f"Erro ao gerar t?tulo da sess?o: {e}")

@app.get("/")
async def read_root():
    return {"status": "Mob.me Backend is running (Pure Async)!"}

@app.get("/api/audits/latest")
async def get_latest_audit():
    audit_dirs = ["/app/auditorias", "scratch/auditorias"]
    for d in audit_dirs:
        latest_file = os.path.join(d, "latest.json")
        if os.path.exists(latest_file):
            try:
                with open(latest_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
    return {"status": "no_audits_found", "message": "Nenhum dossiê de auditoria gerado ainda."}

@app.get("/api/audits/summary")
async def get_audit_summary():
    audit_dirs = ["/app/auditorias", "scratch/auditorias"]
    for d in audit_dirs:
        latest_md = os.path.join(d, "latest.md")
        if os.path.exists(latest_md):
            try:
                with open(latest_md, "r", encoding="utf-8") as f:
                    return Response(content=f.read(), media_type="text/markdown")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
    return Response(content="# Nenhum dossiê disponível ainda", media_type="text/markdown")

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

# =====================================================================
# MOTOR DETERMINÍSTICO DE EXERCÍCIOS (TRILHA PRATICAR - TOLERÂNCIA ZERO)
# =====================================================================

def parse_student_answer(msg: str) -> str:
    """
    Extrai deterministicamente a letra escolhida pelo estudante (A, B, C, D, E)
    ou converte opções numéricas (1=A .. 5=E). Retorna string vazia se ambíguo.
    """
    if not msg:
        return ""
    clean = msg.strip().lower()
    
    # 1. Letra isolada
    if clean in {"a", "b", "c", "d", "e"}:
        return clean.upper()
        
    # 2. Posição numérica 1 a 5
    num_map = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E"}
    if clean in num_map:
        return num_map[clean]
        
    # 3. Padrões textuais: "letra a", "a)", "(a)", "opção a", "alternativa b"
    m = re.search(r"(?:letra|opcao|opção|alternativa)?\s*[\(\[]?([a-e])[\)\]]?(?:\s|$)", clean)
    if m:
        return m.group(1).upper()
        
    return ""


def extract_round_items(full_ex_text: str) -> list[dict]:
    """
    Fatia deterministicamente uma lista oficial -exercicios.md da Educamob em exatamente 15 itens:
    5 Fáceis (de basico), 5 Médios (de intermediario), 5 Difíceis (de dificil).
    Suporta tanto gabarito inline (**Gabarito:** X) quanto seções separadas (## Gabaritos e Resoluções).
    """
    gabaritos_map = {}
    gab_matches = re.finditer(
        r"(?:###\s*Quest[aã]o\s*(\d+)|\*\*Quest[aã]o\s*(\d+)\*\*)[\r\n]+(?:\*\*Gabarito:\*\*\s*([A-Ea-e]))?[\r\n]*(.*?)(?=(?:###\s*Quest[aã]o|\*\*Quest[aã]o|\n##|\Z))",
        full_ex_text,
        re.DOTALL | re.IGNORECASE
    )
    for gm in gab_matches:
        q_idx = int(gm.group(1) or gm.group(2))
        gab_letter = gm.group(3).upper() if gm.group(3) else ""
        raw_res = gm.group(4).strip() if gm.group(4) else ""
        res_clean = re.sub(r"^\*\*Resolu[cç][aã]o(?:\s+Detalhada)?:\*\*\s*", "", raw_res, flags=re.IGNORECASE).strip()
        gabaritos_map[q_idx] = {"gabarito": gab_letter, "resolucao": res_clean}

    q_pattern = re.compile(
        r"<!--\s*id:\s*(q\d+)\s*\|\s*tipo:\s*([^\|]+)\s*\|\s*habilidade:\s*([^\|]+)\s*\|\s*dificuldade:\s*([^\|]+)\s*\|\s*objeto:\s*([^>]+)-->\s*(.*?)(?=(?:<!--\s*id:\s*q|\n##|\Z))",
        re.DOTALL
    )
    
    by_diff = {"basico": [], "intermediario": [], "dificil": []}
    
    for match in q_pattern.finditer(full_ex_text):
        qid = match.group(1).strip()
        qtipo = match.group(2).strip()
        qhab = match.group(3).strip()
        qdiff = match.group(4).strip().lower()
        qobj = match.group(5).strip()
        raw_body = match.group(6).strip()
        
        q_num_match = re.search(r"\d+", qid)
        q_num = int(q_num_match.group(0)) if q_num_match else 0
        
        inline_gab_match = re.search(r"\*\*Gabarito:\*\*\s*([A-Ea-e])", raw_body)
        inline_res_match = re.search(r"\*\*Resolu[cç][aã]o(?:\s+Detalhada)?:\*\*\s*(.*?)(?=\n\n|\Z)", raw_body, re.DOTALL)
        
        gabarito = ""
        resolucao = ""
        if inline_gab_match:
            gabarito = inline_gab_match.group(1).upper()
            if inline_res_match:
                resolucao = inline_res_match.group(1).strip()
            body_question = raw_body[:inline_gab_match.start()].strip()
        elif q_num in gabaritos_map:
            gabarito = gabaritos_map[q_num]["gabarito"]
            resolucao = gabaritos_map[q_num]["resolucao"]
            body_question = raw_body.strip()
        else:
            body_question = raw_body.strip()
            
        body_question = re.sub(r"^(?:###\s*Quest[aã]o\s*\d+|\*\*Quest[aã]o\s*\d+\*\*)\s*", "", body_question, flags=re.IGNORECASE).strip()
        
        # Garante que cada alternativa fique em linha própria isolada por quebra dupla
        body_formatted = re.sub(r"(?:\r?\n)*([a-eA-E]\))", r"\n\n\1", body_question)
        body_formatted = re.sub(r"^\n\n", "", body_formatted).strip()
        
        item_data = {
            "id": qid,
            "q_num": q_num,
            "habilidade": qhab,
            "dificuldade": qdiff,
            "objeto": qobj,
            "gabarito": gabarito,
            "resolucao": resolucao,
            "body": body_formatted
        }
        
        if qdiff in by_diff:
            by_diff[qdiff].append(item_data)
            
    round_items = []
    
    # 5 Fácil (Básico)
    for i, item in enumerate(by_diff["basico"][:5]):
        it = dict(item)
        it["round_q"] = i + 1
        it["level_label"] = "Fácil"
        round_items.append(it)
        
    # 5 Médio (Intermediário)
    for i, item in enumerate(by_diff["intermediario"][:5]):
        it = dict(item)
        it["round_q"] = i + 6
        it["level_label"] = "Médio"
        round_items.append(it)
        
    # 5 Difícil (Difícil)
    for i, item in enumerate(by_diff["dificil"][:5]):
        it = dict(item)
        it["round_q"] = i + 11
        it["level_label"] = "Difícil"
        round_items.append(it)
        
    return round_items


async def resolve_exercise_file_for_topic(topic: str, user_grade: str | None = None, session_discipline: str | None = None) -> tuple[str | None, str | None]:
    """
    Localiza fisicamente o arquivo -exercicios.md mais adequado no repositório,
    com desambiguação inteligente de série (grade-aware) e foco no acervo homologado.
    """
    global deepinfra_client, supabase_client
    if not topic:
        return None, None
        
    if deepinfra_client is None:
        deepinfra_client = AsyncOpenAI(
            api_key=os.getenv("DEEPINFRA_API_TOKEN", ""),
            base_url="https://api.deepinfra.com/v1/openai"
        )
    if supabase_client is None:
        supabase_client = await create_async_client(SUPABASE_URL, SUPABASE_KEY)
        
    search_query = f"E-book Teoria: {topic}"
    try:
        embed_resp = await asyncio.wait_for(
            deepinfra_client.embeddings.create(
                input=search_query,
                model="BAAI/bge-m3"
            ),
            timeout=5.0
        )
        query_embedding = embed_resp.data[0].embedding
        
        response = await asyncio.wait_for(
            supabase_client.rpc(
                "match_documents",
                {"query_embedding": query_embedding, "match_count": 10}
            ).execute(),
            timeout=5.0
        )
        docs_data = response.data or []
    except Exception as e:
        print(f"Erro na busca vetorial de exercícios: {e}")
        docs_data = []

    # Calibração Curricular por Série do Estudante (Grade-Aware Rerank)
    if user_grade and user_grade != "Não informada":
        ug_lower = user_grade.lower()
        def grade_score(doc):
            src = doc.get("metadata", {}).get("source", "").lower()
            if "9" in ug_lower and "9-ano" in src:
                return 10
            if "8" in ug_lower and "8-ano" in src:
                return 10
            if "7" in ug_lower and "7-ano" in src:
                return 10
            if "6" in ug_lower and "6-ano" in src:
                return 10
            if "5" in ug_lower and "5-ano" in src:
                return 10
            if ("médio" in ug_lower or "medio" in ug_lower or "série" in ug_lower or "serie" in ug_lower) and "medio" in src:
                return 10
            return 0
        docs_data = sorted(docs_data, key=grade_score, reverse=True)
    elif any(term in topic.lower() for term in ["segundo grau", "2º grau", "2o grau", "quadrática", "quadratica"]):
        # Priorização pedagógica para tópicos polissêmicos de Equações de 2º Grau:
        # Se nenhuma série estiver informada, prioriza 9º Ano ou Ensino Médio sobre a introdução do 8º ano
        def topic_score(doc):
            src = doc.get("metadata", {}).get("source", "").lower()
            if "9-ano" in src and "equacoes-segundo-grau" in src:
                return 10
            if "medio" in src and "equacoes-quadraticas" in src:
                return 8
            if "8-ano" in src:
                return 4
            return 0
        docs_data = sorted(docs_data, key=topic_score, reverse=True)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if os.path.isdir("/app/content"):
        project_root = "/app"
    elif os.path.isdir("/content"):
        project_root = "/"

    def extract_doc_discipline(path_str: str) -> str | None:
        p = strip_accents(path_str.lower())
        for d in ["fisica", "quimica", "matematica", "ciencias", "historia", "geografia", "calculo"]:
            if f"/{d}/" in p or f"\\{d}\\" in p or f"-{d}-" in p or p.startswith(f"{d}/") or f"_{d}_" in p:
                return d
        return None

    norm_target_disc = strip_accents(session_discipline.lower()) if session_discipline else None

    for d in docs_data:
        src = d.get("metadata", {}).get("source", "")
        if not src:
            continue

        doc_disc = extract_doc_discipline(src)
        # RAG_DISCIPLINA_CRUZADA GUARD: Nunca aceita documento de disciplina diferente da sessão
        if norm_target_disc and doc_disc and doc_disc != norm_target_disc:
            continue

        # GRADE LEVEL GUARD: Nunca aceita Fundamental 1 para estudantes do Ensino Médio
        if user_grade:
            ug_low = user_grade.lower()
            if ("médio" in ug_low or "medio" in ug_low or "série" in ug_low or "serie" in ug_low) and "fundamental-1" in src.lower():
                continue

        ex_src = src if src.endswith("-exercicios.md") else (src[:-3] + "-exercicios.md" if src.endswith(".md") else "")
        clean_rel = ex_src.replace("../../", "")
        candidate_paths = [os.path.join(project_root, clean_rel), ex_src, clean_rel, os.path.join("..", "..", clean_rel)]
        
        top_dir_rel = os.path.dirname(src.replace("../../", ""))
        abs_top_dir = os.path.join(project_root, top_dir_rel)
        dirs_to_check = [abs_top_dir, os.path.dirname(abs_top_dir)]
        for pdir in dirs_to_check:
            if os.path.isdir(pdir):
                for fname in os.listdir(pdir):
                    if fname.endswith("-exercicios.md"):
                        candidate_paths.append(os.path.join(pdir, fname))
                    
        for candidate in candidate_paths:
            if candidate and os.path.exists(candidate):
                cand_disc = extract_doc_discipline(candidate)
                if norm_target_disc and cand_disc and cand_disc != norm_target_disc:
                    continue
                return candidate, clean_rel
                
    return None, None

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
                    
                return StreamingResponse(fallback_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})

        # 2. Salvar a mensagem (agora APENAS TEXTO, sem o base64 para evitar inchaço e amnésia)
        opt_msg_user = add_to_transient_cache(current_session_id, "user", base_user_message, None)
        background_tasks.add_task(save_message, supabase_client, current_session_id, "user", base_user_message, None, opt_msg_user)

        # 3. Detectar o Modo de Operação Ativo, Atualizar Máquina de Estados e Carregar o Prompt Especialista
        active_mode, current_topic, session_state = await resolve_active_mode_and_topic(
            current_session_id, 
            db_history, 
            request.message,
            has_image=has_image,
            extracted_text=extracted_text
        )
        print(f"[{current_session_id[:8]}] Modo Ativo: [{active_mode}] | Tema: [{current_topic}] | Trilha Pendente: [{session_state.get('pending_track')}]")
        
        # RESPOSTA INSTANTÂNEA PARA TEMAS FORA DO ESCOPO DA EDUCAMOB (Zero alucinação, sincronizada com available_subjects)
        if active_mode == "modo_acolhida" and session_state.get("out_of_scope_discipline"):
            disc_name = session_state.pop("out_of_scope_discipline")
            norm_disc_check = strip_accents(disc_name.lower()) if disc_name else ""
            norm_supp = {strip_accents(d.lower()) for d in SUPPORTED_DISCIPLINES}
            
            # Se a disciplina identificada for SUPORTADA, recupera graciosamente e não dá erro de fora do escopo!
            if norm_disc_check in norm_supp:
                session_state["discipline"] = SUBJECT_DISPLAY_MAP.get(norm_disc_check, disc_name)
                save_session_states()
                disc_disp = session_state["discipline"]
                disc_msg = f"Ótimo! Vamos focar em **{disc_disp}**! Qual conteúdo ou assunto específico você quer estudar hoje?"
                async def direct_disc_recovered_stream():
                    yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                    yield f"data: {json.dumps({'chunk': disc_msg})}\n\n"
                    opt_ai = add_to_transient_cache(current_session_id, "ai", disc_msg, None)
                    background_tasks.add_task(save_message, supabase_client, current_session_id, "ai", disc_msg, None, opt_ai)
                    yield "data: [DONE]\n\n"
                return StreamingResponse(direct_disc_recovered_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})

            save_session_states()
            active_list_str = ", ".join(AVAILABLE_SUBJECTS_LIST)
            if not disc_name or disc_name.strip().lower() in {"indefinida", "desconhecida", "outro", "outra", "none", "", "nao identificada", "não identificada"}:
                out_of_scope_msg = (
                    f"No momento, o acervo da Educamob no Mob.me possui materiais homologados estritamente para as disciplinas: **{active_list_str}**.\n\n"
                    f"Qual assunto de **{active_list_str}** você gostaria de estudar hoje?"
                )
            else:
                out_of_scope_msg = (
                    f"No momento, o acervo da Educamob no Mob.me possui materiais homologados estritamente para as disciplinas: **{active_list_str}**. "
                    f"Por isso, ainda não atendo conteúdos de **{disc_name}**.\n\n"
                    f"Qual assunto de **{active_list_str}** você gostaria de estudar hoje?"
                )
            async def direct_out_of_scope_stream():
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                yield f"data: {json.dumps({'chunk': out_of_scope_msg})}\n\n"
                opt_ai = add_to_transient_cache(current_session_id, "ai", out_of_scope_msg, None)
                background_tasks.add_task(save_message, supabase_client, current_session_id, "ai", out_of_scope_msg, None, opt_ai)
                yield "data: [DONE]\n\n"
            return StreamingResponse(direct_out_of_scope_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})

        # RESPOSTA INSTANTÂNEA QUANDO O ALUNO INFORMA APENAS A DISCIPLINA (Impede abrir menu para disciplina genérica)
        if active_mode == "modo_acolhida" and not current_topic and not session_state.get("pending_disambiguation") and session_state.get("discipline"):
            disc_chosen = session_state.get("discipline")
            disc_msg = f"Ótimo, vamos focar em **{disc_chosen}**! Qual assunto ou conteúdo específico de **{disc_chosen}** você quer aprender hoje?"
            async def direct_disc_acolhida_stream():
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                yield f"data: {json.dumps({'chunk': disc_msg})}\n\n"
                opt_ai = add_to_transient_cache(current_session_id, "ai", disc_msg, None)
                background_tasks.add_task(save_message, supabase_client, current_session_id, "ai", disc_msg, None, opt_ai)
                yield "data: [DONE]\n\n"
            return StreamingResponse(direct_disc_acolhida_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})

        # RESPOSTA INSTANTÂNEA DE DESAMBIGUAÇÃO (Garante latência zero, 100% de precisão e empilhamento vertical correto antes do Super Menu)
        if active_mode == "modo_acolhida" and session_state.get("pending_disambiguation") and session_state.get("disambiguation_options"):
            opts = session_state.get("disambiguation_options")
            key_title = session_state.get("pending_disambiguation")
            
            formatted_opts = []
            for i, opt in enumerate(opts):
                num_badge = f"{i+1}️⃣"
                clean_opt = opt.strip()
                for b in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "1.", "2.", "3.", "4.", "5."]:
                    if clean_opt.startswith(b):
                        clean_opt = clean_opt[len(b):].strip()
                formatted_opts.append(f"{num_badge} {clean_opt}")
            opts_str = "\n\n".join(formatted_opts)

            disambig_msg = (
                f"No nosso acervo, **{key_title}** é um tema amplo e com ramificações importantes.\n"
                f"Para garantir que você não perca tempo, em qual foco você quer se aprofundar hoje?\n\n"
                f"{opts_str}\n\n"
                f"Qual desses caminhos é o seu foco hoje?"
            )
            
            async def direct_disambig_stream():
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                yield f"data: {json.dumps({'chunk': disambig_msg})}\n\n"
                opt_ai = add_to_transient_cache(current_session_id, "ai", disambig_msg, None)
                background_tasks.add_task(save_message, supabase_client, current_session_id, "ai", disambig_msg, None, opt_ai)
                yield "data: [DONE]\n\n"
                
            return StreamingResponse(direct_disambig_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})

        # RESPOSTA INSTANTÂNEA DO MENU CANÔNICO DE 6 TRILHAS (Latência 0ms, 100% de fidelidade às 6 opções e imune a re-desambiguação)
        if active_mode == "modo_menu" and current_topic and not has_image:
            super_menu_msg = (
                f"Tema definido: **{current_topic}**. Como você prefere começar?\n\n"
                f"1. Aprender📚\n\n"
                f"2. Praticar📝\n\n"
                f"3. Flashcards 🃏\n\n"
                f"4. Resumo 🧠\n\n"
                f"5. Enviar questão 🖼️\n\n"
                f"6. Finalizar ⏸️\n\n"
                f"Qual caminho você prefere agora?"
            )
            async def direct_super_menu_stream():
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                yield f"data: {json.dumps({'chunk': super_menu_msg})}\n\n"
                opt_ai = add_to_transient_cache(current_session_id, "ai", super_menu_msg, None)
                background_tasks.add_task(save_message, supabase_client, current_session_id, "ai", super_menu_msg, None, opt_ai)
                yield "data: [DONE]\n\n"
            return StreamingResponse(direct_super_menu_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})
        
        system_prompt_base = get_system_prompt_for_mode(active_mode)
        chosen_track_label = session_state.get("pending_track") or active_mode
        state_context = f"\n\n--- ESTADO DA SESSÃO ATUAL ---\nTema atual: {current_topic or 'NENHUM (Ainda não foi informado pelo aluno)'}\nDisciplina informada: {session_state.get('discipline') or 'Geral'}\nTrilha escolhida pelo estudante: {chosen_track_label}"
        if active_mode == "modo_resolve_questao" and extracted_text:
            state_context += f"\nTranscrição/descrição da imagem enviada pelo estudante:\n{extracted_text}"

        if active_mode == "modo_resolve_questao" and session_state.get("paused_track"):
            paused_info = session_state.get("paused_track")
            p_mode = paused_info.get("mode")
            p_name = "treino de exercícios (Praticar)" if p_mode == "modo_praticar" else ("estudo teórico (Aprender)" if p_mode == "modo_aprender" else "flashcards (Revisar)")
            state_context += (
                f"\n\n--- INSTRUÇÃO HÍBRIDA DE RESOLUÇÃO DE IMAGEM EM TRILHA ATIVA ---\n"
                f"O estudante enviou uma imagem enquanto estava em andamento no {p_name} do tema '{current_topic}'.\n"
                f"1. Se a imagem contiver claramente o rascunho de cálculo ou a resolução do próprio aluno para a questão que estava na tela: valide a resolução com acolhimento e sobriedade empática, e continue a sequência pedagógica normalmente.\n"
                f"2. Se a imagem for uma questão nova, externa ou avulsa (de prova, livro ou tarefa): transcreva a questão com clareza, resolva passo a passo com didática acolhedora destacando a resposta final, e ao terminar pergunte gentilmente: 'Quer voltar para onde estávamos no seu {p_name} ou prefere ver o menu?'."
            )
        elif active_mode == "modo_resolve_questao" and has_image:
            state_context += (
                "\n\n--- INSTRUÇÃO DE ENCERRAMENTO DO MODO 5 (ENVIAR QUESTÃO) ---\n"
                "Se a imagem estiver legível e com enunciado completo: transcreva a questão, resolva passo a passo destacando a resposta final e, ao final da mensagem, recomende o próximo passo e exiba OBRIGATORIAMENTE o Menu Canônico de 6 Trilhas completo (1. Aprender📚 até 6. Finalizar ⏸️).\n"
                "Se a imagem estiver cortada ou incompleta: aponte o corte com acolhimento e peça uma nova foto sem inventar os dados ausentes."
            )
        
        msg_action_clean = request.message.strip().lower()
        llm_user_message = base_user_message
        is_resuming = session_state.pop("resuming_track", False)
        is_track_switch = session_state.pop("just_selected_track", False)

        # Preparação do Orquestrador Determinístico para a Trilha Praticar
        praticar_items = []
        if active_mode == "modo_praticar":
            round_data = session_state.get("praticar_round")
            if is_track_switch or not round_data or round_data.get("topic") != current_topic or not round_data.get("items"):
                ex_path, ex_rel = await resolve_exercise_file_for_topic(current_topic, user.get('grade_level'), session_state.get('discipline'))
                if ex_path and os.path.exists(ex_path):
                    try:
                        with open(ex_path, "r", encoding="utf-8") as ef:
                            praticar_items = extract_round_items(ef.read())
                        session_state["praticar_round"] = {
                            "topic": current_topic,
                            "items": praticar_items,
                            "source": ex_rel,
                            "file_path": ex_path
                        }
                        save_session_states()
                    except Exception as e_parse:
                        print(f"Erro ao extrair itens da rodada: {e_parse}")
            else:
                praticar_items = round_data.get("items", [])

        if is_resuming:
            save_session_states()
            resumed_detail = ""
            if active_mode == "modo_praticar":
                for msg in reversed(db_history):
                    if msg.get("role") == "ai":
                        m_q = re.search(r"Quest[aã]o\s+(\d+)/15", msg.get("content", ""), re.IGNORECASE)
                        if m_q:
                            q_num = int(m_q.group(1))
                            d_lbl = "Fácil" if q_num <= 5 else ("Médio" if q_num <= 10 else "Difícil")
                            if praticar_items and 1 <= q_num <= len(praticar_items):
                                it_resumed = praticar_items[q_num - 1]
                                resumed_detail = (
                                    f" Reapresente imediatamente a '📝 Questão {q_num}/15 — {d_lbl}' que estava em aberto antes da pausa, transcrevendo exatamente:\n\n"
                                    f"{it_resumed['body']}\n\n"
                                    f"(Com as alternativas isoladas uma por linha usando \\n\\n, sem exibir o Menu de Trilhas)."
                                )
                            else:
                                resumed_detail = f" Reapresente imediatamente a '📝 Questão {q_num}/15 — {d_lbl}' (com as 5 alternativas uma por linha usando \\n\\n) que estava em aberto antes da pausa, sem exibir o Menu de Trilhas."
                            break
            elif active_mode == "modo_revisar":
                for msg in reversed(db_history):
                    if msg.get("role") == "ai":
                        m_fc = re.search(r"Flashcard\s+(\d+)/(\d+)", msg.get("content", ""), re.IGNORECASE)
                        if m_fc:
                            resumed_detail = f" Reapresente imediatamente o '🃏 Flashcard {m_fc.group(1)}/{m_fc.group(2)}' que estava em aberto antes da pausa, sem exibir o Menu de Trilhas."
                            break
            state_context += f"\nAção do Estudante: O aluno optou por retomar a trilha anterior ({active_mode}). Retome exatamente de onde ele parou com naturalidade e acolhimento.{resumed_detail}"
            llm_user_message = f"[Comando de Retomada]: Quero voltar para onde paramos em {current_topic}.{resumed_detail}"
        elif is_track_switch:
            save_session_states()
            if active_mode == "modo_aprender":
                state_context += (
                    "\nAção do Estudante: O aluno acabou de escolher a Trilha 1 (Aprender). Inicie a primeira etapa de estudos usando exclusivamente o material RAG recuperado para este tema. "
                    "Cada etapa deve ter um objetivo curto, um trecho do e-book e uma checagem de compreensão ancorada no trecho ('### [Título do Tópico]', '**Objetivo:**', trecho e '**Checagem:**'). "
                    "REGRA CRÍTICA: Proibido usar a palavra 'microciclo' ou 'miniciclo' no título ou no texto; use apenas o título do conceito no cabeçalho '###'. "
                    "Não exiba o Menu de Trilhas antes de concluir as etapas disponíveis."
                )
                llm_user_message = f"[Comando de Trilha]: Escolho a opção 1. Aprender📚 sobre {current_topic}. Inicie imediatamente a primeira etapa de estudos."
            elif active_mode == "modo_praticar":
                if praticar_items:
                    item_1 = praticar_items[0]
                    state_context += (
                        f"\nAção do Estudante: O aluno acabou de escolher a Trilha 2 (Praticar). Inicie imediatamente a rodada apresentando a Questão 1/15.\n"
                        f"É TERMINANTEMENTE PROIBIDO inventar, alterar dados ou criar outra questão. Transcreva EXATAMENTE o seguinte item oficial homologado da lista RAG:\n\n"
                        f"📝 Questão 1/15 — {item_1['level_label']}\n\n"
                        f"{item_1['body']}\n\n"
                        f"(AVISO DE BLINDAGEM: Não apresente o gabarito ou resolução nesta mensagem. Apenas cabeçalho, enunciado e alternativas com quebra dupla '\\n\\n'. Aguarde a resposta do estudante)."
                    )
                    llm_user_message = f"[Comando de Trilha]: Escolho a opção 2. Praticar📝 sobre {current_topic}. Apresente a 📝 Questão 1/15 — {item_1['level_label']} da lista oficial."
                else:
                    state_context += "\nAção do Estudante: O aluno acabou de escolher a Trilha 2 (Praticar). Inicie imediatamente a '📝 Questão 1/15 — Fácil' selecionada da lista oficial do RAG (5 fáceis/básicos, 5 médios/intermediários e 5 difíceis). Não peça confirmação e não crie questões fora do banco oficial."
                    llm_user_message = f"[Comando de Trilha]: Escolho a opção 2. Praticar📝 sobre {current_topic}. Ignore qualquer pergunta anterior em aberto e apresente imediatamente a 📝 Questão 1/15 — Fácil da lista oficial do RAG."
            elif active_mode == "modo_revisar":
                state_context += "\nAção do Estudante: O aluno acabou de escolher a Trilha 3 (Flashcards). Inicie imediatamente o '🃏 Flashcard 1/10' com uma pergunta aberta conceitual fundamentada exclusivamente no material RAG recuperado. Aguarde a resposta antes de corrigir."
                llm_user_message = f"[Comando de Trilha]: Escolho a opção 3. Flashcards 🃏 sobre {current_topic}. Ignore qualquer pergunta anterior em aberto e apresente imediatamente o 🃏 Flashcard 1/10."
            elif active_mode == "modo_resumir":
                state_context += "\nAção do Estudante: O aluno acabou de escolher a Trilha 4 (Resumo). Entregue imediatamente a síntese estruturada (600 a 1.000 palavras) usando exclusivamente o material RAG recuperado a partir de '### 🌐 1. Visão Panorâmica', e ao final exiba o Menu de Trilhas de 6 opções."
                llm_user_message = f"[Comando de Trilha]: Escolho a opção 4. Resumo 🧠 sobre {current_topic}. Ignore qualquer pergunta anterior em aberto e gere imediatamente a síntese estruturada completa."
            elif active_mode == "modo_resolve_questao" and not has_image:
                state_context += "\nAção do Estudante: O aluno acabou de escolher a Trilha 5 (Enviar questão). Peça de forma curta e direta para ele enviar o enunciado por texto ou anexar a imagem da questão sobre o tema atual."
                llm_user_message = f"[Comando de Trilha]: Escolho a opção 5. Enviar questão 🖼️ sobre {current_topic}. Peça para eu enviar a questão."
            elif active_mode == "modo_conclusao":
                state_context += "\nAção do Estudante: O aluno escolheu a Trilha 6 (Finalizar). Encerre a sessão em 1 ou 2 linhas factuais registrando apenas o que realmente ocorreu na sessão, sem elogios exagerados, sem novos menus e sem novas perguntas."
                llm_user_message = "[Comando de Trilha]: Escolho a opção 6. Finalizar ⏸️ a sessão de estudo agora."
        else:
            # Durante a progressão pedagógica contínua (estudo ativo turn-by-turn):
            if active_mode == "modo_praticar":
                last_ai_msg = ""
                for msg in reversed(db_history):
                    if msg.get("role") == "ai":
                        last_ai_msg = msg.get("content", "")
                        break
                match_q = re.search(r"Quest[aã]o\s+(\d+)/15", last_ai_msg, re.IGNORECASE)
                if match_q:
                    curr_q = int(match_q.group(1))
                    next_q = curr_q + 1
                    
                    eval_prompt = ""
                    if praticar_items and 1 <= curr_q <= len(praticar_items):
                        curr_item = praticar_items[curr_q - 1]
                        expected_gab = (curr_item.get("gabarito") or "").strip().upper()
                        student_letter = parse_student_answer(request.message)
                        
                        if expected_gab and student_letter:
                            if student_letter == expected_gab:
                                eval_prompt = (
                                    f"AVALIAÇÃO DETERMINÍSTICA DO BACKEND: O estudante ACERTOU a Questão {curr_q} "
                                    f"(marcou a alternativa correta '{expected_gab}'). Valide com sobriedade afirmativa direta e objetiva "
                                    f"(ex: 'Exato, você acertou!', 'Boa, resposta correta.'). "
                                    f"É TERMINANTEMENTE PROIBIDO usar expressões de erro, dúvida ou hesitação como 'Quase lá'."
                                )
                            else:
                                res_hint = f" Use a resolução oficial do RAG: {curr_item['resolucao']}." if curr_item.get('resolucao') else ""
                                eval_prompt = (
                                    f"AVALIAÇÃO DETERMINÍSTICA DO BACKEND: O estudante ERROU a Questão {curr_q} "
                                    f"(marcou '{student_letter}', mas o gabarito oficial é '{expected_gab}'). "
                                    f"Informe o erro com sobriedade acolhedora e apresente a resolução comentada.{res_hint}"
                                )
                        else:
                            res_hint = f" Resolução oficial do RAG: {curr_item['resolucao']}." if curr_item.get('resolucao') else ""
                            eval_prompt = (
                                f"AVALIAÇÃO DA QUESTÃO: O gabarito oficial da Questão {curr_q} é '{expected_gab}'.{res_hint} "
                                f"Avalie a resposta do estudante ('{request.message}') com sobriedade factual."
                            )

                    if next_q <= 15:
                        if praticar_items and next_q <= len(praticar_items):
                            next_item = praticar_items[next_q - 1]
                            state_context += (
                                f"\nInstrução de Progresso da Rodada:\n{eval_prompt}\n\n"
                                f"Em seguida, apresente IMEDIATAMENTE a próxima questão oficial homologada:\n"
                                f"📝 Questão {next_q}/15 — {next_item['level_label']}\n\n"
                                f"{next_item['body']}\n\n"
                                f"(AVISO DE INTEGRIDADE: É TERMINANTEMENTE PROIBIDO criar, inventar, adaptar ou alterar dados de questões. "
                                f"Transcreva EXATAMENTE o item oficial acima com cada alternativa isolada em linha própria com quebra dupla '\\n\\n'. "
                                f"NUNCA repita a Questão {curr_q}, não revele o gabarito da Questão {next_q} e não exiba o Menu de Trilhas)."
                            )
                        else:
                            diff_label = "Fácil" if next_q <= 5 else ("Médio" if next_q <= 10 else "Difícil")
                            state_context += (
                                f"\nInstrução de Progresso da Rodada:\n{eval_prompt}\n\n"
                                f"Apresente IMEDIATAMENTE a '📝 Questão {next_q}/15 — {diff_label}' selecionada da lista oficial do RAG com alternativas uma por linha (\\n\\n). NUNCA repita a Questão {curr_q} e não exiba o Menu de Trilhas."
                            )
                    else:
                        state_context += (
                            f"\nInstrução de Progresso da Rodada:\n{eval_prompt}\n\n"
                            f"Esta foi a última questão (15/15) da rodada. Valide a resposta com sobriedade empática natural e NUNCA use frases empolgadas ou bajuladoras ('Parabéns!', 'Ótimo trabalho', 'Excelente entendimento'). "
                            f"Conclua imediatamente a rodada exibindo '### Seu aproveitamento: X/15 (Z%)', análise concisa e factual de pontos fortes e pontos a melhorar, e o Menu Canônico de 6 Trilhas."
                        )
            elif active_mode == "modo_revisar":
                last_ai_msg = ""
                for msg in reversed(db_history):
                    if msg.get("role") == "ai":
                        last_ai_msg = msg.get("content", "")
                        break
                match_fc = re.search(r"Flashcard\s+(\d+)/(\d+)", last_ai_msg, re.IGNORECASE)
                if match_fc:
                    curr_fc = int(match_fc.group(1))
                    tot_fc = int(match_fc.group(2))
                    next_fc = curr_fc + 1
                    if next_fc <= tot_fc:
                        state_context += f"\nInstrução de Progresso dos Flashcards: O estudante respondeu ao Flashcard {curr_fc}/{tot_fc}. Valide a resposta com sobriedade e apresente o '🃏 Flashcard {next_fc}/{tot_fc}'. Não use múltipla escolha e não exiba o Menu de Trilhas."
                    else:
                        state_context += f"\nInstrução de Progresso dos Flashcards: O estudante respondeu ao último Flashcard ({tot_fc}/{tot_fc}). Conclua com 'Seu aproveitamento: X/{tot_fc} (Z%)', análise concisa e o Menu Canônico de 6 Trilhas."
            
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
            # Se for acolhida, menu inicial, recusa de assunto, encerramento ou sem tema definido, pula a busca no RAG para resposta em tempo real (< 1s)
            if (active_mode in {"modo_acolhida", "modo_menu", "modo_conclusao", "modo_novo_assunto"} or not current_topic) and not request.image_base64:
                print(f"Modo de alta velocidade ou sem tema definido ({active_mode}). Pulando busca no RAG para resposta em tempo real...")
                context_str = ""
            else:
                t_rag_start = time.time()
                target_subject = current_topic if current_topic else request.message
                
                # Calibrar a query e o volume de chunks conforme o modo (chaves fixas por tema para 0ms de cache nos turnos seguintes!)
                if active_mode in {"modo_aprender", "modo_resumir", "modo_revisar"}:
                    search_query = f"E-book Teoria: {target_subject}"
                    match_count = 12
                elif active_mode == "modo_praticar":
                    search_query = f"E-book Teoria: {target_subject}"
                    match_count = 24
                elif active_mode == "modo_resolve_questao":
                    q_snippet = (extracted_text or request.message)[:200]
                    search_query = f"E-book Teoria: {target_subject} - {q_snippet}"
                    match_count = 8
                else:
                    search_query = f"{target_subject} - {request.message}"
                    match_count = 6

                cache_key = f"{active_mode}__{search_query.strip().lower()}__mc{match_count}"
                
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
                        embed_response = await asyncio.wait_for(
                            deepinfra_client.embeddings.create(
                                input=search_query,
                                model="BAAI/bge-m3"
                            ),
                            timeout=5.0
                        )
                        query_embedding = embed_response.data[0].embedding
                        
                        response = await asyncio.wait_for(
                            supabase_client.rpc(
                                "match_documents",
                                {"query_embedding": query_embedding, "match_count": match_count}
                            ).execute(),
                            timeout=5.0
                        )
                        
                        print(f"[{time.time()-t_rag_start:.2f}s] Supabase Vector Search ({match_count} chunks)")
                        
                        docs_data = response.data or []
                        if active_mode == "modo_praticar":
                            # Prioriza os 15 itens oficiais da rodada estruturada determinística
                            round_data = session_state.get("praticar_round")
                            loaded_ex_from_disk = False
                            if round_data and round_data.get("items"):
                                clean_rel = round_data.get("source", "")
                                context_items = [
                                    f"<!-- id: {it['id']} | dificuldade: {it['dificuldade']} -->\n### Questão {it['round_q']}/15 ({it['level_label']})\n{it['body']}\n**Gabarito:** {it['gabarito']}\n**Resolução:** {it['resolucao']}"
                                    for it in round_data["items"]
                                ]
                                docs_data = [{"metadata": {"source": clean_rel}, "content": "\n\n".join(context_items)}]
                                loaded_ex_from_disk = True
                            else:
                                top_src = docs_data[0].get("metadata", {}).get("source", "") if docs_data else ""
                                if top_src:
                                    ex_src = top_src if top_src.endswith("-exercicios.md") else (top_src[:-3] + "-exercicios.md" if top_src.endswith(".md") else "")
                                    clean_rel = ex_src.replace("../../", "")
                                    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
                                    candidate_paths = [os.path.join(project_root, clean_rel), ex_src, clean_rel, os.path.join("..", "..", clean_rel)]
                                    # Fallback: para capítulos do EM onde a lista de exercícios no mesmo diretório 'ebooks/' tem o slug do capítulo
                                    top_dir_rel = os.path.dirname(top_src.replace("../../", ""))
                                    abs_top_dir = os.path.join(project_root, top_dir_rel)
                                    if os.path.isdir(abs_top_dir):
                                        for fname in os.listdir(abs_top_dir):
                                            if fname.endswith("-exercicios.md"):
                                                candidate_paths.append(os.path.join(abs_top_dir, fname))
                                    for candidate in candidate_paths:
                                        if candidate and os.path.exists(candidate):
                                            try:
                                                with open(candidate, "r", encoding="utf-8") as ef:
                                                    full_ex_text = ef.read()
                                                # Extrai até 10 itens de cada nível (Básico=Fácil, Intermediário=Médio, Difícil=Difícil) para cobrir os 15 exercícios (5+5+5) com folga
                                                parts_ex = []
                                                for sec_header, sec_label in [
                                                    ("## Nível Básico", "## Nível Básico (Fácil — dificuldade: basico)"),
                                                    ("## Nível Intermediário", "## Nível Intermediário (Médio — dificuldade: intermediario)"),
                                                    ("## Nível Difícil", "## Nível Difícil (Difícil — dificuldade: dificil)")
                                                ]:
                                                    if sec_header in full_ex_text:
                                                        after_sec = full_ex_text.split(sec_header, 1)[1]
                                                        for next_h in ["## Nível Intermediário", "## Nível Difícil"]:
                                                            if next_h != sec_header and next_h in after_sec:
                                                                after_sec = after_sec.split(next_h, 1)[0]
                                                        q_blocks = after_sec.split("<!-- id: q")
                                                        selected_q = q_blocks[0] + "".join("<!-- id: q" + qb for qb in q_blocks[1:11])
                                                        parts_ex.append(f"{sec_label}\n{selected_q.strip()}")
                                                if parts_ex:
                                                    docs_data = [{"metadata": {"source": clean_rel}, "content": "\n\n".join(parts_ex)}]
                                                    loaded_ex_from_disk = True
                                                break
                                            except Exception:
                                                pass
                            if not loaded_ex_from_disk:
                                ex_docs = [
                                    d for d in docs_data
                                    if "-exercicios.md" in d.get("metadata", {}).get("source", "")
                                    or d.get("metadata", {}).get("chunk_type") == "exercicio"
                                    or "<!-- id: q" in d.get("content", "")
                                ]
                                if ex_docs:
                                    docs_data = ex_docs
                        elif active_mode in {"modo_aprender", "modo_resumir", "modo_revisar"}:
                            # Prioriza chunks teóricos do e-book (sem misturar listas de exercícios na teoria/microciclos)
                            theo_docs = [
                                d for d in docs_data
                                if not d.get("metadata", {}).get("source", "").endswith("-exercicios.md")
                                and d.get("metadata", {}).get("chunk_type") != "exercicio"
                            ]
                            if theo_docs:
                                docs_data = theo_docs
                            # Se o arquivo físico do e-book teórico existir em disco, carrega o e-book completo para garantir sequência integral dos microciclos
                            top_src = docs_data[0].get("metadata", {}).get("source", "") if docs_data else ""
                            if top_src:
                                eb_src = top_src[:-14] + ".md" if top_src.endswith("-exercicios.md") else top_src
                                clean_rel = eb_src.replace("../../", "")
                                project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
                                for candidate in [os.path.join(project_root, clean_rel), eb_src, clean_rel, os.path.join("..", "..", clean_rel)]:
                                    if candidate and os.path.exists(candidate) and not candidate.endswith("-exercicios.md"):
                                        try:
                                            with open(candidate, "r", encoding="utf-8") as ebf:
                                                full_eb_text = ebf.read()
                                            docs_data = [{"metadata": {"source": clean_rel}, "content": full_eb_text}]
                                            break
                                        except Exception:
                                            pass
                        
                        context_str = "\n\n".join([f"--- Contexto Recuperado ({d.get('metadata', {}).get('source', 'Apostila')}) ---\n{d.get('content', '')}" for d in docs_data])
                        
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
            dynamic_system_prompt += f"\n\n--- MATERIAL DE CONSULTA RELEVANTE PARA A PERGUNTA ATUAL ---\n{context_str}\n(Siga suas regras pedagógicas estritamente. Use este material apenas como base de conhecimento. Não complete lacunas com conhecimento externo.)"
            openai_messages[0]["content"] = dynamic_system_prompt
        elif active_mode in {"modo_aprender", "modo_praticar", "modo_revisar", "modo_resumir", "modo_resolve_questao"}:
            dynamic_system_prompt += "\n\n--- MATERIAL DE CONSULTA RELEVANTE PARA A PERGUNTA ATUAL ---\n[NENHUM MATERIAL RECUPERADO NO RAG PARA ESTE TEMA. Aplique estritamente a regra de Lacuna de Material: não preencha a lacuna com conhecimento externo, informe de forma simples a indisponibilidade e ofereça as alternativas do Menu de Trilhas.]"
            openai_messages[0]["content"] = dynamic_system_prompt

        google_contents.append({"role": "user", "parts": [{"text": llm_user_message}]})
        openai_messages.append({"role": "user", "content": llm_user_message})

        async def generate_stream():
            try:
                # 1. Enviar o session_id imediatamente no primeiro chunk
                yield f"data: {json.dumps({'session_id': current_session_id})}\n\n"
                
                # 2. Streaming Multi-LLM (DeepSeek Principal -> Gemini Fallback)
                t_start = time.time()
                full_text = ""
                
                try:
                    # Rota Principal: DeepSeek via DeepInfra (Fail-Fast)
                    max_toks = 8192 if active_mode in {"modo_aprender", "modo_resumir"} else 4096
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
                    max_toks = 8192 if active_mode in {"modo_aprender", "modo_resumir"} else 4096
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

        return StreamingResponse(generate_stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache, no-transform", "Connection": "keep-alive", "X-Accel-Buffering": "no"})

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
