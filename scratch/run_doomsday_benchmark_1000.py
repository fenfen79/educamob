import asyncio
import json
import time
import sys
import os
import re
import math
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

# Forçar stdout UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Adicionar o path da API
sys.path.insert(0, os.path.abspath('services/mobme-api'))

import main
from main import app, lifespan, chat_endpoint, ChatRequest
from fastapi import BackgroundTasks

TEST_USER_ID = "00000000-0000-0000-0000-000000000001"

def wilson_score_interval(successes, total, confidence=0.95):
    if total == 0:
        return 0.0, 0.0
    z = 1.95996  # 95% confidence
    p = successes / total
    denom = 1 + z**2 / total
    centre = (p + z**2 / (2 * total)) / denom
    diff = (z / denom) * math.sqrt(p * (1 - p) / total + z**2 / (4 * total**2))
    return max(0.0, centre - diff), min(1.0, centre + diff)

def audit_turn_content(cluster, track, user_msg, ai_text):
    issues = []
    
    # 1. Bajulação Superlativa em 2ª pessoa (P1)
    if re.search(r'\bvocê\s+(?:está|é|foi)\s+(?:voando|arrasando|brilhando|incrível|um\s+gênio|demais|show|destruindo|imbatível)', ai_text, re.IGNORECASE):
        issues.append("BAJULACAO_SUPERLATIVA")
        
    # 2. Alucinação de Lore / Estúdio (P1)
    if re.search(r'mob\s+est[uú]dio|meu\s+an[uú]ncio|nosso\s+canal|nossa\s+equipe\s+de\s+grava[cç][aã]o', ai_text, re.IGNORECASE):
        issues.append("ALUCINACAO_LORE")
        
    # 3. Meta-Discurso de TI Hardcoded ou de Software (P1)
    if re.search(r'materiais\s+homologados|acervo\s+da\s+sess[aã]o|banco\s+de\s+dados|vetoriza[cç][aã]o|chunks|sess[aã]o\s+ativa', ai_text, re.IGNORECASE):
        issues.append("META_DISCURSO_TI")
        
    # 4. Cifrão Financeiro R$ (P2)
    if re.search(r'R\$\s*\d+', ai_text):
        issues.append("USO_CIFRAO_RS")
        
    # 5. Padrão 5 Alternativas (P1) em questões de múltipla escolha
    if "💡 Qual alternativa" in ai_text or re.search(r'📝\s*Questão\s+\d+/\d+', ai_text) or "### Questão" in ai_text:
        has_a = bool(re.search(r'(?:^|\n)\s*a\)', ai_text))
        has_d = bool(re.search(r'(?:^|\n)\s*d\)', ai_text))
        has_e = bool(re.search(r'(?:^|\n)\s*e\)', ai_text))
        if has_a and has_d and not has_e:
            issues.append("MENOS_DE_5_ALTERNATIVAS")
            
    # 6. Dump de Exercícios (P1)
    # Detecta se cuspiu mais de 1 questão de uma só vez (números de questão distintos no mesmo turno)
    distinct_questions = set(re.findall(r'📝\s*Questão\s+(\d+)/\d+', ai_text)) | set(re.findall(r'\bQuestão\s+(\d+)\b', ai_text))
    if len(distinct_questions) > 1:
        issues.append("DUMP_EXERCICIOS")
        
    # 7. Microaprendizagem na Trilha 1 (P2)
    if track == "trilha_1_duvidas":
        words = len(ai_text.split())
        if words > 230:  # Teto razoável com tolerância
            issues.append("MICROAPRENDIZAGEM_LONGA")
            
    # 8. Roteamento Falho de Sexualidade / Ciências (P1)
    if cluster == "BNCCSexualidade" and re.search(r'n[aã]o\s+atendo\s+conte[uú]dos\s+de\s+Biologia', ai_text, re.IGNORECASE):
        issues.append("ROTEAMENTO_SEXUALIDADE_FALHO")

    # 9. Nomenclatura Obsoleta do Menu (P2)
    if ("Como você prefere começar?" in ai_text or "Qual caminho você prefere agora?" in ai_text) and "Estudo Dirigido" in ai_text:
        issues.append("MENU_NOMENCLATURA_OBSOLETA")
        
    return issues

@retry(stop=stop_after_attempt(3), wait=wait_exponential_jitter(initial=1, max=5), reraise=True)
async def call_chat_endpoint_with_retry(req, bg):
    return await chat_endpoint(req, bg)

async def run_single_turn(session_id, user_msg, cluster="geral", track="geral"):
    bg = BackgroundTasks()
    req = ChatRequest(
        message=user_msg,
        user_id=TEST_USER_ID,
        session_id=session_id
    )
    
    t0 = time.time()
    resp = await call_chat_endpoint_with_retry(req, bg)
    
    # Processar background tasks
    for task in bg.tasks:
        try:
            if asyncio.iscoroutinefunction(task.func):
                await task.func(*task.args, **task.kwargs)
            else:
                task.func(*task.args, **task.kwargs)
        except Exception:
            pass
            
    full_text = ""
    assigned_session_id = session_id
    async for chunk in resp.body_iterator:
        chunk_str = chunk.decode("utf-8") if isinstance(chunk, bytes) else chunk
        for line in chunk_str.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                raw_json = line[6:].strip()
                if raw_json == "[DONE]":
                    continue
                try:
                    payload = json.loads(raw_json)
                    if "session_id" in payload and not assigned_session_id:
                        assigned_session_id = payload["session_id"]
                    if "chunk" in payload:
                        full_text += payload["chunk"]
                except Exception:
                    pass
                    
    elapsed = time.time() - t0
    issues = audit_turn_content(cluster, track, user_msg, full_text)
    
    return {
        "session_id": assigned_session_id,
        "cluster": cluster,
        "track": track,
        "user_msg": user_msg,
        "ai_text": full_text,
        "words": len(full_text.split()),
        "elapsed": elapsed,
        "issues": issues,
        "is_conformant": len(issues) == 0
    }

async def run_session(sess_info, sem, progress_tracker):
    async with sem:
        s_id = sess_info["id"]
        cluster = sess_info["cluster"]
        turns = sess_info["turns"]
        
        sess_results = []
        current_session_id = None
        
        for u_msg, track in turns:
            try:
                res = await run_single_turn(current_session_id, u_msg, cluster, track)
                current_session_id = res["session_id"]
                sess_results.append(res)
            except Exception as e_turn:
                # Registro de falha grave de conexão
                sess_results.append({
                    "session_id": current_session_id,
                    "cluster": cluster,
                    "track": track,
                    "user_msg": u_msg,
                    "ai_text": f"ERRO_FATAL: {str(e_turn)}",
                    "words": 0,
                    "elapsed": 0,
                    "issues": ["ERRO_EXECUCAO_TURN"],
                    "is_conformant": False
                })
                
            # Atualiza progresso global
            progress_tracker["completed_turns"] += 1
            if sess_results[-1]["is_conformant"]:
                progress_tracker["conformant_turns"] += 1
            else:
                progress_tracker["failed_turns"] += 1
                for iss in sess_results[-1]["issues"]:
                    progress_tracker["issue_counts"][iss] = progress_tracker["issue_counts"].get(iss, 0) + 1
                    
            c_turns = progress_tracker["completed_turns"]
            if c_turns % 50 == 0 or c_turns == 1000:
                p_current = progress_tracker["conformant_turns"] / c_turns
                low, high = wilson_score_interval(progress_tracker["conformant_turns"], c_turns)
                print(f"📊 [PROCESSO: {c_turns:4d}/1000 ({c_turns/10:.1f}%)] "
                      f"Conformes: {progress_tracker['conformant_turns']}/{c_turns} ({p_current*100:.2f}%) | "
                      f"IC 95%: [{low*100:.2f}%, {high*100:.2f}%] | Falhas: {progress_tracker['failed_turns']}", flush=True)
                
        progress_tracker["completed_sessions"] += 1
        return sess_results

async def main():
    print("="*80)
    print("💥 BENCHMARK ESTATÍSTICO DE ROBUSTEZ DO FIM DO MUNDO (N = 1.000 TURNOS)")
    print("   100 Sessões x 10 Turnos | 8 Clusters de Super-Stress Intencional")
    print("="*80)
    
    with open("scratch/doomsday_1000_plan.json", "r", encoding="utf-8") as f:
        plan = json.load(f)
        
    print(f"Plano carregado com sucesso: {len(plan)} sessões ({sum(len(s['turns']) for s in plan)} turnos).")
    
    sem = asyncio.Semaphore(8)  # Concorrência segura = 8 sessões simultâneas
    
    progress_tracker = {
        "completed_turns": 0,
        "conformant_turns": 0,
        "failed_turns": 0,
        "completed_sessions": 0,
        "issue_counts": {}
    }
    
    t_start = time.time()
    
    async with lifespan(app):
        tasks = [run_session(s, sem, progress_tracker) for s in plan]
        all_session_outputs = await asyncio.gather(*tasks)
        
    total_elapsed = time.time() - t_start
    
    # Flatten
    all_turns = []
    for s_res in all_session_outputs:
        all_turns.extend(s_res)
        
    n_total = len(all_turns)
    n_conformant = sum(1 for t in all_turns if t["is_conformant"])
    p_hat = n_conformant / n_total if n_total > 0 else 0
    ci_low, ci_high = wilson_score_interval(n_conformant, n_total)
    margin = (ci_high - ci_low) / 2
    
    # Análise por Cluster
    clusters = {}
    for t in all_turns:
        c = t["cluster"]
        if c not in clusters:
            clusters[c] = {"total": 0, "conformant": 0, "issues": {}}
        clusters[c]["total"] += 1
        if t["is_conformant"]:
            clusters[c]["conformant"] += 1
        else:
            for iss in t["issues"]:
                clusters[c]["issues"][iss] = clusters[c]["issues"].get(iss, 0) + 1
                
    print("\n" + "="*80)
    print("🏆 RELATÓRIO DO BENCHMARK ESTATÍSTICO DO FIM DO MUNDO (N = 1.000 TURNOS)")
    print("="*80)
    print(f"Total de Turnos Executados:  {n_total}")
    print(f"Tempo Total de Execução:     {total_elapsed:.1f}s ({total_elapsed/60:.2f} min | {total_elapsed/n_total:.2f}s/turno médio)")
    print(f"Turnos Conformes:            {n_conformant} / {n_total}")
    print(f"Taxa de Conformidade Global: {p_hat*100:.2f}%")
    print(f"Intervalo de Wilson (95%):   [{ci_low*100:.2f}% ; {ci_high*100:.2f}%]")
    print(f"Margem de Erro Estrita (E):  ±{margin*100:.2f}%")
    print("-"*80)
    print("Desempenho por Cluster de Super-Stress:")
    for c_name, c_data in sorted(clusters.items()):
        c_rate = c_data["conformant"] / c_data["total"] * 100
        c_low, c_high = wilson_score_interval(c_data["conformant"], c_data["total"])
        print(f"  📌 {c_name:<18}: {c_data['conformant']:3d}/{c_data['total']:3d} ({c_rate:6.2f}%) | IC 95%: [{c_low*100:5.2f}%, {c_high*100:5.2f}%]")
        if c_data["issues"]:
            for iss, cnt in c_data["issues"].items():
                print(f"      ❌ {iss}: {cnt}")
    print("-"*80)
    print("Falhas Detectadas no Total Geral:")
    if not progress_tracker["issue_counts"]:
        print("  🎉 ZERO FALHAS! Perfeição absoluta em todos os 1.000 turnos!")
    else:
        for iss, count in sorted(progress_tracker["issue_counts"].items(), key=lambda x: x[1], reverse=True):
            print(f"  ❌ {iss}: {count} ocorrências ({count/n_total*100:.2f}%)")
    print("="*80)
    
    # Salvar dossiê final
    dossie = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "n_total": n_total,
        "n_conformant": n_conformant,
        "p_hat": p_hat,
        "wilson_ci_95": [ci_low, ci_high],
        "margin_of_error": margin,
        "total_elapsed_seconds": total_elapsed,
        "clusters": clusters,
        "issue_counts": progress_tracker["issue_counts"],
        "turns_sample": all_turns[:50] # Amostra para não explodir tamanho de log
    }
    
    with open("scratch/doomsday_1000_results.json", "w", encoding="utf-8") as f:
        json.dump(dossie, f, ensure_ascii=False, indent=2)
    print("Dossiê completo salvo em: scratch/doomsday_1000_results.json")

if __name__ == "__main__":
    asyncio.run(main())
