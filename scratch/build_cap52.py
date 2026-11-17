import re
import os

def build_draft_c52():
    frontmatter = """---
série: "Ensino Médio"
disciplina: "História"
objeto_de_conhecimento: "A História Ecológica do Território Brasileiro de Acordo com Warren Dean (A Ferro e Fogo): A Relação Predatória entre a Economia Colonial/Imperial e a Natureza; A Destruição Quase Total da Mata Atlântica pelos Ciclos do Pau-Brasil, da Cana-de-Açúcar, da Mineração e do Café no Vale do Paraíba; O Impacto da Pecuária Extensiva no Cerrado e na Caatinga; A Marcha da Fronteira Agrícola e Madeireira sobre a Floresta Amazônica a Partir da Segunda Metade do Século XX; O Surgimento dos Movimentos Socioambientais: A Luta dos Seringueiros, Chico Mendes e o Conceito de Reservas Extrativistas."
ebook_fonte: "em-his-c52-historia-ambiental-brasil-ciclos-extrativistas-devastacao-biomas.md"
habilidades: "EM13CHS206, EM13CHS301, EM13CHS302, EM13CHS306"
total_exercicios: 60
distribuicao:
  basico: 20
  intermediario: 20
  dificil: 20
---

# Lista de Exercícios: História Ambiental do Brasil: Ciclos Extrativistas e a Devastação dos Biomas

## Nível Básico (Questões 1-20)
"""

    questions_basic = [
        # q01 (A)
        """<!-- id: q01 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: basico | objeto: historia-ambiental-warren-dean -->
### Questão 1
A emergência da História Ambiental, consolidada no Brasil pela obra 'A Ferro e Fogo' (1995) do historiador Warren Dean, operou uma renovação historiográfica ao:

a) Colocar a natureza e os biomas não como cenários estáticos, mas como agentes históricos dinâmicos moldados por ciclos predatórios.
b) Descrever a derrubada de florestas tropicais como uma marcha civilizatória heroica desprovida de impactos ecológicos.
c) Afirmar que a vegetação nativa brasileira permaneceu completamente intocada até a fundação de Brasília na década de 1950.
d) Defender que o cultivo colonial da cana-de-açúcar preservou a cobertura vegetal original das florestas de encosta.
e) Isolar a análise econômica das paisagens naturais, tratando as árvores como obstáculos hostis ao progresso do homem.

**Gabarito:** A

**Resolução:**
Warren Dean superou a visão tradicional ao analisar as florestas e rios como sujeitos históricos, revelando como a exploração extrativista mercantil reduziu a Mata Atlântica a fragmentos ameaçados.
""",
        # q02 (B)
        """<!-- id: q02 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: ciclo-do-pau-brasil -->
### Questão 2
Nas primeiras décadas após 1500, a exploração inicial do pau-brasil na faixa litorânea brasileira caracterizou-se pelo:

a) Plantio em viveiros agrícolas planejados para reflorestar encostas da região Sul.
b) Corte predatório contínuo da espécie para extração de resina têxtil, quase extinguindo a árvore da costa em meio século.
c) Uso exclusivo de maquinário a vapor importado de tecelagens inglesas para transportar troncos.
d) Estabelecimento de leis rigorosas que proibiam o abate de espécies arbóreas nativas da floresta tropical.
e) Boicote dos navegadores portugueses ao comércio de madeiras tintoriais na Europa.

**Gabarito:** B

**Resolução:**
O pau-brasil foi explorado de maneira rápida e predatória: sem qualquer projeto de replantio, milhares de toras foram abatidas com o trabalho tupi, sumindo da faixa costeira acessível em poucas décadas.
""",
        # q03 (C)
        """<!-- id: q03 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: cana-e-fornalhas-dos-engenhos -->
### Questão 3
Durante o ciclo da cana-de-açúcar no litoral nordestino colonial, o principal fator de devastação das matas nativas decorria:

a) Da abertura de canais artificiais de navegação para ligar plantações aos portos fluviais do interior.
b) Da instalação de cercas elétricas para impedir que animais silvestres invadissem as lavouras.
c) Do consumo colossal de lenha nativa para alimentar as fornalhas de fervura do caldo de cana nas caldeiras dos engenhos.
d) Do corte seletivo de palmeiras para fabricação de papel destinado a cartórios e mosteiros reais.
e) Da drenagem obrigatória de lagoas de água doce para criação de tanques de peixes asiáticos.

**Gabarito:** C

**Resolução:**
Cada engenho colonial era uma fornalha insaciável: além do espaço desmatado para os canaviais, queimava-se continuamente madeira das matas de encosta para aquecer caldeiras de cobre, secando rios e nascentes.
""",
        # q04 (D)
        """<!-- id: q04 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: mineracao-desmonte-hidraulico -->
### Questão 4
No século XVIII, a atividade mineradora nas Minas Gerais provocou graves danos ambientais nas bacias dos rios Doce e das Velhas por meio:

a) Da construção de usinas hidrelétricas com barragens de concreto armado nas quedas de água.
b) Da queima de combustíveis fósseis refinados como querosene e óleo diesel nas frentes de garimpo.
c) Da perfuração de poços artesianos profundos de irrigação automática para lavouras de trigo.
d) Do desmonte hidráulico das encostas com fortes jatos de água, causando desmoronamentos e assoreamento dos leitos fluviais.
e) Do despejo de defensivos químicos agrícolas sintéticos nascentes de rios montanhosos.

**Gabarito:** D

**Resolução:**
Para descolar faisqueiras e pepitas de ouro, os mineradores desviavam rios e jogavam fortes torrentes contra morros de encosta, arrastando milhões de toneladas de terra estéril que soterraram os leitos dos rios.
""",
        # q05 (E)
        """<!-- id: q05 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: cafe-lavoura-nomade-vale-paraiba -->
### Questão 5
A expansão da cafeicultura no Vale do Paraíba durante o século XIX ficou conhecida pelo método da 'lavoura nômade', que consistia em:

a) Utilizar sistemas modernos de rotação de culturas e adubação orgânica para recuperar a fertilidade da terra.
b) Manter a floresta nativa preservada nas cristas de morros para assegurar a umidade natural do café.
c) Plantar mudas em curvas de nível para evitar a perda do solo superficial durante enxurradas de verão.
d) Transferir periodicamente os pés de café em vasos cerâmicos móveis entre as diferentes estações do ano.
e) Queimar a floresta nativa, plantar morro abaixo e abandonar as terras exaustas e com crateras de erosão após algumas décadas.

**Gabarito:** E

**Resolução:**
Os cafeicultores do Vale não investiam na terra: queimavam a mata virgem, plantavam em fileiras verticais facilitando a erosão das chuvas e, quando as encostas viravam voçorocas estéreis, migravam para novas frentes.
""",
        # q06 (B)
        """<!-- id: q06 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: cidades-mortas-monteiro-lobato -->
### Questão 6
A expressão 'cidades mortas', consagrada pelo escritor Monteiro Lobato ao descrever municípios do Vale do Paraíba (como Bananal e Vassouras), refere-se:

a) A vilas portuárias que foram submersas pela subida gradual do nível do mar no litoral paulista.
b) Ao rastro de estagnação econômica, casarões abandonados e solos arruinados deixados pela passagem do ciclo cafeeiro itinerante.
c) A fortificações militares fronteiriças destruídas durante os conflitos de limites da Bacia do Prata.
d) A aldeias indígenas que foram abandonadas voluntariamente pelas comunidades após acordos de paz.
e) A centros urbanos planejados pelo império que nunca foram povoados devido à escassez de água potável.

**Gabarito:** B

**Resolução:**
Após sugar o húmus da Mata Atlântica e abrir crateras de erosão, o café migrou para a terra roxa do Oeste Paulista, deixando no Vale do Paraíba fazendas falidas, solos calcinados e cidades sem atividade econômica.
""",
        # q07 (C)
        """<!-- id: q07 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: cerrado-revolucao-verde-calagem -->
### Questão 7
A incorporação intensiva do Cerrado brasileiro à produção agrícola moderna a partir da década de 1970 foi viabilizada pelo:

a) Despejo de rejeitos de carvão mineral nas pastagens para elevar o teor de areia no solo.
b) Uso de técnicas manuais indígenas de plantio consorciado de mandioca sem aditivos químicos.
c) Desenvolvimento da técnica de calagem pela Embrapa, corrigindo a acidez natural do solo para o cultivo de soja e milho.
d) Plantio de árvores tropicais frutíferas que dispensavam o uso de água e fertilizantes minerais.
e) Retorno ao modelo de pequenas propriedades rurais de subsistência familiar com proibição de maquinário.

**Gabarito:** C

**Resolução:**
A correção da acidez do solo por meio do calcário (calagem), combinada a fertilizantes e pesquisas da Embrapa, transformou o Cerrado no polo do agronegócio de grãos, provocando a perda de metade de sua cobertura original.
""",
        # q08 (D)
        """<!-- id: q08 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: amazonia-rodovias-sudam -->
### Questão 8
Na segunda metade do século XX, durante a Ditadura Militar, o avanço da fronteira agropecuária sobre a Floresta Amazônica foi impulsionado por:

a) Tratados internacionais que proibiam a extração de madeiras de lei ao longo de cursos de rios.
b) Doações humanitárias de mudas de castanheiras distribuídas por entidades científicas da Europa.
c) Linhas de crédito bancário exclusivas para pequenas cooperativas de pesca artesanal ribeirinha.
d) Abertura de grandes eixos rodoviários (Transamazônica, Belém-Brasília) e incentivos fiscais concedidos pela SUDAM a fazendas.
e) Criação imediata de parques florestais intocados em todas as margens de rodovias federais.

**Gabarito:** D

**Resolução:**
Sob a justificativa de integrar o território, o governo abriu rodovias na mata e ofereceu renúncias fiscais pela SUDAM para grupos empresariais limparem a floresta com queimadas para criar gado de corte.
""",
        # q09 (E)
        """<!-- id: q09 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: rios-voadores-amazonia -->
### Questão 9
O fenômeno ecológico e climático conhecido como 'Rios Voadores' consiste no:

a) Escoamento de águas subterrâneas que brotam em cavernas cársticas do sertão nordestino.
b) Transporte de sedimentos minerais pesados arrastados por tempestades de poeira do planalto central.
c) Deslocamento de bandos de aves migratórias que viajam da Patagônia até os manguezais do Maranhão.
d) Curso navegável de rios de águas barrentas que cortam as florestas alagadas de várzea do Amazonas.
e) Fluxo aéreo de massas de vapor geradas pela transpiração da Amazônia, levando chuvas para o Centro-Oeste e Sudeste.

**Gabarito:** E

**Resolução:**
As árvores da Amazônia bombeiam diariamente bilhões de litros de vapor para a atmosfera; essa umidade viaja pelos ares, bate nos Andes e desce para o Sudeste, irrigando lavouras e enchendo reservatórios de usinas.
""",
        # q10 (A)
        """<!-- id: q10 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: chico-mendes-seringueiros -->
### Questão 10
Na década de 1980, no Acre, o líder sindical Chico Mendes destacou-se nacional e internacionalmente por:

a) Liderar a resistência pacífica das famílias de seringueiros contra o desmatamento da floresta por fazendeiros grileiros.
b) Comandar empresas madeireiras privadas que exportavam toras de mogno para os Estados Unidos.
c) Recomendar a queima de seringais nativos para implantar monoculturas irrigadas de soja no vale do rio Acre.
d) Assinar decretos municipais proibindo a coleta tradicional de castanha-do-brasil por comunidades ribeirinhas.
e) Financiar a abertura de estradas vicinais de terra para o escoamento rápido de rebanhos bovinos de corte.

**Gabarito:** A

**Resolução:**
Chico Mendes presidiu o Sindicato de Xapuri e organizou comunidades que viviam da borracha e da castanha sem derrubar a mata, unindo a bandeira dos direitos trabalhistas à preservação ambiental.
""",
        # q11 (C)
        """<!-- id: q11 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: os-empates-xapuri -->
### Questão 11
A técnica de ação direta não violenta desenvolvida pelos seringueiros acreanos, conhecida como 'empate', caracterizava-se por:

a) Realizar greves de fome no interior de agências bancárias nas capitais dos estados vizinhos.
b) Incendiar os veículos oficiais de fiscais sanitários responsáveis pelo controle de vacinas rurais.
c) Homens, mulheres e crianças postarem-se desarmados diante de motosserras para convencer peões a parar o desmate.
d) Construir barricadas com pedras dinamitadas para interromper o fluxo de balsas nos rios navegáveis.
e) Pagar indenizações em dinheiro aos capatazes das fazendas para atrasar o abate de castanheiras centenárias.

**Gabarito:** C

**Resolução:**
Nos empates, as famílias colocavam seus próprios corpos na frente das motosserras e dialogavam com os peões, explicando que a derrubada da floresta destruiria a subsistência de ambos os lados, salvando milhares de hectares.
""",
        # q12 (D)
        """<!-- id: q12 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: alianca-povos-da-floresta -->
### Questão 12
Criada em 1985 com a participação de Chico Mendes e lideranças indígenas como Ailton Krenak, a Aliança dos Povos da Floresta representou:

a) Um acordo de venda de direitos de exploração mineral exclusiva para refinarias estatais de petróleo.
b) A dissolução de reservas demarcadas para transformá-las em loteamentos urbanos residenciais abertos.
c) A criação de cooperativas agrícolas destinadas a introduzir o plantio de cana-de-açúcar na Amazônia ocidental.
d) A superação de conflitos históricos para unir seringueiros e povos originários na defesa comum da floresta viva.
e) Um pacto de desarmamento geral de comunidades para facilitar a compra de terras por pecuaristas paulistas.

**Gabarito:** D

**Resolução:**
A aliança quebrou séculos de disputas fomentadas pelos patrões da borracha, unindo índios e seringueiros na percepção de que compartilhavam o mesmo destino e a mesma necessidade de manter a floresta em pé.
""",
        # q13 (E)
        """<!-- id: q13 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: conceito-resex-chico-mendes -->
### Questão 13
O modelo de Reserva Extrativista (RESEX), idealizado pelo movimento socioambientalista e formalizado na legislação brasileira, caracteriza-se por:

a) Áreas onde toda atividade econômica humana é proibida e a população tradicional é removida para cidades.
b) Terrenos privados doados a grandes frigoríficos para confinamento e abate de gado bovino selecionado.
c) Parques estaduais de lazer voltados unicamente à construção de resorts e campos de golfe para turistas.
d) Loteamentos rurais onde os camponeses recebem títulos definitivos de posse individual para revenda livre.
e) Terras públicas de posse coletiva concedidas a populações tradicionais para manejo sustentável e preservação da mata.

**Gabarito:** E

**Resolução:**
A grande sacada das RESEX foi superar o mito da 'natureza intocada': a floresta é preservada justamente porque os povos tradicionais vivem nela, colhendo castanha, borracha e açaí sem destruir o ecossistema.
""",
        # q14 (A)
        """<!-- id: q14 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: basico | objeto: percentual-restante-mata-atlantica -->
### Questão 14
Da cobertura florestal original da Mata Atlântica, que cobria mais de um milhão e trezentos mil quilômetros quadrados da costa brasileira, estima-se que restem hoje:

a) Menos de 12% da área original, fragmentada em ilhas de mata cercadas por lavouras, pastagens e cidades.
b) Mais de 85% de florestas contínuas e intocadas nas planícies do planalto paulista e mineiro.
c) Aproximadamente a metade exata da cobertura registrada nas cartas de navegação de 1500.
d) Apenas árvores plantadas artificialmente em calçadas de capitais do Nordeste por paisagistas modernos.
e) Quase 70% de matas primárias protegidas integralmente por cercamentos de metal em fazendas privadas.

**Gabarito:** A

**Resolução:**
A Mata Atlântica é o bioma brasileiro mais devastado: após sucessivos ciclos de pau-brasil, açúcar, mineração, café e expansão urbana metropolitana, sobrou pouco mais de 10% de sua cobertura primitiva.
""",
        # q15 (B)
        """<!-- id: q15 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: assassinato-chico-mendes-1988 -->
### Questão 15
O assassinato de Chico Mendes em dezembro de 1988, em Xapuri, teve como desdobramento político e ecológico internacional:

a) O cancelamento de todas as comissões de direitos humanos que operavam em capitais da América do Sul.
b) Uma comoção global que forçou o governo a criar as primeiras Reservas Extrativistas oficiais na Amazônia.
c) A paralisação definitiva do comércio de calçados de couro e pneus de borracha sintética no Brasil.
d) A retirada imediata de todos os povos indígenas das bacias do rio Juruá para aldeamentos costeiros.
e) O fechamento de todas as estações de pesquisa biológica instaladas no interior da floresta acreana.

**Gabarito:** B

**Resolução:**
A morte violenta de Chico Mendes gerou indignação mundial na imprensa e na ONU; o governo brasileiro foi empurrado a sancionar a figura legal das RESEX, começando pela criação da grandiosa Reserva Chico Mendes.
""",
        # q16 (D)
        """<!-- id: q16 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: erosao-vocorocas-vale-paraiba -->
### Questão 16
O processo de abertura de profundas crateras erosivas nas encostas do Vale do Paraíba durante o século XIX, conhecidas como voçorocas, foi provocado por:

a) Movimentos tectônicos intensos e terremotos que abalaram as serras do Mar e da Mantiqueira.
b) Desvios voluntários de canais subterrâneos realizados por técnicos de companhias de eletricidade.
c) Perfuração de galerias subterrâneas profundas para mineração de ouro e pedras coradas.
d) Retirada da cobertura florestal original e plantio de café em linhas verticais morro abaixo expostas a chuvas fortes.
e) Passagem frequente de manadas de elefantes e animais de grande porte em trilhas de tropeiros.

**Gabarito:** D

**Resolução:**
Sem as copas das árvores para amortecer a água e sem as raízes para segurar a terra, as torrentes de chuva rasgavam os morros plantados com café, abrindo fendas gigantescas que levaram à perda total do solo fértil.
""",
        # q17 (E)
        """<!-- id: q17 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: cerrado-caixa-dagua -->
### Questão 17
O Cerrado brasileiro é comumente denominado por geógrafos e ambientalistas como a 'caixa-d'água do Brasil' porque:

a) Suas cidades industriais concentram as maiores estações de tratamento de esgoto doméstico do país.
b) Abriga os maiores reservatórios artificiais de água potável canalizada construídos pela engenharia civil.
c) Suas árvores de troncos grossos retêm chuva em tanques naturais escavados nos galhos pelas aves.
d) Suas pastagens de capim braquiária absorvem umidade do mar e transportam para o interior do país.
e) Em seus planaltos nascem os rios e afluentes que alimentam as principais bacias hidrográficas nacionais.

**Gabarito:** E

**Resolução:**
O relevo alto e o solo permeável do Cerrado recarregam aquíferos vitais que abastecem nascentes das três grandes bacias da América do Sul: a Amazônica, a do rio São Francisco e a bacia Platina.
""",
        # q18 (A)
        """<!-- id: q18 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: basico | objeto: mito-da-natureza-inesgotavel -->
### Questão 18
A historiografia ambiental desmistificou a crença colonial e imperial de que a natureza brasileira era inesgotável, demonstrando que:

a) Os recursos naturais são finitos e os ciclos agrícolas predatórios geraram colapsos locais de solos e bacias hídricas.
b) A floresta tropical tem capacidade ilimitada de regenerar sua copa mesmo quando queimada seguidas vezes.
c) A fauna silvestre nativa cresce com mais vigor quando as florestas de encosta são derrubadas para pastos.
d) As secas e enchentes são eventos puramente meteorológicos desvinculados de qualquer intervenção humana.
e) O solo tropical de massapê e argila dispensa adubações porque renova seus nutrientes minerais a cada primavera.

**Gabarito:** A

**Resolução:**
A ideia de um paraíso infinito e intocado serviu de justificativa para saquear a terra sem investir em conservação, gerando crises de abastecimento de madeira, água e alimentos nas regiões mais ricas do país.
""",
        # q19 (B)
        """<!-- id: q19 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: grilagem-amazonia-queimadas -->
### Questão 19
Na dinâmica histórica da expansão da fronteira na Amazônia, a prática da 'grilagem de terras' esteve frequentemente associada a:

a) Doação de pequenas propriedades tituladas para famílias de pescadores ribeirinhos sem terra.
b) Falsificação de títulos de terras públicas florestais, corte de madeiras nobres e queima da vegetação para pasto.
c) Preservação permanente de santuários ecológicos custeados por doações de proprietários de frigoríficos.
d) Assinatura de tratados de proteção biológica com órgãos ambientais do governo federal.
e) Desapropriação de fazendas de gado para reflorestamento compulsório com castanheiras e seringueiras nativas.

**Gabarito:** B

**Resolução:**
Grileiros forjavam papéis de propriedade de terras da União, invadiam florestas públicas, vendiam as madeiras mais valiosas (mogno, cedro) e ateavam fogo na mata para colocar gado e consolidar a posse ilegal da terra.
""",
        # q20 (C)
        """<!-- id: q20 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: socioambientalismo-conceito -->
### Questão 20
O conceito de Socioambientalismo, formulado nos debates ecológicos brasileiros das décadas de 1970 e 1980, diferencia-se do ambientalismo tradicional porque:

a) Recomenda a destruição da floresta nativa para criar postos de emprego na extração mineral mecanizada.
b) Defende que a preservação de florestas tropicais deve ser realizada unicamente por forças militares armadas.
c) Articula a proteção da natureza com a garantia da justiça social, dos direitos territoriais e da cultura dos povos da floresta.
d) Proíbe qualquer forma de aproveitamento econômico sustentável de frutos, sementes e seivas de árvores nativas.
e) Considera que a preservação ambiental só é possível em países industrializados com clima temperado frio.

**Gabarito:** C

**Resolução:**
O socioambientalismo não separa a árvore do ser humano: ele reconhece que os povos que habitam a floresta há gerações (indígenas, seringueiros, quilombolas) são seus melhores guardiões quando têm seus direitos e terras garantidos.
"""
    ]

    questions_inter = [
        # q21 (D)
        """<!-- id: q21 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: intermediario | objeto: analise-tese-warren-dean -->
### Questão 21
Em A Ferro e Fogo, Warren Dean descreve a destruição da Mata Atlântica como um processo em que 'a cada ciclo econômico, o invasor humano tratou a floresta como um capital natural a ser liquidado e convertido em riqueza imediata'. Essa tese contrapõe-se diretamente à narrativa de que:

a) Os barões do café no Vale do Paraíba praticavam o corte raso de matas nativas morro abaixo.
b) As fornalhas dos engenhos coloniais consumiam grandes extensões de lenha silvestre do litoral nordestino.
c) Os desvios de cursos de água e desmontes hidráulicos na mineração causaram assoreamento nos rios de Minas Gerais.
d) A colonização representou uma evolução harmônica em que o progresso civilizatório preservou a estabilidade dos biomas.
e) As populações indígenas utilizavam o fogo de forma controlada em roçados itinerantes de mandioca.

**Gabarito:** D

**Resolução:**
Dean desfaz o mito da ocupação benigna: a riqueza gerada pelo açúcar, ouro e café foi construída mediante a queima e liquidação irreversível do patrimônio biológico, deixando solos empobrecidos e bacias hídricas mutiladas.
""",
        # q22 (E)
        """<!-- id: q22 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: intermediario | objeto: cana-vs-solos-massape -->
### Questão 22
A expansão dos canaviais nos solos de massapê da Zona da Mata nordestina durante os séculos XVI e XVII gerou desequilíbrios ambientais duradouros porque:

a) Estimulou a plantação compulsória de cafeeiros nas faixas litorâneas sujeitas a maresia salina.
b) Introduziu o cultivo de trigo irrigado por bacias de decantação que salinizaram as águas doces.
c) Obrigou os senhores de engenho a construir represas de concreto para desviar cursos fluviais navegáveis.
d) Desestimulou o transporte marítimo de mercadorias em benefício de estradas pavimentadas de rodagem.
e) Suprimiu florestas ciliares e manguezais protetores, reduzindo a umidade local e provocando a lixiviação acelerada de nutrientes.

**Gabarito:** E

**Resolução:**
O corte raso da floresta até as margens dos rios e praias expôs o solo fértil mas frágil às chuvas tropicais violentas; sem a retenção das copas, as águas lavaram os nutrientes, assorearam estuários e secaram riachos.
""",
        # q23 (A)
        """<!-- id: q23 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: mineracao-ouro-pretendido-florestas -->
### Questão 23
A atividade mineradora no século XVIII em Minas Gerais impactou não apenas os rios, mas também a cobertura florestal da região porque:

a) Exigia gigantescas quantidades de madeira para escoramento de túneis em galerias e carvão vegetal para forjas e cozinhas.
b) Proibia a população de recolher gravetos caídos no solo sob pena de expulsão das capitanias hereditárias.
c) Forçava os tropeiros a plantar eucaliptos exóticos para marcar as divisas de lavras concedidas pela coroa.
d) Substituiu as árvores nativas por vinhedos mediterrâneos para abastecer as tropas da intendência real.
e) Impediu a utilização de tração animal nas estradas para não compactar o chão de terra das vilas mineiras.

**Gabarito:** A

**Resolução:**
A mineração era uma consumidora voraz de madeira: galerias profundas demandavam troncos grossos para evitar desabamentos de terra, e as cidades populosas de Ouro Preto e Mariana demandavam lenha diária para fogões e metalurgia.
""",
        # q24 (B)
        """<!-- id: q24 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: monocultura-cafeeira-versus-conservacao -->
### Questão 24
Ao analisar o colapso ambiental do Vale do Paraíba no final do século XIX, os agrônomos da época constataram que a recusa dos fazendeiros em adotar adubações ou terraços decorria:

a) Da escassez absoluta de mão de obra escravizada nas fazendas de café do Rio de Janeiro.
b) Da lógica econômica da época, segundo a qual era mais barato comprar novas terras virgens no interior do que recuperar solos esgotados.
c) De decretos imperiais que proibiam o plantio de leguminosas fixadoras de nitrogênio nas encostas.
d) Do alto preço do frete das ferrovias que ligavam as plantações serranas ao porto de Santos.
e) Da concorrência desleal provocada pela exportação de café em grãos cultivado nas ilhas do Caribe.

**Gabarito:** B

**Resolução:**
A abundância aparente de fronteiras abertas no Oeste Paulista estimulava a rapina: enquanto houvesse matas virgens à disposição para queimar e plantar com mão de obra escrava, cuidar da terra parecia um gasto inútil aos cafeicultores.
""",
        # q25 (C)
        """<!-- id: q25 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: cerrado-e-pivo-central-agua -->
### Questão 25
A intensa exploração agrícola do Cerrado por meio de sistemas mecanizados de irrigação por pivô central e monoculturas de soja gerou preocupações ecológicas crescentes devido:

a) Ao aumento das geadas invernais severas que destruíram plantações de maçãs nas chapadas centrais.
b) À expansão descontrolada de florestas de araucária sobre as pastagens cultivadas de capim braquiária.
c) Ao rebaixamento acelerado do lençol freático e à redução das vazões de rios formadores das bacias do Prata e São Francisco.
d) À proibição de tráfego de caminhões graneleiros nas rodovias federais durante os meses de colheita.
e) À contaminação generalizada dos solos por resíduos de petróleo vazados de dutos industriais litorâneos.

**Gabarito:** C

**Resolução:**
O Cerrado funciona como esponja que absorve a chuva e abastece aquíferos subterrâneos; poços profundos e pivôs de irrigação retiram mais água do que o solo consegue repor, diminuindo o fluxo de rios vitais para o país.
""",
        # q26 (E)
        """<!-- id: q26 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: integracao-militar-amazonia-tipping-point -->
### Questão 26
O projeto geopolítico da Ditadura Militar para a Amazônia resumiu-se na palavra de ordem 'Integrar para não entregar'. Do ponto de vista ambiental contemporâneo, esse modelo é criticado porque:

a) Concedeu autonomia administrativa plena às nações indígenas para demarcar territórios soberanos invioláveis.
b) Financiou pesquisas biomédicas independentes para proteger plantas medicinais raras de laboratórios privados.
c) Impediu que grupos econômicos do Sudeste comprassem títulos de terras ao longo de rodovias federais.
d) Destinou verbas orçamentárias exclusivamente à restauração ecológica de matas de igapó degradadas por enchentes.
e) Estimulou a substituição da cobertura vegetal nativa por pecuária extensiva de baixa produtividade, aproximando o bioma do ponto de não retorno.

**Gabarito:** E

**Resolução:**
O lema militar enxergava a floresta densa como um 'vazio demográfico' perigoso; derrubá-la para colocar bois foi incentivado com dinheiro público, levando à perda de biodiversidade e à ameaça de savanização do bioma.
""",
        # q27 (A)
        """<!-- id: q27 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: empates-estrategia-social -->
### Questão 27
A originalidade dos 'empates' organizados por Chico Mendes e pelas famílias de seringueiros residiu no fato de que o movimento:

a) Uniu mulheres, crianças e homens desarmados na defesa física das árvores, transformando conflitos fundiários em debates morais perante a opinião pública.
b) Organizou milícias armadas clandestinas que explodiam caminhões de abastecimento de combustíveis nas cidades vizinhas.
c) Buscou o apoio exclusivo de fazendeiros paulistas para expulsar comunidades indígenas de áreas de coleta de castanha.
d) Recusou qualquer contato com entidades internacionais para evitar que governos estrangeiros soubessem dos desmatamentos.
e) Exigiu a transferência compulsória de todos os trabalhadores rurais para postos de trabalho em indústrias da Zona Franca de Manaus.

**Gabarito:** A

**Resolução:**
Ao colocar famílias inteiras de mãos dadas abraçadas a castanheiras e conversar com os peões, o movimento seringueiro desarmava os pistoleiros pela força moral da não violência, ganhando repercussão nos jornais e na ONU.
""",
        # q28 (B)
        """<!-- id: q28 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: resex-vs-unidades-preservacao-integral -->
### Questão 28
Ao comparar o modelo de Reserva Extrativista (RESEX) com os Parques Nacionais de Preservação Integral, identifica-se uma diferença conceitual decisiva:

a) As RESEX permitem a instalação de indústrias químicas pesadas de fertilizantes no interior da mata nativa.
b) Os Parques de Preservação Integral vedam a moradia e o uso direto de recursos, enquanto as RESEX integram a presença humana ao manejo sustentável.
c) As RESEX autorizam a venda definitiva de lotes de floresta para grupos empresariais do agronegócio de corte.
d) Os Parques Nacionais exigem que os visitantes comprovem residência na região amazônica para obter autorização de entrada.
e) As RESEX cobram mensalidades dos povos indígenas para permitir a coleta tradicional de sementes e raízes medicinais.

**Gabarito:** B

**Resolução:**
O modelo clássico importado dos EUA (Parques Nacionais) expulsava populações nativas por considerá-las invasoras; a inovação brasileira da RESEX reconheceu que os povos da floresta são seus melhores protetores ao usá-la sem destruí-la.
""",
        # q29 (C)
        """<!-- id: q29 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: intermediario | objeto: extrativismo-mineral-mercurio-rios -->
### Questão 29
A mineração de ouro no leito de rios tropicais — tanto no século XVIII quanto nos garimpos contemporâneos na Amazônia — deixa sequelas ambientais graves porque:

a) Utiliza grandes quantidades de sal marinho que esterilizam a vegetação das várzeas e campos úmidos.
b) Provoca a evaporação instantânea da água doce dos afluentes ao elevar artificialmente a temperatura das correntes.
c) Recorre ao mercúrio líquido para amalgamar o metal precioso, contaminando águas e acumulando veneno na cadeia alimentar dos peixes.
d) Exige a construção de canais de concreto que impedem a reprodução de répteis e quelônios em praias fluviais.
e) Obriga as comunidades vizinhas a consumir exclusivamente enlatados importados por falta de rotas de navegação.

**Gabarito:** C

**Resolução:**
O mercúrio liga-se às partículas de ouro e é queimado com maçarico; resíduos tóxicos caem na água e transformam-se em metilmercúrio, acumulando-se nos peixes e causando danos neurológicos permanentes em populações ribeirinhas e indígenas.
""",
        # q30 (D)
        """<!-- id: q30 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: oeste-paulista-terra-roxa -->
### Questão 30
Após a ruína das fazendas de café no Vale do Paraíba, a marcha da cafeicultura rumo ao Oeste Paulista (Campinas, Ribeirão Preto) caracterizou-se por:

a) Abandonar as ferrovias para transportar toda a safra em lombo de mulas por caminhos serranos íngremes.
b) Retomar as técnicas de cultivo em encostas de morros pedregosos com adubação manual indígena de cinzas.
c) Abolir a derrubada de matas virgens por meio da compra exclusiva de pastos degradados de gado zebu.
d) Encontrar solos de terra roxa basáltica mais planos e férteis, acelerando a substituição da floresta sem solucionar a lógica predatória.
e) Dividir os latifúndios em minifúndios de policultura voltados unicamente ao abastecimento dos mercados de bairro.

**Gabarito:** D

**Resolução:**
A terra roxa de origem vulcânica do interior paulista era muito mais fértil e plana que os morros do Vale, permitindo lucros gigantescos com o café e trens; contudo, a mentalidade extrativista persistiu, varrendo a floresta original do interior de São Paulo.
""",
        # q31 (A)
        """<!-- id: q31 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: rios-voadores-e-agronegocio -->
### Questão 31
A preservação da Floresta Amazônica é descrita por climatologistas como um interesse vital do próprio agronegócio brasileiro porque:

a) O desmatamento quebra o ciclo dos Rios Voadores, reduzindo as chuvas que irrigam as safras de grãos do Centro-Oeste e do Sudeste.
b) As árvores de grande porte impedem a passagem de pragas agrícolas que atacam lavouras de trigo nos planaltos gaúchos.
c) A umidade da mata atrai insetos polinizadores que fertilizam pastagens de gramíneas cultivadas para gado leiteiro.
d) A floresta tropical consome o excesso de chuva que causaria inundações permanentes nas plantações de cana de Ribeirão Preto.
e) O solo amazônico fornece calcário de boa qualidade utilizado na correção de nutrientes de fazendas do Cerrado.

**Gabarito:** A

**Resolução:**
A Amazônia atua como um coração hídrico: sem ela, a umidade vinda do oceano não recircula para o interior; secar a floresta significa condenar as principais regiões agrícolas e geradoras de energia do país a estiagens severas.
""",
        # q32 (B)
        """<!-- id: q32 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: ailton-krenak-alianca-floresta -->
### Questão 32
A participação de lideranças indígenas como Ailton Krenak na fundação da Aliança dos Povos da Floresta em 1985 expressou:

a) A concordância dos povos originários em ceder suas terras demarcadas para projetos de mineração industrial privada.
b) O entendimento compartilhado de que a luta pela terra e a conservação da biodiversidade exigiam ação política unificada entre povos tradicionais.
c) A decisão de abandonar línguas nativas em favor do uso exclusivo de dialetos caboclos seringueiros nas assembleias.
d) A aceitação pacífica das diretrizes governamentais de transferência de comunidades para cidades vizinhas a hidrelétricas.
e) A recusa em dialogar com entidades internacionais de defesa dos direitos humanos e de conservação da natureza.

**Gabarito:** B

**Resolução:**
Krenak e Mendes perceberam que o latifúndio e a grilagem destruíam tanto a aldeia indígena quanto a colocação seringueira; ao unirem suas vozes, criaram uma força política que ecoou na Constituinte de 1988 e no mundo.
""",
        # q33 (C)
        """<!-- id: q33 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: intermediario | objeto: fragmentacao-mata-atlantica-efeito-borda -->
### Questão 33
A fragmentação da Mata Atlântica em pequenas manchas florestais isoladas cercadas por cidades e lavouras gera o chamado 'efeito de borda', caracterizado por:

a) Aceleração do crescimento de árvores centenárias no interior dos fragmentos protegidos por cercas metálicas.
b) Redução imediata da temperatura do ar e aumento das chuvas torrenciais na área central dos remanescentes de mata.
c) Maior penetração de ventos, perda de umidade e maior vulnerabilidade a incêndios e invasão de espécies exóticas nas bordas.
d) Impossibilidade de circulação de animais carnívoros em rodovias que cruzam as serras litorâneas.
e) Expansão do cultivo de espécies nativas de palmito-juçara em áreas de pastagem abandonada.

**Gabarito:** C

**Resolução:**
Mata dividida não é mata preservada: as bordas dos fragmentos ressecam com facilidade, sofrem com a luz solar excessiva e ventos secos, facilitando queimadas e impedindo que grandes mamíferos e aves circulem para se reproduzir.
""",
        # q34 (D)
        """<!-- id: q34 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: pecuaria-extensiva-baixa-produtividade -->
### Questão 34
O modelo de pecuária bovina implantado na Amazônia a partir dos anos 1970 é considerado ecologicamente insustentável sobretudo porque:

a) Exige a construção de galpões refrigerados para proteger os rebanhos das chuvas torrenciais de verão.
b) Requer alimentação exclusiva com rações importadas de cereais cultivados em países de clima frio.
c) Emprega grande número de trabalhadores especializados com altos salários pagos em moeda estrangeira.
d) Desmata milhares de hectares de floresta rica em biodiversidade para manter uma densidade baixa de cabeças de gado por hectare.
e) Reduz a fertilidade dos rios de várzea ao canalizar as águas para bebedouros de alvenaria em confinamentos.

**Gabarito:** D

**Resolução:**
Derruba-se uma floresta com milhares de espécies por hectare para colocar menos de um boi por hectare em capim que perde nutrientes em poucos anos; é a destruição de uma riqueza ecológica colossal para um ganho agropecuário efêmero.
""",
        # q35 (E)
        """<!-- id: q35 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: constituicao-1988-artigo-225 -->
### Questão 35
O Artigo 225 da Constituição Federal de 1988 representou uma conquista histórica do movimento socioambiental brasileiro ao estabelecer que:

a) O desmatamento de florestas públicas é livre desde que os lucros sejam aplicados em empresas siderúrgicas estatais.
b) Os povos indígenas e seringueiros devem pagar tributos territoriais sobre as castanheiras e seringais que manejam.
c) As empresas mineradoras estão desobrigadas de recuperar áreas degradadas após o término de suas concessões portuárias.
d) O direito à propriedade privada de terras florestais é soberano e anula qualquer regra de zoneamento ecológico público.
e) Todos têm direito ao meio ambiente ecologicamente equilibrado, bem de uso comum do povo, cabendo ao Poder Público e à coletividade o dever de defendê-lo.

**Gabarito:** E

**Resolução:**
O constituinte de 1988 acolheu as reivindicações de Chico Mendes e dos movimentos ecológicos: o meio ambiente equilibrado virou direito fundamental de todos os brasileiros, impondo ao Estado e à sociedade a obrigação de guardá-lo para as futuras gerações.
""",
        # q36 (B)
        """<!-- id: q36 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: intermediario | objeto: coivara-indigena-vs-queimada-colonial -->
### Questão 36
Ao analisar o uso do fogo na história do Brasil, os historiadores ambientais diferenciam a 'coivara' tradicional indígena das queimadas comerciais dos engenhos e fazendas de café porque:

a) A coivara indígena utilizava derivados de petróleo para queimar morros inteiros em poucos dias de estiagem.
b) A coivara indígena operava em pequena escala, com roçados móveis de subsistência e longos períodos de pousio que permitiam a recuperação da mata.
c) As queimadas dos engenhos preservavam as árvores maiores e os animais de grande porte para fins de ecoturismo colonial.
d) O fogo indígena destruiu completamente as florestas de restinga da costa leste antes da chegada das caravelas portuguesas.
e) As fazendas de café queimavam apenas capins secos e folhas mortas, preservando as copas das árvores da Mata Atlântica.

**Gabarito:** B

**Resolução:**
O indígena abria pequenos clareiras para mandioca, queimava galhos baixos e, após duas colheitas, mudava de local deixando a floresta se recompor por décadas; o colonizador queimava áreas contínuas gigantescas para monocultura comercial até o esgotamento total.
""",
        # q37 (C)
        """<!-- id: q37 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: cafe-linhas-verticais-morro-abaixo -->
### Questão 37
O plantio de café em linhas retas verticais descendo os morros do Vale do Paraíba, em vez de curvas de nível, foi adotado pelos fazendeiros oitocentistas com a finalidade de:

a) Proteger as raízes dos arbustos contra infestações de fungos subterrâneos e formigas saúvas.
b) Facilitar o transporte de café em embarcações movidas a vapor diretamente nas calhas das montanhas.
c) Facilitar a fiscalização e a vigilância dos capatazes sobre os escravizados que trabalhavam no eito da colheita.
d) Cumprir instruções de manuais agronômicos franceses que recomendavam o escoamento rápido de enxurradas.
e) Impedir que as águas das chuvas de verão penetrassem nas fendas profundas das pedreiras vizinhas.

**Gabarito:** C

**Resolução:**
A disposição em linhas retas morro abaixo tinha motivação de controle social: os feitores posicionavam-se no topo ou na base do morro e enxergavam todos os trabalhadores escravizados alinhados; o custo ecológico foi acelerar a erosão torrencial da terra.
""",
        # q38 (D)
        """<!-- id: q38 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: bid-chico-mendes-denuncia -->
### Questão 38
Em 1987, Chico Mendes viajou aos Estados Unidos e reuniu-se com diretores do Banco Interamericano de Desenvolvimento (BID) e do Congresso norte-americano para:

a) Solicitar empréstimos bancários para instalar serrarias de grande porte na bacia do rio Purus.
b) Pedir a compra de cotas de café brasileiro pelas redes de lanchonetes de fast-food americanas.
c) Recomendar o fechamento de postos médicos rurais que atendiam famílias de posseiros e seringueiros.
d) Denunciar que financiamentos internacionais à pavimentação de rodovias na Amazônia (BR-364) estavam provocando desmatamento e violência contra populações locais.
e) Propor a venda de títulos de terras públicas florestais para fundos de pensão de empresas automobilísticas.

**Gabarito:** D

**Resolução:**
Chico Mendes levou a voz dos povos da floresta ao coração financeiro de Washington: provou que o asfalto financiado por bancos sem garantias territoriais para os seringueiros trazia apenas grilagem, queimadas e assassinatos, suspendendo desembolsos do BID.
""",
        # q39 (E)
        """<!-- id: q39 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: savanizacao-amazonia -->
### Questão 39
O conceito científico de 'ponto de não retorno' (tipping point) aplicado à Floresta Amazônica refere-se ao momento crítico em que o desmatamento acumulado pode:

a) Estimular o surgimento espontâneo de geleiras nas encostas orientais da Cordilheira dos Andes.
b) Aumentar as temperaturas médias do oceano Atlântico a ponto de provocar furacões no litoral paulista.
c) Forçar as populações ribeirinhas a adotar o plantio mecanizado de trigo em ilhas de várzea fluviais.
d) Reduzir o volume de sedimentos transportados pelo rio Amazonas em direção à plataforma continental.
e) Alterar o ciclo de chuvas regionais de tal forma que a floresta perca a capacidade de se sustentar, convertendo-se em savana degradada.

**Gabarito:** E

**Resolução:**
A floresta produz cerca de metade da chuva que cai sobre ela por meio da evapotranspiração; se a cobertura cair além de 20% a 25%, o ciclo quebra, o clima regional seca e a floresta tropical úmida começa a secar e queimar espontaneamente.
""",
        # q40 (A)
        """<!-- id: q40 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: intermediario | objeto: licoes-da-historia-ambiental -->
### Questão 40
A principal lição deixada pela História Ambiental do Brasil para o planejamento econômico e social do século XXI reside na compreensão de que:

a) O crescimento econômico que destrói as bases ecológicas da vida gera riqueza efêmera e crises hídricas e climáticas duradouras.
b) Os ciclos agrícolas extrativistas devem ser mantidos sem regulação estatal porque o mercado equilibra a natureza.
c) A substituição de florestas tropicais por pastagens de gado garante a segurança alimentar perpétua de todo o país.
d) O avanço sobre novos biomas é inevitável para compensar a perda de fertilidade de solos agrícolas arruinados.
e) As comunidades tradicionais que vivem nas florestas representam entraves que precisam ser removidos para o progresso da nação.

**Gabarito:** A

**Resolução:**
A história prova que o modelo predatório esgota a si próprio: arruinou o Vale do Paraíba, fragmentou a Mata Atlântica e ameaça o Cerrado e a Amazônia; sem conservação ecológica e justiça social, não há futuro econômico viável.
"""
    ]

    questions_hard = [
        # q41 (C)
        """<!-- id: q41 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: dificil | objeto: tese-warren-dean-mata-atlantica -->
### Questão 41
Na obra A Ferro e Fogo: A História e a Devastação da Mata Atlântica Brasileira (1995), o historiador norte-americano Warren Dean constrói uma narrativa ecológica detalhada que desmistifica a visão tradicional da colonização como um processo civilizatório e triunfal. Ao investigar as forças estruturais que aceleraram o ecocídio da floresta tropical ao longo de quinhentos anos, Dean demonstra que a destruição:

a) Ocorreu exclusivamente após o início da implantação das primeiras montadoras de automóveis no ABC paulista na década de 1950.
b) Resultou de um plano florestal metódico formulado por engenheiros agrônomos da Coroa portuguesa com foco em reflorestamento.
c) Foi movida pela lógica mercantil colonial e imperial que tratava a biomassa florestal e a terra como bens gratuitos a serem liquidados para lucro imediato.
d) Decorreu das práticas agrícolas dos povos indígenas tupis, que esgotaram a fertilidade do solo litorâneo antes da chegada das caravelas.
e) Teve como causa determinante a queima de madeira para a geração de energia elétrica em ferrovias da capital federal.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** Dean analisa a inserção do Brasil no sistema-mundo moderno como fornecedor de matérias-primas e gêneros agrícolas tropicais de exportação para as metrópoles europeias.
- **Etapa 2:** Sob a lógica colonial e escravista, a exuberante floresta atlântica não era valorizada por seus serviços ecológicos ou biodiversidade; era vista como madeira de queima e solo virgem gratuito que podia ser pilhado sem investimentos em conservação.
- **Etapa 3:** A sucessão predatória de monoculturas itinerantes (cana, mineração, café) operou a liquidação de mais de 88% do bioma original, transferindo o capital natural para centros metropolitanos e deixando para trás bacias desmatadas e erosão.
""",
        # q42 (D)
        """<!-- id: q42 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: dificil | objeto: caldeiras-de-engenho-voracidade-energetica -->
### Questão 42
Ao examinar o impacto ecológico da agroindústria açucareira nos séculos XVI e XVII no litoral nordestino, os historiadores ambientais apontam que o verdadeiro motor da devastação da Mata Atlântica na Zona da Mata não foi apenas a abertura dos canaviais, mas a voracidade energética das caldeiras dos engenhos. Esse processo caracterizou-se concretamente por:

a) Despejar defensivos químicos sintéticos em mananciais de água doce, esterilizando as lagoas costeiras de Olinda.
b) Utilizar óleo de baleia importado de frotas escandinavas para movimentar as turbinas hidráulicas das moendas de pedra.
c) Exigir que as populações de colonos construíssem barragens de concreto armado nas corredeiras dos rios Capibaribe e Beberibe.
d) Consumir milhares de metros cúbicos de lenha nativa diária para manter as fornalhas de cozimento do melaço, dizimando florestas de encosta e secando nascentes.
e) Queimar derivados de carvão mineral de pedreiras do interior para aquecer os fornos de secagem do açúcar refinado.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** A produção do açúcar demandava um ciclo ininterrupto de purificação do caldo de cana, que precisava ferver por horas em tachos e caldeiras de cobre para atingir o ponto de cristalização.
- **Etapa 2:** A única fonte de energia térmica disponível na colônia era a madeira das matas nativas; cada engenho consumia áreas gigantescas de florestas ao longo do ano, obrigando escravizados a desbravar matas cada vez mais distantes.
- **Etapa 3:** O desmatamento para lenha provocou o recuo das florestas de encosta, a morte de nascentes hídricas e o soterramento de manguezais, alterando o microclima e empobrecendo a fertilidade do clássico solo de massapê.
""",
        # q43 (E)
        """<!-- id: q43 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: assoreamento-mineracao-minas-gerais -->
### Questão 43
No século XVIII, a corrida do ouro nas Minas Gerais provocou uma catástrofe geomorfológica e hídrica nas calhas dos rios das Velhas, Doce e das Mortes. Esse processo, decorrente do método da mineração de aluvião e do desmonte hidráulico das encostas, teve como impacto ecológico duradouro:

a) A substituição de gramíneas nativas de capim por plantações de oliveiras e vinhedos trazidos de Portugal.
b) A contaminação do ar metropolitano pela queima de querosene refinado em motores a combustão nas minas.
c) A elevação drástica da temperatura média das bacias subterrâneas provocada pelo calor das tochas de azeite.
d) O desaparecimento de lagoas artificiais que serviam de viveiros de crustáceos marinhos nas capitais provinciais.
e) O soterramento dos leitos fluviais por milhões de toneladas de cascalho e lama estéril, destruindo a fauna aquática e tornando rios outrora cristalinos em canais barrentos.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** Para alcançar o ouro acumulado nas margens e fundos dos rios, os mineradores desviavam leitos naturais e bombardeavam morros com jatos violentos de água represada nos topos das serras.
- **Etapa 2:** Essa técnica arrancava camadas inteiras de rocha e terra, despejando sedimentos estéreis nos cursos de água; a calha dos rios entupiu-se de areia e cascalho, diminuindo a profundidade e extinguindo peixes e moluscos.
- **Etapa 3:** A poluição e o assoreamento histórico de bacias como a do Rio Doce tiveram sua raiz nessa intervenção mineradora colonial, cujos efeitos de degradação da paisagem ribeirinha permaneceram visíveis por séculos.
""",
        # q44 (A)
        """<!-- id: q44 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: lavoura-nomade-cafe-erosao-vale -->
### Questão 44
A expansão da cafeicultura no Vale do Rio Paraíba do Sul durante o século XIX exemplifica o fenômeno que os historiadores econômicos e ambientais denominam 'lavoura nômade'. A engrenagem agronômica e ecológica que levou à exaustão e à ruína precoce das fazendas dos 'barões do café' articulou-se a partir de:

a) A queima contínua da Mata Atlântica nas encostas serranas e o plantio de cafeeiros em linhas retas morro abaixo, provocando erosão severa e abertura de voçorocas com a perda do solo fértil.
b) A recusa dos fazendeiros em utilizar trabalhadores escravizados nas lavouras, contratando técnicos estrangeiros que exigiam adubação orgânica.
c) O cultivo exclusivo de variedades de café de baixa resistência genética que morriam com as primeiras brisas do oceano.
d) A assinatura de convênios florestais que obrigavam as fazendas a destinar a maior parte de suas encostas à conservação integral da flora nativa.
e) A decisão governamental de tabelar os preços internacionais do café nos portos, impedindo a compra de ferramentas de ferro para a capina.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** Os cafeicultores do Vale não adotavam terraceamento, curvas de nível ou adubos; derrubavam a mata virgem de encosta, ateavam fogo para aproveitar as cinzas superficiais e plantavam em linhas verticais.
- **Etapa 2:** As chuvas de verão lavavam a camada de terra fértil morro abaixo em poucos anos; sem a raiz da floresta, a encosta desmoronava, abrindo fendas profundas de erosão (voçorocas) que expunham o barro estéril.
- **Etapa 3:** Após três ou quatro décadas de safra rápida, as terras transformavam-se em capoeiras improdutivas; os fazendeiros simplesmente abandonavam o patrimônio edificado e marchavam para novas florestas do Oeste Paulista, deixando para trás cidades falidas.
""",
        # q45 (B)
        """<!-- id: q45 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: revolucao-verde-cerrado-calagem -->
### Questão 45
A transformação do Cerrado brasileiro no principal polo do agronegócio de grãos e carne a partir da década de 1970 decorreu da articulação entre pesquisas agronômicas desenvolvidas pela Embrapa, investimentos estatais em infraestrutura e abertura de crédito agrícola. Do ponto de vista da História Ambiental, esse processo representou:

a) A erradicação definitiva do uso de agrotóxicos e fertilizantes químicos nas bacias dos rios Tocantins e Araguaia.
b) A conversão radical de uma savana tropical rica em biodiversidade e de solo ácido em monoculturas mecanizadas, gerando a perda de metade de sua vegetação nativa e ameaçando a recarga de aquíferos vitais.
c) O fortalecimento das pequenas propriedades policulturais gerenciadas democraticamente por comunidades indígenas locais.
d) A proibição do cultivo de grãos para exportação com foco na produção exclusiva de frutas nativas para mercados de bairro.
e) A recuperação espontânea da fauna de grandes mamíferos graças ao confinamento de rebanhos bovinos em áreas de terraço.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** Considerado terra infértil por séculos, o Cerrado foi destravado tecnicamente pela aplicação massiva de calcário (calagem) para corrigir a acidez, associada a adubos minerais e sementes selecionadas de soja.
- **Etapa 2:** Essa modernização conservadora transformou o Centro-Oeste em um celeiro global exportador, mas demandou o desmatamento raso de mais de cinquenta por cento do bioma, com tratores puxando correntões para limpar a vegetação nativa.
- **Etapa 3:** O Cerrado é a 'caixa-d'água' do país; o desmatamento acelerado e a irrigação intensa por pivôs centrais rebaixaram os lençóis freáticos e reduziram os fluxos de água que abastecem as grandes bacias hidrográficas nacionais.
""",
        # q46 (D)
        """<!-- id: q46 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: dinamica-fronteira-amazonia-sudam -->
### Questão 46
Na década de 1970, o modelo de ocupação da Amazônia formulado pela Ditadura Militar operou sob a doutrina da segurança nacional e a crença no crescimento econômico a qualquer custo. O mecanismo financeiro e fundiário que alimentou a queima da floresta nesse período caracterizou-se pela:

a) Criação de linhas de microcrédito bancário exclusivas para ribeirinhos que coletavam óleos e seivas medicinais nativas.
b) Exigência de que as empresas agropecuárias mantivessem mais de noventa por cento de suas fazendas como áreas de preservação permanente.
c) Proibição do tráfego de caminhões e tratores ao longo das rodovias federais abertas na selva.
d) Concessão de incentivos fiscais generosos pela SUDAM a grupos econômicos do Centro-Sul, permitindo abater impostos em troca da implantação de fazendas de gado formadas pela derrubada e queima da mata.
e) Desapropriação imediata de propriedades de fazendeiros que cortassem castanheiras e árvores de madeira de lei.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** O governo federal abriu os eixos rodoviários (Transamazônica, BR-364, Belém-Brasília) e utilizou a Superintendência do Desenvolvimento da Amazônia (SUDAM) como instrumento de atração de capital.
- **Etapa 2:** Bancos, montadoras e frigoríficos do Sudeste podiam aplicar parte de seus impostos de renda na abertura de fazendas no Norte; para comprovar que a terra estava 'produtiva' e obter os subsídios, era exigido o desmatamento e a queima da floresta.
- **Etapa 3:** O resultado foi a grilagem violenta de terras públicas de posseiros e povos originários, o avanço de pistoleiros e a destruição de milhões de hectares de floresta primária para manter um gado de baixa densidade.
""",
        # q47 (E)
        """<!-- id: q47 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: rios-voadores-evapotranspiracao-clima -->
### Questão 47
Estudos científicos liderados por climatologistas brasileiros (como Antonio Donato Nobre em 'O Futuro Climático da Amazônia') demonstram a complexa interdependência ecossistêmica entre a Floresta Amazônica e o regime pluviométrico do Centro-Sul do país por meio da teoria dos 'Rios Voadores'. A quebra desse equilíbrio ecológico provocada pelo desmatamento massivo decorre do fato de que:

a) As queimadas na mata aceleram o resfriamento das massas de ar polar que sobem da bacia do Prata em direção aos trópicos.
b) As árvores de folhas largas da floresta consomem toda a água das chuvas, impedindo que o vapor viaje para outros estados vizinhos.
c) O abate de madeiras nobres estimula a formação de geleiras temporárias nas planícies fluviais do vale do rio Guaporé.
d) A substituição da floresta por capim de pastagem aumenta a infiltração de água doce no manto rochoso profundo da crosta terrestre.
e) Cada árvore madura bombeia diariamente centenas de litros de vapor para o ar pela evapotranspiração; a derrubada da mata cessa esse fluxo aéreo e impede que os ventos levem umidade para o Sudeste.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** A Amazônia funciona como uma bomba biótica de água: suas bilhões de árvores transpiram diariamente um volume de água equivalente ou superior à vazão do próprio rio Amazonas para a atmosfera.
- **Etapa 2:** Esses rios aéreos de vapor encontram a barreira física da Cordilheira dos Andes e são desviados para o sul, transportando as chuvas que abastecem o agronegócio de grãos do Centro-Oeste e as represas do Sudeste.
- **Etapa 3:** Quando a floresta é derrubada para dar lugar a pastos, a capacidade de gerar vapor cai drasticamente; o ar resseca, as frentes de chuva escasseiam e o Centro-Sul passa a vivenciar estiagens prolongadas e crises hídricas graves.
""",
        # q48 (A)
        """<!-- id: q48 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: socioambientalismo-chico-mendes-resistencia -->
### Questão 48
Ao analisar a emergência do movimento dos seringueiros no Acre na década de 1970 sob a liderança de Chico Mendes, os historiadores destacam que a inovação do Socioambientalismo consistiu em romper com a dicotomia tradicional entre conservação biológica e presença humana. Essa virada paradigmática fundamentou-se na premissa de que:

a) A defesa da floresta tropical viva e a proteção da dignidade humana e dos direitos territoriais dos trabalhadores tradicionais são lutas inseparáveis e complementares.
b) Os operários industriais das cidades metropolitanas deveriam assumir o controle armado da extração madeireira no interior da selva.
c) As populações ribeirinhas precisavam ser transferidas compulsoriamente para conjuntos habitacionais urbanos para garantir a mata intocada.
d) O comércio internacional da borracha natural dependia do desmatamento das castanheiras centenárias para abrir espaço a seringais de cultivo.
e) A preservação de ecossistemas florestais deve ser financiada exclusivamente pela venda de títulos públicos em bolsas de mercadorias.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** O ambientalismo tradicional muitas vezes via a presença humana como inerentemente predatória, propondo parques cercados e expulsando povos que habitavam a terra há gerações.
- **Etapa 2:** Chico Mendes demonstrou que os seringueiros, indígenas e ribeirinhos tinham um modo de vida sustentável: eles precisavam da floresta de pé para extrair látex e castanhas, sendo os seus verdadeiros guardiões naturais contra o avanço dos grileiros.
- **Etapa 3:** O socioambientalismo uniu ecologia e questão social: não se protege a floresta desrespeitando quem nela vive; a conservação da biodiversidade só é duradoura quando articulada à posse coletiva da terra e à justiça para os povos da floresta.
""",
        # q49 (B)
        """<!-- id: q49 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: criacao-e-natureza-juridica-das-resex -->
### Questão 49
A instituição das Reservas Extrativistas (RESEX) no direito ambiental brasileiro representou uma conquista institucional do movimento socioambiental que desafiou as noções tradicionais de propriedade da terra. A natureza jurídica e o funcionamento das RESEX caracterizam-se pelo fato de que:

a) As áreas são vendidas em leilões judiciais privados para grupos de investimentos imobiliários com foco em loteamentos rurais.
b) A terra permanece como bem público pertencente à União, concedendo-se o usufruto coletivo permanente e o manejo sustentável às comunidades tradicionais organizadas em associações.
c) A gestão das reservas é delegada exclusivamente a companhias mineradoras privadas encarregadas de abrir estradas vicinais.
d) Os trabalhadores das reservas são enquadrados como funcionários públicos estatutários com salários fixados pelo orçamento federal.
e) Os recursos naturais da reserva podem ser comercializados apenas após a assinatura de termos de cessão de direitos a frigoríficos locais.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** A propriedade privada tradicional permitia que grileiros comprassem ou forjassem escrituras de áreas gigantescas, expulsassem posseiros e queimassem a mata para colocar gado.
- **Etapa 2:** A RESEX instituiu uma figura inovadora: a terra é pública (patrimônio inalienável da União), mas concedida em usufruto coletivo para as famílias tradicionais que nela habitam e realizam extrativismo não predatório.
- **Etapa 3:** Por não pertencer individualmente a ninguém, a terra da RESEX não pode ser vendida, loteada ou penhorada por bancos; a floresta fica juridicamente blindada contra a grilagem e a especulação fundiária do agronegócio predatório.
""",
        # q50 (C)
        """<!-- id: q50 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: monocultura-e-perda-de-húmus-voçorocas -->
### Questão 50
A geomorfologia e a pedologia históricas evidenciam que o solo sob a cobertura original da Mata Atlântica é mantido fértil por uma fina camada superficial de matéria orgânica (húmus) gerada pela decomposição contínua de folhas e galhos da própria copa da floresta. Quando os cafeicultores do século XIX retiraram essa cobertura para plantar café morro abaixo, desencadearam um processo de degradação em que:

a) As raízes dos cafeeiros produziam substâncias minerais que endureciam as camadas profundas de calcário basáltico.
b) A terra aumentava espontaneamente o teor de umidade, transformando as encostas serranas em brejos alagados permanentes.
c) A insolação direta e as chuvas torrenciais lavavam rapidamente a fina camada de húmus, expondo o solo argiloso frágil e gerando voçorocas que inviabilizaram a agricultura.
d) Os cursos fluviais locais aprofundavam seus canais rochosos, impedindo que as enxurradas atingissem as áreas cultivadas das várzeas.
e) A vegetação de gramíneas exóticas recuperava a fertilidade original do solo em menos de cinco anos após o abandono das lavouras.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** A floresta tropical alimenta a si mesma: a fertilidade da terra não está no solo profundo (que costuma ser ácido e pobre), mas na fina camada de húmus mantida pela umidade e pelas folhas caídas da copa.
- **Etapa 2:** Com o corte raso e a queima da mata para o café, a proteção da copa desapareceu; o sol ressecou o húmus e as fortes chuvas de verão lavaram todos os nutrientes em um processo violento de lixiviação.
- **Etapa 3:** Desprovido de raízes e matéria orgânica, o solo argiloso das encostas rachou e desmoronou em crateras de erosão (voçorocas); a terra tornou-se estéril, expulsando os fazendeiros e marcando a decadência definitiva do café no Vale do Paraíba.
""",
        # q51 (E)
        """<!-- id: q51 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: alianca-dos-povos-da-floresta-constituinte -->
### Questão 51
A fundação da Aliança dos Povos da Floresta em 1985 reuniu pela primeira vez em um projeto político comum duas populações tradicionalmente colocadas em confronto pela exploração patronal na Amazônia: seringueiros e povos indígenas. Essa convergência histórica operou uma profunda transformação na luta política brasileira porque:

a) Estabeleceu que os seringais de cultivo seriam desmatados para plantio consorciado de eucaliptos comerciais.
b) Determinou o recolhimento de todas as armas de caça em poder de aldeias ribeirinhas do vale do rio Juruá.
c) Concedeu aos fazendeiros de gado o direito de fiscalizar as divisas territoriais de reservas demarcadas pela União.
d) Proibiu que entidades ambientalistas internacionais participassem de reuniões com os sindicatos de trabalhadores rurais.
e) Desfez o discurso governamental de que a Amazônia era um 'vazio demográfico' desabitado, unindo a defesa dos territórios tradicionais à conservação dos biomas na Assembleia Constituinte de 1987-1988.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** Durante décadas, os patrões dos seringais atiçaram conflitos entre seringueiros mestiços e tribos indígenas, dividindo os trabalhadores para enfraquecer resistências e baratear salários de aviamento.
- **Etapa 2:** Sob a liderança de Chico Mendes e Ailton Krenak, essas comunidades perceberam que o inimigo comum era o latifúndio grileiro armado que expulsava ambos e passava o correntão na floresta.
- **Etapa 3:** A união na Aliança dos Povos da Floresta desmontou a falácia militar de 'integrar um espaço vazio': provou perante o país e a Constituinte de 1988 que a Amazônia era habitada por culturas ricas que protegiam o meio ambiente, conquistando os Artigos 225 e 231 da Carta Magna.
""",
        # q52 (A)
        """<!-- id: q52 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: dificil | objeto: mercantilizacao-da-natureza-critica-historica -->
### Questão 52
Ao confrontar a narrativa desenvolvimentista do século XX com os dados empíricos da degradação dos biomas nacionais, os historiadores ambientais demonstram que a riqueza material acumulada nos ciclos do açúcar, do ouro e do café caracterizou-se pela 'externalização dos custos ecológicos'. Esse conceito significa que:

a) Os lucros privados da exportação foram apropriados por elites mercantis e agrárias, enquanto os prejuízos da erosão, do desmatamento e da contaminação hídrica foram transferidos para a sociedade e para as futuras gerações.
b) As companhias agrícolas estrangeiras pagavam indenizações tributárias para reflorestar montanhas degradadas no interior do país.
c) Os custos de adubação química dos solos foram assumidos exclusivamente por ministérios públicos civis de países vizinhos.
d) O valor de venda dos produtos tropicais nos mercados europeus cobria os gastos com a recomposição de matas ciliares nascentes.
e) As fazendas de café mantinham reservas financeiras compulsórias para custear a recuperação de encostas afetadas por voçorocas.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** Na economia tradicional de mercado, custos como adubos, maquinário e salários entram nas planilhas de cálculo; a destruição da floresta nativa e a perda da água de nascentes nunca foram computadas nos custos de produção.
- **Etapa 2:** Barões do café e mineradores obtiveram lucros fabulosos porque exploravam a terra até a morte sem gastar nada para recuperá-la; quando o solo se esgotava, simplesmente marchavam para novas áreas virgens.
- **Etapa 3:** A riqueza concentrou-se nas mãos de poucos proprietários e mercadores, mas a conta da degradação ambiental — desertificação, perda de nascentes, crises hídricas e aridez — foi 'externalizada' e deixada como herança pesada para toda a nação brasileira.
""",
        # q53 (B)
        """<!-- id: q53 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: tipping-point-amazonia-savanizacao -->
### Questão 53
O conceito de 'tipping point' (ponto de inflexão ou não retorno) formulado por cientistas que estudam a bacia amazônica (como Carlos Nobre e Thomas Lovejoy) descreve um risco sistêmico irreversível para o equilíbrio do planeta. Esse ponto crítico ocorreria caso o desmatamento acumulado na Amazônia atinja entre 20% e 25% de sua área total, provocando:

a) A proliferação descontrolada de recifes de corais de água doce nos estuários do rio Pará.
b) O colapso definitivo da capacidade da floresta de reciclar umidade atmosférica, desencadeando um processo espontâneo e acelerado de savanização de grande parte do bioma.
c) O surgimento de correntes marinhas polares que congelariam a foz dos rios tributários do planalto das Guianas.
d) A interrupção da atividade agrícola de grãos na Argentina devido ao excesso de chuvas torrenciais diárias na bacia do Prata.
e) A diminuição das emissões de dióxido de carbono pela queima da vegetação rasteira em pastagens degradadas.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** A Floresta Amazônica produz metade de sua própria precipitação; sua umidade recicla-se de cinco a seis vezes à medida que o vapor viaja do Atlântico em direção aos Andes.
- **Etapa 2:** Cientistas alertam que se o desmatamento ultrapassar o limiar de vinte por cento, a quantidade de árvores remanescentes não será mais suficiente para bombear a umidade necessária para sustentar a floresta úmida nas estações secas.
- **Etapa 3:** O ecossistema atingiria o ponto de não retorno: a floresta começaria a secar e queimar de forma autônoma e irreversível, transformando-se em uma savana pobre e degradada, liberando bilhões de toneladas de carbono e agravando o aquecimento global.
""",
        # q54 (C)
        """<!-- id: q54 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: dificil | objeto: restingas-e-manguezais-destruicao-colonial -->
### Questão 4
A ocupação colonial do litoral brasileiro pelo ciclo do açúcar e pela fundação das primeiras capitanias afetou profundamente ecossistemas costeiros frágeis como os manguezais e as restingas. A degradação desses ambientes litorâneos teve como consequência ecológica:

a) O aumento da salinidade dos poços artesianos nas regiões montanhosas do interior de Goiás.
b) A formação de grandes dunas de areia basáltica que soterraram fazendas de café no vale do rio Paraíba.
c) A destruição de berçários naturais da vida marinha, a perda de proteção costeira contra ressacas e a alteração dos regimes estuarinos fluviais.
d) A redução das temperaturas médias das correntes marinhas equatoriais que cruzavam o canal de Moçambique.
e) A obrigatoriedade de construir quebra-mares de pedra de cantaria em portos mercantis desprovidos de atividade pesqueira.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** Manguezais e restingas funcionam como zonas de transição entre a terra e o mar: os mangues são berçários de peixes, siris e camarões, e as restingas seguram as dunas de areia contra a fúria das ondas.
- **Etapa 2:** Os colonizadores aterraram mangues para construir portos, trapiches e cidades (como Salvador, Recife e Rio de Janeiro), além de cortar espécies de mangue para aproveitar tanino e lenha de alta resistência à água salgada.
- **Etapa 3:** Essa destruição histórica quebrou as teias alimentares marinhas costeiras e retirou a proteção natural contra o avanço das ressacas do mar, intensificando a erosão das praias e prejudicando comunidades pesqueiras tradicionais.
""",
        # q55 (D)
        """<!-- id: q55 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: conflitos-fundiarios-acre-xapuri-violencia -->
### Questão 55
Os conflitos de terra no Acre durante as décadas de 1970 e 1980, que culminaram no assassinato de Chico Mendes em dezembro de 1988, expressaram um choque frontal entre dois projetos civilizatórios e territoriais inconciliáveis para a Amazônia:

a) O modelo de mineração industrial subterrânea de carvão mineral contra o turismo fluvial ecológico internacional.
b) O projeto de instalação de montadoras multinacionais de automóveis elétricos contra o cultivo comunitário de arroz irrigado.
c) O plano de colonização agrícola de famílias camponesas sem terra do Sul contra as comunidades de pescadores de lagoas costeiras.
d) A expansão violenta do latifúndio pecuarista especulativo baseado na queima da floresta contra o modelo socioambiental de conservação produtiva dos povos da floresta.
e) A construção de canais de navegação oceânica em rios afluentes contra as cooperativas de tecelagem manual de algodão nativo.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** De um lado estavam os 'paulistas' — fazendeiros e grupos econômicos do Centro-Sul atraídos por incentivos fiscais e pela especulação de terras valorizadas pela abertura de rodovias federais.
- **Etapa 2:** Do outro estavam os povos tradicionais — seringueiros, ribeirinhos e indígenas que viviam da floresta sem desmatá-la, praticando o extrativismo sustentável do látex e da castanha.
- **Etapa 3:** O assassinato de Chico Mendes foi o desfecho trágico da recusa dos latifundiários grileiros em aceitar a existência de áreas públicas de preservação comunal; a morte do líder transformou-se no símbolo supremo da luta pelo socioambientalismo no mundo.
""",
        # q56 (A)
        """<!-- id: q56 | tipo: multipla-escolha | habilidade: EM13CHS206 | dificuldade: dificil | objeto: fragmentacao-mata-atlantica-perda-polinizadores -->
### Questão 56
A fragmentação florestal extrema da Mata Atlântica ao longo dos séculos produziu o isolamento genético de populações animais e vegetais remanescentes. Na perspectiva da ecologia de paisagens e da biologia da conservação, esse fenômeno de isolamento ecológico gera o risco de:

a) Extinção em cascata de espécies nativas devido à perda de polinizadores e dispersores de sementes e à diminuição da variabilidade genética em ilhas de mata isoladas.
b) Aumento espontâneo da fertilidade de sementes florestais devido à incidência de luz solar direta nas bordas dos fragmentos.
c) Adaptação acelerada de grandes felinos predadores que passam a alimentar-se exclusivamente de sementes e cascas de árvores exóticas.
d) Recuperação autônoma de espécies arbóreas raras em áreas de pastagem contínua sem necessidade de corredores ecológicos.
e) Desaparecimento de parasitas e bactérias benéficas que regulavam o equilíbrio de nutrientes nas raízes de bromélias.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** Quando uma floresta contínua é recortada por estradas, cidades e pastos, as espécies animais não conseguem cruzar os descampados abertos por medo de predadores e atropelamentos.
- **Etapa 2:** Grandes mamíferos (como a onça-pintada e o muriqui) e aves frugívoras (como o tucano e o jacutinga) desaparecem dos fragmentos pequenos; sem eles, as árvores de sementes grandes não encontram dispersores naturais para se espalhar.
- **Etapa 3:** O isolamento gera consanguinidade e enfraquecimento genético, levando ao colapso silencioso da floresta sobrevivente; por isso, a restauração ambiental contemporânea exige a criação de 'corredores ecológicos' que reconectem os fragmentos isolados.
""",
        # q57 (B)
        """<!-- id: q57 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: papel-embrapa-cerrado-calagem -->
### Questão 57
A atuação da Empresa Brasileira de Pesquisa Agropecuária (Embrapa) a partir da década de 1970 no bioma Cerrado é frequentemente apontada como uma das mais expressivas intervenções da ciência agronômica na história nacional. Contudo, ao avaliar criticamente essa conquista técnica sob o prisma socioambiental, os pesquisadores ressaltam que:

a) O domínio da biotecnologia permitiu a eliminação do uso de máquinas pesadas na colheita mecanizada de grãos.
b) A revolução agrícola concentrou terras em grandes latifúndios monoculturais de exportação, gerando desmatamento massivo e vulnerabilidade hídrica em detrimento da agricultura familiar.
c) As tecnologias da calagem foram aplicadas prioritariamente para fortalecer comunidades tradicionais de coletores de baru e pequi.
d) O sucesso das safras de soja eliminou a dependência nacional de fertilizantes e pesticidas importados de refinarias estrangeiras.
e) A introdução de culturas temporárias de milho e algodão restabeleceu a densidade primitiva de animais carnívoros no planalto central.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** A ciência brasileira resolveu o enigma do solo ácido do Cerrado, permitindo que o país multiplicasse safras e batesse recordes históricos de produção de grãos e balança comercial favorável.
- **Etapa 2:** Essa expansão deu-se sob o modelo da grande propriedade monocultural altamente mecanizada, que gera pouquíssimos empregos por hectare e expulsa posseiros, ribeirinhos e geraizeiros tradicionais de suas terras comunais.
- **Etapa 3:** A comemoração dos recordes de exportação de soja contrasta com o custo socioambiental pesado: perda de metade do Cerrado nativo, contaminação de águas por defensivos agrícolas e quebra do equilíbrio de recarga das nascentes do Brasil.
""",
        # q58 (C)
        """<!-- id: q58 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: cidades-mortas-monteiro-lobato-vale -->
### Questão 58
Na obra Cidades Mortas (1919), José Bento Monteiro Lobato documentou o cenário desolador deixado pela passagem da cafeicultura no Vale do Paraíba paulista e fluminense. Sob a ótica da História e da Literatura, o testemunho lobatiano sobre municípios como Bananal, Areias e Silveiras evidencia que:

a) O abandono do cultivo do café no Vale permitiu o renascimento espontâneo imediato da densa floresta tropical de encosta.
b) A riqueza cafeeira baseou-se em investimentos industriais modernos que transformaram o interior paulista em polo de tecnologia mecânica.
c) A prosperidade baseada na pilhagem da natureza foi efêmera, deixando casarões decadentes, populações empobrecidas e uma terra calcinada que perdeu sua capacidade produtiva.
d) As ferrovias construídas pelos barões do café conseguiram evitar o êxodo das famílias de trabalhadores para o Oeste Paulista.
e) A ausência de rios navegáveis foi o único obstáculo para que o Vale do Paraíba continuasse liderando as exportações de grãos do país.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** Monteiro Lobato visitou as cidades do Vale no início do século XX e deparou-se com palacetes neoclássicos vazios, igrejas em ruínas e praças desertas cobertas de poeira e mato.
- **Etapa 2:** Os fazendeiros haviam enriquecido rapidamente exibindo títulos de nobreza imperial, mas sua fortuna assentou-se na queima impiedosa da Mata Atlântica e no trabalho escravo, sem cuidar da reposição de nutrientes do solo.
- **Etapa 3:** Quando a terra exauriu-se e as encostas desmoronaram em voçorocas, os capitais migraram; Lobato retratou a ressaca amarga da predação: cidades fantasmas cercadas por morros despidos e capim estéril, comprovando o caráter passageiro e destrutivo da monocultura predatória.
""",
        # q59 (D)
        """<!-- id: q59 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: gestao-coletiva-resex-chico-mendes -->
### Questão 59
A governança das Reservas Extrativistas (RESEX) baseia-se na elaboração de um documento oficial denominado 'Plano de Manejo', aprovado pelo órgão ambiental federal (ICMBio) em conjunto com as associações comunitárias de moradores tradicionais. Esse instrumento de gestão ecológica e territorial caracteriza-se por:

a) Autorizar a venda irrestrita de madeira de mogno para empresas madeireiras privadas que operam em portos fluviais.
b) Determinar a expulsão temporária de famílias extrativistas durante as estações secas para evitar o pisoteio de sementes nativas.
c) Permitir a queima de áreas florestais primárias sempre que os preços da borracha natural caírem nas cotações internacionais.
d) Estabelecer regras coletivas rigorosas sobre épocas de coleta, limites sustentáveis de extração, zonas de proteção integral e proibição de queimadas e pastagens comerciais.
e) Cobrar taxas tributárias alfandegárias das comunidades tradicionais sobre a farinha de mandioca e o açaí consumidos nos povoados.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** Uma RESEX não é terra de ninguém nem área de livre exploração caótica; ela é uma unidade de conservação de uso sustentável regida por normas técnicas e saberes ancestrais.
- **Etapa 2:** O Plano de Manejo é construído democraticamente: a comunidade define onde se pode coletar borracha, quantos quilos de castanha podem ser colhidos sem prejudicar a reprodução das árvores e quais áreas da mata devem permanecer intocadas.
- **Etapa 3:** É estritamente proibido o uso de motosserras, o fogo comercial e o desmatamento para pasto de gado; os próprios moradores fiscalizam o território contra invasões de grileiros, comprovando que a conservação é mais eficaz quando compartilhada com a comunidade local.
""",
        # q60 (E)
        """<!-- id: q60 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: justica-climatica-e-socioambientalismo-seculo-xxi -->
### Questão 60
Ao analisar a emergência das crises ecológicas contemporâneas — como a escassez de água em metrópoles brasileiras, as queimadas descontroladas no Pantanal e na Amazônia e o aumento das ondas de calor extremo —, os cientistas sociais apontam para a urgência de incorporar o conceito de 'Justiça Climática'. Aplicado à realidade da história ambiental do Brasil, esse conceito revela que:

a) Os impactos das enchentes e secas distribuem-se de maneira perfeitamente homogênea e igualitária entre todos os grupos sociais da população.
b) As nações mais ricas do hemisfério ocidental devem ser desobrigadas de reduzir suas emissões de dióxido de carbono na atmosfera.
c) O uso de tecnologias de ar-condicionado em edifícios empresariais modernos protege as metrópoles contra desequilíbrios do regime hídrico.
d) As comunidades indígenas e ribeirinhas que vivem do extrativismo são as principais responsáveis pelo aquecimento do clima global.
e) As populações mais vulneráveis (povos indígenas, quilombolas, ribeirinhos e periferias urbanas) são as que menos contribuíram para a destruição ecológica, mas são as que sofrem com maior intensidade as perdas socioeconômicas e sanitárias das mudanças climáticas.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** A crise ambiental e climática não é neutra nem afeta a todos da mesma forma; ela reproduz e aprofunda as desigualdades históricas de classe, raça e território.
- **Etapa 2:** As elites econômicas que lucraram com a queima da floresta, a grilagem e o agronegócio predatório possuem recursos financeiros para morar em bairros arborizados, comprar água mineral e proteger-se do calor.
- **Etapa 3:** Quem sofre com a seca dos rios, a queima de suas roças, a contaminação por mercúrio e as enchentes nos morros periféricos são as populações vulneráveis; a Justiça Climática afirma que enfrentar a crise ecológica exige reparar as injustiças históricas contra aqueles que sempre cuidaram da terra.
"""
    ]

    references = """
## Referências

- BRASIL. *Constituição da República Federativa do Brasil de 1988*. Artigo 225. Brasília: Presidência da República, 1988.
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/SEB, 2018.
- CARVALHO, José Alberto de. *Chico Mendes: Um Povo da Floresta*. São Paulo: Brasiliense, 1990.
- DEAN, Warren. *A Ferro e Fogo: A História e a Devastação da Mata Atlântica Brasileira*. São Paulo: Companhia das Letras, 1996.
- DIEGUES, Antonio Carlos. *O Mito Moderno da Natureza Intocada*. São Paulo: Hucitec, 1996.
- NOBRE, Antonio Donato. *O Futuro Climático da Amazônia: Relatório de Avaliação Científica*. São José dos Campos: ARA, CCST-INPE, INPA, 2014.
- PÁDUA, José Augusto. *Um Sopro de Destruição: Pensamento Político e Crítica Ambiental no Brasil Escravista (1786-1888)*. Rio de Janeiro: Jorge Zahar Editor, 2002.
- WORSTER, Donald. *Para Fazer História Ambiental*. Estudos Históricos, Rio de Janeiro, v. 4, n. 8, p. 198-215, 1991.
"""

    content = frontmatter + "\n" + "\n".join(questions_basic) + "\n## Nível Intermediário (Questões 21-40)\n\n" + "\n".join(questions_inter) + "\n## Nível Difícil (Questões 41-60)\n\n" + "\n".join(questions_hard) + "\n" + references
    return content

if __name__ == "__main__":
    output_path = r"c:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\temp_draft_c52.md"
    content = build_draft_c52()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Draft c52 written successfully to {output_path} ({len(content)} chars)")
