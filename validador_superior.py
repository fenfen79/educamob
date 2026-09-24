import sys
import re
import os
import shutil
import difflib
from collections import Counter

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def validar_arquivo(caminho_temporario, caminho_destino):
    try:
        with open(caminho_temporario, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except Exception as e:
        print(f"[ERRO] Não foi possível ler o arquivo temporário {caminho_temporario}. Detalhes: {e}")
        sys.exit(1)

    erros = []

    # Regras Globais
    if re.search(r'R\$\s*\d', conteudo):
        erros.append("O símbolo 'R$' é estritamente proibido. Substitua por 'reais' ou 'centavos' (Regra do MathJax).")
    
    if not conteudo.startswith("---"):
        erros.append("O arquivo deve obrigatoriamente iniciar com YAML frontmatter ('---').")
    
    if "## Referências" not in conteudo:
        erros.append("A seção '## Referências' é obrigatória.")

    # Detecção de Attention Glitch (Alucinação de repetição)
    texto_limpo = re.sub(r'^---.*?---\n', '', conteudo, flags=re.DOTALL) if conteudo.startswith('---') else conteudo
    
    glitch_match = re.search(r'\b(\w{4,})\s+\1\s+\1\b', texto_limpo, re.IGNORECASE)
    if glitch_match:
        palavra_alucinada = glitch_match.group(1)
        erros.append(f"Alucinação/Attention Glitch detectado: a palavra '{palavra_alucinada}' repetiu-se sucessivamente.")

    paragrafos = [p.strip() for p in texto_limpo.split('\n\n') if len(p.strip()) > 150]
    contagem_paragrafos = Counter(paragrafos)
    for p, qtd in contagem_paragrafos.items():
        if qtd >= 2:
            erros.append(f"Alucinação de Bloco Repetido: Um parágrafo de {len(p)} caracteres repetiu-se {qtd} vezes.")
            
    # Validação de Integridade do LaTeX / MathJax
    cifroes = re.findall(r'(?<!\\)\$', texto_limpo)
    if len(cifroes) % 2 != 0:
        erros.append(f"Falha de Renderização LaTeX: Há um número ímpar de cifrões ({len(cifroes)} símbolos '$').")
        
    comandos_quebrados = re.search(r'\n\s*(otin|theta|tau|pi|alpha|beta|gamma|rightarrow|leftarrow|subseteq|subset|supset|supseteq|varnothing|circ|times|cdot)\b', texto_limpo)
    if comandos_quebrados:
        comando = comandos_quebrados.group(1)
        erros.append(f"Falha de Renderização LaTeX: Possível barra invertida convertida em quebra de linha perto de '{comando}'.")

    # Validação do YAML Frontmatter para Superior
    try:
        yaml_blocks = re.findall(r'^---\n(.*?)\n---', conteudo, re.MULTILINE | re.DOTALL)
        if yaml_blocks:
            yaml_content = yaml_blocks[0]
            campos_obrig = ["série:", "disciplina:", "fonte_bibliografica:"]
            for campo in campos_obrig:
                if campo not in yaml_content:
                    erros.append(f"YAML Incompleto: Faltando o campo obrigatório '{campo}' no frontmatter.")
    except Exception:
        erros.append("Falha ao fazer parse do YAML Frontmatter.")

    # 1. Seções obrigatórias para Cálculo
    secoes_obrig = [
        "## Teoremas e Definições Formais", 
        "## Exemplos Resolvidos Passo a Passo", 
        "## Erros Comuns e Pegadinhas", 
        "## Aplicações Práticas", 
        "## Resumo"
    ]
    for secao in secoes_obrig:
        if secao not in conteudo:
            erros.append(f"Seção obrigatória ausente no E-book: '{secao}'.")
            
    # 2. Zero Exercícios
    termos_proibidos = ["Teste Seus Conhecimentos", "Gabarito:", "<!-- tipo:"]
    for termo in termos_proibidos:
        if termo in conteudo:
            erros.append(f"Violação de Teoria Pura: Encontrado o termo de exercício proibido '{termo}'.")
            
    # 3. Densidade de Palavras (Superior exige mais densidade)
    total_palavras = len(texto_limpo.split())
    limite_minimo = 3000
        
    if total_palavras < limite_minimo:
        erros.append(f"Densidade Insuficiente: O E-book possui apenas {total_palavras} palavras. A regra exige no mínimo {limite_minimo} palavras para Cálculo Superior.")

    # 4. Quantidade Mínima de Fontes
    bloco_referencias = re.search(r'## Referências(.*?)(?=\n##|\n>|\Z)', conteudo, re.DOTALL)
    if bloco_referencias:
        texto_refs = bloco_referencias.group(1)
        num_fontes = len(re.findall(r'^\s*[-*]\s', texto_refs, re.MULTILINE))
        if num_fontes < 3:
            erros.append(f"Fontes Insuficientes: O E-book listou apenas {num_fontes} referências. Exige-se no mínimo 3 fontes.")

    # 5. Proporcionalidade Estrutural (Anti-Padding)
    if total_palavras > 0:
        blocos_apendice = re.findall(r'(###? Apêndice.*?)(?=\n##|\Z)', conteudo, re.DOTALL | re.IGNORECASE)
        palavras_apendice = sum(len(bloco.split()) for bloco in blocos_apendice)
        proporcao_apendice = palavras_apendice / total_palavras
        if proporcao_apendice > 0.20:
            erros.append(f"Desbalanceamento Estrutural: Os Apêndices representam {proporcao_apendice:.1%} do texto. O máximo é 20%.")
            
        # Pega desde "Teoremas e Definições Formais" até "Erros Comuns e Pegadinhas" (núcleo duro)
        bloco_core = re.search(r'(## Teoremas e Definições Formais.*?)(?=\n## Erros Comuns e Pegadinhas|\Z)', conteudo, re.DOTALL)
        if bloco_core:
            palavras_core = len(bloco_core.group(1).split())
            proporcao_core = palavras_core / total_palavras
            if proporcao_core < 0.50:
                erros.append(f"Desbalanceamento Estrutural: O núcleo essencial (Teoremas + Exemplos) representa apenas {proporcao_core:.1%} do texto. É exigido no mínimo 50%.")

    if erros:
        print("[BLOQUEIO SISTÊMICO] O arquivo foi rejeitado por falhar nas seguintes regras do Ensino Superior:\n")
        for i, erro in enumerate(erros, 1):
            print(f"  {i}. {erro}")
        print("\nO arquivo temporário NÃO foi salvo no destino. Corrija o rascunho e tente novamente.")
        sys.exit(1)
    
    # Se passou, move/copia para o destino final
    try:
        os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
        shutil.copy2(caminho_temporario, caminho_destino)
        print(f"[SUCESSO] Arquivo validado com sucesso e salvo em: {caminho_destino}")
    except Exception as e:
        print(f"[ERRO GRAVE] O arquivo passou na validação, mas houve falha ao salvar em {caminho_destino}. Detalhes: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correto: python validador_superior.py <caminho_arquivo_temporario> <caminho_destino_final>")
        sys.exit(1)
    
    tmp_path = sys.argv[1]
    dest_path = sys.argv[2]
    validar_arquivo(tmp_path, dest_path)
