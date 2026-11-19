# -*- coding: utf-8 -*-
"""
Script de geração e validação da Lista de Exercícios - Capítulo 17: A Política na Antiguidade: Platão e Aristóteles
Padrão-Ouro Educamob: 60 questões (20 básicas, 20 intermediárias, 20 difíceis com Etapa 1 e Etapa 2).
Gabarito balanceado: exatamente 12 A, 12 B, 12 C, 12 D, 12 E.
"""

import sys
import subprocess
from collections import Counter

def gerar_lista():
    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Qual foi a inovação fundamental da pólis grega clássica em relação aos impérios teocráticos orientais da Antiguidade?",
        "A substituição do combate naval pelo uso exclusivo de arqueiros montados a cavalo.",
        "A transferência das decisões coletivas das vontades arbitrárias de reis ou oráculos para o debate público e a deliberação racional dos cidadãos na ágora.",
        "A proibição do cultivo de oliveiras e videiras em encostas de montanhas rurais.",
        "A determinação de que todas as casas deveriam ser construídas com blocos de mármore branco.",
        "A exigência de que os tratados comerciais fossem chancelados por sacerdotes do Egito antigo.",
        "B",
        "A pólis inaugurou a política ocidental ao consagrar a força da palavra argumentativa (logos) no espaço público como fonte de autoridade legítima para as leis da cidade."
    ))

    questoes_brutas.append((
        2, "EM13CHS601", "basico",
        "O que significava o princípio da 'Isonomia' na democracia ateniense do século V a.C.?",
        "A obrigação de todos os cidadãos possuírem o mesmo saldo de moedas de prata no tesouro municipal.",
        "A igualdade formal de todos os cidadãos perante a lei escrita da cidade, sem privilégios de berço.",
        "A exigência de que todos os soldados de infantaria utilizassem escudos do mesmo diâmetro.",
        "A divisão do trigo colhido nas lavouras públicas em porções rigorosamente idênticas.",
        "O direito de os generais militares alterarem as sentenças dos juízes civis sem consulta à assembleia.",
        "B",
        "Isonomia garantia que a lei (nomos) fosse uma regra comum a todos os membros da comunidade cívica, protegendo o cidadão contra o arbítrio de governantes."
    ))

    questoes_brutas.append((
        3, "EM13CHS601", "basico",
        "Qual era o direito consagrado pelo pilar da 'Isegoria' nas assembleias soberanas de Atenas (Ekklesia)?",
        "O direito de caçar animais selvagens em florestas de carvalhos durante a primavera.",
        "O direito igual de qualquer cidadão tomar a palavra livremente na assembleia para propor, defender ou contestar leis.",
        "A autorização para que mercadores estrangeiros vendessem tecidos importados sem pagar taxas aduaneiras.",
        "A permissão para que os proprietários de navios comandassem frotas de guerra sem treinamento militar.",
        "A determinação de que os julgamentos civis fossem realizados exclusivamente durante a noite.",
        "B",
        "Isegoria era a igualdade de fala: na assembleia ateniense, qualquer cidadão comum tinha o direito fundamental de subir à tribuna e expressar seu voto e sua opinião."
    ))

    questoes_brutas.append((
        4, "EM13CHS602", "basico",
        "Quais grupos sociais estavam sumariamente excluídos da cidadania na democracia ateniense clássica?",
        "Apenas os navegadores que viajavam em embarcações mercantes para o mar Negro.",
        "As mulheres, as pessoas escravizadas e os estrangeiros domiciliados na cidade (metecos).",
        "Apenas os filósofos que frequentavam os jardins da Academia de Platão.",
        "Os soldados de cavalaria e os arqueiros que utilizavam capacetes de bronze.",
        "Os artesãos que trabalhavam em olarias de cerâmica decorada com figuras vermelhas.",
        "B",
        "A cidadania ateniense era altamente seletiva: reservava-se a homens adultos livres nascidos de pai e mãe atenienses, excluindo cerca de 85% a 90% da população total da pólis."
    ))

    questoes_brutas.append((
        5, "EM13CHS102", "basico",
        "Qual evento histórico e biográfico marcou profundamente a desconfiança de Platão em relação à democracia ateniense?",
        "A vitória naval de Atenas sobre as frotas do Império Persa nas águas de Salamina.",
        "A condenação à morte de seu mestre Sócrates em 399 a.C., decretada por votação da maioria na assembleia democrática.",
        "A construção do Partenon na colina da Acrópole sob a liderança de Péricles.",
        "A fundação de colônias comerciais gregas na ilha da Sicília por marinheiros coríntios.",
        "A celebração dos primeiros Jogos Olímpicos na cidade de Olímpia no Peloponeso.",
        "B",
        "A execução de Sócrates — considerado por Platão o mais sábio dos homens — provou a falência da democracia, que se revelou um governo de paixões ignorantes guiadas por demagogos."
    ))

    questoes_brutas.append((
        6, "EM13CHS601", "basico",
        "Como Platão descreve a metáfora da 'Nau do Estado' em A República para criticar a escolha democrática de governantes?",
        "Comparando a cidade a um barco de pesca que navega em rios tranquilos sem necessidade de leme.",
        "Afirmando que entregar o poder por voto de popularidade é tão absurdo quanto escolher o comandante do navio pelo agrado de marinheiros embriagados, em vez de entregá-lo ao piloto que domina a arte da navegação.",
        "Defendendo que todos os passageiros de um navio comercial devem revezar o comando a cada hora de viagem.",
        "Sustentando que os veleiros de guerra devem ser manobrados exclusivamente por remadores voluntários desarmados.",
        "Provando que as bússolas marinhas foram inventadas por tecelões que trabalhavam em oficinas urbanas.",
        "B",
        "Na metáfora da nau, Platão demonstra que governar é uma ciência rigorosa que exige sabedoria verdadeira; entregar o comando ao mais popular ou demagogo leva o navio ao naufrágio."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "Na cidade ideal de Platão (Kallipolis), qual classe social é responsável pela produção dos alimentos e bens materiais da pólis?",
        "Os guardiões guerreiros que vigiam as muralhas externas.",
        "Os artífices e produtores (comerciantes, agricultores e artesãos), cuja virtude correspondente é a moderação.",
        "Os reis-filósofos que contemplaram a Ideia do Bem Supremo.",
        "Os oradores profissionais que ensinam técnicas de retórica em praças públicas.",
        "Os marinheiros que transportam cerâmica pintada em rotas marítimas.",
        "B",
        "A classe dos produtores corresponde à parte concupiscível da alma: deve ser guiada pela temperança e moderação para sustentar materialmente a cidade sem interferir nas leis."
    ))

    questoes_brutas.append((
        8, "EM13CHS102", "basico",
        "Qual virtude ética fundamental deve guiar a classe dos 'Guardiões' em A República de Platão?",
        "A esperteza comercial para obter lucros em feiras municipais.",
        "A coragem, correspondente à parte irascível da alma, para defender a pólis contra ataques externos e manter a ordem interna.",
        "A habilidade manual na escultura de estátuas com pedras de mármore.",
        "A destreza na montaria de cavalos selvagens durante caçadas noturnas.",
        "A capacidade de redigir poemas líricos para apresentações em teatros da capital.",
        "B",
        "Os guardiões encarnam a força e a bravura da alma irascível: devem ser destemidos contra inimigos e leais e protetores em relação aos cidadãos da cidade."
    ))

    questoes_brutas.append((
        9, "EM13CHS601", "basico",
        "O que propõe a célebre tese da 'Sofocracia' formulada por Platão em A República?",
        "Que o poder político supremo da pólis seja exercido por generais militares condecorados em guerras.",
        "Que os filósofos se tornem governantes ou que os governantes se tornem filósofos autênticos, fundando a política na sabedoria da razão.",
        "Que todos os cidadãos da cidade sejam obrigados a trabalhar em lavouras coletivas de trigo.",
        "Que os magistrados públicos sejam sorteados anualmente entre os artesãos mais idosos.",
        "Que as leis civis sejam abolidas em favor de acordos verbais entre vizinhos de bairro.",
        "B",
        "A sofocracia é o governo dos sábios: quem deve guiar a cidade é quem contemplou a Verdade inteligível e o Bem em si mesmo, governando com desprendimento e justiça."
    ))

    questoes_brutas.append((
        10, "EM13CHS602", "basico",
        "Para evitar a corrupção e o enriquecimento pessoal no exercício do poder, qual medida drástica Platão impôs aos governantes e guardiões de Kallipolis?",
        "O aumento anual dos salários pagos em barras de ouro maciço do tesouro público.",
        "A abolição total da propriedade privada e a comunidade de bens e famílias para as castas dirigentes, evitando o nepotismo e a ganância particular.",
        "A concessão de fazendas agrícolas privadas nas encostas férteis das montanhas.",
        "O direito de cobrar tributos pessoais sobre mercadorias vendidas nas feiras do porto.",
        "A permissão para comercializarem cavalos de raça com reinos vizinhos em alto-mar.",
        "B",
        "Sem propriedade privada e sem herança familiar exclusiva, o governante platônico cuida da cidade inteira como seu único bem, não tendo incentivo para desviar recursos públicos."
    ))

    questoes_brutas.append((
        11, "EM13CHS501", "basico",
        "Qual é a célebre definição antropológica e política do ser humano formulada por Aristóteles em A Política?",
        "O homem é um animal solitário que prefere habitar cavernas escuras e isoladas.",
        "O homem é, por natureza, um animal político (zoon politikon), cuja realização ética plena só ocorre na convivência da pólis.",
        "O homem é um guerreiro selvagem cuja única missão consiste em aniquilar povos vizinhos.",
        "O homem é um ser mecânico formado por engrenagens que obedecem a leis hidráulicas.",
        "O homem é um agente econômico focado unicamente na acumulação individual de riquezas mercantis.",
        "B",
        "Para Aristóteles, a sociabilidade não é capricho ou acidente: quem não vive em sociedade ou é uma besta inferior ou um deus autossuficiente; o humano precisa da pólis para ser feliz."
    ))

    questoes_brutas.append((
        12, "EM13CHS502", "basico",
        "Segundo Aristóteles, qual característica natural singular distingue os seres humanos dos demais animais gregários (como abelhas e formigas)?",
        "A capacidade de nadar velozmente em águas marinhas agitadas por tempestades.",
        "A posse do Logos (a linguagem articulada e a razão), que permite deliberar e expressar o justo e o injusto, o bem e o mal.",
        "A habilidade de construir abrigos de madeira utilizando ferramentas de ferro forjado.",
        "O fato de possuir cinco dedos articulados nas mãos e nos pés com unhas planas.",
        "A necessidade de consumir alimentos cozidos em fornos aquecidos com lenha seca.",
        "B",
        "Enquanto os animais têm apenas a voz (phone) para indicar dor e prazer, o homem possui o logos para criar a justiça, a moral e a política compartilhada."
    ))

    questoes_brutas.append((
        13, "EM13CHS603", "basico",
        "Na análise de Aristóteles, qual é a finalidade ética suprema da Pólis que a distingue de uma mera aldeia ou aliança comercial?",
        "Garantir que as frotas de navios mercantes consigam vender tecidos em portos estrangeiros.",
        "A pólis surgiu para assegurar a vida biológica, mas subsiste e se organiza para viabilizar o 'bem viver' (eu zen), a virtude e a felicidade coletiva.",
        "Arrecadar o maior volume de tributos fiscais para financiar desfiles militares festivos.",
        "Obrigar todos os moradores urbanos a dormirem o mesmo número de horas durante a noite.",
        "Proibir a realização de debates públicos para manter a disciplina rígida dos cidadãos.",
        "B",
        "A política não existe apenas para garantir a sobrevivência física ou o comércio; seu objetivo é nobre e ético: promover o florescimento da virtude humana na comunidade."
    ))

    questoes_brutas.append((
        14, "EM13CHS601", "basico",
        "Qual é o critério ético e qualitativo utilizado por Aristóteles para distinguir as 'Formas Puras' das 'Formas Degeneradas' de governo?",
        "A quantidade de soldados que desfilam armados diante dos palácios municipais.",
        "O exercício do poder em favor do bem comum de toda a coletividade (forma pura) versus o exercício em proveito egoísta dos próprios governantes (forma degenerada).",
        "A idade média dos magistrados que compõem o conselho deliberativo da cidade.",
        "A localização geográfica da capital em planícies férteis ou em encostas rochosas.",
        "A quantidade de livros didáticos guardados nas bibliotecas públicas da cidade.",
        "B",
        "Um governo é justo quando busca a felicidade geral da pólis; se o governante usa o poder para se beneficiar ou enriquecer sua facção, o regime torna-se ilegítimo e corrompido."
    ))

    questoes_brutas.append((
        15, "EM13CHS601", "basico",
        "Quais são as três formas de governo consideradas 'Puras e Legítimas' na tipologia política de Aristóteles?",
        "Tirania, Oligarquia e Demagogia popular.",
        "Monarquia (governo de um só), Aristocracia (governo de poucos melhores) e Politeia (governo da maioria sob a lei).",
        "Império absoluto, Feudalismo agrário e Corporativismo fabril.",
        "Ditadura de generais, República mercantil e Teocracia monástica.",
        "Anarquia rural, Monarquia despótica e Plutocracia financeira.",
        "B",
        "As formas puras governam para o bem comum: um só virtuoso governa na Monarquia; os melhores e sábios na Aristocracia; e a maioria cidadã constitucional na Politeia."
    ))

    questoes_brutas.append((
        16, "EM13CHS601", "basico",
        "Quando o exercício da autoridade se desvia do interesse coletivo para servir aos apetites particulares dos governantes, a cidade sofre uma degeneração institucional. De acordo com o livro A Política, quais são as três formas corrompidas de governo que surgem desse desvio ético?",
        "Monarquia esclarecida, Aristocracia tradicional e República constitucional.",
        "A Tirania (usurpação egocêntrica de um só), a Oligarquia (domínio egoísta dos ricos) e a Democracia demagógica (governo faccioso da maioria despossuída sem freios legais).",
        "Presidencialismo de coalizão, Parlamentarismo monárquico e Federação distrital.",
        "Conselho de anciãos guerreiros, Junta militar de infantaria e Federação de corporações de artesãos.",
        "Tribunais eclesiásticos, Comitês agrários de camponeses e Câmaras de mercadores estrangeiros.",
        "B",
        "O desvio do bem comum corrompe as formas retas: a tirania desvirtua o rei; a oligarquia privatiza o Estado em prol dos detentores da riqueza; e a demagogia desorganiza a cidade ao ignorar a lei."
    ))

    questoes_brutas.append((
        17, "EM13CHS603", "basico",
        "Por que Aristóteles defende a superioridade prática da 'Politeia' alicerçada em uma ampla 'Classe Média'?",
        "Porque a classe média consome grandes quantidades de azeite e grãos de trigo importados.",
        "Porque a classe média encontra-se equidistante da arrogância dos super-ricos e do desespero dos miseráveis, atuando como moderadora e garantindo estabilidade e equilíbrio à república.",
        "Porque os membros da classe média possuem carruagens de madeira com rodas reforçadas com ferro.",
        "Porque a classe média é obrigada por decretos municipais a prestar serviços voluntários na marinha.",
        "Porque os cidadãos de classe média são os únicos que dominam técnicas de escultura em cerâmica.",
        "B",
        "A classe média encarna a moderação aristotélica na política: onde ela é forte, evita-se a guerra civil entre oligarcas gananciosos e massas famintas, mantendo a paz constitucional."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "Qual é um erro comum muito frequente sobre a concepção aristotélica de 'Animal Político'?",
        "Reconhecer que o homem é um ser social dotado de linguagem e ética comunitária.",
        "Imaginar que ser um animal político significa ter paixão por disputas partidárias, campanhas eleitorais ou ambição de exercer cargos governamentais.",
        "Compreender que o ser humano necessita da convivência na pólis para atingir a virtude.",
        "Saber que a família e a aldeia antecedem historicamente a formação da cidade autossuficiente.",
        "Identificar que a solidão absoluta desumaniza o indivíduo que se isola da comunidade.",
        "B",
        "Para Aristóteles, zoon politikon não é sobre votos ou partidos; é sobre nossa destinação existencial e social: nossa natureza humana floresce na convivência da cidade justa."
    ))

    questoes_brutas.append((
        19, "EM13CHS602", "basico",
        "Como a prática democrática ateniense realizava a escolha da maioria dos magistrados e membros dos tribunais populares?",
        "Por meio de leilões financeiros em que vencia o comerciante que pagasse mais moedas de ouro.",
        "Por meio de sorteio público anual entre todos os cidadãos aptos, assegurando a alternância democrática de poder.",
        "Através de disputas de corrida e luta física na arena desportiva municipal.",
        "Mediante indicação hereditária transmitida de pais para filhos primogênitos.",
        "Por meio de decretos lavrados por sacerdotes de templos religiosos litorâneos.",
        "B",
        "O sorteio (kleroterion) era a alma da democracia ateniense: evitava a formação de castas de políticos profissionais e garantia que qualquer cidadão comum pudesse governar."
    ))

    questoes_brutas.append((
        20, "EM13CHS101", "basico",
        "Qual é a diferença central no método de reflexão política de Platão em relação ao método de Aristóteles?",
        "Platão viajou em navios mercantes pelo mar Vermelho, enquanto Aristóteles viveu em um convento.",
        "Platão formulou uma cidade ideal perfeita e normativa a partir da teoria das Ideias (dedução racional), enquanto Aristóteles estudou e comparou 158 constituições reais de cidades (indução e empirismo).",
        "Platão defendia a privatização das escolas públicas, enquanto Aristóteles exigia o fechamento dos teatros.",
        "Platão acreditava que os animais marinhos tinham almas políticas, enquanto Aristóteles rejeitava a biologia.",
        "Platão proibia o uso de moedas de prata, enquanto Aristóteles defendia a cobrança de juros compostos.",
        "B",
        "Platão desenha em A República a cidade perfeita que deveria ser; Aristóteles em A Política analisa as cidades que existem de fato para encontrar o melhor regime empiricamente viável."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Como Platão articula o conceito de 'Justiça' (Dikaiosyne) em Kallipolis com a teoria da harmonia das partes da alma?",
        "Afirmando que a justiça é a distribuição igualitária de alimentos e roupas entre todos os habitantes.",
        "Definindo a justiça como a harmonia funcional e a ordem hierárquica na qual cada classe social realiza com perfeição a sua virtude própria sem invadir o papel das demais.",
        "Sustentando que a justiça é a imposição da vontade do guerreiro mais forte sobre os mais fracos.",
        "Comprovando que a justiça depende do pagamento pontual de impostos alfandegários no porto marítimo.",
        "Determinando que a justiça exige que todos os cidadãos aprendam a tocar instrumentos musicais de corda.",
        "B",
        "A justiça platônica é harmonia cósmica e política: há ordem quando a razão governa, a coragem defende e os desejos produzem com moderação, sem usurpação de funções."
    ))

    questoes_brutas.append((
        22, "EM13CHS601", "intermediario",
        "Ao examinar a tese aristotélica da primazia da Pólis sobre o indivíduo, por que o filósofo afirma que 'o todo é necessariamente anterior à parte'?",
        "Porque os edifícios públicos de pedra foram erguidos antes das residências familiares de madeira.",
        "Porque, assim como uma mão decepada do corpo deixa de ser verdadeiramente uma mão funcional, o indivíduo isolado da cidade perde sua destinação ética e seu estatuto de humanidade plena.",
        "Porque os primeiros reis da Grécia eram mais idosos do que os agricultores que cultivavam cevada.",
        "Porque as leis escritas das cidades foram copiadas de inscrições antigas encontradas na Mesopotâmia.",
        "Porque as assembleias cívicas exigiam a presença física de todos os moradores do território urbano.",
        "B",
        "A anterioridade é existencial e finalista: o indivíduo só adquire sentido humano no seio da pólis; separado da comunidade política, ele regride à barbárie animalesca."
    ))

    questoes_brutas.append((
        23, "EM13CHS602", "intermediario",
        "De que modo a exclusão das mulheres da cidadania ateniense refletia a rígida separação entre o 'Espaço Público' (Ágora) e o 'Espaço Privado' (Oikos)?",
        "As mulheres preferiam trabalhar na colheita de uvas nas encostas férteis das colinas do interior.",
        "O espaço público da ágora era o reino da liberdade, do logos e da igualdade política entre pares, enquanto o oikos doméstico era o domínio da necessidade biológica, das tarefas servis e da hierarquia patriarcal que confinava a mulher.",
        "As leis municipais de trânsito proibiam que pessoas descalças circulassem pelas calçadas de pedra da capital.",
        "Os sacerdotes dos templos religiosos exigiam que as mulheres fizessem votos perpétuos de silêncio e jejum.",
        "As assembleias de cidadãos eram realizadas em horários que coincidiam com o preparo de refeições familiares.",
        "B",
        "Para os gregos, a liberdade política na ágora dependia da servidão e do silêncio do oikos doméstico: a mulher geria as necessidades da casa para que o homem desfrutasse do debate cívico."
    ))

    questoes_brutas.append((
        24, "EM13CHS102", "intermediario",
        "Por que, para Platão, a democracia desemboca frequentemente na 'Tirania'?",
        "Porque os cidadãos democráticos se recusam a construir fortificações militares nas fronteiras terrestres.",
        "Porque a liberdade democrática irrestrita degrada-se em anarquia e desordem moral; em meio ao caos social, surge um demagogo audacioso que se apresenta como defensor do povo, concentra o poder absoluto e transforma-se em tirano opressor.",
        "Porque as eleições populares exigiam gastos orçamentários excessivos com a impressão de cédulas de papel.",
        "Porque os comandantes de frotas navais eram obrigados a dividir suas rações diárias de comida com marinheiros.",
        "Porque os tribunais civis cancelavam as sessões de julgamento durante os períodos de eclipse solar.",
        "B",
        "Platão identifica a dialética fatal da democracia degenerada: a anarquia de desejos sem freio clama por um 'salvador da pátria' demagogo, que logo usurpa as instituições e escraviza a cidade."
    ))

    questoes_brutas.append((
        25, "EM13CHS601", "intermediario",
        "Como a teoria contemporânea da 'Esfera Pública' de Jürgen Habermas resgata e ressignifica a experiência da Ágora grega?",
        "Exigindo que os parlamentos modernos sejam construídos ao ar livre em praças públicas de capitais.",
        "Sustentando que a legitimidade democrática contemporânea reside na vitalidade de espaços deliberativos onde cidadãos livres debatem racionalmente com base no melhor argumento, livres de coações burocráticas ou econômicas.",
        "Determinando que os jornais impressos de circulação nacional sejam lidos em voz alta por arautos municipais.",
        "Propondo que os cargos de ministros de Estado devam ser preenchidos mediante sorteios anuais de cidadãos.",
        "Defendendo que as decisões de política econômica devam ser tomadas por conselhos de oficiais de infantaria.",
        "B",
        "Habermas atualiza o ideal clássico do logos na ágora: uma democracia autêntica necessita de uma esfera pública viva, onde o argumento racional dos cidadãos oriente as decisões do Estado."
    ))

    questoes_brutas.append((
        26, "EM13CHS603", "intermediario",
        "Qual é a relação estrutural entre o 'Trabalho Escravo' e a conquista da cidadania plena na Grécia Antiga?",
        "Os escravizados recebiam salários diários que lhes permitiam comprar assentos na assembleia popular.",
        "A escravidão fornecia a base material de produção de alimentos e artesanato, liberando o cidadão livre das tarefas manuais e concedendo-lhe o ócio indispensável (skholé) para dedicar seu tempo aos debates e à governança da pólis.",
        "As pessoas escravizadas participavam de comissões técnicas encarregadas de fiscalizar a arrecadação de tributos.",
        "Os proprietários de terras eram obrigados a prestar serviços braçais na limpeza de praças e teatros municipais.",
        "As leis de Atenas proibiam que os proprietários agrícolas utilizassem ferramentas mecânicas em suas lavouras.",
        "B",
        "O ócio político (skholé) grego não era preguiça; era a dedicação integral ao bem comum da cidade, e esse privilégio aristocraticamente restrito só era possível porque os escravizados sustentavam a labuta."
    ))

    questoes_brutas.append((
        27, "EM13CHS501", "intermediario",
        "Na classificação de Aristóteles, qual é a diferença crucial entre a 'Politeia' (governo constitucional) e a 'Democracia' degenerada?",
        "A Politeia utiliza moedas de bronze cunhadas na cidade, enquanto a Democracia utiliza moedas de prata estrangeiras.",
        "Na Politeia a maioria cidadã governa submetida ao império da lei escrita e buscando o bem comum de todos, enquanto na Democracia degenerada a maioria plebeia governa desrespeitando as leis e espoliando os ricos pela demagogia.",
        "A Politeia é comandada exclusivamente por almirantes da marinha de guerra em tempos de confronto bélico.",
        "A Democracia proíbe a realização de casamentos entre cidadãos de classes socioeconômicas distintas.",
        "A Politeia exige que todos os habitantes adultos usem fardamentos de tecido de lã crua em dias festivos.",
        "B",
        "Para Aristóteles, a democracia pura degenerada é o governo da massa irracional guiada por demagogos sem respeito às leis fundamentais; a Politeia equilibra liberdade e lei em prol do bem geral."
    ))

    questoes_brutas.append((
        28, "EM13CHS502", "intermediario",
        "Como a distinção aristotélica entre 'Justiça Distributiva' e 'Justiça Comutativa' opera na prática social e jurídica?",
        "A distributiva regula o transporte de mercadorias em rios, enquanto a comutativa regula a navegação litorânea.",
        "A distributiva reparte bens públicos e honrarias de forma proporcional ao mérito e à necessidade de cada um (proporção geométrica), enquanto a comutativa regula as trocas particulares e contratos na igualdade estrita aritmética de valor.",
        "A distributiva concede propriedades rurais a generais condecorados, enquanto a comutativa proíbe o comércio de cereais.",
        "A distributiva é aplicada exclusivamente em julgamentos de crimes de traição à pátria militar.",
        "A comutativa estabelece que todas as sentenças judiciais devem ser homologadas por sacerdotes de Delfos.",
        "B",
        "Na distributiva trata-se desigualmente os desiguais segundo seu valor/necessidade (equidade); na comutativa a troca deve ser rigorosamente equivalente (pagar exatamente o valor da mercadoria)."
    ))

    questoes_brutas.append((
        29, "EM13CHS601", "intermediario",
        "De que modo a defesa contemporânea de 'Governos Tecnocráticos' (decisões econômicas entregues exclusivamente a especialistas não eleitos) reatualiza o projeto da Sofocracia de Platão?",
        "Obrigando os ministros da fazenda a utilizarem túnicas de linho branco em sessões plenárias no congresso.",
        "Sustentando a premissa de que a condução das finanças e do Estado exige um saber técnico-científico complexo que o cidadão comum não domina, devendo o poder ser exercido por peritos qualificados e imunes à pressão eleitoral das massas.",
        "Determinando que os bancos centrais devam emitir cédulas de papel-moeda com retratos de atletas olímpicos.",
        "Exigindo que as pesquisas acadêmicas de economia aplicada sejam traduzidas para a língua grega clássica.",
        "Proibindo os cidadãos que possuem cartões bancários de participarem de plebiscitos e consultas eleitorais.",
        "B",
        "A tecnocracia moderna é herdeira da sofocracia: presume que o povo é ignorante e que apenas uma elite técnica esclarecida pode decidir o rumo do Estado, subtraindo o debate da soberania popular."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Por que Platão propôs a dissolução da Família Tradicional e a educação das crianças pelo Estado para as castas dirigentes de Kallipolis?",
        "Para que as crianças fossem treinadas exclusivamente em competições de corrida de revezamento no campo.",
        "Para erradicar o nepotismo e os afetos de favorecimento particular, garantindo que os magistrados cuidem de todos os jovens da cidade com o mesmo amor desinteressado e dediquem suas vidas ao bem público comum.",
        "Para reduzir as despesas orçamentárias com a construção de dormitórios e creches nos bairros centrais.",
        "Para permitir que os pais pudessem realizar viagens anuais de exploração geográfica em países distantes.",
        "Para assegurar que as certidões civis fossem guardadas em recipientes de bronze lacrados com cera.",
        "B",
        "O governante que favorece seu filho comete injustiça: ao criar as crianças em comum pelo Estado, Platão pretendia forjar governantes totalmente desprovidos de interesses dinásticos particulares."
    ))

    questoes_brutas.append((
        31, "EM13CHS603", "intermediario",
        "Qual é a relação entre o diagnóstico de Aristóteles sobre a 'Desigualdade Extrema de Renda' e a eclosão de revoluções e tiranias nas cidades gregas?",
        "A constatação de que os cidadãos ricos comiam alimentos excessivamente gordurosos durante o inverno.",
        "A constatação de que o abismo socioeconômico divide a cidade em dois blocos inimigos (os super-ricos que desprezam os pobres e os miseráveis desesperados), gerando ódio mútuo que destrói a amizade cívica e alimenta golpes tirânicos.",
        "A comprovação de que as indústrias têxteis consumiam muita água potável na lavagem de tecidos de lã.",
        "A certeza de que as famílias que moravam no campo tinham maior fertilidade biológica do que as da capital.",
        "A determinação de que os impostos sobre o gado bovino deveriam ser pagos exclusivamente em sacos de farinha.",
        "B",
        "A desigualdade extrema polariza e destrói a pólis: quando não há coesão nem classe média, a cidade vira um campo de guerra civil perpétua entre oligarcas gananciosos e plebeus famintos."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Em A República, Platão apresenta o 'Mito das Raças' (ou Nobre Mentira). Qual era a finalidade política pedagógica dessa narrativa mítica na cidade ideal?",
        "Ensinar os agricultores a reconhecerem minérios de ferro e cobre enterrados no solo durante o arado.",
        "Convencer os cidadãos de que a divisão social do trabalho e o pertencimento a cada classe decorriam de uma vocação natural da alma (ouro nos governantes, prata nos guardiões e bronze nos produtores), garantindo harmonia e aceitação pacífica das funções.",
        "Obrigar as famílias de artesãos a comprarem joias de metal precioso para cerimônias de casamento.",
        "Justificar a cobrança de tributos municipais proporcionais à quantidade de cavalos utilizados no transporte.",
        "Demonstrar que as estátuas esculpidas em bronze possuíam propriedades mágicas de proteção às muralhas da cidade.",
        "B",
        "A nobre mentira de Platão era um mito pedagógico de coesão: buscava fazer os cidadãos aceitarem suas vocações com serenidade, compreendendo que todas as classes são irmãs filhas da mesma terra."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "De que modo a atuação dos 'Demagogos' na Atenas antiga dialoga diretamente com o fenômeno das 'Fake News' e do populismo digital contemporâneo?",
        "Determinando que os oradores públicos utilizem microfones acústicos confeccionados com conchas marinhas.",
        "Evidenciando que a manipulação oratória de medos, rancores e preconceitos populares corrompe o debate racional da ágora cívica, substituindo argumentos fundamentados em fatos pela histeria e pela desinformação planejada para alcançar o poder.",
        "Provando que as cartas diplomáticas eram enviadas por mensageiros que corriam a pé entre as cidades vizinhas.",
        "Afirmando que os jornais da oposição política devem ter suas sedes administrativas fiscalizadas por guardas municipais.",
        "Sustentando que as campanhas eleitorais devem ser financiadas exclusivamente mediante doações de cereais colhidos no campo.",
        "B",
        "O demagogo ateniense e o manipulador de redes digitais usam o mesmo método: inflamam as paixões mais vis da massa para calar a razão e destruir as salvaguardas republicanas da democracia."
    ))

    questoes_brutas.append((
        34, "EM13CHS502", "intermediario",
        "Por que, para Aristóteles, a 'Amizade Cívica' (Philia) é um pilar tão ou mais importante para a cidade do que as próprias leis escritas?",
        "Porque os cidadãos amigos dividem suas despesas de alimentação em restaurantes comerciais da capital.",
        "Porque a concórdia afetiva e o laço de fraternidade e solidariedade entre os cidadãos sustentam a coesão da vida pública; onde não há amizade cívica, as leis são violadas com hipocrisia e a pólis desmorona em facções rivais.",
        "Porque os tratados de amizade internacional eram registrados em pergaminhos selados com cera vermelha.",
        "Porque as leis cívicas de Atenas proibiam conversas entre vizinhos que discordassem sobre temas de astronomia.",
        "Porque a prática da amizade garantia que os comerciantes recebessem descontos na compra de tecidos importados.",
        "B",
        "Aristóteles afirma que a amizade mantém as cidades unidas mais do que a justiça fria: quando os cidadãos se estimam e compartilham um destino comum, a justiça floresce com naturalidade."
    ))

    questoes_brutas.append((
        35, "EM13CHS602", "intermediario",
        "Como a condição dos 'Metecos' (estrangeiros livres residentes em Atenas) ilustra as tensões entre Economia e Cidadania na Antiguidade?",
        "Eles eram proibidos de praticar qualquer atividade artesanal e sobreviviam de doações públicas de trigo.",
        "Apesar de serem motores essenciais da economia comercial, industrial e tributária de Atenas, eram sumariamente privados de direitos políticos deliberativos, não podiam votar na assembleia nem possuir terras no território da pólis.",
        "Eles comandavam as frotas de navios de guerra nas batalhas marítimas contra as cidades inimigas.",
        "Eles eram obrigados a aprender a tocar instrumentos musicais de sopro para cerimônias litúrgicas municipais.",
        "Eles exerciam com exclusividade as funções de magistrados nos tribunais de julgamento criminal da capital.",
        "B",
        "O meteco vivia uma cidadania econômica amputada da cidadania política: gerava riqueza e pagava taxas, mas a pólis aristocrática mantinha as decisões políticas fechadas a quem não tinha sangue ateniense."
    ))

    questoes_brutas.append((
        36, "EM13CHS102", "intermediario",
        "Por que é incorreto associar a proposta da Sofocracia de Platão aos regimes totalitários e fascistas do século XX?",
        "Porque os governantes fascistas utilizavam cavalos em seus desfiles militares pelas avenidas centrais.",
        "Porque o rei-filósofo platônico governa como um estrito dever de sacrifício ético imposto pela razão, sem exército pessoal de bajuladores, sem propriedades privadas, sem privilégios materiais e subordinado à Verdade inteligível do Bem.",
        "Porque as ditaduras totalitárias da Europa central proibiam o ensino de matemática analítica nas universidades.",
        "Porque Platão defendia que as eleições cívicas deveriam ser realizadas mediante consultas a adivinhos tradicionais.",
        "Porque os filósofos da Academia eram obrigados a prestar juramentos de obediência a imperadores persas.",
        "B",
        "O totalitário moderno busca o culto à sua própria pessoa e o poder pelo poder; o filósofo de Platão não quer governar para si, sacrificando sua paz contemplativa para servir à justiça da cidade."
    ))

    questoes_brutas.append((
        37, "EM13CHS501", "intermediario",
        "Ao examinar a tripartição da alma em Platão e a divisão social em Kallipolis, qual consequência política desastrosa ocorre caso a classe dos 'Produtores' tome o controle do governo da cidade?",
        "As colheitas de trigo nas fazendas aumentam em volume além do consumo médio da população.",
        "A cidade é corrompida pela cupidez, pelo apego egoísta à riqueza material e pelo mercantilismo desmedido, transformando as leis e as instituições públicas em balcões de negócios privados e acelerando a decadência da pólis.",
        "Os tecelões e alfaiates passam a confeccionar uniformes militares com tecidos de seda importada.",
        "As muralhas de pedra da capital são pintadas com cores escuras para refletir o calor do sol no verão.",
        "Os livros de filosofia clássica são impressos em grandes formatos tipográficos por gráficas sindicais.",
        "B",
        "A alma concupiscível busca o ganho e o apetite material: se artífices governam, a pólis vira oligarquia de dinheiro; para Platão, apenas a razão desinteressada tem pureza para governar com justiça."
    ))

    questoes_brutas.append((
        38, "EM13CHS603", "intermediario",
        "Na análise de Moses I. Finley em Democracia Antiga e Moderna, qual é o contraste marcante entre o modelo democrático ateniense e as democracias representativas liberais contemporâneas?",
        "A democracia ateniense utilizava urnas eletrônicas de votação com leitura de impressões digitais.",
        "A democracia ateniense era direta e participativa (os próprios cidadãos reuniam-se na assembleia para debater e votar as leis pessoalmente), enquanto as democracias modernas são indiretas e representativas (os cidadãos elegem deputados e senadores para legislarem em seu nome).",
        "A democracia moderna proíbe a liberdade de expressão de pensamentos em meios de comunicação social.",
        "A democracia antiga exigia que os eleitores fossem graduados em faculdades de direito civil e penal.",
        "A democracia representativa contemporânea proíbe o voto de mulheres e trabalhadores assalariados.",
        "B",
        "O ateniense não terceirizava o poder: ele subia na tribuna da Ekklesia e votava a paz ou a guerra com a própria mão erguida; o cidadão moderno elege representantes para exercerem o mandato em seu lugar."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "O que afirma Aristóteles sobre os indivíduos que afirmam não necessitar da vida na Pólis?",
        "Que eles devem receber títulos nobiliárquicos e propriedades agrícolas nas regiões litorâneas.",
        "Que o ser humano que é incapaz de viver em sociedade ou que não necessita dela por ser autossuficiente não é um homem pleno: ou é uma besta degradada (inferior ao humano) ou é um deus (superior ao humano).",
        "Que eles possuem conhecimentos astronômicos avançados sobre as constelações do hemisfério norte.",
        "Que eles devem trabalhar voluntariamente na manutenção de canais de irrigação de lavouras rurais.",
        "Que eles são os cidadãos mais preparados para exercerem funções de magistrados em tribunais superiores.",
        "B",
        "A humanidade é constitutivamente social: o homem solitário que despreza a pólis mutila sua própria natureza; a dignidade, a fala e a ética só existem em relação com os outros cidadãos."
    ))

    questoes_brutas.append((
        40, "EM13CHS502", "intermediario",
        "Como a reflexão de Francis Wolff em Aristóteles e a Política articula a relação indissociável entre a Ética individual e a Filosofia Política?",
        "Afirmando que a moralidade particular não tem nenhuma relação com as leis e a administração cívica da cidade.",
        "Demonstrando que a ética (que investiga o bem e a felicidade do indivíduo) é apenas a primeira parte da política (que investiga as condições comunitárias e institucionais que tornam essa vida virtuosa possível para todos os cidadãos).",
        "Sustentando que a política deve ser orientada exclusivamente pelo cálculo financeiro de receitas públicas do tesouro.",
        "Defendendo que os filósofos devem abandonar o estudo da lógica para dedicarem-se à carpintaria naval.",
        "Provando que as leis cívicas têm maior eficácia quando redigidas em verso métrico de peças teatrais.",
        "B",
        "Para Aristóteles, Ética e Política são faces da mesma moeda: a ética ensina como o indivíduo floresce na virtude; a política constrói a pólis justa que permite a todos alcançarem esse florescimento."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a famosa passagem do Livro I de A Política de Aristóteles: 'A razão pela qual o homem é um animal político em grau mais elevado que qualquer abelha ou animal gregário é clara: a natureza nada faz em vão, e só o homem, entre todos os animais, é dotado da fala (logos).' De que maneira essa articulação entre a linguagem deliberativa e a sociabilidade humana desmonta a concepção individualista moderna de sociedade?",
        "Provando que os mercadores marítimos da Grécia antiga utilizavam moedas de bronze com inscrições em relevo.",
        "Evidenciando que a sociedade não é um arranjo mecânico ou um contrato artificial firmado a posteriori por indivíduos atômicos isolados em estado de natureza, mas a realização inevitável da própria essência comunicativa e moral do ser humano, cuja faculdade de discernir o justo e o injusto só pode nascer e desabrochar na convivência pública da pólis.",
        "Afirmando que os animais gregários da savana africana comunicam-se através de sinais luminosos de alta intensidade.",
        "Demonstrando que as assembleias democráticas de Atenas deveriam suspender os debates em períodos de seca prolongada.",
        "Sustentando que as leis processuais de tribunais cíveis foram copiadas integralmente de manuais militares persas.",
        "B",
        "**Etapa 1:** Compreender a tese aristotélica da sociabilidade natural: a linguagem (logos) não serve apenas para pedir comida, mas para deliberar sobre o bem e o justo.\n**Etapa 2:** Contrastar com o individualismo moderno: para os contratualistas o homem nasce isolado e cria o Estado por medo; para Aristóteles o homem é político por nascimento, e fora da pólis sua humanidade é incompleta e mutilada."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em A República (Livro VII), Platão articula a célebre 'Alegoria da Caverna' com o dever político do filósofo: após libertar-se das correntes, subir a encosta escarpada e contemplar a luz do Sol (a Ideia do Bem Supremo), o sábio não pode permanecer na beatitude contemplativa solitária; ele tem a obrigação moral intransponível de retornar à escuridão da caverna para educar e governar seus antigos companheiros aprisionados. Como esse movimento de retorno fundamenta o estatuto ético da Sofocracia?",
        "Fazendo com que os alunos da Academia de Atenas praticassem exercícios físicos de marcha militar em praças públicas.",
        "Demonstrando que a sabedoria autêntica não é um privilégio individual para fruição egoísta, mas um compromisso ético de serviço público em prol da justiça da cidade; o filósofo governa não por ambição de poder, honrarias ou riquezas, mas como um estrito dever de sacrifício pessoal imposto pela razão para livrar seus concidadãos das sombras da ignorância e da demagogia.",
        "Obrigando os comerciantes de cereais a venderem produtos agrícolas exclusivamente pelo preço de custo de produção.",
        "Provando que as academias científicas da cidade de Alexandria foram financiadas com moedas de ouro do tesouro real.",
        "Determinando que os juízes de tribunais constitucionais devam usar togas confeccionadas com tecidos de lã de cabra.",
        "B",
        "**Etapa 1:** Analisar o duplo movimento do filósofo platônico: a ascensão dialética para contemplar a Verdade e o doloroso retorno à caverna.\n**Etapa 2:** Concluir com a fundamentação da sofocracia: governar é um dever moral desinteressado; aquele que ama o poder por vaidade ou lucro é o pior governante; quem governa bem é o sábio que despreza os privilégios do poder e governa para iluminar a cidade."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Considere a classificação aristotélica das formas degeneradas de governo, em especial a 'Oligarquia' (governo dos ricos em proveito de sua própria classe) versus a 'Democracia Demagógica' (governo da massa pobre desprovida de formação que busca despojar os proprietários). De que maneira o filósofo demonstra que ambos os regimes são instáveis e injustos por errarem na compreensão do conceito de Igualdade?",
        "Mostrando que as frotas de navios de guerra da Liga de Delos consumiam excesso de madeira nos estaleiros navais.",
        "Evidenciando que os oligarcas cometem o erro de achar que, por serem desiguais na riqueza econômica, devem ser desiguais em tudo (monopolizando todo o poder político), enquanto os democratas demagógicos cometem o erro simétrico de achar que, por serem iguais na liberdade cívica de nascença, devem ser absolutamente iguais em tudo (confiscando bens e silenciando o mérito); a verdadeira justiça distributiva exige tratar desigualmente os desiguais segundo a virtude em prol do bem comum.",
        "Afirmando que os cidadãos que trabalhavam em olarias de cerâmica eram obrigados a pagar tributos aduaneiros no porto.",
        "Provando que as constituições republicanas deixam de ter vigência jurídica quando ocorrem períodos de peste na capital.",
        "Determinando que as assembleias cívicas devem realizar votações secretas utilizando pedras de calcário branco e preto.",
        "B",
        "**Etapa 1:** Mapear o erro simétrico de oligarcas e democratas radicais: confundir desigualdade econômica com superioridade total, ou liberdade básica com igualitarismo aritmético forçado.\n**Etapa 2:** Concluir com a teoria aristotélica da justiça proporcional: a pólis só atinge a estabilidade quando supera a guerra de facções através da Politeia, onde a lei e a classe média equilibram o conflito em prol do florescimento de todos."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Ao examinar a tese aristotélica da 'Escravidão por Natureza' formulada no Livro I de A Política — na qual o filósofo sustenta que certos seres humanos seriam naturalmente desprovidos de capacidade deliberativa plena e, por isso, destinados a serem governados por outros —, como a crítica contemporânea da Filosofia do Direito desvela o viés ideológico de classe e etnocêntrico dessa proposição?",
        "Negando que os remadores de galés de guerra soubessem calcular a velocidade de deslocamento náutico em alto-mar.",
        "Demonstrando que Aristóteles cometeu o erro de naturalizar uma opressão social e histórica contingente da Grécia clássica: para justificar racionalmente a estrutura escravocrata que sustentava o ócio dos cidadãos proprietários, o filósofo atribuiu à ordem cósmica da natureza aquilo que era, na verdade, uma violência política e econômica imposta pela força das armas e pelas dívidas.",
        "Afirmando que os escravizados que trabalhavam em minas de prata recebiam remunerações diárias calculadas em dracmas.",
        "Provando que os tratados de comércio de tecidos foram redigidos por magistrados de cidades fundadas na Ásia Menor.",
        "Defendendo que as leis cívicas de Atenas proibiam a compra e venda de ferramentas de ferro forjado em feiras livres.",
        "B",
        "**Etapa 1:** Desconstruir a falácia da naturalização da desigualdade social: transformar a dominação militar e econômica em uma 'lei biológica' da natureza humana.\n**Etapa 2:** Concluir com a lucidez da crítica contemporânea: a teoria da escravidão por natureza é o exemplo clássico de como a ideologia de uma classe dominante pode cegar até os maiores gênios filosóficos; a dignidade humana universal e inalienável não tolera a divisão entre senhores naturais e servos."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Em Democracia Antiga e Moderna, o historiador Moses I. Finley analisa o julgamento que condenou Sócrates e adverte que a democracia ateniense não conhecia o conceito moderno de 'Direitos Fundamentais Individuais Inalienáveis contra a Tirania da Maioria'. Como a ausência de garantias constitucionais de direitos de minorias explica a vulnerabilidade da democracia clássica diante do arbítrio popular?",
        "Porque os cidadãos atenienses utilizavam pergaminhos de couro animal que se degradavam com a umidade do mar.",
        "Porque, no modelo grego antigo, a liberdade consistia exclusivamente na participação política coletiva na assembleia soberana (a soberania popular sem limites), não existindo a noção de uma esfera privada de direitos subjetivos protegida contra as decisões da maioria; se 51% dos cidadãos votassem pela execução ou banimento de um indivíduo por suas ideias heterodoxas, não havia tribunal constitucional que pudesse frear a vontade soberana da massa.",
        "Porque as forças militares das cidades-Estado gregas eram comandadas por generais eleitos por sorteios anuais.",
        "Provando que as constituições antigas exigiam que todas as leis cívicas fossem aprovadas com unanimidade absoluta de votos.",
        "Determinando que os julgamentos de conflitos de terra deveriam ser suspensos durante os festivais do deus Dioniso.",
        "B",
        "**Etapa 1:** Distinguir a liberdade dos antigos da liberdade dos modernos (Benjamin Constant e Finley): liberdade antiga era soberania coletiva na ágora; liberdade moderna inclui o escudo de direitos individuais contra o Estado e a maioria.\n**Etapa 2:** Concluir com a tragédia de Sócrates: como a assembleia era soberana absoluta sem freios de direitos humanos, a maioria pôde condenar um homem inocente por suas ideias; a democracia contemporânea aprendeu com esse erro, erguendo constituições rígidas que protegem a liberdade de expressão de minorias."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "No Livro VIII de A República, Platão desenvolve sua célebre teoria do ciclo de degeneração sucessiva dos regimes políticos: da Cidade Perfeita (Sofocracia / Aristocracia) passa-se à Timocracia (governo da ambição militar e honra), desta à Oligarquia (governo da ganância e riqueza dos plutocratas), em seguida à Democracia (anarquia e licenciosidade da massa) e, por fim, à Tirania (o despotismo do tirano). Qual é a dinâmica psicológica e moral interna que impulsiona essa decadência contínua?",
        "O esgotamento das jazidas de mármore e minério de cobre nas pedreiras rurais da Península Balcânica.",
        "A perda progressiva da virtude e da harmonia funcional da alma: cada etapa da decadência ocorre quando uma instância inferior da alma assume o comando da pólis; quando a coragem substitui a sabedoria surge a timocracia; quando a ganância de ouro assume o poder nasce a oligarquia; quando os apetites desregrados se rebelam surge a anarquia democrática; e quando o medo e o apetite tirânico triunfam, a cidade desmorona na escravidão total.",
        "O aumento constante dos tributos alfandegários cobrados sobre a importação de especiarias do Oriente Médio.",
        "A determinação de que os cidadãos adultos devam prestar três anos de serviços obrigatórios na vigilância de portos.",
        "A substituição das armas de ferro fundido por arcos e flechas de madeira em combates corpo a corpo.",
        "B",
        "**Etapa 1:** Mapear o isomorfismo platônico alma-cidade: a política reflete a saúde ou a patologia da psique humana.\n**Etapa 2:** Evidenciar o motor da degeneração: à medida que a razão perde o comando para as paixões e para a cobiça material, os regimes descem a ladeira da corrupção; da honra militar ao dinheiro, do dinheiro ao capricho populista, até o colapso no abismo da tirania."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Considere o contraste entre a concepção platônica de Política — entendida como uma ciência do Bem absoluto (*Episteme*) que deve ser imposta à cidade pelos sábios — e a concepção aristotélica de Política — compreendida como uma sabedoria prática (*Phronesis*) que lida com a contingência, a deliberação e a prudência empírica. Quais são as implicações desse abismo metodológico para a teoria da democracia?",
        "Platão defendia a abolição dos tribunais penais, enquanto Aristóteles exigia o aumento de prisões nas ilhas.",
        "Enquanto a perspectiva platônica desqualifica estruturalmente a democracia ao encará-la como o império da opinião ignorante (doxa) que recusa a verdade ideal dos peritos, a perspectiva aristotélica abre espaço para a deliberação plural dos cidadãos, reconhecendo que a sabedoria coletiva reunida na assembleia, mediada pela lei e pela experiência da moderação, pode produzir decisões mais prudentes e estáveis do que o governo solitário de um indivíduo isolado.",
        "Platão afirmava que os marinheiros de frotas mercantes deveriam ser os únicos juízes em audiências comerciais.",
        "Aristóteles sustentava que as cidades rurais deveriam fechar seus mercados municipais durante o período de colheita de cevada.",
        "Ambos os filósofos concordavam que os governantes deveriam ser escolhidos por meio de sorteios cegos com pedras polidas.",
        "B",
        "**Etapa 1:** Contrastar a Episteme platônica (verdade matemática e absoluta que poucos alcançam) com a Phronesis aristotélica (prudência ética que se forja no debate e na convivência cotidiana).\n**Etapa 2:** Concluir com a avaliação da democracia: Platão é antidemocrático por princípio (apenas o filósofo sabe); Aristóteles, embora crítico da demagogia, valoriza a soma das opiniões cidadãs na Politeia (vários cidadãos reunidos podem julgar melhor do que um só especialista isolado)."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Ao examinar a relação entre Cidadania e Riqueza no Brasil contemporâneo, cientistas políticos apontam que a sobrerrepresentação de grandes conglomerados econômicos e bancários no financiamento de campanhas eleitorais e na pressão sobre o Congresso Nacional configura uma 'captura oligárquica da democracia'. De que maneira a análise aristotélica sobre a Oligarquia ilumina criticamente esse dilema da democracia representativa moderna?",
        "Mostrando que os operários das indústrias químicas consomem muita energia elétrica nas linhas de montagem fabril.",
        "Evidenciando que, sob a aparência formal de uma democracia constitucional de voto universal (um cidadão, um voto), o poder real do capital financeiro converte as instituições públicas em instrumentos a serviço dos interesses de uma minoria abastada que financia a política, atualizando a denúncia de Aristóteles de que a oligarquia é a patologia em que os governantes utilizam as leis para defender privilégios e enriquecer sua própria classe à custa da maioria.",
        "Provando que as patentes de fertilizantes agrícolas devem ser aprovadas por comitês de embaixadores estrangeiros.",
        "Determinando que os cidadãos que possuem veículos automotores particulares devem pagar pedágios nas rodovias estaduais.",
        "Sustentando que os tratados de comércio de carnes bovinas perdem a validade em períodos de estiagem nas pastagens.",
        "B",
        "**Etapa 1:** Analisar a definição aristotélica de oligarquia: não é apenas o governo de poucos, mas o governo dos ricos em proveito de sua riqueza.\n**Etapa 2:** Conectar com a crise democrática contemporânea: quando o poder econômico compra bancadas parlamentares e dita a política fiscal, a democracia vira mera fachada para a dominação oligárquica; a lição de Aristóteles nos convoca a regular o poder do dinheiro para resgatar a busca pelo bem comum."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Em A Política, Aristóteles formula a famosa analogia orgânica da anterioridade da Pólis: 'A cidade é por natureza anterior à família e a cada um de nós individualmente; pois o todo deve necessariamente preceder a parte. Se o corpo todo for destruído, não haverá pé nem mão, a não ser por equívoco de linguagem, como se falássemos de uma mão de pedra.' Qual é a implicação dessa tese para a superação do solipsismo ético?",
        "A determinação de que os hospitais militares devam tratar com prioridade os soldados que sofreram fraturas corporais.",
        "A demonstração de que a identidade humana e o agir moral não são propriedades auto-suficientes que o indivíduo carrega isoladamente como uma posse privada em um vácuo, mas funções relacionais que só adquirem vitalidade, sentido e eficácia no interior do corpo orgânico da comunidade política viva que o acolhe, o educa e lhe oferece a linguagem da justiça.",
        "A exigência de que os proprietários agrícolas entreguem metade de suas ferramentas de arado aos cofres da prefeitura.",
        "A comprovação de que as muralhas de pedra das cidades gregas resistiam com maior eficácia a ataques de catapultas.",
        "A regra de que os generais das forças de infantaria devam realizar exercícios matinais de corrida em praias litorâneas.",
        "B",
        "**Etapa 1:** Interpretar a analogia orgânica aristotélica: a mão só é mão viva porque está ligada ao corpo que a nutre e lhe dá função.\n**Etapa 2:** Concluir com a superação do solipsismo: o indivíduo isolado que pensa poder ser ético ou livre sem a comunidade é uma ilusão; nós somos seres relacionais e interdependentes; a saúde moral de cada um depende da saúde e da justiça da pólis que compartilhamos."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "No debate sobre a 'Desigualdade Salarial e Tributária' na América Latina, como a tese aristotélica sobre a 'Classe Média' e a 'Politeia' oferece subsídios para defender políticas públicas de progressividade de impostos e redistribuição de renda em estados democráticos contemporâneos?",
        "Defendendo que os comerciantes de cereais sejam isentos do pagamento de taxas sobre a circulação de mercadorias no porto.",
        "Demonstrando que a concentração obscena de renda em uma elite diminuta e a proliferação da miséria geram a destruição da amizade cívica e a instabilidade institucional permanente; a tributação progressiva sobre os super-ricos e os investimentos em saúde, educação e trabalho emancipatório expandem e fortalecem uma ampla classe média cidadã, recriando o equilíbrio sociopolítico moderado que viabiliza a paz republicana.",
        "Afirmando que as famílias que residem em cidades industriais devem construir habitações com telhados de cerâmica vermelha.",
        "Determinando que os bancos comerciais devam encerrar suas operações de crédito financeiro durante as sextas-feiras festivas.",
        "Provando que as estradas de ferro consomem dormentes de madeira que deveriam ser preservados em florestas ecológicas.",
        "B",
        "**Etapa 1:** Compreender o perigo político da polarização social diagnosticado em A Política: uma sociedade dividida entre plutocratas arrogantes e miseráveis revoltados não sustenta a democracia.\n**Etapa 2:** Concluir com a lição para as políticas públicas: tributar o topo e fortalecer a base constrói a classe média que ancora a estabilidade institucional; a justiça tributária redistributiva é o mecanismo contemporâneo para erguer a Politeia e afastar o fantasma da guerra civil e da tirania."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Ao examinar a relação entre a 'Alegoria da Caverna' e a teoria da 'Opinião' (Doxa) versus 'Ciência' (Episteme), por que Platão sustenta que os cidadãos comuns da democracia ateniense viviam acorrentados na ilusão das sombras?",
        "Porque as assembleias cívicas de Atenas realizavam suas sessões em anfiteatros subterrâneos sem janelas de ventilação.",
        "Porque os cidadãos atenienses pautavam seus julgamentos morais e políticos nas aparências sensíveis imediatas, nas tradições poéticas mitológicas acríticas e nos discursos sedutores de sofistas e demagogos, tomando as sombras passageiras da opinião pública como se fossem a realidade objetiva, permanecendo cegos para a Verdade inteligível e imutável do Bem.",
        "Porque os trabalhadores das oficinas de carpintaria desconheciam as regras de navegação astronômica em mares abertos.",
        "Porque os governantes das cidades gregas proibiam a circulação de livros didáticos encadernados em couro animal.",
        "Porque os generais militares utilizavam tochas acesas com óleo de peixe para iluminar as fortificações noturnas.",
        "B",
        "**Etapa 1:** Desvelar o significado teórico, conceitual e político da caverna: as sombras são as opiniões manipuladas (doxa) pelos demagogos e sofistas da assembleia.\n**Etapa 2:** Concluir com a denúncia de Platão: a democracia é o teatro das sombras; o cidadão que vota levado pela oratória apaixonada é um prisioneiro da ilusão; a libertação exige a conversão dolorosa da alma da doxa para a luz da Episteme (ciência verdadeira)."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Considere a crítica de Aristóteles em A Política (Livro II) ao projeto platônico de Kallipolis, em especial à abolição da família e à propriedade comum absoluta: 'O que é comum a um número muito grande de pessoas é precisamente o que recebe menos cuidados; pois todos se preocupam mais com o que lhes é próprio do que com o que possuem em comum.' De que maneira essa crítica aristotélica estabelece os alicerces do realismo político contra o idealismo utópico?",
        "Provando que as caldeiras a vapor utilizadas nas tecelagens britânicas consumiam muita água de poços artesianos.",
        "Evidenciando que a tentativa platônica de suprimir a individualidade e os afetos humanos naturais (como o apego à própria família e aos bens pessoais) para forjar uma unidade artificial absoluta desconhece a psicologia real da espécie humana; o bem comum autêntico não se constrói destruindo as esferas particulares, mas articulando a pluralidade harmoniosa de cidadãos que cuidam zelosamente de seus lares e estendem esse zelo à cidade através da virtude compartilhada.",
        "Afirmando que os médicos veterinários da Antiguidade desconheciam as técnicas de tratamento de infecções na pele de cavalos.",
        "Determinando que os juízes criminais devam emitir sentenças lavradas em folhas de pergaminho vegetal autenticado.",
        "Sustentando que os soldados de infantaria leve devam utilizar lanças confeccionadas com hastes de madeira de carvalho.",
        "B",
        "**Etapa 1:** Analisar o argumento da 'tragédia dos comuns' antecipado por Aristóteles: quem é pai de todos acaba não sendo pai afetuoso de ninguém; a propriedade de todos vira a negligência de todos.\n**Etapa 2:** Concluir com o realismo de Aristóteles: a pólis é pluralidade por essência; unificar a cidade como uma única família homogênea destrói a própria política; a sabedoria reside em harmonizar as diferenças e cultivar o afeto particular que transborda em compromisso cívico."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "No debate clássico sobre a 'Origem da Lei' na Grécia, qual era o embate filosófico fundamental entre os Sofistas (que defendiam que a lei é mera convenção humana contingente e instrumento do mais forte — Physis versus Nomos) e Platão (que defendia que a lei deve refletir a ordem inteligível da Justiça eterna)?",
        "A controvérsia sobre se os navios mercantes deveriam navegar utilizando velas confeccionadas com tecido de linho ou algodão.",
        "O embate entre o relativismo moral dos sofistas (como Trasímaco, que declarava que 'a justiça é apenas a conveniência do mais forte') e o idealismo metafísico de Platão, que combateu vigorosamente esse cinismo político demonstrando que a verdadeira justiça não é um pacto de conveniência de tiranos, mas uma ordem cósmica objetiva que dignifica a alma e funda a saúde imutável da cidade.",
        "A disputa sobre a quantidade de azeitonas que os agricultores familiares deveriam entregar às feiras municipais em anos de seca.",
        "A decisão sobre se as apresentações de teatro trágico deveriam ser realizadas antes ou depois do pôr do sol na primavera.",
        "O regulamento cívico sobre a obrigatoriedade de os soldados de infantaria usarem botas de couro durante marchas matinais.",
        "B",
        "**Etapa 1:** Descrever a tese sofística do poder cru (Trasímaco no Livro I de A República): a justiça é a força do opressor travestida de lei.\n**Etapa 2:** Concluir com a refutação platônica: se a justiça fosse apenas a conveniência do forte, a tirania seria virtuosa e o crime seria a regra; Platão demonstra que o injusto destrói sua própria alma com o caos interno; a verdadeira lei é reflexo do Bem e da harmonia cósmica."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "De que modo a categoria da 'Isegoria' (o direito igual à palavra pública) na Atenas clássica desafiava a hierarquia tradicional aristocrática baseada na linhagem de nobreza de sangue (*Eupátridas*)?",
        "Exigindo que os generais militares fossem escolhidos exclusivamente entre os poetas que venciam festivais de tragédia.",
        "Rompendo o monopólio da oratória e do poder político tradicionalmente concentrado nas grandes famílias de linhagem nobre, assegurando que um artesão humilde, um sapateiro ou um pequeno agricultor livre pudesse subir na mesma tribuna da Ekklesia para discursar, contestar nobres e influenciar diretamente a aprovação das leis da cidade.",
        "Determinando que os nobres de linhagem deveriam doar suas terras para a construção de praças públicas de jogos.",
        "Proibindo os comerciantes de cereais de assistirem às sessões plenárias da assembleia popular durante os dias úteis.",
        "Obrigando os cidadãos atenienses a assinarem termos de fidelidade política perante comissões de sacerdotes de Apolo.",
        "B",
        "**Etapa 1:** Compreender a revolução democrática ateniense: antes, apenas o sangue azul do nobre falava com autoridade nos conselhos arcaicos.\n**Etapa 2:** Evidenciar o impacto da isegoria: na assembleia popular, o logos substitui o brasão; o que importa é a força do argumento persuasivo perante a comunidade de iguais, consagrando a dignidade cívica de qualquer cidadão livre trabalhador."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Em A Política, Aristóteles sentencia: 'Quem manda na pólis deve ser a Lei, e não os homens; pois a lei é a Razão desprovida de paixão (logos aneu orexeos).' Como essa formulação clássica funda o princípio moderno do 'Estado Democrático de Direito' (Rule of Law)?",
        "Afirmando que os magistrados de tribunais civis devem ser substituídos por estátuas de mármore esculpidas com balanças.",
        "Estabelecendo a supremacia das normas jurídicas gerais, abstratas e impessoais sobre os caprichos arbitrários, vaidades e paixões cegas de governantes individuais, assegurando que o governante seja apenas o servo da lei e que nenhum cidadão fique à mercê da tirania de outro ser humano.",
        "Determinando que os códigos de leis escritas sejam guardados em cofres de ferro fundido nas sedes de consulados marítimos.",
        "Exigindo que as leis penais sejam cantadas em versos métricos de tragédia por arautos públicos em dias de mercado.",
        "Provando que as assembleias cívicas devem cancelar suas reuniões caso ocorram tempestades com raios no interior.",
        "B",
        "**Etapa 1:** Analisar o perigo do governo puramente dos homens: o governante humano, por melhor que seja, é sujeito à cólera, ao favoritismo e à corrupção da vaidade.\n**Etapa 2:** Concluir com a fundação do império da lei (Rule of Law): a lei escrita é a inteligência depurada do vício das paixões particulares; governar sob a lei é a única garantia contra a tirania e a base de todo o constitucionalismo democrático contemporâneo."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Analise a relação entre a 'Crítica de Platão à Democracia' e a 'Alegoria da Nau do Estado': se a política é uma arte e uma ciência rigorosa (*Techne* e *Episteme*) que exige conhecimento profundo dos ventos, das estrelas e da justiça, qual é a contradição insolúvel que Platão aponta no procedimento do Sorteio e do Sufrágio Popular majoritário?",
        "A de que os cidadãos que votavam na assembleia não sabiam manusear bússolas magnéticas de precisão astronômica.",
        "A de que em nenhuma outra atividade técnica essencial (como a medicina, a navegação ou a arquitetura) a sociedade comete o disparate de escolher o cirurgião, o navegador ou o arquiteto por sorteio cego ou por votação da maioria leiga desinformada; apenas na política — a atividade mais vital de todas — a democracia comete a leviandade de entregar o destino da coletividade ao concurso de popularidade entre demagogos que nada entendem da Verdade.",
        "A de que os comandantes de navios de guerra deveriam ser nomeados exclusivamente por reis de dinastias egípcias antigas.",
        "A de que as eleições cívicas consumiam muito carvão vegetal para iluminar os anfiteatros durante a contagem de votos.",
        "A de que os magistrados da cidade deveriam ser proibidos de realizar viagens marítimas para ilhas do mar Egeu.",
        "B",
        "**Etapa 1:** Desvelar a analogia técnica de Platão: ninguém contrata um médico ou piloto de navio perguntando a uma multidão na praça quem fala mais bonito.\n**Etapa 2:** Concluir com a demolição platônica do voto popular leigo: a democracia confunde a liberdade de opinar com a competência de governar; entregar a nau a quem não sabe navegar é suicídio coletivo; por isso, para Platão, o comando deve pertencer ao saber rigoroso da filosofia."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Em A Política, Aristóteles adverte contra os perigos da 'Estase' (a guerra civil e a sedição interna nas cidades). Qual é, segundo o filósofo, a causa psicológica e moral mais profunda das revoltas populares contra as ordens estabelecidas?",
        "A escassez temporária de peixes frescos nas bancas de venda do porto litorâneo da cidade.",
        "O sentimento dilacerante de injustiça gerado pela quebra da equidade distributiva: a revolta explode quando homens que se julgam iguais em dignidade e liberdade são tratados desigualmente pelos governantes oligarcas, ou quando homens que possuem méritos e virtudes superiores são nivelados artificialmente à mediocridade geral por maiorias invejosas.",
        "A exigência de que os proprietários rurais pintassem suas residências familiares com cal branca pura.",
        "A decisão de as assembleias deliberativas aprovarem a substituição de instrumentos musicais tradicionais.",
        "A recusa de mercadores estrangeiros em aceitarem o pagamento de tarifas alfandegárias em moedas de cobre.",
        "B",
        "**Etapa 1:** Diagnosticar a gênese da revolta: a revolução não nasce da fome pura, mas do sentimento moral de que a partilha foi injusta e humilhante.\n**Etapa 2:** Concluir com a lição de estabilidade: a paz social exige proporcionalidade ética; quando a oligarquia humilha o cidadão livre ou o igualitarismo cego castiga a excelência, o veneno da estase rompe o tecido social; a justiça distributiva equitativa é o antídoto supremo contra a guerra civil."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "De que modo a experiência política da Atenas do Século de Péricles influenciou a formulação do conceito contemporâneo de 'Cidadania Ativa' e 'Participação Democrática Deliberativa'?",
        "Obrigando os eleitores contemporâneos a prestarem juramentos militares de vassalagem a autoridades eleitas.",
        "Demonstrando que a cidadania não se resume ao ato passivo e esporádico de comparecer às urnas a cada quatro anos para delegar o poder a representantes, exigindo o envolvimento cotidiano, direto e corresponsável do cidadão na vida pública, na fiscalização dos governantes e na deliberação coletiva sobre o destino comum da comunidade política.",
        "Provando que os parlamentos nacionais devem transferir suas sedes legislativas para cidades litorâneas turísticas.",
        "Exigindo que os candidatos a cargos eletivos apresentem certificados de proficiência em retórica clássica antiga.",
        "Determinando que as assembleias municipais devam ser transmitidas exclusivamente em canais de rádio comunitária.",
        "B",
        "**Etapa 1:** Desmistificar a cidadania passiva do consumidor moderno: votar a cada biênio e desinteressar-se do bem público pelo restante do tempo.\n**Etapa 2:** Resgatar a potência de Atenas: para o grego antigo, o cidadão que não se interessa pelos negócios públicos era um idiota (idiotes — aquele que só cuida do próprio ego privado); a cidadania ativa exige presença, deliberação e paixão pelo destino comum da república."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Considere a abertura do Eixo III (Filosofia Política, Poder, Resistência e Necropolítica): ao examinar as matrizes clássicas de Platão e Aristóteles, quais tensões fundantes inauguradas na Grécia antiga continuarão a estruturar os debates políticos modernos e contemporâneos (como o realismo de Maquiavel, o contratualismo, Foucault e Mbembe)?",
        "A preocupação de engenheiros com a velocidade de transporte de vagões em estradas de ferro industriais.",
        "As tensões permanentes e universais entre a busca ética pelo Bem Comum e a disputa crua pelo Poder; entre a competência técnica/saber (sofocracia/tecnocracia) e a soberania popular democrática; entre o império da Lei impessoal e o arbítrio de governantes; e a contradição entre a promessa de igualdade dos cidadãos e a exclusão estrutural violenta de corpos subordinados (mulheres, escravizados e periferias).",
        "A disputa entre fábricas têxteis sobre a utilização de tecidos de linho importado em fardamentos militares.",
        "A determinação de que os tratados de comércio internacional devam prever cláusulas sobre cultivo de uvas viníferas.",
        "A controvérsia sobre se as cidades capitais devem ser construídas em planícies aluviais ou em topos de montanhas.",
        "B",
        "**Etapa 1:** Mapear o arco reflexivo da Filosofia Política: as categorias fundadas por Platão e Aristóteles são as ferramentas constitutivas de todo o vocabulário político ocidental.\n**Etapa 2:** Concluir com a síntese do Eixo III: ao descer da pólis grega para Maquiavel, Hobbes, Rousseau, Marx, Foucault e a necropolítica de Mbembe, veremos essas mesmíssimas tensões se radicalizarem: quem manda, por que manda, sob quais exclusões o poder opera e como a resistência humana reinventa a liberdade."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "Síntese conclusiva: por que o estudo comparado do pensamento político de Platão e Aristóteles no Ensino Médio é uma ferramenta indispensável para a formação de uma juventude crítica, consciente e emancipada no século XXI?",
        "Porque ele simplifica os exames vestibulares ao exigir apenas a memorização das datas de guerras da Grécia arcaica.",
        "Porque ele instrumentaliza os estudantes com categorias clássicas rigorosas para discernirem com lucidez entre discursos demagógicos populistas e propostas fundamentadas no bem comum, capacitá-los a desconstruir as ilusões do tecnicismo autoritário e compreenderem que a democracia exige tanto a vigilância intransigente do império da lei e da equidade socioeconômica quanto a participação ativa e ética na construção de uma sociedade justa e livre.",
        "Porque ele estabelece a obrigatoriedade de que todos os concluintes do ensino médio aprendam a traduzir textos em grego clássico.",
        "Porque ele comprova que os tratados de diplomacia internacional deixam de ter validade quando ocorrem eclipses lunares.",
        "Porque ele determina que as escolas de ensino médio devam substituir o estudo de sociologia por treinamentos de luta corporal.",
        "B",
        "**Etapa 1:** Compreender a função pedagógica dos clássicos políticos: eles nos oferecem o espelho onde enxergamos as patologias de nossa própria política contemporânea.\n**Etapa 2:** Concluir com a emancipação cidadã: o jovem educado por Platão e Aristóteles não se deixa enganar por falsos salvadores da pátria nem aceita a desigualdade como destino fatal; ele sabe que a política é a arte sublime de cuidar da comunidade e fazer florescer a dignidade humana na história."
    ))

    return questoes_brutas

def main():
    questoes = gerar_lista()
    total = len(questoes)
    print(f"Total de questões brutas: {total}")
    assert total == 60, f"Erro: esperava 60 questões, obteve {total}"

    # Blacklist estrita do validador_educamob.py
    blacklist = [
        "epistemológic", "ontológic", "teleológic", "dicotomi", "intrínsec", "extrínsec",
        "subjacente", "efêmer", "prerrogativa", "prescind", "imprescind", "corrobor",
        "hegemônic", "mitigar", "fomentar", "propedêutic", "inexor", "axiológic",
        "hermenêutic", "mormente", "R$"
    ]

    erros_blacklist = []
    for q in questoes:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        texto_completo = f"{enunc} {a} {b} {c} {d} {e_alt} {resol}".lower()
        for b_word in blacklist:
            if b_word.lower() in texto_completo:
                erros_blacklist.append((num, b_word))

    if erros_blacklist:
        print("\n[ERRO NA AUDITORIA DE TERMOS PROIBIDOS]:")
        for num, w in erros_blacklist:
            print(f" - Questão {num}: termo proibido '{w}' encontrado!")
        sys.exit(1)
    else:
        print("[AUDITORIA INTERNA APROVADA] Nenhuma palavra da blacklist pedagógica encontrada!")

    # Rotação balanceada do gabarito: exatamente 12 A, 12 B, 12 C, 12 D, 12 E
    gabarito_ciclo = ["A", "B", "C", "D", "E"] * 12
    assert len(gabarito_ciclo) == 60

    questoes_rotacionadas = []
    for idx, q in enumerate(questoes):
        num, hab, dif, enunc, a, b, c, d, e_alt, gab_original, resol = q
        alvo = gabarito_ciclo[idx]
        alternativas = {"A": a, "B": b, "C": c, "D": d, "E": e_alt}
        texto_correto = alternativas[gab_original]

        outras = [k for k in ["A", "B", "C", "D", "E"] if k != gab_original]
        textos_distratores = [alternativas[k] for k in outras]

        novas_alts = {}
        novas_alts[alvo] = texto_correto
        pos_dist = 0
        for letra in ["A", "B", "C", "D", "E"]:
            if letra != alvo:
                novas_alts[letra] = textos_distratores[pos_dist]
                pos_dist += 1

        questoes_rotacionadas.append((
            num, hab, dif, enunc,
            novas_alts["A"], novas_alts["B"], novas_alts["C"], novas_alts["D"], novas_alts["E"],
            alvo, resol
        ))

    contagem_gab = Counter([q[9] for q in questoes_rotacionadas])
    print(f"Contagem por letra no gabarito: {contagem_gab}")
    for letra in ["A", "B", "C", "D", "E"]:
        assert contagem_gab[letra] == 12, f"Erro no gabarito para letra {letra}: {contagem_gab[letra]}"

    # Construção do Markdown final
    linhas = []
    linhas.append("---")
    linhas.append('série: "Ensino Médio"')
    linhas.append('disciplina: "Filosofia"')
    linhas.append('eixo: "Eixo III: Filosofia Política, Poder, Resistência e Necropolítica"')
    linhas.append('capitulo: "Capítulo 17: A Política na Antiguidade: Platão e Aristóteles"')
    linhas.append('objeto_de_conhecimento: "A gênese da política na pólis grega, a cidade ideal e a sofocracia em Platão, o homem como animal político (zoon politikon) e as formas de governo em Aristóteles"')
    linhas.append('ebook_fonte: "em-fil-c17-politica-antiga-platao-aristoteles.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: A Política na Antiguidade: Platão e Aristóteles\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-17-politica-antiga-platao-aristoteles -->"
        linhas.append(tag_html)
        linhas.append(f"### Questão {num}\n")
        linhas.append(f"{enunc}\n")
        linhas.append(f"A) {a}")
        linhas.append(f"B) {b}")
        linhas.append(f"C) {c}")
        linhas.append(f"D) {d}")
        linhas.append(f"E) {e_alt}\n")
        linhas.append(f"**Gabarito:** ({gab})\n")
        linhas.append(f"**Resolução Comentada:**\n{resol}\n")

    linhas.append("## Referências\n")
    linhas.append("- PLATÃO. *A República*. Tradução de Anna Lia Amaral de Almeida Prado. São Paulo: Martins Fontes, 2006.")
    linhas.append("- ARISTÓTELES. *A Política*. Tradução de Mário da Gama Kury. 3. ed. Brasília: Editora UnB, 1997.")
    linhas.append("- FINLEY, Moses I. *Democracia antiga e moderna*. Tradução de Waldéa Barcellos. Rio de Janeiro: Graal, 1988.")
    linhas.append("- WOLFF, Francis. *Aristóteles e a política*. Tradução de Thereza Cristina Ferreira Stummer. São Paulo: Discurso Editorial, 1999.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Salvar em temp_draft.md
    with open("temp_draft.md", "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em temp_draft.md ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador Educamob
    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-17-politica-antiga-platao-aristoteles/ebooks/em-fil-c17-politica-antiga-platao-aristoteles-exercicios.md"
    comando = f"{sys.executable} validador_educamob.py temp_draft.md {destino_final}"
    print(f"Executando validador: {comando}")

    resultado = subprocess.run(
        [sys.executable, "validador_educamob.py", "temp_draft.md", destino_final],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    print(resultado.stdout)
    if resultado.stderr:
        print(resultado.stderr)

    if resultado.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 17 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {resultado.returncode}")
        sys.exit(resultado.returncode)

if __name__ == "__main__":
    main()
