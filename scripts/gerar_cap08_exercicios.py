# -*- coding: utf-8 -*-
import os
import sys
import re
import subprocess
from collections import Counter

def balancear_questoes(questoes_brutas):
    alvo_letras = ['A', 'B', 'C', 'D', 'E'] * 12
    questoes_balanceadas = []

    for i, q in enumerate(questoes_brutas):
        num, hab, dif, enunc, a, b, c, d, e, gab_orig, res = q
        alvo = alvo_letras[i]
        
        alt_map = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}
        
        if gab_orig != alvo:
            texto_correto = alt_map[gab_orig]
            texto_outro = alt_map[alvo]
            alt_map[alvo] = texto_correto
            alt_map[gab_orig] = texto_outro
            
        novo_gab = alvo
        questoes_balanceadas.append((
            num, hab, dif, enunc,
            alt_map['A'], alt_map['B'], alt_map['C'], alt_map['D'], alt_map['E'],
            novo_gab, res
        ))
        
    return questoes_balanceadas

def gerar_cap08():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-08-epistemicidio-colonialidade-saber-sueli-carneiro/ebooks/em-fil-c08-epistemicidio-colonialidade-saber-sueli-carneiro-exercicios.md"
    temp_draft = "temp_draft.md"

    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Como a crítica contemporânea define o chamado 'Universalismo Abstrato Eurocêntrico'?",
        "A tese de que a física matemática foi inventada por navegadores fenícios no mar Mediterrâneo.",
        "A pretensão de considerar os padrões culturais e teóricos da Europa Ocidental como a única expressão universal e válida da razão humana.",
        "O estudo comparativo de línguas indígenas promovido por jesuítas na América do Sul.",
        "A defesa do retorno às leis civis da monarquia absolutista em países africanos.",
        "A proposta de proibir o uso de moedas metálicas no comércio internacional de mercadorias.",
        "B",
        "O universalismo abstrato eurocêntrico impõe os modos particulares de pensar da Europa como norma universal para toda a humanidade, desqualificando outras culturas."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "O filósofo Santiago Castro-Gómez utiliza a expressão 'Ponto Zero' para denunciar qual postura teórica da modernidade ocidental?",
        "A medição exata da temperatura de congelamento da água no inverno.",
        "A pretensão do pensador europeu de observar o mundo a partir de uma perspectiva neutra e divina sem ser visto, ignorando sua própria localização corporal e geopolítica.",
        "A criação de mapas de navegação marítima sem o registro da linha do equador.",
        "O hábito de iniciar reuniões acadêmicas exatamente à meia-noite.",
        "A defesa de que as leis da astronomia dependem da direção dos ventos alísios.",
        "B",
        "A 'hybris do Ponto Zero' é a ilusão de um saber desincorporado e pretensamente neutro que julga todos os saberes alheios como primitivos."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Na teoria social de Boaventura de Sousa Santos, o que define a chamada 'Linha Abissal'?",
        "Uma fenda geológica submarina localizada no centro do oceano Atlântico.",
        "Uma divisão invisível que separa o Norte Global (onde vigoram a lei e os saberes reconhecidos) do Sul Global colonizado (onde os saberes são declarados inexistentes ou inferiores).",
        "Uma fronteira militar criada entre os países da Europa após a Primeira Guerra Mundial.",
        "A altitude máxima permitida para o voo de balões meteorológicos.",
        "A demarcação de portos comerciais dedicados ao embarque de café e cana-de-açúcar.",
        "B",
        "O pensamento abissal divide a realidade: do outro lado da linha (Sul Global), os saberes e sujeitos são invisibilizados e tratados como não existentes."
    ))

    questoes_brutas.append((
        4, "EM13CHS102", "basico",
        "Qual intelectual e filósofa brasileira aprofundou de forma monumental o conceito de Epistemicídio em sua tese de doutorado na USP?",
        "Lélia Gonzalez.",
        "Sueli Carneiro.",
        "Conceição Evaristo.",
        "Djamila Ribeiro.",
        "Carolina Maria de Jesus.",
        "B",
        "Sueli Carneiro sistematizou o conceito de epistemicídio em sua seminal tese 'A Construção do Outro como Não-Ser como Fundamento do Ser' (2005)."
    ))

    questoes_brutas.append((
        5, "EM13CHS102", "basico",
        "Como Sueli Carneiro define o conceito de Epistemicídio?",
        "A extinção biológica de espécies animais em florestas tropicais da América do Sul.",
        "O assassinato e a destruição sistemática da capacidade de produzir conhecimento de povos colonizados, acompanhado do rebaixamento de sua autoestima intelectual.",
        "A proibição do ensino de gramática nas escolas públicas de cidades do interior.",
        "O fechamento de livrarias de obras de ficção científica por falta de clientes.",
        "A queima de documentos contábeis de empresas privadas falidas.",
        "B",
        "O epistemicídio é a violência cultural que destrói, desvaloriza e silencia a capacidade cognoscente de populações negras e indígenas para perpetuar a dominação colonial."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Em sua tese, Sueli Carneiro dialoga com Frantz Fanon para demonstrar que a construção do colonizador branco como o 'Ser' pleno exigiu como contrapartida:",
        "A distribuição igualitária de terras cultiváveis entre camponeses.",
        "A construção violenta do povo colonizado como o 'Não-Ser' (sujeito desprovido de história e fala autônoma).",
        "O ensino obrigatório da língua grega antiga nas escolas da África.",
        "A criação de tribunais internacionais de julgamento de dívidas externas.",
        "A abolição de títulos de nobreza nos países da América Latina.",
        "B",
        "A autoproclamação do colonizador europeu como o modelo supremo de humanidade exigiu a negação do colonizado, rebaixado à condição existencial de Não-Ser."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "O sociólogo peruano Aníbal Quijano formulou qual conceito capital para demonstrar que a hierarquia colonial de poder sobreviveu ao fim dos impérios coloniais?",
        "Luta de classes industrial.",
        "Colonialidade do Poder.",
        "Contrato social hobbesiano.",
        "Solidariedade mecânica urbana.",
        "Ação comunicativa universal.",
        "B",
        "Aníbal Quijano formulou a 'Colonialidade do Poder', mostrando que a ideia moderna de raça continua estruturando as desigualdades econômicas e sociais globais."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "Para Aníbal Quijano, qual critério mental e social foi forjado na conquista da América para classificar a população mundial em posições inferiores e superiores?",
        "A preferência musical por instrumentos de corda.",
        "A ideia de Raça, que naturalizou as hierarquias de dominação e a divisão internacional do trabalho.",
        "A proficiência técnica em cálculos de geometria analítica.",
        "O hábito de consumir cereais cozidos nas refeições matinais.",
        "A habilidade em conduzir cavalos de carga em montanhas rochosas.",
        "B",
        "A raça foi construída como instrumento basilar de dominação colonial para legitimar o trabalho compulsório de negros e indígenas e justificar a supremacia europeia."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "O pensador argentino Walter Mignolo destaca a necessidade da 'Desobediência Epistêmica'. Em que consiste essa atitude?",
        "Recusar pagar impostos municipais em cidades com portos abertos.",
        "Romper com a submissão aos modelos conceituais eurocêntricos e valorizar os saberes e perspectivas forjados a partir do Sul Global.",
        "Abandonar o uso de aparelhos telefônicos e computadores digitais nas escolas.",
        "Exigir que todos os tratados filosóficos sejam escritos em versos poéticos.",
        "Proibir a leitura de textos científicos traduzidos de línguas estrangeiras.",
        "B",
        "A desobediência epistêmica desvincula a produção do saber do cânone colonial, afirmando a legitimidade e a dignidade das tradições de conhecimento não ocidentais."
    ))

    questoes_brutas.append((
        10, "EM13CHS502", "basico",
        "O escritor queniano Ngũgĩ wa Thiong'o formulou um influente projeto intelectual em sua obra clássica. Qual é o título e o propósito central dessa obra?",
        "'A Origem dos Metais': investigar minas de ouro na África oriental.",
        "'Descolonizar a Mente': recuperar a língua e a cultura ancestrais contra a imposição linguística colonial.",
        "'O Tratado da Navegação': cartografar rotas marítimas no oceano Índico.",
        "'A Gramática Latina': ensinar a retórica do império romano aos estudantes.",
        "'As Guerras Modernas': analisar o treinamento de infantaria militar.",
        "B",
        "Em 'Descolonizar a Mente', Ngũgĩ wa Thiong'o defende que a colonização domina pela linguagem; libertar-se exige resgatar as línguas maternas e as formas africanas de ver o mundo."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Para Boaventura de Sousa Santos, qual proposta filosófica contrapõe-se à monocultura do saber científico ocidental dominante?",
        "O isolamento geográfico total dos continentes.",
        "A Ecologia de Saberes, que promove o diálogo simétrico entre o conhecimento científico e os saberes tradicionais, populares e comunitários.",
        "A censura obrigatória de todas as pesquisas biomédicas contemporâneas.",
        "A substituição da escrita em papel por sinais de fumaça em montanhas.",
        "A imposição de uma única língua oficial falada por todos os povos do planeta.",
        "B",
        "A Ecologia de Saberes baseia-se na ideia de que não há ignorância nem conhecimento em abstrato; promove a copresença e o aprendizado recíproco entre diversos tipos de saberes."
    ))

    questoes_brutas.append((
        12, "EM13CHS601", "basico",
        "A célebre máxima de Boaventura de Sousa Santos para a emancipação global estabelece que:",
        "'Não há riqueza material sem exploração do trabalho nas minas.'",
        "'Não há justiça social global sem justiça cognitiva global.'",
        "'O comércio internacional dispensa o uso de tratados de paz.'",
        "'As leis dos tribunais dependem da quantidade de ouro nos cofres.'",
        "'A verdade científica pertence exclusivamente aos países mais ricos.'",
        "B",
        "A justiça cognitiva global reconhece que a libertação dos povos espoliados exige a legitimação de suas formas próprias de conhecimento e visão de mundo."
    ))

    questoes_brutas.append((
        13, "EM13CHS502", "basico",
        "No Brasil, qual legislação pioneira tornou obrigatório o ensino da História e Cultura Afro-Brasileira nas escolas públicas e privadas da educação básica?",
        "A Lei de Terras de 1850.",
        "A Lei Federal 10.639/03.",
        "O Código de Defesa do Consumidor.",
        "A Lei do Ventre Livre de 1871.",
        "O Decreto da Regência Trina de 1831.",
        "B",
        "A Lei 10.639/03 alterou a LDB para incluir a história e cultura africana e afro-brasileira no currículo, atuando como reparação histórica contra o epistemicídio."
    ))

    questoes_brutas.append((
        14, "EM13CHS502", "basico",
        "Posteriormente, qual marco legal complementou a Lei 10.639/03 ao incluir a obrigatoriedade da temática indígena nos currículos escolares brasileiros?",
        "A Lei Áurea de 1888.",
        "A Lei Federal 11.645/08.",
        "O Tratado de Tordesilhas.",
        "A Constituição Imperial de 1824.",
        "O Estatuto da Terra de 1964.",
        "B",
        "A Lei 11.645/08 ampliou as diretrizes curriculares nacionais para abarcar também a história, os saberes e as culturas dos povos indígenas originários do Brasil."
    ))

    questoes_brutas.append((
        15, "EM13CHS102", "basico",
        "Ao analisar a experiência educacional de crianças negras em escolas tradicionais, Sueli Carneiro denuncia que o epistemicídio gera qual efeito psicológico nocivo?",
        "O aumento espontâneo da velocidade de leitura de textos matemáticos.",
        "A mutilação da autoestima cognitiva, vergonha da própria identidade e o sentimento de inferioridade intelectual.",
        "A preferência imediata pelo estudo de astronomia e navegação a vela.",
        "A facilidade em memorizar nomes de generais de dinastias do norte da Europa.",
        "A recusa em participar de brincadeiras esportivas com bolas de couro.",
        "B",
        "O currículo eurocêntrico que omite a história e saberes negros gera alienação e baixa autoestima, ensinando a criança subalternizada a rejeitar sua própria ancestralidade."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Em contraposição à razão indolente ocidental, o sociólogo Boaventura de Sousa Santos propõe a 'Sociologia das Ausências', que tem por missão:",
        "Contar quantas cadeiras vazias existem em salas de aula durante o inverno.",
        "Transformar objetos impossíveis em possíveis e saberes declarados ausentes e inferiores em alternativas vivas e credíveis.",
        "Proibir a realização de conferências públicas em universidades metropolitanas.",
        "Calcular a perda financeira provocada por naufrágios de navios no mar Egeu.",
        "Eliminar as matérias de ciências sociais dos currículos de ensino fundamental.",
        "B",
        "A Sociologia das Ausências resgata o que foi desperdiçado e considerado 'não existente' pelo colonialismo, demonstrando a riqueza dos saberes populares e tradicionais."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Qual termo é utilizado por pensadores descoloniais para designar a suposição de que tudo fora do padrão branco europeu é exótico, folclórico e sem valor conceitual?",
        "Racionalismo cartesiano.",
        "Eurocentrismo epistêmico.",
        "Dialética platônica.",
        "Hedonismo helenístico.",
        "Cinismo de Diógenes.",
        "B",
        "O eurocentrismo epistêmico reduz as cosmologias e filosofias de outros continentes a mero 'folclore' ou 'artesanato cultural', negando-lhes rigor conceitual e filosófico."
    ))

    questoes_brutas.append((
        18, "EM13CHS502", "basico",
        "O filósofo Renato Noguera destaca que a valorização da filosofia africana no Brasil contribui para o cumprimento das leis educacionais porque:",
        "Obriga as crianças a decorarem listas de nomes de faraós egípcios sem reflexão.",
        "Apresenta matrizes de pensamento ancestrais (como Maat e Ubuntu) que promovem a dignidade, a ética comunitária e o combate ao racismo estrutural.",
        "Proíbe o uso de instrumentos musicais ocidentais em apresentações escolares.",
        "Substitui as aulas de ciências naturais por competições de danças festivas.",
        "Exige que todas as escolas funcionem em regime de internato rural fechado.",
        "B",
        "O ensino de filosofias africanas expande o repertório ético e reflexivo dos estudantes, rompendo com a invisibilização colonial e fortalecendo a cidadania antirracista."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Na análise de Walter Mignolo, em vez da geopolítica imperial do conhecimento que finge universalidade, a crítica descolonial reivindica a:",
        "Imposição forçada de decretos militares sobre as universidades da periferia.",
        "Corpo-política e Geopolítica do Conhecimento, que reconhece o lugar, a cor e a vivência de onde o pensamento é enunciado.",
        "Proibição do intercâmbio de livros entre bibliotecas de diferentes países.",
        "Submissão dos pesquisadores às ordens de banqueiros de moedas estrangeiras.",
        "Criação de calendários anuais com apenas seis meses de duração nas cidades.",
        "B",
        "A corpo-política e a geopolítica do conhecimento mostram que ninguém pensa no vácuo: todo pensamento tem corpo, gênero, raça e território histórico de enunciação."
    ))

    questoes_brutas.append((
        20, "EM13CHS102", "basico",
        "O conceito de 'Justiça Cognitiva Global' estabelece que a luta contra a opressão material e a desigualdade socioeconômica mundial deve caminhar junto com:",
        "O aumento das taxas aduaneiras sobre a importação de tecidos finos.",
        "O reconhecimento e a legitimação da diversidade de sistemas de conhecimento e saberes que existem no planeta.",
        "A construção de muralhas de pedra ao redor das capitais de países ricos.",
        "A obrigatoriedade de que todos os professores usem roupas de linho branco.",
        "O fechamento dos tribunais que julgam causas de direitos civis de minorias.",
        "B",
        "A justiça cognitiva exige a superação da monocultura do saber eurocêntrico e a valorização equitativa das formas de saber e cosmologias do Sul Global."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao contrastar o modelo do 'Ponto Zero' de Castro-Gómez com a proposta das Epistemologias do Sul, nota-se uma divergência basilar sobre a produção da verdade, pois:",
        "O Ponto Zero defende que a verdade depende de canções de poetas populares, e as Epistemologias do Sul exigem oráculos divinos.",
        "O Ponto Zero finge uma neutralidade divina e desterritorializada, enquanto as Epistemologias do Sul afirmam que todo saber é situado, encarnado e vinculado às lutas contra a opressão.",
        "Ambos os modelos defendem que apenas os cientistas europeus possuem capacidade biológica de raciocínio abstrato.",
        "O Ponto Zero proíbe a observação de estrelas e as Epistemologias do Sul defendem o fechamento de laboratórios.",
        "As Epistemologias do Sul pretendem queimar todos os livros de física e matemática escritos desde o Renascimento.",
        "B",
        "O pensamento do Ponto Zero esconde seus interesses coloniais sob uma falsa máscara de neutralidade; as Epistemologias do Sul assumem a localização histórica e o compromisso emancipatório do saber."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Em sua análise sobre o epistemicídio no currículo escolar, Sueli Carneiro demonstra que a desvalorização dos saberes de matriz africana atua como um mecanismo de dominação porque:",
        "Aumenta os custos de impressão das cartilhas de alfabetização dos alunos.",
        "Ensina os estudantes a interiorizarem a ideia de que a Europa foi a única criadora da civilização, desarmando a resistência crítica e cultural da população negra.",
        "Obriga os professores a ensinarem técnicas de plantio de milho e feijão durante as aulas de geografia.",
        "Proíbe a formação de grêmios estudantis em colégios públicos de bairros periféricos.",
        "Exige que as famílias paguem mensalidades escolares em moedas de ouro maciço.",
        "B",
        "Ao apagar a história e as contribuições civilizatórias africanas, o epistemicídio constrói a subalternidade psicológica, fazendo o grupo dominado assimilar o olhar depreciativo do dominador."
    ))

    questoes_brutas.append((
        23, "EM13CHS101", "intermediario",
        "A distinção feita por Boaventura de Sousa Santos entre 'deste lado da linha' e 'do outro lado da linha' no Pensamento Abissal explica por que certas violências coloniais eram aceitas com naturalidade, uma vez que:",
        "Os oceanos eram considerados zonas de comércio livre de impostos aduaneiros.",
        "Do outro lado da linha (as colônias), o direito e a ética vigentes na metrópole não se aplicavam, legitimando a escravidão, o saque e a desumanização de povos inteiros.",
        "Os tratados de paz eram assinados apenas em línguas que ninguém conseguia falar na Europa.",
        "Os generais de cavalaria não podiam embarcar com suas armaduras de ferro nos navios.",
        "As colônias agrícolas eram consideradas templos religiosos imunes a conflitos de ordem militar.",
        "B",
        "O pensamento abissal opera com padrão duplo: os direitos humanos e as garantias cívicas valiam para o colonizador; para o colonizado além da linha, vigoravam a exceção, o arbítrio e a violência legalizada."
    ))

    questoes_brutas.append((
        24, "EM13CHS502", "intermediario",
        "Ao abordar o papel da linguagem na dominação imperial em Descolonizar a Mente, Ngũgĩ wa Thiong'o alerta que forçar as crianças africanas a falarem exclusivamente a língua do colonizador produzia:",
        "A descoberta imediata de curas para febres e doenças tropicais nas florestas.",
        "Uma ruptura psicológica alienante entre o universo afetivo da comunidade originária e o mundo conceitual da escola, subordinando a mente ao imaginário imperial.",
        "A facilidade em construir pontes de ferro sobre rios caudalosos no interior do país.",
        "A preferência espontânea dos jovens pela leitura de tratados jurídicos em latim arcaico.",
        "O desaparecimento das chuvas de verão nas regiões agrícolas da savana.",
        "B",
        "A imposição da língua colonial opera uma alienação cultural: a criança aprende a ver sua própria língua e experiência comunitária como inferiores, assimilando o mundo pelas categorias do opressor."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Na teoria da Colonialidade do Poder de Aníbal Quijano, por que a proclamação da independência política das repúblicas da América Latina no século XIX não eliminou a estrutura colonial?",
        "Porque as nações independentes foram obrigadas a adotar a mesma bandeira tricolor de governos europeus.",
        "Porque as novas elites criollas mantiveram intactas a hierarquia racial interna e a subordinação das populações indígenas e negras como mão de obra explorada.",
        "Porque os portos marítimos foram fechados para a chegada de navios cargueiros da Ásia.",
        "Porque as moedas de prata foram substituídas por conchas marinhas em todas as feiras comerciais.",
        "Porque os generais dos exércitos libertadores foram impedidos de morar nas capitais dos países.",
        "B",
        "A descolonização formal dos Estados não encerrou a colonialidade: as relações de raça, classe, expropriação de terras e racismo institucional continuaram estruturando o poder nas novas repúblicas."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "O trabalho teórico de Sueli Carneiro estabelece um diálogo crítico e fecundo com a microfísica do poder de Michel Foucault. Qual aspecto do pensamento foucaultiano é ressignificado por Carneiro?",
        "A afirmação de que os manicômios devem funcionar no alto de montanhas rochosas isoladas.",
        "A articulação entre saber e poder: demonstrar que o racismo opera por dispositivos discursivos e institucionais que produzem a exclusão social e a morte simbólica de sujeitos negros.",
        "A defesa de que as prisões devem ser pintadas de azul claro para acalmar os detentos durante a noite.",
        "A proposta de que os professores universitários devem ser escolhidos por meio de competições atléticas.",
        "A tese de que a medicina ocidental não utiliza medicamentos químicos em tratamentos hospitalares.",
        "B",
        "Sueli Carneiro articula Foucault para mostrar que o racismo é um dispositivo de poder-saber: o epistemicídio funciona como tecnologia biopolítica que interdita a fala e a autoridade cognitiva dos corpos negros."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "Como a proposta da 'Ecologia de Saberes' de Boaventura de Sousa Santos aborda a relação entre o conhecimento científico moderno e os saberes tradicionais dos povos originários?",
        "Defendendo que a ciência moderna deve ser banida e que todos os hospitais devem ser fechados.",
        "Recusando a primazia exclusiva da ciência ocidental, propondo um diálogo horizontal em que ciência e saberes tradicionais se complementam para responder a desafios ecológicos e humanos complexos.",
        "Afirmando que os indígenas da Amazônia devem ensinar álgebra nos cursos de pós-graduação de física.",
        "Impondo que as pesquisas botânicas sejam avaliadas por votação secreta de parlamentares europeus.",
        "Exigindo que todos os remédios produzidos por indústrias farmacêuticas sejam jogados nas águas dos rios.",
        "B",
        "A ecologia de saberes não é anticientífica; rejeita o monopólio arrogante da ciência cega, integrando o conhecimento técnico e a sabedoria ancestral (como o manejo florestal sustentável indígena)."
    ))

    questoes_brutas.append((
        28, "EM13CHS502", "intermediario",
        "A implementação das Leis 10.639/03 e 11.645/08 no currículo escolar brasileiro representa uma medida de descolonização pedagógica porque:",
        "Obriga os colégios a utilizarem apenas livros impressos em papel reciclado de fábricas nacionais.",
        "Desloca o centro exclusivo da narrativa histórica da branquitude europeia, inserindo o protagonismo civilizatório, intelectual e estético de africanos e povos originários na formação do Brasil.",
        "Proíbe o ensino de disciplinas de matemática e física em escolas de ensino médio de cidades costeiras.",
        "Exige que os estudantes decorem genealogias de generais militares que governaram a França e a Inglaterra.",
        "Cancela a realização de exames admissionais em faculdades públicas para todos os cursos de ciências.",
        "B",
        "As leis desmantelam o currículo colonial eurocêntrico, garantindo que a contribuição intelectual e histórica das matrizes negra e indígena seja ensinada com rigor e dignidade a todos os estudantes."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Ao examinar a relação entre modernidade e colonialidade, o grupo modernidade/colonialidade (Quijano, Mignolo, Dussel) afirma que a colonialidade não é um acidente externo da modernidade, mas:",
        "Um equívoco administrativo temporário provocado pelo cansaço de navegadores da frota marítima.",
        "O lado escuro e constitutivo indispensável da própria modernidade, que só pôde acumular riquezas e erguer seu modelo civilizatório às custas da pilhagem e da desumanização colonial.",
        "Uma teoria inventada por autores de romances policiais para vender livros impressos nas feiras da Europa.",
        "Um período de paz perpétua celebrado entre reis da Espanha e chefes tribais da Península Arábica.",
        "Um sistema de comércio que durou apenas duas semanas durante o reinado de monarcas ingleses.",
        "B",
        "A modernidade europeia e a colonialidade são duas faces da mesma moeda: o enriquecimento e a iluminação da Europa foram construídos sobre a espoliação violenta, escravidão e genocídio no Sul Global."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Em seu texto clássico 'Enegrecer o Feminismo', Sueli Carneiro formula uma crítica contundente ao feminismo dominante branco liberal ao apontar que:",
        "O feminismo branco defendia que as mulheres não deviam aprender a ler textos de geometria nas escolas.",
        "O feminismo eurocêntrico universalizava a experiência da mulher branca de classe média (focada no direito de sair de casa para trabalhar), desconsiderando que a mulher negra sempre trabalhou na lavoura e na rua sob exploração brutal.",
        "As mulheres brancas eram proibidas de viajar de navio para fora do continente europeu durante o verão.",
        "O movimento feminista deveria ser extinto para permitir que apenas generais homens legislassem na sociedade.",
        "As mulheres negras tinham salários superiores aos dos homens brancos nas fábricas industriais da época.",
        "B",
        "Sueli Carneiro enegrece o feminismo articulando gênero e raça: a mulher negra sofre uma dupla opressão histórica e nunca viveu o confinamento doméstico dourado das elites brancas, exigindo um feminismo antirracista."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Na reflexão de Walter Mignolo, a frase cartesiana 'penso, logo existo' (ego cogito) foi historicamente precedida e tornada possível por qual formulação imperial oculta?",
        "O 'amo, logo perdoo' pregado por monges em mosteiros medievais na Itália.",
        "O 'eu conquisto, logo existo' (ego conquiro), que submeteu territórios e povos antes de proclamar a soberania da razão iluminista.",
        "O 'navego, logo pesco' entoado por pescadores em aldeias costeiras do mar Mediterrâneo.",
        "O 'compro, logo vendo' anunciado por mercadores em feiras públicas de tecidos na Holanda.",
        "O 'canto, logo danço' celebrado em festivais folclóricos durante a colheita da uva.",
        "B",
        "Mignolo e Dussel mostram que o sujeito soberano cartesiano só pôde surgir porque a Europa assumira militarmente o papel de conquistadora mundial (ego conquiro) através da expansão colonial sangrenta."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Ao tratar da apropriação e expropriação epistêmica, estudiosos descoloniais denunciam que a medicina tradicional de povos indígenas frequentemente sofre qual forma de espoliação por empresas transnacionais?",
        "A queima obrigatória de todas as ervas medicinais por ordem de tratados de direito internacional.",
        "A biopirataria e apropriação indevida de saberes ancestrais patenteados por indústrias farmacêuticas do Norte sem retorno financeiro ou reconhecimento ético às comunidades originárias detentoras do saber.",
        "A exigência de que os xamãs e pajés assumam a direção de hospitais públicos nas capitais europeias.",
        "O fechamento de laboratórios de química que utilizavam reagentes produzidos com cana-de-açúcar.",
        "A proibição do uso de termômetros e microscópios ópticos em aldeias de povos da floresta.",
        "B",
        "O epistemicídio manifesta-se também como expropriação: os saberes ancestrais são desqualificados como 'crendice', mas seus princípios ativos são patenteados e privatizados por corporações do Norte Global."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Em contraposição à razão metonímica eurocêntrica (que toma a parte ocidental pelo todo universal da humanidade), Boaventura propõe a 'Razão Cosmopolita'. Essa razão atua por meio de qual prática?",
        "A realização de corridas de bigas na areia das praias do mar Mediterrâneo.",
        "A Tradução Intercultural, que estabelece inteligibilidade mútua entre diferentes experiências, lutas e saberes do mundo sem imperialismo cultural.",
        "A imposição de uma moeda bancária única emitida por governantes de cidades industriais.",
        "O confisco de obras de arte antigas guardadas em museus de países da América do Sul.",
        "A proibição de manifestações religiosas comunitárias em praças públicas de bairros populares.",
        "B",
        "A tradução intercultural permite criar pontes de diálogo entre diferentes cosmologias e linguagens emancipatórias (como os direitos humanos ocidentais e o conceito indígena de Buen Vivir / Sumak Kawsay)."
    ))

    questoes_brutas.append((
        34, "EM13CHS502", "intermediario",
        "Ao debater a literatura africana em línguas europeias (como inglês, francês ou português), autores contemporâneos destacam que o desafio descolonial envolve:",
        "Queimar todas as gráficas de editoras que imprimem livros de literatura em papel de celulose.",
        "Subverter e torcer a língua do colonizador para inscrever nela os ritmos, oralidades, memórias e cosmovisões dos povos subalternizados, desestabilizando o cânone linguístico tradicional.",
        "Proibir que os jovens de cidades africanas aprendam a ler e escrever em línguas alfabéticas.",
        "Exigir que todos os romances literários tratem de batalhas navais travadas no mar Báltico.",
        "Determinar que os poetas utilizem apenas tintas pretas feitas com cinzas de carvão vegetal.",
        "B",
        "Descolonizar a língua envolve apropriar-se criativamente do idioma do opressor (o 'pretuguês' de Lélia Gonzalez ou a recriação literária) para expressar a voz e a resistência da diáspora negra e dos povos colonizados."
    ))

    questoes_brutas.append((
        35, "EM13CHS102", "intermediario",
        "No ambiente universitário e acadêmico brasileiro, o combate ao epistemicídio provocou importantes reformas institucionais nas últimas décadas, entre as quais se destaca:",
        "A exclusão de livros de ciências humanas dos acervos de bibliotecas centrais de universidades federais.",
        "A adoção de políticas de Ações Afirmativas e Cotas Raciais para ingresso na graduação e pós-graduação, permitindo a entrada de corpos e saberes negros e originários na produção do saber.",
        "A proibição de conferências públicas que tratem de temas relacionados à história do trabalho rural.",
        "A exigência de que todos os exames finais de medicina sejam realizados em latim clássico da Antiguidade.",
        "O cancelamento de pesquisas dedicadas ao estudo do clima e da preservação de bacias hidrográficas.",
        "B",
        "As cotas raciais democratizam a universidade: ao incluir estudantes e pesquisadores negros e indígenas, desmantelam o monopólio da branquitude e abrem espaço para epistemologias plurais e emancipatórias."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Qual é a crítica dos pensadores das Epistemologias do Sul ao conceito liberal clássico de Direitos Humanos quando formulado de modo abstrato e descontextualizado?",
        "Eles afirmam que os direitos humanos foram inventados para beneficiar apenas marinheiros em travessias oceânicas.",
        "Eles apontam que, sem a devida contextualização e diálogo intercultural, os direitos humanos podem funcionar como uma nova cartilha civilizatória imperialista imposta de cima para baixo pelo Ocidente sobre o Sul Global.",
        "Eles defendem que a tortura e os castigos corporais devem ser autorizados em disputas de tribunal civil.",
        "Eles sustentam que os direitos de cidadania devem pertencer exclusivamente aos donos de indústrias químicas.",
        "Eles exigem que as sentenças dos juízes sejam escritas em versos métricos de teatro dramático.",
        "B",
        "Para Boaventura, os direitos humanos devem ser descolonizados através da tradução intercultural para não servirem como disfarce moral de intervenções imperiais sobre povos soberanos do Sul."
    ))

    questoes_brutas.append((
        37, "EM13CHS502", "intermediario",
        "No resgate de matrizes filosóficas africanas, o princípio da ética de Maat (originária do Antigo Egito / Kemet) fundamenta qual visão de mundo?",
        "Uma doutrina de conflito armado perpétuo entre nações que disputam jazidas de minério de ferro.",
        "Um imperativo cósmico e social de harmonia, equilíbrio, reciprocidade, justiça distributiva e verdade que organiza a convivência cívica e a relação com a natureza.",
        "Um sistema contábil voltado exclusivamente ao cálculo de juros sobre dívidas financeiras de agricultores.",
        "Uma teoria mecanicista que afirma que o universo é composto de peças de madeira que giram no escuro.",
        "Um conjunto de ordens militares que proibiam a prática de cantos poéticos nos mercados públicos da cidade.",
        "B",
        "Maat representa a busca inegociável da retidão, justiça, ordem e equilíbrio cósmico-social, demonstrando a profundidade ética da filosofia kemética africana muito antes da Grécia clássica."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "Sueli Carneiro ressalta que o epistemicídio se articula diretamente com o genocídio físico da população negra no Brasil contemporâneo. De que maneira esses dois processos se alimentam mutuamente?",
        "Pela importação de tecidos de algodão de fábricas europeias que diminuem a oferta de empregos na tecelagem.",
        "Ao desumanizar simbolicamente os corpos negros e declará-los desprovidos de valor intelectual e moral, o epistemicídio naturaliza e legitima perante a sociedade a violência policial e o extermínio da juventude negra.",
        "Por meio da suspensão de linhas de crédito bancário para agricultores que cultivam lavouras de feijão.",
        "Pela aprovação de leis municipais que exigem o uso de uniformes escuros em repartições públicas.",
        "Através da construção de hospitais com quartos pintados de verde em cidades do interior do país.",
        "B",
        "A desumanização cognitiva prepara a violência física: ao rebaixar o negro à condição de 'Não-Ser' sem valor e perigoso, o racismo estrutural justifica a violência estatal e a indiferença coletiva à morte de jovens negros."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "O conceito de 'Bem Viver' (Sumak Kawsay em quéchua e Suma Qamaña em aimará), incorporado em constituições de países andinos, propõe qual alternativa conceitual e ecológica ao modelo ocidental de desenvolvimento?",
        "A aceleração desenfreada da extração de petróleo e minérios para acumular reservas de dólares no tesouro nacional.",
        "Uma cosmovisão harmônica que subordina a economia à reprodução da vida comunitária e aos direitos da Mãe Terra (Pachamama), superando o produtivismo predatório capitalista.",
        "A construção de rodovias de asfalto cruzando reservas florestais para facilitar a passagem de carretas pesadas.",
        "A substituição de lavouras de alimentos por indústrias de montagem de automóveis de passageiros.",
        "O fechamento de escolas de aldeias rurais para transferir os jovens para centros urbanos industriais.",
        "B",
        "O Bem Viver é uma cosmovisão indígena originária descolonial: recusa o dogma do crescimento econômico infinito predatório e propõe a plenitude de vida em equilíbrio comunitário com a natureza."
    ))

    questoes_brutas.append((
        40, "EM13CHS502", "intermediario",
        "A descolonização do currículo escolar de Filosofia no Ensino Médio, conforme exigido pelas diretrizes da BNCC e leis antirracistas, exige que os professores adotem qual conduta pedagógica?",
        "Substituir todos os livros de história por compêndios de leis aprovados por generais militares condecorados.",
        "Romper com o monopólio exclusivo de filósofos homens brancos europeus, integrando pensadoras negras, sistemas filosóficos africanos, epistemologias ameríndias e saberes descoloniais no centro dos debates.",
        "Proibir que os alunos façam perguntas críticas sobre o passado colonial durante as aulas de humanidades.",
        "Exigir que todos os estudantes decorem em silêncio nomes de batalhas marítimas ocorridas no século XVIII.",
        "Limitar as aulas de filosofia ao estudo exclusivo de manuais de etiqueta palaciana de cortes reais francesas.",
        "B",
        "A descolonização curricular desmantela o eurocentrismo dogmático, apresentando a filosofia como patrimônio plural de toda a humanidade e fortalecendo o pensamento crítico e a diversidade na escola."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a passagem clássica de Walter Mignolo: 'O pensamento descolonial não se propõe como uma nova verdade universal, mas como uma opção que desmascara a hybris do Ponto Zero.' De que maneira essa crítica desmonta a pretensão de universalidade da filosofia europeia moderna?",
        "Negando que os filósofos da Europa tenham escrito textos lógicos com regras gramaticais corretas.",
        "Evidenciando que a razão ocidental moderna é uma tradição etnocêntrica e provinciana específica que mascarou seus interesses geopolíticos de conquista sob o manto de um saber pretensamente desincorporado e divino.",
        "Exigindo que as universidades de países do Norte Global fechem todos os cursos de ciências naturais.",
        "Provando que a matemática foi inventada por mercadores de tecidos da Península Itálica no século XV.",
        "Proibindo o uso de termos em latim nos relatórios de pesquisas acadêmicas de universidades públicas.",
        "B",
        "**Etapa 1:** Interpretar o conceito de 'desmascaramento do Ponto Zero': a razão moderna europeia finge falar de lugar nenhum (universalismo abstrato), mas fala a partir do centro imperial colonizador.\n**Etapa 2:** Concluir que a opção descolonial descentra a Europa: revela que o universalismo abstrato foi o álibi teórico da dominação, reivindicando a pluriversalidade de saberes situados e legítimos."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em sua tese de doutoramento, Sueli Carneiro afirma: 'O epistemicídio é um processo de deslegitimação de um grupo como portador de saber, que atua pela via da inferiorização e da produção sistemática do Outro como Não-Ser.' Qual conexão estrutural Carneiro estabelece entre a negação do saber e a manutenção da hierarquia racial no Brasil?",
        "Ela afirma que as leis de trânsito em cidades litorâneas foram aprovadas para beneficiar motoristas de carruagens.",
        "Ela demonstra que a privação do estatuto de sujeito do conhecimento é a condição indispensável para justificar a subordinação social, política e econômica da população negra, tornando a desigualdade naturalizada perante o senso comum.",
        "Ela comprova que as escolas públicas municipais utilizavam cartilhas escolares impressas em línguas asiáticas.",
        "Ela sustenta que o cultivo do algodão em fazendas coloniais exigia que os escravizados decorassem poemas dramáticos.",
        "Ela defende que o racismo é um fenômeno psicológico passageiro que desaparece espontaneamente com o tempo.",
        "B",
        "**Etapa 1:** Analisar o mecanismo de produção da subalternidade: para dominar um povo sem resistência permanente, é preciso assassinar sua confiança em sua própria inteligência e tradição cultural.\n**Etapa 2:** Evidenciar que o epistemicídio legitima a estratificação de castas raciais no Brasil: ao destituir o negro da condição de produtor de saber universal, naturaliza-se sua presença apenas nos trabalhos braçais e desvalorizados."
    ))

    questoes_brutas.append((
        43, "EM13CHS502", "dificil",
        "Considere o projeto de Ngũgĩ wa Thiong'o ao decidir abandonar a escrita literária em língua inglesa para publicar seus romances e ensaios exclusivamente em Gikuyu (sua língua materna queniana). Qual argumento filosófico descolonial fundamentou essa decisão radical?",
        "Ele pretendia economizar gastos de envio de correspondências para editoras da cidade de Londres.",
        "Ele sustentou que a língua não é apenas uma ferramenta neutra de comunicação, mas o repositório vivo da memória, da identidade e da cosmovisão de um povo; escrever na língua materna é um ato de desobediência epistêmica e reconexão com a comunidade originária.",
        "Ele afirmou que a língua inglesa perdeu sua utilidade após o surgimento das ferrovias de vapor no século XIX.",
        "Ele foi proibido por decretos governamentais da África Oriental de utilizar o alfabeto latino em livros.",
        "Ele acreditava que os animais da savana entendiam apenas as palavras pronunciadas em línguas locais.",
        "B",
        "**Etapa 1:** Compreender a tese central de Descolonizar a Mente sobre o papel existencial e cultural da língua na formação do sujeito.\n**Etapa 2:** Concluir que a renúncia à língua do colonizador constitui um ato revolucionário de restauração da soberania mental e cultural africana, desmantelando a alienação subjetiva provocada pelo imperialismo linguístico."
    ))

    questoes_brutas.append((
        44, "EM13CHS101", "dificil",
        "Boaventura de Sousa Santos argumenta que o modelo dominante de ciência ocidental cometeu reiteradamente o crime de 'desperdício da experiência'. Como a 'Sociologia das Emergências' opera para superar esse desperdício na luta contemporânea por justiça social?",
        "Promovendo o fechamento de laboratórios de física nuclear por tempo indeterminado nas capitais ocidentais.",
        "Investigando os sinais embrionários de alternativas emancipatórias que já brotam nas lutas populares do Sul Global, expandindo o campo das possibilidades históricas contra o fatalismo da globalização neoliberal.",
        "Obrigando os agricultores familiares a utilizarem apenas sementes híbridas fornecidas por multinacionais químicas.",
        "Substituindo a votação de leis em parlamentos pela consulta a sacerdotes de templos religiosos antigos.",
        "Proibindo o uso de computadores eletrônicos em pesquisas dedicadas ao estudo do clima global.",
        "B",
        "**Etapa 1:** Compreender a Sociologia das Emergências em articulação com o conceito de 'Ainda-Não' (Ernst Bloch).\n**Etapa 2:** Concluir que ela atua identificando sementes de resistência e utopias concretas presentes no Sul Global (ecologia camponesa, feminismos comunitários, economia solidária), mostrando que outro mundo é viável e já está em gestação."
    ))

    questoes_brutas.append((
        45, "EM13CHS102", "dificil",
        "Ao examinar a tese de Sueli Carneiro sobre 'A Construção do Outro como Não-Ser como Fundamento do Ser', como a autora articula a questão da branquitude como norma universal não declarada?",
        "Mostrando que a branquitude é uma criação mágica de poetas trágicos da Antiguidade grega sem efeitos práticos.",
        "Demonstrando que o sujeito branco eurocêntrico colocou a si mesmo como o padrão ideal invisível e neutro de humanidade, convertendo todas as diferenças raciais e de gênero em desvios inferiores que justificam o privilégio estrutural da branquitude.",
        "Provando que as diferenças raciais foram inventadas por comerciantes que vendiam tecidos de seda em portos da Ásia.",
        "Exigindo que os tribunais civis aprovem certidões de nascimento que proíbam o uso de sobrenomes europeus.",
        "Afirmando que a história do Brasil não possui registros de trabalho escravizado em fazendas agrícolas.",
        "B",
        "**Etapa 1:** Analisar o conceito crítico de 'branquitude' como posição de poder estrutural e privilégio não examinado.\n**Etapa 2:** Evidenciar a perspicácia de Sueli Carneiro: o branco nunca se vê como uma raça particular, mas como o próprio universal humano, enquanto o negro e o indígena são marcados pela racialização e empurrados para o lugar do Não-Ser."
    ))

    questoes_brutas.append((
        46, "EM13CHS502", "dificil",
        "Em contraposição ao individualismo possessivo eurocêntrico, a filosofia moral africana do Ubuntu sintetizada no aforismo 'Umwntu ngumuntu ngabantu' (Eu sou porque nós somos) propõe qual fundamento para a ética e a comunidade?",
        "A acumulação ilimitada de propriedades privadas de terra com a exclusão de vizinhos e parentes.",
        "A compreensão de que a humanidade de uma pessoa não é um atributo isolado e egoísta, mas uma realização relacional e comunitária indissociável da dignidade e do bem-estar dos outros membros do grupo.",
        "A exigência de que todos os cidadãos prestem juramento militar a governantes absolutistas da capital.",
        "A obrigação cívica de competir agressivamente no comércio exterior para levar empresas rivais à falência.",
        "A tese de que a solidão absoluta em florestas montanhosas é o único caminho para a sabedoria moral.",
        "B",
        "**Etapa 1:** Contrastar a concepção relacional do ser africana com o atomismo individualista do contrato social hobbesiano e lockeano.\n**Etapa 2:** Concluir que a ética do Ubuntu coloca a interdependência e a solidariedade como premissas existenciais: ninguém se torna humano sozinho; minha humanidade realiza-se no cuidado e no respeito à humanidade do outro."
    ))

    questoes_brutas.append((
        47, "EM13CHS101", "dificil",
        "Ao examinar a relação entre o conceito de 'Pensamento Abissal' de Boaventura e as práticas de colonialismo interno no Brasil, cientistas sociais evidenciam que a Linha Abissal se reproduz internamente nas cidades brasileiras porque:",
        "As leis de zoneamento urbano exigem que as casas de bairros nobres sejam construídas com telhas de barro vermelho.",
        "As fronteiras urbanas dividem a cidade entre os bairros ricos (onde os direitos constitucionais e o devido processo legal são garantidos) e as favelas e periferias (onde vigora o estado de exceção, a violência policial letal e a suspensão tácita de direitos fundamentais para a população negra).",
        "Os transportes públicos de ônibus circulam com velocidades reguladas por estações do ano no litoral.",
        "As praias municipais foram cercadas com muros de concreto para impedir o desembarque de peixes marinhos.",
        "As bibliotecas escolares foram fechadas para permitir a instalação de oficinas de calçados de couro.",
        "B",
        "**Etapa 1:** Aplicar a cartografia da linha abissal à segregação socioespacial e racial das metrópoles brasileiras contemporâneas.\n**Etapa 2:** Concluir que o pensamento abissal opera dentro do território nacional: nas favelas e periferias, os corpos negros vivem 'do outro lado da linha', sob a naturalização do arbítrio, das operações policiais violentas e da negação da cidadania plena."
    ))

    questoes_brutas.append((
        48, "EM13CHS102", "dificil",
        "Na obra Pele Negra, Máscaras Brancas, Frantz Fanon formula o conceito de 'Zona do Não-Ser', no qual o sujeito colonizado é encurralado. Como Sueli Carneiro mobiliza esse conceito fanoniano para desvendar a experiência histórica da população negra no Brasil?",
        "Ela afirma que a população negra brasileira sempre teve acesso privilegiado aos cargos de magistratura pública.",
        "Ela demonstra que a Zona do Não-Ser é a morada existencial e política imposta ao negro pelo racismo estrutural: um espaço de invisibilidade social, negação da fala e esvaziamento de humanidade que exige a resistência epistêmica e a luta coletiva para afirmar o direito pleno ao Ser.",
        "Ela comprova que as manifestações culturais de matriz africana foram declaradas patrimônio oficial da coroa portuguesa no século XVII.",
        "Ela sustenta que o conceito de Fanon só tem validade para territórios insulares localizados no mar do Caribe.",
        "Ela defende que a democracia racial no Brasil eliminou todas as formas de discriminação social após a abolição de 1888.",
        "B",
        "**Etapa 1:** Compreender a categoria existencial e sociopolítica da 'Zona do Não-Ser' formulada por Frantz Fanon.\n**Etapa 2:** Reconhecer a aplicação genial feita por Sueli Carneiro: a zona do não-ser no Brasil é mantida pelo mito da democracia racial e pelo epistemicídio, exigindo a descolonização das mentes e a afirmação afirmativa da identidade e dos saberes negros."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Ao aprofundar a crítica descolonial em diálogo com Aníbal Quijano e Walter Mignolo, teóricos latino-americanos articulam a 'Colonialidade do Ser' como desdobramento da colonialidade do poder e do saber. Qual a especificidade dessa dimensão existencial da opressão colonial?",
        "Ela se refere exclusivamente aos custos de transporte marítimo de mercadorias entre continentes.",
        "Ela descreve a desumanização profunda que torna a vida do colonizado dispensável e matável, naturalizando o sofrimento, o trauma psicológico e a violência contra corpos negros e indígenas como se fosse uma condição inerente à sua própria natureza.",
        "Ela trata do treinamento esportivo de jovens que participam de competições atléticas em escolas rurais.",
        "Ela estabelece que as leis da física deixam de funcionar quando o navio cruza a linha imaginária do equador.",
        "Ela exige que os operários de indústrias de calçados usem roupas cerimoniais durante o expediente de trabalho.",
        "B",
        "**Etapa 1:** Diferenciar as três dimensões da matriz colonial: colonialidade do poder (economia/trabalho), do saber (epistemologia) e do ser (existência e humanidade).\n**Etapa 2:** Evidenciar que a colonialidade do ser atinge a própria dignidade existencial: corrói o sentido de humanidade do colonizado, tornando a sua morte e o seu sofrimento fatos rotineiros e desprovidos de luto social no mundo moderno."
    ))

    questoes_brutas.append((
        50, "EM13CHS502", "dificil",
        "Em contraposição à razão indolente ocidental, o filósofo brasileiro Renato Noguera propõe a 'Afroperspectividade' como paradigma pedagógico e filosófico. Em que consiste a afroperspectividade no ensino de filosofia?",
        "Na substituição do método da ciência por rituais de adivinhação oracular noturnos nas salas de aula.",
        "Em tomar as experiências históricas, poéticas, míticas e filosóficas dos povos africanos e da diáspora negra como lentes legítimas e fecundas para pensar os grandes dilemas da condição humana, da ética e da vida coletiva, descentrando o olhar eurocêntrico.",
        "Na proibição de que os estudantes leiam textos escritos por filósofos nascidos na Europa Ocidental.",
        "Na exigência de que todos os exames vestibulares cobrem apenas questões sobre a geografia do deserto do Saara.",
        "No cancelamento de todas as aulas de história universal em escolas de educação básica do país.",
        "B",
        "**Etapa 1:** Compreender a definição de Afroperspectividade como posicionamento ético, político e teórico inovador.\n**Etapa 2:** Concluir com Renato Noguera: não se trata de um essencialismo reverso, mas de ampliar a pluralidade da filosofia, reconhecendo que a matriz africana oferece respostas sofisticadas para a convivência comunitária, a arte e a emancipação humana."
    ))

    questoes_brutas.append((
        51, "EM13CHS102", "dificil",
        "Ao examinar a relação entre o mito da 'Democracia Racial' brasileira e o epistemicídio, intelectuais negros demonstram que essa ideologia atuou de forma perversa porque:",
        "Incentivou a criação de partidos políticos exclusivos para trabalhadores rurais de ascendência europeia.",
        "Camuflou o racismo estrutural sob o discurso da harmonia e da miscigenação cordial, desarmando a denúncia das desigualdades, culpabilizando os próprios negros pelo seu fracasso social e desqualificando o debate racial como 'vitimismo'.",
        "Proibiu a realização de festas de carnaval em cidades litorâneas durante o início do ano civil.",
        "Determinou que as universidades públicas distribuíssem bolsas de estudo em dinheiro apenas para imigrantes asiáticos.",
        "Obrigou os operários de fábricas têxteis a assinarem contratos de trabalho escritos em latim arcaico.",
        "B",
        "**Etapa 1:** Analisar a funcionalidade ideológica do mito da democracia racial formulado a partir de leituras domesticadas de Gilberto Freyre.\n**Etapa 2:** Evidenciar como ela opera o epistemicídio: ao negar a existência do racismo, interdita a produção de conceitos críticos que nomeiem a opressão, bloqueando políticas públicas de reparação e mantendo o privilégio branco intacto."
    ))

    questoes_brutas.append((
        52, "EM13CHS101", "dificil",
        "Boaventura de Sousa Santos utiliza a expressão 'Epistemicídio Massivo' para denunciar a destruição de saberes ancestrais ao longo da expansão colonial europeia (a queima de códices maias e astecas, a inquisição contra curandeiras e parteiras, e o apagamento de cosmologias africanas). Qual prejuízo civilizatório global essa destruição impôs à humanidade?",
        "A perda de moedas de prata que estavam enterradas nas areias de praias oceânicas.",
        "O empobrecimento cognitivo e existencial do mundo, que perdeu uma imensa riqueza de respostas éticas, ecológicas e medicinais para enfrentar crises ecológicas e humanas, ficando prisioneiro de uma única racionalidade predatória.",
        "A impossibilidade de realizar competições de navegação a vela com barcos movidos a remo no mar Egeu.",
        "O aumento do número de páginas em branco nos cadernos escolares distribuídos a estudantes de direito.",
        "A extinção definitiva de todas as línguas antigas faladas em ilhas do mar Mediterrâneo.",
        "B",
        "**Etapa 1:** Avaliar o impacto do epistemicídio histórico sobre o patrimônio imaterial da humanidade.\n**Etapa 2:** Concluir com as Epistemologias do Sul: a monocultura do saber ocidental empobreceu o planeta; ao destruir saberes ancestrais sobre sustentabilidade e cuidado comunitário, a humanidade perdeu repertórios indispensáveis para enfrentar o colapso ecológico moderno."
    ))

    questoes_brutas.append((
        53, "EM13CHS502", "dificil",
        "Ao tratar da cosmologia ameríndia do 'Perspectivismo Animista' (investigada por antropólogos e filósofos a partir de povos da Amazônia), qual ruptura conceitual radical com o naturalismo moderno ocidental se estabelece?",
        "A crença de que as plantas e animais não possuem nenhuma relação física com o solo da floresta tropical.",
        "A concepção de que a condição comum original a todos os seres do cosmos é a humanidade (possuem alma e agência social), variando apenas as vestes corporais biológicas pelas quais enxergam a realidade, superando a divisão ocidental entre natureza e cultura.",
        "A proposta de que os animais da floresta devem ser matriculados em escolas públicas para aprenderem matemática.",
        "A exigência de que os cientistas de laboratório usem penas de arara nos chapéus durante os experimentos químicos.",
        "O fechamento de postos de saúde em aldeias indígenas para impedir o uso de remédios de farmácia.",
        "B",
        "**Etapa 1:** Descrever o perspectivismo ameríndio (Eduardo Viveiros de Castro, Davi Kopenawa e Ailton Krenak): enquanto o Ocidente vê uma natureza e múltiplas culturas, o pensamento ameríndio vê uma cultura cósmica comum e múltiplos corpos.\n**Etapa 2:** Evidenciar que essa epistemologia desestabiliza a arrogância antropocêntrica moderna: animais e espíritos da floresta são sujeitos portadores de ponto de vista, demandando respeito ético e diplomacia cósmica."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Em sua obra A Construção do Outro como Não-Ser como Fundamento do Ser, Sueli Carneiro alerta que as políticas universalistas neutras para a educação (que recusam ações afirmativas sob o argumento de que 'todos são iguais perante a lei') produzem na prática:",
        "A eliminação imediata de qualquer forma de evasão escolar em colégios públicos de bairros periféricos.",
        "A perpetuação e o aprofundamento das desigualdades raciais históricas, pois tratar de forma igualitária abstrata grupos que sofreram séculos de desvantagens e violências desiguais consolida os privilégios da branquitude.",
        "A obrigatoriedade de que todos os alunos de ensino médio ingressem simultaneamente no mercado de trabalho fabril.",
        "A diminuição dos recursos financeiros destinados à compra de merenda escolar em escolas rurais do país.",
        "O aumento do número de professores formados em matemática pura em universidades federais.",
        "B",
        "**Etapa 1:** Compreender a crítica ao universalismo liberal cego às desigualdades de partida e à opressão histórica.\n**Etapa 2:** Concluir com Sueli Carneiro: o universalismo formal abstrato é cúmplice do racismo estrutural; a justiça real exige a equidade substantiva (tratar desigualmente os desiguais na medida de suas desigualdades) por meio de cotas e reparações ativas."
    ))

    questoes_brutas.append((
        55, "EM13CHS101", "dificil",
        "O filósofo camaronês Achille Mbembe, ao dialogar com a crítica descolonial em obras como Crítica da Razão Negra, argumenta que o conceito de 'Negro' foi inventado pela modernidade ocidental como:",
        "Um título de nobreza reservado a generais militares condecorados em guerras coloniais.",
        "Uma categoria jurídica, econômica e simbólica de desumanização que permitiu transformar o ser humano em mercadoria vendável, moeda viva de troca e força bruta de trabalho nas plantações escravistas transatlânticas.",
        "Uma técnica de pintura mural utilizada por artistas do Renascimento em palácios europeus.",
        "Um cálculo numérico adotado por banqueiros de Amsterdã para calcular o peso de barras de ouro.",
        "Uma sociedade secreta de navegadores encarregada de desviar navios mercantes no mar do Caribe.",
        "B",
        "**Etapa 1:** Analisar a gênese do significante 'Negro' no contexto do capitalismo mercantil e do tráfico transatlântico de escravizados.\n**Etapa 2:** Evidenciar que Mbembe demonstra que o Negro foi fabricado como a mercadoria viva por excelência: a privação do nome, da história e do saber (epistemicídio) viabilizou a extração de mais-valia e a acumulação primitiva de capital da Europa."
    ))

    questoes_brutas.append((
        56, "EM13CHS502", "dificil",
        "Ao analisar a obra de intelectuais como Lélia Gonzalez e seu conceito de 'Amefricanidade', percebe-se uma síntese pioneira de descolonização teórica no Brasil. Em que consiste a Amefricanidade?",
        "Na defesa de que todos os habitantes da América do Sul devem falar a mesma língua falada no norte da Europa.",
        "Na afirmação de uma identidade histórica e cultural forjada pela resistência e recriação de negros e indígenas nas Américas, desmascarando a ilusão eurocêntrica e valorizando as raízes afro-ameríndias na formação de nossa civilização.",
        "No fechamento das fronteiras nacionais para impedir o desembarque de navios cargueiros estrangeiros.",
        "Na exigência de que os cursos universitários de direito adotem apenas o código civil dos imperadores romanos.",
        "Na proibição do uso de instrumentos musicais de percussão em festividades públicas de cidades costeiras.",
        "B",
        "**Etapa 1:** Interpretar o conceito seminal de Amefricanidade formulado por Lélia Gonzalez.\n**Etapa 2:** Reconhecer que a Amefricanidade descentra o modelo eurocêntrico da América: resgata a presença negra e indígena na linguagem ('pretuguês'), nos costumes e na luta política como alicerces da identidade descolonial do continente."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "A crítica descolonial recusa a tese de que a história universal avança em uma linha temporal única e linear rumo ao modelo de civilização do Ocidente. Qual concepção temporal alternativa os pensadores do Sul reivindicam?",
        "A crença de que o tempo anda de trás para a frente toda vez que os astrônomos observam a lua cheia no horizonte.",
        "Uma concepção pluriversal e heterocrônica da história, em que diferentes povos e culturas vivem tempos múltiplos, legítimos e contemporâneos entre si, sem obrigação de convergir para o modelo ocidental capitalista.",
        "A obrigação de que todos os calendários do mundo adotem o mesmo início de ano civil aprovado em Roma.",
        "A determinação de que os relógios de sol devem ser instalados em todas as salas de aula de escolas públicas.",
        "A certeza de que a humanidade retornará ao modo de vida de caçadores nômades no próximo século.",
        "B",
        "**Etapa 1:** Criticar o evolucionismo linear eurocêntrico (Hegel e positivismo), que coloca a Europa no cume do progresso e o resto do mundo no passado 'atrasado'.\n**Etapa 2:** Evidenciar que a descolonialidade propõe a contemporaneidade dos tempos: os povos indígenas e africanos não são o passado da humanidade; são sujeitos do presente com visões válidas de futuro para a coexistência planetária."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Em seu livro Lugar de Fala, a filósofa Djamila Ribeiro, dialogando com Sueli Carneiro e Patricia Hill Collins, esclarece que 'lugar de fala' não significa censurar quem pode ou não falar sobre um tema, mas:",
        "Exigir que as pessoas apresentem certidões de nascimento antes de entrar em salas de conferências públicas.",
        "Compreender que todo discurso parte de uma localização social, racial e de gênero específica na hierarquia de poder, exigindo que os sujeitos dominantes reconheçam seus privilégios e que os grupos historicamente silenciados tenham sua autoridade de fala legítima garantida.",
        "Proibir que homens brancos leiam livros de literatura escritos por mulheres de outros continentes.",
        "Determinar que os debates parlamentares sejam realizados apenas por meio de cartas anônimas enviadas pelo correio.",
        "Cancelar as eleições municipais em cidades que não possuam conselhos de defesa de direitos humanos.",
        "B",
        "**Etapa 1:** Desmistificar a falsa caricatura de que o 'lugar de fala' seria uma interdição individual de debate.\n**Etapa 2:** Concluir com a teoria do ponto de vista feminista negro: o lugar de fala é um conceito estrutural que denuncia quem historicamente teve o monopólio da fala e reivindica a quebra da invisibilidade das vozes subalternizadas no espaço público."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "Ao examinar a relação entre Epistemicídio e Racismo Ambiental no Brasil, ativistas e teóricos descoloniais constatam que o apagamento de saberes tradicionais facilita a degradação da natureza porque:",
        "Os cientistas de laboratório químico utilizam água tratada para lavar vidrarias de ensaio.",
        "Ao desqualificar as comunidades quilombolas, ribeirinhas e indígenas como 'atrasadas e ignorantes', o poder público e o agronegócio predatório justificam a invasão de seus territórios ancestrais, a contaminação de seus rios por mercúrio e a destruição de seus ecossistemas sagrados sem consulta prévia informada.",
        "Os pescadores artesanais utilizam redes de tecido que se desgastam com o sal marinho durante o inverno.",
        "As leis de proteção ambiental exigem que as árvores de florestas públicas sejam podadas a cada seis meses.",
        "Os agricultores familiares se recusam a utilizar tratores elétricos em suas hortas comunitárias de verduras.",
        "B",
        "**Etapa 1:** Conectar o epistemicídio à destruição socioambiental territorial (racismo ambiental).\n**Etapa 2:** Evidenciar que o silenciamento dos saberes ancestrais de manejo sustentável serve como justificativa ideológica para o avanço da mineração e grilagem: se o saber da comunidade não vale nada, seu território pode ser saqueado sem dilemas éticos."
    ))

    questoes_brutas.append((
        60, "EM13CHS502", "dificil",
        "Ao sintetizar a emergência das Epistemologias do Sul, a crítica ao epistemicídio de Sueli Carneiro e o projeto de descolonização da mente, qual horizonte emancipatório perene se descortina para a educação e a cidadania democrática no século XXI?",
        "A substituição do modelo de dominação europeu por um novo império militar autoritário instalado no Sul Global.",
        "A construção de uma Pluriversidade radical de saberes, em que o diálogo intercultural simétrico, o desmantelamento do racismo estrutural e o reconhecimento da dignidade cognitiva de todos os povos fundamentem uma sociedade verdadeiramente livre, justa e solidária.",
        "O abandono definitivo da escrita e da leitura de livros didáticos em todas as escolas públicas do planeta.",
        "A imposição de tributos municipais sobre a venda de cadernos escolares de papel reciclado em feiras livres.",
        "O fechamento dos tribunais que julgam causas de direitos civis em nações com democracias consolidadas.",
        "B",
        "**Etapa 1:** Sintetizar o sentido transformador da luta contra o epistemicídio e a colonialidade do saber.\n**Etapa 2:** Concluir que o horizonte descolonial não é o ódio ou o isolamento, mas a Pluriversalidade: um mundo onde caibam muitos mundos e onde a justiça social seja coroada pela justiça cognitiva e pelo florescimento de todas as humanidades."
    ))

    # Auditoria de vocabulário e blacklist
    padroes_proibidos = [
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
        r"\baqueloutro\w*\b", r"R\$\s*\d"
    ]

    print(f"Total de questões brutas: {len(questoes_brutas)}")
    assert len(questoes_brutas) == 60, f"Erro: esperava 60, obteve {len(questoes_brutas)}"

    # Balanceamento de gabaritos
    questoes = balancear_questoes(questoes_brutas)

    # Teste de termos proibidos em todas as questões
    erros_termos = []
    for q in questoes:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        texto_q = f"{enunc} {a} {b} {c} {d} {e} {res}".lower()
        for pat in padroes_proibidos:
            m = re.search(pat, texto_q)
            if m:
                erros_termos.append(f"Questão {num}: termo proibido '{m.group(0)}' encontrado!")

    if erros_termos:
        print("\n[ERRO NA AUDITORIA DE TERMOS PROIBIDOS]:")
        for err in erros_termos:
            print(f" - {err}")
        sys.exit(1)

    # Montagem do Markdown
    header = """---
série: "Ensino Médio"
disciplina: "Filosofia"
eixo: "eixo-1-epistemologia"
capitulo: "cap-08-epistemicidio-colonialidade-saber-sueli-carneiro"
objeto_de_conhecimento: "A Crítica Contemporânea ao Universalismo Abstrato Eurocêntrico: O Conceito Filosófico de Epistemicídio formulado por Boaventura de Sousa Santos e aprofundado por Sueli Carneiro em A Construção do Outro como Não-Ser como Fundamento do Ser; O Assassinato Simbólico, Marginalização e Invisibilização dos Saberes dos Povos Colonizados; A Colonialidade do Poder e do Saber (Aníbal Quijano e Walter Mignolo); Ngũgĩ wa Thiong'o e o Projeto Filosófico de Descolonizar a Mente; A Emergência das Epistemologias do Sul como Justiça Cognitiva Global (Lei 10.639/03)."
ebook_fonte: "em-fil-c08-epistemicidio-colonialidade-saber-sueli-carneiro.md"
habilidades: "EM13CHS101, EM13CHS102, EM13CHS103, EM13CHS502, EM13CHS601, H1, H2, H3, H11, H26"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: Epistemicídio, Colonialidade do Saber e Filosofias da Libertação

"""

    corpo = header
    gabaritos_finais = []

    # Nível Básico
    corpo += "## Nível Básico\n\n"
    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-08-epistemicidio-colonialidade-saber-sueli-carneiro -->\n"
        corpo += f"### Questão {num}\n\n"
        corpo += f"{enunc}\n\n"
        corpo += f"- (A) {a}\n"
        corpo += f"- (B) {b}\n"
        corpo += f"- (C) {c}\n"
        corpo += f"- (D) {d}\n"
        corpo += f"- (E) {e}\n\n"
        corpo += f"**Gabarito:** ({gab})\n\n"
        corpo += f"**Resolução Comentada:**\n{res}\n\n---\n\n"

    # Nível Intermediário
    corpo += "## Nível Intermediário\n\n"
    for q in questoes[20:40]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-08-epistemicidio-colonialidade-saber-sueli-carneiro -->\n"
        corpo += f"### Questão {num}\n\n"
        corpo += f"{enunc}\n\n"
        corpo += f"- (A) {a}\n"
        corpo += f"- (B) {b}\n"
        corpo += f"- (C) {c}\n"
        corpo += f"- (D) {d}\n"
        corpo += f"- (E) {e}\n\n"
        corpo += f"**Gabarito:** ({gab})\n\n"
        corpo += f"**Resolução Comentada:**\n{res}\n\n---\n\n"

    # Nível Difícil
    corpo += "## Nível Difícil\n\n"
    for q in questoes[40:]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-08-epistemicidio-colonialidade-saber-sueli-carneiro -->\n"
        corpo += f"### Questão {num}\n\n"
        corpo += f"{enunc}\n\n"
        corpo += f"- (A) {a}\n"
        corpo += f"- (B) {b}\n"
        corpo += f"- (C) {c}\n"
        corpo += f"- (D) {d}\n"
        corpo += f"- (E) {e}\n\n"
        corpo += f"**Gabarito:** ({gab})\n\n"
        corpo += f"**Resolução Comentada:**\n{res}\n\n---\n\n"

    corpo += """## Referências

- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.
- CARNEIRO, Sueli. *A Construção do Outro como Não-Ser como Fundamento do Ser*. Tese (Doutorado em Educação) — Faculdade de Educação, Universidade de São Paulo, São Paulo, 2005.
- FANON, Frantz. *Pele Negra, Máscaras Brancas*. Tradução de Renato da Silveira. Salvador: EDUFBA, 2008.
- MIGNOLO, Walter. *Histórias Locais/Projetos Globais: Colonialidade, Saberes Subalternos e Pensamento Liminar*. Belo Horizonte: Editora UFMG, 2003.
- NOGUERA, Renato. *O Ensino de Filosofia e a Lei 10.639*. Rio de Janeiro: Pallas/Biblioteca Nacional, 2014.
- QUIJANO, Aníbal. *Colonialidade do Poder, Eurocentrismo e América Latina*. In: LANDER, Edgardo (Org.). *A Colonialidade do Saber: Eurocentrismo e Ciências Sociais*. Buenos Aires: CLACSO, 2005.
- SANTOS, Boaventura de Sousa. *Para Além do Pensamento Abissal: Das Linhas Globais a uma Ecologia de Saberes*. Novos Estudos CEBRAP, São Paulo, n. 79, p. 71-94, 2007.
- THIONG'O, Ngũgĩ wa. *Descolonizar a Mente*. Tradução de Jamille Pinheiro Dias. São Paulo: Editora 34, 2021.
"""

    print("Total de Gabaritos detectados:", len(gabaritos_finais))
    print("Contagem por letra:", Counter(gabaritos_finais))

    assert len(gabaritos_finais) == 60
    assert all(count == 12 for count in Counter(gabaritos_finais).values()), "Gabarito desbalanceado!"

    print("[AUDITORIA INTERNA APROVADA] Todas as 60 questões atendem rigorosamente às travas pedagógicas!")

    # Grava rascunho temporário
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(corpo)
    print(f"Rascunho temporário salvo com sucesso ({len(corpo.encode('utf-8'))} bytes).")

    # Invoca o validador oficial
    cmd = [sys.executable, "validador_educamob.py", temp_draft, dest_path]
    print(f"Executando validador: {' '.join(cmd)}")
    res_val = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res_val.stdout)
    if res_val.stderr:
        print("[STDERR]:", res_val.stderr)

    if res_val.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 08 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {res_val.returncode}")
        sys.exit(res_val.returncode)

if __name__ == "__main__":
    gerar_cap08()
