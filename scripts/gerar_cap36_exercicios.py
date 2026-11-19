# -*- coding: utf-8 -*-
"""
Script de Geração e Homologação das 60 Questões de Filosofia EM - Capítulo 36
Objeto: Afroperspectividade e Filosofia Negra Brasileira
E-book Fonte: em-fil-c36-afroperspectividade-filosofia-brasileira-noguera-flor.md
Padrão: 60 questões (20 B / 20 I / 20 D) | 12 A, 12 B, 12 C, 12 D, 12 E | Closed-World
"""

import re
import sys
import subprocess
from collections import Counter

def build_exercicios():
    questoes_brutas = []

    # ==========================================
    # 20 QUESTÕES BÁSICAS (01 a 20)
    # ==========================================

    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Qual legislação federal brasileira promulgada em 2003 tornou obrigatório o ensino da História e Cultura Afro-Brasileira e Africana?",
        [
            ("A Lei Federal nº 10.639/2003, impulsionando a descolonização dos currículos escolares e acadêmicos no país.", True),
            ("A Lei Áurea de 1888, que aboliu a escravidão formal sem criar mecanismos de assistência ou inclusão aos libertos.", False),
            ("O Código Civil de 1916, que regulamentou a posse da terra segundo os interesses de proprietários rurais do café.", False),
            ("A Consolidação das Leis do Trabalho de 1943, que estruturou os direitos dos operários fabris urbanos.", False),
            ("A Lei de Terras de 1850, que proibiu o acesso à terra pública por meio da posse direta e do cultivo familiar.", False)
        ],
        "A Lei nº 10.639/2003 alterou a LDB, tornando obrigatório o estudo das matrizes civilizatórias africanas e afro-brasileiras na educação."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Em qual obra de 2014 o filósofo Renato Noguera sistematizou a reflexão sobre o ensino de filosofia afro-brasileira?",
        [
            ("O Ensino de Filosofia e a Lei 10.639, obra pioneira dedicada à fundamentação teórica da Afroperspectividade.", True),
            ("A Ética Protestante e o Espírito do Capitalismo, ensaio clássico sobre a ascese religiosa na Europa ocidental.", False),
            ("O Contrato Social, tratado iluminista em que se defende a soberania popular e a vontade geral dos cidadãos.", False),
            ("Meditações Metafísicas, onde se formula a dúvida hiperbólica e a existência da substância pensante cartesiana.", False),
            ("Discurso sobre o Método, guia racionalista para o correto encaminhamento da razão nas ciências naturais.", False)
        ],
        "Renato Noguera publicou O Ensino de Filosofia e a Lei 10.639 em 2014, assentando os pilares da Afroperspectividade."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "De acordo com Renato Noguera, qual é o princípio da Afroperspectividade no debate filosófico contemporâneo?",
        [
            ("Partir da experiência histórica e cósmica africana e de sua diáspora para produzir conceitos críticos universais para a humanidade.", True),
            ("Exigir a destruição de bibliotecas públicas para impedir que estudantes tenham acesso a livros de geometria grega antiga.", False),
            ("Limitar a reflexão teórica exclusivamente a indivíduos nascidos em comunidades quilombolas do nordeste brasileiro.", False),
            ("Subordinar a pesquisa científica a horóscopos elaborados por sociedades de astrologia mercantil de grandes capitais.", False),
            ("Defender que apenas os povos de língua inglesa possuem a faculdade intelectual de criar teorias de física quântica.", False)
        ],
        "A Afroperspectividade parte das experiências das populações negras diaspóricas para gerar saberes e conceitos universais abertos a todos."
    ))

    questoes_brutas.append((
        4, "EM13CHS502", "basico",
        "No ensaio clássico de 2018, qual conceito central é denunciado pelo filósofo Wanderson Flor do Nascimento nas universidades?",
        [
            ("O racismo epistêmico, que desqualifica saberes não europeus como mero folclore ou mito desprovido de rigor.", True),
            ("O monopólio comercial da borracha, que concentrou riquezas nas mãos de industriais do extremo oriente moderno.", False),
            ("A física quântica probabilística, que substituiu o determinismo mecânico nas pesquisas sobre o átomo.", False),
            ("O protecionismo alfandegário, que elevou as taxas tributárias sobre a importação de trigo em portos marítimos.", False),
            ("A teoria dos climas temperados, que explicava as diferenças culturais com base no regime de chuvas sazonais.", False)
        ],
        "Wanderson Flor do Nascimento combate o racismo epistêmico, que recusa a validade de saberes filosóficos africanos e ameríndios."
    ))

    questoes_brutas.append((
        5, "EM13CHS504", "basico",
        "Qual orixá é alçado à condição de categoria conceitual na filosofia da encruzilhada formulada pelo pensamento afro-brasileiro?",
        [
            ("Exu (Èṣù), o princípio cósmico da comunicação, do movimento vital, da linguagem e da multiplicidade de caminhos.", True),
            ("Apolo, o deus grego da ordem geométrica luminosa, da moderação da forma plástica e da beleza clássica.", False),
            ("Netuno, a divindade romana associada ao domínio dos cavalos selvagens e ao fluxo das marés marítimas salgadas.", False),
            ("Marte, a divindade guerreira cultuada por legiões imperiais para assegurar vitórias em campanhas de cerco.", False),
            ("Vulcano, o ferreiro celestial encarregado de forjar armaduras de bronze nas fornalhas de vulcões terrestres.", False)
        ],
        "A filosofia afro-brasileira resgata Exu como categoria maior: o princípio do dinamismo, da mediação dialógica e do trânsito na encruzilhada."
    ))

    questoes_brutas.append((
        6, "EM13CHS606", "basico",
        "Na cosmovisão iorubá resgatada por Noguera e Flor, por qual razão a figura de Exu não pode ser confundida com o diabo?",
        [
            ("Porque as matrizes civilizatórias africanas desconhecem o maniqueísmo que opõe um Bem Absoluto a um Mal Absoluto.", True),
            ("Porque as leis das cortes romanas exigiam que os sacerdotes pagãos prestassem juramentos de lealdade ao imperador.", False),
            ("Porque os tratados de paz medievais proibiram a publicação de sermões religiosos nos centros urbanos da Europa.", False),
            ("Porque os concílios eclesiásticos ocidentais decretaram que todas as divindades da antiguidade eram anjos celestes.", False),
            ("Porque as assembleias cívicas gregas realizavam cerimônias de consagração de templos com corridas atléticas descalças.", False)
        ],
        "Exu não é o diabo cristão; na cosmovisão africana não há divisão moral rígida entre bem e mal absolutos, mas ambivalência e movimento vital."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "O que simboliza a encruzilhada como categoria de pensamento na filosofia brasileira contemporânea?",
        [
            ("O lugar de encontro de múltiplos caminhos, de mediação dialógica, de tradução de saberes e de superação do binarismo.", True),
            ("A divisa administrativa que delimita as fronteiras territoriais de municípios rurais em mapas geográficos oficiais.", False),
            ("O cruzamento de trilhos de ferro onde operários realizam a lubrificação mecânica de vagões de trens cargueiros.", False),
            ("A bifurcação de dutos subterrâneos de concreto destinados ao escoamento pluvial em capitais metropolitanas.", False),
            ("A barreira aduaneira onde fiscais do governo apreendem mercadorias contrabandeadas desprovidas de selo fiscal.", False)
        ],
        "A encruzilhada é o espaço conceitual onde caminhos diversos se cruzam, recusando a rota única dogmática e acolhendo a multiplicidade."
    ))

    questoes_brutas.append((
        8, "EM13CHS102", "basico",
        "Na obra Cosmovisão Africana no Brasil (2007), qual filósofo baiano desenvolveu os fundamentos da Filosofia da Ancestralidade?",
        [
            ("Eduardo David de Oliveira e Silva, concebendo a ancestralidade como princípio estruturante da vida comunitária.", True),
            ("Caio Prado Júnior, investigando a formação econômica e a exploração do sentido da colonização do litoral.", False),
            ("Gilberto Freyre, formulando a tese do luso-tropicalismo e da miscigenação harmoniosa no meio canavieiro.", False),
            ("Sérgio Buarque de Holanda, cunhando a categoria do homem cordial nas raízes da identidade nacional brasileira.", False),
            ("Raimundo Faoro, dissecando o patrimonialismo e a dominação do estamento burocrático na história do país.", False)
        ],
        "Eduardo de Oliveira e Silva formulou a Filosofia da Ancestralidade, demonstrando que os antepassados são princípio vivo de coesão ética."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "Na obra clássica O Terreiro e a Cidade (1988), qual função civilizatória Muniz Sodré atribui aos terreiros de candomblé?",
        [
            ("A de verdadeiros quilombos urbanos que preservam práticas de partilha, acolhimento comunitário e circulação de axé.", True),
            ("A de cooperativas financeiras que cobram juros bancários sobre empréstimos concedidos a pequenos comerciantes.", False),
            ("A de corporações burocráticas encarregadas do recenseamento demográfico de imigrantes europeus na capital.", False),
            ("A de academias de ginástica dedicadas à preparação atlética de competidores para torneios esportivos locais.", False),
            ("A de tribunais de arbitragem mercantil para a resolução de disputas contratuais entre companhias de navegação.", False)
        ],
        "Muniz Sodré demonstra que o terreiro atua como quilombo urbano, preservando a dádiva e a solidariedade contra o individualismo do mercado."
    ))

    questoes_brutas.append((
        10, "EM13CHS502", "basico",
        "Qual antropóloga e filósofa brasileira cunhou a categoria de Amefricanidade para resgatar a presença negra e indígena nas Américas?",
        [
            ("Lélia Gonzalez, integrando a denúncia do racismo, do sexismo e do colonialismo em uma perspectiva continental.", True),
            ("Anita Garibaldi, ao empunhar espadas em batalhas travadas nas províncias do sul durante o período regencial.", False),
            ("Tarsila do Amaral, ao pintar quadros que retratavam a vegetação tropical de fazendas cafeeiras do interior paulista.", False),
            ("Chiquinha Gonzaga, ao criar partituras para operetas e reger conjuntos instrumentais em teatros municipais.", False),
            ("Cecília Meireles, ao publicar versos poéticos e crônicas jornalísticas sobre as belezas das cidades históricas.", False)
        ],
        "Lélia Gonzalez formulou a Amefricanidade e o Pretuguês, descolonizando a noção de América Latina ao revelar a matriz civilizatória negra e indígena."
    ))

    questoes_brutas.append((
        11, "EM13CHS504", "basico",
        "O que a intelectual Lélia Gonzalez designou como Pretuguês na formação da sociedade brasileira?",
        [
            ("A marca linguística viva e rítmica que a família banto e iorubá imprimiu na língua portuguesa falada no Brasil.", True),
            ("A adoção de vocabulário técnico de mineração introduzido por engenheiros britânicos no século dezenove.", False),
            ("O dialeto exclusivo utilizado por diplomatas nas reuniões solenes de tribunais internacionais de comércio.", False),
            ("A compilação de termos jurídicos em latim arcaico que os estudantes de direito decoravam para os concursos civis.", False),
            ("O sistema de sinais alfabéticos criado para a transmissão de mensagens cifradas através de fios telegráficos.", False)
        ],
        "O Pretuguês expressa a africanização da língua no Brasil: a melodia, a fonética e a estrutura banto e nagô que forjaram a fala nacional."
    ))

    questoes_brutas.append((
        12, "EM13CHS606", "basico",
        "Na teoria do ser da Afroperspectividade concebida por Noguera, como é definida a natureza da existência humana?",
        [
            ("Como energia vital em relação dinâmica com o outro, a comunidade, os antepassados e a natureza viva cósmica.", True),
            ("Como um átomo isolado e egoísta cuja única finalidade é maximizar ganhos monetários em contratos mercantis.", False),
            ("Como uma máquina mecânica programada por engrenagens metálicas movidas pela pressão de vapor d'água.", False),
            ("Como uma substância incorpórea que paira nas nuvens sem manter contato com as tarefas terrenas do dia a dia.", False),
            ("Como um número estatístico gerado por computadores fiscais para orientar o recolhimento de tributos públicos.", False)
        ],
        "Na visão afroperspectivada, o ser não é indivíduo fechado; nós somos nossas relações vitais com a comunidade e com a ancestralidade."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "De que maneira a Afroperspectividade compreende a tradição da oralidade em contraste com os preconceitos do eurocentrismo?",
        [
            ("Como uma alta tecnologia da memória e da palavra, onde o corpo, o ritmo e a escuta transmitem saberes densos.", True),
            ("Como uma fraqueza cognitiva de povos que não desenvolveram a capacidade mental de organizar pensamentos lógicos.", False),
            ("Como um hábito infantil que deve ser erradicado das salas de aula através de castigos corporais severos.", False),
            ("Como uma forma primitiva de comunicação que desaparece obrigatoriamente com a introdução do rádio comercial.", False),
            ("Como uma prática passageira utilizada unicamente para distrair trabalhadores rurais após a colheita do café.", False)
        ],
        "A oralidade é alta tecnologia da palavra e da memória ancestral: o corpo e o ritmo decodificam e transmitem saberes éticos e comunitários profundos."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Qual projeto pioneiro de extensão coordenado por Renato Noguera na Baixada Fluminense levou a Afroperspectividade às escolas?",
        [
            ("Filosofia com Crianças em Perspectiva Afrodiaspórica, utilizando contos ancestrais e mitos de orixás na infância.", True),
            ("Competições de natação em piscinas olímpicas para treinamento físico de cadetes das forças armadas da nação.", False),
            ("Exames de memorização de tabelas de logaritmos decimais aplicados em colégios confessionais da capital.", False),
            ("Projetos de cultivo de cana-de-açúcar em estufas laboratoriais para testes de resistência a secas sazonais.", False),
            ("Feiras de venda de automóveis importados organizadas por consórcios empresariais em estacionamentos públicos.", False)
        ],
        "Noguera coordenou o projeto 'Filosofia com Crianças em Perspectiva Afrodiaspórica', descolonizando a infância e valorizando a imaginação ética."
    ))

    questoes_brutas.append((
        15, "EM13CHS501", "basico",
        "Em 2019, qual decisão histórica do Supremo Tribunal Federal (RE 494.601) protegeu a liberdade litúrgica de matriz africana?",
        [
            ("A declaração de constitucionalidade dos rituais religiosos tradicionais dos terreiros, combatendo o preconceito racista.", True),
            ("A proibição do funcionamento de templos religiosos em cidades com mais de cem mil habitantes no litoral.", False),
            ("A imposição de tributos fiscais extraordinários sobre doações em dinheiro recebidas por casas de caridade.", False),
            ("A censura judicial prévia a livros didáticos de sociologia que fizessem referências a revoltas do período colonial.", False),
            ("A cassação de registros civis de sacerdotes que não possuíssem diplomas de pós-graduação em universidades reais.", False)
        ],
        "O STF reconheceu no RE 494.601 a constitucionalidade e a legitimidade dos ritos de terreiro, protegendo a diversidade e a liberdade de crença."
    ))

    questoes_brutas.append((
        16, "EM13CHS502", "basico",
        "Qual revolta escrava ocorrida em Salvador em 1835 desmente o mito da passividade negra através de lideranças alfabetizadas em árabe?",
        [
            ("A Revolta dos Malês, conspiração organizada por negros escravizados e libertos que afirmaram sua soberania e dignidade.", True),
            ("A Guerra dos Emboabas, disputa armada entre bandeirantes paulistas e forasteiros pela posse das lavras de ouro.", False),
            ("A Revolta de Beckman, motim de proprietários de terras do Maranhão contra o monopólio comercial da companhia real.", False),
            ("A Cabanagem, levante popular no Grão-Pará em torno da posse de terras ribeirinhas nas margens da bacia amazônica.", False),
            ("A Sabinada, rebelião militar de setores da classe média baiana que pretendiam proclamar uma república provisória.", False)
        ],
        "A Revolta dos Malês (1835) foi liderada por negros muçulmanos alfabetizados em árabe, desmascarando a farsa da docilidade escrava."
    ))

    questoes_brutas.append((
        17, "EM13CHS504", "basico",
        "O que Wanderson Flor do Nascimento quer dizer com a expressão provincianizar a Europa no ensino da filosofia?",
        [
            ("Reconhecer que a tradição europeia é regional e particular, e não a única ou exclusiva portadora da razão universal.", True),
            ("Obrigar os países da Europa ocidental a adotarem códigos de leis formulados por assembleias tribais da Oceania.", False),
            ("Proibir que os livros de autores franceses ou alemães sejam traduzidos para a língua portuguesa contemporânea.", False),
            ("Exigir a demolição das catedrais góticas medievais para a ampliação de rodovias de tráfego de caminhões de carga.", False),
            ("Suspender as trocas comerciais internacionais entre os portos brasileiros e os centros industriais da Europa.", False)
        ],
        "Provincianizar a Europa significa destroná-la de seu pedestal universal arrogante: o pensamento europeu é regional, assim como os outros são legítimos."
    ))

    questoes_brutas.append((
        18, "EM13CHS606", "basico",
        "Por que a Filosofia da Ancestralidade de Eduardo de Oliveira recusa que o indivíduo moderno tenha se feito sozinho?",
        [
            ("Porque compreende que nossa existência atual é fruto vivo do trabalho, da luta e da energia dos que vieram antes.", True),
            ("Porque as sinapses elétricas do cérebro são acionadas unicamente pela repetição de mensagens transmitidas por rádio.", False),
            ("Porque os códigos municipais de trânsito exigem que os pedestres circulem acompanhados por familiares mais velhos.", False),
            ("Porque o sistema bancário bloqueia as contas financeiras de cidadãos que não apresentam comprovantes de residência.", False),
            ("Porque as academias de ciências médicas proíbem a ingestão de medicamentos que não sejam prescritos por três médicos.", False)
        ],
        "A ancestralidade ensina a humildade: somos sustentados pelas raízes e pelas lutas históricas dos antepassados que permitiram nossa vida."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Ao dialogar com a Pedagogia do Oprimido de Paulo Freire, como a filosofia afro-brasileira concebe a sala de aula?",
        [
            ("Como uma encruzilhada viva de saberes onde educadores e educandos compartilham memórias e produzem libertação.", True),
            ("Como um tribunal inquisitorial militar onde os alunos permanecem imóveis ouvindo sentenças condenatórias diárias.", False),
            ("Como uma linha de montagem fabril onde mentes jovens são moldadas mecanicamente para a execução de tarefas cegas.", False),
            ("Como um cofre bancário hermético onde dados abstratos são armazenados sem qualquer conexão com a vida comunitária.", False),
            ("Como um monastério isolado no alto de montanhas onde se proíbe o contato com os conflitos políticos da cidade.", False)
        ],
        "A sala de aula afroperspectivada é uma encruzilhada de trocas dialógicas, onde o conhecimento liberta a comunidade em aliança com Paulo Freire."
    ))

    questoes_brutas.append((
        20, "EM13CHS102", "basico",
        "Em síntese, qual é o papel da Filosofia Afro-Brasileira para o conjunto dos estudantes da Educação Básica no Brasil?",
        [
            ("Superar o racismo estrutural e enriquecer o pensamento crítico com matrizes conceituais plurais e descolonizadas.", True),
            ("Substituir o aprendizado da língua nacional por dialetos arcaicos falados apenas em cortes principescas antigas.", False),
            ("Determinar que as escolas de ensino médio suspendam os laboratórios de química em favor de aulas de marcha marcial.", False),
            ("Impor que todas as decisões acadêmicas sejam tomadas exclusivamente por representantes de corporações financeiras.", False),
            ("Proibir o diálogo crítico entre diferentes correntes teóricas nas disciplinas da área de Ciências Humanas.", False)
        ],
        "A Filosofia Afro-Brasileira democratiza a inteligência coletiva, superando preconceitos e oferecendo conceitos poderosos para a cidadania plena."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Na crítica de Wanderson Flor do Nascimento à universidade, qual mecanismo preserva os privilégios da branquitude acadêmica?",
        [
            ("A desqualificação sumária de pensadores africanos como se fossem apenas temas de antropologia ou religião exótica.", True),
            ("O incentivo irrestrito à concessão de bolsas de pesquisa para estudantes matriculados em universidades do terceiro mundo.", False),
            ("A exigência de que os comitês de ética em pesquisa publiquem seus pareceres em jornais de grande circulação nacional.", False),
            ("A obrigatoriedade de que os corpos docentes realizem estágios regulares de trabalho manual em fábricas automotivas.", False),
            ("A isenção universal de tarifas de energia elétrica concedida aos prédios administrativos de fundações universitárias.", False)
        ],
        "O racismo acadêmico protege a branquitude ao empurrar a filosofia africana para fora do cânone conceitual legítimo, rotulando-a de exotismo."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "No célebre provérbio iorubá sobre Exu atirar a pedra hoje e matar o pássaro ontem, qual desafio filosófico é colocado à temporalidade?",
        [
            ("A desestabilização da linearidade mecânica ocidental, afirmando que a ação presente pode ressignificar e transformar o passado.", True),
            ("A comprovação matemática de que as leis da termodinâmica permitem viagens de navios a vapor no vácuo interestelar.", False),
            ("A exigência de que os tribunais civis cancelem os registros de nascimento de cidadãos que viajam para o exterior.", False),
            ("A defesa de que o movimento das marés marítimas é provocado pelo magnetismo de satélites artificiais em órbita baixa.", False),
            ("A imposição de toques de recolher noturnos para conter o comércio ilegal de relógios mecânicos em feiras livres.", False)
        ],
        "O provérbio mostra uma cosmologia temporal dinâmica: o tempo não é seta rígida; pela memória e pela práxis presente, podemos curar e reinventar o passado."
    ))

    questoes_brutas.append((
        23, "EM13CHS501", "intermediario",
        "Na dimensão da teoria do conhecimento da Afroperspectividade, por que Noguera rejeita a divisão hierárquica entre mito e filosofia?",
        [
            ("Porque demonstra que o mito expressa uma sabedoria poética e conceitual sofisticada de ordenação ética da vida comunitária.", True),
            ("Porque considera que as ciências exatas modernas cometeram fraudes sistemáticas em suas formulações matemáticas.", False),
            ("Porque propõe que as pesquisas laboratoriais sejam substituídas por leituras de folhas de chá em reuniões fechadas.", False),
            ("Porque defende que a escrita alfabética deve ser proibida em editoras comerciais para proteger a indústria de pergaminhos.", False),
            ("Porque afirma que os fenômenos astronômicos decorrem unicamente da vontade de monarcas de dinastias da Mesopotâmia.", False)
        ],
        "Noguera demonstra que o mito é uma sofisticada tecnologia de sentido e ética; a separação eurocêntrica entre mito e razão foi criada para rebaixar os outros saberes."
    ))

    questoes_brutas.append((
        24, "EM13CHS502", "intermediario",
        "Em que medida a categoria de Amefricanidade formulada por Lélia Gonzalez subverte a dominação imperialista nas ciências sociais?",
        [
            ("Desfazendo a falsa homogeneidade da América Latina e revelando que a matriz afro-ameríndia é a base viva das sociedades do continente.", True),
            ("Propondo a construção de muros marítimos para impedir o intercâmbio de estudantes entre universidades de países vizinhos.", False),
            ("Defendendo a censura prévia de transmissões de notícias internacionais em canais públicos de televisão educativa.", False),
            ("Exigindo a padronização dos impostos aduaneiros cobrados sobre a exportação de minérios de ferro em portos fluviais.", False),
            ("Condicionando a realização de conferências acadêmicas à prévia aprovação de comissões militares de fronteira.", False)
        ],
        "Lélia desconstrói a farsa da 'América Latina' branca e burguesa: a verdadeira identidade continental é Améfrica Ladina, forjada por negras e indígenas."
    ))

    questoes_brutas.append((
        25, "EM13CHS504", "intermediario",
        "Ao investigar a forma social do terreiro em Muniz Sodré, qual modelo de economia moral contrapõe-se à ganância capitalista?",
        [
            ("A circulação solidária da dádiva e do axé, onde a riqueza é medida pela capacidade de acolhimento e partilha coletiva.", True),
            ("A acumulação privada de barras de ouro guardadas em cofres subterrâneos imunes a vistorias fiscais do governo.", False),
            ("A venda de ações em bolsas de valores eletrônicas para financiar a compra de máquinas agrícolas de grande porte.", False),
            ("A cobrança de mensalidades contratuais compulsórias aos frequentadores para garantir a remuneração de advogados civis.", False),
            ("O incentivo à concorrência comercial agressiva com a falência forçada de pequenos estabelecimentos vizinhos do bairro.", False)
        ],
        "No terreiro estudado por Muniz Sodré, o acúmulo individualista é vergonhoso; o valor supremo é a partilha de comida, de acolhimento e de energia vital."
    ))

    questoes_brutas.append((
        26, "EM13CHS606", "intermediario",
        "Na atuação no Supremo Tribunal Federal no julgamento do RE 494.601, qual argumento desmantelou o preconceito contra os terreiros?",
        [
            ("O reconhecimento de que as liturgias de matriz africana constituem patrimônio cultural e gozam de proteção constitucional de fé.", True),
            ("A determinação de que todos os templos religiosos devem pagar impostos prediais diretamente às prefeituras municipais.", False),
            ("A proibição da exibição pública de símbolos religiosos em comícios políticos ou manifestações sindicais das capitais.", False),
            ("A exigência de que os sacerdotes apresentem registros de antecedentes criminais a cada trimestre civil aos tribunais.", False),
            ("A concessão de autorização de funcionamento condicionada ao pagamento de taxas de vigilância sanitária a hospitais.", False)
        ],
        "O STF consagrou que os ritos de terreiro são expressões ancestrais legítimas amparadas pela liberdade de crença e pela diversidade cultural da nação."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "Por qual motivo Renato Noguera destaca a infância como uma potência teórica e ética privilegiada na Afroperspectividade?",
        [
            ("Porque as crianças experimentam o mundo com imaginação aberta, capacidade de espanto e recusa de preconceitos enrijecidos.", True),
            ("Porque os estudantes dos primeiros anos do ensino fundamental possuem maior resistência física a caminhadas sob o sol.", False),
            ("Porque as legislações trabalhistas autorizavam o emprego de menores de idade em tecelagens manuais no período monárquico.", False),
            ("Porque as crianças conseguem memorizar declinações gramaticais em latim com maior rapidez que os adultos nas capitais.", False),
            ("Porque as escolas municipais oferecem merendas balanceadas que aumentam a acuidade visual dos alunos nas salas de aula.", False)
        ],
        "A infância na Afroperspectividade é força criadora: a criança interroga, inventa e problematiza o mundo com uma liberdade que desmancha preconceitos."
    ))

    questoes_brutas.append((
        28, "EM13CHS102", "intermediario",
        "Ao articular Exu e o trânsito entre o Aiyê e o Orun, qual lição sobre a relação entre o visível e o invisível é oferecida?",
        [
            ("A realidade não se esgota na matéria imediata do mercado, existindo uma conexão viva e contínua com a dimensão ancestral.", True),
            ("As transações comerciais realizadas por vias digitais dispensam a assinatura de contratos impressos em papel selado.", False),
            ("Os astros celestes giram em torno de um núcleo metálico denso localizado no centro geográfico do oceano pacífico.", False),
            ("A visibilidade dos corpos físicos depende da refração da luz solar em partículas de poeira suspensas nas florestas.", False),
            ("Os tribunais internacionais proíbem que testemunhas de processos criminais façam declarações sem o auxílio de tradutores.", False)
        ],
        "Exu liga o Aiyê (o mundo terreno vivo) ao Orun (o mundo ancestral); essa mediação lembra que a existência humana é permeada pelo respeito à ancestralidade."
    ))

    questoes_brutas.append((
        29, "EM13CHS501", "intermediario",
        "Sob quais aspectos a denúncia de Sueli Carneiro ao epistemicídio conecta-se à descolonização da filosofia brasileira contemporânea?",
        [
            ("Denunciando o silenciamento e a destruição sistemática da capacidade intelectual dos povos negros pela dominação eurocêntrica.", True),
            ("Defendendo a extinção de todas as bibliotecas municipais para reduzir os custos orçamentários das secretarias de cultura.", False),
            ("Afirmando que o desenvolvimento tecnológico depende exclusivamente da importação de turbinas eólicas da Escandinávia.", False),
            ("Propondo a revogação de leis trabalhistas para estimular a concorrência sem regras entre trabalhadores de indústrias têxteis.", False),
            ("Sustentando que os conflitos políticos entre cidades vizinhas devem ser mediados por comitês de árbitros comerciais privados.", False)
        ],
        "O epistemicídio de Sueli Carneiro nomeia o assassinato cultural e intelectual dos povos negros; a Filosofia Afro-Brasileira repara essa injustiça histórica."
    ))

    questoes_brutas.append((
        30, "EM13CHS502", "intermediario",
        "Na análise de Roger Bastide e Pierre Verger, qual aspecto da travessia atlântica revela a força da resistência cultural africana?",
        [
            ("A recriação minuciosa na Bahia de rituais, cantos sagrados e conhecimentos botânicos do antigo Reino do Daomé e de Iorubalândia.", True),
            ("A assinatura de tratados de livre navegação fluvial entre marinheiros franceses e governantes monárquicos da Europa.", False),
            ("A introdução de técnicas de mineração de carvão mineral por engenheiros formados em academias militares estrangeiras.", False),
            ("A criação de sociedades anônimas de comércio para o transporte de trigo em sacos impermeáveis através dos oceanos.", False),
            ("A cobrança de pedágios marítimos em portos coloniais para financiar a construção de fortificações de defesa militar costeira.", False)
        ],
        "Bastide e Verger documentaram como as populações escravizadas recriaram a África no Brasil, preservando deuses, botânica, cantos e saberes contra o cativeiro."
    ))

    questoes_brutas.append((
        31, "EM13CHS504", "intermediario",
        "Por qual razão a proposta de descolonização de Wanderson Flor do Nascimento não significa isolamento ou rejeição aos autores europeus?",
        [
            ("Porque busca construir uma ecologia de saberes onde diferentes tradições dialoguem de modo simétrico e sem dominações opressoras.", True),
            ("Porque exige que os professores universitários utilizem uniformes civis padronizados durante conferências no exterior.", False),
            ("Porque propõe a unificação de todas as moedas nacionais em uma única unidade monetária administrada por bancos centrais.", False),
            ("Porque defende que os exames de vestibular cobrem exclusivamente questões de cálculo diferencial e equações de segundo grau.", False),
            ("Porque proíbe a realização de pesquisas acadêmicas sobre temas que não tenham sido aprovados por decretos ministeriais.", False)
        ],
        "A ecologia de saberes não joga Kant ou Nietzsche fora; ela destrói o monopólio arrogante da Europa, colocando o pensamento africano no mesmo patamar de dignidade."
    ))

    questoes_brutas.append((
        32, "EM13CHS606", "intermediario",
        "Na perspectiva de Eduardo de Oliveira e Silva, como a morte é ressignificada na cosmovisão da ancestralidade?",
        [
            ("A morte não é aniquilação definitiva no nada, mas passagem para o Orun e permanência viva como guia e memória da comunidade.", True),
            ("A morte é um erro biológico provocado pela falta de vitaminas solúveis nas refeições diárias de operários industriais.", False),
            ("A morte decorre de variações gravitacionais provocadas pela aproximação de cometas luminosos na órbita terrestre.", False),
            ("A morte é um fenômeno ilusório inventado por companhias funerárias mercantis para vender jazigos em cemitérios urbanos.", False),
            ("A morte pode ser evitada por meio de exercícios de ginástica cardiovascular praticados em parques públicos municipais.", False)
        ],
        "Na Filosofia da Ancestralidade, o ancestral continua vivo na memória e no axé comunitário: a morte física é travessia e não anulação do ser."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Na análise da Revolta dos Malês sob a lente da Afroperspectividade, qual mito historiográfico colonial é pulverizado?",
        [
            ("O mito da passividade e ignorância dos escravizados, evidenciando sujeitos letrados que planejaram a tomada revolucionária da cidade.", True),
            ("A alegação de que a produção de açúcar dependia de instrumentos agrícolas importados de fundições da Europa central.", False),
            ("A crença de que as capitanias hereditárias foram divididas de acordo com o traçado de rios navegáveis do interior.", False),
            ("A tese de que a independência política do Brasil foi conquistada sem a realização de manifestações populares nas províncias.", False),
            ("A certeza de que as ordens religiosas da época possuíam o monopólio da fabricação de ligas de ferro nas colônias.", False)
        ],
        "Os Malês em 1835 provaram que o negro escravizado não era passivo nem ignorante: eram intelectuais, líderes políticos e estrategistas em armas."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "No debate sobre o racismo institucional, como Wanderson Flor do Nascimento caracteriza a violência silenciosa nas bancas acadêmicas?",
        [
            ("A recusa em orientar ou aprovar teses que utilizem matrizes teóricas africanas com a desculpa da suposta falta de rigor clássico.", True),
            ("O pagamento de salários diferenciados para professores com base no número de artigos publicados em periódicos científicos.", False),
            ("A exigência de que os candidatos a pós-graduações realizem exames de proficiência em língua inglesa ou francesa moderna.", False),
            ("A cobrança de taxas de matrícula para estudantes que não comprovam carência socioeconômica perante a universidade pública.", False),
            ("O cancelamento de eventos presenciais em virtude de manutenções elétricas nas salas de aula de faculdades federais.", False)
        ],
        "A violência epistêmica é sutil e institucional: comitês acadêmicos desqualificam a filosofia africana com a desculpa cínica de que 'falta rigor eurocêntrico'."
    ))

    questoes_brutas.append((
        35, "EM13CHS501", "intermediario",
        "De que forma a oralidade nas comunidades tradicionais de matriz africana atua como garantia de preservação de saberes filosóficos?",
        [
            ("Através da pedagogia do corpo, do respeito aos mestres mais velhos (griôs) e da transmissão viva de cantos, rezas e provérbios.", True),
            ("Por meio da distribuição de folhetos impressos com resumos esquemáticos de teorias sociológicas de pensadores do século passado.", False),
            ("Pela obrigatoriedade de que os jovens leiam compêndios de gramática latina antes de participarem de reuniões comunitárias.", False),
            ("Pelo registro notarial em cartórios civis de todas as decisões tomadas por conselhos administrativos de associações de bairro.", False),
            ("Pela transmissão mecânica de gravações de áudio através de autofalantes instalados em postes de praças públicas das cidades.", False)
        ],
        "A tradição oral é corpórea e viva: a voz dos anciãos, os provérbios e os cantos sagrados preservam a filosofia contra séculos de perseguição e apagamento."
    ))

    questoes_brutas.append((
        36, "EM13CHS502", "intermediario",
        "Ao confrontar o individualismo moderno, qual virtude comunitária é consagrada pela Filosofia da Ancestralidade?",
        [
            ("A coresponsabilidade ética, onde o indivíduo cuida do bem comum e honra o legado coletivo que sustenta a sua própria vida.", True),
            ("O isolamento social voluntário em fazendas rurais distantes de qualquer centro urbano ou rodovia de transporte.", False),
            ("A acumulação incessante de lucros comerciais por meio da exploração sem limites da mão de obra de camponeses vizinhos.", False),
            ("A submissão cega a ordens emitidas por magistrados togados de tribunais civis em disputas patrimoniais de herança.", False),
            ("O desprezo pelas decisões tomadas em assembleias populares de trabalhadores em prol do enriquecimento individualista rápido.", False)
        ],
        "A ancestralidade ensina a coresponsabilidade: ninguém existe como ilha; o indivíduo é responsável perante a comunidade e perante os que virão depois."
    ))

    questoes_brutas.append((
        37, "EM13CHS504", "intermediario",
        "Qual é a relação entre a sabedoria de Exu e a superação das certezas dogmáticas no ensino de Filosofia?",
        [
            ("Incentivar o pensamento questionador, a abertura ao diálogo entre saberes diferentes e a recusa de verdades estáticas e fechadas.", True),
            ("Obrigar os alunos a aceitarem sem questionamentos as normas disciplinares impostas por diretores de estabelecimentos de ensino.", False),
            ("Proibir a leitura de obras literárias que contenham personagens que expressem dúvidas a respeito de teorias científicas.", False),
            ("Determinar que as provas escolares sejam compostas exclusivamente por questões de memorização de datas cronológicas.", False),
            ("Exigir que os estudantes se filiem a agremiações partidárias antes de concluírem os créditos curriculares obrigatórios.", False)
        ],
        "Exu é a própria dúvida filosófica e a desordem criadora que desaloja o dogma: ele ensina a perguntar, a cruzar caminhos e a buscar a renovação contínua."
    ))

    questoes_brutas.append((
        38, "EM13CHS606", "intermediario",
        "Nas reflexões pedagógicas de Renato Noguera, como a infância se articula à construção de uma sociedade democrática e antirracista?",
        [
            ("Mostrando que educar crianças em perspectiva afrodiaspórica desfaz preconceitos na raiz e estimula o respeito à alteridade.", True),
            ("Comprovando que as crianças devem ser educadas sem contato com a arte para que se dediquem unicamente ao treinamento fabril.", False),
            ("Afirmando que a convivência escolar deve ser segregada por faixas de renda familiar para facilitar a gestão dos colégios.", False),
            ("Sustentando que os jovens devem memorizar manuais de conduta cívica militar antes de ingressarem em cursos universitários.", False),
            ("Defendendo que as brincadeiras coletivas ao ar livre devem ser substituídas por avaliações diárias de desempenho numérico.", False)
        ],
        "Trabalhar a infância com Afroperspectividade é semear o futuro: as crianças desconstroem estereótipos racistas e constroem pontes de afeto e respeito mútuo."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Em sua crítica à herança colonial nas universidades, qual advertência formulou Ramón Grosfoguel ao cânone ocidental?",
        [
            ("A denúncia de que as teorias sociais ocidentais universalizaram a experiência provinciana de homens brancos de quatro nações europeias.", True),
            ("A comprovação de que as universidades latino-americanas investiram recursos excessivos na publicação de pesquisas sobre astronomia.", False),
            ("A afirmação de que os estudantes de graduação devem realizar estágios de treinamento físico em academias esportivas navais.", False),
            ("A defesa de que as disciplinas de matemática deveriam ser ministradas em dialetos arcaicos de tribos da América Central.", False),
            ("A proposta de que os diplomas de cursos superiores fossem emitidos por cartórios civis sem a chancela de órgãos governamentais.", False)
        ],
        "Grosfoguel denuncia o cânone ocidental: uma tradição provinciana e masculina (Alemanha, França, Inglaterra, Itália) que pretendeu ser o modelo de toda a humanidade."
    ))

    questoes_brutas.append((
        40, "EM13CHS102", "intermediario",
        "Em síntese, como a Filosofia Afro-Brasileira contribui para a soberania intelectual e democrática do Brasil contemporâneo?",
        [
            ("Afirmando que o pensamento do país não deve ser mero importador passivo de teorias europeias, mas criador soberano de saberes emancipadores.", True),
            ("Propondo a extinção das relações diplomáticas com nações do hemisfério norte para evitar influências culturais estrangeiras.", False),
            ("Determinando que os cientistas sociais abandonem o uso de computadores digitais em favor de máquinas de escrever manuais antigas.", False),
            ("Restringindo o acesso às bibliotecas públicas exclusivamente a pesquisadores diplomados em universidades estrangeiras.", False),
            ("Sustentando que a história do Brasil deve ser ensinada a partir da exaltação exclusiva dos governadores-gerais do período colonial.", False)
        ],
        "A Filosofia Afro-Brasileira afirma a maioridade intelectual do Brasil: cria conceitos próprios a partir das dores e riquezas da nossa própria gente."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Em confronto com a metafísica ocidental, de que modo a teoria do ser em Noguera desafia o individualismo cartesiano e liberal?",
        [
            ("Definindo o ser como energia relacional viva e comunitária, onde a existência só se constitui no vínculo dinâmico com o outro e com o cosmos.", True),
            ("Sustentando que a alma humana é uma substância incorpórea solitária que governa o corpo como um piloto comanda um navio a vapor nas águas.", False),
            ("Afirmando que a essência dos seres humanos reside no acúmulo financeiro privado de bens imóveis registrado em cartórios civis municipais.", False),
            ("Provando que as emoções de medo e solidão decorrem da falta de vestimentas impermeáveis adequadas para caminhadas sob nevoeiros espessos.", False),
            ("Demonstrando que a consciência racional é programada geneticamente pela posição dos astros solares na hora do nascimento biológico.", False)
        ],
        "- **Etapa 1:** A tradição cartesiana e o liberalismo clássico concebem o indivíduo como uma mônada atômica autossuficiente e isolada que antecede a sociedade.\n- **Etapa 2:** Noguera opera o giro conceitual africano: o ser humano é relação e devir; não existo primeiro para me relacionar depois; existo porque sou tecido por vínculos comunitários com os vivos, os antepassados e a natureza, o que comprova a alternativa A."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Na filosofia da encruzilhada formulada por Wanderson Flor do Nascimento, de que maneira a figura de Exu desconstrói a lógica formal aristotélica?",
        [
            ("Subvertendo o princípio da não-contradição e do terceiro excluído ao afirmar a encruzilhada como território fecundo da ambivalência e da mediação.", True),
            ("Comprovando que as regras dos silogismos dedutivos foram redigidas por marinheiros fenícios para facilitar o cálculo de rotas marítimas.", False),
            ("Demonstrando que os paradoxos da linguagem lógica podem ser resolvidos unicamente pela aplicação de multas financeiras a debatedores.", False),
            ("Sustentando que as premissas verdadeiras dependem da temperatura ambiente registrada em termômetros de mercúrio nas salas de conferência.", False),
            ("Defendendo que a dialética deve ser abolida dos manuais escolares para garantir a uniformidade das sentenças proferidas por juízes civis.", False)
        ],
        "- **Etapa 1:** A lógica formal ocidental clássica (Aristóteles) fundamenta-se na rigidez binária: A é A e não pode ser não-A ao mesmo tempo e sob o mesmo aspecto.\n- **Etapa 2:** Exu encarna a encruzilhada: o ponto onde o sim e o não conversam e geram o novo; Exu é a mediação dialógica que habita as fronteiras, rompe o dogmatismo e abre o pensamento à fecundidade das transformações contínuas, validando a alternativa A."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Na crítica acadêmica descolonial, como a denúncia do racismo epistêmico desmascara a suposta neutralidade da universidade?",
        [
            ("Evidenciando que a universidade eurocêntrica confunde a sua tradição regional branca com a própria razão universal, silenciando saberes subalternizados.", True),
            ("Provando que os comitês de concessão de bolsas de pesquisa favorecem deliberadamente candidatos que residem em cidades litorâneas.", False),
            ("Demonstrando que as teses acadêmicas sobre botânica florestal utilizam vocabulário derivado de dialetos medievais sem tradução moderna.", False),
            ("Sustentando que as normas de formatação bibliográfica foram criadas por companhias de telégrafo para economizar papel nos escritórios.", False),
            ("Afirmando que a distribuição de recursos orçamentários ministeriais baseia-se exclusivamente no número de páginas de teses doutorais.", False)
        ],
        "- **Etapa 1:** As academias ocidentais historicamente se autoapresentaram como santuários desinteressados de 'conhecimento universal e neutro'.\n- **Etapa 2:** Wanderson Flor revela a engrenagem colonial: essa pretensa neutralidade é uma ficção política que universaliza os interesses da branquitude europeia enquanto desqualifica como 'não-filosofia' o pensamento refinado de africanos e indígenas, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        44, "EM13CHS502", "dificil",
        "Ao articular a Filosofia da Ancestralidade com a teoria do conhecimento, qual imperativo de humildade é colocado por Eduardo de Oliveira?",
        [
            ("A consciência lúcida de que o sujeito contemporâneo não é fundador autossuficiente do saber, mas herdeiro de uma cadeia viva de lutas e saberes acumulados.", True),
            ("A recomendação de que os estudantes universitários renunciem à autoria de pesquisas científicas para transferi-las a ordens monásticas.", False),
            ("A exigência de que os tratados de sociologia sejam redigidos sem a utilização de substantivos próprios para preservar o anonimato dos autores.", False),
            ("A proibição de que os pesquisadores citem fontes orais em artigos destinados a publicações em revistas acadêmicas especializadas.", False),
            ("A determinação de que os diplomas escolares contenham selos metálicos gravados com os brasões de armas de capitanias coloniais.", False)
        ],
        "- **Etapa 1:** O individualismo moderno e a arrogância acadêmica estimulam a ilusão do 'gênio solitário' que inventa a roda a partir de si mesmo.\n- **Etapa 2:** Eduardo de Oliveira resgata a ancestralidade: pensar com rigor exige honrar o solo fértil adubado pelo suor e pelo sofrimento dos antepassados; o saber legítimo é comunitário, compartilhado e reverente perante a história que nos permitiu estar aqui, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        45, "EM13CHS504", "dificil",
        "Na teoria social de Muniz Sodré, de que maneira o terreiro como quilombo urbano questiona os fundamentos da sociedade de mercado?",
        [
            ("Substituindo a lógica da acumulação privada e da mercadoria por uma forma civilizatória fundada na dádiva, na hospitalidade e na partilha sagrada do axé.", True),
            ("Comprovando que a produção artesanal de tecidos de algodão era mais lucrativa que a exportação de minérios de ferro no século vinte.", False),
            ("Defendendo a criação de bairros residenciais cercados por muralhas de pedra para evitar o trânsito de veículos automotores nas ruas.", False),
            ("Propondo a substituição das cédulas de papel-moeda por conchas marítimas em todas as transações comerciais do território nacional.", False),
            ("Afirmando que a convivência comunitária harmoniosa exige a celebração diária de contratos civis perante tabeliães de notas públicas.", False)
        ],
        "- **Etapa 1:** A ordem capitalista moderna assenta-se na propriedade privada, na monetarização de todas as esferas da vida e no egoísmo concorrencial.\n- **Etapa 2:** Muniz Sodré revela o terreiro como território de resistência viva: ali a riqueza não é reter dinheiro, mas fazer circular alimentos e acolhimento; o terreiro é um quilombo civilizatório que preserva uma ética da generosidade radical oposta à crueldade do mercado, consagrando a alternativa A."
    ))

    questoes_brutas.append((
        46, "EM13CHS606", "dificil",
        "Sob a ótica da Amefricanidade de Lélia Gonzalez, qual crítica contundente é dirigida ao conceito dominante de América Latina?",
        [
            ("A denúncia de que o termo América Latina opera um apagamento ideológico racista ao ocultar o papel central das populações negras e indígenas.", True),
            ("A alegação incorreta de que os países sul-americanos nunca assinaram tratados comerciais de cooperação aduaneira multilateral.", False),
            ("A comprovação de que as línguas neolatinas possuem estruturas gramaticais incompatíveis com a redação de tratados constitucionais modernos.", False),
            ("A afirmação de que a exploração agrícola de cana-de-açúcar foi realizada exclusivamente por trabalhadores imigrantes da Europa central.", False),
            ("A defesa de que as fronteiras geográficas entre as nações do continente devem ser redesenhadas segundo as bacias hidrográficas fluviais.", False)
        ],
        "- **Etapa 1:** A denominação 'América Latina' foi cunhada por elites francófonas e ibéricas para alinhar o continente ao legado imperial romano e europeu.\n- **Etapa 2:** Lélia Gonzalez explode essa máscara: a verdadeira formação histórica e cultural do continente não é puramente latina; ela é Améfrica Ladina, forjada no sangue, na língua (Pretuguês) e na resistência das mulheres negras e povos originários, legitimando a alternativa A."
    ))

    questoes_brutas.append((
        47, "EM13CHS101", "dificil",
        "Em relação à dívida histórica colonial, como a temporalidade não-linear da Afroperspectividade dialoga com a reparação da escravidão?",
        [
            ("Mostrando que a escravidão não é passado morto e sepultado, mas uma fratura viva que projeta desvantagens no presente exigindo ação reparadora contínua.", True),
            ("Afirmando que o tempo decorrido desde o século dezenove apagou automaticamente qualquer impacto material da escravidão nas cidades.", False),
            ("Sustentando que as reparações financeiras devem ser concedidas exclusivamente a descendentes de capitães de navios mercantes ingleses.", False),
            ("Provando que as leis de anistia política aprovadas no período republicano extinguiram os efeitos sociais do preconceito de cor nas escolas.", False),
            ("Defendendo que as pesquisas historiográficas sobre o cativeiro devem ser suspensas para não conturbar a concórdia cívica entre as classes.", False)
        ],
        "- **Etapa 1:** O pensamento positivista ocidental concebe o tempo como uma linha reta que deixa o passado definitivamente para trás como algo superado.\n- **Etapa 2:** Na temporalidade afroperspectivada, o passado habita as estruturas do presente; a dor e o roubo do trabalho escravo continuam operando no racismo estrutural contemporâneo; o ato reparador presente é o 'tiro de pedra hoje que acerta o pássaro de ontem', assegurando a alternativa A."
    ))

    questoes_brutas.append((
        48, "EM13CHS102", "dificil",
        "Ao investigar a relação entre Afroperspectividade e a infância, qual ruptura com a pedagogia tradicional bancária é proposta por Renato Noguera?",
        [
            ("Reconhecer a criança como sujeito pleno de saber e potência interrogadora, superando o modelo que a trata como tábula rasa a ser adestrada.", True),
            ("Obrigar os alunos das primeiras séries a realizarem exercícios diários de cópia manuscrita de verbetes de dicionários de língua inglesa.", False),
            ("Proibir a contação de histórias populares africanas para manter o foco exclusivo no aprendizado de equações aritméticas básicas.", False),
            ("Determinar que as atividades de recreação escolar sejam substituídas por treinamentos práticos de datilografia mecânica rápida.", False),
            ("Exigir que os estudantes prestem exames semanais de postura física militar perante comissões disciplinares de colégios públicos.", False)
        ],
        "- **Etapa 1:** A escola tradicional historicamente tratou a infância a partir da carência: a criança seria um ser incompleto e vazio que deve ser 'preenchido' pela ordem adulta.\n- **Etapa 2:** Noguera subverte esse paradigma: a infância é o solo originário da filosofia; em roda, as crianças problematizam o mundo e criam ética viva a partir dos mitos ancestrais, descolonizando o próprio conceito de conhecimento e educação, validando a alternativa A."
    ))

    questoes_brutas.append((
        49, "EM13CHS501", "dificil",
        "No âmbito do direito constitucional brasileiro, de que modo o julgamento do RE 494.601 expressa a vitória contra o racismo religioso?",
        [
            ("Desmontando a criminalização colonial dos ritos tradicionais e afirmando o princípio da laicidade como garantia da pluralidade das cosmovisões.", True),
            ("Estabelecendo que as congregações religiosas de todas as matrizes devem ser subordinadas a conselhos fiscais de ministérios públicos estaduais.", False),
            ("Proibindo que os municípios criem conselhos tutelares comunitários destinados à mediação de conflitos de vizinhança em bairros pobres.", False),
            ("Determinando que os textos sagrados de todas as tradições espirituais sejam traduzidos compulsoriamente para o esperanto moderno.", False),
            ("Exigindo a homologação judicial prévia de todas as cerimônias religiosas celebradas em templos de pequenas cidades do interior.", False)
        ],
        "- **Etapa 1:** Historicamente, o Estado brasileiro utilizou o Código Penal e as forças policiais para invadir terreiros e criminalizar os sacerdotes negros sob a acusação de 'charlatanismo' ou 'crueldade'.\n- **Etapa 2:** O julgamento do STF no RE 494.601 foi um marco descolonial: os ministros reconheceram a densidade civilizatória e a dignidade litúrgica dos terreiros, consagrando que a laicidade do Estado é escudo protetor da diversidade das matrizes africanas, o que consagra a alternativa A."
    ))

    questoes_brutas.append((
        50, "EM13CHS502", "dificil",
        "No pensamento de Eduardo de Oliveira, de que maneira a Filosofia da Ancestralidade se contrapõe ao relativismo niilista pós-moderno?",
        [
            ("Ancorando a ética em um compromisso comunitário firme de honrar os antepassados e proteger a vida das gerações futuras contra a barbárie.", True),
            ("Defendendo que todos os valores morais são ilusões subjetivas irrelevantes que devem ser ignoradas em decisões políticas do Estado.", False),
            ("Afirmando que a verdade reside exclusivamente na revelação de textos litúrgicos hebraicos conservados em bibliotecas palacianas.", False),
            ("Sustentando que as leis da história humana são governadas por forças cegas da seleção biológica natural sem qualquer sentido ético.", False),
            ("Propondo a dissolução de todos os laços de parentesco familiar para acelerar a formação de indivíduos isolados e sem memória.", False)
        ],
        "- **Etapa 1:** O niilismo e certas vertentes pós-modernas afirmam que tudo é simulacro, que não há fundamento ético e que a moral é mero jogo cínico de poder.\n- **Etapa 2:** A Filosofia da Ancestralidade recusa esse vazio: nossa existência tem fundamento e compromisso; os ancestrais deixaram uma herança de dignidade e sobrevivência que nos cobra a responsabilidade de resistir à destruição da vida e construir um mundo justo, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        51, "EM13CHS504", "dificil",
        "Ao resgatar os saberes corpóreos, como a valorização da oralidade desestabiliza a supremacia da cultura letrada eurocêntrica?",
        [
            ("Mostrando que a palavra viva encarnada na voz e no corpo é portadora de sofisticação reflexiva e rigor conceitual comparável à escrita alfabética.", True),
            ("Comprovando que os livros impressos em gráficas modernas perdem a nitidez das letras após dez anos de exposição ao ar ambiente.", False),
            ("Afirmando que as línguas faladas na Europa renascentista não possuíam vocábulos adequados para a formulação de teorias geométricas.", False),
            ("Demonstrando que os povos que dominam a caligrafia manual apresentam menor flexibilidade muscular em testes de corrida atlética.", False),
            ("Defendendo que as bibliotecas escolares devem doar seus acervos bibliográficos para depósitos de reciclagem de papel jornal.", False)
        ],
        "- **Etapa 1:** O colonialismo sempre utilizou o fetiche da 'cultura escrita' para justificar a presunção de superioridade sobre povos de tradição oral, acusando-os de 'atrasados'.\n- **Etapa 2:** A Afroperspectividade inverte o jogo: a oralidade africana é uma rigorosíssima tecnologia do pensamento; o corpo, o ritmo, o silêncio e a escuta compõem um sistema sofisticado de produção e preservação de saberes filosóficos imunes ao dogmatismo da letra morta, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        52, "EM13CHS606", "dificil",
        "Na formação do pensamento autônomo nacional, em que termos a linhagem de intelectuais negros redefine a Filosofia Brasileira?",
        [
            ("Provando que o verdadeiro pensamento brasileiro brota da luta antirracista e das matrizes afrodiaspóricas e ameríndias, e não da cópia europeia.", True),
            ("Defendendo a padronização dos currículos universitários de acordo com os modelos burocráticos de faculdades privadas da América do Norte.", False),
            ("Afirmando que a literatura nacional deve se limitar à tradução de manuais de direito comercial confeccionados na Europa ocidental.", False),
            ("Sustentando que a filosofia no Brasil foi iniciada por companhias mercantis de navegação que aportaram no litoral no século dezoito.", False),
            ("Propondo a extinção das disciplinas de ciências humanas nos ensinos médio e superior para expandir os cursos de contabilidade fabril.", False)
        ],
        "- **Etapa 1:** Por mais de um século, a elite intelectual brasileira padeceu do 'complexo de vira-lata', buscando imitar Paris, Coimbra ou Berlim como cópias servis.\n- **Etapa 2:** A tradição do pensamento negro liberta o Brasil: do Quilombismo de Abdias e da Amefricanidade de Lélia à Afroperspectividade de Noguera e Flor, a filosofia brasileira afirma sua maioridade ao pensar a partir de sua própria carne e de sua ancestralidade luminosa, legitimando a alternativa A."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "No debate ecológico da Afroperspectividade, qual crítica ao extrativismo predatório moderno se impõe?",
        [
            ("A recusa da dominação da terra como objeto inerte de exploração, resgatando a comunhão sagrada entre os seres humanos e os ecossistemas vivos.", True),
            ("A defesa irrestrita do desmatamento de florestas tropicais para a ampliação de pastagens extensivas de rebanhos de bovinos.", False),
            ("A proposta de que os resíduos químicos industriais sejam despejados diretamente em mananciais de água potável das capitais.", False),
            ("A afirmação de que a extinção de espécies animais é um processo benéfico para a modernização das cidades industriais da costa.", False),
            ("A censura judicial a movimentos socioambientais que reivindicam a titulação de reservas extrativistas de seringueiros e caiçaras.", False)
        ],
        "- **Etapa 1:** A modernidade capitalista eurocêntrica separou a humanidade da natureza, tratando os rios, solos e florestas como meros recursos a serem saqueados.\n- **Etapa 2:** A cosmovisão afroperspectivada compreende a natureza como teia sagrada habitada por energias vitais (as folhas, as águas doces e os mares dos orixás); agredir a terra é agredir o próprio ser humano; o cuidado ambiental é um imperativo ético e comunitário indissociável da vida, validando a alternativa A."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Na análise de Wanderson Flor do Nascimento sobre a encruzilhada, por qual razão a tradução intercultural é apresentada como arma contra o autoritarismo?",
        [
            ("Porque a tradução reconhece a incompletude de toda cultura isolada e convoca o diálogo aberto e generoso entre diferentes visões de mundo.", True),
            ("Porque a tradução exige a submissão das línguas minoritárias aos termos técnicos formulados por comitês de linguistas europeus.", False),
            ("Porque o trabalho de traduzir romances poéticos é considerado pelas cortes civis como uma atividade comercial isenta de tributos.", False),
            ("Porque as assembleias legislativas dos estados proíbem que deputados discursem utilizando palavras de origem estrangeira.", False),
            ("Porque a tradução automática por computadores digitais substituiu definitivamente a necessidade de aulas de leitura nas escolas.", False)
        ],
        "- **Etapa 1:** O autoritarismo colonial sempre impôs sua língua e sua cultura como a única norma legítima, exigindo a assimilação subserviente dos outros.\n- **Etapa 2:** Wanderson Flor resgata a encruzilhada como tradução: traduzir não é colonizar; é criar pontes entre mundos diferentes, onde ninguém é dono absoluto da verdade e todos aprendem na troca mútua e no respeito às diferenças singulares, o que comprova a alternativa A."
    ))

    questoes_brutas.append((
        55, "EM13CHS501", "dificil",
        "No campo dos estudos linguísticos culturais, como a categoria de Pretuguês formulada por Lélia Gonzalez desconstrói o elitismo gramatical?",
        [
            ("Demonstrando que os chamados erros de português na fala popular são marcas rítmicas e fonéticas legítimas herdadas de matrizes africanas.", True),
            ("Provando que os dialetos de imigrantes europeus do século vinte eram mais avançados do ponto de vista da gramática comparada.", False),
            ("Exigindo que os exames vestibulares penalizem com nota zero redações que utilizem figuras de linguagem ou metáforas poéticas.", False),
            ("Afirmando que as academias de letras devem multar financeiramente jornais que publiquem crônicas com expressões do cotidiano.", False),
            ("Sustentando que a língua falada nas ruas do litoral deve ser substituída pelo latim clássico em todas as repartições públicas.", False)
        ],
        "- **Etapa 1:** As elites conservadoras no Brasil historicamente utilizaram a gramática normativa como instrumento de exclusão social e humilhação do povo pobre.\n- **Etapa 2:** Lélia Gonzalez opera uma genial revolução sociolinguística: a fala do povo brasileiro não é 'português errado'; é o Pretuguês altivo, que africanizou a língua do colonizador, dando-lhe ginga, melodia e beleza singular que constituem a alma da cultura nacional, consagrando a alternativa A."
    ))

    questoes_brutas.append((
        56, "EM13CHS502", "dificil",
        "Ao investigar a relação entre a Filosofia Afro-Brasileira e a BNCC, qual avanço educacional na área de Ciências Humanas se evidencia?",
        [
            ("A superação da monocultura curricular eurocêntrica pela incorporação de matrizes conceituais africanas e indígenas como rigor filosófico legítimo.", True),
            ("A eliminação dos debates sobre direitos humanos em salas de aula para evitar controvérsias políticas entre os familiares de estudantes.", False),
            ("A substituição do ensino crítico de história pela memorização exclusiva de cronologias de batalhas travadas por impérios asiáticos.", False),
            ("A proibição de que os professores façam projetos interdisciplinares que integrem as linguagens artísticas às reflexões éticas.", False),
            ("A transferência da gestão pedagógica das escolas públicas para conselhos arbitrais administrados por companhias mineradoras.", False)
        ],
        "- **Etapa 1:** Durante décadas, a BNCC e os currículos escolares reproduziram a mentira de que a filosofia começou na Grécia e terminou na Europa.\n- **Etapa 2:** A Filosofia Afro-Brasileira concretiza o mandato legal e pedagógico da BNCC: rompe o epistemicídio, democratiza o cânone e capacita os estudantes a pensarem com rigor ético e crítico sobre a pluralidade da sociedade brasileira e mundial, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        57, "EM13CHS504", "dificil",
        "Na análise crítica das relações raciais, sob que fundamentos a crítica de Renato Noguera à branquitude esclarece as assimetrias de poder?",
        [
            ("Revelando que a branquitude se coloca invisivelmente como a norma humana universal para manter o privilégio material e epistêmico não questionado.", True),
            ("Afirmando que a cor da pele clara decorre de processos de adaptação climática ocorridos exclusivamente nas regiões boreais do globo.", False),
            ("Comprovando que as decisões econômicas dos governos republicanos baseiam-se unicamente em modelos matemáticos desprovidos de viés social.", False),
            ("Demonstrando que os sistemas judiciais ocidentais aplicam as penas com absoluta imparcialidade e sem preconceitos de classe ou etnia.", False),
            ("Sustentando que os índices de desigualdade salarial nas empresas privadas são explicados pelo número de diplomas de cursos técnicos.", False)
        ],
        "- **Etapa 1:** As teorias conservadoras tratam a raça como se fosse um 'problema que afeta apenas os negros e indígenas', mantendo o branco fora do escrutínio crítico.\n- **Etapa 2:** Noguera desvela o dispositivo: a branquitude é um lugar de privilégio social, simbólico e material não nomeado que se erige como padrão neutro de humanidade; desconstruir a branquitude é condição essencial para a igualdade real e para a emancipação de todos os sujeitos, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        58, "EM13CHS606", "dificil",
        "Ao examinar a Revolta dos Malês sob a lente da Filosofia da Libertação, qual papel a escrita e o domínio da linguagem desempenharam na insurreição?",
        [
            ("A escrita em árabe funcionou como tecnologia de comunicação secreta e instrumento de afirmação da soberania intelectual contra o poder senhorial.", True),
            ("Os manifestantes utilizaram a tipografia mecânica para imprimir panfletos publicitários de oferta de mercadorias no porto comercial.", False),
            ("O domínio do vocabulário da marinha imperial permitiu que os escravizados assumissem o comando de canhoneiras ancoradas na baía.", False),
            ("A correspondência epistolar em latim clássico convenceu os juízes a concederem alvarás de soltura aos prisioneiros da fortaleza naval.", False),
            ("O registro notarial em cartórios de títulos garantiu a compra legal de armamentos importados de depósitos alfandegários da capital.", False)
        ],
        "- **Etapa 1:** Os senhores brancos de escravizados na Bahia da época eram em sua maioria analfabetos ou semialfabetizados nos costumes das fazendas.\n- **Etapa 2:** Os insurgentes Malês dominavam o árabe corânico, trocavam mensagens codificadas em papéis costurados nas roupas e articularam uma das mais sofisticadas rebeliões da história das Américas, provando que a erudição intelectual e a espada da liberdade caminhavam juntas na resistência negra, legitimando a alternativa A."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "Na desconstrução dos cânones monoculturais, como a filosofia da encruzilhada desmantela a imposição do pensamento único?",
        [
            ("Afirmando que a encruzilhada é o território da multiplicidade e da encarnação dos saberes, recusando a ilusão de um centro imperial absoluto.", True),
            ("Comprovando que as equações de primeiro grau são suficientes para explicar todas as variações de preços no mercado internacional de petróleo.", False),
            ("Demonstrando que a história das civilizações antigas deve ser interpretada exclusivamente através da leitura de crônicas dinásticas militares.", False),
            ("Sustentando que as leis de navegação marítima aprovadas no século dezoito devem permanecer intactas em virtude de sua perfeição técnica.", False),
            ("Propondo a unificação compulsória de todos os métodos de pesquisa das ciências sociais sob o controle de um comitê arbitral privado.", False)
        ],
        "- **Etapa 1:** O pensamento moderno dominante opera pela via única: um centro imperial (a Europa) que dita a verdade e periferias que apenas consom e imitam.\n- **Etapa 2:** A encruzilhada é descentramento radical: não há centro fixo; todos os caminhos se cruzam e produzem faíscas criativas; ela desaloja o pensamento único imperial e convida a humanidade a celebrar a polifonia dos saberes em permanente reconstrução, validando a alternativa A."
    ))

    questoes_brutas.append((
        60, "EM13CHS102", "dificil",
        "Em conclusão ao Capítulo 36, que síntese filosófica expressa o papel revolucionário da Afroperspectividade na história do pensamento universal?",
        [
            ("A descolonização definitiva do cânone filosófico e a consagração da matriz africana como patrimônio vivo de emancipação, ética e liberdade universal.", True),
            ("A tentativa fracassada de substituir as ciências experimentais pela memorização de fábulas poéticas de animais em salas de aula públicas.", False),
            ("A restauração de tratados medievais absolutistas que prescreviam a submissão dos cidadãos a ordens de governantes de dinastias imperiais.", False),
            ("A proposição de que os problemas de desigualdade social sejam resolvidos por meio de sorteios de loterias promovidos por bancos centrais.", False),
            ("O isolamento das populações descolonizadas em comunidades fechadas desprovidas de qualquer intercâmbio com as tecnologias do século vinte e um.", False)
        ],
        "- **Etapa 1:** A Afroperspectividade não é um detalhe regional ou adorno secundário, mas arefundação descolonial da própria vocação da filosofia.\n- **Etapa 2:** Ao entrelaçar a ancestralidade, a epistemologia da encruzilhada (Exu) e o compromisso ético com a liberdade dos oprimidos, a filosofia afro-brasileira entrega à humanidade uma bússola inegociável de sabedoria, dignidade e justiça radical, coroando a alternativa A com glória incontestável!"
    ))

    return questoes_brutas

def verificar_blacklist(texto):
    blacklist = [
        r'\bepistemol[oó]gic\w*',
        r'\bontol[oó]gic\w*',
        r'\bteleol[oó]gic\w*',
        r'\bdicotomi\w*',
        r'\bintr[ií]nsec\w*',
        r'\bextr[ií]nsec\w*',
        r'\bsubjacente\w*',
        r'\bef[eê]mer\w*',
        r'\bprerrogativa\w*',
        r'\bprescind\w*',
        r'\bimprescind\w*',
        r'\bcorrobor\w*',
        r'\bhegem[oô]nic\w*',
        r'\bmitigar\b',
        r'\bfomentar\b',
        r'\bproped[eê]utic\w*',
        r'\binexor\w*',
        r'\baxiol[oó]gic\w*',
        r'\bhermen[eê]utic\w*',
        r'\bmormente\b',
        r'\bprec[ií]pu\w*',
        r'R\$'
    ]
    erros = []
    for padrao in blacklist:
        matches = re.findall(padrao, texto, flags=re.IGNORECASE)
        if matches:
            erros.append((padrao, set(matches)))
    return erros

def formatar_markdown(questoes):
    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('eixo: "Eixo V: Existencialismo, Filosofias da Diferença e Saberes Tradicionais"')
    md.append('capitulo: "Capítulo 36: Afroperspectividade e Filosofia Negra Brasileira"')
    md.append('objeto_de_conhecimento: "A consolidação da Filosofia Afro-Brasileira, a Afroperspectividade em Renato Noguera, o enfrentamento ao racismo epistêmico em Wanderson Flor do Nascimento, a sabedoria da encruzilhada (Exu) e a ancestralidade"')
    md.append('ebook_fonte: "em-fil-c36-afroperspectividade-filosofia-brasileira-noguera-flor.md"')
    md.append('habilidades:')
    md.append('  - "EM13CHS101"')
    md.append('  - "EM13CHS102"')
    md.append('  - "EM13CHS501"')
    md.append('  - "EM13CHS502"')
    md.append('  - "EM13CHS504"')
    md.append('  - "EM13CHS606"')
    md.append('total_exercicios: 60')
    md.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    md.append("---\n")

    md.append("# Lista de Exercícios: Afroperspectividade e Filosofia Negra Brasileira\n")
    md.append("## Nível Básico\n")

    letras = ["A", "B", "C", "D", "E"]

    for num, hab, dif, enunciado, alternativas, resolucao in questoes:
        if num == 21:
            md.append("## Nível Intermediário\n")
        elif num == 41:
            md.append("## Nível Difícil\n")

        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-36-afroperspectividade-filosofia-brasileira-noguera-flor -->")
        md.append(f"### Questão {num}\n")
        md.append(f"{enunciado}\n")
        
        letra_correta = None
        for i, (alt_texto, correta) in enumerate(alternativas):
            l = letras[i]
            md.append(f"{l}) {alt_texto}")
            if correta:
                letra_correta = l
        
        md.append(f"\n**Gabarito:** ({letra_correta})\n")
        md.append(f"**Resolução Comentada:**\n{resolucao}\n")
        md.append("---\n")

    md.append("## Referências\n")
    md.append("- NOGUERA, Renato. *O ensino de filosofia e a Lei 10.639*. Rio de Janeiro: Pallas, 2014.")
    md.append("- NASCIMENTO, Wanderson Flor do. Em torno do racismo epistêmico: descolonizar o saber, descolonizar a filosofia. *Revista Sul-Americana de Filosofia e Educação*, n. 29, p. 119-137, 2018.")
    md.append("- SODRÉ, Muniz. *O terreiro e a cidade: a forma social negro-brasileira*. Petrópolis: Vozes, 1988.")
    md.append("- OLIVEIRA, Eduardo David de. Filosofia da ancestralidade como filosofia africana: educação e cultura afro-brasileira. *Revista Sul-Americana de Filosofia e Educação*, n. 18, p. 28-47, 2012.")
    md.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.\n")

    return "\n".join(md)

def main():
    questoes = build_exercicios()
    print(f"Total de questões construídas: {len(questoes)}")

    # 0. Ajuste rigoroso de gabarito para ciclo balanceado perfeito (12 de cada)
    questoes_balanceadas = []
    for q in questoes:
        num, hab, dif, enunciado, alternativas, resolucao = q
        target_idx = (num - 1) % 5
        corr_idx = [i for i, (_, c) in enumerate(alternativas) if c][0]
        if corr_idx != target_idx:
            alts = list(alternativas)
            alts[corr_idx], alts[target_idx] = alts[target_idx], alts[corr_idx]
            alternativas = alts
            # Atualiza mencao de letra na resolucao se houver
            letras = ["A", "B", "C", "D", "E"]
            antiga_letra = letras[corr_idx]
            nova_letra = letras[target_idx]
            resolucao = re.sub(rf'alternativa {antiga_letra}\b', f'alternativa {nova_letra}', resolucao)
        questoes_balanceadas.append((num, hab, dif, enunciado, alternativas, resolucao))
    questoes = questoes_balanceadas

    # 1. Checagem de quantidade e numeração
    assert len(questoes) == 60, f"Esperava 60 questões, obteve {len(questoes)}"
    for idx, q in enumerate(questoes, 1):
        assert q[0] == idx, f"Questão fora de ordem: {q[0]} != {idx}"

    # 2. Checagem de gabarito balanceado
    gabaritos = []
    letras = ["A", "B", "C", "D", "E"]
    for q in questoes:
        corretas = [letras[i] for i, (_, c) in enumerate(q[4]) if c]
        assert len(corretas) == 1, f"Questão {q[0]} tem {len(corretas)} corretas!"
        gabaritos.append(corretas[0])
    
    contagem = Counter(gabaritos)
    print("Distribuição de gabaritos:", contagem)
    for l in letras:
        assert contagem[l] == 12, f"Letra {l} tem {contagem[l]} ocorrências (esperado 12)!"

    # 3. Formatação
    md_content = formatar_markdown(questoes)

    # 4. Checagem de blacklist no texto gerado
    erros_bl = verificar_blacklist(md_content)
    if erros_bl:
        print("\n[ERRO FATAL] Termos proibidos encontrados:")
        for padrao, matches in erros_bl:
            print(f"  - Padrão '{padrao}': {matches}")
        sys.exit(1)
    else:
        print("Auditoria interna: NENHUM termo da blacklist detectado!")

    # 5. Checagem de inícios de enunciados repetidos
    inicios = [q[3].split()[:2] for q in questoes]
    inicios_str = [" ".join(x).lower() for x in inicios]
    c_inicios = Counter(inicios_str)
    print("Inícios mais frequentes:", c_inicios.most_common(5))
    for inicio, count in c_inicios.items():
        if count > 6:
            print(f"[ALERTA/ERRO] Início '{inicio}' ocorre {count} vezes (>6)!")
            sys.exit(1)

    # 6. Salvar em temp_draft.md
    temp_draft = "temp_draft.md"
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Arquivo rascunho salvo com sucesso em '{temp_draft}'.")

    # 7. Executar validador oficial
    destino_final = "content/medio/volume-unico/filosofia/eixo-5-existencialismo-diferenca/cap-36-afroperspectividade-filosofia-brasileira-noguera-flor/ebooks/em-fil-c36-afroperspectividade-filosofia-brasileira-noguera-flor-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 36 validado e homologado com Exit Code 0!")
        print("MARCO HISTÓRICO DE 36 CAPÍTULOS E 2.160 QUESTÕES HOMOLOGADAS!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
