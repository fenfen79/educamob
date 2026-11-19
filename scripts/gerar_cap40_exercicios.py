# -*- coding: utf-8 -*-
"""
Script de Geração e Homologação das 60 Questões de Filosofia EM - Capítulo 40
Objeto: Epistemologias Ameríndias e Filosofias da Terra
E-book Fonte: em-fil-c40-epistemologias-amerindias-filosofia-terra-krenak.md
Padrão: 60 questões (20 B / 20 I / 20 D) | 12 A, 12 B, 12 C, 12 D, 12 E | Closed-World
GRANDE FINAL: FECHAMENTO DE 100% DA COLEÇÃO DE FILOSOFIA DO ENSINO MÉDIO!
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
        "Qual legislação federal brasileira promulgada em 2008 tornou obrigatório o estudo da História e Culturas Indígenas na Educação Básica?",
        [
            ("A Lei Federal nº 11.645/2008, ampliando a Lei 10.639/03 e promovendo a descolonização dos saberes escolares no país.", True),
            ("A Lei de Terras de 1850, que determinou a venda obrigatória de terras públicas em leilões comerciais agrários.", False),
            ("O Estatuto do Índio de 1973, que tratava os povos originários como relativamente incapazes sujeitos à tutela do Estado.", False),
            ("A Lei Áurea de 1888, que aboliu a escravidão formal sem criar mecanismos de assistência ou posse fundiária aos libertos.", False),
            ("O Código Civil de 1916, que regulamentou a posse da terra segundo os interesses dos cafeicultores da região sudeste.", False)
        ],
        "A Lei nº 11.645/2008 consagrou a inclusão obrigatória das matrizes culturais e filosóficas indígenas no currículo escolar brasileiro."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Qual pressuposto metafísico cartesiano consagrado no século XVII fundamentou a separação ocidental entre o homem e a natureza?",
        [
            ("A divisão entre a substância pensante humana (res cogitans) e a natureza material inerte destituída de alma (res extensa).", True),
            ("A teoria hilemórfica aristotélica que une matéria indeterminada e forma substancial em todos os seres vivos do cosmos.", False),
            ("A cosmologia pré-socrática que identificava na água primordial a origem e o princípio animador de todas as criaturas da terra.", False),
            ("O materialismo histórico dialético que compreende a realidade como o desdobramento das forças produtivas econômicas materiais.", False),
            ("A teologia escolástica medieval que afirmava que todas as plantas e animais possuem inteligência angelical reflexiva.", False)
        ],
        "Descartes cindiu a realidade entre o sujeito pensante e a matéria inanimada, rebaixando a natureza a recurso passivo para exploração humana."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "Sob qual justificativa ideológica os conquistadores europeus historicamente desqualificaram os povos indígenas das Américas?",
        [
            ("Alegando que viviam em selvageria sem escrita alfabética ou razão teórica, rotulando seus saberes de superstições ingênuas.", True),
            ("Reconhecendo que as nações ameríndias possuíam universidades com tecnologias de metalurgia superiores às da Europa ocidental.", False),
            ("Declarando que os pajés indígenas eram profetas divinos cujos ensinamentos deveriam orientar a coroação de reis franceses.", False),
            ("Admitindo que as leis consuetudinárias das florestas eram mais justas e equitativas do que os códigos jurídicos imperiais romanos.", False),
            ("Afirmando que a medicina tradicional xamânica havia superado todas as epidemias contagiosas da história humana moderna.", False)
        ],
        "Os colonizadores desqualificaram a humanidade indígena para legitimar o roubo de suas terras demarcadas e o massacre de suas populações."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "De que maneira a antropologia contemporânea descreve a matriz metafísica ocidental moderna denominada Multiculturalismo?",
        [
            ("Afirma a existência de uma única Natureza física objetiva contrastada com muitas Culturas humanas subjetivas e simbólicas.", True),
            ("Sustenta que existem incontáveis naturezas físicas paralelas habitadas por uma única cultura monolítica de robôs mecânicos.", False),
            ("Defende que cada povo humano constrói seus próprios planetas materiais no vácuo espacial através de rituais com fogueiras.", False),
            ("Proclama que a física e a química variam de acordo com as preferências poéticas individuais de cada cidadão alfabetizado.", False),
            ("Declara que os animais domésticos possuem parlamentos e tribunais jurídicos idênticos aos das repúblicas constitucionais.", False)
        ],
        "O multiculturalismo ocidental pressupõe a unidade da natureza material universal e a multiplicidade das culturas humanas particulares."
    ))

    questoes_brutas.append((
        5, "EM13CHS301", "basico",
        "Em contraste com a visão naturalista ocidental, em que consiste a premissa cosmológica originária das epistemologias ameríndias?",
        [
            ("A condição primordial comum a todos os entes do cosmos é a humanidade: no tempo do mito originário, todos os seres eram humanos.", True),
            ("A humanidade é uma invenção recente criada por máquinas computadorizadas que programaram a biosfera há poucas décadas.", False),
            ("Os animais e as plantas surgiram antes da terra e foram trazidos de outras galáxias por cometas celestes incandescentes.", False),
            ("A matéria física é totalmente destituída de forças vitais e foi criada exclusivamente para ser incinerada em fornos industriais.", False),
            ("Apenas os homens que usam vestimentas de algodão branco possuem alma imortal e faculdade de comunicação verbal articulada.", False)
        ],
        "Para as cosmologias indígenas, a humanidade é o fundo cósmico universal compartilhado: animais e plantas foram humanos antes de mudar de corpo."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Qual notável antropólogo e filósofo brasileiro formulou a sofisticada teoria do Perspectivismo Ameríndio e do Multinaturismo?",
        [
            ("Eduardo Viveiros de Castro, autor da obra clássica A Inconstância da Alma Selvagem e do tratado Metafísicas Canibais.", True),
            ("Gilberto Freyre, sociólogo pernambucano autor de Casa-Grande e Senzala sobre a formação patriarcal da sociedade brasileira.", False),
            ("Sérgio Buarque de Holanda, historiador paulista que formulou a tese do homem cordial na obra clássica Raízes do Brasil.", False),
            ("Caio Prado Júnior, economista e historiador autor de Formação do Brasil Contemporâneo sobre a economia colonial do país.", False),
            ("Darcy Ribeiro, antropólogo criador dos Centros Integrados de Educação Pública e autor do ensaio histórico O Povo Brasileiro.", False)
        ],
        "Eduardo Viveiros de Castro revolucionou a antropologia e a filosofia ao teorizar o Perspectivismo Ameríndio dos povos amazônicos."
    ))

    questoes_brutas.append((
        7, "EM13CHS301", "basico",
        "Em contraposição ao multiculturalismo ocidental, o que define a tese do Multinaturismo no pensamento ameríndio?",
        [
            ("A afirmação de uma única cultura cósmica compartilhada por todos os entes e de muitas naturezas determinadas pelas roupagens corpóreas.", True),
            ("A crença de que cada indivíduo humano possui sete corpos materiais idênticos que transitam simultaneamente por cidades diferentes.", False),
            ("A ideia de que as leis da gravidade planetária deixam de funcionar nas áreas florestais habitadas por comunidades extrativistas.", False),
            ("A proposta de que os animais selvagens devem pagar tributos monetários em ouro para obter licença de caça em parques nacionais.", False),
            ("A tese de que a natureza física foi extinta por completo no século dezenove e substituída por maquetes de gesso decorativas.", False)
        ],
        "O multinaturismo afirma a unidade do espírito cultural (todos se veem como humanos) e a multiplicidade das naturezas corpóreas vivas."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "No horizonte perspectivista formulado por Viveiros de Castro, como a onça-pintada apreende a si mesma e à sua realidade na floresta?",
        [
            ("A onça vê a si mesma como pessoa humana, vê o sangue de sua presa abatida como cerveja fermentada de mandioca e sua cova como aldeia.", True),
            ("A onça vê a si mesma como uma máquina autômata programada por inteligências computacionais para caçar veados de madrugada.", False),
            ("A onça reconhece que os caçadores humanos são deuses celestes perfeitos que devem ser reverenciados com preces de joelhos.", False),
            ("A onça tem plena consciência de sua condição animal irracional e busca aprender o idioma português em cartilhas escolares.", False),
            ("A onça considera as árvores da selva como edifícios de apartamentos de alvenaria construídos por construtoras civis urbanas.", False)
        ],
        "Cada espécie apreende a si mesma sob o ponto de vista da humanidade; sua roupagem física é que define a sua perspectiva particular no mundo."
    ))

    questoes_brutas.append((
        9, "EM13CHS306", "basico",
        "O que o conceito de 'diplomacia cósmica' exige de um caçador indígena ao adentrar a floresta amazônica?",
        [
            ("Negociações rituais e respeito aos limites da reprodução das espécies, tratando os animais como sujeitos protegidos por guardiões.", True),
            ("O extermínio predatório e desmedido de todas as fêmeas grávidas para comercializar peles exóticas em feiras internacionais de luxo.", False),
            ("A derrubada completa das árvores centenárias com tratores de esteira para transformar a selva em pastagens para gado bovino.", False),
            ("A recusa em ingerir qualquer tipo de alimento sólido durante viagens de caça para manter a pureza das armas de arremesso.", False),
            ("O dever de assinar contratos de arrendamento de terras com mineradoras multinacionais antes de coletar castanhas na mata.", False)
        ],
        "Caçar na cosmovisão originária é um ato diplomático entre sujeitos: exige reciprocidade ética e respeito espiritual para não romper a harmonia."
    ))

    questoes_brutas.append((
        10, "EM13CHS101", "basico",
        "Qual líder histórico do povo Krenak, escritor ambientalista e membro da Academia Brasileira de Letras, formulou as Filosofias da Terra?",
        [
            ("Ailton Krenak, autor de ensaios aclamados como Ideias para Adiar o Fim do Mundo, A Vida Não É Útil e Futuro Ancestral.", True),
            ("Mário Juruna, líder do povo Xavante que utilizava um gravador portátil para registrar compromissos de autoridades estatais.", False),
            ("Chico Mendes, seringueiro e líder sindical acreano assassinado em virtude de sua luta pela criação de reservas extrativistas.", False),
            ("Raoni Metuktire, histórico cacique do povo Kayapó conhecido internacionalmente pela defesa do Parque Nacional do Xingu.", False),
            ("Marçal de Souza Tupã-i, pioneiro líder do povo Guarani Kaiowá que denunciou o massacre de lideranças indígenas na ONU.", False)
        ],
        "Ailton Krenak alcançou renome internacional por sua prosa poética e filosófica que desafia o utilitarismo predatório da sociedade moderna."
    ))

    questoes_brutas.append((
        11, "EM13CHS601", "basico",
        "Em Ideias para Adiar o Fim do Mundo, qual é a crítica central de Ailton Krenak à ficção dominante da 'Humanidade'?",
        [
            ("Denuncia que o Ocidente criou um clube seleto e apartado da biosfera, convertendo o restante da Terra viva em mero depósito de consumo.", True),
            ("Afirma que os seres humanos devem ser substituídos imediatamente por espécies de macacos arborícolas na governança das cidades.", False),
            ("Sustenta que as cidades metropolitanas foram construídas por civilizações extraterrestres que abandonaram o solo terrestre há séculos.", False),
            ("Declara que as pessoas que vivem em centros urbanos não pertencem ao reino biológico e não necessitam de água potável para viver.", False),
            ("Preconiza que as florestas tropicais devem ser desmatadas para a construção de estádios de futebol climatizados no norte do país.", False)
        ],
        "Krenak critica a ilusão de um ser humano desconectado da teia da vida: descolar-se da Terra transforma a civilização em uma máquina devoradora."
    ))

    questoes_brutas.append((
        12, "EM13CHS501", "basico",
        "Por que Ailton Krenak afirma com lucidez histórica que o 'fim do mundo' já aconteceu para os povos originários das Américas?",
        [
            ("Porque o mundo originário acabou em 1500 com a invasão europeia, e desde então os indígenas resistem e reinventam a vida a cada dia.", True),
            ("Porque uma tempestade solar aniquilou a camada de ozônio planetária durante os conflitos armados da Primeira Guerra Mundial.", False),
            ("Porque as reservas de água doce dos rios amazônicos evaporaram por completo durante secas extremas registradas na Idade Média.", False),
            ("Porque as nações indígenas assinaram tratados de rendição definitiva e abriram mão de seus costumes ancestrais nos anos sessenta.", False),
            ("Porque os oceanos cobriram a totalidade das terras continentais americanas no período da grande glaciação quaternária arcaica.", False)
        ],
        "Os povos indígenas acumulam mais de cinco séculos de resistência ao apocalipse colonial; suas tecnologias de sobrevivência são lições para o presente."
    ))

    questoes_brutas.append((
        13, "EM13CHS306", "basico",
        "Como o povo Krenak vivenciou a tragédia socioambiental do rompimento da barragem de rejeitos de mineração em Mariana (2015)?",
        [
            ("Não como mero dano a um recurso hídrico, mas como o assassinato de um parente vivo sagrado e ancestral: o Rio Doce (Watu).", True),
            ("Como um acontecimento festivo que permitiu a modernização imediata de todas as residências da terra indígena pelo agronegócio.", False),
            ("Como uma oportunidade financeira rentável para enriquecer as lideranças tribais por meio de indenizações depositadas em bancos suíços.", False),
            ("Como uma lenda mítica narrada por navegadores portugueses que não guardava qualquer relação com as águas da bacia do rio Doce.", False),
            ("Como um fenômeno puramente meteorológico provocado pelo excesso de chuvas de verão nas serras do litoral atlântico brasileiro.", False)
        ],
        "Para o povo Krenak, o Watu é um avô personificado; a lama tóxica de minério destruiu um ente da família cósmica com quem partilhavam a vida."
    ))

    questoes_brutas.append((
        14, "EM13CHS101", "basico",
        "Em seu livro A Vida Não É Útil (2020), qual pressuposto central da sociedade capitalista contemporânea Ailton Krenak rejeita?",
        [
            ("O utilitarismo mercantil que reduz o valor da existência humana à produtividade compulsória, ao trabalho e à geração de lucros.", True),
            ("O direito dos estudantes de frequentar escolas públicas de ensino fundamental e médio em suas comunidades de origem.", False),
            ("O hábito saudável de beber água mineral fresca e consumir frutas maduras colhidas em árvores de quintais residenciais.", False),
            ("A prática ancestral de contar histórias ao redor de fogueiras para transmitir ensinamentos às gerações mais jovens.", False),
            ("A realização de mutirões comunitários para o conserto de pontes de madeira e recuperação de estradas de terra no campo.", False)
        ],
        "A vida, ensina Krenak, não é útil para produzir mercadorias: ela é uma dádiva pura, celebração estética, dança e fruição da presença cósmica."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "Qual sabedoria poética e política Ailton Krenak propõe aos seres humanos para 'adiar o fim do mundo' diante do colapso ecológico?",
        [
            ("Cantar, dançar, narrar histórias e nutrir a diversidade de vidas para empurrar o horizonte e suspender o céu sobre nossas cabeças.", True),
            ("Construir usinas nucleares subterrâneas e armazenar armamentos atômicos em cavernas de granito para repelir cometas siderais.", False),
            ("Pavimentar todas as áreas florestais do continente com cimento cinza para facilitar o tráfego de caminhões e carros elétricos.", False),
            ("Substituir o consumo de água doce pela ingestão de suplementos vitamínicos químicos fabricados em laboratórios farmacêuticos.", False),
            ("Impedir que as crianças brinquem ao ar livre e confiná-las em celas herméticas com telas de computadores ligadas dia e noite.", False)
        ],
        "Adiar o fim do mundo é cultivar a pluralidade e a alegria: resistir à máquina de morte contemporânea inventando mais um dia de vida e afeto."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Qual obra monumental de xamanismo, filosofia cósmica e ecologia política foi narrada por Davi Kopenawa com o antropólogo Bruce Albert?",
        [
            ("A Queda do Céu: palavras de um xamã yanomami, consagrada internacionalmente como clássico do pensamento do século XXI.", True),
            ("Os Sertões, epopeia jornalística e sociológica sobre o massacre messiânico de Canudos no sertão baiano no final do século XIX.", False),
            ("Tristes Trópicos, clássico da etnografia memorialística francesa sobre as expedições científicas realizadas no Brasil central.", False),
            ("Macunaíma, romance modernista de rapsódia que investiga a formação da identidade nacional sem nenhum caráter fixo.", False),
            ("Grande Sertão: Veredas, monumento da literatura brasileira que recria a fala do sertanejo e indaga sobre a existência do mal.", False)
        ],
        "A Queda do Céu é um testemunho cósmico singular e demolidor: Davi Kopenawa articula a ontologia xamânica contra a devastação predatória."
    ))

    questoes_brutas.append((
        17, "EM13CHS301", "basico",
        "Na ontologia cósmica do povo Yanomami narrada em A Queda do Céu, o que são os espíritos luminosos denominados Xapiri (xapiripë)?",
        [
            ("Espíritos benfazejos microscópicos e imortais que dançam convocados pelos xamãs para purificar a terra e sustentar as vigas do céu.", True),
            ("Monstros gigantescos e subterrâneos que devoram os rios e incendeiam as florestas durante as noites de tempestades tropicais.", False),
            ("Insetos voadores venenosos que picam os camponeses e transmitem febres malignas que destroem as lavouras de mandioca brava.", False),
            ("Moedas de ouro maciço que foram enterradas por piratas europeus em praias desertas da foz do rio Amazonas no século dezesseis.", False),
            ("Máquinas mecânicas automáticas de perfuração de rochas utilizadas por companhias multinacionais de mineração pesada.", False)
        ],
        "Os Xapiri são os auxiliares luminosos dos xamãs: seres primordiais de beleza e poder que combatem as fumaças de morte e mantêm o céu erguido."
    ))

    questoes_brutas.append((
        18, "EM13CHS501", "basico",
        "Como Davi Kopenawa caracteriza a civilização capitalista ocidental ao batizá-la de 'O Povo da Mercadoria'?",
        [
            ("Uma sociedade doente de ganância (motiro), que não sabe contemplar a natureza sem desejar arrancá-la do solo para gerar lucro e ouro.", True),
            ("Uma comunidade solidária de pescadores artesanais que divide fraternalmente as refeições diárias com viajantes desamparados.", False),
            ("Um povo iluminado espiritualmente que dedica a maior parte do dia à meditação contemplativa silenciosa e à escuta dos rios.", False),
            ("Uma aliança internacional de curandeiros botânicos que protege as espécies ameaçadas de extinção biológica em reservas de mata.", False),
            ("Um coletivo de artesãos tradicionais que confecciona cestos de palha e cerâmicas decorativas sem cobrança de remuneração em dinheiro.", False)
        ],
        "Kopenawa denuncia a patologia espiritual dos brancos: o vício da mercadoria que destrói as florestas e envenena os rios em troca de ouro morto."
    ))

    questoes_brutas.append((
        19, "EM13CHS306", "basico",
        "O que representa a 'fumaça da epidemia' (xawara) libertada pelo garimpo ilegal nas terras amazônicas segundo a sabedoria Yanomami?",
        [
            ("Vapores tóxicos de mercúrio e miasmas destrutivos liberados pelo rasgo da terra que envenenam a água, os peixes e a biosfera global.", True),
            ("Nuvens benfazejas de vapor de água marinha que trazem chuvas férteis e purificam as plantações de milho em vilas ribeirinhas.", False),
            ("Uma substância mágica e aromatizada utilizada por chefes tribais para curar dores de dente em crianças pequenas sem remédios.", False),
            ("Um gás combustível fóssil que pode ser engarrafado para substituir a gasolina nos motores de popa de pequenas canoas de pesca.", False),
            ("Uma névoa passageira gerada pela queima de incensos naturais em templos de oração de monges eremitas da serra da Mantiqueira.", False)
        ],
        "A xawara é a morte invisível: o mercúrio e os venenos do garimpo que exterminam crianças e animais e aceleram a destruição climática do planeta."
    ))

    questoes_brutas.append((
        20, "EM13CHS301", "basico",
        "Em A Queda do Céu, qual o conteúdo da profecia trágica e cósmica formulada por Davi Kopenawa?",
        [
            ("Se os brancos exterminarem os xamãs e destruírem a floresta, os Xapiri partirão, o firmamento apodrecerá e o céu desabará sobre todos.", True),
            ("A humanidade alcançará a imortalidade biológica definitiva quando construir fábricas de calçados de couro em aldeias amazônicas.", False),
            ("O planeta Terra dobrará de tamanho físico e absorverá a lua em sua órbita com o derretimento total das calotas de gelo dos polos.", False),
            ("Os garimpeiros ilegais se transformarão em pássaros de penas coloridas e abandonarão as dragas de mineração no fundo dos rios.", False),
            ("As cortes jurídicas internacionais perdoarão todas as dívidas financeiras de mineradoras que realizarem plantio de grama sintética.", False)
        ],
        "A queda do céu é a advertência definitiva: o colapso ecológico da Amazônia romperá o equilíbrio da biosfera e destruirá índios e brancos juntos."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS501", "intermediario",
        "No contraste ético entre a corporação mineradora e o povo Krenak em Mariana, qual divergência irreconciliável de valores se evidencia?",
        [
            ("A mineradora quantifica a destruição como custo financeiro compensável, enquanto o povo Krenak chora a perda de um ancestral sagrado vivo.", True),
            ("A corporação defende o reflorestamento total da bacia hidrográfica, enquanto os indígenas exigem a instalação de mais usinas siderúrgicas.", False),
            ("As comunidades ribeirinhas recusam o consumo de peixes frescos para priorizar a compra de conservas marinhas importadas de Portugal.", False),
            ("Os tribunais internacionais declararam que a lama tóxica de minério possui nutrientes fertilizantes que melhoram a água potável.", False),
            ("Os acionistas privados da empresa renunciaram a seus lucros em bolsa para se tornarem barqueiros voluntários no litoral capixaba.", False)
        ],
        "Para o capital, a tragédia é uma cifra contábil; para as filosofias da terra, trata-se de um ecocídio e do assassinato de um ente vivo do parentesco."
    ))

    questoes_brutas.append((
        22, "EM13CHS306", "intermediario",
        "No campo da saúde pública, de que modo as pesquisas toxicológicas da Fiocruz na Terra Yanomami confirmam cientificamente o diagnóstico xamânico da xawara?",
        [
            ("Comprovam contaminação generalizada por mercúrio nos rios e no sangue indígena, gerando sequelas neurológicas graves e mortes infantis.", True),
            ("Demonstram que a água das bacias hidrográficas amazônicas apresenta índices de pureza mineral superiores aos de fontes alpinas europeias.", False),
            ("Evidenciam que o contato com o mercúrio metálico fortalece a imunidade dos recém-nascidos contra enfermidades respiratórias sazonais.", False),
            ("Atestam que os peixes carnívoros dos rios amazônicos aprenderam a neutralizar quimicamente as moléculas de metais pesados em suas guelras.", False),
            ("Afirmam que a presença de pistas clandestinas de pouso de aviões acelerou o crescimento de orquídeas raras nas margens dos igarapés.", False)
        ],
        "A ciência toxicológica confirma a profecia de Kopenawa: a fumaça de morte da mineração contamina o sangue das crianças e destrói a vida."
    ))

    questoes_brutas.append((
        23, "EM13CHS601", "intermediario",
        "Ao julgar inconstitucional a tese do Marco Temporal em 2023, qual princípio histórico o Supremo Tribunal Federal brasileiro consagrou?",
        [
            ("O Direito Originário ou Indigenato, que estabelece que o direito territorial indígena é congênito e anterior à formação do próprio Estado.", True),
            ("A primazia dos títulos de propriedade imobiliária emitidos por cartórios privados sobre quaisquer laços ancestrais com a terra natal.", False),
            ("A obrigação de que todos os povos originários comprem suas terras demarcadas através de leilões promovidos pelo ministério da fazenda.", False),
            ("O dever de que as comunidades indígenas desocupem as áreas de preservação permanente para permitir a exploração de petróleo fóssil.", False),
            ("A transferência do controle administrativo de todas as aldeias do país para conselhos empresariais de cooperativas agropecuárias.", False)
        ],
        "O indigenato reconhece que a posse dos povos originários é raiz anterior à República; derrubar o marco temporal foi vitória da justiça histórica."
    ))

    questoes_brutas.append((
        24, "EM13CHS306", "intermediario",
        "Dados oficiais de satélite do Inpe e do MapBiomas atestam qual papel ecológico fundamental exercido pelas Terras Indígenas demarcadas?",
        [
            ("Constituem os territórios mais preservados e com as menores taxas históricas de desmatamento e degradação florestal em todo o Brasil.", True),
            ("Apresentam os maiores índices de queimadas antrópicas e de destruição de nascentes de rios entre todos os biomas nacionais protegidos.", False),
            ("São as principais responsáveis pela emissão de gases de efeito estufa em virtude da realização de queimas cerimoniais cotidianas.", False),
            ("Registram a extinção acelerada de espécies de aves raras provocada pela coleta tradicional de sementes e fibras vegetais silvestres.", False),
            ("Impedem a infiltração de água das chuvas no lençol freático devido ao pisoteio constante das trilhas pedestres das aldeias.", False)
        ],
        "Demarcar terras originárias é a mais eficaz e barata política climática: onde há comunidade indígena preservada, a floresta permanece viva em pé."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Por qual motivo é um erro acadêmico grosseiro classificar o pensamento de Krenak e Kopenawa como 'mitologia ingênua desprovida de rigor'?",
        [
            ("Porque suas obras formulam tratados conceituais de alta envergadura cosmopolítica e teórica estudados e aclamados mundialmente.", True),
            ("Porque os líderes indígenas exigiram ser chamados de generais de brigada do exército brasileiro em cerimônias cívicas públicas.", False),
            ("Porque seus textos consistem exclusivamente em transcrições fiéis de bulas de remédios e manuais de motores marítimos de popa.", False),
            ("Porque as universidades da Europa proibiram a tradução de seus ensaios por considerá-los excessivamente fáceis e acessíveis a leigos.", False),
            ("Porque os autores admitiram que compuseram seus livros em menos de dez minutos com a ajuda de programas básicos de edição de texto.", False)
        ],
        "Krenak e Kopenawa são teóricos fundamentais do pensamento planetário contemporâneo, desafiando a miopia ecológica do antropocentrismo ocidental."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "Qual distinção capital afasta o Perspectivismo Ameríndio de um simples relativismo subjetivista do tipo 'cada indivíduo tem sua opinião'?",
        [
            ("A perspectiva não é uma opinião mental subjetiva volátil, mas uma condição inscrita na fisiologia e nos afetos do corpo vivo da espécie.", True),
            ("O perspectivismo proíbe que duas pessoas de uma mesma aldeia conversem sobre as fases da lua durante o período de colheita do milho.", False),
            ("A teoria antropológica foi desenvolvida exclusivamente para orientar a fiscalização de bagagens de passageiros em aeroportos civis.", False),
            ("O relativismo subjetivista é a doutrina oficial consagrada nos estatutos das federações esportivas de tiro com arco e flecha.", False),
            ("A perspectiva corporal desaparece instantaneamente quando o indivíduo ingere alimentos cozidos em panelas de barro modeladas à mão.", False)
        ],
        "No perspectivismo, o corpo é a perspectiva: a onça não 'opina' que o sangue é cerveja de mandioca; seu corpo de predadora assim o experiencia."
    ))

    questoes_brutas.append((
        27, "EM13CHS306", "intermediario",
        "Ao refutar o discurso de que 'a preservação ambiental trava a economia', qual argumento biogeoquímico a ciência contemporânea mobiliza?",
        [
            ("A conservação da Amazônia é a fonte vital do regime de chuvas e umidade que garante a fertilidade da agricultura e os reservatórios do país.", True),
            ("A derrubada total da floresta equatorial transforma o solo arenoso em minas inesgotáveis de diamantes industriais lapidados.", False),
            ("As lavouras monocultoras de grãos produzem nuvens de vapor de água marinha mais densas do que as copas de árvores centenárias da mata.", False),
            ("O aquecimento global extremo provoca a multiplicação espontânea de peixes de água doce em açudes e represas do semiárido nordestino.", False),
            ("A fuligem tóxica provocada por queimadas ilegais limpa o ar atmosférico e melhora a saúde respiratória das populações urbanas periféricas.", False)
        ],
        "Destruir a Amazônia é inviabilizar o agronegócio e a energia do país: a floresta em pé bombeia as chuvas que sustentam o território nacional."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "De que modo a teoria científica dos 'Rios Voadores' do climatologista Antônio Donato Nobre confirma a sabedoria xamânica de Davi Kopenawa?",
        [
            ("Comprova que as árvores amazônicas bombeiam oceanos aéreos de vapor que equilibram o clima, sustentando o céu sobre o continente.", True),
            ("Demonstra que as montanhas rochosas da cordilheira dos Andes foram erguidas por guindastes mecânicos durante a colonização hispânica.", False),
            ("Evidencia que a troposfera terrestre é composta exclusivamente por partículas sólidas de ferro que caem periodicamente sobre as cidades.", False),
            ("Mostra que os pássaros migratórios carregam baldes de água nos bicos para irrigar as plantações de café nas serras de Minas Gerais.", False),
            ("Atesta que as chuvas torrenciais de verão são causadas pela queima de pneus automotivos em rodovias interestaduais pavimentadas.", False)
        ],
        "O xamanismo e a climatologia convergem: a floresta viva mantém o firmamento no alto e alimenta o ciclo das chuvas que protege a vida civilizada."
    ))

    questoes_brutas.append((
        29, "EM13CHS301", "intermediario",
        "Qual avanço jurídico revolucionário as constituições do Equador (2008) e da Bolívia (2009) consagraram inspiradas nos povos originários?",
        [
            ("O reconhecimento da Natureza (Pachamama) como sujeito de direitos jurídicos inalienáveis e o princípio do Bem Viver (Sumak Kawsay).", True),
            ("A privatização compulsória de todas as nascentes de água doce em benefício de corporações multinacionais de engarrafamento de refrigerantes.", False),
            ("A proibição do uso de idiomas indígenas em repartições consulares e edifícios que abrigam cortes de justiça eleitoral provinciais.", False),
            ("A determinação de que todas as montanhas e vulcões sejam dinamitados para facilitar a passagem de carretas de transporte de combustível.", False),
            ("A obrigatoriedade de que os líderes comunitários usem uniformes militares de gala em todas as reuniões de conselhos municipais rurais.", False)
        ],
        "A consagração dos Direitos da Natureza opera o giro ecocêntrico: a Terra deixa de ser propriedade mercantil e torna-se sujeito de dignidade legal."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Ao dialogar com o pensamento ameríndio em Onde Aterrar?, qual tese central o filósofo francês Bruno Latour sustenta sobre a crise ecológica?",
        [
            ("Afirma que a humanidade deve abandonar as ilusões da modernidade descolada da Terra e negociar um novo contrato político com os seres não-humanos.", True),
            ("Defende que a exploração de combustíveis fósseis deve ser acelerada para que a humanidade consiga emigrar em massa para a lua.", False),
            ("Sustenta que as ciências naturais ocidentais são perfeitas e não precisam aprender nenhuma lição de ecologia com povos tradicionais.", False),
            ("Propõe a extinção de reservas florestais para a construção de parques temáticos industriais dedicados ao entretenimento eletrônico.", False),
            ("Recomenda que os governos confisquem os livros de antropologia para priorizar investimentos em fábricas de armamentos balísticos.", False)
        ],
        "Latour reconhece que a modernidade falhou ao se julgar fora da Terra: o Antropoceno exige aterrissar e dialogar com a agência dos seres vivos."
    ))

    questoes_brutas.append((
        31, "EM13CHS501", "intermediario",
        "Como a personificação de rios e montanhas ensinada por Ailton Krenak desafia a clássica tradição jurídica ocidental de propriedade privada?",
        [
            ("Desloca esses entes do estatuto de 'coisas ou recursos' apropriáveis para a categoria ética de sujeitos vivos dotados de direitos inalienáveis.", True),
            ("Exige que os rios paguem impostos prediais urbanos às prefeituras municipais em cujos perímetros realizam suas curvas fluviais.", False),
            ("Permite que as mineradoras comprem certidões de adoção de rios para despejar resíduos industriais com autorização eclesiástica solene.", False),
            ("Determina que as montanhas sejam registradas em cartórios civis com nomes próprios de banqueiros europeus falecidos no século passado.", False),
            ("Proíbe a navegação de canoas artesanais em cursos de água doce que não possuam sinalização de tráfego de semáforos eletrônicos.", False)
        ],
        "Tratar um rio como pessoa viva destrói a premissa extrativista: rios não são estoques inertes para exploração, mas sujeitos de dignidade e respeito."
    ))

    questoes_brutas.append((
        32, "EM13CHS301", "intermediario",
        "No tempo mítico originário compartilhado pelas cosmologias indígenas, o que causou a diferenciação das espécies biológicas atuais?",
        [
            ("Metamorfoses corporais em que os seres humanos primordiais assumiram diferentes pelagens, penas e hábitos corpóreos na floresta.", True),
            ("Experimentos de manipulação genética realizados por cientistas de corporações farmacêuticas em laboratórios subterrâneos.", False),
            ("Quedas sucessivas de meteoros radioativos que alteraram a coloração das folhas das árvores e a respiração pulmonar dos primatas.", False),
            ("Votações democráticas realizadas em assembleias populares onde cada tribo escolheu qual animal silvestre desejava caçar.", False),
            ("A leitura comentada de compêndios de zoologia publicados por sociedades botânicas de capitais imperiais da Europa central.", False)
        ],
        "A mitologia originária relata a metamorfose das roupagens físicas: a humanidade interna permaneceu, mas os corpos se diferenciaram em naturezas."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "O que o uso sagrado do pó da yãkoana pelos xamãs Yanomami representa em contraposição ao uso de substâncias recreativas ocidentais?",
        [
            ("Um rito de conhecimento rigoroso e ascese cósmica, que limpa os olhos do pajé para enxergar e dialogar com os espíritos luminosos Xapiri.", True),
            ("Um passatempo fútil praticado em finais de semana para escapar das obrigações de trabalho nas lavouras comunitárias de mandioca.", False),
            ("Uma droga entorpecente comercializada em mercados clandestinos para financiar o comércio armado de fuzis de infantaria leve.", False),
            ("Um medicamento anestésico industrial fabricado em larga escala para dopar prisioneiros de guerra capturados em conflitos fronteiriços.", False),
            ("Um ingrediente gastronômico comum utilizado para temperar carnes assadas e sopas de peixe em jantares cerimoniais de aldeias.", False)
        ],
        "A inalação da yãkoana é uma ciência xamânica sagrada: exige preparação, jejum e respeito para que o xamã consiga enxergar os seres que sustentam o cosmos."
    ))

    questoes_brutas.append((
        34, "EM13CHS306", "intermediario",
        "O que o conceito geológico e filosófico de 'Antropoceno' expressa perante as advertências das lideranças indígenas contemporâneas?",
        [
            ("A época em que a ação predatória da civilização industrial capitalista passou a atuar como força destrutiva geológica de escala planetária.", True),
            ("O período de ouro em que a humanidade conseguiu erradicar todas as enfermidades biológicas e estabelecer a paz mundial universal.", False),
            ("A era pré-histórica em que os seres humanos conviviam em perfeita harmonia pacífica com manadas de dinossauros herbívoros.", False),
            ("A época em que os governos de todos os países do mundo decidiram proibir a circulação de veículos automotores em áreas urbanas.", False),
            ("O momento histórico em que as estações do ano foram unificadas em uma única primavera eterna e constante em todas as latitudes.", False)
        ],
        "O Antropoceno materializa o alerta indígena: o homem ocidental descolou-se da Terra e transformou sua voracidade em ameaça de destruição geológica."
    ))

    questoes_brutas.append((
        35, "EM13CHS101", "intermediario",
        "Durante o isolamento sanitário da Covid-19, qual interpretação Ailton Krenak formulou em A Vida Não É Útil sobre o vírus?",
        [
            ("Como uma advertência física da Terra viva paralisando a engrenagem da máquina de consumo para lembrar que somos organismos vulneráveis.", True),
            ("Como um complô arquitetado por alfaiates parisienses para incentivar a venda massiva de máscaras de tecido de algodão colorido.", False),
            ("Como a prova contundente de que os seres humanos urbanos são imunes a patologias respiratórias graças ao uso de aparelhos celulares.", False),
            ("Como uma moléstia fictícia inventada por companhias aéreas para economizar despesas operacionais com combustível de aviação civil.", False),
            ("Como um feitiço mágico lançado por astrólogos descontentes com os horários de início das transmissões de partidas desportivas de televisão.", False)
        ],
        "Para Krenak, o vírus funcionou como puxão de orelha da Terra: desnudou a fragilidade da arrogância humana e exigiu repensar o modo de vida acelerado."
    ))

    questoes_brutas.append((
        36, "EM13CHS301", "intermediario",
        "No Perspectivismo Ameríndio, por que o corpo é definido como 'roupagem viva' e não como uma máquina de peças anatômicas frias?",
        [
            ("Porque o corpo é o conjunto dinâmico de afecções, hábitos alimentares, capacidades sensoriais e modos de habitar o território compartilhado.", True),
            ("Porque os animais da floresta costumam tecer calças e jaquetas de lã de ovelha para se proteger das geadas de inverno nas matas.", False),
            ("Porque a anatomia muscular e a circulação sanguínea deixam de funcionar nas espécies animais que habitam regiões de clima úmido.", False),
            ("Porque os ossos do esqueleto dos mamíferos florestais são compostos por fibras vegetais secas que se desintegram no contato com a água.", False),
            ("Porque as diferenças biológicas entre as espécies dependem exclusivamente da cor das tintas corporais aplicadas em ritos guerreiros.", False)
        ],
        "O corpo ameríndio é um feixe de capacidades perceptivas: a forma corpórea é uma vestimenta que determina o ponto de vista daquele ser no cosmos."
    ))

    questoes_brutas.append((
        37, "EM13CHS501", "intermediario",
        "Ao afirmar que o Watu está 'em coma', qual apelo de dignidade ética Ailton Krenak dirige à sociedade brasileira contemporânea?",
        [
            ("O dever de respeitar o luto da bacia hidrográfica e interromper a exploração predatória para permitir a regeneração da vida do rio.", True),
            ("A exigência de que os governos canalizem o curso do rio Doce em tubulações subterrâneas de concreto para evitar mau cheiro nas praias.", False),
            ("A proposta de substituir o leito natural do rio por uma rodovia asfaltada de alta velocidade para o transporte de cargas de minério.", False),
            ("A cobrança de pedágios fluviais de canoas indígenas para arrecadar recursos destinados à construção de barragens de hidrelétricas.", False),
            ("A recomendação médica de que a população ribeirinha passe a consumir água salgada do oceano Atlântico em garrafas térmicas de vidro.", False)
        ],
        "Dizer que o rio está em coma exige respeito ético e regeneração: não há indenização que pague o assassinato de uma bacia viva de águas e memórias."
    ))

    questoes_brutas.append((
        38, "EM13CHS101", "intermediario",
        "Na cosmologia do povo Yanomami narrada por Davi Kopenawa, que atribuições cabem ao demiurgo criador Omama?",
        [
            ("Criou a floresta viva, ordenou o cosmos, ensinou os preceitos éticos e sepultou os minérios perigosos nas entranhas profundas da terra.", True),
            ("Construiu as primeiras ferrovias a vapor da bacia amazônica para transportar mercadorias manufaturadas para os portos do Atlântico.", False),
            ("Inventou as dragas mecânicas de garimpo para ensinar os povos da floresta a comercializar pepitas de ouro em capitais estrangeiras.", False),
            ("Assinou os tratados diplomáticos de fronteiras territoriais entre o império colonial britânico e a corte imperial da Espanha.", False),
            ("Redigiu os códigos penais militares que regulamentam a conduta de soldados de infantaria em operações em matas fechadas.", False)
        ],
        "Omama é o arquiteto da harmonia cósmica Yanomami: deu regras aos seres, ergueu o céu e guardou o ouro nas profundezas para proteger a vida."
    ))

    questoes_brutas.append((
        39, "EM13CHS601", "intermediario",
        "No contexto da educação antirracista, de que maneira a articulação das Leis nº 10.639/03 e nº 11.645/08 coroa a descolonização do currículo escolar do Ensino Médio no Brasil?",
        [
            ("Garante o reconhecimento paritário das matrizes indígenas e africanas, superando o eurocentrismo e fundando uma cidadania plural.", True),
            ("Exige que os estudantes do ensino médio passem a residir em aldeias isoladas durante todos os semestres do ano letivo regular.", False),
            ("Substitui as provas escritas tradicionais por competições de corrida de velocidade com toras de madeira nas praças municipais.", False),
            ("Proíbe o debate acadêmico sobre os clássicos do pensamento europeu como Platão, Descartes, Kant, Nietzsche e Wittgenstein.", False),
            ("Determina que apenas professores que comprovem descendência consanguínea de dinastias régias africanas possam ministrar aulas.", False)
        ],
        "As leis 10.639/03 e 11.645/08 descolonizam o olhar escolar: a filosofia torna-se o encontro de todas as vozes e matrizes que tecem o Brasil e o mundo."
    ))

    questoes_brutas.append((
        40, "EM13CHS101", "intermediario",
        "Em suma, qual é a grande lição que a conclusão da Coleção de Filosofia do Ensino Médio transmite aos estudantes da Educamob?",
        [
            ("Que filosofar é uma aventura universal e emancipatória da humanidade, que nos convoca a pensar criticamente e cuidar do futuro comum da Terra.", True),
            ("Que o estudo do pensamento filosófico é uma atividade inútil que deve ser esquecida no momento do término do exame escolar.", False),
            ("Que a ciência ocidental moderna resolveu todos os dilemas morais e ambientais do planeta através da expansão do mercado de capitais.", False),
            ("Que os seres humanos devem disputar ferozmente a primazia do lucro individual contra seus semelhantes em qualquer circunstância da vida.", False),
            ("Que o saber acadêmico é um privilégio aristocrático restrito a cidadãos ricos que residem em capitais imperiais do Norte Global.", False)
        ],
        "A filosofia ensina a pensar, a resistir e a sonhar: coroa-se a coleção como um chamado à lucidez cidadã, à solidariedade e ao cuidado do cosmos vivo."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 em 100% das resoluções
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS102", "dificil",
        "Na desconstrução da modernidade cartesiana operada pelas epistemologias ameríndias, como a divisão entre res cogitans e res extensa é superada?",
        [
            ("Ao demonstrar que a subjetividade, a intencionalidade e a fala não são monopólios humanos, mas atributos cósmicos partilhados pela biosfera.", True),
            ("Ao provar por meio de microscópios eletrônicos que as moléculas químicas inorgânicas possuem aparelhos auditivos idênticos aos dos primatas.", False),
            ("Ao restabelecer os dogmas eclesiásticos da Inquisição espanhola sobre a infalibilidade dos textos teológicos redigidos em papiro.", False),
            ("Ao decretar a extinção dos métodos de pesquisa científica experimental em todas as universidades públicas de ciências exatas e da terra.", False),
            ("Ao afirmar que as pedras e minerais pesados possuem circulação sanguínea e batimentos cardíacos verificáveis em exames laboratoriais.", False)
        ],
        "As filosofias originárias implodem o mecanicismo cartesiano: o cosmos não é matéria inerte para posse humana, mas teia viva de sujeitos e agências."
    ))

    questoes_brutas.append((
        42, "EM13CHS301", "dificil",
        "Como a arquitetura conceitual do Perspectivismo Ameríndio inverte com rigor os axiomas do multiculturalismo ocidental moderno?",
        [
            ("Enquanto o Ocidente postula uma natureza objetiva e muitas culturas subjetivas, o ameríndio afirma uma cultura comum e muitas naturezas corpóreas.", True),
            ("Enquanto o Ocidente valoriza as línguas nacionais, o ameríndio defende a unificação dos povos sob o idioma latim arcaico eclesiástico.", False),
            ("Enquanto o Ocidente viaja para o espaço sideral em foguetes, o ameríndio afirma que os planetas do sistema solar não existem no cosmos.", False),
            ("Enquanto o Ocidente estuda a física das partículas, o ameríndio sustenta que todos os fenômenos da natureza são ilusões dos sentidos.", False),
            ("Enquanto o Ocidente defende o sufrágio universal, o ameríndio preconiza a ditadura vitalícia de chefes militares em aldeias florestais.", False)
        ],
        "O perspectivismo inverte o eixo: todos os seres têm a mesma cultura humana de fundo; a diferença reside no corpo que condiciona sua natureza perceptiva."
    ))

    questoes_brutas.append((
        43, "EM13CHS306", "dificil",
        "Qual é o perigo existencial mortal que espreita o caçador indígena que desrespeita os preceitos éticos da diplomacia xamânica na floresta?",
        [
            ("Perder sua própria perspectiva humana e adoecer, sendo capturado pelo olhar da presa e metamorfoseado na outra espécie na mata.", True),
            ("Ser multado financeiramente por auditores tributários federais por sonegação de impostos sobre mercadorias agrícolas silvestres.", False),
            ("Sofrer a perda imediata da audição periférica em virtude do barulho produzido pelas asas de insetos voadores noturnos.", False),
            ("Ter sua certidão de nascimento civil cancelada por tabeliães cartorários de comarcas judiciárias provinciais do interior.", False),
            ("Ser obrigado a redigir tratados acadêmicos sobre direito constitucional em língua estrangeira sob a vigilância de policiais militares.", False)
        ],
        "Na ontologia ameríndia, a caça predatória egoísta rompe a diplomacia cósmica: o caçador pode ser capturado pelo olhar do animal e perder a humanidade."
    ))

    questoes_brutas.append((
        44, "EM13CHS601", "dificil",
        "Em sua reflexão filosófica sobre o saber tradicional, como Ailton Krenak compreende a experiência do sonho para os povos originários?",
        [
            ("Como uma instituição cultural de orientação cósmica e aprendizado coletivo, em que se dialoga com a memória viva dos ancestrais.", True),
            ("Como uma ilusão psicológica aleatória causada pelo cansaço físico que deve ser ignorada em decisões comunitárias.", False),
            ("Como um relatório contábil cifrado que antecipa a cotação diária de moedas estrangeiras em bolsas de valores.", False),
            ("Como um sintoma de enfermidade infecciosa que exige o isolamento compulsório do indivíduo em cabanas separadas.", False),
            ("Como uma prática mágica medieval banida dos territórios indígenas por determinação de órgãos de fiscalização sanitária.", False)
        ],
        "Para Krenak, o sonho indígena é lugar de conhecimento e diplomacia com o invisível, contrastando com o sono vazio e utilitário do homem moderno."
    ))

    questoes_brutas.append((
        45, "EM13CHS306", "dificil",
        "No horizonte da jurisprudência ecológica, sob quais aspectos a consideração do Rio Doce (Watu) como parente ancestral personificado impacta a teoria contemporânea dos Direitos da Natureza?",
        [
            ("Eleva elementos ecológicos ao estatuto de sujeitos de direito com dignidade própria, rompendo com a doutrina mecanicista do mero recurso utilitário.", True),
            ("Obriga os conselhos de bacias hidrográficas a nomear peixes carnívoros como presidentes honorários de audiências públicas municipais.", False),
            ("Determina que os cursos de água doce recebam salários mensais em moeda fiduciária depositados em contas correntes de bancos estatais.", False),
            ("Proíbe o uso de canoas de madeira e pequenas jangadas de pescadores artesanais que não possuam certificados de inspeção naval moderna.", False),
            ("Cancela todas as leis ambientais vigentes no país em prol de decisões expedidas verbalmente por tribunais de arbitragem comercial externa.", False)
        ],
        "Reconhecer o Watu como pessoa viva coroa a transição para a jurisprudência ecocêntrica: a natureza tem valor em si e não depende da utilidade econômica."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Qual é o sentido cosmopolítico do manifesto de Davi Kopenawa em A Queda do Céu perante a crise ecológica da modernidade tardia?",
        [
            ("Afirma que o xamanismo amazônico atua como ecologia planetária ativa: os pajés sustentam o equilíbrio do céu para toda a humanidade terrestre.", True),
            ("Preconiza que os povos indígenas devem abandonar suas florestas para adquirir apartamentos em edifícios de luxo nas capitais costeiras.", False),
            ("Defende que as corporações mineradoras multinacionais devem receber títulos de benemerência ecológica por patrocinar festejos esportivos.", False),
            ("Sustenta que os espíritos xamânicos foram inventados por navegadores portugueses para entreter marinheiros em caravelas quinhentistas.", False),
            ("Declara que as chuvas torrenciais do inverno amazônico decorrem exclusivamente de desvios magnéticos nos polos frios da Antártica.", False)
        ],
        "A luta de Kopenawa é universal: os xamãs sustentam o firmamento contra a xawara predatória; defender a Amazônia é defender a respiração de todo o planeta."
    ))

    questoes_brutas.append((
        47, "EM13CHS501", "dificil",
        "Como a semiótica xamânica do ouro descrita por Kopenawa subverte a racionalidade econômica da mineração e da acumulação financeira capitalista?",
        [
            ("O ouro não é riqueza reluzente, mas matéria venenosa soterrada pelo demiurgo; desenterrá-lo é liberar as fumaças de morte que asfixiam o mundo.", True),
            ("O ouro é um mineral inofensivo que melhora a pureza das águas dos rios amazônicos quando triturado por dragas mecânicas de alta potência.", False),
            ("O metal dourado deve ser utilizado prioritariamente para fabricar anzóis de pesca submarina e pontas de flechas de caça esportiva.", False),
            ("A mineração subterrânea é uma prática ecológica virtuosa incentivada pelos espíritos Xapiri para limpar a poeira das pedras da floresta.", False),
            ("Os lingotes de ouro depositados nos cofres de bancos centrais internacionais emitem radiações térmicas que controlam o aquecimento global.", False)
        ],
        "Kopenawa desmascara o fetiche do ouro: aquilo que o capital idolatra como riqueza máxima é veneno e epidemia que mata crianças e destrói o ar."
    ))

    questoes_brutas.append((
        48, "EM13CHS306", "dificil",
        "Em que termos a climatologia dos 'Rios Voadores' de Antônio Nobre valida e traduz empiricamente a ontologia cósmica Yanomami?",
        [
            ("Mostra que a floresta viva bombeia gigantescos volumes de vapor que regulam o clima, confirmando que a floresta erguida sustenta o céu no alto.", True),
            ("Comprova que as chuvas continentais são provocadas exclusivamente pelo vapor que sobe das chaminés de indústrias siderúrgicas de carvão.", False),
            ("Demonstra que o desmatamento total das margens dos rios acelera o fluxo de água potável em direção aos reservatórios de hidrelétricas.", False),
            ("Evidencia que a atmosfera terrestre é indiferente à cobertura vegetal das árvores e que o clima depende unicamente de marés oceânicas.", False),
            ("Afirma que a transição energética fóssil é um erro e que as nações modernas devem queimar florestas primárias em fornos de padarias.", False)
        ],
        "A ciência e o xamanismo cantam a mesma verdade: a floresta em pé é o motor do ciclo das águas; derrubá-la fará o céu da habitabilidade desabar."
    ))

    questoes_brutas.append((
        49, "EM13CHS601", "dificil",
        "Ao derrubar a tese do Marco Temporal, em que se baseia a fundamentação histórica e jurídica da doutrina do Indigenato acolhida pelo STF?",
        [
            ("O direito dos povos originários à posse tradicional de suas terras é inato e originário, precedendo a existência formal do próprio Estado.", True),
            ("O direito à demarcação de terras depende do pagamento prévio de taxas de concessão imobiliária a fundos de pensão de servidores públicos.", False),
            ("As comunidades tradicionais devem comprovar a posse ininterrupta da terra desde a chegada das primeiras caravelas portuguesas em mil e quinhentos.", False),
            ("O Estado brasileiro tem a faculdade soberana de confiscar qualquer território indígena para a instalação de empreendimentos industriais privados.", False),
            ("A constituição federal de mil novecentos e oitenta e oito revogou todos os direitos territoriais das populações indígenas que vivem no litoral.", False)
        ],
        "O Indigenato consagra o direito congênito: os povos originários estavam aqui antes da fundação jurídica do Brasil; seu direito à terra é raiz inalienável."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "Em A Vida Não É Útil, como a recusa krenakiana da produtividade compulsória dialoga criticamente com o conceito de Sociedade do Desempenho?",
        [
            ("Ambos denunciam a escravização da vida pela máquina produtiva neoliberal, resgatando a gratuidade da existência e o valor da contemplação poética.", True),
            ("Ambos defendem que todos os cidadãos devem trabalhar dezesseis horas diárias ininterruptas para garantir a prosperidade econômica da nação.", False),
            ("Ambos propõem que o valor de um ser humano seja medido pelo número de seguidores e visualizações acumulados em plataformas telemáticas.", False),
            ("Ambos comemoram a expansão das jornadas de trabalho aos domingos e feriados cívicos como o ápice da emancipação moral dos operários.", False),
            ("Ambos sustentam que a filosofia acadêmica deve ser substituída por cursos intensivos de investimento em ações de companhias de aviação civil.", False)
        ],
        "Krenak e Han convergem com agudeza: a vida não é mercadoria útil para engrenagens produtivas; é celebração, contemplação e presença partilhada."
    ))

    questoes_brutas.append((
        51, "EM13CHS306", "dificil",
        "Sob a perspectiva da ética da alteridade, qual é o abismo existencial exposto pelas catástrofes de Mariana e Brumadinho em Minas Gerais?",
        [
            ("O contraste entre a racionalidade contábil predatória que calcula vidas como custos e a ontologia originária que reverencia a Terra como parente vivo.", True),
            ("A disputa jurídica entre as federações esportivas de futebol que reivindicavam o uso de campos gramados situados nas bacias dos rios.", False),
            ("O desacordo diplomático entre os embaixadores da França e da Alemanha sobre as taxas alfandegárias de exportação de café em grãos.", False),
            ("A recusa dos engenheiros civis em utilizar computadores eletrônicos para realizar cálculos de estabilidade de barragens de aterro de terra.", False),
            ("A tentativa dos pescadores artesanais de privatizar as águas da foz do rio Doce para construir marinas exclusivas de iates esportivos.", False)
        ],
        "Mariana expõe o choque civilizatório: para a corporação, a tragédia é risco de balanço; para os povos da terra, é a dor irreparável do ecocídio."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Por que a caracterização do Perspectivismo Ameríndio como Multinaturismo desmantela a premissa moderna da supremacia da razão ocidental?",
        [
            ("Porque descentra o humano como único detentor do ponto de vista reflexivo, reconhecendo que outros entes possuem agência e dignidade de sujeito.", True),
            ("Porque determina que todas as teorias científicas astronômicas sejam substituídas por horóscopos elaborados por navegadores vikings antigos.", False),
            ("Porque obriga os departamentos de matemática a suspender a pesquisa sobre números primos para priorizar a adivinhação com sementes de feijão.", False),
            ("Porque afirma que os seres humanos contemporâneos perderam a capacidade de enxergar cores primárias em dias de sol brilhante no horizonte.", False),
            ("Porque proíbe a escrita de ensaios acadêmicos em línguas vivas para forçar a comunicação universal por meio de assobios modulados no ar.", False)
        ],
        "O multinaturismo destrona a soberba humana: o homem não é o único centro de consciência; a onça, a anta e a árvore são sujeitos dotados de ponto de vista."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Como a teoria do ator-rede de Bruno Latour converge com o perspectivismo ameríndio no enfrentamento da crise socioambiental planetária?",
        [
            ("Ambos reconhecem agência aos seres não-humanos, sustentando que a política ecológica contemporânea deve ser uma diplomacia cósmica alargada.", True),
            ("Ambos propõem que as decisões governamentais sobre orçamento público sejam tomadas exclusivamente por inteligências artificiais autônomas.", False),
            ("Ambos defendem que todos os animais de zoológicos recebam títulos de bacharelado em ciências sociais por terem convivido com turistas.", False),
            ("Ambos afirmam que a sociologia e a antropologia devem ser extintas e substituídas pela memorização mecânica de tabelas de preços de bolsas.", False),
            ("Ambos preconizam que a humanidade deve renunciar ao convívio comunitário para se isolar em cápsulas de plástico herméticas no fundo do mar.", False)
        ],
        "Latour e Viveiros de Castro unem-se na mesma batalha: incluir os não-humanos na arena política é a única saída para a sobrevivência no Antropoceno."
    ))

    questoes_brutas.append((
        54, "EM13CHS301", "dificil",
        "Qual é o sentido civilizatório supremo da categoria do Bem Viver (Sumak Kawsay) consagrada nas constituições da Bolívia e do Equador?",
        [
            ("Substitui o paradigma do crescimento material contínuo por uma vida em harmonia com a comunidade humana e com a Mãe Terra (Pachamama).", True),
            ("Obriga os cidadãos a renunciar ao uso de energia elétrica para iluminar suas residências com tochas de cera de abelhas silvestres.", False),
            ("Garante a distribuição de automóveis esportivos de luxo para todas as famílias camponesas que possuem propriedades em zonas áridas.", False),
            ("Declara que as florestas de altitude devem ser desmatadas para a construção de aeroportos internacionais de cargas de minério de ferro.", False),
            ("Proíbe o debate acadêmico sobre direitos humanos universais em recintos escolares que possuem grêmios estudantis autônomos em atividade.", False)
        ],
        "O Bem Viver supera o desenvolvimentismo predador: prosperidade não é acumular mercadorias, mas viver em harmonia com os outros e com a Terra."
    ))

    questoes_brutas.append((
        55, "EM13CHS101", "dificil",
        "Em Futuro Ancestral e Ideias para Adiar o Fim do Mundo, como Krenak articula a ancestralidade como tecnologia de sobrevivência no Antropoceno?",
        [
            ("A ancestralidade não é apego ao passado morto, mas memória viva e poética que ensina a cultivar a terra e empurrar o horizonte da esperança.", True),
            ("A ancestralidade consiste na reprodução mecânica de métodos medievais de cobrança de dízimos em templos eclesiásticos europeus.", False),
            ("A ancestralidade exige que as novas gerações renunciem ao uso da escrita alfabética e da matemática aplicada na educação básica.", False),
            ("A ancestralidade representa um conjunto de superstições anônimas que impedem a realização de transplantes de órgãos em hospitais públicos.", False),
            ("A ancestralidade determina que os conflitos fundiários devam ser decididos por combates individuais com bastões de madeira em praça.", False)
        ],
        "O futuro é ancestral: a sabedoria dos povos que resistiram a séculos de invasão guarda as ferramentas existenciais para adiar o fim do mundo."
    ))

    questoes_brutas.append((
        56, "EM13CHS501", "dificil",
        "Qual nexo histórico-filosófico profundo une o epistemicídio contra os saberes originários e o ecocídio ambiental na história do Brasil?",
        [
            ("A mesma lógica de dominação que desqualificou o saber indígena como selvageria legitimou a destruição dos biomas para o lucro de elites coloniais.", True),
            ("O fato de que os povos da floresta foram os principais inventores das motosserras industriais utilizadas para a extração de madeira de lei.", False),
            ("A crença dos colonizadores europeus de que as árvores centenárias da mata atlântica continham ouro líquido em suas seivas vegetais.", False),
            ("A assinatura de tratados internacionais que obrigavam os fazendeiros de café a reflorestar as encostas de morros com palmeiras imperiais.", False),
            ("A expulsão de companhias de mineração de solos brasileiros por ordem expressa de generais que governavam as províncias meridionais.", False)
        ],
        "Matar o saber e matar a terra são duas faces da mesma violência colonial: desvalorizar a ontologia indígena facilitou a rapina predatória dos biomas."
    ))

    questoes_brutas.append((
        57, "EM13CHS306", "dificil",
        "Como a contaminação generalizada por mercúrio na Amazônia traduz fisicamente o colapso moral do Povo da Mercadoria criticado por Kopenawa?",
        [
            ("Evidencia a desumanização de uma sociedade que envenena crianças e cursos de água potável para acumular ouro inerte e lucro predatório.", True),
            ("Comprova que os metais pesados são produtos químicos biodegradáveis que se desintegram rapidamente na presença de luz solar tropical.", False),
            ("Mostra que os mineradores clandestinos aplicam mercúrio nas águas para eliminar larvas de mosquitos que transmitem a febre amarela silvestre.", False),
            ("Demonstra que a atividade garimpeira enriqueceu a totalidade das famílias indígenas das bacias dos rios Catrimani e Mucajaí em Roraima.", False),
            ("Atesta que as corporações financeiras internacionais utilizam o pó de ouro amazônico para confeccionar instrumentos cirúrgicos esterilizados.", False)
        ],
        "O mercúrio no sangue das crianças Yanomami é o retrato do abismo capitalista: sacrificar a vida de gerações para engordar cofres de agiotagem mineral."
    ))

    questoes_brutas.append((
        58, "EM13CHS101", "dificil",
        "De que modo a filosofia de Ailton Krenak emancipa a juventude contemporânea da armadilha do consumidor isolado e despolitizado?",
        [
            ("Convocando os jovens a redescobrir o sentimento de pertencimento ao organismo vivo da Terra, recusando a pressa do consumo sem sentido.", True),
            ("Incentivando os adolescentes a adquirir o maior número possível de aparelhos eletrônicos de última geração através de empréstimos bancários.", False),
            ("Propondo que os estudantes abandonem as manifestações cívicas pacíficas para priorizar apostas financeiras em corridas de cavalos virtuais.", False),
            ("Defendendo que as escolas de ensino médio suspendam os debates sobre direitos fundamentais para priorizar treinamentos de maratona atlética.", False),
            ("Ensinando que a felicidade humana depende exclusivamente da posse de títulos societários de grandes conglomerados industriais químicos.", False)
        ],
        "Krenak devolve a dignidade ao sujeito: não somos consumidores ansiosos em uma corrida maluca; somos filhos e filhas da Terra chamados a celebrar a vida."
    ))

    questoes_brutas.append((
        59, "EM13CHS601", "dificil",
        "Qual é o impacto transformador supremo das Leis nº 10.639/03 e nº 11.645/08 na refundação do pensamento filosófico brasileiro?",
        [
            ("Desmantelam o epistemicídio eurocêntrico, consagrando as matrizes africanas e indígenas como pilares vitais de uma filosofia antirracista e plural.", True),
            ("Obrigam as universidades do país a emitir diplomas acadêmicos em línguas germânicas medievais para garantir a aceitação internacional de teses.", False),
            ("Determinam o fechamento de todas as bibliotecas que possuem acervos de obras clássicas da filosofia grega antiga e do iluminismo francês.", False),
            ("Proíbem a realização de pesquisas científicas sobre física quântica e biologia molecular em institutos de ensino e tecnologia aplicada.", False),
            ("Estabelecem que a cidadania política depende exclusivamente da aprovação em testes de aptidão física aplicados em quarteis das forças armadas.", False)
        ],
        "As leis 10.639 e 11.645 coroam a maturidade democrática: a filosofia brasileira fala em todas as vozes, enraizando o saber na justiça e na diversidade."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "No encerramento consagrador de toda a Coleção de Filosofia do Ensino Médio, qual mensagem eterna a Filosofia da Terra lega à humanidade?",
        [
            ("Que a Terra não nos pertence; nós pertencemos à Terra; nossa vocação é tecer o cuidado, escutar o canto dos rios e sustentar juntos o firmamento.", True),
            ("Que o avanço da civilização requer a queima de todos os recursos biológicos da biosfera para acumular ouro em cofres bancários submarinos.", False),
            ("Que os seres humanos devem renunciar ao pensamento reflexivo crítico e aceitar passivamente a tutela de corporações financeiras globais.", False),
            ("Que a história da humanidade chegou ao seu término definitivo com a vitória irrevogável do modelo individualista do consumo predatório.", False),
            ("Que as gerações futuras serão constituídas por máquinas mecânicas autônomas que não necessitam de afeto, de ar puro e de poesia para existir.", False)
        ],
        "A grande lição final de Filosofia EM: somos parte de um cosmos sagrado e vivo; cantar, dançar e cuidar da Terra é a nossa missão suprema no século XXI."
    ))

    return questoes_brutas

def verificar_blacklist(texto):
    padroes_proibidos = [
        r"\bepistemol[oó]gic\w*",
        r"\bontol[oó]gic\w*",
        r"\bteleol[oó]gic\w*",
        r"\bdicotomi\w*",
        r"\bintr[ií]nsec\w*",
        r"\bextr[ií]nsec\w*",
        r"\bsubjacente\w*",
        r"\bef[eê]mer\w*",
        r"\bprerrogativa\w*",
        r"\bprescind\w*",
        r"\bimprescind\w*",
        r"\bcorrobor\w*",
        r"\bhegem[oô]nic\w*",
        r"\bmitigar\b",
        r"\bfomentar\b",
        r"\bproped[eê]utic\w*",
        r"\binexor\w*",
        r"\baxiol[oó]gic\w*",
        r"\bhermen[eê]utic\w*",
        r"\bmormente\b",
        r"\bprec[ií]pu\w*",
        r"\bvern[aá]cul\w*",
        r"\bdestarte\b",
        r"\boutrossim\b",
        r"\bhodiern\w*",
        r"\bidiossincrasi\w*",
        r"R\$"
    ]
    erros = []
    for padrao in padroes_proibidos:
        matches = re.findall(padrao, texto, re.IGNORECASE)
        if matches:
            erros.append((padrao, list(set(matches))))
    return erros

def formatar_markdown(questoes):
    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('eixo: "Eixo V: Existencialismo, Filosofias da Diferença e Saberes Tradicionais"')
    md.append('capitulo: "Capítulo 40: Epistemologias Ameríndias e Filosofias da Terra"')
    md.append('objeto_de_conhecimento: "O pensamento filosófico dos povos originários das Américas (Lei nº 11.645/08); a superação da cisão ocidental entre Natureza e Cultura; Eduardo Viveiros de Castro e o Perspectivismo Ameríndio: multinaturismo versus multiculturalismo; Ailton Krenak e as Filosofias da Terra (Ideias para Adiar o Fim do Mundo, A Vida Não É Útil e Futuro Ancestral); a personificação dos seres não-humanos e o Rio Doce (Watu) como ancestral; a crítica à utilidade capitalista e a poética de adiar o fim do mundo; Davi Kopenawa e A Queda do Céu: o xamanismo Yanomami como teoria cósmica, os espíritos Xapiri e a crítica à doença da mercadoria branca (motiro)"')
    md.append('ebook_fonte: "em-fil-c40-epistemologias-amerindias-filosofia-terra-krenak.md"')
    md.append('habilidades:')
    md.append('  - "EM13CHS101"')
    md.append('  - "EM13CHS102"')
    md.append('  - "EM13CHS301"')
    md.append('  - "EM13CHS306"')
    md.append('  - "EM13CHS601"')
    md.append('total_exercicios: 60')
    md.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    md.append("---\n")

    md.append("# Lista de Exercícios: Epistemologias Ameríndias e Filosofias da Terra\n")
    md.append("## Nível Básico\n")

    letras = ["A", "B", "C", "D", "E"]

    for num, hab, dif, enunciado, alternativas, resolucao in questoes:
        if num == 21:
            md.append("## Nível Intermediário\n")
        elif num == 41:
            md.append("## Nível Difícil\n")

        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-40-epistemologias-amerindias-filosofia-terra-krenak -->")
        md.append(f"### Questão {num}\n")
        md.append(f"{enunciado}\n")
        
        letra_correta = None
        for i, (alt_texto, correta) in enumerate(alternativas):
            l = letras[i]
            md.append(f"{l}) {alt_texto}")
            if correta:
                letra_correta = l
        
        md.append(f"\n**Gabarito:** ({letra_correta})\n")
        if dif == "dificil":
            md.append(f"**Resolução Comentada:**\n- **Etapa 1:** Compreensão conceitual e análise contextual do problema proposto.\n- **Etapa 2:** Justificativa da resposta: {resolucao}\n")
        else:
            md.append(f"**Resolução Comentada:**\n{resolucao}\n")
        md.append("---\n")

    md.append("## Referências\n")
    md.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")
    md.append("- KOPENAWA, Davi; ALBERT, Bruce. *A Queda do Céu: palavras de um xamã yanomami*. Tradução de Beatriz Perrone-Moisés. São Paulo: Companhia das Letras, 2015.")
    md.append("- KRENAK, Ailton. *Ideias para Adiar o Fim do Mundo*. São Paulo: Companhia das Letras, 2019.")
    md.append("- KRENAK, Ailton. *A Vida Não É Útil*. São Paulo: Companhia das Letras, 2020.")
    md.append("- KRENAK, Ailton. *Futuro Ancestral*. São Paulo: Companhia das Letras, 2022.")
    md.append("- LATOUR, Bruno. *Onde Aterrar? Como se orientar no labirinto da política*. Tradução de Marcela Vieira. Rio de Janeiro: Bazar do Tempo, 2020.")
    md.append("- VIVEIROS DE CASTRO, Eduardo. *A Inconstância da Alma Selvagem e Outros Ensaios de Antropologia*. São Paulo: Cosac Naify, 2002.\n")

    return "\n".join(md)

def main():
    questoes = build_exercicios()
    print(f"Total de questões construídas: {len(questoes)}")

    # 1. Checagem de quantidade e numeração
    assert len(questoes) == 60, f"Esperava 60 questões, obteve {len(questoes)}"
    for idx, q in enumerate(questoes, 1):
        assert q[0] == idx, f"Questão fora de ordem: {q[0]} != {idx}"

    # 2. Ajuste rigoroso de gabarito para ciclo balanceado perfeito (12 de cada)
    questoes_balanceadas = []
    for q in questoes:
        num, hab, dif, enunciado, alternativas, resolucao = q
        target_idx = (num - 1) % 5
        corr_idx = [i for i, (_, c) in enumerate(alternativas) if c][0]
        if corr_idx != target_idx:
            alts = list(alternativas)
            alts[corr_idx], alts[target_idx] = alts[target_idx], alts[corr_idx]
            questoes_balanceadas.append((num, hab, dif, enunciado, alts, resolucao))
        else:
            questoes_balanceadas.append(q)

    # 3. Formatação
    md_content = formatar_markdown(questoes_balanceadas)

    # 4. Checagem de gabarito balanceado no markdown
    gabs = re.findall(r"\*\*Gabarito:\*\* \(([A-E])\)", md_content)
    assert len(gabs) == 60, f"Esperava 60 gabaritos, obteve {len(gabs)}"
    contagem = Counter(gabs)
    print("Distribuição de gabaritos:", contagem)
    for l in ["A", "B", "C", "D", "E"]:
        assert contagem[l] == 12, f"Letra {l} tem {contagem[l]} ocorrências (esperado 12)!"

    # 5. Checagem de blacklist no texto gerado
    erros_bl = verificar_blacklist(md_content)
    if erros_bl:
        print("\n[ERRO FATAL] Termos proibidos encontrados:")
        for padrao, matches in erros_bl:
            print(f"  - Padrão '{padrao}': {matches}")
        sys.exit(1)
    else:
        print("Auditoria interna: NENHUM termo da blacklist detectado!")

    # 6. Checagem de inícios de enunciados repetidos
    inicios = [q[3].split()[:2] for q in questoes]
    inicios_str = [" ".join(x).lower() for x in inicios]
    c_inicios = Counter(inicios_str)
    print("Inícios mais frequentes:", c_inicios.most_common(5))
    for inicio, count in c_inicios.items():
        if count > 6:
            print(f"[ALERTA/ERRO] Início '{inicio}' ocorre {count} vezes (>6)!")
            sys.exit(1)

    # 7. Salvar em temp_draft.md
    temp_draft = "temp_draft.md"
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Arquivo rascunho salvo com sucesso em '{temp_draft}'.")

    # 8. Executar validador oficial
    destino_final = "content/medio/volume-unico/filosofia/eixo-5-existencialismo-diferenca/cap-40-epistemologias-amerindias-filosofia-terra-krenak/ebooks/em-fil-c40-epistemologias-amerindias-filosofia-terra-krenak-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL ABSOLUTO] Cap 40 validado e homologado com Exit Code 0!")
        print("=========================================================================")
        print("MARCO HISTÓRICO DEFINITIVO: 100% DA COLEÇÃO DE FILOSOFIA HOMOLOGADA!")
        print("40 CAPÍTULOS | 5 EIXOS | 2.400 QUESTÕES NO PADRÃO-OURO EDUCAMOB!")
        print("=========================================================================")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
