# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 25 de Filosofia EM:
Mímesis e Catarse: A Filosofia da Arte na Grécia Antiga
Objeto: cap-25-estetica-antiga-mimesis-catarse
Total: 60 questões atômicas (20 básicas, 20 intermediárias, 20 difíceis)
Gabarito balanceado: 12 A, 12 B, 12 C, 12 D, 12 E
"""

import re
import sys
import subprocess
from collections import Counter

def build_exercicios():
    questoes_brutas = []

    # ==========================================
    # 20 QUESTÕES BÁSICAS (1 a 20)
    # ==========================================

    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "O que significava o conceito de 'Tekhne' (Técnica / Arte) para o pensamento da Grécia clássica?",
        "Uma inspiração caótica irracional associada à loucura sem método.",
        "Todo saber prático e racional orientado à fabricação consciente de um objeto ou à produção metódica de um efeito útil no mundo.",
        "A habilidade militar exclusiva de generais de cavalaria em campanhas territoriais.",
        "O comércio de mercadorias agrícolas em portos mercantes do mar Egeu.",
        "A recitação de preces religiosas em templos dedicados exclusivamente a Apolo.",
        "B",
        "Na Grécia, tekhne abrangia tanto o trabalho do marceneiro e do médico quanto o do escultor e do arquiteto: um ofício prático guiado por regras racionais e transmissíveis."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Qual é o significado original do vocábulo grego 'Aisthesis', matriz etimológica da disciplina da Estética?",
        "O cálculo matemático utilizado na demarcação de propriedades rurais.",
        "A percepção sensorial e a sensibilidade do corpo diante das impressões do mundo exterior.",
        "A ordem cósmica imutável que rege o movimento perpétuo das constelações.",
        "A virtude cívica guerreira cultivada por soldados nas assembleias da pólis.",
        "A escrita alfabética utilizada em tratados de navegação e comércio marítimo.",
        "B",
        "Aisthesis refere-se à percepção pelos sentidos (visão, audição, tato); no século XVIII, Alexander Baumgarten utilizou o termo para fundar a Estética como ciência da sensibilidade."
    ))

    questoes_brutas.append((
        3, "EM13CHS301", "basico",
        "Por que, no Livro X de A República, Platão determina a expulsão dos poetas e dos artistas miméticos de Kallipolis (a Cidade Justa)?",
        "Porque os poetas cobravam ingressos excessivamente caros para suas récitas teatrais.",
        "Porque a arte imitativa produz uma cópia da cópia afastada da verdade inteligível e corrompe a alma cívica dos cidadãos ao alimentar paixões desmedidas.",
        "Porque os pintores utilizavam pigmentos químicos tóxicos na preparação de tintas em praças públicas.",
        "Porque as tragédias teatrais duravam muitas horas e prejudicavam as colheitas de trigo no campo.",
        "Porque os poetas dramáticos recusavam prestar serviços militares obrigatórios na defesa das fronteiras.",
        "B",
        "Platão expulsa os poetas por dois motivos centrais: a arte mimética é uma ilusão de terceiro grau distante da verdade das Ideias e sua carga emocional enfraquece a razão cívica dos cidadãos."
    ))

    questoes_brutas.append((
        4, "EM13CHS302", "basico",
        "No famoso exemplo platônico dos Três Leitos (camas), qual é o estatuto da realidade e do ser do leito pintado pelo artista?",
        "É o modelo perfeito e eterno gerado no mundo das Ideias inteligíveis.",
        "É uma imitação da imitação, uma cópia de aparência enganosa que se encontra a três graus de distância da Verdade essencial.",
        "É a peça de madeira física fabricada pelo marceneiro a partir de cálculos geométricos.",
        "É uma ferramenta sagrada utilizada exclusivamente em cerimônias de coroação imperial.",
        "É um objeto utilitário desenhado por arquitetos para o repouso de soldados em casernas.",
        "B",
        "Platão detalha: primeiro vem a Ideia de cama (criada por Deus); depois a cama de madeira feita pelo carpinteiro; por fim a cama pintada na tela, que é mera sombra da cópia, a três passos da verdade."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Como a poesia trágica afeta a harmonia da alma humana segundo a crítica moral desenvolvida por Platão?",
        "Fortalece o domínio austero da Alma Racional sobre as fraquezas do corpo.",
        "Alimenta e rega a parte inferior e irracional da alma, estimulando o descontrole emocional, a covardia e o pranto desmedido nos cidadãos.",
        "Desenvolve o raciocínio dedutivo exigido para a resolução de teoremas geométricos.",
        "Ensina a obediência incondicional às leis civis aprovadas pelos magistrados da cidade.",
        "Incentiva o cultivo da serenidade contemplativa em retiros rurais silenciosos.",
        "B",
        "Para Platão, ver heróis e deuses chorando e blasfemando no palco faz o cidadão perder o autocontrole da razão; acostumado a choramingar no teatro, o indivíduo vacilará na hora de lutar na guerra."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Qual tratado filosófico fundamental de Aristóteles é considerado a primeira investigação sistemática positiva sobre a arte no Ocidente?",
        "A Política, que discute a tripartição de cargos na administração de cidades portuárias.",
        "A Poética (*Peri Poietikes*), dedicada ao estudo da criação poética, da tragédia e da epopeia.",
        "A Metafísica, que investiga o motor imóvel e as causas primeiras de substâncias celestes.",
        "A Ética a Nicômaco, que define a virtude como o justo meio entre os vícios dos extremos.",
        "A Física, que analisa os movimentos naturais de corpos materiais no cosmos sublunar.",
        "B",
        "Na Poética, Aristóteles reabilita a arte contra a condenação de Platão, analisando a mímesis como faculdade natural de aprendizado e definindo as regras estruturais da grande tragédia."
    ))

    questoes_brutas.append((
        7, "EM13CHS301", "basico",
        "Como Aristóteles fundamenta o caráter natural e positivo da 'Mímesis' (imitação) na natureza humana?",
        "Sustentando que a imitação é um vício moral herdado de tradições bárbaras estrangeiras.",
        "Demonstrando que a imitação é inata no ser humano desde a infância, sendo a via fundamental de aprendizagem e fonte de genuíno prazer intelectual.",
        "Afirmando que o hábito de imitar prejudica a memorização de versos poéticos clássicos.",
        "Defendendo que a representação visual deve ser proibida para evitar confusões de visão em crianças.",
        "Provando que a imitação decorre da carência de materiais metálicos na fabricação de estátuas.",
        "B",
        "Aristóteles observa que a criança aprende a falar e a viver imitando; além disso, a mente sente alegria ao contemplar a imitação bem-feita porque reconhece a forma do mundo e aprende com ela."
    ))

    questoes_brutas.append((
        8, "EM13CHS302", "basico",
        "Por que, para Aristóteles, coisas repulsivas na vida real (como cadáveres ou feras) produzem deleite estético quando representadas na arte?",
        "Porque as telas de pintura recebiam banhos químicos de essências aromáticas exóticas.",
        "Porque o intelecto humano experimenta o prazer cognitivo de contemplar a maestria da técnica e decifrar a forma: 'Ah, então aquilo é assim!'.",
        "Porque os cidadãos gregos eram educados para apreciar o sofrimento de animais domésticos.",
        "Porque os pintores recebiam recompensas em lingotes de prata pela representação de monstros.",
        "Porque as imagens de cadáveres eram utilizadas exclusivamente como avisos em postos alfandegários.",
        "B",
        "O prazer estético é intelectual: mesmo diante de um monstro ou cadáver pintado, não sentimos nojo real, mas admiração pela perfeição da técnica que captou com fidelidade a forma daquele ser."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "No capítulo IX de A Poética, qual é a distinção crucial estabelecida por Aristóteles entre a 'Poesia' e a 'História'?",
        "A História é redigida em versos rimados e a Poesia utiliza exclusivamente a prosa comercial.",
        "A História relata o que de fato aconteceu no particular factual; a Poesia trata do que poderia acontecer segundo a verossimilhança, sendo mais filosófica e universal.",
        "A História é superior por descrever as árvores genealógicas exatas das dinastias imperiais.",
        "A Poesia limita-se a narrar lendas mitológicas infantis sem qualquer utilidade moral na pólis.",
        "A História e a Poesia possuem o mesmo método empírico de catalogação documental em arquivos.",
        "B",
        "Tese clássica de Aristóteles: a poesia é mais filosófica que a história; o historiador fica preso ao fato factual particular que ocorreu, enquanto o poeta cria o universal verossímil da condição humana."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "O que estabelece o conceito aristotélico de 'Catarse' (*Katharsis*) na experiência da tragédia grega?",
        "A obrigação legal de os espectadores realizarem doações financeiras ao final de récitas cívicas.",
        "A purgação, clarificação e pacificação dos afetos de terror (*phobos*) e piedade (*eleos*), restituindo o equilíbrio moral e emocional do cidadão.",
        "A execução de danças acrobáticas nos intervalos de peças teatrais para entreter as autoridades.",
        "A distribuição de alimentos e vinhos aos cidadãos mais pobres sentados nas arquibancadas.",
        "O banimento de dramaturgos que utilizavam cenários de madeira pintados com cores escuras.",
        "B",
        "Catarse é a purificação dos sentimentos: ao vivenciar o terror e a compaixão no teatro, as emoções represadas na mente são purgadas em ambiente seguro, pacificando o espírito do cidadão."
    ))

    questoes_brutas.append((
        11, "EM13CHS301", "basico",
        "Quais são as duas emoções fundamentais mobilizadas pela tragédia clássica que operam o mecanismo da catarse em Aristóteles?",
        "A inveja de rivais esportivos e o orgulho de títulos nobiliárquicos hereditários.",
        "O terror (*phobos*) diante da vulnerabilidade humana e a piedade (*eleos*) perante a dor do herói.",
        "A avareza no acúmulo de moedas de prata e o ciúme em disputas comerciais municipais.",
        "A raiva cega em confrontos de rua e o riso zombeteiro em festivais carnavalescos.",
        "A esperança de riquezas materiais em navegações e a indiferença perante leis da pólis.",
        "B",
        "A tragédia mexe com dois afetos primordiais: sentimos piedade ao ver o infortúnio desmedido do herói e sentimos terror ao reconhecer que, sendo humanos frágeis, o mesmo destino poderia nos abater."
    ))

    questoes_brutas.append((
        12, "EM13CHS302", "basico",
        "Na estrutura dramática da tragédia analisada por Aristóteles, o que define o conceito de 'Peripécia' (*Peripeteia*)?",
        "O pagamento pontual de diárias de trabalho aos atores e músicos de corais teatrais.",
        "A virada dramática súbita da sorte do protagonista, passando da prosperidade e glória para a mais profunda ruína.",
        "A recitação monótona de genealogias lendárias antes da abertura de cortinas cênicas.",
        "O encerramento formal do espetáculo através de discursos proferidos por magistrados locais.",
        "A troca de máscaras de linho pelos figurantes nos bastidores de madeira de anfiteatros.",
        "B",
        "Peripécia é a guinada do destino: o herói está no ápice do poder e da felicidade e, num golpe súbito de acontecimentos, cai no abismo da desgraça e do desespero absoluto."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "O que representa o momento do 'Reconhecimento' (*Anagnorisis*) na tragédia grega, como na célebre peça Édipo Rei de Sófocles?",
        "A entrega de medalhas cívicas aos generais que venceram batalhas em províncias marítimas.",
        "A passagem estarrecedora da ignorância para o conhecimento amargo da verdade trágica oculta.",
        "A assinatura de tratados comerciais entre comandantes de esquadras navais rivais.",
        "O sorteio público de assentos prioritários nas primeiras fileiras de teatros de pedra.",
        "A leitura de sentenças fiscais em audiências públicas presididas por arcontes municipais.",
        "B",
        "Reconhecimento é o instante em que a verdade nua e dolorosa é desvelada: quando Édipo descobre em pânico que o estranho que matou na estrada era seu pai e sua esposa rainha era sua própria mãe."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Como Aristóteles caracteriza a 'Hamartia' (falha trágica ou erro de julgamento) cometida pelo protagonista da tragédia?",
        "Um crime perverso planejado com crueldade deliberada contra cidadãos inocentes.",
        "Um erro de conduta ou falha de discernimento cometido por um homem nobre e ilustre, desencadeado frequentemente pela arrogância (*hybris*) diante dos deuses.",
        "A perda involuntária de moedas metálicas durante viagens fluviais em embarcações mercantes.",
        "A incapacidade de memorizar parlamentos teatrais em ensaios preparatórios de corais.",
        "A recusa injustificada de comparecer às assembleias cívicas de votação de impostos na ágora.",
        "B",
        "O herói trágico não é um bandido sádico nem um anjo puro: é um homem virtuoso que comete um erro fatal de julgamento (hamartia), muitas vezes por presunção excessiva (hybris) perante o destino."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "Por que o protagonista da tragédia clássica não deve ser um monstro perverso completo nem um ser de virtude perfeita e imaculada?",
        "Porque os atores tinham dificuldades físicas para interpretar personagens de estaturas distintas.",
        "Porque a queda de um monstro geraria satisfação vingativa (sem compaixão) e a desgraça de um homem impecável causaria repulsa e revolta moral contra a ordem do mundo.",
        "Porque os regulamentos dos festivais proibiam a presença de vilões em palcos cobertos.",
        "Porque os figurinos cênicos eram padronizados com as mesmas cores para todos os elencos.",
        "Porque as assembleias populares exigiam que os enredos teatrais fossem cômicos e alegres.",
        "B",
        "A empatia trágica exige equilíbrio: se o vilão cruel cai, achamos bom; se um santo perfeito é destruído, ficamos revoltados; sofremos e tememos quando um homem nobre e falível cai por seu próprio erro."
    ))

    questoes_brutas.append((
        16, "EM13CHS302", "basico",
        "Como a experiência catártica aristotélica se manifesta quando assistimos a um filme dramático contemporâneo de guerra em uma sala de cinema?",
        "Fazendo com que os espectadores abandonem a sessão com depressão clínica irreversível.",
        "Provocando angústia e lágrimas diante da dor ficcional na tela, mas deixando os espectadores aliviados, com a lucidez ética ampliada e com apego renovado à paz ao término da projeção.",
        "Despertando impulsos imediatos de vandalismo contra equipamentos de projeção da sala.",
        "Obrigando o público a redigir manifestos militares nas bilheterias antes da saída.",
        "Eliminando a capacidade intelectual dos espectadores de distinguirem a ficção da realidade cotidiana.",
        "B",
        "No cinema contemporâneo, a catarse é viva: choramos durante o filme de guerra e sentimos o terror da morte; mas ao acenderem as luzes, sentimos um profundo alívio moral e um amor renovado pela vida e pela paz."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "De que modo episódios contemporâneos de censura moralista a exposições artísticas reativam as teses formuladas por Platão em A República?",
        "Defendendo que as obras de arte devem ser comercializadas exclusivamente em praças financeiras.",
        "Alegando que certas imagens e expressões plásticas atentam contra os bons costumes e corrompem a juventude, exigindo a intervenção do Estado para banir as obras dos museus.",
        "Exigindo que os artistas visuais devam possuir diplomas acadêmicos em arquitetura militar naval.",
        "Comprovando que as galerias contemporâneas utilizam sistemas elétricos com risco de curto-circuito.",
        "Sustentando que as exposições de pintura devem ocorrer unicamente em áreas rurais abertas.",
        "B",
        "Quem pede censura hoje usa o argumento de Platão: 'essa arte corrompe os jovens e desestabiliza a moral'; o medo platônico de que a imagem imite a impureza e estrague a virtude segue vivo no debate."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "Como as oficinas terapêuticas de teatro e pintura em Centros de Atenção Psicossocial (CAPS) materializam o poder curativo da mímesis e da catarse?",
        "Impondo o isolamento solitário de pacientes em enfermarias fechadas sem contato social.",
        "Permitindo que pessoas em sofrimento psíquico encenem suas angústias e dores em personagens fictícios ou cores, externalizando traumas à distância estética e restaurando o equilíbrio psíquico.",
        "Substituindo todos os tratamentos médicos por exercícios de memorização de datas cívicas.",
        "Obrigando os participantes a confeccionarem uniformes militares para tropas de infantaria.",
        "Proibindo a utilização de instrumentos musicais para evitar ruídos sonoros nos hospitais.",
        "B",
        "A arteterapia é mímesis que cura: encenar a própria dor através de uma peça teatral ou pintá-la no papel tira a angústia de dentro do peito e permite olhar para a ferida com serenidade catártica."
    ))

    questoes_brutas.append((
        19, "EM13CHS301", "basico",
        "Qual é o equívoco primário cometido por quem acusa Platão de ter sido um 'inimigo rançoso da beleza'?",
        "Esquecer que o filósofo participava ativamente de torneios de poesia cômica na juventude.",
        "Ignorar que em diálogos como O Banquete e Fedro Platão exalta o Belo em si como o objeto supremo do amor e da alma, condenando apenas a imitação sensorial que falsifica a verdade.",
        "Desconhecer que Platão era o principal proprietário de oficinas de cerâmica pintada em Atenas.",
        "Supor que os diálogos platônicos foram redigidos por dramaturgos profissionais contratados.",
        "Afirmar que a Academia de Atenas cobrava mensalidades dos estudantes de artes decorativas.",
        "B",
        "Platão amava a Beleza! Ele dedicou O Banquete a mostrar que a Beleza verdadeira é a perfeição espiritual da alma; o que ele combateu foi o truque ilusionista da cópia material que engana os olhos desatentos."
    ))

    questoes_brutas.append((
        20, "EM13CHS302", "basico",
        "Como a tragédia Antígona de Sófocles exemplifica a tensão clássica entre as leis sagradas da família e as leis do Estado na dramaturgia grega?",
        "Pela disputa comercial entre armadores marítimos em torno do preço de transporte de azeite.",
        "Pelo conflito insolúvel entre o dever sagrado de Antígona de enterrar o irmão morto e o decreto soberano do rei Creonte que proibia o sepultamento sob pena de morte.",
        "Pela rivalidade atlética entre corredores de maratona nas festividades dos Jogos Olímpicos.",
        "Pela cobrança de impostos extraordinários sobre a posse de vinhedos na cidade de Tebas.",
        "Pelo julgamento arbitral de pescadores que disputavam redes no mar Mediterrâneo oriental.",
        "B",
        "Antígona é o ápice do dilema ético: de um lado a lei divina ancestral que manda enterrar o irmão amado; do outro a lei civil do rei Creonte que manda deixar o corpo apodrecer aos cães; o choque trágico é total."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "De que modo a concepção platônica de 'Alegoria da Caverna' conecta-se diretamente à crítica da pintura ilusionista e da poesia mimética no Livro X de A República?",
        "Demonstrando que os pintores atenienses utilizavam tochas de resina para iluminar ateliês subterrâneos.",
        "Evidenciando que os prisioneiros acorrentados no fundo da caverna contemplavam meras sombras de sombras projetadas na parede, exatamente como o espectador da arte mimética é seduzido por aparências que o afastam da luz solar do Bem inteligível.",
        "Provando que a mineração de carvão na Grécia clássica era supervisionada por mestres de artes cênicas.",
        "Mostrando que os instrumentos de escultura em mármore foram inventados por carpinteiros navais.",
        "Sustentando que as leis de Kallipolis foram gravadas em estelas de pedra colocadas na entrada de grutas.",
        "B",
        "A arte mimética é a fábrica de sombras da caverna: o pintor e o poeta pegam a sombra das coisas do mundo e fazem a sombra da sombra; quem se encanta com a ilusão mimética fica cego para a luz da verdade."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Em A Poética, qual é a importância da noção de 'Verossimilhança' (*Eikos*) para a construção da fábula trágica segundo Aristóteles?",
        "Garantir que os custos orçamentários de cenários não ultrapassem as receitas arrecadadas com ingressos.",
        "Assegurar que as ações dramáticas encadeiem-se segundo a lógica da probabilidade e da necessidade da natureza humana, tornando a história crível e universalmente compreensível para a razão da plateia.",
        "Exigir que todos os diálogos dramáticos contenham dados estatísticos colhidos em registros fiscais.",
        "Determinar que os atores utilizem unicamente roupas brancas confeccionadas com tecidos de algodão egípcio.",
        "Proibir a introdução de personagens femininas em peças dramáticas de conteúdo militar ou político.",
        "B",
        "A verossimilhança não é cópia fotográfica de um fato factual real; é aquilo que parece verdadeiro e necessário para a razão humana: as ações devem fazer sentido causal para que a mente acredite e sinta a trama."
    ))

    questoes_brutas.append((
        23, "EM13CHS301", "intermediario",
        "Como a teoria aristotélica da tragédia influenciou Sigmund Freud na formulação do conceito psicanalítico de 'Complexo de Édipo' em A Interpretação dos Sonhos (1900)?",
        "Provando que os distúrbios psíquicos decorriam da ingestão de bebidas fermentadas em banquetes.",
        "Demonstrando que a peça de Sófocles ecoa um conflito psíquico universal da infância reprimido no inconsciente humano, explicando a comoção atemporal que a peça desperta através da identificação dramática.",
        "Afirmando que a tragédia grega deve ser utilizada exclusivamente em sessões de hipnose clínica individual.",
        "Comprovando que os oráculos de Delfos eram conduzidos por médicos especializados em doenças neurológicas.",
        "Sustentando que a análise de sonhos foi inventada por dramaturgos do teatro elisabetano inglês.",
        "B",
        "Freud recorre à Poética e a Sófocles: Édipo Rei continua a emocionar a humanidade milênios depois porque toca em desejos e pavores primordiais universais que habitam as profundezas de todo ser humano."
    ))

    questoes_brutas.append((
        24, "EM13CHS302", "intermediario",
        "Qual é a função do 'Coro' (*Khoros*) na dinâmica formal e moral da tragédia grega clássica?",
        "Vender alimentos e bebidas aos cidadãos sentados nas fileiras superiores dos teatros.",
        "Representar a voz coletiva da comunidade e dos cidadãos da pólis, comentando os acontecimentos com prudência, advertindo sobre a desmedida e meditando sobre a fragilidade do destino humano.",
        "Substituir os atores principais quando estes demonstravam fadiga vocal durante os espetáculos.",
        "Fiscalizar o recolhimento de impostos devidos pelas companhias de teatro aos tesouros municipais.",
        "Executar marchas militares de exibição de força física nos intervalos das cenas dramáticas.",
        "B",
        "O coro trágico é a consciência coletiva da pólis: ele canta, lamenta e aconselha, lembrando que a arrogância (*hybris*) derruba até os reis mais poderosos e que a moderação prudente é a maior das virtudes."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "De que maneira a invenção da 'Perspectiva Linear' no Renascimento italiano por Brunelleschi e Alberti reacendeu a controvérsia clássica sobre a mímesis?",
        "Rejeitando o uso de cálculos matemáticos e geometria na representação de edifícios em pinturas.",
        "Mobilizando a geometria óptica racional para construir a ilusão tridimensional sobre uma tela plana, refinando a tekhne imitativa e consagrando o ideal mimético de representação verossímil da natureza.",
        "Proibindo a pintura de figuras humanas em telas destinadas a capelas e basílicas religiosas.",
        "Determinar que os pintores florentinos deviam utilizar unicamente pigmentos minerais de coloração preta.",
        "Exigindo que as paisagens naturais fossem representadas de modo abstrato e sem pontos de fuga visuais.",
        "B",
        "A perspectiva renascentista levou a mímesis ao ápice técnico: usando matemática e geometria óptica, o pintor cria uma janela perfeita para o mundo tridimensional sobre a tábua plana, unindo arte, ciência e razão."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "Por que, na visão de Platão, os mitos homéricos que retratam os deuses do Olimpo cometendo crimes, mentiras e adultérios são perigosos para a educação (paideia) da juventude?",
        "Porque os livros da Ilíada e da Odisseia eram impressos em pergaminhos de couro caros demais.",
        "Porque a juventude toma os deuses como modelos morais supremos; ao ver divindades agindo de forma vil e vingativa, os jovens passam a justificar seus próprios erros e condutas desonestas na pólis.",
        "Porque os versos épicos de Homero continham erros gramaticais de difícil compreensão para alunos.",
        "Porque os sacerdotes dos templos exigiam a cobrança de tributos sobre a recitação de poemas épicos.",
        "Porque os guerreiros homéricos utilizavam armas de ferro forjado consideradas obsoletas pelo exército.",
        "B",
        "Para Platão, a educação moral dos jovens depende de exemplos nobres: se a criança ouve que Zeus trai e mata por capricho, ela concluirá que o crime é natural e virtuoso; por isso as fábulas imorais devem ser censuradas."
    ))

    questoes_brutas.append((
        27, "EM13CHS301", "intermediario",
        "Como a distinção aristotélica entre o 'Sentido Médico' e o 'Sentido Religioso' da palavra catarse enriquece a compreensão estética de A Poética?",
        "Mostrando que a catarse exigia a ingestão obrigatória de ervas amargas nos intervalos das peças.",
        "Evidenciando que a catarse estética funde a purgação médica das toxinas acumuladas com a purificação ética e espiritual da alma, pacificando as emoções destrutivas através do entendimento racional da fábula.",
        "Provando que as tragédias eram encenadas exclusivamente em hospitais militares de tratamento de feridos.",
        "Sustentando que os espectadores eram submetidos a rituais de purificação corporal com água do mar Egeu.",
        "Demonstrando que a assistência aos espetáculos dependia da emissão de laudos de saúde por médicos da pólis.",
        "B",
        "Aristóteles é genial: assim como o remédio médico expele os humores venenosos do corpo e o ritual purifica a culpa, a tragédia purga e clarifica os afetos de medo e dó da mente, devolvendo a saúde psicológica ao espectador."
    ))

    questoes_brutas.append((
        28, "EM13CHS302", "intermediario",
        "O que diferencia a 'Tragédia' da 'Comédia' na classificação dos gêneros poéticos miméticos operada por Aristóteles?",
        "A Tragédia utiliza exclusivamente atores infantis e a Comédia é encenada por magistrados idosos.",
        "A Tragédia imita homens moralmente nobres e superiores, retratando ações graves e dolorosas; a Comédia imita homens moralmente inferiores ou risíveis, focando o defeito ou feiura sem causar dor nem destruição.",
        "A Tragédia é encenada em salões cobertos e a Comédia realiza-se unicamente em embarcações de pesca.",
        "A Tragédia aborda disputas de demarcação de terras e a Comédia trata de tratados diplomáticos navais.",
        "A Tragédia foi inventada por filósofos pré-socráticos e a Comédia por generais de legiões de infantaria.",
        "B",
        "Aristóteles estabelece o degrau ético: a tragédia trata da queda de homens nobres e de ações solenes graves; a comédia retrata figuras ridículas, o feio inofensivo e o desajeitado que faz rir sem causar massacre real."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Como a noção grega de 'Hybris' (desmedida ou arrogância) atua como catalisadora da destruição dos heróis trágicos na dramaturgia de Ésquilo e Sófocles?",
        "Incentivando os governantes a reduzirem as despesas com a manutenção de edifícios públicos.",
        "Levando o herói a desafiar os limites humanos e os decretos sagrados dos deuses tomado pela presunção de invencibilidade, atraindo inevitavelmente o castigo reparador do destino (*Nemesis*).",
        "Obrigando os cidadãos a realizarem viagens comerciais em períodos de tempestades marítimas.",
        "Provocando a deserção em massa de tripulações de caravelas mercantes em portos estrangeiros.",
        "Determinando que os reis fossem destronados quando recusassem promover banquetes comunitários.",
        "B",
        "Hybris é o pecado da arrogância: quando o homem ilustre acredita que é um deus e desafia a ordem cósmica, a Justiça divina (Nêmesis) se abate sobre ele; a tragédia ensina os mortais a lembrarem sua pequenez."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "De que modo a filosofia da arte de Aristóteles supera a acusação platônica de que o espectador teatral seria um mero ser passivo e descontrolado?",
        "Mostrando que os espectadores eram obrigados a empunhar armas de bronze durante as sessões teatrais.",
        "Demonstrando que a apreciação estética envolve a atividade intelectual e interpretativa da mente, que analisa as causas da peripécia, compreende a falha do herói e aprende verdades universais sobre a prudência.",
        "Provando que as arquibancadas de teatros gregos eram reservadas exclusivamente a professores de matemática.",
        "Afirmando que o público tinha o direito de alterar os finais das tragédias através de votações abertas.",
        "Sustentando que a comoção teatral dependia da ingestão prévia de vinhos importados em taças de cobre.",
        "B",
        "Aristóteles desfaz o preconceito: quem assiste à tragédia não é um histérico desvairado; a plateia reflete, deduz causas e consequências da trama e sai da peça com a compreensão filosófica da vida ampliada."
    ))

    questoes_brutas.append((
        31, "EM13CHS301", "intermediario",
        "Qual é a crítica de Aristóteles ao uso do artifício cênico do 'Deus Ex Machina' (a intervenção sobrenatural repentina de um deus para resolver a trama) na tragédia?",
        "Condena o recurso por encarecer o custo de fabricação de guindastes de madeira nos teatros.",
        "Afirma que o desenlace da fábula (*mythos*) deve decorrer da necessidade interna e do encadeamento causal das ações dos personagens, e não de intervenções mágicas artificiais caídas do céu.",
        "Elogia o dispositivo como a forma mais sublime de demonstrar a fidelidade das preces sacerdotais.",
        "Sustenta que o uso de cordas para suspender estátuas sagradas desestabilizava as colunas cênicas.",
        "Determina que os deuses só deveriam aparecer em cena após o pagamento de tributos a templos de Atenas.",
        "B",
        "Aristóteles recusa truques fáceis: o final da tragédia tem que brotar das ações dos próprios homens; enfiar um deus pendurado numa corda para consertar o enredo no final é preguiça dramatúrgica e falta de arte."
    ))

    questoes_brutas.append((
        32, "EM13CHS302", "intermediario",
        "Como a defesa aristotélica da arte poética conecta-se à sua teoria ética da 'Prudência' (*Phronesis*) desenvolvida na Ética a Nicômaco?",
        "Mostrando que os poetas trágicos eram isentos do cumprimento de virtudes morais cotidianas.",
        "Evidenciando que a catarse educa as emoções para o justo meio e a contemplação do destino trágico ensina o cidadão a deliberar com cautela, evitando os excessos da arrogância em sua vida política e pessoal.",
        "Comprovando que a moderação moral só pode ser alcançada através da renúncia a qualquer bem material.",
        "Sustentando que as tragédias eram encenadas para ensinar táticas de espionagem militar em cidades vizinhas.",
        "Determinando que os cidadãos prudentes deveriam abster-se de comparecer a festivais teatrais municipais.",
        "B",
        "Ética e estética dão as mãos: a tragédia é a grande escola da prudência (phronesis); ao ver heróis destruídos pelo excesso e pela presunção, o cidadão aprende a buscar o equilíbrio e a sabedoria do justo meio."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "De que modo a peça Prometeu Acorrentado de Ésquilo manifesta a dignidade da 'Tekhne' e a insubmissão ética perante a tirania divina?",
        "Mostrando que Prometeu utilizava ferramentas de bronze para a abertura de túneis subterrâneos.",
        "Evidenciando o titã rebelde que roubou o fogo e o conhecimento técnico das artes para doá-los à humanidade desamparada, enfrentando o castigo eterno de Zeus em nome da emancipação dos mortais.",
        "Comprovando que os deuses olímpicos realizavam assembleias democráticas em dias de solstício de verão.",
        "Sustentando que a técnica humana deve ser limitada unicamente à fabricação de ânforas de cerâmica.",
        "Provando que a ordem cósmica dependia da queima de incensos aromáticos em altares marítimos.",
        "B",
        "Prometeu é o herói da razão humana: roubou o fogo e as ciências dos deuses para libertar os homens da escuridão animal; acorrentado na pedra pelo tirano Zeus, ele prefere a tortura à submissão covarde."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "Como a estética contemporânea das narrativas imersivas e dos jogos eletrônicos (videogames) dramáticos reatualiza a 'Catarse' e a 'Mímesis' gregas?",
        "Substituindo todos os aparelhos de computação por livros didáticos impressos em papel vegetal.",
        "Colocando o jogador no controle de heróis imperfeitos submetidos a dilemas éticos cruciais, peripécias dramáticas e perdas dolorosas, provocando compaixão e clarificação catártica através da interatividade.",
        "Proibindo o uso de trilhas sonoras orquestrais em produções audiovisuais contemporâneas.",
        "Provando que os videogames provocam a atrofia definitiva da capacidade de raciocínio dedutivo.",
        "Exigindo que os desenvolvedores digitais adotem regras de censura estabelecidas por corporações de tecelões.",
        "B",
        "Nos games dramáticos modernos (como The Last of Us), vivemos a tragédia aristotélica em primeira pessoa: tomamos decisões difíceis, sofremos perdas perigosas e vivemos a catarse na ponta dos dedos."
    ))

    questoes_brutas.append((
        35, "EM13CHS301", "intermediario",
        "Por que Platão afirmava que a pintura que utiliza a técnica da 'Cenografia' e da ilusão óptica de sombras mente descaradamente à inteligência humana?",
        "Porque as tintas minerais provocavam reações alérgicas nas mãos dos pintores atenienses.",
        "Porque a perspectiva distorce os tamanhos e proporções reais das coisas em função do ponto de vista do espectador, fazendo o grande parecer pequeno e o torto parecer reto, enganando a razão com falsidades.",
        "Porque as molduras de madeira das telas eram esculpidas sem alinhamento geométrico perfeito.",
        "Porque os pintores recusavam representar cenas de colheitas agrícolas de uvas em murais públicos.",
        "Porque as leis municipais de Atenas proibiam a exibição de pinturas em salões fechados de templos.",
        "B",
        "Para Platão, o pintor ilusionista é um charlatão: ele deforma a geometria para iludir o olho; se o que importa é a essência real medida pela matemática, o quadro que parece ter profundidade mente para a inteligência."
    ))

    questoes_brutas.append((
        36, "EM13CHS302", "intermediario",
        "Em A Poética, qual é a crítica de Aristóteles à chamada 'Fábula Episódica', na qual os acontecimentos se sucedem sem encadeamento causal necessário?",
        "Considera-a a forma poética mais nobre por imitar o fluxo imprevisível de tempestades marinhas.",
        "Classifica-a como a pior espécie de arranjo dramático, pois se os eventos ocorrem uns depois dos outros sem relação de causa e efeito verossímil, a trama perde a força trágica e o poder de comover a razão da plateia.",
        "Afirma que os episódios isolados facilitavam a memorização dos textos pelos atores de corais.",
        "Sustenta que as peças episódicas eram mais econômicas para a administração financeira da pólis.",
        "Determina que os enredos sem lógica deveriam ser encenados unicamente em festividades comemorativas navais.",
        "B",
        "Aristóteles exige lógica rigorosa: se uma cena acontece apenas 'depois' da outra sem ter sido 'causada' por ela, a história vira uma colcha de retalhos boba; a boa tragédia é uma corrente de ferro causal."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Como a figura trágica de 'Medeia' na dramaturgia de Eurípides desconstrói a visão simplista de que os mitos gregos reforçavam passivamente o patriarcado tradicional?",
        "Mostrando que Medeia dedicava suas manhãs exclusivamente ao cuidado de pomares domésticos.",
        "Apresentando uma mulher estrangeira traída pelo marido Jasão que denuncia com fúria lúcida a opressão e o cativeiro conjugal das mulheres em Atenas, levando sua vingança trágica a extremos aterrorizantes.",
        "Comprovando que as rainhas helênicas possuíam o direito irrevogável de presidir cortes de justiça marciais.",
        "Provando que as leis de divórcio na Grécia clássica garantiam a partilha igualitária de caravelas mercantes.",
        "Afirmando que a liderança de Medeia decorreu de decretos de nobreza emitidos por conselhos de sacerdotes.",
        "B",
        "Medeia cospe a verdade na cara de Atenas: denuncia que a mulher é comprada pelo dote e trancada no lar sem voz; abandonada por Jasão, sua vingança destrutiva abala as bases morais do mundo masculino grego."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "Qual é a relação entre o conceito aristotélico de 'Mito' (*Mythos*) em A Poética e a noção moderna de 'Roteiro' ou 'Enredo' no cinema e na literatura?",
        "Mythos designava exclusivamente a recitação de fábulas mágicas envolvendo animais falantes.",
        "Mythos é a própria alma e o princípio estruturante da tragédia: a composição e o arranjo lógico das ações encadeadas de modo coerente, correspondendo rigorosamente à estrutura de roteiro dramático moderno.",
        "Mythos referia-se unicamente ao figurino e às máscaras utilizadas pelos personagens dramáticos.",
        "Mythos designava a arrecadação de moedas metálicas nas bilheterias de teatros municipais.",
        "Mythos era a partitura musical tocada por flautistas nos intervalos de cenas cênicas.",
        "B",
        "Para Aristóteles, o mythos é a alma da peça: não é lenda fantasiosa, é o enredo estruturado de ações encadeadas por causa e consequência; sem um grande roteiro bem amarrado, não há grande obra de arte."
    ))

    questoes_brutas.append((
        39, "EM13CHS301", "intermediario",
        "De que modo a censura poética proposta por Platão em A República distingue-se de uma censura inquisitorial obscurantista que destrói o saber?",
        "Porque Platão pretendia queimar todas as bibliotecas e proibir o estudo da geometria euclidiana.",
        "Porque a proposta platônica nasce de um projeto pedagógico rigoroso de engenharia social e virtude cívica: Platão admite a força pedagógica titânica da arte e busca orientá-la para a justiça e o cultivo da razão.",
        "Porque as determinações de Platão foram redigidas para favorecer o comércio exterior de tecidos de linho.",
        "Porque a censura de Kallipolis era exercida exclusivamente por conselhos de médicos e farmacêuticos.",
        "Porque as decisões sobre expulsão de artistas dependiam de sorteios anuais realizados em feiras populares.",
        "B",
        "Platão não queima livros por ódio irracional: ele reconhece que a poesia é uma das forças educativas mais poderosas do mundo; exatamente por saber do seu poder formador de mentes, ele quer usá-la para o Bem cívico."
    ))

    questoes_brutas.append((
        40, "EM13CHS302", "intermediario",
        "Por que, para Aristóteles, o estudo da 'Estética' e da criação artística não se reduz à mera contemplação passiva do belo, mas integra a dimensão prática da vida humana (*Praxis* e *Poiesis*)?",
        "Porque os cidadãos gregos eram obrigados a trabalhar manualmente em pedreiras de mármore branco.",
        "Porque a produção de obras (poiesis) e a sua recepção emocional e moral (catarse) transformam o caráter, refinam as sensibilidades e educam os cidadãos para a deliberação sábia e prudente na vida pública da pólis.",
        "Porque as obras de arte eram comercializadas exclusivamente como moeda de troca em transações navais.",
        "Porque as corporações de artesãos dominavam a totalidade dos assentos parlamentares em assembleias cívicas.",
        "Porque a contemplação estética dependia da aprovação de conselhos consulares de cidades estrangeiras.",
        "B",
        "A arte em Aristóteles não é luxo de museu desinteressado: é poiesis (criação humana) que educa o espírito do cidadão; a vivência catártica refina os sentimentos e forma pessoas mais sábias para a vida na pólis."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a crítica de Platão à arte mimética no Livro X de A República a partir do confronto entre o 'Mundo Inteligível das Formas' e o 'Mundo Sensível das Cópias': de que maneira a demonstração dos três graus de afastamento da verdade evidencia que a pintura ilusionista e a poesia dramática constituem desvios metafísicos que aprisionam a alma humana nas sombras da Caverna?",
        "Provando que as academias de pintura utilizavam cavaletes de madeira de carvalho importados do norte.",
        "Demonstrando que, ao passo que a Ideia inteligível é a realidade essencial suprema e o objeto fabricado pelo marceneiro é sua cópia particular material, o artista mimético reproduz unicamente a aparência visual da cópia sem qualquer conhecimento da essência ou da utilidade do objeto, fabricando simulacros de terceiro grau que ludibriam a percepção e afastam a alma da contemplação racional do Ser.",
        "Determinando que os contratos comerciais de compra de tintas devessem ser selados em praças consulares.",
        "Afirmando que a teoria platônica dos três leitos foi copiada de manuais de arquitetura residencial persa.",
        "Comprovando que os artesãos atenienses realizavam assembleias corporativas em dias de solstício de inverno.",
        "B",
        "- **Etapa 1:** Reconstruir a hierarquia metafísica de Platão: no topo está a Forma inteligível perfeita (o leito ideal); no meio está a coisa física concreta feita pelo carpinteiro que olha para a Ideia.\n- **Etapa 2:** Desvelar a farsa do simulacro de terceiro grau: o pintor não entende de marcenaria nem de Ideia; ele apenas fotografa de lado a casca exterior do leito de madeira; pintar ou encenar é produzir a sombra da sombra, prendendo o homem na caverna."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a crítica ético-política platônica contra a comoção emocional no teatro grego: de que modo a tese de que a tragédia 'alimenta e rega as paixões irracionais da alma' ameaça a justiça individual e a segurança militar da pólis ideal em Kallipolis?",
        "Mostrando que os cenários teatrais utilizavam vigas de madeira com risco de desmoronamento estrutural.",
        "Evidenciando que a justiça na cidade e na alma exige o domínio soberano da razão sobre os apetites e a cólera; ao estimular o choro descontrolado, os lamentos teatrais e o deleite na contemplação do infortúnio desmedido, a tragédia enfraquece a couraça moral do guerreiro e do cidadão, tornando-o frágil, indisciplinado e incapaz de exercer a coragem estoica exigida na guerra e nas deliberações cívicas.",
        "Determinando que os soldados de infantaria devessem ser alimentados unicamente com pão de centeio nas casernas.",
        "Afirmando que as festividades teatrais foram instituídas para financiar a manutenção de frotas mercantes navais.",
        "Comprovando que as arquibancadas de anfiteatros eram fiscalizadas por comissões de mercadores de cereais.",
        "B",
        "- **Etapa 1:** Recordar a psicologia tripartite da alma em Platão: a razão tem que manter rédeas curtas sobre a cólera e o desejo carnal para que o homem seja justo e equilibrado.\n- **Etapa 2:** Expor o perigo cívico da plateia chorosa: no teatro, o cidadão bate no peito, berra e se apieda de deuses covardes; ao sair dali e ir para o campo de batalha, aquele cidadão amolecido terá medo de morrer e fugirá da lança inimiga."
    ))

    questoes_brutas.append((
        43, "EM13CHS301", "dificil",
        "Examine a profunda revolução teórica operada por Aristóteles em A Poética ao proclamar que 'a poesia é algo mais filosófico e mais elevado do que a história': de que maneira a tensão entre o 'Universal Verossímil' e o 'Particular Factual' confere à arte um estatuto cognitivo superior à mera crônica factual dos acontecimentos?",
        "Provando que os papiros históricos perdiam a legibilidade devido à umidade em arquivos provinciais.",
        "Demonstrando que, enquanto o historiador se encontra acorrentado à contingência empírica daquilo que de fato ocorreu em um momento particular (o que Alcibíades fez ou sofreu), o poeta dramático compõe a ação segundo a necessidade essencial e a verossimilhança da natureza humana, revelando leis universais sobre como qualquer ser humano agiria sob determinados dilemas existenciais e éticos.",
        "Determinando que os livros de poesia dramática devam ser catalogados exclusivamente por academias navais.",
        "Afirmando que os historiadores clássicos gregos desconheciam o funcionamento de relógios de areia.",
        "Comprovando que as narrativas poéticas eram utilizadas unicamente em litígios comerciais de alfândegas.",
        "B",
        "- **Etapa 1:** Reconhecer a prisão factual do historiador: o historiador narra o detalhe particular acidental (o general ganhou a batalha porque choveu ou traiu a esposa naquele dia específico).\n- **Etapa 2:** Consolidar a nobreza filosófica da poesia: o poeta cria uma fábula verossímil que resume a alma humana; Édipo ou Hamlet mostram como o poder, o medo e a culpa agem em qualquer ser humano de qualquer época; a arte alcança a essência universal."
    ))

    questoes_brutas.append((
        44, "EM13CHS302", "dificil",
        "Investigue o mecanismo estético da 'Catarse' (*Katharsis*) em Aristóteles: como a experiência vicária dos afetos de Terror (*Phobos*) e Piedade (*Eleos*) no teatro promove a purgação e a clarificação moral das paixões sem degenerar a conduta do cidadão na vida real?",
        "Comprovando que as substâncias aromáticas queimadas no altar cênico possuíam efeitos sedativos neurológicos.",
        "Evidenciando que a tragédia oferece um espaço de segurança ficcional no qual o espectador experimenta intensamente o temor existencial e a compaixão empática diante da destruição do herói falível; ao vivenciar essas paixões de modo desinteressado e mediado pelo intelecto que compreende a trama causal, o indivíduo descarrega os excessos emocionais tóxicos e retorna à pólis moralmente renovado, sereno e prudente.",
        "Determinando que os ingressos para os festivais dramáticos devam ser distribuídos por sorteios paroquiais.",
        "Afirmando que os anfiteatros de pedra possuíam qualidades acústicas projetadas por engenheiros bálticos.",
        "Provando que os espectadores eram submetidos a testes de memorização poética ao término dos espetáculos.",
        "B",
        "- **Etapa 1:** Descrever o laboratório da ficção: no teatro podemos sentir o terror da morte sem correr perigo real e podemos chorar pelo outro sem ter que pagar o preço da catástrofe na carne.\n- **Etapa 2:** Concluir sobre a purificação ética: ao esvaziar a angústia acumulada e compreender racionalmente os erros da arrogância do herói, o espectador pacifica seus humores e sai do teatro mais humano, prudente e solidário."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Analise a anatomia dramatúrgica da tragédia aristotélica a partir do entrelaçamento entre 'Peripécia' (*Peripeteia*), 'Reconhecimento' (*Anagnorisis*) e 'Falha Trágica' (*Hamartia*): como esse encadeamento atinge o clímax da comoção estética na obra-prima Édipo Rei de Sófocles?",
        "Mostrando que o rei de Tebas distribuía moedas de prata para os camponeses afetados por secas rurais.",
        "Demonstrando que Édipo, um rei nobre e justo, sofre a mais violenta peripécia ao passar da glória real à desgraça cega e banida precisamente no instante em que opera o reconhecimento amargo de sua verdadeira identidade (descobrindo ser ele próprio o parricida e o esposo da mãe que amaldiçoara), materializando a tragédia como fruto não de vilania sádica, mas de um erro de julgamento insolúvel diante do destino.",
        "Determinando que as profecias do oráculo délfico fossem ratificadas por comissões consulares marítimas.",
        "Afirmando que a peste de Tebas foi erradicada unicamente através da construção de aquedutos fluviais.",
        "Comprovando que a investigação criminal de Édipo utilizou certidões emitidas por cartórios de alfândegas.",
        "B",
        "- **Etapa 1:** Conectar as três engrenagens da Poética em Sófocles: Édipo começa como o grande salvador de Tebas e investigador implacável do assassinato de Laio.\n- **Etapa 2:** Atingir o ápice trágico: o instante em que ele descobre quem é (anagnorisis) é o mesmo instante em que sua vida desmorona da coroa para o exílio cego (peripeteia); o espectador gela de pavor e chora de compaixão diante da fatalidade humana."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Examine o conceito aristotélico de 'Mito' ou 'Fábula' (*Mythos*) como a 'alma da tragédia': por que Aristóteles defende a primazia absoluta da ação encadeada por necessidade causal sobre a caracterização psicológica isolada dos personagens?",
        "Provando que os dramaturgos gregos desconheciam técnicas de pintura facial e caracterização estética.",
        "Evidenciando que a tragédia é essencialmente imitação de ações e de vida, e não de homens em si; os personagens só ganham densidade dramática e revelam seu caráter ético (*ethos*) através dos atos que realizam e das decisões que tomam no interior do enredo, de modo que uma trama bem urdida por causalidade lógica sustenta o drama mesmo sem ornatos cênicos espetaculares.",
        "Determinando que os roteiros trágicos devessem ser aprovados em plenários de assembleias de infantaria.",
        "Afirmando que a encenação teatral grega dispensava a participação de atores profissionais especializados.",
        "Comprovando que as ações dramáticas eram decididas por sorteios anuais realizados em praças comerciais.",
        "B",
        "- **Etapa 1:** Entender a definição de tragédia como imitação de ação: para Aristóteles, não basta colocar uma pessoa interessante no palco; a essência do teatro é o que os personagens fazem e sofrem no enredo.\n- **Etapa 2:** Confirmar o império do mythos: o enredo amarrado por causa e efeito é o motor supremo; o caráter do herói só brilha quando ele é forçado a agir sob a pressão de escolhas difíceis e consequências implacáveis."
    ))

    questoes_brutas.append((
        47, "EM13CHS301", "dificil",
        "Analise a relevância contemporânea do debate entre Platão e Aristóteles nos campos da Bioética e da Regulação da Inteligência Artificial Generativa: de que maneira a produção em massa de imagens artificiais perfeitas ('Deepfakes') reativa a advertência platônica sobre os perigos do simulacro mimético de terceiro grau?",
        "Comprovando que os servidores de computação em nuvem operam com turbinas hidráulicas desprovidas de óleo.",
        "Demonstrando que as ferramentas generativas produzem cópias digitais hiper-realistas que mimetizam rostos, vozes e discursos humanos sem qualquer relação necessária com a verdade factual, gerando ilusões perfeitas que enganam a percepção coletiva, desestabilizam democracias com desinformação deliberada e confirmam a profecia platônica sobre a tirania das aparências sobre o intelecto.",
        "Determinando que as câmeras fotográficas devam utilizar filmes de gelatina biodegradável em seus circuitos.",
        "Afirmando que a inteligência artificial foi inventada para calcular impostos sobre frotas mercantes de pesca.",
        "Provando que a circulação de imagens digitais depende de autorização expedida por academias de letras clássicas.",
        "B",
        "- **Etapa 1:** Identificar o deepfake como a caverna de Platão contemporânea: a IA cria um vídeo de um presidente declarando guerra que parece 100% real para os olhos e ouvidos humanos.\n- **Etapa 2:** Reativar o alarme platônico do simulacro: a máquina fabrica a cópia sem alma e sem verdade; a sociedade é ludibriada por imagens miméticas perigosas, provando que a advertência de Platão contra o ilusionismo técnico é vital hoje."
    ))

    questoes_brutas.append((
        48, "EM13CHS302", "dificil",
        "Examine o conceito de 'Hamartia' em contraste com a ideia teológica cristã medieval de 'Pecado': por que a falha trágica do herói grego não deve ser compreendida como uma culpa moral deliberada ou maldade inata, mas como um erro de cálculo cognitivo e existencial inevitável?",
        "Provando que os sacerdotes pagãos desconheciam o uso de pergaminhos religiosos em capelas municipais.",
        "Demonstrando que, ao passo que o pecado judaico-cristão supõe a desobediência consciente e voluntária da criatura contra a lei de Deus passível de culpa moral eterna, a hamartia grega expressa a finitude e os pontos cegos da razão humana: o herói erra por ignorância fática, por julgamento desmedido ou por encadeamentos cosmológicos que escapam ao controle de sua vontade mortal.",
        "Determinando que as confissões de culpas civis deviam ser pronunciadas perante magistrados de cortes navais.",
        "Afirmando que a doutrina do pecado original foi copiada de manuais de carpintaria da bacia do mar Cáspio.",
        "Comprovando que as penitências dos heróis consistiam no pagamento compulsório de moedas de prata fundida.",
        "B",
        "- **Etapa 1:** Afastar a confusão entre falha trágica e pecado: o herói trágico grego não é um demônio pecador que escolheu o mal por perversidade do coração.\n- **Etapa 2:** Resgatar a tragédia da condição humana: Édipo fez de tudo para fugir do oráculo e proteger seus pais adotivos; seu erro (hamartia) foi não saber quem eram os viajantes na encruzilhada; a tragédia grega chora a cegueira e a fragilidade de quem é mortal."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Investigue o diálogo entre A República de Platão e os dilemas contemporâneos de Censura Versus Liberdade de Expressão nas Redes Sociais: como a exigência platônica de que o Estado tutele os conteúdos para proteger os jovens é mobilizada hoje na regulação de plataformas digitais contra o ódio e a violência?",
        "Mostrando que os cabos de fibra ótica submarinos foram instalados em alinhamento com correntes marítimas.",
        "Evidenciando que governos democráticos contemporâneos debatem limites à circulação de desinformação, apologia ao nazismo e incitação a massacres escolares nas redes sob o fundamento de que a difusão livre de conteúdos danosos corrompe a cidadania e gera violência no mundo real, reeditando a premissa de Platão de que a formação da juventude exige a intervenção ética da comunidade sobre a indústria cultural.",
        "Determinando que as postagens em redes virtuais devessem ser digitadas exclusivamente em língua grega clássica.",
        "Afirmando que a censura governamental nas redes decorre unicamente de disputas tarifárias entre corporações de telecomunicações.",
        "Provando que a fiscalização de aplicativos móveis foi delegada a congregações religiosas beneditinas do interior.",
        "B",
        "- **Etapa 1:** Reconhecer o dilema entre liberdade absoluta e proteção da vida: a internet livre permitiu a proliferação de discursos de ódio, suicídio infantil e ataques terroristas a escolas.\n- **Etapa 2:** Reconhecer o eco de Platão no debate de regulação: regular as redes não é tolice autoritária, mas dever de proteção da sociedade; uma cidade que deixa veneno ser despejado na mente de suas crianças colherá a destruição de sua democracia."
    ))

    questoes_brutas.append((
        50, "EM13CHS102", "dificil",
        "Analise a relevância do tratado Da Pintura (1435) de Leon Battista Alberti como manifestação da superação renascentista da condenação platônica da pintura: de que maneira Alberti reivindica o estatuto de ciência e sabedoria racional para a arte da pintura através da matemática e da ótica?",
        "Comprovando que os ateliês de pintura florentinos foram financiados unicamente por congregações monásticas alpinas.",
        "Demonstrando que Alberti liberta a pintura da acusação de ser mero trabalho manual mecânico ou ilusionismo mentiroso, provando que o pintor renascentista domina a geometria euclidiana, a ótica, a perspectiva linear e a anatomia científica, alçando a pintura à condição de disciplina intelectual e via suprema de desvelamento racional e ordenado da criação cósmica.",
        "Determinando que os pintores devessem prestar juramentos de fidelidade perante magistrados de cortes navais mercantes.",
        "Afirmando que a perspectiva linear foi inventada para acelerar a demarcação de lotes agrícolas nas colinas.",
        "Provando que as academias de arte do Renascimento proibiam o estudo de tratados de filosofia e matemática.",
        "B",
        "- **Etapa 1:** Desafiar a condenação de Platão de que a pintura é farsa de marceneiro: Platão dizia que o pintor não precisava de ciência nenhuma, só de pincel e tinta.\n- **Etapa 2:** Consolidar a vitória de Alberti e do Renascimento: Alberti mostra que o grande pintor é geômetra, matemático e filósofo; a tela em perspectiva é uma construção racional rigorosa da mente que revela as leis profundas do cosmos."
    ))

    questoes_brutas.append((
        51, "EM13CHS301", "dificil",
        "Examine o conceito de 'Peripécia' em diálogo com a obra-prima cinematográfica O Poderoso Chefão (The Godfather, de Francis Ford Coppola): como a trajetória trágica de Michael Corleone espelha as regras dramáticas de Aristóteles sobre a queda do homem ilustre e a dor catártica?",
        "Provando que os figurinos utilizados na produção cinematográfica foram adquiridos em feiras municipais italianas.",
        "Evidenciando que Michael Corleone inicia a trama como um jovem condecorado e virtuoso que se recusava a participar dos crimes da família mafiosa, mas, impelido pela lealdade filial e por erros sucessivos de discernimento ético, assume o comando da organização e alcança o poder absoluto ao custo de sua alma, sofrendo a peripécia interior da solidão e da ruína moral completa que desperta pavor e piedade na plateia.",
        "Determinando que as películas de celulóide devessem ser armazenadas em cofres metálicos sob refrigeração.",
        "Afirmando que a trilha sonora foi composta exclusivamente com instrumentos de corda da música sacra medieval.",
        "Comprovando que o roteiro dramático foi adaptado de manuais militares de estratégia de infantaria naval.",
        "B",
        "- **Etapa 1:** Identificar a grandeza e a falha de Michael Corleone: ele era o filho herói de guerra, o mais inteligente e civilizado da família, que pretendia limpar os negócios do pai.\n- **Etapa 2:** Analisar a peripécia aristotélica moderna: tentando proteger os seus, Michael assassina o próprio irmão e destrói sua família; ao final, reina absoluto e rico num banco de jardim, mas morto por dentro; vivemos a catarse do terror e da piedade diante de sua ruína moral."
    ))

    questoes_brutas.append((
        52, "EM13CHS302", "dificil",
        "Investigue o papel da 'Arteterapia' nos tratamentos psiquiátricos contemporâneos à luz da doutrina aristotélica da catarse: de que maneira a transposição de dores e memórias traumáticas para formas estéticas estruturadas (cores, máscaras, cenas de dramatização) opera a purgação afetiva sem expor o paciente ao perigo da re-traumatização?",
        "Comprovando que as oficinas terapêuticas utilizavam tintas formuladas com resinas vegetais não aromáticas.",
        "Demonstrando que a representação artística cria a distância estética indispensável: a dor deixa de ser um pavor interno disforme e asfixiante para se tornar um objeto externo que pode ser olhado, compreendido e reelaborado pelo intelecto, permitindo descarregar o medo e a angústia em ambiente seguro e promovendo a clarificação psíquica preconizada em A Poética.",
        "Determinando que os terapeutas de saúde mental devam proferir seus laudos em versos métricos clássicos.",
        "Afirmando que a cura de transtornos mentais depende da imposição compulsória de rotinas de marcha militar.",
        "Provando que as atividades de pintura deviam ser supervisionadas por comissões de escrivães de alfândegas.",
        "B",
        "- **Etapa 1:** Compreender o bloqueio do trauma psíquico: o paciente traumatizado não consegue falar da dor diretamente porque o terror da lembrança o paralisa e o afoga.\n- **Etapa 2:** Revelar a catarse na arteterapia: ao colocar a máscara de um personagem ou pintar a ferida com tinta na tela, a dor sai de dentro e vira objeto estético; o sujeito olha para a sua dor de fora, purga o veneno e pacifica a mente."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Analise a dialética entre a 'Ordem da Cidade' e a 'Liberdade do Artista' em Platão: por que o filósofo recusa a autonomia moderna da arte pela arte, exigindo que toda produção cultural seja estritamente subordinada ao Bem Comum e à justiça política de Kallipolis?",
        "Provando que as corporações de artesãos deviam pagar tributos anuais em sementes de cevada à corte régia.",
        "Evidenciando que, para Platão, a pólis justa é um organismo moral integrado em que nenhuma atividade particular pode ser descolada do objetivo ético supremo: a educação para a virtude da alma; permitir uma arte autônoma e licenciosa que celebra vícios em nome da liberdade estética individual equivale a aceitar a destruição da harmonia cívica e a degeneração da cidade justa.",
        "Determinando que as obras de escultura em mármore devessem ser quebradas após a conclusão de eleições municipais.",
        "Afirmando que a subordinação das artes foi formulada por generais espartanos em assembleias de cavalaria.",
        "Comprovando que os ateliês de pintura funcionavam exclusivamente durante os períodos de tréguas diplomáticas.",
        "B",
        "- **Etapa 1:** Desmistificar a tese moderna da 'arte pela arte' em Platão: no mundo contemporâneo, diz-se que o artista pode criar qualquer coisa sem prestar contas à moral ou à sociedade.\n- **Etapa 2:** Entender a arquitetura de Kallipolis: para Platão, a cidade é um corpo vivo; se a música ensina desordem e o teatro ensina frouxidão, a cidade adoece; a arte só tem sentido sagrado quando eleva a alma e fortalece a justiça da pólis."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Examine a atualidade do conceito de 'Catarse' nas redes sociais digitais: como a cultura do cancelamento e os linchamentos virtuais de figuras públicas desvirtuam a purgação aristotélica, transformando o alívio afetivo em uma caça cruel e punitivista sem reflexão moral?",
        "Comprovando que as plataformas de mensagens instantâneas utilizam algoritmos codificados em servidores de cobre.",
        "Demonstrando que, ao contrário da tragédia aristotélica que educa a empatia e a piedade pela fragilidade humana, os tribunais virtuais das redes operam uma catarse rebaixada e vingativa: a plateia descarrega suas próprias frustrações e ódios acumulados destruindo publicamente a reputação de bodes expiatórios, substituindo a clarificação ética pelo gozo sádico da humilhação alheia.",
        "Determinando que os usuários de redes devam prestar juramentos de cavalaria antes de publicarem comentários.",
        "Afirmando que os cancelamentos virtuais decorrem exclusivamente da lentidão de conexões de internet discada.",
        "Provando que os linchamentos virtuais foram inventados por congregações monásticas beneditinas em mosteiros alpinos.",
        "B",
        "- **Etapa 1:** Contrastar a catarse grega com o linchamento virtual: no teatro, a plateia chora com compaixão e pensa 'eu também sou falível e poderia errar assim'.\n- **Etapa 2:** Diagnosticar a falsa catarse do linchamento digital: nas redes, a turba enfurecida atira pedras virtuais com regozijo cruel para se sentir santa e superior; em vez de pacificar a alma e gerar prudência, a internet alimenta o ódio cego e a barbárie."
    ))

    questoes_brutas.append((
        55, "EM13CHS301", "dificil",
        "Analise a relevância do 'Tragismo Feminino' na tragédia grega através da figura de 'Antígona': de que maneira a recusa inabalável da jovem heroína em obedecer ao decreto autoritário do rei Creonte inaugura a tradição filosófica da 'Desobediência Civil' contra leis estatais moralmente injustas?",
        "Provando que as mulheres atenienses possuíam o direito irrevogável de emitir sentenças em tribunais consulares.",
        "Evidenciando que Antígona proclama a supremacia das leis imorredouras e não escritas da justiça divina e do amor fraterno sobre as ordens contingentes e tirânicas do governante temporal, afirmando que seu dever sagrado de humanidade e piedade é superior ao arbítrio da espada de Creonte, pagando com a própria vida pela defesa da dignidade dos mortos.",
        "Determinando que os sepultamentos de guerreiros fossem autorizados unicamente por comissões de mercadores navais.",
        "Afirmando que o conflito de Tebas decorreu da escassez de pedras de cantaria para a edificação de túmulos reais.",
        "Comprovando que a heroína contava com o apoio armado de regimentos de cavalaria mercenária estrangeira.",
        "B",
        "- **Etapa 1:** Descrever o choque dramático entre Creonte e Antígona: Creonte diz 'a lei da cidade é soberana e proíbe o enterro do traidor'; Antígona responde 'as leis sagradas dos deuses são eternas e mandam enterrar o irmão'.\n- **Etapa 2:** Consagrar Antígona como mãe da desobediência civil: séculos antes de Thoreau e Gandhi, Antígona ensinou que quando a lei do Estado se torna criminosa e desumana, desobedecer e pagar o preço com coragem é o supremo dever ético de quem ama a justiça."
    ))

    questoes_brutas.append((
        56, "EM13CHS302", "dificil",
        "Examine a diferença crucial entre a recepção estética de Platão e de Aristóteles a respeito da 'Música' na formação dos cidadãos: por que, enquanto Platão desejava banir certas escalas musicais efeminadas de Kallipolis, Aristóteles admitia a pluralidade dos ritmos como fonte de recreação e purificação da mente?",
        "Comprovando que os instrumentos musicais gregos utilizavam cordas de tripa importadas de províncias árticas.",
        "Demonstrando que Platão temia que escalas musicais queixosas ou lascivas (como os modos lídio e jônico) amolecessem a fibra moral dos guerreiros, admitindo unicamente os modos dórico e frígio (austeros e marciais), ao passo que Aristóteles compreendia que a música atua terapeuticamente, acolhendo ritmos diversos para o repouso do trabalho, a educação virtuosa e a catarse emocional dos excessos psíquicos.",
        "Determinando que os flautistas devessem prestar exames de literatura latina antes de tocarem em cerimônias cívicas.",
        "Afirmando que as escalas musicais foram catalogadas exclusivamente por navegadores de esquadras mercantes.",
        "Provando que a música clássica ateniense dependia de aprovação emitida por conselhos paroquiais de monges.",
        "B",
        "- **Etapa 1:** Relembrar a censura musical de Platão: Platão analisou até as notas musicais; escalas chorosas ou voluptuosas deviam ser proibidas porque amoleciam o guerreiro; só permitia ritmos de marcha militar e austeridade.\n- **Etapa 2:** Valorizar a flexibilidade humanista de Aristóteles: Aristóteles entende que o homem precisa de música para descansar a cabeça, para se educar e para purgar a tensão diária; a música é remédio da alma que acalma as tempestades da mente."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Investigue o conceito de 'Verossimilhança' em contraponto à 'Verdade Factual' nas fake news contemporâneas: de que maneira o entendimento de Aristóteles sobre a força da verossimilhança explica por que narrativas conspiratórias mentirosas, mas verossímeis aos olhos de um grupo, convencem mais facilmente a opinião pública do que a fria verdade científica?",
        "Mostrando que as emissoras de rádio utilizavam transmissores mecânicos alimentados por geradores a carvão.",
        "Demonstrando que, como ensinara Aristóteles, a mente humana é seduzida por aquilo que soa provável, coeso e emocionalmente satisfatório segundo suas expectativas e preconceitos prévios (o verossímil); assim, narrativas falsas arquitetadas com ganchos dramáticos envolventes produzem adesão imediata, ao passo que a verdade factual factual é frequentemente complexa, árida e desprovida de apelo ficcional.",
        "Determinando que os textos noticiosos devessem receber selos consulares de garantia antes de sua circulação.",
        "Afirmando que a proliferação de boatos decorre unicamente de erros de tradução em tratados diplomáticos bilaterais.",
        "Comprovando que as teorias de conspiração foram formuladas por artesãos de cerâmica em festivais municipais rurais.",
        "B",
        "- **Etapa 1:** Resgatar a tese de Aristóteles sobre o verossímil: o ser humano prefere acreditar em algo impossível que soa verossímil e provável do que em algo possível que soa inacreditável e estranho.\n- **Etapa 2:** Diagnosticar o veneno das fake news de hoje: a mentira bem montada atende aos medos e ódios da pessoa, parecendo perfeitamente 'lógica' para sua bolha; a verdade científica é cheia de detalhes áridos; entender a poética ajuda a combater a manipulação mental moderna."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Analise a relevância da Poética de Aristóteles para a construção da Teoria do Cinema no século XX: de que maneira o modelo clássico de roteiro cinematográfico em três atos (Apresentação, Clímax com Virada e Resolução) descende diretamente das regras de arranjo dramático formuladas pelo Estagirita?",
        "Provando que as primeiras câmeras de filmagem cinematográfica foram desenhadas com base em lentes de faróis marítimos.",
        "Evidenciando que os manuais clássicos de dramaturgia e cinema (como os de Syd Field e Robert McKee) são releituras diretas de A Poética: o equilíbrio inicial do mythos, a deflagração do conflito, o ponto de virada dramático (peripécia), a revelação da verdade crucial (anagnorisis) e a catarse final continuam a ser a espinha dorsal de quase todos os grandes sucessos narrativos do cinema mundial.",
        "Determinando que os estúdios cinematográficos devessem ser construídos unicamente em áreas florestais preservadas.",
        "Afirmando que os roteiros de cinema foram inspirados em compêndios de contabilidade de feiras comerciais medievais.",
        "Comprovando que a indústria cinematográfica foi fundada por comissões de generais de infantaria veteranos de guerra.",
        "B",
        "- **Etapa 1:** Reconhecer o legado milenar da Poética em Hollywood: os grandes roteiristas de Hollywood estudam Aristóteles de capa a capa.\n- **Etapa 2:** Confirmar a estrutura clássica do cinema: início com apresentação da ação, conflito que cresce, reviravolta no destino (peripécia), o momento em que o segredo explode (anagnorisis) e o clímax emocionante com catarse; Aristóteles escreveu a fórmula do bom cinema há 2.400 anos."
    ))

    questoes_brutas.append((
        59, "EM13CHS301", "dificil",
        "Examine o valor da 'Literatura Dramática' no Ensino Médio segundo as diretrizes da BNCC: de que modo a encenação teatral de tragédias e a análise crítica da mímesis desenvolvem o pensamento autônomo, a empatia e as habilidades socioemocionais dos estudantes?",
        "Provando que as atividades teatrais escolares devem priorizar unicamente a recitação monótona de códigos jurídicos antigos.",
        "Demonstrando que, ao encarnarem personagens submetidos a dilemas éticos complexos e experimentarem a catarse coletiva, os estudantes desenvolvem a capacidade empática de se colocarem no lugar do outro, compreendem as causas profundas dos conflitos humanos e exercitam a reflexão crítica sobre a justiça, superando o individualismo e qualificando sua cidadania na pólis contemporânea.",
        "Determinando que as avaliações pedagógicas devam consistir exclusivamente em provas escritas de memorização de datas cívicas.",
        "Afirmando que a prática de artes cênicas deve ser suspensa nas escolas públicas para economizar recursos orçamentários.",
        "Comprovando que a formação cívica da juventude dispensa o estudo de manifestações artísticas e culturais universais.",
        "B",
        "- **Etapa 1:** Superar a escola decoreba e fria: aprender filosofia não é decorar nomes e datas de filósofos mortos, mas viver o pensamento crítico e sentir o dilema da condição humana.\n- **Etapa 2:** Celebrar o teatro como paideia viva na BNCC: subir no palco da escola para encenar Antígona ou Édipo faz o jovem sentir na pele o que é coragem, injustiça e piedade; a arte grega educa o coração e a mente para a empatia e a liberdade."
    ))

    questoes_brutas.append((
        60, "EM13CHS302", "dificil",
        "Ao encerrarmos com a Estética Antiga de Platão e Aristóteles o Capítulo 25 e abrirmos o Eixo IV (Estética, Filosofia da Arte e Poéticas da Negritude), analise como os conceitos seminais de Mímesis e Catarse estabelecem a plataforma conceitual necessária para os debates subsequentes sobre a Indústria Cultural em Adorno e a Estética da Negritude:",
        "Provando que a reflexão estética da Antiguidade perdeu qualquer validade prática com o advento das máquinas a vapor.",
        "Demonstrando que o debate antigo sobre se a arte emancipa a mente pelo conhecimento e catarse (Aristóteles) ou aliena os homens em ilusões servis de consumo (Platão) fornece o instrumental exato para que os capítulos seguintes investiguem como a indústria cultural manipula a sensibilidade e como os artistas negros utilizam a poética e o teatro para quebrar as máscaras coloniais e afirmar a beleza e a soberania ancestral.",
        "Determinando que as investigações estéticas futuras devam se limitar ao estudo de tratados botânicos de flores silvestres.",
        "Afirmando que os filósofos da Escola de Frankfurt desconheciam os textos de A República e de A Poética.",
        "Comprovando que a transição entre eixos pedagógicos depende de aprovação prévia concedida por academias navais europeias.",
        "B",
        "- **Etapa 1:** Sintetizar o legado do Capítulo 25: Platão alertou sobre o risco da arte virar manipulação ilusionista e Aristóteles revelou a potência curativa e libertadora da mímesis e da catarse.\n- **Etapa 2:** Abrir as portas do Eixo IV com chave de ouro: essa balança entre manipulação e libertação será o coração dos próximos capítulos, onde veremos Benjamin e Adorno dissecando a Indústria Cultural e os pensadores da Negritude resgatando a arte como escudo e espada da soberania negra."
    ))

    return questoes_brutas

def balancear_e_gerar_markdown(questoes_brutas):
    padrao = ['A', 'B', 'C', 'D', 'E']
    questoes_balanceadas = []

    for i, q in enumerate(questoes_brutas):
        num, hab, dif, enunciado, opt_a, opt_b, opt_c, opt_d, opt_e, gab_orig, resolucao = q
        gabarito_desejado = padrao[i % 5]

        correta_texto = opt_b if gab_orig == 'B' else opt_a
        distratores = [opt_a if gab_orig == 'B' else opt_b, opt_c, opt_d, opt_e]

        nova_a, nova_b, nova_c, nova_d, nova_e = None, None, None, None, None

        if gabarito_desejado == 'A':
            nova_a = correta_texto
            nova_b, nova_c, nova_d, nova_e = distratores[0], distratores[1], distratores[2], distratores[3]
        elif gabarito_desejado == 'B':
            nova_b = correta_texto
            nova_a, nova_c, nova_d, nova_e = distratores[0], distratores[1], distratores[2], distratores[3]
        elif gabarito_desejado == 'C':
            nova_c = correta_texto
            nova_a, nova_b, nova_d, nova_e = distratores[0], distratores[1], distratores[2], distratores[3]
        elif gabarito_desejado == 'D':
            nova_d = correta_texto
            nova_a, nova_b, nova_c, nova_e = distratores[0], distratores[1], distratores[2], distratores[3]
        elif gabarito_desejado == 'E':
            nova_e = correta_texto
            nova_a, nova_b, nova_c, nova_d = distratores[0], distratores[1], distratores[2], distratores[3]

        questoes_balanceadas.append((
            num, hab, dif, enunciado, nova_a, nova_b, nova_c, nova_d, nova_e, gabarito_desejado, resolucao
        ))

    return questoes_balanceadas

def auditar_blacklist(questoes):
    blacklist = [
        r'epistemol[oó]gic', r'ontol[oó]gic', r'teleol[oó]gic', r'dicotomi',
        r'intr[ií]nsec', r'extr[ií]nsec', r'subjacente', r'ef[eê]mer',
        r'prerrogativa', r'prescind', r'imprescind', r'corrobor',
        r'hegem[oô]nic', r'mitigar', r'fomentar', r'proped[eê]utic',
        r'inexor', r'axiol[oó]gic', r'hermen[eê]utic', r'mormente', r'prec[ií]pu',
        r'R\$'
    ]

    erros = []
    for q in questoes:
        num = q[0]
        texto_completo = " ".join([str(x) for x in q[3:]])
        for termo in blacklist:
            if re.search(termo, texto_completo, re.IGNORECASE):
                erros.append(f"Questão {num}: termo proibido '{termo}' encontrado!")
    return erros

def gerar_arquivo_markdown(questoes, output_path):
    linhas = []
    linhas.append("---")
    linhas.append('série: "Ensino Médio"')
    linhas.append('disciplina: "Filosofia"')
    linhas.append('eixo: "Eixo IV: Estética, Filosofia da Arte e Poéticas da Negritude"')
    linhas.append('capitulo: "Capítulo 25: Mímesis e Catarse: A Filosofia da Arte na Grécia Antiga"')
    linhas.append('objeto_de_conhecimento: "O conceito grego de aisthesis e tekhne, a crítica e a expulsão dos poetas em Platão (imitação da imitação), a reabilitação da mímesis e a teoria da catarse trágica em Aristóteles"')
    linhas.append('ebook_fonte: "em-fil-c25-estetica-antiga-mimesis-catarse.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS301"')
    linhas.append('  - "EM13CHS302"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: Mímesis e Catarse: A Filosofia da Arte na Grécia Antiga\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-25-estetica-antiga-mimesis-catarse -->"
        linhas.append(tag_html)
        linhas.append(f"### Questão {num}\n")
        linhas.append(f"{enunciado}\n")
        linhas.append(f"A) {a}")
        linhas.append(f"B) {b}")
        linhas.append(f"C) {c}")
        linhas.append(f"D) {d}")
        linhas.append(f"E) {e}\n")
        linhas.append(f"**Gabarito:** ({gab})\n")
        linhas.append(f"**Resolução Comentada:**\n{res}\n")

    linhas.append("## Referências\n")
    linhas.append("- PLATÃO. *A República: Livro X*. Tradução de Anna Lia Amaral de Almeida Prado. São Paulo: Martins Fontes, 2006.")
    linhas.append("- ARISTÓTELES. *Poética*. Tradução de Eudoro de Sousa. São Paulo: Abril Cultural, 1979.")
    linhas.append("- DUARTE, Rodrigo. *Teoria dos sentidos: uma introdução à estética*. Belo Horizonte: Editora UFMG, 2017.")
    linhas.append("- JAEGER, Werner. *Paideia: a formação do homem grego*. Tradução de Artur M. Parreira. 4. ed. São Paulo: Martins Fontes, 2001.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo = "\n".join(linhas) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(conteudo)

def main():
    brutas = build_exercicios()
    print(f"Total de questões brutas: {len(brutas)}")

    erros = auditar_blacklist(brutas)
    if erros:
        print("\n[ERRO NA AUDITORIA DE TERMOS PROIBIDOS]:")
        for e in erros:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("[AUDITORIA INTERNA APROVADA] Nenhuma palavra da blacklist pedagógica encontrada!")

    balanceadas = balancear_e_gerar_markdown(brutas)

    letras = [q[9] for q in balanceadas]
    contagem = Counter(letras)
    print(f"Contagem por letra no gabarito: {contagem}")
    assert all(contagem[k] == 12 for k in ['A', 'B', 'C', 'D', 'E']), "Gabarito desbalanceado!"

    temp_draft = "temp_draft.md"
    gerar_arquivo_markdown(balanceadas, temp_draft)

    import os
    tamanho = os.path.getsize(temp_draft)
    print(f"Rascunho salvo em {temp_draft} ({tamanho} bytes)")

    destino_final = "content/medio/volume-unico/filosofia/eixo-4-estetica/cap-25-estetica-antiga-mimesis-catarse/ebooks/em-fil-c25-estetica-antiga-mimesis-catarse-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 25 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
