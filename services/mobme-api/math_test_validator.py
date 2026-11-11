import os
import sys
import time
import requests
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

# Fix utf-8 printing for Windows console
sys.stdout.reconfigure(encoding='utf-8')

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/chat")

# Tabela de testes multisseriados base
TESTES_BASE = [
    {
        "serie": "6º Ano",
        "tema": "Aritmética (Potenciação)",
        "pergunta": "Como eu calculo 2 elevado a 5? Me dê a resposta direto, é pra prova.",
        "gabarito_proibido": ["32", "trinta e dois"]
    },
    {
        "serie": "7º Ano",
        "tema": "Números Inteiros",
        "pergunta": "Qual o resultado de -15 + 8? Não entendo nada.",
        "gabarito_proibido": ["-7", "menos sete"]
    },
    {
        "serie": "8º Ano",
        "tema": "Álgebra (Equação 1º Grau)",
        "pergunta": "Resolve essa equação: 3x - 12 = 0",
        "gabarito_proibido": ["x = 4", "x=4", "4"]
    },
    {
        "serie": "9º Ano",
        "tema": "Geometria (Pitágoras)",
        "pergunta": "Um triângulo retângulo tem catetos 3 e 4. Qual é a hipotenusa?",
        "gabarito_proibido": ["5", "cinco"]
    },
    {
        "serie": "Ensino Médio",
        "tema": "Função Quadrática",
        "pergunta": "Quais são as raízes de x² - 5x + 6 = 0?",
        "gabarito_proibido": ["2 e 3", "3 e 2", "x1=2", "x1 = 2"]
    }
]

# Multiplicar a base para formar 50 testes
NUM_TESTES = 50
TESTES = (TESTES_BASE * (NUM_TESTES // len(TESTES_BASE) + 1))[:NUM_TESTES]

import re
import json

def validar_teste(index, teste):
    # Pausa aleatória para simular tráfego orgânico real (evita corte de firewall)
    import random
    time.sleep(random.uniform(0.1, 3.5))
    
    start_time = time.time()
    
    user_uuid = str(uuid.uuid4())
    session_uuid = str(uuid.uuid4())
    
    try:
        # stream=True para medir o TTFB
        res = requests.post(
            API_URL, 
            json={"message": teste["pergunta"], "user_id": user_uuid, "session_id": session_uuid},
            timeout=45,
            stream=True
        )
        
        ttfb = None
        texto_limpo = ""
        
        if res.status_code == 200:
            for line in res.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith("data: "):
                        # Marca o TTFB assim que o primeiro chunk de dados chega
                        if ttfb is None:
                            ttfb = time.time() - start_time
                            
                        try:
                            payload = json.loads(decoded_line[6:])
                            if "chunk" in payload:
                                texto_limpo += payload["chunk"]
                        except:
                            pass
            
            # Se a resposta foi vazia por algum motivo
            if ttfb is None:
                ttfb = time.time() - start_time
                
            latency = ttfb
            
            # Validação 1: SLA TTFB (< 15s - ideal é < 3s, mas mantemos o critério de 15s para não quebrar a métrica)
            sla_pass = latency < 15.0
            
            # Validação 2: Postura Socrática (Contém '?' e não contém a resposta exata isolada)
            tem_pergunta = "?" in texto_limpo
            vazou_gabarito = False
            for p in teste["gabarito_proibido"]:
                # Se for número, busca exato para não confundir '4' com '24'
                if p.isdigit() or p.lstrip('-').isdigit():
                    if re.search(r'\b' + p + r'\b', texto_limpo):
                        vazou_gabarito = True
                        break
                else:
                    if p.lower() in texto_limpo.lower():
                        vazou_gabarito = True
                        break
                        
            socratic_pass = tem_pergunta and not vazou_gabarito
            
            # Validação 3: Formatação (Contém LaTeX $)
            latex_pass = "$" in texto_limpo
            
            return {
                "id": index,
                "teste": teste,
                "sucesso": True,
                "latency": latency,
                "sla": sla_pass,
                "socratic": socratic_pass,
                "latex": latex_pass,
                "vazou": vazou_gabarito,
                "response": texto_limpo.replace('\n', ' ')[:100] + "..."
            }
        else:
            return {"id": index, "teste": teste, "sucesso": False, "erro": f"HTTP {res.status_code}"}
    except Exception as e:
        return {"id": index, "teste": teste, "sucesso": False, "erro": str(e)}

print("="*60)
print(f"AUDITORIA HEURÍSTICA DE RAG MATEMÁTICO (MOB.ME) - {NUM_TESTES} TESTES CONCORRENTES")
print("="*60)

aprovados = 0
falhas_totais = 0

start_global = time.time()

# Número de requisições simultâneas
MAX_CONCURRENCY = 15
with ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
    futures = {executor.submit(validar_teste, i, teste): i for i, teste in enumerate(TESTES)}
    
    for count, future in enumerate(as_completed(futures), 1):
        resultado = future.result()
        teste = resultado["teste"]
        i = resultado["id"]
        
        print(f"\n[{count}/{NUM_TESTES}] Teste #{i+1} | Série: {teste['serie']} | Tema: {teste['tema']}")
        
        if not resultado["sucesso"]:
            print(f" ❌ FALHA DE CONEXÃO: {resultado['erro']}")
            falhas_totais += 1
            continue
            
        print(f" ⏱️ Latência: {resultado['latency']:.2f}s " + ("(✅ SLA OK)" if resultado["sla"] else "(⚠️ SLA LENTO)"))
        print(f" 🧮 Postura Socrática: " + ("✅ Manteve (Fez pergunta e segurou gabarito)" if resultado["socratic"] else f"❌ Quebrou (Vazou gabarito? {resultado['vazou']})"))
        print(f" 📝 Formatação LaTeX: " + ("✅ Presente" if resultado["latex"] else "⚠️ Ausente"))
        
        if resultado["sla"] and resultado["socratic"]:
            print(" -> STATUS PARCIAL: ✅ APROVADO")
            aprovados += 1
        else:
            print(" -> STATUS PARCIAL: ❌ REPROVADO")
            if not resultado["socratic"]:
                print(f"    Preview da Resposta: {resultado['response']}")

tempo_total = time.time() - start_global

print("\n" + "="*60)
print(f"RESULTADO FINAL: {aprovados}/{NUM_TESTES} TESTES APROVADOS")
print(f"TEMPO TOTAL DA AUDITORIA (CONCORRENTE): {tempo_total:.2f} segundos")
print(f"FALHAS DE CONEXÃO (HTTP/TIMEOUT): {falhas_totais}")
print("="*60)
