import os
import subprocess
import re
import sys

BASE_DEST = "content/fundamental-2/8-ano/matematica"

mappings = [
    ("temp_draft_cap01.md", "cap-01-notacao-cientifica/ebooks/ef08ma01.md"),
    ("temp_draft_cap02.md", "cap-02-potenciacao-radiciacao/ebooks/ef08ma02.md"),
    ("temp_draft_cap03.md", "cap-03-principio-multiplicativo-contagem/ebooks/ef08ma03.md"),
    ("temp_draft_cap04.md", "cap-04-porcentagens/ebooks/ef08ma04.md"),
    ("temp_draft_cap05.md", "cap-05-dizimas-periodicas-fracao-geratriz/ebooks/ef08ma05.md"),
    ("temp_draft_cap07.md", "cap-07-equacao-linear-primeiro-grau-plano/ebooks/ef08ma07.md"),
    ("temp_draft_cap08.md", "cap-08-sistema-equacoes-primeiro-grau/ebooks/ef08ma08.md"),
    ("temp_draft_cap09.md", "cap-09-equacao-polinomial-segundo-grau/ebooks/ef08ma09.md"),
    ("temp_draft_cap10.md", "cap-10-sequencias-recursivas-nao-recursivas/ebooks/ef08ma10-ma11.md"),
    ("temp_draft_cap12.md", "cap-12-congruencia-triangulos-quadrilateros/ebooks/ef08ma14.md"),
    ("temp_draft_cap13.md", "cap-13-construcoes-geometricas-angulos-poligonos/ebooks/ef08ma15-ma16.md"),
    ("temp_draft_cap14.md", "cap-14-mediatriz-bissetriz/ebooks/ef08ma17.md"),
    ("temp_draft_cap15.md", "cap-15-transformacoes-geometricas/ebooks/ef08ma18.md"),
    ("temp_draft_16.md", "cap-16-area-figuras-planas-circulo/ebooks/ef08ma19.md"),
    ("temp_draft_cap17.md", "cap-17-volume-capacidade/ebooks/ef08ma20-ma21.md"),
    ("temp_draft_cap18.md", "cap-18-probabilidade-espaco-amostral/ebooks/ef08ma22.md"),
    ("temp_draft_cap19.md", "cap-19-graficos-estatisticos/ebooks/ef08ma23.md"),
    ("temp_draft_cap20.md", "cap-20-organizacao-dados-classes/ebooks/ef08ma24.md"),
    ("temp_draft_cap21.md", "cap-21-medidas-tendencia-central-dispersao/ebooks/ef08ma25.md"),
    ("temp_draft_cap22.md", "cap-22-pesquisas-censitaria-amostral/ebooks/ef08ma26-ma27.md"),
]

for src, dest in mappings:
    if not os.path.exists(src):
        print(f"[ERRO] Arquivo não encontrado: {src}")
        continue
    
    with open(src, "r", encoding="utf-8-sig") as f:
        content = f.read()
        
    content = re.sub(r'R\$\s?(\d+,\d+)', r'\1 reais', content)
    content = re.sub(r'R\$\s?(\d+)', r'\1 reais', content)
    content = content.replace('R$', 'reais')
    
    content = content.lstrip()
    if not content.startswith('---'):
        content = '---\n' + content
        
    with open(src, "w", encoding="utf-8") as f:
        f.write(content)
        
    full_dest = os.path.join(BASE_DEST, dest).replace("\\", "/")
    
    print(f"\n--- Validando {src} ---")
    cmd = ["python", "validador_educamob.py", src, full_dest]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

print("\nConcluído processamento em lote.")
