# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 26 de Filosofia EM:
A Estética Moderna: Kant e Hegel
Objeto: cap-26-estetica-moderna-kant-hegel
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
        "Em qual obra de maturidade Immanuel Kant consolida a autonomia da Estética e formula a teoria do Juízo de Gosto?",
        "Na Crítica da Razão Pura (1781), que analisa as categorias do entendimento físico.",
        "Na Crítica da Faculdade do Juízo (1790), que investiga o sentimento de prazer, o belo e o sublime.",
        "Na Crítica da Razão Prática (1788), que estabelece o imperativo categórico da moralidade.",
        "Nos Prolegômenos a Toda Metafísica Futura, que discute a geometria espacial euclidiana.",
        "Na Paz Perpétua, que propõe uma federação de repúblicas para conter guerras internacionais.",
        "B",
        "Na terceira crítica (1790), Kant faz a ponte entre a natureza e a liberdade através da Faculdade de Julgar, emancipando a Estética da tutela da moral e da ciência."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "O que significa afirmar que o prazer estético que define o Belo em Kant é 'desinteressado'?",
        "Que o espectador contempla a obra com completa indiferença, tédio e frieza emocional.",
        "Que a apreciação do belo independe de qualquer cobiça de posse material, utilidade prática instrumental ou satisfação de apetites fisiológicos corporais.",
        "Que as obras de arte devem ser doadas compulsoriamente a museus mantidos pelo Estado.",
        "Que os pintores devem produzir quadros sem receber pagamentos ou recompensas monetárias.",
        "Que as avaliações de peças teatrais dependem de autorização de magistrados consulares.",
        "B",
        "Desinteresse em Kant significa pureza contemplativa: admirar a beleza de uma flor ou estátua sem desejar comê-la, vendê-la no mercado ou usá-la como ferramenta útil."
    ))

    questoes_brutas.append((
        3, "EM13CHS301", "basico",
        "Como Kant distingue o 'Belo' do 'Agradável' e do 'Bom' no primeiro momento da Analítica do Juízo de Gosto?",
        "O Agradável satisfaz a razão pura, o Bom agrada aos animais e o Belo é uma ilusão matemática.",
        "O Agradável interessa aos sentidos físicos (satisfaz apetites corporais), o Bom interessa à utilidade prática ou lei moral, e o Belo agrada desinteressadamente pela pura forma.",
        "O Agradável é eterno e universal, enquanto o Belo e o Bom são costumes passageiros locais.",
        "O Bom é exclusivo de tratados de comércio e o Belo de manuais militares de cavalaria.",
        "O Agradável, o Bom e o Belo possuem o mesmo valor de troca em feiras municipais.",
        "B",
        "Kant separa com rigor: comer uma fruta sacia a fome (agradável); um remédio cura a dor (bom útil); uma bela pintura encanta a mente pela harmonia de sua forma (belo desinteressado)."
    ))

    questoes_brutas.append((
        4, "EM13CHS302", "basico",
        "O que estabelece a tese kantiana da 'Universalidade sem Conceito' na apreciação do Belo?",
        "A exigência de que todas as pessoas devam ler manuais didáticos de história da arte antes de visitarem galerias.",
        "A constatação de que, embora não exista uma regra lógica ou conceito que prove por teoremas que algo é belo, quem julga algo belo supõe que todos os outros deveriam sentir o mesmo encanto.",
        "A obrigatoriedade de adoção de línguas clássicas na redação de críticas artísticas em jornais.",
        "A determinação de que as obras de arte devam ser aprovadas por votação unânime em parlamentos.",
        "A afirmação de que a beleza depende exclusivamente da quantidade de tinta aplicada na tela.",
        "B",
        "Não existe fórmula matemática do belo: não há conceito lógico que prove a beleza; porém, ao contemplar o belo, exigimos o acordo de todos através do livre jogo entre imaginação e entendimento."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Qual é o significado da célebre fórmula kantiana 'Finalidade sem Fim' (*Zweckmässigkeit ohne Zweck*) aplicada à obra de arte?",
        "O objeto artístico foi fabricado sem qualquer método por um operário desatento.",
        "A obra apresenta uma harmonia formal e coerência interna tão perfeita que parece planejada, mas não possui nenhuma função utilitária ou propósito instrumental externo.",
        "A produção de quadros decorativos deve atender unicamente aos comandos de generais militares.",
        "O valor de uma pintura depende exclusivamente do preço de venda de seus pigmentos em bazares.",
        "A arte deve ser destruída periodicamente para acelerar a renovação das indústrias têxteis.",
        "B",
        "Uma flor silvestre ou uma sinfonia exibe proporções perfeitas como se tivesse sido desenhada para um propósito; mas sua beleza reside em não servir a nada prático: é um fim em si mesma."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Como Immanuel Kant define a experiência estética do 'Sublime' (*Das Erhabene*)?",
        "A contemplação pacífica de pequenas conchas marinhas depositadas em praias arenosas.",
        "A experiência vertiginosa despertada diante do desmedido, colossal e avassalador, que ultrapassa a capacidade de apreensão sensorial dos sentidos físicos.",
        "A leitura de romances ligeiros escritos para o entretenimento cômico em festivais populares.",
        "A admiração de tecidos de linho coloridos comercializados em feiras municipais provinciais.",
        "O aprendizado de regras gramaticais em escolas preparatórias de línguas estrangeiras.",
        "B",
        "O sublime não é apenas o muito bonito; é o grandioso e assombroso: oceanos sem fim, montanhas colossais ou tempestades furiosas que desafiam a capacidade da imaginação humana."
    ))

    questoes_brutas.append((
        7, "EM13CHS301", "basico",
        "O que caracteriza especificamente o 'Sublime Matemático' na teoria estética de Kant?",
        "A resolução de equações algébricas complexas em provas de admissão universitária.",
        "O confronto da mente com a incomensurabilidade e a infinitude de escala de grandezas cósmicas (como a abóbada estelar ou cordilheiras titânicas), desafiando a imaginação sensível.",
        "A contagem de moedas de prata armazenadas em cofres de companhias mercantis navais.",
        "A medição topográfica de terras agrícolas para a cobrança de tributos patrimoniais.",
        "O cálculo da velocidade de ventos marítimos realizado por navegadores de caravelas.",
        "B",
        "No sublime matemático, a imaginação sensorial fracassa diante do colossal cósmico (o céu com bilhões de estrelas); mas no fracasso dos olhos desperta a Razão moral que concebe a ideia do infinito."
    ))

    questoes_brutas.append((
        8, "EM13CHS302", "basico",
        "Como Kant caracteriza o 'Sublime Dinâmico' diante das forças avassaladoras da natureza física?",
        "A observação tranquila de animais pastando em planícies ensolaradas durante a primavera.",
        "A contemplação, a partir de um local seguro, da potência destrutiva da natureza (tempestades, vulcões, furacões), que revela a fragilidade do corpo mas afirma a dignidade moral invulnerável do ser humano.",
        "A construção de represas de água de madeira para irrigar hortas comunitárias no interior.",
        "A realização de competições esportivas de corrida em praias litorâneas municipais.",
        "O monitoramento de marés marítimas por capitães de fragatas armadas da marinha real.",
        "B",
        "Diante de um vulcão ou tempestade furiosa, nosso corpo biológico treme de pequenez; porém, como sujeitos morais dotados de liberdade interior, descobrimos que o espírito é superior à força bruta da matéria."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Qual é a célebre definição de beleza artística formulada por G. W. F. Hegel em seus Cursos de Estética?",
        "A imitação matemática exata dos relevos rochosos do mundo exterior sensível.",
        "A manifestação sensível da Ideia (*das sinnliche Scheinen der Idee*).",
        "O conjunto de regras formais estabelecidas por academias de pintura para agradar reis.",
        "A harmonia biológica herdada geneticamente pelos membros de comunidades urbanas.",
        "A cópia de segundo grau das sombras projetadas nas paredes da caverna de Platão.",
        "B",
        "Para Hegel, a arte é a Ideia espiritual que toma corpo sensível: o Espírito humano molda a pedra, a tinta ou o som, transformando a matéria inerte em expressão viva da verdade e da autoconsciência."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Por que, para Hegel, a Beleza Artística é superior à beleza puramente natural encontrada em flores e paisagens?",
        "Porque as obras de arte custam somas financeiras elevadas em leilões comerciais.",
        "Porque a obra de arte é fruto do Espírito consciente (*Geist*), que imprime sua liberdade e reflexão sobre a matéria, ao passo que a natureza é inerte e inconsciente de si.",
        "Porque as flores silvestres murcham rapidamente quando colhidas por camponeses nas matas.",
        "Porque os governantes das metrópoles proibiam a conservação de florestas em áreas urbanas.",
        "Porque a escultura clássica utiliza ligas metálicas mais resistentes do que a argila dos solos.",
        "B",
        "Hegel afirma com vigor: um pensamento ruim na mente de um homem é mais elevado do que o sol, pois o sol não sabe que brilha; a arte é superior porque nasce da liberdade espiritual consciente."
    ))

    questoes_brutas.append((
        11, "EM13CHS301", "basico",
        "Quais são as três figuras supremas do 'Espírito Absoluto' em que a humanidade compreende sua própria verdade em Hegel?",
        "A Economia, a Diplomacia e a Engenharia Civil Mecânica.",
        "A Arte, a Religião e a Filosofia.",
        "A Agricultura, a Mineração e a Navegação Comercial Oceânica.",
        "A Geometria, a Astronomia e a Gramática Clássica Latina.",
        "O Exército, a Magistratura e a Burocracia Imperial Tributária.",
        "B",
        "Hegel coloca Arte, Religião e Filosofia no topo da cultura: a Arte intui a Verdade na forma sensível, a Religião a representa na fé e na devoção interior, e a Filosofia a concebe no conceito puro da Razão."
    ))

    questoes_brutas.append((
        12, "EM13CHS302", "basico",
        "Qual é a primeira forma histórica da arte na dialética hegeliana, típica das antigas civilizações orientais?",
        "A Arte Romântica, caracterizada pelo surgimento de instrumentos sonoros musicais.",
        "A Arte Simbólica, cuja manifestação privilegiada é a Arquitetura monumental (como as pirâmides do Egito e a esfinge).",
        "A Arte Clássica, marcada pela perfeição do corpo humano talhado em mármore.",
        "A Arte Conceitual, fundada no uso de materiais industriais descartáveis em ateliês.",
        "A Arte Neoclássica, voltada para a representação de batalhas cívicas e imperiais.",
        "B",
        "Na arte simbólica (Egito, Babilônia), o Espírito ainda é misterioso e vaga; a matéria colossal das pirâmides domina a Ideia, criando símbolos gigantescos que apontam para um mistério ainda não decifrado."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Qual manifestação artística encarna com perfeição a 'Forma de Arte Clássica' na Grécia Antiga segundo Hegel?",
        "A construção de diques e aquedutos fluviais para escoamento de águas urbanas.",
        "A Escultura antropomórfica em mármore e bronze, que une com harmonia perfeita a Ideia espiritual e o corpo humano livre.",
        "A pintura de naturezas-mortas representando cestos de vimes com frutas de outono.",
        "A composição de marchas militares tocadas por soldados em trompetes de cobre.",
        "A redação de manuais de contabilidade de mercadores marítimos em tábuas de cera.",
        "B",
        "A escultura grega é o ápice da beleza sensível: nela, o corpo humano não é peso opaco; os deuses talhados em mármore por Fídias dão rosto transparente ao Espírito em perfeito equilíbrio de forma e conteúdo."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "O que caracteriza a 'Forma de Arte Romântica' na evolução histórica do Espírito em Hegel?",
        "O retorno obrigatório à construção de pirâmides monumentais em desertos abertos.",
        "A transcendência da Ideia espiritual sobre a matéria sensível física, manifestando-se prioritariamente na Pintura, na Música e na Poesia.",
        "A exclusão de qualquer representação de sentimentos de amor em narrativas escritas.",
        "A proibição do uso de instrumentos de corda em orquestras e celebrações litúrgicas.",
        "A limitação da criação artística à elaboração de brasões nobiliárquicos para cortes.",
        "B",
        "Na arte romântica (da cristandade à modernidade), o espírito descobre que é infinito e que não cabe na pedra da escultura; ele busca artes mais leves e espirituais: a pintura, a música e a palavra poética."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "O que estabelece a polêmica tese hegeliana do 'Fim da Arte' (*Das Ende der Kunst*) no mundo moderno?",
        "A afirmação de que os artistas deixariam de produzir quadros, esculturas ou canções na modernidade.",
        "O diagnóstico de que a arte perdeu sua função histórica suprema de ser a expressão máxima e definitiva da verdade divina e existencial para a sociedade civilizada.",
        "A proibição parlamentar do ensino de desenho e música nas escolas públicas da Europa.",
        "A queima compulsória de instrumentos musicais em praças públicas de capitais industriais.",
        "O esgotamento de minas de mármore e pigmentos utilizados na fabricação de tintas a óleo.",
        "B",
        "Hegel não profetizou a morte da pintura: o que terminou foi o tempo em que o povo se ajoelhava diante da estátua como verdade sagrada do cosmos; hoje olhamos a arte com distanciamento crítico e reflexivo."
    ))

    questoes_brutas.append((
        16, "EM13CHS302", "basico",
        "Por que, para Hegel, a 'Filosofia' assume o papel supremo na autoconsciência da modernidade, ultrapassando a forma sensível da arte?",
        "Porque os filósofos eram remunerados com salários mais elevados do que os pintores de corte.",
        "Porque a nossa época moderna é reflexiva, científica e conceitual, exigindo que a Verdade plena seja apreendida pelo pensamento rigoroso e não mais por imagens materiais sensíveis.",
        "Porque os códigos jurídicos proibiam a presença de artistas em assembleias parlamentares.",
        "Porque os edifícios de universidades foram projetados com salas maiores do que os ateliês de arte.",
        "Porque a produção de livros filosóficos utilizava tipos gráficos de ferro fundido mecanizado.",
        "B",
        "O mundo moderno secular exige o conceito: visitamos o museu, analisamos a técnica e julgamos criticamente a obra; o Espírito Absoluto amadureceu e agora pensa a si mesmo através da Filosofia."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Como a contemplação da famosa escultura da Vênus de Milo no Museu do Louvre exemplifica na prática o 'Juízo de Gosto Desinteressado' de Kant?",
        "Calculando o lucro que seria obtido com a venda clandestina do mármore no mercado financeiro.",
        "Admirando a pureza harmoniosa das proporções, das formas e do drapeado da pedra pelo puro deleite estético, sem cobiça de posse material nem apetite carnal vulgar.",
        "Medindo a densidade mineral da rocha com instrumentos de engenharia de minas terrestres.",
        "Verificando se a estátua atende às normas de segurança contra incêndios em edifícios públicos.",
        "Avaliando a utilidade da escultura para servir como peso de contenção de papéis em bibliotecas.",
        "B",
        "Se o visitante olha para a estátua querendo leiloá-la ou desejando o corpo físico de carne, não há estética; a experiência estética kantiana é a alegria gratuita de contemplar a beleza harmoniosa da forma."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "De que modo obras da Arte Conceitual contemporânea (como o mictório de Marcel Duchamp em A Fonte) confirmam a tese de Hegel sobre a intelectualização da arte?",
        "Provando que as peças de cerâmica sanitária possuem acabamento mais brilhante do que o mármore.",
        "Esvaziando a beleza formal tradicional para transferir o valor artístico à provocação conceitual, à reflexão teórica e ao debate filosófico sobre 'o que é arte'.",
        "Obrigando os museus a instalarem encanamentos de água potável em todas as salas de exposição.",
        "Demonstrando que os artistas plásticos contemporâneos desconhecem técnicas de escultura e pintura.",
        "Exigindo que os visitantes comprem bilhetes de entrada com recibos fiscais autenticados em cartório.",
        "B",
        "O mictório de Duchamp (1917) prova Hegel: não há beleza visual tradicional ali; o que faz dele arte é a pergunta filosófica que ele obriga o espectador a fazer; a arte moderna virou pensamento conceitual puro."
    ))

    questoes_brutas.append((
        19, "EM13CHS301", "basico",
        "Qual é o equívoco primário cometido por quem confunde o 'Sublime' com o 'Belo' na filosofia de Kant?",
        "Supor que o sublime é apenas uma gíria popular empregada para elogiar um prato culinário.",
        "Tratar o sublime como mero superlativo de 'muito belo', ignorando que o Belo nasce da forma harmoniosa finita e o Sublime brota do desmedido, do excesso e do confronto com a imensidão avassaladora.",
        "Acreditar que o belo e o sublime foram categorias copiadas de tratados de carpintaria naval.",
        "Imaginar que o sublime se aplica exclusivamente a pinturas confeccionadas com tintas azuis.",
        "Afirmar que o belo depende de aprovação prévia concedida por conselhos paroquiais de monges.",
        "B",
        "Belo e Sublime são mundos distintos: o belo é a proporção harmoniosa e serena que cabe nos olhos (uma rosa); o sublime é o desmedido aterrador que esmaga os sentidos e desperta a Razão infinita (o oceano em fúria)."
    ))

    questoes_brutas.append((
        20, "EM13CHS302", "basico",
        "Como a pintura romântica de Caspar David Friedrich (O Caminhante sobre o Mar de Névoa) traduz visualmente a estética do Sublime kantiano?",
        "Mostrando operários industriais trabalhando na fiação mecanizada de algodão em fábricas.",
        "Retratando um homem solitário no topo de um rochedo diante de abismos e mares colossais de névoa, expressando a pequenez do corpo perante o infinito cósmico aliada à grandeza interior da mente humana.",
        "Apresentando um soldado de infantaria militar desfilando em praças ensolaradas com fardamentos.",
        "Exibindo banquetes cortesãos com mesas fartas de pães, vinhos e carnes assadas em palácios.",
        "Desenhando plantas arquitetônicas detalhadas para a edificação de fortalezas marítimas de pedra.",
        "B",
        "A tela de Friedrich é o ícone do sublime: o homem de costas vê a imensidão abissal de névoa e montanhas; o corpo é um ponto frágil diante do cosmos, mas o espírito contempla o infinito com coragem e nobreza."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Como o 'Livre Jogo entre Imaginação e Entendimento' fundamenta a universalidade do juízo de gosto na estética transcendental de Kant?",
        "Submetendo a fantasia individual a regras silogísticas rígidas estabelecidas por manuais de lógica.",
        "Promovendo um estado de harmonia comunicável sem conceitos, no qual a imaginação (que capta a variedade das formas) e o entendimento (que busca a unidade) afinam-se livremente perante o objeto belo.",
        "Obrigando os poetas a utilizarem dicionários bilíngues para a escolha de vocábulos rimados.",
        "Determinando que a produção de quadros dependa de autorizações emitidas por guildas de carpinteiros.",
        "Garantindo que todos os cidadãos de uma comarca votem no mesmo estilo arquitetônico em eleições.",
        "B",
        "No belo, a imaginação e o entendimento dançam juntos sem coleira: o entendimento não impõe uma regra lógica e a imaginação não delira no caos; as duas faculdades afinam-se em livre harmonia que qualquer mente partilha."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Em que medida a concepção kantiana de 'Sentido Comum Estético' (*Sensus Communis Aestheticus*) afasta o juízo de gosto tanto do relativismo cético quanto do dogmatismo racionalista?",
        "Provando que as preferências culinárias individuais podem ser demonstradas por pesagens físicas de alimentos.",
        "Recusando o relativismo de que 'o gosto é puramente arbitrário' ao supor uma sensibilidade compartilhada por toda a humanidade, sem cair no dogmatismo que pretendia calcular a beleza por regras objetivas.",
        "Obrigando os professores de estética a aplicarem provas padronizadas de memorização de telas.",
        "Sustentando que as cartas de crítica de arte deviam ser carimbadas por tribunais régios de alfândega.",
        "Comprovando que o padrão universal de beleza foi definido por decretos de imperadores romanos antigos.",
        "B",
        "Kant escapa da armadilha: não cai no ceticismo vulgar ('beleza é gosto pessoal e acabou') nem no dogmatismo ('há uma régua que mede o belo'); o sensus communis é a expectativa legítima de que outros sintam o mesmo encanto."
    ))

    questoes_brutas.append((
        23, "EM13CHS301", "intermediario",
        "Como a distinção entre a 'Beleza Livre' (*Pulchritudo Vaga*) e a 'Beleza Aderente' (*Pulchritudo Adhaerens*) enriquece a Analítica do Belo de Immanuel Kant?",
        "A beleza livre refere-se a pássaros de florestas e a beleza aderente a animais confinados em jaulas de zoológicos.",
        "A beleza livre agrada puramente pela forma sem pressupor o conceito do que o objeto deve ser (flores, conchas, arabescos); a beleza aderente pressupõe o conceito do que o objeto deve ser e sua perfeição funcional (um edifício, um cavalo, um ser humano).",
        "A beleza livre é exclusiva de cidadãos nobres e a beleza aderente de trabalhadores de lavouras rurais.",
        "A beleza livre depende de pigmentos minerais raros e a beleza aderente de tintas sintéticas comuns.",
        "A beleza livre foi inventada por filósofos renascentistas e a beleza aderente por juristas medievais.",
        "B",
        "Uma flor ou desenho abstrato é beleza livre: não sabemos para que serve e admiramos a forma pura; uma catedral ou um palácio tem beleza aderente: julgamos a forma sabendo qual é a função prática que ela deve cumprir."
    ))

    questoes_brutas.append((
        24, "EM13CHS302", "intermediario",
        "De que modo a experiência do Sublime conduz o sujeito kantiano à tomada de consciência de sua própria 'Destinação Moral Superior'?",
        "Fazendo com que o indivíduo abdique de bens materiais para viver como eremita solitário nas matas.",
        "Demonstrando que, embora a colossalidade e a violência da natureza revelem a fragilidade biológica do homem perante a matéria, o fracasso da imaginação desperta a Razão que descobre a dignidade espiritual da liberdade humana inviolável.",
        "Provando que a estabilidade social depende da proibição da escalada esportiva de montanhas alpinas.",
        "Exigindo que os exploradores polares prestem relatórios científicos semanais a comissões consulares.",
        "Comprovando que as tempestades oceânicas podem ser contidas através de preces coletivas em portos.",
        "B",
        "O sublime é uma escada para a moral: a montanha colossal e o vulcão mostram que o corpo humano é um sopro perecível; mas a mente percebe que carrega o imperativo moral e a liberdade que nenhuma tempestade mecânica pode dobrar."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Por que, para Hegel, a arte da Grécia Clássica atingiu um cume insuperável de beleza sensível que jamais poderá ser reeditado na história moderna?",
        "Porque os ateliês de Atenas guardavam fórmulas químicas secretas de fundição de bronze que foram destruídas.",
        "Porque somente na pólis grega a fé religiosa, a política e a vida espiritual do povo coincidiam perfeitamente com a corporeidade física harmoniosa, gerando uma unidade transparente entre conteúdo divino e forma sensível que a modernidade reflexiva cindiu.",
        "Porque as leis eleitorais de Atenas concediam pensões vitalícias a todos os escultores diplomados.",
        "Porque a escultura clássica utilizava mármores retirados de pedreiras que se esgotaram no século IV a.C.",
        "Porque os cidadãos gregos eram obrigados a praticar ginástica olímpica antes de entrarem em teatros.",
        "B",
        "Na Grécia clássica houve um milagre histórico irrepetível: os deuses eram humanos e o corpo humano era sagrado; Ideia e mármore se casaram com perfeição transparente; a modernidade é complexa demais para caber na estátua."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "Como a transição da Escultura clássica para a Pintura, a Música e a Poesia românticas expressa o processo hegeliano de 'Desmaterialização Progressiva do Espírito'?",
        "Reduzindo as dimensões físicas da matéria: a pedra tridimensional da escultura dá lugar ao plano bidimensional de luz da pintura, à vibração sonora invisível da música e à representação interior pura da palavra poética.",
        "Incentivando a queima de manuscritos poéticos para a extração de carvão combustível em fábricas.",
        "Exigindo que os compositores utilizem unicamente instrumentos de percussão metálica em concertos.",
        "Provando que as obras pictóricas possuem maior durabilidade geológica do que monumentos de mármore.",
        "Substituindo todos os museus de belas artes por salas de leitura de compêndios de direito civil.",
        "A",
        "A dialética de Hegel desmaterializa a arte: sai do peso da pedra (escultura), vai para a tela plana de luz (pintura), passa para o som invisível no tempo (música) e culmina na palavra pensada (poesia), onde a matéria quase some."
    ))

    questoes_brutas.append((
        27, "EM13CHS301", "intermediario",
        "De que maneira a teoria hegeliana das três formas históricas da arte desmente a ideia racista eurocêntrica de que a arte oriental antiga seria mero 'primitivismo infantil'?",
        "Afirmando que as pirâmides egípcias foram construídas por navegadores europeus em expedições secretas.",
        "Demonstrando que a arte simbólica oriental foi um momento dialético rigoroso e grandioso da autoconsciência do Espírito, que expressava com monumentalidade arquitetônica a luta primordial da Ideia para dominar a matéria física colossal.",
        "Sustentando que as escritas hieroglíficas foram copiadas de códigos legislativos da Roma imperial.",
        "Provando que os templos asiáticos eram destinados exclusivamente à estocagem de cereais agrícolas.",
        "Comprovando que as estátuas da Mesopotâmia utilizavam ligas de bronze importadas da Grécia clássica.",
        "B",
        "Hegel respeita a grandiosidade oriental: as pirâmides e a Esfinge não são tolices; são o esforço titânico da humanidade nascente tentando plasmar na pedra colossal o mistério do divino antes que o conceito pudesse ser dito."
    ))

    questoes_brutas.append((
        28, "EM13CHS302", "intermediario",
        "Como a crítica de Hegel ao conceito kantiano de 'Belo Natural' (as belezas da natureza) revela a centralidade do Espírito (*Geist*) em sua estética?",
        "Provando que as florestas e rios contêm micro-organismos que desgastam telas de pintura a óleo.",
        "Evidenciando que a natureza é matéria inanimada que não tem consciência de sua beleza, ao passo que a obra de arte é espírito que se projeta no mundo sensível, carregando o pensamento e a liberdade humana.",
        "Afirmando que a contemplação de paisagens naturais provoca tédio e melancolia em todos os viajantes.",
        "Determinar que os jardins públicos devessem ser replantados unicamente com espécies botânicas exóticas.",
        "Comprovando que os animais silvestres desconhecem regras harmônicas de composição de cores.",
        "B",
        "Para Hegel, uma flor não sabe que é bela; a arte humana é reflexiva e livre: o homem pega a madeira ou a pedra e grava nela a sua alma, sua história e sua busca pela verdade, tornando a arte infinitamente superior à flor."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Qual é o significado do diagnóstico hegeliano de que 'hoje a arte nos convida ao julgamento do pensamento' em relação à função da Crítica de Arte moderna?",
        "Que as pinturas contemporâneas devem conter textos explicativos redigidos em rodapés de molduras.",
        "Que não nos prostramos mais devotamente perante a obra como um ídolo sagrado indiscutível: nós a analisamos criticamente, julgamos seu valor conceitual, examinamos sua técnica e deciframos seu contexto histórico.",
        "Que os visitantes de museus são obrigados a prestar exames orais perante comissões de curadores.",
        "Que a crítica jornalística de arte deve ser realizada exclusivamente por oficiais militares reformados.",
        "Que as obras de arte plásticas deixaram de ser exibidas em salões públicos e foram trancadas em cofres.",
        "B",
        "A atitude moderna diante da arte é reflexiva: visitamos a bienal não para adorar um santo, mas para pensar, debater com amigos e escrever artigos; a obra de arte moderna se completa no debate crítico do pensamento."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Como a obra Teoria Estética (1970) de Theodor W. Adorno retoma criticamente a dialética hegeliana da arte no contexto da barbárie do século XX?",
        "Exigindo que os artistas contemporâneos pintem exclusivamente cenas alegres de celebração de colheitas.",
        "Sustentando que, após os horrores de Auschwitz e a alienação da sociedade administrada, a arte autêntica deve recusar a beleza harmoniosa ilusória e assumir a negatividade, a dissonância e a fratura como protesto ético.",
        "Defendendo que as produções cinematográficas de entretenimento comercial são as mais elevadas da história.",
        "Provando que as composições musicais de vanguarda foram financiadas por companhias mercantis navais.",
        "Afirmando que a indústria cultural cumpriu integralmente as profecias emancipatória da filosofia hegeliana.",
        "B",
        "Adorno atualiza Hegel: depois do Holocausto, a arte que finge que tudo está lindo é cúmplice da barbárie; a grande arte contemporânea tem que ser incômoda, dissonante (como Schoenberg e Beckett), berrando contra a ordem injusta."
    ))

    questoes_brutas.append((
        31, "EM13CHS301", "intermediario",
        "Em que sentido o 'Juízo de Gosto' kantiano estabelece um modelo exemplar de autonomia moral e liberdade subjetiva perante a autoridade externa?",
        "Porque o cidadão deve aceitar cegamente as recomendações de compras ditadas por críticos profissionais.",
        "Porque ninguém pode ser coagido a achar algo belo por imposição de decretos estatais, leis religiosas ou argumentos lógicos: o juízo estético exige a adesão sincera e livre do sentimento do próprio sujeito.",
        "Porque as obras de arte devem ser destruídas caso não agradem à totalidade dos membros da família.",
        "Porque o julgamento estético depende da aprovação prévia concedida por magistrados de cortes civis.",
        "Porque os cidadãos das repúblicas democráticas devem eleger estilos pictóricos em escrutínios anuais.",
        "B",
        "O gosto é a cidadela da liberdade íntima: um imperador ou papa pode me obrigar a obedecer uma lei com a espada, mas ninguém pode me forçar a achar um quadro belo se meu coração não sentir; o gosto é livre e autônomo."
    ))

    questoes_brutas.append((
        32, "EM13CHS302", "intermediario",
        "De que modo a filosofia romântica do 'Círculo de Jena' (irmãos Schlegel e Novalis) desdobrou as reflexões de Kant e Hegel sobre o poder da poesia?",
        "Propondo a queima de todos os instrumentos musicais em fogueiras públicas comemorativas.",
        "Afirmando que a poesia é a língua primordial da humanidade e a força mágica capaz de 'romantizar o mundo', devolvendo o mistério, o sagrado e a imaginação viva contra a frieza do cálculo mecanicista industrial.",
        "Defendendo a subordinação de todas as produções poéticas a manuais de contabilidade de fábricas de tecidos.",
        "Exigindo que os versos rimados devessem ser recitados exclusivamente em dialetos de marinheiros mercantes.",
        "Comprovando que as metáforas literárias foram inventadas por comissões de generais de infantaria naval.",
        "B",
        "Novalis e os românticos alemães proclamaram a salvação pela poesia: contra a fábrica cinzenta, o lucro frio e o desencantamento burguês, a poesia romântica reacende a chama mágica da alma e devolve o sagrado ao mundo."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Como a categoria kantiana de 'Gênio Artístico' (*Genie*) opera a passagem das regras da natureza para a criação artística autêntica?",
        "O gênio é aquele que copia fielmente manuais didáticos de pintura sem alterar nenhum traço original.",
        "O gênio é o talento inato através do qual a própria natureza dá as regras à arte, produzindo obras exemplares e originais sem que o próprio artista consiga explicar por teoremas lógicos como as criou.",
        "O gênio é o comerciante que obtém os maiores lucros financeiros no leilão de esculturas e quadros.",
        "O gênio é o burocrata estatal encarregado de carimbar alvarás de funcionamento de ateliês de gravura.",
        "O gênio é o soldado que transporta peças de mármore de pedreiras montanhosas para portos fluviais.",
        "B",
        "O gênio para Kant não é quem aprende regras de cor: é o talento da natureza viva que inventa caminhos inéditos; o gênio cria a obra-prima que vira modelo para a história, mas nem ele mesmo sabe provar como a concebeu."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "Qual é a diferença fundamental entre a concepção de 'Sublime' em Edmund Burke (empirista) e em Immanuel Kant (transcendental)?",
        "Burke associava o sublime a equações matemáticas e Kant a manuais de carpintaria naval de caravelas.",
        "Burke explicava o sublime fisiologicamente através do terror físico corporal e do instinto de autopreservação; Kant localiza o sublime na faculdade transcendental da mente, onde o fracasso dos sentidos desperta a Razão.",
        "Burke defendia a proibição de pinturas de tempestades e Kant exigia que todos os cidadãos navegassem oceanos.",
        "Burke considerava o sublime exclusivo de poemas gregos e Kant restrito a monumentos arquitetônicos persas.",
        "Burke e Kant concordavam que o sublime e o belo eram termos sinônimos utilizados para agradar imperadores.",
        "B",
        "Burke era empirista e olhava o susto do corpo (o calafrio nos nervos perante o perigo); Kant vai além: o susto dos sentidos é apenas a faísca que faz a mente humana despertar para a sua nobreza moral e liberdade infinita."
    ))

    questoes_brutas.append((
        35, "EM13CHS301", "intermediario",
        "Como o Neoclassicismo de Jacques-Louis David e o Romantismo de William Turner espelham a contraposição estética entre o 'Belo Harmonioso' e o 'Sublime Avassalador'?",
        "David utilizava unicamente tintas aquosas perecíveis e Turner pintava exclusivamente sobre placas de bronze.",
        "David expressava o Belo neoclássico através de linhas límpidas, proporções geométricas e heroísmo austero; Turner expressava o Sublime romântico através de turbilhões de vapor, fogo, mar em fúria e horizontes infinitos.",
        "David pintava unicamente paisagens marinhas pacíficas e Turner retratava assembleias legislativas solenes.",
        "David defendia a destruição de esculturas clássicas e Turner propunha a extinção de museus de belas artes.",
        "David e Turner foram generais militares que combateram nas guerras navais pelo controle de rotas de especiarias.",
        "B",
        "David é a forma perfeita da razão (o Juramento dos Horácios: linhas retas, luz clara, equilíbrio heroico); Turner é o sublime em carne viva (tempestades no mar, névoa e chamas onde a forma se dissolve no abismo cósmico)."
    ))

    questoes_brutas.append((
        36, "EM13CHS302", "intermediario",
        "Por que, para Hegel, a arte da 'Arquitetura' é a forma de arte mais material e menos espiritual, correspondendo à infância da história da arte?",
        "Porque os arquitetos utilizavam esquadros e réguas de madeira fabricados por corporações de sapateiros.",
        "Porque a arquitetura manipula a matéria bruta e pesada em três dimensões segundo leis da gravidade e da estática exterior, não conseguindo ainda fazer a matéria se tornar a expressão transparente da subjetividade viva.",
        "Porque os edifícios públicos eram destruídos anualmente por tempestades fluviais nas capitais orientais.",
        "Porque os códigos imperiais proibiam a gravação de versos poéticos em colunas e portais de palácios.",
        "Porque os templos de pedra dependiam da importação compulsória de mármores extraídos do mar Báltico.",
        "B",
        "A arquitetura trabalha com pedra maciça, peso e gravidade: a matéria domina o espaço; as pirâmides abrigam o mistério da morte, mas a pedra continua pedra inerte; o espírito só se descola dessa opacidade na escultura e na pintura."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Como a música atua como o 'ápice da interioridade emocional' na forma de arte romântica segundo a estética de Hegel?",
        "Obrigando os ouvintes a realizarem marchas cênicas em formação de combate em salas fechadas.",
        "Abandonando a visibilidade espacial e a matéria corporal tridimensional para vibrar como puro tempo, afeto interior e movimento do sentimento no íntimo da alma do sujeito.",
        "Comprovando que as cordas de instrumentos musicais eram fabricadas exclusivamente com fibras de seda oriental.",
        "Submetendo as partituras musicais a aprovações prévias concedidas por magistrados de alfândegas portuárias.",
        "Exigindo que os concertos sinfônicos fossem realizados unicamente durante períodos de solstício de verão.",
        "B",
        "A música não ocupa lugar no espaço: não tem parede nem cor; ela é tempo, respiração e vibração invisível; para Hegel, a música conversa diretamente com o coração do homem, tocando a interioridade espiritual nua."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "De que modo a reflexão de Kant sobre a 'Comunicação Universal do Sentimento' prefigura a importância da Arte e da Cultura para a convivência democrática nas sociedades pluralistas?",
        "Defendendo que as opiniões divergentes devem ser silenciadas através da censura prévia ministerial.",
        "Demonstrando que a experiência estética educa o ser humano a compartilhar sentimentos e a construir consensos desinteressados com os outros, superando o egoísmo privado através da sensibilidade comum.",
        "Provando que as obras de arte devem ser financiadas exclusivamente por companhias mercantis de exportação.",
        "Exigindo que os museus fechem suas portas aos finais de semana para garantir o descanso de funcionários.",
        "Determinando que as festividades artísticas comunitárias devam ser supervisionadas por generais reformados.",
        "B",
        "A arte é a escola da democracia em Kant: quando duas pessoas de origens diferentes se emocionam diante da mesma sinfonia ou quadro, descobrem que partilham a mesma humanidade sensível, superando o ódio e o egoísmo."
    ))

    questoes_brutas.append((
        39, "EM13CHS301", "intermediario",
        "Por que a crítica de Hegel aos juízos de gosto meramente empíricos ('cada um tem seu gosto e nada mais') é fundamental para a afirmação da Arte como portadora de Verdade histórica?",
        "Porque o filósofo pretendia confiscar todas as coleções privadas de pintura para leiloá-las na bolsa.",
        "Porque se a arte fosse apenas preferência arbitrária de entretenimento particular, ela não passaria de passatempo fútil; ao demonstrar que a arte expressa a Ideia de uma época, Hegel a eleva a documento supremo do Espírito.",
        "Porque os pintores de cortes dependiam de avaliações médicas semanais para a renovação de subsídios.",
        "Porque os tratados de estética deviam ser escritos exclusivamente por professores de teologia escolástica.",
        "Porque as assembleias parlamentares exigiam a padronização das molduras utilizadas em retratos oficiais.",
        "B",
        "Dizer que 'gosto é cada um com o seu' apequena a arte: se a arte fosse só cócega no olho, seria irrelevante; para Hegel, a grande arte revela a alma de uma civilização: a Grécia no mármore, o Egito na pirâmide e a Europa na catedral."
    ))

    questoes_brutas.append((
        40, "EM13CHS302", "intermediario",
        "Como a categoria contemporânea de 'Design' e 'Estética Industrial' desafia a tese kantiana da 'Finalidade sem Fim' ao unir intencionalmente a beleza formal e a funcionalidade utilitária do produto?",
        "Eliminando completamente o uso de computadores no planejamento de ferramentas residenciais modernas.",
        "Criando objetos cotidianos (automóveis, celulares, móveis) cuja beleza estética visual é planejada precisamente para otimizar sua função instrumental prática e seu consumo mercantil, fundindo o belo e o utilitário.",
        "Proibindo o uso de materiais metálicos na fabricação de eletrodomésticos para reduzir custos de energia.",
        "Exigindo que todos os utensílios domésticos sejam esculpidos manualmente em pedras de mármore branco.",
        "Determinando que o design de produtos industriais seja fiscalizado por comissões de filologia clássica.",
        "B",
        "O design moderno subverte Kant: Kant dizia que o belo não tem utilidade prática; o designer de um smartphone ou carro faz o oposto: desenha curvas harmoniosas exatamente para que o aparelho funcione melhor e seja vendido."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a operação arquitetônica de Immanuel Kant na Crítica da Faculdade do Juízo (1790): de que maneira o filósofo erige o 'Juízo Reflexionante Estético' como a ponte mediadora indispensável para reconciliar o abismo entre o reino da Natureza (determinismo da causalidade física) e o reino da Liberdade (imperativo moral incondicional)?",
        "Provando que as academias científicas do século XVIII utilizavam relógios de pêndulo de fabricação suíça.",
        "Demonstrando que, ao passo que o entendimento legisla sobre os fenômenos físicos e a razão pura sobre a vontade moral, a faculdade de julgar reflexionante descobre na experiência da beleza formal a conformidade da natureza com as nossas faculdades espirituais, permitindo ao ser humano conceber que a liberdade moral pode e deve se realizar concretamente no interior do mundo sensível da natureza.",
        "Determinando que os contratos comerciais de compra de madeira devessem ser selados em praças consulares.",
        "Afirmando que a reconciliação entre os reinos da razão foi formulada por generais militares em casernas.",
        "Comprovando que as distinções entre a natureza e a moralidade foram copiadas de códigos monásticos bizantinos.",
        "B",
        "- **Etapa 1:** Compreender a fratura do sistema kantiano: a 1ª crítica diz que a natureza é uma engrenagem de leis cegas e necessárias; a 2ª crítica diz que o homem é livre e tem que cumprir o dever moral no mundo.\n- **Etapa 2:** Descobrir a ponte mágica do juízo estético: na beleza e na finalidade sem fim da natureza e da arte, a mente sente que o mundo físico acolhe as faculdades humanas; o belo dá esperança sensível de que o bem moral pode florescer na Terra."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a tensão dialética entre a 'Imaginação' (*Einbildungskraft*) e o 'Entendimento' (*Verstand*) no Juízo de Gosto kantiano: por que o 'Livre Jogo' sem subordinação a conceitos determinados garante a pureza desinteressada e a universalidade subjetiva da experiência estética?",
        "Mostrando que os artistas de corte utilizavam paletas de tintas padronizadas por decretos imperiais.",
        "Evidenciando que, no conhecimento científico comum, a imaginação é escravizada e limitada pelas regras conceituais rígidas do entendimento; ao passo que, no prazer estético, o entendimento contempla a multiplicidade harmoniosa da forma trazida pela imaginação sem aprisioná-la em uma definição lógica fixa, permitindo que a mente usufrua de uma harmonia livre, aberta e universalmente comunicável a todo ser racional.",
        "Determinando que os pintores devessem prestar juramentos de fidelidade perante magistrados de cortes navais.",
        "Afirmando que o livre jogo das faculdades decorria do consumo compulsório de chás de ervas medicinais.",
        "Comprovando que as avaliações estéticas eram decididas através de sorteios anuais realizados em praças públicas.",
        "B",
        "- **Etapa 1:** Contrastar a ciência com a arte: quando o cientista olha para uma flor, ele a classifica em gênero, espécie e pétalas usando conceitos rígidos do entendimento que fecham a interpretação.\n- **Etapa 2:** Celebrar o livre jogo do gosto: diante do quadro belo, a mente não precisa classificar nem provar nada; imaginação e entendimento brincam livres em harmonia fecunda, proporcionando o prazer contemplativo que qualquer ser humano pode partilhar."
    ))

    questoes_brutas.append((
        43, "EM13CHS301", "dificil",
        "Investigue a analítica kantiana do 'Sublime Dinâmico' diante das catástrofes naturais avassaladoras: de que maneira o terror diante do perigo físico converte-se, através da mediação da Razão prática, em júbilo estético e revelação da superioridade moral da humanidade sobre o império cego da matéria?",
        "Comprovando que os abrigos de montanha utilizavam paredes de pedra assentadas com argamassas especiais.",
        "Demonstrando que, desde que o observador esteja resguardado de perigo imediato real, o espetáculo assombroso de furacões e erupções vulcânicas esmaga nossa pretensão de resistência corporal biológica mortal, mas, por esse mesmo choque, desperta a consciência da lei moral e da dignidade da liberdade que nos tornam cidadãos do mundo inteligível, espiritualmente superiores a qualquer fúria mecânica da natureza física.",
        "Determinando que as expedições a vulcões ativos fossem supervisionadas exclusivamente por astrônomos reais.",
        "Afirmando que a contemplação do perigo natural foi inventada por corporações mercantis de navegação oceânica.",
        "Provando que as sensações de pavor cósmico decorriam unicamente da inalação de vapores de enxofre em fendas vulcânicas.",
        "B",
        "- **Etapa 1:** Descrever o duplo movimento do sublime dinâmico: diante de um furacão devastador, o homem sente a sua fraqueza biológica ridícula; uma rajada de vento ou uma avalanche pode matar o corpo num piscar de olhos.\n- **Etapa 2:** Desvelar a vitória do espírito sobre o cosmos: mesmo sabendo que a pedra pode me esmagar, sei que ela é matéria cega e eu sou um ser dotado de consciência moral e liberdade; o sublime revela a nobreza invencível da alma perante as forças cegas do universo."
    ))

    questoes_brutas.append((
        44, "EM13CHS302", "dificil",
        "Analise a crítica contundente de G. W. F. Hegel ao formalismo e ao subjetivismo kantiano em seus Cursos de Estética: por que o filósofo de Berlim sustenta que a beleza não pode ser reduzida a um sentimento psicológico do sujeito contemplador, exigindo sua inscrição na história da verdade do Espírito Absoluto?",
        "Mostrando que os manuais de estética de Kant eram impressos em gráficas com tipos de chumbo defeituosos.",
        "Evidenciando que Kant confinou o belo ao agrado formal da subjetividade individual em livre jogo cognitivo, ignorando que as grandes obras de arte de uma civilização carregam o conteúdo histórico substantivo da autoconsciência de um povo; para Hegel, a arte é a própria manifestação sensível da Ideia, cujo valor repousa na densidade com que expressa a verdade espiritual de uma época histórica.",
        "Determinando que os museus alemães devessem cobrar ingressos equivalentes ao preço de um saco de farinha de trigo.",
        "Afirmando que a estética subjetiva de Kant foi copiada de manuais de etiqueta social de cortes francesas.",
        "Comprovando que os filósofos do Idealismo alemão participavam de conferências diplomáticas em caravelas mercantes.",
        "B",
        "- **Etapa 1:** Apontar o limite da estética de Kant: Kant tratou a beleza como um sentimento interno que acontece na cabeça do observador diante de uma concha ou flor, esvaziando o significado histórico e cultural da obra.\n- **Etapa 2:** Resgatar a potência histórica em Hegel: a arte não é gosto fútil; a escultura grega ou a catedral gótica são o modo como civilizações inteiras responderam quem são e o que é Deus; a arte é a Ideia tomando corpo vivo na história universal."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Examine a dialética hegeliana da 'Forma de Arte Clássica' na Grécia Antiga: de que maneira a união perfeita e a adequação transparente entre o 'Conteúdo Espiritual' e a 'Forma Sensível Antropomórfica' da estátua grega representam o apogeu da beleza sensível e, simultaneamente, o início de sua superação histórica?",
        "Provando que as ferramentas de ferro para polimento de mármore foram inventadas por guerreiros espartanos.",
        "Demonstrando que, ao encarnar o divino na harmonia finita do corpo humano livre esculpido por Fídias, a arte clássica alcança a perfeição plástica absoluta; contudo, precisamente por haver esgotado a perfeita adequação exterior com a matéria finita, o Espírito descobre ulteriormente que sua interioridade infinita e subjetiva não cabe em nenhum bloco de pedra, abrindo caminho dialético para a arte romântica.",
        "Determinando que as estátuas de deuses devessem ser pintadas exclusivamente com pigmentos de ouro fundido.",
        "Afirmando que a decadência da escultura grega decorreu de derrotas militares em conflitos com frotas persas.",
        "Comprovando que os templos clássicos realizavam leilões de obras de arte para financiar obras de saneamento.",
        "B",
        "- **Etapa 1:** Celebrar o meio-dia da beleza na Grécia clássica: a forma clássica casou a alma divina com o mármore humano em harmonia impecável; nada na história foi tão belo e límpido aos olhos quanto a estátua grega.\n- **Etapa 2:** Reconhecer o limite dialético do mármore: a pedra é finita e exterior; quando o ser humano aprofunda sua alma com o cristianismo e a modernidade, percebe que o amor, a culpa e a fé infinita não cabem na estátua; o espírito precisa quebrar o mármore e buscar a música e o pensamento."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Investigue a tese hegeliana do 'Fim da Arte' (*Das Ende der Kunst*): de que maneira o filósofo desmistifica a acusação vulgar de que a produção artística teria cessado fisicamente, demonstrando que a arte perdeu sua função histórica como expressão suprema da Verdade Absoluta em uma modernidade dominada pelo pensamento reflexivo?",
        "Comprovando que as fábricas de papel da Prússia suspenderam a produção de blocos de desenho para pintores.",
        "Evidenciando que a proclamação hegeliana é de ordem estrutural e histórica: a arte não acabou empiricamente, mas deixou de ser o veículo definitivo pelo qual uma cultura se ajoelha perante os deuses e decifra o sentido do cosmos; no mundo moderno secular, a arte tornou-se objeto de juízo crítico, sociologia e estética reflexiva, cabendo à Filosofia e ao conceito abstrato a tarefa suprema de pensar a Verdade.",
        "Determinando que os ministérios de educação devam banir as aulas de artes práticas dos currículos escolares.",
        "Afirmando que o declínio da arte decorreu da invenção de máquinas a vapor e locomotivas mecânicas industriais.",
        "Provando que a tese do fim da arte foi formulada para justificar a cobrança de tributos fiscais sobre espetáculos teatrais.",
        "B",
        "- **Etapa 1:** Desmentir a lenda de que 'Hegel matou a arte': Hegel sabia que haveria milhares de novos romances, óperas e telas; ele não predisse o fim dos pincéis, mas o fim da veneração religiosa da estátua.\n- **Etapa 2:** Confirmar a era da reflexão e da filosofia: hoje ninguém reza para um quadro no museu achando que o próprio Deus habita o óleo da tela; nós criticamos, teorizamos e julgamos a obra com a razão; a verdade do nosso tempo é filosófica e conceitual."
    ))

    questoes_brutas.append((
        47, "EM13CHS301", "dificil",
        "Analise a relação entre a 'Finalidade sem Fim' de Kant e a resistência das obras de arte contra a lógica da 'Mercadorização Capitalista': como o caráter desinteressado e a ausência de função utilitária instrumental protegem a dignidade estética contra a redução de tudo a valor de troca de mercado?",
        "Provando que as galerias comerciais de arte utilizam notas fiscais autenticadas por tabelionatos provinciais.",
        "Demonstrando que, ao postular que o objeto belo não serve a um propósito externo nem a uma finalidade utilitária de consumo imediato, a analítica kantiana oferece a base conceitual para refutar a redução da arte a mercadoria fútil, afirmando a obra como um refúgio da gratuidade, da contemplação desalienada e da autonomia formal diante do império do lucro monetário.",
        "Determinando que os artistas plásticos devam doar seus quadros a hospitais públicos de atendimento infantil.",
        "Afirmando que as teorias de mercado capitalista foram extraídas de tratados de estética do Iluminismo francês.",
        "Comprovando que as exposições de pintura são isentas do pagamento de tarifas alfandegárias portuárias.",
        "B",
        "- **Etapa 1:** Reconhecer a obsessão do capitalismo em transformar tudo em mercadoria: o mercado quer que tudo sirva para algo prático, tenha preço de etiqueta e possa ser consumido ou vendido com lucro.\n- **Etapa 2:** Resgatar a trincheira de resistência da finalidade sem fim: ao dizer que o belo agrada desinteressadamente sem utilidade instrumental externa, Kant blinda a arte; uma flor ou um poema belo são valiosos em si mesmos, recusando a humilhação de virarem pura moeda de troca."
    ))

    questoes_brutas.append((
        48, "EM13CHS302", "dificil",
        "Examine a influência do conceito de 'Sublime' kantiano na poética do 'Romantismo Sombrio' e na pintura de tempestades de William Turner: de que maneira o esfacelamento das fronteiras geométricas e a dissolução da luz em turbilhões de vapor encarnam o colapso da representação sensível diante da infinitude cósmica?",
        "Provando que os pigmentos de óleo utilizados por Turner eram diluídos em solventes químicos inflamáveis.",
        "Evidenciando que, enquanto a pintura clássica renascentista buscava a linha nítida, a estabilidade e o repouso sereno da forma finita, a arte de Turner desmantela a contorno estável dos objetos, submergindo locomotivas, navios e marinheiros em abismos cósmicos de tempestade, bruma e fogo onde a imaginação sensorial naufraga perante a magnitude avassaladora do sublime.",
        "Determinando que as telas marítimas devessem ser emolduradas com madeiras de carvalho colhidas no inverno.",
        "Afirmando que o estilo de Turner foi copiado de compêndios de engenharia naval de frotas mercantes britânicas.",
        "Comprovando que as pinturas de tempestades eram utilizadas para alertar pescadores sobre previsões meteorológicas.",
        "B",
        "- **Etapa 1:** Contrastar a clareza da forma clássica com o turbilhão romântico: a arte clássica traça contornos nítidos onde cada coisa fica no seu lugar com luz límpida e perspectiva geométrica.\n- **Etapa 2:** Mergulhar no sublime de Turner: nas telas de Turner (como Chuva, Vapor e Velocidade), a fumaça engole o trem e o mar engole o navio; a forma geométrica se despedaça perante a força do universo; é o sublime kantiano pintado na tela com espanto e assombro."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Investigue o diálogo entre a tese hegeliana do 'Fim da Arte' e as vanguardas estéticas do século XX (como o Dadaísmo e a Arte Conceitual de Marcel Duchamp): como a colocação de um objeto industrial comum em um pedestal de museu confirmou a dissolução da beleza formal na reflexão conceitual filosófica?",
        "Comprovando que os materiais cerâmicos industriais possuíam patentes registradas em alfândegas portuárias.",
        "Demonstrando que, ao apresentar o mictório invertido como obra em 1917, Duchamp esvaziou qualquer resquício de manufatura virtuosa ou beleza sensível tradicional, transferindo a totalidade do acontecimento estético para a pergunta teórica e para o choque conceitual da mente ('o que define a arte?'), concretizando a previsão de Hegel de que a arte se converteria em filosofia.",
        "Determinando que as peças de ready-made devessem ser higienizadas semanalmente com soluções de amoníaco.",
        "Afirmando que as vanguardas estéticas foram financiadas por companhias mercantis de transporte ferroviário.",
        "Provando que os museus modernos proibiam a exibição de quadros a óleo confeccionados no século XIX.",
        "B",
        "- **Etapa 1:** Compreender o gesto demolidor de Duchamp: ao assinar um mictório comprado numa loja de canos e colocá-lo num pedestal, ele disse 'aqui não há beleza de mármore nem virtude técnica de pincel'.\n- **Etapa 2:** Confirmar a profecia de Hegel: se não há beleza sensível, por que aquilo é arte? Porque aquilo obriga a mente a pensar e debater o próprio conceito de arte; o mictório de Duchamp é a prova viva de que a arte moderna se desmaterializou em filosofia pura."
    ))

    questoes_brutas.append((
        50, "EM13CHS102", "dificil",
        "Analise a distinção kantiana entre o 'Juízo de Gosto Puro' e o 'Juízo Empírico dos Sentidos': por que a confusão entre o valor universal do belo e a simples gratificação fisiológica do apetite carnal degrada a dignidade da reflexão estética em mero hedonismo subjetivista?",
        "Provando que os cardápios de restaurantes utilizavam impressões tipográficas com tintas ecológicas minerais.",
        "Evidenciando que o agrado fisiológico empírico (o sabor de um prato ou o conforto térmico de um manto) depende da constituição particular dos órgãos corporais de cada indivíduo e não tem direito a exigir a concordância alheia; ao passo que o belo puro assenta-se no livre jogo das faculdades cognitivas humanas que todo ser racional compartilha, elevando a experiência estética acima do egoísmo sensorial animal.",
        "Determinando que os cidadãos devessem comparecer a exposições artísticas em jejum de alimentos sólidos.",
        "Afirmando que o hedonismo gastronômico foi a doutrina fundadora das primeiras escolas de pintura renascentistas.",
        "Comprovando que os juízos de gosto eram fiscalizados por comissões de saúde pública e higiene militar.",
        "B",
        "- **Etapa 1:** Desmascarar o 'gosto gastronômico': se eu adoro pimenta e você odeia, isso é mera reação dos nossos nervos na língua; ninguém briga porque outro não gosta de jiló; o agradável é fisiologia privada animal.\n- **Etapa 2:** Elevar o juízo de gosto puro: quando dizemos que a Nona Sinfonia de Beethoven é bela, não estamos falando de sabor de comida; estamos falando de uma harmonia espiritual que apela à inteligência e ao coração de toda a humanidade."
    ))

    questoes_brutas.append((
        51, "EM13CHS301", "dificil",
        "Examine o conceito de 'Forma de Arte Romântica' em Hegel e a ascensão da 'Música' e da 'Poesia' como expressões da interioridade cristã e moderna: de que maneira o esgotamento da escultura clássica reflete a descoberta de que o infinito da alma humana não cabe na finitude da matéria exterior?",
        "Comprovando que as partituras de cantos litúrgicos medievais utilizavam folhas de pergaminho vegetal.",
        "Demonstrando que, com a emergência do princípio da subjetividade livre, da culpa, do amor e da redenção espiritual, o Espírito humano transborda a casca exterior do mármore grego; a música (que é puro tempo sonoro sem espaço) e a poesia (que opera pela imaginação pura da palavra) tornam-se os receptáculos adequados para exprimir as dores, esperanças e a infinita transcendência interior da consciência moderna.",
        "Determinando que os escultores devessem migrar obrigatoriamente para corporações de carpinteiros navais.",
        "Afirmando que a decadência da escultura decorreu do encarecimento das ferramentas de bronze na Europa central.",
        "Provando que as catedrais góticas eram utilizadas exclusivamente para a estocagem de cereais agrícolas no inverno.",
        "B",
        "- **Etapa 1:** Compreender a revolução da interioridade na alma moderna: a estátua grega é perfeita por fora, mas é calada e fria por dentro; quando surge a consciência da culpa, do pecado, da redenção e do amor infinito, a pedra racha.\n- **Etapa 2:** Consagrar o triunfo da música e da poesia: o sofrimento e a paixão da alma humana só encontram eco no som que vibra no peito sem ocupar espaço (música) e na palavra poética que constrói mundos inteiros na mente; a arte vira espírito puro."
    ))

    questoes_brutas.append((
        52, "EM13CHS302", "dificil",
        "Investigue a advertência de Theodor Adorno em Teoria Estética sobre a 'Arte Afirmativa e Conciliatória' à luz da estética hegeliana: por que a beleza que oferece harmonia fácil e consolo sentimental em um mundo despedaçado por guerras e desigualdades atua como ideologia de apaziguamento da opressão social?",
        "Provando que as canções de música popular eram gravadas em estúdios desprovidos de isolamento acústico.",
        "Demonstrando que, quando a arte contemporânea insiste em pintar mundos dourados e reconciliados fingindo que não existem o sofrimento, o racismo e a miséria, ela vende uma ilusão entorpecente que reconcilia falsamente os oprimidos com suas correntes; para Adorno, a arte autêntica deve ser a ferida aberta da sociedade, mantendo a dissonância que recusa calar diante da barbárie.",
        "Determinando que as salas de concerto devam manter suas luzes acesas durante a execução de sinfonias.",
        "Afirmando que os compositores de vanguarda eram sustentados financeiramente por companhias mercantis de sal.",
        "Comprovando que as teorias de Adorno foram formuladas a partir de regulamentos disciplinares militares prussianos.",
        "B",
        "- **Etapa 1:** Diagnosticar o perigo da 'beleza adocicada': obras que vendem finais felizes açucarados e harmonia fácil funcionam como um calmante para quem é explorado na vida real, dizendo 'tudo está em paz'.\n- **Etapa 2:** Resgatar a missão crítica da arte dissonante: Adorno lembra que vivemos num mundo que gerou Auschwitz e as favelas; a arte séria não pode ser anestesia alegre da classe dominante; ela tem que chocar, incomodar e manter acesa a indignação contra a injustiça."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Analise a relevância do 'Sublime Matemático' kantiano na Astrofísica e na Cosmologia contemporâneas (como nas imagens de galáxias profundas capturadas pelo Telescópio Espacial James Webb): de que maneira o choque da mente humana perante bilhões de anos-luz e trilhões de estrelas atualiza a dialética entre a impotência dos sentidos e a grandeza da Razão?",
        "Provando que os telescópios espaciais utilizam espelhos de berílio revestidos por lâminas de ouro fundido.",
        "Evidenciando que a contemplação de fotografias de campos profundos do cosmos escancara o colapso sensorial da imaginação humana, que não consegue abarcar distâncias de bilhões de anos-luz nem a imensidão do vácuo cósmico; contudo, a própria capacidade científica da inteligência humana de teorizar as leis do Big Bang e construir o telescópio revela a vitória da Razão que concebe o infinito com reverência estética sublime.",
        "Determinando que as imagens astrofísicas devessem ser exibidas unicamente em sessões de academias de jurisprudência.",
        "Afirmando que a admiração astronômica foi inventada por corporações mercantis de transporte fluvial em rios.",
        "Comprovando que as constelações galácticas eram catalogadas exclusivamente para orientar rotas de caravelas mercantes.",
        "B",
        "- **Etapa 1:** Sentir o choque da insignificância humana no universo: ao olhar para a foto do James Webb com milhares de galáxias onde cada pontinho de luz tem 100 bilhões de sóis, o cérebro humano buga; a imaginação falha diante do infinito.\n- **Etapa 2:** Reconhecer a glória da mente que compreende: quem construiu o espelho do telescópio e equacionou a física que decifra aquela luz fóssil foi a inteligência de um animal frágil na Terra; o sublime une o pavor da pequenez ao júbilo da Razão humana."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Examine o conceito kantiano de 'Sensus Communis' (Sentido Comum Estético) em contraponto ao 'Senso Comum' vulgar empírico: por que o juízo de gosto não se apoia na média estatística dos preconceitos populares da maioria, mas na suposição transcendental de uma comunicabilidade universal do sentimento entre seres racionais livres?",
        "Mostrando que as pesquisas de opinião pública sobre arte utilizavam questionários impressos em papéis coloridos.",
        "Evidenciando que o senso comum vulgar é apenas a soma dos hábitos, clichês e preconceitos passivos de uma sociedade em um dado momento; ao passo que o Sensus Communis estético kantiano é uma faculdade ideal da mente que exige que o indivíduo saia de seu egoísmo sensorial privado e pense 'do ponto de vista de qualquer outro', aspirando a uma universalidade partilhada da dignidade humana.",
        "Determinando que os críticos de arte devam aplicar testes de alfabetização aos frequentadores de museus.",
        "Afirmando que a sensibilidade estética foi uma concessão concedida por monarcas absolutistas a plebeus.",
        "Comprovando que as preferências artísticas populares eram calculadas por escrivães de alfândegas provinciais.",
        "B",
        "- **Etapa 1:** Separar o senso comum vulgar do sensus communis de Kant: senso comum na rua é o preconceito da maioria (o clichê 'arte moderna é rabisco de criança que não sabe desenhar').\n- **Etapa 2:** Fundamentar a grandeza transcendental de Kant: o sensus communis estético é a capacidade nobre de sair do próprio umbigo e julgar como um cidadão do mundo; ele nos desafia a olhar para a obra a partir da sensibilidade universal de qualquer outro ser humano."
    ))

    questoes_brutas.append((
        55, "EM13CHS301", "dificil",
        "Analise a contradição entre a 'Autonomia Estética Moderna' (iniciada por Kant e Hegel) e a captura contemporânea da arte pelos algoritmos de recomendação e pelas métricas de engajamento do Capitalismo de Plataforma: de que maneira o império das visualizações destrói a contemplação desinteressada e a densidade histórica da obra?",
        "Provando que as plataformas digitais utilizam servidores de computação instalados em porões de edifícios antigos.",
        "Demonstrando que, ao submeter a criação cultural à tirania da retenção de segundos, dos cliques e do consumo compulsivo monetizado, as plataformas digitais anulam a autonomia estética: a arte deixa de ser finalidade sem fim ou manifestação sensível da Ideia para se degradar em mercadoria algorítmica passageira desenhada para excitar os sentidos e gerar lucro corporativo imediato.",
        "Determinando que as telas de smartphones devam utilizar iluminação monocromática para a leitura de poemas clássicos.",
        "Afirmando que a inteligência algorítmica foi inventada por corporações têxteis para acelerar o tecer de mantos.",
        "Comprovando que os museus virtuais dependem de autorização expressa emitida por comissões de generais militares.",
        "B",
        "- **Etapa 1:** Recordar a conquista da autonomia em Kant e Hegel: a arte lutou séculos para se libertar dos padres e dos reis, provando que é um fim em si mesma e a voz do espírito livre.\n- **Etapa 2:** Denunciar o aprisionamento algorítmico de hoje: o feed das redes sociais tritura a arte; músicas são feitas para virar dancinha de 15 segundos no TikTok e quadros viram posts descartáveis; o algoritmo mata o desinteresse e transforma a cultura em caça-níquel de dopamina."
    ))

    questoes_brutas.append((
        56, "EM13CHS302", "dificil",
        "Examine a tese hegeliana de que 'a arte simbólica é a busca da forma, a clássica é o encontro harmonioso da forma e a romântica é o ultrapassamento da forma': como essa tríade dialética espelha a própria odisséia do Espírito humano em busca de sua liberdade absoluta no cosmos?",
        "Provando que as civilizações antigas utilizavam calendários agrícolas com meses divididos em semanas de dez dias.",
        "Demonstrando que no Egito a Ideia busca a forma mas é esmagada pela matéria pesada da pedra; na Grécia a Ideia encontra seu lar perfeito e transparente no corpo humano límpido; e na modernidade romântica o Espírito descobre que sua profundidade infinita transcende qualquer matéria, completando a libertação do pensamento que culminará na autoconsciência filosófica plena.",
        "Determinando que as obras de arte clássicas devessem ser enterradas em covas rasas após festivais cívicos.",
        "Afirmando que a evolução da arte decorreu exclusivamente de melhorias no transporte marítimo de pigmentos.",
        "Comprovando que a tríade hegeliana foi copiada de manuais de estratégia militar de infantaria romana antiga.",
        "B",
        "- **Etapa 1:** Sintetizar os três passos da dialética da arte: a Arquitetura oriental busca o formato na montanha de pedras; a Escultura grega atinge a harmonia milagrosa da forma no mármore; a Poesia moderna rompe a forma exterior.\n- **Etapa 2:** Coroar a marcha da liberdade humana: não é apenas história de quadros e estátuas; é a própria história do ser humano aprendendo que não é escravo da matéria cega, descobrindo passo a passo que é espírito livre dotado de razão e infinito."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Investigue o papel pedagógico e emancipatório da Estética no Ensino Médio de acordo com a BNCC: de que maneira o aprendizado das teorias do Juízo de Gosto de Kant e da historicidade da arte em Hegel instrumentaliza os jovens contra a passividade alienante do consumo cultural de massas?",
        "Provando que as matrizes curriculares escolares devem priorizar unicamente a reprodução de cópias de desenhos pré-fabricados.",
        "Evidenciando que a formação estética desaliena o estudante: ensina a contemplar com autonomia crítica e desinteresse libertador, desconfiando de modismos impostos pelo mercado, compreendendo as raízes históricas das linguagens visuais e valorizando a arte como uma arena viva de expressão da dignidade, da diversidade e da autoconsciência da condição humana.",
        "Determinando que os estudantes devessem realizar avaliações pedagógicas unicamente através de testes de memorização de datas.",
        "Afirmando que o estudo de filosofia da arte deve ser suspenso nas escolas públicas para reduzir despesas de material didático.",
        "Comprovando que a apreciação artística escolar depende de laudos emitidos por comissões disciplinares militares.",
        "B",
        "- **Etapa 1:** Denunciar a passividade da juventude tragada pelo consumo raso: a indústria cultural quer jovens passivos que consumam qualquer modismo enlatado sem pensar.\n- **Etapa 2:** Libertar a mente com Kant e Hegel na BNCC: aprender estética ensina o jovem a julgar com a própria cabeça, a enxergar a história por trás de cada imagem e a respeitar a arte como patrimônio sagrado da liberdade e da inteligência humana."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Analise a relação entre o conceito hegeliano de 'Manifestação Sensível da Ideia' e o patrimônio da arquitetura colonial barroca brasileira (como as igrejas de Ouro Preto esculpidas por Aleijadinho): de que maneira o gênio barroco mineiro imprimiu o Espírito de resistência e religiosidade na dureza da pedra-sabão e do cedro?",
        "Mostrando que os monumentos coloniais de Minas Gerais foram desenhados com base em planos de quartéis prussianos.",
        "Demonstrando que Aleijadinho subverteu a matéria bruta da pedra-sabão e do cedro para materializar o drama sagrado, a dor, a esperança e a espiritualidade de um povo escravizado e mestiço sob o jugo colonial, transformando capelas e os profetas de Congonhas na mais vigorosa manifestação sensível da Ideia e da dignidade humana no barroco universal.",
        "Determinando que os templos religiosos barrocos devessem ser demolidos após a conclusão das colheitas de café.",
        "Afirmando que a escultura em pedra-sabão foi introduzida no Brasil por navegadores mercantes do mar Báltico.",
        "Comprovando que as obras de Aleijadinho dependiam de autorização prévia emitida por tribunais de comércio britânicos.",
        "B",
        "- **Etapa 1:** Descrever o milagre de Aleijadinho nas Minas do ouro: com o corpo mutilado pela doença, amarrando o cinzel nos punhos, ele esculpiu profetas e passos da paixão em pedra-sabão e madeira de cedro.\n- **Etapa 2:** Confirmar a tese de Hegel no Brasil: Aleijadinho não copiou Lisboa friamente; ele fez a pedra chorar o sofrimento do escravo e do povo oprimido; os profetas de Congonhas são a Ideia de liberdade e transcendência brilhando viva na rocha mineira."
    ))

    questoes_brutas.append((
        59, "EM13CHS301", "dificil",
        "Examine o conceito de 'Necessidade Exemplar' no juízo de gosto kantiano: por que, embora o indivíduo não possa demonstrar logicamente que um quadro é belo, ele legitimamente supõe que todos os outros deveriam concordar com seu julgamento, tratando seu sentimento como um 'dever-sentir' compartilhado?",
        "Comprovando que as galerias de arte utilizavam sistemas de votação informatizados em urnas eletrônicas.",
        "Demonstrando que o juízo de gosto não expressa mera certeza matemática privada, mas uma exigência ética e cognitiva fundada na hipótese necessária de um sentido comum (Sensus Communis): julgamos como se fôssemos a voz exemplar da própria humanidade, demandando que a sensibilidade alheia seja capaz de vibrar na mesma afinação da harmonia formal das faculdades humanas.",
        "Determinando que os críticos que discordassem de opiniões majoritárias devessem pagar multas consulares.",
        "Afirmando que a necessidade exemplar foi copiada de regulamentos jurídicos de tribunais de navegação naval.",
        "Provando que a apreciação artística dependia de atestados de aprovação expedidos por congregações religiosas beneditinas.",
        "B",
        "- **Etapa 1:** Compreender a estranha força do 'isto é belo': quando eu digo 'este sorvete é gostoso para mim', sei que você pode não gostar; mas quando contemplo a Capela Sistina e digo 'isto é belo', espero que qualquer ser humano veja essa beleza.\n- **Etapa 2:** Revelar a necessidade exemplar: essa expectativa de concordância não é tirania; é a crença de que compartilhamos uma mesma mente e sensibilidade humana; julgamos em nome de toda a humanidade, oferecendo nosso sentimento como um exemplo vivo de harmonia."
    ))

    questoes_brutas.append((
        60, "EM13CHS302", "dificil",
        "Ao encerrarmos o Capítulo 26 com a Estética Moderna de Kant e Hegel, analise como o legado do gosto desinteressado, do sublime e da historicidade da Ideia prepara o terreno filosófico para o Capítulo 27, onde Friedrich Nietzsche demolirá o racionalismo estético clássico com o choque entre o Apolíneo e o Dionisíaco em O Nascimento da Tragédia:",
        "Provando que as investigações filosóficas da arte perderam qualquer utilidade teórica com a expansão das ferrovias a vapor.",
        "Demonstrando que, após Kant emancipar o juízo de gosto e Hegel declarar o fim da arte pela supremacia do conceito reflexivo, Nietzsche insurgir-se-á contra a tirania da razão socrática, resgatando a força telúrica, selvagem e trágica de Dioniso para proclamar que a existência e o mundo só se justificam plenamente como fenômeno estético vivo e passional.",
        "Determinando que os manuais didáticos futuros devam limitar-se ao estudo de compêndios de agronomia prática rural.",
        "Afirmando que Nietzsche rejeitou a leitura dos textos de Kant e Hegel por considerá-los autores de peças teatrais cômicas.",
        "Comprovando que a transição entre capítulos depende de aprovações formais expedidas por cortes de comércio marítimo internacional.",
        "B",
        "- **Etapa 1:** Sintetizar o cume da estética racional moderna: Kant libertou o gosto e ergueu o sublime moral; Hegel desdobrou a arte na marcha do Espírito Absoluto e coroou a Filosofia no cume do pensamento.\n- **Etapa 2:** Abrir as portas com entusiasmo para Nietzsche no Capítulo 27: Nietzsche chegará com o martelo na mão dizendo 'a razão matou a vida!'; resgatará a embriaguez de Dioniso contra a medida de Apolo, provando que a arte trágica é a maior alavanca da vida; fechamos o Cap 26 com a chave de ouro da modernidade!"
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
    linhas.append('capitulo: "Capítulo 26: A Estética Moderna: Kant e Hegel"')
    linhas.append('objeto_de_conhecimento: "A analítica do belo e do sublime em Kant, o juízo de gosto desinteressado, a finalidade sem fim, a estética hegeliana da manifestação sensível da Ideia e a tese do fim da arte"')
    linhas.append('ebook_fonte: "em-fil-c26-estetica-moderna-kant-hegel.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS301"')
    linhas.append('  - "EM13CHS302"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: A Estética Moderna: Kant e Hegel\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-26-estetica-moderna-kant-hegel -->"
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
    linhas.append("- KANT, Immanuel. *Crítica da faculdade do juízo*. Tradução de Valerio Rohden e António Marques. 2. ed. Rio de Janeiro: Forense Universitária, 2005.")
    linhas.append("- HEGEL, Georg Wilhelm Friedrich. *Cursos de estética: volume I*. Tradução de Marco Aurélio Werle e Oliver Tolle. 2. ed. São Paulo: Edusp, 2001.")
    linhas.append("- DUARTE, Rodrigo. *O belo autônomo: textos clássicos de estética*. Belo Horizonte: Autêntica Editora, 2012.")
    linhas.append("- WERLE, Marco Aurélio. *A questão do fim da arte em Hegel*. São Paulo: Hedra, 2011.")
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

    destino_final = "content/medio/volume-unico/filosofia/eixo-4-estetica/cap-26-estetica-moderna-kant-hegel/ebooks/em-fil-c26-estetica-moderna-kant-hegel-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 26 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
