# -*- coding: utf-8 -*-
"""
Gerador das 60 questões atômicas de Filosofia EM - Capítulo 18:
A Invenção da Política Moderna: O Realismo de Maquiavel
Destino: content/medio/volume-unico/filosofia/eixo-3-politica/cap-18-realismo-politico-maquiavel/ebooks/em-fil-c18-realismo-politico-maquiavel-exercicios.md
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
        "Qual foi a ruptura fundamental introduzida por Nicolau Maquiavel na história do pensamento político ocidental?",
        "A subordinação definitiva das leis civis aos mandamentos da teologia cristã medieval.",
        "A emancipação da reflexão política da moralidade religiosa e das utopias metafísicas clássicas, fundando a autonomia da ciência política moderna.",
        "A defesa do retorno aos modelos de monarquia absolutista da Antiguidade oriental.",
        "A proposição de que as cidades fossem governadas exclusivamente por corporações monásticas de monges beneditinos.",
        "A exigência de que os governantes abolissem a cobrança de tributos municipais sobre o comércio de especiarias.",
        "B",
        "Maquiavel separou a política da moral e da teologia: o poder não é dádiva divina nem busca da perfeição platônica, mas um fenômeno terreno de forças e estratégias reais."
    ))

    questoes_brutas.append((
        2, "EM13CHS601", "basico",
        "Como a situação geopolítica da península itálica no início do século XVI influenciou as preocupações teóricas de Maquiavel?",
        "A península era um império unificado e pacífico dotado da maior marinha de guerra do continente.",
        "A península era um mosaico fragmentado em repúblicas e principados rivais, assolado por guerras fratricidas e dependente de tropas mercenárias infiéis, tornando-se presa fácil de invasões estrangeiras.",
        "A Itália vivia sob o controle político exclusivo de conselhos de artesãos tecelões de lã.",
        "Os principados italianos haviam banido o uso de armas de fogo e canhões de ferro fundido.",
        "A região encontrava-se isolada comercialmente do restante do continente europeu por barreiras alfandegárias.",
        "B",
        "A humilhação da Itália, invadida por exércitos estrangeiros e dilacerada por conflitos internos, fez Maquiavel buscar a verdade crua do poder para libertar e unificar a pátria."
    ))

    questoes_brutas.append((
        3, "EM13CHS102", "basico",
        "Qual cargo público Nicolau Maquiavel exerceu durante o período republicano de Florença antes de sua prisão e exílio?",
        "Sumo Pontífice e administrador de bens da Santa Sé em Roma.",
        "Segundo Chanceler e diplomata da República de Florença, atuando em missões internacionais perante cortes europeias.",
        "Comandante supremo de regimentos de cavalaria pesada do exército imperial.",
        "Juiz de apelações eclesiásticas em tribunais da inquisição regional.",
        "Inspetor de obras públicas e pontes fluviais no vale do rio Arno.",
        "B",
        "Por catorze anos, Maquiavel vivenciou os bastidores da alta política e da diplomacia europeia, acumulando a experiência prática que fundamentou suas obras."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "O que Maquiavel quer dizer com a expressão 'Verdade Efetiva das Coisas' (verità effettuale della cosa) no capítulo XV de O Príncipe?",
        "Que a política deve ser guiada por revelações místicas anunciadas por profetas bíblicos.",
        "Que a análise do poder deve se basear na observação empírica de como os homens agem concretamente na realidade histórica, e não em como deveriam idealmente agir.",
        "Que os governantes devem organizar plebiscitos semanais para auscultar a opinião dos sacerdotes.",
        "Que os códigos de leis devem ser redigidos em versos rimados de poesia lírica.",
        "Que as decisões diplomáticas precisam aguardar o alinhamento favorável dos corpos celestes.",
        "B",
        "A verità effettuale é a recusa dos mundos ideais imaginados: quem despreza o que se faz pelo que se deveria fazer aprende sua própria ruína em meio a homens imperfeitos."
    ))

    questoes_brutas.append((
        5, "EM13CHS601", "basico",
        "O que eram os 'Espelhos de Príncipes' (specula principum) medievais que Maquiavel rejeitou expressamente?",
        "Instrumentos ópticos de vidro espelhado utilizados por reis para inspecionar trajes de gala.",
        "Manuais morais e teológicos que prescreviam aos governantes uma conduta de santidade, caridade e humildade cristã abstrata.",
        "Tratados de astronomia que previam o movimento dos planetas em torno do Sol.",
        "Manuais de esgrima e duelo com espadas de aço forjado para nobres cavaleiros.",
        "Compêndios de jurisprudência marítima para o comércio com portos do mar Mediterrâneo.",
        "B",
        "Maquiavel rompeu com a ilusão dos espelhos de príncipes: o governante que busca ser bondoso em todas as ocasiões é aniquilado por adversários impiedosos."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Ao examinar o comportamento dos súditos perante o poder temporal, o diplomata florentino recusa qualquer ilusão piedosa sobre a bondade espontânea da sociedade. Como a antropologia realista formulada no texto de 1513 caracteriza os traços predominantes da conduta humana comum?",
        "Os seres humanos são santos benevolentes que buscam a caridade espontânea e o perdão mútuo.",
        "Os homens são, em geral, ingratos, volúveis, simuladores e dissimuladores, covardes diante do perigo e ávidos de lucro.",
        "A humanidade é constituída exclusivamente por sábios que renunciam aos bens materiais.",
        "Os homens são dotados de inclinação inata e inabalável para o cumprimento de pactos verbais.",
        "A natureza humana é puramente angelical, tornando as leis penais desnecessárias.",
        "B",
        "Maquiavel não tem ilusões piedosas sobre a antropologia humana: governar exige reconhecer a volatilidade e o egoísmo dos indivíduos para evitar traições."
    ))

    questoes_brutas.append((
        7, "EM13CHS602", "basico",
        "Quais são os dois 'Humores Sociais' opostos e fundamentais que habitam qualquer cidade, segundo Maquiavel?",
        "O humor dos pescadores de alto-mar e o humor dos carpinteiros navais.",
        "O humor dos Grandes (que desejam comandar e oprimir) e o humor do Povo (que deseja não ser comandado nem oprimido).",
        "O humor dos astrônomos da corte e o humor dos alquimistas de laboratório.",
        "O humor dos guardas municipais e o humor dos cocheiros de diligências urbanas.",
        "O humor dos poetas dramáticos e o humor dos cantores de coro sacro.",
        "B",
        "A sociedade é marcada por um conflito irreconciliável: os poderosos buscam dominar, e o povo anseia por liberdade e proteção contra o arbítrio dos grandes."
    ))

    questoes_brutas.append((
        8, "EM13CHS603", "basico",
        "Por que Maquiavel recomenda que o príncipe procure consolidar sua autoridade com base no apoio do Povo e não no dos Grandes?",
        "Porque os cidadãos comuns distribuem donativos em ouro aos ministros do governo.",
        "Porque o desejo do povo é mais honrado (não ser oprimido) e a sua fidelidade é mais sólida, enquanto os grandes se julgam iguais ao soberano e vivem tramando conspirações.",
        "Porque o povo aceita trabalhar sem descanso sem receber alimentos ou abrigo familiar.",
        "Porque as elites nobres residem em ilhas fluviais inacessíveis durante os meses de inverno.",
        "Porque os grandes são impedidos por preceitos canônicos de portarem armas de duelo.",
        "B",
        "O príncipe que se apoia nos ricos está em areia movediça; já o príncipe apoiado no povo possui uma base estável, pois as aspirações populares são justas e protetivas."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "O que significa o conceito de 'Virtù' na formulação política de Maquiavel?",
        "A prática monástica da castidade, do silêncio penitencial e do jejum religioso.",
        "A capacidade estratégica, a inteligência perspicaz, a coragem resoluta e a flexibilidade para agir com eficácia de acordo com a necessidade política.",
        "A recusa absoluta ao exercício de qualquer forma de poder ou autoridade temporal.",
        "A submissão piedosa aos decretos papais e a oração contemplativa em templos sagrados.",
        "A habilidade de confeccionar tapeçarias decorativas para salões de embaixadas.",
        "B",
        "Virtù maquiaveliana não é santidade cristã; é energia política, discernimento da ocasião oportuna e audácia para preservar o Estado e vencer os desafios."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Qual é o significado da categoria 'Fortuna' na obra O Príncipe?",
        "A quantidade exata de moedas de prata guardadas nos cofres do tesouro público.",
        "O acaso, a contingência, o imponderável e as circunstâncias históricas externas que fogem ao controle direto da vontade do governante.",
        "O conjunto de heranças territoriais recebidas por laços de casamento nobre.",
        "A cobrança de juros compostos em empréstimos de banqueiros venezianos.",
        "O lucro mercantil obtido na exportação de tecidos finos para feiras do norte da Europa.",
        "B",
        "A Fortuna é a deusa romana do destino: personifica o imprevisto da história, que pode erguer ou destruir governantes que não souberem enfrentá-la."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Como Maquiavel ilustra o impacto da Fortuna através da metáfora do 'Rio Torrencial' no capítulo XXV?",
        "Comparando a fortuna a um lago calmo onde se pescam trutas de água doce.",
        "Comparando a fortuna a um rio que transborda e destrói tudo em sua enchente, mas cujos danos podem ser prevenidos se homens dotados de virtù construírem diques e canais nos tempos de estiagem.",
        "Defendendo que as navegações fluviais devem ser suspensas durante os períodos de lua cheia.",
        "Mostrando que as águas dos rios secam quando a população deixa de orar aos santos patronos.",
        "Sustentando que os diques de contenção devem ser erguidos exclusivamente com madeira de lei aromática.",
        "B",
        "A virtù constrói barragens preventivas na calmaria: não se pode impedir que o rio encha, mas a previdência e o preparo evitam que a inundação arrase a cidade."
    ))

    questoes_brutas.append((
        12, "EM13CHS102", "basico",
        "No célebre dilema do capítulo XVII de O Príncipe, seria melhor ao governante ser amado ou ser temido?",
        "Ser odiado e desprezado por todos os cidadãos da cidade.",
        "O ideal seria ser ambas as coisas; mas, como é quase impossível conciliar as duas, é muito mais seguro ser temido do que amado.",
        "Ser amado cegamente, dispensando qualquer aparato de tribunais ou forças armadas.",
        "Permanecer indiferente à opinião dos cidadãos e fechar as portas dos palácios.",
        "Delegar todo o comando da segurança pública a conselhos de mercadores estrangeiros.",
        "B",
        "O amor é volúvel e rompido pelo interesse egoísta; o temor é sustentado pelo medo da punição, um sentimento implacável que nunca falha ao governante."
    ))

    questoes_brutas.append((
        13, "EM13CHS601", "basico",
        "Qual advertência imperativa Maquiavel faz ao soberano para que o temor não se transforme em ódio?",
        "Aumentar o valor das multas de trânsito cobradas de carroças mercantes.",
        "Jamais atentar contra o patrimônio particular dos governados nem violar as suas famílias e mulheres.",
        "Proibir a realização de festividades carnavalescas nas praças públicas municipais.",
        "Obrigar todos os artesãos a vestirem túnicas pretas durante as sessões plenárias.",
        "Exigir que as propriedades rurais cultivem apenas cereais de grão miúdo.",
        "B",
        "O ódio destrói o soberano: quem perde seus bens ou tem sua família ultrajada busca vingança mortal; o príncipe deve ser severo, mas respeitar as propriedades e os lares."
    ))

    questoes_brutas.append((
        14, "EM13CHS602", "basico",
        "Por que Maquiavel sentencia que 'os homens esquecem mais depressa a morte do pai do que a perda do patrimônio'?",
        "Porque os ritos funerários da Renascença duravam apenas três horas consecutivas.",
        "Porque o luto familiar é apaziguado pelo tempo, enquanto a ruína material e a perda de bens continuam a golpear e empobrecer a família cotidianamente, alimentando o rancor contra o governante confisco.",
        "Porque as certidões de óbito eram emitidas em folhas de pergaminho de baixa durabilidade.",
        "Porque as propriedades rurais eram isentas do pagamento de dízimos eclesiásticos.",
        "Porque a legislação romana garantia heranças automáticas aos tios maternos.",
        "B",
        "A dor da perda patrimonial é permanente e gera inimigos irreconciliáveis; por isso, o confisco arbitrário é a rota mais rápida para o soberano despertar o ódio popular."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "Para instruir os governantes a respeito dos perigos palacianos e das agressões bélicas, Maquiavel recorre à célebre alegoria dos dois animais selvagens. Quais atributos da fera astuta e do predador feroz devem ser integrados na conduta do soberano prudente?",
        "O governante deve manter animais ferozes aprisionados em jaulas no pátio do palácio.",
        "O soberano precisa combinar a astúcia da raposa (para identificar armadilhas e traições nos bastidores) com a força do leão (para amedrontar os lobos e inimigos externos).",
        "O príncipe deve se alimentar unicamente de carnes de caça obtidas em florestas alpinas.",
        "O comandante militar deve usar casacos de pele de raposa durante os desfiles de inverno.",
        "Os diplomatas devem imitar os movimentos de felinos para impressionar embaixadores rivais.",
        "B",
        "A força bruta (leão) não percebe os ardis da diplomacia; a astúcia pura (raposa) não resiste ao ataque dos lobos; a virtù do príncipe harmoniza inteligência e vigor."
    ))

    questoes_brutas.append((
        16, "EM13CHS601", "basico",
        "O que a análise historiográfica rigorosa esclarece sobre a célebre frase 'os fins justificam os meios' comumente atribuída a Maquiavel?",
        "Que essa frase foi gravada em letras de ouro no túmulo do filósofo na igreja de Santa Cruz.",
        "Que Maquiavel jamais escreveu essa frase literal em nenhuma de suas páginas, sendo ela uma simplificação moralista equivocada de sua análise sobre a razão de Estado e a preservação da comunidade.",
        "Que a expressão foi retirada de um discurso que Maquiavel proferiu perante a corte imperial alemã.",
        "Que o autor exigia que a frase fosse decorada por todos os jovens aprendizes de alfaiate.",
        "Que a citação foi redigida originalmente em árabe clássico por tradutores andaluzes.",
        "B",
        "A frase literal nunca existiu em Maquiavel; o autor afirmou que, nas ações humanas, julga-se o resultado de salvar a pátria e que os meios adequados a esse fim nobre serão honrados."
    ))

    questoes_brutas.append((
        17, "EM13CHS102", "basico",
        "Ao examinar a conduta do tirano Agátocles de Siracusa no capítulo VIII de O Príncipe, qual distinção crucial Maquiavel estabelece?",
        "Que Agátocles foi o maior estrategista militar de toda a história mediterrânica.",
        "Que trair companheiros, assassinar concidadãos e agir sem palavra e sem piedade pode proporcionar a conquista do poder bruto, mas não pode conferir verdadeira glória nem honra perante a história.",
        "Que o tirano de Siracusa deveria ter sido canonizado pelo Papa como defensor da cristandade.",
        "Que o confisco de terras comunais foi uma medida correta para subsidiar companhias navais.",
        "Que as crueldades praticadas por prazer sádico devem ser elogiadas pelos historiadores.",
        "B",
        "Maquiavel condena a violência estéril e vaidosa: a força só é legítima quando estritamente necessária para evitar o caos social; o massacre gratuito desonra o líder."
    ))

    questoes_brutas.append((
        18, "EM13CHS602", "basico",
        "Qual é o cerne da reflexão política desenvolvida por Maquiavel em sua consagrada obra Discursos sobre a Primeira Década de Tito Lívio?",
        "A apologia da ditadura imperial absoluta como forma perfeita e definitiva de governo civil.",
        "A defesa do modelo republicano democrático e a tese de que o conflito cívico institucionalizado entre plebeus e aristocratas foi a fonte da liberdade e grandeza de Roma.",
        "A exigência de que todas as repúblicas modernas adotassem o latim arcaico como língua cotidiana.",
        "A proposta de restauração do Senado feudal subordinado a bispos católicos.",
        "A condenação da participação popular na formulação das leis de cidades italianas.",
        "B",
        "Nos Discursos, Maquiavel revela sua alma republicana: o melhor governo é a república com leis firmes e participação popular ativa, onde a discórdia regrada fortalece a cidadania."
    ))

    questoes_brutas.append((
        19, "EM13CHS603", "basico",
        "Qual instituição da República Romana clássica é enaltecida por Maquiavel como escudo vital dos direitos do povo contra os abusos do Senado?",
        "A Guarda Pretoriana dos imperadores.",
        "O Tribunato da Plebe (Tribunos da Plebe), que possuía o poder de veto legal sobre decisões abusivas das elites nobres.",
        "O Colégio dos Sacerdotes Áugures.",
        "A Corporação dos Cobradores de Pedágios Fluviais.",
        "O Conselho de Comandantes de Galeras Navais.",
        "B",
        "Os Tribunos da Plebe canalizaram a insubordinação popular em conquistas jurídicas, impedindo que a aristocracia esmagasse as massas trabalhadoras de Roma."
    ))

    questoes_brutas.append((
        20, "EM13CHS501", "basico",
        "Por que Maquiavel criticava asperamente o uso de exércitos mercenários (*condottieri*) pelos governantes de sua época?",
        "Porque os mercenários usavam uniformes de tecido grosseiro que desvalorizavam a corte.",
        "Porque as tropas mercenárias eram desunidas, ambiciosas, indisciplinadas, infiéis e covardes diante do perigo, desertando quando a batalha se tornava difícil.",
        "Porque os capitães mercenários exigiam pagamentos exclusivamente em especiarias da Índia.",
        "Porque os soldados de aluguel recusavam-se a empunhar armas durante os dias de chuva.",
        "Porque a contratação de mercenários violava tratados astronômicos sobre navegação costeira.",
        "B",
        "Tropas mercenárias lutam apenas por soldo vil; para defender a pátria com determinação, o soberano precisa de um exército cívico formado por seus próprios cidadãos."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Como a autonomia da política postulada por Maquiavel subverte a concepção clássica aristotélica da relação entre Ética e Política?",
        "Ao proclamar que a teologia deve ser o tribunal final de todas as disputas legislativas.",
        "Ao separar a lógica da sobrevivência do Estado das virtudes da vida privada, estabelecendo que a política possui normas, dinâmicas e exigências próprias que não se confundem com a moral individual.",
        "Ao exigir que os magistrados se recolham a conventos contemplativos antes de lavrarem decisões penais.",
        "Ao provar que a polis grega dependia exclusivamente de monarquias absolutistas de linhagem.",
        "Ao determinar que os soldados devam professar votos monásticos de silêncio e renúncia material.",
        "B",
        "Para Aristóteles, a política é a extensão direta da ética visando o Bem Comum; para Maquiavel, a política tem suas próprias leis de conservação do poder e da estabilidade pública."
    ))

    questoes_brutas.append((
        22, "EM13CHS601", "intermediario",
        "Na análise de Maquiavel sobre a governança de crises no capítulo VIII de O Príncipe, qual é a regra de ouro referente à aplicação do mal e do bem?",
        "Praticar pequenas injustiças todos os dias para habituar a população ao sofrimento contínuo.",
        "Executar todas as medidas duras e impopulares de uma só vez, no início do mandato, e conceder os benefícios e benesses aos poucos, para que sejam mais valorizados e saboreados.",
        "Distribuir todo o orçamento público em donativos logo na primeira semana de governo.",
        "Adiar indefinidamente as reformas necessárias esperando que os problemas se resolvam espontaneamente.",
        "Entregar o controle fazendário a companhias de comércio naval estrangeiras.",
        "B",
        "O golpe amargo deve ser rápido e concentrado para doer menos no tempo; já as benesses devem ser espaçadas paulatinamente para gerar gratidão contínua nos cidadãos."
    ))

    questoes_brutas.append((
        23, "EM13CHS102", "intermediario",
        "Como a conferência 'A Política como Vocação' (1919) do sociólogo Max Weber dialoga diretamente com o realismo de Maquiavel?",
        "Afirmando que os governantes republicanos devem abandonar o parlamento para viver como ascetas.",
        "Formulando a distinção entre a 'Ética da Convicção' (dos princípios dogmáticos incondicionais) e a 'Ética da Responsabilidade' (que avalia as consequências reais das decisões para a preservação do Estado).",
        "Defendendo que a economia industrial deve ser planificada por guildas medievais de tecelões.",
        "Rejeitando o uso de qualquer força policial na repressão de crimes violentos nas cidades.",
        "Sustentando que os tratados diplomáticos devem ser firmados sob juramentos religiosos solenes.",
        "B",
        "Weber bebe na fonte maquiaveliana: quem atua na política não pode se refugiar na pureza moral de belas intenções; deve responder pelas consequências concretas do uso do poder."
    ))

    questoes_brutas.append((
        24, "EM13CHS602", "intermediario",
        "De que modo a reaproximação diplomática entre os Estados Unidos e a China comunista em 1972 exemplifica a aplicação da Realpolitik maquiaveliana?",
        "Comprovando que os dois países compartilhavam os mesmos ideais religiosos de fraternidade cristã.",
        "Evidenciando que razões estratégicas de sobrevivência nacional e isolamento geopolítico da União Soviética se sobrepuseram às abismais divergências ideológicas e morais entre os dois regimes.",
        "Demonstrando que os diplomatas chineses aceitaram adotar a Constituição dos Estados Unidos.",
        "Mostrando que o comércio de seda e chá foi a única motivação para o cessar-fogo no Pacífico.",
        "Exigindo que os presidentes das duas nações disputassem um torneio esportivo de esgrima naval.",
        "B",
        "A Realpolitik é Maquiavel em ação: governos põem de lado dogmas doutrinários para firmar pactos com rivais em nome do interesse vital e estratégico da segurança do Estado."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "De acordo com Maquiavel nos Discursos, por que o conflito social em Roma não causou a destruição da república, mas sim a sua ampliação democrática?",
        "Porque os cidadãos romanos eram proibidos por lei de expressar opiniões dissidentes nas praças.",
        "Porque o conflito encontrou canais institucionais republicanos legítimos (como o Tribunato da Plebe), transformando as tensões entre classes em leis protetivas que asseguraram a liberdade cívica.",
        "Porque o Senado distribuía alimentos importados gratuitamente a todos os escravizados do campo.",
        "Porque os generais do exército dissolviam as assembleias sempre que havia divergências verbais.",
        "Porque a religião pagã ordenava que os plebeus se submetessem passivamente aos ditames nobres.",
        "B",
        "Maquiavel inverte a visão tradicional: a discórdia civil regrada por instituições não é fraqueza, mas a fonte viva da liberdade e dos direitos conquistados pelo povo."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Qual é a proporção de influência que Maquiavel atribui respectivamente à Fortuna e à Virtù no destino humano e político?",
        "A fortuna governa 100% dos eventos terrenos, restando ao ser humano aceitar o destino com resignação.",
        "A fortuna arbitra cerca de metade das ações humanas, mas deixa a outra metade — ou quase — sob a governança e o comando da virtù dos homens de ação.",
        "A virtù humana anula completamente qualquer interferência da contingência e do acaso cósmico.",
        "A fortuna só tem efeito sobre o clima e as colheitas agrícolas, não afetando os governos civis.",
        "O destino dos povos é governado exclusivamente por conjunções astrais mapeadas por astrólogos.",
        "B",
        "Maquiavel recusa o fatalismo paralisante: o acaso existe e desafia o homem, mas a coragem estratégica e a preparação inteligente (virtù) decidem o rumo da história."
    ))

    questoes_brutas.append((
        27, "EM13CHS601", "intermediario",
        "Em que sentido Jean-Jacques Rousseau e Baruch Spinoza afirmaram que O Príncipe de Maquiavel é, na verdade, um 'livro de republicanos'?",
        "Afirmando que o autor foi contratado para redigir o código civil da confederação suíça.",
        "Sustentando que, ao ensinar cinicamente aos monarcas todos os artifícios e ardis do poder autoritário, Maquiavel estava secretamente desmascarando a tirania e educando os povos sobre como os déspotas agem.",
        "Argumentando que o texto pretendia abolir todas as formas de tribunais criminais da Europa.",
        "Defendendo que a obra propunha a extinção imediata de todas as forças de infantaria cívica.",
        "Provando que o livro foi censurado por conspiradores aristocratas contrários ao teatro cômico.",
        "B",
        "Ao desnudar os bastidores do poder sem hipocrisia piedosa, Maquiavel entregou aos cidadãos a lente crítica para enxergar as manobras dos dominadores e defender a liberdade."
    ))

    questoes_brutas.append((
        28, "EM13CHS602", "intermediario",
        "Como a história da promulgação de leis sociais e protetivas no Brasil (como o ECA e a Lei Maria da Penha) ilustra a tese maquiaveliana sobre o atrito cívico?",
        "Provando que as leis foram concedidas por pura benevolência espontânea das elites parlamentares.",
        "Demonstrando que tais conquistas democráticas nasceram da mobilização coletiva, dos protestos e da pressão incessante de movimentos populares e feministas sobre o Estado brasileiro.",
        "Evidenciando que a legislação foi imposta por tribunais internacionais de comércio marítimo.",
        "Mostrando que a cidadania brasileira resulta exclusivamente de decretos monárquicos imperiais.",
        "Indicando que a harmonia passiva e a ausência de reivindicações são as geradoras dos direitos humanos.",
        "B",
        "Assim como a plebe romana arrancou seus direitos por meio da resistência e da contestação, os avanços na cidadania brasileira resultam da coragem e das lutas cívicas da sociedade."
    ))

    questoes_brutas.append((
        29, "EM13CHS102", "intermediario",
        "Por que o florentino condena governantes que tentam se manter numa posição de 'Neutralidade Hesitante' diante de disputas entre vizinhos poderosos?",
        "Porque os tratados internacionais exigem a cobrança de tributos aduaneiros uniformes.",
        "Porque quem permanece neutro torna-se presa certa do vencedor com o desprezo e ódio do perdedor, não conquistando aliados fiéis nem respeito por sua determinação militar.",
        "Porque a legislação romana obrigava os magistrados a realizarem casamentos consanguíneos.",
        "Porque os astrólogos da corte recomendavam alianças exclusivas com navegadores oceânicos.",
        "Porque as assembleias cívicas suspendiam a cunhagem de moedas em anos de neutralidade.",
        "B",
        "O príncipe indeciso que foge de tomar partido para tentar agradar a todos é abandonado por ambos os lados na crise; a política exige clareza e determinação audaciosa."
    ))

    questoes_brutas.append((
        30, "EM13CHS601", "intermediario",
        "Qual é a função sociopolítica da Religião na análise de Maquiavel em O Príncipe e nos Discursos?",
        "Garantir a salvação mística das almas dos crentes após a morte física no paraíso.",
        "Atuar como um vigoroso instrumento cívico de coesão comunitária (instrumentum regni), inspirando disciplina, lealdade à pátria, respeito aos juramentos e valor militar.",
        "Promover o isolamento dos cidadãos em retiros de oração silenciosa fora das cidades.",
        "Proibir a fabricação de lanças e armaduras de metal por artesãos municipais.",
        "Submeter os exércitos nacionais ao comando direto de monges mendicantes.",
        "B",
        "Maquiavel não vê a fé sob o prisma teológico, mas sob a ótica civil: a religião romana ensinava a bravura e a união da cidade; a fé instrumentalizada consolida o respeito à lei."
    ))

    questoes_brutas.append((
        31, "EM13CHS603", "intermediario",
        "O que Maquiavel critica na interpretação predominante do Cristianismo medieval em comparação com os valores cívicos da Antiguidade clássica?",
        "O uso do latim litúrgico nas cerimônias dominicais de consagração de templos.",
        "A exaltação da humildade, do sofrimento resignado, da contemplação passiva e do desprezo pelo mundo terreno, que tornou os homens fracos e fáceis presas para tiranos desalmados.",
        "A celebração festiva da colheita de trigo nas paróquias rurais do norte italiano.",
        "A construção de catedrais com arcos ogivais e vitrais de cristal colorido.",
        "A organização de peregrinações fluviais para santuários localizados na foz de rios.",
        "B",
        "Ao glorificar a fraqueza e a submissão, a fé medieval desarmou o cidadão; Maquiavel admira os antigos, cuja fé enaltecia a força viril, a glória cívica e a defesa ativa da pátria."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Como a peça teatral cômica A Mandrágora (La Mandragola), de autoria de Maquiavel, dialoga com sua visão política realista?",
        "Apresentando fábulas morais sobre princesas encantadas que salvam reinos pacíficos.",
        "Retratando de forma satírica, lúcida e mordaz a hipocrisia, a corrupção de costumes e os interesses mesquinhos das elites nobres e do clero de sua Florença natal.",
        "Ensinando técnicas de navegação marítima e cartografia para comerciantes de lã.",
        "Celebrando a perfeição das leis imperiais germânicas aplicadas em feiras rurais.",
        "Demonstrando que a poesia mística cura enfermidades infecciosas em hospitais urbanos.",
        "B",
        "Tanto no teatro quanto na ciência política, Maquiavel arranca o véu da falsa santidade para mostrar as fraquezas, vaidades e cálculos egoístas que movem a sociedade real."
    ))

    questoes_brutas.append((
        33, "EM13CHS102", "intermediario",
        "Por que, para Maquiavel, o príncipe que necessita recorrer à crueldade deve fazê-lo 'Bem Usada' e não 'Mal Usada'?",
        "Porque as sentenças judiciais devem ser redigidas em versos poéticos para encantar os réus.",
        "Porque a violência bem usada é aplicada de uma só vez, por necessidade imperativa de segurança, e não se prolonga, convertendo-se logo em benefícios públicos; enquanto a mal usada se repete e cresce com o tempo.",
        "Porque os carrascos municipais devem receber gratificações salariais pagas em linho fino.",
        "Porque as celas prisionais devem ser decoradas com afrescos de pinturas bucólicas.",
        "Porque o soberano deve convidar os parentes dos condenados para banquetes cerimoniais.",
        "B",
        "A crueldade mal usada não cessa e gera paranoia no governante e revolta no povo; a violência cirúrgica pontual estanca o caos e abre espaço para a ordem restaurada."
    ))

    questoes_brutas.append((
        34, "EM13CHS601", "intermediario",
        "Como o capítulo XXVI de O Príncipe ('Exortação para libertar a Itália das mãos dos bárbaros') inspirou os movimentos de unificação italiana no século XIX (Risorgimento)?",
        "Propondo a colonização imediata de territórios ultramarinos no hemisfério sul.",
        "Convertendo-se em um manifesto patriótico profético de afirmação da soberania nacional contra a humilhação do domínio e ocupação militar estrangeira.",
        "Defendendo a adesão irrestrita das cidades italianas ao Santo Império Romano Germânico.",
        "Exigindo o desmantelamento de todas as academias de ciências de Roma e Nápoles.",
        "Estabelecendo a obrigatoriedade da celebração anual dos jogos olímpicos gregos.",
        "B",
        "Líderes do Risorgimento como Mazzini e Garibaldi viram em Maquiavel o pioneiro que já no século XVI clamou pela redenção patriótica da Itália unida e livre de invasores."
    ))

    questoes_brutas.append((
        35, "EM13CHS602", "intermediario",
        "De acordo com a antropologia maquiaveliana, por que os homens apoiam o governante em tempos de paz e prosperidade, mas podem rebelar-se em momentos de extrema adversidade?",
        "Porque as leis cívicas prescrevem a troca obrigatória de governantes a cada biênio.",
        "Porque os vínculos baseados puramente na gratidão egoísta dissolvem-se quando os indivíduos sentem seus interesses imediatos ameaçados pela carência ou pelo medo da morte.",
        "Porque os cidadãos perdem o entusiasmo esportivo com corridas de cavalos na arena.",
        "Porque os mercadores estrangeiros compram os votos das assembleias populares com seda.",
        "Porque as monarquias renascentistas suspendiam o abastecimento de pão durante o outono.",
        "B",
        "A lealdade humana ordinária é contingente ao benefício próprio: quando o custo da fidelidade fica alto na crise, os pactos de palavras são abandonados sem remorso."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Qual é a postura de Maquiavel sobre a 'Aparência' e a 'Simulação' no exercício do poder pelo governante?",
        "O príncipe deve sempre agir com absoluta candura e revelar todos os seus planos secretos em praça pública.",
        "Não é necessário ao príncipe ter todas as qualidades nobres (piedade, fidelidade, integridade), mas é indispensável parecer tê-las, pois a maioria julga pelos olhos e poucos tocam a realidade das coisas.",
        "O soberano deve usar máscaras de madeira entalhada em todas as cerimônias de recepção consular.",
        "Os magistrados devem proibir o espelhamento de imagens em lagos e fontes municipais.",
        "Os cortesãos devem se comunicar unicamente por sinais manuais de linguagem cifrada.",
        "B",
        "Na política, a imagem pública é capital de poder: o povo julga pelo que vê; o príncipe deve dominar a arte de parecer íntegro e virtuoso para manter a autoridade moral perante a multidão."
    ))

    questoes_brutas.append((
        37, "EM13CHS603", "intermediario",
        "Por que a 'Flexibilidade Moral' é considerada uma virtude mestra para o estadista maquiaveliano?",
        "Porque o soberano deve trocar de convicções religiosas a cada estação do ano agrícola.",
        "Porque um líder de índole imutável que tenta aplicar as mesmas fórmulas morais em tempos pacíficos e em conjunturas de guerra violenta caminha fatalmente para o fracasso e a ruína de seu povo.",
        "Porque as normas constitucionais devem ser queimadas após a posse de novos governantes.",
        "Porque os generais devem combater usando estratégias sorteadas por dados de osso.",
        "Porque os tesouros públicos devem ser aplicados em investimentos fabris no exterior.",
        "B",
        "O mundo muda constantemente e a fortuna sopra em direções imprevisíveis; o príncipe sábio sabe moldar seu agir à necessidade dos tempos, sendo flexível para vencer."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "Ao examinar a conduta de César Bórgia (Duque Valentino) em O Príncipe, o que Maquiavel destaca como exemplo de virtù estratégica?",
        "A sua humildade ao renunciar ao comando de tropas e refugiar-se em mosteiros alpinos.",
        "A sua determinação implacável para pacificar a Romanha, eliminar capitães mercenários rebeldes e instituir tribunais civis eficientes para conquistar a lealdade da população.",
        "A doação de todos os seus bens e castelos para guildas de pedreiros da Toscana.",
        "A nomeação de filósofos platônicos para o comando de frotas marítimas mercantes.",
        "A recusa sistemática em portar armaduras de aço em cerimônias de condecoração militar.",
        "B",
        "César Bórgia usou a energia resoluta e a inteligência tática para criar ordem onde havia banditismo, exemplificando a ação firme necessária para forjar um Estado moderno."
    ))

    questoes_brutas.append((
        39, "EM13CHS601", "intermediario",
        "Como a distinção entre a moral individual e o agir político em Maquiavel fundamenta a moderna doutrina da 'Razão de Estado'?",
        "Proclamando que o cidadão comum tem licença para cometer delitos patrimoniais.",
        "Estabelecendo que a salvação, a soberania e a segurança do corpo coletivo da sociedade constituem a lei suprema que justifica decisões estatais extraordinárias vedadas aos indivíduos na vida privada.",
        "Exigindo que os governantes sejam julgados por comitês de vizinhança paroquial.",
        "Defendendo que as forças policiais sejam desarmadas em períodos de insurreição civil.",
        "Determinando que os diplomatas firmem acordos internacionais utilizando moedas de barro.",
        "B",
        "A Razão de Estado (salus publica suprema lex) dita que o estadista não atua em nome do próprio ego, mas da comunidade inteira; seu dever prioritário é a defesa e sobrevivência da pátria."
    ))

    questoes_brutas.append((
        40, "EM13CHS501", "intermediario",
        "Por que Maquiavel considera o governo de uma República mais resistente e perene a longo prazo do que o governo de um Principado individual?",
        "Porque as repúblicas contam com maior número de embarcações fluviais para o comércio.",
        "Porque a república comporta uma multiplicidade de cidadãos com temperamentos, saberes e habilidades diversas, sendo mais capaz de se adaptar às mudanças de conjuntura da fortuna do que um único príncipe de conduta rígida.",
        "Porque as eleições populares eliminam completamente a existência de tributos sobre bens de consumo.",
        "Porque os cidadãos republicanos trabalham sem exigir o pagamento de salários semanais.",
        "Porque as decisões legislativas em repúblicas são tomadas mediante leitura de cartas celestes.",
        "B",
        "Um príncipe sozinho tem seu temperamento fixo; já a república dispõe da riqueza e variedade dos seus cidadãos: na crise elege o audacioso, na calmaria elege o prudente, adaptando-se melhor aos tempos."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60 - Com Etapas 1 e 2)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a ruptura entre a concepção finalista clássica da política (Platão e Aristóteles) e o realismo imanente de Nicolau Maquiavel: de que modo a substituição da busca pelo 'Bem Supremo' pela análise da 'Preservação do Poder' transformou o estatuto da teoria política?",
        "Afirmando que a felicidade dos cidadãos decorre da contemplação de obras teatrais clássicas.",
        "Deslocando a reflexão política do plano normativo idealizado (como os homens deveriam agir em uma cidade perfeita) para o plano descritivo empírico e funcional (como o poder é conquistado, exercido e mantido na materialidade concreta da história humana), tornando a política uma ciência autônoma das forças sociais reais.",
        "Comprovando que as constituições democráticas antigas foram redigidas por navegadores de ilhas jônicas.",
        "Determinando que as assembleias cívicas devam realizar consultas oraculares a templos sagrados.",
        "Estabelecendo que as forças de segurança pública devam ser subordinadas a ordens religiosas mendicantes.",
        "B",
        "- **Etapa 1:** Identificar o paradigma clássico normativo: para Platão e Aristóteles, a pólis só é legítima se direcionar a alma humana para a virtude e a justiça ideal do Bem Supremo.\n- **Etapa 2:** Evidenciar a revolução empírica maquiaveliana: Maquiavel descarta o dever-ser utópico e funda o realismo; a legitimidade decorre da eficácia em conter o caos, afastar invasores e garantir a segurança coletiva na contingência histórica real."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "No capítulo XVII de O Príncipe, Maquiavel formula seu célebre postulado antropológico: 'Os homens hesitam menos em ofender a quem se faz amar do que a quem se faz temer; pois o amor é sustentado por um laço de gratidão que os homens rompem sempre que lhes convém; mas o temor é mantido pelo medo da punição, que nunca nos abandona.' Analise as implicações desse princípio para a estabilidade da governança pública.",
        "Demonstrando que os tribunais de justiça devem conceder anistia geral a todos os crimes fiscais.",
        "Evidenciando que a ordem institucional e o cumprimento das leis não podem repousar na ingênua aposta na boa-vontade sentimental dos cidadãos, exigindo um arcabouço crível e constante de coerção legal legítima que dissuada a desobediência e a desordem civil.",
        "Determinando que os soberanos devem organizar celebrações festivas com fogueiras matinais.",
        "Provando que as relações diplomáticas entre nações soberanas dispensam a existência de forças de defesa.",
        "Afirmando que os servidores públicos municipais devem fazer juramentos de fidelidade canônica.",
        "B",
        "- **Etapa 1:** Desconstruir a ingenuidade do amor como sustentáculo político: o amor é um afeto dependente da conveniência e do egoísmo particular do indivíduo, rompendo-se na primeira adversidade.\n- **Etapa 2:** Concluir com a necessidade da coerção justa: o medo da penalidade impessoal e firme da lei estabelece a previsibilidade e a ordem pública; quem governa apenas pelo afeto gera anarquia e desmorona perante a primeira crise."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Em Discursos sobre a Primeira Década de Tito Lívio (Livro I, Cap. IV), Maquiavel declara: 'Afirmo que os que condenam os tumultos entre os nobres e a plebe atacam o que foi a causa principal da liberdade de Roma; atentam mais para as desordens que essas comoções provocavam do que para os bons efeitos que geravam.' De que maneira essa tese subverte a visão tradicional sobre a ordem e o conflito social?",
        "Sustentando que os conflitos armados entre facções militares são benéficos mesmo quando incendeiam hospitais.",
        "Demonstrando que o conflito político institucionalizado não é uma anomalia patológica a ser extirpada pela tirania, mas a própria energia vital e criadora do direito público que limita o poder dos dominadores e expande a liberdade cívica republicana.",
        "Determinando que as assembleias populares devem ser fechadas sempre que ocorrerem discordâncias verbais.",
        "Provando que a estabilidade social depende da submissão passiva de todas as classes a decretos imperiais.",
        "Afirmando que as desavenças entre senadores decorriam da escassez de trigo nas feiras portuárias.",
        "B",
        "- **Etapa 1:** Desconstruir o mito clássico da harmonia estática: antes de Maquiavel, filósofos viam a discórdia como veneno mortal que destruía a cidade, defendendo uma paz imposta de cima para baixo.\n- **Etapa 2:** Consagrar o conflito como gerador de liberdade: Maquiavel mostra que a liberdade é filha do choque entre os Grandes e a Plebe; foram as greves e rebeliões do povo que criaram as leis protetivas e a grandeza duradoura de Roma."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Analise a metáfora do centauro Quíron (meio homem e meio cavalo) evocada no capítulo XVIII de O Príncipe: por que o governante deve ser educado nessa dupla natureza animal e racional para enfrentar as contingências do poder?",
        "Porque os monarcas da Renascença deveriam dedicar suas tardes ao treinamento de hipismo de corrida.",
        "Porque o exercício soberano da política opera em duas dimensões inseparáveis: a das leis civis e do diálogo racional (própria do homem) e a da força coercitiva e da sagacidade estratégica (própria da fera), sendo o soberano obrigado a manejar ambas para preservar o Estado.",
        "Porque a legislação clássica grega prescrevia que os juízes criminais usassem arreios de montaria.",
        "Porque as florestas do norte italiano eram habitadas por criaturas mitológicas protegidas por leis florestais.",
        "Porque os generais de brigada deveriam alimentar seus soldados com rações de cevada forrageira.",
        "B",
        "- **Etapa 1:** Interpretar o símbolo do centauro: Quíron educou os grandes heróis da Antiguidade porque conhecia a razão humana e a ferocidade animal das forças naturais.\n- **Etapa 2:** Concluir com a dualidade do poder real: quando a lei e a palavra (homem) são insuficientes diante de conspiradores e inimigos impiedosos, o estadista precisa saber recorrer à força e à astúcia (fera) para salvar a comunidade política da aniquilação."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Ao examinar a relação dialética entre Virtù e Fortuna, de que modo a construção prévia de 'Diques e Barragens' se aplica à moderna gestão de riscos sanitários, climáticos e econômicos por parte de governos contemporâneos?",
        "Determina que os ministérios da fazenda suspendam a arrecadação de tributos em anos bissextos.",
        "Demonstra que governos esclarecidos e dotados de virtù institucional investem preventivamente em ciência, infraestrutura de saneamento, transição energética e reservas orçamentárias nos momentos de normalidade, mitigando os efeitos devastadores de catástrofes climáticas e pandemias imprevisíveis geradas pela contingência histórica.",
        "Exige que as companhias de eletricidade desliguem seus reatores industriais durante tempestades de verão.",
        "Comprova que as crises financeiras mundiais decorrem exclusivamente de desvios morais de cidadãos individuais.",
        "Afirma que a ocorrência de inundações fluviais depende exclusivamente do volume de orações dedicadas aos santos.",
        "B",
        "- **Etapa 1:** Compreender a analogia dos diques: a inundação (fortuna) virá de forma inevitável; quem espera a cheia chegar para pensar no que fazer é varrido pela destruição das águas.\n- **Etapa 2:** Projetar a lição para as políticas públicas: a virtù contemporânea é a capacidade de planejamento estratégico e resiliência estatal; governos prudentes preparam o sistema de saúde, a infraestrutura e a proteção social antes que a tragédia aconteça."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Considere a reflexão de Maquiavel no capítulo XVIII de O Príncipe: 'Um governante prudente não pode nem deve guardar a palavra empenhada quando isso lhe for prejudicial e quando tiverem desaparecido as razões que a fizeram prometer.' Como essa tese desafia o contratualismo ingênuo e funda a soberania da diplomacia internacional contemporânea?",
        "Autorizando os cidadãos individuais a descumprirem contratos comerciais de aluguel residencial.",
        "Evidenciando que os pactos entre potências soberanas vigoram sob a cláusula implícita da alteração substancial das circunstâncias de sobrevivência do Estado (rebus sic stantibus), pois nenhum líder tem o direito de sacrificar a existência de seu povo para manter uma palavra dada a rivais que não cumprem as suas.",
        "Provando que as trocas de embaixadores diplomáticos devem ocorrer anualmente durante o solstício de verão.",
        "Exigindo que os tratados bilaterais de desarmamento sejam assinados em folhas de tecido de algodão cru.",
        "Determinando que as cortes arbitrais internacionais sejam presididas exclusivamente por generais reformados.",
        "B",
        "- **Etapa 1:** Avaliar a conduta dos adversários na arena geopolítica: Maquiavel adverte que, se todos os homens fossem leais e bons, esse preceito seria imoral; mas como muitos são pérfidos e quebram pactos ao sabor do interesse, o governante fiel e ingênuo torna-se vítima de sua própria bondade.\n- **Etapa 2:** Estabelecer a soberania da razão de Estado: o compromisso primordial de um chefe de Estado é a defesa de seus cidadãos; manter um pacto caduco que leva seu país à subjugação e destruição é traição à pátria, não virtude."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Em Discursos sobre Tito Lívio, Maquiavel adverte contra a corrupção moral dos costumes públicos e afirma que 'onde a matéria não está corrompida, os tumultos e escândalos não causam dano; mas onde ela está apodrecida, as melhores leis são inúteis'. O que essa formulação nos ensina sobre os limites institucionais de reformas puramente formais?",
        "Que a impressão de novos manuais de legislação civil é suficiente para restaurar a honestidade de magistrados corruptos.",
        "Que leis e textos constitucionais perfeitos no papel não operam milagres se o tecido social da cidadania estiver degradado pela apatia, pelo cinismo, pelo corporativismo egoísta e pela perda da devoção cívica ao bem público, exigindo a revitalização moral dos costumes cívicos da sociedade.",
        "Que as câmaras legislativas municipais devem terceirizar a redação de seus códigos a bancas estrangeiras.",
        "Que a criminalidade urbana pode ser erradicada mediante a distribuição de diplomas acadêmicos de honra.",
        "Que as eleições republicanas devem ser canceladas em anos que coincidam com o início de secas agrícolas.",
        "B",
        "- **Etapa 1:** Analisar o conceito maquiaveliano de 'matéria corrupta': quando o egoísmo desenfreado e o suborno tomam conta da elite e do povo, a república perde o amor à liberdade e apodrece por dentro.\n- **Etapa 2:** Concluir sobre o limite da lei formal: uma constituição moderna não funciona no vácuo de uma sociedade cínica; a salvação da democracia exige virtude cidadã ativa, sentimento coletivo de corresponsabilidade e instituições capazes de punir exemplarmente os corruptores."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Analise a condenação enfática de Maquiavel ao uso de tropas mercenárias e à dependência de exércitos auxiliares estrangeiros. De que maneira essa crítica estabelece os pilares do conceito moderno de 'Soberania Nacional' e monopólio legítimo da violência?",
        "Sugerindo que as repúblicas devam dispensar totalmente aparatos de defesa armada e viver em pacifismo absoluto.",
        "Demonstrando que um Estado que não dispõe de forças militares próprias formadas por seus próprios cidadãos leais não possui autonomia real nem soberania verdadeira, permanecendo à mercê da ganância de mercenários de aluguel ou da chantagem armada de potências estrangeiras.",
        "Defendendo que as forças de segurança de uma nação devam ser alugadas de guildas mercantis vizinhas.",
        "Exigindo que os comandantes de regimentos de infantaria devam residir em ilhas marítimas fortificadas.",
        "Provando que as armas brancas de combate corpo a corpo são superiores aos canhões de artilharia pesada.",
        "B",
        "- **Etapa 1:** Identificar o vício das armas de aluguel: soldados mercenários não têm afeição pela pátria; em tempos de paz saqueiam o tesouro e em tempos de combate fogem covardemente.\n- **Etapa 2:** Fundar a soberania e a cidadania armada: a defesa da nação deve pertencer ao seu próprio povo; a soberania estatal nasce da capacidade de mobilizar seus próprios cidadãos, que lutam pela preservação de seus lares e de sua república."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Ao examinar a dialética entre os 'Grandes' e o 'Povo' em O Príncipe (Capítulo IX), por que Maquiavel sustenta que é muito mais fácil ao governante conter as ambições dos poderosos apoiando-se no povo do que governar ao lado dos poderosos submetendo o povo?",
        "Porque os cidadãos populares fornecem cereais e tecidos artesanais para o custeio da guarda municipal.",
        "Porque os Grandes são em número reduzido e podem ser vigiados ou neutralizados institucionalmente, enquanto o Povo constitui a imensa maioria da cidade e não pode ser aniquilado nem mantido permanentemente sob rédeas se for tomado pelo ódio contra o governante tirano.",
        "Porque as assembleias populares eram realizadas em anfiteatros cobertos com telhas de mármore branco.",
        "Porque os membros da nobreza de sangue não sabiam ler nem interpretar despachos diplomáticos em latim.",
        "Porque a legislação eleitoral de Florença concedia aos artesãos o direito perpétuo de nomear os magistrados.",
        "B",
        "- **Etapa 1:** Analisar a desproporção numérica e o alcance da força: um governante pode vigiar e isolar algumas dúzias de nobres conspiradores, mas não consegue policiar a totalidade da população.\n- **Etapa 2:** Concluir com a sustentabilidade política: o ódio de um povo inteiro derruba qualquer império; o soberano prudente satisfaz o anseio elementar do povo de não ser oprimido, construindo uma muralha de lealdade popular imbatível contra qualquer tentativa de golpe aristocrático."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Como a obra de Maquiavel influenciou a formulação do conceito contemporâneo de 'Campo Político Autônomo' pelo sociólogo francês Pierre Bourdieu?",
        "Defendendo que as corporações religiosas de monges deveriam ditar as regras das eleições parlamentares.",
        "Inaugurando a compreensão de que a política não é um reflexo mecânico da moral religiosa nem mero apêndice da economia, mas um espaço de disputa simbólica e material dotado de capitais, regras de jogo, estratégias e lógicas próprias e irredutíveis a outras esferas da vida social.",
        "Provando que as campanhas eleitorais modernas consomem recursos orçamentários excessivos com cartazes impressos.",
        "Exigindo que os líderes partidários prestem juramentos cívicos perante estátuas de deusas romanas.",
        "Determinando que os diplomatas devam receber condecorações literárias antes de assumirem seus postos consulares.",
        "B",
        "- **Etapa 1:** Resgatar a gênese da autonomia política em Maquiavel: a recusa em avaliar as ações de Estado por métricas de catecismo e o reconhecimento da lógica singular do poder e da força.\n- **Etapa 2:** Conectar com a sociologia de Bourdieu: o campo político consolida-se como um microcosmo com seus agentes específicos, habitus próprio e lutas internas pela conquista da autoridade legítima, confirmando a intuição inaugural maquiaveliana."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Analise a distinção fundamental feita por Maquiavel entre a 'Glória Duradoura' e o mero 'Poder Tirânico': de que maneira essa fronteira ética refuta a acusação de que o autor foi um apologista desavergonhado do crime e da imoralidade despótica?",
        "Demonstrando que os governantes que conquistam o poder por assassinatos em massa e traições mesquinhas podem deter a força bruta circunstancial, mas são eternamente amaldiçoados e desprezados pela história, sendo desprovidos da verdadeira glória que somente a fundação de instituições justas e a salvação da pátria podem outorgar.",
        "Provando que todos os tiranos da Antiguidade grega foram condecorados postumamente com coroas de louro em Roma.",
        "Afirmando que a glória de um governante depende da quantidade de moedas de prata guardadas em seus baús particulares.",
        "Exigindo que os memoriais cívicos registrem unicamente os nomes de generais que venceram disputas desportivas navais.",
        "Sustentando que os historiadores devem abster-se de emitir julgamentos avaliativos sobre períodos de guerra.",
        "B",
        "- **Etapa 1:** Desmontar a lenda negra do maquiavelismo vulgar: a leitura moralista acusa Maquiavel de ensinar o mal pelo mal; o texto revela repulsa ao tirano sádico que mata para saciar a vaidade particular.\n- **Etapa 2:** Evidenciar o critério supremo da virtù: o soberano virtuoso usa a dureza somente quando forçado pela necessidade de salvar a comunidade; seu objetivo não é o deleite na opressão, mas a fundação duradoura da ordem e da liberdade republicana, único caminho para a glória verdadeira."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "No capítulo XXV de O Príncipe, Maquiavel descreve a Fortuna sob a imagem arquetípica de uma força a ser subjugada pela impetuosidade: 'É melhor ser impetuoso do que prudente, porque a fortuna é mulher, e se queres dominá-la é necessário castigá-la e contrariá-la.' Contextualize historicamente essa retórica renascentista e analise criticamente a sua mensagem política substantiva.",
        "Defende que os governos civis devem proibir o ingresso de mulheres em bibliotecas municipais de consulta.",
        "Emprega uma alegoria patriarcal típica de seu tempo para defender que a ação política diante da contingência histórica e das crises radicais exige coragem decisória, ousadia estratégica e capacidade de tomar a iniciativa, em vez da hesitação paralisante e passiva dos governantes temerosos.",
        "Comprova que as decisões diplomáticas entre repúblicas soberanas eram tomadas após torneios de tiro com arco.",
        "Exige que os tratados de cessar-fogo sejam lavrados unicamente durante os períodos de eclipse solar.",
        "Determina que os generais de infantaria devam usar adereços de lã escarlate em batalhas noturnas.",
        "B",
        "- **Etapa 1:** Contextualizar criticamente a alegoria de época: Maquiavel utiliza a personificação clássica da deusa romana Fortuna com a linguagem patriarcal do Renascimento do século XVI.\n- **Etapa 2:** Extrair o núcleo da teoria da decisão política: em momentos de ruptura e perigo, o governante que hesita indefinidamente é atropelado pela história; a virtù exige audácia criativa para agarrar a ocasião (*kairós*) e mudar o curso dos acontecimentos."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "Ao examinar a gênese da 'Opinião Pública' nas democracias modernas, de que modo a tese maquiaveliana sobre o 'Parecer' em oposição ao 'Ser' antecipa a centralidade da comunicação política e do marketing nas sociedades do espetáculo?",
        "Comprovando que os canais de rádio e televisão foram concebidos originalmente por corporações de tipógrafos florentinos.",
        "Evidenciando com lucidez pioneira que os cidadãos comuns raramente têm acesso direto às deliberações secretas dos governantes, julgando as autoridades a partir das narrativas, símbolos, imagens e percepções públicas que estas projetam na esfera social comunicativa.",
        "Determinando que os candidatos a cargos eletivos devem usar vestimentas bordadas com fios de cobre.",
        "Exigindo que as pesquisas de intenção de voto sejam realizadas exclusivamente por correspondência postal lacrada.",
        "Provando que a confiança pública decorre do silêncio absoluto das autoridades em períodos de comoção civil.",
        "B",
        "- **Etapa 1:** Resgatar a observação de Maquiavel no Cap. XVIII: os homens em geral julgam mais com os olhos do que com as mãos; todos podem ver o que pareces, poucos sabem o que realmente és.\n- **Etapa 2:** Conectar com a esfera pública contemporânea: muito antes da televisão e das redes digitais, Maquiavel entendeu que a política é mediação e espetáculo; a gestão da percepção pública e da autoridade simbólica é condição de governabilidade em qualquer regime representativo."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "Em Discursos sobre Tito Lívio, Maquiavel analisa o papel do 'Tribunato da Plebe' e argumenta que essa magistratura foi indispensável para a república porque funcionou como uma instituição de 'Denúncia Pública e Salvação dos Plebeus'. Qual é a correspondência dessa análise com os órgãos contemporâneos de controle social e defensoria pública?",
        "Defendendo que os órgãos de ouvidoria pública devem cobrar taxas judiciais sobre queixas populares.",
        "Demonstrando que democracias duradouras necessitam de instituições estatais autônomas e acessíveis (como o Ministério Público e a Defensoria Pública) que acolham as denúncias dos cidadãos vulneráveis contra o arbítrio dos poderosos, evitando a violência desregrada e legitimando o pacto social republicano.",
        "Provando que as denúncias criminais devem ser apresentadas exclusivamente em sessões solenes de tribunais militares.",
        "Afirmando que a contestação jurídica das decisões de governantes constitui crime de lesa-majestade em repúblicas.",
        "Exigindo que os advogados de réus vulneráveis prestem cauções financeiras em moedas de ouro maciço.",
        "B",
        "- **Etapa 1:** Identificar o papel dos Tribunos na Roma republicana: oferecer canal legítimo para a revolta do povo contra a opressão dos patrícios; sem esse canal, a tensão explodia em assassinatos e vingança privada.\n- **Etapa 2:** Articular com as instituições democráticas modernas: a Defensoria Pública e os mecanismos de controle externo institucionalizam a defesa do cidadão comum contra abusos estatais e corporativos, assegurando a saúde republicana e a vigência real dos direitos."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Como a crítica de Maquiavel à pretensa 'Santidade e Inocência' dos governantes desmistifica o moralismo ingênuo na política e previne os cidadãos contra a sedução de líderes messiânicos?",
        "Provando que os sermões clericais devem ser proferidos no início de todas as sessões parlamentares.",
        "Demonstrando que líderes que se apresentam como arautos da pureza moral absoluta e inimigos de qualquer negociação política costumam esconder intenções tirânicas dissimuladas ou, se sinceros em sua inocência, provocam catástrofes de desgoverno ao desconhecerem as duras regras e correlações de força da realidade concreta.",
        "Exigindo que os governantes passem por testes de pureza moral administrados por corporações de monges.",
        "Comprovando que as alianças partidárias entre facções rivais enfraquecem a estabilidade constitucional.",
        "Determinando que os cidadãos devem votar unicamente em candidatos que comprovem linhagem de sangue nobre.",
        "B",
        "- **Etapa 1:** Diagnosticar o perigo do moralismo messiânico: o falso santo na política ou é um hipócrita perigoso que usa o discurso da pureza para eliminar adversários, ou um tolo que leva o Estado à falência.\n- **Etapa 2:** Formar a lucidez cidadã: Maquiavel vacina o jovem contra a demagogia populista; a política madura exige estadistas competentes, responsáveis pelas consequências de seus atos e capazes de dialogar com a pluralidade do mundo real."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "De que modo a tese maquiaveliana sobre a 'Acomodação dos Meios aos Fins' na conservação do Estado influenciou a formulação jurídica das chamadas 'Medidas Constitucionais de Exceção' (como o Estado de Defesa e o Estado de Sítio na Constituição Federal de 1988)?",
        "Autorizando os governantes a suspenderem a vigência da Constituição para benefício patrimonial particular de suas famílias.",
        "Estabelecendo que, em situações extremas de ameaça iminente à integridade da pátria, agressão militar externa ou calamidade pública sem precedentes, o ordenamento jurídico prevê instrumentos temporários e rigorosamente delimitados para concentrar poderes e atribuições de defesa da própria ordem democrática contra a aniquilação pelo caos.",
        "Comprovando que as cartas constitucionais deixam de vigorar sempre que ocorrem eleições municipais suplementares.",
        "Determinando que os tribunais civis devem terceirizar os julgamentos de segurança nacional a comandos estrangeiros.",
        "Exigindo que as medidas extraordinárias de defesa territorial sejam decretadas unicamente por autoridades religiosas.",
        "B",
        "- **Etapa 1:** Compreender a intuição pioneira de Maquiavel: uma constituição que não prevê mecanismos excepcionais para combater emergências mortais é destruída por quem não tem freios legais.\n- **Etapa 2:** Conectar com o Direito Constitucional contemporâneo: instrumentos como o Estado de Defesa e de Sítio são previsões de legalidade extraordinária (fundadas na razão de Estado); sua missão não é destruir a democracia, mas salvar a comunidade para que a normalidade constitucional seja restabelecida."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Analise a relação entre a 'Crítica de Maquiavel à Neutralidade' e o dilema das alianças no cenário contemporâneo de polarização geopolítica: por que o pensador sentencia que 'o perdedor não terá compaixão de ti e o vencedor desconfiará de ti'?",
        "Porque os tratados de amizade internacional eram escritos com tintas vegetais que desapareciam na água.",
        "Porque o governante que se omite e recusa compromissos claros em tempos de crise decisiva revela covardia e deslealdade estratégica; após o desfecho do embate, não é acolhido como amigo pelo triunfante (que o vê como oportunista inútil) nem pelo derrotado (que o enxerga como traidor indiferente ao seu sofrimento).",
        "Porque as assembleias cívicas suspendiam o comércio de carnes defumadas com cidades neutras.",
        "Porque a legislação romana exigia que todas as cidades da liga prestassem cultos matinais aos mesmos oráculos.",
        "Porque os generais mercenários cobravam taxas dobradas de principados que mantinham as portas fechadas.",
        "B",
        "- **Etapa 1:** Interpretar o diagnóstico do oportunismo da neutralidade covarde: ficar no muro para não se indispor com ninguém é a fórmula perfeita para atrair a hostilidade de todos.\n- **Etapa 2:** Concluir com a lição para as relações de poder: o respeito e a segurança na arena política internacional exigem posicionamento firme, compromisso leal com aliados e coragem de assumir os riscos da história."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "Ao examinar a dialética do 'Amor versus Temor' no âmbito da gestão escolar e pedagógica contemporânea, como a lição maquiaveliana ajuda a superar tanto o autoritarismo violento quanto a frouxidão permissiva?",
        "Exigindo que as diretorias de escolas apliquem punições corporais com varas de madeira nos alunos desatentos.",
        "Demonstrando que um ambiente formativo de excelência e segurança não se constrói nem pelo ódio da opressão humilhante (que gera rebelião e desengajamento dos estudantes), nem pela frouxidão do compadrio permissivo sem regras (que gera caos e desrespeito), mas pela autoridade ética e firme, transparente e coerente nas normas, mantendo o respeito mútuo sem tirania.",
        "Determinando que os coordenadores pedagógicos devem fechar as salas de aula durante o horário de almoço.",
        "Provando que as avaliações curriculares devem ser aplicadas unicamente aos concluintes do terceiro ano.",
        "Afirmando que a convivência escolar dispensaria códigos disciplinares caso houvesse aulas de música lírica.",
        "B",
        "- **Etapa 1:** Afastar o extremo do ódio: a escola autoritária que humilha os estudantes perde a legitimidade educativa e cria ressentimento e agressividade.\n- **Etapa 2:** Afastar o extremo da demagogia frouxa: o educador que renuncia à autoridade e à firmeza das regras em nome de ser amado a qualquer custo gera a desestruturação do ambiente pedagógico; o equilíbrio reside na autoridade firme, justa e respeitosa que protege a comunidade de aprendizagem."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Em Discursos sobre Tito Lívio, Maquiavel afirma categoricamente que 'a multidão é mais prudente, mais constante e de melhor juízo do que um príncipe'. De que maneira essa formulação derruba a tese de que o pensador era um elitista autoritário e consagra a superioridade da inteligência coletiva democrática?",
        "Provando que os plebiscitos populares em Roma eram decididos por consultas a folhas de oliveira seca.",
        "Evidenciando que, embora a massa possa se equivocar temporariamente por arroubos passionais, ela é infinitamente mais capaz de corrigir seus rumos sob o império de boas leis do que um único soberano individual, que frequentemente enlouquece pelo absolutismo do poder, adulação palaciana e caprichos egoístas incontroláveis.",
        "Comprovando que as repúblicas clássicas proibiam a cobrança de tributos municipais sobre cereais importados.",
        "Exigindo que os senadores de linhagem nobre fossem julgados exclusivamente por comissões de mercadores.",
        "Determinando que os votos populares fossem depositados em urnas de barro cozido decoradas com flores.",
        "B",
        "- **Etapa 1:** Desmistificar o desprezo aristocrático pelas multidões: filósofos tradicionais rotulavam o povo como massa irracional e perigosa.\n- **Etapa 2:** Resgatar a sabedoria republicana de Maquiavel: o julgamento coletivo dos cidadãos sob leis estáveis é superior à mente instável de um déspota; o povo delibera com maior apego à justiça e à preservação da cidade, tornando a democracia participativa o regime supremo."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Síntese conclusiva do Capítulo 18: por que o estudo crítico do Realismo Político de Maquiavel no Ensino Médio é indispensável para emancipar o jovem cidadão contra a hipocrisia e capacitá-lo a intervir com eficácia e ética na vida democrática do século XXI?",
        "Porque ele ensina técnicas de espionagem militar e desvio de recursos públicos para contas no exterior.",
        "Porque ele instrumentaliza o estudante com uma lucidez desassombrada para decifrar as engrenagens ocultas do poder e as artimanhas dos dominadores, vacinando a juventude contra a ingenuidade moralista e o cinismo niilista, e demonstrando que a defesa dos direitos, da liberdade e da justiça exige organização coletiva consciente, clareza estratégica e mobilização cidadã firme na história concreta.",
        "Porque ele estabelece a obrigatoriedade da inclusão de línguas latinas mortas nos currículos do ensino fundamental.",
        "Porque ele comprova que as disputas partidárias contemporâneas perdem o sentido diante de avanços tecnológicos fabris.",
        "Porque ele determina que as escolas públicas devem suspender as aulas de sociologia em anos eleitorais.",
        "B",
        "- **Etapa 1:** Superar os dois perigos formativos opostos: a ingenuidade moralista (que acredita nas promessas vazias das elites) e o cinismo apático (que desiste da política achando que tudo é corrupção sem solução).\n- **Etapa 2:** Forjar a cidadania transformadora: Maquiavel ensina que o poder é feito por homens e pode ser disputado e transformado por homens; o jovem consciente entende o terreno do jogo real para lutar por um mundo mais justo, onde a dignidade popular e a república prevaleçam."
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
    linhas.append('capitulo: "Capítulo 18: A Invenção da Política Moderna: O Realismo de Maquiavel"')
    linhas.append('objeto_de_conhecimento: "A autonomia da política, a verdade efetiva das coisas, a dialética entre virtù e fortuna, a natureza humana e o republicanismo em Maquiavel"')
    linhas.append('ebook_fonte: "em-fil-c18-realismo-politico-maquiavel.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS501"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: A Invenção da Política Moderna: O Realismo de Maquiavel\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-18-realismo-politico-maquiavel -->"
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
    linhas.append("- MAQUIAVEL, Nicolau. *O Príncipe*. Tradução de Maurício Santana Dias. São Paulo: Penguin Classics Companhia das Letras, 2010.")
    linhas.append("- MAQUIAVEL, Nicolau. *Discursos sobre a primeira década de Tito Lívio*. Tradução de Sérgio Bath. Brasília: Editora UnB, 1994.")
    linhas.append("- SKINNER, Quentin. *As fundações do pensamento político moderno*. Tradução de Renato Janine Ribeiro e Laura Teixeira Motta. São Paulo: Companhia das Letras, 1996.")
    linhas.append("- LEFORT, Claude. *As formas da história: ensaios de antropologia política*. São Paulo: Brasiliense, 1990.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Gravação no temp_draft.md
    caminho_draft = "temp_draft.md"
    with open(caminho_draft, "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em {caminho_draft} ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador oficial
    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-18-realismo-politico-maquiavel/ebooks/em-fil-c18-realismo-politico-maquiavel-exercicios.md"
    cmd = [sys.executable, "validador_educamob.py", caminho_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode != 0:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)
    else:
        print("\n[SUCESSO TOTAL] Cap 18 validado e homologado com Exit Code 0!")

if __name__ == "__main__":
    main()
