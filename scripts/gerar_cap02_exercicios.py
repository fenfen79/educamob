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

def gerar_cap02():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-02-mito-ao-logos-pre-socraticos/ebooks/em-fil-c02-mito-ao-logos-pre-socraticos-exercicios.md"
    temp_draft = "temp_draft.md"

    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "A passagem do Mito ao Logos na Grécia Antiga caracterizou-se principalmente por qual mudança no modo de explicar a realidade?",
        "Substituição de narrativas sagradas e divinas por explicações racionais baseadas em causas naturais.",
        "Proibição imediata de qualquer forma de religiosidade cívica nas cidades gregas.",
        "Criação de academias militares para treinar soldados no combate a mitos persas.",
        "Adoção de rituais mágicos egípcios como método único para prever eclipses solares.",
        "Eliminação total do uso da poesia em cerimônias públicas e peças teatrais.",
        "A",
        "O Logos instaura a busca de causas naturais e argumentos demonstrativos em substituição à autoridade divina dos mitos."
    ))

    questoes_brutas.append((
        2, "EM13CHS103", "basico",
        "Segundo o helenista Jean-Pierre Vernant, qual transformação material favoreceu o desenvolvimento da razão na Grécia Arcaica?",
        "O isolamento geográfico que impediu qualquer contato com navegadores estrangeiros.",
        "A invenção da moeda cunhada e a expansão do comércio marítimo cosmopolita.",
        "A centralização do poder militar nas mãos de um rei absoluto de origem divina.",
        "A restrição do uso da escrita alfabética a uma casta fechada de sacerdotes.",
        "O abandono das navegações para priorizar a caça em florestas montanhosas.",
        "B",
        "A moeda, o comércio e a escrita fonética aberta criaram as bases sociais para o debate racional na pólis."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Os primeiros filósofos gregos foram chamados por Aristóteles de 'Fisiólogos' porque investigavam primordialmente qual objeto?",
        "A organização burocrática dos tribunais judiciais de Atenas.",
        "As leis de mercado que regulavam o preço de cereais no porto.",
        "A origem, a ordem e os processos de transformação da natureza (Physis).",
        "Os métodos retóricos empregados em campanhas eleitorais municipais.",
        "A vida pessoal dos imperadores persas que invadiram o mar Egeu.",
        "C",
        "Os fisiólogos dedicavam-se ao estudo racional da natureza (Physis) e à busca do princípio originário (Arché)."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "Qual elemento material foi escolhido por Tales de Mileto como o princípio gerador de todas as coisas vivas?",
        "O Fogo.",
        "A Água.",
        "A Terra.",
        "O Ar.",
        "O Vácuo.",
        "B",
        "Tales observou que a umidade alimenta as sementes e o calor vital, concluindo que a Água é a arché de tudo."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Anaximandro de Mileto propôs como princípio fundamental o Ápeiron, conceito que pode ser definido como:",
        "Uma substância gasosa invisível que se contrai para formar pedras.",
        "Um elemento mineral sólido encontrado no fundo dos oceanos.",
        "Uma substância primordial ilimitada, eterna e indeterminada.",
        "O calor gerado pela fricção de madeiras secas durante o verão.",
        "Uma combinação fixa de terra seca e água doce dos rios.",
        "C",
        "O Ápeiron é o princípio infinito e indeterminado de onde brotam e para onde retornam todos os elementos do cosmos."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "Anaxímenes de Mileto explicou as transformações da matéria a partir do Ar utilizando dois mecanismos físicos:",
        "Sublimação e cristalização rápida.",
        "Fusão nuclear e fissão atômica.",
        "Rarefação e condensação.",
        "Evaporação e fotossíntese natural.",
        "Erosão e sedimentação marinha.",
        "C",
        "Para Anaxímenes, a rarefação do ar gera o fogo, enquanto a sua condensação produz vento, nuvem, água, terra e pedra."
    ))

    questoes_brutas.append((
        7, "EM13CHS103", "basico",
        "Para a confraria fundada por Pitágoras de Samos, qual elemento inteligível constituía a essência e o princípio de todas as coisas?",
        "A matéria sólida palpável.",
        "O Número e a proporção matemática.",
        "O vapor expelido por vulcões ativos.",
        "A vontade impulsiva das multidões.",
        "O vácuo espacial infinito.",
        "B",
        "Os pitagóricos identificaram na proporção numérica e na harmonia matemática o fundamento ordenador do Universo."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "Heráclito de Éfeso formulou o pensamento do Devir (Panta Rhei), que se apoia na constatação de que:",
        "Todas as coisas estão em constante transformação e nada permanece idêntico.",
        "O Universo é estático e imutável perante os sentidos humanos.",
        "A matéria surgiu de um ato de criação mágica realizado em um único dia.",
        "Os seres vivos nunca sofrem alterações biológicas ao longo do tempo.",
        "A terra é sustentada por colunas de mármore construídas pelos deuses.",
        "A",
        "O devir heraclitiano expressa o fluxo perpétuo da realidade, onde tudo se move e se transforma sem cessar."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "A famosa metáfora do rio formulada por Heráclito ilustra qual ideia filosófica central?",
        "A constância inalterável das correntes marítimas durante as quatro estações.",
        "A impossibilidade de entrar duas vezes no mesmo rio, pois novas águas fluem sempre.",
        "O perigo de navegar por rios desconhecidos durante o período das cheias de inverno.",
        "A obrigação cívica de construir pontes de madeira para facilitar o comércio.",
        "A crença de que os rios eram moradas sagradas de ninfas protetoras da cidade.",
        "B",
        "A metáfora do rio sintetiza a impermanência radical: ao entrar novamente, as águas já mudaram e nós também mudamos."
    ))

    questoes_brutas.append((
        10, "EM13CHS101", "basico",
        "No poema Sobre a Natureza de Parmênides de Eleia, qual é a proposição lógica fundante da via da Verdade (Aletheia)?",
        "O Ser muda constantemente e convive em harmonia com o Não-Ser.",
        "O Ser é, e não pode não ser; o Não-Ser não é, e não pode ser.",
        "O Não-Ser é a matriz criadora de todos os objetos materiais visíveis.",
        "O conhecimento humano depende exclusivamente de opiniões sensíveis passageiras.",
        "O movimento dos corpos comprova a falsidade de qualquer raciocínio lógico.",
        "B",
        "Parmênides formula o princípio de identidade e não contradição: o Ser é pleno e eterno, e o Não-Ser é impensável."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Segundo Parmênides, o caminho da Opinião (Doxa) conduz o ser humano ao erro porque se baseia em qual faculdade?",
        "No cálculo matemático demonstrativo rigoroso.",
        "Na reflexão silenciosa do intelecto puro.",
        "Nos sentidos corporais enganosos que mostram mudança e multiplicidade.",
        "Nas consultas feitas a sacerdotes de templos dedicados a Apolo.",
        "Na leitura atenta de tratados de lógica formal clássica.",
        "C",
        "A Doxa repousa nos sentidos corpóreos ilusórios, que apresentam o nascimento, a morte e o movimento como se fossem reais."
    ))

    questoes_brutas.append((
        12, "EM13CHS101", "basico",
        "Zenão de Eleia criou seus célebres paradoxos lógicos com o objetivo principal de defender qual tese de seu mestre Parmênides?",
        "A comprovação prática de que a velocidade de Aquiles era infinita.",
        "A demonstração de que a crença na realidade do movimento gera contradições lógicas.",
        "A defesa do livre comércio de tartarugas nos mercados da Magna Grécia.",
        "A valorização dos jogos olímpicos como espaço de união entre as pólis.",
        "A necessidade de usar réguas de bronze em disputas atléticas de corrida.",
        "B",
        "Zenão usou o método da redução ao absurdo para provar que aceitar a divisibilidade do movimento incorre em aporias lógicas."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "A teoria pluralista de Empédocles de Agrigento estabeleceu que o Universo é composto por quantas raízes fundamentais?",
        "Uma única raiz material infinita: a poeira cósmica.",
        "Duas substâncias imateriais: a luz e a escuridão absoluta.",
        "Quatro elementos indestrutíveis: Fogo, Terra, Ar e Água.",
        "Dez números geométricos sagrados dispostos em triângulos.",
        "Infinitas sementes invisíveis desprovidas de qualquer forma.",
        "C",
        "Empédocles propôs as quatro raízes materiais eternas que se misturam e se separam pelas forças do Amor e do Ódio."
    ))

    questoes_brutas.append((
        14, "EM13CHS101", "basico",
        "Na cosmologia de Empédocles, quais forças cósmicas dinâmicas são responsáveis por unir e separar as quatro raízes da matéria?",
        "A Gravidade e o Eletromagnetismo.",
        "O Amor (Philia) e a Discórdia (Neikos).",
        "A Coragem cívica e a Covardia militar.",
        "O Vento solar e a Maré lunar.",
        "O Calor vulcânico e a Geada de inverno.",
        "B",
        "O Amor atrai e agrega os quatro elementos em harmonia, enquanto a Discórdia os repele e dispersa em ciclos cósmicos."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "Anaxágoras de Clazômenas introduziu na filosofia a ideia de uma Inteligência Cósmica ordenadora, designada pelo termo grego:",
        "Logos.",
        "Physis.",
        "Nous.",
        "Ápeiron.",
        "Kenon.",
        "C",
        "O Nous é a Mente Cósmica inteligente que pôs em rotação as sementes primordiais e organizou o cosmos com propósito."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Demócrito de Abdera definiu os Átomos como partículas materiais que possuem qual característica física fundamental?",
        "Partículas divisíveis ao infinito em partes cada vez mais macias.",
        "Fragmentos gelatinosos capazes de alterar sua cor com a luz solar.",
        "Partículas indivisíveis, eternas, impenetráveis e invisíveis aos olhos.",
        "Pontos matemáticos sem massa que desaparecem quando aquecidos.",
        "Gotas líquidas que evaporam rapidamente no espaço sideral.",
        "C",
        "O átomo (que significa literalmente 'sem divisão') é uma unidade sólida, eterna e indivisível de matéria pura."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Para que os átomos pudessem se movimentar e colidir livremente, o atomismo de Leucipo e Demócrito postulou a existência de qual elemento?",
        "Do Fogo divino sagrado.",
        "Do Vácuo ou espaço vazio (Kenon).",
        "De correntes de água subterrâneas.",
        "De campos magnéticos gerados pelos astros.",
        "De raios luminosos emitidos por deuses olímpicos.",
        "B",
        "O vácuo é a condição física necessária para que os átomos circulem, colidam e se agreguem formando os corpos materiais."
    ))

    questoes_brutas.append((
        18, "EM13CHS103", "basico",
        "A praça pública das cidades gregas (Ágora) tornou-se o centro da pólis porque nela ocorria qual prática essencial à cidadania?",
        "O comércio clandestino de escravizados capturados em alto-mar.",
        "O debate público e o confronto de argumentos entre cidadãos livres.",
        "A coroação de reis absolutistas em cerimônias de lealdade armada.",
        "O sacrifício obrigatório de prisioneiros de guerras territoriais.",
        "A cobrança compulsória de pedágio para carretas de transporte rural.",
        "B",
        "Na ágora, os cidadãos deliberavam sobre as leis por meio do debate argumentativo, da persuasão racional e da isonomia."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Heráclito escolheu o Fogo Eterno como símbolo supremo do cosmos porque essa substância material manifesta de forma exemplar:",
        "A imobilidade perfeita e a solidez permanente das montanhas.",
        "O consumo, a transformação e a renovação ininterrupta da matéria.",
        "A temperatura constante necessária para preservar peças de ferro.",
        "A frieza calculadora requerida para comandar batalhas navais.",
        "A escuridão profunda que envolve os oceanos durante a noite.",
        "B",
        "O fogo vive da morte do combustível e gera cinzas e calor, representando visualmente a dinâmica do devir perpétuo."
    ))

    questoes_brutas.append((
        20, "EM13CHS105", "basico",
        "O alfabeto fonético grego contribuiu para a democratização do saber porque, diferentemente de escritas hieroglíficas antigas:",
        "Era composto por poucos signos acessíveis, permitindo que a lei fosse lida por qualquer cidadão.",
        "Exigia dez anos de internato em templos religiosos para ser compreendido.",
        "Podia ser escrito exclusivamente com tinta de ouro em pergaminhos reais.",
        "Foi proibido para mulheres e comerciantes que viajavam pelo Mediterrâneo.",
        "Servia apenas para registrar transações bancárias com nações do Oriente Médio.",
        "A",
        "A simplicidade fonética do alfabeto grego libertou a escrita do monopólio sacerdotal e a transformou em bem comum na pólis."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao confrontar o modelo explicativo do Mito com o do Logos, constata-se que a autoridade do mito apoiava-se principalmente:",
        "Na comprovação matemática de hipóteses submetidas a testes de laboratório.",
        "Na confiança sagrada concedida ao poeta-rapsodo inspirado diretamente por musas divinas.",
        "Na votação aberta de cidadãos reunidos na assembleia popular da pólis.",
        "Na publicação de decretos jurídicos fundamentados em pesquisas censitárias.",
        "Na exigência de que qualquer ouvinte pudesse contestar o poema em praça pública.",
        "B",
        "O mito fundava-se na tradição oral sagrada e na autoridade religiosa do rapsodo (aedo), sem exigência de demonstração laica."
    ))

    questoes_brutas.append((
        22, "EM13CHS103", "intermediario",
        "A introdução da moeda cunhada na Grécia Arcaica gerou impactos no pensamento que ultrapassaram a economia, pois habituou a mente a:",
        "Trocar cavalos por fardos de trigo sem calcular medidas exatas.",
        "Operar com abstrações matemáticas e mensurar grandezas qualitativamente distintas sob um padrão comum.",
        "Rejeitar qualquer forma de cálculo numérico na vida cotidiana da cidade.",
        "Guardar riquezas materiais em cofres de templos sem colocá-las em circulação.",
        "Recorrer a sacerdotes para determinar o valor de troca de mercadorias no porto.",
        "B",
        "A moeda promoveu a abstração quantitativa, treinando o intelecto a desvincular o valor de seu suporte físico imediato."
    ))

    questoes_brutas.append((
        23, "EM13CHS101", "intermediario",
        "A tese de Anaximandro sobre o Ápeiron superou a visão de Tales de Mileto ao reconhecer um limite lógico na escolha da água, a saber:",
        "A água é um elemento frio e úmido que seria destruído em um conflito direto com o calor e a secura do fogo.",
        "A água é muito pesada para permitir o nascimento de astros celestes luminosos.",
        "A observação empírica da chuva exige instrumentos de navegação que Mileto desconhecia.",
        "A água dos rios evapora no verão e impede o crescimento de árvores em regiões de serra.",
        "O mar Mediterrâneo possui salinidade variável que confunde o cálculo de seus volumes.",
        "A",
        "Anaximandro percebeu que um elemento particular determinado não pode gerar seu oposto sem ser anulado por ele."
    ))

    questoes_brutas.append((
        24, "EM13CHS101", "intermediario",
        "Para os pitagóricos, a descoberta de que as notas musicais harmônicas correspondem a frações numéricas exatas comprovou que:",
        "A música deve ser banida da educação dos jovens por despertar paixões guerreiras.",
        "A ordem cósmica possui uma estrutura inteligível regida por relações de proporção matemática.",
        "Os instrumentos de corda dependem de orações a Apolo para emitir sons agradáveis.",
        "A poesia homérica é superior a qualquer demonstração geométrica de figuras planas.",
        "As notas musicais foram inventadas por generais espartanos para cadenciar marchas.",
        "B",
        "A acústica revelou aos pitagóricos que a harmonia do mundo audível expressa a ordem matemática e geométrica do cosmos."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Na visão de Heráclito sobre a luta dos contrários (Pólemos), o conflito não representa uma falha destrutiva do cosmos, porque:",
        "As forças em tensão mútua geram a medida, a dinâmica e a harmonia viva de toda a realidade.",
        "Os homens precisam guerrear periodicamente para reduzir a população das cidades costeiras.",
        "A vitória definitiva da noite sobre o dia trará o repouso eterno à totalidade dos seres.",
        "Os deuses olímpicos se divertem assistindo a confrontos armados entre nações rivais.",
        "A paz perpétua provocaria o resfriamento imediato de todas as fontes de água doce.",
        "A",
        "Para Heráclito, a harmonia cósmica decorre da tensão dinâmica entre forças opostas, como a corda e o arco que lançam a flecha."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Parmênides sustentou que 'pensar e ser são a mesma coisa'. Essa célebre formulação filosófica implica afirmar que:",
        "Tudo o que uma pessoa imagina durante o sono adquire existência física imediata.",
        "Apenas aquilo que pode ser pensado de forma logicamente coerente e não contraditória possui realidade objetiva.",
        "A realidade material independe completamente de princípios racionais demonstrativos.",
        "Os pensamentos dos governantes da pólis têm força de lei sobre a natureza física dos ventos.",
        "O intelecto humano é incapaz de formular qualquer juízo seguro sobre o mundo exterior.",
        "B",
        "A equivalência entre pensar e ser estabelece que o contraditório (o Não-Ser) não pode ser pensado nem ter existência real."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "No paradoxo de Aquiles e a Tartaruga, Zenão demonstra que, se o espaço for concebido como uma grandeza divisível ao infinito:",
        "O herói grego ultrapassará a tartaruga logo no primeiro passo da competição atlética.",
        "Aquiles jamais alcançará o animal, pois terá que esgotar uma série infinita de distâncias espaciais finitas.",
        "A tartaruga morrerá de cansaço antes de completar a metade do percurso estabelecido.",
        "Os juízes da corrida declararão empate por falta de critérios de medição temporal.",
        "A velocidade de um guerreiro em marcha varia de acordo com a altitude do terreno.",
        "B",
        "Zenão mostra que dividir o espaço infinitamente cria uma aporia lógica em que o mais rápido nunca atinge o mais lento."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "A teoria dos Quatro Elementos de Empédocles respondeu ao impasse criado por Parmênides ao conciliar permanência e mudança por meio de:",
        "Elementos eternos e imutáveis em si mesmos que se misturam e se separam mecanicamente no espaço.",
        "Uma criação contínua de novas substâncias materiais a partir do nada absoluto a cada instante.",
        "Uma ilusão coletiva produzida por encantamentos sonoros entoados por sacerdotes no templo.",
        "Uma transformação química irreversível que consome as quatro raízes da matéria cósmica.",
        "Um retorno periódico ao caos primordial onde toda a matéria existente é aniquilada.",
        "A",
        "Empédocles preservou a eternidade do Ser parmenidiano nas 4 raízes, explicando a mudança pela combinação mecânica delas."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Anaxágoras introduziu a noção de sementes (homeomerias) afirmando que 'em tudo há uma porção de tudo'. Essa tese visava explicar:",
        "Como um alimento ingerido pelo organismo humano (como pão) pode se transformar em ossos, carne e cabelo.",
        "Por que as sementes de trigo plantadas na areia seca nunca germinam durante as chuvas.",
        "A razão de os agricultores jônicos colherem frutos diferentes em uma mesma árvore frutífera.",
        "O motivo de as cidades costeiras comercializarem grãos produzidos em ilhas do mar Egeu.",
        "A proibição religiosa do consumo de feijões imposta aos iniciados da escola de Crotona.",
        "A",
        "Se o Não-Ser não existe, o cabelo e o osso não brotam do nada; suas sementes já estavam presentes na matéria do pão digerido."
    ))

    questoes_brutas.append((
        30, "EM13CHS101", "intermediario",
        "O atomismo de Demócrito representou uma solução inovadora ao problema do movimento porque aceitou a existência física:",
        "De deuses benevolentes que empurram os planetas ao longo de suas órbitas elípticas.",
        "Do Não-Ser sob a forma do Vácuo espacial onde os corpos atômicos circulam e colidem.",
        "De forças magnéticas invisíveis emanadas do centro da Terra em direção ao céu estrelado.",
        "De almas vegetais presentes em todas as pedras e minérios enterrados no solo fértil.",
        "De uma substância etérea que impede a aproximação de partículas sólidas no ar.",
        "B",
        "Demócrito legitimou o Não-Ser como o Vácuo real, permitindo que os átomos de Parmênides se movessem sem contradição."
    ))

    questoes_brutas.append((
        31, "EM13CHS103", "intermediario",
        "Ao instituir o princípio da Isonomia (igualdade perante a lei), a pólis grega estabeleceu uma ruptura com regimes autoritários ao determinar que:",
        "A palavra escrita e debatida publicamente tinha primazia sobre os decretos de reis ou vontades divinas.",
        "Os sacerdotes tinham o direito de anular julgamentos civis sempre que o oráculo silenciasse.",
        "Apenas nobres de linhagem guerreira podiam votar em assembleias populares na praça da cidade.",
        "Os tributos arrecadados deviam ser divididos igualmente entre marinheiros de outras nações.",
        "A justiça das decisões dependia da força física demonstrada pelos oradores na tribuna.",
        "A",
        "A isonomia substituiu o privilégio de sangue pela igualdade perante a norma escrita debatida pelos cidadãos na ágora."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Heráclito afirmava que a maioria dos homens 'vive como em um sonho' porque comete qual equívoco diante da realidade?",
        "Confia em horóscopos astronômicos em vez de prestar atenção às cheias dos rios navegáveis.",
        "Deixa-se levar por opiniões particulares e sensações superficiais, ignorando o Logos Universal que governa o cosmos.",
        "Trabalha em tarefas manuais na cidade em vez de se dedicar a campanhas militares no exterior.",
        "Recusa o diálogo com cidadãos atenienses para evitar disputas sobre leis orçamentárias.",
        "Acredita que as estátuas de deuses podem caminhar durante a noite sem auxílio de cordas.",
        "B",
        "O 'sono' heraclitiano é a ignorância do Logos cósmico, fazendo com que as pessoas vivam iludidas em suas convicções particulares."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "A crítica parmenidiana aos sentidos corporais lançou as bases de uma separação que atravessou a história da filosofia ocidental, opondo:",
        "A intuição poética de oráculos sagrados às práticas agrícolas de camponeses no interior.",
        "O conhecimento sensível imperfeito da opinião (Doxa) e o conhecimento inteligível da verdade (Aletheia).",
        "A disciplina militar dos espartanos à vida mercantil dos navegadores de navios da Jônia.",
        "A oratória utilizada em funerais à linguagem técnica de construtores de muralhas de pedra.",
        "A riqueza obtida em minas de prata aos ganhos gerados pela pesca artesanal nas praias.",
        "B",
        "Parmênides cindiu a apreensão da realidade entre os enganos da percepção sensorial e o rigor demonstrativo do intelecto puro."
    ))

    questoes_brutas.append((
        34, "EM13CHS101", "intermediario",
        "O modelo atômico de Demócrito explicava as diferenças entre substâncias (como água, ferro e fogo) por meio de qual fator puramente mecânico?",
        "Pela intensidade do sopro espiritual injetado em cada corpo durante a criação inicial.",
        "Pela forma geométrica, ordem e arranjo espacial com que os átomos se encaixam e se agrupam.",
        "Pela cor externa que cada partícula atômica recebe ao ser exposta à luz do sol de verão.",
        "Pelo peso moral das almas dos seres vivos que habitavam as pedras no início dos tempos.",
        "Pelo número de orações dedicadas aos deuses da forja pelos ferreiros das oficinas.",
        "B",
        "Para Demócrito, o ferro é duro por ter átomos pontiagudos que se entrelaçam; a água corre porque seus átomos são lisos e redondos."
    ))

    questoes_brutas.append((
        35, "EM13CHS103", "intermediario",
        "Ao comparar o papel da escrita alfabética grega com o dos hieróglifos egípcios, Jean-Pierre Vernant enfatizou que a escrita helênica:",
        "Desempenhou uma função mágica restrita a proteger as tumbas fúnebres de reis e generais.",
        "Tornou-se instrumento de publicidade e debate aberto, fixando a lei no olhar crítico de todos os cidadãos.",
        "Serviu unicamente para catalogar receitas médicas em mosteiros isolados nas montanhas.",
        "Foi utilizada de forma clandestina por marinheiros que tentavam contrabandear especiarias finas.",
        "Manteve-se como patrimônio reservado a uma dinastia aristocrática de adivinhos reais.",
        "B",
        "A escrita alfabética na Grécia dessacralizou o saber e colocou a lei e o argumento sob a fiscalização laica da comunidade cívica."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Anaxímenes escolheu o Ar como arché por julgar que esse elemento possuía uma vantagem teórica sobre a terra e a água, qual seja:",
        "Sua infinita mobilidade, invisibilidade e capacidade de envolver e sustentar a totalidade da vida.",
        "Sua rigidez mecânica capaz de impedir que as estrelas caiam sobre as cidades litorâneas.",
        "Seu peso elevado que obriga os corpos celestes a girarem ao redor de montanhas rochosas.",
        "Sua facilidade de ser engarrafado em vasos de cerâmica para comercialização em feiras livres.",
        "Seu brilho luminoso dourado que ilumina os caminhos percorridos por viajantes à noite.",
        "A",
        "O ar une a extensão infinita do Ápeiron com a tangibilidade empírica da água, atuando como o sopro vital (pneuma) que anima o cosmos."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "A recusa do atomismo de Demócrito em relação a causas finais ou propósitos teológicos no Universo caracteriza essa filosofia como:",
        "Um espiritualismo teocêntrico que subordina a física às ordens de divindades do Olimpo.",
        "Um materialismo mecanicista no qual todos os acontecimentos decorrem de choques e necessidades materiais.",
        "Uma teoria mística que atribui aos números a responsabilidade moral pela conduta cívica.",
        "Um ceticismo desesperado que nega a possibilidade de investigar a natureza das coisas vivas.",
        "Um relativismo retórico voltado unicamente a treinar oradores para disputas eleitorais.",
        "B",
        "Demócrito explica o cosmos sem recorrer a vontades divinas ou desígnios inteligentes: tudo decorre do choque atômico no vácuo."
    ))

    questoes_brutas.append((
        38, "EM13CHS105", "intermediario",
        "A convivência entre o mito e o logos na cultura grega clássica revela que a emergência da razão demonstrativa:",
        "Eliminou imediatamente qualquer vestígio de crença religiosa na população de Atenas e Esparta.",
        "Ocorreu como um processo gradual no qual o mito continuou presente em ritos cívicos, tragédias e alegorias filosóficas.",
        "Limitou-se a círculos de navegadores estrangeiros, sem impactar o teatro ou a poesia da época.",
        "Foi revogada por decretos de tribunais que proibiram o ensino da geometria em praça pública.",
        "Dependeu do aval prévio de líderes militares macedônios para ser tolerada nos templos.",
        "B",
        "O mito permaneceu atuante no teatro, na religião da cidade e até nos mitos pedagógicos de Platão, coexistindo com o Logos."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "O conceito pré-socrático de Hilozoísmo, associado à visão de Tales de que 'tudo está cheio de deuses', significa que:",
        "A matéria inanimada precisa de estátuas douradas para adquirir valor de troca no comércio.",
        "A natureza física é concebida como viva e animada por forças ativas imanentes a ela mesma.",
        "Os cientistas devem sacrificar bois nas praias antes de iniciar observações astronômicas.",
        "Os deuses interferem arbitrariamente a cada segundo para mudar a direção das ondas do mar.",
        "A água perde suas propriedades nutritivas caso não receba orações diárias de sacerdotes.",
        "B",
        "O hilozoísmo (de hyle, matéria, e zoe, vida) concebe a matéria viva e pulsante, sem a separação moderna entre corpo e alma."
    ))

    questoes_brutas.append((
        40, "EM13CHS101", "intermediario",
        "A harmonia das esferas, formulada pela escola pitagórica, expressava a crença cosmológica de que:",
        "Os planetas e estrelas emitem frequências musicais harmônicas proporcionais às suas distâncias matemáticas.",
        "A Terra flutua imóvel sobre um bloco de gelo sólido situado no centro de uma cúpula de vidro.",
        "O som dos sinos dos templos de Crotona afastava espíritos malignos das plantações de uva.",
        "As guerras navais do Mediterrâneo eram provocadas por ruídos ensurdecedores vindos do céu.",
        "A música cantada nas praças devia obedecer aos ritmos ditados por generais da infantaria.",
        "A",
        "Para Pitágoras, o movimento regular dos corpos celestes obedece a proporções numéricas que geram uma consonância cósmica divina."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # Com resolução detalhada: - **Etapa 1:** ... - **Etapa 2:** ...
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Considere o texto: 'Não se pode entrar duas vezes no mesmo rio, pois novas águas correm sobre nós, e nós mesmos já não somos os mesmos.' A partir dessa tese de Heráclito, deduz-se que a realidade:",
        "Possui uma essência imóvel acessível apenas quando o sujeito fecha os olhos para o mundo.",
        "É marcada pela impermanência universal do devir, onde sujeito e objeto transformam-se continuamente.",
        "Constitui uma cópia imperfeita de arquétipos celestes preservados no palácio dos deuses do Olimpo.",
        "Depende de decisões burocráticas tomadas por magistrados reunidos nas assembleias da pólis.",
        "Pode ser congelada de forma definitiva por meio de leis civis que proíbem o comércio marítimo.",
        "B",
        "- **Etapa 1:** Interpretação da metáfora do rio de Heráclito. O texto destaca a fluidez ininterrupta tanto da corrente de águas quanto da própria constituição interior da pessoa que se banha.\n- **Etapa 2:** Dedução teórica fundamental. O ser heraclitiano não é uma substância estática, mas um processo incessante de devir (Panta Rhei), em que a identidade é tecida pela permanente transformação."
    ))

    questoes_brutas.append((
        42, "EM13CHS101", "dificil",
        "Analise a premissa de Parmênides: 'O Ser é e não pode não ser; o Não-Ser não é.' Se levada ao rigor lógico absoluto, essa tese exige concluir que a mudança observada no mundo sensível é:",
        "Uma prova definitiva de que as leis da lógica devem ser descartadas pela ciência experimental.",
        "Uma aparência ilusória da percepção sensorial que não se sustenta perante o intelecto puro.",
        "O resultado mecânico de colisões entre partículas microscópicas que viajam pelo espaço vazio.",
        "Uma dádiva divina concedida aos seres humanos para aliviar a monotonia da eternidade.",
        "A confirmação de que o Não-Ser exerce domínio pleno sobre a matéria das quatro estações.",
        "B",
        "- **Etapa 1:** Análise lógica da exigência parmenidiana. Se o Não-Ser não existe e nada pode brotar do nada, a mudança (que implica deixar de ser para passar a ser outra coisa) exigiria a atuação do Não-Ser.\n- **Etapa 2:** Julgamento sobre o estatuto da sensibilidade. Sendo o Não-Ser logicamente impossível, o movimento captado pelos olhos corpóreos pertence à Doxa (opinião ilusória), e não à Aletheia (verdade do Ser)."
    ))

    questoes_brutas.append((
        43, "EM13CHS101", "dificil",
        "Em redes digitais, dados cadastrais e históricos biométricos são gravados em registros indeléveis de bancos de dados. Esse cenário confronta o devir de Heráclito com o Ser de Parmênides porque:",
        "O feed dinâmico das postagens representa a imutabilidade, enquanto os bancos de dados vivem em perpétuo caos.",
        "A timeline instantânea reflete a fluidez heraclitiana, ao passo que os registros indeléveis congelam a identidade do cidadão no modo parmenidiano.",
        "Os algoritmos de inteligência artificial foram programados para seguir exclusivamente as regras dos poetas-rapsodos gregos.",
        "Os usuários recusam o uso de computadores para voltar à comunicação oral praticada na ágora antiga.",
        "As empresas de tecnologia eliminam todos os dados de navegação a cada vinte e quatro horas de forma espontânea.",
        "B",
        "- **Etapa 1:** Identificação das dinâmicas tecnológicas no estudo de caso. As postagens temporárias nas redes sociais mudam a cada segundo (devir), enquanto os registros de logs e biometria tornam-se perpétuos e imutáveis.\n- **Etapa 2:** Conexão conceitual. A tensão manifesta-se entre a aspiração do sujeito à transformação livre (Heráclito) e a petrificação de seu perfil em dados estáticos sem direito ao esquecimento (Parmênides)."
    ))

    questoes_brutas.append((
        44, "EM13CHS103", "dificil",
        "Ao investigar a emergência da democracia na pólis grega, Jürgen Habermas retoma a tradição da ágora para fundamentar a esfera pública moderna. Esse diálogo teórico fundamenta-se no princípio de que:",
        "As decisões coletivas devem emanar do melhor argumento debatido racionalmente e livre de coerções.",
        "O poder político legítimo deve ser exercido por generais condecorados em guerras internacionais.",
        "A riqueza material acumulada por grandes corporações deve definir o teor das leis municipais.",
        "As assembleias de cidadãos devem reunir-se em sigilo total para impedir críticas da imprensa livre.",
        "O voto popular deve ser substituído por sorteios de pedras coloridas retiradas de ânforas sagradas.",
        "A",
        "- **Etapa 1:** Exame da teoria da esfera pública habermasiana. Habermas inspira-se no espaço cívico da pólis para definir a deliberação democrática fundamentada no uso público da razão comunicativa.\n- **Etapa 2:** Vinculação com o modelo grego. O valor normativo da ágora reside na substituição do mando pela persuasão lógica racional, onde a autoridade decorre da força do argumento entre iguais."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Na nanotecnologia farmacêutica, nanopartículas poliméricas com encaixes moleculares liberam quimioterápicos apenas em células tumorais. Esse arranjo experimental valida historicamente a intuição de Demócrito de que:",
        "As propriedades observáveis dos corpos materiais decorrem da forma geométrica e do encaixe mecânico de partículas infinitesimais.",
        "A saúde do corpo humano depende de manter o equilíbrio térmico entre o amor cósmico e o ódio cósmico.",
        "As células biológicas surgem da condensação de ar frio acumulado nas cavidades pulmonares.",
        "Os medicamentos funcionam unicamente se forem fabricados sob a influência da constelação de Órion.",
        "A matéria dos tumores é composta por sementes espirituais que resistem à ação da física mecanicista.",
        "A",
        "- **Etapa 1:** Análise do funcionamento molecular dos fármacos modernos. O princípio ativo liga-se a receptores específicos por complementaridade geométrica em escala nanométrica.\n- **Etapa 2:** Confronto com a filosofia de Demócrito. Isso confirma a intuição do atomismo materialista antigo, que explicava as propriedades sensíveis e biológicas macroscópicas pelo formato espacial e encaixe mecânico dos átomos."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Ao formular a teoria das Homeomerias, Anaxágoras propôs que o Nous (Mente) organizou o cosmos. Essa tese diferencia-se do atomismo de Demócrito porque:",
        "Atribui a ordem cósmica a um propósito racional transcendente, enquanto Demócrito postula o choque mecânico e cego no vácuo.",
        "Nega a existência de sementes materiais, defendendo que o Universo é formado apenas por pensamentos puros.",
        "Recusa qualquer tipo de movimento da matéria, aceitando a imobilidade absoluta do Ser parmenidiano.",
        "Afirma que os deuses do Olimpo fabricaram as partículas atômicas em forjas subterrâneas na ilha de Creta.",
        "Sustenta que a água de Tales é a única substância presente no interior das células vivas.",
        "A",
        "- **Etapa 1:** Comparação dos motores explicativos. Anaxágoras introduz o Nous como uma inteligência cósmica que ordena intencionalmente a matéria em direção ao equilíbrio e à beleza cósmica.\n- **Etapa 2:** Diferenciação teórica com Demócrito. Enquanto Anaxágoras acolhe uma finalidade racional organizadora, o atomismo democriteano recusa propósitos cósmicos, fundamentando-se no mecanicismo estrito dos choques no vazio."
    ))

    questoes_brutas.append((
        47, "EM13CHS103", "dificil",
        "Diante da proliferação contemporânea de desinformação em redes digitais, o resgate das condições materiais do Logos na Grécia Arcaica sugere que a superação desse problema exige:",
        "A proibição do uso de aparelhos de telefonia celular em todos os ambientes acadêmicos e escolares.",
        "A revitalização da esfera pública compartilhada, pautada pela exigência de provas e pela deliberação crítica entre diferentes visões.",
        "A delegação das decisões judiciais e legislativas a influenciadores digitais com maior número de seguidores.",
        "A volta à censura prévia de textos para evitar que trabalhadores leiam notícias sobre política externa.",
        "O fechamento das universidades públicas para reduzir o número de debates teóricos na sociedade civil.",
        "B",
        "- **Etapa 1:** Diagnóstico da crise informacional atual. As bolhas algorítmicas funcionam como narrativas míticas dogmáticas, exigindo adesão emocional sem apresentação de demonstrações lógicas verificáveis.\n- **Etapa 2:** Resposta fundamentada no Logos. O remédio democrático inspirado na ágora grega é a reconstrução do espaço comum do debate transparente, onde argumentos são expostos à prova e ao escrutínio racional da cidadania."
    ))

    questoes_brutas.append((
        48, "EM13CHS101", "dificil",
        "Considere a afirmação de Anaxímenes: 'Assim como nossa alma, que é ar, nos sustenta, o sopro e o ar envolvem todo o cosmos.' Essa passagem expressa qual concepção cosmológica típica dos pré-socráticos?",
        "A ruptura absoluta entre as leis da biologia humana e a estrutura material dos astros celestes.",
        "A correspondência analógica entre o microcosmo humano e o macrocosmo universal, regidos pelo mesmo princípio vital.",
        "A convicção de que o corpo dos animais não necessita de oxigênio para manter as funções vitais ativas.",
        "A negação da existência da alma humana em prol de um reducionismo puramente mineral sem vida.",
        "A dependência dos fenômenos meteorológicos em relação aos ritos fúnebres celebrados em portos marítimos.",
        "B",
        "- **Etapa 1:** Interpretação da correlação formulada por Anaxímenes. O autor compara o papel animador da respiração na vida humana com o papel do ar como sustentáculo da totalidade do cosmos.\n- **Etapa 2:** Síntese cosmológica. Esse raciocínio articula a unidade profunda entre microcosmo e macrocosmo, na qual a mesma substância originária (o Ar / Pneuma) gera, nutre e conecta todos os planos do real."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Zenão de Eleia utilizou o paradoxo da Flecha em Repouso para demonstrar a impossibilidade do movimento. O núcleo desse argumento lógico baseia-se em afirmar que:",
        "A ponta da flecha perde o fio de corte ao perfurar o ar denso das planícies do litoral.",
        "Em cada instante indivisível do tempo, a flecha ocupa um espaço igual ao seu próprio volume, estando, portanto, parada em repouso.",
        "O arqueiro precisa rezar à deusa Ártemis para que o vento não desvie o trajeto da flecha até o alvo.",
        "A velocidade da madeira varia de acordo com o tipo de árvore utilizada na fabricação da flecha.",
        "A gravidade da Terra atrai a flecha imediatamente para o chão no momento em que ela deixa o arco.",
        "B",
        "- **Etapa 1:** Exame da estrutura do paradoxo temporal de Zenão. Se o tempo for uma soma de instantes indivisíveis finitos, em cada um desses instantes a flecha não está mudando de lugar; ela ocupa apenas o seu próprio volume espacial.\n- **Etapa 2:** Conclusão parmenidiana. Uma soma de infinitos instantes em repouso jamais poderá gerar movimento real; logo, o movimento percebido é uma contradição lógica insustentável perante o intelecto."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "Ao buscar uma única Arché capaz de unificar todos os fenômenos da natureza, os pensadores de Mileto inauguraram uma atitude que se conecta contemporaneamente com:",
        "A pesquisa teórica em física de partículas que busca uma teoria unificadora de todas as forças fundamentais do cosmos.",
        "A astrologia mística que atribui aos signos do zodíaco a responsabilidade pela saúde dos indivíduos.",
        "A engenharia militar que fabrica armas de fogo inspiradas em desenhos de catapultas gregas.",
        "O direito consuetudinário medieval que julgava conflitos de terra por meio de duelos armados entre cavaleiros.",
        "A arqueologia submarina que busca tesouros enterrados em embarcações afundadas sem documentação escrita.",
        "A",
        "- **Etapa 1:** Caracterização do projeto investigativo dos fisiólogos jônicos. Tales, Anaximandro e Anaxímenes buscavam um único princípio originário imanente para explicar a totalidade da Physis.\n- **Etapa 2:** Conexão científica moderna. Essa atitude fundou o programa da física teórica que busca formular uma Grande Teoria Unificada capaz de integrar as forças da natureza sob uma mesma equação fundamental."
    ))

    questoes_brutas.append((
        51, "EM13CHS103", "dificil",
        "O conceito grego de Isegoria (igualdade no direito de discursar na assembleia popular) pressupunha que a verdade política na pólis não era um dogma hereditário, mas:",
        "Uma imposição formulada por sacerdotes com poderes concedidos por generais de infantaria.",
        "O resultado transitório alcançado pelo confronto público de argumentos demonstrativos entre cidadãos livres.",
        "Um cálculo financeiro sigiloso elaborado por mercadores de especiarias no porto de Pireu.",
        "Uma revelação mística concedida em sonhos a magistrados idosos da corte de justiça.",
        "Uma decisão judicial transmitida por reis de Esparta através de mensageiros velozes.",
        "B",
        "- **Etapa 1:** Definição do instituto da Isegoria na democracia da pólis. Todos os cidadãos adultos tinham o direito cívico de subir à tribuna da Eclésia e manifestar suas propostas perante a comunidade.\n- **Etapa 2:** Julgamento sobre o estatuto da verdade política. Isso consagra o Logos deliberativo: a legitimidade da lei nasce do debate argumentativo laico e do convencimento racional dos pares, e não de mandos autocráticos."
    ))

    questoes_brutas.append((
        52, "EM13CHS101", "dificil",
        "Empédocles formulou que as quatro raízes são eternas e imutáveis, enquanto os seres concretos perecem. Essa formulação resolve o paradoxo do Ser parmenidiano porque:",
        "Nenhum novo ser surge a partir do nada e nada se aniquila no nada; ocorrem apenas misturas e separações espaciais mecânicas.",
        "A terra e o fogo transformam-se espontaneamente em ouro quando expostos a tempestades de verão.",
        "O amor cósmico é capaz de destruir as quatro raízes para criar uma matéria totalmente imaterial.",
        "Os quatro elementos foram forjados por ferreiros de Agrigento em fornalhas de alta temperatura.",
        "A morte dos seres humanos decorre do resfriamento total da água armazenada nas artérias sanguíneas.",
        "A",
        "- **Etapa 1:** Interpretação da solução pluralista. Empédocles aceita o axioma de Parmênides: nada nasce do Não-Ser e nada retorna ao Não-Ser absoluto.\n- **Etapa 2:** Mecanismo da composição. O nascimento é apenas a confluência harmoniosa das quatro raízes eternas impulsionada pelo Amor (Philia); a morte é apenas a sua dissolução e separação espacial pela Discórdia (Neikos)."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Considere o fragmento de Heráclito: 'O mar é a água mais pura e a mais poluída: para os peixes é saudável e conservadora de vida; para os homens é venenosa e mortal.' Esse fragmento exemplifica:",
        "A ausência total de regras lógicas na natureza, que impede qualquer estudo científico sobre as marés.",
        "A relatividade das propriedades perceptíveis e a tensão dos contrários que estruturam a harmonia do cosmos.",
        "A defesa do fechamento dos portos marítimos para proteger a saúde das famílias de pescadores locais.",
        "A recomendação médica de não consumir sal marinho em dietas prescritas para atletas de corrida.",
        "A convicção de que os peixes possuem almas racionais semelhantes às dos filósofos de Mileto.",
        "B",
        "- **Etapa 1:** Análise do fragmento heraclitiano sobre a água do mar. O mesmo elemento empírico produz efeitos opostos e simultâneos de acordo com a perspectiva e a constituição dos seres que com ele interagem.\n- **Etapa 2:** Articulação conceitual. O exemplo ilustra a dialética dos contrários: a realidade é relacional e multifacetada, mantendo sua coerência cósmica sob a lei unificadora do Logos."
    ))

    questoes_brutas.append((
        54, "EM13CHS101", "dificil",
        "Parmênides deduziu que o Ser é 'semelhante a uma esfera perfeita, bem redonda e de peso igual a partir do centro'. Essa metáfora geométrica visa expressar:",
        "Que o Universo tem a consistência de uma bola de argila assada por oleiros da cidade de Eleia.",
        "A total plenitude, homogeneidade e perfeita completude do Ser, que não tem carência, falta ou partes desiguais.",
        "A trajetória circular descrita por cometas luminosos durante os meses de colheita de azeitonas.",
        "A obrigatoriedade de construir templos religiosos em formatos circulares com colunas de granito.",
        "A crença de que a Terra era oca e guardava em seu centro as almas de navegadores desaparecidos.",
        "B",
        "- **Etapa 1:** Exame da imagem da esfera no poema de Parmênides. A esfera é a figura geométrica onde todos os pontos da superfície estão à mesma distância do centro, sem vértices ou assimetrias.\n- **Etapa 2:** Dedução conceitual. Parmênides utiliza a esfera para expressar a perfeição absoluta e contínua do Ser: pleno em todas as direções, sem vazios, lacunas ou fraquezas onde pudesse insinuar-se o Não-Ser."
    ))

    questoes_brutas.append((
        55, "EM13CHS101", "dificil",
        "Anaximandro afirmou que os mundos 'pagam castigo e expiação recíproca pela sua injustiça de acordo com a ordem do tempo'. Essa formulação expressa:",
        "A cobrança de multas monetárias sobre cidades portuárias que atrasavam o pagamento de tributos cívicos.",
        "A visão cosmológica de que a predominância de um elemento contrário (como o calor no verão) deve ser equilibrada pela chegada do oposto (o frio no inverno).",
        "A condenação militar imposta aos soldados derrotados em combates terrestres contra nações vizinhas.",
        "O dever religioso de realizar jejuns de água salgada durante os períodos de seca prolongada.",
        "A necessidade de sacrificar animais nas praças para afastar epidemias contagiosas dos portos.",
        "B",
        "- **Etapa 1:** Interpretação da metáfora jurídica da injustiça em Anaximandro. O autor projeta no cosmos as noções de justiça e equilíbrio social da pólis.\n- **Etapa 2:** Síntese cosmológica. A invasão de um contrário sobre o território do outro (o excesso de calor ou de frio) é uma injustiça cósmica reparada pela alternância necessária do tempo, que restaura a harmonia do Ápeiron."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Ao afirmar que 'a harmonia invisível é superior à visível', Heráclito estabelece uma distinção essencial entre:",
        "A beleza estética superficial dos monumentos esculpidos e a ordem cósmica profunda regulada pelo Logos oculta aos sentidos.",
        "A música tocada em flautas de osso e o canto fúnebre entoado por mulheres idosas em funerais.",
        "O preço de tecidos de linho importados do Egito e o custo de fabricação de cerâmicas locais.",
        "As palavras pronunciadas por advogados em julgamentos e os votos secretos depositados em urnas.",
        "A luminosidade das estrelas visíveis a olho nu e o clarão produzido por fogueiras em acampamentos.",
        "A",
        "- **Etapa 1:** Exame da antítese entre harmonia visível e invisível em Heráclito. A primeira é a consonância aparente apreendida pelos sentidos corporais; a segunda é a lei oculta que rege as tensões contrárias.\n- **Etapa 2:** Avaliação conceitual. A razão filosófica busca ultrapassar a aparência sensível imediata para atingir a lei fundamental da Physis, inteligível apenas para a consciência atenta ao Logos."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Demócrito postulou que qualidades como cor, sabor e temperatura não pertencem aos átomos em si mesmos, mas são:",
        "Entidades divinas invisíveis que habitam o interior de cada fruta madura colhida no pomar.",
        "Efeitos secundários resultantes da interação sensível entre os arranjos atômicos dos corpos e os órgãos sensoriais humanos.",
        "Substâncias químicas adicionadas pelos cozinheiros de palácios durante o preparo de banquetes reais.",
        "Ilusões mágicas criadas por tempestades solares sobre a atmosfera dos oceanos navegáveis.",
        "Propriedades exclusivas dos metais nobres como o ouro e a prata refinados em fundições.",
        "B",
        "- **Etapa 1:** Compreensão da distinção qualitativa no atomismo antigo. Os átomos possuem apenas forma geométrica, tamanho, ordem e posição espacial no vácuo.\n- **Etapa 2:** Antecipação da teoria das qualidades secundárias. Sabores, odores e cores (por convenção) não residem na partícula atômica, mas são efeitos perceptivos gerados quando o arranjo atômico estimula os sentidos do observador."
    ))

    questoes_brutas.append((
        58, "EM13CHS103", "dificil",
        "A passagem da tradição oral homérica para a prosa reflexiva dos pré-socráticos representou um marco na história da linguagem porque:",
        "Impediu que os cidadãos atenienses cantassem em festividades públicas e comemorações agrícolas.",
        "Submeteu o vocabulário à precisão conceitual e à exigência de concatenação lógica dos argumentos em praça pública.",
        "Restringiu a língua grega ao uso exclusivo em quartéis militares encarregados da defesa costeira.",
        "Eliminou a necessidade de estudar gramática nos cursos preparatórios para magistrados da pólis.",
        "Obrigou os historiadores a queimar todos os manuscritos poéticos anteriores ao século VI a.C.",
        "B",
        "- **Etapa 1:** Avaliação filológica e histórica da evolução da língua grega. O verso homérico organizava-se por fórmulas rítmicas e epítetos mnemônicos voltados à evocação emotiva dos mitos ancestrais.\n- **Etapa 2:** Impacto da prosa filosófica. A prosa pré-socrática inaugurou a linguagem do conceito laico, exigindo definições precisas, nexos causais rigorosos e abertura ao questionamento crítico da comunidade."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "A Tetraktys pitagórica (1 + 2 + 3 + 4 = 10) era reverenciada pelos iniciados de Crotona como juramento sagrado porque expressava:",
        "O número exato de dias necessários para viajar de barco a vela entre Atenas e Alexandria.",
        "A totalidade harmoniosa do Universo, sintetizando o ponto, a linha, a superfície plana e o volume sólido tridimensional.",
        "O total de bois que deviam ser sacrificados a cada novo ciclo da lua cheia nas praias do mar Jônio.",
        "A quantidade de magistrados encarregados de fiscalizar os pesos e medidas nas feiras municipais.",
        "O limite máximo de propriedades rurais que um nobre podia possuir na Península Itálica.",
        "B",
        "- **Etapa 1:** Análise geométrica e numérica da Tetraktys. O número 1 representa o ponto; o 2, a reta unidimensional; o 3, a superfície bidimensional (triângulo); o 4, o volume tridimensional (tetraedro).\n- **Etapa 2:** Significado cósmico. A soma das quatro primeiras dimensões resulta no número 10 (a perfeição decimal), simbolizando para os pitagóricos a chave geométrica e harmônica de toda a criação física."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "Ao sintetizar o debate entre o mobilismo de Heráclito e o imobilismo de Parmênides, conclui-se que esse embate inaugurou o problema filosófico fundamental:",
        "Da construção de portos marítimos com pedras resistentes ao impacto contínuo de ondas salgadas.",
        "Da relação dialética entre a permanência e a mudança na compreensão da totalidade do real.",
        "Do cálculo de impostos sobre vendas de cereais para custear expedições bélicas no exterior.",
        "Da criação de técnicas teatrais para ensinar crianças a memorizarem poemas de Homero.",
        "Da divisão dos exércitos de infantaria em pelotões de ataque rápido durante as guerras médicas.",
        "B",
        "- **Etapa 1:** Identificação do cerne especulativo do embate. Heráclito defendeu a primazia do devir e do fluxo perpétuo; Parmênides defendeu a imutabilidade estrita e a eternidade do Ser pleno.\n- **Etapa 2:** Legado fundante para a metafísica ocidental. Esse conflito estabeleceu o problema que desafiou Platão, Aristóteles e toda a tradição posterior: como explicar a multiplicidade e a transformação do mundo concreto sem anular a permanência e a verdade dos conceitos racionais."
    ))

    # Balanceamento perfeito
    questoes = balancear_questoes(questoes_brutas)

    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('objeto_de_conhecimento: "A Passagem da Narrativa Mítica (Homero e Hesíodo) para a Explicação Racional do Cosmos (Logos); As Condições Materiais da Pólis Grega: Comércio Marítimo, Moeda, Escrita Alfabética e Democracia; Os Filósofos da Physis e a Busca pelo Princípio Originário (Arché): Tales de Mileto (Água), Anaximandro (Ápeiron), Anaxímenes (Ar) e Pitágoras (Número); O Debate Ontológico Fundamental: Heráclito de Éfeso (O Devir, A Mudança Perpétua e o Conflito dos Opostos) vs. Parmênides de Eleia (A Imutabilidade do Ser: \'O ser é e o não-ser não é\')."')
    md.append('ebook_fonte: "em-fil-c02-mito-ao-logos-pre-socraticos.md"')
    md.append('habilidades: "EM13CHS101, EM13CHS103, EM13CHS105, H1, H2, H11"')
    md.append("total_exercicios: 60")
    md.append("distribuicao:")
    md.append("  basico: 20")
    md.append("  intermediario: 20")
    md.append("  dificil: 20")
    md.append("---")
    md.append("")
    md.append("# Exercícios — Do Mito ao Logos na Grécia Antiga: Os Filósofos Pré-Socráticos")
    md.append("")
    md.append("## Nível Básico (Questões 1 a 20)")
    md.append("")

    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: mito-ao-logos-pre-socraticos -->")
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
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: mito-ao-logos-pre-socraticos -->")
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
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: mito-ao-logos-pre-socraticos -->")
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
    md.append("- BORNHEIM, Gerd. *Os Filósofos Pré-Socráticos*. São Paulo: Cultrix, 1993.")
    md.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.")
    md.append("- CHAUÍ, Marilena. *Introdução à História da Filosofia: Dos Pré-Socráticos a Aristóteles*. 2. ed. São Paulo: Companhia das Letras, 2002. v. 1.")
    md.append("- KIRK, Geoffrey S.; RAVEN, John E.; SCHOFIELD, Malcolm. *Os Filósofos Pré-Socráticos: História Crítica com Seleção de Textos*. Tradução de Carlos Alberto Louro Fonseca. 4. ed. Lisboa: Fundação Calouste Gulbenkian, 1994.")
    md.append("- MARCONDES, Danilo. *Iniciação à História da Filosofia: Dos Pré-Socráticos a Wittgenstein*. 11. ed. Rio de Janeiro: Jorge Zahar, 2007.")
    md.append("- VERNANT, Jean-Pierre. *As Origens do Pensamento Grego*. Tradução de Ísis Borges B. da Fonseca. 16. ed. Rio de Janeiro: Difel, 2006.")
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
        print("[SUCESSO TOTAL] Cap 02 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    gerar_cap02()
