# -*- coding: utf-8 -*-
"""
Script de Geração e Validação das 60 Questões de Filosofia - Cap 10
Objeto: A Ética das Virtudes: Aristóteles e as Escolas Helenísticas
Habilidades BNCC: EM13CHS101, EM13CHS104, EM13CHS501, EM13CHS502
"""

import os
import re
import sys
import subprocess
from collections import Counter

def construir_exercicios():
    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Na Ética a Nicômaco, Aristóteles afirma que todas as ações e escolhas humanas visam a algum Bem. Qual é o Bem supremo ou finalidade última da vida humana?",
        "A acumulação ilimitada de moedas de prata e barras de ouro.",
        "A Felicidade (Eudaimonia), compreendida como a plena realização e florescimento das potencialidades humanas ao longo de uma vida inteira.",
        "A conquista de territórios estrangeiros por meio de campanhas militares.",
        "A obtenção de títulos de nobreza concedidos por governantes absolutistas.",
        "A celebração diária de banquetes suntuosos com iguarias exóticas.",
        "B",
        "Para Aristóteles, a felicidade (Eudaimonia) é o fim supremo desejado por si mesmo e nunca como meio para outra coisa, consistindo na plena realização da natureza racional humana."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "Ao formular o 'argumento da função' (Ergon), Aristóteles compara o homem a um artesão. Qual é a atividade própria e exclusiva do ser humano que define sua excelência moral?",
        "A capacidade de correr com grande velocidade em terrenos arenosos.",
        "A atividade da alma orientada pela Razão (Logos) e pela prática da virtude.",
        "A digestão eficiente de alimentos vegetais e sementes silvestres.",
        "A construção de abrigos de madeira para proteger animais domésticos.",
        "O repouso absoluto durante todas as horas de luz solar.",
        "B",
        "Diferente das plantas (vida vegetativa) e dos animais irracionais (vida sensitiva), a função própria do ser humano é o agir consciente guiado pela razão."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "De acordo com a ética aristotélica, como uma pessoa se torna virtuosa e adquire a excelência moral (Aretê)?",
        "Nascendo com privilégios divinos concedidos apenas a reis da Antiguidade.",
        "Pela prática constante e repetida de ações justas até que a virtude se torne um hábito espontâneo e estável (Héxis).",
        "Memorizando definições teóricas de manuais jurídicos em escolas públicas.",
        "Consumindo remédios fabricados com plantas medicinais de florestas temperadas.",
        "Participando de sorteios anuais realizados em praças municipais.",
        "B",
        "A virtude moral em Aristóteles não é inata nem puramente teórica; ela é construída pelo hábito: tornamo-nos justos praticando atos justos."
    ))

    questoes_brutas.append((
        4, "EM13CHS501", "basico",
        "A célebre Teoria do Justo Meio (Mesótes) formulada por Aristóteles define que a virtude ética se situa:",
        "No cumprimento rigoroso de ordens emitidas por comandantes de guarnições militares.",
        "No equilíbrio prudente e harmônico entre dois extremos viciosos: um vício pelo excesso e outro vício pela falta.",
        "Na recusa absoluta de qualquer tipo de prazer material ou convívio familiar.",
        "No cálculo matemático estrito de juros cobrados por comerciantes marítimos.",
        "Na obediência cega a tradições herdadas sem qualquer exame racional.",
        "B",
        "A virtude da mediania situa-se no equilíbrio ótimo entre o exagero e a carência: por exemplo, a coragem equilibra-se entre a covardia (falta) e a temeridade (excesso)."
    ))

    questoes_brutas.append((
        5, "EM13CHS501", "basico",
        "Na doutrina aristotélica das virtudes, a virtude da Coragem representa o justo meio entre quais dois vícios opostos?",
        "A avareza e o esbanjamento de moedas de prata.",
        "A covardia (falta de bravura diante do perigo) e a temeridade (excesso irresponsável de arrojo).",
        "A mentira descarada e a tagarelice em feiras públicas.",
        "A preguiça matinal e a insônia provocada por febres corporais.",
        "A ambição desmedida por honras e a submissão humilhante a tiranos.",
        "B",
        "A coragem é a justa medida no enfrentamento do perigo, evitando tanto a paralisia do covarde quanto o arrojo cego e destrutivo do temerário."
    ))

    questoes_brutas.append((
        6, "EM13CHS502", "basico",
        "Qual é o papel da Prudência (Phrónesis) na vida ética descrita por Aristóteles na Ética a Nicômaco?",
        "Calcular a velocidade de deslocamento de frotas navais em alto-mar.",
        "Atuar como sabedoria prática que permite deliberar com discernimento sobre qual é o melhor meio para alcançar fins justos em situações concretas.",
        "Impor que todos os cidadãos usem roupas confeccionadas com tecidos de lã escura.",
        "Proibir a realização de debates políticos na ágora durante as tardes de calor.",
        "Determinar o peso exato de sacas de cevada vendidas nos mercados locais.",
        "B",
        "A phrónesis é a virtude intelectual prática que guia o homem a discernir o justo meio e agir com equilíbrio diante da complexidade da vida real."
    ))

    questoes_brutas.append((
        7, "EM13CHS104", "basico",
        "O Período Helenístico da filosofia grega teve início após qual grande acontecimento histórico e geopolítico?",
        "A construção das primeiras pirâmides de pedra no vale do rio Nilo.",
        "A conquista da Grécia pelas tropas macedônicas de Alexandre Magno e a consequente dissolução da soberania das cidades-estado (pólis).",
        "A assinatura de tratados comerciais entre navegadores fenícios e marinheiros etruscos.",
        "A expulsão definitiva de todos os comerciantes de vinho da Península Ibérica.",
        "A fundação da primeira fábrica de ferramentas agrícolas de ferro na Europa central.",
        "B",
        "Com o império de Alexandre Magno, a pólis clássica perdeu sua autonomia, transformando o antigo cidadão em súdito de um vasto império e gerando nova postura existencial."
    ))

    questoes_brutas.append((
        8, "EM13CHS104", "basico",
        "Diante da perda da autonomia política da pólis no Helenismo, qual foi a principal transformação sofrida pela reflexão filosófica?",
        "Passou a se dedicar exclusivamente ao cálculo de trajetórias de cometas celestes.",
        "Converteu-se em uma terapêutica da alma voltada a ensinar ao indivíduo a serenidade interior e a paz de espírito em um mundo de incertezas.",
        "Limitou-se a traduzir poemas trágicos para dialetos falados em ilhas remotas.",
        "Proibiu o ensino de línguas alfabéticas em todas as escolas de educação básica.",
        "Substituiu a escrita em papiros pelo uso exclusivo de placas de argila cozida.",
        "B",
        "A filosofia helenística tornou-se uma arte de viver e um refúgio interior para o sujeito que não mais encontrava amparo na participação política local."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "O filósofo Epicuro de Samos estabeleceu sua comunidade filosófica em Atenas nos arredores de sua casa. Como esse espaço ficou conhecido na história da filosofia?",
        "O Ginásio Militar da Fronteira.",
        "O Jardim (Kepos), aberto fraternalmente à convivência de homens, mulheres e pessoas escravizadas.",
        "O Tribunal de Sentenças Civis.",
        "O Arsenal de Armaduras de Bronze.",
        "O Observatório de Estrelas Marinhas.",
        "B",
        "O Jardim de Epicuro acolhia a todos de modo igualitário e comunitário, valorizando a amizade sincera, a conversa filosófica e a vida frugal."
    ))

    questoes_brutas.append((
        10, "EM13CHS501", "basico",
        "Qual é o objetivo ético supremo buscado pelos adeptos do Epicurismo?",
        "A conquista de postos de comando no senado imperial romano.",
        "A conquista da Ataraxia (imperturbabilidade da alma) e da Aponia (ausência de dor física no corpo).",
        "A construção de navios mercantes com três fileiras de remos reforçados.",
        "O acúmulo de propriedades rurais em planícies irrigadas por rios caudalosos.",
        "A vitória em corridas atléticas realizadas durante festivais religiosos.",
        "B",
        "Para Epicuro, o bem supremo reside na paz de espírito e na tranquilidade interior, livre de ansiedades e angústias desnecessárias."
    ))

    questoes_brutas.append((
        11, "EM13CHS501", "basico",
        "Na classificação dos prazeres e desejos formulada por Epicuro, qual categoria abrange beber água quando se tem sede e comer pão simples quando se tem fome?",
        "Desejos artificiais criados pela publicidade mercantil.",
        "Desejos Naturais e Necessários, indispensáveis para a sobrevivência e fáceis de serem satisfeitos.",
        "Desejos vãos que geram ansiedade perpétua na mente humana.",
        "Desejos miraculosos concedidos por oráculos durante cerimônias noturnas.",
        "Desejos suntuosos próprios de nobres e monarcas absolutistas.",
        "B",
        "Os desejos naturais e necessários são limitados pela própria biologia: exigem pouco para ser atendidos e geram a satisfação do equilíbrio corpóreo e mental."
    ))

    questoes_brutas.append((
        12, "EM13CHS501", "basico",
        "O 'Tetrapharmakos' de Epicuro propõe quatro remédios da razão para curar a angústia humana. Qual é a resposta epicurista para o medo da morte?",
        "A promessa de que a alma reencarnará no corpo de reis poderosos e generais condecorados.",
        "A constatação de que a morte nada é para nós: enquanto existimos, a morte não está presente; e quando a morte chega, nós já não existimos.",
        "A obrigação de construir túmulos monumentais de mármore para preservar o corpo intacto.",
        "A certeza de que os deuses castigam apenas os pescadores que navegam sem redes de linho.",
        "A esperança mágica de que a juventude biológica durará por vários séculos seguidos.",
        "B",
        "Sendo a alma composta de átomos mortais, com a morte cessa toda sensação e consciência; portanto, temê-la é temer uma ilusão que nunca coexistirá conosco."
    ))

    questoes_brutas.append((
        13, "EM13CHS501", "basico",
        "A escola filosófica do Estoicismo recebeu esse nome em razão de seu fundador, Zenão de Cício, lecionar em qual local de Atenas?",
        "No interior de cavernas escuras localizadas em montanhas rochosas.",
        "Sob as colunatas pintadas da praça pública de Atenas (a Stoa Poikile ou Pórtico Pintado).",
        "A bordo de barcos mercantes atracados no porto do Pireu.",
        "Nos aposentos privados de imperadores da dinastia macedônica.",
        "Em oficinas de fundição de cobre e armaduras militares.",
        "B",
        "Zenão ensinava no Pórtico Pintado (Stoa Poikile), de onde se originou a denominação de seus seguidores como estóicos."
    ))

    questoes_brutas.append((
        14, "EM13CHS502", "basico",
        "Entre os grandes pensadores do estoicismo romano, quem foi o imperador que escreveu suas reflexões íntimas de autoexame moral em tendas militares durante campanhas no rio Danúbio?",
        "Júlio César.",
        "Marco Aurélio.",
        "Alexandre Magno.",
        "Nero Cláudio.",
        "Otávio Augusto.",
        "B",
        "Marco Aurélio governou Roma como o 'imperador-filósofo', registrando suas profundas reflexões estóicas em sua obra pessoal conhecida como Meditações."
    ))

    questoes_brutas.append((
        15, "EM13CHS502", "basico",
        "No Manual de Epicteto, o filósofo estabelece a célebre separação entre as coisas que governam nossa existência. Quais são as coisas que dependem de nós?",
        "A quantidade de chuvas nas lavouras e a duração das estações do ano.",
        "Nossos pensamentos, julgamentos morais, desejos, impulsos e a atitude ética diante da vida.",
        "A riqueza financeira de nossos vizinhos e o sucesso comercial de feiras locais.",
        "A saúde biológica perfeita de nosso corpo e a imortalidade física terrena.",
        "A reputação e a opinião que os outros cidadãos manifestam sobre nós nas ruas.",
        "B",
        "Para Epicteto, apenas o universo interior (nossa razão, juízos e virtudes) está sob nosso domínio direto, constituindo a cidadela inexpugnável da liberdade."
    ))

    questoes_brutas.append((
        16, "EM13CHS502", "basico",
        "O sábio estóico busca cultivar a 'Apatheia'. Qual é o verdadeiro significado desse ideal ético?",
        "A crueldade voluntária contra pessoas em situação de vulnerabilidade social.",
        "A libertação das paixões irracionais destrutivas (ira, pânico, inveja) e a conquista da serenidade da razão.",
        "A recusa em prestar socorro a amigos que necessitam de auxílio material.",
        "A perda total da memória de acontecimentos vivenciados na infância.",
        "O hábito de dormir de olhos abertos para evitar sonhos noturnos perturbadores.",
        "B",
        "Apatheia não significa indiferença apática ao próximo, mas o autodomínio sereno que extirpa as paixões desgovernadas que escravizam a consciência."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "O filósofo Diógenes de Sínope foi o expoente máximo da escola cínica. Qual atitude pública marcou sua busca pela verdade em Atenas?",
        "Organizar desfiles com cavalos brancos pelas ruas centrais da cidade.",
        "Caminhar em plena luz do meio-dia carregando uma lamparina acesa dizendo procurar um homem honesto e autêntico.",
        "Distribuir moedas de prata a comerciantes para comprar ferramentas agrícolas.",
        "Pintar murais com figuras geométricas nos muros do porto municipal.",
        "Recitar tratados jurídicos em latim arcaico durante o pôr do sol.",
        "B",
        "Diógenes usava a lâmpada à luz do dia para desmascarar a hipocrisia e a falsidade dos cidadãos que viviam de máscaras e convenções sociais artificiais."
    ))

    questoes_brutas.append((
        18, "EM13CHS101", "basico",
        "Diógenes de Sínope escolheu um modo de vida radicalmente despojado para provar sua autossuficiência moral (Autarkeia). Onde ele costumava dormir nas ruas de Atenas?",
        "Em palácios de mármore construídos por governantes da Macedônia.",
        "Dentro de um grande barril de cerâmica (pithos) colocado na praça pública.",
        "No alto de torres de vigilância militar de fortalezas costeiras.",
        "Em aposentos luxuosos decorados com tapetes de seda importados da Pérsia.",
        "A bordo de carruagens douradas reservadas a magistrados da corte.",
        "B",
        "Morando em um barril de barro, Diógenes demonstrava que a liberdade moral não necessita de luxos materiais nem de propriedades suntuosas."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Quando o imperador Alexandre Magno visitou Diógenes de Sínope e perguntou o que poderia conceder ao filósofo, qual foi a célebre resposta de Diógenes?",
        "'Desejo ser nomeado governador de todas as províncias da Ásia Menor.'",
        "'Sim, afasta-te do meu sol.'",
        "'Preciso de dez carruagens repletas de barras de ouro maciço.'",
        "'Construa para mim um templo de mármore branco nas colinas de Atenas.'",
        "'Ensine minhas tropas a empunhar lanças de combate de longo alcance.'",
        "B",
        "Com sua resposta desconcertante, Diógenes provou que a soberania de sua liberdade interior e autossuficiência moral era superior a todo o poder do maior conquistador da Terra."
    ))

    questoes_brutas.append((
        20, "EM13CHS104", "basico",
        "Diógenes de Sínope foi pioneiro ao recusar lealdade exclusiva a fronteiras nacionais fechadas, proclamando-se:",
        "Um soldado fiel das legiões militares de Roma.",
        "Um Cidadão do Mundo (Cosmopolita), membro da comunidade humana universal.",
        "Um sacerdote exclusivo dos oráculos da montanha do Parnaso.",
        "Um juiz encarregado de fixar impostos sobre a navegação marítima.",
        "Um embaixador diplomático da coroa persa nas cidades gregas.",
        "B",
        "Ao afirmar-se cosmopolita, Diógenes rompeu com o provincianismo xenofóbico da pólis clássica, inaugurando o ideal de cidadania planetária universal."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao contrastar a visão de virtude de Platão e Sócrates com a teoria aristotélica da Ética a Nicômaco, percebe-se uma divergência fundamental sobre o aprendizado moral, pois:",
        "Sócrates afirmava que a virtude depende de rituais com fogo e Aristóteles recorria a cartas astrológicas.",
        "Para Sócrates e Platão, bastava conhecer o Bem teoricamente para praticá-lo; para Aristóteles, o saber teórico não basta: a virtude exige a prática deliberada e a formação contínua do hábito.",
        "Ambos defendiam que as crianças devem ser educadas em internatos militares sem contato com a arte poética.",
        "Aristóteles negava a existência da razão e Sócrates defendia o hedonismo corporal irrestrito.",
        "Platão sustentava que apenas os agricultores manuais possuem capacidade de deliberar com justiça.",
        "B",
        "Aristóteles supera o intelectualismo moral socrático: a excelência ética exige disciplina do caráter e treinamento prático; saber o que é certo não garante agir com retidão sem hábito."
    ))

    questoes_brutas.append((
        22, "EM13CHS501", "intermediario",
        "Na análise aristotélica da virtude moral, por que a mediania (Justo Meio) não pode ser compreendida como uma média matemática rígida e fria?",
        "Porque os filósofos gregos desconheciam as regras elementares de soma e subtração de números inteiros.",
        "Porque o justo meio é relativo à situação concreta e às características do agente: agir de modo corajoso exige avaliar as forças reais, o momento certo, a pessoa correta e a finalidade justa.",
        "Porque as leis da pólis proibiam o uso de números pares em tratados de moral prática.",
        "Porque o justo meio aplica-se exclusivamente a compras e vendas realizadas em feiras de tecidos.",
        "Porque Aristóteles defendia que as virtudes deveriam ser sorteadas em vasos de cerâmica a cada lua nova.",
        "B",
        "A mesótes não é um meio aritmético abstrato (como 5 entre 0 e 10), mas a medida qualitativa adequada: o que é alimento suficiente para um atleta olímpico seria excesso para um iniciante."
    ))

    questoes_brutas.append((
        23, "EM13CHS501", "intermediario",
        "Por que as riquezas financeiras e o dinheiro não podem constituir, de acordo com Aristóteles, a Felicidade Suprema (Eudaimonia)?",
        "Porque as moedas de prata perdem o brilho quando armazenadas em baús de madeira úmida.",
        "Porque o dinheiro é apenas um meio intermediário para alcançar outras coisas, nunca sendo desejado por si mesmo como um fim último realizador da alma.",
        "Porque as leis comerciais de Atenas proibiam a posse individual de propriedades agrícolas produtivas.",
        "Porque a riqueza atrai tempestades marítimas que afundam barcos de pesca nas praias litorâneas.",
        "Porque o dinheiro foi inventado por governantes estrangeiros para cobrar tributos de camponeses.",
        "B",
        "A felicidade suprema deve ter valor realizador em si mesma; o dinheiro é puramente instrumental, servindo apenas para comprar bens ou serviços que satisfaçam necessidades."
    ))

    questoes_brutas.append((
        24, "EM13CHS501", "intermediario",
        "Qual é a acusação moral infundada que os críticos tradicionais formulavam contra Epicuro na Antiguidade, e como a sua verdadeira filosofia a desmente?",
        "Acusavam Epicuro de fabricar moedas falsas; ele provou que trabalhava em oficinas de cantaria de mármore.",
        "Acusavam o epicurismo de pregar o desregramento sensual e as orgias; na realidade, Epicuro defendia a frugalidade sóbria (pão e água), a moderação dos apetites e a paz de espírito.",
        "Afirmavam que Epicuro era um general militar disfarçado; ele comprovou que nunca empunhou espadas de bronze.",
        "Diziam que o Jardim era um tribunal secreto; ele demonstrou que ali funcionava uma fábrica de calçados de couro.",
        "Sustentavam que os epicuristas não sabiam escrever; Epicuro publicou compêndios astronômicos sobre o céu.",
        "B",
        "O hedonismo de Epicuro é racional e austero: prazer supremo é a ausência de dor no corpo e perturbação na mente; excessos sensoriais geram ressacas, doenças e angústias maiores."
    ))

    questoes_brutas.append((
        25, "EM13CHS501", "intermediario",
        "Por que a política partidária e a busca obsessiva por cargos de poder eram rejeitadas por Epicuro como fontes de profunda infelicidade humana?",
        "Porque as eleições municipais consumiam muitas tochas de azeite durante as sessões noturnas na ágora.",
        "Porque a ambição política constitui um desejo não natural e vão, insaciável por natureza, que expõe o indivíduo a intrigas, rivalidades, ódios públicos e permanente ansiedade da mente.",
        "Porque os governantes de cidades vizinhas proibiam o plantio de oliveiras em terras públicas.",
        "Porque os tribunais cívicos exigiam que todos os magistrados morassem em tendas de couro fora da cidade.",
        "Porque as leis atenienses impediam que os oradores bebessem água fresca antes de pronunciarem discursos.",
        "B",
        "Epicuro cunhou a máxima 'Vive na obscuridade' (Lathe biosas): a glória pública e o poder escravizam o homem aos caprichos da multidão, destruindo a serenidade da ataraxia."
    ))

    questoes_brutas.append((
        26, "EM13CHS502", "intermediario",
        "De acordo com a física panteísta do Estoicismo, como se compreende a relação entre a Razão Cósmica (Logos) e os acontecimentos do mundo natural?",
        "O cosmos é governado por sorteios acidentais e tempestades sem qualquer conexão lógica ou harmônica.",
        "O universo é uma totalidade harmônica viva permeada pelo Logos racional e providencial, no qual tudo o que ocorre decorre de uma necessidade sábia e inflexível da natureza.",
        "Os acontecimentos terrenos dependem exclusivamente das decisões tomadas por marinheiros em travessias oceânicas.",
        "O destino dos planetas é calculado por artesãos que fundem lingotes de ferro em fornos quentes.",
        "As leis da física deixam de funcionar durante os períodos em que ocorrem colheitas agrícolas de cereais.",
        "B",
        "Para os estóicos, o cosmos é racional e interligado por um princípio divino imanente; viver bem é viver em conformidade com essa ordem cósmica universal."
    ))

    questoes_brutas.append((
        27, "EM13CHS502", "intermediario",
        "Na psicologia estoica de Epicteto, o que provoca as dores psíquicas, o desespero e a amargura nos seres humanos diante de fatos adversos?",
        "A picada de insetos voadores que habitam áreas pantanosas em épocas de chuva.",
        "Não os acontecimentos externos em si mesmos, mas os julgamentos subjetivos e interpretações equivocadas que a mente humana formula sobre esses acontecimentos.",
        "A ingestão de águas de poços artesianos que contêm excesso de sais minerais dissolvidos.",
        "A mudança repentina no preço do pão de centeio vendido nos mercados populares das capitais.",
        "A falta de uniformes de linho claro em escolas de primeiras letras para jovens da periferia.",
        "B",
        "Máxima clássica de Epicteto: 'Não são as coisas que perturbam os homens, mas o julgamento que eles fazem das coisas'. A demissão ou a doença só nos arruínam se julgarmos que o bem supremo se perdeu."
    ))

    questoes_brutas.append((
        28, "EM13CHS502", "intermediario",
        "Como a atitude estoica do Amor Fati (amor afirmativo ao destino) se diferencia da mera resignação passiva e derrotista perante o sofrimento?",
        "Ela exige que o indivíduo destrua todos os seus pertences materiais e passe a viver em barcos de pesca.",
        "Ela não é acomodação covarde, mas a acolhida consciente da realidade: ver cada dificuldade como um exercício pedagógico necessário para testar, temperar e aperfeiçoar a virtude moral.",
        "Ela obriga os cidadãos a aplaudirem invasões estrangeiras que saqueiem suas cidades de residência.",
        "Ela determina que as famílias não construam muros de proteção contra animais selvagens nas fazendas.",
        "Ela defende que as pessoas devem comemorar a queima acidental de seus estoques de mantimentos.",
        "B",
        "O estóico não lamenta o que o destino traz: ele assume cada obstáculo como oportunidade de praticar a serenidade, a paciência e a integridade, transformando tropeços em matéria de virtude."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Ao rejeitar as leis civis, títulos honoríficos e posses de bens, qual era o objetivo moral central de Diógenes de Sínope e da escola cínica?",
        "Incentivar o banditismo armado em estradas rurais para enriquecer líderes comunitários.",
        "Desmascarar a hipocrisia e a artificialidade das convenções sociais, provando que a liberdade autêntica exige o retorno à simplicidade da natureza e a autossuficiência moral plena.",
        "Obrigar as cidades gregas a adotarem o sistema monetário utilizado por mercadores de Tiro e Sídon.",
        "Proibir a realização de peças de teatro dramático e competições musicais nos festivais de primavera.",
        "Exigir que todos os habitantes do Mediterrâneo abandonassem suas casas para dormirem em tendas de couro.",
        "B",
        "O cinismo propunha um choque ético: mostrar que o homem moderno tornara-se escravo de futilidades criadas pela opinião pública, perdendo a soberania de seu próprio ser natural."
    ))

    questoes_brutas.append((
        30, "EM13CHS104", "intermediario",
        "Na comparação entre a Ataraxia de Epicuro e a Apatheia dos estóicos, constata-se uma diferença de fundamentação filosófica, uma vez que:",
        "Epicuro acreditava em milagres mágicos e os estóicos defendiam que a terra era sustentada por elefantes gigantes.",
        "Epicuro busca a tranquilidade pela satisfação comedida dos desejos corporais simples e repouso no Jardim; os estóicos buscam a imperturbabilidade pelo domínio absoluto da razão e cumprimento firme do dever cósmico.",
        "Ambos defendiam que a única forma de alcançar a paz interior era combater em frotas navais em alto-mar.",
        "Epicuro proibia a amizade fraternal e os estóicos defendiam o acúmulo de propriedades comerciais no porto.",
        "Os estóicos pregavam a busca desenfreada do luxo e Epicuro exigia a prática diária de jejuns rigorosos.",
        "B",
        "A ataraxia epicurista repousa no prazer negativo da ausência de dores na vida comunitária privada; a apatheia estóica funda-se na virtude cívica do dever heroico perante a Providência cósmica."
    ))

    questoes_brutas.append((
        31, "EM13CHS502", "intermediario",
        "Em suas Cartas a Lucílio, Lúcio Aneu Sêneca reflete intensamente sobre a 'Brevidade da Vida'. Qual advertência o filósofo estóico formula contra o desperdício do tempo humano?",
        "Que as horas do dia devem ser contadas por ampulhetas de vidro instaladas nas praças públicas.",
        "Que a vida não é curta por natureza, mas nós a tornamos breve ao desperdiçá-la em ambições fúteis, luxos vazios e preocupações vãs com o futuro, adiando indefinidamente a verdadeira existência.",
        "Que os jovens devem trabalhar dezoito horas diárias em plantações de uva para acumularem heranças de prata.",
        "Que o governo imperial deveria aprovar calendários anuais com mais de quinhentos dias corridos de trabalho.",
        "Que a leitura de tratados filosóficos consome tempo útil que deveria ser empregado em treinos de cavalaria.",
        "B",
        "Sêneca constata com lucidez: 'Não temos pouco tempo, mas perdemos muito'. A sabedoria estóica ensina a tomar posse do presente e a não subordinar a vida a caprichos de terceiros."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Como a concepção de Amizade (Philia) no Jardim de Epicuro se articulava com o projeto de felicidade comunitária dos seus seguidores?",
        "Como uma associação comercial voltada a comprar navios de carga para transportar azeite e trigo.",
        "Como o refúgio seguro de lealdade fraterna, apoio mútuo e conversação filosófica serena, considerado o maior dos bens para garantir a tranquilidade da alma ao longo da existência.",
        "Como uma aliança militar secreta destinada a derrubar os governantes das cidades vizinhas de Atenas.",
        "Como um contrato de casamento formal assinado obrigatoriamente perante magistrados municipais.",
        "Como uma sociedade de caçadores encarregada de capturar animais silvestres para banquetes do imperador.",
        "B",
        "Para Epicuro, a amizade autêntica é o bálsamo da vida: proporciona acolhimento emocional recíproco e segurança existencial sem os perigos da competição política egoísta."
    ))

    questoes_brutas.append((
        33, "EM13CHS501", "intermediario",
        "Na tabela das virtudes de Aristóteles, na esfera da ação que envolve o uso de recursos financeiros e do dinheiro, qual atitude expressa a virtude moral?",
        "Guardar todas as moedas de prata no fundo de poços de pedra sem nunca utilizá-las.",
        "A Generosidade (ou Liberalidade), que equilibra o gasto equilibrado e o apoio justo aos outros, evitando a mesquinharia avarenta e o esbanjamento pródigo inconsequente.",
        "Gastar todo o patrimônio da família em um único banquete com vinhos raros importados da ilha de Chipre.",
        "Pedir empréstimos diários a comerciantes do porto sem intenção de quitar as dívidas assumidas.",
        "Exigir que os funcionários de propriedades agrícolas trabalhem sem receber alimentação diária.",
        "B",
        "A generosidade aristotélica administra os bens materiais com nobreza e justeza: sabe dar e receber na medida correta, fugindo da avareza sórdida e da ostentação fútil."
    ))

    questoes_brutas.append((
        34, "EM13CHS104", "intermediario",
        "Por que as filosofias helenísticas são frequentemente descritas pelos historiadores do pensamento como 'Filosofias de Tempos de Crise'?",
        "Porque os filósofos desse período passavam fome devido à queima de armazéns de trigo em guerras costeiras.",
        "Porque surgiram como respostas existenciais concretas ao colapso das certezas cívicas da pólis, oferecendo guias práticos de sobrevivência espiritual e paz interna em um mundo turbulento.",
        "Porque as escolas helenísticas foram proibidas de imprimir livros em virtude de decretos imperiais romanos.",
        "Porque os cidadãos gregos perderam o interesse pelo estudo da geometria euclidiana e da física mecânica.",
        "Porque as bibliotecas públicas das grandes capitais foram transformadas em estábulos de cavalaria militar.",
        "B",
        "O Helenismo respondeu à angústia do indivíduo desamparado diante de impérios despóticos, transformando a filosofia em salvação pessoal, autodomínio e terapia moral diária."
    ))

    questoes_brutas.append((
        35, "EM13CHS502", "intermediario",
        "Em que consiste a técnica terapêutica estóica da 'Praemeditatio Malorum' (Premeditação das Adversidades)?",
        "Em praticar rituais oraculares com cinzas de carvão vegetal para prever a data exata de naufrágios.",
        "Em antecipar mentalmente as possíveis perdas, desgraças e tragédias que podem acontecer para treinar a serenidade da alma e não ser surpreendido nem abatido pelo pânico diante do inevitável.",
        "Em fugir apressadamente de cidades litorâneas sempre que o céu estiver coberto por nuvens escuras.",
        "Em recusar convites para festas cívicas para não contrair enfermidades contagiosas de outros cidadãos.",
        "Em guardar reservas de água potável em vasos de argila enterrados no quintal de casa durante o inverno.",
        "B",
        "A premeditação das adversidades dessensibiliza o medo: ao contemplar com serenidade a hipótese da doença, da perda material ou da morte, o sábio liberta-se do terror do imprevisto."
    ))

    questoes_brutas.append((
        36, "EM13CHS501", "intermediario",
        "No livro I da Ética a Nicômaco, Aristóteles refuta a tese vulgar de que a Felicidade consistiria no 'Prazer Sensorial Bruto da Carne'. Qual argumento sustenta essa refutação?",
        "Aristóteles afirma que os alimentos doces provocam cáries dentárias nos jovens de escolas atenienses.",
        "Ele argumenta que reduzir a felicidade aos prazeres corporais do comer, beber e copular iguala o ser humano aos animais de pasto, rebaixando a dignidade sublime da razão humana à condição de bestas servis.",
        "Ele comprova que os animais da savana vivem mais tempo do que os homens que praticam ginástica diária.",
        "Ele demonstra que as carnes assadas perdem o sabor nutritivo quando temperadas com ervas marinhas secas.",
        "Ele proíbe que os agricultores comam pão fresco após o término dos trabalhos de colheita no campo.",
        "B",
        "Uma vida voltada apenas ao prazer sensorial é escrava dos apetites físicos que compartilhamos com os bois; o homem só floresce plenamente quando realiza a atividade de sua mente racional."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Qual é a relação entre o conceito grego de 'Autarkeia' (autossuficiência moral) e a conduta de Diógenes de Sínope ao mendigar pelas ruas de Atenas?",
        "Diógenes mendigava porque pretendia acumular moedas para comprar fazendas de trigo na Beócia.",
        "Ele mendigava para demonstrar sua total independência em relação ao julgamento alheio e provar que precisava de muito pouco para viver com dignidade, subvertendo a vergonha burguesa da pobreza material.",
        "Ele era forçado por magistrados civis a pedir esmolas como punição penal por não prestar serviço militar.",
        "Ele acreditava que os deuses castigavam com febres corporais aqueles que trabalhavam em oficinas de ferro.",
        "Ele pretendia fundar um banco municipal com os donativos recolhidos nas feiras populares de tecidos.",
        "B",
        "A autarkeia cínica é a posse soberana de si: mendigar sem vergonha mostrava que as noções de honra e status social eram ilusões arbitrárias que não diminuíam a grandeza do sábio livre."
    ))

    questoes_brutas.append((
        38, "EM13CHS502", "intermediario",
        "Na reflexão de Marco Aurélio em suas Meditações, como o dever de governar o Império Romano era conciliado com os princípios estóicos da igualdade e fraternidade universal?",
        "Marco Aurélio ordenou que todos os povos conquistados fossem transformados em remadores de frotas navais.",
        "Ele considerava o império uma responsabilidade cívica sagrada e pesada, exercida como serviço ao bem comum dos cidadãos, vendo a todos como irmãos pertencentes à mesma grande Cidade Cósmica do Logos.",
        "Ele transferiu o tesouro público de Roma para templos religiosos localizados em ilhas do mar Egeu.",
        "Ele proibiu a concessão de cidadania a qualquer pessoa nascida fora dos limites geográficos da Itália.",
        "Ele exigiu que os senadores romanos prestassem juramentos de lealdade montados em camelos de carga.",
        "B",
        "Marco Aurélio via a coroa imperial não como privilégio de vaidade egoísta, mas como dever austero de servir à humanidade, fundamentado no cosmopolitismo e na razão estóica universal."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Em contraposição ao intelectualismo que reduz a ética a teorias de livros, como o pensador francês Pierre Hadot define a prática da filosofia helenística?",
        "Como um passatempo reservado a nobres que se reuniam em salões de banquetes durante o inverno.",
        "Como um 'Modo de Vida' e um conjunto articulado de 'Exercícios Espirituais' diários destinados a transformar profundamente a visão de mundo e a personalidade moral do praticante.",
        "Como um curso profissionalizante voltado a ensinar contabilidade comercial a navegadores marítimos.",
        "Como uma doutrina mágica transmitida exclusivamente por meio de juramentos secretos em cavernas.",
        "Como uma série de disputas oratórias destinadas a eleger deputados para o parlamento municipal de Atenas.",
        "B",
        "Hadot demonstra que, na Antiguidade, a filosofia não era teoria pura de gabinete, mas conversão da existência: meditação, controle dos desejos e treino do caráter no cotidiano da vida real."
    ))

    questoes_brutas.append((
        40, "EM13CHS504", "intermediario",
        "Na recepção contemporânea da ética das virtudes de Aristóteles na economia, a abordagem de Amartya Sen e Martha Nussbaum propõe avaliar o desenvolvimento dos países com base:",
        "No valor de mercado das ações financeiras negociadas em bolsas de valores internacionais.",
        "Na capacidade substantiva real das pessoas de serem e fazerem aquilo que têm razões para valorizar (saúde, instrução, liberdade e realização plena das capacidades humanas).",
        "Na quantidade de minérios de ferro exportados por portos alfandegários para indústrias automotivas.",
        "No número de edifícios construídos com estruturas de concreto armado em capitais metropolitanas.",
        "Na velocidade com que as rodovias de asfalto cruzam as reservas florestais no interior dos países.",
        "B",
        "Sen e Nussbaum traduzem a eudaimonia aristotélica em termos modernos: o verdadeiro desenvolvimento não é o mero crescimento do PIB, mas a expansão das capacidades e liberdades reais de cada ser humano."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a famosa passagem do Livro II da Ética a Nicômaco: 'A virtude moral é uma mediania entre dois vícios, um pelo excesso e outro pelo defeito; e ela é tal por visar o meio-termo nas paixões e nas ações.' De que maneira essa formulação diferencia a virtude aristotélica da obediência a leis exteriores formais?",
        "Negando que a razão humana tenha qualquer utilidade na hora de tomar decisões práticas no convívio comunitário.",
        "Evidenciando que a virtude não é uma lista de proibições mecânicas prontas, mas a capacidade interna autônoma de calibrar o sentimento e a ação de modo ótimo diante da singularidade de cada situação irrepetível.",
        "Afirmando que as virtudes morais deixam de ter valor prático sempre que o Estado se encontra em guerras bélicas.",
        "Determinando que os cidadãos devem seguir à risca os mandamentos de tabelas astronômicas desenhadas em cerâmica.",
        "Provando que apenas os generais de exércitos militares conseguem agir com temperança e prudência moral.",
        "B",
        "**Etapa 1:** Interpretar a essência da mesótes aristotélica como sabedoria qualitativa situada.\n**Etapa 2:** Concluir que a ética aristotélica é das virtudes e do caráter (não do mero dever deôntico abstrato): agir bem exige o discernimento do justo meio no momento certo, em relação à pessoa certa e pelo motivo nobre."
    ))

    questoes_brutas.append((
        42, "EM13CHS501", "dificil",
        "Em sua Ética a Nicômaco, Aristóteles formula o conceito de 'Akrásia' (Incontinência ou Fraqueza da Vontade), em que o sujeito sabe intelectualmente o que é correto, mas cede ao impulso da paixão desmedida. Como esse conceito desmonta a tese socrática do 'Intelectualismo Moral'?",
        "Provando que Sócrates nunca escreveu tratados de geometria durante sua vida em Atenas.",
        "Demonstrando que o conhecimento teórico abstrato do Bem é insuficiente para garantir a retidão moral, sendo necessária a disciplina constante do desejo e a consolidação do hábito virtuoso no caráter do indivíduo.",
        "Afirmando que a razão humana é incapaz de distinguir entre o frio do inverno e o calor do verão em cidades costeiras.",
        "Defendendo que os criminosos devem ser inocentados caso comprovem ter lido livros de poesia trágica grega.",
        "Sustentando que a vontade humana é movida exclusivamente por influências de constelações astrais no céu.",
        "B",
        "**Etapa 1:** Analisar o intelectualismo de Sócrates, que afirmava que ninguém erra voluntariamente e que o mal é mera ignorância.\n**Etapa 2:** Concluir com a observação realista de Aristóteles: a akrasia comprova que o homem pode ter o saber teórico do bem, mas sucumbir à paixão desregrada se não possuir a virtude moral construída pelo hábito prático."
    ))

    questoes_brutas.append((
        43, "EM13CHS104", "dificil",
        "Considere o contraste entre o modelo político clássico de Aristóteles (na obra A Política) e a postura de Diógenes de Sínope no Helenismo. Enquanto Aristóteles proclama que 'o homem é por natureza um animal político' (Zoon Politikon), Diógenes declara-se 'Cidadão do Mundo' (Cosmopolita). Qual ruptura teórica profunda sobre a pertença cívica se estabelece nesse confronto?",
        "A concordância de que as cidades-estado devem proibir o comércio marítimo com nações que cultivam trigo.",
        "A passagem da comunidade ética restrita da pólis grega para a fraternidade humana universal: Diógenes desterritorializa a cidadania, afirmando que a dignidade humana independe dos muros e leis de um Estado particular.",
        "A exigência de que todos os cidadãos atenienses prestem homenagens públicas a estátuas de deuses do mar Egeu.",
        "A tese de que a política deve ser administrada exclusivamente por médicos especializados em doenças de pele.",
        "A conclusão de que a vida em sociedade deve ser abolida para que a humanidade retorne ao modo de caçadores nômades.",
        "B",
        "**Etapa 1:** Compreender a tese aristotélica da realização humana circunscrita à comunidade fechada da pólis.\n**Etapa 2:** Evidenciar a revolução cosmopolita de Diógenes: ao recusar os preconceitos locais e proclamar-se cosmopolita, liberta a dignidade do indivíduo das amarras da lealdade nacionalista estreita."
    ))

    questoes_brutas.append((
        44, "EM13CHS501", "dificil",
        "Analise a máxima fundamental de Epicuro na Carta a Meneceu: 'A morte nada é para nós. Quando existimos, nós a morte não é; quando a morte é, nós não somos mais.' Como essa formulação lógica materialista desmonta o poder de coerção psicológica dos mitos religiosos sobre a alma humana?",
        "Negando que os corpos dos seres humanos sejam formados por elementos químicos presentes na terra e no ar.",
        "Evidenciando que a alma é mortal e material; com o fim da consciência na morte, todo sofrimento ou castigo no além-túmulo torna-se impossível, libertando o indivíduo do terror paralisante do inferno.",
        "Afirmando que as tempestades de chuva são provocadas por deuses irritados com as faltas dos agricultores.",
        "Sustentando que os rituais funerários devem ser realizados apenas em noites de eclipse total da lua.",
        "Provando que as almas dos guerreiros viajam para ilhas distantes onde o trigo nasce sem necessidade de arado.",
        "B",
        "**Etapa 1:** Interpretar o atomismo mecanicista de Epicuro aplicado à finitude biológica da consciência humana.\n**Etapa 2:** Concluir com a crítica epicurista à superstição: o medo da punição divina eterna nos infernos é uma ficção que gera angústia vazia; a consciência extingue-se com o corpo e a morte é o repouso absoluto do nada."
    ))

    questoes_brutas.append((
        45, "EM13CHS502", "dificil",
        "No primeiro parágrafo do Manual de Epicteto, afirma-se: 'Entre as coisas que existem, algumas dependem de nós e outras não dependem de nós.' Como essa separação analítica serve de fundamento para a libertação da ansiedade e do estresse cotidiano na vida prática?",
        "Incentivando as pessoas a apostarem moedas de prata em jogos de dados para tentar prever o futuro financeiro.",
        "Deslocando a energia e o cuidado moral do indivíduo para a única esfera que ele pode realmente controlar (seus próprios julgamentos e ações), aceitando serenamente o que escapa ao seu domínio direto.",
        "Obrigando os cidadãos a se mudarem para cidades portuárias onde o trânsito de navios seja regulamentado pelo Estado.",
        "Exigindo que os trabalhadores rurais assinem contratos de trabalho em dias que não tenham vento forte no litoral.",
        "Determinando que os juízes de tribunais públicos não devam emitir pareceres sobre litígios comerciais de vizinhos.",
        "B",
        "**Etapa 1:** Compreender a divisão estóica fundamental entre controle interno inalienável e contingências externas incontroláveis.\n**Etapa 2:** Concluir que a causa primordial da angústia moderna é a tentativa ilusória de controlar o exterior (saúde dos outros, economia, fama), negligenciando o cultivo virtuoso de si mesmo."
    ))

    questoes_brutas.append((
        46, "EM13CHS501", "dificil",
        "Ao examinar a relação entre o Hedonismo de Epicuro e a Virtude Moral, como o filósofo demonstra que é impossível alcançar o prazer genuíno da Ataraxia sem praticar a sabedoria, a justiça e a temperança?",
        "Afirmando que a virtude é um conjunto de fórmulas matemáticas que os jovens devem recitar antes das refeições.",
        "Mostrando que atos injustos, gananciosos e desregrados geram o medo constante de ser descoberto e punido, envenenando a alma com a ansiedade da culpa e destruindo a paz interior necessária para desfrutar da vida.",
        "Defendendo que os comerciantes de cereais devem pagar tributos adicionais para custear cerimônias religiosas.",
        "Provando que os homens que praticam a justiça perdem o apetite por alimentos simples como pão e água pura.",
        "Exigindo que os moradores de cidades rurais instalem cercas de madeira ao redor de seus pomares de frutas.",
        "B",
        "**Etapa 1:** Analisar a interdependência entre prazer prudente e justiça na Carta a Meneceu de Epicuro.\n**Etapa 2:** Evidenciar que o injusto nunca atinge a ataraxia: mesmo que escape da lei dos homens, vive assombrado pelo pavor do flagrante e pela perturbação da mente, provando que a virtude é indispensável à verdadeira alegria."
    ))

    questoes_brutas.append((
        47, "EM13CHS502", "dificil",
        "No pensamento do filósofo estóico Sêneca em Sobre a Tranquilidade da Alma, como ele responde ao cidadão que deseja abandonar completamente os deveres sociais e o serviço público para fugir dos problemas da política corrupta?",
        "Ele recomenda que o cidadão se torne comandante de tropas militares para enriquecer com o saque de cidades conquistadas.",
        "Ele sustenta que o dever moral estóico exige não desertar da humanidade: mesmo quando as condições políticas forem hostis, o homem justo deve encontrar formas de ser útil à comunidade através do exemplo moral, da escrita e do conselho prudente.",
        "Ele aconselha a queima de todos os livros de filosofia prática para se dedicar exclusivamente à pesca artesanal de camarões.",
        "Ele defende que o cidadão deve se aliar a tiranos corruptos para obter vantagens comerciais na venda de tecidos.",
        "Ele determina que os homens justos devem morar em barcos sem remos e deixar as correntes marítimas os guiarem.",
        "B",
        "**Etapa 1:** Compreender a tensão entre o retiro pessoal contemplativo (*otium*) e o dever cívico ativo (*negotium*) em Sêneca.\n**Etapa 2:** Concluir com a ética cívica estóica: o sábio não foge do mundo em uma apatia egoísta; se a ágora estiver corrompida, ele atua no horizonte mais amplo da cidade cósmica da humanidade, educando pelo caráter e pela razão."
    ))

    questoes_brutas.append((
        48, "EM13CHS101", "dificil",
        "Considere a atitude de Diógenes de Sínope diante das instituições sociais consagradas (o casamento tradicional, o dinheiro cunhado, as leis positivas e os títulos de honra). Por que a crítica cínica a essas instituições constitui uma denúncia de alienação e perda da liberdade autêntica?",
        "Porque Diógenes afirmava que as leis foram escritas por artesãos que não entendiam de navegação marítima.",
        "Porque ele demonstrava que essas convenções artificiais criam necessidades falsas e dependências supérfluas que aprisionam os indivíduos na corrida pela vaidade social, tornando-os escravos do medo da opinião alheia.",
        "Porque os títulos de nobreza eram confeccionados em pergaminhos que apodreciam com as chuvas de inverno.",
        "Porque ele pretendia que o dinheiro fosse substituído pelo escambo de conchas marinhas em todas as praças públicas.",
        "Porque as cerimônias de casamento consumiam muito azeite para manter acesas as lamparinas dos convidados.",
        "B",
        "**Etapa 1:** Desconstruir a idolatria das convenções sociais através do método de choque e parresia cínica de Diógenes.\n**Etapa 2:** Concluir que o cinismo é uma filosofia de emancipação radical: ao demonstrar que o homem precisa apenas do essencial natural para viver bem, quebra as correntes da aprovação alheia e do consumo compulsivo."
    ))

    questoes_brutas.append((
        49, "EM13CHS502", "dificil",
        "Na obra Meditações, o imperador estóico Marco Aurélio formula repetidamente o exercício da 'Visão de Cima' (contemplar a Terra e as grandezas humanas do ponto de vista do cosmos inteiro). Qual o impacto ético e psicológico dessa prática espiritual?",
        "Incentivar o imperador a construir torres de observação militar nas fronteiras rochosas do norte da Europa.",
        "Reduzir à sua real insignificância temporal as guerras, os louvores mundanos, a fama passageira e as aflições cotidianas, pacificando a alma e fortalecendo o foco no cumprimento do dever justo e sereno no presente.",
        "Exigir que os soldados romanos utilizem mapas desenhados em couro de carneiro durante marchas no campo.",
        "Provocar o desinteresse total pelos tratados de paz assinados com generais de povos vizinhos do império.",
        "Determinar que os tribunais de justiça funcionem apenas em dias em que o céu esteja sem nuvens de tempestade.",
        "B",
        "**Etapa 1:** Analisar o exercício espiritual da Visão de Cima (Hadot e Marco Aurélio): perspectivar a pequenez da vida humana na imensidão cósmica.\n**Etapa 2:** Evidenciar o ganho ético: desinfla o orgulho e a arrogância dos poderosos, dissolve a ansiedade neurótica e reafirma a igualdade universal de todos os mortais perante a Razão Cósmica."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "Ao examinar a relação entre a 'Phrónesis' (Prudência) e as virtudes morais na Ética a Nicômaco, Aristóteles formula uma tese de mútua dependência: 'Não é possível ser verdadeiramente virtuoso sem prudência, nem prudente sem virtude moral.' Por que essas duas dimensões não podem ser separadas?",
        "Porque a phrónesis depende do pagamento de taxas anuais a academias fundadas por alunos de Platão.",
        "Porque a virtude moral define a retidão dos fins e das intenções da alma, mas é a phrónesis que calcula os meios justos para realizá-los; sem phrónesis, a boa intenção descamba no erro; sem virtude moral, o cálculo vira mera astúcia perversa.",
        "Porque os homens prudentes são obrigados por lei a trabalhar como contadores de frotas mercantis marítimas.",
        "Porque as virtudes morais são sorteadas por magistrados municipais no início de cada ano civil em Atenas.",
        "Porque a prudência é uma habilidade física adquirida apenas por atletas que vencem competições de salto em distância.",
        "B",
        "**Etapa 1:** Diferenciar virtude do caráter (retidão da meta/desejo) de virtude intelectual prática (discernimento deliberativo dos caminhos).\n**Etapa 2:** Concluir com a unidade da vida ética aristotélica: a inteligência sem retidão moral é ardil criminoso egoísta; a boa vontade sem sabedoria prática é ineficaz e pode produzir desastres na pólis."
    ))

    questoes_brutas.append((
        51, "EM13CHS501", "dificil",
        "No Helenismo, como a tese epicurista de que 'Os deuses existem, mas vivem nos espaços intermundanos sem interferir na história humana nem castigar os mortais' influenciou a autonomia moral dos indivíduos?",
        "Obrigando os agricultores a dedicarem metade de seus rebanhos de ovelhas a sacrifícios religiosos no início da primavera.",
        "Transferindo a responsabilidade da felicidade e da conduta ética inteiramente para a razão e escolhas dos próprios seres humanos, extirpando a culpa religiosa e a dependência servil de oráculos mágicos.",
        "Proibindo a construção de templos de pedra em cidades que não possuíssem portos marítimos naturais.",
        "Determinando que as festividades públicas celebrassem exclusivamente as estações do ano e o movimento das marés.",
        "Exigindo que os generais militares consultassem adivinhos antes de atravessarem rios caudalosos no inverno.",
        "B",
        "**Etapa 1:** Analisar a teologia racionalista e desconstrutiva de Epicuro: os deuses são modelos de beatitude ataráxica, não tiranos vingativos.\n**Etapa 2:** Concluir com a emancipação da razão moral: ao afastar a chantagem do castigo divino, Epicuro funda a ética na lucidez da consciência humana e na busca do bem comum terreno."
    ))

    questoes_brutas.append((
        52, "EM13CHS502", "dificil",
        "Em suas Memórias Póstumas de Brás Cubas, o escritor brasileiro Machado de Assis ironiza correntes filosóficas através da filosofia do Humanitismo formulada por Quincas Borba. De que maneira a sátira machadiana dialoga criticamente com o determinismo cósmico estóico e a teleologia dos fins?",
        "Afirmando que a literatura brasileira deve adotar exclusivamente o modelo métrico de poemas épicos medievais.",
        "Parodiando a ideia de harmonia providencial do destino através do humor cáustico de que 'a dor e o sofrimento alheio são meras etapas necessárias para o triunfo do vencedor', denunciando o cinismo das elites sociais do século XIX.",
        "Determinando que os romances literários devessem ser impressos em papel fabricado com celulose de palmeiras nativas.",
        "Exigindo que os personagens da ficção pertencessem unicamente a famílias de navegadores do litoral fluminense.",
        "Demonstrando que os filósofos da corte imperial brasileira desconheciam as obras escritas em línguas clássicas da Europa.",
        "B",
        "**Etapa 1:** Analisar a paródia do Humanitismo de Quincas Borba ('Ao vencedor, as batatas!') como distorção utilitária e darwinista social da teleologia e do destino.\n**Etapa 2:** Evidenciar a genialidade crítica de Machado de Assis: expõe como doutrinas filosóficas sublimes eram deformadas pelas classes senhoriais brasileiras para legitimar a opressão e a indiferença perante a miséria."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Considere o encontro histórico entre Diógenes de Sínope e Alexandre Magno. Quando o conquistador do mundo declara: 'Pede-me o que quiseres e eu to darei', e Diógenes responde: 'Afasta-te do meu sol', qual princípio de poder e liberdade se choca nessa resposta?",
        "A disputa por jazidas de minério de prata que estavam localizadas nas montanhas ao norte da Macedônia.",
        "O confronto entre o poder imperial exterior (baseado na riqueza, armas e submissão material) e o poder da soberania interior (baseado na autossuficiência moral, que nada deseja e por isso não pode ser comprado nem dobrado por nenhum tirano).",
        "A divergência sobre quais técnicas de plantio de cevada deveriam ser aplicadas nas planícies agrícolas de Atenas.",
        "A discussão sobre a rota marítima mais rápida para transportar tropas armadas até o delta do rio Nilo.",
        "O desacordo entre os dois sobre o modelo de sandálias de couro que os soldados deveriam calçar em marchas bélicas.",
        "B",
        "**Etapa 1:** Contrastar as duas figuras arquetípicas: o homem que conquistou o mundo exterior (Alexandre) versus o homem que conquistou a si mesmo (Diógenes).\n**Etapa 2:** Concluir com a lição magistral do cinismo: o verdadeiro senhor é aquele que nada teme e nada cobiça; perante o homem autossuficiente e livre, o maior imperador do planeta é apenas um obstáculo que tampa a luz do sol."
    ))

    questoes_brutas.append((
        54, "EM13CHS502", "dificil",
        "Na psicologia contemporânea, a Terapia Cognitivo-Comportamental (TCC) de Aaron Beck e Albert Ellis reconhece sua filiação direta à filosofia estoica de Epicteto. Como a máxima de Epicteto ('não são as coisas que perturbam, mas os juízos sobre elas') fundamenta a reestruturação cognitiva de pacientes com transtornos de ansiedade?",
        "Substituindo as consultas médicas por caminhadas matinais em praias litorâneas desacompanhadas de familiares.",
        "Ensinando o paciente a identificar, questionar e flexibilizar as distorções cognitivas e crenças catastróficas automáticas que ele formula sobre os eventos da vida, resgatando a capacidade da razão de reagir com serenidade e equilíbrio perante as adversidades reais.",
        "Exigindo que os pacientes decorem em silêncio nomes de imperadores que governaram Roma durante a Antiguidade.",
        "Proibindo o uso de medicamentos químicos e determinando o consumo exclusivo de chás feitos com folhas de louro.",
        "Obrigando as pessoas que sofrem de estresse a doarem todos os seus pertences móveis para instituições de caridade.",
        "B",
        "**Etapa 1:** Compreender a transposição da distinção estóica do controle para o campo clínico da psicoterapia moderna.\n**Etapa 2:** Evidenciar o mecanismo da reestruturação cognitiva: a angústia não brota da demissão ou da crítica em si, mas da interpretação absolutista ('isso é o fim'); ao reformular o juízo racional, restaura-se a resiliência emocional."
    ))

    questoes_brutas.append((
        55, "EM13CHS501", "dificil",
        "Em sua obra Ética a Nicômaco, Aristóteles dedica os Livros VIII e IX inteiramente ao estudo da Amizade (Philia), afirmando que 'sem amigos ninguém escolheria viver, mesmo que possuísse todos os outros bens'. Por que a Amizade Virtuosa (baseada no Bem) é considerada por Aristóteles superior à amizade por utilidade ou por prazer passageiro?",
        "Porque amigos virtuosos são obrigados por lei a emprestar moedas de ouro sem cobrança de juros mercantis.",
        "Porque a amizade por utilidade ou prazer dura apenas enquanto subsistir o ganho ou o deleite momentâneo, enquanto a amizade baseada na virtude é duradoura e desinteressada: nela, os amigos amam o caráter nobre um do outro e desejam o Bem recíproco por si mesmo.",
        "Porque os amigos de nobres atenienses possuíam o privilégio de viajar em carruagens oficiais do governo da cidade.",
        "Porque a amizade perfeita exige que os indivíduos assinem contratos comerciais de sociedade agrícola perante juízes civis.",
        "Porque a convivência entre pessoas virtuosas dispensa o uso da fala racional e comunica-se apenas por sinais manuais.",
        "B",
        "**Etapa 1:** Diferenciar os três tipos aristotélicos de amizade: acidental por utilidade, acidental por prazer e amizade perfeita por excelência do caráter.\n**Etapa 2:** Concluir que a amizade autêntica é uma virtude indispensável à eudaimonia: ela espelha o crescimento moral compartilhado, onde o amigo é um 'outro si-mesmo' amado pelo que é em sua dignidade."
    ))

    questoes_brutas.append((
        56, "EM13CHS502", "dificil",
        "No terceiro volume de sua História da Sexualidade (O Cuidado de Si), o filósofo Michel Foucault analisa os exercícios morais dos estóicos greco-romanos. De que maneira Foucault reabilita o estoicismo como uma 'Estética da Existência' contemporânea?",
        "Defendendo que os cidadãos modernos devem usar togas de lã e participar de rituais com tochas de azeite.",
        "Demonstrando que o estoicismo não era uma moral de repressão e obediência cega a códigos universais, mas uma arte de autogoverno e estilização da própria liberdade, na qual o sujeito cuida de si para não ser governado despoticamente pelo poder ou pelas paixões cegas.",
        "Afirmando que as teorias de Foucault devem ser aplicadas apenas no treinamento físico de atletas olímpicos.",
        "Exigindo que os hospitais psiquiátricos passem a funcionar sob o comando de generais de infantaria militar.",
        "Provando que as academias de ginástica das cidades industriais consomem recursos financeiros excessivos do tesouro.",
        "B",
        "**Etapa 1:** Interpretar o conceito foucaultiano de 'Tecnologias do Eu' (*Technologies of the Self*) e 'Cuidado de Si' (*Epimeleia Heautou*).\n**Etapa 2:** Concluir com a emancipação subjetiva: Foucault mostra que os estóicos inventaram práticas de resistência ética cotidiana contra a alienação, transformando a própria vida em uma obra de arte moral de autodomínio lúcido."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Analise a seguinte reflexão de Pierre Hadot em O que é a Filosofia Antiga?: 'O discurso filosófico não tem seu fim em si mesmo; ele é apenas o meio de preparar, justificar e orientar a vida filosófica autêntica.' Como essa tese desmonta a caricatura da filosofia helenística como mera 'fuga alienada da realidade política'?",
        "Provando que os filósofos helenísticos eram todos analfabetos que se recusavam a escrever cartas a amigos.",
        "Evidenciando que a busca da ataraxia e da apatheia não era uma fuga covarde do mundo, mas uma pedagogia engajada de resistência e sanidade espiritual diante da barbárie tirânica, ensinando o indivíduo a manter a dignidade e a integridade ética em qualquer circunstância histórica adversa.",
        "Demonstrando que os pensadores do Pórtico e do Jardim deveriam ter fundado empresas de exportação de azeite e trigo.",
        "Afirmando que a filosofia antiga perdeu sua utilidade prática após a invenção da imprensa de tipos móveis no século XV.",
        "Defendendo que os estudantes de ensino médio devem decorar listas de datas históricas sem refletir sobre o seu significado.",
        "B",
        "**Etapa 1:** Desmistificar o preconceito historiográfico que rotula o Helenismo como época de decadência e evasão passiva.\n**Etapa 2:** Concluir com Pierre Hadot: as escolas helenísticas foram laboratórios heroicos de autonomia existencial; quando o espaço democrático da pólis ruiu, a filosofia preservou a liberdade humana no território inalienável da consciência lúcida."
    ))

    questoes_brutas.append((
        58, "EM13CHS504", "dificil",
        "No debate sobre o Hiperconsumismo contemporâneo e o Movimento Minimalista, como a distinção epicurista entre 'Desejos Naturais e Necessários' versus 'Desejos Vãos e Não Naturais' oferece uma crítica ecológica e psicológica ao capitalismo de marketing?",
        "Determinando que os governos confisquem todos os aparelhos eletrônicos de comunicação das residências urbanas.",
        "Evidenciando que a publicidade industrial fabrica artificialmente desejos insaciáveis de status, ostentação e novidades descartáveis, condenando os indivíduos à ansiedade do endividamento e à sobrecarga do trabalho exaustivo, ao mesmo tempo em que devora os recursos naturais finitos do planeta Terra.",
        "Obrigando os trabalhadores das indústrias químicas a utilizarem máscaras de proteção confeccionadas com tecidos de linho.",
        "Proibindo o uso de computadores eletrônicos no cálculo de estoques de produtos alimentícios em supermercados.",
        "Exigindo que as famílias que moram no campo plantem apenas sementes de girassol em suas hortas caseiras.",
        "B",
        "**Etapa 1:** Aplicar a crítica epicurista da insaciabilidade dos desejos vãos ao fetiche do consumo moderno.\n**Etapa 2:** Concluir com a atualidade de Epicuro: a verdadeira liberdade exige desarmar as falsas necessidades criadas pelo mercado; simplificar a vida material liberta o tempo humano para o convívio, a saúde e a preservação ecológica sustentável."
    ))

    questoes_brutas.append((
        59, "EM13CHS104", "dificil",
        "Em que medida a concepção estóica do Cosmopolitismo (Cidadania Universal do Logos) antecipou e inspirou as bases filosóficas das modernas declarações de Direitos Humanos universais?",
        "Ao defender que todos os governos democráticos deveriam adotar o mesmo brasão de armas com figuras de águias douradas.",
        "Ao afirmar a dignidade comum como seres humanos e a fraternidade racional universal de todos os indivíduos, independentemente de nascimento, etnia, gênero ou condição social (como escravo ou imperador), superando a divisão grega clássica entre 'cidadãos civilizados' e 'bárbaros inferiores'.",
        "Ao propor que as leis civis de todos os países do mundo deveriam ser redigidas em versos poéticos rimados.",
        "Ao determinar que os tribunais internacionais deveriam cobrar taxas em barras de ouro de marinheiros que cruzam oceanos.",
        "Ao proibir a navegação de barcos que não tivessem suas velas pintadas em cores claras pelas frotas costeiras.",
        "B",
        "**Etapa 1:** Rastrear a genealogia do universalismo moral na Stoa (Epicteto, escravo libertado, e Marco Aurélio, imperador soberano, compartilhavam a mesma dignidade humana pelo Logos).\n**Etapa 2:** Concluir com a influência sobre o direito moderno: o cosmopolitismo estóico demoliu o etnocentrismo da Antiguidade, lançando as sementes da igualdade inata de todos os membros da família humana que culminou na DUDH de 1948."
    ))

    questoes_brutas.append((
        60, "EM13CHS501", "dificil",
        "Analise a seguinte passagem de Aristóteles na Ética a Nicômaco: 'Aquele que não pode viver em sociedade, ou que não tem necessidade de nada por bastar-se a si mesmo, não é parte de uma comunidade: é uma fera selvagem ou um deus.' De que maneira essa formulação sintetiza a dimensão intrinsecamente relacional e comunitária da ética e da felicidade humana?",
        "Afirmando que os eremitas que moram em florestas isoladas são superiores aos reis que governam grandes nações.",
        "Demonstrando que a excelência humana não pode ser realizada no solipsismo egoísta e desvinculado; a prática da justiça, da generosidade, da amizade e da virtude só faz sentido e se aperfeiçoa no tecido vivo da convivência partilhada entre cidadãos livres em uma comunidade.",
        "Defendendo que as cidades industriais devem ser cercadas por muros de tijolos para impedir a saída de seus operários.",
        "Determinando que os cidadãos que cometerem erros de julgamento moral sejam expulsos para ilhas desabitadas no oceano.",
        "Provando que as leis da pólis foram promulgadas para beneficiar exclusivamente os artesãos que fabricam armaduras de bronze.",
        "B",
        "**Etapa 1:** Interpretar a clássica sentença aristotélica sobre a sociabilidade inerente da condição humana.\n**Etapa 2:** Concluir com o telos da ética das virtudes: o homem é um ser comunitário; a virtude moral e a felicidade realizam-se na teia das relações humanas; o isolamento total é desumanização bestial ou perfeição divina inalcançável para os mortais."
    ))

    return questoes_brutas


def balancear_gabarito(questoes_brutas):
    distribuicao_alvo = ['A', 'B', 'C', 'D', 'E'] * 12
    questoes_balanceadas = []

    for i, q in enumerate(questoes_brutas):
        num, hab, dif, enunciado, a, b, c, d, e, gab_original, feedback = q
        alvo = distribuicao_alvo[i]

        opcoes = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}
        texto_correto = opcoes[gab_original]
        textos_incorretos = [opcoes[k] for k in ['A', 'B', 'C', 'D', 'E'] if k != gab_original]

        novas_opcoes = {}
        novas_opcoes[alvo] = texto_correto

        letras_restantes = [k for k in ['A', 'B', 'C', 'D', 'E'] if k != alvo]
        for k, texto_inc in zip(letras_restantes, textos_incorretos):
            novas_opcoes[k] = texto_inc

        questoes_balanceadas.append((
            num, hab, dif, enunciado,
            novas_opcoes['A'], novas_opcoes['B'], novas_opcoes['C'], novas_opcoes['D'], novas_opcoes['E'],
            alvo, feedback
        ))

    return questoes_balanceadas


def auditar_termos_proibidos(questoes):
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

    erros = []
    for q in questoes:
        num = q[0]
        conteudo = f"{q[3]} {q[4]} {q[5]} {q[6]} {q[7]} {q[8]} {q[10]}".lower()
        for pattern in padroes_proibidos:
            match = re.search(pattern, conteudo, re.IGNORECASE)
            if match:
                erros.append(f"Questão {num}: termo proibido '{match.group(0)}' encontrado!")

    if erros:
        print("\n[ERRO NA AUDITORIA DE TERMOS PROIBIDOS]:")
        for e in erros:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("[AUDITORIA INTERNA APROVADA] Nenhuma palavra da blacklist pedagógica encontrada!")


def gerar_markdown(questoes):
    header = """---
série: "Ensino Médio"
disciplina: "Filosofia"
eixo: "eixo-2-etica"
capitulo: "cap-10-etica-virtudes-aristoteles-helenismo"
objeto_de_conhecimento: "A Ética Teleológica Aristotélica (Ética a Nicômaco): A Felicidade (Eudaimonia) como Fim Supremo; A Teoria do Justo Meio (Mesótes); A Prudência (Phrónesis); As Escolas Helenísticas: Epicurismo (Ataraxia e Hedonismo Racional), Estoicismo (Apatheia e Autodomínio) e Cinismo de Diógenes."
ebook_fonte: "em-fil-c10-etica-virtudes-aristoteles-helenismo.md"
habilidades: "EM13CHS101, EM13CHS104, EM13CHS501, EM13CHS502, H1, H2, H16, H17"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: A Ética das Virtudes: Aristóteles e as Escolas Helenísticas

"""

    corpo = header
    slug_cap = "cap-10-etica-virtudes-aristoteles-helenismo"

    # Nível Básico
    corpo += "## Nível Básico\n\n"
    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: {slug_cap} -->\n"
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
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: {slug_cap} -->\n"
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
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: {slug_cap} -->\n"
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

- ARISTÓTELES. *Ética a Nicômaco*. Tradução, introdução e notas de Luciano de Crescenzo e Mário da Gama Kury. 4. ed. Brasília: Editora UnB, 2002.
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.
- CHAUÍ, Marilena. *Introdução à História da Filosofia: Dos Pré-Socráticos a Aristóteles*. 2. ed. São Paulo: Companhia das Letras, 2002. v. 1.
- EPICTETO. *Manual de Epicteto*. Tradução de Aldo Dinucci e Alfredo Julien. São Cristóvão: EdiUFS, 2006.
- EPICURO. *Carta sobre a Felicidade (a Meneceu)*. Tradução de Álvaro Lorencini e Enzo Del Carratore. São Paulo: Editora Unesp, 2002.
- HADOT, Pierre. *O que é a Filosofia Antiga?* Tradução de Dionísio da Silva Mourão. São Paulo: Loyola, 2002.
- JAEGER, Werner. *Aristóteles: Bases para la historia de su desarrollo intelectual*. Tradução de José Gaos. Madri: Fondo de Cultura Económica, 2001.
- REALE, Giovanni. *História da Filosofia Antiga: O Helenismo*. Tradução de Henrique C. de Lima Vaz e Marcelo Perine. 3. ed. São Paulo: Loyola, 2008. v. 3.
- ROSS, David. *Aristóteles*. Tradução de Luís Filipe Bragança S. S. Teixeira. Lisboa: Publicações Dom Quixote, 1995.
- SÊNECA, Lúcio Aneu. *Sobre a Brevidade da Vida e Sobre a Tranquilidade da Alma*. Tradução de William Li. São Paulo: Nova Alexandria, 2006.
"""

    return corpo


def main():
    brutas = construir_exercicios()
    print(f"Total de questões brutas: {len(brutas)}")
    if len(brutas) != 60:
        print(f"[ERRO] Número de questões incorreto: {len(brutas)} (esperado: 60)")
        sys.exit(1)

    auditar_termos_proibidos(brutas)

    balanceadas = balancear_gabarito(brutas)

    contagem_gab = Counter([q[9] for q in balanceadas])
    print(f"Contagem por letra no gabarito: {contagem_gab}")

    # Verificar streak
    for i in range(len(balanceadas) - 1):
        if balanceadas[i][9] == balanceadas[i+1][9]:
            print(f"[ERRO] Streak consecutivo detectado entre Q{balanceadas[i][0]} e Q{balanceadas[i+1][0]}: letra {balanceadas[i][9]}")
            sys.exit(1)

    md_content = gerar_markdown(balanceadas)

    temp_path = "temp_draft.md"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Rascunho salvo em {temp_path} ({len(md_content.encode('utf-8'))} bytes)")

    dest_rel = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-10-etica-virtudes-aristoteles-helenismo/ebooks/em-fil-c10-etica-virtudes-aristoteles-helenismo-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_path, dest_rel]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 10 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
