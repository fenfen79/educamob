# -*- coding: utf-8 -*-
"""
Script de geração e validação da Lista de Exercícios - Capítulo 14: Filosofia Moral Africana e o Princípio Ubuntu
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
        "Qual é a tradução mais precisa e consagrada do aforismo de matriz linguística banta 'Umuntu ngumuntu ngabantu'?",
        "O homem nasce livre, mas por toda parte vive acorrentado por leis da corte.",
        "Uma pessoa só é uma pessoa através de outras pessoas, revelando que a condição humana é relacional e comunitária.",
        "O olho humano é o espelho que reflete as sombras na caverna escura.",
        "A riqueza individual determina o valor de cada guerreiro perante o rei.",
        "O pensamento solitário basta para fundar a certeza da existência física.",
        "B",
        "O aforismo banta sintetiza o núcleo do Ubuntu: a humanidade não é um atributo isolado de um átomo autônomo, mas um processo vivo de co-humanização tecido nas relações de acolhimento e cuidado com o outro."
    ))

    questoes_brutas.append((
        2, "EM13CHS501", "basico",
        "Em contraposição ao cogito cartesiano ('Penso, logo existo'), como o filósofo John Mbiti sintetizou a perspectiva africana sobre o ser humano?",
        "Eu conquisto territórios novos, logo me torno senhor da história.",
        "Eu sou porque nós somos; e, visto que nós somos, logo eu sou.",
        "Eu possuo propriedades de terra, logo tenho direitos políticos plenos.",
        "Eu calculo meus lucros mercantis, logo posso governar a cidade.",
        "Eu duvido da matéria corpórea, logo afirmo a primazia do espírito.",
        "B",
        "John Mbiti evidencia que no pensamento comunitário africano o 'nós' precede e fundamenta o 'eu': a identidade individual não surge do isolamento reflexivo, mas da pertença orgânica à teia social."
    ))

    questoes_brutas.append((
        3, "EM13CHS102", "basico",
        "Segundo a obra de Mogobe Ramose, qual preconceito colonial europeu precisou ser desconstruído para afirmar a legitimidade da filosofia africana?",
        "A ideia de que o comércio de tecidos africanos dependia de navegação fluvial.",
        "O mito colonial racista de que os povos da África Subsaariana seriam desprovidos de capacidade racional e de pensamento abstrato reflexivo.",
        "A tese de que a agricultura familiar consome menos água do que a pecuária extensiva.",
        "A premissa de que os instrumentos musicais de percussão não produzem harmonias melódicas.",
        "A crença de que as línguas bantas possuíam poucos vocábulos para nomear plantas medicinais.",
        "B",
        "Ramose denuncia a violência colonial que utilizou o mito da racionalidade como privilégio branco para negar a humanidade dos povos africanos e legitimar a escravidão e o colonialismo."
    ))

    questoes_brutas.append((
        4, "EM13CHS502", "basico",
        "Na análise etimológica das línguas bantas apresentada no e-book, como se estrutura o termo Ubuntu?",
        "Pela junção de termos que significam apenas vitória militar e disciplina armada.",
        "Pela composição dos morfemas 'Ubu-' (a universalidade contínua do ser) e '-Ntu' (a manifestação concreta da vida na pessoa humana).",
        "Pela combinação de palavras que descrevem rotas marítimas comerciais do oceano Índico.",
        "Pela aglutinação de conceitos que regulam o pagamento de tributos reais em ouro.",
        "Pela fusão de vocábulos que delimitam cercas territoriais entre pastagens rurais.",
        "B",
        "A estrutura morfológica revela a dinâmica entre o ser universal em fluxo (Ubu-) e a sua corporificação viva na singularidade humana convivente (-Ntu)."
    ))

    questoes_brutas.append((
        5, "EM13CHS503", "basico",
        "Qual marco legal brasileiro tornou obrigatório o ensino da história e da cultura afro-brasileira e africana na educação básica nacional?",
        "O Decreto Imperial de abertura dos portos de 1808 assinado pela corte portuguesa.",
        "A Lei Federal nº 10.639/2003, que alterou as diretrizes da educação nacional.",
        "O Código de Processo Penal promulgado durante a década de 1940.",
        "A Lei das Doze Tábuas que regia a convivência civil na Roma republicana.",
        "O Tratado de Tordesilhas celebrado entre as coroas ibéricas no século XV.",
        "B",
        "A Lei 10.639/03 é o marco legal fundamental que combate o racismo estrutural e o eurocentrismo curricular, exigindo a inclusão das matrizes filosóficas e culturais africanas nas escolas."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Qual papel histórico e ético foi desempenhado pelo arcebispo Desmond Tutu na transição democrática da África do Sul na década de 1990?",
        "Ele comandou batalhões de infantaria armada que cercaram as capitais provinciais.",
        "Ele presidiu a Comissão da Verdade e Reconciliação (CVR), aplicando o princípio do Ubuntu para promover a pacificação nacional.",
        "Ele redigiu os decretos de censura sobre a imprensa esportiva e literária de Joanesburgo.",
        "Ele organizou a cobrança de taxas aduaneiras sobre os navios de carga no porto de Durban.",
        "Ele fundou companhias privadas de mineração de diamantes na região de Pretória.",
        "B",
        "Desmond Tutu liderou a CVR propondo um caminho fundado no Ubuntu: a revelação pública da verdade plena para viabilizar a reconciliação e a cura social sem vingança sangrenta."
    ))

    questoes_brutas.append((
        7, "EM13CHS501", "basico",
        "Em que consiste a concepção de ser humano como 'energia vital em fluxo' no pensamento banta?",
        "Em uma teoria mecânica sobre a queima de carvão mineral em locomotivas a vapor.",
        "Na compreensão de que o ser humano não é uma substância estática e isolada, mas uma potência contínua que se constrói e se realiza na teia das relações comunitárias.",
        "Na defesa de que os indivíduos devem acumular moedas de ouro para fortalecer seus corpos.",
        "No cálculo estatístico das calorias gastas pelos agricultores durante as colheitas.",
        "Na certeza de que as estações do ano determinam o destino moral dos governantes.",
        "B",
        "O ser é devir e relação viva: o indivíduo não nasce com sua condição humana plenamente consolidada; ele se humaniza no cuidado ético recíproco."
    ))

    questoes_brutas.append((
        8, "EM13CHS502", "basico",
        "O que afirma o provérbio tradicional banta 'O rei só é rei por causa do povo' a respeito da autoridade política?",
        "Que os governantes devem manter exércitos permanentes com espadas de ferro.",
        "Que o poder político não reside na força tirânica, mas é um mandato comunitário que depende do serviço ao bem comum e da mediação harmônica.",
        "Que a coroa real deve ser confeccionada com pedras preciosas encontradas em rios.",
        "Que os monarcas possuem ascendência divina irrevogável perante os súditos camponeses.",
        "Que os tributos sobre alimentos devem ser aumentados em períodos de geada no inverno.",
        "B",
        "Mogobe Ramose destaca que a legitimidade governativa na tradição banta emana da comunidade: governar é encarnar o Ubuntu na preservação da justiça e da concórdia coletiva."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "Qual é o objetivo central do paradigma da 'Justiça Restaurativa' fundamentado na ética do Ubuntu?",
        "Impor penas de isolamento carcerário em celas escuras sem contato humano.",
        "Reparar os danos sofridos pela vítima, restabelecer laços humanos rompidos e reintegrar o ofensor por meio da verdade e da responsabilidade.",
        "Arrecadar fundos pecuniários para os cofres do Tesouro Nacional através de multas diárias.",
        "Proibir que os acusados tenham direito a falar durante as audiências públicas de custódia.",
        "Executar punições corporais severas em praça pública diante de multidões de curiosos.",
        "B",
        "A justiça restaurativa foca na cura das relações feridas e na reparação concreta do dano, recusando o mero castigo retributivo que multiplica o sofrimento."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Em contraposição à justiça restaurativa, qual é o princípio orientador da 'Justiça Retributiva' tradicional de matriz ocidental?",
        "Promover o perdão incondicional sem apuração de qualquer culpa ou responsabilidade.",
        "Encarar o delito como uma afronta abstrata à lei do Estado e aplicar ao culpado um castigo proporcional de dor ou encarceramento.",
        "Distribuir cestas de alimentos para todas as famílias do bairro onde ocorreu a infração.",
        "Substituir os julgamentos de magistrados por consultas a adivinhos tradicionais.",
        "Financiar a construção de bibliotecas públicas com doações anônimas de comerciantes.",
        "B",
        "O modelo retributivo tradicional pune a quebra da norma estatal aplicando uma pena proporcional de sofrimento ('dor por dor'), alijando a vítima do processo."
    ))

    questoes_brutas.append((
        11, "EM13CHS501", "basico",
        "Quem compõe a chamada 'tríade cósmica comunitária' na filosofia de Mogobe Ramose?",
        "Os generais do exército, os ministros da fazenda e os cobradores de impostos da capital.",
        "Os antepassados (a memória ancestral), os vivos (o presente comunitário) e as gerações futuras (o compromisso de preservação da terra).",
        "Os mercadores marítimos, os pescadores litorâneos e os tecelões de algodão do campo.",
        "Os legisladores civis, os juízes criminais e os carcereiros das prisões urbanas.",
        "Os médicos da corte, os botânicos exploradores e os farmacêuticos de laboratório.",
        "B",
        "A comunidade no Ubuntu abarca a linhagem temporal e ecológica plena: respeita os que vieram antes, cuida dos que vivem agora e protege a Terra para os que virão depois."
    ))

    questoes_brutas.append((
        12, "EM13CHS503", "basico",
        "Por que, para Desmond Tutu, a vingança e o ressentimento destroem tanto a vítima quanto o agressor?",
        "Porque as armas brancas de combate corpo a corpo se desgastam quando utilizadas com frequência.",
        "Porque ao desumanizar o outro por vingança, o próprio indivíduo perde sua dignidade humana e se corrompe no ciclo destrutivo do ódio.",
        "Porque as leis civis de trânsito proíbem manifestações públicas durante o período noturno.",
        "Porque os tribunais internacionais cobram taxas processuais elevadas para registrar queixas.",
        "Porque os governos estrangeiros suspendem a compra de trigo de países que adotam leis duras.",
        "B",
        "Tutu demonstra que a humanidade é indivisível: quem alimenta o ódio para destruir o agressor acaba por se desumanizar no mesmo veneno, inviabilizando a reconstrução social."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Qual era a condição mandatória e indispensável imposta pela Comissão da Verdade e Reconciliação (CVR) da África do Sul para a concessão de anistia aos perpetradores do apartheid?",
        "O pagamento de quantias milionárias em moedas estrangeiras aos diplomatas estrangeiros.",
        "A confissão pública irrestrita e integral de todos os crimes cometidos, incluindo a indicação do paradeiro das vítimas desaparecidas.",
        "A renúncia voluntária ao direito de voto em todas as eleições sindicais do país.",
        "A realização de viagens de exílio marítimo para cidades do hemisfério norte.",
        "A assinatura de termos de fidelidade militar aos generais condecorados do exército.",
        "B",
        "A verdade plena perante a comunidade foi a chave da anistia restaurativa: sem a revelação transparente dos fatos e a escuta do lamento das vítimas, não há reconciliação genuína."
    ))

    questoes_brutas.append((
        14, "EM13CHS502", "basico",
        "Como a filosofia moral africana encara a apropriação predatória da natureza e o enriquecimento individual desmedido?",
        "Como demonstrações legítimas de astúcia comercial e progresso técnico irrefutável.",
        "Como rompimentos graves da reciprocidade cósmica que agridem a memória dos ancestrais e roubam o futuro das próximas gerações.",
        "Como práticas necessárias para financiar a expansão de frotas navais em alto-mar.",
        "Como direitos naturais sagrados assegurados pelo contrato social de governança civil.",
        "Como etapas inevitáveis que dispensam preocupações ecológicas ou solidariedade mútua.",
        "B",
        "A ecologia relacional do Ubuntu compreende a Terra como patrimônio vivo compartilhado; a destruição ambiental é vista como crime contra a teia comunitária total."
    ))

    questoes_brutas.append((
        15, "EM13CHS501", "basico",
        "Qual é um dos erros comuns mais frequentes na interpretação contemporânea da filosofia do Ubuntu?",
        "Imaginar que ela foi escrita na língua alemã clássica por professores de física mecânica.",
        "Reduzir sua ética a um sentimentalismo romântico ingênuo ou passividade conformista, ignorando sua exigência profunda de verdade, justiça e reparação.",
        "Achar que seus princípios regulam apenas a navegação de canoas em rios tropicais.",
        "Sustentar que ela proíbe qualquer tipo de conversa entre vizinhos de um mesmo bairro.",
        "Afirmar que ela foi formulada durante os julgamentos medievais da inquisição papal.",
        "B",
        "Ubuntu não é tolerância piegas ao erro: é uma ética rigorosa que confronta a injustiça exigindo revelação total da verdade, responsabilização de atos e restauração do tecido social."
    ))

    questoes_brutas.append((
        16, "EM13CHS102", "basico",
        "Outro equívoco habitual sobre o pensamento comunitário africano consiste em confundi-lo com:",
        "Um tratado militar sobre o posicionamento de canhões de ferro em fortes litorâneos.",
        "Um coletivismo autoritário totalitário que sufoca a liberdade e a singularidade de cada indivíduo.",
        "Um compêndio de receitas culinárias tradicionais para festas de início de colheita.",
        "Um manual técnico de mineração de cobre para operários de fábricas industriais.",
        "Uma teoria de astronomia sobre os anéis de poeira que orbitam planetas gasosos.",
        "B",
        "Ramose e Wiredu enfatizam que o Ubuntu não anula a individualidade: a comunidade não é um bloco tirânico, mas um solo fértil onde a originalidade de cada pessoa floresce no diálogo com os outros."
    ))

    questoes_brutas.append((
        17, "EM13CHS502", "basico",
        "Como os Círculos de Construção de Paz aplicados no ambiente escolar brasileiro expressam a filosofia do Ubuntu?",
        "Substituindo todos os livros didáticos de história por filmes de ficção científica.",
        "Promovendo o diálogo restaurativo entre vítimas, ofensores e comunidade para reparar o dano e reconstituir os laços de convivência escolar sem exclusão.",
        "Determinando que os alunos reprovados devam prestar serviços militares de vigilância.",
        "Obrigando os professores a aplicarem provas de matemática com questões de concurso público.",
        "Cobrando mensalidades financeiras proporcionais ao comportamento disciplinar de cada turma.",
        "B",
        "Os círculos escolares de paz trazem a sabedoria restaurativa para o cotidiano: a palavra compartilhada cicatriza o atrito e reintegra o jovem ao grupo social."
    ))

    questoes_brutas.append((
        18, "EM13CHS501", "basico",
        "Como a experiência dos Bancos Comunitários de Desenvolvimento nas periferias brasileiras (como o Banco Palmas) reflete o princípio comunitário africano?",
        "Cobrando as maiores taxas bancárias do mercado financeiro internacional sobre pequenos empréstimos.",
        "Organizando moedas sociais locais e crédito solidário baseado na confiança recíproca e no apoio mútuo, fortalecendo a economia do próprio território.",
        "Proibindo que moradores de favelas comercializem produtos artesanais em feiras de bairro.",
        "Importando moedas de ouro de bancos centrais da Europa para transações no varejo.",
        "Exigindo que os clientes comprovem posse de grandes propriedades de terra para abrir contas.",
        "B",
        "A economia solidária periférica coloca a vida e a cooperação no centro: a riqueza circula internamente e emancipa a comunidade através da interdependência generosa."
    ))

    questoes_brutas.append((
        19, "EM13CHS503", "basico",
        "Qual é o significado do lema 'Uma sobe e puxa a outra', adotado por coletivos negros em universidades públicas brasileiras, à luz do Ubuntu?",
        "A exigência de que os estudantes usem escadas de corda para subir aos prédios das reitorias.",
        "A celebração da conquista acadêmica como vitória partilhada com toda a linhagem ancestral e comunitária, convertendo a ascensão individual em compromisso de acolhimento aos demais.",
        "A determinação de que apenas alunas de cursos de engenharia civil possam participar de congressos científicos.",
        "A proibição de que os estudantes graduados exerçam suas profissões em cidades do interior do país.",
        "A defesa de que o mérito acadêmico é uma propriedade puramente egoísta e individual do concorrente.",
        "B",
        "A prática antirracista recusa o mérito solitário liberal: cada conquista é fruto de resistências geracionais e deve servir para abrir portas e amparar os companheiros de jornada."
    ))

    questoes_brutas.append((
        20, "EM13CHS101", "basico",
        "Por que é incorreto supor que a filosofia africana se reduza a mitos orais sem tradição acadêmica rigorosa?",
        "Porque todos os povos da África antiga utilizavam computadores eletrônicos de precisão.",
        "Porque a filosofia africana contemporânea é um campo acadêmico fecundo e metódico, com correntes consolidadas como a filosofia profissional, a filosofia interpretativa do sentido e a filosofia sagaz.",
        "Porque os primeiros tratados de física quântica foram impressos em tipografias de Alexandria.",
        "Porque as universidades europeias adotaram o idioma suaíli em todas as aulas de teologia clássica.",
        "Porque as assembleias tribais seguiam rigorosamente os manuais de retórica forense de Roma.",
        "B",
        "A filosofia africana é plural e erudita: pensadores renomados como Hountondji, Wiredu, Okere e Oruka debatem de modo sistemático problemas éticos, lógicos e existenciais globais."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao comparar a fundamentação do sujeito no 'Cogito' de René Descartes com a perspectiva relacional do Ubuntu, qual é o contraste central entre os dois modelos?",
        "Descartes defendia que a certeza decorre da convivência em praça pública, enquanto o Ubuntu prega o isolamento mental voluntário.",
        "Descartes funda a certeza da existência na interioridade reflexiva solitária da mente que duvida, enquanto o Ubuntu afirma que o indivíduo só alcança a plena condição humana através da reciprocidade comunitária.",
        "Descartes acreditava que os animais marinhos possuíam almas racionais, enquanto os filósofos bantas negavam a existência do mundo material visível.",
        "Descartes rejeitava o uso da matemática para medir a natureza, enquanto o Ubuntu priorizava a astronomia de posição nas navegações litorâneas.",
        "Descartes afirmava que o Estado soberano deve controlar a moralidade particular, enquanto o Ubuntu defendia o liberalismo econômico radical.",
        "B",
        "O contraste é paradigmático: o sujeito moderno cartesiano é atomista e solipsista ('eu penso'); o sujeito africano do Ubuntu é intrinsecamente relacional ('nós somos, logo eu sou')."
    ))

    questoes_brutas.append((
        22, "EM13CHS501", "intermediario",
        "De acordo com a crítica de Mogobe Ramose, como o racismo epistêmico ocidental atuou nas obras de pensadores iluministas como David Hume e Immanuel Kant?",
        "Afirmando que os povos africanos possuíam técnicas metalúrgicas superiores às europeias em fundição de ferro.",
        "Desqualificando explicitamente os povos negros como incapazes de reflexão filosófica abstrata, utilizando esse juízo discriminatório para justificar a espoliação e a escravização.",
        "Propondo a tradução de cantos sagrados africanos para o latim eclesiástico utilizado em cerimônias litúrgicas.",
        "Defendendo que os comerciantes britânicos deveriam adotar moedas de cobre emitidas por reinos africanos.",
        "Sustentando que o clima equatorial era o mais favorável ao desenvolvimento de academias científicas de matemática.",
        "B",
        "Ramose e teóricos descoloniais evidenciam que grandes nomes do iluminismo europeu sustentaram teses racistas abertas, vinculando a racionalidade filosófica exclusivamente ao homem branco."
    ))

    questoes_brutas.append((
        23, "EM13CHS502", "intermediario",
        "No vocabulário conceitual do Ubuntu, por que a condição humana é compreendida como um 'processo de aperfeiçoamento contínuo' e não como um dado biológico acabado?",
        "Porque os ossos do esqueleto humano continuam crescendo durante todas as décadas da velhice.",
        "Porque pertencer à espécie biológica não garante automaticamente a realização da dignidade ética; torna-se pessoa aquele que aprende a praticar o respeito, a empatia e o cuidado com a vida coletiva.",
        "Porque as leis civis de cidadania só são conferidas aos adultos que concluem o ensino médio superior.",
        "Porque o indivíduo necessita de autorização militar para circular pelas ruas de cidades industriais.",
        "Porque a humanidade de um sujeito depende da quantidade de cabeças de gado registradas em seu nome.",
        "B",
        "A condição de 'pessoa' (muntu) é uma conquista ética: quem age com crueldade ou despreza os laços comunitários empobrece sua própria humanidade, desumanizando-se no convívio."
    ))

    questoes_brutas.append((
        24, "EM13CHS102", "intermediario",
        "Como a Comissão da Verdade e Reconciliação (CVR) da África do Sul lidou com o dilema entre a impunidade geral e o revanchismo punitivista?",
        "Promulgando uma anistia incondicional e proibindo a imprensa de publicar notícias sobre o período do apartheid.",
        "Criando um procedimento singular de justiça restaurativa no qual a anistia individual exigia a confissão pública minuciosa dos crimes perante as vítimas, priorizando a reconciliação e a verdade.",
        "Condenando todos os policiais e ministros do regime anterior à pena capital em tribunais de exceção militar.",
        "Determinando que a população branca deveria abandonar o país em navios de transporte de passageiros.",
        "Transferindo a administração da justiça penal sul-africana para comissões nomeadas por governos estrangeiros.",
        "B",
        "A CVR recusou tanto a anistia cega (que enterra os crimes sem memória) quanto o punitivismo cego de Talião (que alimentaria nova guerra civil), fundando na verdade o caminho da cura nacional."
    ))

    questoes_brutas.append((
        25, "EM13CHS501", "intermediario",
        "Qual é a diferença estrutural no tratamento conferido à 'Vítima' na Justiça Retributiva tradicional em relação à Justiça Restaurativa de matriz Ubuntu?",
        "Na justiça retributiva a vítima decide a sentença final do juiz, enquanto na restaurativa ela é silenciada.",
        "Na justiça retributiva a vítima é reduzida a mera testemunha da acusação estatal, enquanto na restaurativa sua dor é o centro do processo, recebendo escuta atenta e reparação concreta de sua dignidade.",
        "Na justiça retributiva a vítima recebe indenizações milionárias imediatas pagas pelos fundos de pensão pública.",
        "Na justiça restaurativa a vítima é obrigada a realizar trabalhos manuais em benefício da família do ofensor.",
        "Na justiça retributiva a vítima escolhe qual presídio deverá custodiar o condenado pelo delito.",
        "B",
        "O modelo retributivo confisca o conflito: o Estado assume o papel de ofendido e a vítima real é marginalizada; a justiça restaurativa devolve o protagonismo à vítima e à sua cicatrização."
    ))

    questoes_brutas.append((
        26, "EM13CHS503", "intermediario",
        "Por que o modelo de Justiça Restaurativa exige que o 'Ofensor' participe ativamente do processo em vez de adotar postura meramente defensiva?",
        "Para que ele possa negociar descontos em multas contratuais utilizando serviços de advogados comerciais.",
        "Para que ele tome consciência direta do sofrimento que causou, assuma a responsabilidade moral por suas condutas e participe ativamente da construção do plano de reparação para com a vítima.",
        "Para que ele seja submetido a humilhações físicas perante os guardas das muralhas carcerárias.",
        "Para que ele assine documentos renunciando à propriedade de suas ferramentas agrícolas no campo.",
        "Para que ele cumpra plantões de vigilância noturna em prédios públicos municipais da capital.",
        "B",
        "O ofensor não é simplesmente punido passivamente como um objeto do Estado; ele é chamado a responder como sujeito ético, encarando o impacto de seus atos e trabalhando para recompor o dano."
    ))

    questoes_brutas.append((
        27, "EM13CHS102", "intermediario",
        "Em Sem Perdão Não Há Futuro, Desmond Tutu formula a advertência: 'Sem perdão não há futuro'. Qual é o fundamento filosófico dessa tese no contexto de sociedades fraturadas por violências históricas?",
        "A ideia de que as vítimas de violência devem esquecer os fatos do passado para facilitar o trânsito comercial de produtos nas feiras.",
        "A convicção de que manter aceso o desejo de vingança retributiva perpetua o ódio e a destruição recíproca, ao passo que o perdão corajoso liberta a comunidade para construir um horizonte coletivo compartilhado.",
        "A certeza de que as ordens religiosas devem administrar todos os hospitais e asilos da federação.",
        "A defesa de que as leis penais devem prever o banimento territorial de quem professar religiões tradicionais.",
        "O argumento de que os acordos de paz só têm validade se forem assinados embaixadas de nações ricas.",
        "B",
        "Perdoar não é esquecimento frouxo nem fraqueza: é um ato político sublime que desativa a espiral da retaliação infinita, impedindo que os erros do passado devorem as gerações vindouras."
    ))

    questoes_brutas.append((
        28, "EM13CHS501", "intermediario",
        "Como a tríade cósmica do Ubuntu (antepassados, vivos e gerações futuras) oferece subsídios para o debate contemporâneo sobre Sustentabilidade e Ecologia Política?",
        "Incentivando o desmatamento acelerado para que as florestas sejam substituídas por estacionamentos de concreto.",
        "Mostrando que o meio ambiente não é mercadoria explorável ao bel-prazer de indivíduos particulares, mas um patrimônio sagrado recebido dos ancestrais que deve ser conservado para as gerações que hão de vir.",
        "Defendendo que as indústrias químicas devam despejar seus efluentes em rios de grande curso de água.",
        "Afirmando que a água potável deve ser vendida em leilões internacionais pelo preço das ações em bolsa.",
        "Provando que as mudanças de temperatura global dependem exclusivamente do ciclo das marés oceânicas.",
        "B",
        "O compromisso com as gerações futuras e com a terra viva estabelece um limite ético intransponível contra a predação capitalista, dialogando de perto com as éticas ecológicas mais avançadas."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Ao estabelecer diálogo com a criminologia crítica de Nils Christie, como a justiça restaurativa fundamentada no Ubuntu critica o sistema penal moderno?",
        "Afirmando que as prisões estatais consomem pouca energia elétrica nas celas de convivência coletiva.",
        "Denunciando que o Estado ocidental desapropriou o conflito das pessoas concretas envolvidas, transformando a dor humana em processo burocrático estéril que encarcera em massa sem promover cura nem segurança.",
        "Defendendo que as sentenças condenatórias de tribunais municipais deveriam ser cantadas em versos de teatro lírico.",
        "Propondo que os juízes criminais devam acumular funções de prefeitos civis nas cidades do interior.",
        "Comprovando que o uso de uniformes listrados em presídios melhora o comportamento dos internos.",
        "B",
        "Nils Christie cunhou a tese de que o Estado 'roubou os conflitos': o Ubuntu resgata a soberania da comunidade, permitindo que as pessoas reais enfrentem sua ferida e construam a pacificação."
    ))

    questoes_brutas.append((
        30, "EM13CHS502", "intermediario",
        "De que modo a filosofia do Ubuntu dialoga com o pensamento de lideranças indígenas brasileiras contemporâneas, como Ailton Krenak e Davi Kopenawa?",
        "Defendendo a expansão do garimpo mecanizado em terras demarcadas para acelerar o progresso econômico nacional.",
        "Compartilhando a convicção de que a vida humana é inseparável da teia viva da natureza e das forças cósmicas, repudiando a ilusão moderna de que o ser humano pode viver isolado agredindo o planeta.",
        "Afirmando que os povos tradicionais devem abandonar suas aldeias para trabalhar em fábricas automobilísticas urbanas.",
        "Sustentando que as florestas tropicais produzem excesso de umidade prejudicial à agricultura intensiva.",
        "Determinando que os cantos ancestrais de cura devem ser submetidos à aprovação de academias de letras da capital.",
        "B",
        "Tanto o Ubuntu banta quanto o bem viver indígena reconhecem a interdependência radical entre humanidade e cosmos: destruir rios e florestas é destruir a nós mesmos."
    ))

    questoes_brutas.append((
        31, "EM13CHS503", "intermediario",
        "Na análise de Kwasi Wiredu e Mogobe Ramose, qual é o papel do 'Consenso' nas práticas de governança comunitária africana tradicional?",
        "Impor as decisões da maioria simples através de votações rápidas que silenciam por completo os grupos vencidos.",
        "Buscar a deliberação paciente e o entendimento compartilhado na tomada de decisões coletivas, assegurando que todas as vozes sejam ouvidas para preservar a harmonia da comunidade.",
        "Delegar todo o poder legislativo a um general armado que comande as guarnições militares do território.",
        "Submeter os projetos de lei civil a sorteios realizados com sementes de árvores raras em tigelas de barro.",
        "Proibir que os anciãos e as mulheres participem de assembleias deliberativas nas vilas rurais.",
        "B",
        "Ao contrário da democracia majoritária ocidental (que frequentemente cria minorias ressentidas), a deliberação tradicional africana busca o consenso participativo para manter o tecido social intacto."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Como a distinção entre Ubuntu e individualismo liberal se expressa no tratamento da propriedade e dos recursos fundamentais para a sobrevivência?",
        "O individualismo liberal defende que toda a terra deve ser estatizada por comitês de planejamento central burocrático.",
        "Enquanto o individualismo liberal concebe a propriedade privada absoluta como direito pré-social inegociável, o Ubuntu submete o uso dos bens à dignidade coletiva e ao sustento de todos os membros do grupo.",
        "O Ubuntu proíbe que qualquer membro da comunidade possua roupas pessoais ou ferramentas de trabalho próprias.",
        "O individualismo liberal exige que as heranças financeiras sejam integralmente doadas a orfanatos públicos municipais.",
        "O Ubuntu estabelece que os preços de alimentos de feiras livres devem ser cotados em bolsas de mercadorias estrangeiras.",
        "B",
        "No horizonte comunitário do Ubuntu, os recursos materiais têm função fiduciária: ninguém tem o direito moral de acumular em excesso enquanto seus vizinhos padecem de privação básica."
    ))

    questoes_brutas.append((
        33, "EM13CHS501", "intermediario",
        "Por que, segundo Mogobe Ramose, a transição sul-africana liderada por Nelson Mandela e Desmond Tutu foi considerada um feito ético sem precedentes mundiais?",
        "Porque ela conseguiu quadruplicar as exportações de ouro da África do Sul em menos de doze meses civis.",
        "Porque evitou um banho de sangue e uma guerra civil genocida que muitos julgavam inevitável, refundando a convivência nacional sobre os pilares da dignidade humana compartilhada e da justiça restaurativa.",
        "Porque ela aboliu o uso de veículos a motor em todas as avenidas centrais da cidade do Cabo.",
        "Porque as forças militares do regime supremacista foram integradas à frota naval de países vizinhos sem treinamento.",
        "Porque ela estabeleceu que os tribunais criminais deveriam funcionar apenas aos finais de semana festivos.",
        "B",
        "O mundo aguardava um massacre de vingança; a África do Sul respondeu com o Ubuntu, provando que a dignidade e a sabedoria restaurativa têm força para transformar o ódio em reconciliação."
    ))

    questoes_brutas.append((
        34, "EM13CHS502", "intermediario",
        "Em relação à dimensão do tempo e da história, como a filosofia tradicional africana rompe com a concepção linear com finalidade pré-fixada ocidental?",
        "Defendendo que as horas do relógio devem ser contadas de trás para frente em edifícios públicos.",
        "Compreendendo o tempo como um fluxo rítmico integrado à natureza e às gerações comunitárias, onde o passado ancestral fertiliza ativamente o presente ético dos vivos.",
        "Afirmando que o tempo cronológico foi inventado por navegadores da frota mercante da cidade de Veneza.",
        "Sustentando que a história humana terminará em uma data precisa fixada pelo alinhamento dos planetas.",
        "Determinando que os acontecimentos históricos só adquirem importância quando registrados em livros escolares impressos.",
        "B",
        "O tempo banta não é uma flecha mecânica em direção a um progresso abstrato; é presença viva dos laços entre os que já foram e os que agem hoje para manter o cosmos em harmonia."
    ))

    questoes_brutas.append((
        35, "EM13CHS503", "intermediario",
        "Qual é a relação fundamental entre a aplicação da Lei 10.639/03 no ensino de filosofia e a superação do racismo estrutural nas escolas brasileiras?",
        "A garantia de que os estudantes aprendam a desenhar mapas cartográficos de desertos africanos.",
        "O reconhecimento acadêmico da igualdade humana essencial e da riqueza conceitual do pensamento africano, combatendo a inferiorização cultural de estudantes negros e valorizando sua ancestralidade.",
        "A determinação de que as provas finais de vestibular devam cobrar exclusivamente vocábulos de línguas estrangeiras.",
        "A exigência de que os diretores escolares participem de campeonatos anuais de atletismo esportivo.",
        "A obrigação de fechar as bibliotecas que não possuam romances publicados no século XIX.",
        "B",
        "A Lei 10.639/03 opera como justiça curricular: ao apresentar a filosofia africana com rigor e beleza, desconstrói estereótipos colonialistas e forma cidadãos comprometidos com a equidade racial."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Como a antropologia banta define a figura do 'Inimigo' em comparação com a lógica da aniquilação bélica ocidental?",
        "O inimigo é considerado uma fera selvagem incorrigível que deve ser exterminada fisicamente sem julgamento.",
        "O inimigo é compreendido como um ser humano desorientado e doente de humanidade, cuja conduta feriu a teia comunitária e que necessita de reabilitação e reencontro com o próprio Ubuntu.",
        "O inimigo é alguém que deve ter todas as suas terras confiscadas para o pagamento de dívidas tributárias.",
        "O inimigo é um viajante que perdeu seus documentos de identificação civil durante viagens de trem.",
        "O inimigo é uma pessoa que recusa o trabalho voluntário em obras públicas de canalização de esgoto.",
        "B",
        "No horizonte do Ubuntu, a monstruosidade do ato não anula a humanidade essencial de quem o praticou: o objetivo ético superior não é vingar-se matando, mas resgatar e curar o humano perdido."
    ))

    questoes_brutas.append((
        37, "EM13CHS501", "intermediario",
        "Ao examinar a prática dos Círculos Restaurativos em Varas da Infância e Juventude no Brasil, qual elemento comprova sua eficácia na prevenção da reincidência de infrações juvenis?",
        "A aplicação de multas pecuniárias aos pais dos menores que cometeram faltas leves.",
        "A oportunidade de o jovem ouvir o relato genuíno da vítima, compreender o impacto real de suas atitudes e assumir um compromisso voluntário de reparação diante de sua comunidade.",
        "A transferência dos jovens para centros de internação disciplinar localizados em ilhas distantes.",
        "A proibição de que os adolescentes assistam a programas de televisão durante os dias de semana.",
        "O cancelamento do título de eleitor de todos os parentes em primeiro grau do adolescente infrator.",
        "B",
        "O diálogo restaurativo produz uma transformação subjetiva profunda: o jovem deixa de encarar a infração como um jogo contra a polícia e percebe a dor de outro ser humano, assumindo responsabilidade."
    ))

    questoes_brutas.append((
        38, "EM13CHS502", "intermediario",
        "Qual é o significado de 'Cura Comunitária' (healing) na teologia pública e na filosofia moral de Desmond Tutu?",
        "A distribuição gratuita de remédios e antibióticos fabricados em laboratórios farmacêuticos europeus.",
        "O processo de cicatrização emocional, moral e relacional de uma sociedade traumatizada pela opressão, que só se viabiliza pelo conhecimento transparente da verdade e pelo acolhimento das dores históricas.",
        "A realização de cirurgias médicas em hospitais de campanha montados nas capitais provinciais.",
        "A pulverização de produtos químicos sobre lavouras de trigo para combater pragas de gafanhotos.",
        "A vacinação compulsória de crianças matriculadas em colégios confessionais da Inglaterra.",
        "B",
        "A cura comunitária é a restauração espiritual e política do corpo social: sem a luz da verdade sobre os massacres do passado, a ferida coletiva permanece purulenta sob a carcaça da aparente paz."
    ))

    questoes_brutas.append((
        39, "EM13CHS503", "intermediario",
        "Por que as chamadas 'Leis do Passe' (Pass Laws) e o 'Group Areas Act' do regime do Apartheid constituíram a antítese mais brutal da ética do Ubuntu?",
        "Porque essas leis exigiam que os motoristas de caminhão fizessem manutenção periódica nos freios dos veículos.",
        "Porque foram dispositivos jurídicos opressores criados expressamente para segregar, fragmentar e despedaçar a convivência comunitária humana com base na cor da pele, proibindo a solidariedade e desumanizando as pessoas.",
        "Porque elas aumentavam os impostos cobrados sobre as exportações de maçãs frescas para cidades litorâneas.",
        "Porque elas obrigavam os moradores urbanos a pintarem seus portões residenciais com tinta escura.",
        "Porque elas proibiam a circulação de trens de passageiros durante os meses de estiagem no campo.",
        "B",
        "O apartheid foi a tentativa sistemática de destruir a teia humana relacional através de barreiras policiais e segregação racial forçada, encarnando o oposto absoluto da fraternidade do Ubuntu."
    ))

    questoes_brutas.append((
        40, "EM13CHS101", "intermediario",
        "Como a tradição filosófica africana avalia o 'Individualismo Atomista' presente em teorias de contrato social como as de Thomas Hobbes e John Locke?",
        "Como o modelo mais perfeito e acabado de convivência pacífica e florescimento dos potenciais humanos.",
        "Como uma ficção teórica reducionista que isola o indivíduo de seus laços orgânicos de solidariedade, imaginando falsamente que o homem pode existir de modo pleno fora e antes da comunidade viva que o acolhe.",
        "Como uma proposta científica comprovada pelos experimentos de anatomia e química biológica.",
        "Como um regulamento mercantil adequado para o comércio de especiarias entre portos fluviais.",
        "Como uma doutrina teológica que confirma as profecias bíblicas sobre a salvação universal de almas.",
        "B",
        "Para a filosofia banta, ninguém nasce em um vácuo isolado como um átomo independente: nascemos no seio de uma comunidade que nos ampara; supor o indivíduo sem a comunidade é uma ilusão metafísica."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a seguinte reflexão de Mogobe Ramose em African Philosophy Through Ubuntu: 'A pergunta sobre se os africanos podem filosofar nunca foi uma questão genuína sobre o pensamento; foi sempre uma estratégia de desumanização colonial para legitimar o direito de conquista e escravização.' De que maneira essa formulação desnuda a cumplicidade entre a teoria eurocêntrica do saber e a violência colonial?",
        "Provando que as academias científicas de Londres e Paris não mantinham relações de correspondência por cartas.",
        "Evidenciando que o monopólio da razão arrogado pelo Ocidente operou como instrumento de desqualificação da dignidade humana dos colonizados: ao declarar o africano incapaz de razão abstrata, a Europa legitimou moralmente a pilhagem de suas terras e o comércio de escravizados sob o pretexto de uma missão civilizadora.",
        "Demonstrando que os marinheiros portugueses desconheciam as técnicas de navegação astronômica através de bússolas magnéticas.",
        "Afirmando que os filósofos iluministas rejeitavam categoricamente o ensino de línguas latinas nas universidades imperiais.",
        "Sustentando que as leis de navegação de rios africanos foram criadas por comerciantes holandeses da Companhia das Índias.",
        "B",
        "**Etapa 1:** Desvelar a tese de Ramose sobre a natureza política do 'mito da racionalidade': negar a capacidade de pensar ao colonizado é retirar-lhe a própria condição de sujeito de direitos.\n**Etapa 2:** Concluir com a crítica descolonial: o saber eurocêntrico e a dominação colonial são duas faces da mesma moeda; a filosofia africana afirma sua dignidade metodológica ao resgatar a legitimidade autônoma de suas categorias éticas."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em Sem Perdão Não Há Futuro, Desmond Tutu descreve as audiências da Comissão da Verdade e Reconciliação (CVR): 'As pessoas choravam abertamente; algo sagrado estava acontecendo ali. Quando o perpetrador finalmente confessava a verdade perante a mãe do jovem assassinado, uma ponte invisível de humanidade começava a ser reconstruída.' Como essa dinâmica ilustra a superioridade da justiça restaurativa sobre a justiça punitiva tradicional?",
        "Fazendo com que os réus de crimes penais assinassem notas promissórias para o pagamento de fianças bancárias na capital.",
        "Demonstrando que, ao passo que a pena prisional isolada apenas segrega o criminoso em uma cela sem tocar no trauma da família ou na verdade dos fatos, o encontro restaurativo abre espaço para a dor da vítima ser ouvida e reconhecida, desfazendo a negação e possibilitando a cicatrização do tecido social ferido.",
        "Obrigando os familiares das vítimas a realizarem reformas nas paredes externas dos fóruns municipais.",
        "Provando que os juízes de tribunais constitucionais deveriam dispensar o uso de capas pretas de tecido em sessões públicas.",
        "Determinando que os jornais da oposição fossem distribuídos gratuitamente nas entradas das estações de trem.",
        "B",
        "**Etapa 1:** Contrastar a frieza burocrática da pena carcerária com a profundidade do encontro restaurativo da verdade.\n**Etapa 2:** Evidenciar o poder do Ubuntu na reconciliação: a verdade confessa diante do sofrimento compartilhado tem a força de regenerar a dignidade tanto da vítima violada quanto do agressor desumanizado por sua violência."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Considere o contraste na concepção sobre o ser formulado pelo filósofo queniano John Mbiti: 'Eu sou porque nós somos; e, visto que nós somos, logo eu sou'. De que maneira essa inversão do Cogito cartesiano desestabiliza a tradição da ética normativa moderna fundada no indivíduo autônomo kantiano?",
        "Negando que os matemáticos franceses soubessem resolver equações de segundo grau com coeficientes fracionários.",
        "Mostrando que, enquanto Kant fundamenta a moralidade no dever da razão pura de um sujeito desincorporado e autossuficiente, a ética do Ubuntu compreende que a obrigação moral não decorre de imperativos abstratos da mente solitária, mas da responsabilidade afetiva e concreta que nasce da interdependência orgânica com a comunidade viva.",
        "Defendendo que os comerciantes urbanos deveriam trocar todas as moedas de prata por tecidos de algodão cru nas feiras.",
        "Afirmando que as regras gramaticais das línguas europeias impedem a formulação de preceitos de solidariedade fraterna.",
        "Provando que as academias militares prussianas utilizavam manuais de instrução copiados de legiões romanas.",
        "B",
        "**Etapa 1:** Analisar a divergência de ponto de partida: a razão legisladora solitária de Kant versus a comunidade viva relacional de Mbiti e Ramose.\n**Etapa 2:** Concluir com a emancipação ética: a dignidade humana no Ubuntu não é um axioma racional abstrato em si mesmo; ela é uma práxis cotidiana de cuidado, onde eu só cuido de mim cuidando da comunidade que me permite ser."
    ))

    questoes_brutas.append((
        44, "EM13CHS502", "dificil",
        "Em sua obra sobre o Ubuntu, Mogobe Ramose analisa a sentença 'Umuntu ngumuntu ngabantu' e adverte que a perda do Ubuntu acarreta a desumanização profunda daquele que pratica a violência. Qual é a fundamentação lógica dessa tese?",
        "A ideia de que quem comete crimes perde o direito de utilizar transporte coletivo em avenidas municipais.",
        "A tese de que, como a humanidade não é uma posse individual isolada mas um produto da rede de reciprocidade, quem viola a dignidade de outrem agride a própria matriz que sustenta a sua própria humanidade, rebaixando a si mesmo à condição de destruidor da força vital coletiva.",
        "O argumento de que os infratores de trânsito perdem a autorização para conduzir cavalos e carroças em vias públicas.",
        "A premissa de que os tratados de comércio marítimo deixam de vigorar quando ocorrem tempestades no oceano.",
        "A convicção de que os estudantes que reprovam em exames escolares devem trabalhar em oficinas de tecelagem manual.",
        "B",
        "**Etapa 1:** Compreender a concepção relacional sobre a condição humana: o ser humano só existe na relação com o outro.\n**Etapa 2:** Explicitar a desumanização do opressor: ao torturar ou oprimir o irmão, o carrasco amputa a fonte de sua própria integridade ética; Desmond Tutu resume: a liberdade do opressor é uma farsa, pois ele é prisioneiro do próprio monstro que criou."
    ))

    questoes_brutas.append((
        45, "EM13CHS503", "dificil",
        "Ao examinar a transição pacífica da África do Sul, analistas ocidentais previam um colapso social em meio a confrontos de vingança sangrenta após 46 anos de violência do Apartheid. De que maneira a liderança moral de Nelson Mandela e Desmond Tutu, nutrida pelo Ubuntu, neutralizou a lógica da vingança histórica?",
        "Proibindo os cidadãos sul-africanos de assistirem a partidas de futebol em estádios desportivos da federação.",
        "Demonstrando à maioria negra oprimida que responder à barbárie com os métodos do carrasco perpetuaria o sofrimento e a desolação em solo nacional; ao escolher a justiça restaurativa e o perdão como armas de reconstrução, eles transformaram a dor em pacto de dignidade cidadã inclusiva.",
        "Vendendo os estoques de minério de carvão para governos estrangeiros a fim de comprar fuzis modernos.",
        "Exigindo que os ministros do governo deposto prestassem juramentos de vassalagem em latim clássico.",
        "Decretando que todos os processos cíveis pendentes nos tribunais deveriam ser queimados em fogueiras públicas.",
        "B",
        "**Etapa 1:** Interpretar o perigo da vingança reativa após décadas de opressão estruturada do apartheid.\n**Etapa 2:** Evidenciar o triunfo ético do Ubuntu: Mandela e Tutu lideraram a reconciliação demonstrando que destruir os brancos não tornaria os negros livres; a verdadeira liberdade exigia libertar ambos do inferno da segregação em uma pátria arco-íris compartilhada."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "No campo da Filosofia do Direito, de que modo a oposição entre Justiça Retributiva e Justiça Restaurativa desmonta o dogma da infalibilidade e da suficiência da pena de prisão estatal?",
        "Mostrando que a construção de celas penitenciárias consome cimento que deveria ser usado em hospitais infantis.",
        "Evidenciando que o aprisionamento retributivo moderno opera como uma vingança burocrática institucionalizada que isola o condenado em condições degradantes sem reparar a dor da vítima nem conter a criminalidade, ao passo que a justiça restaurativa produz responsabilidade pessoal real e reconciliação duradoura.",
        "Afirmando que os carcereiros de presídios prussianos utilizavam chaves de bronze para abrir portas de ferro fundido.",
        "Provando que as leis processuais foram copiadas integralmente de tratados marítimos de frotas comerciais britânicas.",
        "Sustentando que os julgamentos de conflitos de terras rurais devem ser decididos por disputas de corrida de revezamento.",
        "B",
        "**Etapa 1:** Desconstruir a ilusão da pena carcerária como solução para o delito: ela gera estigma e reproduz a violência sem acolher a vítima.\n**Etapa 2:** Concluir com a potência restaurativa do Ubuntu: o delito não é apenas a quebra de um artigo de lei frio; é o rompimento de relações humanas vivas que demanda restauração, verdade e reintegração comunitária."
    ))

    questoes_brutas.append((
        47, "EM13CHS501", "dificil",
        "Considere a ecologia relacional da filosofia de Mogobe Ramose, que define a comunidade como uma tríade inseparável de ancestrais, vivos e gerações futuras. Como essa cosmovisão filosófica desafia o modelo de desenvolvimento predatório do capitalismo globalizado contemporâneo?",
        "Negando que os navios mercantes a vapor consigam transportar cargas pesadas através de canais estreitos de navegação.",
        "Denunciando que a mercantilização desenfreada da natureza e a exaustão dos recursos naturais tratam a Terra como mercadoria descartável para o lucro imediato do indivíduo burguês, rompendo o pacto sagrado de preservação com a ancestralidade e sabotando a existência biológica e moral das gerações vindouras.",
        "Afirmando que as empresas mineradoras deveriam utilizar pás de ferro forjado em substituição a tratores mecânicos.",
        "Determinando que os bancos centrais devam emitir cédulas de papel-moeda decoradas exclusivamente com desenhos botânicos.",
        "Defendendo que as pesquisas meteorológicas sobre correntes de ar devem ser conduzidas por oficiais de cavalaria militar.",
        "B",
        "**Etapa 1:** Contrastar a temporalidade imediata e predatória do lucro com a responsabilidade trina e intergeracional do Ubuntu.\n**Etapa 2:** Concluir com a alternativa emancipatória: a natureza não é coisa morta sem valor; ela é a morada comum que liga os que nos geraram àqueles que nos sucederão, tornando a proteção ambiental um dever ético e comunitário inegociável."
    ))

    questoes_brutas.append((
        48, "EM13CHS502", "dificil",
        "Ao articular o princípio do Ubuntu com as práticas de mediação e círculos restaurativos em conflitos escolares no Brasil, qual transformação estrutural na cultura pedagógica é almejada?",
        "A substituição das aulas presenciais de biologia por treinamentos em ginástica olímpica preparatória.",
        "A superação da pedagogia punitiva tradicional (suspensões, advertências e expulsões que rotulam e excluem o estudante) em favor de uma cultura do diálogo e da responsabilidade ativa, onde o erro é encarado como oportunidade educativa de reparação de danos e amadurecimento comunitário coletivo.",
        "A contratação de seguranças armados para patrulharem os corredores e salas de aula das escolas municipais.",
        "A obrigatoriedade de aplicar provas discursivas de redação todas as sextas-feiras antes da saída das turmas.",
        "A proibição de que os grêmios estudantis organizem festivais de música ou campeonatos desportivos amadores.",
        "B",
        "**Etapa 1:** Analisar a insuficiência da punição punitiva na escola: advertências e suspensões apenas reforçam a exclusão e o ódio institucional do aluno.\n**Etapa 2:** Evidenciar o impacto pedagógico do Ubuntu: ao reunir agressor e vítima para dialogar e construir acordos reais de reparação, a comunidade escolar educa para a alteridade e constrói um ambiente de convivência respeitosa e solidária."
    ))

    questoes_brutas.append((
        49, "EM13CHS503", "dificil",
        "No clássico estudo sobre os Bancos Comunitários de Desenvolvimento e o Banco Palmas citado no e-book, como a criação de moedas sociais locais e crédito produtivo baseado na confiança territorial materializa a ética relacional africana na economia contemporânea?",
        "Comprovando que as moedas de papel tradicional deveriam ser substituídas por lingotes de ouro guardados em caixas-fortes.",
        "Provando que a riqueza autêntica não emana da acumulação solitária ou da especulação financeira egoísta, mas da densidade das relações humanas de solidariedade, onde a confiança mútua e a circulação comunitária dos recursos garantem a dignidade material de todos os moradores periféricos.",
        "Afirmando que os comerciantes de periferia devem cobrar juros bancários exorbitantes para enriquecerem rapidamente.",
        "Defendendo que as compras de mantimentos em padarias de bairro devam ser pagas por meio de transferências em dólar.",
        "Determinando que os governos estaduais devam fechar as pequenas feiras de artesanato para abrir grandes hipermercados.",
        "B",
        "**Etapa 1:** Desmistificar a lógica financeira tradicional que exclui as classes populares por falta de garantias patrimoniais individuais.\n**Etapa 2:** Concluir com a lição do Ubuntu na economia solidária: o aval no Banco Palmas não é uma hipoteca, é a palavra do vizinho; o crédito é aposta na força produtiva comum, gerando soberania e dignidade compartilhada no território."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "Em Para a Genealogia da Filosofia Africana, pensadores contemporâneos advertem contra o duplo perigo de interpretar as tradições africanas: de um lado, o etnofilosofismo romântico ingênuo; de outro, o eurocentrismo acadêmico preconceituoso. Como a obra de Mogobe Ramose navega entre esses dois extremos?",
        "Negando a importância da linguagem e dos provérbios tradicionais nas deliberações de assembleias públicas.",
        "Recusando tanto o preconceito eurocêntrico que nega racionalidade ao pensamento banta quanto a idealização romântica ingênua, demonstrando com rigor analítico, conceitual e crítico que a sabedoria tradicional do Ubuntu possui arquitetura filosófica, categorias sobre a existência e rigor ético próprios capazes de dialogar com os grandes debates contemporâneos.",
        "Defendendo que todas as universidades africanas deveriam fechar seus cursos de graduação em ciências humanas.",
        "Sustentando que a filosofia só pode ser expressa através de fórmulas de lógica simbólica matemática contemporânea.",
        "Afirmando que os filósofos africanos devem adotar integralmente as regras do método empírico de Francis Bacon.",
        "B",
        "**Etapa 1:** Identificar os perigos teóricos: a redução folclórica (etnofilosofia) e a negação colonial da capacidade de pensar (eurocentrismo).\n**Etapa 2:** Explicitar a lucidez de Ramose: o Ubuntu é sistematizado como filosofia rigorosa e viva, fornecendo instrumentos teóricos precisos para desconstruir o solipsismo ocidental sem cair em sentimentalismo ingênuo."
    ))

    questoes_brutas.append((
        51, "EM13CHS102", "dificil",
        "De que maneira a reflexão de Kwasi Wiredu sobre a 'Democracia por Consenso' nas sociedades tradicionais africanas desfaz a ilusão ocidental de que a regra da maioria simples é o único método legítimo de deliberação democrática?",
        "Mostrando que a contagem de votos em urnas eleitorais consome tempo excessivo dos funcionários públicos municipais.",
        "Evidenciando que a regra da maioria simples frequentemente converte a democracia em uma tirania institucionalizada de maiorias conjunturais sobre minorias marginalizadas, ao passo que a busca paciente pelo consenso tradicional assegura que todas as partes sejam escutadas e integradas na decisão governativa final.",
        "Afirmando que os parlamentos nacionais deveriam ser compostos apenas por cidadãos com títulos honoríficos de nobreza.",
        "Provando que as constituições republicanas deixam de vigorar quando ocorrem períodos de seca prolongada no interior.",
        "Determinando que os cidadãos que perdem eleições civis devem prestar serviços braçais na construção de estradas.",
        "B",
        "**Etapa 1:** Analisar a limitação estrutural da democracia majoritária: 51% podem oprimir e esmagar 49%, gerando exclusão e ressentimento político crônico.\n**Etapa 2:** Concluir com a lição do consenso comunitário africano: a legitimidade da decisão reside na capacidade de compor divergências no diálogo respeitoso, preservando a unidade harmônica da coletividade política."
    ))

    questoes_brutas.append((
        52, "EM13CHS501", "dificil",
        "Ao examinar a relação entre a dignidade humana no Ubuntu e a concepção moderna de Direitos Humanos fundamentais, qual contribuição decisiva o pensamento africano oferece para descolonizar o conceito de direitos da pessoa?",
        "Propondo a revogação de todos os tratados internacionais de proteção aos direitos civis e políticos aprovados na ONU.",
        "Demonstrando que os direitos do indivíduo não podem ser concebidos como escudos de egoísmo isolado contra a sociedade, mas como faculdades indissociáveis dos deveres correlatos de solidariedade, cuidado e responsabilidade mútua para com a comunidade que torna o ser humano possível.",
        "Defendendo que apenas as nações possuidoras de frotas mercantes a vapor têm autoridade para fiscalizar os direitos fundamentais.",
        "Sustentando que os direitos humanos foram inventados exclusivamente para proteger os contratos comerciais entre companhias privadas.",
        "Provando que as cortes de justiça internacionais deveriam aplicar sentenças formuladas na língua alemã do século XVIII.",
        "B",
        "**Etapa 1:** Desvelar a limitação da visão liberal de direitos: centrada no indivíduo abstrato contra o Estado, esquecendo a dimensão social e fraterna.\n**Etapa 2:** Concluir com o aporte do Ubuntu: os direitos humanos ganham densidade plena quando articulados aos deveres de responsabilidade comunitária; a verdadeira dignidade floresce quando o direito de um é compromisso solidário de todos."
    ))

    questoes_brutas.append((
        53, "EM13CHS502", "dificil",
        "Em O Ensino de Filosofia e a Lei 10.639, o filósofo Renato Noguera adverte contra o risco de 'epistemicídio' curricular na educação brasileira. Como a inclusão do pensamento de Ramose e Tutu desativa as armadilhas do epistemicídio nas salas de aula de Ensino Médio?",
        "Obrigando as escolas públicas a realizarem viagens semanais de excursão aos portos marítimos litorâneos.",
        "Substituindo o apagamento histórico e a subalternização sistemática das culturas africanas pela apresentação metódica de seus conceitos, sistemas éticos e autores seminais, formando uma juventude capaz de reconhecer a pluralidade epistêmica do planeta e combater o racismo institucional.",
        "Determinando que os livros didáticos de filosofia devam ser confeccionados apenas com capas de tecido bordado manual.",
        "Exigindo que os exames vestibulares cobrem exclusivamente datas comemorativas de batalhas militares do século XIX.",
        "Proibindo os professores de utilizarem quadros de giz ou lousas digitais durante as explicações de temas teóricos.",
        "B",
        "**Etapa 1:** Compreender o conceito de epistemicídio: o assassinato simbólico e o apagamento forçado da capacidade de produção de conhecimento dos povos oprimidos.\n**Etapa 2:** Concluir com o papel reparador da Lei 10.639/03: ao ensinar o Ubuntu e Ramose com rigor e centralidade, a escola devolve à juventude a riqueza do pensamento negro, afirmando a igualdade no valor dos saberes da humanidade."
    ))

    questoes_brutas.append((
        54, "EM13CHS503", "dificil",
        "Considere a prática da CVR sul-africana em confrontar torturadores e oficiais do Apartheid com o sofrimento das famílias de militantes assassinados. Por que a comissão considerava que o perdão não poderia ser concedido sem a prévia confissão pública circunstanciada da verdade integral?",
        "Porque o governo precisava registrar os nomes dos oficiais em livros contábeis de despesas militares.",
        "Porque sem a verdade integral o perdão converte-se em mera farsa ou amnésia forçada que protege a impunidade dos criminosos e revitima os ofendidos; a verdade plena perante a comunidade é a condição indispensável para a purificação da dor e o restabelecimento da justiça real.",
        "Porque as leis comerciais exigiam que as testemunhas apresentassem recibos fiscais de todas as transações realizadas no período.",
        "Porque os magistrados dos tribunais de apelação necessitavam de assinaturas com selos de chumbo em todos os autos processuais.",
        "Porque a anistia só era outorgada aos indivíduos que comprovassem não ter parentesco com generais das forças de fronteira.",
        "B",
        "**Etapa 1:** Desmistificar a falsa oposição entre perdão e verdade: o perdão sem verdade é cinismo institucional que consagra a mentira.\n**Etapa 2:** Evidenciar a lucidez de Desmond Tutu: o Ubuntu exige olhar a ferida de frente; o torturador só se liberta de sua culpa monstruosa quando confessa tudo perante a vítima, devolvendo os restos mortais e encarando a humanidade que tentou esmagar."
    ))

    questoes_brutas.append((
        55, "EM13CHS101", "dificil",
        "No diálogo interdisciplinar entre a filosofia africana e a sociologia do direito, qual é o paralelo teórico entre a denúncia de desumanização prisional feita por Angela Davis e a concepção de justiça restaurativa inspirada no Ubuntu?",
        "Ambas as autoras defendem que os presídios femininos deveriam ser construídos nas encostas de regiões montanhosas frias.",
        "Tanto a crítica abolicionista prisional quanto a justiça restaurativa convergem no diagnóstico de que o complexo penitenciário retributivo opera como máquina de dor e estigmatização racial e de classe que não resolve as causas do crime nem acolhe as vítimas, devendo ser superado por alternativas de cuidado comunitário e reparação coletiva.",
        "As duas perspectivas sugerem que os julgamentos de processos criminais deveriam ser transmitidos em emissoras de rádio comunitária.",
        "Ambas sustentam que as penas de reclusão disciplinar deveriam ser cumpridas integralmente em oficinas têxteis de linho.",
        "As duas visões propõem que as leis de compensação civil sejam aplicadas exclusivamente mediante a doação de ferramentas de carpintaria.",
        "B",
        "**Etapa 1:** Mapear a convergência crítica entre o abolicionismo penal de Davis e o modelo restaurativo do Ubuntu.\n**Etapa 2:** Concluir com a alternativa ética: ambas recusam a falácia de que engaiolar pessoas gera segurança; a justiça autêntica exige investir nas causas sociais do conflito, restaurar os laços de confiança e curar o trauma comunitário com dignidade."
    ))

    questoes_brutas.append((
        56, "EM13CHS102", "dificil",
        "Analise a seguinte situação hipotética: um jovem morador de periferia pratica uma agressão física contra um colega em uma festa comunitária. Se o caso for processado sob a ótica estrita da Justiça Retributiva tradicional versus a ótica da Justiça Restaurativa do Ubuntu, quais serão os desfechos estruturais de cada caminho?",
        "Na retributiva ele é obrigado a doar roupas de inverno para orfanatos; na restaurativa ele é imediatamente expulso da cidade.",
        "Na retributiva o Estado assume a acusação, afasta a vítima do diálogo e condena o jovem ao encarceramento juvenil (estigmatizando-o e gerando revolta); na restaurativa reúne-se o círculo com vítima, famílias e mediador, oportunizando o reconhecimento da culpa, o pedido sincero de perdão e a prestação de serviços comunitários pedagógicos que o reintegram.",
        "Na retributiva o jovem escolhe qual advogado do Estado defenderá sua causa em sessão secreta; na restaurativa o caso é arquivado sumariamente.",
        "Na retributiva a polícia municipal confisca todos os bens materiais dos pais do agressor; na restaurativa a vítima deve pagar os custos do processo.",
        "Na retributiva as decisões são homologadas por sorteios em praça pública; na restaurativa o julgamento ocorre sob sigilo de Estado absoluto.",
        "B",
        "**Etapa 1:** Descrever o percurso e as consequências do sistema retributivo punitivo convencional.\n**Etapa 2:** Evidenciar o itinerário restaurativo do Ubuntu: em vez de empurrar o jovem para a engrenagem desumanizadora da marginalidade, a comunidade acolhe o conflito, exige responsabilidade sincera e costura a reparação viva da dignidade das partes."
    ))

    questoes_brutas.append((
        57, "EM13CHS501", "dificil",
        "De que maneira o provérbio banta 'A pessoa se torna pessoa através de outras pessoas' atua como uma barreira ética intransponível contra a manipulação instrumental do outro denunciada por Kant em sua segunda formulação do imperativo categórico?",
        "Proibindo os comerciantes de venderem produtos agrícolas com prazos de validade vencidos nos mercados municipais.",
        "Aprofundando a advertência kantiana de jamais tratar o ser humano como mero meio instrumental: no Ubuntu, utilizar o outro como ferramenta descartável de ganho egoísta é uma impossibilidade moral radical, pois ao destruir ou instrumentalizar o outro eu destruo e rebaixo a própria base relacional que sustenta a minha humanidade.",
        "Defendendo que os contratos de trabalho devem prever pagamentos mensais adiantados em barras de metal precioso.",
        "Exigindo que os tratados de diplomacia internacional sejam chancelados com selos de cera vermelha derretida.",
        "Provando que as academias de oficiais de infantaria devem incluir aulas de retórica e oratória em seus currículos.",
        "B",
        "**Etapa 1:** Confrontar a fórmula kantiana da dignidade (agir para tratar o outro como fim em si) com a concepção relacional do ser no Ubuntu.\n**Etapa 2:** Concluir com a radicalidade do Ubuntu: em Kant a razão do sujeito respeita o outro por obediência formal à lei universal; no Ubuntu o respeito é visceral e orgânico, pois a minha própria existência depende e transborda da existência do irmão que está diante de mim."
    ))

    questoes_brutas.append((
        58, "EM13CHS502", "dificil",
        "Ao examinar a transição do regime racista do Apartheid para a democracia na África do Sul, por que a Comissão da Verdade liderada por Desmond Tutu sustentou a necessidade de desarmar a lógica da inimizade perpétua entre negros e brancos?",
        "Porque o presidente de Klerk abriu as fronteiras para o livre comércio de caminhões pesados de transporte de carga.",
        "Porque, em vez de construir a nova ordem constitucional sobre a liquidação física ou o encarceramento revanchista dos antigos dominadores brancos, o Ubuntu sustentou que a única vitória definitiva sobre a opressão consistia em dissolver a própria categoria do 'inimigo irreconciliável', convertendo os opressores de ontem em concidadãos corresponsáveis pela reconstrução democrática.",
        "Porque as bandeiras nacionais antigas foram guardadas em gavetas de aço nos arquivos da corte suprema.",
        "Porque os soldados das forças armadas foram dispensados do uso de armamentos de fogo em patrulhas de rotina.",
        "Porque os partidos políticos foram obrigados a se fundir em uma única agremiação de centro nas eleições legislativas.",
        "B",
        "**Etapa 1:** Mapear a armadilha clássica das revoluções: substituir o senhor branco pelo senhor negro mantendo a lógica de sangue e inimizade ativa.\n**Etapa 2:** Concluir com a grandeza do Ubuntu: desinventar o inimigo é a revolução suprema; como sentenciava Tutu, se nos vingarmos dos torturadores nós nos tornaremos iguais a eles; a vitória real do oprimido é ensinar ao algoz o significado esquecido de ser verdadeiramente humano."
    ))

    questoes_brutas.append((
        59, "EM13CHS503", "dificil",
        "No debate sobre 'Filosofia e Ancestralidade' presente na tradição acadêmica africana e afro-brasileira, qual é o papel epistêmico da escuta atenta aos mais velhos (os griôs e anciãos comunitários)?",
        "A preservação de superstições ingênuas que impedem os jovens de estudarem matemática e ciências da computação.",
        "O reconhecimento de que a sabedoria não é propriedade de diplomas acadêmicos burocráticos, mas um acervo vivo de memórias históricas, tecnologias de convivência e orientações éticas preservadas pelas linhagens mais experientes, orientando a comunidade para que não repita os erros do passado.",
        "A determinação de que os anciãos devam exercer funções de tesoureiros em cooperativas de plantio de milho híbrido.",
        "A exigência de que os jovens devam memorizar os nomes de todos os monarcas da Europa central do século XVII.",
        "A obrigação de que as consultas aos avós sejam homologadas perante tabeliães de cartórios civis municipais.",
        "B",
        "**Etapa 1:** Desconstruir o preconceito moderno que desvaloriza a velhice em nome de uma juventude passageira consumista.\n**Etapa 2:** Explicitar a sabedoria da ancestralidade no Ubuntu: o ancião é uma biblioteca viva que encarna o elo entre os antepassados e o presente; escutar os mais velhos é um ato de discernimento ético e respeito à memória viva da resistência humana."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "Síntese conclusiva: por que a inclusão estrutural da filosofia do Ubuntu no currículo de Filosofia do Ensino Médio brasileiro atende, simultaneamente, a uma exigência de justiça histórica e a uma renovação profunda nos saberes para a cidadania democrática contemporânea?",
        "Porque ela simplifica as provas escolares ao dispensar os estudantes da leitura de autores clássicos do pensamento ocidental.",
        "Porque ela desfaz a violência epistêmica do eurocentrismo secular — que ensinou que só o homem branco europeu pensava com rigor —, ampliando o repertório ético dos jovens com um modelo comunitário de alteridade, solidariedade e justiça restaurativa indispensável para enfrentar a polarização, o ódio social e as crises ecológicas do século XXI.",
        "Porque ela estabelece a obrigatoriedade de que todos os concluintes do ensino médio dominem fluentemente o idioma zulu.",
        "Porque ela transfere a fiscalização pedagógica das escolas estaduais para missões diplomáticas da União Africana.",
        "Porque ela comprova que as teorias de física atômica foram desenvolvidas a partir de rituais tradicionais de cura florestal.",
        "B",
        "**Etapa 1:** Compreender a dupla função transformadora: reparar uma dívida histórica curricular (Lei 10.639/03) e superar o etnocentrismo racista da tradição acadêmica.\n**Etapa 2:** Concluir com o horizonte emancipatório do Ubuntu: em um mundo ferido pela desagregação individualista, pela devastação climática e pelo punitivismo cego, a sabedoria africana do 'Eu sou porque nós somos' ergue-se como farol de dignidade, paz e co-humanização radical para a juventude."
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
    linhas.append('eixo: "Eixo II: Ética, Moral e Filosofias Práticas Comunitárias"')
    linhas.append('capitulo: "Capítulo 14: Filosofia Moral Africana e o Princípio Ubuntu: Ramose e Tutu"')
    linhas.append('objeto_de_conhecimento: "A ontologia relacional africana, o princípio Ubuntu, Mogobe Ramose, Desmond Tutu, a justiça restaurativa e a crítica ao individualismo liberal"')
    linhas.append('ebook_fonte: "em-fil-c14-filosofia-moral-africana-ubuntu-ramose.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS501"')
    linhas.append('  - "EM13CHS502"')
    linhas.append('  - "EM13CHS503"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: Filosofia Moral Africana e o Princípio Ubuntu: Ramose e Tutu\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-14-filosofia-moral-africana-ubuntu-ramose -->"
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
    linhas.append("- RAMOSE, Mogobe B. Sobre a legitimidade e o estudo da filosofia africana. *Ensaios Filosóficos*, v. 4, p. 6-23, 2011.")
    linhas.append("- TUTU, Desmond. *Sem perdão não há futuro*. Tradução de Waldéa Barcellos. Rio de Janeiro: Rosa dos Tempos, 2001.")
    linhas.append("- MBITI, John S. *Religiões e filosofia africana*. Tradução de Nelio Schneider. São Paulo: Paulus, 2010.")
    linhas.append("- NOGUERA, Renato. *O ensino de filosofia e a Lei 10.639*. Rio de Janeiro: Pallas, 2014.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Salvar em temp_draft.md
    with open("temp_draft.md", "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em temp_draft.md ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador Educamob
    destino_final = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-14-filosofia-moral-africana-ubuntu-ramose/ebooks/em-fil-c14-filosofia-moral-africana-ubuntu-ramose-exercicios.md"
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
        print("\n[SUCESSO TOTAL] Cap 14 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {resultado.returncode}")
        sys.exit(resultado.returncode)

if __name__ == "__main__":
    main()
