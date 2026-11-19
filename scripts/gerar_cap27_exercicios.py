# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 27 de Filosofia EM:
A Arte Trágica em Nietzsche: Apolíneo e Dionisíaco
Objeto: cap-27-arte-tragica-nietzsche-apolineo-dionisiaco
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
        "Em qual obra de estreia, publicada em 1872, Friedrich Nietzsche desconstrói a visão serena da Grécia e apresenta a dualidade entre o apolíneo e o dionisíaco?",
        "Em Crepúsculo dos Ídolos, que analisa o martelo da filosofia contemporânea.",
        "Em O Nascimento da Tragédia no Espírito da Música, escrita aos 27 anos como professor na Basiléia.",
        "Em Assim Falou Zaratustra, que narra os discursos poéticos do profeta persa.",
        "Em Genealogia da Moral, que investiga a origem dos ressentimentos clericais.",
        "Em Humano, Demasiado Humano, dedicada aos estudos da psicologia científica livre.",
        "B",
        "O Nascimento da Tragédia (1872) foi o primeiro livro de Nietzsche, no qual ele desafia a filologia clássica tradicional ao revelar as forças vitais da tragédia grega."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Qual historiador da arte e classicista europeu difundiu a imagem idealizada dos gregos antigos como modelo de 'nobre simplicidade e serena grandeza' combatida por Nietzsche?",
        "O poeta latino Virgílio em seus cantos épicos da Eneida.",
        "O historiador alemão Johann Joachim Winckelmann em seus tratados clássicos sobre a arte grega.",
        "O filósofo empirista David Hume em seus ensaios sobre a moralidade comercial.",
        "O dramaturgo barroco Pedro Calderón de la Barca em suas comédias sacras espanholas.",
        "O geógrafo Ptolomeu em seus mapas das rotas comerciais do mar Mediterrâneo.",
        "B",
        "Winckelmann e o classicismo idealizavam a Grécia como pura harmonia e serenidade; Nietzsche desmascara esse mito mostrando que os gregos conheciam o pavor e a dor cósmica profunda."
    ))

    questoes_brutas.append((
        3, "EM13CHS301", "basico",
        "O que respondeu o sátiro Sileno, companheiro de Dioniso, quando o rei Midas lhe exigiu saber o que seria o melhor para os seres humanos?",
        "Que o melhor era acumular moedas de ouro em baús para garantir banquetes festivos.",
        "Que o melhor de tudo era inalcançável: não ter nascido, nada ser; e o segundo melhor era morrer logo.",
        "Que o homem devia consagrar sua vida à redação de leis cívicas no tribunal da pólis.",
        "Que a felicidade suprema residia em navegar oceanos desconhecidos em frotas comerciais.",
        "Que a mais bela destinação mortal consistia em memorizar hinos solenes de templos oraculares.",
        "B",
        "A sabedoria de Sileno expressa a consciência crua do sofrimento mortal: os gregos sabiam que viver dói; e foi para suportar esse fardo sem se matar que eles inventaram a beleza da arte."
    ))

    questoes_brutas.append((
        4, "EM13CHS302", "basico",
        "Qual é o estado fisiológico humano associado ao impulso estético de Apolo na teoria nietzschiana da arte?",
        "O estado de fadiga muscular provocado por marchas militares prolongadas.",
        "O estado do Sonho (Traum), no qual a mente cria imagens luminosas, figuras nítidas e formas delimitadas.",
        "O estado de sonolência profunda sem lembrança de imagens ou sensações conscientes.",
        "O delírio febril originado de infecções pulmonares contagiosas em invernos frios.",
        "A náusea estomacal decorrente do consumo desmedido de temperos picantes em banquetes.",
        "B",
        "Apolo é o deus das belas ilusões do sonho: no sonho vemos formas perfeitas, deuses resplandecentes e contornos nítidos que trazem serenidade e consolo aos olhos humanos."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Qual princípio metafísico e formal define a função ordenadora e individualizante de Apolo perante o mundo da experiência?",
        "A diluição de fronteiras entre todas as criaturas terrestres em cerimônias místicas.",
        "O Princípio de Individuação (Principium Individuationis), que estabelece limites, medidas e fronteiras entre os seres.",
        "A suspensão voluntária das leis penais durante celebrações rurais de solstício de verão.",
        "A exigência de compartilhamento de bens móveis entre vizinhos de aldeias pastoris.",
        "A obrigatoriedade de uso de máscaras de barro por atores em competições trágicas.",
        "B",
        "Apolo rege o princípio de individuação: ele diz 'conhece-te a ti mesmo' e 'nada em excesso', traçando contornos firmes que impedem o indivíduo de se afogar no mar caótico do infinito."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Quais modalidades artísticas expressam predominantemente a força formativa do impulso apolíneo segundo Nietzsche?",
        "O canto coral litúrgico acompanhado por tambores rítmicos de casca de carvalho.",
        "A Escultura clássica e a Arquitetura monumental, que organizam a matéria em proporções e volumes nítidos.",
        "As danças místicas extáticas realizadas ao redor de fogueiras em noites de lua cheia.",
        "Os solos de flauta de bambu tocados por navegadores em travessias marinhas perigosas.",
        "As fábulas orais improvisadas por contadores populares em feiras de troca de gado.",
        "B",
        "Apolo é o escultor e arquiteto da forma: a pedra talhada com precisão e os templos com colunas harmônicas refletem a vitória da medida e da bela aparência sobre o informe."
    ))

    questoes_brutas.append((
        7, "EM13CHS301", "basico",
        "Qual é o estado fisiológico que caracteriza o impulso primordial do deus Dioniso em O Nascimento da Tragédia?",
        "O torpor letárgico induzido pela leitura solitária de tratados de geometria espacial.",
        "A Embriaguez (Rausch) extática, na qual desabam os limites da individualidade e o homem se une à natureza.",
        "O sono calmo e sem perturbações desfrutado por crianças em berços domésticos de madeira.",
        "A ansiedade burocrática despertada pela prestação de contas fiscais a tabelionatos municipais.",
        "A compostura rígida exigida de soldados durante inspeções matinais em casernas cívicas.",
        "B",
        "Dioniso é o deus da embriaguez: pelo vinho ou pelo despertar da primavera, o homem quebra as algemas do egoísmo particular e celebra a comunhão jubilosa com todos os seres vivos."
    ))

    questoes_brutas.append((
        8, "EM13CHS302", "basico",
        "O que ocorre com as divisões e hierarquias sociais humanas sob a influência do êxtase dionisíaco?",
        "Tornam-se mais severas e vigiadas por magistrados com aplicação de punições monetárias.",
        "São dissolvidas e superadas temporariamente, fazendo com que o escravizado se sinta livre e o senhor o abrace como irmão.",
        "Ficam submetidas à fiscalização de corporações mercantis de transporte fluvial em rios.",
        "Passam a ser registradas em livros contábeis de couro para consulta de cortes dinásticas.",
        "Exigem a construção de muralhas divisórias de pedra entre os diferentes bairros urbanos.",
        "B",
        "Sob Dioniso cai a barreira que separa os homens: não há nobre nem servo; todos se redescobrem membros da mesma grande família da vida cósmica que celebra a existência na terra."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Identifique as formas de arte que traduzem de modo mais imediato e potente o ímpeto criador de Dioniso segundo a obra de estreia de Nietzsche:",
        "A pintura em afrescos de gesso e os arabescos decorativos geométricos.",
        "A Música de timbres viscerais profundos e a Dança corporal extática.",
        "A tecelagem de tapetes de lã crua e a encadernação de pergaminhos.",
        "O desenho técnico de mapas cartográficos e o polimento de lentes ópticas.",
        "A cantaria de pedras para pavimentação de estradas provinciais rurais.",
        "B",
        "A arte dionisíaca opera pelo som e pelo movimento corpóreo: a música rítmica e a dança comunicam a torrente vital da natureza sem mediações conceituais abstratas."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Como a Tragédia Ática de Ésquilo e Sófocles se consolidou no século V a.C. na cidade de Atenas?",
        "Como um banquete aristocrático particular financiado por mercadores navais estrangeiros.",
        "Como o matrimônio sublime e a aliança fecunda entre o coro musical dionisíaco e a cena dramática apolínea.",
        "Como uma cerimônia fúnebre restrita a chefes militares veteranos de guerras marítimas.",
        "Como um concurso de memorização de artigos de leis cívicas disputado por escrivães públicos.",
        "Como um espetáculo de acrobacias com cavalos adestrados para exibição em pistas de circo.",
        "B",
        "A tragédia grega clássica é o milagre do equilíbrio: o coro dionisíaco canta as forças abissais da natureza e o palco apolíneo desenha a figura límpida do herói em cena brilhante."
    ))

    questoes_brutas.append((
        11, "EM13CHS301", "basico",
        "Qual era o papel desempenhado pelo 'Coro de Sátiros' no nascimento e desenvolvimento da tragédia grega arcaica?",
        "Vender cópias de manuscritos teatrais nas portas das arenas aos cidadãos mais abastados.",
        "Expressar a voz coletiva da natureza indômita através do canto e da dança sagrada ao redor da orquestra.",
        "Interromper o espetáculo para recolher moedas doadas pela plateia para obras sanitárias.",
        "Fiscalizar o cumprimento dos horários de entrada e saída dos espectadores nas arquibancadas.",
        "Redigir resumos das fábulas míticas em cartazes de tecido pendurados nas colunas dos templos.",
        "B",
        "O coro trágico não era figurante: ele era o útero de onde nascia a peça; os sátiros com pés de bode cantavam a força eterna da vida que chora e celebra perante o mistério da terra."
    ))

    questoes_brutas.append((
        12, "EM13CHS302", "basico",
        "De que modo a cena apolínea sobre o palco completava a força profunda da música coral dionisíaca na tragédia?",
        "Substituindo todos os instrumentos sonoros por discursos judiciais recitados em latim arcaico.",
        "Projetando a dor primordial em imagens visíveis e heróis individuais memoráveis como Prometeu e Édipo.",
        "Cobrando tributos financeiros dos atores ao final de cada ato encenado perante as autoridades.",
        "Proibindo o uso de figurinos coloridos para evitar distrações visuais entre os jurados da pólis.",
        "Obrigando a plateia a permanecer de olhos fechados durante os diálogos dos personagens cênicos.",
        "B",
        "Se o coro mostrasse apenas o abismo musical, o público enlouqueceria de terror; Apolo ergue no palco a figura bela de Édipo ou Prometeu, permitindo contemplar a dor sem ser engolido pelo nada."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Quem foram os dois protagonistas da cultura ateniense responsabilizados pelo filósofo pelo assassinato da genuína tragédia grega?",
        "O estrategista Péricles e o comandante militar Alcibíades em campanhas marítimas.",
        "O tragediógrafo Eurípides e o pensador Sócrates, arautos do racionalismo otimista.",
        "O poeta lírico Píndaro e o legislador Clístenes durante reformas cívicas.",
        "O escultor Fídias e o arquiteto Ictino responsáveis pelas obras do Partenon.",
        "O historiador Tucídides e o médico Hipócrates em seus estudos da guerra do Peloponeso.",
        "B",
        "Nietzsche acusa Eurípides e Sócrates de conspirarem contra o mistério trágico: expulsaram Dioniso da cena para entronizar a lógica silogística e o debate racionalista burguês."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Qual máxima filosófica sintetiza o princípio do 'Socratismo Estético' duramente denunciado em O Nascimento da Tragédia?",
        "A sabedoria brota do silêncio contemplativo dos eremitas solitários que habitam cavernas.",
        "Tudo deve ser consciente para ser belo; a virtude é o saber; somente o virtuoso é feliz.",
        "A beleza das coisas sensíveis depende exclusivamente da pureza dos minerais extraídos da terra.",
        "O valor de uma representação cênica calcula-se pela quantidade de tochas acesas no tablado.",
        "A verdadeira harmonia cósmica manifesta-se no canto afinado de pássaros migratórios nas florestas.",
        "B",
        "O socratismo estético acreditava que só o que a mente racional explica é bonito; ao tentar domesticar a poesia com lógica silogística, secou a seiva vital e misteriosa da arte trágica."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "Como Nietzsche define a célebre figura do 'Homem Teórico' originada do modelo socrático da civilização ocidental?",
        "Aquele que vive isolado no topo de penhascos sem manter contato com familiares ou amigos.",
        "Aquele que acredita ingenuamente que o pensamento lógico pode decifrar o ser e corrigir a dor do cosmos.",
        "Aquele que fabrica instrumentos náuticos de medição astronômica para navios mercantes oceânicos.",
        "Aquele que se dedica unicamente à modelagem de vasos cerâmicos com argilas retiradas de rios.",
        "Aquele que renuncia ao uso da linguagem escrita para comunicar-se apenas por gestos silenciosos.",
        "B",
        "O homem teórico é o otimista ingênuo: acha que a ciência vai consertar tudo, curar a morte e explicar o universo; para Nietzsche, essa crença é uma ilusão que tenta esconder o abismo trágico da vida."
    ))

    questoes_brutas.append((
        16, "EM13CHS302", "basico",
        "Qual proposição monumental sintetiza a resposta definitiva de Nietzsche contra o pessimismo niilista e a decadência moral ocidental?",
        "O destino glorioso das sociedades humanas será alcançado com a cobrança justa de impostos patrimoniais.",
        "Somente como fenômeno estético a existência e o mundo podem ser eternamente justificados.",
        "A salvação da alma individual depende da mortificação contínua do corpo biológico em mosteiros.",
        "O objetivo supremo de um povo culto consiste em conquistar territórios férteis em combates armados.",
        "A verdade suprema da história revelou-se na obediência passiva a códigos militares de infantaria.",
        "B",
        "Para Nietzsche, o mundo não tem sentido moral de fábrica nem juiz no céu; o mundo é criação estética contínua, e o homem nobre justifica a sua vida fazendo de sua caminhada uma bela obra de arte."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Qual manifestação cultural popular brasileira contemporânea foi destacada no capítulo como exemplo magistral da irrupção dionisíaca coletiva?",
        "A cerimônia protocolar de posse de magistrados em tribunais de justiça estaduais.",
        "O Carnaval de rua de Salvador, Recife, Olinda e Rio de Janeiro com seus tambores e multidões unidas.",
        "O desfile cívico de comemoração da proclamação da república em quartéis militares do exército.",
        "A sessão solene de encerramento do ano judiciário com leitura de acórdãos em plenários públicos.",
        "A prova teórica de suficiência aplicada por conselhos de contabilidade a bacharéis graduados.",
        "B",
        "O Carnaval de rua é puro Dioniso: o povo esquece a rotina de trabalho opressiva, veste fantasias, pula em multidão ao som de tambores e frevo, dissolvendo o egoísmo particular em alegria comum."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "Como os grandes festivais contemporâneos de música (como o Rock in Rio) reproduzem a experiência ancestral do dionisíaco?",
        "Reunindo milhares de pessoas que dançam e cantam em coro uníssono em transe coletivo arrebatador.",
        "Obrigando os presentes a permanecerem sentados em fileiras silenciosas durante todo o concerto musical.",
        "Distribuindo cadernos escolares para que o público anote termos técnicos de harmonia orquestral.",
        "Proibindo o uso de iluminação cênica para transformar o gramado em espaço de reflexão matemática.",
        "Aplicando testes de conhecimentos gerais sobre a biografia dos guitarristas antes da entrada na arena.",
        "A",
        "Em um festival com 100 mil pessoas pulando no mesmo ritmo com o som no peito, quebra-se a solidão das telas digitais; o sujeito experimenta a vibração física de pertencer a uma grande onda coletiva."
    ))

    questoes_brutas.append((
        19, "EM13CHS301", "basico",
        "Qual é o equívoco primário de quem supõe que Friedrich Nietzsche rejeitava a beleza de Apolo em defesa da loucura de Dioniso?",
        "Ignorar que a tragédia autêntica exige o equilíbrio dinâmico e a tensão criativa mútua entre os dois impulsos.",
        "Acreditar que os dois deuses gregos foram personagens fictícios inventados por geógrafos bizantinos.",
        "Imaginar que Apolo era a divindade responsável pela fermentação do mosto de uvas em tonéis de carvalho.",
        "Supor que Dioniso exigia que seus seguidores lessem manuais de direito civil romano antes das danças.",
        "Afirmar que a estética nietzschiana foi escrita exclusivamente para monges que habitavam abadias alpinas.",
        "A",
        "Nietzsche nunca mandou jogar fora Apolo: o caos de Dioniso sozinho é destruição cega; a forma de Apolo sozinha é estátua de gesso fria; a obra-prima trágica é a forma perfeita contendo o fogo sagrado."
    ))

    questoes_brutas.append((
        20, "EM13CHS302", "basico",
        "Como a sabedoria de Sileno deve ser interpretada à luz da superação afirmativa ensinada pela filosofia da tragédia?",
        "Como uma ordem irrevogável para que os cidadãos cometam renúncia covarde e suicídio em massa.",
        "Como a constatação do sofrimento da existência que a arte trágica enfrenta para dizer um firme 'Sim!' à vida.",
        "Como um conselho cívico formulado para estimular a poupança monetária de famílias camponesas.",
        "Como uma receita médica tradicional prescrita para combater dores de cabeça crônicas em idosos.",
        "Como uma fábula pedagógica voltada para o adestramento de animais de carga em viagens fluviais.",
        "B",
        "A frase de Sileno não é para chorar e desistir: é o chão de pedra da realidade que o grego encarou com coragem heroica; sabendo que a dor existe, ele fez da arte a maior arma para celebrar e amar a vida."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "De que maneira a teoria nietzschiana em O Nascimento da Tragédia abalou as bases da filologia acadêmica do século XIX?",
        "Substituindo a leitura de manuscritos gregos antigos por romances populares de cavalaria espanhola.",
        "Desmascarando o helenismo plácido ensinado nas universidades e revelando que a cultura grega nasceu da luta entre forças vitais cósmicas.",
        "Propondo a destruição física de todas as ruínas de mármore localizadas na península do Peloponeso.",
        "Exigindo que as cátedras universitárias fossem ocupadas unicamente por compositores de marchas militares.",
        "Provando que a civilização grega desconhecia o cultivo de vinhedos e a fabricação de instrumentos musicais.",
        "B",
        "A academia da época tratava os gregos como velhinhos bem-comportados que só pensavam em lógica e mármores frios; Nietzsche chocou a todos ao mostrar o vulcão de paixões e sangue que ardia sob aquela serenidade."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Como a imagem homérica dos 'Deuses do Olimpo' atuava na vida dos gregos arcaicos como uma transfiguração salvadora da existência?",
        "Impondo mandamentos punitivos que prometiam recompensas no purgatório aos camponeses resignados.",
        "Justificando a condição humana ao retratar divindades que viviam com esplendor, paixões e tragédias a própria vida terrena.",
        "Obrigando os marinheiros a entregarem suas cargas comerciais em portos antes do início de guerras.",
        "Instituindo tribunais de inquisição eclesiástica encarregados de queimar heréticos em praças municipais.",
        "Proibindo a prática de ginástica olímpica e os jogos desportivos em santuários dedicados a Zeus.",
        "B",
        "Os deuses gregos não eram santos puritanos cobrando pecados: eram humanos gigantescos que amavam, lutavam e festejavam; ver seus deuses vivendo intensamente na Terra fazia o grego amar a sua própria vida humana."
    ))

    questoes_brutas.append((
        23, "EM13CHS301", "intermediario",
        "Em que sentido o conceito de 'Sonho' (Traum) em Apolo difere de uma simples ilusão enganosa desprovida de valor?",
        "Por constituir a bela aparência redentora que torna o mundo visível ordenado, inteligível e suportável para a mente humana.",
        "Por consistir em fórmulas matemáticas exatas capazes de medir a distância orbital entre a Lua e o planeta Marte.",
        "Por ser um regulamento disciplinar militar adotado por generais espartanos para treinar cavaleiros novatos.",
        "Por depender da inalação de fumaças tóxicas emanadas de minas subterrâneas de carvão mineral betuminoso.",
        "Por ter sido catalogado por tabelionatos florestais como uma infração contra a tranquilidade de vilarejos rurais.",
        "A",
        "O sonho apolíneo não é mentira boba: é a forma bela que a alma humana cria para que a existência não seja um caos disforme e pavoroso; a bela aparência dá abrigo, luz e medida para que possamos viver com nobreza."
    ))

    questoes_brutas.append((
        24, "EM13CHS302", "intermediario",
        "De que modo a dissolução do 'Princípio de Individuação' na embriaguez dionisíaca reflete a sabedoria da natureza viva?",
        "Exigindo que cada indivíduo construa cercas de pedra mais altas ao redor de suas propriedades rurais.",
        "Revelando que as fronteiras do ego egoísta são transitórias perante a torrente una e eterna da vida cósmica compartilhada.",
        "Provando que as relações de parentesco consanguíneo dependem de certidões lavradas por escrivães públicos.",
        "Obrigando os cidadãos das repúblicas democráticas a votarem no mesmo candidato em pleitos eleitorais anuais.",
        "Demonstrando que os recursos pesqueiros dos rios pertenciam exclusivamente a navegadores armados do mar.",
        "B",
        "Quando o indivíduo se fecha no seu ego pequenino, vive com medo da morte e inveja do vizinho; na embriaguez dionisíaca ele sente que o seu eu é apenas uma gota passageira no oceano indestrutível da vida universal."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Qual é a relação mítica entre a tragédia clássica e o mito órfico do despedaçamento de Dioniso pelos Titãs?",
        "Os heróis trágicos como Édipo e Prometeu sofrem e sucumbem em cena como reflexos do sofrimento e renascimento do próprio Dioniso.",
        "Os atores gregos eram obrigados a sacrificar touros brancos sobre o tablado cênico diante dos magistrados.",
        "As peças de teatro eram apresentadas unicamente durante eclipses lunares para agradar corporações mercantis.",
        "Os textos dramáticos deviam ser gravados em placas de chumbo fundido antes de sua leitura em assembleias.",
        "Os dramaturgos atenienses recebiam subsídios financeiros pagos diretamente pelo tesouro da Pérsia antiga.",
        "A",
        "No mito, os Titãs despedaçam o jovem Dioniso, mas ele renasce glorioso; na peça de teatro, o herói Édipo ou Prometeu é despedaçado pelo destino, espelhando a dor sagrada do deus e a renovação eterna da vida."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "Como Eurípides transformou os personagens míticos tradicionais ao submeter o teatro grego ao influxo do pensamento socrático?",
        "Tornando-os divindades invisíveis que se manifestavam exclusivamente por meio de relâmpagos noturnos.",
        "Substituindo a grandeza misteriosa dos heróis trágicos por homens comuns repletos de debates retóricos cotidianos e mesquinharias.",
        "Exigindo que todos os diálogos cênicos fossem entoados em língua persa por cantores profissionais diplomados.",
        "Obrigando os atores a utilizarem armaduras de infantaria pesada pesando mais de quarenta quilos no tablado.",
        "Transformando as peças dramáticas em competições atléticas de arremesso de discos de bronze polido.",
        "B",
        "Eurípides levou a fofoca da praça e o cálculo dos tribunais para o teatro: o herói mítico perdeu seu mistério assombroso e virou um burguês que discute argumentos, enfraquecendo a magia sagrada da tragédia."
    ))

    questoes_brutas.append((
        27, "EM13CHS301", "intermediario",
        "Por que Nietzsche sustenta que a pretensão socrática de que 'a virtude é o saber' gerou um homem doente e desenraizado da vida?",
        "Porque o filósofo de Atenas defendia a queima compulsória de navios mercantes em portos comerciais abertos.",
        "Porque ao subordinar os instintos criadores e o corpo à tutela de conceitos abstratos, castrou a coragem trágica e as paixões vitais da humanidade.",
        "Porque a lógica silogística exigia o pagamento de honorários elevados aos sofistas que lecionavam retórica.",
        "Porque os cidadãos atenienses foram proibidos de praticar atividades agropecuárias durante as estações chuvosas.",
        "Porque a filosofia socrática impunha a destruição de todas as colunas de mármore dos templos dedicados a Hera.",
        "B",
        "Ao ensinar que quem peca é quem não sabe lógica e que tudo tem que passar pela peneira do cérebro calculista, Sócrates domesticou os instintos do homem; o ocidente ficou com a cabeça cheia de conceitos e o peito vazio de paixão."
    ))

    questoes_brutas.append((
        28, "EM13CHS302", "intermediario",
        "Qual é o significado da metáfora da 'criança brincando na areia da praia' utilizada por Nietzsche para descrever o jogo do mundo?",
        "Indica que as sociedades humanas devem ser governadas por tutores indicados por congregações religiosas.",
        "Expressa a realidade cósmica como pura criação e destruição inocente de formas, sem finalidade moral externa nem culpa punitiva.",
        "Comprova que a economia mercantil dependia da exploração de minérios de silício em costas litorâneas.",
        "Demonstra que as brincadeiras infantis devessem ser regulamentadas por assembleias populares municipais.",
        "Afirma que a história universal caminha necessariamente para o restabelecimento de monarquias absolutistas.",
        "B",
        "A criança faz o castelo de areia na praia e depois passa a mão derrubando com uma gargalhada; não há maldade nela; o cosmos é assim: estrelas nascem e morrem, flores desabrocham e murcham, num jogo magnífico e inocente."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Em que medida a dedicatória inicial de O Nascimento da Tragédia a Richard Wagner reflete as esperanças artísticas do jovem Nietzsche?",
        "Nietzsche considerava as óperas monumentais de Wagner como o renascimento da tragédia grega na Europa através da Obra de Arte Total.",
        "Nietzsche pretendia obter auxílio financeiro do compositor para custear a compra de caravelas mercantes alemãs.",
        "Nietzsche buscava aprovação do músico para ingressar como primeiro-tenente nas fileiras da marinha imperial.",
        "Nietzsche planejava abandonar a filosofia para trabalhar como afinador de órgãos tubulares em igrejas rurais.",
        "Nietzsche pretendia proibir a circulação de livros didáticos em conservatórios musicais da Saxônia central.",
        "A",
        "O jovem Nietzsche via em Wagner (com Tristão e Isolda) o ressurgimento da grande arte total: música profunda, drama e mito unidos no palco alemão para curar a Europa do racionalismo frio e vazio."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Por que Nietzsche posteriormente rompeu de forma amarga e definitiva sua amizade com Richard Wagner?",
        "Porque o compositor se recusou a pagar o aluguel de cavalos utilizados em viagens alpinas pelo filósofo.",
        "Porque Wagner curvou-se à religiosidade cristã e ao moralismo de redenção em sua última ópera Parsifal, capitulando perante a negação da vida.",
        "Porque os teatros de ópera da Alemanha foram confiscados por comissões disciplinares de veteranos de guerra.",
        "Porque Wagner passou a compor unicamente canções ligeiras para espetáculos circenses itinerantes populares.",
        "Porque o músico assinou um contrato comercial para exportar partituras impressas para cidades coloniais asiáticas.",
        "B",
        "Nietzsche não perdoou a ópera Parsifal: para ele, Wagner ajoelhou-se na cruz da moral cristã pedindo perdão e castidade, traindo o fogo dionisíaco e a coragem de amar a terra com paixão."
    ))

    questoes_brutas.append((
        31, "EM13CHS301", "intermediario",
        "De que modo a literatura trágica de Guimarães Rosa em Grande Sertão: Veredas dialoga com a tensão entre o apolíneo e o dionisíaco?",
        "Excluindo qualquer menção a conflitos de jagunços para focar exclusivamente na descrição botânica de cactos.",
        "Transmutando as paixões indômitas, o medo do diabo e a violência da terra sertaneja na arquitetura sublime e inventiva de sua linguagem poética.",
        "Exigindo que os moradores do sertão prestassem juramentos solenes perante comissões consulares de alfândegas.",
        "Provando que as veredas do cerrado mineiro foram cartografadas por engenheiros militares da Prússia ocidental.",
        "Limitando o vocabulário das narrativas sertanejas a provérbios tradicionais retirados de manuais agrícolas.",
        "B",
        "O sertão de Guimarães Rosa é o próprio caos dionisíaco: tiros, pactos com o demo, paixão cega e a morte rondando; e tudo isso ganha forma milagrosa através da prosa apolínea mais bela já escrita em língua portuguesa."
    ))

    questoes_brutas.append((
        32, "EM13CHS302", "intermediario",
        "Como as adaptações cinematográficas de Shakespeare dirigidas por Akira Kurosawa (como Ran) encarnam o milagre da tragédia nietzschiana?",
        "Utilizando unicamente atores amadores selecionados através de sorteios realizados em escolas de desenho.",
        "Combinando a fúria sanguinária das batalhas e a insensatez do destino com uma composição visual austera, planos equilibrados e beleza plástica impecável.",
        "Eliminando todas as sequências dramáticas para exibir documentários sobre técnicas agrícolas de cultivo de arroz.",
        "Obrigando os espectadores de salas de exibição a memorizarem as árvores genealógicas de clãs samurais.",
        "Proibindo o uso de trilhas sonoras instrumentais para privilegiar discursos cívicos sobre tributação fundiária.",
        "B",
        "Em Ran de Kurosawa, o mundo está pegando fogo em traição, loucura e guerra (Dioniso puro); mas a câmera se posiciona com uma geometria de cores, silêncios e enquadramentos tão perfeitos (Apolo) que a dor vira puro encanto estético."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Qual é a correspondência entre a teoria estética de Nietzsche e os estudos antropológicos de Victor Turner sobre a 'Liminaridade' nos rituais comunitários?",
        "A comprovação de que as leis cívicas de todas as cidades antigas foram compiladas por astrônomos persas.",
        "O reconhecimento de que as festividades extáticas suspendem temporariamente normas sociais para renovar os laços de fraternidade e vitalidade do corpo social.",
        "A exigência de que os participantes de ritos coletivos devessem pagar tributos a corporações de marceneiros.",
        "A afirmação de que as danças tribais eram executadas unicamente para garantir a orientação de caravelas mercantes.",
        "A determinação de que os líderes religiosos aplicassem sanções monetárias a jovens durante períodos de colheita.",
        "B",
        "A antropologia comprova Nietzsche: toda sociedade que não enlouquece precisa de um momento carnavalesco ou ritual onde patrão e empregado se misturam e as regras travadas caem para a vida voltar a respirar com força."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "Como a distinção freudiana entre Eros e a Pulsão de Morte (Thanatos) em O Mal-Estar na Civilização antecipa os temas de O Nascimento da Tragédia?",
        "Negando a existência de conflitos psicológicos no interior da mente de operários e comerciantes urbanos.",
        "Espelhando a permanente tensão humana entre a força apolínea construtora da civilização e as forças dionisíacas de agressividade, dissolução e retorno à natureza.",
        "Exigindo que os estudos psicanalíticos utilizassem unicamente relógios de pêndulo para registrar sonhos.",
        "Provando que as patologias nervosas eram causadas exclusivamente pela ingestão de águas fluviais não filtradas.",
        "Determinando que os tratamentos clínicos fossem conduzidos sob a fiscalização de comandantes militares de casernas.",
        "B",
        "Freud ecoa Nietzsche: Eros é Apolo querendo erguer a casa, a ordem e o laço do indivíduo; Thanatos é Dioniso rompendo as portas para a terra primordial; a condição humana é essa corda esticada entre construir a forma e beijar o abismo."
    ))

    questoes_brutas.append((
        35, "EM13CHS301", "intermediario",
        "O que representa a imagem dos 'homens-bodes' (os sátiros que compunham o coro) na concepção da natureza defendida pela tragédia?",
        "Um símbolo de ignorância e rusticidade que devia ser eliminado pela civilização urbana esclarecida.",
        "A representação viva e sagrada do homem natural primordial, livre das hipocrisias morais e das máscaras artificiais da vida em sociedade.",
        "Um modelo pedagógico criado para ensinar técnicas de pastoreio de caprinos em encostas montanhosas.",
        "Uma figura grotesca destinada unicamente a provocar risos ligeiros em crianças durante feiras rurais.",
        "Uma imagem alegórica desenhada por magistrados consulares para alertar cidadãos sobre perigos florestais.",
        "B",
        "O sátiro não é um bicho nojento: ele é o homem autêntico da floresta, que ri, deseja, canta e não tem vergonha do próprio corpo; o coro de sátiros lavava a alma dos gregos cansados do teatro de aparências da vida civilizada."
    ))

    questoes_brutas.append((
        36, "EM13CHS302", "intermediario",
        "Por que, para Nietzsche, a atitude trágica é o oposto absoluto da atitude resignada do homem ressentido?",
        "Porque o homem trágico ama a luta e aceita a dor do combate como parte do jogo, enquanto o ressentido cultiva ódio, mágoa e culpa contra a vida.",
        "Porque o homem trágico recusa-se a participar de celebrações festivas comunitárias em praças públicas.",
        "Porque o homem ressentido é sempre o fundador de companhias mercantis de navegação comercial no mar.",
        "Porque o homem trágico gasta sua renda familiar comprando peças de mármore para erguer monumentos.",
        "Porque o homem ressentido foi educado em academias de equitação militar para servir em guerras externas.",
        "A",
        "O ressentido chora no canto, culpa os outros, amaldiçoa a carne e sonha com o céu vingativo; o homem trágico toma a dor no peito, olha no olho da tempestade e diz: 'Era isto a vida? Pois muito bem! Outra vez!'."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Qual é o papel da arte de Ésquilo e Sófocles na transformação do horror cósmico em sublime consolo metafísico?",
        "Substituir o sofrimento por orações que garantem a fertilidade das lavouras em anos de estiagem prolongada.",
        "Permitir ao ser humano olhar o abismo da destruição sem se desesperar, sabendo que a Vida é indestrutível por trás dos heróis mortais.",
        "Obrigar os jovens cidadãos a prestarem serviço voluntário na limpeza de arquibancadas de madeira de teatros.",
        "Provar que as tempestades marinhas podem ser contidas por meio da leitura pública de certidões cívicas.",
        "Submeter a produção de peças dramáticas à censura prévia de comissões formadas por oficiais da marinha.",
        "B",
        "O consolo metafísico não é dizer que Édipo não sofreu; Édipo sofreu e arrancou os olhos; mas ao final da peça sentimos que a Vida humana é majestosa e grandiosa, e que vale a pena existir nesta Terra."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "Como a crítica de Nietzsche a Sócrates antecipa sua demolição genealógica dos valores da moralidade cristã no Capítulo 13?",
        "Mostrando que a moral socrática foi um complô orquestrado por banqueiros fenícios para monopolizar rotas marítimas.",
        "Identificando no socratismo a raiz da covardia ocidental que odeia o corpo, teme a tragédia e inventa um Além-Mundo para fugir da realidade terrena.",
        "Provando que as regras gramaticais clássicas foram adulteradas por escrivães de alfândegas portuárias imperiais.",
        "Demonstrando que os filósofos pré-socráticos utilizavam métodos contábeis mais avançados do que os atenienses.",
        "Afirmando que a decadência de Atenas decorreu unicamente da escassez de pedreiras de mármore de boa qualidade.",
        "B",
        "Sócrates é o bisavô do cristianismo para Nietzsche: foi ele quem começou com a conversa de que a carne não presta, que o sofrimento é culpa e que a felicidade está num mundo perfeito invisível; a vida virou pecado."
    ))

    questoes_brutas.append((
        39, "EM13CHS301", "intermediario",
        "De que modo a experiência estética trágica opera como o antídoto supremo contra o tédio existencial e a anestesia emocional contemporânea?",
        "Prescrevendo o isolamento total dos indivíduos em cabines acústicas vedadas em edifícios de escritórios.",
        "Reconectando a sensibilidade humana com a intensidade de sentimentos profundos que arrancam a mente do conformismo passivo das redes digitais.",
        "Exigindo que os estudantes devessem memorizar cronologias de batalhas militares do Império Austro-Húngaro.",
        "Proibindo o uso de instrumentos musicais eletrônicos em festas populares realizadas em bairros litorâneos.",
        "Determinando que a frequência a espetáculos artísticos seja controlada por cartões de ponto corporativos.",
        "B",
        "Num mundo onde as pessoas rolam telas zumbis sem sentir nada real, a arte trágica arromba o peito: ela traz o arrepio do assombro, o riso da festa e a lágrima autêntica que nos lembram de que estamos vivos."
    ))

    questoes_brutas.append((
        40, "EM13CHS302", "intermediario",
        "Por que a 'Justificação Estética' formulada por Nietzsche não deve ser confundida com um esteticismo fútil ou capricho burguês de consumo?",
        "Porque ela não é hobby decorativo de salão; é uma postura ética e existencial heroica de afirmar a vida e criar a si mesmo diante do abismo da realidade.",
        "Porque as obras de arte clássicas eram comercializadas com isenção compulsória de tributos de importação naval.",
        "Porque os filósofos românticos eram remunerados com pensões concedidas por assembleias parlamentares prussianas.",
        "Porque a fruição artística dependia de atestados de idoneidade moral emitidos por congregações paroquiais.",
        "Porque a justificação do mundo foi concebida originalmente como uma tática de propaganda militar para guerras.",
        "A",
        "Não se trata de colecionar vasinhos caros na sala: justificar a vida esteticamente é a coragem de ser o autor da sua própria história, esculpindo sentido onde não havia sentido nenhum, amando a própria jornada."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a crítica radical empreendida por Friedrich Nietzsche em O Nascimento da Tragédia contra o modelo civilizatório erigido pelo 'Socratismo Estético': de que maneira o filósofo alemão desarticula a equação socrática entre Razão, Virtude e Felicidade, demonstrando que o otimismo teórico castrou as forças criadoras arcaicas da cultura ocidental?",
        "Provando que os manuscritos de Platão foram redigidos com tintas extraídas de frutos de oliveiras silvestres.",
        "Evidenciando que, ao postular que apenas o que é racionalmente transparente e consciente é belo e virtuoso, Sócrates baniu o mistério dionisíaco, os instintos viscerais e o pavor cósmico da existência, instaurando uma cultura doente e ressentida que acredita ingenuamente que a ciência teórica e a dialética abstrata podem curar o sofrimento primordial e redimir o homem de sua condição mortal.",
        "Determinando que as academias atenienses devessem ser transformadas em entrepostos de comercialização de linho.",
        "Afirmando que a decadência do teatro clássico grego decorreu do encarecimento das vestimentas de linho dos sátiros.",
        "Comprovando que os sofistas mantinham sociedades anônimas para o financiamento de expedições navais mercantes.",
        "B",
        "- **Etapa 1:** Desmascarar o dogma socrático: Sócrates proclamou que 'a virtude é o saber' e que quem compreende o bem é feliz; com isso, ele tentou submeter toda a exuberância da vida aos conceitos frios do intelecto.\n- **Etapa 2:** Revelar a mutilação da civilização: ao expulsar a embriaguez, a música e o mistério de Dioniso, Sócrates gerou um homem teórico enfraquecido que tem medo da terra e da carne, trocando a tragédia viva por silogismos estéreis."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a dialética do 'Matrimônio Trágico' entre Apolo e Dioniso em Ésquilo e Sófocles: por que a grandeza estética insuperável da Tragédia Ática reside na tensão fecunda entre o abismo dionisíaco da música do coro e a ilusão apolínea da cena do herói, e não na supressão de um pelo outro?",
        "Mostrando que os cenários de madeira dos teatros gregos eram pintados com pigmentos solúveis em água de chuva.",
        "Demonstrando que o Dionisíaco fornece a força vital primordial, a música arrebatadora e o contato com a dor profunda da terra, enquanto o Apolíneo engendra a forma nítida, a beleza plástica da palavra e o herói individual que permite ao espectador contemplar a destruição sem se afogar no terror, realizando a transfiguração redentora do caos em arte sublime.",
        "Determinando que as apresentações teatrais devessem ser encerradas obrigatoriamente antes do pôr do sol em Atenas.",
        "Afirmando que a aliança entre os deuses foi formulada para comemorar tratados de armistício assinados com Esparta.",
        "Comprovando que a arquitetura dos teatros ao ar livre utilizava pedras calcárias retiradas de ilhas do mar Egeu.",
        "B",
        "- **Etapa 1:** Reconhecer a catástrofe de uma força isolada da outra: Dioniso puro seria a fúria cega que destrói a mente humana no terror; Apolo puro seria a frieza acadêmica de estátuas sem vida e sem alma.\n- **Etapa 2:** Celebrar o matrimônio trágico perfeito: a música selvagem do coro dionisíaco sobe do fundo da terra e o palco apolíneo desenha o rosto límpido de Édipo ou Prometeu; a forma segura salva os olhos enquanto a música sacode a alma."
    ))

    questoes_brutas.append((
        43, "EM13CHS301", "dificil",
        "Investigue a tese nietzschiana de que 'o Olimpo e os deuses homéricos foram criados pelos gregos como um escudo de beleza contra o terror de Sileno': de que maneira a transfiguração artística apolínea operou como condição biológica e espiritual de sobrevivência para o helenismo?",
        "Comprovando que os templos do monte Olimpo eram utilizados para estocar colheitas agrícolas durante geadas.",
        "Demonstrando que os helenos conheciam o abismo da enfermidade, da dor e do nada revelado pela profecia de Sileno; perante o risco de suicídio e paralisia existencial, forjaram os deuses olímpicos como espelhos resplandecentes que viviam com intensidade a própria existência humana, transfigurando o pavor primordial em júbilo estético afirmativo.",
        "Determinando que os sacerdotes dos templos de Apolo fossem selecionados exclusivamente entre generais navais veteranos.",
        "Afirmando que as narrativas mitológicas foram inventadas por corporações de sapateiros para promover feiras rurais.",
        "Provando que a veneração aos deuses olímpicos decorria de decretos de reis micênicos gravados em lâminas de bronze.",
        "B",
        "- **Etapa 1:** Encarar o pesadelo de Sileno: o sábio Sileno gritou no ouvido do rei Midas que o melhor era não ter nascido e morrer logo; os gregos sentiam esse pavor nos ossos e na carne mortal.\n- **Etapa 2:** Erigir o escudo resplandecente da arte: para não morrer de desgosto, os gregos criaram os deuses do Olimpo; deuses que amam, brigam, riem e festejam; ao olhar para seus deuses radiantes, o grego pôde dizer: 'Vale a pena viver nesta Terra!'."
    ))

    questoes_brutas.append((
        44, "EM13CHS302", "dificil",
        "Analise a ruptura histórica perpetrada por Eurípides na estrutura dramática da tragédia grega: de que modo a expulsão do coro dionisíaco e a introdução do 'espectador comum' no tablado transformaram a tragédia arcaica na comédia nova e no drama burguês da decadência?",
        "Mostrando que os dramaturgos atenienses do século IV a.C. utilizavam tablados confeccionados com madeiras de pinho.",
        "Evidenciando que Eurípides reduziu a magnitude misteriosa dos heróis míticos a indivíduos comuns que expõem justificativas racionais mesquinhas e litígios cívicos no palco; ao secundarizar a música sagrada do coro em favor da verborragia lógica, desmantelou o arrebatamento trágico, rebaixando a obra de arte à reprodução moralizante do cotidiano prosaico.",
        "Determinando que os ingressos para as representações dramáticas devessem ser pagos com moedas de chumbo carimbadas.",
        "Afirmando que a decadência do teatro decorreu de desentendimentos matrimoniais entre os atores principais da companhia.",
        "Comprovando que os festivais dionisíacos foram substituídos por conferências diplomáticas sobre tarifas marítimas.",
        "B",
        "- **Etapa 1:** Descrever o golpe de Eurípides no palco sagrado: ele olhou para o herói mítico colossal e disse 'vou colocar no palco o homem comum da feira, com suas fofocas, argumentos jurídicos e continhas de dinheiro'.\n- **Etapa 2:** Constatar a morte do arrebatamento cósmico: o coro de sátiros perdeu a voz e virou enfeite descartável; o palco virou um tribunal burguês morno; a tragédia que abalava o universo morreu assassinada pela prosa do dia a dia."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Examine o alcance ético e cósmico da tese 'Somente como fenômeno estético a existência e o mundo podem ser eternamente justificados': por que essa formulação nietzschiana desmantela simultaneamente a teologia cristã e o cientificismo utilitarista burguês?",
        "Provando que as investigações filológicas de Nietzsche dependiam de autorizações expedidas por tribunais prussianos.",
        "Demonstrando que, ao destituir o cosmos de qualquer desígnio moral transcendental (julgamento final cristão) ou propósito de progresso histórico mecânico (utilitarismo científico), Nietzsche afirma a realidade como devir trágico inocente, convocando o homem a se emancipar da culpa e a criar sua própria vida como uma obra de arte apaixonada que diz um vibrante 'Sim!' à existência.",
        "Determinando que as cátedras universitárias de filosofia devessem ser financiadas por companhias mercantis de sal.",
        "Afirmando que a justificação estética do mundo foi concebida por generais militares para justificar derrotas bélicas.",
        "Comprovando que a recusa da teologia moral foi uma tese copiada de regulamentos disciplinares de marinheiros russos.",
        "B",
        "- **Etapa 1:** Demolir as muletas do consolo moral: o padre diz 'sofra aqui que Deus vai pagar no céu'; o cientista ingênuo diz 'a técnica vai acabar com todo sofrimento na Terra'; os dois mentem para fugir da dor real do mundo.\n- **Etapa 2:** Assumir a glória do criador trágico: o mundo não tem roteiro pronto nem sentido automático; o mundo é um jogo belo e terrível; o homem forte não chora suas cicatrizes: faz delas a matéria-prima de sua grandeza estética."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Investigue a aproximação e o posterior distanciamento estético de Friedrich Nietzsche em relação a Richard Wagner: por que a defesa apaixonada da 'Obra de Arte Total' (Gesamtkunstwerk) em 1872 converteu-se em repúdio implacável na obra Crepúsculo dos Ídolos?",
        "Comprovando que as partituras sinfônicas alemãs utilizavam pautas impressas em papéis de linho importado.",
        "Evidenciando que Nietzsche enxergava inicialmente nas óperas monumentais wagnerianas a ressurreição heroica do coro dionisíaco e do mito trágico capaz de regenerar a Europa; contudo, ao presenciar em Parsifal a capitulação do compositor à religiosidade cristã, ao consolo da renúncia ascética e à teatralidade histriônica, denunciou Wagner como um decadentista apóstata que traiu a vida.",
        "Determinando que as apresentações de ópera na Baviera fossem suspensas durante períodos de colheita de cevada.",
        "Afirmando que a amizade entre Nietzsche e Wagner foi desfeita por desavenças relativas ao preço de passagens de trem.",
        "Provando que Wagner planejava transferir seus festivais de Bayreuth para cidades litorâneas do mar Negro.",
        "B",
        "- **Etapa 1:** Recordar o entusiasmo juvenil por Wagner: Nietzsche dedicou seu primeiro livro ao amigo Wagner, jurando que sua música trágica gigantesca (como em Tristão) traria Dioniso de volta para curar a Europa moderna.\n- **Etapa 2:** Sentir o choque da traição em Parsifal: quando Wagner colocou sinos de igreja, sangue de Cristo e redenção moral no palco, Nietzsche vomitou de nojo; acusou o velho mestre de virar beato frouxo que trocou o martelo da vida pela hóstia."
    ))

    questoes_brutas.append((
        47, "EM13CHS301", "dificil",
        "Analise o papel da Música como a 'Linguagem Imediata da Vontade e do Cósmico' em O Nascimento da Tragédia: por que a música dionisíaca opera em um nível de profundidade existencial inacessível às artes plásticas figurativas?",
        "Provando que as cordas de harpas gregas eram confeccionadas com tendões de ovelhas criadas em planícies.",
        "Demonstrando que, ao passo que a escultura e a pintura criam cópias de formas individuais visíveis delimitadas no espaço (apolíneo), a música dionisíaca não imita o fenômeno exterior passageiro; ela expressa diretamente a seiva palpitante da própria vida, o coração agitado da natureza e a força indestrutível que sobrevive a todas as formas particulares mortais.",
        "Determinando que as partituras musicais devessem ser catalogadas unicamente por bibliotecários de cortes dinásticas.",
        "Afirmando que a primazia da música decorria de sua utilidade militar para ditar o ritmo de remadores em galeras navais.",
        "Comprovando que os compositores gregos recebiam salários pagos em sementes de cevada por magistrados da pólis.",
        "B",
        "- **Etapa 1:** Separar o olho do ouvido: a escultura de mármore e a pintura mostram uma forma finita que você olha de longe e que ocupa um lugar estático no espaço; é a beleza da casca exterior.\n- **Etapa 2:** Sentir o poder visceral do som: a música não tem casca nem parede; ela é tempo, vibração e sangue; a música dionisíaca entra direto nas entranhas da alma e conecta o homem com o pulsar indomável da própria terra viva."
    ))

    questoes_brutas.append((
        48, "EM13CHS302", "dificil",
        "Examine o conceito nietzschiano de 'Consolo Metafísico' proporcionado pela tragédia grega arcaica: de que maneira o espectador ateniense saía do teatro reconciliado com o destino e fortalecido para enfrentar as agruras da vida real?",
        "Comprovando que os espectadores recebiam certidões de comparecimento que asseguravam isenção de impostos cívicos.",
        "Demonstrando que, em vez de ser entorpecido por uma promessa de paraíso no além ou alienado por finais felizes fáceis, o espectador contemplava a destruição inelutável do herói com a convicção serena de que, embora os indivíduos pereçam, a torrente da Vida permanece eternamente fecunda e indestrutível, retornando ao cotidiano com coragem e amor à existência.",
        "Determinando que os cidadãos devessem jejuar de alimentos cárneos nos três dias que antecediam as encenações dramáticas.",
        "Afirmando que o consolo metafísico foi uma teoria formulada por comissões de saúde pública para conter surtos de cólera.",
        "Provando que as apresentações trágicas eram encerradas com discursos patrióticos proferidos por generais da marinha.",
        "B",
        "- **Etapa 1:** Recusar a mentira da 'anestesia barata': consolo trágico não é o filminho com final feliz onde tudo dá certo e o mocinho casa; na tragédia, Édipo é cegado e Prometeu tem o fígado devorado pelo abutre.\n- **Etapa 2:** Descobrir a força heróica do consolo autêntico: mesmo vendo a catástrofe do herói, o espectador descobre que a Vida é maior que a morte de um homem só; ele sai do teatro com o peito erguido, pronto para encarar sua própria caminhada sem medo."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Investigue o diálogo entre a estética dionisíaca de Nietzsche e a celebração do Carnaval popular no Brasil: de que maneira a subversão temporária de fronteiras de classe, gênero e poder confirma a atualidade do conceito de 'Dissolução da Individuação' nas culturas contemporâneas?",
        "Mostrando que os carros alegóricos dos desfiles utilizavam estruturas metálicas montadas por estaleiros navais.",
        "Evidenciando que, durante os dias de festa carnavalesca, as barreiras sociais rígidas do capitalismo são suspensas pela embriaguez do riso, pelo transe coletivo dos tambores e pela fusão dos corpos na rua, recriando empiricamente o momento sagrado dionisíaco no qual a multidão transcende o isolamento privado para comungar na alegria visceral da matéria viva.",
        "Determinando que as festividades populares de rua sejam reguladas exclusivamente por manuais de etiqueta de cortes europeias.",
        "Afirmando que a experiência carnavalesca foi criada por companhias mercantis de café para elevar o consumo de açúcar refinado.",
        "Comprovando que a alegria popular dependia de concessões concedidas anualmente por comissões de disciplina militar.",
        "B",
        "- **Etapa 1:** Descrever o aprisionamento da rotina moderna: o ano todo a pessoa vive trancada no ônibus lotado, humilhada pelo chefe, separada por contas bancárias e isolada pelo celular.\n- **Etapa 2:** Celebrar o estouro dionisíaco do Carnaval: quando a bateria do samba e os tambores do maracatu explodem, cai o crachá e cai o terno; o povo dança junto, se beija e se abraça; é Dioniso vivo nas ruas do Brasil quebrando as correntes da separação."
    ))

    questoes_brutas.append((
        50, "EM13CHS102", "dificil",
        "Analise a relação entre o pessimismo heroico grego em Nietzsche e a recusa radical do 'Pessimismo Niilista Passivo' de Arthur Schopenhauer: por que o filósofo de O Nascimento da Tragédia utiliza o vocabulário schopenhaueriano (como a Vontade e o véu de Maia) para alcançar uma conclusão diametralmente oposta sobre o valor da vida?",
        "Provando que Schopenhauer utilizava bengalas de madeira de jacarandá em suas caminhadas diárias por Frankfurt.",
        "Demonstrando que, enquanto Schopenhauer concluía que a Vontade é sofrimento cego e que a única saída digna é a renúncia ascética, a castidade e a negação da existência, Nietzsche descobre na arte trágica a força jubilosa para afirmar a vida com todas as suas dores, convertendo a náusea do absurdo no mais ardente e corajoso 'Sim!' pronunciado perante o cosmos.",
        "Determinando que os livros de filosofia alemã fossem traduzidos compulsoriamente para o dialeto dos pescadores do Báltico.",
        "Afirmando que o distanciamento entre Nietzsche e Schopenhauer decorreu de disputas por direitos autorais em livrarias de Berlim.",
        "Comprovando que Schopenhauer recomendava a seus alunos a prática diária de natação em rios congelados durante o inverno.",
        "B",
        "- **Etapa 1:** Notar o ponto de partida comum com Schopenhauer: Schopenhauer ensinou que viver é querer, e querer é sofrer; o mundo é dor e a morte engole tudo; Nietzsche concordava que o mundo dói.\n- **Etapa 2:** Virar a mesa e dar o salto trágico: Schopenhauer covardemente propôs virar monge e negar a vida; Nietzsche fez o oposto com a tragédia: 'o mundo dói? Então vamos cantar, dançar e amar a vida com coragem heroica!'; é a virada da renúncia para a afirmação."
    ))

    questoes_brutas.append((
        51, "EM13CHS301", "dificil",
        "Examine a advertência contida no capítulo sobre os perigos da 'Degeneração Dionisíaca Desmedida': por que as orgias e bacanais arcaicas pré-gregas do Oriente representavam uma ameaça destrutiva à cultura antes de sua domesticação artística pela aliança com Apolo?",
        "Comprovando que as celebrações bárbaras utilizavam tochas acesas com azeites de baixa qualidade e cheiro desagradável.",
        "Demonstrando que o impulso dionisíaco desprovido da contenção formal apolínea degenera em violência caótica informe, desregramento destrutivo e barbárie selvagem; a genialidade helênica consistiu em forjar um dique de medida e beleza plástica através de Apolo, transmutando a fúria cega da natureza em arte sublime e celebração civilizada da vida.",
        "Determinando que os governantes das cidades bárbaras aplicassem sanções disciplinares a todos os fabricantes de vinho.",
        "Afirmando que as festas bárbaras foram reprimidas por expedições militares comandadas por navegadores da frota persa.",
        "Provando que as celebrações místicas utilizavam instrumentos sonoros afinados segundo tratados de aritmética egípcia.",
        "B",
        "- **Etapa 1:** Olhar o horror do dionisíaco desatado na barbárie: nos cultos selvagens arcaicos do Oriente, havia mutilações, violência desmedida e orgias sangrentas onde o ser humano virava bicho raivoso.\n- **Etapa 2:** Exaltar o milagre grego com Apolo: a Grécia não proibiu Dioniso, mas o casou com a medida e a nobreza de Apolo; o resultado não foi sangueira nas matas, mas a beleza sagrada da tragédia teatral no coração da cidade."
    ))

    questoes_brutas.append((
        52, "EM13CHS302", "dificil",
        "Investigue a crítica nietzschiana ao conceito de 'Catarse' aristotélica e à moralização pedagógica da arte: por que conceber a tragédia como uma purgação medicinal de paixões doentias ou lição cívica rebaixa a soberania do acontecimento estético?",
        "Provando que Aristóteles utilizava balanças mecânicas defeituosas para medir as proporções de remédios em ateliês.",
        "Demonstrando que, ao reduzir a fruição trágica a um remédio moralizante para apaziguar o medo e a compaixão no cidadão, Aristóteles subordinou a arte a finalidades terapêuticas e morais medíocres; para Nietzsche, a tragédia não serve para domesticar cidadãos: é o júbilo cósmico do guerreiro espiritual que celebra a força invulnerável da vida perante o terror.",
        "Determinando que os manuscritos da Poética fossem arquivados em caixas de carvalho trancadas por comissões de generais.",
        "Afirmando que a catarse foi inventada por corporações mercantis de teatro para justificar a cobrança de ingressos públicos.",
        "Comprovando que as peças dramáticas eram avaliadas por veterinários responsáveis pela saúde de animais em Atenas.",
        "B",
        "- **Etapa 1:** Criticar a redução burguesa de Aristóteles: Aristóteles dizia que vamos ao teatro para chorar o medo e a pena, limpando as emoções doentias para voltar para casa como um cidadão manso e comportado.\n- **Etapa 2:** Resgatar a fogueira nietzschiana da arte: a tragédia não é remédio de farmácia nem xarope para acalmar nervos; a tragédia é o relâmpago que desperta a coragem da alma para rir diante da dor e abraçar a vida como um leão."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Analise a relevância do conceito de 'Socratismo Estético' para a compreensão crítica da Sociedade Tecnocrática Contemporânea: de que maneira a obsessão pelo cálculo algorítmico, pela utilidade mensurável e pela erradicação técnica da dor reproduz a patologia do homem teórico socrático?",
        "Provando que os servidores de telecomunicações modernos utilizam cabos submarinos revestidos por polímeros plásticos.",
        "Evidenciando que a civilização contemporânea hiper-racionalizada herda a utopia socrática de que métricas, inteligências artificiais e protocolos técnicos podem erradicar o trágico, anestesiar o sofrimento e substituir o mistério da existência pela gestão algorítmica da vida, gerando uma sociedade entorpecida que perdeu a capacidade poética de habitar a terra com intensidade trágica.",
        "Determinando que os computadores digitais devessem ser programados unicamente com base em manuais de retórica clássica.",
        "Afirmando que a tecnologia digital foi criada para cumprir previsões oraculares gravadas em colunas de santuários gregos.",
        "Comprovando que a gestão de redes sociais depende de inspeções realizadas por comissões disciplinares de infantaria.",
        "B",
        "- **Etapa 1:** Diagnosticar a ilusão tecnocrata de hoje: achamos que o aplicativo, a pílula que anestesia a dor e o algoritmo que prevê tudo vão fazer o ser humano feliz sem esforço e sem angústia.\n- **Etapa 2:** Denunciar o ápice do socratismo doente: ao fugir de qualquer dor e tentar transformar a vida numa planilha de produtividade, viramos robôs frios; a tragédia de Nietzsche nos chama de volta à vida com seus mistérios, dores e grandezas irrepetíveis."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Examine o paralelismo entre a tragédia de 'Prometeu Acorrentado' de Ésquilo e o 'Mito de Édipo Rei' de Sófocles sob a ótica de O Nascimento da Tragédia: como esses heróis encarnam, respectivamente, o sofrimento titanicamente ativo e a sabedoria trágica que nasce do contato com o abismo?",
        "Comprovando que os figurinos dos atores utilizavam máscaras de gesso cozidas em fornos alimentados por carvão vegetal.",
        "Demonstrando que Prometeu expressa a audácia titânica que desafia os deuses pelo bem da humanidade e aceita a dor heróica do castigo cósmico, enquanto Édipo encarna a sabedoria que decifra o enigma da esfinge mas é obrigado a descer ao abismo do incesto e da cegueira, provando que a grandeza do homem autêntico reside em sua capacidade inquebrantável de carregar o fardo de seu destino.",
        "Determinando que as tragédias sobre deuses e heróis fossem encenadas unicamente por sacerdotes do templo de Delfos.",
        "Afirmando que as narrativas sobre Prometeu e Édipo foram elaboradas por escrivães públicos para instruir processos criminais.",
        "Provando que as obras de Ésquilo e Sófocles eram financiadas por ligas marítimas para promover o comércio de armamentos.",
        "B",
        "- **Etapa 1:** Admirar a coragem titânica de Prometeu: ele rouba o fogo para os mortais e, amarrado na rocha com o abutre comendo sua carne, não se ajoelha perante a tirania de Zeus; ele é o rebelde nobre que sofre de pé.\n- **Etapa 2:** Aprofundar o mistério doloroso de Édipo: ele desvenda o enigma, salva a cidade, mas ao descobrir seu próprio destino terrível, fura os olhos e assume sua dor sem culpar os deuses; os dois mostram a nobreza sublime do herói trágico."
    ))

    questoes_brutas.append((
        55, "EM13CHS301", "dificil",
        "Investigue o papel da 'Dança Extática' na comunhão dionisíaca arcaica: por que Nietzsche afirma que sob o encanto dionisíaco o homem 'não é mais artista, tornou-se ele próprio obra de arte'?",
        "Provando que os passos de dança eram registrados em pergaminhos preservados em bibliotecas de mosteiros beneditinos.",
        "Demonstrando que, ao dançar e cantar arrebatado pelo ritmo sagrado, o homem abandona a atitude passiva de espectador exterior que apenas contempla telas ou estátuas; ele próprio transfigura seu corpo e seus movimentos na expressão viva das forças da natureza cósmica, integrando-se como matéria vibrante e criadora no jogo glorioso da vida universal.",
        "Determinando que as festividades coreográficas devessem ser supervisionadas por fiscais de corporações de pedreiros.",
        "Afirmando que a dança extática foi introduzida na Grécia por companhias mercantis navais especializadas em transporte de especiarias.",
        "Comprovando que as danças coletivas dependiam de atestados médicos de aptidão física expedidos por comissões sanitárias.",
        "B",
        "- **Etapa 1:** Romper com o espectador passivo de museu: o homem comum fica sentado na cadeira olhando para um quadro na parede, separado da obra como um consumidor curioso de domingo.\n- **Etapa 2:** Tornar-se a própria obra de arte em Dioniso: na dança extática e no coro, o corpo do homem sua, pula, canta e vibra; ele não pinta mais o quadro: ele é a tela viva da natureza, transbordando o sagrado em cada músculo e respiração."
    ))

    questoes_brutas.append((
        56, "EM13CHS302", "dificil",
        "Analise a relação entre o 'Pessimismo da Força' (conceito introduzido por Nietzsche no prefácio de 1886) e o 'Pessimismo da Fraqueza': por que o olhar sem ilusões para o horror da existência pode ser uma manifestação de exuberante saúde vital e não de decadência mórbida?",
        "Mostrando que os prefácios de livros filosóficos eram impressos em oficinas tipográficas autorizadas por cortes dinásticas.",
        "Evidenciando que o pessimismo da fraqueza é o definhamento do covarde que, apavorado diante da dor, cai na depressão, no ressentimento e na fuga moralista do mundo; ao passo que o pessimismo da força é o atributo do espírito exuberante que, transbordando vitalidade e audácia, busca conscientemente a dureza do trágico porque sabe que somente a luta contra o abismo forja a nobreza suprema da condição humana.",
        "Determinando que os estudantes devessem realizar avaliações pedagógicas unicamente através de questionários de memorização.",
        "Afirmando que a distinção entre formas de pessimismo foi copiada de relatórios contábeis de corporações mercantis marítimas.",
        "Comprovando que as teses do prefácio de 1886 foram redigidas para justificar alianças políticas entre reinos germânicos.",
        "B",
        "- **Etapa 1:** Separar o pessimismo do fraco: o fraco vê a dor da vida e se encolhe na cama, vira cínico apático ou chora pedindo que Deus acabe logo com o mundo para levá-lo ao céu.\n- **Etapa 2:** Celebrar o pessimismo do forte: os gregos arcaicos tinham tanta saúde e tanta vida no sangue que queriam encarar o perigo nos olhos; a tragédia é a arte dos fortes que amam o desafio e sorriem perante o dragão da existência."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Examine o papel pedagógico do estudo da dialética entre o Apolíneo e o Dionisíaco no Ensino Médio de acordo com as diretrizes da BNCC: de que maneira o aprendizado da tragédia nietzschiana desenvolve no estudante a sensibilidade crítica contra o niilismo e as pressões de sucesso imediato da sociedade de consumo?",
        "Provando que as matrizes curriculares nacionais devem priorizar unicamente a reprodução técnica de modelos pré-fabricados.",
        "Demonstrando que a formação estética trágica ensina o jovem a acolher as dores, incertezas e frustrações da juventude sem desespero ou apatia, compreendendo que a vida autêntica não é uma vitrine de perfeição das redes sociais, mas um processo vivo de criação e superação de si mesmo, municiando-o de autonomia ética e coragem para fazer de sua história uma obra singular de dignidade e beleza.",
        "Determinando que os estudantes devessem realizar testes vocacionais padronizados baseados em critérios puramente contábeis.",
        "Afirmando que a leitura de obras filosóficas clássicas deve ser suspensa nas escolas para reduzir custos de aquisição de livros.",
        "Comprovando que o estudo de artes trágicas depende de autorizações prévias expedidas por comissões de disciplina militar.",
        "B",
        "- **Etapa 1:** Diagnosticar a angústia da juventude de hoje: nas redes sociais tudo parece perfeito, milionário e feliz; quando o jovem comum tropeça, erra ou sofre, ele se sente um fracassado indigno de viver.\n- **Etapa 2:** Libertar a mente com Nietzsche na BNCC: a tragédia ensina que errar, sofrer e lutar faz parte da vida de qualquer gigante; o jovem aprende a não ter vergonha de suas feridas e a construir sua própria grandeza com paixão e verdade."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Analise a articulação entre a sabedoria de Sileno e o conceito contemporâneo de 'Resiliência Psicológica e Existencial': como a superação estética grega desautoriza leituras superficialistas da autoajuda comercial que pregam o positivismo cego e a eliminação mágica do sofrimento?",
        "Mostrando que os manuais didáticos de psicologia utilizavam encadernações de couro fabricadas em feiras artesanais.",
        "Evidenciando que a autoajuda rasa vende a ilusão tóxica de que todo sofrimento é falha de pensamento e que a felicidade plena pode ser comprada em passos simples; ao passo que a sabedoria trágica parte da constatação honesta de Sileno de que a existência é dura e contingente, ensinando que a verdadeira força humana não reside em fingir que a dor não existe, mas em transmutar as agruras da realidade em grandeza e sentido estético profundo.",
        "Determinando que os livros de filosofia moral devam conter advertências sanitárias obrigatórias em suas capas.",
        "Afirmando que as teorias de resiliência foram elaboradas por companhias mercantis de navegação para treinar marujos novatos.",
        "Comprovando que as narrativas sobre o rei Midas foram catalogadas exclusivamente para orientar cobranças fiscais de tributos.",
        "B",
        "- **Etapa 1:** Desmascarar o 'positivismo tóxico': a autoajuda barata diz 'pense positivo e tudo dará certo, sofrer é fraqueza sua'; isso gera culpa e desespero quando a desgraça real bate na porta.\n- **Etapa 2:** Afirmar a honra trágica da dor: Nietzsche e Sileno mostram que a dor é real e inescapável; resiliência de verdade não é sorrir amarelo na foto: é ter a coragem de encarar o temporal e fazer da própria vida um monumento de superação e beleza."
    ))

    questoes_brutas.append((
        59, "EM13CHS301", "dificil",
        "Investigue a tese nietzschiana sobre a 'Transfiguração da Feiura e da Desarmonia' na arte dionisíaca: de que maneira a inclusão da dissonância, da feiura e da ruína no espetáculo estético expande a compreensão da beleza para muito além do mero agrado decorativo superficial?",
        "Comprovando que os cenários das comédias gregas utilizavam madeiras de demolição recolhidas em portos marítimos.",
        "Demonstrando que, enquanto a estética classicista ingênua confina o belo às linhas calmas e agradáveis, a tragédia dionisíaca acolhe a dissonância e a feiura como expressões necessárias do devir da vida que se renova; a arte trágica prova que o horrível transfigurado pela forma e pela música desperta o prazer mais sublime e arrebatador que a mente humana pode experimentar.",
        "Determinando que os dramaturgos que utilizassem temas tristes devessem pagar multas aos tesouros municipais da pólis.",
        "Afirmando que a dissonância musical foi proibida por decretos de magistrados consulares em assembleias cívicas abertas.",
        "Provando que a inclusão de ruínas em telas pictóricas decorria da falta de recursos financeiros para restaurar monumentos.",
        "B",
        "- **Etapa 1:** Romper com a 'beleza cor-de-rosa': achar que só é belo o que é bonitinho, liso e perfumado é uma tolice que apequena a alma humana e exclui metade da nossa experiência.\n- **Etapa 2:** Celebrar o júbilo da dissonância: na música pesada ou na tragédia de Shakespeare e Kurosawa, o grito, o sangue e a quebra de harmonia causam um choque tão profundo que a mente acorda; a feiura transfigurada em arte revela a majestade terrível da vida."
    ))

    questoes_brutas.append((
        60, "EM13CHS302", "dificil",
        "Ao encerrarmos o Capítulo 27 com a demolição do racionalismo clássico pela dualidade Apolíneo-Dionisíaco em Nietzsche, analise como a passagem da arte ritualística e mítica para o Capítulo 28 preparará o terreno para Walter Benjamin, onde a reprodução mecânica no século XX decretará o 'declínio da aura' da obra de arte na modernidade industrial:",
        "Provando que as investigações de história da arte perderam relevância após a inauguração de linhas telegráficas urbanas.",
        "Demonstrando que, após Nietzsche revelar que a tragédia repousava no coro sagrado e na experiência mítica irrepetível do culto, Walter Benjamin investigará como a fotografia e o cinema industrial liquidaram o valor de culto e a 'aura' mágica tradicional da obra, transferindo a arte da esfera do ritual dionisíaco para o campo da política de massas e da reprodutibilidade técnica.",
        "Determinando que os currículos de filosofia devam limitar-se ao estudo de compêndios de contabilidade de empresas têxteis.",
        "Afirmando que Walter Benjamin rejeitou as teses de Nietzsche por considerá-lo um autor de manuais de carpintaria naval.",
        "Comprovando que a transição entre os capítulos estéticos depende de laudos periciais expedidos por alfândegas marítimas.",
        "B",
        "- **Etapa 1:** Sintetizar o cume da arte trágica no Cap 27: Nietzsche mostrou que a grande arte clássica nascia do ritual sagrado, do mistério coletivo e da presença viva do coro irrepetível na orquestra grega.\n- **Etapa 2:** Abrir as portas com entusiasmo para Walter Benjamin no Cap 28: no século XX, chegam a câmera fotográfica e o rolo de cinema; a obra é copiada milhões de vezes e perde sua 'aura' mágica única; fechamos o Cap 27 com a chave de ouro da tragédia viva para mergulhar na era da reprodutibilidade técnica!"
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
    linhas.append('capitulo: "Capítulo 27: A Arte Trágica em Nietzsche: Apolíneo e Dionisíaco"')
    linhas.append('objeto_de_conhecimento: "A dualidade estética entre o apolíneo e o dionisíaco em O Nascimento da Tragédia, a sabedoria de Sileno, a morte da tragédia pelo socratismo estético e a justificação estética da existência"')
    linhas.append('ebook_fonte: "em-fil-c27-arte-tragica-nietzsche-apolineo-dionisiaco.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS301"')
    linhas.append('  - "EM13CHS302"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: A Arte Trágica em Nietzsche: Apolíneo e Dionisíaco\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-27-arte-tragica-nietzsche-apolineo-dionisiaco -->"
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
    linhas.append("- NIETZSCHE, Friedrich. *O nascimento da tragédia: ou helenismo e pessimismo*. Tradução de J. Guinsburg. São Paulo: Companhia das Letras, 1992.")
    linhas.append("- NIETZSCHE, Friedrich. *Crepúsculo dos ídolos: ou como se filosofa com o martelo*. Tradução de Paulo César de Souza. São Paulo: Companhia das Letras, 2006.")
    linhas.append("- MARTON, Scarlett. *Nietzsche: das forças cósmicas aos valores humanos*. 2. ed. Belo Horizonte: Editora UFMG, 2010.")
    linhas.append("- GIACOIA JÚNIOR, Oswaldo. *Nietzsche*. São Paulo: Publifolha, 2000.")
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

    destino_final = "content/medio/volume-unico/filosofia/eixo-4-estetica/cap-27-arte-tragica-nietzsche-apolineo-dionisiaco/ebooks/em-fil-c27-arte-tragica-nietzsche-apolineo-dionisiaco-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 27 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
