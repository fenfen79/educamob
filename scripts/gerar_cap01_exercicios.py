# -*- coding: utf-8 -*-
import os
import sys
import re
import subprocess
from collections import Counter

def balancear_questoes(questoes_brutas):
    # Alvo: padrão circular ['A', 'B', 'C', 'D', 'E'] * 12
    # Isso garante exatamente 12 A, 12 B, 12 C, 12 D, 12 E e streak máxima 1!
    alvo_letras = ['A', 'B', 'C', 'D', 'E'] * 12
    
    questoes_balanceadas = []
    letras = ['A', 'B', 'C', 'D', 'E']

    for i, q in enumerate(questoes_brutas):
        num, hab, dif, enunc, a, b, c, d, e, gab_orig, res = q
        alvo = alvo_letras[i]
        
        # Mapeamento atual de alternativas
        alt_map = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}
        
        if gab_orig != alvo:
            # Troca o texto da alternativa correta original com a do alvo
            texto_correto = alt_map[gab_orig]
            texto_outro = alt_map[alvo]
            alt_map[alvo] = texto_correto
            alt_map[gab_orig] = texto_outro
            
        novo_gab = alvo
        
        # Atualiza a resolução se ela fizer menção explícita à letra anterior
        # No nosso caso, as resoluções explicam o conceito ou usam Etapa 1 / Etapa 2
        questoes_balanceadas.append((
            num, hab, dif, enunc,
            alt_map['A'], alt_map['B'], alt_map['C'], alt_map['D'], alt_map['E'],
            novo_gab, res
        ))
        
    return questoes_balanceadas

def gerar_cap01():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-01-filosofia-kemetica-egito-pre-grega/ebooks/em-fil-c01-filosofia-kemetica-egito-pre-grega-exercicios.md"
    temp_draft = "temp_draft.md"

    # 60 questões brutas
    questoes_brutas = []

    # NÍVEL BÁSICO (Questões 1 a 20)
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "O conceito de 'Milagre Grego', difundido por historiadores europeus no século XIX, sustentava qual ideia sobre o nascimento da razão?",
        "A filosofia surgiu de modo espontâneo e exclusivo na Grécia, sem ligação com outros povos.",
        "A racionalidade foi construída a partir da incorporação direta de saberes de Roma.",
        "O pensamento crítico foi elaborado como cópia fiel de tradições míticas persas.",
        "A ciência grega nasceu da recusa expressa de qualquer forma de diálogo comercial marítimo.",
        "A reflexão racional começou simultaneamente em todos os continentes do planeta.",
        "A",
        "O mito do 'Milagre Grego' defendia o nascimento espontâneo e isolado da razão na Grécia clássica."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "As pesquisas antropológicas e linguísticas de Cheikh Anta Diop demonstraram qual característica central sobre a civilização do Antigo Egito?",
        "Pertencia ao universo nórdico por sua estrutura física e mitologia guerreira.",
        "Era uma civilização de matriz africana, conectada cultural e biologicamente aos povos do continente.",
        "Tinha origens mesopotâmicas exclusivas, sem contato com o restante da África.",
        "Constituía uma colônia grega estabelecida antes da formação das primeiras dinastias.",
        "Limitava-se a imitar preceitos religiosos surgidos na Península Arábica.",
        "B",
        "Diop comprovou a raiz africana e autóctone de Kemet por meio de análises biológicas e culturais."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Na tradição do Antigo Kemet, qual significado fundamental possuía o princípio de Ma'at?",
        "Um ritual guerreiro destinado a justificar a invasão de territórios vizinhos.",
        "Um conjunto mecânico de regras comerciais voltadas ao comércio de cereais.",
        "A harmonia cósmica, a verdade, a justiça social e a retidão moral.",
        "Uma técnica mágica de mumificação restrita aos faraós de dinastias guerreiras.",
        "Uma teoria voltada exclusivamente a calcular a área de monumentos fúnebres.",
        "C",
        "Ma'at traduz os valores integrados de verdade, justiça, ordem universal e equilíbrio moral."
    ))

    questoes_brutas.append((
        4, "EM13CHS103", "basico",
        "A obra As Máximas de Ptahhotep, redigida por volta de 2400 a.C., é reconhecida na história do pensamento por qual motivo?",
        "Apresentar a primeira codificação de leis baseada na pena de talião.",
        "Ser o primeiro tratado sistemático de conduta moral e sabedoria prática documentado por escrito.",
        "Defender o isolamento do filósofo em relação aos problemas da administração pública.",
        "Instituir a obrigatoriedade de sacrifícios de animais para a purificação da alma.",
        "Estabelecer a retórica de confronto agressivo como método supremo de verdade.",
        "B",
        "As Máximas de Ptahhotep constituem o mais antigo texto conhecido de reflexão moral e ética."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Em oposição a Ma'at, qual força cósmica e moral representava a mentira, o caos e a injustiça na visão kemética?",
        "Ankh.",
        "Ptah.",
        "Isfet.",
        "Nun.",
        "Ib.",
        "C",
        "Isfet personifica o princípio da desordem, mentira, destruição e injustiça que ameaça o equilíbrio do cosmos."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "O linguista Théophile Obenga comprovou a relação do Antigo Egito com a África por meio de qual elemento científico?",
        "Parentesco linguístico direto entre o egípcio clássico e línguas africanas modernas.",
        "Semelhança arquitetônica entre templos egípcios e muralhas medievais europeias.",
        "Uso compartilhado de sistemas numéricos criados por matemáticos romanos.",
        "Identidade genética comprovada entre faraós e imperadores da dinastia persa.",
        "Presença de ferramentas de ferro idênticas às fabricadas na Grécia clássica.",
        "A",
        "Obenga demonstrou os laços lexicais e estruturais entre o egípcio antigo e famílias linguísticas africanas."
    ))

    questoes_brutas.append((
        7, "EM13CHS105", "basico",
        "O historiador Martin Bernal, na obra Black Athena, denominou de 'Modelo Antigo' qual concepção histórica sobre a Grécia?",
        "A tese oitocentista que considerava a civilização grega de origem puramente nórdica.",
        "O reconhecimento feito pelos próprios gregos clássicos de suas dívidas culturais com o Egito.",
        "A ideia de que a filosofia grega copiou integralmente a religião politeísta romana.",
        "A teoria de que Atenas foi fundada por navegadores originários da Europa Central.",
        "A negação de que tenha havido qualquer contato entre o Mediterrâneo e o Nilo.",
        "B",
        "O Modelo Antigo descreve o reconhecimento dos historiadores e sábios gregos sobre as origens egípcias de seus saberes."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "No ritual da Psicostasia, narrado no livro Pert Em Hru, o que era colocado no prato da balança para ser pesado contra a pena de Ma'at?",
        "O cérebro do falecido.",
        "O ouro acumulado em vida.",
        "Os títulos de nobreza conquistados.",
        "O coração humano (Ib).",
        "O papiro funerário com orações.",
        "D",
        "O coração (Ib), considerado o centro da consciência moral e do julgamento, era colocado na balança de Ma'at."
    ))

    questoes_brutas.append((
        9, "EM13CHS103", "basico",
        "Na primeira máxima de seu tratado moral, o vizir Ptahhotep orienta o sábio a adotar qual postura diante do conhecimento?",
        "Ouvir com modéstia tanto o ignorante quanto o instruído, pois a arte não tem limites.",
        "Debater apenas com magistrados de posição social superior para demonstrar poder.",
        "Impor silêncio absoluto a todos os trabalhadores braçais da comunidade.",
        "Guardar os ensinamentos em segredo para assegurar vantagens financeiras pessoais.",
        "Afirmar a perfeição de suas próprias ideias em qualquer disputa pública.",
        "A",
        "Ptahhotep ensina que a sabedoria exige humildade, pois boas palavras podem vir até de quem trabalha no moinho."
    ))

    questoes_brutas.append((
        10, "EM13CHS105", "basico",
        "Qual pensador pioneiro viveu no Egito e associou o princípio primordial de todas as coisas à Água, espelhando o conceito de Nun?",
        "Heráclito de Éfeso.",
        "Parmênides de Eleia.",
        "Sócrates.",
        "Tales de Mileto.",
        "Demócrito de Abdera.",
        "D",
        "Tales de Mileto estudou no Egito e concebeu a água como princípio gerador de tudo, refletindo as águas primordiais de Nun."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Na cosmologia kemética, qual termo designava o oceano primordial caótico de onde surgiu o Universo?",
        "Atum.",
        "Nun.",
        "Ma'at.",
        "Shu.",
        "Ankh.",
        "B",
        "Nun representa o oceano de águas infinitas e caóticas que existia antes da organização da criação cósmica."
    ))

    questoes_brutas.append((
        12, "EM13CHS103", "basico",
        "As Instruções para Meri-Ka-Ré, texto do Império Médio kemético, afirmam que a conduta do governante deve priorizar qual elemento?",
        "A construção de pirâmides monumentais para intimidar cidades vizinhas.",
        "A prática da justiça e do coração pacífico, mais valiosa que sacrifícios de animais.",
        "A cobrança de tributos impiedosos para garantir os luxos da corte real.",
        "A punição física severa como único instrumento para manter a ordem civil.",
        "A conquista de territórios ricos em minérios e metais preciosos.",
        "B",
        "O texto ensina que a retidão e a justiça do governante agradam mais ao sagrado do que rituais vazios de bois."
    ))

    questoes_brutas.append((
        13, "EM13CHS102", "basico",
        "O termo Kemet, utilizado pelos próprios habitantes do Antigo Egito para designar sua terra, tinha qual significado original?",
        "Terra Dourada dos Faraós.",
        "Império do Sol Nascente.",
        "Terra Negra, em alusão ao lodo fertilizante e à população.",
        "Reino Sagrado de Gizé.",
        "Terra Seca entre os Mares.",
        "C",
        "Kemet significa 'Terra Negra', referindo-se tanto à fertilidade do lodo do Nilo quanto à cor da população."
    ))

    questoes_brutas.append((
        14, "EM13CHS105", "basico",
        "A famosa inscrição no pórtico de templos gregos 'Conhece-te a ti mesmo' já estava presente nos templos de Luxor e Karnak sob qual formulação?",
        "'Ganha honras militares e serás lembrado pelos teus feitos.'",
        "'Homem, conhece a ti mesmo e conhecerás os deuses e o universo.'",
        "'Submete tua vontade ao rei e alcançarás a paz duradoura.'",
        "'Evita a dúvida e segue cegamente as regras dos sacerdotes.'",
        "'O conhecimento é perigoso para quem não governa a cidade.'",
        "B",
        "A reflexão voltada ao autoconhecimento já era ensinada nos templos egípcios como chave para compreender o cosmos."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "No tribunal de Osíris, se o coração do indivíduo fosse mais pesado que a pena da verdade, qual destino trágico ele sofria?",
        "Era devorado pelo monstro Ammit e condenado ao esquecimento definitivo.",
        "Recebia nova chance encarnando imediatamente como sacerdote em Tebas.",
        "Era banido para as terras secas do deserto líbio sem direito a julgamento.",
        "Ganhava um túmulo simples com permissão para repousar junto aos servos.",
        "Tornava-se um juiz auxiliar no próprio tribunal do mundo subterrâneo.",
        "A",
        "O coração injusto era consumido por Ammit, o que representava a aniquilação moral e o esquecimento cósmico."
    ))

    questoes_brutas.append((
        16, "EM13CHS102", "basico",
        "O conceito de 'epistemicídio', articulado por Sueli Carneiro a partir de Boaventura de Sousa Santos, designa qual fenômeno histórico?",
        "A celebração da diversidade de teorias em universidades públicas.",
        "A criação de bibliotecas comunitárias em áreas rurais periféricas.",
        "A destruição, desvalorização e invisibilização sistemática dos saberes de povos colonizados.",
        "A adoção de tecnologias digitais para preservar línguas indígenas ancestrais.",
        "A tradução integral de tratados clássicos para línguas regionais africanas.",
        "C",
        "Epistemicídio é a supressão sistemática da capacidade racional e das memórias de povos submetidos ao colonialismo."
    ))

    questoes_brutas.append((
        17, "EM13CHS105", "basico",
        "No diálogo Fedro, Platão atribui a invenção da escrita, dos números e da geometria a qual divindade do Vale do Nilo?",
        "Osíris.",
        "Ísis.",
        "Anúbis.",
        "Hórus.",
        "Thot (Tehuti).",
        "E",
        "Platão registra explicitamente em Fedro que o deus egípcio Thot inventou os números, o cálculo, a geometria e a escrita."
    ))

    questoes_brutas.append((
        18, "EM13CHS103", "basico",
        "Qual pensador grego viveu cerca de 22 anos no Egito, aprendendo geometria e a doutrina da transmigração da alma?",
        "Tales de Mileto.",
        "Pitágoras de Samos.",
        "Anaxágoras.",
        "Epicuro.",
        "Zenão de Eleia.",
        "B",
        "Pitágoras residiu por mais de duas décadas em Kemet, absorvendo ritos sacerdotais, matemática sagrada e a metempsicose."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "As 42 Declarações de Inocência, pronunciadas pelo falecido no salão do julgamento, tinham como foco principal qual compromisso ético?",
        "Provar riqueza material e ostentação de poder político na comunidade.",
        "Pedir clemência cega por meio de promessas de suborno aos juízes divinos.",
        "Afirmar a ausência de atos lesivos a outras pessoas e ao equilíbrio da natureza.",
        "Justificar guerras de pilhagem feitas em nome do crescimento do reino.",
        "Demonstrar a superioridade dos nobres sobre os trabalhadores escravizados.",
        "C",
        "As confissões comprovavam que o indivíduo não cometeu roubo, mentira, poluição da terra ou dano contra semelhantes."
    ))

    questoes_brutas.append((
        20, "EM13CHS105", "basico",
        "A Lei Federal brasileira nº 10.639/2003 tem como objetivo curricular prioritário na Educação Básica promover qual transformação?",
        "Retirar conteúdos de história clássica para ensinar apenas línguas modernas.",
        "Tornar obrigatório o ensino de História e Cultura Afro-Brasileira e Africana, superando preconceitos curriculares.",
        "Proibir o estudo de filósofos gregos e romanos em escolas públicas de Ensino Médio.",
        "Limitar as aulas de Filosofia a temas voltados exclusivamente ao mercado financeiro.",
        "Substituir o currículo nacional por normas educacionais de organizações estrangeiras.",
        "B",
        "A Lei 10.639/2003 combate o racismo institucional ao incluir as contribuições civilizatórias africanas no currículo."
    ))

    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao comparar a ética de Ptahhotep com visões de conduta que privilegiam a vitória verbal a qualquer custo, nota-se que o vizir egípcio propunha:",
        "A humilhação pública do oponente fraco para consolidar o prestígio perante a multidão.",
        "O domínio sereno das palavras e a recusa da ira, pois a razão perde a força quando cede ao descontrole.",
        "A imposição de punições corporais imediatas a qualquer cidadão que fizesse perguntas críticas.",
        "A defesa do enriquecimento pessoal por meios escusos como prova máxima de inteligência prática.",
        "O uso deliberado da mentira para desarticular os argumentos apresentados pelo adversário no tribunal.",
        "B",
        "Ptahhotep ensina o controle emocional e a calma como virtudes essenciais para manter a dignidade no debate."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "No Colóquio do Cairo organizado pela UNESCO em 1974, Cheikh Anta Diop e Théophile Obenga enfrentaram teses colonialistas demonstrando que:",
        "O Egito era uma sociedade biologicamente isolada de qualquer influência de outros continentes.",
        "A cultura do vale do Nilo foi inteiramente introduzida por conquistadores vindos do mar Báltico.",
        "Os vestígios materiais, linguísticos e corporais convergem para a matriz autóctone negro-africana de Kemet.",
        "A civilização faraônica teve início somente após a dominação imperialista macedônia de Alexandre.",
        "Os hieróglifos egípcios eram decodificados unicamente por meio de dialetos germânicos ancestrais.",
        "C",
        "Diop e Obenga apresentaram provas laboratoriais e linguísticas que ratificaram a identidade africana do Antigo Egito."
    ))

    questoes_brutas.append((
        23, "EM13CHS101", "intermediario",
        "Na relação entre Ma'at e a conduta cotidiana no Antigo Kemet, a prática da justiça pelo ser humano era entendida como:",
        "Um mero cálculo burocrático de conveniência para obter privilégios fiscais da corte.",
        "Uma obrigação vital para preservar o próprio equilíbrio do cosmos frente ao avanço do caos.",
        "Uma tarefa secundária reservada exclusivamente aos sacerdotes em dias de celebração fúnebre.",
        "Um recurso retórico passageiro para iludir juízes e fugir das penalidades de contratos civis.",
        "Um costume supersticioso sem nenhuma conexão com a vida política da comunidade urbana.",
        "B",
        "Para a cosmologia kemética, as ações humanas justas alimentam Ma'at e impedem a desagregação da ordem natural."
    ))

    questoes_brutas.append((
        24, "EM13CHS105", "intermediario",
        "Martin Bernal argumenta que o 'Modelo Ariano' foi formulado a partir do final do século XVIII com qual propósito ideológico central?",
        "Celebrar as raízes afrodiaspóricas da civilização europeia durante a Revolução Industrial.",
        "Apagar as dívidas culturais da Grécia para com a África, alinhando a história ao racismo e colonialismo.",
        "Incentivar o intercâmbio de estudantes entre universidades de Paris, Londres e do Vale do Nilo.",
        "Reconhecer a primazia dos conhecimentos técnicos de povos do Sul Global em feiras de ciências.",
        "Unificar os cultos politeístas do Mediterrâneo sob a liderança dos templos de Tebas e Mênfis.",
        "B",
        "O Modelo Ariano retirou o Egito da origem do pensamento clássico para servir aos interesses racistas e coloniais europeus."
    ))

    questoes_brutas.append((
        25, "EM13CHS103", "intermediario",
        "Os Ensinamentos de Amenemope guardam notável semelhança temática e textual com qual livro sapiencial do Antigo Testamento bíblico?",
        "Gênesis.",
        "Levítico.",
        "Provérbios.",
        "Apocalipse.",
        "Números.",
        "C",
        "Capítulos do Livro dos Provérbios bíblico refletem a estrutura poética e moral das máximas de Amenemope sobre solidariedade."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "A acusação de ganância destrutiva (Un-Ma'at) feita por Ptahhotep tinha como alvo principal evitar qual desfecho na vida coletiva?",
        "O aumento do número de artesãos especializados nas oficinas de tecelagem.",
        "A corrupção do caráter moral dos líderes e a dissolução dos laços comunitários e familiares.",
        "A diminuição das áreas de plantio nas margens do Nilo durante os períodos de seca.",
        "O surgimento de novos estilos poéticos voltados ao louvor dos trabalhadores do campo.",
        "A perda de registros astronômicos guardados nas bibliotecas sagradas dos templos.",
        "B",
        "Ptahhotep via a avareza como uma patologia moral contagiosa que corrompe governantes e dilacera as relações sociais."
    ))

    questoes_brutas.append((
        27, "EM13CHS105", "intermediario",
        "Ao analisar a passagem do legislador Sólon pela cidade egípcia de Saís narrada no diálogo Timeu de Platão, observa-se que os sacerdotes afirmavam:",
        "Que a Grécia possuía as memórias mais antigas de toda a humanidade sobre o dilúvio universal.",
        "Que os helenos eram jovens no saber e desconheciam as tradições antigas preservadas no Nilo.",
        "Que as ciências egípcias precisavam da aprovação de sábios atenienses para serem válidas.",
        "Que o alfabeto grego havia sido trazido diretamente do norte europeu por povos caçadores.",
        "Que os templos de Saís deviam seus projetos de arquitetura a artesãos de Esparta.",
        "B",
        "Os sacerdotes declaravam a Sólon que os gregos eram 'eternos jovens' perante a ancestralidade dos saberes de Kemet."
    ))

    questoes_brutas.append((
        28, "EM13CHS102", "intermediario",
        "A abordagem crítica desenvolvida por Cheikh Anta Diop em relação à egiptologia tradicional revelou que o eurocentrismo acadêmico agia para:",
        "Destacar a igualdade cultural de todos os povos da bacia do Mediterrâneo antigo.",
        "Desvincular o Egito de seu território continental africano, criando uma separação artificial.",
        "Valorizar a literatura oral dos povos do Nilo em comparação com tratados em grego.",
        "Promover o ensino obrigatório de hieróglifos nas escolas de ensino primário na Europa.",
        "Preservar os monumentos faraônicos sem intervenções de museus e colecionadores privados.",
        "B",
        "O colonialismo criou a ficção de um Egito 'desafricanizado' para justificar a dominação sobre o continente."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Nas 42 Declarações de Inocência presentes no Pert Em Hru, constata-se uma preocupação ética com o meio ambiente expressa em proibições como:",
        "Deixar de construir muros de pedra ao redor das propriedades rurais particulares.",
        "Não desviar as águas dos canais de irrigação nem contaminar as águas limpas do rio.",
        "Recusar o pagamento de tributos em grãos ao faraó em épocas de colheita farta.",
        "Caçar leões nas savanas distantes sem a bênção de autoridades religiosas da capital.",
        "Consumir peixes criados em tanques artificiais durante o período de cheia anual.",
        "B",
        "As declarações mostram respeito ecológico, como não poluir rios e não roubar a água que irriga lavouras vizinhas."
    ))

    questoes_brutas.append((
        30, "EM13CHS103", "intermediario",
        "Ao instruir o governante sobre o trato com debatedores, Ptahhotep estabelece uma diferença clara de atitude quando o adversário é arrogante e igual:",
        "Responder com insultos públicos imediatos para intimidar o debatedor perante os presentes.",
        "Empregar argumentos pausados e fundados na razão serena, demonstrando firmeza sem cair na fúria.",
        "Abandonar o tribunal às pressas para evitar o confronto de ideias com concidadãos.",
        "Mandar prender o oponente sob a alegação de traição aos preceitos sagrados do Estado.",
        "Concordar com tudo o que for dito pelo opositor apenas para encerrar a discussão.",
        "B",
        "Frente a um debatedor arrogante de igual condição, o sábio se sobressai pela serenidade do argumento comedido."
    ))

    questoes_brutas.append((
        31, "EM13CHS105", "intermediario",
        "A doutrina da transmigração da alma adotada por Pitágoras encontra antecedentes documentados em qual tradição do Mediterrâneo?",
        "Nos tratados de direito civil da Roma republicana.",
        "Nos mitos de caça dos povos nômades das estepes asiáticas.",
        "Nas crenças egípcias sobre o julgamento moral e a continuidade da essência humana.",
        "Nas fábulas de guerra dos guerreiros micênicos descritas na Ilíada.",
        "Nos preceitos práticos de navegação comercial elaborados pelos marinheiros cartagineses.",
        "C",
        "A metempsicose e a imortalidade da alma pitagórica derivam diretamente dos saberes sacerdotais de Kemet."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "A Psicostasia expressa uma concepção de salvação pós-morte que se diferencia de visões baseadas em privilégio social porque:",
        "Garante a eternidade apenas para quem possui riquezas suficientes para erguer pirâmides.",
        "Fundamenta o julgamento na integridade da vida moral vivida, pesando a justiça do coração.",
        "Concede perdão automático a qualquer cidadão que conheça senhas fúnebres secretas.",
        "Isenta os magistrados do julgamento divino, reservando a balança somente aos camponeses.",
        "Exige o sacrifício de bens materiais para anular faltas graves cometidas na comunidade.",
        "B",
        "No tribunal de Ma'at, a retidão das condutas cotidianas é o único critério que define o destino moral do falecido."
    ))

    questoes_brutas.append((
        33, "EM13CHS102", "intermediario",
        "Para a pensadora brasileira Sueli Carneiro, o resgate das tradições intelectuais africanas como a de Kemet atua como instrumento de:",
        "Criação de novos preconceitos que invertem as hierarquias acadêmicas tradicionais.",
        "Reparação histórica e combate ao epistemicídio que desumanizou a população negra.",
        "Substituição de todo o conhecimento científico moderno por práticas exclusivamente rituais.",
        "Isolamento dos estudantes negros em relação aos debates gerais de cidadania no país.",
        "Recusa do uso de métodos acadêmicos rigorosos em pesquisas universitárias contemporâneas.",
        "B",
        "Carneiro defende a valorização dos saberes africanos para restituir a dignidade intelectual negada pelo racismo."
    ))

    questoes_brutas.append((
        34, "EM13CHS103", "intermediario",
        "A literatura sapiencial kemética de Sebayt não deve ser reduzida a um manual de etiqueta superficial porque seus textos:",
        "Tratam da ordenação ética do sujeito, da responsabilidade pública e da justiça coletiva.",
        "Ensinavam técnicas mágicas para manipular os sentimentos de governantes estrangeiros.",
        "Tinham como finalidade preparar os soldados para saques territoriais em nações vizinhas.",
        "Concentravam-se apenas em prescrever fórmulas de higiene física para a nobreza palaciana.",
        "Destinavam-se unicamente a instruir escribas na contabilidade de sacas de cevada e trigo.",
        "A",
        "Os tratados de Sebayt articulam uma profunda pedagogia do dever cívico, da escuta atenta e da harmonia moral."
    ))

    questoes_brutas.append((
        35, "EM13CHS105", "intermediario",
        "Tales de Mileto, ao formular sua tese sobre a água como princípio de tudo, transformou a noção mítica kemética de Nun em uma explicação que:",
        "Preservava a necessidade de realizar danças rituais para fazer a chuva cair nas colheitas.",
        "Buscava um princípio natural e racional para explicar as transformações da matéria viva.",
        "Negava a existência de qualquer relação material entre os seres do mundo físico observável.",
        "Dependia do aval de sacerdotes do templo de Apolo para ser debatida em praça pública.",
        "Atribuía o movimento dos rios ao capricho individual de deuses com forma humana.",
        "B",
        "Tales retirou a roupagem teológica de Nun e formulou um princípio explicativo racional baseado na natureza da água."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Na dialética entre Ma'at e Isfet, a passividade de um governante diante da corrupção em sua cidade produz qual efeito cósmico e social?",
        "Fortalece a posição do reino frente a possíveis ameaças militares vindas do mar.",
        "Permite que as forças desordenadas de Isfet avancem, gerando sofrimento e crise coletiva.",
        "Eleva a arrecadação de tributos públicos pelo estímulo ao livre comércio de mercadorias.",
        "Garante a estabilidade climática permanente no vale fértil durante as cheias regulares.",
        "Transfere a responsabilidade dos julgamentos civis para cortes jurídicas internacionais.",
        "B",
        "A tolerância com a injustiça e a ganância abre espaço para a desordem moral e cósmica simbolizada por Isfet."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "Ao refutar o mito do 'Milagre Grego', historiadores contemporâneos não pretendem anular o valor da cultura helênica, mas sim:",
        "Provar que os filósofos gregos não produziram nenhum conceito original em suas obras.",
        "Inserir a Grécia em uma ampla rede de trocas e influências culturais com a África e o Oriente.",
        "Declarar a superioridade moral definitiva de civilizações do continente americano sobre a Europa.",
        "Impedir a leitura de autores clássicos como Platão e Aristóteles nos cursos escolares.",
        "Substituir o estudo de línguas antigas por técnicas aplicadas de engenharia comercial moderna.",
        "B",
        "A crítica histórica devolve à Grécia seu lugar real em uma rica dinâmica de trocas culturais mediterrânicas."
    ))

    questoes_brutas.append((
        38, "EM13CHS103", "intermediario",
        "O ensinamento de Ptahhotep referente à atitude para com o debatedor inferior em status social e descontrolado recomenda:",
        "Responder com zombarias impiedosas para divertir o público reunido na praça.",
        "Poupar o oponente e não humilhá-lo, pois o próprio despropósito de sua fala revelará seu erro.",
        "Exigir a expulsão imediata do cidadão para que ele nunca mais participe de reuniões públicas.",
        "Imitar seus gritos de desespero para provar que a assembleia não teme seus ataques.",
        "Recorrer à força física de guardas reais para silenciar o manifestante de forma rápida.",
        "B",
        "Ptahhotep mostra grandeza moral ao orientar a não humilhação do inferior, deixando que a insensatez caia por si só."
    ))

    questoes_brutas.append((
        39, "EM13CHS105", "intermediario",
        "Platão, em sua obra A República, propõe uma organização social baseada na justiça da cidade que dialoga estruturalmente com:",
        "A defesa do individualismo liberal moderno focado na posse de bens de consumo imediato.",
        "O ideal de harmonia cósmica e retidão de funções verificado no modelo kemético de Ma'at.",
        "A anarquia política total onde cada habitante decide suas próprias leis a cada dia.",
        "A supremacia dos guerreiros sobre os governantes como forma de garantir conquistas bélicas.",
        "A abolição de qualquer reflexão moral em nome da prosperidade financeira de navegadores.",
        "B",
        "A cidade justa platônica, governada por sábios em harmonia funcional, reflete o ideal egípcio de ordem equilibrada de Ma'at."
    ))

    questoes_brutas.append((
        40, "EM13CHS101", "intermediario",
        "A pena de avestruz que simboliza Ma'at funciona no ritual da pesagem da consciência como uma metáfora de:",
        "Leveza moral, retidão e ausência de culpas pesadas provocadas pela prática de crimes.",
        "Fragilidade biológica da espécie humana perante as tempestades do deserto oriental.",
        "Poderio militar dos arqueiros do faraó durante as campanhas de defesa das fronteiras.",
        "Riqueza material acumulada pelos comerciantes de tecidos finos nos portos do Nilo.",
        "Submissão cega do povo a mandamentos religiosos sem direito a questionamentos.",
        "A",
        "A pena representa a suavidade do coração desprovido de pesos morais como mentiras, cobiça e injustiças."
    ))

    # NÍVEL DIFÍCIL (Questões 41 a 60)
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Considere o texto: 'O Modelo Ariano, forjado no século XVIII, expurgou as origens egípcias da Grécia para coincidir com a expansão colonialista.' A partir dessa tese de Martin Bernal, infere-se que a historiografia eurocêntrica operou:",
        "Uma revalorização dos laços científicos compartilhados por povos do mar Mediterrâneo.",
        "Um apagamento deliberado das raízes africanas do saber ocidental para justificar o racismo.",
        "Uma crítica rigorosa às práticas coloniais inglesas e francesas no norte da África.",
        "Uma celebração das origens múltiplas do pensamento em universidades alemãs clássicas.",
        "Um incentivo direto à autonomia política dos povos colonizados no continente africano.",
        "B",
        "- **Etapa 1:** Interpretação da tese histórica. O texto destaca que o Modelo Ariano foi fabricado para legitimar o colonialismo por meio do apagamento deliberado da influência egípcia sobre a Grécia.\n- **Etapa 2:** Análise de causa e efeito. Ao retirar a África do papel de berço civilizatório e instituir a pureza ariana, a historiografia eurocêntrica justificou a dominação racial e colonial sobre os povos africanos."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a máxima: 'Não te envaideças com teu saber; aconselha-te com o ignorante e com o sábio, pois a arte não tem limites.' A relação estabelecida por Ptahhotep entre conhecimento e sociedade revela:",
        "O desprezo pelo estudo formal e a valorização exclusiva do trabalho braçal no campo.",
        "Uma concepção aberta e humilde do saber, que reconhece a inteligência em todos os estratos sociais.",
        "A defesa de que o conhecimento verdadeiro só pode ser alcançado por membros da corte real.",
        "A tentativa de criar ilusões retóricas para enfraquecer o rigor dos julgamentos no tribunal.",
        "A convicção de que a sabedoria é uma propriedade definitiva conquistada por poucos nobres.",
        "B",
        "- **Etapa 1:** Extração do núcleo argumentativo da máxima. Ptahhotep afirma que os limites da arte nunca são atingidos e que a fala sábia pode surgir até de quem moi grãos na pedra.\n- **Etapa 2:** Síntese conceitual. Essa perspectiva instaura a humildade intelectual e a escuta ativa como fundamentos da sabedoria, rompendo com o elitismo arrogante na produção do saber."
    ))

    questoes_brutas.append((
        43, "EM13CHS103", "dificil",
        "Diante de um escândalo contemporâneo de fraude em verbas da saúde, a reflexão ética de Ptahhotep sobre Un-Ma'at (a ganância) ofereceria qual diagnóstico central?",
        "A fraude é um comportamento normal de mercado que impulsiona o crescimento das cidades.",
        "A ganância individual é uma moléstia moral que corrompe governantes e degrada a vida coletiva.",
        "O problema decorre unicamente da ausência de computadores modernos para fiscalizar pagamentos.",
        "O desvio de recursos públicos é aceitável quando parte do valor é doado a templos sagrados.",
        "A administração deve tolerar pequenas falhas financeiras para garantir a rapidez das obras.",
        "B",
        "- **Etapa 1:** Identificação do conceito de Un-Ma'at. Nas Máximas de Ptahhotep, a avareza e a ganância desmedida são descritas como males que destroem a moral de quem governa e trazem ruína às famílias.\n- **Etapa 2:** Aplicação à situação contemporânea. A fraude e o desvio de recursos públicos representam a perda da integridade moral em prol do ganho privado, resultando na degradação dos serviços vitais da comunidade."
    ))

    questoes_brutas.append((
        44, "EM13CHS101", "dificil",
        "No ritual da Psicostasia, as 42 Confissões Negativas articulam deveres morais e ecológicos. Essa combinação atesta que, na tradição kemética, a justiça:",
        "Era restrita ao cumprimento de contratos comerciais firmados entre marinheiros estrangeiros.",
        "Integrava a conduta do cidadão, a paz entre semelhantes e o equilíbrio do ecossistema natural.",
        "Limitava-se ao pagamento regular de dízimos para manter o luxo dos sacerdotes em Mênfis.",
        "Tinha valor apenas se o falecido pertencesse à guarda de elite responsável pelas carruagens.",
        "Ignorava a preservação dos rios e das terras cultiváveis por considerá-los bens infinitos.",
        "B",
        "- **Etapa 1:** Análise dos elementos das Declarações de Inocência. Os aforismos rejeitam tanto o dano social ('não causei sofrimento', 'não roubei pão') quanto o desrespeito ambiental ('não poluí o rio', 'não desviei o canal').\n- **Etapa 2:** Julgamento da amplitude ética. Isso demonstra uma visão integrada em que a conduta ética do ser humano é inseparável do respeito às outras pessoas e da preservação dos recursos naturais que garantem a vida coletiva."
    ))

    questoes_brutas.append((
        45, "EM13CHS105", "dificil",
        "O Teorema de Tales e o Teorema de Pitágoras têm suas origens práticas vinculadas aos métodos de medição e aprumo de Kemet. Essa constatação histórica evidencia que:",
        "A matemática nasceu pronta e acabada na Grécia sem nenhum experimento prévio com a matéria.",
        "Os gregos sistematizaram e abstraíram conhecimentos técnicos e geométricos herdados do Egito.",
        "Os sacerdotes de Heliópolis copiaram as fórmulas criadas por geômetras da ilha de Creta.",
        "A agrimensura do Vale do Nilo era uma atividade mágica desprovida de rigor numérico real.",
        "A geometria clássica grega recusou qualquer aplicação prática na arquitetura de seus templos.",
        "B",
        "- **Etapa 1:** Contextualização histórica das viagens de Tales e Pitágoras ao Egito. Ambos aprenderam a agrimensura do Nilo e as proporções do triângulo sagrado 3-4-5 utilizado nas pirâmides.\n- **Etapa 2:** Dedução histórica. Os pensadores gregos não inventaram a geometria a partir do nada, mas reelaboraram teoricamente procedimentos práticos e saberes ancestrais cultivados no Vale do Nilo."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Em debates sobre justiça criminal, a Justiça Restaurativa propõe a reparação do dano e o diálogo em vez da mera punição vingativa. Esse modelo conecta-se à lógica de Ma'at porque:",
        "Procura restabelecer a harmonia comunitária e a consciência moral do autor do ato danoso.",
        "Aplica tortura física imediata para satisfazer o rancor da família prejudicada pelo crime.",
        "Isenta os infratores de qualquer responsabilidade social desde que façam oferendas públicas.",
        "Elimina a figura dos magistrados e transfere o poder decisório para gangues de rua.",
        "Restringe os julgamentos a acordos monetários sigilosos sem participação da comunidade.",
        "A",
        "- **Etapa 1:** Exame dos fundamentos da Justiça Restaurativa. Esse paradigma busca recompor laços comunitários dilacerados e promover a responsabilização autêntica de quem cometeu o delito.\n- **Etapa 2:** Conexão com o princípio de Ma'at. Assim como na pesagem do coração egípcia, o objetivo da justiça não é o sadismo da vingança estatal, mas a restauração da verdade, da retidão moral e do equilíbrio coletivo."
    ))

    questoes_brutas.append((
        47, "EM13CHS101", "dificil",
        "Considere a sentença: 'Quem é fiel a Ma'at caminha com passo firme; a herança pertence àquele de coração limpo.' Sob o prisma da filosofia política kemética, essa máxima ensina que:",
        "O poder político só se sustenta de forma legítima se for amparado na integridade e na virtude.",
        "A autoridade do magistrado depende exclusivamente de seu poder financeiro para pagar soldados.",
        "A astúcia militar justifica o uso contínuo da crueldade contra cidadãos descontentes.",
        "O destino dos povos é governado pelo acaso cego, sem relação com as ações dos governantes.",
        "A obediência aos deuses dispensa os administradores públicos de prestar contas de seus atos.",
        "A",
        "- **Etapa 1:** Compreensão da relação entre legitimidade e ética no pensamento de Ptahhotep. O texto associa a estabilidade da liderança à fidelidade a Ma'at.\n- **Etapa 2:** Conclusão teórica. A durabilidade do poder público e a memória honrada de um governante derivam de sua conduta justa perante a sociedade, e não do acúmulo egoísta de riquezas ou do medo imposto pela força."
    ))

    questoes_brutas.append((
        48, "EM13CHS105", "dificil",
        "Ao estudar o diálogo platônico Timeu, constata-se a menção à civilização de Saís e às narrativas de Sólon. Esse dado textual confirma qual aspecto da historiografia contemporânea?",
        "A inexistência de viagens marítimas de intelectuais helênicos no período clássico.",
        "O testemunho explícito deixado por Platão sobre a admiração grega pela sabedoria do Nilo.",
        "A condenação sumária que os filósofos de Atenas faziam da astronomia e da matemática egípcias.",
        "A comprovação de que Atenas foi fundada militarmente por navegadores vindos da Escandinávia.",
        "A recusa dos gregos em registrar informações sobre povos com línguas distintas da sua.",
        "B",
        "- **Etapa 1:** Análise dos diálogos platônicos (Timeu, Fedro). Platão não oculta o apreço grego pelas tradições egípcias, citando diálogos de Sólon com sacerdotes de Saís e a invenção das ciências por Thot.\n- **Etapa 2:** Confronto com as teses historiográficas. Essa documentação direta desmente a fábula do 'Milagre Grego' isolado e atesta que os próprios clássicos reverenciavam o legado cultural africano."
    ))

    questoes_brutas.append((
        49, "EM13CHS102", "dificil",
        "A implementação da Lei nº 10.639/2003 nas aulas de Filosofia exige a revisão de manuais escolares tradicionais. Essa medida pedagógica justifica-se pelo fato de que:",
        "As civilizações africanas não possuíam escrita e devem ser estudadas apenas pela dança.",
        "A formação cidadã crítica requer a superação de narrativas eurocêntricas e a valorização da pluralidade de saberes.",
        "O estudo de filósofos gregos deve ser completamente banido das salas de aula do Ensino Médio.",
        "As escolas devem priorizar exclusivamente os saberes de povos que viveram após a Idade Média.",
        "A filosofia precisa afastar-se das questões étnico-raciais para focar apenas em lógica abstrata.",
        "B",
        "- **Etapa 1:** Diagnóstico do problema educacional histórico. Os livros didáticos tradicionais silenciaram as matrizes africanas e indígenas, promovendo o epistemicídio curricular.\n- **Etapa 2:** Fundamentação da mudança pedagógica. Ao incluir o pensamento de Kemet e tradições afrodiaspóricas, a escola desfaz preconceitos históricos e assegura uma formação humanística plural e democrática."
    ))

    questoes_brutas.append((
        50, "EM13CHS103", "dificil",
        "Ptahhotep ensina: 'A fala virtuosa é mais rara que a esmeralda verde, e, no entanto, pode ser encontrada até entre as moedoras de grãos.' Essa afirmação formula qual princípio sobre o discernimento humano?",
        "A capacidade de reflexão e sabedoria não está subordinada à classe social ou à hierarquia de gênero.",
        "O saber verdadeiro pertence apenas aos donos de terras férteis e minas de pedras preciosas.",
        "O trabalho com grãos de cereais é a única atividade econômica digna de respeito comunitário.",
        "As mulheres devem abster-se do debate público para não comprometer o ritmo das tarefas agrícolas.",
        "A busca de esmeraldas nas montanhas deve ser financiada pelos sacerdotes de templos sagrados.",
        "A",
        "- **Etapa 1:** Interpretação da metáfora da esmeralda e das trabalhadoras do moinho. Ptahhotep confronta o elitismo ao afirmar que a sabedoria autêntica pode se manifestar em pessoas em situação de subordinação social.\n- **Etapa 2:** Formulação do princípio fundamental. Isso instaura um princípio democrático universalizante em que o valor da fala justa repousa na verdade de seu conteúdo, e não na posição de privilégio do falante."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Ao examinar a relação entre o faraó e o princípio de Ma'at, historiadores notam que o governante egípcio não era um tirano absoluto livre de regras, porque:",
        "Precisava dividir suas decisões diárias com parlamentos populares eleitos anualmente.",
        "Sua autoridade sagrada estava subordinada ao dever de manter a ordem justa e proteger os desvalidos.",
        "Devia prestar contas semanais a generais persas encarregados da segurança externa do reino.",
        "Não possuía nenhum poder para assinar decretos ou julgar conflitos entre nobres palacianos.",
        "Tinha sua permanência no trono decidida por sorteios públicos realizados na foz do rio.",
        "B",
        "- **Etapa 1:** Análise do estatuto político do faraó em Kemet. Embora visto como representante das forças divinas, o monarca tinha a missão obrigatória de encarnar Ma'at na Terra.\n- **Etapa 2:** Dedução sobre os limites do poder. Se o rei agisse com tirania, injustiça ou ganância (Isfet), ele violava a ordem cósmica, perdendo a legitimidade moral perante a tradição e o julgamento cósmico."
    ))

    questoes_brutas.append((
        52, "EM13CHS105", "dificil",
        "A passagem de Sócrates pelo julgamento em Atenas evoca o ideal de integridade perante a morte. Comparando sua conduta com os ensinamentos de Sebayt, nota-se como traço comum:",
        "A aceitação de suborno financeiro para evitar a condenação por tribunais da cidade.",
        "A recusa em trair os princípios morais e a convicção de que uma vida sem virtude não vale a pena.",
        "A tentativa de humilhar os juízes por meio de ofensas pessoais e acusações de traição à pátria.",
        "A fuga precipitada para terras estrangeiras como forma de escapar do cumprimento da sentença.",
        "O arrependimento público expresso em pedidos dramáticos de clemência perante a multidão.",
        "B",
        "- **Etapa 1:** Identificação da atitude de Sócrates perante a condenação. Sócrates recusa a fuga e a mentira, mantendo-se fiel à vida filosófica e à justiça das leis da cidade.\n- **Etapa 2:** Confronto com a sabedoria de Kemet (Ptahhotep, Meri-Ka-Ré). Ambas as tradições colocam a integridade moral da consciência acima da preservação covarde da vida biológica sem honra."
    ))

    questoes_brutas.append((
        53, "EM13CHS102", "dificil",
        "Em seu livro Civilização ou Barbárie, Cheikh Anta Diop utiliza testes com dosagem de melanina em múmias para fundamentar suas conclusões. Esse método comprova:",
        "O uso de técnicas modernas das ciências da natureza para fundamentar teses históricas e antropológicas.",
        "A dependência que a história da África teria de narrativas míticas transmitidas sem comprovação física.",
        "A impossibilidade de realizar pesquisas científicas seguras sobre o período faraônico da humanidade.",
        "A superioridade racial de povos da antiguidade oriental em relação às sociedades do presente.",
        "O fracasso dos exames laboratoriais diante de materiais orgânicos submetidos ao embalsamamento.",
        "A",
        "- **Etapa 1:** Exame dos procedimentos metodológicos adotados por Diop. Físico nuclear e egiptólogo, Diop coletou amostras de pele de múmias egípcias e aplicou ensaios fotoquímicos para medir os níveis de melanina.\n- **Etapa 2:** Avaliação do impacto científico. Ao integrar física, biologia e arqueologia, Diop desconstruiu com dados empíricos irrefutáveis as ideologias racistas que tentavam branquear o Antigo Egito."
    ))

    questoes_brutas.append((
        54, "EM13CHS101", "dificil",
        "Considere o aforismo de Amenemope: 'Não mudes o marco das fronteiras do campo nem invadas a terra da viúva.' Esse mandamento ilustra a preocupação da sabedoria de Kemet com:",
        "O incentivo à disputa violenta pela posse de terras desocupadas nas margens de lagos.",
        "A proteção aos cidadãos vulneráveis e a condenação formal da usurpação fraudulenta da propriedade alheia.",
        "A cobrança de juros exorbitantes sobre sementes emprestadas a famílias camponesas.",
        "A destruição de pequenas lavouras para criar áreas de caça reservadas a generais de infantaria.",
        "A transferência compulsória de famílias pobres para regiões áridas afastadas dos canais do Nilo.",
        "B",
        "- **Etapa 1:** Interpretação da máxima ética de Amenemope. O texto veda a alteração de marcos territoriais e a tomada das terras de pessoas desamparadas, como as viúvas.\n- **Etapa 2:** Síntese conceitual. Isso evidencia que a sabedoria kemética fundamentava-se na solidariedade ativa e na defesa do vulnerável contra o arbítrio e a ganância dos poderosos."
    ))

    questoes_brutas.append((
        55, "EM13CHS103", "dificil",
        "A teoria de Ma'at influenciou a visão de ordem pública nas cidades do Nilo ao instituir que o administrador justo deve:",
        "Julgar com rigor imparcial, sem favorecer parentes ricos nem perseguir cidadãos humildes.",
        "Priorizar as demandas da nobreza militar para assegurar o apoio das armas ao governo central.",
        "Determinar a sentença judicial de acordo com o valor das propinas entregues em seu gabinete.",
        "Ignorar as queixas dos artesãos para manter a harmonia superficial com os chefes de oficinas.",
        "Aplicar punições baseadas unicamente em boatos ouvidos nas praças e tavernas das redondezas.",
        "A",
        "- **Etapa 1:** Análise dos deveres do juiz e do vizir segundo Ma'at. Ptahhotep e outros autores de Sebayt exigem do magistrado a impessoalidade e a busca rigorosa da verdade nos litígios.\n- **Etapa 2:** Conclusão sobre a conduta judicial. A justiça autêntica exige neutralidade e respeito à dignidade humana, vedando o nepotismo, a venalidade e o abuso contra quem não possui recursos para se defender."
    ))

    questoes_brutas.append((
        56, "EM13CHS102", "dificil",
        "Ao desconstruir o mito do 'Milagre Grego', teóricos contemporâneos apontam que a filosofia não nasceu de uma ruptura mágica, mas de um processo histórico que envolveu:",
        "O isolamento deliberado de Atenas em relação a todas as cidades vizinhas da Península Balcânica.",
        "Trocas mercantis contínuas, circulação de viajantes e apropriação criativa de saberes ancestrais africanos e asiáticos.",
        "A imposição armada do modelo monárquico absolutista sobre as comunidades rurais periféricas.",
        "A renúncia coletiva ao uso da razão demonstrativa em favor de rituais de sacrifício coletivo.",
        "A queima de bibliotecas do Oriente Próximo por legiões de soldados vindos da Macedônia.",
        "B",
        "- **Etapa 1:** Exame dos fatores materiais e culturais que propiciaram o florescimento do pensamento grego. O comércio marítimo mediterrânico facilitou o trânsito contínuo de pessoas, técnicas e ideias.\n- **Etapa 2:** Articulação histórica. A razão filosófica grega floresceu como síntese e reelaboração crítica de contribuições milenares desenvolvidas no Egito (Kemet), na Fenícia e na Mesopotâmia."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "A leitura das 42 Confissões Negativas revela que a concepção kemética de dignidade humana não admitia a justificativa do 'cumprimento cego de ordens injustas', porque:",
        "O tribunal de Osíris julgava a responsabilidade ética pessoal de cada indivíduo por seus atos conscientes.",
        "Os subordinados eram isentos de qualquer julgamento fúnebre caso provassem sua condição servil.",
        "As leis da cidade previam anistia total a crimes cometidos a mando de superiores hierárquicos.",
        "O coração humano (Ib) era incapaz de registrar sentimentos de culpa ou remorso pelas faltas vividas.",
        "A balança divina aceitava que nobres indicassem servos substitutos para a pesagem da consciência.",
        "A",
        "- **Etapa 1:** Análise da natureza do julgamento no Salão das Duas Verdades. O falecido fala em primeira pessoa ('Eu não fiz sofrer', 'Eu não roubei'), respondendo perante os 42 juízes divinos.\n- **Etapa 2:** Julgamento sobre a responsabilidade moral. Isso consagra o princípio da autodeterminação e da responsabilidade ética intransferível, em que nenhum agente pode transferir para outrem a culpa por seus atos."
    ))

    questoes_brutas.append((
        58, "EM13CHS105", "dificil",
        "No Fedro de Platão, o rei egípcio Thamus critica a escrita oferecida por Thot, argumentando que ela geraria esquecimento na mente dos homens. Essa passagem dialoga com:",
        "A certeza de que a escrita mecânica não substitui a reflexão dialógica e a memória interior viva do sujeito.",
        "A recusa dos egípcios em utilizar hieróglifos para registrar leis civis e tratados de comércio.",
        "A proibição religiosa do uso de tintas vegetais em folhas de papiro durante o Império Novo.",
        "A convicção de que os gregos eram os únicos capazes de compreender a função da escrita alfabética.",
        "A tentativa de Thot de destruir as bibliotecas sagradas mantidas nos templos de Tebas.",
        "A",
        "- **Etapa 1:** Interpretação da crítica do rei Thamus no diálogo platônico. Thamus alerta que a dependência externa de sinais gráficos pode atrofiar o cultivo ativo da memória e da compreensão viva.\n- **Etapa 2:** Vinculação filosófica. Essa crítica platônica reflete a pedagogia socrática e a tradição kemética de Sebayt, nas quais o saber deve ser incorporado na consciência e na ação, e não apenas estocado passivamente."
    ))

    questoes_brutas.append((
        59, "EM13CHS103", "dificil",
        "Um gestor público que utiliza artimanhas jurídicas para burlar licitações e beneficiar seus próprios negócios estaria, sob a ótica de Ptahhotep, praticando:",
        "Uma virtude administrativa necessária para contornar atrasos burocráticos do Estado.",
        "Uma forma danosa de avareza (Un-Ma'at) que destrói a confiança social e fere a justiça de Ma'at.",
        "Um ato de humildade que permite aos subordinados aprenderem a negociar contratos livres.",
        "Um procedimento normal que engrandece a honra de sua família perante a comunidade cívica.",
        "Uma manobra aconselhável para garantir que as verbas públicas permaneçam na cidade.",
        "B",
        "- **Etapa 1:** Caracterização da conduta do agente no estudo de caso. O administrador usa pretextos legais para obter ganho pessoal ilícito às custas do erário.\n- **Etapa 2:** Aplicação das categorias de Ptahhotep. Tal conduta encarna Un-Ma'at (ganância desmedida), que violenta Ma'at (justiça e probidade) e corrompe a legitimidade moral indispensável a qualquer governança."
    ))

    questoes_brutas.append((
        60, "EM13CHS102", "dificil",
        "A descolonização do currículo escolar promovida por leis de ações afirmativas visa combater o racismo institucional. Filosoficamente, essa medida assegura:",
        "A substituição do rigor argumentativo pelo elogio superficial a lendas folclóricas descontextualizadas.",
        "A justiça cognitiva global, reconhecendo que múltiplos povos formularam modos legítimos de saber e de viver.",
        "A exclusão de dados científicos contemporâneos em favor de práticas arcaicas de mumificação.",
        "A imposição de uma única visão de mundo que anula o diálogo crítico entre culturas distintas.",
        "O encerramento de pesquisas sobre a história da filosofia europeia nas universidades públicas.",
        "B",
        "- **Etapa 1:** Compreensão do conceito de justiça cognitiva formulado por Boaventura de Sousa Santos e Sueli Carneiro. Trata-se da garantia de que todos os saberes ancestrais tenham sua dignidade respeitada.\n- **Etapa 2:** Conclusão crítica. A superação do epistemicídio curricular não fecha o diálogo, mas o amplia verdadeiramente, permitindo que a juventude compreenda a humanidade em sua rica pluralidade."
    ))

    # Aplica o balanceamento perfeito
    questoes = balancear_questoes(questoes_brutas)

    # Montar markdown
    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('objeto_de_conhecimento: "A Desconstrução do Mito Eurocêntrico do \'Milagre Grego\' como Berço Exclusivo da Razão Humana (Cheikh Anta Diop, Théophile Obenga e Martin Bernal); As Tradições Filosóficas do Antigo Kemet (Egito Antigo) Anteriores aos Pré-Socráticos: Os Ensinamentos de Ptahhotep (O Primeiro Filósofo Moral da História, c. 2400 a.C.), Amenemope e Meri-Ka-Ré; O Conceito Cósmico e Ontológico de Ma\'at: O Princípio Supremo da Verdade, Justiça, Ordem Universal, Equilíbrio e Harmonia; A Influência Africana sobre os Primeiros Pensadores Gregos (Tales, Pitágoras e Platão que Estudaram nos Templos do Vale do Nilo)."')
    md.append('ebook_fonte: "em-fil-c01-filosofia-kemetica-egito-pre-grega.md"')
    md.append('habilidades: "EM13CHS101, EM13CHS102, EM13CHS103, EM13CHS105, H1, H2, H11"')
    md.append("total_exercicios: 60")
    md.append("distribuicao:")
    md.append("  basico: 20")
    md.append("  intermediario: 20")
    md.append("  dificil: 20")
    md.append("---")
    md.append("")
    md.append("# Exercícios — O Pensamento Filosófico no Antigo Kemet (Egito) e a Crítica ao 'Milagre Grego'")
    md.append("")
    md.append("## Nível Básico (Questões 1 a 20)")
    md.append("")

    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: filosofia-kemetica-egito-pre-grega -->")
        md.append(f"### Questão {num}")
        md.append("")
        md.append(enunc)
        md.append("")
        md.append(f"a) {a}")
        md.append(f"b) {b}")
        md.append(f"c) {c}")
        md.append(f"d) {d}")
        md.append(f"e) {e}")
        md.append("")
        md.append(f"**Gabarito:** {gab}")
        md.append(f"**Resolução:** {res}")
        md.append("")

    md.append("## Nível Intermediário (Questões 21 a 40)")
    md.append("")

    for q in questoes[20:40]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: filosofia-kemetica-egito-pre-grega -->")
        md.append(f"### Questão {num}")
        md.append("")
        md.append(enunc)
        md.append("")
        md.append(f"a) {a}")
        md.append(f"b) {b}")
        md.append(f"c) {c}")
        md.append(f"d) {d}")
        md.append(f"e) {e}")
        md.append("")
        md.append(f"**Gabarito:** {gab}")
        md.append(f"**Resolução:** {res}")
        md.append("")

    md.append("## Nível Difícil (Questões 41 a 60)")
    md.append("")

    for q in questoes[40:]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: filosofia-kemetica-egito-pre-grega -->")
        md.append(f"### Questão {num}")
        md.append("")
        md.append(enunc)
        md.append("")
        md.append(f"a) {a}")
        md.append(f"b) {b}")
        md.append(f"c) {c}")
        md.append(f"d) {d}")
        md.append(f"e) {e}")
        md.append("")
        md.append(f"**Gabarito:** {gab}")
        md.append("**Resolução Detalhada:**")
        md.append(res)
        md.append("")

    md.append("## Referências")
    md.append("")
    md.append("- BERNAL, Martin. *Black Athena: The Afroasiatic Roots of Classical Civilization*. New Brunswick: Rutgers University Press, 1987. v. 1: The Fabrication of Ancient Greece 1785-1985.")
    md.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.")
    md.append("- BURNET, John. *Early Greek Philosophy*. 3. ed. Londres: A. & C. Black, 1920.")
    md.append("- CARNEIRO, Sueli. *A Construção do Outro como Não-Ser como Fundamento do Ser*. Tese (Doutorado em Educação) — Faculdade de Educação, Universidade de São Paulo, São Paulo, 2005.")
    md.append("- DIOP, Cheikh Anta. *Civilização ou Barbárie: Uma Antropologia Autêntica*. Tradução de Martha Rosa Amoroso. Paris: Présence Africaine, 1981.")
    md.append("- KARENGA, Maulana. *Maat, The Moral Ideal in Ancient Egypt: A Study in Classical African Ethics*. Los Angeles: University of Sankore Press, 2004.")
    md.append("- NOGUERA, Renato. *O Ensino de Filosofia e a Lei 10.639*: Diálogos entre Epistemologias Africanas e a Educação Básica. Rio de Janeiro: Pallas, 2014.")
    md.append("- OBENGA, Théophile. *La philosophie africaine de la période pharaonique: 2780-330 avant notre ère*. Paris: L'Harmattan, 1990.")
    md.append("- RENAN, Ernest. *Prière sur l'Acropole*. Paris: Calmann-Lévy, 1883.")
    md.append("- RIBEIRO, Katiúscia. *Filosofia Africana: Raízes Keméticas e Perspectivas Contemporâneas*. Rio de Janeiro: Ananse, 2021.")
    md.append("- SANTOS, Boaventura de Sousa. *Para uma sociologia das ausências e uma sociologia das emergências*. Revista Crítica de Ciências Sociais, Coimbra, n. 63, p. 237-280, 2002.")
    md.append("- UNESCO. *História Geral da África*. Coordenação de Joseph Ki-Zerbo. Paris: UNESCO, 1982. v. 2: Antigas Civilizações da África.")
    md.append("")

    conteudo = "\n".join(md)

    # 1. Auditoria Preventiva de Gabaritos
    gabs = re.findall(r'\*\*Gabarito:\*\*\s*([A-E])', conteudo)
    print(f"Total de Gabaritos detectados: {len(gabs)}")
    counts = Counter(gabs)
    print(f"Contagem por letra: {counts}")
    if len(gabs) != 60:
        print(f"[ERRO CRÍTICO] Total de questões diferente de 60: {len(gabs)}")
        sys.exit(1)
    for letra in ['A', 'B', 'C', 'D', 'E']:
        qtd = counts.get(letra, 0)
        if qtd != 12:
            print(f"[ERRO CRÍTICO] Letra {letra} com {qtd} ocorrências (esperado 12)!")
            sys.exit(1)

    # 2. Auditoria Preventiva de R$
    if "R$" in conteudo:
        print("[ERRO CRÍTICO] Símbolo 'R$' detectado no conteúdo gerado!")
        sys.exit(1)

    # 3. Auditoria Preventiva de Termos Pedantes / Proibidos
    texto_sem_yaml = re.sub(r'^---.*?---\n', '', conteudo, flags=re.DOTALL) if conteudo.startswith('---') else conteudo
    corpo_questoes = texto_sem_yaml.split("## Referências")[0]
    padroes_pedantes = [
        r"\bsupracitad[oa]s?\b", r"\boutrossim\b", r"\bdestarte\b", r"\bprecípu[oa]s?\b",
        r"\bconsubstancia\w*\b", r"\bdepreende-se\b", r"\bassertiva\b", r"\bmormente\b",
        r"\bno\s+tocante\s+a\b", r"\batinente\w*\b", r"\bconcernente\w*\b", r"\bdirimir\b",
        r"\benseja\w*\b", r"\bauferir\b", r"\bprescind\w*\b", r"\bimprescind\w*\b",
        r"\binexor\w*\b", r"\bidiossincra\w*\b", r"\banátema\b", r"\bprerrogativa\w*\b",
        r"\bcorrobor\w*\b", r"\bintrínsec[oa]s?\b", r"\bextrínsec[oa]s?\b", r"\bdicotomi\w*\b",
        r"\bsubjacente\w*\b", r"\befêmer[oa]s?\b", r"\bmitigar\b", r"\bfomentar\b",
        r"\bhegemônic\w*\b", r"\bepistemológic\w*\b", r"\bontológic\w*\b", r"\baxiológic\w*\b",
        r"\bteleológic\w*\b", r"\bhermenêutic\w*\b", r"\bpropedêutic\w*\b", r"\bvernáculo\b"
    ]
    for pat in padroes_pedantes:
        m = re.search(pat, corpo_questoes, re.IGNORECASE)
        if m:
            print(f"[ERRO CRÍTICO] Termo proibido detectado: '{m.group(0)}'!")
            sys.exit(1)

    print("[AUDITORIA INTERNA APROVADA] Todas as 60 questões atendem rigorosamente às travas pedagógicas!")

    # Escrever no rascunho temporário
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"Rascunho temporário salvo com sucesso ({len(conteudo)} bytes).")

    # Invocar o validador educamob
    cmd = [sys.executable, "validador_educamob.py", temp_draft, dest_path]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 01 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    gerar_cap01()
