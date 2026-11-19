# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 28 de Filosofia EM:
A Reprodutibilidade Técnica em Walter Benjamin
Objeto: cap-28-reprodutibilidade-tecnica-walter-benjamin
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
        "Em qual célebre ensaio de 1936 Walter Benjamin investiga o impacto das tecnologias de reprodução em massa sobre a arte?",
        "Em O Conceito de História, que analisa as teses sobre o tempo messiânico.",
        "Em A Obra de Arte na Era de sua Reprodutibilidade Técnica, analisando o cinema e a fotografia.",
        "Em Rua de Mão Única, dedicado a aforismos urbanos e vinhetas parisienses.",
        "Em Origem do Drama Trágico Alemão, focado nas peças barrocas do luto.",
        "Em O Narrador, dedicado à sabedoria ancestral das narrativas de camponeses.",
        "B",
        "O ensaio de 1936 é o marco fundador da estética materialista moderna, desvendando como as mídias industriais transformaram radicalmente a função social da arte."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Como Walter Benjamin define de forma poética e rigorosa o conceito de 'Aura' da obra de arte tradicional?",
        "A quantia financeira obtida pelo leilão de pinturas raras em praças comerciais.",
        "Uma trama singular de espaço e tempo: a aparição única de uma coisa distante, por mais perto que ela esteja.",
        "A composição química dos pigmentos de tinta a óleo aplicados sobre placas de madeira.",
        "O certificado formal de autenticidade emitido por tabelionatos provinciais de cortes régias.",
        "A velocidade de rotação das bobinas de películas em projetores cinematográficos de salas escuras.",
        "B",
        "A aura benjaminiana expressa a singularidade sagrada da obra: sua distância mística e sua presença irrepetível no tempo e no espaço que despertam veneração solene."
    ))

    questoes_brutas.append((
        3, "EM13CHS301", "basico",
        "Qual elemento material fundamenta a autenticidade e a autoridade histórica da obra de arte com aura?",
        "O número de série gravado em carimbos industriais de prensas tipográficas.",
        "O seu 'aqui e agora' (hic et nunc), compreendendo sua presença física única e sua história viva de conservação.",
        "O valor do seguro contra roubos contratado por galerias comerciais privadas.",
        "A quantidade de cópias litográficas distribuídas gratuitamente em feiras municipais.",
        "O peso bruto da moldura de cedro dourada utilizada na exposição em salões palacianos.",
        "B",
        "A autenticidade da obra tradicional depende de sua localização real única: o quadro que sobreviveu séculos, absorvendo a fuligem do tempo e a história concreta de suas mãos."
    ))

    questoes_brutas.append((
        4, "EM13CHS302", "basico",
        "Quais inovações tecnológicas do final do século XIX e início do século XX inauguraram a era da reprodutibilidade técnica em massa?",
        "A fabricação manual de instrumentos de corda em ateliês familiares de marcenaria.",
        "A Fotografia de lentes industriais e o Cinema baseado na reprodução mecânica de fotogramas em série.",
        "A encadernação artesanal de manuscritos jurídicos com capas de couro bovino curtido.",
        "O corte manual de pedras calcárias para a construção de colunas de templos religiosos.",
        "O uso de caravelas mercantes movidas a vento para o transporte de tecidos de algodão cru.",
        "B",
        "A fotografia e o cinema mudaram tudo: pela primeira vez a própria criação da obra tornou-se técnica e reprodutível industrialmente em milhões de cópias iguais."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "O que impulsiona o processo histórico de declínio e perda da aura da arte na sociedade urbana de massas?",
        "A escassez mundial de madeiras nobres utilizadas na confecção de cavaletes para pintores.",
        "A necessidade das massas de aproximar espacialmente as coisas e a tendência de superar a unicidade pela repetição em série.",
        "A proibição papal da celebração de missas solenes em catedrais dotadas de altares góticos.",
        "A diminuição drástica do número de estudantes matriculados em cursos de desenho técnico.",
        "O fechamento obrigatório de museus de belas artes durante períodos de colheita agrícola.",
        "B",
        "O homem moderno das metrópoles quer a obra por perto: quer vê-la no livro, no jornal ou na parede de casa, quebrando o distanciamento aristocrático e a exclusividade do original."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Em qual domínio da atividade humana a obra de arte tradicional esteve historicamente enraizada antes de sua secularização?",
        "Na elaboração de balanços contábeis de corporações mercantis marítimas em portos abertos.",
        "Na esfera do Ritual mágico e religioso, servindo à veneração devota e a liturgias sagradas.",
        "No treinamento tático de regimentos de cavalaria armada para combates fronteiriços.",
        "Na catalogação burocrática de impostos alfandegários recolhidos em províncias imperiais.",
        "Na aferição metrológica de pesos e medidas de cereais comercializados em bazares públicos.",
        "B",
        "A arte nasceu no altar e na caverna mágica: a estátua do faraó ou o ícone do santo existiam para o culto sagrado; a autoridade da aura é a herança direta desse antigo poder ritual."
    ))

    questoes_brutas.append((
        7, "EM13CHS301", "basico",
        "Como se caracteriza a esfera do 'Valor de Culto' (Kultwert) na história da arte tradicional?",
        "Pela obrigação de projetar as imagens em telas gigantescas montadas em praças cívicas.",
        "Pela exigência de manter a obra oculta e recolhida em espaços sagrados fechados para a veneração reverente.",
        "Pelo comércio ambulante de cópias impressas em papel jornal distribuídas a trabalhadores urbanos.",
        "Pela realização de votações populares semanais para a escolha dos melhores afrescos murais.",
        "Pela venda de ingressos com recibos numerados para acesso de multidões aos ateliês de escultura.",
        "B",
        "No valor de culto, o mais importante é que a obra exista para a divindade, não que todos a vejam; certas esculturas ficavam na escuridão dos santuários, vistas apenas por sacerdotes."
    ))

    questoes_brutas.append((
        8, "EM13CHS302", "basico",
        "O que distingue fundamentalmente a esfera moderna do 'Valor de Exposição' (Ausstellungswert)?",
        "O recolhimento forçado de todas as imagens em cofres subterrâneos vedados a visitantes.",
        "A prevalência da exibição pública e do acesso do maior número possível de pessoas para o julgamento visual coletivo.",
        "A exclusão de qualquer representação de figuras humanas em painéis decorativos urbanos.",
        "A exigência de que os pintores trabalhem unicamente em ateliês instalados no topo de torres.",
        "A proibição do uso de legendas explicativas em exposições montadas em centros de convenções.",
        "B",
        "O valor de exposição inverte o culto: a obra moderna só faz sentido se for vista, exibida e debatida pelo grande público; o museu, o cartaz e a tela de cinema nascem dessa nova lógica."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Qual gênero fotográfico serviu como o 'último refúgio defensivo' do valor de culto na aurora da fotografia?",
        "A fotografia aérea de paisagens montanhosas com grandes formações geológicas abertas.",
        "O Retrato humano dos rostos de parentes ausentes ou falecidos, mantendo um halo de lembrança emotiva e reverência.",
        "O registro documental de peças mecânicas de locomotivas a vapor em pátios industriais.",
        "A fotografia de animais de pastoreio confinados em currais de fazendas leiteiras.",
        "O enquadramento topográfico de leitos de rios navegáveis para orientar capitanias portuárias.",
        "B",
        "Ao fotografar a mãe, o filho ou o avô que morreu, a família ainda olhava o retrato com carinho e oração; ali a aura sobreviveu como último suspiro da memória afetuosa do rosto humano."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Como a montagem cinematográfica altera a atitude do espectador em comparação à contemplação de um quadro a óleo em uma galeria?",
        "Substitui a reflexão ativa por um sono hipnótico contínuo provocado pelo calor da sala escura.",
        "Quebra o devaneio passivo e solitário por meio do choque perceptivo contínuo da rápida sucessão de planos e imagens cortadas.",
        "Obriga o visitante a permanecer em pé e descalço durante toda a projeção dos rolos de filme.",
        "Impede que a coletividade de espectadores manifeste risos ou comentários durante as exibições.",
        "Exige a leitura prévia de tratados de ótica física para a compreensão do enredo dramático.",
        "B",
        "No quadro na parede o burguês se isola e viaja em devaneio calmo; no cinema a montagem emenda um plano no outro como choques na retina, exigindo um estado de atenção desperta e viva."
    ))

    questoes_brutas.append((
        11, "EM13CHS301", "basico",
        "O que significa a revelação do 'Inconsciente Óptico' proporcionada pelo uso de lentes cinematográficas?",
        "A medição matemática das pulsações cardíacas dos atores durante cenas de combate corporal.",
        "A capacidade da câmera de desvelar detalhes, tremores e movimentos da matéria que o olho humano nu jamais conseguiria registrar.",
        "A gravação clandestina de confissões religiosas realizadas no interior de templos sacramentais.",
        "A elaboração de previsões astrológicas sobre colheitas agrícolas com base em eclipses solares.",
        "O cálculo da quantidade de luz refletida por espelhos de prata instalados em cabines de projeção.",
        "B",
        "A câmera lenta mostra o cavalo saltando no ar e o close-up revela a micro-expressão do lábio; assim como Freud descobriu o inconsciente da mente, a câmera revela o inconsciente óptico da matéria."
    ))

    questoes_brutas.append((
        12, "EM13CHS302", "basico",
        "Quais recursos técnicos cinematográficos foram destacados por Benjamin como instrumentos privilegiados do inconsciente óptico?",
        "A iluminação com tochas de breu e o uso de cortinas de veludo vermelho ao redor do tablado.",
        "O Close-up (primeiro plano detalhado da fisionomia) e a Câmera Lenta (slow-motion que desacelera o movimento).",
        "A projeção de sombras chinesas com cartolinas pretas sobre paredes de salas de jantar familiares.",
        "A pintura manual de molduras de madeira para guardar rolos de películas de celulóide.",
        "A queima de compostos químicos aromáticos para perfumar o ar durante as sessões públicas.",
        "B",
        "Com o close-up entramos no detalhe invisível da pele e das coisas; com a câmera lenta vemos o tempo dilatar-se; a tecnologia amplia a percepção sensorial da humanidade moderna."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Como a prática fascista da 'Estetização da Política' opera sobre as massas trabalhadoras nas sociedades modernas?",
        "Garantindo a partilha equitativa dos lucros das empresas industriais entre operários fabris.",
        "Oferecendo às massas o espetáculo visual grandioso de comícios, cultos ao líder e desfiles marciais sem alterar a exploração de classe.",
        "Incentivando a leitura autônoma de tratados filosóficos em centros culturais de bairros periféricos.",
        "Reduzindo as jornadas de trabalho diárias para permitir visitas gratuitas a bibliotecas comunitárias.",
        "Proibindo o uso de uniformes padronizados em eventos comemorativos oficiais de órgãos do Estado.",
        "B",
        "O fascismo não dá comida, terra nem salários dignos; ele oferece tochas, bandeiras e um chefe gritando no palanque; desvia o povo da luta real por direitos dando em troca o show de um espetáculo estético."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Qual cineasta alemã produziu para o regime nazista a obra cinematográfica O Triunfo da Vontade, exemplo clássico da estetização da política?",
        "A escritora modernista que traduziu os ensaios poéticos de Charles Baudelaire.",
        "A diretora e fotógrafa Leni Riefenstahl com seus documentários grandiosos sobre comícios em Nuremberg.",
        "A ensaísta e dramaturga que colaborou nas encenações do teatro épico de Bertolt Brecht.",
        "A montadora de películas cinematográficas da vanguarda soviética de Serguei Eisenstein.",
        "A pesquisadora de teoria crítica orientada pelas teses filosóficas de Theodor Adorno.",
        "B",
        "Leni Riefenstahl colocou câmeras em guindastes e trilhos para filmar milhares de homens marchando como engrenagens de ferro; o cinema virou ferramenta pura para transformar a tirania em espetáculo."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "Como o poeta futurista Filippo Tommaso Marinetti exaltava a barbárie bélica sob o prisma da estetização fascista?",
        "Exigindo a assinatura compulsória de acordos diplomáticos de paz permanente entre todas as nações.",
        "Proclamando que a guerra é bela porque cria a metalização do corpo humano e realiza a sinfonia dos canhões e do fogo.",
        "Defendendo a substituição de armas de fogo por instrumentos musicais de madeira em celebrações cívicas.",
        "Propondo a doação de tanques de combate blindados para a agricultura familiar de cultivo de trigo.",
        "Criticando a exibição de paradas militares em avenidas principais de capitais metropolitanas europeias.",
        "B",
        "O futurismo fascista levou o absurdo ao ápice: achava bombas e aviões em chamas obras de arte límpidas; fez da própria carnificina humana um show pirotécnico para satisfazer a vaidade dos tiranos."
    ))

    questoes_brutas.append((
        16, "EM13CHS302", "basico",
        "Qual é a resposta necessária apresentada por Walter Benjamin para combater a estetização fascista da política?",
        "O confinamento voluntário de todos os artistas em ateliês isolados no topo de cordilheiras montanhosas.",
        "A Politização da Arte, transformando os meios técnicos em instrumentos conscientes de esclarecimento e libertação popular.",
        "A queima de todos os aparelhos de projeção cinematográfica em fogueiras públicas comemorativas.",
        "A exigência de que os museus fechem suas portas durante a realização de pleitos eleitorais municipais.",
        "O restabelecimento obrigatório de guildas medievais de pintores mantidas por doações paroquiais.",
        "B",
        "Contra a mentira do espetáculo que anestesia, a resposta é a politização da arte: colocar o cinema, o rádio e os livros a serviço da verdade, da denúncia da opressão e da luta da classe trabalhadora."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Como a transformação contemporânea do quadro da Mona Lisa em memes de redes digitais exemplifica as teses de Benjamin?",
        "Provando que a conservação física de telas a óleo depende da aplicação de vernizes de fabricação artesanal.",
        "Evidenciando o esvaziamento total da aura aristocrática sagrada através da apropriação irreverente e cotidiana pelas massas conectadas.",
        "Demonstrando que os museus europeus pretendem transferir suas coleções de arte para plataformas de leilões mercantis.",
        "Exigindo que os visitantes de exposições públicas assinem termos de compromisso de silêncio absoluto nas salas.",
        "Comprovando que a pintura renascentista utilizava pigmentos minerais importados de colônias ultramarinas.",
        "B",
        "A Mona Lisa saiu do altar inalcançável do Louvre e foi parar na caneca de café, na camiseta e no meme engraçado do WhatsApp; a aura do distanciamento sagrado desabou na cultura popular moderna."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "Qual é o equívoco primário de quem supõe que Walter Benjamin era um filósofo conservador que lamentava a perda da aura?",
        "Ignorar que Benjamin celebrava o declínio da aura como uma emancipação que liberta a arte da servidão ao ritual sagrado.",
        "Acreditar que o pensador berlinense defendia a substituição da fotografia por tapeçarias bordadas à mão.",
        "Supor que os ensaios de Benjamin foram escritos para orientar diretores de museus arqueológicos imperiais.",
        "Imaginar que o conceito de aura foi copiado de manuais de navegação astronômica utilizados por corsários.",
        "Afirmar que a Escola de Frankfurt foi fundada para promover o consumo mercantil de televisores domésticos.",
        "A",
        "Benjamin não era um saudosista burguês chorando pelo passado: ele via com alegria a quebra da aura porque ela destruía a exclusividade dos ricos e abria caminho para a democratização real da cultura."
    ))

    questoes_brutas.append((
        19, "EM13CHS301", "basico",
        "Como Walter Benjamin define a fabricação da 'Falsa Aura' artificiosa promovida pela indústria do cinema de Hollywood?",
        "Uma técnica de restauração de películas antigas através de lavagens químicas com solventes neutros.",
        "O culto publicitário às celebridades (Star System) que compensa a ausência de aura com glamour e fetichismo mercantil.",
        "Um sistema de iluminação de cenários teatrais baseado no uso exclusivo de lâmpadas incandescentes de tungstênio.",
        "A distribuição de autógrafos colecionáveis em portas de salas de cinema para financiar caridades comunitárias.",
        "A exigência de que os figurinos de atores sejam costurados com tecidos de seda importados de cidades asiáticas.",
        "B",
        "Como o filme não tem original com aura autêntica, Hollywood inventa uma aura de mentira: fofocas de atores, tapete vermelho e glamour fabricado para vender ingressos e encantar consumidores ingênuos."
    ))

    questoes_brutas.append((
        20, "EM13CHS302", "basico",
        "O que caracteriza a atitude do público de cinema definida por Benjamin como 'examinador em estado de distração' (Zerstreuung)?",
        "A incapacidade de compreender histórias complexas em virtude de preguiça intelectual ou sonolência constante.",
        "A recepção coletiva e crítica da obra através do hábito e do choque sensorial, sem veneração ajoelhada nem passividade beata.",
        "A prática de abandonar as salas de exibição antes da conclusão do primeiro ato da narrativa cinematográfica.",
        "A recusa sistemática de consumir produtos alimentícios ou bebidas durante a projeção de filmes dramáticos.",
        "A obrigatoriedade de preenchimento de cadernos de exercícios escolares ao término de cada sessão de cinema.",
        "B",
        "Distração aqui não é burrice: é o modo como o homem da metrópole aprende as coisas pelo costume e pelo reflexo rápido; no cinema, o público assiste junto, julga, come pipoca, ri e pensa criticamente sem reverência cega."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Em que medida a posição filosófica de Walter Benjamin difere do pessimismo cultural manifestado por Theodor W. Adorno sobre a cultura de massas?",
        "Benjamin enxergava a ambivalência dialética da técnica, descobrindo no cinema e na fotografia brechas de democratização e emancipação das massas que Adorno rejeitava como pura alienação mercantil.",
        "Benjamin defendia o fechamento definitivo de salas de cinema populares para preservar os lucros de ateliês de pintura a óleo.",
        "Adorno propunha a transmissão compulsória de óperas barrocas por meio de emissoras de rádio estatais prussianas.",
        "Benjamin e Adorno concordavam que as câmeras fotográficas deveriam ser destruídas por comissões de operários têxteis.",
        "Adorno considerava que as produções cinematográficas hollywoodianas eram os documentos mais revolucionários da humanidade.",
        "A",
        "Adorno era cético e via a indústria cultural como máquina de emburrecer; Benjamin tinha um olhar dialético: sabia do perigo fascista, mas viu que a reprodução tirava o monopólio da arte das mãos da elite."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Como a distinção entre 'Reprodução Manual' (xilogravura, cópia de pintor) e 'Reprodutibilidade Técnica' (fotografia, cinema) evidencia o salto histórico da era industrial?",
        "Demonstrando que a reprodução técnica independe da presença física do original e atinge uma ubiquidade espacial de difusão que a mão humana artesanal jamais poderia alcançar.",
        "Provando que as gravuras em blocos de madeira possuíam maior resistência geológica do que as películas de celulóide.",
        "Comprovando que as prensas tipográficas de Gutenberg eram movidas unicamente por energia hidrelétrica gerada em rios.",
        "Exigindo que os falsificadores de telas de arte devessem prestar exames práticos em academias militares de cavalaria.",
        "Afirmando que a pintura a óleo foi inventada no século XIX por engenheiros químicos da indústria automobilística.",
        "A",
        "O gravador manual copiava devagar e ficava preso à sua habilidade; a lente técnica capta o que o olho não vê e a impressora solta um milhão de cópias que viajam para o mundo todo num piscar de olhos."
    ))

    questoes_brutas.append((
        23, "EM13CHS301", "intermediario",
        "De que modo a experiência do 'aqui e agora' (hic et nunc) conferia à obra tradicional um estatuto de testemunho histórico irrepetível?",
        "Submetendo as avaliações estéticas a sorteios anuais realizados por corporações mercantis de pescado.",
        "Garantindo que a matéria física da obra testemunhasse as passagens de séculos, as alterações químicas de seus pigmentos e as lutas políticas em torno de sua posse.",
        "Obrigando os proprietários de castelos a contratarem escrivães públicos para registrar a temperatura diária dos salões.",
        "Impedindo que os afrescos religiosos fossem limpos com esponjas úmidas durante cerimônias de canonização de mártires.",
        "Determinando que as esculturas de bronze devessem ser refundidas a cada cinqüenta anos para evitar desgastes de ferrugem.",
        "B",
        "O quadro antigo viu reis caírem e sobreviveu a guerras; suas rachaduras e marcas do tempo são documentos materiais vivos da história da humanidade que nenhuma cópia de fábrica pode imitar."
    ))

    questoes_brutas.append((
        24, "EM13CHS302", "intermediario",
        "Como o 'Teatro Épico' de Bertolt Brecht dialoga com as teses de Walter Benjamin sobre a desconstrução da ilusão artística tradicional?",
        "Utilizando o Efeito de Distanciamento (Verfremdungseffekt) para interromper a identificação emocional cega da plateia, forçando-a a pensar criticamente sobre os conflitos sociais encenados.",
        "Exigindo que os atores declamassem todos os textos dramáticos em línguas estrangeiras desconhecidas do público operário.",
        "Proibindo o acendimento de refletores elétricos para que as peças fossem apresentadas em escuridão completa nas salas.",
        "Substituindo todos os atores profissionais por marionetes de madeira articuladas através de fios de seda vegetal.",
        "Determinando que as peças teatrais devessem ser encerradas com a leitura de balanços de companhias mercantis de ferro.",
        "A",
        "Brecht e Benjamin eram parceiros: Brecht quebrava a ilusão mágica no palco acendendo as luzes e falando com a plateia; assim como no cinema, o público não deve sonhar acordado, mas despertar para transformar a realidade."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Qual é a relação entre a 'Montagem Dialética' de Serguei Eisenstein em O Encouraçado Potemkin e o choque perceptivo teorizado por Benjamin?",
        "O cineasta soviético unia dois planos visuais contrastantes cuja colisão no corte gerava uma ideia revolucionária na mente do trabalhador, superando o entretenimento narrativo burguês.",
        "A montagem de Eisenstein consistia na filmagem contínua de paisagens florestais estáticas sem nenhum corte de cena.",
        "O filme sobre a revolta dos marinheiros foi financiado por companhias mercantis de navegação comercial no mar Cáspio.",
        "A técnica de edição de películas dependia da supervisão direta de tabelionatos públicos da marinha czarista russa.",
        "Os cortes cinematográficos eram realizados através de lâminas de bronze aquecidas em caldeiras de trens a vapor.",
        "A",
        "Eisenstein bate a imagem do canhão contra a imagem do olho ensanguentado na escadaria de Odessa: o corte gera choque e pensamento crítico na cabeça do espectador; a montagem é o motor da politização da arte."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "Por que as tecnologias contemporâneas de Inteligência Artificial generativa de imagens (Midjourney, DALL-E) aprofundam a crise da autenticidade descrita por Benjamin?",
        "Porque geram fotografias sintéticas hiper-realistas a partir de textos sem a existência de nenhum referente físico no mundo real, liquidando o testemunho empírico da imagem.",
        "Porque exigem o uso compulsório de telas de pintura de linho importadas de cidades litorâneas do Mediterrâneo.",
        "Porque os servidores de processamento algorítmico foram construídos exclusivamente no interior de cavernas paleolíticas.",
        "Porque as imagens computadorizadas dependem da aprovação prévia concedida por congregações paroquiais de monges.",
        "Porque os modelos generativos só conseguem reproduzir partituras musicais escritas para instrumentos de percussão.",
        "A",
        "Hoje uma IA gera a foto do Papa de jaqueta ou de um presidente preso que nunca existiram; o que Benjamin viu na fotografia mecânica chega ao ápice: a imagem descola-se de vez do original físico real."
    ))

    questoes_brutas.append((
        27, "EM13CHS301", "intermediario",
        "De que modo a propaganda política moderna nas campanhas eleitorais reproduz a lógica da 'Estetização da Política' analisada por Walter Benjamin?",
        "Substituindo debates profundos sobre reformas estruturais, tributação e desigualdade de classes por jingles emocionais, cenários virtuais e narrativas publicitárias sedutoras.",
        "Obrigando todos os candidatos a apresentarem comprovantes de quitação de tributos municipais em cartórios eleitorais.",
        "Exigindo que os programas partidários sejam lidos na íntegra por locutores oficiais em estações de trens urbanos.",
        "Proibindo o uso de cartazes coloridos e faixas de tecido durante períodos de convenções democráticas abertas.",
        "Determinando que os cidadãos aptos a votar compareçam às urnas trajando uniformes de corporações de pedreiros.",
        "A",
        "A eleição moderna gasta fortunas com marqueteiros que fabricam o político como sabão em pó: jingle bonito, lágrimas na tela e promessas vazias; mascara-se a exploração com um show de marketing eleitoral."
    ))

    questoes_brutas.append((
        28, "EM13CHS302", "intermediario",
        "Como a prática de filmar e fotografar telas famosas com celulares em museus reflete o paradoxo contemporâneo da aura na sociedade hiperconectada?",
        "O visitante estica o smartphone para capturar a cópia digital do quadro, priorizando o registro para redes sociais em detrimento da contemplação da presença original irrepetível.",
        "A presença de aparelhos de telecomunicações nas galerias provoca descargas elétricas que danificam molduras antigas de cedro.",
        "Os diretores de museus exigem que os turistas realizem pagamentos monetários adicionais por cada fotografia digital tirada.",
        "As lentes de telefones celulares conseguem regenerar os pigmentos de tintas a óleo desgastados pela oxidação atmosférica.",
        "Os visitantes de galerias públicas são obrigados a doar seus aparelhos eletrônicos ao acervo institucional ao término da visita.",
        "A",
        "Na sala da Mona Lisa, centenas de pessoas dão as costas para a tela para tirar uma selfie; a obsessão em registrar a cópia no feed do Instagram engoliu a experiência de estar ali presente de corpo e alma."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Qual é a conexão entre o conceito de 'Inconsciente Óptico' e a Psicanálise de Sigmund Freud destacada expressamente por Benjamin em seu texto?",
        "Assim como a Psicanálise revelou que lapsos verbais e sonhos desvelam desejos reprimidos, a câmera fotográfica e cinematográfica revela minúcias materiais ocultas ao olhar consciente da vigília.",
        "Benjamin defendia que os operadores de câmera cinematográfica devessem realizar sessões diárias de hipnose antes das filmagens.",
        "Freud propôs a substituição de consultas clínicas individuais por exibições públicas de filmes mudos em auditórios hospitalares.",
        "Os dois pensadores concordavam que as perturbações psicológicas decorriam da exposição prolongada a lâmpadas de magnésio.",
        "A teoria do inconsciente óptico foi formulada para justificar o uso de aparelhos de eletrochoque em sanatórios prussianos.",
        "A",
        "O paralelo é genial: Freud mostrou que o ato falho revela a verdade oculta da alma que a mente esconde; a lente cinematográfica em câmera lenta revela a verdade oculta do movimento que o olho nu não vê."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Por que as primeiras fotografias de ruas e praças vazias de Paris realizadas por Eugène Atget foram comparadas por Benjamin a 'cenas de crimes'?",
        "Porque o fotógrafo utilizava equipamentos apreendidos por delegacias de polícia em batidas noturnas no submundo parisiense.",
        "Porque ao retirar os pedestres e capturar os detalhes frios de portas, calçamentos e esquinas, Atget exigia do espectador um olhar investigativo de perito que busca vestígios e pistas históricas.",
        "Porque a prefeitura de Paris contratou o artista para catalogar edifícios condenados à demolição por infestação de pestes.",
        "Porque as imagens de Atget eram comercializadas exclusivamente com agentes de espionagem de frotas mercantes estrangeiras.",
        "Porque os primeiros fotógrafos urbanos eram obrigados a registrar acidentes provocados por carruagens puxadas a cavalos.",
        "B",
        "As fotos de Atget não têm pose de modelo nem halo de santo: a rua deserta parece o local onde um crime aconteceu; a foto passa a exigir que o espectador seja um investigador crítico que decifra a cidade."
    ))

    questoes_brutas.append((
        31, "EM13CHS301", "intermediario",
        "De que modo a emergência da fotografia libertou a Pintura clássica da obrigação mimética de imitar fielmente o mundo exterior sensível?",
        "Obrigando os mestres pintores a abandonarem suas paletas de cores para se dedicarem exclusivamente à fabricação de molduras.",
        "Permitindo que a arte pictórica abandonasse a tarefa documental de retratar a realidade física (assumida pela câmera) para explorar a abstração formal, as cores e a subjetividade pura.",
        "Provando que as academias de belas artes da Europa dependiam de doações concedidas por companhias mercantis marítimas.",
        "Exigindo que os artistas plásticos prestassem juramentos de lealdade perante comissões de generais de infantaria armada.",
        "Demonstrando que as tintas a óleo aplicadas sobre tecidos de linho eram mais baratas do que as películas de brometo de prata.",
        "B",
        "Quando a câmera tirou o retrato do rei com perfeição e sem cansaço, o pintor foi libertado: 'já que a máquina copia a cara das pessoas, eu posso pintar a luz impressionista, o cubismo e o abstrato!'; a pintura voou livre."
    ))

    questoes_brutas.append((
        32, "EM13CHS302", "intermediario",
        "Como a arquitetura moderna das grandes metrópoles habituou o ser humano a uma percepção estética baseada na distração e no hábito motor?",
        "O morador da cidade transita pelas ruas e edifícios absorvendo a forma dos espaços não pela contemplação beata, mas pelo uso cotidiano e pela locomoção natural.",
        "Os engenheiros municipais exigiram que os edifícios residenciais fossem construídos com paredes de mármore translúcido.",
        "Os prefeitos das capitais industriais determinaram o fechamento obrigatório de todas as calçadas para pedestres ao entardecer.",
        "A circulação de veículos automotores dependia de concessões temporárias expedidas por congregações religiosas paroquiais.",
        "Os habitantes de bairros urbanos eram obrigados a realizar visitas guiadas aos reservatórios de água potável da comarca.",
        "A",
        "Ninguém para numa esquina de São Paulo para ficar uma hora meditando sobre o desenho de um poste ou prédio: nós aprendemos a cidade andando, atravessando a rua e desviando de carros; é a percepção pelo hábito."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Por que, para Walter Benjamin, a introdução de 'Legendas Explicativas' em fotos jornalísticas marca a vitória definitiva do valor de exposição?",
        "Porque a legenda impede a deriva mística e contemplativa do olhar, ancorando a imagem em um sentido político e documental que convoca o leitor ao julgamento crítico do fato.",
        "Porque as impressoras industriais exigiam o preenchimento obrigatório de margens brancas com caracteres tipográficos de chumbo.",
        "Porque os jornais da época eram obrigados a publicar decretos governamentais em rodapés de ilustrações cívicas.",
        "Porque os editores de publicações periódicas precisavam cumprir normas ortográficas estabelecidas por academias de letras.",
        "Porque a ausência de textos explicativos provocava desentendimentos comerciais entre assinantes de folhas diárias.",
        "A",
        "A foto de uma criança com fome ou de uma fábrica em greve precisa de legenda: 'esta foto foi tirada na favela X no dia Y'; a legenda mata a divagação poética e aponta o dedo na ferida política da realidade."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "De que maneira a teoria benjaminiana antecipou os impactos culturais contemporâneos da cultura de 'Memes' e 'Remixes' na internet?",
        "Ao demonstrar que as massas não querem apenas receber passivamente a obra de arte original, mas recortá-la, manipulá-la e utilizá-la como ferramenta ativa de comunicação cotidiana.",
        "Ao defender que a circulação de imagens digitais deve ser submetida à fiscalização de tribunais de alfândegas portuárias.",
        "Ao propor que as plataformas virtuais de mensagens cobrem tarifas financeiras sobre o envio de figurinhas eletrônicas.",
        "Ao provar que o humor popular decorria unicamente da leitura de compêndios medievais de teologia dogmática escolástica.",
        "Ao exigir que os criadores de conteúdos de internet devessem possuir diplomas de graduação em artes visuais clássicas.",
        "A",
        "O meme de internet é o sonho profético de Benjamin: a imagem sagrada foi arrancada do museu, recortada no Photoshop do celular e usada pelo jovem da periferia para fazer piada sobre a vida; a massa virou produtora da cultura."
    ))

    questoes_brutas.append((
        35, "EM13CHS301", "intermediario",
        "Qual é o papel atribuído ao 'Coletivo de Espectadores' na sala de cinema em contraposição ao fruidor solitário de artes plásticas?",
        "O público de cinema constitui uma massa reunida que reage de modo sincronizado e coletivo aos estímulos da tela, potencializando o debate social e o julgamento comum das obras.",
        "A plateia reunida em auditórios fechados deve permanecer em silêncio absoluto sob pena de prisão por guardas municipais.",
        "Os espectadores de sessões noturnas eram selecionados através de sorteios realizados em fábricas têxteis da capital.",
        "A reunião coletiva nas salas de exibição era proibida por autoridades de saúde pública para evitar contágios de febre amarela.",
        "Os frequentadores de cinemas populares deviam comprovar o pagamento pontual de seus tributos prediais urbanos.",
        "A",
        "O burguês na galeria apreciava o quadro sozinho no seu egoísmo particular; na sala de cinema 500 pessoas tomam o mesmo susto, dão a mesma gargalhada e saem na rua conversando juntas sobre o que viram."
    ))

    questoes_brutas.append((
        36, "EM13CHS302", "intermediario",
        "Como a ascensão do 'Cinema Falado' na década de 1930 complicou o potencial universal do cinema mudo segundo Walter Benjamin?",
        "Restringindo a circulação internacional das películas através de barreiras linguísticas nacionais e acelerando a submissão dos estúdios aos interesses comerciais de grandes capitais.",
        "Obrigando os estúdios de gravação a utilizarem orquestras sinfônicas compostas exclusivamente por cem músicos diplomados.",
        "Impedindo que as salas de projeção utilizassem aparelhos amplificadores de som alimentados por energia elétrica.",
        "Exigindo que os diálogos dos filmes fossem traduzidos compulsoriamente para o dialeto dos pescadores do mar do Norte.",
        "Eliminando completamente o uso de roteiros literários na preparação de produções cinematográficas dramáticas.",
        "A",
        "O cinema mudo de Charlie Chaplin era universal: um operário em Tóquio, em Paris ou no Rio entendia tudo pela mímica; quando veio a fala em inglês, reergueram-se fronteiras nacionais e o controle dos grandes monopólios de estúdio."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Em que sentido o cinema permitiu ao trabalhador urbano alienado das fábricas 'reconquistar a representação do seu próprio mundo'?",
        "Mostrando nas telas os ambientes industriais, as metrópoles barulhentas, os cortiços e os conflitos que faziam parte da sua vida real, conferindo visibilidade poética e crítica à sua existência.",
        "Obrigando os operários a realizarem horas extras de trabalho voluntário em oficinas de montagem de projetores de cinema.",
        "Prometendo que os melhores funcionários das fábricas seriam escalados como protagonistas de romances hollywoodianos.",
        "Substituindo os maquinários de tecelagem mecânica por ferramentas manuais de marcenaria e carpintaria naval.",
        "Proibindo a filmagem de cenas cotidianas para focar exclusivamente em celebrações nupciais de famílias aristocráticas.",
        "A",
        "O operário vivia esmagado na engrenagem da fábrica; no filme de Chaplin em Tempos Modernos ele viu a fábrica na tela, riu de si mesmo e percebeu que a sua dor e a sua luta eram o centro da história moderna."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "Como a crise do jornalismo impresso e a circulação de notícias em redes digitais atualizam a perda da autoridade aurática da palavra escrita?",
        "A notícia deixou de ser o relato oficial incontestável chancelado por monopólios editoriais para se tornar um fluxo fragmentado e disputado por milhares de produtores de conteúdo nas redes.",
        "As redações de jornais diários passaram a utilizar prensas mecânicas movidas a óleo de baleia em porões escuros.",
        "Os leitores de notícias impressas foram obrigados a prestar depoimentos juramentados perante magistrados de cortes civis.",
        "A distribuição de periódicos foi proibida em estações ferroviárias para conter o desperdício de celulose vegetal.",
        "Os correspondentes de imprensa internacional passaram a ser nomeados diretamente por decretos de monarquias hereditárias.",
        "A",
        "Antigamente o jornal impresso tinha aura: 'saiu no jornal, é verdade sagrada!'; hoje qualquer pessoa com um celular posta a imagem do fato no Twitter; a autoridade centralizada da informação desabou em disputa permanente."
    ))

    questoes_brutas.append((
        39, "EM13CHS301", "intermediario",
        "De que modo a valorização benjaminiana da 'fragmentação e do detalhe' opõe-se aos sistemas filosóficos totalizantes tradicionais?",
        "Benjamin busca nas sobras, nos dejetos urbanos, nos rodapés e nas imagens passageiras os vestígios materiais da verdade histórica, desconfiando de narrativas grandiosas que celebram os vencedores.",
        "O filósofo defendia a queima de todos os livros de história que contivessem mais de duzentas páginas de extensão.",
        "Benjamin propunha que os estudos acadêmicos fossem realizados unicamente através da memorização de provérbios rurais.",
        "A filosofia alemã exigia a submissão de todas as teses teóricas a aprovações concedidas por generais de infantaria armada.",
        "Os tratados sobre a fragmentação foram elaborados por corporações mercantis de transporte fluvial de cargas sólidas.",
        "A",
        "Benjamin é o filósofo que cata os cacos na calçada: enquanto Hegel e os reis contam a história das grandes vitórias imperiais, Benjamin olha o sapato do operário, o cartaz rasgado e o close-up da dor do oprimido."
    ))

    questoes_brutas.append((
        40, "EM13CHS302", "intermediario",
        "Por que o ensaio sobre a reprodutibilidade técnica encerra-se com uma das advertências políticas mais urgentes do século XX?",
        "Porque previa que se as classes trabalhadoras não se apropriassem conscientemente das tecnologias visuais para politizar a arte, o fascismo usaria essas mesmas mídias para conduzir a humanidade ao holocausto da guerra total.",
        "Porque o autor alertava sobre os perigos da escassez de sais minerais de prata utilizados na revelação de chapas fotográficas.",
        "Porque o filósofo pretendia transferir todos os arquivos de cinema da Europa para bibliotecas públicas da cidade de Moscou.",
        "Porque a legislação alfandegária internacional ameaçava aplicar tarifas tributárias extorsivas sobre o comércio de filmes.",
        "Porque as companhias de eletricidade da Prússia planejavam racionar o fornecimento de energia a salas de espetáculos teatrais.",
        "A",
        "O final do ensaio é um grito profético: ou a classe trabalhadora acorda e usa a tecnologia para se libertar (politização da arte), ou os tiranos nazifascistas usarão a tecnologia para queimar o mundo no fogo da guerra (estetização da política)."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a dialética materialista da perda da 'Aura' em Walter Benjamin: de que maneira o esvaziamento do halo de autenticidade e a destruição da distância inalcançável da obra de arte abalam a autoridade da tradição aristocrática, inaugurando a possibilidade de fundação da prática artística sobre uma nova práxis política democrática?",
        "Provando que as galerias de arte da República de Weimar utilizavam livros fiscais autenticados por tabelionatos municipais.",
        "Evidenciando que a aura repousava na inserção da obra no ritual sagrado e na hierarquia social que reservava a experiência estética às elites privilegiadas; ao emancipar a obra de sua dependência cúltica e torná-la ubiquamente acessível às massas pela reprodução técnica, Benjamin demonstra que a arte deixa de se fundar no ritual místico para se fundar na práxis social e na consciência política emancipatória.",
        "Determinando que os ministérios de educação devam proibir a exibição de pinturas clássicas em livros didáticos escolares.",
        "Afirmando que a perda da aura decorreu unicamente da escassez de pigmentos minerais de chumbo na indústria de tintas europeia.",
        "Comprovando que os museus alemães devessem cobrar ingressos equivalentes ao preço de um saco de carvão mineral.",
        "B",
        "- **Etapa 1:** Identificar o fundamento aristocrático da aura: a aura não era apenas um efeito óptico bonito; ela mantinha a obra intocável no altar do padre ou no castelo do nobre, mantendo o povo na condição de servo reverente.\n- **Etapa 2:** Celebrar o salto emancipatório da reprodução técnica: ao multiplicar a obra aos milhões e colocá-la na mão do trabalhador, a arte perde o medo sagrado; ela deixa de ser milagre do além e vira ferramenta de debate político e libertação na Terra."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a polaridade teórica entre o 'Valor de Culto' (Kultwert) e o 'Valor de Exposição' (Ausstellungswert) na história da civilização ocidental: de que modo a transição quantitativa da circulação das imagens operou uma mutação qualitativa definitiva na própria natureza material e na função social da obra de arte?",
        "Mostrando que os templos da Antiguidade utilizavam sistemas de escoamento de águas fluviais construídos com manilhas de barro.",
        "Demonstrando que, ao passo que a obra tradicional confinada ao valor de culto exigia a invisibilidade quase mágica e o recolhimento em santuários para a contemplação piedosa de iniciados, a arte técnica da modernidade só adquire existência e sentido na medida em que é exposta e consumida publicamente; essa ampliação quantitativa da visibilidade transforma a arte de objeto de temor sagrado em mercadoria profana e arena viva de disputa ideológica entre as classes sociais.",
        "Determinando que os retratos pintados a óleo devam ser destruídos após o falecimento dos cidadãos retratados.",
        "Afirmando que o valor de exposição foi um conceito criado por companhias mercantis de navegação para atrair turistas a portos.",
        "Comprovando que a transição entre valores decorreu de tratados diplomáticos assinados entre cortes monárquicas no século XVII.",
        "B",
        "- **Etapa 1:** Rastrear a raiz do valor de culto: as primeiras obras de arte existiam mesmo que ninguém as visse; a estátua no fundo da pirâmide existia para a alma do faraó e a pintura na caverna existia para os espíritos da caça.\n- **Etapa 2:** Consagrar o triunfo do valor de exposição: no cinema e na foto, a obra que não é vista não existe; a mudança de escala transformou a arte: ela perdeu o manto da reza e virou alimento da opinião pública e da inteligência coletiva das massas."
    ))

    questoes_brutas.append((
        43, "EM13CHS301", "dificil",
        "Investigue o diagnóstico benjaminiano da 'Estetização da Política' pelo Fascismo nas páginas finais de seu ensaio: como a manipulação cênica dos rituais de massas e a exaltação da guerra imperialista operam a capitulação suprema da humanidade, fazendo-a vivenciar a própria aniquilação física como um espetáculo estético?",
        "Comprovando que os comícios nazistas utilizavam lâmpadas elétricas alimentadas por geradores a diesel de baixa potência.",
        "Demonstrando que o fascismo mobiliza os recursos mais avançados da tecnologia de massas (cinema, rádio, iluminação monumental) para oferecer às multidões proletárias uma ilusão estética de unidade e grandiosidade nacional sem expropriar os grandes capitalistas nem alterar as relações de produção opressivas; essa mistificação culmina na apoteose da guerra, na qual a tecnologia mecânica destrói o próprio corpo humano sob o aplauso alienado de espectadores esteticamente fascinados.",
        "Determinando que os festivais cinematográficos europeus fossem suspensos durante a vigência de eleições proporcionais municipais.",
        "Afirmando que a crítica à estetização fascista foi extraída de regulamentos disciplinares militares da infantaria britânica.",
        "Provando que o culto ao líder decorria exclusivamente da ausência de jornais diários em cidades do interior da Baviera.",
        "B",
        "- **Etapa 1:** Desmascarar o truque fascista das massas: o fascismo dá bandeira, desfile e tochas na noite; ele dá a sensação de poder para quem ganha salário de fome, mantendo intactos os lucros dos barões do aço e da indústria armamentista.\n- **Etapa 2:** Denunciar o suicídio estético da guerra: ao transformar a marcha para a morte em filme heroico e os canhões em música sublime, o fascismo anestesiou o ser humano; a humanidade sentou na cadeira para aplaudir sua própria destruição na guerra."
    ))

    questoes_brutas.append((
        44, "EM13CHS302", "dificil",
        "Analise a resposta formulada por Walter Benjamin sintetizada na máxima 'A essas tentativas do fascismo de estetizar a política, as forças revolucionárias respondem com a Politização da Arte': de que maneira autores como Bertolt Brecht e Serguei Eisenstein concretizaram essa diretriz no teatro e no cinema contemporâneo?",
        "Mostrando que os dramaturgos alemães utilizavam figurinos costurados com tecidos de algodão fornecidos por cooperativas rurais.",
        "Evidenciando que a politização da arte recusa tanto o esteticismo elitista da 'arte pela arte' quanto a propaganda alienante do espetáculo; através de inovações formais rigorosas como a montagem dialética de choques conceituais (Eisenstein) e o efeito de distanciamento épico que impede a catarse passiva (Brecht), os artistas revolucionários transformaram os meios audiovisuais em laboratórios de desmontagem das ideologias da classe dominante e em alavancas de tomada de consciência histórica dos trabalhadores.",
        "Determinando que os cinemas operários fossem obrigados a cobrar ingressos equivalentes a dez gramas de sal marinho refinado.",
        "Afirmando que o cinema soviético dependia de câmeras mecânicas doadas por instituições financeiras de Nova York.",
        "Comprovando que a politização estética decorreu de decretos régios expedidos por cortes dinásticas da Escandinávia.",
        "B",
        "- **Etapa 1:** Recusar a 'arte decorativa desengajada': a burguesia dizia que arte não deve se meter em política para mantê-la como passatempo fútil dos ricos; Benjamin responde que em tempos de barbárie a neutralidade é cumplicidade.\n- **Etapa 2:** Armar a arte com a razão crítica: Brecht no teatro e Eisenstein nas telas pegaram a técnica moderna e disseram 'vamos usá-la para abrir os olhos do povo!'; a arte politizada desmonta as mentiras da opressão e acende a centelha da revolução."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Examine a analogia cognitiva e metodológica traçada por Walter Benjamin entre a 'Psicanálise Freudiana' e as descobertas proporcionadas pela tecnologia cinematográfica: por que a formulação do conceito de 'Inconsciente Óptico' representa uma revolução na teoria do conhecimento e na sensibilidade sensorial moderna?",
        "Provando que as clínicas psicanalíticas de Viena mantinham convênios com produtoras cinematográficas de filmes científicos.",
        "Demonstrando que, assim como Freud demonstrou que os detalhes aparentemente insignificantes da fala (lapsos, atos falhos) e dos sonhos revelam as estruturas ocultas do inconsciente pulsional reprimido, o cinema, através da desaceleração temporal da câmera lenta e da hipervisibilidade microscópica do close-up, revela dimensões físicas, dinâmicas e texturas da matéria que habitualmente passam despercebidas ao olhar adestrado da vigília, dilatando a consciência humana sobre o mundo material.",
        "Determinando que as sessões de análise psicanalítica devam ser acompanhadas por projeções de lanternas mágicas.",
        "Afirmando que a descoberta do inconsciente óptico decorreu de investigações sobre a fadiga visual de maquinistas de trens.",
        "Comprovando que a teoria do cinema foi redigida para subsidiar a regulamentação do trabalho noturno em indústrias químicas.",
        "B",
        "- **Etapa 1:** Reconhecer a cegueira do olhar comum: no dia a dia nosso olho vê por cima, no piloto automático; achamos que vemos tudo, mas não enxergamos a gota d'água caindo nem o tremor no canto do olho de quem sofre.\n- **Etapa 2:** Descobrir o inconsciente óptico com a lente: a câmera é a psicanálise do visível; ela para o tempo, dá zoom no detalhe oculto e escancara o que a matéria escondia; o cinema ensina a humanidade a ver a realidade de verdade."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Investigue o debate histórico e teórico entre Walter Benjamin e Theodor W. Adorno acerca do potencial emancipatório da cultura técnica: por que a tese benjaminiana de que o público de cinema atua como um 'examinador distraído e progressista' foi duramente confrontada pela teoria adorniana da 'Indústria Cultural'?",
        "Comprovando que as cartas entre Adorno e Benjamin eram transportadas por carruagens postais de tração animal.",
        "Evidenciando que, enquanto Benjamin sustentava que a destruição da aura e a recepção em massa habituavam o público a decifrar a fragmentação metropolitana com distanciamento crítico desalienado, Adorno e Horkheimer alertavam que o cinema e os meios de comunicação tornaram-se engrenagens padronizadas do capitalismo monopolista, cujo único efeito prático é a atrofia da imaginação reflexiva, a passividade psicológica e a reprodução da ideologia do capital nas massas administradas.",
        "Determinando que as obras de crítica cultural devessem ser aprovadas previamente por conselhos de operários metalúrgicos.",
        "Afirmando que a controvérsia teórica foi motivada por disputas em torno da herança de acervos bibliográficos familiares.",
        "Provando que Adorno defendia a conversão compulsória de estúdios cinematográficos em fábricas de gramofones manuais.",
        "B",
        "- **Etapa 1:** Compreender a aposta esperançosa de Benjamin: Benjamin achava que as massas na sala de cinema, rindo juntas e absorvendo o choque das imagens, viravam juízes críticos que não engoliam mais a autoridade da elite.\n- **Etapa 2:** Pesar a advertência implacável de Adorno: Adorno retrucou que o cinema de Hollywood não emancipa ninguém; ele cria fórmulas enlatadas, vende pipoca e emburrece o trabalhador para ele continuar obediente na fábrica na segunda-feira."
    ))

    questoes_brutas.append((
        47, "EM13CHS301", "dificil",
        "Analise a desconstrução da 'Autenticidade' na era da Reprodutibilidade Técnica algorítmica e da Inteligência Artificial generativa: de que maneira o desaparecimento definitivo do 'original físico' em arquivos digitais em nuvem e a síntese computacional de imagens desafiam as fronteiras entre o Real e a Simulação?",
        "Provando que as redes de fibra óptica submarinas utilizam cabos de transmissão revestidos por lâminas de cobre puro.",
        "Demonstrando que, ao passo que a fotografia tradicional ainda guardava um vínculo químico e físico com a luz refletida por um objeto real existente perante a lente, as imagens sintéticas de inteligências generativas não possuem matriz empírica originária nem 'aqui e agora'; a reprodutibilidade atinge seu cume desmaterializado, no qual o conceito de autenticidade é pulverizado em favor de simulações digitais infinitamente manipuláveis, transformando a verdade em arena de guerra cognitiva.",
        "Determinando que os arquivos digitais devessem ser impressos em papéis especiais e arquivados em caixas de chumbo seladas.",
        "Afirmando que os algoritmos de geração de imagens foram programados com base em teoremas geométricos da Babilônia antiga.",
        "Comprovando que a validação de imagens virtuais depende de certidões expedidas por comissões de meteorologia espacial.",
        "B",
        "- **Etapa 1:** Lembrar do fio que ligava a foto ao real: na foto analógica, a luz do sol batia no rosto da pessoa e queimava o sal de prata no filme; havia um elo físico verdadeiro com a matéria do mundo.\n- **Etapa 2:** Naufragar no abismo da IA generativa de hoje: na IA não há câmera, não há pessoa e não há luz real; há matrizes de números que calculam o que parece real; a cópia engoliu o original e a autenticidade virou pura poeira no ar."
    ))

    questoes_brutas.append((
        48, "EM13CHS302", "dificil",
        "Examine a crítica de Walter Benjamin ao 'Culto das Estrelas de Cinema' (o Star System de Hollywood): de que maneira a indústria cultural capitalista forja uma 'falsa aura' artificial e mercantil para compensar o esvaziamento da autenticidade da película técnica?",
        "Comprovando que as estrelas do cinema clássico de Hollywood recebiam seus pagamentos em moedas de ouro cunhadas na Califórnia.",
        "Demonstrando que, ciente de que a película cinematográfica reproduzível em milhares de cópias não possui o halo único da presença física irrepetível do ator no palco teatral, a indústria do entretenimento constrói meticulosamente o mito da celebridade fora das telas; através de campanhas publicitárias, festas suntuosas e exploração da intimidade particular, a estrela é fetichizada como um semideus intocável para vender bilheterias e apaziguar a alienação dos espectadores.",
        "Determinando que os atores de estúdios devam assinar termos de compromisso de residência permanente em bairros murados.",
        "Afirmando que a fabricação de celebridades cinematográficas foi uma estratégia militar criada para elevar o moral de marinheiros em guerras.",
        "Provando que o sistema de estrelas dependia de avaliações psicológicas conduzidas por oficiais reformados da infantaria naval.",
        "B",
        "- **Etapa 1:** Notar a frieza do celulóide cinematográfico: o ator de cinema não está ali na sua frente; o que está ali é uma sombra de luz passando num pano branco 24 vezes por segundo, copiada em mil cidades ao mesmo tempo.\n- **Etapa 2:** Revelar a fabricação da ilusão de Hollywood: para que o público sinta que está diante de deuses, o estúdio fabrica o glamour: fofocas nas revistas, mansões cinematográficas e escândalos; a falsa aura é a máscara que vende a mercadoria humana."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Investigue o papel da 'Desacralização da Arte' na emergência de novas práticas culturais participativas e na criação de conteúdos digitais periféricos: como o declínio da veneração reverente autorizou as classes populares a se apropriarem dos meios audiovisuais para expressar sua própria voz?",
        "Mostrando que as câmeras de vídeo portáteis utilizavam baterias recarregáveis montadas com compostos químicos de níquel.",
        "Evidenciando que, enquanto a arte aurática impunha a contemplação humilde e o silêncio respeitoso perante a genialidade sagrada de mestres consagrados, a secularização técnica desmontou o pedestal elitista da cultura; as juventudes periféricas e as massas trabalhadoras deixaram de ser meros receptores passivos para se tornarem produtores diretos de suas próprias narrativas visuais através de smartphones, vídeos musicais e coletivos de audiovisual comunitário.",
        "Determinando que as produções cinematográficas independentes devessem ser censuradas por comissões de delegados civis.",
        "Afirmando que a democratização do audiovisual foi uma concessão concedida por fundações filantrópicas de empresas automobilísticas.",
        "Comprovando que as oficinas de vídeo comunitário dependiam de licenças ambientais emitidas por capitanias de portos fluviais.",
        "B",
        "- **Etapa 1:** Recordar o medo reverente no museu tradicional: a elite ensinava que arte é coisa de gênio iluminado e que o povo da favela só podia entrar de cabeça baixa para admirar o que não entende.\n- **Etapa 2:** Celebrar o microfone e a câmera na mão da quebrada: quando o celular virou câmera de cinema, o jovem da periferia começou a filmar a blitz policial, o baile funk e a sua poesia; a perda da aura sagrada abriu as portas da auto-expressão para o povo."
    ))

    questoes_brutas.append((
        50, "EM13CHS102", "dificil",
        "Analise a relação entre o conceito benjaminiano de 'Aura Natural' (a contemplação de uma cordilheira montanhosa ou de um ramo que projeta sua sombra sobre nós) e a 'Aura Histórica da Obra de Arte': por que a experiência aurática original depende profundamente e em sua essência da faculdade humana de atribuir às coisas a capacidade de nos 'retribuir o olhar'?",
        "Provando que as cordilheiras montanhosas da Europa central foram cartografadas por equipes de topógrafos militares prussianos.",
        "Demonstrando que, em seus ensaios complementares sobre Baudelaire, Benjamin esclarece que a experiência da aura consiste na expectativa poética de que o objeto contemplado seja dotado de uma alma viva capaz de olhar de volta para quem o observa; na sociedade metropolitana dominada pela técnica instrumental e pelo valor de troca, as coisas tornam-se mercadorias opacas e descartáveis que perderam a capacidade de devolver o olhar humano, desencantando o mundo.",
        "Determinando que as expedições botânicas devam recolher amostras vegetais unicamente durante noites de lua cheia.",
        "Afirmando que a contemplação da natureza foi uma prática inventada por corporações mercantis têxteis para incentivar passeios turísticos.",
        "Comprovando que a perda da capacidade de olhar decorreu do uso continuado de óculos com lentes corretivas de quartzo.",
        "B",
        "- **Etapa 1:** Sentir a alma mágica do olhar da natureza: quando você deita na grama numa tarde de verão e contempla uma montanha distante, parece que o universo está olhando de volta para você com ternura e mistério sagrado.\n- **Etapa 2:** Lamentar o olhar morto da mercadoria moderna: na cidade capitalista acelerada, olhamos para a vitrine e vemos coisas mortas com etiqueta de preço; a técnica sem poesia transformou o mundo num monte de objetos descartáveis que não conversam mais com o coração."
    ))

    questoes_brutas.append((
        51, "EM13CHS301", "dificil",
        "Examine o conceito de 'Aparato Técnico' no cinema e a perda do controle do ator sobre sua própria atuação: por que o ator cinematográfico é expropriado de sua corporeidade viva, diferentemente do ator de teatro clássico que se apresenta diante de uma plateia de carne e osso?",
        "Comprovando que os camarins de teatros europeus utilizavam espelhos de cristal bisotado importados de oficinas de Veneza.",
        "Demonstrando que, no tablado do teatro, o ator sustenta a presença viva e irrepetível de seu corpo e de sua voz modulada perante um público presente em tempo real; no cinema, o ator não atua para uma plateia, mas para um conjunto de aparelhos mecânicos (lentes, microfones, refletores) que fragmentam sua performance em tomadas desconexas, cabendo à montagem final do diretor a criação do personagem, privando o ator de sua aura performática imediata.",
        "Determinando que os atores de teatro clássico devessem pagar taxas sindicais maiores do que os intérpretes cinematográficos.",
        "Afirmando que a expropriação do ator foi uma tese copiada de manuais de estratégia militar sobre o adestramento de cavalos de combate.",
        "Provando que as companhias teatrais realizavam censuras prévias aos ensaios com o auxílio de fiscais do ministério da fazenda.",
        "B",
        "- **Etapa 1:** Celebrar o calor vivo do tablado de teatro: no teatro, o ator erra, sua, chora e sente a respiração da primeira fila; se ele fraquejar, a peça cai; há uma comunhão humana sagrada e irrepetível no palco.\n- **Etapa 2:** Revelar a frieza cirúrgica do set de filmagem: no cinema, o ator grava o final antes do começo, fala para uma lente de ferro e repete a cena dez vezes; quem monta a atuação é a tesoura do editor na sala de corte; o corpo do ator foi fatiado pela máquina."
    ))

    questoes_brutas.append((
        52, "EM13CHS302", "dificil",
        "Investigue o diálogo entre a 'Reprodutibilidade Técnica' benjaminiana e o conceito contemporâneo de 'Cultura do Cancelamento' e 'Tribunais das Redes Sociais': de que maneira a viralização instantânea de fragmentos descontextualizados de vídeos atualiza o choque perceptivo e a violência da exposição pública de massas?",
        "Provando que os servidores de bancos de dados modernos são refrigerados com sistemas de ar condicionado de alta potência.",
        "Evidenciando que, nas redes digitais, um recorte de vídeo de dez segundos é arrancado de sua temporalidade viva histórica (o seu aqui e agora concreto) e multiplicado em milhões de telas instantaneamente; submetido ao valor de exposição absoluto, o sujeito filmado é julgado pela coletividade de usuários em estado de choque e distração emocional contínua, reproduzindo uma dinâmica punitiva de massa desprovida da densidade meditativa da justiça reflexiva.",
        "Determinando que as postagens em redes sociais devessem conter aprovações prévias emitidas por conselhos tutelares municipais.",
        "Afirmando que as reações de indignação em redes virtuais foram programadas com base em tratados de retórica clássica romana.",
        "Comprovando que os linchamentos virtuais decorrem exclusivamente da utilização de conexões de internet sem fio em áreas públicas.",
        "B",
        "- **Etapa 1:** Arrancar o fato do seu 'aqui e agora': quando um vídeo de 5 segundos é cortado da vida de alguém e jogado na rede, ele perde todo o contexto humano real, as conversas anteriores e a história viva do momento.\n- **Etapa 2:** Acionar o choque do julgamento da multidão: milhões de pessoas assistem ao recorte em trânsito no ônibus, dão o clique de ódio e condenam o indivíduo sem pensar; é o valor de exposição levado ao paroxismo de uma arena de linchamento instantâneo."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Analise a articulação entre a teoria estética de Walter Benjamin e a sua concepção de 'Materialismo Histórico' nas Teses sobre o Conceito de História: por que a denúncia de que 'nunca houve um monumento da cultura que não fosse também um monumento da barbárie' ilumina sua recusa em venerar a aura dos tesouros das classes dominantes?",
        "Provando que os manuscritos históricos de arquivos públicos eram guardados em pastas confeccionadas com cartolinas coloridas.",
        "Demonstrando que Benjamin enxerga com clareza marxista que as catedrais resplandecentes, os palácios barrocos e os quadros clássicos cercados de aura foram construídos através do suor, da escravidão e da espoliação sangrenta de gerações incalculáveis de trabalhadores anônimos; venerar a aura dessas obras sem questionar o sangue que as ergueu significa celebrar o triunfo dos opressores que desfilam com o botim cultural da história.",
        "Determinando que os estudantes de história devam memorizar cronologias de reinados dinásticos europeus em ordem alfabética.",
        "Afirmando que a crítica aos monumentos culturais foi inspirada em tratados de engenharia civil de construções de represas fluviais.",
        "Comprovando que os tesouros artísticos eram utilizados exclusivamente como garantia para empréstimos bancários concedidos a navegadores.",
        "B",
        "- **Etapa 1:** Olhar o sangue por trás da beleza do monumento: as pirâmides egípcias e as igrejas douradas de Minas Gerais são deslumbrantes aos olhos; mas foram erguidas com o chicote estalando nas costas de milhares de escravizados.\n- **Etapa 2:** Quebrar a veneração cega aos vencedores: Benjamin lembra que a aura tradicional celebra o nobre e o bispo que pagaram a conta; o materialista histórico tem a coragem de lembrar dos que tombaram no chão; a beleza não pode apagar o crime da opressão."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Examine o conceito benjaminiano de 'Recepção Coletiva em Estado de Distração' aplicado ao consumo diário de plataformas digitais (como feeds do TikTok e vídeos curtos do YouTube): de que maneira essa modalidade de consumo perceptivo transita entre a potencia crítica do hábito motor e a anestesia alienante do algoritmo de dopamina?",
        "Mostrando que os chips de circuitos integrados utilizados em smartphones utilizam lâminas finas de silício purificado.",
        "Evidenciando que, enquanto Benjamin acreditava que o choque e a distração cinematográfica poderiam treinar o cidadão para agir criticamente na metrópole moderna, o capitalismo de dados hiper-otimizou esse fluxo contínuo de choques sensoriais em vídeos de poucos segundos desenhados especificamente para capturar a atenção reflexiva e mantê-la em um transe perpétuo de consumo passivo, invertendo o potencial emancipatório em adestramento mercadológico algorítmico.",
        "Determinando que as telas de aparelhos eletrônicos devam ser bloqueadas automaticamente durante períodos de orações noturnas.",
        "Afirmando que o vício em conteúdos curtos foi desenvolvido por companhias mercantis de café para aumentar a produtividade fabril.",
        "Comprovando que a velocidade das conexões digitais depende de autorizações prévias emitidas por comissões de disciplina militar.",
        "B",
        "- **Etapa 1:** Recordar a aposta de Benjamin no treinamento perceptivo: Benjamin achava que aprender a ver imagens rápidas sem se assustar ajudaria o operário a atravessar a cidade caótica e a pensar com agilidade mental.\n- **Etapa 2:** Denunciar o aprisionamento pelo TikTok contemporâneo: as grandes corporações pegaram o choque perceptivo e colocaram no feed infinito; a pessoa passa três horas rolando o dedo zumbi sem pensar em nada; a distração virou prisão de dopamina lucrativa."
    ))

    questoes_brutas.append((
        55, "EM13CHS301", "dificil",
        "Investigue o papel da Fotografia Documental e do Fotojornalismo na construção da 'Consciência Histórica e Política das Massas': por que imagens como a da menina vietnamita correndo nua queimada por napalm (Nick Ut) ou a do operário enfrentando tanques na Praça da Paz Celestial possuem força estética e política demolidora contra as narrativas oficiais dos Estados?",
        "Comprovando que os rolos de filmes fotográficos utilizados por correspondentes de guerra utilizavam estojos de folha-de-flandres.",
        "Demonstrando que, ao operar inteiramente no domínio do valor de exposição e do registro técnico cru da realidade material, a grande fotografia documental desmantela a estetização romântica da guerra promovida pelos governos militaristas; a imagem escancara a dor dos corpos inocentes e a violência estatal, funcionando como um tribunal visual incontestável que mobiliza a indignação moral e a oposição popular internacional contra os horrores da barbárie.",
        "Determinando que as fotografias de conflitos armados sejam arquivadas em cofres militares vedados a publicações jornalísticas.",
        "Afirmando que a credibilidade do fotojornalismo dependia de atestados de idoneidade moral emitidos por congregações consulares marítimas.",
        "Provando que as câmeras dos correspondentes eram inspecionadas semanalmente por comissões de saúde pública e higiene militar.",
        "B",
        "- **Etapa 1:** Desmontar os discursos oficiais dos governantes: generais e políticos sempre dizem na televisão que a guerra é limpa, heroica e para salvar a pátria; o discurso tenta anestesiar a consciência das pessoas.\n- **Etapa 2:** Sentir o soco no estômago da foto documental: quando a foto da menina queimada por napalm saiu na capa do jornal nos Estados Unidos, a mentira desmoronou; a imagem crua da dor humana politizou a juventude e forçou o fim da guerra."
    ))

    questoes_brutas.append((
        56, "EM13CHS302", "dificil",
        "Analise a relevância do estudo da obra de Walter Benjamin no Ensino Médio segundo as competências da BNCC (especificamente EM13CHS603 e EM13CHS102): de que maneira o domínio dos conceitos de aura, valor de exposição e estetização da política prepara os estudantes para exercer a cidadania crítica na era da desinformação e das fake news?",
        "Provando que os currículos de filosofia devem limitar-se à reprodução de cópias manuscritas de compêndios didáticos aprovados pelo governo.",
        "Evidenciando que a formação estética benjaminiana capacita o estudante a não ser um consumidor ingênuo de imagens e algoritmos; ensina a identificar como discursos de ódio e populismos autoritários utilizam recursos visuais sedutores para ocultar projetos de supressão de direitos, municiando a juventude de instrumentos reflexivos para analisar criticamente a mídia, desmascarar manipulações e participar ativamente da vida democrática com responsabilidade ética e social.",
        "Determinando que os estudantes devessem realizar avaliações pedagógicas unicamente através de questionários de múltipla escolha padronizados.",
        "Afirmando que a análise crítica de imagens digitais deve ser suspensa nas escolas públicas para reduzir custos com equipamentos de informática.",
        "Comprovando que a formação para o uso de tecnologias audiovisuais depende de laudos emitidos por comissões disciplinares militares.",
        "B",
        "- **Etapa 1:** Alertar sobre a manipulação da juventude conectada: os jovens são bombardeados o dia todo por vídeos montados, discursos fascistas maquiados de piada e mentiras criadas para manipular o voto e a opinião.\n- **Etapa 2:** Fortalecer a cidadania com Benjamin na BNCC: aprender Benjamin dá régua e compasso para a juventude; o aluno aprende a perguntar 'a serviço de quem está esta imagem? O que ela está escondendo?'; o jovem vira cidadão livre e pensante."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Examine o conceito de 'Magia versus Técnica' na gênese das artes visuais em Walter Benjamin: de que maneira o filósofo alemão traça o percurso histórico secularizador que vai do feiticeiro ancestral paleolítico que pinta a caverna ao cirurgião e ao cineasta moderno que opera tecnicamente a matéria?",
        "Mostrando que os curandeiros tribais utilizavam recipientes de cerâmica para misturar óleos vegetais curativos em rituais.",
        "Demonstrando que, enquanto o pintor tradicional assemelha-se ao mago ou feiticeiro que mantém uma distância sagrada entre si e o doente operando por imposição de mãos exteriores, o cineasta assemelha-se ao cirurgião que renuncia à mística da distância e penetra ativamente no interior do tecido da matéria com seus instrumentos cortantes (a lente e a montagem), compondo uma nova realidade a partir de múltiplos fragmentos mecânicos articulados.",
        "Determinando que os operadores de aparelhos cinematográficos devam realizar cursos preparatórios em hospitais veterinários públicos.",
        "Afirmando que a comparação entre magia e cirurgia foi copiada de regulamentos marítimos de navegação de frotas mercantes britânicas.",
        "Comprovando que a transição entre feiticeiros e cineastas dependia de autorizações concedidas por corporações paroquiais medievais.",
        "B",
        "- **Etapa 1:** Entender a metáfora do feiticeiro e do pintor: o feiticeiro reza de longe e o pintor fica no cavalete olhando a tela com reverência; eles não colocam as mãos dentro da carne do mundo, mantendo a distância mágica.\n- **Etapa 2:** Descobrir a audácia do cirurgião e do cineasta: o cirurgião corta a pele com o bisturi para consertar o órgão e o cineasta penetra com a lente até o fundo da matéria com a montagem; o cinema opera o mundo sem medo místico."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Analise a relação entre a 'Crítica da Mercantilização da Arte' em Benjamin e a transformação do patrimônio cultural e das cidades históricas (como Ouro Preto, Olinda ou Paraty) em atrações da Indústria do Turismo Global: como o turismo predatório de massas fabrica uma 'aura de consumo cenográfica' que esvazia a vida comunitária real dos moradores?",
        "Mostrando que os centros históricos brasileiros utilizam pedras de calçamento assentadas com areia e cal por escravizados no século XVIII.",
        "Demonstrando que o turismo globalizado transforma cidades vivas em museus a céu aberto higienizados e gentrificados; a antiga aura sagrada das igrejas e casarios é empacotada como mercadoria turística para consumo de visitantes rápidos que fotografam fachadas sem interagir com as dores e lutas da população local, transformando o patrimônio histórico em espetáculo decorativo vazio a serviço da acumulação do capital imobiliário.",
        "Determinando que os moradores de cidades históricas devam utilizar trajes de época durante o atendimento a turistas estrangeiros.",
        "Afirmando que a preservação do patrimônio arquitetônico foi criada por corporações mercantis de transporte naval para incentivar a venda de mapas.",
        "Comprovando que a atividade turística colonial depende de fiscalizações sanitárias semanais coordenadas por oficiais de cavalaria.",
        "B",
        "- **Etapa 1:** Descrever o casario colonial vivo da comunidade: a cidade histórica é onde as pessoas moram, rezam, fazem feira e vivem o seu cotidiano concreto de trabalho e convivência.\n- **Etapa 2:** Denunciar a gentrificação turística de consumo: o grande capital expulsa os moradores pobres para a periferia e transforma as casas em pousadas de luxo e lojas caras; a história vira cenário cenográfico fake para tirar fotos no Instagram."
    ))

    questoes_brutas.append((
        59, "EM13CHS301", "dificil",
        "Investigue a tese de Walter Benjamin de que 'a reprodutibilidade técnica emancipa a obra de arte de sua existência parasitária no ritual': de que modo essa libertação do jugo religioso e aristocrático reconfigurou os critérios de julgamento estético nas sociedades democráticas contemporâneas?",
        "Comprovando que os membros de júris de exposições de pintura utilizavam urnas de votação fabricadas em fundições de bronze.",
        "Demonstrando que, enquanto a arte confinada ao ritual exigia a aceitação passiva dos cânones sagrados impostos pela autoridade incontestável de sacerdotes e soberanos dinásticos, a emancipação técnica descentralizou o julgamento; em uma sociedade democrática secularizada, a qualidade da obra não é ditada por mandamentos divinos, mas pela sua capacidade viva de provocar reflexão, suscitar debates coletivos e enriquecer a sensibilidade humana comum.",
        "Determinando que os críticos de arte devam pagar tributos especiais aos tesouros municipais antes da publicação de resenhas.",
        "Afirmando que a libertação da arte decorreu de concessões temporárias expedidas por comissões de generais veteranos de guerras.",
        "Provando que a quebra dos cânones rituais foi formulada por companhias mercantis de navegação para facilitar a exportação de gravuras.",
        "B",
        "- **Etapa 1:** Recordar a prisão da arte no ritual parasitário: por séculos a arte foi escrava da igreja e da corte; se o bispo ou o rei dissessem que a pintura era boa e sagrada, todo mundo tinha que baixar a cabeça e rezar sem discutir.\n- **Etapa 2:** Celebrar a soberania do julgamento popular democrático: liberta da coleira do padre e do nobre, a arte passa a ser julgada pelo povo; o que importa agora não é se agrada ao trono, mas se emociona, questiona e faz a humanidade pensar."
    ))

    questoes_brutas.append((
        60, "EM13CHS302", "dificil",
        "Ao encerrarmos o Capítulo 28 com a estética da reprodutibilidade técnica em Walter Benjamin, analise como a transição para o Capítulo 29 desdobrará a dialética da cultura de massas, onde Theodor W. Adorno e Max Horkheimer denunciarão a transformação da cultura em 'Indústria Cultural' (Kulturindustrie) e a conversão de toda criação artística em mercadoria padronizada de alienação social:",
        "Provando que as investigações sociológicas da Escola de Frankfurt perderam utilidade teórica após a expansão do comércio de eletrodomésticos.",
        "Demonstrando que, após Benjamin identificar as potencialidades emancipatórias do cinema e da quebra da aura, Adorno e Horkheimer investigarão no Capítulo 29 o lado mais sombrio da técnica moderna: demonstrarão como o capitalismo tardio monopolizou o rádio, a televisão e o cinema para fabricar a 'indústria cultural', gerando padronização em série, pseudo-individualidade e conformismo político nas massas trabalhadoras.",
        "Determinando que os currículos de filosofia do Ensino Médio devam limitar-se ao estudo de manuais de contabilidade de fábricas de sabão.",
        "Afirmando que Adorno e Horkheimer rejeitaram os escritos de Benjamin por considerá-lo um autor de folhetins de entretenimento popular.",
        "Comprovando que a transição entre capítulos teóricos depende de autorizações prévias concedidas por tribunais alfandegários marítimos.",
        "B",
        "- **Etapa 1:** Sintetizar as luzes e brechas em Walter Benjamin no Cap 28: Benjamin nos mostrou que a técnica destrói a aura sagrada dos tiranos e abre caminhos revolucionários para a educação das massas e politização da arte.\n- **Etapa 2:** Abrir as portas com entusiasmo para Adorno e Horkheimer no Cap 29: fechamos o Cap 28 com chave de ouro e entramos no clássico Dialética do Esclarecimento; veremos como o grande capital comprou os estúdios e criou a Indústria Cultural; a batalha pela libertação da mente continua!"
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
    linhas.append('capitulo: "Capítulo 28: A Reprodutibilidade Técnica em Walter Benjamin"')
    linhas.append('objeto_de_conhecimento: "A obra de arte na era de sua reprodutibilidade técnica, o conceito de aura e sua decadência, valor de culto versus valor de exposição, o cinema e o inconsciente óptico, e a polarização entre estetização da política e politização da arte"')
    linhas.append('ebook_fonte: "em-fil-c28-reprodutibilidade-tecnica-walter-benjamin.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS301"')
    linhas.append('  - "EM13CHS302"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: A Reprodutibilidade Técnica em Walter Benjamin\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-28-reprodutibilidade-tecnica-walter-benjamin -->"
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
    linhas.append("- BENJAMIN, Walter. A obra de arte na época de sua reprodutibilidade técnica. In: *Obras escolhidas I: magia e técnica, arte e política*. Tradução de Sérgio Paulo Rouanet. 7. ed. São Paulo: Brasiliense, 2012.")
    linhas.append("- GAGNEBIN, Jeanne Marie. *História e narração em Walter Benjamin*. 2. ed. São Paulo: Perspectiva, 2004.")
    linhas.append("- DUARTE, Rodrigo. *Teoria crítica da indústria cultural*. Belo Horizonte: Editora UFMG, 2003.")
    linhas.append("- ADORNO, Theodor W.; HORKHEIMER, Max. *Dialética do esclarecimento: fragmentos filosóficos*. Tradução de Guido Antonio de Almeida. Rio de Janeiro: Jorge Zahar, 1985.")
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

    destino_final = "content/medio/volume-unico/filosofia/eixo-4-estetica/cap-28-reprodutibilidade-tecnica-walter-benjamin/ebooks/em-fil-c28-reprodutibilidade-tecnica-walter-benjamin-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 28 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
