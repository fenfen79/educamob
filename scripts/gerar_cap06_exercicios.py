# -*- coding: utf-8 -*-
import os
import sys
import re
import subprocess
from collections import Counter

def balancear_questoes(questoes_brutas):
    alvo_letras = ['A', 'B', 'C', 'D', 'E'] * 12
    questoes_balanceadas = []

    for i, q in enumerate(questoes_brutas):
        num, hab, dif, enunc, a, b, c, d, e, gab_orig, res = q
        alvo = alvo_letras[i]
        
        alt_map = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}
        
        if gab_orig != alvo:
            texto_correto = alt_map[gab_orig]
            texto_outro = alt_map[alvo]
            alt_map[alvo] = texto_correto
            alt_map[gab_orig] = texto_outro
            
        novo_gab = alvo
        questoes_balanceadas.append((
            num, hab, dif, enunc,
            alt_map['A'], alt_map['B'], alt_map['C'], alt_map['D'], alt_map['E'],
            novo_gab, res
        ))
        
    return questoes_balanceadas

def gerar_cap06():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-06-epistemologia-moderna-racionalismo-empirismo/ebooks/em-fil-c06-epistemologia-moderna-racionalismo-empirismo-exercicios.md"
    temp_draft = "temp_draft.md"

    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "A passagem da Idade Média para a Idade Moderna abalou a visão geocêntrica tradicional de mundo. Qual ramo da filosofia passou a ocupar o centro das investigações intelectuais nesse período?",
        "A Teoria do Conhecimento, voltada a investigar a origem, os limites e a certeza do saber humano.",
        "A Astrologia mística, dedicada a adivinhar o destino das batalhas por meio do alinhamento das constelações.",
        "A Poética clássica, concentrada em ditar as métricas de sonetos para festividades palacianas.",
        "A Alquimia medieval, interessada em transformar metais comuns em barras de ouro puro.",
        "A Demonologia, voltada a catalogar os espíritos das florestas e cavernas.",
        "A",
        "Com o colapso do geocentrismo e da física aristotélica, a Teoria do Conhecimento (investigação sobre como conhecemos a verdade) assumiu o protagonismo filosófico moderno."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "René Descartes inaugurou a filosofia moderna propondo um método de purificação intelectual para encontrar uma verdade indubitável. Qual é o nome desse método?",
        "Ceticismo niilista definitivo.",
        "Dúvida Metódica e Hiperbólica.",
        "Dialética mitológica dos deuses.",
        "Iluminação divina involuntária.",
        "Retórica persuasiva sofística.",
        "B",
        "Descartes utilizou a Dúvida Metódica e Hiperbólica: uma ferramenta sistemática e deliberadamente radical para rejeitar tudo o que pudesse ser alvo da menor incerteza."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Qual é a primeira etapa do itinerário da dúvida cartesiana formulado no Discurso sobre o Método e nas Meditações Metafísicas?",
        "A suspeita sobre a existência de livros de história antiga.",
        "A constatação de que os sentidos corpóreos já nos enganaram em certas ocasiões e não merecem confiança cega.",
        "A certeza de que as equações da álgebra foram inventadas por generais romanos.",
        "A renúncia à capacidade humana de pensar e de formular raciocínios.",
        "O abandono da fé nas leis civis da monarquia francesa.",
        "B",
        "Descartes inicia notando que os sentidos corporais (visão, audição, tato) frequentemente erram diante de distâncias e ilusões de ótica, não servindo como fundamento inabalável."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "Ao formular o 'Argumento do Sonho', qual dúvida radical Descartes apresenta sobre a realidade imediata?",
        "Ele afirma que os sonhos revelam o futuro com exatidão matemática.",
        "Ele aponta que não há sinais seguros para distinguir com clareza a vigília lúcida do sono profundo.",
        "Ele sustenta que o ser humano só pensa verdadeiramente quando está dormindo.",
        "Ele defende que os animais sonham com teoremas de geometria no inverno.",
        "Ele comprova que as cores vistas nos sonhos pertencem a outro universo físico.",
        "B",
        "O argumento do sonho mostra que temos sonhos tão vívidos que parecem reais, tornando incerto se agora estamos realmente acordados ou apenas sonhando."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Para testar até mesmo a validade das verdades matemáticas na dúvida hiperbólica, Descartes formula qual hipótese?",
        "A hipótese de que o tempo corre de trás para a frente no espaço.",
        "A hipótese do Gênio Maligno, um ser astuto e poderoso que poderia nos induzir ao erro constante.",
        "A teoria de que as estrelas são feitas de gelo marinho refletindo luz de tochas.",
        "A tese de que os números foram proibidos pelos magistrados de Paris.",
        "A ideia de que a mente humana se desfaz quando fechamos os olhos.",
        "B",
        "A hipótese do Gênio Maligno funciona como uma ficção de pensamento extrema para questionar se até cálculos simples poderiam ser enganos impostos por um poder ardiloso."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "Qual é a primeira certeza inabalável descoberta por Descartes que resiste a todas as etapas da dúvida metódica?",
        "A certeza de que o Sol gira em torno da Terra.",
        "O 'Penso, logo existo' (Cogito, ergo sum): para duvidar ou ser enganado, é forçoso que eu seja algo pensante.",
        "A evidência palpável de que nosso corpo físico possui carne e ossos.",
        "A confiança irrestrita nos relatos históricos escritos na Idade Média.",
        "A comprovação de que os sonhos nunca se repetem durante a vida.",
        "B",
        "Mesmo que um gênio enganador exista, para me enganar eu preciso pensar; e se penso, existo necessariamente enquanto ser pensante (Cogito, ergo sum)."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "Na teoria cartesiana das ideias, como são chamadas as ideias colocadas na mente humana desde o nascimento, como a ideia de perfeição e de infinito?",
        "Ideias Fictícias inventadas pela imaginação.",
        "Ideias Adventícias vindas dos sentidos corpóreos.",
        "Ideias Inatas, impressas na razão pelo Criador.",
        "Ideias Passageiras decorrentes do cansaço físico.",
        "Ideias Emocionais aprendidas em peças de teatro.",
        "C",
        "As ideias inatas não derivam dos sentidos nem da imaginação; são marcas racionais originárias da mente, como os conceitos de infinito, perfeição e geometria."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "Descartes divide a realidade em duas substâncias distintas no dualismo psicofísico. Quais são elas?",
        "Substância Terrestre e Substância Celestial.",
        "Res Cogitans (coisa pensante, alma) e Res Extensa (coisa extensa, matéria corpórea).",
        "Água primordial e Fogo destrutivo.",
        "Luz invisível e Treva absoluta.",
        "Corpo atômico e Vácuo estelar.",
        "B",
        "O dualismo cartesiano separa a substância pensante (Res Cogitans, mente imaterial e livre) da substância extensa (Res Extensa, corpo material regido por leis mecânicas)."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Em oposição ao racionalismo, qual filósofo empirista britânico escreveu o Ensaio sobre o Entendimento Humano?",
        "Nicolau Maquiavel.",
        "John Locke.",
        "Baruch Spinoza.",
        "Gottfried Leibniz.",
        "Francis Bacon.",
        "B",
        "John Locke foi o principal formulador do empirismo clássico moderno em sua monumental obra Ensaio sobre o Entendimento Humano (1690)."
    ))

    questoes_brutas.append((
        10, "EM13CHS101", "basico",
        "Qual metáfora célebre John Locke utiliza para descrever o estado inicial da mente humana ao nascer?",
        "Uma biblioteca repleta de pergaminhos antigos de sabedoria.",
        "Uma Tábula Rasa (folha em branco sem nenhuma inscrição prévia).",
        "Um espelho mágico capaz de refletir o futuro das nações.",
        "Uma semente dourada que já contém árvores em miniatura.",
        "Um cofre trancado com segredos matemáticos da criação.",
        "B",
        "Locke afirma que a mente é como uma folha em branco (Tábula Rasa), sobre a qual a experiência concreta e sensorial escreve todo o conhecimento humano."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Para John Locke, de onde provêm todas as ideias simples que preenchem a mente humana?",
        "De lembranças de vidas passadas na alma imortal.",
        "Da Experiência, dividida em Sensação (sentidos externos) e Reflexão (operações internas da mente).",
        "De decretos promulgados pelos monarcas ingleses no parlamento.",
        "De revelações místicas concedidas aos profetas durante o sono.",
        "De cálculos matemáticos desenvolvidos sem ver o mundo exterior.",
        "B",
        "Segundo Locke, a experiência é a fonte exclusiva de todo o saber, manifestando-se pela sensação (estímulos do mundo externo) e reflexão (percepção das operações mentais)."
    ))

    questoes_brutas.append((
        12, "EM13CHS101", "basico",
        "Na distinção de John Locke, o que são as chamadas 'Qualidades Primárias' de um corpo físico?",
        "A cor, o cheiro agradável e o sabor doce percebidos pelo paladar.",
        "Propriedades inseparáveis do próprio corpo físico, como extensão, figura, solidez, movimento e número.",
        "As opiniões morais aprovadas pelos vizinhos em um bairro comercial.",
        "O valor monetário cobrado pela venda daquele objeto na feira.",
        "Os sentimentos de tristeza ou alegria despertados no observador.",
        "B",
        "Qualidades primárias pertencem aos próprios corpos (tamanho, formato, número, solidez), enquanto as secundárias (cor, som, sabor) dependem da percepção do sujeito."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Qual filósofo escocês aprofundou o empirismo até as suas últimas consequências na Investigação sobre o Entendimento Humano?",
        "Francis Bacon.",
        "David Hume.",
        "Thomas Hobbes.",
        "René Descartes.",
        "Immanuel Kant.",
        "B",
        "David Hume levou o empirismo a um rigoroso exame crítico, formulando uma teoria cética moderada sobre a causalidade e a natureza humana."
    ))

    questoes_brutas.append((
        14, "EM13CHS101", "basico",
        "Na teoria das percepções de David Hume, qual é a diferença entre 'Impressões' e 'Ideias'?",
        "As impressões são pensamentos fracos de sono, e as ideias são visões luminosas de anjos.",
        "As impressões são percepções vívidas e imediatas da experiência; as ideias são cópias pálidas e imagens fracas dessas impressões na memória.",
        "As ideias são dadas por Deus ao nascer, e as impressões são inventadas por pintores.",
        "Não existe diferença para Hume, sendo dois nomes para o mesmo fenômeno biológico.",
        "As impressões pertencem apenas aos animais e as ideias são exclusivas dos reis da Europa.",
        "B",
        "Hume distingue impressões (dados diretos, fortes e vívidos da sensação) de ideias (lembranças menos vívidas que copiam as impressões na mente)."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "O que estabelece o 'Princípio da Cópia' formulado por David Hume na análise do entendimento?",
        "Que todos os livros devem ser transcritos à mão por estudantes de direito.",
        "Que toda ideia legítima na mente é uma cópia direta ou indireta de uma impressão sensível anterior.",
        "Que a arte da pintura consiste em imitar estátuas de mármore feitas na Grécia antiga.",
        "Que as leis do governo copiam as regras das ordens religiosas medievais.",
        "Que os animais copiam os hábitos humanos ao conviverem em fazendas rurais.",
        "B",
        "Pelo Princípio da Cópia, qualquer conceito que não possa ser rastreado até uma impressão sensível original correspondente deve ser rejeitado como ficção sem fundamento."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Qual noção fundamental da ciência moderna foi alvo da crítica mais contundente de David Hume?",
        "O princípio do cálculo de áreas geométricas planas.",
        "O Princípio da Causalidade necessária entre dois eventos sucessivos.",
        "A tabela periódica dos elementos químicos da natureza.",
        "A lei biológica da circulação do sangue nos mamíferos.",
        "A teoria da gravitação descrita em poemas latinos.",
        "B",
        "Hume demonstrou que a conexão causal necessária não pode ser observada pelos sentidos nem demonstrada por dedução lógica pura, abalando a certeza da ciência."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Segundo David Hume, por que acreditamos com tanta certeza de que o Sol nascerá amanhã de manhã?",
        "Porque vimos equações que obrigam o Sol a obedecer às leis humanas.",
        "Por causa do Hábito ou Costume psicológico gerado pela repetição constante do fenômeno no passado.",
        "Porque os deuses olímpicos fizeram uma promessa solene aos marinheiros do mar Egeu.",
        "Porque o fogo do Sol depende de combustíveis renovados a cada meia-noite pelos astrônomos.",
        "Porque os animais da fazenda cantam no horizonte antes do raiar do dia.",
        "B",
        "Para Hume, nossa crença na regularidade da natureza e no nascer do sol repousa no hábito psicológico adquirido pela experiência reiterada, e não em necessidade lógica absoluta."
    ))

    questoes_brutas.append((
        18, "EM13CHS101", "basico",
        "Em um jogo de bilhar, ao vermos a bola branca se mover e bater na bola preta, o que nossa experiência sensível observa de fato, segundo David Hume?",
        "O poder invisível da gravidade fluindo de uma bola para a outra.",
        "Apenas a contiguidade espacial e a sucessão temporal entre dois movimentos, mas nunca a conexão causal invisível.",
        "A vontade consciente da bola de madeira em empurrar sua companheira de jogo.",
        "A alma imaterial da mesa de bilhar atuando como juíza da pontuação.",
        "A corrupção moral do jogador que calculou a tacada errada na partida.",
        "B",
        "Hume aponta que vemos a bola A se mover e, logo em seguida, a bola B se deslocar; jamais vemos ou sentimos pelos sentidos a suposta força necessária que as une."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Qual corrente filosófica sustenta que a Razão humana é a fonte primordial, confiável e soberana do conhecimento verdadeiro sobre a realidade?",
        "O Racionalismo.",
        "O Empirismo radical.",
        "O Hedonismo vulgar.",
        "O Cinismo socrático.",
        "O Vitalismo mitológico.",
        "A",
        "O racionalismo defende a primazia da razão e do raciocínio dedutivo lógico como via autêntica para atingir certezas universais e necessárias."
    ))

    questoes_brutas.append((
        20, "EM13CHS101", "basico",
        "E qual corrente filosófica oposta afirma categoricamente que todos os nossos saberes e ideias procedem exclusivamente da Experiência e dos sentidos?",
        "O Idealismo platônico.",
        "O Empirismo.",
        "O Ceticismo niilista absoluto.",
        "O Dogmatismo religioso escolástico.",
        "A Sofística retórica.",
        "B",
        "O empirismo estabelece que não há ideias inatas e que todo o conteúdo mental é adquirido pela experiência empírica através dos sentidos e da percepção."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "A dúvida metódica de René Descartes distingue-se categoricamente do ceticismo pirrônico da Antiguidade grega porque:",
        "O ceticismo duvida por prazer esportivo para vencer debates retóricos na praça pública.",
        "A dúvida cartesiana não é um fim em si mesma, mas um instrumento temporário para alcançar uma certeza firme e inabalável.",
        "Descartes acreditava que os deuses castigavam com doenças os filósofos que fizessem perguntas.",
        "O ceticismo grego defendia a queima de todos os livros didáticos produzidos nas cidades da Jônia.",
        "Descartes usava a dúvida para defender o retorno da astronomia geocêntrica dos babilônios.",
        "B",
        "A dúvida de Descartes é metódica: visa expurgar o erro para construir um fundamento indubitável, enquanto o ceticismo clássico suspendia o juízo permanentemente."
    ))

    questoes_brutas.append((
        22, "EM13CHS101", "intermediario",
        "No famoso exemplo do pedaço de cera nas Meditações Metafísicas, Descartes observa que ao aproximar a cera do fogo, sua cor, cheiro e forma mudam completamente. O que esse experimento mental prova?",
        "Que a cera deixou de existir e se transformou em cinzas frias sem valor.",
        "Que a substância da cera não é conhecida pelas sensações mutáveis, mas apreendida pelo intelecto racional puro.",
        "Que os artesãos que fabricam velas devem ser proibidos de trabalhar perto de lareiras acesas.",
        "Que o fogo possui uma inteligência divina superior à mente dos sábios.",
        "Que as propriedades físicas dos corpos desaparecem durante a noite nas casas francesas.",
        "B",
        "Todas as sensações (dureza, cheiro, cor) se alteram com o calor, mas sabemos que a cera permanece a mesma cera; logo, o conhecimento de sua essência é obra do intelecto, não dos sentidos."
    ))

    questoes_brutas.append((
        23, "EM13CHS101", "intermediario",
        "Como John Locke refuta a tese racionalista de que os seres humanos possuem ideias inatas universais (como o princípio de não-contradição)?",
        "Mostrando que crianças, pessoas sem instrução formal e povos de diferentes culturas desconhecem essas formulações lógicas abstratas ao nascer.",
        "Provando que as ideias inatas só aparecem na mente de indivíduos que completam quarenta anos de idade.",
        "Defendendo que as fórmulas matemáticas mudam toda vez que um rei assina um armistício militar.",
        "Afirmando que a memória humana é incapaz de guardar mais de dez palavras diferentes por dia.",
        "Sustentando que os animais da floresta possuem mais ideias inatas do que os estudantes universitários.",
        "A",
        "Locke argumenta que se houvesse ideias inatas universais, crianças e povos não letrados as conheceriam espontaneamente desde o berço, o que a realidade empírica desmente."
    ))

    questoes_brutas.append((
        24, "EM13CHS101", "intermediario",
        "Na crítica de David Hume à ideia de substância ou de 'Eu' (identidade pessoal permanente), qual conclusão cética o pensador escocês sustenta?",
        "Que a alma humana é uma esfera sólida de ferro localizada atrás dos olhos.",
        "Que nunca percebemos um 'Eu' fixo e estável, mas apenas um feixe contínuo e veloz de percepções mutáveis em fluxo constante.",
        "Que as pessoas esquecem suas identidades toda vez que viajam de navio para outros continentes.",
        "Que o governo municipal tem o direito de confiscar a certidão de nascimento de quem duvida da fé.",
        "Que a mente humana é uma criação mágica de poetas trágicos da Grécia clássica.",
        "B",
        "Ao examinar a própria mente, Hume encontra apenas percepções particulares passageiras (calor, frio, dor, alegria), nunca o suposto sujeito substancial imutável (a 'mente feixe')."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Por que o dualismo cartesiano de mente e corpo (Res Cogitans vs. Res Extensa) gerou um grande enigma para a ciência e a filosofia modernas?",
        "Porque as leis da França proibiam que cirurgiões examinassem corpos de soldados falecidos.",
        "Porque tornou difícil explicar como uma substância puramente espiritual e imaterial pode interagir e mover um corpo material mecânico.",
        "Porque Descartes afirmou que os animais possuíam alma racional superior à dos reis europeus.",
        "Porque a Igreja determinou que o corpo humano não podia ser desenhado em manuais de anatomia.",
        "Porque os telescópios ópticos não conseguiam enxergar a órbita das luas de Júpiter no espaço.",
        "B",
        "Se a mente é imaterial e sem extensão, e o corpo é pura matéria física com peso e volume, como eles se comunicam fisicamente para permitir ações voluntárias (o problema mente-corpo)?"
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Ao analisar a causalidade, David Hume afirma que a afirmação 'o Sol nascerá amanhã' não é uma verdade necessária da razão como 'dois mais dois são quatro'. Qual é a justificativa de Hume?",
        "Porque o sol pode ser apagado por tempestades de poeira no deserto do Saara a qualquer instante.",
        "Porque a negação de que o Sol nascerá não implica contradição lógica; é concebível sem absurdo que o Sol não nasça amanhã.",
        "Porque as leis da física foram redigidas por imperadores persas que cometeram erros de cálculo.",
        "Porque a rotação da Terra depende da força muscular dos remadores que navegam pelo oceano.",
        "Porque o calendário anual foi alterado por decretos dos papas em Roma no século XVI.",
        "B",
        "Negar uma verdade de fato (o Sol não nascer amanhã) é uma proposição perfeitamente compreensível sem contradição lógica, ao contrário de negar uma relação de ideias matemática."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "No debate sobre Inteligência Artificial contemporânea e testes de raciocínio lógico em máquinas, qual concepção cartesiana é diretamente colocada em xeque?",
        "A crença de que os planetas do sistema solar giram em círculos perfeitos no céu.",
        "A tese de que processos intelectuais e de linguagem pertencem exclusivamente a uma alma imaterial descolada de suportes materiais.",
        "A teoria de que as árvores não respiram durante as noites de tempestade no inverno.",
        "A afirmação de que a matemática foi inventada por mercadores da cidade de Veneza.",
        "A defesa de que o cérebro humano não possui células nervosas conectadas entre si.",
        "B",
        "A IA moderna demonstra que operações complexas de linguagem e raciocínio lógico podem emergir de processamentos físicos de circuitos eletrônicos materiais, desafiando o dualismo estrito."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "Na distinção de David Hume entre 'Relações de Ideias' e 'Questões de Fato', qual característica define as Relações de Ideias?",
        "Dependem de observações empíricas colhidas com instrumentos de medição em laboratório.",
        "São verdades demonstrativamente certas e intuitivas (como na matemática), cuja negação implica contradição lógica direta.",
        "Podem ser modificadas sempre que uma lei municipal for votada pelos vereadores da cidade.",
        "Pertencem apenas aos povos antigos que viviam na Mesopotâmia antes da escrita alfabética.",
        "São comprovadas por meio de viagens marítimas ao redor do continente africano.",
        "B",
        "As relações de ideias (aritmética, álgebra, geometria) operam pela pura razão e pelo princípio de não-contradição, sendo verdades necessárias e independentes dos fatos do mundo."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Para John Locke, como se formam as chamadas 'Ideias Complexas' na mente humana (como as ideias de beleza, gratidão ou exército)?",
        "Brotam espontaneamente dos sonhos quando a pessoa atinge a maturidade biológica.",
        "São construídas pelo intelecto ativo ao combinar, comparar e abstrair múltiplas ideias simples recebidas pela experiência.",
        "São ensinadas por anjos que sussurram fórmulas secretas durante a madrugada.",
        "São herdadas dos genes dos antepassados que lutaram em guerras medievais.",
        "São retiradas de tábuas de pedra encontradas em escavações arqueológicas no Egito.",
        "B",
        "A mente humana é passiva ao receber ideias simples da sensação, mas torna-se ativa ao combinar, relacionar e abstrair essas ideias simples para compor ideias complexas."
    ))

    questoes_brutas.append((
        30, "EM13CHS101", "intermediario",
        "Ao rebater a tese empirista de que a mente é passiva na recepção dos dados, o filósofo racionalista Leibniz formulou a célebre ressalva: 'Nada está no intelecto sem ter passado antes pelos sentidos, exceto...'",
        "...o próprio intelecto com suas estruturas racionais inatas.",
        "...a força física dos músculos que sustentam o crânio.",
        "...o ar que respiramos durante as caminhadas matinais.",
        "...as leis escritas em latim nos códigos jurídicos.",
        "...o ouro guardado nos cofres dos banqueiros de Amsterdã.",
        "A",
        "Leibniz sintetiza a posição racionalista: os sentidos fornecem materiais brutos, mas a própria mente (o intelecto e suas categorias) já é ativa e inata para organizá-los."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "O ceticismo moderado de David Hume teve um impacto demolidor sobre as pretensões dogmáticas da metafísica porque demonstrou que:",
        "As fórmulas da geometria de Euclides continham erros grosseiros de cálculo numérico.",
        "Conceitos transcendentais que não possuem nenhuma impressão sensível correspondente carecem de validade cognitiva comprovável.",
        "Os cientistas devem abandonar as pesquisas astronômicas em favor da leitura de mitos poéticos.",
        "A verdade depende de votações orais realizadas pelos trabalhadores das fábricas de tecidos.",
        "Os aparelhos de laboratório foram inventados para iludir os estudantes de medicina.",
        "B",
        "Hume adverte que se pegarmos um livro de teologia ou metafísica escolástica que não contenha raciocínio matemático abstrato nem evidência experimental empírica, devemos atirá-lo ao fogo."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Ao examinar a ideia de Deus nas Meditações Metafísicas, Descartes argumenta que um ser finito e imperfeito como o homem jamais poderia ter inventado a ideia de um ser sumamente perfeito e infinito. Qual conclusão ele extrai disso?",
        "Que a ideia de Deus foi comprada de mercadores estrangeiros que viajavam pelo mar Mediterrâneo.",
        "Que a ideia de perfeição e infinitude é uma marca inata colocada na mente pelo próprio Deus real que existe fora de nós.",
        "Que o conceito de infinito é uma ilusão matemática passageira que deve ser descartada pelos cientistas.",
        "Que as pessoas imperfeitas não têm permissão para estudar geometria nas faculdades de medicina.",
        "Que os deuses das antigas mitologias gregas retornaram para governar as florestas da França.",
        "B",
        "O argumento cartesiano da marca do artífice: o efeito (a ideia de infinito e perfeição na mente) não pode ter menos realidade do que a causa; logo, um Deus infinito real existe e a imprimiu em nós."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Como a economia comportamental contemporânea (de autores como Daniel Kahneman) dialoga com a teoria do hábito formulada por David Hume?",
        "Negando que os seres humanos tenham órgãos dos sentidos para perceber o valor das moedas.",
        "Confirmando que a maioria das decisões humanas cotidianas apoia-se em atalhos mentais rápidos e hábitos automáticos, e não em cálculos lógicos perfeitos.",
        "Defendendo que a riqueza de um país depende exclusivamente de oferendas religiosas feitas nos portos.",
        "Provando que os computadores digitais operam impulsionados por sentimentos de raiva e piedade.",
        "Mostrando que o comércio exterior deve ser proibido para preservar o silêncio nas cidades industriais.",
        "B",
        "A economia comportamental comprova o insight de Hume: a mente humana guia-se prevalentemente pelo hábito e heurísticas associativas rápidas diante de regularidades empíricas."
    ))

    questoes_brutas.append((
        34, "EM13CHS101", "intermediario",
        "No método cartesiano exposto no Discurso sobre o Método, qual regra estabelece que se deve decompor cada dificuldade encontrada no maior número possível de partes simples para resolvê-la?",
        "A Regra da Evidência indubitável.",
        "A Regra da Análise (divisão dos problemas complexos em partes menores).",
        "A Regra da Síntese ordenadora progressiva.",
        "A Regra da Enumeração ou revisão completa.",
        "A Regra da Dúvida definitiva sobre as leis civis.",
        "B",
        "A regra da análise consiste em dividir cada dificuldade em tantas partes quantas forem possíveis e necessárias para melhor resolvê-las a partir do mais simples."
    ))

    questoes_brutas.append((
        35, "EM13CHS101", "intermediario",
        "Em contraposição ao mecanicismo determinista dos corpos físicos (Res Extensa), como Descartes preserva a responsabilidade moral e a dignidade do ser humano?",
        "Atribuindo aos seres humanos uma força muscular superior à dos animais selvagens da selva.",
        "Garantindo que a alma racional (Res Cogitans) é livre e dotada de vontade consciente, escapando às leis mecânicas rígidas da matéria física.",
        "Afirmando que o homem recebe salários proporcionais ao número de orações que decora nas igrejas.",
        "Defendendo que os reis de sangue nobre não precisam prestar contas de seus atos a ninguém.",
        "Proibindo o estudo da anatomia humana para manter em segredo os ossos do esqueleto.",
        "B",
        "Ao separar a mente imaterial da matéria, Descartes preserva o livre-arbítrio e a autonomia moral da pessoa humana, impedindo que ela seja tratada como mera máquina biológica."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Na terminologia de David Hume, a associação de ideias na mente humana opera por meio de quais três princípios universais de ligação psicológica?",
        "Terra, Água e Fogo celestial.",
        "Semelhança, Contiguidade no tempo/espaço e Causa e Efeito.",
        "Compra, Venda e Empréstimo com juros bancários.",
        "Nascimento, Casamento e Sepultamento em jazigos familiares.",
        "Cálculo, Medição e Desenho de plantas de cidades.",
        "B",
        "Hume identifica três princípios de associação de ideias que unem pensamentos na imaginação: semelhança (um retrato faz lembrar o original), contiguidade e causalidade."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Qual é a função do Deus sumamente bom e veraz na arquitetura filosófica de René Descartes após a descoberta do Cogito?",
        "Ele funciona como um juiz punitivo que castiga os pecados dos cidadãos franceses no além-túmulo.",
        "Ele é a garantia de que as ideias claras e distintas do intelecto sobre o mundo exterior correspondem à realidade real, afastando a hipótese do gênio maligno.",
        "Ele é uma metáfora literária inventada por poetas trágicos para agradar aos bispos da corte.",
        "Ele comanda os batalhões de cavalaria que defendiam as fronteiras das cidades costeiras da Europa.",
        "Ele proíbe que os astrônomos utilizem telescópios de vidro para examinar os anéis de Saturno.",
        "B",
        "Para Descartes, Deus não é enganador; sua veracidade infinita garante que tudo aquilo que a razão concebe com clareza e distinção é real e confiável no mundo fático."
    ))

    questoes_brutas.append((
        38, "EM13CHS101", "intermediario",
        "Quando John Locke formula sua teoria política no Segundo Tratado sobre o Governo Civil, como sua posição filosófica sobre o conhecimento dialoga com seus ideais liberais?",
        "Rejeita a autoridade divina inata dos monarcas absolutistas, defendendo que a legitimidade do poder nasce do consentimento racional dos governados.",
        "Afirma que os reis nascem com conhecimentos inatos especiais que os colocam acima de qualquer lei moral.",
        "Defende a escravização dos trabalhadores rurais que não sabem ler nem escrever em língua inglesa.",
        "Exige que todas as decisões do parlamento sejam tomadas por meio de sorteios de cartas de baralho.",
        "Propõe a queima de todos os contratos comerciais para abolir o uso de moedas de prata no país.",
        "A",
        "Ao negar ideias inatas na mente humana, Locke desmonta a doutrina do direito divino dos reis: ninguém nasce com mandato sagrado inato para mandar; a autoridade depende de pacto cívico consentido."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "David Hume formula o chamado 'Problema da Indução', demonstrando que saltar de premissas particulares para uma lei universal necessária é logicamente injustificável porque:",
        "Os cientistas de laboratório utilizam microscópios antigos com lentes de aumento riscadas.",
        "Mesmo que tenhamos observado milhões de cisnes brancos no passado, isso não garante com necessidade lógica de que o próximo cisne observado não possa ser negro.",
        "As leis da astronomia só valem para cidades construídas perto do mar e com portos abertos.",
        "Os cisnes selvagens voam mais rápido durante a noite do que os pássaros domésticos da fazenda.",
        "O parlamento inglês aprovou uma lei que proíbe o registro de animais de plumagem escura no país.",
        "B",
        "A indução parte do observado para o não observado; não há justificativa puramente lógica para garantir que o futuro repetirá o passado de modo invariável (o problema da indução)."
    ))

    questoes_brutas.append((
        40, "EM13CHS101", "intermediario",
        "Em síntese, o embate secular entre o Racionalismo e o Empirismo na modernidade colocou frente a frente duas fontes antagônicas de legitimação da verdade, a saber:",
        "A revelação mística de profetas antigos versus os decretos administrativos de magistrados municipais.",
        "A dedução apriorística fundada na evidência lógica da Razão pura versus a indução e a validação a posteriori calcadas na Experiência sensível.",
        "A astrologia babilônica de mapas estelares versus a alquimia mineral de oficinas subterrâneas.",
        "A arte da oratória militar de generais condecorados versus o comércio marítimo de tecidos asiáticos.",
        "A leitura de romances medievais de cavalaria versus o treinamento físico de ginastas nos jogos gregos.",
        "B",
        "O racionalismo priorizou a dedução a priori a partir de primeiros princípios racionais evidentes; o empirismo priorizou a observação sensível e a indução a posteriori como critério de verdade."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS103", "dificil",
        "Analise a passagem das Meditações Metafísicas: 'Notei há alguns anos que admitira muitas falsas opiniões como verdadeiras e que o que fundara sobre princípios tão mal assegurados só podia ser muito duvidoso e incerto.' Como essa atitude cartesiana funda uma nova postura crítica para a ciência moderna?",
        "Negando a possibilidade de qualquer certeza científica e adotando o desespero existencial perene.",
        "Estabelecendo a exigência metodológica de examinar criticamente as premissas herdadas da tradição e fundar o conhecimento sobre demonstrações racionais rigorosamente verificadas.",
        "Proibindo o uso de ferramentas de cálculo nas academias científicas de Paris e Londres.",
        "Submetendo as pesquisas astronômicas ao crivo final de adivinhos e astrólogos da corte francesa.",
        "Defendendo que as opiniões populares recolhidas nas ruas são superiores a qualquer teorema matemático.",
        "B",
        "**Etapa 1:** Interpretar o diagnóstico cartesiano de ruptura com o dogmatismo escolástico medieval.\n**Etapa 2:** Concluir que a atitude crítica e a exigência de justificação racional das premissas inauguram a postura do método científico moderno, que recusa a autoridade cega da tradição."
    ))

    questoes_brutas.append((
        42, "EM13CHS103", "dificil",
        "Ao examinar a hipótese do Gênio Maligno, nota-se que ela leva a dúvida metódica a um limite radical. Por que mesmo esse ser malévolo todo-poderoso é incapaz de derrubar a certeza do 'Penso, logo existo'?",
        "Porque o gênio maligno tem medo de tempestades de relâmpagos e foge da mente do filósofo.",
        "Porque para que o gênio me engane sistematicamente, faz-se estritamente necessário que eu exista enquanto sujeito enganado que pensa e duvida de algo.",
        "Porque os jurados do tribunal de Paris proibiram o gênio de se manifestar em livros impressos.",
        "Porque as verdades matemáticas têm o poder físico de destruir qualquer entidade espiritual.",
        "Porque o sono profundo impede a ação de forças mágicas sobre o corpo biológico dos seres humanos.",
        "B",
        "**Etapa 1:** Analisar a condição formal de possibilidade do ato de ser enganado por uma força ardilosa.\n**Etapa 2:** Reconhecer que o ato de ser induzido ao erro pressupõe necessariamente a existência do ser que erra e pensa; logo, enquanto penso que sou enganado, existo com certeza absoluta."
    ))

    questoes_brutas.append((
        43, "EM13CHS105", "dificil",
        "Na obra Ensaio sobre o Entendimento Humano, John Locke afirma: 'Suponhamos, pois, que a mente é, como dizemos, um papel em branco, sem nenhuma letra, sem nenhuma ideia. Como ela vem a ser preenchida? A isso respondo com uma só palavra: da experiência.' Qual impacto essa formulação sobre a mente provocou sobre a pedagogia e a política do Iluminismo?",
        "Reforçou a tese de que os nobres de sangue real possuem inteligência inata geneticamente superior aos camponeses.",
        "Democratizou a compreensão do potencial humano: se todos nascem como uma tábula rasa, as diferenças de talento e sabedoria decorrem da educação e do ambiente social, abrindo caminho para a defesa da escola universal e da igualdade cívica.",
        "Provou que o cérebro das crianças deve ser submetido a cirurgias para apagar memórias familiares antes de aprender ciências.",
        "Determinou que o ensino de humanidades fosse abolido em todas as universidades do Reino Unido.",
        "Impediu que os filhos de trabalhadores manuais ingressassem em bibliotecas públicas municipais.",
        "B",
        "**Etapa 1:** Compreender o alcance da metáfora da tábula rasa em contraposição ao inatismo das elites aristocráticas.\n**Etapa 2:** Concluir que, ao nivelar a origem da mente de todos os seres humanos à experiência recebida, Locke funda a base teórica iluminista para a emancipação pela educação universal e a igualdade de oportunidades."
    ))

    questoes_brutas.append((
        44, "EM13CHS103", "dificil",
        "A crítica demolidora de David Hume ao conceito de causalidade provocou um profundo choque na ciência do século XVIII. Qual dilema essa crítica colocou perante os físicos que defendiam as leis de Newton como verdades eternas e imutáveis?",
        "Provou que os corpos pesados caem para cima quando lançados no ar em dias de vento forte.",
        "Evidenciou que as chamadas 'leis causais da natureza' não possuem necessidade lógica demonstrável a priori, consistindo em generalizações probabilísticas fundadas na expectativa do hábito psicológico.",
        "Comprovou que os telescópios ópticos invertem as posições das estrelas no firmamento por defeito das lentes.",
        "Obrigou os astrônomos a renunciarem ao uso do cálculo diferencial inventado por Newton e Leibniz.",
        "Demonstrou que a gravidade só atua sobre objetos de metal, dispensando corpos de madeira e pedra.",
        "B",
        "**Etapa 1:** Analisar a ruptura entre necessidade lógica a priori e conexão empírica factual demonstrada por Hume.\n**Etapa 2:** Reconhecer que, desprovida de demonstração apriorística, a causalidade física torna-se uma crença indutiva empírica muito provável, abalando a pretensão dogmática de certezas imutáveis absolutas na ciência."
    ))

    questoes_brutas.append((
        45, "EM13CHS105", "dificil",
        "Considere as pesquisas atuais em neurociência e ciências cognitivas que investigam como o cérebro processa informações sensoriais e cria modelos mentais de antecipação do mundo. Como esse campo contemporâneo dialoga com as teses de David Hume sobre o hábito e a causalidade?",
        "Negando que o cérebro humano tenha conexões sinápticas ativas durante a infância.",
        "Reforçando a tese humeana de que o cérebro opera como uma máquina de predição estatística, utilizando correlações passadas de estímulos sensoriais para antecipar acontecimentos futuros por associação e hábito.",
        "Afirmando que a memória humana funciona guardando pergaminhos escritos em latim na base do cerebelo.",
        "Demonstrando que os neurônios cerebrais são formados exclusivamente por substâncias mágicas imateriais.",
        "Provando que as ilusões de ótica decorrem de encantamentos pronunciados por oradores teatrais.",
        "B",
        "**Etapa 1:** Associar a teoria do hábito e associação de percepções de Hume com o conceito neurocientífico de 'cérebro preditivo'.\n**Etapa 2:** Constatar que a mente antecipa cenários com base na regularidade estatística de dados sensoriais anteriores, confirmando em bases empíricas contemporâneas a genial intuição humeana sobre o hábito cognitivo."
    ))

    questoes_brutas.append((
        46, "EM13CHS103", "dificil",
        "Na análise do dualismo cartesiano, Descartes defendeu que animais não humanos são como autômatos mecânicos sem alma racional (a teoria do animal-máquina). Qual consequência ética e científica dessa formulação repercutiu nos séculos seguintes?",
        "Levou à proibição imediata de qualquer criação de animais domésticos nas cidades da Europa.",
        "Favoreceu a desvalorização do sofrimento animal e legitimou a vivissecção e a exploração mecânica desprovida de freios morais na experimentação biológica moderna.",
        "Incentivou a criação de santuários sagrados para proteger lobos e ursos das florestas francesas.",
        "Fez com que os governos europeus outorgassem direitos cívicos de voto aos cavalos de infantaria.",
        "Determinou que os cientistas não pudessem comer carne bovina em períodos de estudos astronômicos.",
        "B",
        "**Etapa 1:** Compreender a divisão radical entre a alma racional imaterial (exclusiva do ser humano) e a matéria mecanicista desprovida de consciência (Res Extensa).\n**Etapa 2:** Evidenciar que conceber animais como autômatos sem dor moral retirou-os da consideração ética clássica, justificando abusos mecânicos e desdobramentos críticos para a bioética moderna."
    ))

    questoes_brutas.append((
        47, "EM13CHS101", "dificil",
        "Ao examinar a célebre frase de René Descartes no Discurso sobre o Método — 'penso, logo existo' —, alguns críticos alegaram que se tratava de um silogismo incompleto ('Tudo o que pensa existe; eu penso; logo, existo'). Como Descartes defendeu a natureza puramente intuitiva dessa verdade?",
        "Afirmando que aprendeu a frase decorando versos cômicos em peças de teatro em Amsterdã.",
        "Esclarecendo que o Cogito não é uma dedução deduzida de premissas anteriores, mas uma intuição racional imediata e evidente na qual pensar e existir se manifestam como a mesma certeza indissociável.",
        "Concordando que o argumento estava incompleto e reescrevendo a obra para incluir cem novas premissas lógicas.",
        "Recorrendo à autoridade de teólogos de Roma para aprovar formalmente a validade de sua oração filosófica.",
        "Defendendo que a certeza do pensar só tem validade se for confirmada por instrumentos de laboratório químico.",
        "B",
        "**Etapa 1:** Diferenciar uma dedução silogística mediada por regras lógicas de uma intuição racional direta da mente.\n**Etapa 2:** Reconhecer que Descartes sustenta que o Cogito é apreendido em um único relâmpago de evidência imediata: no ato mesmo de duvidar/pensar, a consciência apreende instantaneamente sua própria existência sem precisar de premissas formais intermediárias."
    ))

    questoes_brutas.append((
        48, "EM13CHS103", "dificil",
        "Em contraposição ao racionalismo, o empirismo de David Hume adota o ceticismo mitigado ou moderado. Em que consiste essa moderação perante o conhecimento científico?",
        "Em suspender qualquer juízo prático e recusar alimentar-se ou caminhar pelas ruas por medo de acidentes.",
        "Em abandonar as especulações metafísicas dogmáticas sobre o além e limitar a investigação ao que pode ser verificado na experiência sensível, aceitando o conhecimento útil como probabilidade razoável para a vida prática.",
        "Em aceitar passivamente qualquer boato divulgado em jornais populares sem fazer perguntas.",
        "Em proibir o uso de termômetros e bússolas nas navegações de longa distância pelo oceano.",
        "Em afirmar que a mente humana é perfeita e imune a quaisquer equívocos de percepção visual.",
        "B",
        "**Etapa 1:** Distinguir o ceticismo pirrônico radical (paralisia prática) do ceticismo mitigado humeano.\n**Etapa 2:** Evidenciar que Hume reconhece os limites do intelecto para alcançar essências metafísicas ocultas, mas defende o rigor das ciências experimentais empíricas como guias práticos essenciais para a conduta diária e o progresso social."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "No Ensaio sobre o Entendimento Humano, John Locke estabelece a distinção entre substância material e substância espiritual, concluindo que o conceito de substância em si mesmo é:",
        "Um conceito perfeitamente transparente demonstrado por fórmulas matemáticas em quadros de giz.",
        "Uma suposição obscura de um suporte desconhecido ('um não sei quê') para qualidades que sabemos que existem na experiência sensível, mas cuja essência última não conseguimos perscrutar diretamente.",
        "Uma fraude linguística deliberada criada por generais que desejavam confiscar propriedades de camponeses.",
        "O único objeto que os olhos humanos conseguem enxergar no escuro com precisão cirúrgica.",
        "Uma palavra mágica herdada de hinos cantados pelos marinheiros fenícios no mar Mediterrâneo.",
        "B",
        "**Etapa 1:** Analisar a crítica empírica à categoria metafísica de substância independente.\n**Etapa 2:** Concluir que Locke reconhece a limitação cognitiva da mente: percebemos feixes de qualidades (cor, textura, peso), inferindo a existência de um substrato unificador material, mas sem jamais observar a substância pura em si mesma."
    ))

    questoes_brutas.append((
        50, "EM13CHS105", "dificil",
        "Considere o problema da indução de Hume aplicado ao aprendizado de máquina (Machine Learning) na Ciência da Computação moderna: se um algoritmo de inteligência artificial é treinado apenas com dados históricos passados, qual vulnerabilidade estrutural decorrente da crítica de Hume afeta seu desempenho?",
        "O algoritmo se recusará a processar números pares por considerá-los matematicamente desnecessários.",
        "O sistema pode falhar catastroficamente diante de cenários inéditos ('cisnes negros') ou rupturas de padrões, pois generalizar o passado para prever o futuro carece de necessidade lógica absoluta e pressupõe a uniformidade da natureza.",
        "Os computadores sofrerão superaquecimento térmico imediato toda vez que realizarem cálculos estatísticos de probabilidade.",
        "O software apagará automaticamente o sistema operacional caso encontre uma frase escrita por filósofos empiristas.",
        "A máquina perderá a conexão com a rede elétrica sempre que o operador humano fechar os olhos no laboratório.",
        "B",
        "**Etapa 1:** Conectar o problema metodológico da indução ao funcionamento de redes neurais artificiais e modelos de predição estatística.\n**Etapa 2:** Identificar que todo modelo indutivo de IA assume que a distribuição dos dados futuros repetirá a regularidade dos dados de treinamento passados; diante de rupturas imprevistas de contexto, o algoritmo padece da mesma fragilidade lógica apontada por David Hume."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Ao formular a teoria das Qualidades Primárias e Secundárias, John Locke fundamenta o nascimento da física moderna mecanicista. Qual o sentido dessa distinção para o conhecimento científico da matéria?",
        "Demonstra que o sabor doce do mel é a única propriedade física real que os astrônomos devem medir nos corpos celestes.",
        "Separa as propriedades objetivas e mensuráveis da matéria matemática (extensão, movimento, forma) das impressões subjetivas dos órgãos dos sentidos (cor, calor, cheiro), permitindo uma ciência física quantitativa e rigorosa.",
        "Comprova que os seres humanos não devem confiar na geometria para projetar pontes de travessia sobre rios.",
        "Afirma que os objetos materiais deixam de ter forma quando saímos da sala e apagamos a luz da lâmpada.",
        "Determina que a física quântica foi totalmente desenvolvida por artesãos de relógios de pêndulo na Inglaterra.",
        "B",
        "**Etapa 1:** Analisar o papel das qualidades primárias como propriedades reais inerentes aos corpos materiais em movimento.\n**Etapa 2:** Sintetizar que a ciência galileana e newtoniana repousa na geometrização e quantificação das qualidades primárias mensuráveis, tratando as qualidades secundárias como efeitos subjetivos na mente do observador."
    ))

    questoes_brutas.append((
        52, "EM13CHS103", "dificil",
        "Por que o filósofo racionalista René Descartes dedicou uma de suas regras do método à exigência da 'Evidência Clara e Distinta' como critério supremo de verdade?",
        "Porque ele queria vender óculos de aumento para comerciantes que contavam moedas nos cais dos portos.",
        "Porque apenas aquilo que se apresenta à razão de modo tão vívido, nítido e separado de qualquer outra ideia que não deixe espaço para dúvida concebível pode servir de base segura para o edifício do saber.",
        "Porque ele pretendia fechar os cursos universitários de química que utilizavam fumaça e fogo em laboratório.",
        "Porque as leis da língua francesa proibiam que os autores usassem metáforas em tratados científicos.",
        "Porque a verdade só pode ser descoberta por generais que marcham em linha reta em campos abertos.",
        "B",
        "**Etapa 1:** Compreender a definição cartesiana de clareza (presença manifesta à mente atenta) e distinção (separação nítida que impede a confusão com outros conceitos).\n**Etapa 2:** Concluir que a evidência racional substitui o critério escolástico do argumento de autoridade tradicional, instaurando a certeza interior da mente autônoma como padrão metodológico do saber."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Ao examinar a ideia de milagres religiosos em sua obra Investigação sobre o Entendimento Humano, qual argumento cético David Hume mobiliza contra os relatos de suspensão das leis da natureza?",
        "Ele afirma que os milagres só acontecem durante o dia, quando os astrônomos estão dormindo em suas casas.",
        "Ele demonstra que a evidência empírica acumulada pela experiência constante em favor da regularidade das leis naturais é esmagadoramente superior ao testemunho humano falível e suscetível à superstição, de modo que nenhum relato pode conferir certeza a um milagre.",
        "Ele defende que as leis da física foram aprovadas por jurados em audiências públicas de Atenas.",
        "Ele prova que os rios nunca transbordam durante tempestades de verão em cidades do interior.",
        "Ele sustenta que os profetas medievais utilizavam relógios de bolso para cronometrar a queima de lenha.",
        "B",
        "**Etapa 1:** Analisar o conflito de evidências na epistemologia empírica humeana entre a regularidade invariável da experiência das leis naturais e a fragilidade dos relatos testemunhais humanos.\n**Etapa 2:** Concluir com Hume que é sempre mais provável que quem relata um milagre esteja enganado, delirando ou mentindo do que a ordem regular da natureza física ter sido subvertida."
    ))

    questoes_brutas.append((
        54, "EM13CHS103", "dificil",
        "O Racionalismo de Descartes e o Empirismo de Locke e Hume chegaram a um impasse teórico no final do século XVIII que parecia insolúvel. Como esse dilema pode ser resumido?",
        "Ou a física era uma criação mágica de poetas trágicos, ou a geometria devia ser esquecida pelos cientistas.",
        "Ou o conhecimento repousa na razão pura com ideias inatas sem contato seguro com os fatos materiais, ou deriva da experiência contingente que desemboca no ceticismo de Hume sobre a causalidade e a certeza científica.",
        "Ou os homens deviam retornar ao convívio nas cavernas, ou os animais deviam governar as cidades da Europa.",
        "Ou a matemática dependia de orações religiosas em mosteiros, ou a astronomia precisava fechar os observatórios ópticos.",
        "Ou a escrita em papel devia ser proibida por decreto real, ou a memória humana perderia todas as suas palavras.",
        "B",
        "**Etapa 1:** Identificar o beco sem saída deixado pelas duas grandes correntes da teoria do conhecimento moderna.\n**Etapa 2:** Reconhecer que o racionalismo arriscava cair no dogmatismo especulativo sem validação empírica fática, enquanto o empirismo radical conduzia ao ceticismo que ameaçava o estatuto de verdade das leis newtonianas, preparando o terreno para a revolução crítica de Kant."
    ))

    questoes_brutas.append((
        55, "EM13CHS105", "dificil",
        "Na análise de John Locke sobre a identidade pessoal no Livro II do Ensaio, qual critério inovador ele estabelece para a continuidade do 'Eu' ao longo do tempo, em substituição à posse de uma alma imaterial metafísica?",
        "A conservação do mesmo corte de cabelo e das mesmas roupas cerimoniais ao longo de toda a velhice.",
        "A continuidade da Consciência reflexiva e da Memória psicológica, que unifica as ações passadas e presentes como pertencentes à mesma pessoa moral.",
        "A obrigação de morar na mesma casa de pedra e na mesma rua até o dia do sepultamento.",
        "A posse contínua de moedas de prata guardadas em arcas trancadas com cadeados de ferro.",
        "A presença obrigatória do nome de batismo registrado em placas de bronze instaladas no tribunal.",
        "B",
        "**Etapa 1:** Compreender a ruptura de Locke com a tese cartesiana de que a identidade reside na substância espiritual imaterial fixa (alma).\n**Etapa 2:** Sintetizar que Locke inaugura o conceito moderno de identidade pessoal psicológica: o que define o 'Eu' é o alcance retrospectivo da consciência pela memória de suas experiências e ações voluntárias."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Ao examinar a passagem da Dúvida Hiperbólica para a reconstituição do mundo exterior nas Meditações, qual papel desempenha a dedução da existência de Deus em Descartes?",
        "Funciona como um mero artifício protocolar para evitar condenações inquisitoriais sem função no sistema filosófico.",
        "Atua como a ponte teórica indispensável que rompe o solipsismo do Cogito, garantindo que o sujeito pensante não está isolado e que suas representações claras do mundo material correspondem a coisas reais.",
        "Serve para revogar as leis do movimento mecânico e permitir que milagres aconteçam diariamente nos laboratórios.",
        "Demonstra que o corpo biológico dos animais possui mais inteligência do que a mente dos filósofos.",
        "Obriga os astrônomos a rezarem orações matinais antes de apontarem os telescópios para as luas de Júpiter.",
        "B",
        "**Etapa 1:** Entender o risco do solipsismo em que Descartes se encontrava (ter certeza apenas de que 'eu penso e existo', sem saber se o mundo exterior é real).\n**Etapa 2:** Concluir que a demonstração de um Deus perfeito e não enganador funciona como o fiador da objetividade científica: permite restabelecer a validade do conhecimento sobre o mundo corpóreo material exterior."
    ))

    questoes_brutas.append((
        57, "EM13CHS103", "dificil",
        "Considere a crítica de David Hume à noção de causalidade: se ela é um produto do hábito psicológico e não uma lei necessária do Ser, o que fundamenta a prática contínua do método científico experimental?",
        "A certeza dogmática de que os deuses nunca mudam as regras da física terrestre.",
        "O pragmatismo crítico: a ciência não opera com certezas absolutas metafísicas, mas com generalizações empíricas probabilísticas que funcionam e se sustentam enquanto novas experiências não as contradisserem.",
        "A crença cega de que os cientistas possuem poderes mágicos que garantem o funcionamento dos experimentos.",
        "A exigência de que todos os teoremas de física sejam aprovados por votação dos trabalhadores das oficinas.",
        "O abandono definitivo de qualquer tipo de teste ou observação em laboratórios de química.",
        "B",
        "**Etapa 1:** Analisar o destino do método indutivo experimental após a desconstrução humeana da necessidade causal absoluta.\n**Etapa 2:** Concluir que a ciência moderna readapta sua pretensão: passa a operar no registro da falibilidade, da probabilidade estatística cumulativa e da heurística instrumental bem-sucedida para a vida prática."
    ))

    questoes_brutas.append((
        58, "EM13CHS105", "dificil",
        "Em discussões contemporâneas sobre algoritmos e inteligência artificial generativa (Large Language Models), alguns teóricos afirmam que esses sistemas operam como mentes empiristas puras. Qual argumento fundamenta essa analogia?",
        "Os modelos de IA nascem com almas imateriais doadas por programadores durante o teste de software.",
        "Os modelos de linguagem iniciam sem conhecimentos inatos a priori, sendo alimentados por gigantescos volumes de dados e ajustando pesos estatísticos de previsão textual a partir da experiência cumulativa de exemplos empíricos.",
        "Os computadores precisam tomar banhos de sol matinais para aquecer as placas de silício dos servidores de nuvem.",
        "Os algoritmos rejeitam qualquer cálculo numérico por considerarem a matemática uma convenção passageira.",
        "Os processadores perdem a capacidade de raciocinar quando são desconectados das bibliotecas medievais de Paris.",
        "B",
        "**Etapa 1:** Comparar o modelo da Tábula Rasa e da associação estatística de percepções com a arquitetura de aprendizado profundo de máquina (Deep Learning).\n**Etapa 2:** Evidenciar que os LLMs operam de forma análoga à psicologia empirista: sem conceitos inatos prévios, constroem representações do mundo a partir da ingestão massiva de dados textuais e correlações empíricas reiteradas."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "Ao contrastar a metafísica de Descartes com o empirismo de Locke, como cada um concebe a possibilidade de alcançar a verdade sobre o cosmos?",
        "Descartes acredita que a verdade só é alcançada por meio de rituais com fogo, e Locke sustenta que apenas generais sabem fazer ciências.",
        "Descartes confia na dedução a priori das ideias claras e distintas da razão independente dos sentidos, enquanto Locke exige a indução empírica e a ancoragem rigorosa nos dados da experiência concreta.",
        "Descartes afirma que o cosmos é uma ilusão que desaparecerá amanhã, e Locke defende que as pedras pensam como filósofos.",
        "Ambos defendem que a verdade não pode ser conhecida e que os cientistas devem dedicar-se apenas à poesia dramática.",
        "Ambos sustentam que as leis da física foram redigidas por reis divinos que governavam o Egito antes dos gregos.",
        "B",
        "**Etapa 1:** Sintetizar os vetores metodológicos divergentes do Racionalismo e do Empirismo.\n**Etapa 2:** Explicitar a oposição: a confiança cartesiana na geometria e na dedução racional apriorística como acesso às essências versus a exigência lockeana de validação sensível a posteriori e limites epistêmicos da experiência."
    ))

    questoes_brutas.append((
        60, "EM13CHS103", "dificil",
        "Ao examinar o legado do debate entre Racionalismo e Empirismo para a teoria contemporânea do conhecimento, conclui-se que o método científico maduro superou essa polarização unilateral ao estabelecer que:",
        "As ciências devem ignorar tanto a razão matemática quanto os testes empíricos em benefício da intuição artística pura.",
        "O conhecimento científico autêntico exige a articulação dialética indispensável entre a formulação racional de hipóteses teóricas e modelos matemáticos dedutivos e a verificação empírica sistemática e controlada na experiência.",
        "O racionalismo estava cem por cento correto e os laboratórios experimentais foram fechados nas universidades de ponta.",
        "O empirismo provou que a matemática é uma mentira que deve ser expurgada de todas as faculdades de engenharia.",
        "Os governantes da sociedade devem decidir por decreto eleitoral quais hipóteses científicas são verdadeiras.",
        "B",
        "**Etapa 1:** Analisar a síntese conceitual que emerge da superação do confronto Racionalismo vs. Empirismo.\n**Etapa 2:** Concluir que a ciência moderna (e o posterior criticismo kantiano) demonstra que 'teorias sem dados empíricos são vazias, e dados empíricos sem teorias racionais são cegos', consagrando o método hipotético-dedutivo que une modelo racional e teste experimental."
    ))

    # Auditoria de vocabulário e blacklist
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

    print(f"Total de questões brutas: {len(questoes_brutas)}")
    assert len(questoes_brutas) == 60, f"Erro: esperava 60, obteve {len(questoes_brutas)}"

    # Balanceamento de gabaritos
    questoes = balancear_questoes(questoes_brutas)

    # Teste de termos proibidos em todas as questões
    erros_termos = []
    for q in questoes:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        texto_q = f"{enunc} {a} {b} {c} {d} {e} {res}".lower()
        for pat in padroes_proibidos:
            m = re.search(pat, texto_q)
            if m:
                erros_termos.append(f"Questão {num}: termo proibido '{m.group(0)}' encontrado!")

    if erros_termos:
        print("\n[ERRO NA AUDITORIA DE TERMOS PROIBIDOS]:")
        for err in erros_termos:
            print(f" - {err}")
        sys.exit(1)

    # Montagem do Markdown
    header = """---
série: "Ensino Médio"
disciplina: "Filosofia"
eixo: "eixo-1-epistemologia"
capitulo: "cap-06-epistemologia-moderna-racionalismo-empirismo"
objeto_de_conhecimento: "A Origem e Validade do Conhecimento na Idade Moderna; O Racionalismo de René Descartes (Discurso sobre o Método): Dúvida Hiperbólica Metódica, O Cogito, ergo sum e as Ideias Inatas; Dualismo Mente-Corpo (Res Cogitans vs. Res Extensa); O Empirismo Britânico: John Locke e a Mente como Tábula Rasa (Rejeição das Ideias Inatas); David Hume e o Ceticismo Epistemológico: A Crítica ao Princípio da Causalidade como Hábito Psicológico."
ebook_fonte: "em-fil-c06-epistemologia-moderna-racionalismo-empirismo.md"
habilidades: "EM13CHS101, EM13CHS103, EM13CHS105, H1, H2, H11"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: A Epistemologia Moderna: Racionalismo Cartesiano vs. Empirismo Britânico

"""

    corpo = header
    gabaritos_finais = []

    # Nível Básico
    corpo += "## Nível Básico\n\n"
    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-06-epistemologia-moderna-racionalismo-empirismo -->\n"
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
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-06-epistemologia-moderna-racionalismo-empirismo -->\n"
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
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-06-epistemologia-moderna-racionalismo-empirismo -->\n"
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
- CHAUÍ, Marilena. *Convite à Filosofia*. São Paulo: Ática, 2002.
- COTTINGHAM, John. *Dicionário Descartes*. Tradução de Helena Martins. Rio de Janeiro: Jorge Zahar, 1995.
- DESCARTES, René. *Discurso sobre o Método e Meditações Metafísicas*. Tradução de J. Guinsburg e Bento Prado Júnior. São Paulo: Nova Cultural, 2001.
- HUME, David. *Investigação sobre o Entendimento Humano*. Tradução de José Oscar de Almeida Marques. São Paulo: Editora Unesp, 2003.
- LOCKE, John. *Ensaio sobre o Entendimento Humano*. Tradução de Eduardo Abranches de Soveral. Lisboa: Fundação Calouste Gulbenkian, 1999. v. 1 e 2.
- MARCONDES, Danilo. *Iniciação à História da Filosofia: Dos Pré-Socráticos a Wittgenstein*. 11. ed. Rio de Janeiro: Jorge Zahar, 2007.
"""

    print("Total de Gabaritos detectados:", len(gabaritos_finais))
    print("Contagem por letra:", Counter(gabaritos_finais))

    assert len(gabaritos_finais) == 60
    assert all(count == 12 for count in Counter(gabaritos_finais).values()), "Gabarito desbalanceado!"

    print("[AUDITORIA INTERNA APROVADA] Todas as 60 questões atendem rigorosamente às travas pedagógicas!")

    # Grava rascunho temporário
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(corpo)
    print(f"Rascunho temporário salvo com sucesso ({len(corpo.encode('utf-8'))} bytes).")

    # Invoca o validador oficial
    cmd = [sys.executable, "validador_educamob.py", temp_draft, dest_path]
    print(f"Executando validador: {' '.join(cmd)}")
    res_val = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res_val.stdout)
    if res_val.stderr:
        print("[STDERR]:", res_val.stderr)

    if res_val.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 06 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {res_val.returncode}")
        sys.exit(res_val.returncode)

if __name__ == "__main__":
    gerar_cap06()
