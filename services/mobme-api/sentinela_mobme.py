# -*- coding: utf-8 -*-
"""
sentinela_mobme.py - Sentinela Noturno de Telemetria e Auditoria de Conversas
Executado diariamente na VPS Oracle Cloud via cron para auditar 100% das mensagens das últimas 24h.
Avalia:
- P0: Falhas Críticas de Roteamento, Bloqueio de Fluxo, Desambiguação e RAG Cruzado
- P1: Falhas Altas de System Prompt, Gaslighting Pedagógico, Amnésia de Tema e Postura
- P2: Falhas Médias de Formatação KaTeX, Excesso de Alternativas e Botões Falsos
- P3: Mineração de Frustração, Atrito e Sinais Diretos do Estudante
Calcula Intervalos de Confiança de Wilson a 95% para conformidade estatística.
"""

import asyncio
import os
import sys
import re
import json
import math
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from supabase.client import create_async_client

sys.stdout.reconfigure(encoding='utf-8')

# Localizar .env
env_paths = [
    'services/mobme-api/.env',
    '🚀 Educamob - DevOps e Infra/services/mobme-api/.env',
    '/app/.env',
    '.env'
]
for p in env_paths:
    if os.path.exists(p):
        load_dotenv(p)
        break

def wilson_ci_95(successes: int, total: int):
    """Calcula o Intervalo de Confiança de Wilson (95%) para taxas binárias."""
    if total == 0:
        return (0.0, 0.0, 0.0)
    z = 1.96
    phat = successes / total
    denom = 1 + (z ** 2) / total
    center = (phat + (z ** 2) / (2 * total)) / denom
    half_width = (z * math.sqrt((phat * (1 - phat) / total) + ((z ** 2) / (4 * (total ** 2))))) / denom
    low = max(0.0, center - half_width)
    high = min(1.0, center + half_width)
    return (round(phat * 100, 2), round(low * 100, 2), round(high * 100, 2))

# ==============================================================================
# DICIONÁRIOS CURRICULARES E DETECTOR SEMÂNTICO DE ALINHAMENTO DE HABILIDADES
# ==============================================================================
DOMAIN_KEYWORDS = {
    "Física": [
        "força", "newton", "pressão", "fluido", "empuxo", "pascal", "stevin", "arquimedes",
        "velocidade", "aceleração", "cinética", "potencial", "gravidade", "massa", "dinâmica",
        "atrito", "energia mecânica", "hidrostática", "densidade", "trabalho", "calor", "óptica"
    ],
    "Química": [
        "átomo", "elétron", "próton", "tabela periódica", "oxidação", "redução", "nox",
        "ligação", "ácido", "base", "sal", "óxido", "estequiometria", "reação", "solução",
        "massa molar", "eletronegatividade", "raio atômico", "energia de ionização", "afinidade"
    ],
    "Matemática": [
        "equação", "função", "triângulo", "seno", "cosseno", "tangente", "geometria",
        "porcentagem", "fração", "razão", "proporção", "juros", "desconto", "quadrante",
        "matriz", "probabilidade", "estatística", "logaritmo", "polinômio", "progressão"
    ],
    "História": [
        "guerra", "revolução", "império", "século", "república", "monarquia", "feudalismo",
        "escravidão", "colonial", "tratado", "presidente", "ditadura", "constituição", "nazismo"
    ],
    "Geografia": [
        "relevo", "clima", "vegetação", "bioma", "hidrografia", "cartografia", "urbanização",
        "migração", "placas tectônicas", "globalização", "demografia", "geopolítica", "solo"
    ],
    "Ciências": [
        "célula", "fotossíntese", "ecossistema", "espécie", "evolução", "genética", "tecido",
        "vírus", "bactéria", "reprodução", "cadeia alimentar", "seres vivos", "organismo"
    ]
}

DISCIPLINE_BNCC_PREFIXES = {
    "Matemática": ["MA", "MAT"],
    "Física": ["CNT", "FIS"],
    "Química": ["CNT", "QUI"],
    "Ciências": ["CI", "CNT"],
    "História": ["HI", "CHS"],
    "Geografia": ["GE", "CHS"]
}

def infer_topic_discipline(topic: str) -> str:
    if not topic:
        return None
    top_low = topic.lower()
    for disc, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in top_low for kw in keywords):
            return disc
    return None

def check_skill_alignment(session_topic: str, session_disc: str, content: str, round_item: dict = None, round_source: str = None) -> tuple[bool, str]:
    """
    Valida rigorosamente o alinhamento curricular entre a questão entregue e o tema/disciplina da sessão.
    Retorna (True, motivo) se for detectada incompatibilidade de habilidade ou disciplina cruzada.
    """
    disc = session_disc or infer_topic_discipline(session_topic)
    if not disc and not session_topic:
        return False, ""

    # 1. Checagem por metadados de arquivo de origem (source path em session_states.json)
    if round_source and disc:
        m_src = re.search(r'content/[^/]+/[^/]+/([^/]+)/', round_source.replace('\\', '/').lower())
        if m_src:
            src_disc_slug = m_src.group(1)
            disc_slug_map = {
                "fisica": "Física", "quimica": "Química", "matematica": "Matemática",
                "historia": "História", "geografia": "Geografia", "ciencias": "Ciências"
            }
            mapped_src_disc = disc_slug_map.get(src_disc_slug)
            if mapped_src_disc and mapped_src_disc != disc:
                return True, f"Questão originada do acervo de '{mapped_src_disc}' ({round_source}) entregue em sessão de '{disc}' ('{session_topic}')."

    # 2. Checagem por metadados do item (habilidade BNCC oficial e objeto)
    if round_item:
        hab = round_item.get("habilidade", "").upper()
        obj = round_item.get("objeto", "")
        m_bncc = re.search(r'EF\d{2}([A-Z]{2})|EM13([A-Z]{3})', hab)
        if m_bncc and disc:
            code_disc = m_bncc.group(1) or m_bncc.group(2)
            allowed_prefixes = DISCIPLINE_BNCC_PREFIXES.get(disc, [])
            if code_disc and allowed_prefixes and code_disc not in allowed_prefixes:
                return True, f"Questão com habilidade oficial '{hab}' ({code_disc}) não pertence à disciplina '{disc}' da sessão ('{session_topic}'). Objeto: '{obj}'."
        
        # Mismatch de série curricular (ex: Fundamental 1 em Ensino Médio)
        if any(hab.startswith(f"EF0{i}") for i in range(1, 6)):
            if disc in ["Física", "Química"] or any(t in (session_topic or "").lower() for t in ["médio", "medio", "pascal", "stevin", "termodinâmica", "funções orgânicas", "1ª série", "1-serie"]):
                return True, f"Questão de habilidade do Fundamental 1 ('{hab}' - '{obj}') entregue em sessão de nível médio incompatível ('{session_topic}')."

    # 3. Checagem por menção direta de código BNCC no texto
    m_text_bncc = re.search(r'\b(EF\d{2}[A-Z]{2}\d{2}|EM13[A-Z]{3}\d{3})\b', content)
    if m_text_bncc:
        code_str = m_text_bncc.group(1).upper()
        m_code = re.search(r'EF\d{2}([A-Z]{2})|EM13([A-Z]{3})', code_str)
        if m_code and disc:
            code_disc = m_code.group(1) or m_code.group(2)
            allowed_prefixes = DISCIPLINE_BNCC_PREFIXES.get(disc, [])
            if code_disc and allowed_prefixes and code_disc not in allowed_prefixes:
                return True, f"Código de habilidade BNCC '{code_str}' no texto não pertence à disciplina '{disc}' do tema '{session_topic}'."

    # 4. Checagem Semântica de Conteúdo da Questão vs Disciplina/Tema
    if disc:
        low_content = content.lower()
        if disc in ["Física", "Química"]:
            math_elem = ["porcentagem de 100%", "razão centesimal", "grade de 100 quadradinhos", "taxa percentual", "desconto de 20%", "quadrante da grade", "ef05ma", "ef06ma"]
            if any(term in low_content for term in math_elem):
                return True, f"Questão de habilidade elementar de Matemática/Porcentagem entregue em sessão de {disc} ('{session_topic}')."
            hist_elem = ["segunda guerra mundial", "trincheiras da guerra", "atentado de sarajevo", "revolução francesa", "era vargas"]
            if any(term in low_content for term in hist_elem):
                return True, f"Questão de habilidade de História entregue em sessão de {disc} ('{session_topic}')."

        elif disc == "História":
            phys_elem = ["calcule a velocidade", "aceleração média", "força resultante em newtons", "empuxo hidrostático"]
            if any(term in low_content for term in phys_elem):
                return True, f"Questão de habilidade de Física entregue em sessão de História ('{session_topic}')."

        elif disc == "Matemática":
            bio_elem = ["mitocôndria", "fotossíntese celular", "ribossomos", "cadeia alimentar ecológica"]
            if any(term in low_content for term in bio_elem):
                return True, f"Questão de habilidade de Ciências/Biologia entregue em sessão de Matemática ('{session_topic}')."

    return False, ""

async def run_sentinel_audit(hours: int = 24, output_dir: str = None):
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')
    if not url or not key:
        print("[SENTINELA] ERRO: Credenciais do Supabase não encontradas no ambiente (.env).")
        return None

    supabase = await create_async_client(url, key)
    
    # Janela de tempo auditada
    now_utc = datetime.now(timezone.utc)
    cutoff_time = (now_utc - timedelta(hours=hours)).isoformat()
    audit_date_str = now_utc.strftime("%Y-%m-%d")
    
    print(f"[SENTINELA] Iniciando auditoria para janela de {hours}h (desde {cutoff_time})...")

    # 1. Carregar mapeamento de usuários beta se existir
    user_map = {}
    csv_candidates = [
        'services/mobme-api/beta_testers.csv',
        '🚀 Educamob - DevOps e Infra/services/mobme-api/beta_testers.csv',
        '/app/beta_testers.csv'
    ]
    for cp in csv_candidates:
        if os.path.exists(cp):
            import csv
            try:
                with open(cp, 'r', encoding='utf-8', errors='ignore') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        uid = row.get('id') or row.get('user_id')
                        name = row.get('nome') or row.get('email')
                        if uid and name:
                            user_map[uid] = name
            except Exception:
                pass
            break

    # Tenta carregar também via auth admin se tiver privilégio
    try:
        auth_users = await supabase.auth.admin.list_users()
        for u in auth_users:
            uid = getattr(u, 'id', None) or (u.get('id') if isinstance(u, dict) else '')
            meta = getattr(u, 'user_metadata', {}) or (u.get('user_metadata', {}) if isinstance(u, dict) else {})
            name = meta.get('full_name') or meta.get('name') or getattr(u, 'email', '')
            if uid and name:
                user_map[uid] = name
    except Exception:
        pass

    # 2. Coletar Sessões e Mensagens
    sessions_resp = await supabase.table('chat_sessions').select('*').gte('created_at', cutoff_time).order('created_at', desc=False).execute()
    sessions = sessions_resp.data or []

    msgs_resp = await supabase.table('messages').select('*').gte('created_at', cutoff_time).order('created_at', desc=False).execute()
    all_msgs = msgs_resp.data or []

    msgs_by_session = {}
    for m in all_msgs:
        sid = m.get('session_id')
        msgs_by_session.setdefault(sid, []).append(m)

    total_sessions = len(sessions)
    total_messages = len(all_msgs)
    ai_messages = [m for m in all_msgs if m.get('role') == 'ai']
    total_ai_msgs = len(ai_messages)

    print(f"[SENTINELA] Coletadas {total_sessions} sessões ativas e {total_messages} mensagens ({total_ai_msgs} da IA).")

    # 3. Auditoria Forense por Sessão
    session_audits = []
    issues_by_priority = {"P0": [], "P1": [], "P2": [], "P3": []}
    clean_ai_msgs_count = 0

    # Carregar cache de estados de sessão (session_states.json) para conferência de habilidades e acervo
    session_states_cache = {}
    for ssp in [
        '/app/session_states.json',
        'services/mobme-api/session_states.json',
        '🚀 Educamob - DevOps e Infra/services/mobme-api/session_states.json',
        'session_states.json'
    ]:
        if os.path.exists(ssp):
            try:
                with open(ssp, 'r', encoding='utf-8') as sf:
                    session_states_cache = json.load(sf)
                break
            except Exception:
                pass

    TOXIC_PRAISE = [
        "parabéns, você é genial", "espetacular!", "maravilhoso!", "sensacional!",
        "você é incrível", "perfeito, você é brilhante"
    ]

    for s in sessions:
        sid = s['id']
        uid = s.get('user_id', 'unknown')
        user_label = user_map.get(uid, uid[:8] if uid else "Anônimo")
        title = s.get('title', 'Sem título')
        s_msgs = msgs_by_session.get(sid, [])
        if not s_msgs:
            continue

        st_info = session_states_cache.get(sid, {})
        pr_round = st_info.get("praticar_round", {})
        round_items = pr_round.get("items", [])
        round_source = pr_round.get("source", "")

        s_audit = {
            "session_id": sid,
            "user": user_label,
            "title": title,
            "message_count": len(s_msgs),
            "created_at": s.get('created_at', ''),
            "issues": []
        }

        # Estado da conversa para rastrear fluxo inter-turnos
        last_ai_menu = False
        last_ai_disambiguation = False
        last_user_content = ""
        session_topic = None

        for idx, m in enumerate(s_msgs):
            role = m.get('role')
            content = m.get('content', '')
            mid = m.get('id', '')
            msg_has_issue = False

            if role == 'ai':
                is_menu = ("Como você prefere começar?" in content or "Qual caminho você prefere agora?" in content) and len(content.strip()) < 450
                is_disambig = (
                    ("qual desses caminhos é o seu foco" in content.lower() or 
                     "em qual foco você quer se aprofundar" in content.lower() or
                     ("1️⃣" in content and "2️⃣" in content and any(w in content.lower() for w in ["foco", "amplo", "caminhos", "ramificações"])))
                    and not is_menu
                )

                # Rastrear se a IA definiu tema formalmente
                m_top = re.search(r"Tema definido:\s*\*\*([^\*]+)\*\*", content)
                if m_top:
                    session_topic = m_top.group(1).strip()
                elif title and title not in {"Saudação inicial", "Saudação informal", "Sem título", "None"}:
                    if not session_topic:
                        session_topic = title

                # ==============================================================
                # --- P0: FALHAS CRÍTICAS DE ROTEAMENTO, BLOQUEIO E RAG CRUZADO ---
                # ==============================================================
                
                # P0.1 Colisão de Menu em Desambiguação de Assuntos (A falha prioritária apontada pelo usuário)
                if last_ai_disambiguation and last_user_content:
                    user_chose_number = re.match(r"^([1-5]|1️⃣|2️⃣|3️⃣|4️⃣|5️⃣|\bopção\s+[1-5]\b|\b[1-5]\.|\b[1-5]\))", last_user_content, re.IGNORECASE)
                    if user_chose_number:
                        # Se a IA respondeu ativando uma trilha do menu principal sem confirmar o tema, ou caiu em questão/flashcard direto:
                        if ("Você escolheu a trilha de" in content or 
                            "📝 Questão 1/15" in content or 
                            "🃏 Flashcard" in content or 
                            ("Como você prefere começar?" in content and not m_top) or
                            ("Para montar os exercícios certinhos, me diga" in content and not m_top)):
                            issue = {
                                "priority": "P0",
                                "type": "DESAMBIGUACAO_COLISAO_MENU",
                                "session_id": sid,
                                "msg_id": mid,
                                "turn": idx + 1,
                                "desc": f"Aluno escolheu a opção '{last_user_content}' na desambiguação de temas, mas o sistema colidiu o número com as opções do menu principal.",
                                "snippet": f"Input do Aluno: '{last_user_content}' -> Resposta da IA: '{content[:180].replace(chr(10), ' ')}'"
                            }
                            s_audit["issues"].append(issue)
                            issues_by_priority["P0"].append(issue)
                            msg_has_issue = True

                # P0.2 Falso Bloqueio de Disciplina Homologada ("ainda não atendo conteúdos de Física")
                m_falso = re.search(r"ainda não atendo conteúdos de \*\*(Física|Matemática|Química|Ciências|História|Geografia|Cálculo 1)\*\*", content, re.IGNORECASE)
                if m_falso:
                    issue = {
                        "priority": "P0",
                        "type": "FALSO_BLOQUEIO_DISCIPLINA",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": f"O sistema disparou bloqueio indevido afirmando não atender a disciplina homologada: '{m_falso.group(1)}'.",
                        "snippet": content[:200]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P0"].append(issue)
                    msg_has_issue = True

                # P0.3 RAG com Injeção de Disciplina Cruzada / Habilidade Incompatível com o Tema
                if "📝 Questão" in content or "**Checagem:**" in content:
                    item_obj = None
                    m_q = re.search(r"Quest[aã]o\s+(\d+)/15", content, re.IGNORECASE)
                    if m_q and round_items:
                        q_idx = int(m_q.group(1)) - 1
                        if 0 <= q_idx < len(round_items):
                            item_obj = round_items[q_idx]

                    is_mismatch, reason = check_skill_alignment(session_topic, s.get('discipline'), content, item_obj, round_source)
                    if is_mismatch:
                        issue = {
                            "priority": "P0",
                            "type": "RAG_DISCIPLINA_CRUZADA",
                            "session_id": sid,
                            "msg_id": mid,
                            "turn": idx + 1,
                            "desc": reason,
                            "snippet": content[:220]
                        }
                        s_audit["issues"].append(issue)
                        issues_by_priority["P0"].append(issue)
                        msg_has_issue = True

                # P0.4 Queda em disciplina "Indefinida" ou "Não identificada"
                if "conteúdos de **indefinida**" in content.lower() or "conteúdos de **não identificada**" in content.lower() or "disciplinas: ****" in content:
                    issue = {
                        "priority": "P0",
                        "type": "ROTEAMENTO_DISCIPLINA_INDEFINIDA",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "O sistema respondeu com disciplina 'Indefinida' ou 'Não identificada' ao estudante.",
                        "snippet": content[:200]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P0"].append(issue)
                    msg_has_issue = True

                # P0.5 Loop de Menu (Menu repetido em turnos consecutivos após input do aluno)
                if is_menu and last_ai_menu:
                    issue = {
                        "priority": "P0",
                        "type": "MENU_EM_LOOP",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "O Menu de Trilhas foi exibido repetidamente em turnos consecutivos sem avanço.",
                        "snippet": content[:150]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P0"].append(issue)
                    msg_has_issue = True

                last_ai_menu = is_menu
                last_ai_disambiguation = is_disambig

                # ==============================================================
                # --- P1: FALHAS ALTAS DE SYSTEM PROMPT E CONDUTA PEDAGÓGICA ---
                # ==============================================================

                # P1.5 Dump Massivo de Exercícios no Chat (Quebra de Interatividade)
                q_matches = len(re.findall(r"(?:\*\*Quest[ãa]o\s*\d+\*\*|📝 Questão)", content))
                if q_matches > 2:
                    issue = {
                        "priority": "P1",
                        "type": "DUMP_EXERCICIOS_CHAT",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": f"A IA despejou {q_matches} questões em um único turno no chat, violando o princípio socrático unitário.",
                        "snippet": content[:180]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # P1.1 Gaslighting Pedagógico (IA justificando entrega errada como se a sessão fosse de outra matéria)
                if (("esta é uma sessão de prática de" in content.lower() and "e não sobre" in content.lower()) or 
                    ("as questões que apresentei são de" in content.lower() and "não fazem parte do material" in content.lower())):
                    issue = {
                        "priority": "P1",
                        "type": "GASLIGHTING_PEDAGOGICO",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "A IA tentou justificar a entrega de questão errada afirmando que a sessão era de outra matéria ou culpando o acervo.",
                        "snippet": content[:220]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # P1.2 Amnésia de Tema na Mesma Sessão
                if session_topic and any(phrase in content.lower() for phrase in [
                    "qual é o assunto específico que você quer praticar hoje?",
                    "qual é o assunto específico que você quer revisar hoje?",
                    "qual conteúdo você quer aprender?",
                    "qual é o assunto específico que você quer"
                ]):
                    issue = {
                        "priority": "P1",
                        "type": "AMNESIA_TEMA_SESSAO",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": f"A IA perdeu a memória do tema ativo '{session_topic}' e voltou a perguntar o assunto ao aluno.",
                        "snippet": content[:200]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # P1.3 Vazamento de Jargão Proibido ("microciclo" ou "miniciclo")
                if re.search(r'\b(microciclo|miniciclo)s?\b', content, re.IGNORECASE):
                    issue = {
                        "priority": "P1",
                        "type": "JARGON_PROIBIDO",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "Uso indevido das palavras proibidas 'microciclo' ou 'miniciclo'.",
                        "snippet": [l for l in content.split('\n') if re.search(r'\b(microciclo|miniciclo)s?\b', l, re.IGNORECASE)][:2]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # P1.4 Modo Aprender sem alternativas A-E (checagem aberta proibida)
                if "**Checagem:**" in content and not re.search(r'[a-eA-E]\)[ \t]+\S', content):
                    issue = {
                        "priority": "P1",
                        "type": "CHECAGEM_SEM_MULTIPLA_ESCOLHA",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "A checagem de compreensão foi apresentada sem as 5 alternativas obrigatórias (a, b, c, d, e).",
                        "snippet": content[content.find("**Checagem:**"):content.find("**Checagem:**")+250]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # P1.5 Postura: Bajulação tóxica proibida
                if any(tp in content.lower() for tp in TOXIC_PRAISE):
                    issue = {
                        "priority": "P1",
                        "type": "BAJULACAO_TOXICA",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "Uso de comemorações extravagantes ou bajulação proibida pelas regras de postura.",
                        "snippet": content[:180]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # ==============================================================
                # --- P2: FALHAS MÉDIAS DE FORMATAÇÃO E TELEMETRIA DO QUIZ ---
                # ==============================================================

                # P2.1 Padrão Oficial Unificado de 5 Alternativas (A-E Obrigatório)
                # Toda questão oficial ("📝 Questão") e checagem teórica ("**Checagem:**") DEVE ter exatamente 5 alternativas (a, b, c, d, e).
                if ("📝 Questão" in content or "**Checagem:**" in content or bool(re.search(r"\*\*Quest[ãa]o\s*\d+\*\*", content))):
                    has_options = bool(re.search(r'(?:^|\n)\s*[a-dA-D]\)', content))
                    has_opt_e = bool(re.search(r'(?:^|\n)\s*[eE]\)', content))
                    has_opt_f = bool(re.search(r'(?:^|\n)\s*[f-zF-Z]\)', content))

                    if has_options and not has_opt_e:
                        issue = {
                            "priority": "P2",
                            "type": "DEFICIT_ALTERNATIVAS_PADRAO_5",
                            "session_id": sid,
                            "msg_id": mid,
                            "turn": idx + 1,
                            "desc": "A questão/checagem foi entregue com menos de 5 alternativas, violando o padrão oficial unificado da plataforma (a-e).",
                            "snippet": [l.strip() for l in content.split('\n') if re.search(r'^\s*[a-eA-E]\)', l.strip())][:5]
                        }
                        s_audit["issues"].append(issue)
                        issues_by_priority["P2"].append(issue)
                        msg_has_issue = True
                    elif has_opt_f:
                        issue = {
                            "priority": "P2",
                            "type": "EXCESSO_ALTERNATIVAS_QUIZ",
                            "session_id": sid,
                            "msg_id": mid,
                            "turn": idx + 1,
                            "desc": "A questão/checagem foi entregue com mais de 5 alternativas (ultrapassando o padrão oficial A-E).",
                            "snippet": [l.strip() for l in content.split('\n') if re.search(r'^\s*[a-zA-Z]\)', l.strip())][:7]
                        }
                        s_audit["issues"].append(issue)
                        issues_by_priority["P2"].append(issue)
                        msg_has_issue = True

                # P2.2 Alternativas agrupadas na mesma linha (Limpando KaTeX e temperaturas para evitar falsos positivos como (0°C))
                clean_no_katex = re.sub(r'\$\$.*?\$\$', '', content, flags=re.DOTALL)
                clean_no_katex = re.sub(r'\$.*?\$', '', clean_no_katex)
                clean_no_katex = re.sub(r'\(?\s*[\d\.,]+\s*°\s*[a-zA-Z]\s*\)?', '', clean_no_katex)
                clean_no_katex = re.sub(r'\(?\s*°\s*[a-zA-Z]\s*\)?', '', clean_no_katex)
                if re.search(r'(?:^|\s)[a-dA-D]\)\s+[^\n]+?(?<=\s)[b-eB-E]\)\s+', clean_no_katex):
                    issue = {
                        "priority": "P2",
                        "type": "ALTERNATIVAS_AGRUPADAS",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "Alternativas de múltipla escolha coladas na mesma linha sem quebra dupla (\n\n).",
                        "snippet": [l for l in clean_no_katex.split('\n') if re.search(r'(?:^|\s)[a-dA-D]\)\s+[^\n]+?(?<=\s)[b-eB-E]\)\s+', l)][:2]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P2"].append(issue)
                    msg_has_issue = True

                # P2.3 Subscrito duplo KaTeX sem chaves
                if re.search(r'_[a-zA-Z0-9]+_[a-zA-Z0-9]+', content) and not re.search(r'\$[A-Z][a-z]?_\d+[A-Z][a-z]?_\d+', content):
                    issue = {
                        "priority": "P2",
                        "type": "KATEX_DOUBLE_SUBSCRIPT",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "Subscrito duplo KaTeX sem chaves protetoras que gera erro de render.",
                        "snippet": [l for l in content.split('\n') if re.search(r'_[a-zA-Z0-9]+_[a-zA-Z0-9]+', l)][:2]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P2"].append(issue)
                    msg_has_issue = True

                # P2.4 Gabarito em negrito no feedback formatado como **c) ...** sem 'Gabarito:'
                if re.search(r'(?:^|\n)\s*\*\*([a-eA-E]\)[^\n]+)\*\*', content) and "Gabarito:" not in content and "✅" not in content:
                    issue = {
                        "priority": "P2",
                        "type": "GABARITO_FEEDBACK_BOTAO_FALSO",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "Resposta de feedback em negrito que pode ser interpretada como botão falso de quiz.",
                        "snippet": [l for l in content.split('\n') if re.search(r'(?:^|\n)\s*\*\*([a-eA-E]\)[^\n]+)\*\*', l)][:2]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P2"].append(issue)
                    msg_has_issue = True

                if not msg_has_issue:
                    clean_ai_msgs_count += 1

            elif role == 'user':
                last_user_content = content.strip()
                # --- P3: MINERAÇÃO DE ATRITO E SENTIMENTO DO ESTUDANTE ---
                low_c = content.lower()
                friction_cues = [
                    "não entendi", "muito avançado", "muito difícil", "você errou", 
                    "não é isso", "pulou", "não pedi isso", "travou", "bug", "tá errado",
                    "o que isso tem a ver", "o que isso tem haver", "essas questoes nao sao",
                    "vai direto ao assunto", "mds", "meu deus", "enrola", "enrolando", "enrolação", "só falou quatro"
                ]
                for cue in friction_cues:
                    if cue in low_c:
                        issue = {
                            "priority": "P3",
                            "type": "ATRITO_ESTUDANTE",
                            "session_id": sid,
                            "msg_id": mid,
                            "turn": idx + 1,
                            "desc": f"Sinal de frustração ou correção direta feita pelo estudante: '{cue}'",
                            "snippet": content
                        }
                        s_audit["issues"].append(issue)
                        issues_by_priority["P3"].append(issue)
                        break

        session_audits.append(s_audit)

    # ==============================================================
    # --- AUDITORIA DE USUÁRIO: SESSÕES ABORTADAS EM CASCATA ---
    # ==============================================================
    user_sessions = {}
    for s in sessions:
        uid = s.get('user_id')
        if uid:
            user_sessions.setdefault(uid, []).append(s)

    for uid, u_sess in user_sessions.items():
        if len(u_sess) >= 3:
            sorted_s = sorted(u_sess, key=lambda x: x.get('created_at', ''))
            for i in range(len(sorted_s) - 2):
                s1, s2, s3 = sorted_s[i], sorted_s[i+1], sorted_s[i+2]
                m_count1 = len(msgs_by_session.get(s1['id'], []))
                m_count2 = len(msgs_by_session.get(s2['id'], []))
                m_count3 = len(msgs_by_session.get(s3['id'], []))
                if m_count1 <= 10 and m_count2 <= 10 and m_count3 <= 10:
                    try:
                        t1 = datetime.fromisoformat(s1['created_at'].replace('Z', '+00:00'))
                        t3 = datetime.fromisoformat(s3['created_at'].replace('Z', '+00:00'))
                        diff_mins = (t3 - t1).total_seconds() / 60
                        if diff_mins <= 45:
                            u_name = user_map.get(uid, uid[:8])
                            issue = {
                                "priority": "P0",
                                "type": "SESSAO_ABORTADA_CASCATA",
                                "session_id": s3['id'],
                                "turn": 1,
                                "desc": f"Estudante '{u_name}' abandonou e recriou 3 sessões consecutivas em {int(diff_mins)} minutos (Sessões `{s1['id'][:8]}`, `{s2['id'][:8]}`, `{s3['id'][:8]}`), evidenciando travamento ou frustração severa.",
                                "snippet": f"Títulos das sessões abandonadas: '{s1.get('title')}', '{s2.get('title')}', '{s3.get('title')}'"
                            }
                            issues_by_priority["P0"].append(issue)
                            break
                    except Exception:
                        pass

    # 4. Cálculo Estatístico com Intervalo de Confiança de Wilson 95%
    p_global, ci_low, ci_high = wilson_ci_95(clean_ai_msgs_count, total_ai_msgs)
    
    # Taxas por prioridade
    p0_count = len(issues_by_priority["P0"])
    p1_count = len(issues_by_priority["P1"])
    p2_count = len(issues_by_priority["P2"])
    p3_count = len(issues_by_priority["P3"])
    total_issues = p0_count + p1_count + p2_count + p3_count

    stats = {
        "audit_timestamp": now_utc.isoformat(),
        "audit_date": audit_date_str,
        "hours_covered": hours,
        "total_sessions": total_sessions,
        "total_messages": total_messages,
        "total_ai_messages": total_ai_msgs,
        "clean_ai_messages": clean_ai_msgs_count,
        "total_issues": total_issues,
        "issues_by_priority": {
            "P0_critica_roteamento": p0_count,
            "P1_alta_system_prompt": p1_count,
            "P2_media_formatacao_katex": p2_count,
            "P3_atrito_estudante": p3_count
        },
        "statistical_metrics": {
            "prompt_compliance_rate_pct": p_global,
            "wilson_ci_95_low_pct": ci_low,
            "wilson_ci_95_high_pct": ci_high,
            "statistically_sound": total_ai_msgs >= 30,
            "target_threshold_pct": 98.0
        }
    }

    # 5. Montagem do Relatório Markdown
    md_lines = []
    md_lines.append(f"# Dossiê Forense de Auditoria Noturna da Mob.me — {audit_date_str}")
    md_lines.append(f"> **Gerado em:** {now_utc.strftime('%d/%m/%Y às %H:%M:%S UTC')} | **Janela:** Últimas {hours} horas")
    md_lines.append(f"> **Métricas:** {total_sessions} sessões | {total_messages} mensagens | {total_ai_msgs} respostas da IA\n")

    md_lines.append("## 1. Confiabilidade Estatística e Conformidade (Wilson 95%)\n")
    md_lines.append(f"- **Taxa de Conformidade Geral do System Prompt:** **{p_global}%**")
    md_lines.append(f"- **Intervalo de Confiança de Wilson (95%):** `[{ci_low}% — {ci_high}%]`")
    md_lines.append(f"- **Total de Falhas Detectadas:** {total_issues}")
    md_lines.append(f"  - 🚨 **P0 (Crítica / Roteamento & RAG):** {p0_count}")
    md_lines.append(f"  - 🔥 **P1 (Alta / System Prompt & Conduta):** {p1_count}")
    md_lines.append(f"  - ⚠️ **P2 (Média / Formatação & Quiz):** {p2_count}")
    md_lines.append(f"  - 💬 **P3 (Sinais de Atrito Aluno):** {p3_count}\n")

    md_lines.append("## 2. Sumário das Falhas por Ordem de Prioridade\n")
    if total_issues == 0:
        md_lines.append("🏆 **Nenhuma falha detectada! A plataforma operou com 100% de conformidade nas últimas 24 horas.**\n")
    else:
        for prio in ["P0", "P1", "P2", "P3"]:
            items = issues_by_priority[prio]
            if not items:
                continue
            md_lines.append(f"### Prioridade {prio} ({len(items)} ocorrência(s))\n")
            for it in items:
                md_lines.append(f"- **[{it['type']}]** (Sessão `{it['session_id'][:8]}` - Turno {it['turn']}): {it['desc']}")
                if 'snippet' in it and it['snippet']:
                    if isinstance(it['snippet'], list):
                        for s in it['snippet']:
                            md_lines.append(f"  > `{s.strip()}`")
                    else:
                        md_lines.append(f"  > `{str(it['snippet']).strip()}`")
            md_lines.append("")

    # 6. Salvar em Disco
    if not output_dir:
        output_dir = "/app/auditorias" if os.path.exists("/app/auditorias") else "scratch/auditorias"
    os.makedirs(output_dir, exist_ok=True)

    json_path = os.path.join(output_dir, f"auditoria_{audit_date_str}.json")
    md_path = os.path.join(output_dir, f"auditoria_{audit_date_str}.md")
    latest_json = os.path.join(output_dir, "latest.json")
    latest_md = os.path.join(output_dir, "latest.md")

    full_payload = {
        "stats": stats,
        "issues_by_priority": issues_by_priority,
        "sessions": session_audits
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(full_payload, f, ensure_ascii=False, indent=2)
    with open(latest_json, 'w', encoding='utf-8') as f:
        json.dump(full_payload, f, ensure_ascii=False, indent=2)

    report_markdown = "\n".join(md_lines)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(report_markdown)
    with open(latest_md, 'w', encoding='utf-8') as f:
        f.write(report_markdown)

    print(f"[SENTINELA] Auditoria concluída com sucesso!")
    print(f"[SENTINELA] Conformidade: {p_global}% (IC 95%: [{ci_low}%, {ci_high}%]) | Falhas: {total_issues}")
    print(f"[SENTINELA] Dossiê salvo em: {json_path} e {md_path}")
    return full_payload

if __name__ == "__main__":
    asyncio.run(run_sentinel_audit())
