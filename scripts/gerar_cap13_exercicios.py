# -*- coding: utf-8 -*-
"""
Script de Geração e Validação das 60 Questões de Filosofia - Cap 13
Objeto: Nietzsche: Genealogia da Moral e Niilismo
Habilidades BNCC: EM13CHS101, EM13CHS102, EM13CHS501, EM13CHS502
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
        "O que propõe o 'Método Genealógico' formulado por Friedrich Nietzsche em Para a Genealogia da Moral?",
        "Buscar a árvore genealógica de dinastias monárquicas que governaram a Europa central.",
        "Investigar as origens históricas, psicológicas e materiais concretas dos valores morais, desmistificando sua pretensa eternidade e pureza transcendental.",
        "Calcular a velocidade de deslocamento de cometas através de equações matemáticas.",
        "Provar que os textos de poesia homérica foram traduzidos para dialetos asiáticos arcaicos.",
        "Determinar o valor de mercado de ferramentas agrícolas comercializadas na Idade Média.",
        "B",
        "A genealogia nietzschiana recusa essências imutáveis e investiga sob quais condições históricas e afetivas a humanidade inventou para si os juízos de bem e mal."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "Ao utilizar a expressão 'Filosofar com o Martelo', qual atitude crítica Nietzsche assume perante a tradição ocidental?",
        "Destruir monumentos de pedra e esculturas clássicas em museus municipais.",
        "Auscultar e percutir os grandes monumentos metafísicos e morais para revelar o som oco de sua decadência interior e desmascarar ilusões consagradas.",
        "Trabalhar como artesão em oficinas de forja de ferraduras para cavalos de carga.",
        "Construir pontes de concreto armado para facilitar o trânsito de trens ferroviários.",
        "Exigir que os filósofos utilizem ferramentas pesadas durante aulas de lógica formal.",
        "B",
        "O martelo nietzschiano funciona como um diapasão crítico: percute os ídolos venerados pela moral para demonstrar que estão vazios por dentro e doentes da vitalidade."
    ))

    questoes_brutas.append((
        3, "EM13CHS102", "basico",
        "Na 'Moral dos Senhores' (Herrenmoral) analisada por Nietzsche, como os nobres e fortes originariamente definiam o conceito de 'Bom'?",
        "Pela capacidade de jejuar por semanas em mosteiros rurais isolados.",
        "Pela autoafirmação afirmativa de sua própria força, exuberância vital, beleza física, destemor e nobreza de espírito.",
        "Pelo número de moedas de prata guardadas em cofres de bancos comerciais.",
        "Pela obediência passiva às ordens emitidas por comandantes de guarnições militares.",
        "Pela habilidade em memorizar regras gramaticais de idiomas estrangeiros.",
        "B",
        "O conceito nobre de 'bom' nasce de um transbordamento afirmativo: o nobre olha para si mesmo, reconhece sua grandeza e exclama com altivez 'eu sou bom!'."
    ))

    questoes_brutas.append((
        4, "EM13CHS102", "basico",
        "Para a Moral dos Senhores, o que significava o termo 'Ruim' (schlecht), que se opunha ao 'Bom'?",
        "Um pecado diabólico imperdoável que condenava a alma ao fogo eterno do inferno.",
        "Aquilo que era vulgar, comum, fraco, covarde ou medroso, olhado com distanciamento sereno ou comiseração, sem ódio vingativo.",
        "Uma doença contagiosa transmitida por águas poluídas de rios urbanos.",
        "A falta de uniformes de linho claro em festividades cívicas municipais.",
        "A recusa em participar de assembleias políticas na praça central de Atenas.",
        "B",
        "Para os nobres, o 'ruim' não era um inimigo a ser exterminado; era simplesmente a ausência de distinção e nobreza, desprovido de rancor teológico."
    ))

    questoes_brutas.append((
        5, "EM13CHS102", "basico",
        "A 'Moral dos Escravos' (Sklavenmoral) nasce a partir de qual sentimento psicológico e afetivo dominante naqueles que são impotentes e dominados?",
        "O amor desinteressado e fraterno à natureza e aos animais silvestres.",
        "O Ressentimento (ressentiment), que constitui a vingança psíquica imaginária da fraqueza contra a nobreza e a força.",
        "A vontade de construir bibliotecas públicas em cidades do interior do país.",
        "A alegria espontânea e festiva compartilhada com parentes em colheitas de trigo.",
        "A coragem cívica de enfrentar perigos marítimos a bordo de barcos a vela.",
        "B",
        "Incapaz de agir diretamente no mundo real, o homem do ressentimento engendra uma vingança simbólica na moral, odiando a grandeza alheia que ele não pode alcançar."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Como opera a inversão de valores operada pela 'Revolta dos Escravos na Moral' descrita por Nietzsche?",
        "O escravo compra terras agrícolas e passa a contratar trabalhadores assalariados.",
        "O escravo categoriza primeiro o senhor forte e dominador como o 'Mau' e, em seguida, por mera reação defensiva, define a si mesmo e à sua fraqueza como o 'Bom'.",
        "O escravo aprende a ler tratados de física mecânica para ingressar em academias militares.",
        "O escravo viaja para ilhas remotas para escapar do pagamento de tributos reais.",
        "O escravo substitui suas roupas velhas por túnicas de seda importadas da Ásia.",
        "B",
        "A moral do ressentimento é puramente reativa: cria o conceito de 'mau' para rotular o forte e depois, por antítese, consagra sua própria impotência e passividade como virtude."
    ))

    questoes_brutas.append((
        7, "EM13CHS501", "basico",
        "Na análise etimológica de Nietzsche no segundo tratado da Genealogia da Moral, a palavra alemã para culpa (Schuld) origina-se de qual termo material concreto?",
        "Da palavra que designava sementes de cevada utilizadas em plantações.",
        "Do termo material para dívida financeira (Schulden), originado das relações brutais entre credor e devedor.",
        "Do nome dado às tempestades de granizo que destruíam telhados no inverno.",
        "Do vocábulo que identificava as armas de ferro empunhadas por guerreiros.",
        "Da expressão utilizada para saudar marinheiros em portos marítimos.",
        "B",
        "A moralidade da culpa não descendeu dos céus: ela brotou da contabilidade crua do direito contratual arcaico, onde o sofrimento físico do corpo servia como caução de dívidas."
    ))

    questoes_brutas.append((
        8, "EM13CHS501", "basico",
        "O que é a 'Má Consciência' (schlechtes Gewissen) de acordo com o diagnóstico nietzschiano?",
        "A perda da memória de fatos vivenciados durante os anos da infância.",
        "A interiorização forçada dos instintos agressivos e selvagens que, impedidos de se descarregar no exterior pelas leis civilizatórias, voltam-se para dentro e autoflagelam a psique humana.",
        "O hábito de dormir de olhos abertos para evitar pesadelos noturnos no quarto.",
        "A sensação de frio sentida por viajantes que cruzam montanhas cobertas de neve.",
        "A recusa voluntária em assinar contratos de trabalho em fazendas agrícolas.",
        "B",
        "Com a domesticação civilizatória, o homem virou um animal enjaulado; sem poder lutar para fora, passou a dilacerar a si mesmo, criando a culpa, a vergonha e a autoflagelação."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "No célebre aforismo 125 de A Gaia Ciência, o personagem do 'Homem Louco' corre pela praça pública com uma lanterna acesa gritando qual proclamação radical?",
        "'O inverno durará por mais de dez meses seguidos!'",
        "'Deus está morto! E fomos nós que o matamos!'",
        "'As frotas navais francesas desembarcaram nas praias litorâneas!'",
        "'Os bancos municipais fecharam suas portas para balanço anual!'",
        "'Todas as moedas de prata perderam seu valor de compra no comércio!'",
        "B",
        "A morte de Deus anunciada pelo louco representa o diagnóstico histórico da dissolução irreversível de todos os fundamentos transcendentais e verdades absolutas no Ocidente."
    ))

    questoes_brutas.append((
        10, "EM13CHS501", "basico",
        "O que significa, em sentido profundo e cultural, o anúncio nietzschiano da 'Morte de Deus'?",
        "A morte física de um ser celestial que habitava as nuvens visíveis do céu.",
        "O colapso irreversível da crença em um fundamento absoluto, metafísico ou universal que outorgue sentido predeterminado e garantia última à moral e ao cosmos.",
        "A vitória definitiva de monarquias absolutistas sobre as repúblicas europeias.",
        "A proibição de cultos religiosos em virtude de decretos emitidos por magistrados civis.",
        "A destruição acidental de catedrais góticas provocada por incêndios florestais.",
        "B",
        "Deus era a pedra angular que sustentava a moral, a teleologia e a verdade ocidental; sua morte deixa a civilização sem céu protetor, abrindo as portas do niilismo."
    ))

    questoes_brutas.append((
        11, "EM13CHS501", "basico",
        "O que é o 'Niilismo Passivo' diagnosticado por Nietzsche na modernidade ocidental?",
        "A prática diária de exercícios de ginástica e corridas atléticas no parque.",
        "A atitude de desânimo, resignação, tédio e conformismo apático que paralisa o homem diante da perda de sentido metafísico da vida.",
        "A recusa em consumir alimentos industrializados vendidos em feiras públicas.",
        "A decisão de emigrar para continentes distantes a bordo de navios mercantes.",
        "O costume de colecionar ferramentas de carpintaria em oficinas domésticas.",
        "B",
        "No niilismo passivo, o ser humano constata o vazio cósmico, mas, desprovido de força criativa, afunda na mediocridade, no cansaço e na desistência de grandes ideais."
    ))

    questoes_brutas.append((
        12, "EM13CHS502", "basico",
        "Quem é a figura do 'Último Homem' (der letzte Mensch) profetizada por Zaratustra como a encarnação do niilismo passivo?",
        "Um guerreiro invencível que comanda legiões militares em campos de batalha.",
        "O indivíduo medíocre, pequeno e conformista que busca apenas o conforto rasteiro, o entretenimento fácil, a segurança burocrática e a ausência de dor.",
        "Um sábio contemplativo que vive isolado no topo de montanhas cobertas de florestas.",
        "Um cientista que descobre novas fórmulas químicas em laboratórios universitários.",
        "Um marinheiro que cruza oceanos polares sem bússola de navegação marítima.",
        "B",
        "O último homem quer apenas a sua 'pequena volúpia de dia e pequena volúpia de noite', contentando-se com a mediocridade domesticada e sem qualquer centelha de superação."
    ))

    questoes_brutas.append((
        13, "EM13CHS502", "basico",
        "Em contraposição ao niilismo passivo, em que consiste a atitude do 'Niilismo Ativo' para Friedrich Nietzsche?",
        "Em fechar todas as livrarias públicas para que a população trabalhe na tecelagem.",
        "Em assumir a ausência de sentido transcendente como uma soberana libertação, destruindo os ídolos remanescentes e criando novos valores afirmativos para a existência terrena.",
        "Em abandonar as cidades urbanas para habitar cavernas escuras e úmidas no campo.",
        "Em obedecer fielmente a todos os decretos governamentais aprovados por parlamentares.",
        "Em negar a existência do mundo material para buscar a salvação em visões místicas.",
        "B",
        "O niilista ativo é o espírito forte e corajoso que toma o vazio como tela em branco, realizando a transvaloração dos valores com júbilo e soberania criadora."
    ))

    questoes_brutas.append((
        14, "EM13CHS501", "basico",
        "O que é a 'Vontade de Poder' (Wille zur Macht) na ontologia e na psicologia nietzschiana?",
        "A ambição mesquinha de banqueiros por acumular moedas de prata e ouro em cofres.",
        "A pulsão primordial e cósmica de crescimento, expansão, autossuperação, comando de si mesmo e criação afirmativa que anima todos os seres vivos.",
        "O treinamento obrigatório de recrutas para o uso de espadas de ferro em guerras.",
        "A imposição de tributos fiscais sobre mercadorias vendidas em feiras litorâneas.",
        "A obediência servil dos escravos perante as leis dos mestres da corte real.",
        "B",
        "A vida não é mera vontade de sobreviver passivamente (Schopenhauer); ela é ímpeto de expansão, triunfo sobre obstáculos e estilização criativa da própria força."
    ))

    questoes_brutas.append((
        15, "EM13CHS502", "basico",
        "O que representa o conceito nietzschiano de 'Além-do-Homem' (Übermensch) anunciado em Assim Falou Zaratustra?",
        "Um soldado geneticamente modificado treinado para batalhas territoriais bélicas.",
        "Um ideal ético-espiritual de ser humano emancipado da moral de rebanho e do ressentimento, capaz de criar seus próprios valores e afirmar a vida terrena com júbilo.",
        "Um governante autoritário que promulga leis de censura sobre livros de literatura.",
        "Um sacerdote que orienta a população por meio de sermões de penitência e culpa.",
        "Um comerciante marítimo que enriquece vendendo especiarias importadas da Índia.",
        "B",
        "O Übermensch é o superador da mediocridade do homem comum domesticado; é o espírito livre que cria sentidos na imanência da Terra, sem muletas celestes."
    ))

    questoes_brutas.append((
        16, "EM13CHS502", "basico",
        "Nas célebres 'Três Metamorfoses do Espírito' de Zaratustra, qual atitude existencial é representada pela figura do 'Camelo'?",
        "A capacidade de correr com grande velocidade através de dunas de areia fina.",
        "O espírito subserviente e obediente que se ajoelha para carregar fardos pesadíssimos sob o comando dogmático do 'Tu deves!'.",
        "A revolta agressiva contra todas as regras instituídas em sociedades urbanas.",
        "A inocência da criança que brinca com conchas marinhas em praias de água limpa.",
        "A fuga apressada de animais que tentam escapar de tempestades de chuva no deserto.",
        "B",
        "O camelo simboliza o homem de rebanho vergado sob a moral da renúncia, do dever kantiano e da culpa religiosa, carregando pesos morais alheios sem questionar."
    ))

    questoes_brutas.append((
        17, "EM13CHS502", "basico",
        "Ainda nas Três Metamorfoses, qual transformação é encarnada pelo 'Leão'?",
        "O leão é o predador que destrói plantações de trigo de camponeses no interior.",
        "O leão representa a rebelião sagrada da liberdade que enfrenta o dragão do 'Tu deves!' com o rugido do 'Eu quero!', conquistando a independência contra a tradição.",
        "O leão é o símbolo de governantes absolutistas que cobram impostos sobre tecidos.",
        "O leão simboliza a paciência do pescador que aguarda a subida da maré no litoral.",
        "O leão é o animal de montaria utilizado por generais de cavalaria militar.",
        "B",
        "O leão conquista o espaço da liberdade negativa: ele diz NÃO à tirania dogmática do passado, destruindo ídolos, embora ainda seja incapaz de criar novos valores puros."
    ))

    questoes_brutas.append((
        18, "EM13CHS502", "basico",
        "Qual é o significado sublime da terceira e última metamorfose do espírito: a 'Criança'?",
        "A fase infantil em que o ser humano não sabe ler livros de geometria aplicada.",
        "A inocência, o esquecimento salutar, um novo começo e um jogo sagrado: a capacidade de criar valores afirmativos e dizer um santo SIM à existência com leveza lúdica.",
        "A necessidade de ser tutorado por mestres em colégios públicos da capital.",
        "O medo irracional da escuridão noturna e de animais selvagens em florestas.",
        "A submissão voluntária às regras estritas de conduta aprovadas pelos pais.",
        "B",
        "A criança é o ápice do Übermensch: livre do ressentimento do leão e do peso do camelo, ela brinca como a roda que gira por si mesma, criando sentidos novos com alegria pura."
    ))

    questoes_brutas.append((
        19, "EM13CHS501", "basico",
        "O experimento de pensamento do 'Eterno Retorno do Mesmo' (die ewige Wiederkehr) propõe qual desafio existencial radical à consciência humana?",
        "Calcular a data exata em que todos os planetas do sistema solar ficarão alinhados.",
        "Imaginar que teremos de reviver esta mesmíssima vida com todas as suas dores, humilhações e júbilos infinitas vezes sucessivas, sem a menor alteração em cada detalhe.",
        "Prever quantas gerações de descendentes familiares habitarão a mesma cidade natal.",
        "Contar quantas folhas caem de árvores de florestas temperadas durante o outono.",
        "Determinar se as moedas de prata retornarão aos cofres públicos após crises fiscais.",
        "B",
        "O eterno retorno atua como o mais implacável teste ético: viver de tal modo a amar cada instante e querer sua repetição infinita sem queixas nem arrependimentos covardes."
    ))

    questoes_brutas.append((
        20, "EM13CHS501", "basico",
        "O que prescreve a atitude ética fundamental do 'Amor Fati' (amor ao destino) na filosofia de Nietzsche?",
        "A resignação passiva e derrotista de quem aceita a miséria sem lutar por seus direitos.",
        "O abraço afirmativo e amoroso à existência em sua totalidade de luz e sombra, compreendendo que as dores e adversidades são a forja necessária que fortalece a grandeza da alma.",
        "A obrigação cívica de prestar homenagens a generais que venceram campanhas militares.",
        "O hábito de consultar astrólogos antes de assinar contratos de compra e venda de terras.",
        "A fuga de qualquer tipo de dificuldade material para viver em comunidades isoladas.",
        "B",
        "Amor fati não é queixa nem fatalismo passivo: é a reconciliação jubilosa com a realidade; não querer nada diferente, nem no passado, nem no futuro, amando o destino como obra de arte."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao investigar a história da moral ocidental, por que Nietzsche identifica Sócrates e Platão como os primeiros grandes inauguradores da 'Decadência' da cultura grega clássica?",
        "Porque Sócrates e Platão recusavam-se a participar de disputas atléticas no ginásio da cidade.",
        "Porque eles subordinaram a exuberância trágica, os instintos corporais vitais e as paixões afirmativas ao primado tirânico de uma razão abstrata e de um além-mundo inteligível perfeito fictício.",
        "Porque eles introduziram o uso de moedas cunhadas em cobre no comércio marítimo do porto de Atenas.",
        "Porque eles defenderam que as cidades-estado deveriam fechar seus portos para navios mercantes persas.",
        "Porque Sócrates era analfabeto e Platão escrevia seus diálogos utilizando apenas tintas pretas.",
        "B",
        "Para Nietzsche, o socratismo inventou a fábula do 'mundo verdadeiro' das Ideias para desvalorizar a terra, criando a cisão moral entre corpo e mente que adoeceu o Ocidente."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Como a psicologia do Ressentimento se manifesta nos discursos moralizantes contemporâneos nas redes sociais digitais?",
        "Pela organização voluntária de mutirões para reformar praças públicas em bairros populares.",
        "Pelo prazer sádico e dissimulado de vigiar, julgar e cancelar indivíduos bem-sucedidos ou talentosos, mascarando a própria inveja e impotência criativa sob o manto da santidade e da superioridade moral.",
        "Pelo compartilhamento de textos poéticos que ensinam regras de cultivo de hortas comunitárias.",
        "Pela realização de debates acadêmicos com apresentação de documentos históricos arquivados em bibliotecas.",
        "Pela compra coletiva de ferramentas manuais para trabalhadores de oficinas de marcenaria.",
        "B",
        "O homem do ressentimento virtual compensa sua mediocridade fiscalizando o próximo: coloca-se como paladino da ética sem precisar realizar nada sublime, apenas atacando a potência alheia."
    ))

    questoes_brutas.append((
        23, "EM13CHS102", "intermediario",
        "Qual é a crítica de Nietzsche ao 'Ideal Ascético' professado historicamente pela casta sacerdotal nas religiões de salvação?",
        "A de que as roupas dos sacerdotes consumiam tecidos de seda importados de fábricas da Ásia.",
        "A denúncia de que o ascetismo prescreve a negação dos instintos carnais, a vergonha da sensualidade e o desprezo pela vida terrena, canalizando a energia vital do homem para a culpa e a servidão voluntária.",
        "A constatação de que os monges deveriam trabalhar dezoito horas diárias em plantações de cana-de-açúcar.",
        "A alegação de que os templos religiosos foram construídos com pedras que sofrem desgaste acelerado pela chuva.",
        "A tese de que a ascese monástica diminui a quantidade de livros publicados em gráficas municipais.",
        "B",
        "Nietzsche diagnostica o sacerdote como o médico perverso que trata a doença da vida inoculando mais veneno: prescreve a mortificação do corpo e o ódio ao mundo sensível em troca de um céu fictício."
    ))

    questoes_brutas.append((
        24, "EM13CHS501", "intermediario",
        "Como as teses da Genealogia da Moral sobre a interiorização forçada dos instintos agressivos anteciparam as descobertas da Psicanálise de Sigmund Freud em O Mal-Estar na Civilização?",
        "Provando que as doenças físicas do coração decorrem exclusivamente da ingestão de carnes com muita gordura.",
        "Demonstrando pioneiramente que a civilização exige a renúncia e a repressão dos impulsos primitivos humanos, cuja energia represada se volta contra o próprio sujeito na forma de culpa inconsciente gerida pelo Superego.",
        "Exigindo que os médicos psiquiatras utilizem instrumentos de choque elétrico durante sessões clínicas hospitalares.",
        "Comprovando que os sonhos noturnos são reproduções exatas de poemas épicos lidos durante a juventude.",
        "Determinando que os tratamentos de ansiedade mental devam ocorrer em salas de internatos rurais fechados.",
        "B",
        "Freud reconheceu a genialidade antecipatória de Nietzsche: a civilização civiliza domesticando os impulsos; a agressividade que não pode sair para o exterior volta-se para dentro como má consciência e culpa."
    ))

    questoes_brutas.append((
        25, "EM13CHS502", "intermediario",
        "Por que, para Nietzsche, a compaixão indiscriminada (Mitleid) celebrada pela moralidade cristã e pela ética de Arthur Schopenhauer é considerada uma atitude perigosa para a saúde da cultura?",
        "Porque ela encarece os custos com a compra de ataduras de pano em hospitais de cidades costeiras.",
        "Porque ela multiplica o sofrimento no mundo, preserva artificialmente o que é doente e decadente, e desarma a capacidade de superação e a dureza fecunda necessária para a grande criação humana.",
        "Porque ela impede que os operários industriais trabalhem aos sábados em fábricas de armamentos militares.",
        "Porque ela obriga os cidadãos ricos a dividirem suas carruagens com pessoas que caminham a pé pelas estradas.",
        "Porque ela diminui a arrecadação de impostos tributários cobrados sobre a importação de trigo e cevada.",
        "B",
        "Para Nietzsche, a compaixão contagia com a dor do fraco e glorifica a fraqueza; o sofrimento deve ser superado com valentia e amor fati, e não cultivado como valor sagrado que amolece o caráter."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "No diálogo com a literatura universal, como o dilema de Ivan Karamazov no romance Os Irmãos Karamazov de Dostoiévski ('Se Deus não existe, tudo é permitido?') relaciona-se com o niilismo nietzschiano?",
        "Dostoiévski afirma que as igrejas de madeira devem ser pintadas de azul claro para atrair novos fiéis aos cultos.",
        "Ambos diagnosticam a vertigem da ausência de garantias metafísicas no mundo moderno; contudo, enquanto Dostoiévski teme o caos moral da falta de Deus, Nietzsche celebra esse vazio como o advento da autêntica soberania e responsabilidade criadora do homem livre.",
        "Ambos defendem que os cidadãos que cometem crimes devem ser absolvidos mediante a doação de pães aos necessitados.",
        "Dostoiévski sustenta que as pessoas que vivem em cidades litorâneas não sentem angústias espirituais perante a morte.",
        "Nietzsche afirma que os governantes absolutistas da Rússia deveriam adotar o código civil dos imperadores romanos.",
        "B",
        "A frase de Dostoiévski expõe a angústia da perda do juiz cósmico; Nietzsche responde que 'tudo é permitido' não significa barbárie cega, mas o fardo grandioso de o homem ser o único responsável pela criação de seus valores."
    ))

    questoes_brutas.append((
        27, "EM13CHS502", "intermediario",
        "Como a adulteração dos manuscritos de Nietzsche realizada por sua irmã Elisabeth Förster-Nietzsche alimentou a apropriação indevida do pensamento nietzschiano pelo nazismo na década de 1930?",
        "Ela vendeu as máquinas de escrever utilizadas pelo filósofo para empresas fabricantes de relógios de bolso.",
        "Ela manipulou fragmentos póstumos e os publicou na coletânea forjada A Vontade de Poder, associando indevidamente conceitos éticos e espirituais (como Übermensch) ao antissemitismo e ao nacionalismo germânico racista que Nietzsche expressamente repudiara em vida.",
        "Ela queimou os tratados de filologia clássica que tratavam da gramática da língua grega antiga.",
        "Ela exigiu que os livros de Nietzsche fossem lidos exclusivamente por oficiais condecorados da marinha de guerra.",
        "Ela proibiu que as editoras alemãs publicassem obras de literatura dramática compostas por autores ingleses.",
        "B",
        "A irmã nacionalista forjou uma caricatura racista: Nietzsche declarava-se anti-antissemita, rompeu com Wagner pelo racismo deste e considerava o nacionalismo germânico uma tolice decadente."
    ))

    questoes_brutas.append((
        28, "EM13CHS102", "intermediario",
        "Em Para a Genealogia da Moral, Nietzsche formula a clássica metáfora das 'Aves de Rapina e os Cordeiros'. O que essa alegoria revela sobre a moralidade do ressentimento?",
        "Que as aves de rapina são culpadas por terem bicos curvos e garras afiadas confeccionadas em oficinas de ferro.",
        "Que os cordeiros consideram as aves de rapina 'más' porque devoram cordeiros e, por consequência, consideram-se 'bons' porque não devoram ninguém, esquecendo que exigir que a força não se manifeste como força é tão absurdo quanto exigir que a fraqueza seja força.",
        "Que os fazendeiros devem instalar espantalhos de palha em pastagens para evitar o ataque de falcões às ovelhas.",
        "Que os animais carnívoros perdem o instinto de caça quando alimentados com grãos de milho cozido nas fazendas.",
        "Que as leis de proteção ambiental exigem que as aves de rapina sejam mantidas em gaiolas de arame farpado.",
        "B",
        "A ave de rapina não odeia o cordeiro; ela apenas come porque é forte. Mas o cordeiro moraliza a natureza, fingindo que sua fraqueza involuntária é um mérito moral de virtude e mansidão voluntária."
    ))

    questoes_brutas.append((
        29, "EM13CHS501", "intermediario",
        "Qual é o significado da 'Transvaloração de Todos os Valores' (Umwertung aller Werte) proposta por Nietzsche como missão de sua filosofia madura?",
        "O aumento do valor nominal das moedas de ouro nos bancos centrais da Europa.",
        "A superação definitiva dos valores doentes e niilistas da moral ascética (que negam a terra e glorificam a fraqueza) e a fundação de novos valores afirmativos centrados na vida, na saúde e na plenitude da vontade de poder.",
        "A queima de livros de matemática e de física mecânica em fogueiras públicas nas capitais.",
        "A substituição de todas as leis civis por decretos editados por generais militares condecorados.",
        "A determinação de que todos os cidadãos adultos devem aprender a esculpir estátuas de bronze.",
        "B",
        "Transvalorar não é anarquia destruidora: é submeter os valores existentes ao critério da saúde vital; derrubar os ídolos que rebaixam a condição humana e inaugurar uma tábua afirmativa de grandeza terrena."
    ))

    questoes_brutas.append((
        30, "EM13CHS502", "intermediario",
        "Em Assim Falou Zaratustra, Nietzsche adverte: 'O homem é uma corda, atada entre o animal e o além-do-homem — uma corda sobre um abismo'. O que essa imagem poética expressa sobre o destino da humanidade?",
        "Que os seres humanos devem praticar acrobacias com cordas de linho em circos e festivais de rua.",
        "Que o ser humano atual não é um fim definitivo em si mesmo, mas uma transição perigosa e uma ponte necessária rumo à superação da mediocridade em direção ao além-do-homem.",
        "Que as pontes suspensas sobre rios montanhosos devem ser construídas com cabos de aço galvanizado.",
        "Que a humanidade retornará inevitavelmente ao modo de vida dos animais de pasto nas savanas tropicais.",
        "Que os governantes de cidades industriais devem proibir a travessia de desfiladeiros durante o inverno.",
        "B",
        "O homem é um projeto em travessia: sua grandeza reside no fato de ser uma ponte que pode ser superada; estacionar no 'último homem' é a morte espiritual; avançar é conquistar o Übermensch."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Como a obra de Michel Foucault em Vigiar e Punir e em Nietzsche, a Genealogia, a História foi influenciada pelo método genealógico nietzschiano?",
        "Foucault utilizou as técnicas de tipografia alemã para imprimir panfletos em gráficas sindicais de Paris.",
        "Foucault aplicou a genealogia para desmantelar a ilusão da neutralidade das ciências humanas e das instituições disciplinares (prisões, manicômios, clínicas), mostrando que o saber e a verdade são moldados por micropoderes históricos e disputas pelo controle de corpos.",
        "Foucault defendeu que as sentenças dos tribunais penais deveriam ser lavradas em versos métricos de teatro dramático.",
        "Foucault propôs que os hospitais psiquiátricos fossem administrados exclusivamente por generais de infantaria.",
        "Foucault comprovou que as celas dos presídios parisienses consumiam muita tinta branca nas paredes internas.",
        "B",
        "Foucault retoma Nietzsche contra a metafísica: não há essência eterna da loucura ou da penalidade; o método genealógico rastreia como práticas de poder inventaram os conceitos normativos da modernidade."
    ))

    questoes_brutas.append((
        32, "EM13CHS501", "intermediario",
        "No pensamento nietzschiano, por que o 'Eterno Retorno do Mesmo' funciona como o martelo mais implacável contra o ressentimento e o remorso doentio?",
        "Porque ele comprova que os relógios mecânicos das torres de igrejas mantêm a mesma velocidade de marcha.",
        "Porque ele exige do indivíduo uma reconciliação total com tudo o que viveu: não é possível desejar o retorno infinito da própria vida lamentando o passado; ou se afirma a existência inteira com júbilo ou ela se torna um fardo insuportável.",
        "Porque ele demonstra que os deuses dos oceanos viajam em carruagens puxadas por cavalos marinhos brancos.",
        "Porque ele obriga as famílias rurais a realizarem o plantio das mesmas sementes de cevada em todas as safras.",
        "Porque ele comprova que as leis de rotação do planeta Terra são imutáveis ao longo dos séculos da história.",
        "B",
        "O homem do ressentimento vive de queixas contra o passado ('se ao menos isso não tivesse ocorrido'); o eterno retorno exige o 'assim eu quis!': transmutar todo 'foi' em 'assim o desejei!', banindo o remorso estéril."
    ))

    questoes_brutas.append((
        33, "EM13CHS502", "intermediario",
        "Na análise das Três Metamorfoses, qual é o limite característico da fase do 'Leão' que o impede de ser a consumação final do espírito nobre?",
        "O leão é um animal que sofre com o calor escaldante de desertos de areia fina durante o meio-dia.",
        "O leão é mestre na negação e na destruição sagrada dos ídolos do passado, mas ainda é incapaz de criar novos valores positivos a partir de si mesmo, permanecendo amarrado àquilo contra o que lutou.",
        "O leão recusa-se a obedecer aos comandos emitidos por domadores profissionais em arenas públicas.",
        "O leão não possui dedos articulados para escrever frases curtas em cadernos escolares de papelão.",
        "O leão perde as presas carnívoras quando atinge idades avançadas em reservas naturais selvagens.",
        "B",
        "A liberdade do leão é apenas liberdade 'de' (libertação contra os laços do dragão moral); ela prepara o terreno, mas a liberdade 'para' a criação afirmativa e jubilosa exige a inocência da criança."
    ))

    questoes_brutas.append((
        34, "EM13CHS504", "intermediario",
        "Em Crepúsculo dos Ídolos, Nietzsche cunhou o célebre aforismo: 'Aquilo que não me mata me fortalece.' Como essa sentença expressa a ética do Amor Fati e a superação do sofrimento?",
        "Ela afirma que as pessoas que sobrevivem a quedas de carruagens devem participar de corridas atléticas no parque.",
        "Ela proclama que as dores, derrotas e tragédias da vida não são erros a serem amaldiçoados, mas a resistência e a forja existencial necessária para desenvolver resiliência, agudeza de espírito e nobreza de caráter.",
        "Ela comprova que as feridas físicas no corpo humano cicatrizam mais rápido quando expostas a ventos litorâneos.",
        "Ela exige que os médicos de hospitais públicos suspendam a aplicação de remédios químicos em enfermos.",
        "Ela determina que as famílias que moram no campo abandonem suas residências para dormirem em tendas de couro.",
        "B",
        "A adversidade é a matéria-prima da virtude trágica: a árvore nobre precisa fincar suas raízes no abismo da dor para que seus galhos alcancem as alturas luminosas; o sofrimento tempera os espíritos superiores."
    ))

    questoes_brutas.append((
        35, "EM13CHS501", "intermediario",
        "Ao desconstruir o conceito de 'Livre-Arbítrio', Nietzsche formula em Crepúsculo dos Ídolos a crítica aos 'Quatro Grandes Erros' da razão ocidental. Por que Nietzsche afirma que o livre-arbítrio foi inventado pelos teólogos?",
        "Para permitir que os jovens escolhessem suas próprias profissões em academias de direito e medicina.",
        "Para transformar as pessoas em culpadas perante a lei divina, criando a ficção de que suas ações decorrem de uma vontade pura e arbitrária para justificar moralmente a aplicação de punições e tormentos pelo clero.",
        "Para incentivar a compra de terras agrícolas férteis por camponeses que pagavam em moedas de prata.",
        "Para demonstrar que os animais da savana agem impulsionados por cálculos matemáticos em suas caçadas.",
        "Para proibir a realização de feiras populares de tecidos durante as estações chuvosas do ano civil.",
        "B",
        "Para Nietzsche, a fábula do livre-arbítrio é o estratagema da casta sacerdotal para tornar o homem culpável e dependente da absolvição eclesiástica, aprisionando a inocência do devir biológico no tribunal da culpa."
    ))

    questoes_brutas.append((
        36, "EM13CHS102", "intermediario",
        "Como a crítica nietzschiana ao 'Egalitarismo Rasteiro' da modernidade (democracia liberal e socialismo) se articula com a sua denúncia da moral dos escravos?",
        "Nietzsche defendia que todos os trabalhadores industriais deveriam receber pagamentos mensais em barras de ouro maciço.",
        "Ele sustentava que a insistência em nivelar todas as diferenças e igualar artificialmente os seres humanos opera como a continuação secularizada da moralidade dos fracos, asfixiando a emergência de talentos excepcionais e espíritos nobres.",
        "Ele propunha que as leis eleitorais de cidades portuárias deveriam proibir o voto de marinheiros e pescadores.",
        "Ele afirmava que as escolas públicas deveriam ensinar apenas disciplinas de artesanato manual em cerâmica.",
        "Ele comprovava que a divisão técnica do trabalho fabril consumia muita energia gerada por carvão vegetal.",
        "B",
        "Para Nietzsche, a busca obsessiva pela igualdade absoluta nivela a humanidade por baixo, domesticando a singularidade criadora em favor do conformismo homogêneo do rebanho medíocre."
    ))

    questoes_brutas.append((
        37, "EM13CHS501", "intermediario",
        "Qual é a relação que Nietzsche estabelece entre a Saúde Biológica e Fisiológica do corpo e a produção de sistemas filosóficos metafísicos?",
        "Ele afirma que os filósofos que comem pão integral formulam teorias geométricas corretas sobre o universo.",
        "Ele defende que as grandes doutrinas filosóficas não são verdades celestes neutras, mas sintomas e confissões involuntárias da fisiologia, dos apetites reprimidos e da saúde vital ou decadência do organismo de seus autores.",
        "Ele demonstra que as pessoas que praticam natação no mar Egeu não formulam perguntas metafísicas sobre o ser.",
        "Ele exige que os estudantes universitários realizem exames físicos diários antes de assistirem a aulas teóricas.",
        "Ele comprova que o clima úmido da Inglaterra impedia que os pensadores compreendessem a dialética de Platão.",
        "B",
        "Nietzsche inaugura a suspeita fisiológica: quem é doente e fraco inventa além-mundos celestes para escapar do sofrimento da terra; quem é saudável e pleno cria deuses solares e afirma a beleza trágica do corpo."
    ))

    questoes_brutas.append((
        38, "EM13CHS502", "intermediario",
        "Em Ecce Homo, em sua autobiografia intelectual, Nietzsche declara-se com orgulho: 'Eu não sou um homem, sou dinamite!'. O que essa metáfora incendiária expressa sobre o impacto de sua filosofia?",
        "O filósofo pretendia trabalhar em empresas fabricantes de explosivos para abrir túneis ferroviários em montanhas.",
        "Ela proclama sua missão de demolir os alicerces milenares da civilização ocidental (o platonismo e o cristianismo), abrindo caminho para uma era sem precedentes de transvaloração e renascimento do espírito livre.",
        "Ela afirmava que as cidades industriais da Alemanha corriam o risco de sofrer ataques com bombas químicas.",
        "Ela exigia que as bibliotecas escolares de capitais europeias queimassem seus acervos de livros de história antiga.",
        "Ela demonstrava que as discussões acadêmicas em universidades públicas consumiam recursos fiscais excessivos do tesouro.",
        "B",
        "A dinamite nietzschiana explode a crosta dos dogmas metafísicos e morais; desmantela as mentiras milenares com as quais o Ocidente adoeceu a vida, convocando o homem à vertigem da criação autônoma."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Por que Nietzsche admirava profundamente a cultura trágica da Grécia Pré-Socrática (Homero, Ésquilo e Sófocles) antes do advento do racionalismo de Sócrates?",
        "Porque os marinheiros gregos utilizavam embarcações de guerra com três ordens de remos no mar Egeu.",
        "Porque os gregos arcaicos sabiam abraçar o sofrimento, a finitude e o terror da existência através da beleza e da exuberância da arte trágica, afirmando a vida em sua plenitude sem fugir para ilusões de paraísos celestes.",
        "Porque as esculturas de templos sagrados de Atenas eram confeccionadas exclusivamente com blocos de argila cozida.",
        "Porque as leis civis da Grécia arcaica proibiam o casamento entre pessoas que moravam em cidades rivais.",
        "Porque os poetas da Antiguidade eram obrigados a pagar tributos fiscais sobre a declamação de seus versos.",
        "B",
        "Na tragédia ática (equilíbrio entre o apolíneo e o dionisíaco), o grego arcaico olhava no abismo do sofrimento e dizia SIM à vida com valentia e esplendor estético, sem a covardia da moral do pecado."
    ))

    questoes_brutas.append((
        40, "EM13CHS502", "intermediario",
        "Ao examinar a ética contemporânea perante o niilismo das sociedades de consumo no século XXI, qual sintoma cultural reflete diretamente a vitória do 'Último Homem' descrito por Nietzsche?",
        "A realização de competições esportivas de natação em piscinas olímpicas aquecidas por energia solar.",
        "A busca obsessiva por segurança anestesiada, o consumo compulsivo de mercadorias descartáveis e medicamentos para suprimir qualquer inquietação existencial, e o horror visceral a qualquer risco, dor ou esforço sublime de criação.",
        "A obrigatoriedade de que todos os cidadãos adultos aprendam a cultivar sementes de girassol em vasos domésticos.",
        "A determinação de que as assembleias parlamentares aprovem códigos penais impressos em papéis coloridos.",
        "A exigência de que os jovens que concluem o ensino médio trabalhem como carpinteiros em feiras rurais.",
        "B",
        "A sociedade da dopamina rápida e do conforto passivo encarna o último homem: troca a grandeza trágica da vida por entretenimento anestesiante, inventando a felicidade rasteira da ausência de atrito e esforço."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a famosa passagem do Prólogo de Para a Genealogia da Moral: 'Precisamos de uma crítica dos valores morais, o valor desses valores deve ele mesmo ser colocado em questão — e para isso é necessário um conhecimento das condições e circunstâncias em que eles nasceram, sob as quais se desenvolveram e se modificaram.' De que maneira essa exigência genealógica rompe com a fundamentação ética kantiana do imperativo categórico?",
        "Negando que os astrônomos prussianos tenham utilizado lunetas ópticas para observar o céu noturno.",
        "Demonstrando que o imperativo categórico de Kant finge ser uma lei pura e a priori da razão, mas oculta a sua origem histórica e psicológica real no ressentimento, na coerção disciplinar e na moral ascética de renúncia aos instintos vitais.",
        "Provando que a matemática foi inventada por mercadores de seda da Península Itálica durante o século XV.",
        "Afirmando que os filósofos que trabalhavam em universidades públicas eram obrigados a usar fardas de infantaria.",
        "Defendendo que as regras morais de uma sociedade dependem exclusivamente da quantidade de chuva que cai no inverno.",
        "B",
        "**Etapa 1:** Interpretar o deslocamento genealógico: colocar em questão o próprio valor dos valores tidos como sagrados e universais.\n**Etapa 2:** Concluir com a demolição de Kant: o imperativo categórico não é a voz divina da razão pura; o martelo nietzschiano revela que o 'dever desinteressado' é a sublimação requintada da má consciência e da crueldade voltada para dentro."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em Para a Genealogia da Moral, Nietzsche formula a seguinte análise sobre o papel do ressentimento na história ocidental: 'A revolta dos escravos na moral começa quando o próprio ressentimento se torna criador e gera valores: o ressentimento de seres aos quais a verdadeira reação, a do ato, é negada, e que se desforram com uma vingança imaginária.' Qual foi o impacto histórico civilizatório dessa revolta sacerdotal no triunfo do cristianismo sobre o Império Romano?",
        "Ela provocou o fechamento definitivo de todos os portos comerciais da Península Itálica por marinheiros franceses.",
        "Ela realizou a mais formidável inversão de valores da história: Roma e sua aristocracia da força viril e orgulho terreno foram derrotadas espiritualmente pela moralidade plebeia e sacerdotal da humildade, da culpa e da igualdade metafísica dos fracos.",
        "Ela determinou que os generais das legiões militares deveriam ser escolhidos por meio de sorteios em praças públicas.",
        "Ela obrigou os cidadãos romanos a pagarem suas dívidas financeiras exclusivamente em cestas de peixes frescos.",
        "Ela causou a destruição física das bibliotecas da cidade de Alexandria por exércitos armados com catapultas.",
        "B",
        "**Etapa 1:** Analisar a luta histórica de dois pares de valores: Roma contra a Judeia (os nobres conquistadores contra a casta sacerdotal do ressentimento).\n**Etapa 2:** Evidenciar o triunfo da moral dos escravos: a fraqueza venceu a força domesticando o senhor por meio da culpa; o Império Romano desmoronou moralmente quando sua nobreza foi contaminada pela má consciência e pela moral da renúncia."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Considere a gênese da 'Culpa' (Schuld) analisada por Nietzsche: 'Como fazer no animal humano uma memória? Como imprimir algo nessa inteligência do instante, de modo que permaneça presente? Grava-se a fogo, para que fique na memória: apenas o que não cessa de causar dor permanece na memória.' Como essa tese desmonta a crença de que a consciência moral teria uma origem sublime e divina?",
        "Provando que as tábuas de argila da Mesopotâmia eram queimadas em fornos de carvão vegetal com cinzas escuras.",
        "Evidenciando que a consciência e a responsabilidade moral humana foram forjadas por meio de séculos de crueldades físicas sistemáticas, torturas, mutilações e sacrifícios rituais sangrentos para domesticar a besta humana e obrigá-la a cumprir contratos e promessas.",
        "Afirmando que os médicos da Antiguidade utilizavam plantas venenosas para tratar infecções bacterianas na pele de jovens.",
        "Sustentando que os juízes civis dos tribunais europeus desconheciam as regras de comércio marítimo de cereais.",
        "Defendendo que as crianças nascidas em climas montanhosos possuem memória visual superior à de adultos urbanos.",
        "B",
        "**Etapa 1:** Compreender a mnemotécnica da dor na genealogia nietzschiana: a memória da promessa foi gravada com ferro em brasa no corpo do devedor.\n**Etapa 2:** Concluir com a desmistificação da moralidade: a doce consciência moral de hoje é filha da crueldade e do terror institucionalizado do passado; não há pureza nos alicerces éticos da civilização pacificada."
    ))

    questoes_brutas.append((
        44, "EM13CHS501", "dificil",
        "No aforismo 341 de A Gaia Ciência, Nietzsche introduz o Eterno Retorno através da figura do 'Demônio': 'Se um dia ou uma noite um demônio se esgueirasse em tua mais solitária solidão e te dissesse: Esta vida, como tu a vives e a viveste, terás de vivê-la mais uma vez e inumeráveis vezes mais...' De que maneira essa hipótese atua como o filtro seletivo ético supremo para distinguir a alma forte da alma decadente?",
        "Fazendo com que as pessoas que têm medo de insetos noturnos comprem lamparinas a óleo para iluminar quartos escuros.",
        "Revelando que a alma ressentida e decadente, que odeia o mundo e sonha com paraísos futuros, entra em desespero e amaldiçoa o demônio, enquanto a alma nobre e afirmativa acolhe o desafio com êxtase sagrado, pois ama a existência terrena de tal forma que deseja sua repetição eterna.",
        "Obrigando os governantes de cidades industriais a reformarem as estradas de ferro para facilitar o trânsito de trens.",
        "Provando que os filósofos iluministas da Alemanha desconheciam as equações de física quântica formuladas séculos depois.",
        "Determinando que os cidadãos que cometem infrações civis devam cumprir penas de trabalhos manuais em pedreiras rurais.",
        "B",
        "**Etapa 1:** Analisar a função do eterno retorno como critério ético e existencial de seleção da alma.\n**Etapa 2:** Concluir com a vitória sobre o niilismo: quem depende de salvação celestial no além não suporta a ideia da eternidade da terra; apenas o Übermensch dotado de amor fati possui a exuberância vital de dizer SIM infinito a cada detalhe de seu destino real."
    ))

    questoes_brutas.append((
        45, "EM13CHS502", "dificil",
        "Em Assim Falou Zaratustra, na seção sobre as Três Metamorfoses, Zaratustra proclama: 'A criança é inocência e esquecimento, um novo começo, um jogo, uma roda que gira por si mesma, um primeiro movimento, um santo dizer-sim.' Por que o esquecimento ativo (Vergesslichkeit) é considerado por Nietzsche uma faculdade indispensável para a grandeza moral e a saúde da cultura?",
        "Porque os seres humanos que esquecem nomes de pessoas do passado dormem mais horas seguidas durante o período da noite.",
        "Porque o excesso de memória e rancor do passado paralisa o homem no ressentimento e na ruminação estéril; a capacidade nobre de esquecer é a condição de saúde mental para fechar feridas, agir no presente e criar o novo com leveza virginal.",
        "Porque as escolas públicas municipais seriam obrigadas a queimar cadernos com anotações de anos anteriores.",
        "Porque os cidadãos adultos esqueceriam o valor de compra de moedas bancárias utilizadas no comércio popular.",
        "Porque os tratados de paz internacionais perderiam a eficácia jurídica caso as cláusulas não fossem decoradas por magistrados.",
        "B",
        "**Etapa 1:** Interpretar o conceito nietzschiano de força plástica e esquecimento ativo (em *Segunda Consideração Intempestiva* e *Genealogia*).\n**Etapa 2:** Evidenciar o abismo entre o nobre e o escravo: o ressentido rumina o passado como um monstro rancoroso incapaz de digerir ofensas; o nobre perdoa esquecendo de imediato, desobstruindo a alma para o júbilo da ação criadora soberana."
    ))

    questoes_brutas.append((
        46, "EM13CHS501", "dificil",
        "No fragmento póstumo da Vontade de Poder, Nietzsche declara: 'Não há fatos morais, mas apenas uma interpretação moral de certos fenômenos.' Qual é a implicação dessa tese para a desconstrução da objetividade científica e ética proclamada pelo Iluminismo e pelo Positivismo?",
        "A comprovação de que as leis da gravidade deixam de funcionar quando os astrônomos fecham suas lunetas de observação.",
        "A demonstração de que a pretensa verdade neutra, objetiva e desinteressada é uma ficção metafísica; todo conhecimento e toda tábua de valores são construções perspectivadas por interesses vitais de poder, pulsões inconscientes e pontos de vista situados no mundo corpóreo.",
        "A afirmação de que os termômetros de vidro não conseguem medir a temperatura de águas fluviais em estações frias.",
        "A determinação de que os matemáticos devem abandonar o estudo da geometria analítica para escrever romances literários.",
        "A certeza de que as transações comerciais nos portos marítimos deixam de ter validade quando as marés estão baixas.",
        "B",
        "**Etapa 1:** Compreender o perspectivismo radical de Nietzsche contra o dogma positivista do 'fato puro'.\n**Etapa 2:** Concluir com a desconstrução do universalismo moderno: não existem verdades em si desincorporadas; toda teoria científica ou sistema moral expressa a perspectiva de um corpo e de uma vontade de poder em luta por expansão."
    ))

    questoes_brutas.append((
        47, "EM13CHS502", "dificil",
        "Ao examinar a relação entre o Niilismo e a Crítica da Religião Cristã em O Anticristo (1888), por que Nietzsche formula a acusação demolidora de que 'o cristianismo é o crime supremo contra a vida terrena'?",
        "Porque as ordens religiosas proibiam os agricultores de cultivarem vinhedos de uva nas encostas de montanhas.",
        "Porque o cristianismo santificou a fraqueza, a subserviência e a culpa mórbida, travando uma guerra implacável de difamação contra o corpo, o intelecto corajoso e os instintos vitais saudáveis, promovendo o adoecimento sistemático do Ocidente.",
        "Porque os mosteiros medievais consumiam quantidades excessivas de carvão vegetal para aquecerem suas capelas.",
        "Porque os sacerdotes e bispos recusavam-se a participar de competições atléticas de corrida de revezamento.",
        "Porque as bíblias impressas em papel de linho eram muito pesadas para serem transportadas em mochilas de lona.",
        "B",
        "**Etapa 1:** Analisar a denúncia nietzschiana da moral cristã como negação do mundo empírico visível.\n**Etapa 2:** Concluir com a tragédia da decadência: o cristianismo colocou veneno na raiz da vida ao declarar o corpo pecaminoso e o orgulho abominável, castrando a força da civilização e preparando o colapso do niilismo passivo moderno."
    ))

    questoes_brutas.append((
        48, "EM13CHS102", "dificil",
        "Considere a gênese do conceito de 'Justiça' no segundo tratado de Para a Genealogia da Moral. Como Nietzsche demonstra que a verdadeira justiça aristocrática arcaica não brotou do sentimento de vingança dos ofendidos, mas do poder soberano do mais forte?",
        "Afirmando que os nobres utilizavam togas de linho branco em todos os julgamentos de conflitos civis municipais.",
        "Evidenciando que a justiça autêntica nasce da magnanimidade e do transbordamento de poder do governante ou do grupo forte que, sentindo-se acima da ofensa e seguro de sua soberania, recusa o ódio reativo e pode declarar com nobreza: 'Que me importam os meus parasitas? Que vivam e prosperem!'",
        "Provando que as leis de compensação de danos materiais foram copiadas de códigos jurídicos de dinastias persas.",
        "Sustentando que os juízes da Antiguidade eram obrigados a doar metade de suas colheitas de trigo aos necessitados.",
        "Defendendo que as decisões de sentenças judiciais eram tomadas mediante o lançamento de moedas de prata ao chão.",
        "B",
        "**Etapa 1:** Desmistificar a tese de que a justiça teria nascido do ressentimento ou do anseio de vingança dos fracos.\n**Etapa 2:** Concluir com a clemência aristocrática: a verdadeira justiça é a superação da vingança mesquinha; quando uma comunidade se torna imensamente poderosa, ela deixa de punir o ofensor com fúria e o tolera como o forte tolera o mosquito que o pica."
    ))

    questoes_brutas.append((
        49, "EM13CHS501", "dificil",
        "Em Crepúsculo dos Ídolos, no capítulo intitulado 'Como o Mundo Verdadeiro se Tornou uma Fábula', Nietzsche resume a história de um erro metafísico em seis etapas, desde Platão até a filosofia do martelo. Qual é o clímax da etapa final dessa história da ilusão?",
        "A comprovação científica de que a luz do sol é composta por partículas que viajam em velocidade constante pelo vácuo.",
        "A constatação de que, ao abolirmos o fictício 'mundo verdadeiro' das essências celestes perfeitas, nós também abolimos e superamos o 'mundo aparente': resta agora a própria realidade exuberante da imanência terrena sem antíteses enganosas.",
        "A exigência de que os governantes de nações democráticas devam fechar os cursos universitários de ciências humanas.",
        "A determinação de que as obras de literatura clássica sejam traduzidas para dialetos falados em ilhas da Oceania.",
        "A certeza de que as estações do ano afetam a quantidade de ferro fundido nas oficinas de cantaria de pedra.",
        "B",
        "**Etapa 1:** Acompanhar a progressiva dissolução da metafísica ocidental: do mundo inteligível platônico à coisa-em-si incognoscível de Kant.\n**Etapa 2:** Evidenciar o golpe de mestre de Nietzsche: destruído o além-mundo ideal, a noção de que este mundo concreto seria 'apenas cópia ou aparência' perde todo o sentido; a imanência terrena ressurge como a única e sagrada realidade viva."
    ))

    questoes_brutas.append((
        50, "EM13CHS502", "dificil",
        "No diagnóstico de Nietzsche sobre o Niilismo Europeu nos Fragmentos Póstumos, ele adverte que a tentativa moderna de substituir Deus por novos ídolos seculares (como a Razão Iluminista, a Ciência Neutra, a Nação Soberana ou o Progresso Tecnológico) constitui uma farsa. Por que esses novos ídolos falham em conter o niilismo?",
        "Porque as máquinas a vapor construídas na Inglaterra consumiam muito carvão fóssil extraído de minas subterrâneas.",
        "Porque esses ideais modernos continuam mantendo a mesma estrutura metafísica platônica e cristã de crença em uma verdade absoluta exterior que salvará a humanidade, operando como meros paliativos hipócritas que adiam a transvaloração autêntica.",
        "Porque os cientistas de laboratórios universitários não possuíam diplomas reconhecidos por academias de ciências.",
        "Porque as eleições de presidentes em repúblicas liberais eram realizadas com cédulas de votação em papel reciclado.",
        "Porque os governos europeus foram forçados a assinar tratados de paz que proibiam o desenvolvimento de ferrovias.",
        "B",
        "**Etapa 1:** Analisar o fenômeno do niilismo incompleto (ou disfarçado): adorar a ciência, o Estado ou o dinheiro como se fossem o novo Deus.\n**Etapa 2:** Concluir com a radicalidade nietzschiana: trocar Deus pela 'Deusa Ciência' ou pela 'Pátria' é trocar uma muleta metafísica por outra; o homem permanece na menoridade da heteronomia até que crie seus próprios valores com coragem."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Em Para a Genealogia da Moral, Nietzsche formula uma análise demolidora sobre a psicologia do Castigo: 'A pena tem por efeito aguçar o entendimento, tornar a memória mais longa, inspirar o cálculo da prudência; mas ela não melhora moralmente o criminoso, ela o torna mais cauteloso, mais dissimulado e mais duro.' Qual crítica moderna ao sistema penitenciário essa observação antecipou?",
        "A denúncia de que as prisões utilizavam celas com fechaduras de latão que poderiam ser abertas por gazuas de ferro.",
        "A constatação de que a prisão retributiva e a punição carcerária violenta não despertam a consciência moral sincera nem reabilitam o sujeito, funcionando apenas como uma escola de frieza, astúcia criminosa e endurecimento do caráter contra o Estado.",
        "A comprovação de que as prisões estaduais deveriam ser construídas exclusivamente em terrenos arenosos próximos ao mar.",
        "A exigência de que os detentos em cumprimento de pena devam receber remunerações pagas em barras de ferro fundido.",
        "A afirmação de que os guardas penitenciários deveriam ser treinados em técnicas de oratória e declamação poética.",
        "B",
        "**Etapa 1:** Analisar a desconstrução da eficácia pedagógica da punição física e da prisão na psicologia genealógica.\n**Etapa 2:** Concluir com a penologia crítica: a violência do Estado gera cinismo e cálculo de defesa, jamais arrependimento virtuoso; o carrasco e o carcereiro apenas domesticam o medo, ensinando o infrator a esconder o dolo com maior dissimulação."
    ))

    questoes_brutas.append((
        52, "EM13CHS502", "dificil",
        "Ao examinar a relação entre o Além-do-Homem (Übermensch) e a Terra em Assim Falou Zaratustra, qual exortação sagrada Zaratustra faz aos seus discípulos logo em seu primeiro discurso público?",
        "'Abandonai vossas cidades e buscai a iluminação nas cavernas das montanhas desertas!'",
        "'Eu vos suplico, meus irmãos, permanecei fiéis à Terra, e não acrediteis naqueles que vos falam de esperanças supraterrenas! São envenenadores, saibam eles disso ou não.'",
        "'Entregai metade de vossas colheitas de trigo aos magistrados civis para que eles comprem armamentos de bronze!'",
        "'Proibi que vossos filhos aprendam a ler livros que tratem de astronomia e de física mecânica!'",
        "'Caminhai sempre descalços pelas ruas de pedra para provar vossa humildade perante os governantes da corte!'",
        "B",
        "**Etapa 1:** Interpretar o mandamento fundante do Übermensch: a fidelidade incondicional à Terra e à imanência corpórea.\n**Etapa 2:** Concluir com o repúdio aos envenenadores de além-mundos: sonhar com céus fictícios é trair e caluniar o único solo sagrado onde a existência se desenrola; a redenção não está no além, mas na transvaloração afirmativa do aqui e agora."
    ))

    questoes_brutas.append((
        53, "EM13CHS501", "dificil",
        "Considere o contraste entre a concepção nietzschiana de 'Vontade de Poder' e a 'Luta pela Sobrevivência' do Darwinismo biológico clássico. Por que Nietzsche afirma que Charles Darwin cometeu um erro capital ao descrever a dinâmica da natureza?",
        "Porque Darwin realizou suas expedições científicas a bordo de barcos que utilizavam motores a vapor com caldeiras fracas.",
        "Porque Darwin enxergava a vida sob a ótica reativa da mera adaptação e defesa da autopreservação estática da espécie (a moral inglesa da carência e da fome), enquanto a natureza em sua essência transborda fartura, esbanjamento de forças e ímpeto soberano de conquista e expansão afirmativa.",
        "Porque as teorias da evolução biológica foram proibidas por decretos governamentais aprovados no parlamento britânico.",
        "Porque Darwin utilizava espécimes de fósseis que haviam sofrido desgaste químico pelo contato com águas marinhas salgadas.",
        "Porque a seleção natural não considerava a quantidade de ovos postos por tartarugas em praias da América do Sul.",
        "B",
        "**Etapa 1:** Confrontar o evolucionismo utilitarista e adaptativo de Darwin com a fisiologia da força de Nietzsche.\n**Etapa 2:** Concluir com a primazia da expansão sobre a mera conservação: os seres vivos não querem apenas não morrer; a vida é generosidade destemida e gasto exuberante de energia; quem pensa apenas em sobreviver já adotou a psicologia do escravo."
    ))

    questoes_brutas.append((
        54, "EM13CHS504", "dificil",
        "Ao analisar os comportamentos coletivos na cultura contemporânea, como a genealogia nietzschiana da moral dos escravos elucida a dinâmica de cancelamentos moralizantes e vigilância punitiva nas redes digitais?",
        "Demonstrando que os trabalhadores urbanos deveriam ser obrigados a dormir em tendas de lona armada em praças municipais.",
        "Evidenciando que indivíduos impotentes de realizar obras afirmativas buscam uma superioridade ética meramente reativa, rotulando qualquer distinção, talento ou excelência alheia como arrogância ou perversidade, encontrando prazer punitivo na desqualificação daquele que se destaca.",
        "Afirmando que os computadores eletrônicos e redes de dados digitais consomem muito combustível fóssil em usinas térmicas.",
        "Determinando que os bancos comerciais devam fechar suas agências durante todos os meses chuvosos do ano civil.",
        "Comprovando que as empresas de tecnologia digital deveriam proibir o uso de teclados alfanuméricos em escritórios.",
        "B",
        "**Etapa 1:** Interpretar a manifestação contemporânea do ressentimento: a fraqueza que se vinga não pela criação afirmativa de potência, mas pelo policiamento moral da grandeza alheia.\n**Etapa 2:** Concluir com a tese do e-book: as redes digitais operam muitas vezes como tribunais da moral dos escravos, nos quais o sujeito inofensivo se declara eticamente superior pelo simples fato de condenar publicamente quem produz e sobressai."
    ))

    questoes_brutas.append((
        55, "EM13CHS102", "dificil",
        "Em Para Além de Bem e Mal (1886), Nietzsche adverte: 'Aquele que luta com monstros deve velar para que, ao fazê-lo, não se transforme ele mesmo em monstro. E se olhares durante muito tempo para um abismo, o abismo também olhará para dentro de ti.' De que maneira essa advertência alerta para os perigos da militância moral cega?",
        "Alertando os caçadores de animais selvagens a utilizarem capacetes de ferro para não serem mordidos por lobos da floresta.",
        "Advertindo que a obsessão apaixonada em combater e destruir o mal moral exterior consome a alma com o próprio veneno do ódio, da intransigência e do ressentimento, fazendo com que o justiceiro acabe adotando os mesmíssimos métodos desumanos e autoritários daquilo que combatia.",
        "Determinando que as patrulhas de infantaria militar devam circular pelas fronteiras acompanhadas de cães farejadores.",
        "Exigindo que os tribunais civis aprovem sentenças de indenização redigidas exclusivamente na língua francesa clássica.",
        "Comprovando que as pessoas que passam muitas horas olhando para o fundo de poços de pedra sofrem de vertigens visuais.",
        "B",
        "**Etapa 1:** Analisar a contaminação psíquica operada pela fixação no combate àquilo que se odeia.\n**Etapa 2:** Concluir com a lucidez nietzschiana: quem se embriaga na cruzada moral contra o 'monstro' é devorado pelo abismo do rancor; a verdadeira nobreza não reside em policiar o mal alheio, mas em criar beleza, luz e força afirmativa a partir de si."
    ))

    questoes_brutas.append((
        56, "EM13CHS501", "dificil",
        "Ao examinar a tese do 'Amor Fati' em Ecce Homo, Nietzsche declara: 'Minha fórmula para a grandeza no ser humano é o amor fati: não querer nada diferente, nem para a frente, nem para trás, nem em toda a eternidade. Não apenas suportar o necessário, menos ainda ocultá-lo, mas amá-lo.' Como essa formulação supera o conformismo resignado do Estoicismo tradicional?",
        "Obrigando os cidadãos a assinarem documentos de fidelidade eterna aos generais comandantes da frota naval.",
        "Diferente da apatheia estóica (que busca a indiferença serena e o desapego frio perante a dor do mundo), o amor fati nietzschiano é paixão afirmativa jubilosa, abraçando o sofrimento com entusiasmo dionisíaco como condição orgânica indissociável da beleza suprema da vida.",
        "Defendendo que as construções residenciais em cidades litorâneas devam ter suas paredes pintadas com cal branca.",
        "Provando que as leis do direito civil romano foram copiadas de inscrições gravadas em placas de mármore persas.",
        "Determinando que as festas cívicas devam celebrar exclusivamente a chegada das chuvas de primavera nas lavouras.",
        "B",
        "**Etapa 1:** Contrastar a apatia e a mortificação das paixões da Stoa helenística com a afirmação dionisíaca de Nietzsche.\n**Etapa 2:** Concluir com a exaltação da vida: o estóico quer não sofrer anestesiando os afetos; Nietzsche quer viver tudo com intensidade ardente, acolhendo o espinho e a rosa, o veneno e o remédio, em uma celebração divina do destino terreno."
    ))

    questoes_brutas.append((
        57, "EM13CHS502", "dificil",
        "No livro Assim Falou Zaratustra, no discurso 'Dos Desprezadores do Corpo', Zaratustra afirma: 'Há mais razão em teu corpo do que em tua melhor sabedoria.' De que maneira essa proposição desmantela o dualismo metafísico entre mente e corpo inaugurado por René Descartes e sua Res Cogitans?",
        "Negando que os nervos biológicos e os músculos do corpo humano sejam formados por tecidos celulares e sangue.",
        "Evidenciando que o intelecto consciente (o Ego pensante) não é o mestre soberano desincorporado da existência, mas apenas um pequeno instrumento e brinquedo da Grande Razão: a totalidade orgânica sábia do Corpo, de seus instintos e de sua vontade de poder imanente.",
        "Afirmando que os médicos da corte imperial francesa desconheciam as regras de circulação sanguínea no coração.",
        "Determinando que as escolas de primeiras letras devam substituir as aulas de gramática por treinamentos de hipismo militar.",
        "Provando que os tratados de geometria analítica foram redigidos com canetas feitas com penas de gansos selvagens.",
        "B",
        "**Etapa 1:** Desconstruir a ilusão cartesiana da mente transparente separada do corpo material mecanicista.\n**Etapa 2:** Concluir com a virada fisiológica de Nietzsche: a alma é apenas uma palavra para designar algo no corpo; a verdadeira inteligência reside nas pulsões, na respiração, na digestão e na saúde viva do organismo que pensa encarnado na Terra."
    ))

    questoes_brutas.append((
        58, "EM13CHS101", "dificil",
        "Em Para Além de Bem e Mal, Nietzsche faz a seguinte provocação filosófica: 'Supondo que a verdade seja uma mulher — e por que não? — não seria justificada a suspeita de que todos os filósofos, enquanto foram dogmáticos, entenderam muito mal as mulheres?' O que expressa essa metáfora brilhante sobre a arrogância do dogmatismo filosófico ocidental?",
        "Que as mulheres da Antiguidade clássica eram proibidas por leis cívicas de estudarem astronomia e física mecânica.",
        "Que a verdade não se deixa capturar por fórmulas dogmáticas rígidas, violências conceituais ou sistemas metafísicos fechados; ela exige a arte da sedução, o respeito ao mistério, a agudeza da perspectiva e a consciência de que toda certeza absoluta é apenas uma máscara grosseira da vaidade racionalista.",
        "Que os tratados de lógica formal deveriam ser publicados em volumes encadernados com tecidos de seda importada.",
        "Que os magistrados de tribunais civis devem consultar adivinhos antes de proferirem sentenças sobre partilha de terras.",
        "Que os filósofos da Europa central desconheciam as regras de etiqueta palaciana das cortes reais da França.",
        "B",
        "**Etapa 1:** Interpretar a metáfora nietzschiana da verdade como mulher que recusa o assédio canhestro e arrogante do dogmático.\n**Etapa 2:** Evidenciar o perspectivismo e o fim do absolutismo: o filósofo autêntico sabe que a realidade é devir multifacetado; pretender aprisionar a verdade em um sistema eterno é a ilusão patética de quem não entendeu a complexidade viva da existência."
    ))

    questoes_brutas.append((
        59, "EM13CHS501", "dificil",
        "No terceiro tratado da Genealogia da Moral, Nietzsche formula a perturbadora indagação: 'Que significam ideais ascéticos?'. Ao analisar como até mesmo a Ciência Moderna e o Ateísmo secular continuam prisioneiros do ideal ascético, qual denúncia surpreendente o filósofo formula?",
        "A de que os laboratórios de química analítica utilizavam microscópios ópticos que consumiam muita energia elétrica.",
        "A de que a ciência moderna, ao adorar a 'Verdade' como um ídolo inquestionável pelo qual o homem deve sacrificar seus desejos e submeter-se com fanatismo asséptico, mantém viva a fé ascética milenar na negação do erro, da ilusão e da perspectiva vital, operando como a forma mais refinada e sutil do próprio cristianismo.",
        "A de que os astrônomos de universidades públicas eram obrigados a pertencer a ordens monásticas da Igreja católica.",
        "A de que as pesquisas sobre vacinas contra doenças infecciosas deveriam ser financiadas exclusivamente com moedas de ouro.",
        "A de que os livros de física e química foram redigidos por monges que viviam em conventos isolados nas montanhas.",
        "B",
        "**Etapa 1:** Analisar o aforismo sobre a ciência como o mais recente disfarce do ideal ascético.\n**Etapa 2:** Concluir com a genealogia da fé na verdade: a ciência acredita na verdade com a mesma fé cega com que o cristão acredita em Deus; ela ainda não colocou em questão o *valor* da verdade e o papel da ilusão na manutenção e no florescimento da vida."
    ))

    questoes_brutas.append((
        60, "EM13CHS502", "dificil",
        "Analise a seguinte passagem de Assim Falou Zaratustra: 'O homem é algo que deve ser superado. Que fizestes vós para superá-lo? Todas as criaturas até agora criaram algo acima de si mesmas: e vós quereis ser o refluxo dessa grande maré, e preferis retornar ao animal do que superar o homem?' Qual imperativo ético da grande saúde essa convocação poética consagra para o futuro da cultura?",
        "A obrigação de que todos os cidadãos trabalhem na agricultura irrigada para aumentar os estoques de grãos de trigo.",
        "A recusa categórica em conformar-se com a mediocridade anestesiada do homem domesticado e o chamado sublime à autossuperação contínua da própria subjetividade, forjando uma existência que seja uma obra de arte criadora e afirmativa de novos sentidos para além do rebanho.",
        "A necessidade de construir muralhas de pedra ao redor de todas as capitais europeias para impedir invasões militares.",
        "A exigência de que os jovens estudantes decorem listas de batalhas navais travadas no mar Egeu durante a Antiguidade.",
        "A determinação de que as assembleias municipais aprovem calendários anuais com mais de quatrocentos feriados cívicos.",
        "B",
        "**Etapa 1:** Interpretar o conceito de 'Grande Saúde' e superação de si (*Selbstüberwindung*) como motor da vida nobre.\n**Etapa 2:** Concluir com o telos afirmativo de Zaratustra: a evolução humana não parou no animal racional moderno domesticado; o dever supremo do espírito livre é esculpir a si mesmo como um novo começo, gerando valores que honrem a Terra e dignifiquem o destino humano."
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
capitulo: "cap-13-nietzsche-genealogia-moral-niilismo"
objeto_de_conhecimento: "O método genealógico, a moral dos senhores e dos escravos, o ressentimento, a morte de Deus, as tipologias do niilismo, a vontade de poder, o Übermensch e o eterno retorno"
ebook_fonte: "em-fil-c13-nietzsche-genealogia-moral-niilismo.md"
habilidades: "EM13CHS101, EM13CHS102, EM13CHS501, EM13CHS502, H23, H24, H25"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: Nietzsche: Genealogia da Moral e Niilismo

"""

    corpo = header
    slug_cap = "cap-13-nietzsche-genealogia-moral-niilismo"

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

- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.
- MARTON, Scarlett. *Nietzsche: das forças cósmicas aos valores humanos*. 2. ed. Belo Horizonte: Editora UFMG, 2010.
- NIETZSCHE, Friedrich. *Além do bem e do mal: prelúdio a uma filosofia do futuro*. Tradução de Paulo César de Souza. São Paulo: Companhia das Letras, 2005.
- NIETZSCHE, Friedrich. *A gaia ciência*. Tradução de Paulo César de Souza. São Paulo: Companhia das Letras, 2001.
- NIETZSCHE, Friedrich. *Para a genealogia da moral: uma polêmica*. Tradução de Paulo César de Souza. São Paulo: Companhia das Letras, 1998.
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

    dest_rel = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-13-nietzsche-genealogia-moral-niilismo/ebooks/em-fil-c13-nietzsche-genealogia-moral-niilismo-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_path, dest_rel]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 13 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
