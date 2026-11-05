# -*- coding: utf-8 -*-
"""
sentinela_mobme.py - Sentinela Noturno de Telemetria e Auditoria de Conversas
Executado diariamente na VPS Oracle Cloud via cron para auditar 100% das mensagens das últimas 24h.
Avalia:
- P0: Falhas de Roteamento e Bloqueio de Fluxo
- P1: Falhas de System Prompt e Desvios Pedagógicos
- P2: Falhas de Formatação e Renderização KaTeX
- P3: Sinais de Atrito e Frustração do Estudante
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

        s_audit = {
            "session_id": sid,
            "user": user_label,
            "title": title,
            "message_count": len(s_msgs),
            "created_at": s.get('created_at', ''),
            "issues": []
        }

        # Estado da conversa para detectar loops
        last_ai_menu = False

        for idx, m in enumerate(s_msgs):
            role = m.get('role')
            content = m.get('content', '')
            mid = m.get('id', '')
            msg_has_issue = False

            if role == 'ai':
                is_menu = "Como você prefere começar?" in content or "1. Aprender📚" in content
                
                # --- P0: FALHAS DE ROTEAMENTO E BLOQUEIO DE FLUXO ---
                # P0.1 Queda em disciplina "Indefinida"
                if "conteúdos de **indefinida**" in content.lower() or "disciplinas: ****" in content:
                    issue = {
                        "priority": "P0",
                        "type": "ROTEAMENTO_DISCIPLINA_INDEFINIDA",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "O sistema respondeu com disciplina 'Indefinida' ao estudante.",
                        "snippet": content[:200]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P0"].append(issue)
                    msg_has_issue = True

                # P0.2 Loop de Menu (Menu repetido em turnos consecutivos após input do aluno)
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

                # --- P1: FALHAS DE SYSTEM PROMPT E DESVIOS PEDAGÓGICOS ---
                # P1.1 Vazamento de Jargão Proibido ("microciclo" ou "miniciclo")
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

                # P1.2 Modo Aprender sem alternativas A-D (checagem aberta proibida)
                if "**Checagem:**" in content and not re.search(r'[a-dA-D]\)[ \t]+\S', content):
                    issue = {
                        "priority": "P1",
                        "type": "CHECAGEM_SEM_MULTIPLA_ESCOLHA",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "A checagem de compreensão foi apresentada sem as 4 alternativas obrigatórias (a, b, c, d).",
                        "snippet": content[content.find("**Checagem:**"):content.find("**Checagem:**")+250]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P1"].append(issue)
                    msg_has_issue = True

                # P1.3 Postura: Bajulação tóxica proibida
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

                # --- P2: FALHAS DE FORMATAÇÃO E RENDERIZAÇÃO KATEX ---
                # P2.1 Alternativas agrupadas na mesma linha
                if re.search(r'[a-dA-D]\)[^\n]+[b-eB-E]\)', content):
                    issue = {
                        "priority": "P2",
                        "type": "ALTERNATIVAS_AGRUPADAS",
                        "session_id": sid,
                        "msg_id": mid,
                        "turn": idx + 1,
                        "desc": "Alternativas de múltipla escolha coladas na mesma linha sem quebra dupla (\n\n).",
                        "snippet": [l for l in content.split('\n') if re.search(r'[a-dA-D]\)[^\n]+[b-eB-E]\)', l)][:2]
                    }
                    s_audit["issues"].append(issue)
                    issues_by_priority["P2"].append(issue)
                    msg_has_issue = True

                # P2.2 Subscrito duplo KaTeX sem chaves
                if re.search(r'_[a-zA-Z0-9]+_[a-zA-Z0-9]+', content):
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

                # P2.3 Gabarito em negrito no feedback formatado como **c) ...** sem 'Gabarito:'
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
                # --- P3: MINERAÇÃO DE ATRITO E SENTIMENTO DO ESTUDANTE ---
                low_c = content.lower()
                friction_cues = [
                    "não entendi", "muito avançado", "muito difícil", "você errou", 
                    "não é isso", "pulou", "não pedi isso", "travou", "bug", "tá errado"
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
    md_lines.append(f"  - 🚨 **P0 (Crítica / Roteamento):** {p0_count}")
    md_lines.append(f"  - 🔥 **P1 (Alta / System Prompt):** {p1_count}")
    md_lines.append(f"  - ⚠️ **P2 (Média / Formatação KaTeX):** {p2_count}")
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
        # Tenta /app/auditorias (no container) ou scratch/auditorias (local)
        output_dir = "/app/auditorias" if os.path.exists("/app") else "scratch/auditorias"
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
