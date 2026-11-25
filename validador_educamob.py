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
        erros.append("A seção '## Referências' (ABNT) é obrigatória.")

    # Detecção de Attention Glitch (Alucinação de repetição)
    # Removemos o frontmatter YAML para a checagem não pegar repetições normais de metadados, embora improvável
    texto_limpo = re.sub(r'^---.*?---\n', '', conteudo, flags=re.DOTALL) if conteudo.startswith('---') else conteudo
    
    # 1. Repetição de palavras sucessivas
    glitch_match = re.search(r'\b(\w{4,})\s+\1\s+\1\b', texto_limpo, re.IGNORECASE)
    if glitch_match:
        palavra_alucinada = glitch_match.group(1)
        erros.append(f"Alucinação/Attention Glitch detectado: a palavra '{palavra_alucinada}' repetiu-se sucessivamente de forma anômala.")

    # 2. Repetição de Blocos / Parágrafos Inteiros
    # Separa por quebras duplas (parágrafos)
    paragrafos = [p.strip() for p in texto_limpo.split('\n\n') if len(p.strip()) > 150]
    contagem_paragrafos = Counter(paragrafos)
    for p, qtd in contagem_paragrafos.items():
        if qtd >= 2:
            erros.append(f"Alucinação de Bloco Repetido: Um parágrafo ou seção de {len(p)} caracteres repetiu-se {qtd} vezes no documento.")
            
    # Validação de Integridade do LaTeX / MathJax
    # A) Contagem de Cifrões (Blocos Abertos/Fechados)
    cifroes = re.findall(r'(?<!\\)\$', texto_limpo)
    if len(cifroes) % 2 != 0:
        erros.append(f"Falha de Renderização LaTeX: Há um número ímpar de cifrões ({len(cifroes)} símbolos '$'), indicando um bloco matemático não fechado.")
        
    # B) Quebras de linha destruindo comandos (ex: \n otin$)
    comandos_quebrados = re.search(r'\n\s*(otin|theta|tau|pi|alpha|beta|gamma|rightarrow|leftarrow|subseteq|subset|supset|supseteq|varnothing|circ|times|cdot)\b', texto_limpo)
    if comandos_quebrados:
        comando = comandos_quebrados.group(1)
        erros.append(f"Falha de Renderização LaTeX: Possível barra invertida convertida em quebra de linha perto do comando '{comando}'.")

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
            
        # 6. Auditoria Universal de Balanceamento de Gabaritos (A-E)
        gabs = [g.upper() for g in re.findall(r'\*\*Gabarito:\*\*\s*(?:Alternativa\s*)?\(?([A-Ea-e])\)?', conteudo)]
        if len(gabs) == 60:
            contagem_gabs = Counter(gabs)
            # Verifica equilíbrio em torno de 12 (tolerância: entre 9 e 15 por letra)
            for letra in ['A', 'B', 'C', 'D', 'E']:
                qtd = contagem_gabs.get(letra, 0)
                if qtd < 8 or qtd > 16:
                    erros.append(
                        f"Desbalanceamento Crítico de Gabarito: A alternativa ({letra}) possui {qtd} respostas corretas "
                        f"(esperado: equilibrado em ~12 por letra, tolerância de 8 a 16). Elimine vícios de resposta."
                    )
            # Trava de repetição consecutiva (máximo 3 consecutivas)
            streak = 1
            max_streak = 1
            letra_max_streak = gabs[0]
            for idx_g in range(1, len(gabs)):
                if gabs[idx_g] == gabs[idx_g - 1]:
                    streak += 1
                    if streak > max_streak:
                        max_streak = streak
                        letra_max_streak = gabs[idx_g]
                else:
                    streak = 1
            if max_streak > 3:
                erros.append(
                    f"Repetição Viciada de Gabarito: A alternativa ({letra_max_streak}) repetiu-se {max_streak} vezes "
                    f"consecutivas (o limite máximo permitido é 3 repetições consecutivas)."
                )

        # 7. Motor Universal de Pareamento e Aderência Teórica (E-book Fonte <-> Exercícios)
        # O E-book Teórico é a ÚNICA fonte da verdade autorizada (Single Source of Truth) para qualquer disciplina/nível
        m_fonte = re.search(r'ebook_fonte:\s*["\']?(.*?)["\']?\s*$', conteudo, re.MULTILINE)
        conteudo_ebook_fonte = ""
        if m_fonte:
            fontes_declaradas = [f.strip(' "\'[]') for f in m_fonte.group(1).split(',') if f.strip(' "\'[]')]
            for f_dec in fontes_declaradas:
                caminho_ebook_resolvido = None
                # Tenta resolver o caminho relativo ou na mesma pasta
                candidatos_path = [
                    f_dec,
                    os.path.join(os.path.dirname(caminho_destino), f_dec),
                    os.path.join(os.path.dirname(caminho_destino), os.path.basename(f_dec))
                ]
                for cand in candidatos_path:
                    if cand and os.path.isfile(cand):
                        caminho_ebook_resolvido = cand
                        break

                if caminho_ebook_resolvido:
                    try:
                        with open(caminho_ebook_resolvido, 'r', encoding='utf-8') as ef:
                            conteudo_ebook_fonte += "\n" + ef.read().lower()
                    except Exception:
                        pass
                else:
                    erros.append(f"Pareamento Teórico Quebrado: O e-book fonte '{f_dec}' não foi encontrado no disco.")

        # 8. Verificação de Questões, Faixa Etária, Decorebas e Extrapolação Teórica
        blocos_questoes = re.split(r'### Questão \d+', conteudo)
        enunciados = []
        caminho_lower = caminho_destino.lower()
        eh_fundamental = "fundamental" in caminho_lower
        eh_5_ano = "5-ano" in caminho_lower

        max_len_enunciado = 340 if eh_5_ano else (420 if eh_fundamental else 800)
        max_len_alternativa = 150 if eh_5_ano else (210 if eh_fundamental else 400)

        if len(blocos_questoes) > 1:
            for i, bloco in enumerate(blocos_questoes[1:], 1):
                # Remove comentários HTML invisíveis antes de extrair enunciado e alternativas
                bloco_sem_tag = re.sub(r'<!--.*?-->', '', bloco, flags=re.DOTALL).strip()
                # Extrai o enunciado antes da alternativa 'a)' ou '- (A)' ou similar
                match = re.search(r'^(.*?)(?=\n\s*(?:\*\*|-)?\s*\(?[aA][\)\.])', bloco_sem_tag, re.DOTALL)
                if match:
                    enunciado = match.group(1).strip()
                else:
                    enunciado = bloco_sem_tag.split('\n\n')[0].strip()
                enunciados.append((i, enunciado))

                if eh_fundamental and len(enunciado) > max_len_enunciado:
                    erros.append(
                        f"Inadequação de Faixa Etária (Enunciado Longo): A Questão {i} possui {len(enunciado)} caracteres "
                        f"(limite máximo para esta série: {max_len_enunciado}). Use linguagem direta e adequada à idade."
                    )

                # Trava Universal Anti-Decoreba (Ensino Fundamental)
                if eh_fundamental:
                    if re.search(r'^\s*(?:em\s+qual\s+ano|em\s+que\s+ano|qual\s+foi\s+o\s+ano|em\s+qual\s+data|qual\s+o\s+nome\s+da\s+(?:caravela|nau|embarcação)|qual\s+o\s+nome\s+do\s+papa)\b', enunciado, re.IGNORECASE):
                        erros.append(
                            f"Questão Decoreba Proibida: A Questão {i} cobra memorização isolada de datas ou fatos biográficos/históricos secundários. "
                            f"Foque no método científico, relações causais e habilidades BNCC."
                        )

                # Verifica tamanho das alternativas no Ensino Fundamental
                if eh_fundamental:
                    alternativas = re.findall(r'^\s*(?:\*\*|-)?\s*\(?[a-eA-E][\)\.]\)?\*?\*?\s*(.+)$', bloco_sem_tag, re.MULTILINE)
                    for idx_alt, alt_txt in enumerate(alternativas[:5], 1):
                        if len(alt_txt.strip()) > max_len_alternativa:
                            erros.append(
                                f"Inadequação de Faixa Etária (Alternativa Longa): A Questão {i} tem uma alternativa com "
                                f"{len(alt_txt.strip())} caracteres (limite máximo: {max_len_alternativa})."
                            )
                            break

                # Auditoria de Modelos e Entidades Científicas contra o E-book Fonte (Mundo Fechado Universal)
                if conteudo_ebook_fonte:
                    # Captura menções a modelos, teoremas, leis, teorias, equilíbrios ou nomes compostos científicos
                    padroes_entidades = [
                        r'\b(?:teorema|lei|modelo|princípio|equilíbrio|ciclo|efeito|equação|teoria)\s+de\s+([A-ZÁÉÍÓÚ][a-záéíóú]+(?:\s+e\s+[A-ZÁÉÍÓÚ][a-záéíóú]+|-?[A-ZÁÉÍÓÚ][a-záéíóú]+)?)\b',
                        r'\b([A-ZÁÉÍÓÚ][a-z]+-[A-ZÁÉÍÓÚ][a-z]+)\b'
                    ]
                    # Termos hifenizados ou expressões da língua portuguesa/geografia que não são epônimos científicos
                    excecoes_comuns = {
                        'de-obra', 'bem-estar', 'guarda-chuva', 'sul-americano', 'sul-americana',
                        'norte-americano', 'norte-americana', 'meio-dia', 'dia-a-dia', 'quebra-cabeça',
                        'leste-oeste', 'oeste-leste', 'norte-sul', 'sul-norte', 'centro-oeste', 'centro-sul',
                        'centro-norte', 'meia-noite', 'sol-lua', 'terra-lua', 'terra-sol', 'lua-terra',
                        'beija-flor', 'cão-guia', 'wi-fi', 'no-break', 'ultra-alta', 'super-terras',
                        'mini-netunos', 'auto-incompatibilidade', 'peru-chile', 'pan-africano', 'si-si',
                        'adenina-timina', 'guanina-citosina', 'cl-cl', 'br-br', 'h-br', 'h-h', 'c-h', 'c-c', 'c-cl', 'o-h', 'n-h', 'c-o', 'f-f', 'i-i', 'h-cl', 'h-f', 'h-i', 'ar-ar', 'rim-bexiga', 'brasil-malvinas',
                        'terra-atmosfera', 'mato-grossense', 'cambriano-ordoviciano', 'graus-dia', 'degree-days', 'cachorro-quente'
                    }
                    for padrao in padroes_entidades:
                        for m_ent in re.finditer(padrao, bloco_sem_tag):
                            entidade_str = m_ent.group(0).lower()
                            termo_nucleo = m_ent.group(1).lower() if m_ent.groups() else entidade_str
                            
                            # Ignora se for exceção comum ou ponto cardeal/geográfico
                            if termo_nucleo in excecoes_comuns or entidade_str in excecoes_comuns:
                                continue
                            # Ignora se for princípio genérico com verbos no infinitivo (ex: reduzir e reciclar)
                            if 'reduzir' in entidade_str or 'reciclar' in entidade_str or 'reutilizar' in entidade_str:
                                continue
                                
                            # Se for termo composto com hífen, aceita se todas as partes constam no e-book (ex: Watson e Crick no e-book vs Watson-Crick na lista)
                            if '-' in termo_nucleo:
                                partes_hifen = [p.strip() for p in termo_nucleo.split('-') if len(p.strip()) > 2]
                                if partes_hifen and all(p in conteudo_ebook_fonte for p in partes_hifen):
                                    continue

                            if termo_nucleo not in conteudo_ebook_fonte and entidade_str not in conteudo_ebook_fonte:
                                erros.append(
                                    f"Violação de Pareamento Teórico (Mundo Fechado): A Questão {i} cobra a entidade/modelo '{m_ent.group(0)}', "
                                    f"mas esse conceito NÃO foi ensinado no e-book base '{caminho_ebook_resolvido}'. "
                                    f"Exercícios devem derivar estritamente da teoria ensinada."
                                )

        # 9. Bloqueio Universal de Pedantismo/"Concursês" e Extrapolação Etária por Segmento (5º Ano ao Ensino Médio)
        corpo_questoes_sem_ref = texto_limpo.split("## Referências")[0] if "## Referências" in texto_limpo else texto_limpo
        corpo_lower = corpo_questoes_sem_ref.lower()

        # 9.1. Bloqueio Universal de Linguagem Rebuscada / "Concursês" (Aplica-se a TODOS os segmentos, inclusive Ensino Médio)
        padroes_pedantes_universais = [
            r"\bsupracitad[oa]s?\b", r"\boutrossim\b", r"\bdestarte\b", r"\bprecípu[oa]s?\b",
            r"\bconsubstancia\w*\b", r"\bdepreende-se\b", r"\binfere-se\s+que\s+a\s+assertiva\b",
            r"\bassertiva\b", r"\bmormente\b", r"\bno\s+tocante\s+a\b", r"\batinente\w*\b",
            r"\bconcernente\w*\b", r"\bdirimir\b", r"\benseja\w*\b", r"\bauferir\b",
            r"\bprescind\w*\b", r"\bimprescind\w*\b", r"\binexor\w*\b", r"\bidiossincra\w*\b",
            r"\banátema\b", r"\bprerrogativa\w*\b", r"\bcorrobor\w*\b", r"\bintrínsec[oa]s?\b",
            r"\bextrínsec[oa]s?\b", r"\bdicotomi\w*\b", r"\bsubjacente\w*\b", r"\befêmer[oa]s?\b",
            r"\bmitigar\b", r"\bfomentar\b", r"\bhegemônic\w*\b", r"\bepistemológic\w*\b",
            r"\bontológic\w*\b", r"\baxiológic\w*\b", r"\bteleológic\w*\b", r"\bhermenêutic\w*\b",
            r"\bpropedêutic\w*\b", r"\bvernáculo\b", r"\bqui-la\b", r"\bfi-lo\b", r"\bfizerdes\b",
            r"\baqueloutro\w*\b"
        ]
        for pat_ped in padroes_pedantes_universais:
            m_ped = re.search(pat_ped, corpo_lower)
            if m_ped:
                erros.append(
                    f"Violação de Simplicidade Didática (Concursês / Linguagem Rebuscada): "
                    f"O termo '{m_ped.group(0)}' dificulta a leitura. A linguagem da Educamob deve ser simples, direta e facilitadora em todos os segmentos."
                )

        # 9.2. Bloqueio de Extrapolação de Ensino Superior no Ensino Médio
        eh_medio = "medio" in caminho_lower or "médio" in caminho_lower or "serie" in caminho_lower
        if eh_medio:
            termos_proibidos_em = [
                "tolman-oppenheimer", "chandrasekhar", "schwarzschild", "ergosfera",
                "lense-thirring", "instabilidade de pares", "teorema do virial",
                "ressonância de hoyle", "trilha de hayashi", "zams", "paczynski",
                "cáustica gravitacional", "rede de cáusticas", "microlenteamento",
                "equação de drake", "kardashev", "quilonova", "processo-r", "processo-s",
                "terceiro dragado", "ramo gigante assintótico", "instabilidade de jeans",
                "fuga hidrodinâmica", "klein-gordon", "dq/dt", "tensor de inércia",
                "transformada de fourier", "operon lac", "clearance renal", "burgess shale"
            ]
            for termo_em in termos_proibidos_em:
                if termo_em in corpo_lower:
                    erros.append(
                        f"Extrapolação Etária no Ensino Médio (Jargão Universitário/Pós-Graduação): "
                        f"O termo '{termo_em}' extrapola o currículo do Ensino Médio / ENEM."
                    )

        # 9.3. Bloqueio de Extrapolação Etária por Série no Ensino Fundamental (5º ao 9º Ano)
        if eh_fundamental:
            termos_proibidos_ef = [
                "tolman-oppenheimer", "chandrasekhar", "schwarzschild", "ergosfera", "penrose",
                "lense-thirring", "instabilidade de pares", "degenerescência", "exclusão de pauli",
                "fermi-dirac", "bose-einstein", "teorema do virial", "índice adiabático",
                "ressonância de hoyle", "trilha de hayashi", "zams", "paczynski",
                "cáustica gravitacional", "rede de cáusticas", "microlenteamento",
                "stefan-boltzmann", "equação de drake", "kardashev", "quilonova",
                "processo-r", "processo-s", "captura rápida de nêutrons", "captura lenta de nêutrons",
                "terceiro dragado", "ramo gigante assintótico", "instabilidade de jeans",
                "fuga hidrodinâmica", "schrödinger", "heisenberg", "klein-gordon",
                "cúbica de faces centradas", "cúbica de corpo centrado", "discordâncias atômicas",
                "endurecimento por solução sólida", "dq/dt", "energia livre de gibbs",
                "equação de nernst", "equação de arrhenius", "orbital molecular", "hibridização sp",
                "forças de london", "dipolo induzido", "diamagnétic", "paramagnétic",
                "susceptibilidade magnética", "cisalhamento", "módulo de young", "tensão de escoamento",
                "michaelis-menten", "ciclo de krebs", "fosforilação oxidativa",
                "cadeia transportadora de elétrons", "piruvato desidrogenase", "acetil-coa",
                "potencial de ação despolarizante", "exaptação", "anidrobiose", "criptobiose",
                "transposon", "operon lac", "transcriptase", "aminoacil-trna", "fator de transcrição",
                "pressão coloidosmótica", "clearance renal", "renina-angiotensina",
                "biot-savart", "equações de maxwell", "força de lorentz", "indutância mútua",
                "impedância capacitiva", "reatância indutiva", "equação de clapeyron",
                "ciclo de carnot", "entropia molar", "transformada de fourier",
                "efeito doppler relativístico", "aberração cromática", "birrefringência",
                "equação de bernoulli", "número de reynolds", "viscosidade cinemática", "tensor de inércia",
                "hardy-weinberg", "equilíbrio de hardy", "frequência alélica", "frequência genotípica",
                "seleção disruptiva", "seleção direcional", "seleção estabilizadora", "deriva genética",
                "relógio molecular", "coevolução gene-cultura", "teoria do sinal honesto", "sinal honesto",
                "burgess shale", "explosão cambriana", "explosão do cambriano", "fanerozoico"
            ]
            if eh_5_ano:
                termos_proibidos_ef.extend([
                    "arquimedes", "retículo cristalino", "ligação metálica", "ligação covalente",
                    "ligação iônica", "elétrons livres", "fótons", "entalpia", "entropia",
                    "lei de ohm", "lei de fourier", "calor específico molar"
                ])
            for termo in termos_proibidos_ef:
                if termo in corpo_lower:
                    erros.append(
                        f"Extrapolação Curricular / Jargão Avançado Proibido no Ensino Fundamental: "
                        f"O termo '{termo}' é incompatível com a faixa etária de 10 a 14 anos (BNCC)."
                    )

            # Bloqueio específico de metalinguagem e abstrações por série (5º ao 7º ano) e teóricos de pós-graduação (5º ao 9º ano)
            padroes_idade_ef = [
                r"\bbraudel\b", r"\bkoselleck\b", r"\bspivak\b", r"\bbertin\b", r"\bbauman\b", r"\bgramsci\b"
            ]
            if eh_5_ano:
                padroes_idade_ef.extend([
                    r"\balomorfi\w*\b", r"\bdesinência\w*\b", r"\bvogal\s+temática\b",
                    r"\benclític\w*\b", r"\bproclític\w*\b", r"\bmesóclise\b", r"\bênclise\b", r"\bpróclise\b",
                    r"\banafóric\w*\b", r"\bcatanfóric\w*\b", r"\bcatafóric\w*\b", r"\bendofóric\w*\b",
                    r"\banáfora\b", r"\bcatáfora\b", r"\bdeixis\b", r"\bdêitic\w*\b",
                    r"\bmorfossint\w*\b", r"\badjunto\s+adnominal\b", r"\bobjeto\s+direto\b",
                    r"\bobjeto\s+indireto\b", r"\bsujeito\s+desinencial\b", r"\btransitividade\b",
                    r"\bregência\s+verbal\b", r"\bpredicativo\b", r"\blexical\b", r"\beufoni\w*\b",
                    r"\beufônic\w*\b", r"\boração\s+reduzida\b", r"\boração\s+coordenada\b",
                    r"\boração\s+subordinada\b", r"\bverbo\s+defectivo\b", r"\bforma\s+defectiva\b",
                    r"\bpostulado\b", r"\baxioma\b", r"\bincógnita\b", r"\bpolinômio\b",
                    r"\bestamental\b", r"\bantropocêntric\w*\b", r"\bgeocêntric\w*\b", r"\bheliocêntric\w*\b"
                ])
            elif "6-ano" in caminho_lower or "7-ano" in caminho_lower:
                padroes_idade_ef.extend([
                    r"\balomorfi\w*\b", r"\bendofóric\w*\b", r"\bdeixis\b", r"\bdêitic\w*\b",
                    r"\boração\s+reduzida\b", r"\bmesóclise\b", r"\bestamental\b", r"\bmacroeconômic\w*\b"
                ])

            for pat_id in padroes_idade_ef:
                m_id = re.search(pat_id, corpo_lower)
                if m_id:
                    erros.append(
                        f"Inadequação de Linguagem à Idade do Estudante: "
                        f"O termo '{m_id.group(0)}' extrapola a maturidade linguística desta série escolar."
                    )

        encontrou_similaridade = False
        for i in range(len(enunciados)):
            for j in range(i + 1, len(enunciados)):
                q_num_1, txt_1 = enunciados[i]
                q_num_2, txt_2 = enunciados[j]
                
                if len(txt_1) > 20 and len(txt_2) > 20:
                    ratio = difflib.SequenceMatcher(None, txt_1, txt_2).ratio()
                    if ratio >= 0.60:
                        erros.append(f"Falta de diversidade temática: As questões {q_num_1} e {q_num_2} são muito similares ({ratio:.0%} de igualdade. Limite máximo: 60%).")
                        encontrou_similaridade = True
                        break
            if encontrou_similaridade:
                break
                
        prefixos = []
        for _, txt in enunciados:
            palavras = txt.split()
            if len(palavras) >= 3:
                prefixo = " ".join([re.sub(r'[^\w\s]', '', p).lower() for p in palavras[:3]])
                prefixos.append(prefixo)
        
        if prefixos:
            contagem = Counter(prefixos)
            prefixo_comum, qtd = contagem.most_common(1)[0]
            if qtd > 6:
                erros.append(f"Falta de diversidade de modelos: O início de frase '{prefixo_comum}' repetiu-se em {qtd} questões (o limite máximo é 6, equivalente a 10%).")
            
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
                
        # 3. Densidade de Palavras Dinâmica por Nível (Fundamental vs Médio/Superior)
        # Removemos o frontmatter YAML para contar apenas o texto real
        texto_limpo = re.sub(r'^---.*?---\n', '', conteudo, flags=re.DOTALL) if conteudo.startswith('---') else conteudo
        total_palavras = len(texto_limpo.split())
        
        # Define o limite baseado no caminho (ex: content/ensino-medio/...)
        caminho_lower = caminho_destino.lower()
        if "medio" in caminho_lower or "superior" in caminho_lower:
            limite_minimo = 2000
            nivel_nome = "Ensino Médio/Superior"
        else:
            # Assume Fundamental por padrão ou se "fundamental" estiver no path
            limite_minimo = 2000
            nivel_nome = "Ensino Fundamental"
            
        if total_palavras < limite_minimo:
            erros.append(f"Densidade Insuficiente ({nivel_nome}): O E-book possui apenas {total_palavras} palavras. A regra da skill E-book Creator exige no mínimo {limite_minimo} palavras para esta etapa de ensino.")

        # 4. Quantidade Mínima de Fontes (Mínimo 5)
        bloco_referencias = re.search(r'## Referências(.*?)(?=\n##|\n>|\Z)', conteudo, re.DOTALL)
        if bloco_referencias:
            texto_refs = bloco_referencias.group(1)
            # Conta itens de lista que começam com hífen ou asterisco
            num_fontes = len(re.findall(r'^\s*[-*]\s', texto_refs, re.MULTILINE))
            if num_fontes < 5:
                erros.append(f"Fontes Insuficientes: O E-book listou apenas {num_fontes} referências. A regra da skill E-book Creator exige no mínimo 5 fontes bibliográficas distintas.")
                
            # Verifica BNCC para Fundamental e Médio
            if "medio" in caminho_lower or "fundamental" in caminho_lower:
                if "bncc" not in texto_refs.lower() and "base nacional comum curricular" not in texto_refs.lower():
                    erros.append("Alinhamento BNCC Ausente: A BNCC (Base Nacional Comum Curricular) deve ser obrigatoriamente citada como uma das fontes bibliográficas nos e-books do Ensino Fundamental e Médio.")

        # 5. Proporcionalidade Estrutural (Anti-Padding)
        if total_palavras > 0:
            # A) Trava de Apêndices (Máximo 20%)
            blocos_apendice = re.findall(r'(###? Apêndice.*?)(?=\n##|\Z)', conteudo, re.DOTALL | re.IGNORECASE)
            palavras_apendice = sum(len(bloco.split()) for bloco in blocos_apendice)
            proporcao_apendice = palavras_apendice / total_palavras
            if proporcao_apendice > 0.20:
                erros.append(f"Desbalanceamento Estrutural: Os Apêndices representam {proporcao_apendice:.1%} do texto ({palavras_apendice} palavras). O limite máximo permitido é 20% para evitar 'padding' artificial. Invista em 'Exemplos'.")
                
            # B) Trava de Core Teórico (Mínimo 50%)
            # Pega desde "## Conceitos" até antes de "## Erros Comuns" (engloba Conceitos e Exemplos)
            bloco_core = re.search(r'(## Conceitos.*?)(?=\n## Erros Comuns|\n## Conexões|\n## Resumo|\Z)', conteudo, re.DOTALL)
            if bloco_core:
                palavras_core = len(bloco_core.group(1).split())
                proporcao_core = palavras_core / total_palavras
                if proporcao_core < 0.50:
                    erros.append(f"Desbalanceamento Estrutural: O núcleo essencial (Conceitos + Exemplos) representa apenas {proporcao_core:.1%} do texto ({palavras_core} palavras). É exigido no mínimo 50% de dedicação à teoria base e resoluções práticas.")

    if erros:
        print("[BLOQUEIO SISTÊMICO] O arquivo foi rejeitado por falhar nas seguintes regras da Educamob:\n")
        for i, erro in enumerate(erros, 1):
            print(f"  {i}. {erro}")
        print("\nO arquivo temporário NÃO foi salvo no destino. Corrija o rascunho e tente novamente.")
        sys.exit(1)
    
    # Se passou, move/copia para o destino final se forem caminhos distintos
    try:
        abs_temp = os.path.abspath(caminho_temporario)
        abs_dest = os.path.abspath(caminho_destino)
        if abs_temp != abs_dest:
            os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
            shutil.copy2(caminho_temporario, caminho_destino)
            print(f"[SUCESSO] Arquivo validado com sucesso e salvo em: {caminho_destino}")
        else:
            print(f"[SUCESSO] Arquivo já está em conformidade com todas as regras: {caminho_destino}")
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
