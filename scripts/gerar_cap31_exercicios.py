# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 31 de Filosofia EM:
Poéticas Afrodiaspóricas e Afrofuturismo
Objeto: cap-31-poeticas-afrodiasporicas-afrofuturismo
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
        "Quem é o autor da clássica obra de 1993 intitulada O Atlântico Negro: Modernidade e Dupla Consciência, que analisa as rotas marítimas e a cultura diaspórica?",
        [
            ("Paul Gilroy, sociólogo e crítico cultural britânico que formulou a tese do Atlântico Negro como contracultura transnacional.", True),
            ("Mark Dery, jornalista norte-americano que cunhou pela primeira vez a expressão linguística do afrofuturismo.", False),
            ("Sun Ra, pianista de jazz pioneiro da música cósmica e das túnicas intergalácticas no século vinte.", False),
            ("Ferréz, romancista e ensaísta brasileiro criador do manifesto da literatura marginal de periferia.", False),
            ("Ryan Coogler, cineasta contemporâneo responsável pela direção audiovisual do filme Pantera Negra.", False)
        ],
        "Paul Gilroy é o autor de O Atlântico Negro: Modernidade e Dupla Consciência (1993), obra na qual investiga a matriz marítima e transnacional da cultura negra."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Qual elemento foi escolhido por Paul Gilroy como o cronótopo ou símbolo central espacial e temporal supremo da modernidade atlântica?",
        [
            ("A ferrovia industrial britânica que conectava centros mineradores europeus.", False),
            ("O navio negreiro, que sintetizou a travessia violenta, o confinamento e a criação de novas identidades.", True),
            ("A fábrica têxtil urbana que padronizou a jornada do trabalho assalariado moderno.", False),
            ("O teatro de arena clássico que organizava o debate parlamentar das cortes.", False),
            ("O museu colonial etnográfico que guardava peças antigas da África ocidental.", False)
        ],
        "Gilroy elege o navio negreiro como o cronótopo da modernidade atlântica, marcando a violência do tráfico e o nascimento forçado de identidades transnacionais."
    ))

    questoes_brutas.append((
        3, "EM13CHS301", "basico",
        "Como se denominam os quatro elementos estéticos complementares que estruturam a cultura do Movimento Hip-Hop?",
        [
            ("O mestre de cerimônias, o baterista de jazz, o escultor clássico e o poeta lírico.", False),
            ("O trompetista de rua, o solista de blues, o dançarino de salão e o pintor de telas.", False),
            ("O DJ, o MC (mestre de cerimônias), o breakdance (B-Boy/B-Girl) e o grafite.", True),
            ("O repentista, o cordelista, o sanfoneiro nordestino e o xilogravurista popular.", False),
            ("O griô tradicional, o guerreiro banto, o tecelão de kente e o fundidor de bronze.", False)
        ],
        "O Movimento Hip-Hop constitui-se a partir de quatro pilares estéticos fundamentais: o DJ, o MC, o breakdance e o grafite."
    ))

    questoes_brutas.append((
        4, "EM13CHS302", "basico",
        "Em que ano e em qual álbum antológico o grupo brasileiro Racionais MC's produziu a clássica faixa Diário de um Detento?",
        [
            ("No álbum Da Lama ao Caos, produzido e gravado no ano de 1994.", False),
            ("No álbum Raio X Brasil, gravado na capital de São Paulo em 1993.", False),
            ("No disco Cores e Valores, lançado nas plataformas no ano de 2014.", False),
            ("No álbum Sobrevivendo no Inferno, lançado oficialmente no ano de 1997.", True),
            ("No disco Rastros de Resistência, publicado em formato livre em 2002.", False)
        ],
        "A composição Diário de um Detento integra o histórico álbum Sobrevivendo no Inferno, lançado pelos Racionais MC's em 1997."
    ))

    questoes_brutas.append((
        5, "EM13CHS603", "basico",
        "Qual intelectual norte-americano formulou originalmente o conceito de dupla consciência na obra As Almas da Gente Negra em 1903?",
        [
            ("Samuel R. Delany, ao desenvolver romances de ficção especulativa no século vinte.", False),
            ("Marc Smith, ao inaugurar as batalhas de versos competitivos na cidade de Chicago.", False),
            ("Afrika Bambaataa, ao organizar as primeiras festas comunitárias no bairro do Bronx.", False),
            ("George Clinton, ao compor canções para o coletivo Parliament-Funkadelic.", False),
            ("W.E.B. Du Bois, sociólogo e pensador afro-americano em As Almas da Gente Negra.", True)
        ],
        "O conceito de dupla consciência foi formulado pelo pensador afro-americano W.E.B. Du Bois em 1903, em As Almas da Gente Negra."
    ))

    questoes_brutas.append((
        6, "EM13CHS606", "basico",
        "Em que década e ensaio o crítico cultural Mark Dery empregou pela primeira vez a denominação Afrofuturismo?",
        [
            ("Na década de 1990, no ensaio Black to the Future publicado no livro Flame Wars.", True),
            ("Na década de 1970, no manifesto de fundação do sarau de poesia da Cooperifa.", False),
            ("Nos anos 1960, na apresentação da orquestra de jazz The Arkestra em Chicago.", False),
            ("Na década de 1980, na criação do primeiro torneio de poesias orais nos Estados Unidos.", False),
            ("Nos anos 1950, na conferência de escritores e artistas negros reunida em Paris.", False)
        ],
        "Mark Dery cunhou o termo Afrofuturismo em 1993 no texto Black to the Future, que integrou a antologia Flame Wars."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "Qual ideograma tradicional africano, associado ao pássaro que voa para a frente olhando para trás, simboliza a temporalidade circular afrofuturista?",
        [
            ("O cetro imperial de Mali, que representava a soberania dos reis mandingas.", False),
            ("O símbolo de Sankofa, presente nos tecidos e tradições dos povos acãs e iorubás.", True),
            ("A máscara cerimonial de bronze forjada nas oficinas reais da Nigéria antiga.", False),
            ("A lança guerreira dos zulus, utilizada na defesa territorial contra invasões.", False),
            ("A balança de comércio saariana, empregada nas trocas mercantis de sal e ouro.", False)
        ],
        "Sankofa é o símbolo ancestral acã que expressa a necessidade de resgatar o passado para compreender o presente e construir o futuro."
    ))

    questoes_brutas.append((
        8, "EM13CHS102", "basico",
        "Quem é a escritora pioneira da ficção científica afrofuturista que conquistou os prêmios Hugo e Nebula com obras como Kindred e A Parábola do Semeador?",
        [
            ("Roberta Estrela D'Alva, dramaturga e poetisa fundadora das batalhas de slam no Brasil.", False),
            ("Lu Ain-Zaila, romancista fluminense autora dos livros Sankofia e In-Verdades.", False),
            ("Octavia Butler, aclamada autora norte-americana de Kindred e A Parábola do Semeador.", True),
            ("Érica Peçanha do Nascimento, socióloga brasileira que pesquisou as vozes marginais.", False),
            ("Alondra Nelson, cientista social que teorizou a relação entre cultura digital e negritude.", False)
        ],
        "Octavia Butler consolidou-se como a principal romancista da ficção científica afrofuturista mundial, premiada com os troféus Hugo e Nebula."
    ))

    questoes_brutas.append((
        9, "EM13CHS301", "basico",
        "Qual músico de jazz adotou uma estética espacial, afirmou ter vindo do planeta Saturno e liderou o grupo musical The Arkestra?",
        [
            ("DJ Kool Herc, técnico sonoro pioneiro nas festas musicais suburbanas de Nova York.", False),
            ("Mano Brown, letrista paulistano e articulador das narrativas poéticas da periferia.", False),
            ("George Clinton, líder das apresentações festivas do coletivo Parliament-Funkadelic.", False),
            ("Sun Ra, pianista e compositor norte-americano que dirigiu o grupo The Arkestra.", True),
            ("Afrika Bambaataa, ativista comunitário do hip-hop no cenário metropolitano do Bronx.", False)
        ],
        "Sun Ra (nascido Herman Poole Blount) celebrizou-se pela poética cósmica, afirmando sua origem simbólica no planeta Saturno à frente da orquestra The Arkestra."
    ))

    questoes_brutas.append((
        10, "EM13CHS302", "basico",
        "Como se caracterizam as regras centrais das batalhas de poesia falada denominadas slams, introduzidas pioneiramente no Brasil?",
        [
            ("Exibição de poemas clássicos de Camões com acompanhamento de orquestra barroca.", False),
            ("Declamação livre sem tempo fixo, com fantasias teatrais luxuosas e júri profissional.", False),
            ("Apresentação de textos dramáticos anônimos, com uso de cenários e efeitos digitais.", False),
            ("Leitura cantada de hinos oficiais da pátria, avaliada exclusivamente por docentes.", False),
            ("Poemas de autoria própria, até três minutos, sem figurino ou música, julgados pela plateia.", True)
        ],
        "Nos slams, o participante dispõe de até três minutos para declamar poema autoral, sem música nem figurino, avaliado por jurados da plateia."
    ))

    questoes_brutas.append((
        11, "EM13CHS603", "basico",
        "Qual universidade pública brasileira incluiu pioneiramente a obra Sobrevivendo no Inferno dos Racionais MC's em seu vestibular de 2018?",
        [
            ("A Universidade Estadual de Campinas (UNICAMP), consagrando o rap no cânone nacional.", True),
            ("A Universidade de Brasília, ao criar cotas experimentais de literatura moderna.", False),
            ("A Universidade Federal do Paraná, ao avaliar letras populares do movimento operário.", False),
            ("A Universidade Federal do Rio de Janeiro, no concurso vestibular de belas artes.", False),
            ("A Universidade de Coimbra, no convênio lusófono de poesias rimadas contemporâneas.", False)
        ],
        "A UNICAMP incluiu o álbum Sobrevivendo no Inferno dos Racionais MC's em sua lista de leituras obrigatórias no vestibular de 2018."
    ))

    questoes_brutas.append((
        12, "EM13CHS606", "basico",
        "Qual nação fictícia do universo cinematográfico de Pantera Negra representa uma sociedade africana tecnologicamente avançada que nunca foi colonizada?",
        [
            ("Carthago, antigo império fenício no litoral setentrional do continente.", False),
            ("Wakanda, rica em vibranium e governada por líderes e cientistas negras de destaque.", True),
            ("Songhai, lendário entreposto comercial estabelecido nas margens do Rio Níger.", False),
            ("Kush, reino núbio que estabeleceu dinastias faraônicas ao longo do vale fértil.", False),
            ("Zion, fortaleza subterrânea dos rebeldes humanos na narrativa cinematográfica.", False)
        ],
        "Wakanda é a nação imaginária que condensa o imaginário afrofuturista no cinema, exibindo alta tecnologia e soberania preservada da colonização."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Quem fundou em São Paulo a Zona Autônoma da Palavra (ZAP! Slam), deflagrando a difusão dos torneios de poesia falada no Brasil?",
        [
            ("Sérgio Vaz, criador e animador do sarau literário da Cooperifa na zona sul.", False),
            ("Ferréz, romancista periférico que publicou a história do livro Capão Pecado.", False),
            ("Roberta Estrela D'Alva, atriz e poeta que introduziu a modalidade no país em 2008.", True),
            ("Xênia França, musicista baiana que uniu beats contemporâneos ao canto tradicional.", False),
            ("Lu Ain-Zaila, escritora que estruturou narrativas especulativas afro-brasileiras.", False)
        ],
        "Roberta Estrela D'Alva fundou o ZAP! Slam em 2008, marcando o marco inicial das competições de poesia falada nas praças e palcos brasileiros."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Qual objeto estelar é estudado com precisão milenar pelo Povo Dogon no Mali, citado como evidência de conhecimento astronômico africano ancestral?",
        [
            ("A estrela polar do hemisfério setentrional utilizada pelos navegantes fenícios.", False),
            ("O cometa periódico que atravessa a atmosfera a cada período de três séculos.", False),
            ("A constelação zodiacal que orientava o calendário das colheitas de trigo no Nilo.", False),
            ("A estrela binária Sirius, cujas órbitas foram mapeadas sem uso de telescópios modernos.", True),
            ("O planeta Júpiter e o balé de luas galileanas observadas no renascimento europeu.", False)
        ],
        "A astronomia do Povo Dogon mapeou a órbita da estrela Sirius, servindo de exemplo afrofuturista de ciência e tecnologia ancestral africana."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "Identifique a função central do DJ no interior das manifestações do movimento Hip-Hop:",
        [
            ("Escrever panfletos políticos e organizar o sindicato de artistas plásticos da capital.", False),
            ("Cantar melodias líricas no microfone com arranjos vocais inspirados na ópera ocidental.", False),
            ("Dançar sobre o chão pavimentado realizando giros corporais acrobáticos em alta rotação.", False),
            ("Pintar os painéis murais da metrópole utilizando latas de tinta e bicos reguláveis.", False),
            ("Manipular discos de vinil, fitas e samplers para mixar bases sonoras e ritmos novos.", True)
        ],
        "O DJ opera as tecnologias sonoras, como toca-discos e samplers, manipulando bases e texturas rítmicas essenciais para as rimas do MC."
    ))

    questoes_brutas.append((
        16, "EM13CHS302", "basico",
        "No contexto da literatura marginal brasileira, qual definição expressa o sentido comunitário do Sarau da Cooperifa fundado por Sérgio Vaz?",
        [
            ("Um sarau comunitário que converteu um bar de periferia em polo de criação e poesia.", True),
            ("Uma gráfica comercial que monopolizou a distribuição de folhetos acadêmicos no centro.", False),
            ("Um auditório fechado reservado à premiação anual de intelectuais universitários renomados.", False),
            ("Um tribunal de censura poética organizado para fiscalizar o linguajar popular urbano.", False),
            ("Uma escola técnica de edição digital focada em publicações de autores europeus.", False)
        ],
        "O Sarau da Cooperifa, liderado por Sérgio Vaz na zona sul de São Paulo, transformou o espaço de um bar popular em centro de difusão literária periférica."
    ))

    questoes_brutas.append((
        17, "EM13CHS603", "basico",
        "Qual grupo musical norte-americano liderado por George Clinton encenava pousos de naves espaciais de mentira em seus shows ao vivo?",
        [
            ("The Wailers, banda jamaicana que internacionalizou o ritmo religioso do reggae.", False),
            ("Parliament-Funkadelic, criador do P-Funk que utilizava a nave The Mothership no palco.", True),
            ("Public Enemy, conjunto de rap engajado na agitação política dos bairros operários.", False),
            ("Grandmaster Flash, grupo pioneiro no uso de toca-discos elétricos nos anos setenta.", False),
            ("The Sugarhill Gang, primeira gravação comercial que alcançou as paradas de rádio.", False)
        ],
        "George Clinton e o coletivo Parliament-Funkadelic consagraram a estética espacial do P-Funk com a mítica nave The Mothership pousando em suas apresentações."
    ))

    questoes_brutas.append((
        18, "EM13CHS606", "basico",
        "Em qual cidade brasileira situava-se a estação de metrô São Bento, célebre ponto de encontro dos pioneiros do hip-hop nacional nos anos 1980?",
        [
            ("Na cidade do Rio de Janeiro, próxima aos estúdios de gravação do samba moderno.", False),
            ("Na cidade de Salvador, nos arredores das praças históricas do centro antigo baiano.", False),
            ("Na cidade de São Paulo, polo de confluência dos primeiros b-boys, DJs e MCs paulistanos.", True),
            ("Na cidade de Belo Horizonte, nas imediações do viaduto central da linha férrea.", False),
            ("Na cidade de Porto Alegre, junto aos cais portuários do lago metropolitano.", False)
        ],
        "A estação São Bento do metrô de São Paulo foi o ponto nevrálgico onde dançarinos de break, DJs e rimadores organizaram o movimento hip-hop no Brasil."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Qual episódio trágico de violência estatal ocorrido em 1992 no Brasil é narrado na faixa Diário de um Detento dos Racionais MC's?",
        [
            ("O incêndio acidental de galpões fabris no bairro da Mooca durante manifestações.", False),
            ("O conflito fundiário entre posseiros e mineradoras clandestinas no interior paraense.", False),
            ("O bombardeio aéreo naval que destruiu baterias costeiras no período da ditadura.", False),
            ("O massacre na Casa de Detenção do Carandiru que vitimou mais de uma centena de presos.", True),
            ("A rebelião de trabalhadores da construção civil nas obras da rodovia litorânea.", False)
        ],
        "Diário de um Detento retrata com minúcia o massacre do Carandiru em 1992, quando 111 pessoas detidas foram mortas pelas forças de segurança pública."
    ))

    questoes_brutas.append((
        20, "EM13CHS102", "basico",
        "Qual das seguintes práticas do público nos torneios de slam evita o abafamento da dicção e preserva a voz dos poetas?",
        [
            ("Acender tochas decorativas nas laterais das calçadas durante a contagem do cronômetro.", False),
            ("Bater palmas estrondosas e apitar de modo contínuo durante os versos dos competidores.", False),
            ("Gritar palavras de ordem partidárias no megafone antes da liberação do microfone.", False),
            ("Fazer silêncio absoluto sem qualquer manifestação de afeto ou aprovação do conteúdo.", False),
            ("Estalar os dedos em vez de palmas barulhentas para demonstrar sintonia com a declamação.", True)
        ],
        "Nos slams, o estalar de dedos tornou-se convenção do público para manifestar aplauso e entusiasmo sem prejudicar a audição das rimas do orador."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Por que Paul Gilroy considera o Atlântico Negro como uma contracultura transnacional da modernidade em vez de um nacionalismo cultural fechado?",
        [
            ("Porque mostra que a cultura negra floresceu no trânsito marítimo e desmascara o mito da liberdade do Iluminismo europeu.", True),
            ("Porque defende a pureza étnica intacta que recusa qualquer contato histórico com a cultura de outras sociedades.", False),
            ("Porque condiciona a produção artística diaspórica à validação prévia dos museus etnográficos das capitais coloniais.", False),
            ("Porque entende que os navios mercantis europeus transportavam civilização pacífica para os povos desprovidos de técnica.", False),
            ("Porque restringe a experiência humana dos negros ao isolamento rural sem diálogo com a economia e a política mundiais.", False)
        ],
        "A tese de Gilroy expõe que a diáspora africana articulou uma cultura transnacional e crítica que contesta a hipocrisia emancipatória do Iluminismo."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Na perspectiva de W.E.B. Du Bois e Paul Gilroy, em que consiste a experiência da dupla consciência na sensibilidade do sujeito negro na diáspora?",
        [
            ("Como certeza inabalável de que o Estado colonial tutela com justiça todos os seus cidadãos de forma igualitária.", False),
            ("Como a experiência dilacerante de habitar a identidade negra e a nacionalidade ocidental, sob o olhar do preconceito branco.", True),
            ("Como a anulação completa de qualquer memória ancestral em troca do acesso irrestrito aos cargos da burocracia estatal.", False),
            ("Como a crença de que as teorias científicas do século dezenove haviam comprovado a harmonia entre todas as etnias.", False),
            ("Como a celebração ingênua da modernidade industrial como um processo isento de violências e conflitos territoriais.", False)
        ],
        "A dupla consciência traduz a tensão de ser negro e simultaneamente cidadão ocidental, vendo a si próprio mediado pelo preconceito dominante."
    ))

    questoes_brutas.append((
        23, "EM13CHS301", "intermediario",
        "Segundo Paul Gilroy, que função desempenha a música no contexto em que a escrita colonial foi negada aos povos escravizados?",
        [
            ("Funcionar como entretenimento passivo destinado a acalmar os trabalhadores nos canaviais e minas.", False),
            ("Atuar como mecanismo exclusivo de propaganda política a favor das cortes régias do continente europeu.", False),
            ("Constituir a linguagem de comunicação de memórias, saberes éticos e anseios de liberdade coletiva.", True),
            ("Imitar estritamente as partituras da música sacra medieval produzidas nos mosteiros do norte.", False),
            ("Servir de mercadoria puramente comercial para enriquecimento dos traficantes de mão de obra.", False)
        ],
        "A música diaspórica tornou-se veículo de transmissão de saberes, testemunhos de dor e horizontes de emancipação diante do bloqueio da palavra escrita."
    ))

    questoes_brutas.append((
        24, "EM13CHS302", "intermediario",
        "Em que sentido as letras dos Racionais MC's em Sobrevivendo no Inferno operam como uma filosofia da sobrevivência para os jovens da periferia?",
        [
            ("Ao incentivarem a submissão aos mandos da ordem instituída e a aceitação resignada da pobreza.", False),
            ("Ao proporem a fuga da realidade urbana em direção a mundos imaginários desvinculados do cotidiano.", False),
            ("Ao reduzirem os dilemas morais da metrópole a uma disputa comercial por marcas e grifes internacionais.", False),
            ("Ao analisarem a violência policial e o racismo, formulando ética comunitária e consciência política autônoma.", True),
            ("Ao reproduzirem discursos acadêmicos herméticos sem diálogo com a experiência viva dos bairros periféricos.", False)
        ],
        "As narrativas dos Racionais MC's desmontam o mito da democracia racial e estabelecem uma reflexão ética de respeito e resistência comunitária."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "Nas composições dos Racionais MC's, de que forma a teologia periférica articula elementos bíblicos à resistência cotidiana das favelas?",
        [
            ("Defende que a prosperidade financeira imediata é a prova máxima de retidão moral dos moradores das quebradas.", False),
            ("Recusa qualquer menção a textos sagrados, adotando uma postura materialista mecanicista sobre a sociedade.", False),
            ("Prega a resignação silenciosa diante das injustiças, aguardando compensações passivas em outra vida.", False),
            ("Subordina as decisões da comunidade às determinações dogmáticas de bispos e teólogos tradicionais europeus.", False),
            ("Funde a fé cristã popular e símbolos de resistência ancestral na denúncia da injustiça e no cuidado entre irmãos.", True)
        ],
        "A lírica de Mano Brown cruza a Bíblia e o vocabulário das ruas em chave profética de denúncia da violência e solidariedade entre os oprimidos."
    ))

    questoes_brutas.append((
        26, "EM13CHS606", "intermediario",
        "Ao proclamar a força da favela, em que sentido a Literatura Marginal brasileira desafia as hierarquias tradicionais do sistema literário nacional?",
        [
            ("Proclamando que o morador da favela não demanda apenas bens básicos, mas produz e protagoniza alta literatura.", True),
            ("Exigindo que todos os livros de autores de periferia sejam revisados previamente pelos membros da Academia de Letras.", False),
            ("Limitando suas produções a cartilhas técnicas sobre saneamento básico e higiene nos loteamentos urbanos.", False),
            ("Defendendo a queima de todos os livros clássicos da tradição lusófona como forma única de expressão artística.", False),
            ("Afirmando que a verdadeira arte exige afastamento absoluto dos temas políticos e das dores da vida real.", False)
        ],
        "A literatura marginal desconstrói a exclusão cultural ao afirmar a favela como centro produtor de literatura crítica de alto valor estético."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "Em seu ensaio de 1993, que questionamento fundamental formula Mark Dery contra a tradição da ficção científica ocidental?",
        [
            ("Aponta que o gênero literário dava destaque excessivo a personagens de etnias minoritárias nas tramas.", False),
            ("Denuncia o apagamento do corpo negro nas projeções futuristas, apesar de a escravidão espelhar temas de abdução.", True),
            ("Afirma que as tecnologias descritas nos livros de ficção eram excessivamente realistas e pouco imaginativas.", False),
            ("Sustenta que as viagens espaciais deveriam ser tratadas exclusivamente em manuais militares governamentais.", False),
            ("Considera que a literatura especulativa não possuía nenhum valor poético para o debate sobre os rumos da civilização.", False)
        ],
        "Dery indagou por que narrativas de abdução e tecnologias futuras apagavam os povos negros, cujas histórias reais carregam traumas análogos aos contos de terror."
    ))

    questoes_brutas.append((
        28, "EM13CHS102", "intermediario",
        "Com os estudos de Alondra Nelson e Kodwo Eshun, de que maneira a definição conceitual do Afrofuturismo foi aprofundada?",
        [
            ("Reduziu o movimento a um modismo passageiro focado na venda de roupas prateadas para gravações de videoclipes.", False),
            ("Definiu o termo como um retrocesso conservador que rejeita todo o aparato técnico da ciência moderna.", False),
            ("Estruturou o afrofuturismo como estratégia política, artística e filosófica que entrelaça tecnologia e ancestralidade.", True),
            ("Determinou que apenas cientistas da computação e matemáticos poderiam emitir pareceres sobre ficção científica.", False),
            ("Concluiu que a cultura africana tradicional é incompatível com as inovações digitais e aeroespaciais do presente.", False)
        ],
        "Nelson e Eshun conceberam o afrofuturismo como projeto emancipatório amplo, conectando o saber ancestral africano às tecnologias contemporâneas."
    ))

    questoes_brutas.append((
        29, "EM13CHS301", "intermediario",
        "Ao valorizar saberes ancestrais, em que medida a filosofia afrofuturista desconstrói a tese colonial de que a ciência e a técnica seriam monopólios europeus?",
        [
            ("Admitindo que as ferramentas tecnológicas surgiram na Europa, mas pedindo doações para os centros de ensino periféricos.", False),
            ("Reconhecendo a primazia de metalurgias, geometrias fractais e astronomias avançadas criadas em civilizações africanas.", True),
            ("Propondo a proibição do uso de qualquer maquinário digital por parte de coletivos artísticos e culturais negros.", False),
            ("Negando que as leis da física e da matemática possam ser aplicadas aos problemas do cotidiano das comunidades.", False),
            ("Defendendo que a técnica moderna é um mal que deve ser completamente abolido para o retorno à vida primitiva.", False)
        ],
        "O afrofuturismo resgata a tecnologia como patrimônio ancestral negro, evidenciado na metalurgia do Benim, nos tecidos Adinkra e na astronomia Dogon."
    ))

    questoes_brutas.append((
        30, "EM13CHS302", "intermediario",
        "Identifique a relação estabelecida entre o conceito acã de Sankofa e a descolonização do tempo promovida pelos artistas afrofuturistas:",
        [
            ("A imposição de uma marcha histórica linear que apaga o passado em nome da modernização fabril acelerada.", False),
            ("A recusa em construir projetos futuros, optando por um saudosismo imobilista das eras que já terminaram.", False),
            ("A crença de que os eventos históricos acontecem ao acaso sem qualquer causalidade ética ou social identificável.", False),
            ("A adoção de um tempo circular no qual o avanço em direção ao porvir requer a recuperação crítica da raiz ancestral.", True),
            ("A suposição de que o tempo é uma ilusão dos sentidos que deve ser descartada nas deliberações científicas.", False)
        ],
        "Sankofa sintetiza o tempo espiralar e circular: avançar tecnologicamente rumo ao cosmos exige recuperar saberes mutilados pela colonização."
    ))

    questoes_brutas.append((
        31, "EM13CHS603", "intermediario",
        "Por que Kodwo Eshun aproxima a experiência dos africanos na travessia atlântica das histórias distópicas de ficção científica?",
        [
            ("Porque os navios de guerra coloniais possuíam motores nucleares semelhantes aos de naves intergalácticas.", False),
            ("Porque a abdução, a despersonalização e o transporte em porões metálicos constituíram um apocalipse real para o colonizado.", True),
            ("Porque os exploradores do comércio marítimo utilizavam capacetes espaciais para suportar as variações de pressão.", False),
            ("Porque as comunidades africanas confundiam os tecidos europeus com vestimentas de astronautas extraterrestres.", False),
            ("Porque os arquivos históricos do tráfico foram redigidos integralmente sob a forma de roteiros cinematográficos.", False)
        ],
        "Eshun nota que a escravidão foi um pesadelo de ficção científica em escala real: povos capturados por seres estranhos, despojados de língua e levados a terras distantes."
    ))

    questoes_brutas.append((
        32, "EM13CHS606", "intermediario",
        "Como a orquestra The Arkestra de Sun Ra articulava a ancestralidade egípcia com a ficção espacial no contexto do jazz?",
        [
            ("Negando o uso de instrumentos eletrônicos para imitar exclusivamente os cantos fúnebres dos faraós antigos.", False),
            ("Utilizando sintetizadores e figurinos cósmicos para propor a música como espaçonave de libertação espiritual negra.", True),
            ("Rejeitando as tradições afro-americanas em troca de uma cópia dos arranjos das sinfonias clássicas germânicas.", False),
            ("Limitando suas apresentações a feiras agropecuárias do interior com repertório baseado em marchas militares.", False),
            ("Condicionando a entrada em seus shows à filiação obrigatória em organizações astronômicas governamentais.", False)
        ],
        "Sun Ra cruzou o Egito ancestral com sintetizadores cósmicos, transformando a performance sonora em meio de transporte para utopias espaciais."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Em quais temas centrais concentram-se as narrativas literárias afrofuturistas de Octavia Butler em obras como A Parábola do Semeador?",
        [
            ("Guerras medievais travadas por cavaleiros feudais pela posse de terras santas no continente europeu.", False),
            ("Colapsos climáticos, crises profundas do capitalismo e protagonistas negras articulando sobrevivência e comunidade.", True),
            ("Crônicas biográficas de famílias aristocráticas parisienses durante a era da monarquia absolutista.", False),
            ("Descrições satíricas sobre as disputas burocráticas entre funcionários de agências espaciais governamentais.", False),
            ("Tratados puramente acadêmicos de física quântica sem personagens ou enredos de ficção dramática.", False)
        ],
        "Octavia Butler retrata sociedades distópicas assoladas pelo colapso ecológico, nas quais mulheres negras mobilizam saberes éticos para refundar a vida coletiva."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "De que maneira o filme Pantera Negra rompe com as representações consagradas da África no cinema comercial tradicional ocidental?",
        [
            ("Ao apresentar Wakanda como nação soberana e hipertecnológica protegida da pilhagem, com cientistas negras geniais.", True),
            ("Ao retratar os povos africanos como grupos dependentes de ajuda humanitária externa para resolver suas crises internas.", False),
            ("Ao mostrar cidades devastadas pela fome onde os protagonistas buscam imigrar para centros urbanos europeus.", False),
            ("Ao sugerir que o desenvolvimento técnico e científico só ocorre após a intervenção militar de potências estrangeiras.", False),
            ("Ao manter os cientistas e líderes políticos em segundo plano, enfatizando apenas elementos de selva inexplorada.", False)
        ],
        "O longa-metragem inova ao imaginar uma potência africana soberana e detentora do saber técnico mais refinado do globo, protagonizado por mulheres negras."
    ))

    questoes_brutas.append((
        35, "EM13CHS301", "intermediario",
        "Qual é o sentido filosófico das oficinas de robótica ancestral e criação de games realizadas em comunidades como a Maré e o Capão Redondo?",
        [
            ("Treinar mão de obra barata para a montagem de computadores descartáveis destinados ao mercado externo.", False),
            ("Substituir o ensino de história e geografia por manuais de reparo elétrico sem reflexão crítica.", False),
            ("Capacitar os jovens como autores de suas próprias narrativas digitais a partir de suas realidades e memórias.", True),
            ("Obrigar os estudantes a abandonarem as práticas de reciclagem para adquirir produtos importados de alto custo.", False),
            ("Restringir o acesso dos moradores a jogos digitais produzidos com temas da mitologia medieval europeia.", False)
        ],
        "A apropriação comunitária de tecnologias transforma jovens periféricos em produtores de cosmologias digitais emancipadas."
    ))

    questoes_brutas.append((
        36, "EM13CHS302", "intermediario",
        "Por que as batalhas de poesia dos slams são comparadas à ágora grega em termos de participação cívica e deliberação?",
        [
            ("Porque cobram ingressos caros e exigem diplomas universitários para quem deseja subir na tribuna de fala.", False),
            ("Porque acontecem em templos de mármore isolados do tráfego das ruas centrais das capitais metropolitanas.", False),
            ("Porque reservam o direito de discursar exclusivamente aos magistrados e homens proprietários de imóveis.", False),
            ("Porque recriam um espaço público aberto nas ruas onde vozes plurais debatem injustiças e avaliam discursos.", True),
            ("Porque impõem o silêncio da plateia perante a autoridade inquestionável dos dirigentes políticos locais.", False)
        ],
        "Os slams revitalizam a dimensão democrática da palavra pública nas praças, permitindo que juventudes marginalizadas manifestem seus dilemas sociais."
    ))

    questoes_brutas.append((
        37, "EM13CHS603", "intermediario",
        "Qual equívoco analítico é cometido ao reduzir o Afrofuturismo a uma mera tendência de moda ou fantasia espacial com estampas africanas?",
        [
            ("Ignorar que o afrofuturismo é uma reflexão política e existencial profunda sobre governança de dados e soberania.", True),
            ("Deixar de perceber que a moda europeia foi historicamente superior a todas as vestimentas rituais diaspóricas.", False),
            ("Supor que todo movimento estético precisa recusar o uso de figurinos e cores brilhantes em suas apresentações.", False),
            ("Afirmar que a ficção científica não possui nenhuma relação com o cinema e com as artes visuais contemporâneas.", False),
            ("Acreditar que os povos da diáspora não dominavam técnicas de tingimento têxtil e tecelagem manual.", False)
        ],
        "O afrofuturismo não é um capricho visual fugaz; é um campo de disputa filosófica e política sobre tecnologia, IA, meio ambiente e autonomia histórica."
    ))

    questoes_brutas.append((
        38, "EM13CHS606", "intermediario",
        "Por que sociólogos da cultura refutam a alegação conservadora de que o rap e as estéticas periféricas fariam apologia da marginalidade?",
        [
            ("Porque os músicos e poetas periféricos afirmam desconhecer a rotina violenta vivenciada nos bairros afastados.", False),
            ("Porque as letras do rap comprovam que o crime organizado é um fenômeno benéfico para a coesão das famílias.", False),
            ("Porque as estéticas periféricas não criam o conflito, mas documentam criticamente a violência já praticada pelo sistema.", True),
            ("Porque a poesia falada se limita a temas idílicos da natureza sem tocar em assuntos relativos à segurança pública.", False),
            ("Porque o Estado brasileiro já resolveu todas as desigualdades econômicas nas regiões metropolitanas do país.", False)
        ],
        "O rap funciona como testemunho e crônica sociológica das tensões reais, acusando a seletividade penal e o abandono imposto às periferias."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Como a teoria do Atlântico Negro de Paul Gilroy se posiciona diante de propostas pan-africanistas de retorno físico integral à África?",
        [
            ("Apoia a repatriação imediata de todos os descendentes de africanos para aldeias rurais pré-coloniais.", False),
            ("Critica o essencialismo nacionalista e valoriza a diáspora como identidade móvel, híbrida e transnacional.", True),
            ("Afirma que as populações negras devem adotar integralmente as tradições culturais das monarquias europeias.", False),
            ("Defende que a travessia atlântica não gerou nenhuma mudança cultural relevante para os povos escravizados.", False),
            ("Considera que a experiência marítima foi uma ilusão ideológica inventada por historiadores contemporâneos.", False)
        ],
        "Gilroy recusa o essencialismo de um regresso estático, celebrando a riqueza criativa e a modernidade múltipla forjada nas rotas da diáspora."
    ))

    questoes_brutas.append((
        40, "EM13CHS102", "intermediario",
        "Qual é o elo estabelecido pelos estudos culturais entre as batalhas de rima do hip-hop e a ancestralidade dos griôs da África Ocidental?",
        [
            ("A substituição da memória viva por bancos de dados corporativos controlados por cartórios coloniais.", False),
            ("A ideia de que a palavra oral é uma forma primitiva de pensamento que deve ser superada pelo código escrito.", False),
            ("A tradição oral como sofisticada tecnologia de preservação de memórias históricas e valores éticos comunitários.", True),
            ("A exigência de que todo poeta popular utilize instrumentos clássicos de corda fabricados no período renascentista.", False),
            ("A determinação legal de que os poemas cantados não podem abordar questões relativas à ancestralidade dos clãs.", False)
        ],
        "Tanto os griôs quanto os MCs praticam a oralidade como saber mnemônico e pedagógico de alto refinamento, transmitindo sabedoria pela palavra falada."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Como Paul Gilroy articula o navio negreiro como cronótopo à desconstrução da autoimagem emancipatória do Iluminismo europeu?",
        [
            ("O navio negreiro revela que o progresso capitalista e a racionalidade moderna foram alimentados pelo terror do tráfico transatlântico.", True),
            ("O cronótopo marítimo prova que a navegação mercantil britânica foi motivada por ideais fraternos de compartilhamento pacífico.", False),
            ("A travessia dos oceanos demonstra que o pensamento iluminista conseguiu erradicar a escravidão nas primeiras décadas do século dezoito.", False),
            ("O espaço do navio funcionou como uma escola liberal onde os cativos aprenderam as noções universais de direito de propriedade.", False),
            ("A rota transatlântica é interpretada como um detalhe acessório que em nada influenciou o acúmulo de capitais nos países imperiais.", False)
        ],
        "- **Etapa 1:** Gilroy adota a noção de cronótopo para apontar o navio negreiro como a condensação de tempo e espaço da modernidade. Enquanto a Europa celebrava o império da Razão e a emancipação humana, seus navios transportavam cativos sob violência sistemática.\n- **Etapa 2:** O navio negreiro desmascara a contradição estrutural do Iluminismo ocidental, provando que o tráfico e a exploração colonial foram os verdadeiros motores materiais da modernidade burguesa, tornando a alternativa A exata."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Ao examinar a dupla consciência de W.E.B. Du Bois, de que modo Gilroy a afasta de um vitimismo passivo para transformá-la em fonte estética revolucionária?",
        [
            ("Demonstrando que a sensação de fratura identitária levou as populações afro-americanas a abandonarem todas as manifestações musicais.", False),
            ("Mostrando que a condição de estar dentro e fora da civilização ocidental conferiu uma lucidez crítica expressa em músicas emancipatórias.", True),
            ("Sustentando que a dupla consciência é superada pela aceitação passiva dos padrões comportamentais das elites das metrópoles.", False),
            ("Argumentando que a convivência com duas culturas impede a formulação de qualquer pensamento filosófico original e consistente.", False),
            ("Provando que os sujeitos da diáspora só conseguem produzir arte quando recebem financiamento exclusivo das cortes reinantes.", False)
        ],
        "- **Etapa 1:** A dupla consciência descrita por Du Bois assinala a tensão de enxergar o próprio reflexo através do filtro racista da sociedade branca envolvente.\n- **Etapa 2:** Gilroy enfatiza que os povos negros transformaram essa cisão interna em contracultura: a lucidez de habitar as margens permitiu desmascarar os limites da modernidade e inventar linguagens artísticas inauditas como o blues, o jazz e o rap, confirmando a alternativa B."
    ))

    questoes_brutas.append((
        43, "EM13CHS301", "dificil",
        "No campo da Estética contemporânea, qual interpretação teórica explica o procedimento da amostragem (sampling) executado pelos DJs no Hip-Hop?",
        [
            ("Como um ato mecânico de plágio desprovido de engenho criativo, que desrespeita os princípios formais da composição clássica.", False),
            ("Como uma incapacidade dos produtores musicais periféricos de dominarem instrumentos harmônicos tradicionais das orquestras.", False),
            ("Como uma arqueologia sonora que recontextualiza fragmentos do passado musical negro para responder às urgências do presente.", True),
            ("Como um esforço publicitário voltado a promover vendas de discos antigos das grandes gravadoras industriais do norte.", False),
            ("Como uma recusa niilista em produzir qualquer tipo de melodia original, priorizando a repetição ensurdecedora de ruídos.", False)
        ],
        "- **Etapa 1:** O sampler opera o recorte, a sobreposição e a ressignificação de trechos gravados do passado musical da diáspora (soul, funk, jazz, samba).\n- **Etapa 2:** Filosoficamente, o DJ não comete cópia passiva; ele opera como historiador sônico, resgatando vozes ancestrais para intervir no tempo presente e construir uma textura polifônica de resistência, validando a alternativa C."
    ))

    questoes_brutas.append((
        44, "EM13CHS302", "dificil",
        "Por qual razão a canção Diário de um Detento dos Racionais MC's pode ser caracterizada como uma obra literária trágica de densidade filosófica?",
        [
            ("Por reproduzir com fidelidade relatórios burocráticos oficiais elaborados pelas diretorias penitenciárias do período republicano.", False),
            ("Por converter o massacre estatal em espetáculo burlesco isento de julgamentos morais sobre os agentes penitenciários envolvidos.", False),
            ("Por limitar seu enredo ao relato biográfico de guardas prisionais que tentavam manter a ordem contra insurreições armadas.", False),
            ("Por dar voz ao sujeito encarcerado, expondo a engrenagem letal da punição e questionando a retórica civilizatória da nação.", True),
            ("Por defender a punição sumária e a extinção de garantias fundamentais para indivíduos condenados criminalmente pela justiça.", False)
        ],
        "- **Etapa 1:** A letra elaborada por Mano Brown e Jocenir rompe com o discurso oficial das autoridades sobre o sistema carcerário brasileiro.\n- **Etapa 2:** Ao assumir a perspectiva da vítima no limiar do extermínio do Carandiru, a narrativa expõe a engrenagem seletiva e necropolítica do Estado brasileiro, elevando o relato a uma reflexão trágica sobre justiça, poder e dignidade humana, o que consagra a alternativa D."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Ao acolher Sobrevivendo no Inferno no vestibular de 2018, de que modo a UNICAMP confrontou as fronteiras históricas do cânone literário nacional?",
        [
            ("Acolhe a linguagem oral das periferias e o rap como alta reflexão poética, implodindo o elitismo racista que monopolizava a grande arte.", False),
            ("Determina que todas as obras literárias em prosa escrita sejam banidas dos currículos escolares em favor de composições rimadas.", False),
            ("Reduz os critérios de avaliação acadêmica a pesquisas de popularidade quantitativa veiculadas nas rádios comerciais.", False),
            ("Demonstra que a academia brasileira sempre acolheu os saberes das favelas desde a proclamação da república sem nenhum conflito.", False),
            ("Legitima formalmente a criação artística marginal no cânone institucional, afirmando a favela como centro produtor de pensamento crítico.", True)
        ],
        "- **Etapa 1:** O cânone literário brasileiro tradicional esteve ancorado no eurocentrismo e na supremacia do texto escrito cultivado pelas elites letradas.\n- **Etapa 2:** A decisão da UNICAMP não foi concessão condescendente; reconheceu a sofisticação métrica, a relevância sociológica e a densidade estética da obra dos Racionais MC's, rompendo com o bloqueio elitista do cânone oficial, legitimando a alternativa E."
    ))

    questoes_brutas.append((
        46, "EM13CHS606", "dificil",
        "Ao indagar por que tão poucos negros escreviam ficção científica, qual paralelo histórico crucial foi traçado pelo crítico Mark Dery?",
        [
            ("A semelhança radical entre os traumas reais da escravidão (abdução, corpos violentados e desterro) e as tramas clássicas de terror distópico.", True),
            ("A correspondência biológica entre seres alienígenas descritos em romances pulp e as etnias que habitavam o continente africano.", False),
            ("A falta crônica de imaginação nas narrativas da tradição oral banta e iorubá diante de fenômenos de ordem mecânica e física.", False),
            ("A recusa dos escritores afro-americanos em utilizarem computadores portáteis durante a elaboração de seus manuscritos literários.", False),
            ("A dependência financeira integral das comunidades negras em relação aos subsídios concedidos pelas editoras norte-americanas.", False)
        ],
        "- **Etapa 1:** Mark Dery identificou a contradição de a literatura de ficção científica ser branca, enquanto seus temas giravam em torno de invasões alienígenas e abduções violentas.\n- **Etapa 2:** Os afrodescendentes já haviam vivido o pesadelo distópico concreto na diáspora escravista, sendo arrancados de suas terras por estranhos para serem tratados como coisas mecânicas, o que valida a alternativa A."
    ))

    questoes_brutas.append((
        47, "EM13CHS101", "dificil",
        "Na história da ciência e da técnica, que efeito produz a valorização afrofuturista dos saberes do Povo Dogon e dos tecidos Kente?",
        [
            ("Mostra que as civilizações ocidentais inventaram a matemática sem qualquer inspiração ou contato com outros territórios.", False),
            ("Desmonta a tese colonial eurocêntrica ao provar que povos africanos desenvolveram geometrias fractais e astronomias refinadas.", True),
            ("Afirma que o conhecimento empírico tradicional deve ser rejeitado em favor dos métodos padronizados dos laboratórios fabris.", False),
            ("Restringe o valor da cultura africana às danças folclóricas rituais desvinculadas de qualquer rigor lógico ou técnico.", False),
            ("Propõe que a física moderna dispense o uso de aparelhos de medição em favor de leituras místicas de oráculos orais.", False)
        ],
        "- **Etapa 1:** O discurso colonialista sustentava que a África vivia em estado pré-lógico e natural, desprovida de pensamento técnico-científico.\n- **Etapa 2:** A valorização da astronomia Dogon e da geometria fractal nos tecidos africanos prova que as ciências exatas e a observação do cosmos foram cultivadas por civilizações africanas muito antes das academias europeias, assegurando a alternativa B."
    ))

    questoes_brutas.append((
        48, "EM13CHS102", "dificil",
        "De que modo a temporalidade circular de Sankofa desmonta o conceito ocidental burguês de progresso histórico?",
        [
            ("Prescrevendo a renúncia total à esperança em favor de um pessimismo determinista que impede qualquer projeto social.", False),
            ("Exigindo o isolamento geográfico das comunidades tradicionais para que não sejam contaminadas pelo ritmo fabril moderno.", False),
            ("Afirmando que o futuro não decorre do esquecimento do passado, mas exige a recuperação ativa das memórias e saberes ancestrais.", True),
            ("Sustentando que todas as gerações humanas cometem os mesmos erros sem nenhuma possibilidade de acúmulo de aprendizados.", False),
            ("Defendendo que a industrialização acelerada do século vinte realizou todas as promessas de igualdade sonhadas pelos povos.", False)
        ],
        "- **Etapa 1:** O modelo de progresso iluminista e capitalista pressupõe uma linha reta na qual o passado deve ser superado e descartado como atraso.\n- **Etapa 2:** Sankofa propõe o tempo espiralar: avançar rumo às fronteiras do futuro intergaláctico depende de voltar o olhar para trás e resgatar a ancestralidade esmagada, fazendo da memória motor de libertação, o que confirma a alternativa C."
    ))

    questoes_brutas.append((
        49, "EM13CHS301", "dificil",
        "Na imaginação do futuro espacial, de que maneira a tese afrofuturista da cura do trauma colonial ressignifica a presença do corpo negro?",
        [
            ("Afirma que os negros devem atuar como soldados subordinados nas frotas militares chefiadas por capitães estrangeiros.", False),
            ("Propõe que as tecnologias espaciais sejam reservadas exclusivamente para o transporte de minérios preciosos entre planetas.", False),
            ("Determina que o racismo é um traço insolúvel da psicologia dos seres que se repetirá invariavelmente em todas as galáxias.", False),
            ("Posiciona o negro como piloto de sua própria libertação cósmica, capaz de criar mundos onde o colonialismo foi extirpado.", True),
            ("Nega que a exploração do universo tenha qualquer relevância ética para a superação das desigualdades históricas da Terra.", False)
        ],
        "- **Etapa 1:** A ficção tradicional branca frequentemente excluía corpos não brancos de cidades futuristas ou os mantinha como subalternos.\n- **Etapa 2:** O afrofuturismo reivindica o protagonismo do negro no leme das naves e na vanguarda do cosmos; aquele que sobreviveu à catástrofe da escravidão é quem detém a resiliência para forjar utopias justas, confirmando a alternativa D."
    ))

    questoes_brutas.append((
        50, "EM13CHS302", "dificil",
        "Na análise de Kodwo Eshun em Mais Brilhante que o Sol, como a ficção sônica do jazz e da música eletrônica negra opera politicamente?",
        [
            ("Alienando as massas populares das lutas sindicais através de harmonias repetitivas desprovidas de sentido reflexivo.", False),
            ("Submetendo as composições dos cantores de rua à aprovação técnica de regentes formados nos conservatórios alemães.", False),
            ("Restringindo a criatividade musical negra aos modelos sonoros das igrejas reformadas do período barroco europeu.", False),
            ("Transformando a música em mercadoria barata para consumo rápido e passageiro nos balcões das grandes redes de lojas metropolitanas.", False),
            ("Funcionando como laboratório estético que desestabiliza a ordem colonial e programa novas frequências de liberdade humana.", True)
        ],
        "- **Etapa 1:** Eshun examina como músicos negros utilizaram sintetizadores, efeitos de estúdio e frequências baixas para reinventar a sensibilidade humana.\n- **Etapa 2:** A ficção sônica afrodiaspórica não visa à passividade; ela opera como tecnologia de descolonização psíquica, criando novos horizontes cognitivos e afetivos que desprogramam o racismo estrutural, consolidando a alternativa E."
    ))

    questoes_brutas.append((
        51, "EM13CHS603", "dificil",
        "Nos espetáculos do coletivo Parliament-Funkadelic, que significado assume a nave espacial cenográfica The Mothership criada por George Clinton?",
        [
            ("Materializar um ritual festivo de libertação mental coletiva, no qual o funk convida o povo negro a transcender a opressão terrestre.", True),
            ("Fazer propaganda governamental para o programa espacial da corrida armamentista durante as disputas da Guerra Fria.", False),
            ("Demonstrar aos espectadores que o acesso à tecnologia avançada era privilégio exclusivo das indústrias cinematográficas.", False),
            ("Simular um acidente militar para afugentar a polícia dos locais onde ocorriam os espetáculos musicais da juventude.", False),
            ("Vender ingressos com preços diferenciados para os admiradores de temas militares das capitais norte-americanas.", False)
        ],
        "- **Etapa 1:** George Clinton concebeu o P-Funk como uma força libertadora capaz de desarmar preconceitos e libertar a mente dos corpos oprimidos.\n- **Etapa 2:** A chegada visual da Mothership ao palco materializava a utopia de uma nave-mãe intergaláctica que resgatava a comunidade do pesadelo do preconceito cotidiano, reafirmando o direito cósmico à alegria e à soberania, o que comprova a alternativa A."
    ))

    questoes_brutas.append((
        52, "EM13CHS606", "dificil",
        "Como a personagem Lauren Olamina, criada por Octavia Butler em A Parábola do Semeador, articula a filosofia da mudança diante de distopias ecológicas?",
        [
            ("Apegando-se a dogmas religiosos conservadores do passado que recusam a realidade do aquecimento global contemporâneo.", False),
            ("Fundando a religião Semente da Terra, baseada no princípio de que Deus é a Mudança e que a humanidade deve se adaptar rumo às estrelas.", True),
            ("Aceitando passivamente a destruição de sua comunidade em troca de refúgio isolado nos castelos das corporações privadas.", False),
            ("Recusando qualquer diálogo com outras vítimas da crise, defendendo a sobrevivência egoísta do indivíduo armado.", False),
            ("Negando que a crise ecológica guarde qualquer relação com a ganância do modelo de exploração econômica vigente.", False)
        ],
        "- **Etapa 1:** Em A Parábola do Semeador, Butler antecipa crises climáticas severas e a fragmentação social sob o capitalismo predatório.\n- **Etapa 2:** A protagonista concebe a crença de que 'Deus é Mudança', ensinando que a resiliência adaptativa comunitária e a visão de longo prazo em direção ao espaço sideral constituem a única salvação para a espécie humana, confirmando a alternativa B."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Na arquitetura visual e política de Pantera Negra, como se manifesta a síntese afrofuturista entre ancestralidade e alta tecnologia?",
        [
            ("Mostrando que a riqueza científica da nação exigiu a destruição completa das florestas e a poluição das águas locais.", False),
            ("Retratando a liderança wakandiana como submissa aos acordos multilaterais controlados pelas potências do norte global.", False),
            ("Integrando naves de ponta, trajes em vibranium e cidades sustentáveis com rituais tradicionais, monarquia sagrada e conselhos de anciãos.", True),
            ("Propondo que os cidadãos abandonem suas vestimentas tradicionais para vestir apenas uniformes metálicos padronizados.", False),
            ("Afirmando que a ciência da computação wakandiana foi desenvolvida a partir de manuais doados por laboratórios europeus.", False)
        ],
        "- **Etapa 1:** A ficção colonial sempre opôs a tradição africana à técnica ocidental, rotulando o costume tribal como incompatível com a modernidade.\n- **Etapa 2:** Wakanda funde os dois polos em harmonia sublime: arranha-céus integrados à natureza, transporte magnético e o vibranium coexistem com a coroação sagrada e a veneração às deusas e divindades ancestrais, o que torna a alternativa C exata."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Ao confrontar o racismo algorítmico, de que modo as reflexões de Ruha Benjamin e Safiya Noble se vinculam à agenda emancipadora do Afrofuturismo?",
        [
            ("Ao alertarem que os algoritmos de inteligência artificial são neutros e resolvem automaticamente os preconceitos históricos.", False),
            ("Ao demonstrarem que o racismo algorítmico replica discriminações em bancos de dados, exigindo que o povo negro assuma o design tecnológico.", False),
            ("Ao proibirem que estudantes negros usem computadores para proteger suas mentes da influência da cibercultura contemporânea.", False),
            ("Ao desvelarem vieses racistas em sistemas digitais, convocando criadores negros a programarem ferramentas com princípios libertadores.", True),
            ("Ao sustentarem que as redes sociais são ambientes imunes a interesses financeiros e monopólios de grandes empresas de mídia.", False)
        ],
        "- **Etapa 1:** Pesquisadoras como Benjamin e Noble revelam que sistemas digitais automatizados e ferramentas de reconhecimento facial reproduzem vieses racistas.\n- **Etapa 2:** O afrofuturismo se articula diretamente a essa crítica, demandando que a comunidade negra não seja apenas consumidora dos softwares do Vale do Silício, mas arquiteta de seus próprios algoritmos e plataformas digitais justas, assegurando a alternativa D."
    ))

    questoes_brutas.append((
        55, "EM13CHS301", "dificil",
        "Por que as batalhas de poesia dos slams contemporâneos são vistas como instrumentos pedagógicos de descolonização curricular no Ensino Médio?",
        [
            ("Por incentivarem os estudantes a memorizarem gramáticas normativas sem qualquer debate sobre os problemas sociais do bairro.", False),
            ("Por transferirem a gestão das salas de aula para companhias privadas de entretenimento televisivo comercial.", False),
            ("Por proibirem a discussão de questões de gênero, raça e classe nas escolas para evitar desacordos ideológicos entre jovens.", False),
            ("Por limitarem as apresentações poéticas a competições esportivas nas quais o vencedor recebe bolsas financeiras exclusivas.", False),
            ("Por estimularem a escrita autoral, a presença corporal e a tomada da palavra por estudantes de grupos historicamente marginalizados.", True)
        ],
        "- **Etapa 1:** A escola tradicional muitas vezes reproduziu um ensino passivo e focado na memorização de cânones literários distantes da realidade discente.\n- **Etapa 2:** Os slams em sala de aula restituem o corpo, a oralidade e a vivência cotidiana dos alunos como matéria poética nobre, promovendo autoestima, criticidade cidadã e cumprimento das diretrizes antirracistas da Lei 10.639/03, o que legitima a alternativa E."
    ))

    questoes_brutas.append((
        56, "EM13CHS302", "dificil",
        "Qual é o papel do grafite nos centros urbanos quando analisado a partir das reflexões de Paul Gilroy sobre a estética de resistência periférica?",
        [
            ("Interromper a monotonia cinzenta da segregação urbana, demarcando presença, memória visual e direito soberano à metrópole.", True),
            ("Depredar edifícios tombados para desvalorizar os bairros centrais e afugentar investimentos em transporte público.", False),
            ("Divulgar marcas de refrigerantes e roupas de grife através de logomarcas comerciais encomendadas por agências.", False),
            ("Substituir placas de trânsito oficiais para criar desordem no fluxo de veículos automotores nas grandes avenidas.", False),
            ("Isolar os artistas visuais populares das reivindicações comunitárias, priorizando a comercialização em galerias nobres.", False)
        ],
        "- **Etapa 1:** A metrópole moderna estabelece uma separação espacial rígida entre os bairros ricos e as periferias segregadas.\n- **Etapa 2:** O grafiteiro intervém nas superfícies cinzentas e muros excludentes da cidade com spray, reivindicando visualmente o direito à cidade e celebrando identidades negras e ancestrais no espaço comum, tornando a alternativa A correta."
    ))

    questoes_brutas.append((
        57, "EM13CHS603", "dificil",
        "De que modo a literatura de Ale Santos em O Último Ancestral e de Lu Ain-Zaila projeta um Afrofuturismo com matizes singulares brasileiros?",
        [
            ("Copiando estritamente os cenários de ficção científica dos Estados Unidos sem qualquer menção à cultura das periferias locais.", False),
            ("Entrelaçando elementos do candomblé, tecnologias populares de favela e o quilombismo em cenários distópicos e cyberpunk.", True),
            ("Afirmando que o Brasil é uma nação imune a tensões raciais em virtude da vigência permanente de uma democracia racial idílica.", False),
            ("Rejeitando o uso de termos em português em favor da redação exclusiva de romances na língua inglesa para exportação.", False),
            ("Condicionando suas narrativas à autorização prévia das comissões editoriais dos ministérios militares nacionais.", False)
        ],
        "- **Etapa 1:** O afrofuturismo brasileiro não é simples importação dos modelos norte-americanos; ele possui lastro material e espiritual próprio.\n- **Etapa 2:** Autores nacionais incorporam a sabedoria dos orixás, a mística dos quilombos e a capacidade inventiva das favelas a tramas tecnológicas futuristas, criando um imaginário singular de emancipação afro-brasileira, confirmando a alternativa B."
    ))

    questoes_brutas.append((
        58, "EM13CHS606", "dificil",
        "Ao conectar o rap dos Racionais MC's às pesquisas sociológicas de Gabriel Feltran e Érica Peçanha, que dinâmica social se evidencia nas periferias?",
        [
            ("A ausência total de qualquer forma de organização cívica, deixando as comunidades inteiramente à mercê da anarquia social.", False),
            ("A perda contínua do interesse dos jovens pelas expressões artísticas em prol de atividades estritamente burocráticas.", False),
            ("A constituição da cultura periférica (rap, saraus e slams) como rede de sociabilidade, proteção e mediação crítica de conflitos.", True),
            ("A aceitação incondicional das propostas estéticas divulgadas pelos grandes canais de televisão aberta comercial.", False),
            ("O fechamento hermético das quebradas a qualquer diálogo político ou cultural com o restante do território nacional.", False)
        ],
        "- **Etapa 1:** Estudos contemporâneos de sociologia urbana investigam como a juventude periférica sobrevive em contextos de abandono e violência de Estado.\n- **Etapa 2:** Conforme Feltran e Peçanha, coletivos de rap, saraus e slams funcionam como teias vitais de acolhimento ético, produção de sentido e defesa dos direitos humanos contra a barbárie cotidiana, legitimando a alternativa C."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "Como a prática de estalar os dedos nos torneios de slam sintetiza uma ética de escuta e acolhimento comunitário da palavra falada?",
        [
            ("Constitui um sinal de desrespeito acordado previamente para pressionar os jurados a reduzirem as notas dos concorrentes.", False),
            ("Representa uma imposição das emissoras de rádio para evitar ruídos de fundo durante as transmissões digitais ao vivo.", False),
            ("Trata-se de uma imposição médica para evitar lesões musculares nas palmas das mãos causadas por aplausos prolongados.", False),
            ("Permite à assembleia demonstrar entusiasmo e sintonia com os versos sem ensurdecer nem sobrepor a voz de quem declama.", True),
            ("Funciona como senha secreta entre os competidores para sinalizar que o tempo regulamentar de declamação expirou.", False)
        ],
        "- **Etapa 1:** Nos slams, a palavra oral é a protagonista soberana; o microfone ou a voz no peito precisam alcançar os ouvidos de toda a plateia.\n- **Etapa 2:** O estalo coletivo dos dedos manifesta carinho, calor humano e vibração política imediata sem produzir o estrondo das palmas, garantindo a escuta atenta da dicção de quem fala, o que consagra a alternativa D."
    ))

    questoes_brutas.append((
        60, "EM13CHS102", "dificil",
        "Em síntese, qual é a principal vitória intelectual e cultural das poéticas afrodiaspóricas e do Afrofuturismo diante da modernidade ocidental?",
        [
            ("A comprovação definitiva de que os países europeus foram os únicos criadores das artes visuais e da literatura no planeta.", False),
            ("O confinamento eterno dos povos colonizados ao espaço das lembranças rurais sem direito a debater ciência e técnica.", False),
            ("A demonstração de que a tecnologia moderna opera de forma neutra e não possui vínculos com disputas sociais ou raciais.", False),
            ("O abandono definitivo de todas as matrizes culturais africanas ancestrais em nome da assimilação dos valores burgueses.", False),
            ("A restituição do corpo negro como sujeito soberano do saber, da tecnologia e da imaginação dos rumos futuros da humanidade.", True)
        ],
        "- **Etapa 1:** Por séculos, o racismo colonial buscou reduzir o negro a mero objeto de estudo, força de trabalho escravizada e corpo do passado.\n- **Etapa 2:** O afrofuturismo e as poéticas da diáspora quebram esse cárcere epistêmico, afirmando que o negro domina as tecnologias do presente, reinventa o tempo a partir da memória ancestral e possui a chave visionária para projetar o futuro da civilização, validando com distinção a alternativa E."
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
    md.append('eixo: "Eixo IV: Estética, Filosofia da Arte e Poéticas da Negritude"')
    md.append('capitulo: "Capítulo 31: Poéticas Afrodiaspóricas e Afrofuturismo"')
    md.append('objeto_de_conhecimento: "O Atlântico Negro em Paul Gilroy, as estéticas periféricas e o hip-hop como filosofia de sobrevivência, a poesia dos slams e o Afrofuturismo como reconfiguração existencial do futuro"')
    md.append('ebook_fonte: "em-fil-c31-poeticas-afrodiasporicas-afrofuturismo.md"')
    md.append('habilidades:')
    md.append('  - "EM13CHS101"')
    md.append('  - "EM13CHS102"')
    md.append('  - "EM13CHS301"')
    md.append('  - "EM13CHS302"')
    md.append('  - "EM13CHS603"')
    md.append('  - "EM13CHS606"')
    md.append('total_exercicios: 60')
    md.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    md.append("---\n")

    md.append("# Lista de Exercícios: Poéticas Afrodiaspóricas e Afrofuturismo\n")
    md.append("## Nível Básico\n")

    letras = ["A", "B", "C", "D", "E"]

    for num, hab, dif, enunciado, alternativas, resolucao in questoes:
        if num == 21:
            md.append("## Nível Intermediário\n")
        elif num == 41:
            md.append("## Nível Difícil\n")

        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-31-poeticas-afrodiasporicas-afrofuturismo -->")
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
    md.append("- GILROY, Paul. *O Atlântico negro: modernidade e dupla consciência*. Tradução de Cid Knipel Moreira. 2. ed. São Paulo: Editora 34, 2012.")
    md.append("- DERY, Mark. Black to the future: interviews with Samuel R. Delany, Greg Tate, and Tricia Rose. In: DERY, Mark (Ed.). *Flame wars: the discourse of cyberculture*. Durham: Duke University Press, 1994.")
    md.append("- ESHUN, Kodwo. *Mais brilhante que o sol: aventuras na ficção sônica*. Tradução de Rogério de Campos. São Paulo: Veneta, 2023.")
    md.append("- RACIONAIS MC'S. *Sobrevivendo no inferno*. São Paulo: Companhia das Letras, 2018.")
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
    destino_final = "content/medio/volume-unico/filosofia/eixo-4-estetica/cap-31-poeticas-afrodiasporicas-afrofuturismo/ebooks/em-fil-c31-poeticas-afrodiasporicas-afrofuturismo-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 31 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
