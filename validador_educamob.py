import sys
import re
import os
import shutil

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
    if "R$" in conteudo:
        erros.append("O símbolo 'R$' é estritamente proibido. Substitua por 'reais' ou 'centavos' (Regra do MathJax).")
    
    if not conteudo.startswith("---"):
        erros.append("O arquivo deve obrigatoriamente iniciar com YAML frontmatter ('---').")
    
    if "## Referências" not in conteudo:
        erros.append("A seção '## Referências' (ABNT) é obrigatória.")

    # Detecção de Attention Glitch (Alucinação de repetição)
    # Removemos o frontmatter YAML para a checagem não pegar repetições normais de metadados, embora improvável
    texto_limpo = re.sub(r'^---.*?---\n', '', conteudo, flags=re.DOTALL) if conteudo.startswith('---') else conteudo
    
    # Procura por qualquer palavra de 4+ caracteres repetida 3 vezes seguidas
    glitch_match = re.search(r'\b(\w{4,})\s+\1\s+\1\b', texto_limpo, re.IGNORECASE)
    if glitch_match:
        palavra_alucinada = glitch_match.group(1)
        erros.append(f"Alucinação/Attention Glitch detectado: a palavra '{palavra_alucinada}' repetiu-se múltiplas vezes de forma anômala.")

    # Regras Específicas por Tipo
    is_exercicios = caminho_destino.endswith("-exercicios.md")
    
    # Validação do YAML Frontmatter
    try:
        yaml_blocks = re.findall(r'^---\n(.*?)\n---', conteudo, re.MULTILINE | re.DOTALL)
        if yaml_blocks:
            yaml_content = yaml_blocks[0]
            if is_exercicios:
                campos_obrig = ["série:", "disciplina:", "objeto_de_conhecimento:", "ebook_fonte:", "habilidades:", "total_exercicios:", "distribuicao:"]
            else:
                campos_obrig = ["série:", "disciplina:", "unidade_temática:", "objeto_de_conhecimento:", "habilidades:", "pré-requisitos:", "nível_dificuldade:", "tempo_estimado_de_leitura:", "status_de_revisao:", "palavras_chave:", "fonte_bibliografica:"]
            
            for campo in campos_obrig:
                if campo not in yaml_content:
                    erros.append(f"YAML Incompleto: Faltando o campo obrigatório '{campo}' no frontmatter.")
    except Exception:
        erros.append("Falha ao fazer parse do YAML Frontmatter.")

    if is_exercicios:
        # 1. Deve ter exatamente 60 tags de ID
        tags = re.findall(r'<!-- id: q\d{2}', conteudo)
        if len(tags) != 60:
            erros.append(f"Quantidade incorreta de questões. Exigido: exatas 60. Encontrado: {len(tags)}.")
        
        # 2. Formato da tag (tipo, habilidade, dificuldade, objeto)
        # Verifica se pelo menos a maioria (ou a primeira) está completa para não dar falso negativo em regex quebrada, mas ideal é checar todas
        for i in range(1, 61):
            tag_regex = rf'<!-- id: q{i:02d} \| tipo: multipla-escolha \| habilidade: .* \| dificuldade: (basico|intermediario|dificil) \| objeto: .* -->'
            if not re.search(tag_regex, conteudo):
                erros.append(f"Tag HTML ausente ou mal formatada para a questão q{i:02d}. Verifique o padrão obrigatório.")
        
        # 3. Divisões de Nível
        if "## Nível Básico" not in conteudo or "## Nível Intermediário" not in conteudo or "## Nível Difícil" not in conteudo:
            erros.append("Faltando cabeçalhos de níveis de dificuldade obrigatórios.")
            
        # 4. Estrutura de Alternativas
        if conteudo.count("**Gabarito:**") != 60:
            erros.append(f"Quantidade incorreta de gabaritos. Exigido: 60. Encontrado: {conteudo.count('**Gabarito:**')}.")
            
        # 5. Passo a passo nas difíceis
        if "**Etapa 1:**" not in conteudo:
            erros.append("Resolução detalhada com marcações '**Etapa 1:**', '**Etapa 2:**' ausente nas questões difíceis.")
            
    else:
        # É um E-book Teórico
        # 1. Seções obrigatórias
        secoes_obrig = ["## Conceitos", "## Exemplos (Na Prática)", "## Erros Comuns", "## Conexões Interdisciplinares", "## Resumo para Revisão"]
        for secao in secoes_obrig:
            if secao not in conteudo:
                erros.append(f"Seção obrigatória ausente no E-book: '{secao}'.")
                
        # 2. Zero Exercícios
        termos_proibidos = ["Teste Seus Conhecimentos", "Gabarito:", "<!-- tipo:"]
        for termo in termos_proibidos:
            if termo in conteudo:
                erros.append(f"Violação de Teoria Pura: Encontrado o termo de exercício proibido '{termo}'.")

    if erros:
        print("[BLOQUEIO SISTÊMICO] O arquivo foi rejeitado por falhar nas seguintes regras da Educamob:\n")
        for i, erro in enumerate(erros, 1):
            print(f"  {i}. {erro}")
        print("\nO arquivo temporário NÃO foi salvo no destino. Corrija o rascunho e tente novamente.")
        sys.exit(1)
    
    # Se passou, move/copia para o destino final
    try:
        os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
        shutil.copy2(caminho_temporario, caminho_destino)
        print(f"[SUCESSO] Arquivo validado com sucesso e salvo em: {caminho_destino}")
        # Remove arquivo temporário se quiser limpar
        # os.remove(caminho_temporario)
    except Exception as e:
        print(f"[ERRO GRAVE] O arquivo passou na validação, mas houve falha ao salvar em {caminho_destino}. Detalhes: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correto: python validador_educamob.py <caminho_arquivo_temporario> <caminho_destino_final>")
        sys.exit(1)
    
    tmp_path = sys.argv[1]
    dest_path = sys.argv[2]
    validar_arquivo(tmp_path, dest_path)
