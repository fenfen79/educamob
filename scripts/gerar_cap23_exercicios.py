# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 23 de Filosofia EM:
Achille Mbembe e a Necropolítica
Objeto: cap-23-achille-mbembe-necropolitica
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
        "Qual é a nacionalidade e a formação intelectual do filósofo Achille Mbembe, criador do conceito de Necropolítica?",
        "Sociólogo britânico especialista em economia industrial do século XIX.",
        "Historiador e filósofo camaronês que leciona e pesquisa a partir da perspectiva do Sul Global.",
        "Economista norte-americano focado no comércio financeiro de derivativos bancários.",
        "Geógrafo alemão dedicado ao mapeamento geológico de cordilheiras alpinas.",
        "Antropólogo australiano dedicado ao estudo exclusivo de línguas insulares extintas.",
        "B",
        "Achille Mbembe nasceu em Camarões e tornou-se um dos maiores filósofos políticos contemporâneos, pensando a soberania e o poder a partir da história africana e pós-colonial."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Qual é a tese definidora central do conceito de 'Necropolítica' formulado por Achille Mbembe?",
        "A organização de competições esportivas entre cidades metropolitanas para promover a paz.",
        "A capacidade e o poder soberano do Estado ou de dispositivos armados de ditar quem tem o direito de viver e quem deve ser exposto à morte.",
        "A criação de incentivos fiscais para empresas que comercializam veículos elétricos.",
        "A substituição de moedas fiduciárias por recibos lastreados em safras de cereais.",
        "A administração hospitalar centrada unicamente no atendimento médico pediátrico.",
        "B",
        "Necropolítica é a política da morte: o poder soberano não atua apenas gerindo a vida, mas decidindo ativamente quais populações são descartáveis e podem ser sacrificadas."
    ))

    questoes_brutas.append((
        3, "EM13CHS601", "basico",
        "De que maneira a teoria de Achille Mbembe expande e complementa o conceito foucaultiano de 'Biopoder'?",
        "Rejeitando integralmente a existência de leis sanitárias nos países ocidentais modernos.",
        "Demonstrando que, nas colônias e no Sul Global, o poder não se restringe à fórmula de 'fazer viver e deixar morrer', organizando-se ativamente para matar e administrar o extermínio de corpos racializados.",
        "Afirmando que a medicina hospitalar europeia foi criada por corporações de navegadores marítimos.",
        "Sustentando que as epidemias do século XX foram erradicadas unicamente por orações monásticas.",
        "Provando que as prisões modernas foram substituídas por tribunais de conciliação comunitária.",
        "B",
        "Mbembe expande Foucault: o biopoder cuidava da vida da metrópole, mas nas colônias e periferias o poder sempre foi necropolítico, governando pelo cano do fuzil e pelo massacre planejado."
    ))

    questoes_brutas.append((
        4, "EM13CHS602", "basico",
        "O que Mbembe conceitua como 'Políticas da Inimizade' no funcionamento do necropoder contemporâneo?",
        "A assinatura pacífica de tratados comerciais de redução de tarifas alfandegárias.",
        "A fabricação discursiva do 'Inimigo Absoluto' desumanizado, explorando o medo e o pânico moral da sociedade para legitimar intervenções armadas e massacres de populações marginalizadas.",
        "A obrigatoriedade de disputas de esgrima para resolver litígios possessórios entre vizinhos.",
        "O estabelecimento de quotas diplomáticas para o intercâmbio de estudantes de belas artes.",
        "A celebração de acordos navais para a padronização de uniformes de tripulações mercantes.",
        "B",
        "As políticas da inimizade criam um bode expiatório desumanizado: a sociedade é convencida de que o outro é um perigo biológico mortal, aplaudindo a polícia que o abate sem piedade."
    ))

    questoes_brutas.append((
        5, "EM13CHS603", "basico",
        "Qual é a perturbadora definição fornecida por Achille Mbembe para o conceito de 'Mundos de Morte' (*Death-worlds*)?",
        "Parques temáticos recreativos dedicados à representação teatral de lendas mitológicas antigas.",
        "Formas de existência social em territórios sitiados onde vastas populações são submetidas a condições de vida que lhes conferem o estatuto permanente de mortos-vivos.",
        "Zonas francas industriais isentas de tributação sobre a montagem de computadores portáteis.",
        "Acampamentos florestais temporários instalados para a pesquisa botânica de orquídeas raras.",
        "Câmaras legislativas municipais que realizam votações orçamentárias no período noturno.",
        "B",
        "Os mundos de morte são lugares onde a vida foi desmantelada: sem esgoto, sem remédio, sob tiros diários e vigilância contínua, onde o ser humano vive na fronteira perpétua da aniquilação física."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "Por que a Plantação Escravocrata (*Plantation*) nas Américas coloniais é considerada por Mbembe a primeira matriz histórica da necropolítica?",
        "Porque os latifúndios canavieiros utilizavam moinhos d'água construídos por engenheiros franceses.",
        "Porque submeteu o ser humano escravizado à perda da terra, à perda de direitos sobre o próprio corpo (transformado em mercadoria) e à morte civil total, onde o senhor tinha o poder ilimitado de vida e morte.",
        "Porque as mercadorias agrícolas coloniais eram comercializadas exclusivamente em feiras municipais locais.",
        "Porque os proprietários de engenho eram obrigados a prestar contas a comissões consulares marítimas.",
        "Porque os trabalhadores das lavouras recebiam salários pagos em moedas metálicas de prata e ouro.",
        "B",
        "A plantação foi o primeiro laboratório do terror: o escravizado não era pessoa, mas propriedade; sua vida pertencia ao capataz que podia torturá-lo e matá-lo impunemente pelo direito soberano colonial."
    ))

    questoes_brutas.append((
        7, "EM13CHS102", "basico",
        "Como a ocupação colonial na África e na Ásia no século XIX funcionou como laboratório para as tecnologias de extermínio contemporâneas?",
        "Estimulando a realização de feiras gastronômicas para a fusão de pratos tradicionais.",
        "Instituindo espaços onde a moralidade e os tratados ocidentais de guerra não se aplicavam, utilizando armas de repetição massiva contra povos nativos em guerras de massacre total.",
        "Proibindo o uso de caravelas movidas a velas nas rotas fluviais de navegação comercial.",
        "Concedendo cidadania parlamentar a todos os líderes comunitários das aldeias africanas.",
        "Distribuindo ferramentas agrícolas de ferro a famílias camponesas com isenção fiscal integral.",
        "B",
        "Nas colônias, o colonizador europeu sentia-se livre de freios morais: testava metralhadoras em aldeias desarmadas e governava pela chacina; esse massacre colonial preparou os totalitarismos do século XX."
    ))

    questoes_brutas.append((
        8, "EM13CHS601", "basico",
        "Qual território contemporâneo é analisado por Achille Mbembe como modelo emblemático de 'Urbanismo de Cerco' e 'Soberania Vertical'?",
        "O arquipélago das ilhas Galápagos no oceano Pacífico sul.",
        "A ocupação militar israelense nos territórios palestinos da Faixa de Gaza e da Cisjordânia.",
        "O principado de Mônaco na costa litorânea do mar Mediterrâneo.",
        "O vale do rio Danúbio na região central do continente europeu.",
        "As províncias agrícolas do interior da península escandinava.",
        "B",
        "Mbembe estuda a Palestina: o território é fragmentado por muros de oito metros, estradas segregadas e postos de controle; o ocupante domina a água subterrânea, o solo e o ar com drones letais."
    ))

    questoes_brutas.append((
        9, "EM13CHS602", "basico",
        "O que caracteriza a chamada 'Soberania Vertical' descrita por Mbembe na gestão territorial militarizada contemporânea?",
        "A proibição do plantio de árvores frutíferas em áreas urbanas residenciais metropolitanas.",
        "O fatiamento tridimensional do espaço, onde o soberano controla o subsolo (aquíferos e túneis), o solo (muros e postos armados) e o céu (drones assassinos, radares e satélites).",
        "A concessão de incentivos creditícios para a construção de edifícios públicos de tijolo ecológico.",
        "O transporte compulsório de passageiros intermunicipais por linhas ferroviárias eletrificadas.",
        "A delimitação de fronteiras continentais a partir da observação de astros por telescópios óticos.",
        "B",
        "A soberania vertical não olha apenas para o mapa plano: o opressor vigia de cima com satélites e drones, controla os portões e cancelas no chão e confisca os lençóis de água subterrânea no subsolo."
    ))

    questoes_brutas.append((
        10, "EM13CHS603", "basico",
        "O que são as 'Novas Máquinas de Guerra' no diagnóstico de Achille Mbembe sobre a fragmentação contemporânea da soberania?",
        "Equipamentos a vapor inventados para acelerar a fundição de chapas de aço em siderúrgicas.",
        "Atores armados não estatais ou paraestatais (milícias urbanas, cartéis do narcotráfico e empresas privadas de mercenários) que exercem o controle violento sobre territórios e recursos estratégicos.",
        "Locomotivas a carvão construídas para a ligação rápida de capitais provinciais do interior.",
        "Tratores agrícolas automatizados utilizados na colheita mecanizada de lavouras de soja.",
        "Embarcações mercantes modernas projetadas para o transporte intercontinental de contêineres.",
        "B",
        "O Estado perdeu o monopólio da força: mercenários corporativos, cartéis de drogas e milicianos armados viraram máquinas de guerra que dominam territórios, cobram taxas e executam pessoas sumariamente."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Como a necropolítica se manifesta na segurança pública brasileira contemporânea segundo dados do Fórum Brasileiro de Segurança Pública e do Atlas da Violência?",
        "Na distribuição homogênea das mortes violentas por todas as faixas de renda e bairros metropolitanos.",
        "Na disparidade brutal da letalidade policial, em que cerca de 80% dos mortos em intervenções do Estado são jovens negros e pardos das favelas e periferias urbanas.",
        "No recrutamento obrigatório de jovens universitários de classe média para tropas de infantaria armada.",
        "Na isenção tributária concedida a importadores de uniformes de policiais rodoviários federais.",
        "Na obrigatoriedade de julgamento por tribunais comunitários de todas as ocorrências de trânsito urbano.",
        "B",
        "A letalidade policial brasileira tem cor e endereço: oito em cada dez abatidos pela polícia são jovens negros de periferia; o Estado opera a seleção de quais corpos podem ser eliminados com respaldo oficial."
    ))

    questoes_brutas.append((
        12, "EM13CHS102", "basico",
        "Qual mecanismo jurídico-policial é historicamente mobilizado no Brasil para justificar e arquivar homicídios de civis cometidos por policiais?",
        "O alvará consular de livre navegação fluvial em bacias hidrográficas.",
        "O registro sumário de 'Auto de Resistência' (ou morte decorrente de intervenção policial), que presume a legitimidade do ato do agente e bloqueia investigações criminais rigorosas.",
        "A emissão de títulos de nobreza militar a patrulheiros destacados em cidades turísticas.",
        "O contrato comercial de arrendamento de veículos para transporte de passageiros suburbanos.",
        "A ata de conciliação assinada por comissões paroquiais em festivais comemorativos municipais.",
        "B",
        "O 'auto de resistência' serviu como licença burocrática para matar: bastava alegar que a vítima armada revidou para o inquérito ser arquivado, blindando execuções sumárias nas periferias brasileiras."
    ))

    questoes_brutas.append((
        13, "EM13CHS601", "basico",
        "Como o conceito de 'Racismo Ambiental' ilustra a dimensão indireta e estrutural da necropolítica no Brasil?",
        "Pela substituição de calçadas de pedra por canteiros de flores cultivadas por botânicos.",
        "Pela exposição desproporcional e deliberada de populações indígenas, quilombolas e periféricas aos efeitos de desastres ecológicos, contaminações por veneno e falta crônica de saneamento.",
        "Pela imposição de multas administrativas a motoristas que estacionam veículos em praias fluviais.",
        "Pelo incentivo governamental ao cultivo de hortas comunitárias em terraços de edifícios públicos.",
        "Pela proibição de passeios turísticos guiados em parques florestais durante o período de chuvas.",
        "B",
        "O racismo ambiental decide onde o lixo e o veneno são jogados: os rejeitos da mineração, o mercúrio do garimpo e o esgoto a céu aberto são empurrados para os territórios de negros e indígenas."
    ))

    questoes_brutas.append((
        14, "EM13CHS602", "basico",
        "De que modo a situação do Povo Indígena Yanomami, exposta em 2023 com quadros de desnutrição severa e malária, exemplifica a necropolítica por omissão?",
        "Pelo desmantelamento premeditado de postos de saúde, abandono de medicamentos e conivência estatal com o garimpo armado ilegal que envenenou rios e destruiu os meios tradicionais de vida.",
        "Pela recusa espontânea dos povos ancestrais em utilizar embarcações a motor em travessias fluviais.",
        "Pelo congelamento repentino das águas fluviais provocado por variações de correntes polares árticas.",
        "Pela proibição parlamentar da exibição de filmes educativos em aldeias indígenas isoladas da floresta.",
        "Pela transferência forçada de bibliotecas comunitárias para centros de pesquisa em cidades litorâneas.",
        "A",
        "A tragédia Yanomami foi necropolítica de Estado: cortar remédios, desmontar a fiscalização e deixar garimpeiros armados contaminarem as águas com mercúrio é provocar o genocídio por asfixia calculada."
    ))

    questoes_brutas.append((
        15, "EM13CHS603", "basico",
        "Qual é o erro conceitual primário cometido por estudantes ao aplicarem de forma leviana o termo 'Necropolítica'?",
        "Utilizar o conceito para explicar disputas territoriais em conflitos bélicos internacionais.",
        "Confundir a necropolítica com qualquer crime individual ou violência interpessoal privada (como um assalto comum de rua), esquecendo que se trata de uma tecnologia de poder soberano de Estado.",
        "Relacionar o conceito às investigações sociológicas sobre a escravidão nas Américas coloniais.",
        "Associar as teses de Mbembe à crítica de políticas migratórias excludentes de governos europeus.",
        "Vincular o necropoder às análises sobre a militarização do policiamento nas cidades periféricas.",
        "B",
        "Necropolítica não é um assalto cometido por um ladrão na esquina; é uma estratégia soberana e governamental de gestão populacional da morte, executada ou tolerada por instituições de Estado."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Como a tragédia contínua de naufrágios de migrantes e refugiados africanos no Mar Mediterrâneo expressa a necropolítica internacional contemporânea?",
        "Pela realização de desfiles náuticos comemorativos organizados anualmente por armadores europeus.",
        "Pela omissão calculada de socorro em alto-mar, criminalização de navios de ONGs humanitárias e financiamento de guardas costeiras violentas, deixando milhares de vidas negras afogarem-se nas águas.",
        "Pela concessão de passaportes diplomáticos automáticos a todos os tripulantes de barcos pesqueiros.",
        "Pela obrigatoriedade de transporte exclusivo de cargas agrícolas em embarcações de madeira clássica.",
        "Pela instalação de faróis marítimos luminosos em todas as enseadas costeiras do norte da África.",
        "B",
        "A Europa deixa morrer no mar: em vez de resgatar pessoas vulneráveis, prende os ativistas que salvam vidas e patrulha as águas para que os botes afundem longe da costa; a fronteira vira um cemitério líquido."
    ))

    questoes_brutas.append((
        17, "EM13CHS102", "basico",
        "Em sua obra Crítica da Razão Negra, como Achille Mbembe analisa a categoria racial do 'Negro' forjada pela modernidade colonial capitalista?",
        "Como uma categoria estética puramente poética concebida por teatrólogos da Grécia antiga.",
        "Como a primeira mercadoria humana viva do capitalismo global, um ser espoliado de humanidade e reduzido a valor de troca, cuja descartabilidade é o alicerce oculto da acumulação ocidental.",
        "Como uma patente militar concedida a comandantes de caravelas mercantes do mar Mediterrâneo.",
        "Como uma classificação botânica empregada na catalogação de sementes silvestres de lavouras tropicais.",
        "Como um título nobiliárquico honorífico concedido por cortes imperiais a viajantes estrangeiros.",
        "B",
        "A 'Razão Negra' foi a invenção do negro como mercadoria: arrancado de sua terra e precificado na senzala, o homem africano foi o combustível financeiro e o corpo sacrificado para enriquecer o Ocidente."
    ))

    questoes_brutas.append((
        18, "EM13CHS601", "basico",
        "Qual decisão histórica do Supremo Tribunal Federal brasileiro (na ADPF 347) reconheceu a precariedade inconstitucional das prisões, alinhando-se aos diagnósticos da necropolítica carcerária?",
        "A declaração de que os estabelecimentos prisionais operavam como academias de ginástica comunitária.",
        "O reconhecimento formal de que o sistema penitenciário brasileiro vive um 'Estado de Coisas Inconstitucional', marcado por violações massivas, desumanização e superlotação degradante.",
        "A determinação de que todos os presos deveriam receber uniformes de gala confeccionados em linho.",
        "A exigência de que as sentenças condenatórias fossem proferidas em versos poéticos clássicos.",
        "A autorização para que os detentos assumissem cargos honorários em embaixadas consulares no exterior.",
        "B",
        "O STF admitiu o óbvio na ADPF 347: as prisões brasileiras violam frontalmente a dignidade humana; são masmorras superlotadas onde o Estado submete 800 mil pessoas a doenças e à morte civil degradante."
    ))

    questoes_brutas.append((
        19, "EM13CHS602", "basico",
        "Como o uso de helicópteros blindados da polícia realizando disparos aéreos sobre favelas cariocas exemplifica na prática o conceito de 'Soberania Vertical'?",
        "Comprovando a pontualidade horária de voos comerciais entre aeroportos metropolitanos.",
        "Demonstrando como o Estado projeta o poder de matar do ar contra telhados de civis desarmados, suspendendo o direito à vida e convertendo a comunidade inteira em um território sob cerco bélico.",
        "Evidenciando que as operações de segurança utilizavam aeronaves para o plantio aéreo de árvores nativas.",
        "Provando que as patrulhas aéreas eram supervisionadas por conselhos de astrônomos de universidades.",
        "Mostrando que os helicópteros distribuíam gêneros alimentícios e agasalhos para famílias carentes.",
        "B",
        "O 'caveirão do ar' atirando de cima sobre lajes de zinco e escolas é a soberania vertical nua e crua: o Estado cerca a favela pelo ar e despeja chumbo grosso, tratando a comunidade como praça de guerra colonial."
    ))

    questoes_brutas.append((
        20, "EM13CHS603", "basico",
        "Por que, para Mbembe, a necropolítica contemporânea não opera unicamente pelo disparo de projéteis e armas de fogo?",
        "Porque as forças militares foram desmobilizadas e substituídas por tribunais de conciliação voluntária.",
        "Porque ela opera igualmente de modo silencioso e letal através do abandono planejado, da negação de remédios oncológicos, do corte de saneamento, da fome tolerada e do desamparo sanitário estrutural.",
        "Porque os governantes modernos assinaram tratados mundiais que proibiram a fabricação de munições.",
        "Porque a segurança pública passou a ser exercida exclusivamente por sensores térmicos robotizados.",
        "Porque as disputas políticas foram transferidas integralmente para ambientes virtuais de computadores.",
        "B",
        "A necropolítica mata com bala e mata com caneta: cortar o orçamento de remédios, não construir esgoto e deixar o povo passar fome é matar por omissão programada, sem gastar uma cápsula de fuzil."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Como Achille Mbembe articula a relação entre a 'Crise do Estado-Nação' e a proliferação das novas máquinas de guerra privadas na África contemporânea?",
        "Mostrando que os países africanos enriqueceram a ponto de dispensar a presença de forças armadas públicas.",
        "Demonstrando que o enfraquecimento fiscal dos Estados periféricos, induzido por planos de ajuste estrutural, permitiu a corporações privadas e milícias armadas assumirem o controle territorial de enclaves minerais ricos em petróleo, diamantes e coltã através do terror.",
        "Provando que os tratados de comércio de especiarias agrícolas foram unificados por parlamentos rurais.",
        "Afirmando que a segurança de minas de ouro era fiscalizada por congregações religiosas beneditinas.",
        "Sustentando que as milícias locais foram criadas para promover festivais folclóricos de música ancestral.",
        "B",
        "Quando o Estado falha ou recua, surgem milícias e mercenários privados: corporações financiam exércitos mercenários para roubar minérios e esmagar a população local, instaurando enclaves de terror lucrativo."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Em Políticas da Inimizade (2020), como Mbembe descreve a transformação da democracia liberal ocidental diante do avanço do sentimento de medo e da segurança nacional?",
        "Pela ampliação imediata de direitos políticos para cidadãos estrangeiros indocumentados.",
        "Pela mutação da democracia em uma 'sociedade de segurança e inimizade', na qual as garantias constitucionais são paulatinamente corroídas por muros, vigilâncias biométricas e ódio ao estrangeiro.",
        "Pela substituição compulsória de tribunais de justiça criminais por comitês de vizinhança pacíficos.",
        "Pela concessão de passes livres de transporte internacional a todos os estudantes de ciências sociais.",
        "Pelo fechamento voluntário de todas as indústrias bélicas e descarte de fuzis militares em rios.",
        "B",
        "A obsessão por segurança devora a democracia por dentro: os governos liberais erguem muros, monitoram celulares e fecham fronteiras; a democracia liberal adoece de medo e adota práticas do estado policial."
    ))

    questoes_brutas.append((
        23, "EM13CHS601", "intermediario",
        "Qual é a relação genealógica direta estabelecida por Mbembe entre a desumanização do escravizado na plantação americana e a figura moderna do 'Morto-Vivo' nos campos de concentração?",
        "Em ambos os espaços vigora uma rotina de trabalho regulada por sinos e descansos semanais remunerados.",
        "Tanto na plantação escravocrata quanto no campo de concentração, os sujeitos foram rebaixados à condição de corpos sem proteção jurídica, cuja existência é despojada de soberania e submetida ao arbítrio de morte do opressor.",
        "Nas duas instituições os internos recebiam assistência médica preventiva de alta especialização.",
        "Nos dois modelos históricos os reclusos possuíam o direito de eleger seus próprios representantes cívicos.",
        "Em ambos os territórios a alimentação era composta exclusivamente por frutos silvestres colhidos na mata.",
        "B",
        "A senzala pariu o campo: o que os nazistas fizeram nos anos 1940 com os prisioneiros judeus (tirar seus direitos e usá-los como corpos descartáveis) os impérios ocidentais já faziam séculos antes com os negros."
    ))

    questoes_brutas.append((
        24, "EM13CHS602", "intermediario",
        "De que maneira a exploração de minérios raros como o 'Coltã' (columbita-tantalita) na República Democrática do Congo alimenta as redes necropolíticas transnacionais?",
        "Incentivando a criação de parques botânicos públicos dedicados à conservação da fauna e flora locais.",
        "Financiando milícias sanguinárias que escravizam populações locais e crianças em minas precárias para abastecer de componentes eletrônicos a milionária indústria ocidental de smartphones e computadores.",
        "Promovendo a elevação generalizada dos salários pagos a engenheiros mecânicos congoleses.",
        "Permitindo que as receitas da exportação de minérios sejam distribuídas igualmente a todas as famílias rurais.",
        "Garantindo a estabilidade institucional e a pacificação duradoura das fronteiras da África Central.",
        "B",
        "Nossos celulares carregam sangue necropolítico: o coltã do chip é extraído por crianças congolesas sob o fuzil de milícias patrocinadas pelo comércio internacional; o luxo tecnológico repousa no inferno mineral."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "Como a categoria de 'Morte Civil' desenvolvida na análise da plantação escravocrata se aplica aos indivíduos submetidos ao sistema carcerário brasileiro contemporâneo?",
        "Garantindo aos detentos o acesso irrestrito a linhas de crédito imobiliário subsidiadas pelo governo.",
        "Evidenciando que, embora biologicamente vivos, os encarcerados perdem direitos políticos, têm sua voz social cancelada, habitam celas insalubres e sofrem estigmatização perpétua que bloqueia sua reinserção digna.",
        "Assegurando a concessão de títulos acadêmicos honorários a todos os custodiados com boa conduta.",
        "Permitindo que os réus condenados presidam audiências públicas em assembleias legislativas estaduais.",
        "Transferindo a administração dos presídios para associações cooperativas de tecelões industriais.",
        "B",
        "Estar preso no Brasil é sofrer morte civil: perde-se a cidadania, o respeito e a saúde; amontoados em masmorras imundas, os presos viram zumbis para a sociedade, marcados pelo estigma eterno do cárcere."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "De que modo a filosofia de Mbembe dialoga com a tese de Giorgio Agamben sobre o 'Estado de Exceção Permanente'?",
        "Afirmando que a normalidade constitucional vigora com plena solidez em todas as fronteiras periféricas.",
        "Mostrando que, nas colônias de ontem e nos mundos de morte de hoje, a exceção não é um evento pontual de crise passageira, mas a própria matriz habitual de gestão territorial e militar das vidas descartáveis.",
        "Comprovando que os tratados de extradição internacional dependem da concordância de chefes tribais.",
        "Sustentando que as cortes de justiça marciais deixam de operar em períodos de colheita agrícola.",
        "Provando que as constituições liberais foram escritas exclusivamente por marinheiros veteranos de guerras navais.",
        "B",
        "Para a favela e para a colônia, a exceção sempre foi a regra: ninguém precisa declarar estado de sítio formal para invadir um barraco sem mandado; a violência desmedida é o modo normal de o poder operar ali."
    ))

    questoes_brutas.append((
        27, "EM13CHS102", "intermediario",
        "Por que, segundo Achille Mbembe, as democracias liberais ocidentais enfrentam uma 'fratura ética' irreparável ao celebrarem os Direitos Humanos em suas capitais?",
        "Porque as convenções de direitos humanos foram traduzidas em dialetos de difícil memorização pública.",
        "Porque proclamam solenemente a universalidade da dignidade humana em seus fóruns metropolitanos enquanto terceirizam a violência, erguem muros contra refugiados e pilham os recursos do Sul Global.",
        "Porque os juízes de cortes internacionais utilizavam vestimentas confeccionadas com fios de algodão cru.",
        "Porque as assembleias parlamentares metropolitanas fechavam suas galerias durante feriados municipais.",
        "Porque as declarações constitucionais proibiam a importação de especiarias agrícolas de colônias ultramarinas.",
        "B",
        "O cinismo europeu denunciado por Mbembe e Fanon: falam em direitos universais do homem na ONU e em Paris, mas deixam barcos de refugiados negros afundarem e compram minérios de guerras sangrentas na África."
    ))

    questoes_brutas.append((
        28, "EM13CHS601", "intermediario",
        "Como a teoria necropolítica de Mbembe desconstrói a visão weberiana clássica de que o Estado Moderno detém o 'monopólio legítimo da violência física'?",
        "Provando que as patrulhas policiais urbanas foram extintas e substituídas por guardas florestais voluntários.",
        "Demonstrando a privatização e proliferação de atores violentos autônomos (milícias, empresas mercenárias e cartéis) que operam paralelamente ao Estado ou em simbiose com ele, fatiando a soberania da morte.",
        "Evidenciando que os crimes violentos foram completamente erradicados através da expansão de ferrovias.",
        "Sustentando que os governantes republicanos deixaram de utilizar recursos orçamentários na segurança pública.",
        "Afirmando que a autoridade soberana passou a ser exercida unicamente por comissões de filologia clássica.",
        "B",
        "Weber dizia que só o Estado tem a arma legal; Mbembe mostra que hoje a violência foi privatizada: milícias e cartéis disputam o poder com a polícia, dividindo as cidades e exercendo poder de vida e morte."
    ))

    questoes_brutas.append((
        29, "EM13CHS602", "intermediario",
        "De que maneira o desastre criminoso do rompimento da barragem de Brumadinho (2019) ilustra a confluência entre a ganância corporativa e a necropolítica ambiental?",
        "Pela substituição voluntária de barragens de terra por estruturas construídas com blocos de mármore.",
        "Pela decisão consciente da mineradora corporativa de priorizar a maximização de lucros e dividendos a acionistas, negligenciando laudos de instabilidade e sacrificando vidas de trabalhadores e comunidades pobres.",
        "Pela transferência forçada de funcionários de minas para escritórios administrativos em cidades litorâneas.",
        "Pelo pagamento antecipado de indenizações astronômicas a todas as famílias residentes nas encostas.",
        "Pela proibição parlamentar do uso de caminhões pesados em estradas municipais vizinhas às represas.",
        "B",
        "Brumadinho foi necropolítica corporativa: a empresa sabia dos riscos de colapso, mas calculou que o lucro das ações valia mais do que as vidas dos trabalhadores; a lama tóxica soterrou e matou com a frieza do cálculo."
    ))

    questoes_brutas.append((
        30, "EM13CHS603", "intermediario",
        "Como a 'Governança Algorítmica da Segurança' contemporânea (reconhecimento facial e policiamento preditivo) reproduz os padrões da necropolítica nas cidades?",
        "Corrigindo espontaneamente todas as distorções históricas de renda entre trabalhadores de diferentes classes.",
        "Alimentando sistemas informatizados com bancos de dados enviesados que tratam traços fenotípicos negros como suspeitos por padrão, direcionando o policiamento ostensivo e prisões arbitrárias contra periferias.",
        "Proibindo o uso de câmeras digitais de vigilância em áreas residenciais de bairros metropolitanos nobres.",
        "Assegurando o sigilo absoluto de dados biométricos de cidadãos em trânsito por postos de fronteira aérea.",
        "Determinando que os algoritmos de busca devam exibir exclusivamente biografias de filósofos do Iluminismo.",
        "B",
        "O algoritmo aprendeu o racismo da sociedade: câmeras de vigilância confundem jovens negros com foragidos e a polícia invade bairros pobres orientada por 'mapas de calor'; a necropolítica ganha roupagem digital."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Qual é o significado do conceito mbembeano de 'Descartabilidade dos Corpos' na dinâmica do capitalismo global contemporâneo?",
        "A reciclagem industrial compulsória de componentes plásticos descartados em praias públicas.",
        "A produção estrutural de massas populacionais que se tornaram economicamente inúteis e supérfluas tanto para a produção quanto para o consumo, cuja contenção e eliminação violenta tornam-se rotina de Estado.",
        "A distribuição equitativa de agasalhos térmicos para trabalhadores rurais durante geadas de inverno.",
        "A demolição controlada de edifícios fabris desativados em centros urbanos para a construção de praças.",
        "A substituição de ferramentas de ferro por instrumentos de cerâmica nas lavouras camponesas.",
        "B",
        "O capitalismo atual não precisa mais de tantos braços operários: milhões de jovens da periferia viraram 'sobras' do mercado; sem emprego e sem direitos, são geridos pela polícia como lixo humano descartável."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Em Necropolítica, como Achille Mbembe analisa a coexistência e a articulação complementar entre a Biopolítica e a Necropolítica na gestão do capitalismo global contemporâneo?",
        "Afirmando que a biopolítica desapareceu integralmente após os conflitos armados do século XX.",
        "Demonstrando que a biopolítica é reservada preferencialmente para gerir, proteger e prolongar a vida das populações ricas e brancas dos países centrais, ao passo que a necropolítica atua como a retaguarda violenta nas periferias, fronteiras e no Sul Global para policiar, conter e expor à morte os corpos considerados descartáveis.",
        "Comprovando que as políticas sanitárias são coordenadas exclusivamente por conselhos de navegadores mercantes.",
        "Sustentando que os governos contemporâneos aboliram o uso de forças policiais armadas em áreas urbanas.",
        "Afirmando que as disparidades sociais decorrem unicamente da ausência de ferrovias em áreas rurais.",
        "B",
        "Mbembe não descarta Foucault: a biopolítica cuida dos bairros nobres e dos países ricos (saúde, vacina, longevidade), enquanto a necropolítica é a face de ferro que cerca favelas e fronteiras do Sul Global com fuzis e descaso."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "De que modo a cobertura da grande imprensa comercial frequentemente atua como legitimadora da necropolítica nas periferias brasileiras?",
        "Questionando rigorosamente todos os relatórios policiais e ouvindo prioritariamente os moradores locais.",
        "Adotando a narrativa policial acriticamente, rotulando sumariamente todas as vítimas de tiroteios como 'suspeitos' ou 'traficantes' antes de qualquer perícia, justificando a violência fatal diante da opinião pública.",
        "Interrompendo a programação de transmissões esportivas para ler tratados de direito constitucional.",
        "Concedendo prêmios de reportagem investigativa exclusivamente a matérias sobre agroecologia florestal.",
        "Recusando a veiculação de imagens de intervenções armadas para preservar o sossego das famílias.",
        "B",
        "A imprensa sensacionalista chapa-branca valida a matança: se a polícia atira e mata um rapaz negro, a manchete já chama a vítima de 'suspeito abatido'; cria-se o clima de conformismo moral perante a barbárie."
    ))

    questoes_brutas.append((
        34, "EM13CHS602", "intermediario",
        "Qual é a relação entre as reflexões de Achille Mbembe e as denúncias de Sueli Carneiro sobre o 'Biopoder e Dispositivo de Racialidade' no Brasil?",
        "Ambos sustentam que a escravidão foi abolida sem deixar marcas materiais nas instituições republicanas.",
        "Ambos demonstram que a raça opera como o grande dispositivo ordenador da distribuição de privilégios e violências: enquanto corpos brancos são protegidos pelo biopoder, corpos negros são expostos à morte necropolítica.",
        "Os dois pensadores concordam que o racismo é um fenômeno acidental decorrente unicamente da má educação.",
        "Ambos propõem que o combate às desigualdades deve ser delegado a companhias de comércio marítimo.",
        "Os dois autores afirmam que as ciências biológicas do século XIX desconheciam as divisões humanas em raças.",
        "B",
        "Mbembe e Sueli Carneiro convergem na precisão: a raça é a linha divisória do Estado brasileiro; quem nasce branco recebe biopolítica (creche, hospital, asfalto), quem nasce negro recebe necropolítica (tiro e cadeia)."
    ))

    questoes_brutas.append((
        35, "EM13CHS603", "intermediario",
        "Como as políticas de 'Tolerância Zero' e 'Guerra às Drogas' implementadas nas Américas servem como justificativa discursiva para a ampliação do necropoder?",
        "Reduzindo significativamente o número de armas de fogo em circulação no mercado consumidor civil.",
        "Criando a ilusão de um conflito moral inadiável contra um inimigo químico e armado abstrato, sob cuja bandeira se militarizam as cidades, suspendem-se garantias processuais e autorizam-se execuções em bairros pobres.",
        "Estimulando a substituição de prisões fechadas por oficinas terapêuticas de artesanato em palha de milho.",
        "Transferindo a coordenação da segurança de capitais para conselhos de professores de história antiga.",
        "Concedendo remissões de penas judiciais a todos os réus que concluírem cursos de jardinagem urbana.",
        "B",
        "A 'guerra às drogas' nunca acabou com o consumo de substâncias; sua função real é justificar a invasão de favelas, o massacre de jovens negros e o encarceramento massivo em nome de uma cruzada moral hipócrita."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Por que, para Mbembe, as cercas de arame farpado e os campos de concentração não são aberrações medievais, mas criações plenamente e tipicamente modernas do capitalismo industrial?",
        "Porque as máquinas de fabricação de arames utilizavam correias de couro importadas da Ásia Menor.",
        "Porque a modernidade capitalista refinou o cálculo burocrático, a compartimentação espacial racional e a tecnologia de gestão de massas, colocando a ciência e a técnica a serviço do confinamento e da destruição humana.",
        "Porque os primeiros campos de prisioneiros foram edificados por monges copistas em vales montanhosos.",
        "Porque os arames farpados eram utilizados para delimitar pistas de corrida de carruagens aristocráticas.",
        "Porque os manuais militares de confinamento foram copiados de tratados de jurisprudência bizantina antiga.",
        "B",
        "O campo de concentração não é barbárie do passado: ele usa trens velozes, química industrial, listas datilografadas e engenharia moderna; é a tecnologia do capitalismo moderno posta a serviço da morte organizada."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "De que modo a militarização da vida cotidiana e o avanço das milícias no Rio de Janeiro concretizam o diagnóstico mbembeano de 'Fusão entre Crime, Negócio e Poder Armado'?",
        "Provando que as comunidades periféricas alcançaram a autonomia econômica através de feiras cooperativas.",
        "Evidenciando grupos que combinam o domínio de armas de fogo pesadas, cobrança forçada de taxas de segurança de comerciantes, monopólio de botijões de gás e internet com conexões e imunidades nos poderes políticos locais.",
        "Mostrando que os condomínios residenciais adotaram regras de moradia baseadas na caridade monástica.",
        "Provando que a ordem pública nas praias depende unicamente da fiscalização de fiscais sanitários civis.",
        "Sustentando que as facções armadas desapareceram com a inauguração de estações de metrô de superfície.",
        "B",
        "A milícia é a máquina de guerra do século XXI: policiais e bandidos unidos no mesmo negócio, fuzil na mão cobrando pedágio de moradores pelo botijão de gás e pela internet, com padrinhos eleitos nos parlamentos."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Qual é a crítica de Achille Mbembe ao 'Iluminismo Eurocêntrico' no ensaio Necropolítica?",
        "Critica o fato de os filósofos das luzes terem redigido suas obras em línguas nacionais vernáculas.",
        "Denuncia que o Iluminismo proclamou o primado da Razão e a emancipação humana enquanto convivia tranquilamente com o comércio negreiro transatlântico e a escravização nas colônias, naturalizando a barbárie racial.",
        "Acusa os enciclopedistas franceses de terem omitido dados sobre o cultivo de beterrabas açucareiras.",
        "Afirma que os pensadores iluministas recusavam utilizar relógios de pêndulo em suas bibliotecas privadas.",
        "Sustenta que as academias científicas do século XVIII eram sustentadas por doações de pastores de ovelhas.",
        "B",
        "A grande hipocrisia iluminista: Voltaire, Kant e Locke falavam em liberdade e igualdade enquanto a Europa enchia porões de navios negreiros com seres humanos acorrentados; o lado escuro da Razão é o racismo colonial."
    ))

    questoes_brutas.append((
        39, "EM13CHS602", "intermediario",
        "Como a necropolítica opera na gestão da crise climática global, dividindo desigualmente os custos ecológicos entre os povos do planeta?",
        "Distribuindo tempestades tropicais de modo idêntico e equilibrado por todas as capitais mundiais.",
        "Fazendo com que os países e populações mais pobres do Sul Global (que menos emitiram carbono na história) sofram secas severas, inundações mortais e perda de terras, enquanto as elites do Norte se blindam com muros.",
        "Exigindo que todos os habitantes do planeta utilizem unicamente embarcações a remo em viagens marinhas.",
        "Transferindo a posse de todas as indústrias petroquímicas para fundações filantrópicas monásticas.",
        "Obrigando as cidades litorâneas a suspenderem o fornecimento de energia elétrica durante o inverno.",
        "B",
        "O apartheid climático: quem esquentou o planeta foram as fábricas ricas do Norte; quem morre de sede, fome e deslizamento de terra são os povos da África, Ásia e favelas latino-americanas sem proteção alguma."
    ))

    questoes_brutas.append((
        40, "EM13CHS603", "intermediario",
        "Por que, para Mbembe, a superação da necropolítica exige uma 'Ética do Passante' e o reconhecimento de uma Terra comum compartilhada?",
        "Porque os passaportes diplomáticos internacionais deveriam ser impressos em folhas de papiro egípcio.",
        "Porque a humanidade só poderá romper a espiral do massacre e do extermínio se abandonar a lógica da inimizade e da fronteira murada, reconhecendo que a vida é precária e que todos os seres vivos dividem o mesmo mundo.",
        "Porque os viajantes intercontinentais devem ser obrigados a plantar mudas de videiras em suas escalas.",
        "Porque os tratados de paz mundial dependem da renúncia compulsória ao uso de aparelhos de telefonia móvel.",
        "Porque as assembleias internacionais devem proferir seus discursos unicamente na língua hebraica antiga.",
        "B",
        "Contra o ódio e o muro, Mbembe propõe a ética do cuidado comum: a Terra não pertence a um grupo soberano que pode matar os outros; ou aprendemos a conviver na mesma casa planetária ou o necropoder devorará a todos."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a superação crítica da biopolítica operada por Achille Mbembe em Necropolítica: de que maneira o filósofo camaronês demonstra que o paradigma da soberania moderna, quando analisado a partir das margens coloniais, não repousa sobre a gestão da vida, mas sobre o exercício absoluto da faculdade soberana de matar?",
        "Provando que as academias militares do século XVIII utilizavam tratados de cavalaria clássica grega.",
        "Evidenciando que a formulação foucaultiana do biopoder permaneceu prisioneira do horizonte eurocêntrico da pacificação interna metropolitana; ao deslocar o eixo da análise para a colônia e para o Sul Global, Mbembe desvela que a modernidade produziu enclaves onde a soberania se expressa como o poder supremo de matar, ferir, expor ao terror e produzir massas de mortos-vivos, tornando a necropolítica o verdadeiro substrato material do poder global.",
        "Determinando que as patrulhas aduaneiras deviam realizar inspeções portuárias unicamente sob a luz solar.",
        "Afirmando que a soberania estatal se consolidou com a fundação de hospitais administrados por tecelões.",
        "Comprovando que as guerras coloniais eram disputadas através de torneios pacíficos de esgrima naval.",
        "B",
        "- **Etapa 1:** Compreender o limite do modelo foucaultiano: Foucault pensou o biopoder ('fazer viver e deixar morrer') a partir do bem-estar, das vacinas e das polícias urbanas das capitais europeias.\n- **Etapa 2:** Desvelar a virada necropolítica de Mbembe: fora da Europa, a soberania nunca foi benevolente; o império sempre governou mandando matar e criando campos de morte; a necropolítica revela que o poder moderno tem no assassinato gerido a sua verdadeira essência."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a genealogia da necropolítica na 'Plantação Escravocrata Moderna' dissecada por Mbembe: como a conjunção entre a perda do lar territorial, a coisificação mercantil do corpo negro e a anulação civil do sujeito escravizado inaugurou o laboratório do biopoder violento na modernidade?",
        "Mostrando que as frotas de navios negreiros utilizavam cordas fabricadas com cânhamo de lavouras alpinas.",
        "Demonstrando que a plantação operou a primeira desumanização industrial e jurídica em massa do capitalismo moderno: o homem negro escravizado foi transformado em propriedade física descartável (*res*), despido de direitos e submetido ao poder de morte ilimitado do senhor, criando um espaço de exceção permanente que antecipou os métodos de extermínio industrial do século XX.",
        "Determinando que os capatazes de engenho deveriam prestar exames de literatura latina antes das contratações.",
        "Afirmando que as lavouras de cana-de-açúcar coloniais funcionavam como cooperativas agrárias fraternas.",
        "Provando que os escravizados eram protegidos por tratados de mediação civil assinados em praças consulares.",
        "B",
        "- **Etapa 1:** Reconstruir a tripla espoliação do escravizado na plantação: perda da terra natal, perda da propriedade sobre o próprio corpo e morte civil perante a lei colonial.\n- **Etapa 2:** Concluir sobre a senzala como berço do terror moderno: a plantação provou que o capitalismo é capaz de tratar vidas humanas como ferramentas de consumo e descarte; essa engrenagem de crueldade calculada foi a raiz de todos os campos de concentração posteriores."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Examine a tese de Achille Mbembe sobre as 'Políticas da Inimizade' e a fabricação discursiva do 'Inimigo Absoluto': de que maneira a inculcação social do medo, do pânico moral e da neurose securitária legitima a exceção jurídica e autoriza o massacre de grupos marginalizados pelo Estado sem provocar indignação pública?",
        "Comprovando que os comitês de censura teatral atuavam unicamente em comemorações cívicas municipais.",
        "Evidenciando que o necropoder educa a população para enxergar certos grupos sociais (jovens negros da favela, imigrantes e refugiados) não como concidadãos dotados de direitos, mas como uma ameaça biológica degenerada cuja destruição física é celebrada como um ato indispensável de profilaxia social e defesa da civilização, suspendendo a empatia e normalizando a barbárie estatal.",
        "Determinando que os orçamentos de defesa devam ser aprovados em escrutínios secretos de guildas rurais.",
        "Afirmando que as teorias de inimizade foram formuladas por monges solitários em retiros espirituais alpinos.",
        "Provando que a ordem pública metropolitana dependia da proibição da venda de tecidos de linho importados.",
        "B",
        "- **Etapa 1:** Investigar a psicologia coletiva do medo: quando os jornais e políticos repetem que 'eles vão invadir nossas casas e destruir nossas famílias', o medo cega a sociedade.\n- **Etapa 2:** Desvelar a autorização moral para o massacre: transformado em monstro pela propaganda de segurança, o morador da periferia pode ser abatido com um tiro na nuca sem que a classe média se comova; a inimizade anestesia a consciência coletiva."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Analise a anatomia do 'Urbanismo de Cerco' e da 'Soberania Vertical' nos territórios ocupados da Palestina descrita em Necropolítica: como a sobreposição tridimensional de barreiras de concreto, postos de controle biométricos, controle de aquíferos subterrâneos e patrulhamento aéreo por drones assassinos opera o estrangulamento da vida sitiada?",
        "Provando que as rodovias segregadas foram construídas para viabilizar corridas de carruagens desportivas.",
        "Demonstrando que o poder ocupante fragmenta e asfixia a população através de uma arquitetura total de guerra: confisca a água no subsolo, impede a locomoção na superfície através de muros e bloqueios humilhantes que separam famílias e hospitais, e aterroriza pelo céu com zumbidos contínuos de aeronaves letais, reduzindo os palestinos a corpos em suspensão de sobrevivência.",
        "Determinando que as cercas territoriais devam ser decoradas com motivos florais de espécies nativas.",
        "Afirmando que os postos de controle militar foram desenhados por comissões de arqueólogos universitários.",
        "Comprovando que as restrições de trânsito vigoravam exclusivamente durante períodos de tempestades de granizo.",
        "B",
        "- **Etapa 1:** Descrever o fatiamento tridimensional do espaço de cerco: o poder não controla apenas as fronteiras no mapa; ele controla a água embaixo da terra, coloca arames no chão e drones no ar.\n- **Etapa 2:** Diagnosticar o sofrimento da população sitiada: a vida diária vira um pesadelo onde uma ambulância leva horas no checkpoint para passar com um doente; o território é transformado em um imenso campo de concentração a céu aberto."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Investigue o surgimento das 'Novas Máquinas de Guerra' no século XXI segundo Mbembe: como a fragmentação e privatização da violência armada (empresas mercenárias, facções do narcotráfico e milícias) subvertem a teoria clássica hobbesiana e weberiana do Estado como guardião soberano da paz e da lei?",
        "Mostrando que os soldados de infantaria moderna utilizam elmos metálicos forjados em bigornas artesanais.",
        "Evidenciando que o monopólio estatal da força desmoronou em vastas regiões periféricas, dando lugar a corporações bélicas nômades e milícias violentas que disputam enclaves de extração mineral predatória e rotas ilícitas através do terror, governando populações sem qualquer pretensão de construir pactos sociais republicanos ou instituições de cidadania.",
        "Determinando que os tratados de cessar-fogo internacional devam ser gravados em placas de bronze polido.",
        "Afirmando que os exércitos privados contemporâneos foram fundados por congregações monásticas beneditinas.",
        "Provando que as facções armadas dependiam da aprovação prévia concedida por tribunais marítimos consulares.",
        "B",
        "- **Etapa 1:** Recordar o dogma de Hobbes e Weber: o Estado existe para deter o monopólio das armas e proteger a vida dos cidadãos contra a guerra de todos contra todos.\n- **Etapa 2:** Revelar a mutação das máquinas de guerra de Mbembe: no capitalismo desregulado, mercenários corporativos e milícias armadas dominam bairros e minas com fuzis; o Estado abdica da lei e o território vira couto de caça e espoliação armada privada."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Analise a relação entre a 'Letalidade Policial Seletiva' no Brasil e a figura jurídica do 'Homo Sacer' recuperada por Agamben e Mbembe: por que a morte de jovens negros nas favelas brasileiras ocorre sob um regime prático de impunidade e desvalor moral?",
        "Comprovando que as câmeras acopladas a fardamentos operam com pilhas alcalinas de baixa duração.",
        "Demonstrando que, na prática cotidiana das operações de segurança e do sistema judiciário, o corpo negro periférico é despido de sua cidadania e rebaixado à condição de vida nua matável: o policial que o abate em intervenções armadas não é punido, a promotoria arquiva o caso como 'resistência' e a sociedade aceita o óbito com naturalidade, provando a vigência da necropolítica.",
        "Determinando que os policiais de patrulha devam prestar juramentos de cavalaria em capelas militares.",
        "Afirmando que as mortes em operações de segurança decorrem unicamente de defeitos de fabricação de projéteis.",
        "Provando que as investigações de homicídios dependiam de autorização expressa de comissões astronômicas.",
        "B",
        "- **Etapa 1:** Relembrar a figura do Homo Sacer: o indivíduo que foi expulso da proteção da lei e cuja morte não conta como assassinato perante a sociedade.\n- **Etapa 2:** Enxergar a realidade brasileira: quando a polícia mata um jovem negro na favela com um tiro nas costas, quase nunca há julgamento ou condenação; o corpo negro é tratado pelo Estado como vida descartável que pode ser executada sem crime."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Examine o conceito de 'Racismo Ambiental' à luz da necropolítica: de que maneira desastres como Mariana (2015), Brumadinho (2019) e o envenenamento dos rios Yanomami por mercúrio expressam a decisão soberana de sacrificar territórios e populações periféricas em benefício da acumulação do grande capital?",
        "Provando que as barragens de rejeitos minerais eram construídas com materiais cerâmicos biodegradáveis.",
        "Evidenciando que as escolhas sobre onde instalar estruturas perigosas, onde tolerar contaminações tóxicas de águas e onde cortar fiscalizações de segurança não são neutras: elas sacrificam deliberadamente as terras ancestrais de povos indígenas, quilombolas e ribeirinhos, tratando seus habitantes como populações dispensáveis que podem ser intoxicadas e soterradas para gerar lucros extraordinários a mineradoras.",
        "Determinando que as bacias hidrográficas devam ser administradas unicamente por comissões de pescadores artesanais.",
        "Afirmando que as rupturas de barragens resultavam unicamente de movimentos tectônicos imprevisíveis no interior.",
        "Comprovando que as comunidades atingidas por rejeitos recebiam previamente alvarás de reassentamento em ilhas.",
        "B",
        "- **Etapa 1:** Desmascarar o mito do desastre ecológico 'acidental': mineradoras e o Estado sabem dos riscos, mas escolhem economizar em segurança para pagar bilhões em dividendos na bolsa de valores.\n- **Etapa 2:** Reconhecer a seletividade racial e social da morte: a lama nunca soterra bairros nobres de capitais; ela soterra aldeias indígenas e vilas pobres; o racismo ambiental é o braço ecológico da necropolítica."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Examine a tese historiográfica e filosófica presente em Necropolítica que conecta a escravidão moderna nas Américas ao desenvolvimento do capitalismo industrial ocidental (articulando as teses de Eric Williams e C.L.R. James): por que a plantação escravocrata não deve ser compreendida como um arcaísmo pré-moderno, mas como o próprio motor originário da acumulação capitalista global?",
        "Provando que as frotas de caravelas utilizavam velas tecidas com linho importado de portos bálticos.",
        "Demonstrando que o comércio triangular de africanos escravizados e a superexploração mortal nas lavouras coloniais de cana e algodão geraram os lucros astronômicos e o capital primitivo acumulado que financiaram diretamente a Revolução Industrial britânica e europeia, evidenciando que a riqueza e as instituições liberais do Ocidente foram construídas sobre a violência necropolítica da escravidão.",
        "Determinando que os proprietários agrícolas deviam pagar salários fixados em barras de cobre fundido.",
        "Afirmando que o comércio triangular foi inventado por monges beneditinos em mosteiros alpinos.",
        "Comprovando que as mercadorias coloniais eram transportadas unicamente por tração animal terrestre.",
        "B",
        "- **Etapa 1:** Desmistificar a narrativa liberal de que a escravidão foi um atraso feudal isolado: a historiografia de Williams e James comprova que a senzala financiou as fábricas de Manchester e os bancos de Londres.\n- **Etapa 2:** Revelar a base necropolítica da riqueza moderna: o capitalismo não nasceu da pura inovação técnica descolada da violência; ele nasceu da pilhagem de corpos negros na plantação, provando a tese de Mbembe de que a morte gerida é a base material da ordem ocidental."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Analise a relação entre o 'Encarceramento em Massa' e a produção da morte civil no Brasil: de que maneira o aprisionamento de mais de 800 mil pessoas — a maioria jovens negros sem condenação definitiva — opera como um dispositivo necropolítico de gestão e neutralização da juventude periférica?",
        "Provando que as prisões nacionais foram projetadas por arquitetos com base em mosteiros beneditinos da Itália.",
        "Evidenciando que o sistema carcerário brasileiro não visa reabilitar cidadãos, mas funcionar como um depósito humano de segregação e destruição física e moral: o confinamento em condições medievais de insalubridade, fome e tuberculose neutraliza politicamente a juventude negra e pobre, submetendo-a à morte civil sob o beneplácito de decisões judiciais punitivistas.",
        "Determinando que os estabelecimentos penais devam fornecer cursos regulares de filologia e latim aos detentos.",
        "Afirmando que a expansão prisional decorreu do crescimento desordenado de fábricas de tecidos de linho.",
        "Comprovando que as penas de reclusão eram decididas através de sorteios anuais realizados em praças públicas.",
        "B",
        "- **Etapa 1:** Descrever o quadro do sistema carcerário: superlotação, esgoto correndo nas celas, doenças contagiosas e 40% dos presos aguardando julgamento por anos por porte de poucas gramas de entorpecentes.\n- **Etapa 2:** Revelar a engrenagem necropolítica: o cárcere atua como uma máquina de triturar corpos negros e pobres; em vez de escolas e empregos, o Estado oferece grades e abandono, administrando a exclusão pela jaula."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Examine a crítica de Achille Mbembe à 'Gestão Neoliberal das Fronteiras' na União Europeia: como a transformação do Mar Mediterrâneo em uma gigantesca vala comum revela que o humanismo europeu é subordinado à lógica necropolítica de defesa da fortaleza branca?",
        "Comprovando que as águas do Mediterrâneo foram poluídas por vazamentos de óleo de caravelas mercantes antigas.",
        "Demonstrando que, ao recusar o resgate de botes à deriva, criminalizar militantes humanitários que salvam náufragos e terceirizar a contenção armada para milícias líbias notórias por torturas, a Europa decide soberanamente que as vidas de africanos e asiáticos não merecem ser salvas, tratando o mar como uma cerca líquida necropolítica de contenção da miséria.",
        "Determinando que as frotas pesqueiras devam utilizar redes tecidas exclusivamente com fibras de sisal cru.",
        "Afirmando que os naufrágios migratórios resultavam unicamente de desvios magnéticos de bússolas marítimas.",
        "Provando que as leis de asilo político europeias foram formuladas por conselhos de mercadores de especiarias.",
        "B",
        "- **Etapa 1:** Contrastar a retórica europeia com a prática de fronteira: a Europa se diz o berço da civilização e da fraternidade universal, mas assiste indiferente a crianças refugiadas morrerem afogadas.\n- **Etapa 2:** Desvelar a necropolítica de fronteira: deixar morrer no mar é uma decisão calculada de dissuasão; a Europa prefere transformar o Mediterrâneo em cemitério a acolher seres humanos negros e empobrecidos em fuga de guerras."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Investigue o conceito mbembeano de 'Mundos de Morte' aplicado às favelas cariocas sob intervenção militar e policial contínua: de que maneira o confinamento sob tiroteios rotineiros e o uso de helicópteros armados suspendem a cidadania e forjam a condição de 'Morto-Vivo' para os moradores periféricos?",
        "Mostrando que os operários da construção civil utilizavam ferramentas fabricadas com cobre martelado à mão.",
        "Evidenciando que a rotina das favelas sitiadas desmantela a estrutura psíquica e material da existência: escolas e creches são fechadas sob disparos, postos de saúde cancelam atendimentos, trabalhadores vivem com medo constante de balas perdidas e o direito à integridade física é anulado, rebaixando os residentes à condição existencial de mortos-vivos cercados pela violência letal do Estado.",
        "Determinando que os telhados das casas populares sejam pintados exclusivamente com tintas ecológicas azuis.",
        "Afirmando que as incursões policiais eram planejadas por comissões de professores de astronomia clássica.",
        "Comprovando que os confrontos armados decorriam da escassez de farinha de trigo em padarias comunitárias.",
        "B",
        "- **Etapa 1:** Compreender a experiência concreta de morar na favela sob cerco: a mãe não sabe se o filho volta vivo da escola; o trabalhador passa a noite agachado no corredor para escapar de tiros de fuzil.\n- **Etapa 2:** Reconhecer o 'morto-vivo' de Mbembe: a cidadania vira fumaça; as pessoas habitam uma suspensão dolorosa onde a morte pode cair do céu a qualquer segundo, provando a existência dos mundos de morte no Brasil."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Analise a relação entre o 'Neoliberalismo Extrativista' e a proliferação das máquinas de guerra na América Latina contemporânea: como o assassinato sistemático de lideranças indígenas, quilombolas e ambientalistas na Amazônia brasileira manifesta o necropoder a serviço do agronegócio e do garimpo?",
        "Comprovando que os conflitos agrários eram motivados pela ausência de cercas eletrificadas em fazendas.",
        "Demonstrando como grileiros armados, jagunços de madeireiras e garimpeiros ilegais atuam como milícias paraestatais violentas que assassinam ativistas e invadem terras protegidas com apoio tácito ou omissão de setores do Estado, utilizando o terror para impor a destruição florestal e a extração predatória de recursos naturais lucrativos.",
        "Determinando que os títulos de demarcação territorial devam ser redigidos em pergaminhos com tintas minerais.",
        "Afirmando que as mortes de ambientalistas decorriam exclusivamente de ataques de animais selvagens na selva.",
        "Provando que as patrulhas rurais eram fiscalizadas por comissões de navegadores marítimos mercantes.",
        "B",
        "- **Etapa 1:** Descrever o conflito na fronteira amazônica: quem defende a árvore, a água e a terra indígena enfrenta pistoleiros armados a soldo de madeireiros e grileiros de terras públicas.\n- **Etapa 2:** Identificar o necropoder do extrativismo: matar o ambientalista ou a liderança indígena é a forma rápida de abrir clareira para o boi e a soja; a máquina de guerra privada limpa o terreno pelo sangue com cumplicidade estatal."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "Examine a crítica de Achille Mbembe ao 'Poder Farmacológico e Médico' contemporâneo: de que modo a distribuição global desigual de vacinas durante emergências sanitárias internacionais reproduz a clivagem necropolítica entre populações que devem viver e populações abandonadas à contaminação?",
        "Provando que as fórmulas químicas de imunizantes eram patenteadas por corporações de tecelões industriais.",
        "Evidenciando o chamado 'Apartheid Vacinal': países ricos monopolizaram estoques excedentes de doses e blindaram os lucros e patentes de grandes corporações farmacêuticas, enquanto países pobres da África e da América Latina foram privados de vacinas básicas, demonstrando que a vida biológica só é prioridade máxima quando pertence aos centros do grande capital dominante.",
        "Determinando que as seringas médicas devam ser fabricadas com ligas de prata importadas de minas árticas.",
        "Afirmando que as campanhas de vacinação eram coordenadas por conselhos monásticos de eremitas alpinos.",
        "Comprovando que as epidemias virais eram erradicadas unicamente através de exercícios matinais coletivos.",
        "B",
        "- **Etapa 1:** Observar a partilha de vacinas na pandemia: países europeus e norte-americanos compraram doses suficientes para vacinar sua população quatro vezes, enquanto na África faltava a primeira dose para médicos.\n- **Etapa 2:** Desvelar a necropolítica farmacêutica: defender a patente de laboratórios bilionários em vez de liberar a fórmula para salvar vidas pobres no Sul Global é a escolha deliberada de deixar morrer em nome do lucro corporativo."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "Analise a influência das teses de Frantz Fanon sobre Achille Mbembe na caracterização do espaço colonial: de que maneira Mbembe desdobra a clássica cisão maniqueísta fanoniana entre a 'cidade do colono' e a 'cidade do colonizado' na era dos drones e da vigilância digital?",
        "Comprovando que as construções arquitetônicas coloniais utilizavam blocos de mármore esculpidos à mão.",
        "Demonstrando que Mbembe atualiza a partição espacial de Fanon para a modernidade tecnológica: as antigas fronteiras de arame farpado transformaram-se em sistemas biométricos, sensores térmicos e drones letais de ataque cirúrgico que monitoram as periferias e colônias, mantendo a mesma divisão violenta entre os que desfrutam da civilização e os confinados na zona do terror.",
        "Determinando que os muros de contenção devam receber camadas protetoras de verniz ecológico transparente.",
        "Afirmando que a vigilância urbana moderna foi inspirada em técnicas de pastoreio de ovelhas medievais.",
        "Provando que as divisões territoriais de cidades africanas obedeciam a coordenadas traçadas por astrólogos.",
        "B",
        "- **Etapa 1:** Resgatar a intuição de Fanon: o mundo colonial é cindido pelo fuzil em duas cidades irreconciliáveis (a cidade saciada do branco e a favela faminta do negro).\n- **Etapa 2:** Analisar a sofisticação tecnológica com Mbembe: a separação segue a mesma, mas agora com câmeras de reconhecimento facial, drones que zumbem no céu e cercas inteligentes; a tecnologia hipermoderna serve à mesma segregação colonial."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Investigue o papel da linguagem e das 'Metáforas Biológicas de Higiene' na legitimação do necropoder: como o vocabulário que trata criminosos ou grupos marginalizados como 'cânceres sociais', 'pragas' ou 'ervas daninhas' desumaniza os alvos e autoriza sua eliminação física?",
        "Mostrando que os manuais de botânica do século XIX utilizavam gravuras ilustradas por marinheiros mercantes.",
        "Demonstrando que, ao rebaixar seres humanos à categoria de parasitas ou doenças infecciosas que ameaçam o corpo social sadio, a linguagem necropolítica retira o adversário do terreno ético e da lei civil, transformando seu assassinato policial em um imperativo sanitário e profilático indiscutível, onde exterminar vidas equivale a 'limpar a sociedade'.",
        "Determinando que os pronunciamentos oficiais de segurança devam ser transmitidos em língua latina arcaica.",
        "Afirmando que as metáforas higienistas foram criadas por artesãos de cerâmica em feiras rurais medievais.",
        "Provando que os termos biológicos de segurança foram copiados de tratados de alquimia renascentista.",
        "B",
        "- **Etapa 1:** Descrever o veneno das palavras desumanizadoras: quando um comandante ou apresentador de TV diz que a polícia foi 'fazer a limpa' ou 'extirpar um tumor' na favela, o ser humano é rebaixado a parasita.\n- **Etapa 2:** Revelar a eficácia da metáfora sanitária: ninguém tem pena de matar um inseto ou remover um tumor; ao animalizar o pobre, o discurso retira a culpa moral do matador e prepara o terreno para a chacina limpa."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Analise a relação entre o 'Endividamento das Famílias Trabalhadoras' e a precarização necropolítica no capitalismo financeirizado contemporâneo: como a asfixia pelo crédito predatório e juros bancários escorchantes atua como uma violência lenta contra as classes populares?",
        "Provando que as cédulas monetárias de papel moeda perdiam valor devido à umidade em cofres subterrâneos.",
        "Evidenciando que a financeirização captura a renda futura do trabalhador através de juros abusivos, obrigando famílias empobrecidas a escolherem diariamente entre comprar alimentos, pagar contas de luz ou adquirir remédios vitais, gerando desgaste físico acelerado, estresse crônico debilitante e encurtamento deliberado da expectativa de vida das populações periféricas.",
        "Determinando que as agências bancárias devam fechar suas portas durante períodos de alinhamento planetário.",
        "Afirmando que os cálculos de taxas de juros eram formulados exclusivamente por congregações monásticas beneditinas.",
        "Comprovando que as dívidas civis eram canceladas anualmente através de celebrações de jubileus rurais.",
        "B",
        "- **Etapa 1:** Compreender a agiotagem legalizada do sistema financeiro: os grandes bancos cobram juros de cartão e cheque especial que multiplicam dívidas em progressão geométrica para os mais pobres.\n- **Etapa 2:** Diagnosticar a asfixia lenta necropolítica: quem deve e não tem como pagar come mal, adoece de angústia e não consegue comprar medicamentos; o capital financeiro drena a saúde do povo, encurtando a vida dos trabalhadores da periferia."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Examine o conceito de 'Necropolítica de Fronteira' aplicado à crise humanitária dos refugiados indocumentados nos Estados Unidos: de que maneira a separação forçada de crianças de seus pais e o encarceramento em gaiolas metálicas expressam o exercício soberano da humilhação e da violência corporal?",
        "Provando que os centros de triagem fronteiriços utilizavam telhados cobertos por palha de milho colhida no outono.",
        "Demonstrando como o Estado norte-americano mobiliza a dor psíquica, a desumanização infantil e o aprisionamento em condições degradantes como táticas deliberadas de terror exemplar e dissuasão, comunicando aos povos do Sul que seus corpos e famílias não têm direito à dignidade nem à proteção de tratados internacionais de direitos humanos.",
        "Determinando que os agentes de imigração devam prestar juramentos de cavalaria em capelas militares do deserto.",
        "Afirmando que as detenções de imigrantes resultavam da carência de formulários impressos em língua espanhola.",
        "Comprovando que as famílias separadas recebiam indenizações em barras de ouro fundido antes de deportações.",
        "B",
        "- **Etapa 1:** Descrever o horror das jaulas na fronteira sul dos EUA: crianças arrancadas dos braços das mães, dormindo no chão de cimento frio sob luzes fluorescentes acesas 24 horas por dia.\n- **Etapa 2:** Revelar a crueldade programada do poder: a humilhação não é erro administrativo; ela é planejada para mandar o recado ao México e à América Central de que o migrante será triturado se tentar cruzar o muro."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "Investigue a tese de Achille Mbembe sobre a 'Desinstitucionalização da Morte' nas sociedades contemporâneas: por que, nos mundos de morte, o rito do luto e a despedida digna dos entes queridos são sistematicamente negados às famílias oprimidas?",
        "Comprovando que os serviços funerários municipais utilizavam carruagens puxadas por cavalos de raça.",
        "Evidenciando que a violência soberana não se contenta em tirar a vida biológica: ela sequestra corpos de desaparecidos, impede enterros com sepulturas identificadas, proíbe autópsias imparciais e intimida cortejos fúnebres de jovens assassinados em favelas, negando aos sobreviventes o sagrado direito ético ao luto e à memória de seus mortos.",
        "Determinando que os cemitérios públicos devam plantar mudas de ciprestes em alinhamento astronômico.",
        "Afirmando que os ritos funerários foram suspensos devido à escassez de tecidos de algodão para mortalhas.",
        "Provando que as certidões de óbito eram emitidas unicamente por comissões de filologia clássica universitária.",
        "B",
        "- **Etapa 1:** Reconhecer o papel civilizatório do luto: desde a Antígona grega, enterrar e chorar os mortos com dignidade é a fronteira que separa a civilização da barbárie pura.\n- **Etapa 2:** Desvelar a crueldade necropolítica que persegue o defunto: desaparecer com corpos, dar sumiço em laudos periciais e jogar gás lacrimogêneo em enterro de jovem de periferia é o ápice da covardia do necropoder."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Analise a fecundidade da categoria de 'Necropolítica' para a reflexão crítica da Filosofia do Ensino Médio no cumprimento da Lei Federal nº 10.639/2003: de que maneira o estudo de Achille Mbembe descoloniza o pensamento político e prepara os jovens estudantes para a defesa dos Direitos Humanos fundamentais?",
        "Provando que os exames nacionais de admissão devem priorizar unicamente o estudo de guerras imperiais romanas.",
        "Demonstrando que Mbembe instrumentaliza os estudantes com categorias analíticas que desvelam as raízes coloniais do racismo estrutural brasileiro, rompem a ilusão da cordialidade racial, denunciam a seletividade da violência de Estado e despertam a consciência cidadã emancipatória para a defesa intransigente da vida, da dignidade e dos direitos de todas as populações historicamente marginalizadas.",
        "Determinando que os manuais didáticos devam eliminar capítulos sobre as transformações urbanas do século XX.",
        "Afirmando que os currículos escolares devem ser redigidos unicamente por generais de infantaria militar veteranos.",
        "Comprovando que a formação filosófica moderna dispensa a discussão sobre ética política e relações raciais.",
        "B",
        "- **Etapa 1:** Superar o currículo colonizado e eurocêntrico: estudar apenas autores europeus que ignoraram a escravidão deixa os estudantes cegos para a realidade violenta das periferias brasileiras.\n- **Etapa 2:** Formar para a cidadania ativa e emancipada: aprender Mbembe cumpre a Lei 10.639/03, dá nome à violência que a juventude negra sofre e capacita os estudantes a lutarem por uma sociedade onde nenhuma vida seja descartável."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Examine o manifesto de esperança e reconstrução que encerra as reflexões de Achille Mbembe em Políticas da Inimizade: como a proposta de uma 'Comunidade Planetária' e o cuidado com a fragilidade de todos os seres vivos apontam o caminho para a superação definitiva das tecnologias da morte e a construção da paz mundial?",
        "Comprovando que os tratados de desarmamento bélico devem ser ratificados por academias de letras clássicas.",
        "Evidenciando que a superação da necropolítica exige abandonar a fantasia da soberania armada que mata para dominar, refundando a convivência humana na partilha desinteressada da Terra, no acolhimento irrestrito ao passante e ao migrante e na corresponsabilidade ética radical pela preservação da vida vulnerável de todos os seres do ecossistema planetário comum.",
        "Determinando que as assembleias diplomáticas internacionais devam ser transferidas para arquipélagos árticos.",
        "Afirmando que a convivência pacífica mundial depende da imposição compulsória de moedas fiduciárias de ouro.",
        "Provando que a fraternidade universal foi alcançada com a abolição definitiva de tarifas aduaneiras fluviais.",
        "B",
        "- **Etapa 1:** Reconhecer que Mbembe não é um teórico do desespero: ele diagnostica o horror da necropolítica justamente para mostrar que outro mundo é urgente e necessário.\n- **Etapa 2:** Abraçar a comunidade planetária: a saída da barbárie é derrubar os muros e as máquinas de guerra; precisamos cuidar da Terra como morada comum, protegendo o frágil e acolhendo o outro com amor e fraternidade universal."
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
    linhas.append('eixo: "Eixo III: Filosofia Política, Poder, Resistência e Necropolítica"')
    linhas.append('capitulo: "Capítulo 23: Achille Mbembe e a Necropolítica"')
    linhas.append('objeto_de_conhecimento: "O conceito de necropolítica em Achille Mbembe, a soberania como poder de matar, os mundos de morte (death-worlds), a plantação escravocrata, as novas máquinas de guerra e o racismo de Estado contemporâneo"')
    linhas.append('ebook_fonte: "em-fil-c23-achille-mbembe-necropolitica.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('  - "EM13CHS606"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: Achille Mbembe e a Necropolítica\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-23-achille-mbembe-necropolitica -->"
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
    linhas.append("- MBEMBE, Achille. *Necropolítica: biopoder, soberania, estado de exceção, política da morte*. Tradução de Renata Santini. São Paulo: n-1 edições, 2018.")
    linhas.append("- MBEMBE, Achille. *Crítica da razão negra*. Tradução de Marta Lança. São Paulo: n-1 edições, 2018.")
    linhas.append("- MBEMBE, Achille. *Políticas da inimizade*. Tradução de Marta Lança. São Paulo: n-1 edições, 2020.")
    linhas.append("- FOUCAULT, Michel. *Em defesa da sociedade: curso no Collège de France (1975-1976)*. Tradução de Maria Ermantina Galvão. São Paulo: Martins Fontes, 1999.")
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

    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-23-achille-mbembe-necropolitica/ebooks/em-fil-c23-achille-mbembe-necropolitica-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 23 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
