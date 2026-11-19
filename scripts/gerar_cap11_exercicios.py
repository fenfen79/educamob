# -*- coding: utf-8 -*-
"""
Script de Geração e Validação das 60 Questões de Filosofia - Cap 11
Objeto: A Ética Deontológica e o Imperativo Categórico de Kant
Habilidades BNCC: EM13CHS101, EM13CHS501, EM13CHS502, EM13CHS605
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
        "Etimologicamente, o termo 'Deontologia' tem sua raiz no vocábulo grego déon (déontos). Qual é o significado original dessa palavra grega?",
        "Cálculo matemático de figuras geométricas tridimensionais.",
        "O dever, a obrigação moral ou aquilo que é vinculante por princípio.",
        "Comércio de especiarias e tecidos finos em cidades marítimas.",
        "Trabalho artesanal de fabricação de armas de bronze.",
        "Alegria passageira obtida em celebrações e banquetes públicos.",
        "B",
        "A palavra grega déon/déontos designa o dever, aquilo que se deve fazer por princípio racional, fundando a ética deontológica do dever puro."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "Na abertura de sua obra Fundamentação da Metafísica dos Costumes, Immanuel Kant afirma que a única coisa boa sem limitação no mundo é:",
        "A grande riqueza material acumulada em cofres bancários.",
        "A Boa Vontade (Guter Wille), que é boa em si mesma pelo seu próprio querer racional.",
        "A inteligência viva utilizada para ludibriar adversários no comércio.",
        "A força física de guerreiros que vencem competições atléticas.",
        "A fama pública obtida por meio de discursos na tribuna da cidade.",
        "B",
        "Para Kant, dons da fortuna e talentos intelectuais podem ser corrompidos para o mal; apenas a boa vontade é incondicionalmente boa pelo seu princípio moral puro."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "Por que Kant rejeita a busca da 'Felicidade' como fundamento supremo para a lei moral universal?",
        "Porque os cidadãos de cidades portuárias preferem morar em casas de campo.",
        "Porque a felicidade é empírica, subjetiva e variável para cada indivíduo, não podendo fornecer uma regra moral necessária e válida para todos os seres racionais.",
        "Porque as leis civis do Estado proíbem a leitura de poemas trágicos em praças públicas.",
        "Porque o clima frio do norte da Europa impede a celebração de casamentos no inverno.",
        "Porque a felicidade foi inventada por astrônomos para calcular o movimento dos cometas.",
        "B",
        "O que faz um indivíduo feliz pode desagradar a outro; a lei moral, para ser universal, deve fundar-se na razão pura e no dever, não na volubilidade dos desejos empíricos."
    ))

    questoes_brutas.append((
        4, "EM13CHS501", "basico",
        "De acordo com a tipologia kantiana das ações, o que é uma ação 'Conforme ao Dever' (Pflichtmässig)?",
        "Uma ação que viola diretamente a lei moral e prejudica os semelhantes.",
        "Uma ação que cumpre externamente o que a lei prescreve, mas é motivada por um interesse egoísta, medo de castigo ou inclinação afetiva.",
        "Uma ação realizada sem que o sujeito saiba o que está fazendo no momento.",
        "Uma ação decidida por meio de sorteios feitos em templos sagrados.",
        "Uma ação que produz apenas resultados matemáticos em planilhas contábeis.",
        "B",
        "A ação conforme ao dever tem legalidade externa, mas não tem valor moral autêntico porque o motivo impulsionador não é o respeito à lei moral, mas a conveniência."
    ))

    questoes_brutas.append((
        5, "EM13CHS501", "basico",
        "No célebre exemplo kantiano do comerciante que cobra o preço justo de crianças ingênuas para não perder a clientela, qual é a classificação moral dessa ação?",
        "Ação plenamente virtuosa dotada do mais elevado mérito moral.",
        "Ação conforme ao dever, com legalidade externa, porém desprovida de valor moral puro, pois decorre do cálculo do interesse comercial.",
        "Ação contrária ao dever que merece punição penal imediata pelo tribunal.",
        "Ação heroica inspirada no modelo do bom samaritano da tradição bíblica.",
        "Ação involuntária provocada por delírios febris passageiros do comerciante.",
        "B",
        "O comerciante pratica o preço justo não por amor ao dever, mas para preservar sua reputação e seus lucros; logo, sua ação tem conveniência pragmática, mas não valor moral."
    ))

    questoes_brutas.append((
        6, "EM13CHS501", "basico",
        "Qual é a condição indispensável para que uma ação humana possua 'Valor Moral Autêntico' de acordo com a ética deontológica de Kant?",
        "Ser aprovada por votação secreta de parlamentares de assembleias civis.",
        "Ser praticada exclusivamente por dever (Aus Pflicht), motivada pelo puro respeito à Lei Moral, mesmo contrariando as inclinações sensíveis do sujeito.",
        "Produzir riquezas financeiras que possam ser doadas para reformas de edifícios.",
        "Ser elogiada em jornais e periódicos publicados na capital do país.",
        "Ser executada por pessoas que possuam patentes de oficiais de cavalaria militar.",
        "B",
        "O mérito moral resplandece quando o indivíduo age por puro dever e respeito à lei da razão, superando seus interesses imediatos e simpatias passageiras."
    ))

    questoes_brutas.append((
        7, "EM13CHS502", "basico",
        "O 'Imperativo Hipotético' formulado por Immanuel Kant comanda uma ação sob qual estrutura lógica condicional?",
        "'Deves agir sempre sem pensar nas consequências práticas de teus atos.'",
        "'Se queres alcançar o objetivo X, deves praticar a ação Y como meio necessário.'",
        "'Proíbe-se qualquer debate racional sobre as decisões tomadas por governantes.'",
        "'Todas as pessoas devem adotar a mesma religião ensinada nas escolas públicas.'",
        "'As leis da natureza deixam de funcionar quando o indivíduo dorme à noite.'",
        "B",
        "O imperativo hipotético comanda a conduta como meio para atingir outro fim exterior almejado (habilidade técnica ou prudência), perdendo a força se o sujeito renunciar àquele fim."
    ))

    questoes_brutas.append((
        8, "EM13CHS502", "basico",
        "O 'Imperativo Categórico' de Kant distingue-se do imperativo hipotético porque comanda a conduta humana de maneira:",
        "Condicionada ao humor passageiro do indivíduo no momento da decisão.",
        "Incondicional, absoluta, necessária e válida por si mesma para todos os seres racionais.",
        "Dependente da quantidade de moedas de prata que o agente possui no banco.",
        "Válida exclusivamente para marinheiros que viajam por mares gelados do norte.",
        "Limitada aos períodos em que as colheitas de trigo são abundantes no campo.",
        "B",
        "O imperativo categórico prescreve uma ação como objetivamente necessária em si mesma, sem relação com qualquer fim externo ou condição particular."
    ))

    questoes_brutas.append((
        9, "EM13CHS502", "basico",
        "A Primeira Fórmula do Imperativo Categórico (Fórmula da Lei Universal) estabelece o seguinte preceito basilar para o agir:",
        "'Age de modo a acumular o maior número possível de propriedades rurais.'",
        "'Age apenas segundo uma máxima tal que possas ao mesmo tempo querer que ela se torne uma lei universal da natureza.'",
        "'Age de acordo com as ordens verbais emitidas por magistrados em audiências públicas.'",
        "'Age sempre imitando os costumes dos cidadãos mais velhos de tua cidade.'",
        "'Age de forma a evitar qualquer tipo de trabalho físico durante os finais de semana.'",
        "B",
        "A fórmula da lei universal propõe o teste de não contradição racional: a máxima particular de minha ação só é justa se puder ser universalizada para toda a humanidade."
    ))

    questoes_brutas.append((
        10, "EM13CHS605", "basico",
        "A Segunda Fórmula do Imperativo Categórico (Fórmula da Humanidade) ordena que tratemos a humanidade, em nós e nos outros, da seguinte forma:",
        "Como mercadorias úteis que podem ser trocadas por bens materiais no comércio.",
        "Sempre e simultaneamente como um Fim em si mesmo, e nunca simplesmente como um Meio descartável.",
        "Como peças mecânicas de engrenagens de fábricas industriais de calçados.",
        "Como escravos submetidos aos interesses econômicos de proprietários de terra.",
        "Como súditos obrigados a aplaudir generais de exércitos militares em desfiles.",
        "B",
        "A fórmula da humanidade proíbe a instrumentalização da pessoa humana: o ser humano é portador de dignidade inalienável e não pode ser coisificado para benefício alheio."
    ))

    questoes_brutas.append((
        11, "EM13CHS605", "basico",
        "Na distinção kantiana entre Coisas e Pessoas, qual característica fundamental define o estatuto moral das pessoas?",
        "Elas possuem um preço de mercado que varia de acordo com a inflação econômica.",
        "Elas possuem Dignidade (Würde), não têm preço e não admitem substituição por nenhum equivalente material.",
        "Elas podem ser vendidas em leilões públicos de feiras municipais de tecidos.",
        "Elas perdem seus direitos civis sempre que cometem erros de cálculo aritmético.",
        "Elas devem prestar juramentos de submissão a corporações comerciais privadas.",
        "B",
        "Coisas têm preço e podem ser substituídas por moedas; pessoas têm dignidade incondicional, merecendo respeito inviolável e reverência ética absoluta."
    ))

    questoes_brutas.append((
        12, "EM13CHS502", "basico",
        "O que significa o conceito de 'Heteronomia da Vontade' na filosofia moral de Immanuel Kant?",
        "A capacidade de governar a si mesmo por meio de princípios racionais puros.",
        "A condição em que a vontade é determinada por forças exteriores à razão (como o medo da punição, a busca de louvores sociais ou as inclinações dos sentidos).",
        "O hábito de escrever cartas com tintas coloridas importadas de cidades costeiras.",
        "A habilidade em calcular medidas de terrenos agrícolas utilizando cordas de linho.",
        "O cultivo de amizades fraternas em comunidades filosóficas rurais isoladas.",
        "B",
        "Na heteronomia, o agente não é verdadeiramente livre: sua vontade obedece a leis alheias (sociais, biológicas ou religiosas), comportando-se como autômato de impulsos externos."
    ))

    questoes_brutas.append((
        13, "EM13CHS502", "basico",
        "Para Kant, a verdadeira 'Autonomia' moral do ser humano ocorre quando o sujeito:",
        "Faz tudo o que lhe dá na cabeça sem respeitar nenhuma lei ou direito alheio.",
        "Obedece à Lei Moral que a sua própria Razão pura formulou para si mesma, sendo ao mesmo tempo súdito e soberano legislador.",
        "Entrega suas economias financeiras para que magistrados comprem ferramentas de trabalho.",
        "Decide morar dentro de um barril de cerâmica em praças públicas de capitais.",
        "Recusa-se a falar qualquer idioma que não seja o latim clássico da Antiguidade.",
        "B",
        "Autonomia não é capricho ou anarquia, mas autolegislação da razão: o sujeito moral livre é aquele que dá a lei a si mesmo e a cumpre com fidelidade inabalável."
    ))

    questoes_brutas.append((
        14, "EM13CHS101", "basico",
        "O que é o 'Reino dos Fins' (Reich der Zwecke) concebido por Immanuel Kant em sua teoria ética?",
        "Um território geográfico delimitado por muralhas de pedra no leste da Europa.",
        "Uma comunidade moral ideal formada por todos os seres racionais que se tratam reciprocamente como fins em si mesmos e portadores de dignidade inalienável.",
        "Um banco comercial responsável pela emissão de moedas de prata para o comércio exterior.",
        "Um tribunal militar encarregado de julgar motins em frotas navais em alto-mar.",
        "Uma sociedade de artesãos dedicada à confecção de tapeçarias de seda bordadas a ouro.",
        "B",
        "O Reino dos Fins é a união sistemática de seres racionais que legislam em harmonia, onde nenhuma pessoa é usada como ferramenta descartável para os propósitos de outrem."
    ))

    questoes_brutas.append((
        15, "EM13CHS605", "basico",
        "O princípio fundamental da Dignidade da Pessoa Humana, consagrado no artigo 1º da Constituição Brasileira de 1988, possui raiz filosófica direta em qual conceito kantiano?",
        "No conceito de estado de natureza hobbesiano dominado pela guerra de todos contra todos.",
        "Na Segunda Fórmula do Imperativo Categórico, que proíbe instrumentalizar o ser humano e reconhece seu valor absoluto como fim em si mesmo.",
        "Na teoria da tábula rasa de John Locke sobre o aprendizado infantil.",
        "Na física mecanicista de Descartes que divide a realidade em mente e matéria extensa.",
        "Na doutrina do justo meio aristotélico entre a avareza e a prodigalidade monetária.",
        "B",
        "A vedação à tortura, a proteção aos direitos fundamentais e o combate à exploração repousam diretamente no princípio kantiano de que o ser humano não admite preço."
    ))

    questoes_brutas.append((
        16, "EM13CHS501", "basico",
        "No teste de universalização da máxima da 'Falsa Promessa' (pegar dinheiro emprestado prometendo pagar sabendo que não pagará), por que essa conduta é imoral para Kant?",
        "Porque as cédulas de papel-moeda podem perder o valor de troca com o tempo.",
        "Porque, se essa máxima fosse universalizada, a própria instituição da promessa se autodestruiria, pois ninguém mais acreditaria em promessa alguma na sociedade.",
        "Porque os bancos municipais cobram taxas muito altas para abrir contas bancárias.",
        "Porque as testemunhas do empréstimo teriam de comparecer diariamente ao tribunal civil.",
        "Porque as dívidas financeiras deveriam ser quitadas exclusivamente em sacas de trigo.",
        "B",
        "A falsa promessa gera uma autocontradição lógica interna: quem promete falsamente quer que acreditem nele, mas quer que a quebra de promessa seja regra, destruindo a confiança."
    ))

    questoes_brutas.append((
        17, "EM13CHS605", "basico",
        "No contexto da bioética e dos ensaios clínicos com seres humanos, qual atrocidade histórica comprovou a urgência de aplicar a proibição kantiana da instrumentalização das pessoas?",
        "A construção de estradas de ferro no deserto do Saara durante o início do século XX.",
        "O Estudo de Sífilis de Tuskegee, no qual homens negros pobres foram usados deliberadamente como cobaias sem tratamento médico para observação científica.",
        "A reforma de bibliotecas escolares em capitais europeias durante o período de férias.",
        "O cultivo de lavouras de arroz irrigado em margens de rios que sofriam com inundações.",
        "A realização de competições esportivas de barco a remo em lagos de água doce.",
        "B",
        "O caso de Tuskegee utilizou vidas humanas indefesas como meros meios para fins de terceiros, violando o princípio kantiano que originou o Código de Nuremberg."
    ))

    questoes_brutas.append((
        18, "EM13CHS501", "basico",
        "No célebre debate sobre 'O Suposto Direito de Mentir por Amor à Humanidade' travado com Benjamin Constant, qual foi a posição rigorosa de Kant?",
        "Kant defendeu que as pessoas devem mentir sempre que quiserem obter vantagens comerciais.",
        "Kant sustentou que mentir é categoricamente imoral em qualquer hipótese, pois abrir exceções destrói a universalidade da lei moral e a confiança na linguagem humana.",
        "Kant afirmou que apenas os médicos de hospitais públicos têm o direito legal de mentir aos doentes.",
        "Kant propôs que as disputas verbais fossem resolvidas por duelos de esgrima ao amanhecer.",
        "Kant determinou que as testemunhas de tribunal deveriam assinar certidões escritas em versos rimados.",
        "B",
        "Para Kant, a veracidade é um dever estrito incondicional; admitir que se pode mentir por conveniência destrói o fundamento de todo contrato social e da verdade objetiva."
    ))

    questoes_brutas.append((
        19, "EM13CHS502", "basico",
        "Em seu ensaio filosófico À Paz Perpétua (1795), Immanuel Kant estendeu os princípios de sua ética deontológica para o plano das relações internacionais, propondo:",
        "A invasão armada de países vizinhos para unificar todos os territórios sob um único império militar.",
        "A criação de uma federação cosmopolita de repúblicas livres e pacíficas, orientadas pelo direito internacional e pela hospitalidade universal.",
        "O fechamento definitivo de todos os portos marítimos para impedir o intercâmbio de mercadorias.",
        "A cobrança de pedágios em ouro sobre navios que cruzam os estreitos de navegação comercial.",
        "A substituição de diplomatas civis por esquadrões de infantaria treinados em montanhas geladas.",
        "B",
        "Kant concebeu a paz perpétua como um imperativo moral global, antecipando as bases da Liga das Nações e da ONU na construção de uma ordem mundial regida pelo direito e não pela força."
    ))

    questoes_brutas.append((
        20, "EM13CHS501", "basico",
        "Quando um estudante devolve uma carteira recheada de dinheiro encontrada na rua unicamente por receio de ter sido flagrado por câmeras de segurança, sua ação tem:",
        "Valor moral genuíno e puro de acordo com a ética deontológica kantiana.",
        "Conformidade externa ao dever, porém desprovida de mérito moral puro, pois seu motivo foi o medo da punição e não o respeito autônomo à lei moral.",
        "Natureza criminosa gravíssima prevista nos códigos penais das capitais.",
        "Aprovação divina equivalente aos votos de pobreza de monges medievais.",
        "Inconsistência física provocada pela falta de identificação do dono da carteira.",
        "B",
        "A conduta é correta aos olhos da lei civil, mas moralmente oca para Kant: o estudante não agiu pelo dever de justiça, mas pelo medo da vergonha pública e da sanção penal."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao contrastar a ética deontológica de Kant com o utilitarismo moderno, percebe-se uma divergência frontal sobre o critério de avaliação moral, pois:",
        "Kant valoriza os lucros financeiros das empresas e o utilitarismo defende o jejum de alimentos.",
        "Kant avalia a moralidade a partir da intenção pura e do dever incondicional da vontade, enquanto o utilitarismo julga a ação unicamente pelo cálculo de suas consequências empíricas úteis.",
        "Ambos defendem que a verdade moral deve ser revelada através de oráculos em montanhas sagradas.",
        "O utilitarismo proíbe a busca do prazer e Kant exige que todos os cidadãos trabalhem na agricultura.",
        "Kant afirma que os sentimentos devem governar a razão e o utilitarismo prega a indiferença total à dor.",
        "B",
        "A deontologia kantiana é principiológica e apriorística (a ação vale por si mesma); o utilitarismo é consequencialista (a ação vale pela quantidade de bem-estar ou dor que produz)."
    ))

    questoes_brutas.append((
        22, "EM13CHS501", "intermediario",
        "Por que, para Kant, uma pessoa caridosa que ajuda os necessitados movida por compaixão natural e alegria de ver os outros felizes não pratica uma ação de 'valor moral puro'?",
        "Porque Kant considerava que a caridade aos necessitados deve ser proibida por leis do Estado.",
        "Porque a compaixão é uma inclinação sensível involuntária que decorre do temperamento; a moralidade pura exige o dever racional que se impõe mesmo quando não sentimos simpatia alguma pelo outro.",
        "Porque a compaixão consome energias corporais que deveriam ser empregadas em treinos atléticos.",
        "Porque os necessitados deveriam trabalhar dezoito horas por dia em oficinas de tecelagem manual.",
        "Porque as doações financeiras desvalorizam a circulação de moedas bancárias nas feiras locais.",
        "B",
        "Kant não diz que ter compaixão é ruim (é louvável e bela), mas sustenta que sentimentos são inconstantes e não podem fundar a lei moral; o verdadeiro valor moral resplandece quando agimos por dever."
    ))

    questoes_brutas.append((
        23, "EM13CHS502", "intermediario",
        "Considere a máxima de quem decide cometer suicídio para fugir de uma sequência desesperadora de dores existenciais. Ao aplicar o teste da universalização kantiana, por que essa ação se revela imoral?",
        "Porque os hospitais públicos perderiam receitas cobradas pelos atendimentos de pronto-socorro.",
        "Porque utilizar a própria vida (que é a condição da racionalidade e da moralidade) como mero meio instrumental para cessar dores sensíveis destrói a humanidade em si mesmo como fim supremo.",
        "Porque os túmulos nos cemitérios municipais ocupam terrenos que deveriam ser destinados ao cultivo de grãos.",
        "Porque as cerimônias de luto consomem velas de parafina que poderiam iluminar salas de aula.",
        "Porque a pessoa que comete suicídio deixa de pagar tributos fiscais sobre propriedades urbanas.",
        "B",
        "Destruir a própria existência racional para escapar da dor é tratar a si mesmo como coisa ou instrumento de alívio; a pessoa tem o dever estrito incondicional de preservar sua humanidade como fim em si."
    ))

    questoes_brutas.append((
        24, "EM13CHS605", "intermediario",
        "No ambiente de trabalho e nas relações corporativas, a Segunda Fórmula do Imperativo Categórico kantiano proíbe que contratemos pessoas para prestar serviços (como um pedreiro ou motorista)?",
        "Sim, a fórmula proíbe terminantemente qualquer relação contratual em que alguém preste serviços a outrem.",
        "Não; a fórmula proíbe tratar a pessoa simplesmente ou unicamente como meio descartável, exigindo que o trabalhador seja respeitado simultaneamente como um fim em si mesmo, com salário justo e dignidade inviolável.",
        "Sim, porque todos os cidadãos adultos deveriam ser obrigados a produzir seus próprios alimentos e roupas.",
        "Não, desde que o empregador pague os salários em barras de ferro fundido sem emitir recibos formais.",
        "Sim, porque as relações de trabalho remunerado foram banidas pelos tratados de direito internacional.",
        "B",
        "O imperativo não proíbe a cooperação funcional na divisão social do trabalho, mas condena a exploração desumanizadora: nunca trate o ser humano apenas como instrumento de seus interesses."
    ))

    questoes_brutas.append((
        25, "EM13CHS501", "intermediario",
        "No romance O Processo de Franz Kafka, o cidadão Josef K. é preso e julgado por um tribunal misterioso sem nunca ser informado de qual crime teria cometido. Como a ética kantiana analisa essa opressão burocrática?",
        "Como um modelo perfeito de organização administrativa que deveria ser implementado em todas as capitais.",
        "Como a mais brutal violação do Reino dos Fins, na qual o ser humano é integralmente coisificado, esvaziado de dignidade e reduzido a um joguete descartável de um poder cego e heterônomo.",
        "Como um exercício espiritual salutar voltado a ensinar a paciência e a frugalidade a bancários urbanos.",
        "Como uma consequência inevitável da falta de investimentos públicos no transporte ferroviário de passageiros.",
        "Como um litígio civil comum sobre posse de propriedades agrícolas que deveria ser resolvido por agrimensores.",
        "B",
        "Kafka denuncia a tragédia da heteronomia total: quando o sistema burocrático e estatal rebaixa o indivíduo a mero número e ferramenta manipulável, a dignidade moral kantiana é assassinada."
    ))

    questoes_brutas.append((
        26, "EM13CHS502", "intermediario",
        "Em quais termos Kant fundamenta a distinção entre uma ordem legal tirânica de um Estado e o dever de obediência moral do cidadão autônomo?",
        "O cidadão deve obedecer cegamente a qualquer ordem do governante, mesmo que este ordene o extermínio de inocentes.",
        "A verdadeira lei moral reside na razão autônoma; se uma ordem positiva do Estado exigir a violação da dignidade humana e o tratamento do outro como mero instrumento, o cidadão tem o dever ético de recusar obediência.",
        "O cidadão só pode desobedecer às leis do Estado caso comprove que seus impostos foram desviados por banqueiros.",
        "A legitimidade das leis do governo depende exclusivamente da quantidade de soldados armados que patrulham as ruas.",
        "O dever moral é determinado pelo voto da maioria em eleições municipais de cidades costeiras.",
        "B",
        "A lei civil não pode sobrepor-se à lei moral universal da razão; obedecer a decretos desumanos apenas por medo ou subserviência cega é heteronomia covarde e cumplicidade moral."
    ))

    questoes_brutas.append((
        27, "EM13CHS605", "intermediario",
        "No debate sobre a Pirataria Digital de softwares e livros, como a aplicação do teste de universalização kantiano desqualifica a desculpa de que 'uma cópia a mais em PDF não custa nada para a editora'?",
        "Mostrando que a eletricidade consumida pelos servidores virtuais descarrega as baterias de carros elétricos.",
        "Demonstrando que, se a máxima de nunca pagar por obras intelectuais fosse universalizada, a produção cultural e científica entraria em colapso, provando que o infrator atua como parasita da honestidade alheia.",
        "Afirmando que os jovens que baixam arquivos virtuais devem ser proibidos de ingressar em cursos de direito.",
        "Evidenciando que os autores de livros acadêmicos deveriam trabalhar gratuitamente para o governo nacional.",
        "Comprovando que os discos rígidos de computadores sofrem desgaste acelerado ao armazenarem textos digitais.",
        "B",
        "A pirataria não resiste ao teste da lei universal: se todos piratearem, ninguém mais produzirá; quem pirateia quer a exceção para si enquanto os outros pagam, violando a moralidade pura."
    ))

    questoes_brutas.append((
        28, "EM13CHS501", "intermediario",
        "Por que, para a deontologia de Immanuel Kant, prometer algo sabendo que não se cumprirá constitui uma quebra da razão prática muito mais profunda do que um mero prejuízo financeiro?",
        "Porque os bancos municipais cobram multas em dinheiro muito elevadas sobre promissórias vencidas.",
        "Porque destrói a própria condição de inteligibilidade e confiança mútua entre seres racionais, transformando a palavra humana em mentira e usando o outro como objeto ingênuo de manipulação egoísta.",
        "Porque as pessoas que recebem promessas falsas perdem a vontade de comer alimentos nutritivos durante o dia.",
        "Porque os juízes civis são obrigados a gastar folhas de pergaminho para redigir intimações judiciais.",
        "Porque as promessas não cumpridas provocam tempestades de poeira nas estradas rurais do interior.",
        "B",
        "A falsa promessa corrói a própria racionalidade da linguagem humana e instrumentaliza o semelhante; ela viola frontalmente tanto a fórmula da universalidade quanto a da dignidade humana."
    ))

    questoes_brutas.append((
        29, "EM13CHS502", "intermediario",
        "Na análise do Imperativo Categórico, qual é a falha estrutural de quem age buscando exclusivamente a recompensa do céu ou o temor do fogo do inferno?",
        "O indivíduo gasta muito azeite para manter acesas as velas de capelas e templos religiosos.",
        "A conduta é totalmente heterônoma e instrumental: age-se por interesse em uma recompensa exterior ou por pavor de uma punição futura, e não pelo dever puro de respeito à dignidade e à justiça.",
        "As religiões históricas proíbem a leitura de tratados de geometria e de astronomia moderna.",
        "Os sacerdotes de ordens monásticas são proibidos de possuir propriedades agrícolas no campo.",
        "O sujeito esquece que as leis civis dos governos democráticos exigem o recolhimento de tributos bancários.",
        "B",
        "Agir pelo medo da danação ou pelo desejo do paraíso é seguir um imperativo hipotético de cálculo ('Se queres o céu, faze Y'); não é moralidade pura, mas interesse pragmático transmundano."
    ))

    questoes_brutas.append((
        30, "EM13CHS605", "intermediario",
        "Qual conexão ética e jurídica se estabelece entre a proibição kantiana da instrumentalização das pessoas e o princípio do 'Consentimento Livre e Esclarecido' na medicina moderna?",
        "A exigência de que os pacientes internados assinem termos de compromisso redigidos em línguas estrangeiras.",
        "A garantia inegociável de que nenhum paciente pode ser submetido a cirurgias, vacinas experimentais ou pesquisas sem que compreenda os riscos e consinta voluntariamente, preservando sua autonomia como sujeito.",
        "A obrigação de que os hospitais públicos cobrem taxas de consulta em moedas de ouro maciço dos doentes.",
        "A proibição de que os médicos conversem sobre o estado de saúde dos pacientes com seus familiares diretos.",
        "A determinação de que os medicamentos farmacêuticos sejam distribuídos apenas aos finais de semana.",
        "B",
        "O consentimento informado é a concretização do princípio da autonomia kantiana: o indivíduo é soberano sobre seu próprio corpo e mente, não podendo ser transformado em cobaia involuntária."
    ))

    questoes_brutas.append((
        31, "EM13CHS501", "intermediario",
        "No caso limite do 'Assassino à Porta' formulado por Benjamin Constant contra o rigorismo kantiano, qual foi o argumento de Constant para defender que existe um direito de mentir?",
        "Constant afirmou que os assassinos têm alergia a mentiras e fogem imediatamente ao ouvirem relatos falsos.",
        "Ele argumentou que o dever de dizer a verdade só se aplica perante quem tem direito à verdade; um assassino que pretende cometer um crime violento perdeu qualquer legitimidade moral para exigir a verdade.",
        "Ele defendeu que as pessoas que moram em casas de campo não precisam fechar suas portas durante a noite.",
        "Ele sustentou que os crimes cometidos com armas de ferro não são punidos pelos códigos penais modernos.",
        "Ele afirmou que os proprietários de residências urbanas devem pagar tributos adicionais para manter policiais na rua.",
        "B",
        "Benjamin Constant propõe a flexibilização relacional do dever: a verdade é um direito de quem age retamente; quem vem para assassinar quebrou o pacto da justiça e não faz jus à veracidade."
    ))

    questoes_brutas.append((
        32, "EM13CHS502", "intermediario",
        "Como a distinção entre a 'Res Cogitans' (pensamento livre) e a 'Res Extensa' (natureza mecanicista) em Descartes preparou a concepção kantiana da liberdade moral autônoma?",
        "Permitindo que os navegadores marítimos calculassem a longitude das praias utilizando bússolas de latão.",
        "Mostrando que, enquanto o corpo físico pertence ao reino causal da natureza mecânica, a razão humana possui a faculdade transcendental de autodeterminar-se livremente no plano moral.",
        "Provando que as leis da gravidade não afetam os pássaros que voam sobre florestas de pinheiros no inverno.",
        "Exigindo que os filósofos da natureza abandonem a pesquisa anatômica para se dedicarem à poesia épica.",
        "Determinando que as crianças de colégios públicos aprendam a falar francês antes de aprenderem matemática.",
        "B",
        "A separação entre natureza e liberdade permitiu a Kant demonstrar que o homem como ser biológico sofre impulsos causais, mas como sujeito racional é livre para legislar sua própria lei moral."
    ))

    questoes_brutas.append((
        33, "EM13CHS605", "intermediario",
        "Na esfera da ética política, por que as tiranias, os regimes totalitários e as ditaduras militares representam a negação absoluta do imperativo categórico kantiano?",
        "Porque os governantes autoritários costumam fechar fábricas que produzem tecidos de algodão cru.",
        "Porque reduzem os cidadãos a meros instrumentos descartáveis do poder do Estado ou da ideologia de um líder supremo, privando-os de sua dignidade, de sua liberdade de expressão e de sua soberania moral.",
        "Porque os ministros de governos ditatoriais utilizam carruagens puxadas por quatro cavalos brancos.",
        "Porque as tropas do exército nacional patrulham as fronteiras rurais durante os meses de colheita agrícola.",
        "Porque os tribunais de exceção realizam audiências apenas nas primeiras horas da manhã ensolarada.",
        "B",
        "O totalitarismo subordina o ser humano à engrenagem do poder estatal, tratando cidadãos como cobaias ou meios descartáveis para fins exteriores, violando frontalmente a dignidade humana."
    ))

    questoes_brutas.append((
        34, "EM13CHS501", "intermediario",
        "Ao examinar a máxima da preguiça: 'Vou passar minha vida inteira no ócio e nos prazeres sem cultivar nenhum dos meus talentos naturais', por que essa conduta falha no teste de universalização de Kant?",
        "Porque os campos de trigo ficariam desprovidos de ferramentas manuais de colheita no verão.",
        "Porque, embora se possa conceber uma sociedade de homens ociosos, nenhum ser racional pode 'querer' racionalmente que essa máxima seja universalizada, pois como ser racional ele deseja o desenvolvimento de suas próprias capacidades para agir no mundo.",
        "Porque os agricultores que trabalham com arados de tração animal pagam impostos mais altos ao tesouro.",
        "Porque as escolas públicas municipais seriam obrigadas a fechar suas portas por falta de giz escolar.",
        "Porque o cultivo dos talentos exige que todos os jovens aprendam a tocar instrumentos musicais de corda.",
        "B",
        "Kant demonstra que há deveres para consigo mesmo: o ser humano racional não pode querer a universalização do desperdício de suas faculdades intelectuais e morais sem cair em autocontradição volitiva."
    ))

    questoes_brutas.append((
        35, "EM13CHS502", "intermediario",
        "Qual é a relação que Immanuel Kant estabelece entre o conceito de 'Liberdade Transcendental' e a capacidade de ser imputável moralmente pelos próprios atos?",
        "A liberdade consiste em poder voar com asas de penas de ganso sobre montanhas rochosas isoladas.",
        "A liberdade é a faculdade de iniciar espontaneamente uma cadeia causal de eventos no mundo; sem essa liberdade de autodeterminação da razão, a responsabilidade e a culpa moral seriam ficções sem sentido.",
        "A liberdade depende da autorização concedida por certidões lavradas em cartórios de cidades litorâneas.",
        "A imputabilidade moral aplica-se apenas a indivíduos que possuem patentes militares em exércitos da corte.",
        "A culpa penal deixa de existir sempre que os crimes são cometidos durante as noites de lua minguante.",
        "B",
        "Se o homem fosse inteiramente determinado pelo mecanicismo biológico exterior, não haveria mérito nem culpa; a liberdade moral é a premissa indispensável para que o sujeito responda por seus atos."
    ))

    questoes_brutas.append((
        36, "EM13CHS605", "intermediario",
        "Por que as práticas contemporâneas de trabalho análogo à escravidão e o tráfico internacional de pessoas constituem a mais flagrante profanação da moralidade deontológica?",
        "Porque essas práticas diminuem a arrecadação de tributos alfandegários sobre a exportação de minério de ferro.",
        "Porque tratam o ser humano como pura mercadoria com preço de compra e venda, apropriando-se de seus corpos como ferramentas descartáveis de lucro e anulando sua dignidade como fim em si mesmo.",
        "Porque os trabalhadores explorados em fazendas rurais utilizam foices confeccionadas com ferro enferrujado.",
        "Porque os traficantes de pessoas utilizam navios cargueiros que poluem as águas dos oceanos com óleo diesel.",
        "Porque as leis trabalhistas nacionais exigem que os contratos de trabalho sejam arquivados em pastas de plástico.",
        "B",
        "A escravidão é a coisificação absoluta da pessoa: aniquila a dignidade incondicional do sujeito racional e o rebaixa à condição de objeto comercializável com preço de mercado."
    ))

    questoes_brutas.append((
        37, "EM13CHS501", "intermediario",
        "Em sua obra Crítica da Razão Prática, Kant declara: 'Duas coisas enchem o ânimo de admiração e respeito sempre novos e crescentes: o céu estrelado sobre mim e a lei moral em mim.' O que expressa essa célebre afirmação?",
        "A preferência do filósofo pelo estudo da astronomia telescópica em detrimento da convivência social comunitária.",
        "A consciência da grandiosidade do cosmos físico visível que revela a pequenez biológica do homem, contrastada com a majestade infinita da razão moral autônoma que eleva o ser humano acima da natureza material.",
        "A obrigação de que os governantes instalem lunetas de observação astronômica nas praças centrais das cidades.",
        "A comprovação de que as leis morais foram desenhadas por deuses nas constelações estelares do céu noturno.",
        "A certeza de que as estações do ano determinam o nascimento de homens com temperamentos generosos e prudentes.",
        "B",
        "O céu estrelado situa o homem como átomo insignificante na imensidão física; a lei moral interior revela sua sublime dignidade e liberdade racional inalienável como legislador no Reino dos Fins."
    ))

    questoes_brutas.append((
        38, "EM13CHS502", "intermediario",
        "Ao examinar a conduta de um militar que obedece a ordens superiores para fuzilar civis desarmados sob a alegação de 'cumprir meu dever militar de soldado', como a deontologia kantiana desconstrói esse álibi?",
        "Afirmando que os fuzis utilizados pelas tropas militares eram de fabricação estrangeira e apresentavam defeitos de mira.",
        "Evidenciando que a obediência cega a ordens hierárquicas criminosas é heteronomia vil e covardia moral: o dever genuíno nunca pode violar o imperativo categórico da dignidade humana inalienável dos inocentes.",
        "Determinando que os julgamentos de crimes de guerra sejam realizados exclusivamente em tribunais de ilhas remotas.",
        "Sustentando que os soldados deveriam ter negociado pagamentos adicionais em barras de ouro antes de cumprirem as ordens.",
        "Provando que as leis militares dos países europeus proibiam a prática de tiros de festim em treinamentos de infantaria.",
        "B",
        "O dever autêntico em Kant não é submissão cega a regulamentos estatais tiranos; a lei moral proíbe transformar o inocente em alvo; cumprir ordens desumanas é cumplicidade indesculpável com o assassinato."
    ))

    questoes_brutas.append((
        39, "EM13CHS605", "intermediario",
        "No debate sobre o Marketing e a Publicidade de Consumo que utiliza gatilhos psicológicos inconscientes para manipular decisões de compra, qual crítica ética kantiana se impõe?",
        "A de que os cartazes publicitários colados em postes de luz urbana consomem muita cola à base de farinha de trigo.",
        "A de que essa manipulação emocional subordina a consciência do consumidor à condição de mero instrumento passivo para o lucro de empresas, solapando a autonomia racional de escolha do indivíduo.",
        "A de que os produtos anunciados nas transmissões de televisão possuem preços tabelados por ministérios públicos.",
        "A de que as empresas comerciais deveriam divulgar apenas mensagens poéticas escritas em línguas da Antiguidade.",
        "A de que os anúncios publicitários induzem os jovens a comprarem apenas calçados confeccionados com couro animal.",
        "B",
        "Ao explorar vulnerabilidades e medos inconscientes para arrancar compras mecânicas, o marketing manipulador desrespeita a agência autônoma da pessoa, instrumentalizando-a como mero meio de lucro."
    ))

    questoes_brutas.append((
        40, "EM13CHS501", "intermediario",
        "Como a distinção entre a 'Legalidade Externa' e a 'Moralidade Interna' em Kant permite desmascarar a hipocrisia de figuras públicas que cumprem as leis apenas quando estão sob os olhos das câmeras?",
        "Provando que as câmeras de vigilância urbana consomem muita energia elétrica gerada por hidrelétricas.",
        "Demonstrando que o mero cumprimento formal das leis por vaidade ou medo da opinião pública é legalidade oca; a verdadeira retidão moral exige a adesão pura e sincera da vontade interior ao princípio do dever.",
        "Exigindo que os políticos em campanha usem uniformes de linho branco em todos os debates em praça pública.",
        "Determinando que os discursos governamentais sejam conferidos por magistrados civis antes de serem transmitidos pelo rádio.",
        "Comprovando que os eleitores escolhem seus representantes com base na altura física e na cor dos sapatos dos candidatos.",
        "B",
        "Para a ética kantiana, o tribunal exterior da lei vigia apenas os atos visíveis; mas o tribunal autêntico da moralidade é o da própria consciência reflexiva, que exige honestidade incondicional no silêncio."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a célebre passagem de Kant na Fundamentação da Metafísica dos Costumes: 'A necessidade de minhas ações por puro respeito à lei prática é o que constitui o dever, perante o qual qualquer outro motivo tem de ceder, porque ele é a condição de uma vontade boa em si, cujo valor está acima de tudo.' De que maneira essa tese anula a validade ética de qualquer moral consequencialista?",
        "Negando que a experiência sensorial tenha utilidade na fabricação de tecidos e sapatos em indústrias urbanas.",
        "Evidenciando que o valor moral de uma ação não reside nos efeitos exteriores ou na utilidade futura que ela pode produzir, mas na máxima formal e incondicional da vontade que age por puro respeito ao dever.",
        "Afirmando que a razão humana é incapaz de distinguir entre o certo e o errado durante períodos de crise inflacionária.",
        "Determinando que as ações humanas devem ser sorteadas anualmente em urnas de barro por magistrados da capital.",
        "Provando que os filósofos iluministas da Prússia desconheciam as regras de comércio marítimo de portos estrangeiros.",
        "B",
        "**Etapa 1:** Interpretar o rigorismo apriorístico kantiano: a moralidade não depende do sucesso ou fracasso do ato no mundo sensível.\n**Etapa 2:** Concluir com a refutação do consequencialismo: se o valor moral dependesse dos efeitos externos, estaria subordinado à contingência empírica; para Kant, o bem reside na pureza do motivo interior e no respeito à lei."
    ))

    questoes_brutas.append((
        42, "EM13CHS501", "dificil",
        "No célebre debate entre Kant e Benjamin Constant sobre 'O Suposto Direito de Mentir por Amor à Humanidade', Constant argumentou que 'dizer a verdade é um dever apenas perante quem tem direito à verdade'. Por que Kant rejeitou categoricamente essa proposta de flexibilização moral?",
        "Porque Kant possuía vínculos comerciais com empresas que fabricavam fechaduras de metal para residências urbanas.",
        "Porque Kant sustentava que a veracidade é um dever estrito incondicional perante a humanidade inteira; admitir exceções de conveniência anularia a universalidade da lei moral e destruiria a validade de todos os pactos jurídicos e contratos sociais.",
        "Porque Constant defendia que as leis de trânsito em cidades costeiras deveriam ser fiscalizadas por generais do exército.",
        "Porque as portas de madeira das casas de campo poderiam ser arrombadas facilmente por assaltantes armados com machados.",
        "Porque o assassino armado possuía certidões de registro expedidas por tribunais da cidade de Paris.",
        "B",
        "**Etapa 1:** Analisar a proposta de Constant: introduzir um critério relacional e condicional para o dever da verdade.\n**Etapa 2:** Concluir com a defesa inflexível do universalismo kantiano: mentir, mesmo para salvar um amigo, abre uma fenda fatal na lei moral; o dever da veracidade não admite relativização sem destruir a confiança na linguagem e a dignidade do ser racional."
    ))

    questoes_brutas.append((
        43, "EM13CHS605", "dificil",
        "Considere a Segunda Fórmula do Imperativo Categórico: 'Age de tal maneira que uses a humanidade, tanto na tua pessoa como na pessoa de qualquer outro, sempre e simultaneamente como um fim, e nunca simplesmente como um meio.' De que maneira essa formulação estabelece uma barreira intransponível contra o utilitarismo na distribuição de recursos em saúde pública?",
        "Determinando que os hospitais das grandes cidades atendam apenas pacientes que comprovem residência fixa no campo.",
        "Proibindo categoricamente que uma pessoa inocente ou um grupo minoritário vulnerável seja sacrificado, abandonado à morte ou usado em experimentos sem consentimento, mesmo que esse sacrifício traga a cura e salve a vida da imensa maioria da população.",
        "Exigindo que os médicos e enfermeiros utilizem uniformes confeccionados exclusivamente com tecidos de linho importado.",
        "Obrigando as famílias rurais a pagarem as consultas médicas por meio da doação de sacas de cevada colhida no verão.",
        "Determinando que os medicamentos farmacêuticos sejam produzidos apenas em dias de céu aberto sem nuvens escuras.",
        "B",
        "**Etapa 1:** Contrastar a lógica utilitarista da 'maximização do bem-estar coletivo' com a deontologia kantiana dos direitos absolutos.\n**Etapa 2:** Concluir com o princípio da dignidade inviolável: na ótica kantiana, uma vida humana não tem preço nem pode ser tratada como moeda de troca; sacrificar um inocente para salvar cinco é um crime hediondo que coisifica a pessoa humana."
    ))

    questoes_brutas.append((
        44, "EM13CHS502", "dificil",
        "Na Fundamentação da Metafísica dos Costumes, Kant afirma que 'a autonomia da vontade é o único princípio de todas as leis morais'. Como Kant demonstra que qualquer moral fundamentada na religião da recompensa celeste ou no medo do inferno constitui uma forma de alienação e Heteronomia?",
        "Provando que as escrituras sagradas foram impressas em papel de celulose importado de florestas da Ásia.",
        "Evidenciando que agir por medo do castigo divino ou por ganância da salvação eterna reduz a ação moral a um imperativo hipotético de cálculo egoísta de vantagens, no qual a vontade é escrava de forças exteriores e incapaz de agir pelo puro amor à justiça.",
        "Afirmando que os sacerdotes de templos religiosos deveriam pagar tributos fiscais sobre a venda de velas de cera.",
        "Sustentando que os fiéis que frequentam cerimônias noturnas sofrem de fadiga muscular acelerada no dia seguinte.",
        "Defendendo que as construções de capelas e mosteiros deveriam ser fiscalizadas por oficiais de guarnições militares.",
        "B",
        "**Etapa 1:** Analisar o conceito kantiano de heteronomia teológica: a vontade curvada a um poder externo por medo ou esperança de prêmio.\n**Etapa 2:** Concluir com a soberania da razão prática: a moralidade autêntica não precisa de chantagens transcendentais; ela brota da autonomia do sujeito racional que obedece à lei do dever pelo valor puro da dignidade e da justiça."
    ))

    questoes_brutas.append((
        45, "EM13CHS501", "dificil",
        "Analise o teste kantiano da universalização aplicado ao dilema do 'Avaro que se recusa a ajudar os miseráveis', sustentando a máxima: 'Cada um que cuide de si; não farei mal a ninguém, mas não moverei um dedo para socorrer quem passa fome'. Por que essa máxima é imoral para a razão prática?",
        "Porque as leis municipais de cidades portuárias obrigam a distribuição de pão fresco aos sábados.",
        "Porque, embora uma sociedade humana pudesse subsistir sob essa regra fria, é impossível 'querer' sem contradição volitiva que essa máxima seja universal, pois o indivíduo que hoje nega socorro inevitavelmente necessitará do auxílio e da solidariedade alheia em momentos futuros de fraqueza ou tragédia.",
        "Porque as moedas de prata guardadas em baús de ferro perdem o valor comercial com a mudança das marés.",
        "Porque os cidadãos miseráveis poderiam organizar competições esportivas que bloqueassem as vias públicas municipais.",
        "Porque os donos de armazéns de trigo são obrigados por decretos governamentais a doar cereais aos viajantes.",
        "B",
        "**Etapa 1:** Diferenciar as duas formas de contradição no imperativo categórico: contradição no conceito (como a mentira) e contradição na vontade.\n**Etapa 2:** Evidenciar que a máxima do egoísmo absoluto cai em contradição na vontade: como ser racional finito sujeito a acidentes, o homem não pode querer universalmente um mundo sem compaixão mútua, pois privaria a si mesmo de socorro indispensável."
    ))

    questoes_brutas.append((
        46, "EM13CHS605", "dificil",
        "Ao examinar o Tribunal Militar Internacional de Nuremberg (1945–1946) que julgou os criminosos de guerra nazistas, a defesa dos réus alegou o princípio jurídico da 'Obediência Devida' (eles apenas cumpriam as leis vigentes de seu Estado soberano). De que maneira a ética deontológica de Kant forneceu o fundamento filosófico para a condenação desses carrascos?",
        "Demonstrando que os tribunais militares devem cobrar custas judiciais em barras de ouro maciço dos réus condenados.",
        "Afirmando que a legalidade positiva formal de um Estado criminoso jamais pode anular a lei moral universal da dignidade humana: todo ser consciente tem o dever absoluto e intransferível de recusar a ordem de cometer atrocidades contra seus semelhantes.",
        "Provando que as leis da Alemanha nazista foram redigidas com tintas pretas de má qualidade que borravam os papéis.",
        "Sustentando que os juízes civis da cidade de Nuremberg deveriam ter suspendido as audiências durante o inverno.",
        "Defendendo que os generais militares deveriam ter sido perdoados caso comprovassem ter participado de feiras de artesanato.",
        "B",
        "**Etapa 1:** Contrastar o positivismo jurídico formalista cego (a lei é a lei) com o jusracionalismo deontológico kantiano.\n**Etapa 2:** Concluir com o legado de Nuremberg: acima das ordens dos tiranos vigora a dignidade inegociável da pessoa humana como fim em si; o indivíduo é moralmente autônomo e plenamente responsável por não se curvar a ordens genocidas."
    ))

    questoes_brutas.append((
        47, "EM13CHS502", "dificil",
        "Em sua obra À Paz Perpétua, Immanuel Kant formula o 'Imperativo da Hospitalidade Universal' como pilar do Direito Cosmopolita. Qual fundamento ético sustenta esse dever perante o estrangeiro que chega a uma terra desconhecida?",
        "A obrigação de que todos os imigrantes paguem taxas alfandegárias para construir monumentos aos governantes locais.",
        "A posse comum originária da superfície da Terra por toda a espécie humana, o que confere a qualquer pessoa o direito sagrado de não ser tratada como inimiga nem agredida com violência ao desembarcar pacificamente em outro país.",
        "A determinação de que os marinheiros de navios mercantes adotem as mesmas roupas dos cidadãos que moram na capital.",
        "O confisco de livros de literatura e tratados de filosofia estrangeiros que estejam guardados nas bagagens de viajantes.",
        "A exigência de que os turistas participem de corridas atléticas antes de receberem autorização para entrar nas cidades.",
        "B",
        "**Etapa 1:** Interpretar o conceito kantiano de posse comum da esfericidade do globo terrestre (*Besitz des Bodens*).\n**Etapa 2:** Concluir com a fundação do direito cosmopolita: como a Terra é finita e redonda, os seres humanos são constrangidos a coexistir em vizinhança mútua; a dignidade da pessoa humana impõe o dever moral e jurídico de acolhida pacífica e respeito ao forasteiro."
    ))

    questoes_brutas.append((
        48, "EM13CHS501", "dificil",
        "Considere a distinção entre 'Ação por Dever' e 'Ação por Inclinação'. Um cidadão bilionário doa milhões de reais para construir um hospital oncológico infantil exclusivamente porque sonha em ver seu nome gravado em letras douradas na fachada do prédio e ser aplaudido pelo público. Qual o juízo rigoroso de Kant sobre essa doação filantrópica?",
        "A doação constitui um crime penal de ostentação que deve ser punido com o confisco total de suas propriedades bancárias.",
        "A doação é uma ação de utilidade pública meritória e vantajosa para os enfermos, mas carece de valor moral genuíno e puro, pois seu princípio de ação foi o amor-próprio e a vaidade egoísta, e não o respeito incondicional ao dever moral.",
        "A doação garante automaticamente a beatitude espiritual do bilionário e o perdoa de todas as fraudes comerciais passadas.",
        "A doação deveria ser rejeitada pela diretoria do hospital para não ferir o orgulho de outros empresários da cidade.",
        "A doação comprova que os sentimentos empíricos são os únicos alicerces seguros para edificar a justiça coletiva no mundo.",
        "B",
        "**Etapa 1:** Avaliar os resultados práticos da ação benfeitora no plano fenomênico empírico (o hospital salva vidas).\n**Etapa 2:** Aplicar o critério deontológico do móbil interior: Kant distingue legalidade e eficácia de pureza moral; se a ação é movida pelo narcisismo e busca de glória, ela tem preço e vaidade, mas não o brilho incondicional da boa vontade pura."
    ))

    questoes_brutas.append((
        49, "EM13CHS605", "dificil",
        "Na reflexão contemporânea sobre a Inteligência Artificial Autônoma em armas de guerra letais (drones e robôs assassinos que decidem alvos humanos sem supervisão direta de operadores), de que maneira a Segunda Fórmula do Imperativo Categórico fundamenta a proibição internacional desses armamentos?",
        "Demonstrando que os circuitos eletrônicos desses aparelhos militares sofrem panes quando expostos a chuvas de granizo.",
        "Evidenciando que delegar a uma máquina desprovida de consciência a decisão de tirar uma vida humana reduz a pessoa a um algoritmo numérico descartável, violando a dignidade inalienável do ser humano e destruindo o Reino dos Fins.",
        "Exigindo que os drones de combate militar sejam pintados de azul claro para que os pássaros não colidam com suas asas.",
        "Afirmando que as empresas de tecnologia militar devem recolher taxas ambientais sobre o descarte de pilhas de lítio.",
        "Determinando que os generais do exército controlem os robôs de guerra utilizando cabos telefônicos subterrâneos.",
        "B",
        "**Etapa 1:** Analisar a coisificação radical da vida humana em sistemas de armas autônomas letais (LAWS).\n**Etapa 2:** Concluir com a deontologia kantiana dos direitos humanos: a dignidade humana exige que a decisão sobre a vida e a morte seja guiada pelo discernimento moral consciente e pela prestação de contas de um sujeito ético; máquinas operam por cálculo mecânico desprovido de moralidade."
    ))

    questoes_brutas.append((
        50, "EM13CHS502", "dificil",
        "Em sua obra Crítica da Razão Prática, Kant formula o conceito de 'Fato da Razão' (Factum der Vernunft). O que representa esse conceito na fundamentação da lei moral autônoma?",
        "A comprovação científica de que a matemática foi inventada por mercadores de seda da Península Itálica.",
        "A constatação imediata e inegável da presença da Lei Moral na consciência humana, que se impõe à razão com autoridade soberana incondicional sem precisar de demonstrações empíricas ou deduções exteriores.",
        "A exigência de que todos os cidadãos declarem fidelidade aos decretos governamentais em cerimônias cívicas.",
        "A certeza de que as tempestades de vento que ocorrem no mar Egeu são provocadas por deuses irritados.",
        "O hábito de registrar todos os nascimentos civis em placas de argila cozida guardadas em bibliotecas públicas.",
        "B",
        "**Etapa 1:** Compreender a natureza singular da lei moral em Kant: não é um fato empírico da física, mas um fato transcendental da própria razão prática pura.\n**Etapa 2:** Concluir que a consciência do dever não precisa de comprovação externa: mesmo o mais corrupto dos homens reconhece interiormente a voz da lei moral quando transgride a dignidade de seu semelhante."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Ao examinar a relação entre o Iluminismo (Aufklärung) e a Ética Deontológica, no célebre ensaio Resposta à Pergunta: O que é o Esclarecimento? (1784), Kant define a 'Menoridade' como:",
        "A fase biológica em que as crianças não possuem idade legal para assinar contratos de trabalho em fábricas.",
        "A incapacidade do homem de fazer uso do seu próprio entendimento sem a tutela e condução de outrem, quando a causa dessa dependência não reside na falta de inteligência, mas na falta de decisão e coragem moral para pensar por si mesmo.",
        "A obrigação cívica de obedecer a ordens emitidas por comandantes de frotas navais em travessias oceânicas.",
        "A falta de livros de história impressos com letras de tamanho legível para estudantes de escolas públicas.",
        "O período em que os governantes absolutistas da Europa proibiam a realização de casamentos civis no campo.",
        "B",
        "**Etapa 1:** Interpretar o lema iluminista de Kant: *Sapere Aude!* (Ousa saber! Tem a coragem de fazer uso do teu próprio entendimento!).\n**Etapa 2:** Conectar a menoridade à heteronomia moral: o homem torna-se livre e autônomo quando quebra as correntes da covardia e da tutela de líderes, sacerdotes ou costumes cegos, legislando sobre sua própria existência pela razão crítica."
    ))

    questoes_brutas.append((
        52, "EM13CHS605", "dificil",
        "Considere o problema contemporâneo da Exploração do Trabalho Infantil em lavouras de cacau e fábricas têxteis da cadeia global de valor de grandes corporações multinacionais. Sob a ótica da Segunda Fórmula do Imperativo Categórico, como essa exploração é caracterizada?",
        "Como um acidente operacional aceitável provocado pela falta de ferramentas mecânicas de colheita nas fazendas.",
        "Como a mais hedionda violação da dignidade humana, em que crianças vulneráveis são roubadas de seu desenvolvimento e reduzidas a meras engrenagens descartáveis de barateamento de custos e maximização de lucros corporativos.",
        "Como uma prática benéfica de aprendizado prático que deveria ser incentivada por ministérios da educação de países pobres.",
        "Como um problema puramente contábil que pode ser resolvido pelo aumento das taxas de juros cobradas por bancos centrais.",
        "Como uma consequência natural das variações climáticas que reduzem o rendimento de lavouras de cana-de-açúcar.",
        "B",
        "**Etapa 1:** Aplicar a proibição da instrumentalização humana de Kant ao trabalho infantil internacional.\n**Etapa 2:** Evidenciar a indignidade estrutural: crianças possuem valor absoluto e direito ao pleno florescimento humano; tratá-las como mão de obra barata para baratear produtos de luxo no Norte Global é usar o ser humano unicamente como meio de lucro."
    ))

    questoes_brutas.append((
        53, "EM13CHS501", "dificil",
        "Em que consiste a crítica contundente formulada pelo filósofo alemão G. W. F. Hegel contra o 'Formalismo Abstrato' da ética deontológica de Immanuel Kant?",
        "Hegel afirma que Kant desconhecia as regras de gramática da língua alemã utilizada em tratados universitários.",
        "Hegel argumenta que a ética kantiana do dever puro é vazia e puramente formal, desvinculada das instituições concretas, da história e dos laços comunitários da sociedade civil (a Eticidade ou Sittlichkeit), sendo incapaz de resolver dilemas morais reais sem cair no rigorismo impotente.",
        "Hegel sustenta que os filósofos da Prússia deveriam ter trabalhado como contadores em empresas de transporte fluvial.",
        "Hegel defende que a moralidade deve ser regulamentada exclusivamente por corporações de militares da corte de Berlim.",
        "Hegel comprova que as leis morais deixam de ter eficácia prática sempre que ocorrem geadas severas no campo.",
        "B",
        "**Etapa 1:** Compreender a distinção hegeliana entre *Moralität* (moralidade subjetiva abstrata de Kant) e *Sittlichkeit* (eticidade viva das instituições históricas: família, sociedade civil e Estado).\n**Etapa 2:** Concluir com a crítica de Hegel: o imperativo categórico é uma moldura formal sem conteúdo concreto; sem a historicidade e os costumes compartilhados de uma comunidade justa, o 'dever pelo dever' corre o risco de virar uma tautologia estéril."
    ))

    questoes_brutas.append((
        54, "EM13CHS502", "dificil",
        "Considere a máxima de um agente que decide colar em um exame vestibular concorrido sob a justificativa de que 'precisa muito da vaga para ajudar sua família'. Ao aplicar a fórmula da Lei Universal, por que essa ação se contradiz a si mesma?",
        "Porque as canetas esferográficas utilizadas nos vestibulares poderiam ficar sem tinta durante a redação.",
        "Porque, se todos os candidatos universalizassem a máxima de colar, o próprio exame vestibular perderia a sua função de avaliação e seria abolido pela sociedade, desfazendo a própria utilidade que o trapaceiro buscava explorar para si.",
        "Porque os fiscais de sala de aula são obrigados por lei a usar óculos de proteção contra reflexos de sol.",
        "Porque as carteiras de madeira das salas de aula seriam desgastadas com o peso de livros e mochilas dos alunos.",
        "Porque os resultados dos exames vestibulares são divulgados apenas no início do ano civil seguinte.",
        "B",
        "**Etapa 1:** Identificar o parasitismo moral do trapaceiro que formula a máxima particular da fraude.\n**Etapa 2:** Aplicar o teste de não contradição racional: a cola só funciona como vantagem se os outros candidatos forem honestos; ao universalizar a fraude, o próprio sistema do exame desmorona, provando a irracionalidade moral do ato."
    ))

    questoes_brutas.append((
        55, "EM13CHS605", "dificil",
        "No debate sobre a Bioética e o Tráfico de Órgãos Humanos, uma pessoa em extrema miséria deseja vender um de seus rins a um milionário para poder comprar uma casa para seus filhos. Como a moral deontológica kantiana julga essa transação comercial voluntária?",
        "Como uma troca de mercado justa e perfeita em que ambos os lados saem ganhando pelo livre acordo de vontades.",
        "Como uma ação imoral e violadora da dignidade humana, pois o indivíduo não tem o direito moral de dispor de partes de seu próprio corpo como mercadorias com preço, mutilando sua humanidade como meio de subsistência financeira.",
        "Como uma cerimônia cívica de solidariedade que deveria ser financiada por subsídios fiscais de governos estaduais.",
        "Como uma cirurgia hospitalar que deve ser realizada exclusivamente em navios atracados em águas internacionais.",
        "Como uma medida econômica recomendada para reduzir os índices de desemprego em regiões metropolitanas.",
        "B",
        "**Etapa 1:** Analisar o conceito kantiano dos deveres do homem para consigo mesmo enquanto ser moral dotado de dignidade.\n**Etapa 2:** Concluir com a recusa da mercantilização do corpo humano: mesmo com consentimento voluntário, vender partes do próprio corpo é rebaixar a pessoa a instrumento utilitário com preço; a dignidade proíbe a autoprossituição e a automutilação comercial."
    ))

    questoes_brutas.append((
        56, "EM13CHS501", "dificil",
        "Em sua obra Doutrina da Virtude (Metafísica dos Costumes, 1797), Kant distingue entre 'Deveres Perfeitos' e 'Deveres Imperfeitos'. Qual é a especificidade dos deveres perfeitos?",
        "Eles podem ser cumpridos apenas nos meses de primavera e dispensam o uso da razão prática deliberativa.",
        "São deveres negativos de obrigação estrita que proíbem categoricamente certas ações em qualquer circunstância (como a proibição do suicídio e da promessa falsa), não admitindo nenhuma margem de discricionariedade ou exceção.",
        "São deveres que exigem o pagamento de taxas bancárias adicionais para custear despesas de tribunais civis.",
        "São ordens militares aplicadas exclusivamente no treinamento de generais condecorados em guerras passadas.",
        "São recomendações poéticas que os jovens podem seguir voluntariamente caso tenham tempo livre durante o dia.",
        "B",
        "**Etapa 1:** Diferenciar deveres perfeitos (deveres jurídicos e estritos de não transgressão) de imperfeitos (deveres de virtude ampla, como cultivar talentos e ajudar necessitados).\n**Etapa 2:** Evidenciar que os deveres perfeitos não concedem folga ou ponderação: não matar, não roubar e não mentir são proibições absolutas e invioláveis perante a lei moral universal."
    ))

    questoes_brutas.append((
        57, "EM13CHS502", "dificil",
        "Ao examinar a tese kantiana da 'Incompatibilidade entre a Lei Moral e o Fanatismo Religioso', como Kant demonstra que aquele que afirma 'Deus me ordenou em um sonho a assassinar meu filho ou exterminar uma aldeia' comete um erro conceitual e moral gravíssimo?",
        "Porque as noites em que os sonhos ocorrem costumam ter quedas bruscas na temperatura do ar atmosférico.",
        "Porque nenhuma voz ou aparição sensível empírica pode contradizer a lei moral pura da razão (o mandamento incondicional de não assassinar inocentes); atribuir ordens imorais à divindade é fanatismo supersticioso e degradação da razão prática.",
        "Porque as certidões de nascimento dos filhos são emitidas por cartórios municipais com assinaturas formais de juízes.",
        "Porque os cidadãos adultos são obrigados a registrar suas armas de caça em repartições de segurança pública.",
        "Porque as construções de casas de campo devem obedecer a normas técnicas aprovadas por conselhos de engenharia.",
        "B",
        "**Etapa 1:** Analisar a subordinação da teologia à moral na filosofia crítica de Kant: a moralidade não deriva de comandos divinos arbitrários; ao contrário, reconhecemos Deus porque Ele é a expressão máxima da razão moral justa.\n**Etapa 2:** Concluir com a barreira contra o fanatismo: se uma suposta revelação mandar assassinar um ser inocente, a razão prática sabe com certeza absoluta que tal ordem não provém de Deus, pois a lei moral da dignidade é sagrada e inviolável."
    ))

    questoes_brutas.append((
        58, "EM13CHS605", "dificil",
        "No campo contemporâneo dos Direitos Fundamentais, a teoria kantiana do ser humano como 'Fim em Si Mesmo' é mobilizada pela Suprema Corte brasileira para declarar a inconstitucionalidade da revista íntima vexatória em presídios (obrigar visitantes a desnudarem-se diante de agentes). Qual é o fundamento filosófico dessa decisão?",
        "O receio de que as instalações sanitárias dos presídios estaduais sofram entupimentos frequentes na rede de água.",
        "A constatação de que a segurança pública não pode ser alcançada mediante a humilhação desmedida e a desumanização de corpos inocentes, devendo o Estado utilizar scanners tecnológicos que preservem a dignidade humana sem rebaixar a pessoa a objeto de devassa corporal invasiva.",
        "A comprovação de que as roupas de linho claro utilizadas pelos visitantes perdem a cor quando lavadas com sabão líquido.",
        "A determinação de que as visitas aos detentos em presídios de segurança máxima devam ocorrer apenas por meio de cartas escritas.",
        "O aumento dos custos financeiros com a compra de luvas descartáveis utilizadas pelos policiais penais durante as inspeções.",
        "B",
        "**Etapa 1:** Aplicar a segunda fórmula do imperativo categórico à colisão entre segurança institucional e direitos humanos.\n**Etapa 2:** Concluir com a jurisprudência da dignidade da pessoa humana: o combate ao crime não confere ao Estado a licença de aniquilar a dignidade e a honra corporal dos cidadãos; fins republicanos exigem meios eticamente legítimos."
    ))

    questoes_brutas.append((
        59, "EM13CHS501", "dificil",
        "Na Fundamentação da Metafísica dos Costumes, Kant afirma que 'a moralidade é a única condição que pode fazer de um ser racional um fim em si mesmo'. O que fundamenta a superioridade ética do ser humano em relação ao restante dos animais e objetos do cosmos físico?",
        "A habilidade física em correr com velocidade superior à de leopardos e leões da savana africana.",
        "A capacidade de transcender os instintos e apetites biológicos cegos para autodeterminar sua vontade por meio de princípios racionais universais de justiça e respeito mútuo, convertendo-se em sujeito ético responsável.",
        "A capacidade de armazenar moedas de prata em bancos comerciais para utilizá-las no comércio de importação.",
        "A prática de construir pontes de pedra sobre rios caudalosos para facilitar a passagem de carruagens militares.",
        "A facilidade em memorizar poemas épicos escritos em dialetos falados na Península Ibérica durante a Idade Média.",
        "B",
        "**Etapa 1:** Analisar a vocação moral humana em contraste com a pura causalidade mecânica que governa a fauna e a flora.\n**Etapa 2:** Concluir que a dignidade humana repousa na razão prática legisladora: o homem é o único ser capaz de agir contra seus próprios instintos e interesses egoístas em nome do dever e da justiça, fundando o Reino dos Fins."
    ))

    questoes_brutas.append((
        60, "EM13CHS502", "dificil",
        "Considere a célebre passagem de Kant na Crítica da Razão Prática: 'O dever! Nome sublime e grande, que nada conténs em ti de deleitável que encerre atrativo ou lisonja, mas exiges submissão, sem contudo nada ameaçares que excite no ânimo aversão natural ou terror para mover a vontade.' Qual síntese sobre a natureza do agir moral puro essa ode ao dever consagra?",
        "Que a moralidade exige que todos os seres humanos abandonem suas famílias para viverem isolados em mosteiros florestais.",
        "Que o dever moral autêntico não depende da chantagem do medo nem da sedução do prazer sensual, mas impõe-se à consciência humana pela força límpida de sua majestade racional, que desperta a reverência mais profunda da alma livre.",
        "Que as regras morais de uma sociedade devem ser aprovadas exclusivamente por generais comandantes de tropas militares.",
        "Que os jovens que estudam em colégios públicos devem decorar fórmulas de física mecânica antes de praticarem atos de caridade.",
        "Que o ser humano só consegue ser virtuoso caso possua patentes de oficial de marinha e grandes fortunas em ouro.",
        "B",
        "**Etapa 1:** Analisar o sentimento singular de 'Respeito' (*Achtung*) na filosofia kantiana: um sentimento produzido unicamente pela razão ao contemplar a grandeza da lei moral.\n**Etapa 2:** Concluir com a essência da deontologia: o dever kantiano não é tirania servil, mas a celebração mais sublime da liberdade e da nobreza humana; ao curvarmos nossa vontade perante o dever, elevamo-nos como soberanos legisladores no Reino dos Fins."
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
capitulo: "cap-11-deontologia-kantiana-imperativo-categorico"
objeto_de_conhecimento: "A Ética do Dever na Fundamentação da Metafísica dos Costumes; A Boa Vontade como Bem Incondicional; Ação por Dever vs. Ação Conforme ao Dever; O Imperativo Hipotético vs. O Imperativo Categórico; As Duas Fórmulas: A Universalidade da Máxima e a Dignidade Humana como Fim em Si Mesmo; Autonomia vs. Heteronomia da Vontade."
ebook_fonte: "em-fil-c11-deontologia-kantiana-imperativo-categorico.md"
habilidades: "EM13CHS101, EM13CHS501, EM13CHS502, EM13CHS605, H1, H2, H16, H17, H21"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: A Ética Deontológica e o Imperativo Categórico de Kant

"""

    corpo = header
    slug_cap = "cap-11-deontologia-kantiana-imperativo-categorico"

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

- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.
- CHAUÍ, Marilena. *Convite à Filosofia*. 13. ed. São Paulo: Ática, 2002.
- KANT, Immanuel. *Fundamentação da Metafísica dos Costumes*. Tradução de Paulo Quintela. Lisboa: Edições 70, 2007.
- MARCONDES, Danilo. *Textos Básicos de Ética: De Platão a Foucault*. 2. ed. Rio de Janeiro: Jorge Zahar, 2007.
- REALE, Giovanni; ANTISERI, Dario. *História da Filosofia: Do Romantismo ao Empiriocriticismo*. São Paulo: Paulus, 2007. v. 5.
- SCHNEEWIND, Jerome B. *A Invenção da Autonomia: Uma História da Filosofia Moral Moderna*. Tradução de Magda França Lopes. São Leopoldo: Editora Unisinos, 2001.
- WOOD, Allen W. *Kant's Ethical Thought*. Cambridge: Cambridge University Press, 1999.
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

    dest_rel = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-11-deontologia-kantiana-imperativo-categorico/ebooks/em-fil-c11-deontologia-kantiana-imperativo-categorico-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_path, dest_rel]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 11 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
