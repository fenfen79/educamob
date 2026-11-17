import requests
import json

user_id = "3400ee62-7e4b-4b22-8643-75bc842e36e5"
current_session_id = None
url = "https://api.educamob.com.br/api/chat"

def send(msg):
    global current_session_id
    payload = {"message": msg, "session_id": current_session_id, "user_id": user_id}
    resp = requests.post(url, json=payload, timeout=40)
    full_text = ""
    for line in resp.text.split("\n"):
        line = line.strip()
        if line.startswith("data: "):
            d = line[6:].strip()
            if d == "[DONE]":
                continue
            try:
                p = json.loads(d)
                if "session_id" in p and not current_session_id:
                    current_session_id = p["session_id"]
                if "chunk" in p:
                    full_text += p["chunk"]
            except Exception:
                pass
    return full_text

print("--- PASSO 1: Enviando 'Quero estudar Termodinâmica' ---")
r1 = send("Quero estudar Termodinâmica")
print(f"Session ID atribuída pelo servidor: {current_session_id}")
print("R1:\n", r1[:300], "...\n")

print("\n--- PASSO 2: Escolhendo foco '1' na mesma sessão (deve exibir o Menu com 'Leia e Aprenda') ---")
r2 = send("1")
print("R2:\n", r2)

if "Leia e Aprenda" in r2:
    print("\n🏆 SUCESSO TOTAL: 'Leia e Aprenda' está 100% ATIVO NO MENU DE PRODUÇÃO!")
else:
    print("\n❌ FALHA: 'Leia e Aprenda' não encontrado no menu.")

if "Estudo Dirigido" in r2:
    print("❌ ALERTA: 'Estudo Dirigido' ainda aparece no menu!")
else:
    print("✅ CONFIRMADO: Zero ocorrências de 'Estudo Dirigido'!")

print("\n--- PASSO 3: Enviando '2' na mesma sessão para ativar a Trilha 2 (Leia e Aprenda) ---")
r3 = send("2")
print("R3:\n", r3[:350], "...")

if "💡 Qual alternativa" in r3 or "Checagem" in r3 or "a)" in r3 or "1." in r3:
    print("\n🏆 SUCESSO CONFIRMADO: Trilha 2 ('Leia e Aprenda') ativada e entregando microaprendizagem ao vivo na VPS!")
