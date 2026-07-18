import os
import subprocess
import re
import sys

BASE_DEST = "content/fundamental-2/9-ano/matematica"

mappings = [
    ("temp_draft_cap01.md", "cap-01-numeros-irracionais/ebooks/ef09ma01-ma02.md"),
    ("temp_draft_cap02.md", "cap-02-calculos-numeros-reais/ebooks/ef09ma03.md"),
    ("temp_draft_cap03.md", "cap-03-problemas-notacao-cientifica/ebooks/ef09ma04.md"),
    ("temp_draft_cap04.md", "cap-04-porcentagens-sucessivas/ebooks/ef09ma05.md"),
    ("temp_draft_cap05.md", "cap-05-introducao-funcoes/ebooks/ef09ma06.md"),
    ("temp_draft_cap06.md", "cap-06-razao-grandezas-diferentes/ebooks/ef09ma07.md"),
    ("temp_draft_cap07.md", "cap-07-proporcionalidade-escalas/ebooks/ef09ma08.md"),
    ("temp_draft_cap08.md", "cap-08-fatoracao-equacoes-segundo-grau/ebooks/ef09ma09.md"),
    ("temp_draft_cap09.md", "cap-09-retas-paralelas-transversais/ebooks/ef09ma10.md"),
    ("temp_draft_cap10.md", "cap-10-arcos-angulos-circunferencia/ebooks/ef09ma11.md"),
    ("temp_draft_cap11.md", "cap-11-semelhanca-triangulos/ebooks/ef09ma12.md"),
    ("temp_draft_cap12.md", "cap-12-teorema-pitagoras-tales/ebooks/ef09ma13-ma14.md"),
    ("temp_draft_cap13.md", "cap-13-construcao-poligonos-regulares/ebooks/ef09ma15.md"),
    ("temp_draft_cap14.md", "cap-14-distancia-ponto-medio/ebooks/ef09ma16.md"),
    ("temp_draft_cap15.md", "cap-15-vistas-ortogonais-geometria-espacial/ebooks/ef09ma17.md"),
    ("temp_draft_cap16.md", "cap-16-unidades-medidas-grandes-pequenas/ebooks/ef09ma18.md"),
    ("temp_draft_cap17.md", "cap-17-volume-prismas-cilindros/ebooks/ef09ma19.md"),
    ("temp_draft_cap18.md", "cap-18-probabilidade-eventos-dependentes/ebooks/ef09ma20.md"),
    ("temp_draft_cap19.md", "cap-19-analise-escolha-graficos/ebooks/ef09ma21-ma22.md"),
    ("temp_draft_cap20.md", "cap-20-pesquisas-amostrais/ebooks/ef09ma23.md"),
]

for src, dest in mappings:
    if not os.path.exists(src):
        print(f"[ERRO] Arquivo não encontrado: {src}")
        continue
    
    with open(src, "r", encoding="utf-8-sig") as f:
        content = f.read()
        
    # Correções automáticas
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
