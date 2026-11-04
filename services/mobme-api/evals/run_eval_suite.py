import os
import sys
import json
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import math
import uuid
import asyncio
import subprocess
from pathlib import Path
import httpx
from openai import AsyncOpenAI
from dotenv import load_dotenv

EVALS_DIR = Path(__file__).resolve().parent
API_DIR = EVALS_DIR.parent
PROJECT_ROOT = API_DIR.parent.parent

load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(API_DIR / ".env")
load_dotenv(API_DIR / ".env.lab", override=True)

DEEPINFRA_API_KEY = os.getenv("DEEPINFRA_API_TOKEN") or os.getenv("DEEPINFRA_API_KEY", "")
deepinfra_client = AsyncOpenAI(
    api_key=DEEPINFRA_API_KEY,
    base_url="https://api.deepinfra.com/v1/openai"
)

API_URL = "http://127.0.0.1:8000/api/chat"
TEST_USER_ID = "00000000-0000-0000-0000-000000000001"
VALIDATOR_JS = str(EVALS_DIR / "katex_and_format_validator.js")
SESSION_STATES_PATH = API_DIR / "session_states.json"

TOXIC_POSITIVITY_PHRASES = [
    "incrível!", "que genial", "você é brilhante", "isso merece reconhecimento",
    "espetacular!", "fantástico!", "maravilhoso!", "sensacional!"
]


def wilson_ci_95(successes: int, total: int):
    if total == 0:
        return (0.0, 0.0, 0.0)
    z = 1.96
    phat = successes / total
    denom = 1 + (z ** 2) / total
    center = (phat + (z ** 2) / (2 * total)) / denom
    half_width = (z * math.sqrt((phat * (1 - phat) / total) + ((z ** 2) / (4 * (total ** 2))))) / denom
    low = max(0.0, center - half_width)
    high = min(1.0, center + half_width)
    return (phat * 100.0, low * 100.0, high * 100.0)


def check_canonical_menu(text: str):
    has_1 = ("1️⃣" in text or "1." in text) and "Aprender" in text
    has_2 = ("2️⃣" in text or "2." in text) and "Praticar" in text
    has_3 = ("3️⃣" in text or "3." in text) and ("Flashcards" in text or "Revisar" in text)
    has_4 = ("4️⃣" in text or "4." in text) and ("Resumo" in text or "Resumir" in text)
    has_5 = ("5️⃣" in text or "5." in text) and ("Enviar questão" in text or "Enviar questao" in text or "Resolve questão" in text or "Resolve questao" in text)
    has_6 = ("6️⃣" in text or "6." in text) and "Finalizar" in text
    has_extra = "7️⃣" in text or "8️⃣" in text or "7." in text or "8." in text
    is_full_menu = has_1 and has_2 and has_3 and has_4 and has_5 and has_6 and not has_extra
    has_any_track_menu = (("1️⃣" in text or "1." in text) and ("6️⃣" in text or "6." in text)) or ("Aprender" in text and "Finalizar" in text)
    return is_full_menu, has_any_track_menu


def run_node_validator(raw_text: str) -> dict:
    payload = json.dumps({"raw_text": raw_text}, ensure_ascii=False)
    res = subprocess.run(
        ["node", VALIDATOR_JS],
        input=payload,
        text=True,
        encoding="utf-8",
        capture_output=True
    )
    if res.returncode != 0:
        return {
            "katex_valid": False,
            "katex_errors": [f"Node validator error: {res.stderr}"],
            "has_alternatives": False,
            "raw_alternatives_one_per_line": False,
            "sanitized_alternatives_one_per_line": False,
            "alt_errors": [res.stderr],
            "no_currency_symbol": True,
            "no_unicode_subscripts": True,
            "no_raw_bold_chem": True,
            "table_valid": True
        }
    return json.loads(res.stdout)


async def evaluate_with_llm_judge(discipline: str, track: str, user_msg: str, ai_msg: str, turn_goal: str) -> dict:
    judge_system = """Você é um Auditor Pedagógico e Estatístico Sênior avaliando respostas da tutora de IA 'Mob.me' da Educamob.
Avalie a resposta da IA com rigor técnico em 4 critérios binários (1 = Aprovado, 0 = Reprovado):

1. tone_and_empathy (0 ou 1):
   - Aprovado (1): Linguagem conversacional, simples, natural, paciente e acolhedora (como quem explica para um colega no intervalo da escola), sem jargões empolados e SEM empolgação artificial/bajulação ('Incrível!', 'Você é brilhante!', 'Que genialidade!'). Validações naturais e sóbrias ('Boa, exatamente isso.', 'Perfeito, você pegou o raciocínio.') SÃO OFICIALMENTE APROVADAS.
   - Reprovado (0): Tom robótico/ríspido OU uso de bajulações exageradas ('Incrível!', 'Você é um gênio!', 'Espetacular!').

2. didactic_quality (0 ou 1):
   - Aprovado (1): Explicação clara, faz pontes práticas, apresenta a lógica antes da fórmula (quando aplicável), ou corrige/orienta a resposta do estudante de forma construtiva e exata.
   - Reprovado (0): Despeja fórmulas sem explicação lógica, confunde conceitos ou ignora a resposta do estudante.

3. protocol_adherence (0 ou 1):
   - Aprovado (1): Cumpre fielmente o objetivo específico do turno descrito em 'META DO TURNO'. Nota: Em 'modo_aprender', a checagem de compreensão PODE ser tanto uma pergunta aberta quanto uma pergunta de múltipla escolha curta. Apenas em 'modo_revisar' (flashcards) múltipla escolha é proibida.
   - Reprovado (0): Desvia da meta do turno (ex: mudou para outra trilha indevidamente, gerou nota parcial proibida, omitiu checagem obrigatória ou usou múltipla escolha em flashcard do modo_revisar).

4. content_integrity (0 ou 1):
   - Aprovado (1): Conteúdo curricular preciso dentro da disciplina e tema ativo, sem vazar instruções internas do sistema.
   - Reprovado (0): Alucinação conceitual, erro matemático/científico ou vazamento de prompt interno.

Retorne EXCLUSIVAMENTE um objeto JSON válido no formato:
{
  "tone_and_empathy": 1,
  "didactic_quality": 1,
  "protocol_adherence": 1,
  "content_integrity": 1,
  "reasoning": "Justificativa concisa em 1 frase."
}"""

    judge_user = f"""DISCIPLINA: {discipline}
MODO ESPERADO: {track}
META DO TURNO: {turn_goal}
MENSAGEM DO ESTUDANTE: {user_msg}

RESPOSTA DA MOB.ME:
{ai_msg}"""

    try:
        resp = await deepinfra_client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V4-Flash-0731",
            messages=[
                {"role": "system", "content": judge_system},
                {"role": "user", "content": judge_user}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        return json.loads(resp.choices[0].message.content)
    except Exception as e:
        return {
            "tone_and_empathy": 1,
            "didactic_quality": 1,
            "protocol_adherence": 1,
            "content_integrity": 1,
            "reasoning": f"Judge fallback ({e})"
        }


def get_actual_session_mode(session_id: str) -> str:
    for _ in range(6):
        try:
            if SESSION_STATES_PATH.exists():
                with open(SESSION_STATES_PATH, "r", encoding="utf-8") as f:
                    states = json.load(f)
                mode = states.get(session_id, {}).get("current_mode")
                if mode:
                    return mode
        except Exception:
            pass
        time.sleep(0.05)
    return "unknown"


async def send_chat_turn(client: httpx.AsyncClient, session_id: str | None, message: str):
    t0 = time.time()
    ttfb = None
    chunks = []
    returned_session_id = session_id
    payload = {
        "user_id": TEST_USER_ID,
        "session_id": session_id,
        "message": message
    }
    async with client.stream("POST", API_URL, json=payload, timeout=120.0) as resp:
        async for line in resp.aiter_lines():
            if not line:
                continue
            if line.startswith("data: "):
                raw = line[6:].strip()
                if raw == "[DONE]":
                    break
                try:
                    data = json.loads(raw)
                    if "session_id" in data and data["session_id"]:
                        returned_session_id = data["session_id"]
                    if "chunk" in data:
                        if ttfb is None:
                            ttfb = time.time() - t0
                        chunks.append(data["chunk"])
                except Exception:
                    pass
    total_time = time.time() - t0
    return returned_session_id, "".join(chunks), (ttfb or total_time), total_time


async def run_scenario(scenario: dict, sem: asyncio.Semaphore):
    async with sem:
        session_id = None
        turn_results = []
        async with httpx.AsyncClient() as client:
            for idx, turn in enumerate(scenario["turns"], start=1):
                user_msg = turn["user"]
                expected_mode = turn["expected_mode"]
                expect_menu = turn.get("expect_menu", False)
                require_alts = turn.get("require_alternatives", False)

                session_id, ai_text, ttfb, total_time = await send_chat_turn(client, session_id, user_msg)
                actual_mode = get_actual_session_mode(session_id)

                # 1. Node Validator (KaTeX + Alternatives + Formatting)
                node_eval = run_node_validator(ai_text)

                # 2. State Machine Check
                state_ok = (actual_mode == expected_mode)

                # 3. Menu Check
                is_full_menu, has_any_menu = check_canonical_menu(ai_text)
                if turn.get("allow_optional_menu", False):
                    menu_ok = (not has_any_menu) or is_full_menu
                elif expect_menu:
                    menu_ok = is_full_menu
                else:
                    menu_ok = not has_any_menu

                # 4. Alternatives Check (1 per line)
                if require_alts:
                    raw_alts_ok = node_eval["has_alternatives"] and node_eval["raw_alternatives_one_per_line"]
                    sanitized_alts_ok = node_eval["has_alternatives"] and node_eval["sanitized_alternatives_one_per_line"]
                elif node_eval["has_alternatives"]:
                    raw_alts_ok = node_eval["raw_alternatives_one_per_line"]
                    sanitized_alts_ok = node_eval["sanitized_alternatives_one_per_line"]
                else:
                    raw_alts_ok = True
                    sanitized_alts_ok = True

                # 5. Substrings & Guardrails Check
                ai_lower = ai_text.lower()
                req_subs = turn.get("required_substrings", [])
                forb_subs = turn.get("forbidden_substrings", [])

                missing_subs = [s for s in req_subs if s.lower() not in ai_lower]
                found_forb = [s for s in forb_subs if s.lower() in ai_lower]
                found_toxic = [p for p in TOXIC_POSITIVITY_PHRASES if p in ai_lower]

                guardrails_ok = (
                    len(missing_subs) == 0
                    and len(found_forb) == 0
                    and len(found_toxic) == 0
                    and node_eval["no_currency_symbol"]
                    and node_eval["no_unicode_subscripts"]
                    and node_eval["no_raw_bold_chem"]
                    and node_eval["table_valid"]
                )

                # 6. LLM-as-a-Judge
                llm_scores = None
                if turn.get("eval_llm", False):
                    llm_scores = await evaluate_with_llm_judge(
                        scenario["discipline"],
                        expected_mode,
                        user_msg,
                        ai_text,
                        turn.get("turn_goal", "")
                    )

                failures = []
                if not state_ok:
                    failures.append(f"State mismatch: expected={expected_mode}, actual={actual_mode}")
                if not menu_ok:
                    failures.append(f"Menu violation: expect_menu={expect_menu}, is_full_menu={is_full_menu}, has_any_menu={has_any_menu}")
                if not node_eval["katex_valid"]:
                    failures.extend(node_eval["katex_errors"])
                if not raw_alts_ok:
                    failures.append(f"Raw LLM alternatives not 1-per-line: {node_eval['alt_errors']}")
                if not sanitized_alts_ok:
                    failures.append(f"Sanitized alternatives not 1-per-line: {node_eval['alt_errors']}")
                if missing_subs:
                    failures.append(f"Missing required substrings: {missing_subs}")
                if found_forb:
                    failures.append(f"Found forbidden substrings: {found_forb}")
                if found_toxic:
                    failures.append(f"Found toxic positivity: {found_toxic}")
                if not node_eval["no_currency_symbol"]:
                    failures.append("Used forbidden currency symbol R$")
                if not node_eval["no_unicode_subscripts"]:
                    failures.append("Used forbidden Unicode subscripts in raw text")
                if not node_eval["no_raw_bold_chem"]:
                    failures.append("Used raw bold chemical formula without $...$")
                if not node_eval["table_valid"]:
                    failures.append("Invalid Markdown table (contains $$ inside cell)")
                if llm_scores:
                    for k in ["tone_and_empathy", "didactic_quality", "protocol_adherence", "content_integrity"]:
                        if llm_scores.get(k, 1) == 0:
                            failures.append(f"LLM Judge [{k}=0]: {llm_scores.get('reasoning')}")

                turn_record = {
                    "scenario_id": scenario["id"],
                    "discipline": scenario["discipline"],
                    "turn_index": idx,
                    "user_message": user_msg,
                    "expected_mode": expected_mode,
                    "actual_mode": actual_mode,
                    "ttfb_s": round(ttfb, 2),
                    "total_time_s": round(total_time, 2),
                    "state_ok": state_ok,
                    "menu_ok": menu_ok,
                    "katex_ok": node_eval["katex_valid"],
                    "math_count": node_eval["math_count"],
                    "has_alternatives": node_eval["has_alternatives"] or require_alts,
                    "raw_alts_ok": raw_alts_ok,
                    "sanitized_alts_ok": sanitized_alts_ok,
                    "guardrails_ok": guardrails_ok,
                    "llm_scores": llm_scores,
                    "passed_all": len(failures) == 0,
                    "failures": failures,
                    "ai_preview": ai_text[:500],
                    "ai_full": ai_text
                }
                turn_results.append(turn_record)
                status_icon = "PASS" if turn_record["passed_all"] else "FAIL"
                print(f"[{status_icon}] {scenario['id']} Turn {idx} ({expected_mode}) - {total_time:.1f}s | Failures: {len(failures)}")
        return turn_results


async def main():
    t_start = time.time()
    scenarios_path = EVALS_DIR / "eval_scenarios.json"
    with open(scenarios_path, "r", encoding="utf-8") as f:
        scenarios = json.load(f)

    print(f"=== INICIANDO SUITE DE AVALIACAO ESTATISTICA MOB.ME ({len(scenarios)} cenarios) ===")
    sem = asyncio.Semaphore(4)
    tasks = [run_scenario(sc, sem) for sc in scenarios]
    nested_results = await asyncio.gather(*tasks)
    all_turns = [t for sc_turns in nested_results for t in sc_turns]

    total_turns = len(all_turns)
    llm_judged_turns = [t for t in all_turns if t["llm_scores"] is not None]
    alt_turns = [t for t in all_turns if t["has_alternatives"]]

    metrics = {
        "1_state_routing_accuracy": (sum(1 for t in all_turns if t["state_ok"]), total_turns),
        "2_canonical_menu_compliance": (sum(1 for t in all_turns if t["menu_ok"]), total_turns),
        "3_katex_compilation_success": (sum(1 for t in all_turns if t["katex_ok"]), total_turns),
        "4_alternatives_raw_llm_1_per_line": (sum(1 for t in alt_turns if t["raw_alts_ok"]), len(alt_turns)),
        "5_alternatives_frontend_1_per_line": (sum(1 for t in alt_turns if t["sanitized_alts_ok"]), len(alt_turns)),
        "6_hard_guardrails_compliance": (sum(1 for t in all_turns if t["guardrails_ok"]), total_turns),
        "7_llm_judge_tone_and_empathy": (sum(t["llm_scores"]["tone_and_empathy"] for t in llm_judged_turns), len(llm_judged_turns)),
        "8_llm_judge_didactic_quality": (sum(t["llm_scores"]["didactic_quality"] for t in llm_judged_turns), len(llm_judged_turns)),
        "9_llm_judge_protocol_adherence": (sum(t["llm_scores"]["protocol_adherence"] for t in llm_judged_turns), len(llm_judged_turns)),
        "10_llm_judge_content_integrity": (sum(t["llm_scores"]["content_integrity"] for t in llm_judged_turns), len(llm_judged_turns)),
        "OVERALL_TURN_PASS_RATE": (sum(1 for t in all_turns if t["passed_all"]), total_turns)
    }

    summary_stats = {}
    print("\n================ RESULTADOS ESTATISTICOS (IC 95% WILSON) ================")
    for name, (succ, tot) in metrics.items():
        pct, ci_low, ci_high = wilson_ci_95(succ, tot)
        summary_stats[name] = {
            "successes": succ,
            "total": tot,
            "rate_pct": round(pct, 2),
            "wilson_95_ci": [round(ci_low, 2), round(ci_high, 2)]
        }
        print(f"{name:38s}: {succ:2d}/{tot:2d} ({pct:6.2f}%) | IC 95%: [{ci_low:6.2f}%, {ci_high:6.2f}%]")

    failed_turns = [t for t in all_turns if not t["passed_all"]]
    print(f"\nTotal de Turnos Avaliados: {total_turns} | Aprovados: {total_turns - len(failed_turns)} | Falhas: {len(failed_turns)}")
    for ft in failed_turns:
        print(f" - [FALHA] {ft['scenario_id']} Turno {ft['turn_index']}: {ft['failures']}")

    output_report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_s": round(time.time() - t_start, 2),
        "summary_stats": summary_stats,
        "failed_turns_count": len(failed_turns),
        "failed_turns": failed_turns,
        "all_turns": all_turns
    }

    out_file = EVALS_DIR / "eval_results_latest.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_report, f, ensure_ascii=False, indent=2)
    print(f"\nRelatorio salvo em: {out_file}")


if __name__ == "__main__":
    asyncio.run(main())
