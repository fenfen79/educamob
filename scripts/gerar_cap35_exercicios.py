# -*- coding: utf-8 -*-
"""
Script de Geração e Homologação das 60 Questões de Filosofia EM - Capítulo 35
Objeto: O Existencialismo Negro em Frantz Fanon
E-book Fonte: em-fil-c35-existencialismo-negro-frantz-fanon.md
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
        "Qual pensador martinicano publicou em 1952 o clássico Pele Negra, Máscaras Brancas, fundando o Existencialismo Negro?",
        [
            ("Frantz Fanon, médico psiquiatra e filósofo que analisou o impacto da opressão colonial sobre a consciência.", True),
            ("G. W. F. Hegel, ao descrever o desdobramento da Ideia absoluta e a dialética nos compêndios de Berlim.", False),
            ("René Descartes, ao estabelecer a certeza indubitável do pensamento racional no discurso do método.", False),
            ("Auguste Comte, ao fundar a física social e formular a lei dos três estados da humanidade moderna.", False),
            ("Arthur Schopenhauer, ao definir o mundo fenomênico como representação ilusória da vontade cega.", False)
        ],
        "Frantz Fanon publicou Pele Negra, Máscaras Brancas em 1952, analisando a experiência vivida do negro e fundando o Existencialismo Negro."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Em qual obra de 2000 o filósofo Lewis Gordon formalizou os fundamentos do pensamento existencial negro?",
        [
            ("Existentia Africana: Understanding Africana Existential Thought, explorando a urgência da liberdade na diáspora.", True),
            ("O Capital, onde se analisa a acumulação primitiva de riquezas e a mais-valia nas indústrias inglesas.", False),
            ("A República, obra platônica dedicada à definição da justiça e à cidade ideal governada por reis filósofos.", False),
            ("Leviatã, tratado político que defende a soberania absoluta do governante para conter o estado de guerra de todos.", False),
            ("Crítica da Razão Pura, investigação kantiana sobre os limites transcendentais do conhecimento humano.", False)
        ],
        "Lewis Gordon publicou Existentia Africana (2000), demonstrando que o pensamento existencial floresce onde a dignidade humana é negada."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "No capítulo A Experiência Vivida do Negro, qual reação de uma criança branca na rua quebra a tranquilidade de Fanon?",
        [
            ("A criança encolhe-se aterrorizada, chora e grita para a mãe: Olhe, um preto! O preto vai me comer!", True),
            ("A criança aproxima-se com um livro de fábulas antigas e pede para o médico ler uma história infantil.", False),
            ("A criança convida o médico para participar de uma partida de xadrez na mesa de um parque municipal.", False),
            ("A criança entrega uma flor colhida nos jardins públicos como homenagem aos médicos estrangeiros da cidade.", False),
            ("A criança pergunta o caminho para a estação ferroviária central em virtude de ter se perdido da mãe.", False)
        ],
        "O grito da criança branca ('Olhe, um preto!') expõe a violência com que o racismo colonial desmorona a subjetividade do negro no espaço público."
    ))

    questoes_brutas.append((
        4, "EM13CHS502", "basico",
        "De acordo com Maurice Merleau-Ponty, qual conceito fenomenológico expressa a orientação dinâmica e espontânea do corpo no espaço?",
        [
            ("O esquema corporal, que sintetiza a consciência intuitiva de nossos membros e posições no ambiente material.", True),
            ("A alma desencarnada, que sobrevive como substância pensante independente das leis da gravidade física.", False),
            ("O reflexo mecânico autômato, que reduz o movimento biológico a transmissões elétricas em cabos nervosos.", False),
            ("A mônada isolada, que contempla o universo físico sem manter janelas de comunicação com o mundo exterior.", False),
            ("O arquétipo universal, que guarda memórias ancestrais transmitidas por hereditariedade sanguínea.", False)
        ],
        "Merleau-Ponty formula o esquema corporal para explicar como o sujeito habita o espaço com seu corpo de maneira fluida e não calculada."
    ))

    questoes_brutas.append((
        5, "EM13CHS504", "basico",
        "Na terminologia de Frantz Fanon, qual categoria substitui o esquema corporal quando o negro é aprisionado pelo olhar racista?",
        [
            ("O esquema histórico-racial, um emaranhado de lendas, superstições e preconceitos coloniais impostos ao sujeito.", True),
            ("O cálculo utilitarista da felicidade, que mede o prazer dos cidadãos em decisões econômicas do Estado.", False),
            ("A harmonia pré-estabelecida divina, que coordena as substâncias corporais segundo uma vontade celestial.", False),
            ("O contrato social civilizatório, que garante a igualdade jurídica irrestrita nos códigos civis burgueses.", False),
            ("O método indutivo empírico, que generaliza dados observados na natureza por meio de experimentos de laboratório.", False)
        ],
        "Fanon demonstra que o olhar racista destrói o esquema corporal equilibrado, impondo ao negro o pesado esquema histórico-racial colonial."
    ))

    questoes_brutas.append((
        6, "EM13CHS606", "basico",
        "Segundo Lewis Gordon, qual pergunta primordial formulada por W.E.B. Du Bois em 1903 sintetiza o drama existencial negro?",
        [
            ("O que é ser tratado como um problema humano no próprio solo onde se vive e trabalha?", True),
            ("Qual é o valor monetário das exportações de tecidos de algodão para portos comerciais do oriente?", False),
            ("Como demonstrar a existência de Deus por meio das cinco vias da teologia escolástica medieval?", False),
            ("Por quais razões o movimento dos astros celestes obedece a órbitas elípticas perfeitas no vácuo?", False),
            ("Qual técnica de pintura renascentista consegue produzir a mais fiel ilusão de profundidade geométrica?", False)
        ],
        "W.E.B. Du Bois sintetizou o dilema do negro no mundo ocidental com a indagação existencial: 'O que é ser tratado como um problema?'."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "Na investigação da corporeidade racializada, o que Fanon quer dizer ao proclamar que o negro é escravo da sua aparição?",
        [
            ("Que a sua pele escura é imediatamente vista e capturada por estereótipos coloniais antes de qualquer diálogo humano.", True),
            ("Que as roupas elegantes confeccionadas por alfaiates parisienses perdem o brilho quando expostas à luz do sol.", False),
            ("Que as leis de trânsito exigem que os pedestres usem faixas refletivas durante caminhadas noturnas na cidade.", False),
            ("Que os atores de peças dramáticas são obrigados a decorar falas escritas por dramaturgos do século passado.", False),
            ("Que os cidadãos devem comparecer às assembleias cívicas usando uniformes regulamentados pelas autoridades.", False)
        ],
        "A aparência visual imediata da pele negra funciona na sociedade colonial como um estigma inescapável que precede a individualidade do sujeito."
    ))

    questoes_brutas.append((
        8, "EM13CHS102", "basico",
        "No famoso ensaio Orfeu Negro, como Jean-Paul Sartre classificou o movimento da Negritude dentro da dialética histórica?",
        [
            ("Como uma antítese provisória e transitória destinada a dissolver-se na síntese da sociedade sem classes.", True),
            ("Como a realização definitiva da verdade religiosa revelada aos profetas da Antiguidade bíblica oriental.", False),
            ("Como um retrocesso moral bárbaro que deveria ser reprimido imediatamente pelas cortes de justiça imperial.", False),
            ("Como a única filosofia política autorizada a redigir manifestos econômicos em conferências operárias mundiais.", False),
            ("Como um gênero poético pitoresco restrito a apresentações musicais em salões literários da corte real.", False)
        ],
        "Sartre reduziu a Negritude a um momento negativo transitório (antítese) rumo à sociedade comunista universal, o que provocou o protesto de Fanon."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "Por qual razão Frantz Fanon revoltou-se contra a interpretação dialética formulada por Sartre sobre a Negritude?",
        [
            ("Porque considerou que Sartre desvalorizou a vivência viva do orgulho negro ao tratá-la como mero degrau descartável.", True),
            ("Porque Sartre recusou-se a publicar os artigos de médicos martinicanos em revistas de cardiologia de Paris.", False),
            ("Porque o existencialismo francês defendia a restauração de coroas monárquicas em territórios do Caribe.", False),
            ("Porque as teorias hegelianas exigiam que todos os livros de poesia fossem impressos em folhas de papiro egípcio.", False),
            ("Porque a filosofia francesa apoiava abertamente o envio de colonizadores agrícolas para ilhas da Oceania.", False)
        ],
        "Fanon sentiu que Sartre apagava a paixão da Negritude ao transformá-la em instrumento lógico subordinado a uma síntese hegeliana abstrata."
    ))

    questoes_brutas.append((
        10, "EM13CHS502", "basico",
        "Na conclusão de Pele Negra, Máscaras Brancas, qual é a postura de Fanon a respeito do passado da escravidão?",
        [
            ("Afirma que o homem negro não deve ser escravo do passado, pois o salto genuíno consiste em criar o próprio futuro.", True),
            ("Defende que as gerações contemporâneas devem viver em luto contínuo e abster-se de projetos de renovação social.", False),
            ("Propõe que a história universal seja apagada das escolas para que ninguém conheça os nomes das nações antigas.", False),
            ("Exige que os governos criem reservas rurais exclusivas para que os jovens não tenham contato com a modernidade.", False),
            ("Sustenta que as feridas da escravidão só serão curadas com doações de terras concedidas por cortes imperiais.", False)
        ],
        "Fanon prega a desalienação: o negro é livre para inventar sua própria existência e não deve ser prisioneiro eterno do sofrimento passado."
    ))

    questoes_brutas.append((
        11, "EM13CHS504", "basico",
        "Qual é a comovente oração final que encerra a obra Pele Negra, Máscaras Brancas de Frantz Fanon?",
        [
            ("Ó meu corpo, faz de mim sempre um homem que interroga!", True),
            ("Ó meu cérebro, livra-me para sempre do contato com as dores materiais da vida terrena!", False),
            ("Ó soberano Estado, concede-me pensões vitalícias para que eu possa repousar sem aflições!", False),
            ("Ó natureza cósmica, revela-me as fórmulas matemáticas secretas que governam as galáxias!", False),
            ("Ó tradição imutável, conserva intactos os costumes morais herdados de nossos antepassados!", False)
        ],
        "A obra termina com a célebre oração: 'Ó meu corpo, faz de mim sempre um homem que interroga!', coroando a corporeidade crítica da liberdade."
    ))

    questoes_brutas.append((
        12, "EM13CHS606", "basico",
        "Em cumprimento à Lei Federal nº 10.639/2003, qual é a importância pedagógica de estudar o pensamento de Frantz Fanon?",
        [
            ("Valorizar a história, a filosofia e a dignidade das populações negras, desmantelando preconceitos e visões eurocêntricas.", True),
            ("Exigir a substituição do ensino da língua portuguesa pelo latim clássico nos exames vestibulares das capitais.", False),
            ("Obrigar os estabelecimentos de ensino a suspenderem aulas de matemática em favor de disciplinas de etiqueta naval.", False),
            ("Determinar que apenas estudantes nascidos em ilhas do hemisfério norte possam concorrer a bolsas universitárias.", False),
            ("Proibir a leitura de autores estrangeiros nas bibliotecas das escolas públicas de educação básica do país.", False)
        ],
        "A Lei 10.639/03 estabelece a obrigatoriedade do ensino da história e cultura afro-brasileira e africana, resgatando intelectuais negros essenciais como Fanon."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Ao comparar o racismo antinegro com o antissemitismo europeu, qual distinção anatômica visual é enfatizada por Fanon?",
        [
            ("O preconceito antinegro é imediato e visual em razão da cor da pele, enquanto o judeu podia circular sem detecção imediata.", True),
            ("Os preconceitos contra povos nórdicos baseavam-se exclusivamente na altura corporal registrada em passaportes.", False),
            ("A discriminação racial afetava apenas trabalhadores que não sabiam manusear instrumentos de tecelagem mecânica.", False),
            ("O preconceito social dependia exclusivamente das marcas de sapatos utilizadas pelos cidadãos nas ruas de comércio.", False),
            ("Os governantes absolutistas perseguiam apenas artesãos que não participavam de procissões religiosas solenes.", False)
        ],
        "Fanon aponta que o preconceito antinegro tem caráter visual imediato: a cor da pele é identificada instantaneamente à distância perante o colonizador."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "De que maneira a fenomenologia existencial de Fanon qualifica a situação do homem branco no espaço público europeu?",
        [
            ("Como um sujeito que desfruta do privilégio de caminhar como indivíduo neutro e universal sem carregar estigmas de raça.", True),
            ("Como uma criatura submetida a rígidos toques de recolher noturnos decretados por prefeituras municipais.", False),
            ("Como um viajante obrigado a prestar continência militar perante qualquer autoridade diplomática estrangeira.", False),
            ("Como uma pessoa proibida de escolher sua própria carreira profissional em virtude da cor de seus olhos claros.", False),
            ("Como um cidadão obrigado a portar carteiras de vacinação visíveis para poder ingressar em salas de cinema.", False)
        ],
        "O homem branco vive o privilégio da não-marcação: seu corpo não é racializado como desvio, sendo visto como o padrão humano neutro."
    ))

    questoes_brutas.append((
        15, "EM13CHS501", "basico",
        "No terreno da psicologia médica, qual profissão exercida por Frantz Fanon conferiu base clínica e científica às suas reflexões?",
        [
            ("Médico psiquiatra, investigando o sofrimento mental, a alienação e as neuroses geradas pelo colonialismo na psique.", True),
            ("Engenheiro civil, projetando canais de irrigação e pontes ferroviárias em províncias rurais do continente asiático.", False),
            ("Comandante de marinha mercante, coordenando navios cargueiros no transporte de especiarias entre ilhas tropicais.", False),
            ("Arquiteto paisagista, desenhando jardins ornamentais para palácios aristocráticos nos subúrbios de grandes capitais.", False),
            ("Geólogo mineralogista, extraindo amostras de petróleo e ligas de carvão vegetal para indústrias siderúrgicas.", False)
        ],
        "Fanon era médico psiquiatra (formado na França), aplicando diagnósticos clínicos rigorosos à psicopatologia e às alienações do colonialismo."
    ))

    questoes_brutas.append((
        16, "EM13CHS502", "basico",
        "Qual intelectual brasileira pioneira aplicou a clínica existencial fanoniana em Tornar-se Negro (1983)?",
        [
            ("Neusa Santos Souza, demonstrando os custos psíquicos de ascensão social sob a imposição do ideal de branquitude.", True),
            ("Anita Garibaldi, ao combater nas guerras farroupilhas travadas no sul do continente durante o império.", False),
            ("Chiquinha Gonzaga, ao compor marchas carnavalescas e reger partituras orquestrais em teatros do Rio de Janeiro.", False),
            ("Tarsila do Amaral, ao pintar telas modernistas com temas florais inspirados em fazendas do interior paulista.", False),
            ("Princesa Isabel, ao assinar decretos civis autorizando a inauguração de linhas de telégrafo na capital federal.", False)
        ],
        "A psiquiatra Neusa Santos Souza publicou Tornar-se Negro (1983), pioneiro estudo sobre o sofrimento psíquico do racismo no Brasil inspirado em Fanon."
    ))

    questoes_brutas.append((
        17, "EM13CHS504", "basico",
        "O que expressa o conceito contemporâneo de branquitude discutido em diálogo interdisciplinar com o pensamento de Fanon?",
        [
            ("A posição estrutural de privilégio material, simbólico e político não nomeada que se coloca como norma universal.", True),
            ("A preferência estética por paredes de cor clara no acabamento arquitetônico de salas de aula universitárias.", False),
            ("O consumo de produtos farmacêuticos desenvolvidos para acelerar a regeneração celular da pele após queimaduras.", False),
            ("A escolha de vestimentas esportivas claras para a prática de modalidades de ginástica olímpica nos estádios.", False),
            ("A padronização das certidões civis impressas em papel sulfite imune ao desgaste provocado pela umidade do ar.", False)
        ],
        "A branquitude é o lugar estrutural de poder e privilégio simbólico não questionado que define a si mesmo como humanidade universal neutra."
    ))

    questoes_brutas.append((
        18, "EM13CHS606", "basico",
        "Ao abordar os equívocos comuns sobre Fanon, por que é incorreto afirmar que o pensador rejeitava a razão humana?",
        [
            ("Porque ele combatia a falsa universalidade eurocêntrica que justificou a escravidão, defendendo um humanismo autêntico.", True),
            ("Porque ele publicou tratados de lógica matemática propondo a eliminação de todas as teorias científicas do ocidente.", False),
            ("Porque a sua filosofia proibia que os estudantes matriculados em universidades lessem livros de física experimental.", False),
            ("Porque ele considerava que a sabedoria residia exclusivamente na adivinhação do futuro por meio de rituais com pedras.", False),
            ("Porque os psiquiatras da sua época recusavam o uso de medicamentos clínicos no tratamento de crises convulsivas.", False)
        ],
        "Fanon não era irracionalista: combatia o racismo travestido de ciência e defendia uma razão humanista verdadeiramente universal e libertadora."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Qual é o impacto existencial relatado por Fanon ao descobrir-se cindido e tripartido pelo olhar da sociedade colonial?",
        [
            ("Descobrir-se responsável ao mesmo tempo por seu corpo físico, por sua raça e pelos estigmas atribuídos a seus antepassados.", True),
            ("Receber autorização judicial para exercer três cargos executivos simultaneamente em tribunais da capital francesa.", False),
            ("Adquirir a faculdade auditiva sobrenatural de escutar conversas telefônicas privadas em diferentes línguas estrangeiras.", False),
            ("Perder a capacidade de falar fluentemente a sua língua materna durante conferências realizadas perante magistrados civis.", False),
            ("Ter o direito consuetudinário de votar três vezes consecutivas nas urnas eleitorais de províncias ultramarinas.", False)
        ],
        "Fanon relata a amputação do sujeito negro: ele não pode ser apenas ele mesmo; o racismo o obriga a carregar o fardo coletivo de sua raça e de séculos de estigmas."
    ))

    questoes_brutas.append((
        20, "EM13CHS102", "basico",
        "Por que o Existencialismo Negro recusa que a liberdade humana seja definida apenas como um ato interior da mente?",
        [
            ("Porque as barreiras materiais, policiais e sociais do racismo bloqueiam concretamente as vias de escolha do sujeito.", True),
            ("Porque as sinapses neuronais do cérebro são desativadas quando os indivíduos respiram o ar úmido de regiões litorâneas.", False),
            ("Porque as leis constitucionais republicanas proíbem que cidadãos façam reflexões teóricas fora das salas de aula.", False),
            ("Porque a linguagem poética não possui capacidade expressiva para traduzir sentimentos de angústia perante a morte.", False),
            ("Porque os tribunais de arbitragem mercantil anulam os contratos de pessoas que não possuem imóveis residenciais próprios.", False)
        ],
        "O Existencialismo Negro ensina que a liberdade é situada: de nada adianta proclamar a mente livre se o corpo está cercado pela violência racial e material."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Na fenomenologia da percepção merleau-pontyana, como se dá a integração entre o organismo vivo e o meio físico?",
        [
            ("Por meio de um esquema dinâmico onde o corpo antecipa distâncias e obstáculos de forma intuitiva e integrada ao mundo.", True),
            ("Através da memorização consciente de manuais de geometria espacial antes de qualquer deslocamento pelas ruas da cidade.", False),
            ("Pela intervenção contínua de espíritos guardiões que sustentam os passos dos pedestres para evitar quedas no chão.", False),
            ("Por meio de comandos numéricos transmitidos por satélites de navegação marítima diretamente ao sistema circulatório.", False),
            ("Pelo bloqueio involuntário dos sentidos que impede que o sujeito perceba a aproximação de perigos em praças públicas.", False)
        ],
        "Merleau-Ponty define o esquema corporal como síntese perceptiva espontânea que permite ao ser humano agir e navegar no mundo sem cálculo reflexivo."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Na ruptura com Merleau-Ponty, de que modo Fanon explica a desestruturação do corpo negro perante a branquitude?",
        [
            ("O olhar do colonizador fragmenta a harmonia do sujeito, substituindo a fluidez motora pelo peso de mitos de selvageria e canibalismo.", True),
            ("A perda de coordenação física decorre do uso de sapatos desconfortáveis fabricados por indústrias têxteis metropolitanas.", False),
            ("A digestão alimentar é paralisada pela ingestão de águas contaminadas por resíduos de usinas químicas instaladas nos portos.", False),
            ("Os reflexos corporais são acelerados pela luz emitida por lanternas elétricas utilizadas pela polícia nas patrulhas de rua.", False),
            ("A audição dos indivíduos sofre danos permanentes decorrentes do ruído mecânico produzido por trens a vapor nas estações.", False)
        ],
        "Fanon demonstra que o olhar racista desarticula a síntese motora corporal: sob o estigma colonial, o corpo vira objeto de medo e desprezo social."
    ))

    questoes_brutas.append((
        23, "EM13CHS501", "intermediario",
        "Ao defender o Movimento da Negritude formulado por Aimé Césaire e Léopold Senghor, que valor Fanon atribui à afirmação poética negra?",
        [
            ("A afirmação orgulhosa da cultura e da beleza negra como resistência viva e dignidade autônoma perante a humilhação colonial.", True),
            ("A exigência de que os governos europeus financiem viagens turísticas anuais para estudantes de escolas literárias de vanguarda.", False),
            ("A tentativa de padronizar a métrica de sonetos clássicos em conformidade com as regras de academias de letras da capital.", False),
            ("A criação de guildas mercantis fechadas com monopólio sobre o transporte de especiarias entre ilhas tropicais distantes.", False),
            ("A proposta de abandonar a escrita alfabética em favor do uso exclusivo de hieróglifos esculpidos em monumentos de pedra.", False)
        ],
        "Fanon defende que a Negritude de Césaire e Senghor expressa a paixão viva da dignidade negra, que não pode ser subordinada a esquemas dialéticos frios."
    ))

    questoes_brutas.append((
        24, "EM13CHS502", "intermediario",
        "Por qual razão Fanon afirma que a pele negra torna-se uma prisão existencial sob o domínio do colonialismo cultural?",
        [
            ("Porque a pigmentação corporal atua como uma barreira visível imediata à qual a branquitude associa defeitos morais prévios.", True),
            ("Porque a exposição contínua aos raios solares causa o endurecimento das camadas superficiais do tecido da derme.", False),
            ("Porque os uniformes civis desenhados por autoridades de saúde pública impediam a transpiração natural dos operários nas docas.", False),
            ("Porque os registros de imigração nos aeroportos utilizavam tintas químicas escuras que manchavam as mãos dos passageiros.", False),
            ("Porque as tinturas de tecidos fabricadas no Caribe desbotavam com rapidez quando submetidas a lavagens frequentes.", False)
        ],
        "A epidermização do racismo aprisiona o homem negro: ele não tem direito ao anonimato ou à neutralidade; sua pele é lida como sinônimo de perigo."
    ))

    questoes_brutas.append((
        25, "EM13CHS504", "intermediario",
        "Ao confrontar o existencialismo europeu, como Lewis Gordon caracteriza a diferença na origem da angústia em Sartre e em Fanon?",
        [
            ("Sartre parte da vertigem de escolher projetos no mundo burguês, enquanto Fanon parte da luta para ser reconhecido como ser humano.", True),
            ("Sartre preocupava-se exclusivamente com epidemias agrícolas, enquanto Fanon dedicava suas pesquisas à fabricação de relógios.", False),
            ("Sartre defendia a supremacia da nobreza feudal, ao passo que Fanon propunha a extinção de todas as instituições hospitalares.", False),
            ("Sartre acreditava que as emoções humanas eram ilusões de óptica, enquanto Fanon afirmava que os sonhos governavam as leis.", False),
            ("Sartre investigava a física de corpos celestes distantes, enquanto Fanon analisava a pureza das águas minerais do Caribe.", False)
        ],
        "Lewis Gordon destaca que a angústia do negro é profunda e existencial: o combate diário para provar que é um ser humano dotado de direitos."
    ))

    questoes_brutas.append((
        26, "EM13CHS606", "intermediario",
        "No contexto das práticas policiais brasileiras, como se manifesta a aplicação prática do esquema histórico-racial fanoniano?",
        [
            ("Na abordagem seletiva e na suspeição generalizada de jovens negros nas ruas, vistos como ameaça pelo perfil preconcebido.", True),
            ("Na aplicação equitativa e impessoal de testes de velocidade automobilística em rodovias estaduais bem sinalizadas.", False),
            ("Na distribuição universal de cartilhas educativas sobre regras de trânsito em colégios públicos de bairros residenciais.", False),
            ("Na contratação prioritária de fiscais aduaneiros graduados em cursos de relações internacionais de faculdades federais.", False),
            ("No pagamento regular de diárias de viagem a policiais designados para a vigilância de prédios da administração pública.", False)
        ],
        "O preconceito institucional da 'suspeição padrão' que visa jovens negros nas cidades do Brasil é o reflexo direto do esquema histórico-racial que antecipa o julgamento."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "Em relação aos preconceitos velados em espaços de elite no Brasil, qual situação exemplifica a violência do olhar que desindividualiza?",
        [
            ("Profissionais negros serem tomados como manobristas ou seguranças em restaurantes requintados devido aos estereótipos da servidão.", True),
            ("Clientes de bancos receberem senhas de atendimento preferencial com base na ordem cronológica de chegada às agências.", False),
            ("Advogados de grandes escritórios utilizarem ternos escuros em audiências solenes perante magistrados de cortes superiores.", False),
            ("Consumidores receberem notas fiscais detalhadas com os valores dos impostos pagos na compra de artigos eletrônicos importados.", False),
            ("Médicos especialistas participarem de conferências científicas apresentando dados estatísticos sobre vacinação coletiva.", False)
        ],
        "Quando profissionais negros em locais nobres são confundidos com serviçais, manifesta-se a recusa patriarcal/racista em reconhecer a autonomia e o sucesso do negro."
    ))

    questoes_brutas.append((
        28, "EM13CHS102", "intermediario",
        "Qual é o sentido da expressão amputação existencial utilizada para descrever o impacto psicológico do preconceito racial?",
        [
            ("A fratura da unidade subjetiva do indivíduo, forçado a lidar com uma imagem distorcida e humilhante fabricada pelo opressor.", True),
            ("A retirada cirúrgica de órgãos vitais em procedimentos hospitalares de emergência motivados por acidentes rodoviários.", False),
            ("A demolição de monumentos históricos em praças centrais durante reformas de reurbanização promovidas por prefeituras.", False),
            ("A anulação de registros de marcas comerciais por tribunais após a falência de indústrias alimentícias na capital.", False),
            ("A transferência compulsória de servidores públicos aposentados para diretorias regionais afastadas dos centros urbanos.", False)
        ],
        "A 'amputação existencial' expressa a violência psíquica do racismo, que mutila a autoimagem soberana do indivíduo negro e o aliena de si mesmo."
    ))

    questoes_brutas.append((
        29, "EM13CHS501", "intermediario",
        "Na análise de Roland Barthes em Mitologias, como a foto do soldado negro na capa de revista dialoga com as teses de Fanon?",
        [
            ("Utiliza a imagem do jovem uniformizado para disfarçar a violência colonial e criar o mito hipócrita de um império igualitário.", True),
            ("Critica a qualidade gráfica das técnicas de impressão fotográfica utilizadas por jornais parisienses no pós-guerra.", False),
            ("Comprova que os uniformes militares confeccionados com fios de algodão tropical eram mais resistentes à umidade do deserto.", False),
            ("Denuncia o atraso no pagamento dos salários dos recrutas alistados em batalhões de infantaria das forças armadas da França.", False),
            ("Propõe que as cerimônias de continência à bandeira nacional sejam celebradas sem a presença de instrumentos de sopro militar.", False)
        ],
        "Barthes desconstrói a capa da Paris Match: o soldado negro prestando continência é um artefato mitológico para legitimar a dominação colonial francesa."
    ))

    questoes_brutas.append((
        30, "EM13CHS502", "intermediario",
        "Por que as rodas de conversa e acolhimento psicológico de estudantes negros nas universidades recuperam a clínica de Fanon?",
        [
            ("Porque ajudam a superar o sofrimento do racismo institucional e desconstroem o sentimento de impostura imposto pela branquitude.", True),
            ("Porque ensinam técnicas de memorização mnemônica para provas de física termodinâmica em cursos de engenharia civil.", False),
            ("Porque organizam viagens de férias para praias do litoral sul durante os meses de recesso escolar de inverno.", False),
            ("Porque cobram mensalidades em dinheiro para financiar campanhas publicitárias de candidatos a cargos eletivos municipais.", False),
            ("Porque substituem os estágios curriculares supervisionados exigidos por conselhos profissionais de medicina e odontologia.", False)
        ],
        "A clínica fanoniana acolhe a dor psíquica do racismo, desfazendo as máscaras assimilacionistas e fortalecendo a emancipação coletiva dos sujeitos."
    ))

    questoes_brutas.append((
        31, "EM13CHS504", "intermediario",
        "Na interpretação da oração Ó meu corpo, faz de mim sempre um homem que interroga!, qual postura diante de dogmas é reivindicada?",
        [
            ("A atitude crítica permanente que recusa o conformismo e questiona continuamente as injustiças institucionais do mundo.", True),
            ("A obediência cega aos decretos administrativos emitidos por conselhos corporativos de empresas monopolistas privadas.", False),
            ("A aceitação resignada de que as hierarquias sociais são leis imutáveis determinadas pela providência divina dos céus.", False),
            ("A recusa em participar de assembleias sindicais para manter a harmonia comercial entre trabalhadores e empresários da capital.", False),
            ("O isolamento intelectual em bibliotecas fechadas desprovidas de qualquer compromisso com as lutas concretas da sociedade.", False)
        ],
        "Interrogar permanentemente é a vocação da liberdade fanoniana: duvidar das certezas do poder dominante, contestar o racismo e buscar a verdade humana."
    ))

    questoes_brutas.append((
        32, "EM13CHS606", "intermediario",
        "No debate sobre a desalienação, por qual razão Fanon adverte que o negro não deve viver apenas em função do ressentimento?",
        [
            ("Porque a liberdade autêntica exige inventar novas possibilidades de futuro e não permanecer aprisionado às dores do passado.", True),
            ("Porque as empresas estrangeiras pagavam indenizações pecuniárias generosas para famílias de trabalhadores agrícolas vitimados.", False),
            ("Porque os tribunais internacionais proibiram que historiadores publicassem pesquisas sobre o tráfico atlântico de escravizados.", False),
            ("Porque o rancor contra antigos governantes monárquicos diminui as vendas de mercadorias no comércio varejista das metrópoles.", False),
            ("Porque a Igreja católica concedia perdão universal a todos os administradores de feudos e feitorias coloniais no litoral.", False)
        ],
        "Fanon defende que a superação da alienação colonial não se resume a lamentar o passado: o verdadeiro salto existencial consiste em criar um amanhã livre."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "No debate sobre a corporeidade, de que modo a distinção entre corpo biológico e corpo racializado aprofunda a compreensão da violência colonial em Fanon?",
        [
            ("Mostrando que o corpo biológico neutro é soterrado por camadas históricas de desprezo que desumanizam o sujeito perante a sociedade.", True),
            ("Comprovando que os exercícios de corrida ao ar livre melhoram o funcionamento das válvulas cardíacas de atletas profissionais.", False),
            ("Afirmando que a anatomia humana foi desenhada por engenheiros medievais para suportar o peso de armaduras de combate militar.", False),
            ("Demonstrando que a respiração pulmonar em altitudes elevadas exige a utilização contínua de cilindros de gás comprimido medicinal.", False),
            ("Defendendo que a taxa de glicose no sangue de operários fabris varia de acordo com as flutuações das cotações da bolsa de valores.", False)
        ],
        "O corpo negro não é apenas biologia: é um território socialmente marcado e estigmatizado pela história colonial, o que funda a fenomenologia da raça."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "Ao investigar a relação entre Frantz Fanon e Jean-Paul Sartre, qual obra posterior de Fanon contou com prefácio escrito por Sartre?",
        [
            ("Os Condenados da Terra (1961), manifesto contundente sobre a descolonização e a libertação dos povos do terceiro mundo.", True),
            ("A Náusea, romance existencialista centrado nas angústias solitárias de um professor em uma cidade do litoral francês.", False),
            ("O Ser e o Tempo, tratado existencial que examina a estrutura da existência humana e a temporalidade autêntica do ser.", False),
            ("Discurso sobre a Origem da Desigualdade, ensaio que analisa a propriedade privada como origem dos conflitos sociais humanos.", False),
            ("A Ideologia Alemã, manuscrito dedicado à crítica dos jovens hegelianos e à fundamentação da concepção materialista da história.", False)
        ],
        "Sartre redigiu o célebre e inflamado prefácio de Os Condenados da Terra (1961), reconhecendo a liderança intelectual de Fanon na luta anticolonial."
    ))

    questoes_brutas.append((
        35, "EM13CHS501", "intermediario",
        "Na prática psiquiátrica clínica, como a análise de Fanon conecta os distúrbios emocionais dos colonizados ao colonialismo?",
        [
            ("Demonstrando que as neuroses e depressões não são fraquezas biológicas inatas, mas sintomas da violência sistemática da dominação.", True),
            ("Provando que os distúrbios da memória são causados pela ingestão de frutas cítricas colhidas fora do período de safra regular.", False),
            ("Afirmando que as dores articulares em camponeses resultavam da leitura noturna de romances de cavalaria da Idade Média.", False),
            ("Sustentando que as alterações de humor decorriam unicamente da aproximação de cometas visíveis a olho nu no horizonte noturno.", False),
            ("Argumentando que a ansiedade social dos pacientes desaparecia imediatamente após a compra de apólices de seguro de vida.", False)
        ],
        "Fanon revolucionou a psiquiatria ao provar que o colonialismo é um sistema patogênico que gera adoecimento mental na população subjugada."
    ))

    questoes_brutas.append((
        36, "EM13CHS502", "intermediario",
        "Qual é a crítica de Fanon à assimilação cultural como estratégia de aceitação do negro na sociedade burguesa branca?",
        [
            ("A assimilação exige que o negro use máscaras brancas e renuncie à sua identidade sem jamais ser plenamente aceito como igual.", True),
            ("A assimilação garante cargos de liderança diplomática e salários iguais a todos os emigrantes que chegam a portos europeus.", False),
            ("A assimilação resulta na concessão automática de títulos nobiliárquicos para estudantes formados em conservatórios musicais.", False),
            ("A assimilação foi instituída por tratados de paz firmados entre monarquias vizinhas para facilitar o comércio de seda fina.", False),
            ("A assimilação permitiu que camponeses analfabetos assumissem a direção de companhias marítimas transatlânticas.", False)
        ],
        "O drama de 'Pele negra, máscaras brancas': ao tentar falar, vestir e agir como o branco para ser aceito, o negro aliena-se e continua barrado pelo racismo."
    ))

    questoes_brutas.append((
        37, "EM13CHS504", "intermediario",
        "Sob a ótica da corporeidade, por qual razão a oração do corpo representa uma ruptura com o racionalismo cartesiano clássico?",
        [
            ("Porque recoloca o corpo sensível e vivo no centro da experiência filosófica, superando a separação abstrata entre mente e carne.", True),
            ("Porque proíbe o estudo de regras de dedução lógica e álgebra linear nos primeiros anos de cursos secundários da rede pública.", False),
            ("Porque determina que as decisões administrativas sejam tomadas por juízes após a realização de corridas de resistência física.", False),
            ("Porque afirma que os sentimentos de afeto entre as pessoas decorrem de variações na densidade do oxigênio nas salas de aula.", False),
            ("Porque condiciona a emissão de títulos de propriedade imobiliária à realização de exames de flexibilidade muscular em praça pública.", False)
        ],
        "Enquanto Descartes isolava o pensamento puro ('penso, logo existo'), Fanon ancora a consciência na carne concreta que sofre e interroga no mundo."
    ))

    questoes_brutas.append((
        38, "EM13CHS606", "intermediario",
        "Nos movimentos sociais contemporâneos no Brasil, como o Existencialismo Negro fornece armas teóricas para o combate ao racismo?",
        [
            ("Fornecendo instrumentos conceituais para desmascarar o mito da democracia racial e afirmar a soberania dos sujeitos marginalizados.", True),
            ("Defendendo a extinção do ensino gratuito de história nas universidades públicas para reduzir os gastos do orçamento ministerial.", False),
            ("Exigindo que os partidos políticos suspendam seus congressos anuais até a resolução definitiva de contestações eleitorais de vizinhos.", False),
            ("Propondo a revogação de todas as leis trabalhistas em vigor para incentivar a competição comercial irrestrita entre artesãos fabris.", False),
            ("Sustentando que os protestos pacíficos de trabalhadores devem ser mediados por representantes diplomáticos de tribunais arbitrais.", False)
        ],
        "Fanon fornece a base crítica para desmontar a ilusão da harmonia racial no Brasil, denunciando a violência real do racismo e empoderando os corpos negros."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Em contraposição às teorias racialistas do século dezenove, qual verdade sociológica é consagrada por Frantz Fanon?",
        [
            ("A raça não é um dado biológico natural ou genético, mas uma construção política e social inventada para legitimar a dominação colonial.", True),
            ("As raças humanas dividem-se em grupos estanques com aptidões intelectuais previamente determinadas pelo formato dos ossos cranianos.", False),
            ("A capacidade de governar cidades industriais modernas depende do percentual de cálcio presente nos dentes dos magistrados civis.", False),
            ("O clima das regiões polares favorece o desenvolvimento de habilidades musicais superiores em virtude das baixas temperaturas do ar.", False),
            ("A nobreza moral dos povos camponeses decorre da sua descendência genealógica direta de governantes das primeiras dinastias egípcias.", False)
        ],
        "Fanon e a teoria crítica demonstram que raça não existe na biologia: ela é um artefato sociopolítico criado pelo colonialismo para justificar o saque e a exploração."
    ))

    questoes_brutas.append((
        40, "EM13CHS102", "intermediario",
        "Em síntese, qual é a principal contribuição do Existencialismo Negro para a história geral da filosofia ocidental contemporânea?",
        [
            ("Desvelar que a liberdade não pode ser pensada como abstração pura, exigindo considerar a corporeidade racializada e a violência material.", True),
            ("Restaurar o modelo escolástico de ensino baseado na memorização de silogismos em latim sem qualquer contato com problemas sociais.", False),
            ("Demonstrar que as teorias científicas devem ser submetidas à prévia homologação de assembleias clericais de basílicas de grandes capitais.", False),
            ("Restringir a reflexão moral exclusivamente a proprietários de terras e diplomatas de nações do hemisfério norte da Europa ocidental.", False),
            ("Provar que os conflitos políticos entre nações soberanas decorrem de divergências estilísticas na redação de tratados comerciais de paz.", False)
        ],
        "O Existencialismo Negro desfez a miopia do universalismo abstrato europeu, provando que a liberdade autêntica deve nascer da carne ferida pela opressão histórica."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Sob quais aspectos a fenomenologia da corporeidade de Maurice Merleau-Ponty é desestabilizada pelo racismo antinegro descrito por Frantz Fanon?",
        [
            ("Merleau-Ponty supunha um corpo neutro integrado espontaneamente ao espaço; Fanon revela que a pele negra é amputada pelo olhar branco opressor.", True),
            ("Merleau-Ponty sustentava que a visão dependia de raios luminosos emitidos pelos próprios olhos, enquanto Fanon provou o papel das lentes óticas.", False),
            ("Merleau-Ponty limitava seus estudos à anatomia das articulações ósseas de equinos, enquanto Fanon pesquisou o sistema respiratório de pássaros.", False),
            ("Merleau-Ponty afirmava que a mente residia no coração biológico, enquanto Fanon demonstrou a primazia da circulação sanguínea periférica.", False),
            ("Merleau-Ponty negava que os seres humanos pudessem aprender línguas estrangeiras na infância, enquanto Fanon comprovou o bilinguismo martinicano.", False)
        ],
        "- **Etapa 1:** A fenomenologia tradicional de Merleau-Ponty parte do sujeito universal cujo 'esquema corporal' harmoniza-se de modo desimpedido com o ambiente físico.\n- **Etapa 2:** Fanon desvela o ponto cego eurocêntrico: o corpo negro não navega livremente; ao entrar na esfera pública racista, seu esquema corporal é implodido pelo 'esquema histórico-racial', sendo capturado por mitos coloniais prévios, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Ao investigar a experiência vivida do negro, de que maneira Fanon desconstrói a alegação de que a angústia existencial seria idêntica para todos os seres humanos?",
        [
            ("Diferenciando a angústia sartriana da escolha burguesa da angústia urgente do homem negro que precisa lutar para ser reconhecido como ser humano.", True),
            ("Afirmando que a tristeza é um sentimento que afeta exclusivamente pessoas desprovidas de residências com aquecimento a carvão na Europa.", False),
            ("Provando que as emoções de medo e pânico foram inventadas por corporações de seguros comerciais para vender apólices de viagem marítima.", False),
            ("Sustentando que os habitantes de ilhas tropicais desconhecem crises depressivas em virtude da alta luminosidade solar durante todas as estações.", False),
            ("Demonstrando que os operários das docas parisienses recebiam salários suficientes para contratar serviços regulares de psicanálise freudiana.", False)
        ],
        "- **Etapa 1:** O existencialismo europeu clássico concebia a angústia como um drama metafísico abstrato perante o nada e a responsabilidade infinita da escolha.\n- **Etapa 2:** Fanon situa a existência: o negro vive uma angústia primordial que antecede a escolha de projetos; ele enfrenta o horror de habitar uma 'zona do não-ser', onde sua própria condição de sujeito pensante é violentamente contestada pela branquitude, validando a alternativa A."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Na polêmica aberta com Jean-Paul Sartre sobre o ensaio Orfeu Negro, por que Fanon considerou a posição sartriana um golpe contra a dignidade da Negritude?",
        [
            ("Porque Sartre reduziu o orgulho e a vivência existencial negra a uma antítese descartável subordinada a uma dialética hegeliana eurocêntrica.", True),
            ("Porque Sartre proibiu que os poetas do Caribe publicassem seus versos em editoras de literatura de vanguarda da cidade de Paris.", False),
            ("Porque Sartre defendia o restabelecimento de impostos alfandegários abusivos sobre mercadorias têxteis exportadas pelas colônias caribenhas.", False),
            ("Porque Sartre exigiu que a filosofia existencialista fosse ensinada exclusivamente nos seminários católicos do norte da França.", False),
            ("Porque Sartre afirmou que a música popular de percussão africana era uma invenção de marinheiros mercantes holandeses do século dezenove.", False)
        ],
        "- **Etapa 1:** No ensaio Orfeu Negro, Sartre aplicou uma leitura dialética mecânica: o racismo branco era a tese; a Negritude, a antítese provisória; a sociedade comunista sem raças, a síntese absorvente.\n- **Etapa 2:** Fanon protesta com veemência: a vivência negra não é um teorema abstrato de gabinete; ela é carne viva e paixão presente; reduzir o grito poético da Negritude a um instrumento passageiro foi uma violência que desarmou a potência existencial autônoma do negro, consagrando a alternativa A."
    ))

    questoes_brutas.append((
        44, "EM13CHS502", "dificil",
        "Ao analisar a alienação subjetiva, em que termos a tese da epidermização da inferioridade esclarece a dor psíquica do colonizado?",
        [
            ("Evidenciando como o colonizado internaliza a ideologia do dominador, sentindo vergonha de seu próprio corpo e adotando máscaras brancas para ser tolerado.", True),
            ("Provando que a melanina da pele humana sofre alterações químicas quando exposta a soluções salinas concentradas de águas marinhas.", False),
            ("Demonstrando que as doenças dermatológicas nos trópicos decorriam unicamente da falta de vestimentas de lã importadas de fábricas inglesas.", False),
            ("Argumentando que a baixa frequência cardíaca em jovens estudantes decorria da privação involuntária de sobremesas açucaradas no almoço.", False),
            ("Sustentando que os indivíduos negros possuíam anticorpos genéticos naturais contra todas as espécies de venenos de serpentes venenosas.", False)
        ],
        "- **Etapa 1:** A violência colonial não se restringe à ocupação territorial militar e à espoliação econômica de matérias-primas e trabalho.\n- **Etapa 2:** O colonialismo opera uma devastação subjetiva: a 'epidermização' significa que a inferioridade forjada pelo branco se entranha na carne do negro, gerando neuroses, ódio de si e a vã tentativa de usar 'máscaras brancas' para fugir da condenação de sua cor, legitimando a alternativa A."
    ))

    questoes_brutas.append((
        45, "EM13CHS504", "dificil",
        "Na conclusão sublime de Pele Negra, Máscaras Brancas, qual síntese ética entre corporeidade e liberdade é alcançada por Fanon?",
        [
            ("A superação da alienação pelo compromisso da carne sensível com a atitude crítica inegociável que recusa a resignação e reinventa a humanidade.", True),
            ("A entrega da soberania política individual a chefes carismáticos de governos centralizadores encarregados de manter a estabilidade financeira.", False),
            ("A convicção de que a história universal já foi totalmente concluída e que aos cidadãos resta apenas o recolhimento em preces silenciosas.", False),
            ("A rejeição de qualquer diálogo ou cooperação internacional entre povos libertados de antigas dominações coloniais no hemisfério sul.", False),
            ("O fechamento das universidades públicas para impedir que o excesso de debates acadêmicos conturbe a tranquilidade dos bairros nobres.", False)
        ],
        "- **Etapa 1:** A prece ao corpo não é um apelo místico desvinculado do mundo, mas o ápice da fenomenologia fanoniana da desalienação subjetiva.\n- **Etapa 2:** Fanon ancora a liberdade no corpo que sente e resiste: interrogar é a recusa suprema da passividade colonizada; o corpo que interroga questiona o racismo, destrói os dogmas imperiais e afirma a humanidade plena e soberana de todos os sujeitos, o que comprova a alternativa A."
    ))

    questoes_brutas.append((
        46, "EM13CHS606", "dificil",
        "Em que medida a distinção fanoniana entre o antissemitismo e o racismo antinegro ilumina a especificidade estrutural da opressão racial contemporânea?",
        [
            ("Enquanto o preconceito contra o judeu opera por representações culturais que permitem o disfarce, o negro é imediatamente julgado pela cor visível de sua pele.", True),
            ("Enquanto o antissemitismo europeu foi um fenômeno pacífico e sem violência, o racismo antinegro provocou embates nos tribunais arbitrais da ONU.", False),
            ("Enquanto os judeus eram proibidos de navegar em embarcações fluviais, as populações africanas detinham o controle de refinarias de carvão mineral.", False),
            ("Enquanto as leis discriminatórias antigas afetavam apenas os hábitos alimentares, o preconceito moderno regula a escolha de calçados de ginástica.", False),
            ("Enquanto as congregações religiosas europeias protegiam os operários, as corporações de médicos martinicanos recusavam pacientes estrangeiros.", False)
        ],
        "- **Etapa 1:** Fanon dialoga com as teses de Sartre em Reflexões sobre o Racismo e a Questão Judaica para pontuar a diferença profunda da experiência racial.\n- **Etapa 2:** O judeu podia circular anonimamente na praça pública europeia sem que sua pertença étnico-religiosa fosse denunciada de imediato pelo olhar distante; o negro, contudo, é 'escravo de sua aparição': sua pele negra é uma bandeira visível imediata capturada instantaneamente pelo estigma racista da branquitude, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        47, "EM13CHS101", "dificil",
        "Na análise de Lewis Gordon sobre a má-fé institucional, como se manifesta a fuga da responsabilidade coletiva perante o racismo nas democracias liberais?",
        [
            ("Na crença cômoda de que o racismo é mero desvio moral de indivíduos isolados, recusando admitir o caráter estrutural e institucional da discriminação.", True),
            ("Na aprovação de leis orçamentárias que destinam todas as receitas fiscais para a preservação de florestas equatoriais virgens no continente.", False),
            ("Na assinatura de tratados internacionais que garantem a isenção de pedágios para motoristas de ambulâncias hospitalares em rodovias.", False),
            ("No recolhimento voluntário de impostos extraordinários por parte de banqueiros que desejam patrocinar festivais anuais de poesia barroca.", False),
            ("Na exigência de que os editais de licitação de obras civis sejam redigidos em dialetos arcaicos para dificultar a concorrência comercial.", False)
        ],
        "- **Etapa 1:** Sartre definiu a má-fé como a mentira que a consciência conta a si mesma para escapar da angústia da sua própria liberdade e escolha.\n- **Etapa 2:** Lewis Gordon transpõe o conceito para a sociologia: as sociedades brancas praticam a má-fé institucional quando fingem que o racismo 'não existe mais' ou o reduzem a incidentes pontuais de pessoas mal-educadas, ocultando a opressão material sistemática das instituições, validando a alternativa A."
    ))

    questoes_brutas.append((
        48, "EM13CHS102", "dificil",
        "Ao examinar a dialética da desalienação em Pele Negra, Máscaras Brancas, qual advertência filosófica Fanon formula contra o apego estéril ao passado?",
        [
            ("O homem negro não deve se transformar em escravo perpétuo da escravidão sofrida por seus pais, pois o dever supremo do sujeito é inventar sua liberdade.", True),
            ("As populações descolonizadas devem queimar os documentos de bibliotecas antigas para evitar que os jovens aprendam línguas românicas.", False),
            ("Os historiadores dos países africanos devem suspender as escavações arqueológicas para direcionar recursos a montadoras de tratores.", False),
            ("As tradições musicais tradicionais dos povos indígenas da América devem ser proibidas em rádios comerciais para acelerar o progresso.", False),
            ("O ensino de matérias teóricas nas academias de ciências deve ser condicionado à realização de testes de aptidão militar prévios.", False)
        ],
        "- **Etapa 1:** Certas vertentes anticoloniais caíam no risco do romantismo reacionário ou da paralisia do ressentimento amargo contra os crimes do colonizador.\n- **Etapa 2:** Fanon assume postura existencial límpida: o passado de dores não deve ser esquecido, mas não pode virar algema; o negro é um sujeito soberano do presente, livre para construir um mundo novo e desalienado onde a dignidade humana reine sem rancores paralisantes, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        49, "EM13CHS501", "dificil",
        "No exercício da prática psiquiátrica hospitalar, de que maneira a observação clínica de Fanon revelou o caráter patogênico do colonialismo?",
        [
            ("Observando que os sintomas psíquicos de torturadores franceses e de rebeldes argelinos decorriam da violência desumanizadora do próprio sistema colonial.", True),
            ("Constatando que as neuroses dos soldados europeus eram provocadas pela altitude elevada das montanhas onde acampavam durante as manobras.", False),
            ("Comprovando que o uso de aparelhos de eletrochoque resolvia definitivamente todas as disputas territoriais travadas entre povos vizinhos.", False),
            ("Demonstrando que os pacientes internados em enfermarias melhoravam rapidamente quando ouviam leituras de tragédias gregas em grego arcaico.", False),
            ("Defendendo que as aflições da mente deviam ser tratadas com o confinamento perpétuo dos doentes em celas subterrâneas sem iluminação.", False)
        ],
        "- **Etapa 1:** Em sua prática psiquiátrica clínica, Fanon tratou tanto os militares encarregados da repressão violenta quanto os combatentes torturados.\n- **Etapa 2:** Fanon concluiu com lucidez clínica: o colonialismo é uma estrutura desumanizadora que enlouquece tanto o colonizador quanto o colonizado; não é possível curar os doentes psíquicos sem demolir as estruturas violentas e desumanas da dominação política colonial, consagrando a alternativa A."
    ))

    questoes_brutas.append((
        50, "EM13CHS502", "dificil",
        "Ao articular o pensamento de Fanon com a obra Tornar-se Negro de Neusa Santos Souza, qual conclusão sobre a identidade negra no Brasil contemporâneo se sustenta?",
        [
            ("A ascensão social da pessoa negra é marcada pela armadilha psíquica de rejeitar seus traços ancestrais para se conformar ao ideal de branquitude dominante.", True),
            ("A mobilidade econômica no Brasil assegura o desaparecimento automático de qualquer forma de preconceito de cor no mercado de trabalho formal.", False),
            ("Os cidadãos negros que completam cursos de pós-graduação universitária passam a usufruir de isenção integral no pagamento de tributos prediais.", False),
            ("A sociedade brasileira resolveu todos os seus dilemas de desigualdade de renda após a publicação da Constituição Federal promulgada em 1988.", False),
            ("As universidades públicas do país sempre reservaram metade das vagas de seus corpos docentes para intelectuais nascidos no continente africano.", False)
        ],
        "- **Etapa 1:** Neusa Santos Souza parte das categorias fanonianas de alienação e de máscara branca para analisar o caso dos negros de classe média no Brasil.\n- **Etapa 2:** Revela-se a armadilha psíquica: para ser aceito nos círculos de prestígio da sociedade brasileira, o sujeito é impelido a renunciar à sua identidade negra e mimetizar a branquitude; a libertação requer o doloroso e belo processo de 'tornar-se negro', afirmando a dignidade e a beleza de sua corporeidade, validando a alternativa A."
    ))

    questoes_brutas.append((
        51, "EM13CHS504", "dificil",
        "No campo da teoria crítica, em que termos a categoria fanoniana de zona do não-ser redefine a discussão sobre os direitos humanos na modernidade?",
        [
            ("Evidenciando que a humanidade universal da modernidade foi construída excluindo as populações colonizadas da plena dignidade de seres humanos.", True),
            ("Comprovando que as cartas constitucionais do século dezoito garantiam salários iguais para trabalhadores manuais em todas as colônias ultramarinas.", False),
            ("Afirmando que as teorias de direitos naturais foram inspiradas em sistemas jurídicos criados por reinos camponeses do interior da Ásia.", False),
            ("Demonstrando que os tratados sobre a dignidade do homem prescreviam a abolição imediata da escravidão em todas as potências imperialistas.", False),
            ("Sustentando que as leis civis europeias concediam direito ao voto secreto para escravizados que prestassem serviços domésticos nas capitais.", False)
        ],
        "- **Etapa 1:** A tradição iluminista eurocêntrica proclamava a 'declaração universal dos direitos do homem', mas convivia pacificamente com a escravidão nas colônias.\n- **Etapa 2:** Fanon desmascara a farsa: o mundo moderno está cindido; há uma 'zona do ser' (onde os brancos têm direitos, cidadania e dignidade) e uma 'zona do não-ser' (onde os colonizados e negros são desumanizados e tratados como coisas); os direitos humanos só serão autênticos quando demolirem essa fronteira colonial abissal, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        52, "EM13CHS606", "dificil",
        "Ao examinar a recepção de Frantz Fanon na teoria crítica contemporânea, qual é a crítica dirigida aos discursos que tentam esvaziar seu radicalismo político?",
        [
            ("A tentativa liberal de reduzi-lo a um mero terapeuta individual da linguagem, apagando sua defesa inegociável da revolução social e da descolonização.", True),
            ("A censura imposta por revistas acadêmicas que proíbem a citação de obras publicadas antes da Segunda Guerra Mundial em artigos de pesquisa.", False),
            ("A acusação infundada de que ele nunca participou de conferências internacionais de médicos dedicadas à saúde pública em hospitais rurais.", False),
            ("A alegação incorreta de que ele defendia a restauração de regimes monárquicos em ilhas do mar Mediterrâneo durante a guerra de libertação.", False),
            ("A falsa convicção de que ele recusava o uso de instrumentos cirúrgicos esterilizados em intervenções ortopédicas de emergência médica.", False)
        ],
        "- **Etapa 1:** Setores acadêmicos liberais tentam higienizar a memória de Fanon, domesticando-o como um autor 'pós-moderno' que apenas falava de identidades fluidas.\n- **Etapa 2:** Intelectuais descoloniais resgatam a integridade de seu pensamento: a fenomenologia de Pele Negra, Máscaras Brancas é indissociável da práxis anticolonial armada de Os Condenados da Terra; Fanon une a psiquiatria íntima à luta revolucionária coletiva contra o imperialismo, legitimando a alternativa A."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Na trajetória militante de Fanon na Guerra da Argélia, como as reflexões de Pele Negra, Máscaras Brancas ganham dimensão revolucionária coletiva?",
        [
            ("Passando da crítica existencial e psicológica do racismo individual para a teoria e a prática da descolonização material coletiva dos povos subjugados.", True),
            ("Abandonando a defesa dos direitos dos povos africanos para assumir a direção de conservatórios literários financiados pela coroa imperial.", False),
            ("Propondo que os conflitos por terras entre colônias e metrópoles fossem resolvidos por meio de campeonatos de tiro ao alvo desportivo.", False),
            ("Defendendo que as nações do terceiro mundo deveriam entregar suas reservas minerais para consórcios privados administrados pela Europa.", False),
            ("Afirmando que a independência das colônias deveria ser adiada por cem anos para permitir a alfabetização completa de todos os camponeses.", False)
        ],
        "- **Etapa 1:** Em Pele Negra, Máscaras Brancas (1952), Fanon diagnostica a alienação psíquica e a fenomenologia da corporeidade racializada nas metrópoles.\n- **Etapa 2:** Ao engajar-se na Frente de Libertação Nacional da Argélia e escrever Os Condenados da Terra (1961), Fanon conclui que a cura psíquica do colonizado exige a vitória política e militar da descolonização: a libertação do homem depende da emancipação material de sua terra, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Ao investigar a relação entre linguagem e opressão colonial em Fanon, qual papel é atribuído à imposição da língua da metrópole ao colonizado?",
        [
            ("Falar a língua do colonizador de forma perfeita é a primeira exigência assimilacionista, que força o negro a assumir os valores do império que o oprime.", True),
            ("Aprender novas línguas aumenta a velocidade de cicatrização de ferimentos provocados por picadas de insetos tropicais nos braços dos camponeses.", False),
            ("O domínio do vocabulário da corte europeia garantia a isenção vitalícia de impostos alfandegários para pescadores artesanais no Caribe.", False),
            ("O estudo da gramática latina clássica permitia que crianças camponesas pilotassem embarcações marítimas sem o auxílio de bússolas de metal.", False),
            ("As variações de entonação vocal em reuniões diplomáticas eram causadas exclusivamente pela ingestão de águas com elevado teor de enxofre.", False)
        ],
        "- **Etapa 1:** O primeiro capítulo de Pele Negra, Máscaras Brancas é dedicado ao tema: 'O Negro e a Linguagem'.\n- **Etapa 2:** Fanon demonstra que falar uma língua significa assumir um mundo e carregar o peso de uma civilização; na sociedade colonial antilhana, o negro é cobrado a falar o francês acadêmico escorreito para provar que é 'civilizado', mas essa mímica linguística reforça a subordinação ao poder branco imperial, validando a alternativa A."
    ))

    questoes_brutas.append((
        55, "EM13CHS501", "dificil",
        "Na superação dos impasses identitários, sob que fundamentos a desalienação fanoniana rejeita tanto as máscaras brancas quanto o tradicionalismo estático?",
        [
            ("Recusando a imitação das máscaras brancas e evitando a fixação em um passado idílico fossilizado, afirmando a soberania da invenção contínua da liberdade.", True),
            ("Propondo a fusão de todas as línguas nacionais em um código mecânico universal criado por linguistas teóricos de academias científicas da capital.", False),
            ("Exigindo que os cidadãos dos países do sul global renunciem ao uso de tecnologias modernas em favor de ferramentas rudimentares da pré-história.", False),
            ("Defendendo a censura prévia de romances poéticos e crônicas jornalísticas que façam referências a eventos da história colonial antiga.", False),
            ("Condicionando a participação cívica em eleições republicanas à apresentação de certificados de pureza genealógica expedidos por cartórios.", False)
        ],
        "- **Etapa 1:** De um lado, a assimilação aliena o negro no ideal do colonizador; de outro lado, o nacionalismo romântico ingênuo pode aprisioná-lo no culto cego ao passado pré-colonial.\n- **Etapa 2:** Fanon encontra a síntese libertadora: a desalienação é um ato de criação soberana no presente; o homem negro não precisa pedir licença ao branco nem ficar paralisado em mitos; ele é um homem livre entre iguais, comprometido com a construção de uma nova humanidade, o que comprova a alternativa A."
    ))

    questoes_brutas.append((
        56, "EM13CHS502", "dificil",
        "Sob a ótica pedagógica da Lei nº 10.639/2003, de que modo o ensino do Existencialismo Negro transforma as práticas escolares no Brasil?",
        [
            ("Rompendo com a visão eurocêntrica que reduzia o negro ao papel de escravo passivo, afirmando sua condição de sujeito pensante, filósofo e agente histórico.", True),
            ("Determinando que os estabelecimentos de ensino suspendam os cursos regulares de ciências biológicas para ministrar apenas disciplinas de etiqueta militar.", False),
            ("Obrigando os estudantes a decorarem datas de coroação de governantes monárquicos da Europa renascentista antes de ingressarem em cursos superiores.", False),
            ("Proibindo que os professores de filosofia façam comparações entre as ideias de autores europeus e as teorias de pensadores latino-americanos.", False),
            ("Exigindo a cobrança de taxas financeiras obrigatórias para a emissão de boletins de notas trimestrais em escolas públicas municipais.", False)
        ],
        "- **Etapa 1:** O currículo escolar tradicional brasileiro historicamente invisibilizou a intelectualidade negra, retratando o negro apenas no capítulo da escravidão.\n- **Etapa 2:** Ao levar Fanon, Lewis Gordon e intelectuais negras para a sala de aula, a Lei 10.639/03 opera um giro descolonial: os estudantes compreendem o negro como arquiteto de epistemologias densas, filósofo da liberdade e protagonista vivo da transformação emancipadora da sociedade, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        57, "EM13CHS504", "dificil",
        "Em diálogo com a teoria social brasileira, de que maneira a fenomenologia de Fanon fundamenta o conceito de racismo institucional de Silvio Almeida?",
        [
            ("Demonstrando que o racismo não é anomalia individual, mas regra de funcionamento que estrutura as práticas do Estado, do direito e da economia.", True),
            ("Afirmando que o racismo no Brasil foi extinto de modo pacífico com a promulgação do Código Civil de 1916 e a expansão de estradas de ferro.", False),
            ("Sustentando que os conflitos de raça nas cidades decorrem unicamente da falta de iluminação com lâmpadas incandescentes em vias públicas.", False),
            ("Defendendo que as corporações financeiras privadas devem manter segredo sobre as remunerações de seus diretores executivos da capital.", False),
            ("Provando que as diferenças salariais entre etnias resultam exclusivamente de preferências individuais na escolha de horários de lazer.", False)
        ],
        "- **Etapa 1:** Fanon demonstrou que o racismo colonial é totalizante e atravessa a língua, a medicina, a polícia e o cotidiano subjetivo das pessoas.\n- **Etapa 2:** O jurista e filósofo brasileiro Silvio Almeida atualiza essa linhagem: o racismo não é falha episódica ou desvio comportamental privado; é uma dimensão estrutural e institucional que molda o direito, o poder político e as relações de produção econômica, exigindo transformação sistêmica, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        58, "EM13CHS606", "dificil",
        "Ao investigar a relação entre a teoria de Fanon e a psicologia social de Neusa Santos Souza, qual impacto o ideal de branquitude provoca na subjetividade?",
        [
            ("Produz uma mutilação da autoimagem e uma auto-rejeição constante, onde o sujeito negro busca embranquecer-se para escapar da condenação social.", True),
            ("Estimula a fundação de empresas comerciais de exportação de café verde para abastecer entrepostos mercantis de províncias costeiras.", False),
            ("Garante a imunidade absoluta contra aflições respiratórias provocadas pelo acúmulo de poeiras industriais em fábricas têxteis da capital.", False),
            ("Assegura a aprovação unânime de propostas de reforma tributária apresentadas por comitês de finanças aos plenários das câmaras de deputados.", False),
            ("Incentiva o consumo de alimentos desidratados durante expedições de reconhecimento geográfico em regiões montanhosas do interior.", False)
        ],
        "- **Etapa 1:** Neusa Santos Souza investiga o drama da mobilidade social do negro em ascensão no Brasil: para ser tolerado, ele se depara com a exigência de adotar o 'ideal de ego branco'.\n- **Etapa 2:** Essa imposição gera um terrível sofrimento narcísico: o negro internaliza o padrão branco como beleza, sabedoria e pureza moral, passando a rejeitar seu próprio corpo, seus cabelos e sua história; romper com essa alienação exige a afirmação orgulhosa da negritude autêntica, legitimando a alternativa A."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "Ao relatar o episódio da criança na praça pública, como Frantz Fanon transforma radicalmente o debate existencialista sobre a alteridade?",
        [
            ("Evidenciando que a alteridade na sociedade colonial não é encontro simétrico entre consciências livres, mas imposição violenta de um estigma que coisifica.", True),
            ("Provando que os pedestres que circulam descalços pelas calçadas das cidades possuem reflexos mais rápidos diante de animais ferozes.", False),
            ("Demonstrando que os ruídos de carruagens puxadas por cavalos assustavam os transeuntes que caminhavam pelos bulevares das capitais.", False),
            ("Sustentando que os encontros fortuitos entre desconhecidos em jardins públicos devem ser registrados em atas notariais por tabeliães de cartórios.", False),
            ("Afirmando que a convivência harmônica entre os povos depende da uniformização dos cardápios alimentares servidos em cantinas escolares.", False)
        ],
        "- **Etapa 1:** O existencialismo e a fenomenologia europeus (Sartre, Lévinas) teorizavam o encontro com o Outro a partir de uma suposta paridade moral abstrata de olhares.\n- **Etapa 2:** Fanon choca a teoria com a realidade da opressão: na praça colonial, o olhar branco da criança não reconhece o negro como semelhante soberano; o olhar o devora, o aniquila e o devolve ao mundo como um objeto monstruoso fabricado pelo preconceito, validando a alternativa A."
    ))

    questoes_brutas.append((
        60, "EM13CHS102", "dificil",
        "Em conclusão ao Capítulo 35, que síntese filosófica expressa o papel fundador de Frantz Fanon na construção de um novo humanismo universal?",
        [
            ("A recusa radical da hierarquização racial e a refundação da liberdade na carne dos oprimidos, abrindo caminho para uma sociedade de seres humanos plenamente emancipados.", True),
            ("A proposição de que as disputas políticas internacionais entre nações sejam decididas por votações secretas em assembleias acadêmicas fechadas.", False),
            ("A restauração dos códigos civis da Idade Média como o modelo mais justo de regulamentação das relações de trabalho nas cidades industriais.", False),
            ("A substituição das pesquisas científicas sobre medicina preventiva pela memorização diária de tratados astrológicos da Antiguidade oriental.", False),
            ("O isolamento das populações descolonizadas em arquipélagos territoriais desprovidos de qualquer diálogo com os saberes do mundo contemporâneo.", False)
        ],
        "- **Etapa 1:** Frantz Fanon não encerrou seu pensamento no ressentimento amargo nem no ódio separatista, mas convocou a humanidade a 'dar meia-volta' e fundar um novo homem.\n- **Etapa 2:** O Existencialismo Negro fanoniano refunde a filosofia: liberta a liberdade das abstrações eurocêntricas e a ancora no corpo que sofre, que resiste e que interroga; ao destruir a mentira do racismo colonial, Fanon entrega à história universal a bússola inegociável da dignidade de todos os seres humanos, coroando a alternativa A com glória incontestável!"
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
    md.append('capitulo: "Capítulo 35: O Existencialismo Negro em Frantz Fanon"')
    md.append('objeto_de_conhecimento: "O existencialismo negro em Frantz Fanon, a experiência vivida do negro, o esquema histórico-racial e a amputação corporal, a crítica a Sartre em Orfeu Negro e a oração do corpo interrogador"')
    md.append('ebook_fonte: "em-fil-c35-existencialismo-negro-frantz-fanon.md"')
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

    md.append("# Lista de Exercícios: O Existencialismo Negro em Frantz Fanon\n")
    md.append("## Nível Básico\n")

    letras = ["A", "B", "C", "D", "E"]

    for num, hab, dif, enunciado, alternativas, resolucao in questoes:
        if num == 21:
            md.append("## Nível Intermediário\n")
        elif num == 41:
            md.append("## Nível Difícil\n")

        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-35-existencialismo-negro-frantz-fanon -->")
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
    md.append("- FANON, Frantz. *Pele negra, máscaras brancas*. Tradução de Renato da Silveira. Salvador: EDUFBA, 2008.")
    md.append("- GORDON, Lewis R. *Existentia Africana: understanding Africana existential thought*. New York: Routledge, 2000.")
    md.append("- MERLEAU-PONTY, Maurice. *Fenomenologia da percepção*. Tradução de Carlos Alberto Ribeiro de Moura. 4. ed. São Paulo: Martins Fontes, 2011.")
    md.append("- SARTRE, Jean-Paul. *O ser e o nada*. Tradução de Paulo Perdigão. 13. ed. Petrópolis: Vozes, 2005.")
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
    destino_final = "content/medio/volume-unico/filosofia/eixo-5-existencialismo-diferenca/cap-35-existencialismo-negro-frantz-fanon/ebooks/em-fil-c35-existencialismo-negro-frantz-fanon-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 35 validado e homologado com Exit Code 0!")
        print("MARCO HISTÓRICO DE 35 CAPÍTULOS E 2.100 QUESTÕES HOMOLOGADAS!")
        print("LOTE 7 (CAPS 31 AO 35) CONCLUÍDO COM 100% DE APROVAÇÃO!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
