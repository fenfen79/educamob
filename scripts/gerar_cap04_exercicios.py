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

def gerar_cap04():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-04-platao-mundo-ideias-caverna/ebooks/em-fil-c04-platao-mundo-ideias-caverna-exercicios.md"
    temp_draft = "temp_draft.md"

    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Na teoria das Ideias de Platão, como é caracterizado o Mundo Sensível em relação à realidade?",
        "Um plano composto por entidades eternas, imutáveis e perfeitas acessíveis pela razão pura.",
        "A dimensão material em que vivemos, marcada pela mudança, imperfeição e cópias transitórias.",
        "O espaço sideral infinito onde habitam as almas dos governantes justos.",
        "Uma ilusão linguística passageira criada por poetas trágicos em peças teatrais.",
        "Um reino estritamente matemático desprovido de qualquer objeto palpável.",
        "B",
        "O mundo sensível é o plano físico empírico, composto por cópias imperfeitas e mutáveis das Ideias eternas."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "O Mundo Inteligível platônico abriga as Formas ou Ideias puras. Qual propriedade define essas essências?",
        "São perecíveis e desaparecem quando as coisas materiais morrem.",
        "São imateriais, eternas, imutáveis, perfeitas e apreensíveis pelo intelecto.",
        "Dependem da imaginação psicológica de cada ser humano para existirem.",
        "São cópias pintadas em telas de madeira por artesãos da Academia.",
        "Podem ser tocadas e medidas por meio de réguas de metal e balanças.",
        "B",
        "As Ideias puras são realidades objetivas, perfeitas, eternas e incorruptíveis, acessíveis pela mente racional."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "No ápice da hierarquia do Mundo das Ideias, Platão posiciona qual Forma suprema, comparada ao Sol?",
        "A Ideia de Força Física.",
        "A Ideia de Beleza Sensível.",
        "A Ideia do Bem.",
        "A Ideia de Riqueza Material.",
        "A Ideia de Movimento Perpétuo.",
        "C",
        "A Ideia do Bem é o princípio supremo que confere verdade, ser e inteligibilidade a todas as demais Formas."
    ))

    questoes_brutas.append((
        4, "EM13CHS103", "basico",
        "A Teoria da Reminiscência (Anamnese) afirma que o ato de conhecer consiste fundamentalmente em:",
        "Inventar novas fórmulas científicas por meio de experimentos casuais.",
        "Decorar os decretos jurídicos aprovados pelos magistrados da cidade.",
        "Recordar as verdades eternas que a alma contemplou antes de nascer.",
        "Copiar os gestos e as opiniões de oradores bem-sucedidos na ágora.",
        "Aceitar sem questionar os dogmas tradicionais transmitidos pela família.",
        "C",
        "Para Platão, conhecer é recordar (Anamnese): a alma imortal já viu as Ideias e as relembra ao ser estimulada."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Na Alegoria da Caverna, o que representam as correntes que prendem os prisioneiros desde a infância?",
        "As muralhas de pedra construídas para proteger as cidades gregas de invasões.",
        "Os preconceitos acríticos, as paixões e as ilusões dos sentidos corporais.",
        "As leis justas redigidas por reis sábios para manter a ordem social.",
        "Os ensinamentos de geometria que exigiam disciplina mental dos jovens.",
        "Os laços de amizade sincera cultivados pelos membros da Academia.",
        "B",
        "As correntes simbolizam as amarras dos sentidos e os preconceitos superficiais que impedem o acesso à verdade."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "Na caverna subterrânea descrita no Livro VII de A República, o que os prisioneiros enxergam na parede do fundo?",
        "Objetos reais iluminados pela luz do Sol do meio-dia.",
        "Projeções de sombras produzidas pela fogueira atrás de artefatos.",
        "Pinturas de deuses olímpicos feitas por sacerdotes de Delfos.",
        "Estrelas luminosas visíveis através de frestas abertas na rocha.",
        "Reflexos nítidos de seus próprios rostos em espelhos de bronze.",
        "B",
        "Os prisioneiros contemplam apenas sombras de estátuas e artefatos, tomando essas aparências pela realidade objetiva."
    ))

    questoes_brutas.append((
        7, "EM13CHS103", "basico",
        "Quando o prisioneiro libertado sai da caverna e atinge a superfície ensolarada, qual é sua reação inicial?",
        "Enxerga imediatamente todas as árvores e animais com nitidez e alegria.",
        "Sente dores nos olhos e ofuscamento pela intensidade da luz solar.",
        "Corre de volta para a caverna para recuperar seus pertences pessoais.",
        "Proclama-se rei de todas as terras visíveis ao redor da montanha.",
        "Dorme profundamente por não conseguir suportar o calor das chamas.",
        "B",
        "O contato inicial com a luz plena da verdade gera dor e cegueira temporária, exigindo adaptação gradual (Paideia)."
    ))

    questoes_brutas.append((
        8, "EM13CHS103", "basico",
        "Na alegoria platônica, o que o filósofo liberto deve fazer após contemplar a luz do Sol e o mundo real?",
        "Permanecer no alto da montanha em contemplação solitária e isolada.",
        "Retornar ao fundo da caverna para orientar e desacorrentar seus semelhantes.",
        "Fundar uma nova cidade militar na superfície para guerrear contra a caverna.",
        "Cobrar moedas de ouro para descrever o céu aos homens acorrentados.",
        "Escrever peças de teatro satíricas zombando da ignorância dos prisioneiros.",
        "B",
        "O filósofo tem o dever cívico e moral de voltar à caverna para educar e governar a pólis com justiça."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Na metáfora da Linha Dividida, qual grau de conhecimento representa o nível mais baixo, baseado em conjecturas e sombras?",
        "Noesis.",
        "Dianoia.",
        "Pistis.",
        "Eikasia.",
        "Episteme.",
        "D",
        "A Eikasia (ilusão ou conjectura) é o primeiro estágio da Doxa, correspondendo às sombras da caverna e aparências vagas."
    ))

    questoes_brutas.append((
        10, "EM13CHS101", "basico",
        "O segundo grau do conhecimento sensível na Linha Dividida, denominado Pistis (crença), refere-se à percepção de:",
        "Sombras projetadas na água durante noites de tempestade.",
        "Objetos materiais físicos, animais, plantas e artefatos fabricados.",
        "Axiomas matemáticos abstratos desprovidos de figuras empíricas.",
        "Ideias puras contempladas na esfera luminosa do Hiperurânio.",
        "Leis divinas reveladas por sacerdotisas em templos oraculares.",
        "B",
        "A Pistis é a confiança sensorial nos objetos materiais do mundo sensível, ainda situada no domínio da opinião (Doxa)."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "No Mundo Inteligível, o grau da Dianoia caracteriza-se principalmente pelo modo de pensar próprio de qual disciplina?",
        "Da oratória eleitoral dos sofistas em praças públicas.",
        "Da pintura de murais em templos dedicados à deusa Atena.",
        "Das matemáticas e da geometria que partem de hipóteses.",
        "Da poesia dramática cantada por rapsodos em festejos cívicos.",
        "Da culinária palaciana que combina temperos agridoces.",
        "C",
        "A Dianoia é a razão discursiva que opera com hipóteses matemáticas e representações geométricas auxiliares."
    ))

    questoes_brutas.append((
        12, "EM13CHS101", "basico",
        "O grau supremo do conhecimento inteligível na filosofia de Platão é a Noesis, alcançada por meio de qual método?",
        "Da observação empírica com auxílio de telescópios modernos.",
        "Da Dialética ascendente que atinge a visão direta das Ideias e do Bem.",
        "Do sorteio de sentenças jurídicas em urnas de barro cozido.",
        "Da memorização mecânica de cantos militares em quartéis.",
        "Do consumo de substâncias aromáticas em cerimônias religiosas.",
        "B",
        "A Noesis é a intuição intelectiva pura, conquistada pela Dialética que dispensa apoios sensíveis e contempla o Bem."
    ))

    questoes_brutas.append((
        13, "EM13CHS103", "basico",
        "No diálogo Mênon, Sócrates demonstra a teoria da reminiscência ao guiar um jovem escravo a realizar qual façanha intelectual?",
        "Citar de memória os nomes de todos os reis da dinastia macedônia.",
        "Deduzir a resolução geométrica para o problema da duplicação da área do quadrado.",
        "Elaborar um discurso retórico capaz de absolver um réu perante o tribunal.",
        "Pintar uma representação exata do mapa das muralhas da cidade de Atenas.",
        "Adivinhar o número de grãos de areia contidos em uma ânfora fechada.",
        "B",
        "Apenas formulando perguntas, Sócrates faz o escravo relembrar conceitos geométricos e duplicar a área do quadrado."
    ))

    questoes_brutas.append((
        14, "EM13CHS105", "basico",
        "A proposta política central de A República de Platão estabelece a tese da Sofocracia, que defende:",
        "O governo dos guerreiros mais fortes e disciplinados militarmente.",
        "O sorteio aleatório de cargos de magistratura entre todos os cidadãos.",
        "O governo da cidade confiado aos filósofos, guiados pela razão e pela justiça.",
        "O controle da administração pública pelos comerciantes mais ricos da pólis.",
        "A entrega do comando cívico a sacerdotes de templos tradicionais de Delfos.",
        "C",
        "A Sofocracia postula que a cidade só será justa quando os filósofos forem reis ou os reis se tornarem verdadeiros filósofos."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "A expressão platônica soma sema ('o corpo é o túmulo da alma') traduz qual concepção antropológica?",
        "A imortalidade do corpo físico diante da rápida decomposição do espírito.",
        "A alma prisioneira no invólucro corporal sensível, que limita sua visão da verdade.",
        "A obrigação cívica de construir túmulos monumentais de mármore para generais.",
        "A união perfeita e inseparável entre matéria e pensamento racional puro.",
        "A celebração dos prazeres sensoriais como caminho supremo para a felicidade.",
        "B",
        "Para o dualismo platônico, a alma imortal encontra-se aprisionada no corpo sensível, sofrendo a amnésia das Ideias."
    ))

    questoes_brutas.append((
        16, "EM13CHS103", "basico",
        "Na fundação da Academia de Platão em 387 a.C., qual inscrição solene figurava no frontispício da entrada?",
        "'Não entre aqui quem não pagar a taxa anual em moedas de ouro.'",
        "'Não entre aqui quem não for geômetra.'",
        "'Proibido o diálogo com cidadãos desprovidos de títulos nobres.'",
        "'Apenas os guerreiros condecorados têm direito ao estudo da lei.'",
        "'Dedique sua vida ao cultivo exclusivo de oliveiras e vinhas.'",
        "B",
        "A exigência da geometria visava treinar a mente na abstração matemática preparatória para a contemplação das Ideias."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Quando o filósofo liberto regressa à caverna para libertar os companheiros, qual reação os prisioneiros manifestam?",
        "Acolhem o filósofo com coroas de louros e o elegem líder imediato da caverna.",
        "Zombam de sua cegueira na escuridão e ameaçam matá-lo se tentar soltá-los.",
        "Abandonam correndo as correntes para contemplar as árvores na superfície.",
        "Oferecem moedas de prata para aprenderem a calcular áreas de triângulos.",
        "Destroem a fogueira para que a caverna permaneça em escuridão total.",
        "B",
        "Acostumados às sombras, os prisioneiros julgam que o filósofo arruinou a visão e reagem com violência contra quem os desafia."
    ))

    questoes_brutas.append((
        18, "EM13CHS101", "basico",
        "Para Platão, o conceito de Mímesis no plano da arte e da pintura é avaliado de modo crítico porque a obra artística:",
        "Constitui uma cópia da cópia, afastando os homens da verdade inteligível das Formas.",
        "Substitui perfeitamente as leis escritas aprovadas na assembleia popular.",
        "Exige o conhecimento exato de teoremas matemáticos de geometria plana.",
        "Garante a eternidade física dos corpos representados nas telas pintadas.",
        "Impede que os cidadãos gastem recursos materiais na compra de alimentos.",
        "A",
        "O artesão copia a Ideia eterna ao fazer um objeto; o pintor copia o objeto físico, gerando uma cópia a dois graus da verdade."
    ))

    questoes_brutas.append((
        19, "EM13CHS105", "basico",
        "No filme Matrix (1999), a cena em que Neo ingere a pílula vermelha e é retirado de sua cápsula subterrânea simboliza:",
        "A aceitação confortável das sombras projetadas pelas redes de computadores.",
        "O doloroso processo de desacorrentamento e despertar para a realidade objetiva.",
        "A vitória definitiva das máquinas inteligentes sobre a resistência humana.",
        "A submissão do programador às ordens dos diretores de corporações digitais.",
        "O esquecimento completo de todas as lembranças vividas durante a juventude.",
        "B",
        "A pílula vermelha rompe a ilusão da simulação neural (a caverna), iniciando a dolorosa libertação em direção ao mundo real."
    ))

    questoes_brutas.append((
        20, "EM13CHS101", "basico",
        "A noção platônica de Doxa (opinião) diferencia-se da Episteme (ciência) porque a opinião:",
        "É imutável, necessária e demonstrada por princípios universais firmes.",
        "É instável, mutável, baseada em aparências sensíveis e desprovida de fundamento causal necessário.",
        "Pode ser alcançada exclusivamente por meio da contemplação da Ideia do Bem.",
        "Representa a sabedoria divina transmitida por oráculos sagrados de Delfos.",
        "Exige dez anos de estudos de geometria e dialética em academias filosóficas.",
        "B",
        "A Doxa é o saber superficial dos sentidos e aparências, enquanto a Episteme é a ciência fundamentada e demonstrativa."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "A Teoria das Ideias de Platão superou o embate entre Heráclito e Parmênides ao conciliar as duas visões por meio de:",
        "Uma negação total da existência do mundo material sensível e dos sentidos corporais.",
        "Um modelo dualista no qual o devir de Heráclito rege o mundo sensível e o Ser de Parmênides habita o mundo inteligível.",
        "Uma teoria mecanicista em que átomos colidem espontaneamente no espaço vazio.",
        "Uma cosmologia mística que atribui aos planetas a responsabilidade pelos atos dos homens.",
        "Uma submissão da reflexão filosófica às narrativas mitológicas de Homero e Hesíodo.",
        "B",
        "Platão acomoda o fluxo heraclitiano no mundo empírico e a permanência parmenidiana no plano das Ideias perfeitas."
    ))

    questoes_brutas.append((
        22, "EM13CHS103", "intermediario",
        "No paradoxo de Mênon, questiona-se a possibilidade de buscar o conhecimento se não se sabe o que se busca. A resposta platônica resolve o dilema afirmando que:",
        "O homem nunca conhece nada de verdade, devendo contentar-se com opiniões passageiras.",
        "A alma já contemplou a verdade e não aprende do zero, mas recorda o que esqueceu ao encarnar.",
        "Os sacerdotes devem ditar as respostas prontas para que os jovens não percam tempo investigando.",
        "A busca da verdade deve ser adiada até que a cidade conquiste novas colônias no exterior.",
        "O conhecimento depende exclusivamente de sorteios realizados nas assembleias populares.",
        "B",
        "A reminiscência (Anamnese) resolve o paradoxo: a investigação é possível porque o saber já está na alma em estado latente."
    ))

    questoes_brutas.append((
        23, "EM13CHS105", "intermediario",
        "Ao formular a tese do Rei-Filósofo em A República, Platão estabeleceu exigências severas para os guardiões-governantes, incluindo:",
        "O direito de acumular terras, palácios de luxo e barras de ouro nos bancos municipais.",
        "A proibição de possuírem propriedade privada e riquezas pessoais, governando pelo bem comum.",
        "O dever de transmitir seus cargos governamentais de forma hereditária aos seus próprios filhos.",
        "A permissão para cobrar propinas em contratos de fornecimento de armas para a infantaria.",
        "A dispensa do estudo da matemática e da dialética após assumirem o poder do Estado.",
        "B",
        "Os governantes platônicos não podiam acumular patrimônio particular, evitando que usassem a autoridade em proveito familiar."
    ))

    questoes_brutas.append((
        24, "EM13CHS101", "intermediario",
        "A analogia do Sol presente no Livro VI de A República explica o papel da Ideia do Bem afirmando que, assim como o Sol físico ilumina os olhos:",
        "A Ideia do Bem queima a mente dos cidadãos que tentam estudar geometria em praça pública.",
        "A Ideia do Bem confere verdade aos objetos cognoscíveis e capacidade de conhecer ao intelecto humano.",
        "O calor solar obriga os agricultores a encerrarem as colheitas durante o inverno chuvoso.",
        "A luz divina afasta os marinheiros das rotas mercantis que ligam o porto de Pireu ao Egito.",
        "As tempestades solares alteram as leis da física registradas nos compêndios da Academia.",
        "B",
        "O Bem desempenha no plano inteligível a função do Sol no visível: concede existência, ordem e inteligibilidade a todo o real."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Na Linha Dividida, a passagem da Dianoia (razão matemática) para a Noesis (intuição dialética) representa um avanço qualitativo porque:",
        "A Noesis abandona o uso de figuras sensíveis auxiliares e ascende até o princípio incondicionado supremo.",
        "A Dianoia é um tipo de mentira consciente ensinada pelos sofistas para enganar credores na praça.",
        "O cálculo geométrico impede que o cidadão participe de decisões militares durante as guerras cívicas.",
        "A Noesis exige a realização de jejuns prolongados e o isolamento em cavernas escuras da serra.",
        "As matemáticas deixam de ter utilidade prática na construção de embarcações e templos da cidade.",
        "A",
        "A Dianoia ainda usa desenhos empíricos (como triângulos desenhados); a Noesis alcança o Bem por dialética pura sem imagens."
    ))

    questoes_brutas.append((
        26, "EM13CHS104", "intermediario",
        "A crítica de Platão à poesia e ao teatro homérico no Livro X de A República fundamentava-se no receio de que essas narrativas:",
        "Incentivassem os jovens a abandonar a prática de exercícios físicos nos ginásios da pólis.",
        "Estimulassem as paixões inferiores e descontroladas, enfraquecendo o domínio da razão sobre a alma.",
        "Custassem verbas excessivas do erário público que deveriam financiar frotas de navios armados.",
        "Fossem encenadas exclusivamente em dialetos estrangeiros incompreensíveis para os atenienses.",
        "Exigissem a queima de todos os instrumentos musicais de corda fabricados nas oficinas.",
        "B",
        "Platão alertava que a tragédia alimenta o choro excessivo e paixões desmedidas, prejudicando o autodomínio racional do cidadão."
    ))

    questoes_brutas.append((
        27, "EM13CHS105", "intermediario",
        "Em análises sobre mídias digitais contemporâneas, o algoritmo que personaliza feeds com conteúdos hiper-realistas atua como:",
        "A luz plena do Sol que emancipa o cidadão das limitações do mundo sensível imediato.",
        "A fogueira e os manipuladores de marionetes da caverna, projetando sombras sob medida para reter o usuário.",
        "A dialética socrática que obriga os indivíduos a examinarem suas contradições morais na praça.",
        "O teorema geométrico que comprova a igualdade dos lados de um triângulo equilátero.",
        "A lei cívica escrita na ágora para garantir a todos a igualdade formal de manifestação pública.",
        "B",
        "As bolhas digitais e deepfakes operam como a fogueira e os fantoches de Platão, prendendo a atenção na simulação de sombras."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "A relação de Participação (Méthexis) estabelecida por Platão entre os dois mundos explica que uma coisa bela no mundo físico:",
        "É bela por um capricho momentâneo de deuses olímpicos que a abençoaram em rituais sagrados.",
        "Só é bela na medida em que reflete e participa imperfeitamente da Ideia eterna e imutável de Beleza.",
        "Deixará de ser bela caso os magistrados da cidade aprovem um decreto mudando as regras de arte.",
        "Possui em si mesma uma beleza infinita que nunca sofrerá o desgaste do tempo ou do clima.",
        "Foi esculpida por artesãos que copiaram desenhos encontrados em pirâmides do Vale do Nilo.",
        "B",
        "A beleza das coisas materiais é derivada e passageira; ela decorre da participação daquela matéria na Forma inteligível da Beleza."
    ))

    questoes_brutas.append((
        29, "EM13CHS103", "intermediario",
        "O conceito platônico de Paideia (educação) não se reduz ao acúmulo passivo de dados informativos, mas é concebido como:",
        "A conversão do olhar da alma, arrancando o sujeito da ilusão das sombras para o discernimento da verdade.",
        "O treinamento mecânico de marinheiros para remar com velocidade em dias de combate naval.",
        "A memorização compulsória de todas as sentenças judiciais arquivadas nos tribunais populares.",
        "A prática diária de exercícios atléticos para conquistar medalhas de ouro nos jogos olímpicos.",
        "A cobrança de mensalidades financeiras para ensinar técnicas de persuasão a filhos de nobres.",
        "A",
        "A Paideia platônica é uma conversão profunda da alma (periagoge), reorientando a atenção das sombras corpóreas para o ser inteligível."
    ))

    questoes_brutas.append((
        30, "EM13CHS101", "intermediario",
        "No platonismo matemático sustentado por pensadores como Kurt Gödel, as propriedades e teoremas da matemática são entendidos como:",
        "Invenções linguísticas convenientes criadas pela mente humana para facilitar cálculos de comércio.",
        "Estruturas objetivas e eternas da realidade que o cientista descobre, e não meras criações arbitrárias.",
        "Regras burocráticas temporárias que mudam de acordo com a moeda circulante em cada país.",
        "Fórmulas mágicas reveladas em sonhos a sacerdotes de templos dedicados a Apolo.",
        "Desenhos estéticos feitos por pintores para decorar salas de conferência em universidades.",
        "B",
        "O realismo platônico sustenta que entidades e relações matemáticas têm existência objetiva independente do sujeito cognoscente."
    ))

    questoes_brutas.append((
        31, "EM13CHS105", "intermediario",
        "A alegoria da caverna funciona também como uma interpretação filosófica do destino histórico de Sócrates, porque antecipa que:",
        "O filósofo seria aclamado como general supremo e lideraria Atenas em vitórias no exterior.",
        "O homem liberto que desce à caverna para despertar seus concidadãos seria incompreendido e morto por eles.",
        "A cidade de Atenas construiria templos de mármore branco em homenagem à memória do filósofo.",
        "Os juízes populares pediriam perdão público por terem emitido uma sentença injusta contra o mestre.",
        "Os amigos do filósofo organizariam uma fuga bem-sucedida para as cidades do norte da Grécia.",
        "B",
        "Platão alude claramente ao martírio de Sócrates: os prisioneiros apegados às sombras matam aquele que tenta desatar suas correntes."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Ao distinguir a opinião correta (orthē doxa) da ciência verdadeira (Episteme), Platão observa no diálogo Mênon que a opinião correta:",
        "É sempre uma mentira perversa inventada para desviar a comunidade dos deveres da virtude.",
        "Pode acertar o caminho prático, mas é instável e foge da mente por carecer de justificação racional necessária.",
        "Tem o mesmo valor demonstrativo eterno de um teorema geométrico comprovado por deduções.",
        "Deve ser punida com penas de prisão pelos magistrados encarregados da vigilância cívica.",
        "Pertence exclusivamente aos animais que vivem em rebanhos domesticados no campo.",
        "B",
        "A opinião correta acerta por acaso ou intuição prática, mas é como as estátuas de Dédalo: foge se não for amarrada pelo Logos."
    ))

    questoes_brutas.append((
        33, "EM13CHS103", "intermediario",
        "O filósofo cristão Santo Agostinho de Hipona adaptou a teoria platônica da reminiscência ao formular qual conceito teológico?",
        "A predestinação biológica dos pecados corporais transmitida pelo sangue.",
        "A Teoria da Iluminação Divina, em que Deus ilumina a mente humana para que ela enxergue as verdades eternas.",
        "A reencarnação sucessiva das almas em corpos de animais conforme os atos praticados em vida.",
        "A negação de qualquer capacidade racional na inteligência dos seres humanos após a queda.",
        "A exigência de que todos os fiéis aprendam geometria grega antes de receberem o batismo.",
        "B",
        "Agostinho substituiu a recordação de vidas passadas pela iluminação interior que Deus concede à razão para captar as verdades."
    ))

    questoes_brutas.append((
        34, "EM13CHS101", "intermediario",
        "Para Platão, a Ideia de Círculo difere fundamentalmente de qualquer círculo desenhado a giz na lousa por um professor porque:",
        "O desenho a giz é perfeito e eterno, enquanto a Ideia de Círculo sofre desgaste com a umidade da sala.",
        "O desenho material é uma aproximação sensível imperfeita, enquanto a Ideia é a perfeição geométrica absoluta da equidistância.",
        "O círculo da lousa pode ser visto por todas as pessoas, enquanto a Ideia de Círculo não tem nenhuma realidade.",
        "A Ideia de Círculo depende do tipo de giz utilizado pelo mestre para manter seus ângulos corretos.",
        "Os geômetras da Academia proibiam o estudo de círculos por considerá-los figuras caóticas sem ordem.",
        "B",
        "Nenhum círculo material é perfeitamente plano ou equidistante; ele apenas imita a perfeição conceitual da Forma pura de Círculo."
    ))

    questoes_brutas.append((
        35, "EM13CHS105", "intermediario",
        "A decepção de Platão com a democracia ateniense (expressa na Carta VII) decorreu primordialmente do fato de que esse regime:",
        "Tinha se recusado a construir navios de guerra para apoiar generais rebeldes na Sicília.",
        "Condenou à morte por motivos políticos aquele que ele considerava o homem mais justo de seu tempo: Sócrates.",
        "Tinha abolido a cobrança de tributos sobre mercadores que importavam vinhos estrangeiros.",
        "Permitiu que filósofos estrangeiros assumissem o comando dos tribunais judiciais da cidade.",
        "Proibiu as viagens de estudo de jovens atenienses aos centros científicos do Antigo Egito.",
        "B",
        "A injustiça cometida contra Sócrates convenceu Platão de que a pólis estava moralmente adoecida e precisava de reis-filósofos."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "No primeiro momento da saída da caverna, o prisioneiro liberto contempla primeiro as sombras e os reflexos na água antes de olhar o Sol. Essa gradação pedagógica evidencia que:",
        "A visão da verdade exige um processo metódico de adaptação intelectual para não cegar o entendimento do sujeito.",
        "O mundo exterior é composto por ilusões ainda mais enganosas do que as sombras do fundo da caverna.",
        "O ser humano é biologicamente incapaz de contemplar o meio ambiente sem óculos de proteção solar.",
        "A água dos lagos possui propriedades mágicas que curam as dores provocadas pela fogueira subterrânea.",
        "O filósofo deve abandonar a busca da verdade e contentar-se com os reflexos superficiais da matéria.",
        "A",
        "A libertação cognitiva não ocorre por salto instantâneo; requer scaffolding pedagógico e tempo para que a razão suporte a luz plena."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "A teoria platônica da alma (Psyché) tripartite — dividida em racional, irascível e concupiscível — estabelece que a justiça interior do indivíduo é alcançada quando:",
        "Os desejos corporais concupiscíveis governam as decisões de coragem militar da cidade.",
        "A parte racional soberana comanda a coragem e modera os apetites materiais em harmonia.",
        "A cólera impulsiva do peito comanda os pensamentos da cabeça sem consultar a moderação.",
        "O indivíduo renuncia a qualquer reflexão lógica para seguir os impulsos de alimentação e sono.",
        "As três partes da alma guerreiam perpetuamente até a dissolução completa da memória do sujeito.",
        "B",
        "A justiça pessoal espelha a justiça da cidade: a razão deve governar com sabedoria, amparada pela coragem e temperando os apetites."
    ))

    questoes_brutas.append((
        38, "EM13CHS105", "intermediario",
        "No clássico filme Matrix, o personagem Cypher decide trair a tripulação de Morpheus para retornar à simulação computadorizada. Essa atitude ilustra:",
        "A coragem heroica do filósofo que busca libertar seus semelhantes da caverna escura.",
        "A escolha dos prisioneiros platônicos que preferem a ilusão reconfortante das sombras à aspereza do mundo real.",
        "A dedicação altruísta de cientistas que pesquisam curas para doenças genéticas raras.",
        "O compromisso moral irrestrito com as leis civis aprovadas pelos tribunais populares.",
        "A vitória definitiva da razão dialética sobre os ardis retóricos dos sofistas contemporâneos.",
        "B",
        "Cypher verbaliza a preferência pelo autoengano: 'a ignorância é uma bênção', preferindo o bife simulado na Matrix ao deserto do real."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Ao examinar a relação entre o carpinteiro que faz a cama, o pintor que retrata a cama e a Ideia de Cama, Platão demonstra que:",
        "O pintor está mais próximo da verdade do que o carpinteiro por usar tintas coloridas refinadas.",
        "O carpinteiro produz um objeto que participa da Ideia, enquanto o pintor cria uma ilusão imitativa de terceiro grau.",
        "A cama de madeira feita pelo carpinteiro é a essência eterna que jamais poderá ser destruída pelo fogo.",
        "A pintura de uma cama serve como instrumento indispensável para o descanso dos guerreiros na guarda.",
        "Os filósofos devem dedicar seus estudos à fabricação artesanal de móveis domésticos de linho.",
        "B",
        "O marceneiro fabrica uma cópia útil da Forma; o pintor imita apenas a aparência visual dessa cópia, situando-se a dois graus do real."
    ))

    questoes_brutas.append((
        40, "EM13CHS103", "intermediario",
        "A virtude da Dialética em Platão diferencia-se das disputas oratórias dos sofistas porque a dialética platônica:",
        "Tem como finalidade derrotar o oponente para obter aplausos e ganhos financeiros na assembleia.",
        "É um caminho cooperativo e rigoroso da inteligência que busca a essência pura do Ser e a Ideia do Bem.",
        "Proíbe o uso de perguntas e exige que um único orador fale durante várias horas seguidas.",
        "Utiliza fábulas cômicas para entreter os ouvintes e desviar a atenção de problemas éticos sérios.",
        "Depende da força militar de generais para fazer valer suas conclusões perante os tribunais civis.",
        "B",
        "A dialética platônica não é erística (disputa de vaidades), mas o método de ascese intelectual que conduz a alma à verdade do Bem."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # Com resolução detalhada: - **Etapa 1:** ... - **Etapa 2:** ...
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Considere o texto: 'As Ideias não são pensamentos subjetivos da mente humana, mas entidades objetivas, perfeitas e eternas.' A partir dessa tese platônica, conclui-se que a extinção de todos os seres humanos acarretaria:",
        "O desaparecimento imediato da Ideia de Justiça e de todas as leis da geometria pura.",
        "A permanência intacta das Ideias puras no Mundo Inteligível, cuja existência independe de cérebros humanos que as pensem.",
        "A transformação do Mundo Inteligível em um caos material desprovido de qualquer proporção matemática.",
        "O retorno do cosmos às águas caóticas de Nun sem possibilidade de nova reorganização física.",
        "A queima definitiva dos monumentos da Academia de Atenas por tempestades elétricas solares.",
        "B",
        "- **Etapa 1:** Compreensão da teoria platônica das Formas. As Ideias (Eidos) não são conceitos mentais ou representações psicológicas subjetivas; possuem existência objetiva em si mesmas (realismo das Ideias).\n- **Etapa 2:** Dedução lógica sobre a independência das essências. Mesmo sem mentes humanas no mundo físico, a verdade de que a soma dos ângulos de um triângulo é 180 graus e a Ideia de Bem continuam existindo eternamente no plano inteligível."
    ))

    questoes_brutas.append((
        42, "EM13CHS103", "dificil",
        "Na Alegoria da Caverna, o prisioneiro libertado é arrastado por uma subida 'áspera e íngreme'. Sob a perspectiva pedagógica da Paideia platônica, essa metáfora traduz:",
        "A facilidade do aprendizado escolar quando mediado por brincadeiras lúdicas infantis.",
        "A exigência de esforço rigoroso e por vezes desconfortável para superar preconceitos imediatos e conquistar o pensamento conceitual.",
        "A obrigação cívica de construir estradas de pedra para facilitar a marcha das tropas de infantaria.",
        "A recusa dos filósofos em aceitar estudantes que não possuam preparo físico atlético para corridas.",
        "A impossibilidade de libertar os cidadãos que trabalham em atividades manuais nas oficinas da pólis.",
        "B",
        "- **Etapa 1:** Interpretação da metáfora da subida íngreme da caverna. O caminho em direção à luz exterior não é um passeio suave, mas um percurso árduo que exige esforço, disciplina e ruptura com o comodismo sensorial.\n- **Etapa 2:** Aplicação educacional. A formação humanística autêntica (Paideia) demanda dedicação intelectual e desacomodação crítica; o estudante precisa superar a inércia dos preconceitos fáceis para ascender ao rigor dos conceitos abstratos."
    ))

    questoes_brutas.append((
        43, "EM13CHS105", "dificil",
        "Em redes digitais, usuários frequentemente rejeitam evidências empíricas consolidadas por cientistas para acreditar em teorias conspiratórias hiper-realistas. Esse fenômeno repete a tragédia da caverna platônica porque:",
        "As pessoas preferem a ilusão reconfortante das sombras que confirmam suas paixões ao esforço analítico de encarar a complexidade do real.",
        "Os cientistas contemporâneos recusam o uso da internet para divulgar artigos em revistas especializadas.",
        "A inteligência artificial foi programada para eliminar todos os dados matemáticos dos servidores mundiais.",
        "Os cidadãos perderam a capacidade biológica de enxergar imagens emitidas por telas de computadores.",
        "As leis das democracias ocidentais proíbem a leitura de textos clássicos em universidades públicas.",
        "A",
        "- **Etapa 1:** Diagnóstico sociotécnico contemporâneo. Algoritmos e deepfakes geram simulações envolventes que reforçam preconceitos e paixões imediatas da audiência em bolhas digitais.\n- **Etapa 2:** Conexão com o drama dos prisioneiros acorrentados. Assim como na caverna de Platão, os indivíduos apegam-se às sombras familiares e zombam de quem tenta libertá-los com a luz dos fatos, preferindo a comodidade do autoengano ao desafio da verdade."
    ))

    questoes_brutas.append((
        44, "EM13CHS101", "dificil",
        "Ao examinar a teoria da reminiscência no Mênon, constata-se que o escravo resolve o problema da duplicação do quadrado sem ter estudado matemática. Essa experiência visa demonstrar que:",
        "O escravo possuía poderes de adivinhação concedidos em rituais religiosos no templo de Delfos.",
        "A verdade matemática não é inventada pela experiência sensorial empírica, mas descoberta na própria razão como recordação da alma.",
        "Os generais atenienses deveriam libertar todos os escravos para atuarem como professores de geometria.",
        "As figuras geométricas desenhadas na areia têm vida própria e corrigem os erros cometidos pelos mestres.",
        "A educação militar de Esparta era superior aos debates dialógicos praticados nas praças de Atenas.",
        "B",
        "- **Etapa 1:** Análise do experimento socrático com o jovem escravo no Mênon. Sócrates não ensina teoremas nem fornece fórmulas prontas; ele faz apenas perguntas que orientam o raciocínio dedutivo do jovem.\n- **Etapa 2:** Validação da tese da Anamnese. Ao chegar à resposta correta por dedução interior, o escravo comprova que os fundamentos da geometria já residiam em sua alma racional, necessitando apenas do estímulo maiêutico para serem recordados."
    ))

    questoes_brutas.append((
        45, "EM13CHS103", "dificil",
        "A condenação moral e política do filósofo que retorna à caverna estabelece que o compromisso da filosofia não é a fuga individualista para um paraíso contemplativo, mas sim:",
        "O dever inegociável de atuar politicamente na cidade para emancipar os concidadãos e governar segundo a justiça e o Bem.",
        "A fundação de bancos comerciais para financiar campanhas eleitorais de marinheiros no porto de Pireu.",
        "O apoio incondicional a regimes de tirania militar que usem a força para silenciar dissidentes cívicos.",
        "O isolamento em mosteiros rurais distantes para preservar a pureza de livros raros em pergaminho.",
        "A cobrança de ingressos para permitir que moradores da cidade visitem as colunatas da Academia.",
        "A",
        "- **Etapa 1:** Identificação do imperativo ético da Alegoria da Caverna. Platão não permite que o sábio desfrute egoisticamente da luz do Sol na superfície; ele impõe o retorno obrigatório à escuridão da caverna.\n- **Etapa 2:** Síntese sobre a missão da filosofia política. O verdadeiro filósofo não busca o refúgio na contemplação privada; sua vocação culmina na responsabilidade cívica de transformar a pólis, arriscando a própria vida para libertar a comunidade da ignorância e da injustiça."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Na Linha Dividida, a distinção entre a Dianoia e a Noesis reside no fato de que a Dianoia parte de hipóteses e utiliza apoios sensíveis, ao passo que a Noesis:",
        "Dispensa qualquer imagem sensível e ascende dialeticamente de Ideia em Ideia até o princípio absoluto incondicionado do Bem.",
        "Depende de cálculos astronômicos realizados em noites de lua cheia nas praias do mar Egeu.",
        "É uma técnica retórica desenvolvida por Górgias para persuadir jurados em litígios de herança.",
        "Limita-se a descrever os hábitos de alimentação e sono dos animais domésticos no interior.",
        "Submete as verdades da matemática aos decretos aprovados pelos senadores da assembleia popular.",
        "A",
        "- **Etapa 1:** Exame dos dois patamares do Mundo Inteligível na Linha Dividida de A República. A matemática (Dianoia) toma postulados e axiomas como certos e desenha figuras visíveis como suporte auxiliar.\n- **Etapa 2:** Caracterização da intuição dialética (Noesis). A Noesis trata as hipóteses apenas como degraus provisórios para alcançar o fundamento absoluto (a Ideia do Bem), operando no plano puramente inteligível das essências sem qualquer muleta sensorial."
    ))

    questoes_brutas.append((
        47, "EM13CHS105", "dificil",
        "Ao transpor a teoria platônica para o filme Matrix, a 'pílula vermelha' ingerida por Neo representa simbolicamente:",
        "A aceitação passiva dos prazeres de consumo imediato proporcionados pela sociedade industrial.",
        "A ruptura dolorosa com a ilusão do mundo sensível e a decisão ética de encarar a verdade objetiva da realidade.",
        "Um composto químico fabricado por máquinas inteligentes para apagar as memórias rebeldes do cérebro.",
        "O pacto secreto firmado entre navegadores do espaço e líderes de governos autoritários terrestres.",
        "O encerramento de qualquer investigação científica em benefício da fé cega em profecias religiosas.",
        "B",
        "- **Etapa 1:** Interpretação da escolha da pílula vermelha em contraste com a pílula azul no filme Matrix. A pílula azul preserva a ignorância confortável da simulação sensorial; a pílula vermelha arranca o sujeito da docilização da Matrix.\n- **Etapa 2:** Correspondência com a filosofia de Platão. O ato de Neo personifica o desacorrentamento do prisioneiro da caverna: romper com a ilusão da Doxa exige coragem existencial para enfrentar o deserto do real e assumir a responsabilidade pela emancipação coletiva."
    ))

    questoes_brutas.append((
        48, "EM13CHS101", "dificil",
        "No Livro X de A República, Platão acusa os poetas imitativos de estarem 'a três graus de distância da verdade'. O fundamento conceitual dessa crítica estética reside em afirmar que:",
        "Os poetas cobram cachês muito elevados para recitar seus versos em praças públicas da cidade.",
        "O poeta imita a aparência visual de objetos sensíveis concretos, os quais já são cópias imperfeitas das Ideias eternas.",
        "As tragédias gregas foram escritas em línguas bárbaras que deformaram o vocabulário filosófico da pólis.",
        "Os atores de teatro recusavam o uso de máscaras cênicas durante as festividades cívicas da primavera.",
        "A poesia épica defendia a abolição da moeda cunhada e o retorno ao comércio de escambo tradicional.",
        "B",
        "- **Etapa 1:** Compreensão da hierarquia da representação em Platão. No topo está a Ideia pura (criada pelo divino); no segundo grau está o artefato material feito pelo artífice (que participa da Ideia); no terceiro grau está a pintura ou poema imitativo.\n- **Etapa 2:** Conclusão crítica sobre a mímesis. A arte poética e visual mimética é cópia da cópia (fantasma de uma sombra); ao fixar os olhos humanos na aparência de segundo nível, afasta a alma da verdade das Formas inteligíveis e alimenta paixões acríticas."
    ))

    questoes_brutas.append((
        49, "EM13CHS103", "dificil",
        "A sofocracia platônica propõe que o poder político não deve pertencer à maioria despreparada nem aos homens mais ricos, mas àqueles que:",
        "Dominam a arte de inventar notícias falsas para acalmar rebeliões populares nos portos da cidade.",
        "Alcançaram o conhecimento da Ideia do Bem e possuem desprendimento moral das riquezas materiais e honras mundanas.",
        "Possuem frotas de embarcações de guerra capazes de impor tributos armados a cidades costeiras rivais.",
        "Conquistaram medalhas de ouro em três edições consecutivas dos jogos olímpicos de atletismo.",
        "Recusam o diálogo com a juventude para preservar os segredos das leis em cofres de santuários sagrados.",
        "B",
        "- **Etapa 1:** Análise do fundamento da legitimidade do governante em Platão. Nem a força das armas (timocracia), nem o dinheiro (oligarquia), nem o capricho da massa sem preparo (democracia desvirtuada) garantem a justiça do Estado.\n- **Etapa 2:** Síntese da tese do Rei-Filósofo. Apenas quem contemplou a Ideia do Bem (Noesis) conhece a medida objetiva do justo e, não cobiçando privilégios pessoais ou propriedades privadas, governa a pólis com sabedoria imparcial e dedicação integral ao bem comum."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "Ao afirmar que 'conhecer é recordar', Platão rejeita a tese de que a mente humana nasce como uma folha em branco (tábula rasa). Essa recusa fundamenta-se na certeza de que:",
        "Os bebês aprendem a falar línguas estrangeiras logo nos primeiros dias de vida sem ouvir adultos.",
        "A alma racional é imortal e traz em si mesma, de forma inata e latente, os conceitos universais contemplados na eternidade.",
        "Os professores têm o dever de punir com castigos físicos as crianças que erram contas de divisão.",
        "O cérebro humano é incapaz de absorver novas impressões empíricas transmitidas pelos órgãos sensoriais.",
        "Todas as teorias científicas foram ditadas diretamente aos filósofos por deuses olímpicos em sonhos.",
        "B",
        "- **Etapa 1:** Confronto entre o inatismo platônico e o empirismo da tábula rasa. Se a mente fosse vazia e dependesse apenas dos dados sensíveis imperfeitos e mutáveis, jamais poderia conceber a perfeição absoluta e necessária da matemática ou da justiça em si.\n- **Etapa 2:** Fundamentação da Anamnese. A mente reconhece a perfeição porque sua alma já a contemplou no Hiperurânio antes de encarnar; os dados sensíveis funcionam como gatilhos mnemônicos que ativam o saber inato adormecido."
    ))

    questoes_brutas.append((
        51, "EM13CHS103", "dificil",
        "A imagem platônica dos homens manipulando estátuas atrás do muro baixo na caverna desmascara qual engrenagem da vida política em sociedades desiguais?",
        "O trabalho digno de artesãos dedicados à construção de casas confortáveis para famílias camponesas.",
        "A atuação de grupos de interesse que projetam narrativas artificiais e imagens sedutoras para controlar a opinião coletiva.",
        "A bravura de guardas municipais que arriscam suas vidas para patrulhar praças públicas durante a noite.",
        "A cooperação fraterna entre cidades marítimas que dividem seus estoques de azeite em épocas de escassez.",
        "A necessidade de utilizar bonecos de madeira para ensinar matemática a jovens nas escolas primárias.",
        "B",
        "- **Etapa 1:** Interpretação da figura dos manipuladores de marionetes na caverna. Eles não estão acorrentados; caminham por trás do biombo exibindo artefatos para que suas sombras sejam projetadas na parede diante dos prisioneiros.\n- **Etapa 2:** Crítica política e ideológica. Trata-se da antecipação da manipulação das massas por elites retóricas e marqueteiros: aqueles que detêm o controle dos meios de difusão de imagens governam a mente dos acorrentados, mantendo-os cativos de falsas percepções."
    ))

    questoes_brutas.append((
        52, "EM13CHS101", "dificil",
        "Considere o paradoxo platônico: o filósofo liberto, ao descer à caverna, parece ridículo e desastrado aos olhos dos prisioneiros. Esse descompasso ocorre porque:",
        "O filósofo perdeu sua memória e esqueceu completamente a língua falada pelos cidadãos de Atenas.",
        "Seus olhos acostumados à luz solar da verdade ficam temporariamente ofuscados pela escuridão e pela baixeza das disputas superficiais da caverna.",
        "Os prisioneiros dominam teorias astronômicas avançadas que o filósofo desconhece por ter passado anos estudando geometria.",
        "O filósofo tenta roubar os artefatos de pedra transportados atrás do muro para vendê-los em portos estrangeiros.",
        "As leis da pólis proibiam que homens livres conversassem com prisioneiros condenados por crimes de sangue.",
        "B",
        "- **Etapa 1:** Análise da adaptação visual regressiva na caverna. Ao retornar da luz ofuscante do Sol para o breu subterrâneo, os olhos do filósofo precisam de tempo para se acostumar novamente à escuridão.\n- **Etapa 2:** Significado formativo e social. Aquele que contempla os princípios eternos da justiça e da virtude parece ingênuo e inábil nas pequenas artimanhas, fraudes e disputas egoístas do cotidiano medíocre, sendo ridicularizado por quem vive preso às aparências."
    ))

    questoes_brutas.append((
        53, "EM13CHS105", "dificil",
        "Em discussões pedagógicas sobre evasão escolar, educadores apontam que a busca por gratificações imediatas em redes sociais afasta os jovens do estudo aprofundado. Esse dilema ilustra a tese de Platão de que:",
        "A educação requer o esforço de conversão da alma, que liberta o sujeito das ilusões fáceis para capacitá-lo a pensar por conceitos.",
        "As escolas devem fechar suas portas e permitir que os alunos aprendam tudo em jogos de videogame comerciais.",
        "Os jovens do Ensino Médio são biologicamente incapazes de compreender teoremas geométricos abstratos.",
        "A leitura de livros de literatura deve ser substituída pela exibição contínua de vídeos curtos em sala de aula.",
        "Apenas os filhos de famílias nobres têm o direito de aprender disciplinas teóricas em instituições públicas.",
        "A",
        "- **Etapa 1:** Diagnóstico da sedução do entretenimento imediato. Estímulos sensoriais rápidos alimentam a Doxa e a gratificação passiva dos sentidos, gerando aversão ao esforço reflexivo da leitura densa.\n- **Etapa 2:** Resposta da Paideia platônica. A educação autêntica não é adestramento de consumo, mas conversão da alma (periagoge): arrancar o jovem das amarras da passividade para que conquiste a autonomia intelectual e a nobreza moral do saber verdadeiro."
    ))

    questoes_brutas.append((
        54, "EM13CHS101", "dificil",
        "Santo Agostinho reinterpretou o Mundo das Ideias platônico no contexto do pensamento cristão medieval sustentando que as Ideias eternas:",
        "Foram fabricadas por artesãos gregos que fundiram metais em fornalhas no alto de montanhas rochosas.",
        "Residem eternamente na mente de Deus Criador como arquétipos perfeitos segundo os quais Ele ordenou a criação do Universo.",
        "Desapareceram completamente após a condenação de Sócrates pelos juízes do tribunal popular de Atenas.",
        "São alucinações passageiras provocadas por febres que atacam viajantes que navegam pelo mar Egeu.",
        "Devem ser destruídas pela igreja para evitar que os fiéis aprendam teoremas de geometria demonstrativa.",
        "B",
        "- **Etapa 1:** Exame da recepção do platonismo na filosofia patrística de Santo Agostinho. Agostinho reconheceu a profundidade do dualismo platônico, mas cristianizou a morada suprassensível das Formas puras.\n- **Etapa 2:** Síntese teológica agostiniana. As Ideias imutáveis (Justiça, Bem, Verdade) não habitam um Hiperurânio impessoal autônomo, mas constituem as razões eternas (rationes aeternae) presentes na própria sabedoria do Logos divino criador."
    ))

    questoes_brutas.append((
        55, "EM13CHS103", "dificil",
        "Na Carta VII, Platão afirma que a legislação de todas as cidades de seu tempo era 'quase incurável sem uma maravilhosa reforma aliada à boa fortuna'. Essa constatação fundamentou sua recusa em participar da política prática de Atenas para dedicar-se a:",
        "Organizar expedições militares de pirataria no mar Mediterrâneo para saquear embarcações fenícias.",
        "Fundar a Academia como centro de formação moral e filosófica dos futuros governantes justos da civilização grega.",
        "Compor comédias teatrais para ridicularizar os magistrados que atuavam no tribunal popular da Helieia.",
        "Comprar grandes propriedades agrícolas no sul da Itália para enriquecer com o comércio de vinhos e azeite.",
        "Defender réus culpados em julgamentos cívicos em troca de doações financeiras para sua família.",
        "B",
        "- **Etapa 1:** Interpretação da trajetória biográfica e política de Platão após o trauma de 399 a.C. Platão percebeu a inutilidade de disputar cargos em governos corruptos e instáveis sem uma prévia transformação dos homens.\n- **Etapa 2:** Criação da Academia como projeto institucional. A fundação da Academia de Atenas foi a concretização pedagógica de seu ideal: criar uma comunidade de pesquisa racional e moral para formar estadistas que governassem com justiça."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Ao examinar a relação entre a Beleza das coisas sensíveis e a Ideia de Beleza em si, Platão observa no diálogo Banquete que o amor (Eros) deve orientar a alma a:",
        "Fixar-se perpetuamente na contemplação de um único corpo jovem e belo para desfrutar de prazeres carnais.",
        "Ascender dos belos corpos materiais para a beleza das condutas éticas, das ciências e, finalmente, para a Beleza em si.",
        "Destruir todas as esculturas de mármore que retratem divindades em praças públicas da cidade de Atenas.",
        "Recusar o convívio comunitário para viver em embarcações de pesca isoladas em alto-mar durante o inverno.",
        "Submeter as escolhas afetivas às decisões tomadas por generais condecorados em assembleias populares.",
        "B",
        "- **Etapa 1:** Análise da dialética ascensional do amor no Banquete. Eros não é mera pulsão corporal bruta, mas o anseio da alma humana pela beleza e pela imortalidade que transcende a matéria perecível.\n- **Etapa 2:** Degraus da ascese estética e intelectual. A alma deve usar a beleza corporal como trampolim inicial para reconhecer a beleza das almas, a beleza das leis justas e das ciências, até alcançar a contemplação da Beleza suprema em si."
    ))

    questoes_brutas.append((
        57, "EM13CHS105", "dificil",
        "A alegoria da caverna platônica desmente a concepção comum de que o saber é uma posse individual para benefício egoísta, porque estabelece que:",
        "O homem liberto só tem valor civil se utilizar a ciência para enriquecer rapidamente no comércio marítimo.",
        "A verdadeira sabedoria culmina na responsabilidade moral e na solidariedade ativa com a libertação de toda a comunidade.",
        "Os governantes da pólis devem guardar os teoremas de geometria em segredo absoluto para evitar revoltas populares.",
        "Os cidadãos instruídos têm o direito de escravizar os moradores da caverna para explorar sua mão de obra braçal.",
        "A contemplação da verdade dispensa qualquer cuidado com o cumprimento de leis justas na vida comunitária.",
        "B",
        "- **Etapa 1:** Julgamento ético da conclusão da Alegoria da Caverna. Se a sabedoria fosse vaidade individualista, o filósofo permaneceria na luz contemplando as maravilhas da superfície ensolarada sem se importar com os outros.\n- **Etapa 2:** Síntese da virtude cívica platônica. A emancipação da razão só adquire sentido ético pleno quando posta a serviço do bem comum; descer à caverna para iluminar os acorrentados é o imperativo supremo da justiça."
    ))

    questoes_brutas.append((
        58, "EM13CHS101", "dificil",
        "Na Linha Dividida, a passagem da Doxa (opinião) para a Episteme (ciência) marca a fronteira conceitual entre:",
        "O conhecimento de fórmulas de navegação fenícia e a escrita de poemas satíricos em peças de teatro da cidade.",
        "O saber instável sobre coisas materiais perecíveis e o conhecimento demonstrativo necessário de essências eternas e imutáveis.",
        "A leitura de tratados de história geral e a memorização de discursos de generais em tribunais de julgamento militar.",
        "A obediência cega a mandamentos de reis absolutistas e a submissão aos conselhos de adivinhos em praça aberta.",
        "O uso de moedas de prata nas feiras municipais e a troca direta de sacas de cevada nos portos mercantes.",
        "B",
        "- **Etapa 1:** Definição da fronteira central da Linha Dividida no Livro VI de A República. A Doxa engloba Eikasia e Pistis no mundo sensível; a Episteme engloba Dianoia e Noesis no mundo inteligível.\n- **Etapa 2:** Significado conceitual da ruptura. Romper com a Doxa significa ultrapassar o fluxo empírico mutável para atingir o saber rigoroso, universal e imutável que se sustenta pela demonstração racional das Formas puras."
    ))

    questoes_brutas.append((
        59, "EM13CHS103", "dificil",
        "A crítica platônica à democracia ateniense (onde todos os cidadãos votavam indistintamente sobre todos os temas) comparava a cidade a um navio em alto-mar, argumentando que:",
        "O comando da embarcação deve ser sorteado entre os passageiros mais ricos e com roupas luxuosas.",
        "A pilotagem de um navio em tempestade exige perícia técnica de navegação, e não a gritaria da maioria despreparada.",
        "Os marinheiros devem queimar os lemes e deixar que as correntes marinhas decidam o destino da viagem.",
        "As decisões sobre rotas náuticas devem ser tomadas exclusivamente por crianças que viajam no porão.",
        "A tripulação deve jogar o capitão ao mar sempre que houver ventos contrários soprando do norte.",
        "B",
        "- **Etapa 1:** Interpretação da metáfora da nau do Estado em A República (Livro VI). Platão questiona: numa tempestade em alto-mar, confiaríamos o leme a uma eleição de marinheiros embriagados ou ao piloto com conhecimentos de astronomia e ventos?\n- **Etapa 2:** Conclusão política da analogia. A condução da pólis em direção à justiça exige saber especializado e discernimento moral (Sofocracia); deixar o destino da comunidade ao capricho da massa desinformada conduz ao naufrágio coletivo."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "Ao sintetizar a Teoria das Ideias e a Alegoria da Caverna, constata-se que o idealismo platônico estruturou o pensamento ocidental ao propor que:",
        "A matéria sensível palpável é a única e absoluta realidade existente, devendo a razão rejeitar qualquer conceito abstrato.",
        "A verdadeira realidade e a dignidade do humano residem na capacidade de transcender as aparências materiais para guiar-se pela luz da razão e do Bem.",
        "Os homens devem aceitar com resignação a condição de prisioneiros acorrentados, pois a busca da verdade gera sofrimento inútil.",
        "O valor das ciências da natureza depende da quantidade de ouro acumulada nos cofres de templos sagrados de Delfos.",
        "A vida na cidade dispensa a obediência a princípios morais universais desde que a economia comercial seja lucrativa.",
        "B",
        "- **Etapa 1:** Avaliação sintética do projeto filosófico de Platão. Platão enfrenta o ceticismo e o relativismo pragmático dos sofistas propondo uma arquitetura metafísica e moral sólida.\n- **Etapa 2:** Legado perene para a civilização. O platonismo ensina que o homem não está condenado às sombras da ignorância e da barbárie; pela educação rigorosa (Paideia) e pelo compromisso com o Bem, a razão humana pode romper as amarras e construir uma vida pessoal e coletiva digna e justa."
    ))

    # Balanceamento perfeito
    questoes = balancear_questoes(questoes_brutas)

    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('objeto_de_conhecimento: "O Dualismo Ontológico e Epistemológico Platônico: Mundo Sensível (Mutável, Ilusório, Acessível pelos Sentidos, Fonte de Opinião/Doxa) vs. Mundo Inteligível (Eterno, Imutável, Acessível Apenas pelo Intelecto, Sede da Verdade/Episteme); A Teoria da Reminiscência (Anamnese); A Alegoria da Caverna (A República, Livro VII): A Ilusão das Sombras, O Processo Educativo como Desacorrentamento e o Papel Crítico do Filósofo na Libertação Coletiva."')
    md.append('ebook_fonte: "em-fil-c04-platao-mundo-ideias-caverna.md"')
    md.append('habilidades: "EM13CHS101, EM13CHS103, EM13CHS104, EM13CHS105, H1, H2, H11"')
    md.append("total_exercicios: 60")
    md.append("distribuicao:")
    md.append("  basico: 20")
    md.append("  intermediario: 20")
    md.append("  dificil: 20")
    md.append("---")
    md.append("")
    md.append("# Exercícios — Platão: O Idealismo, A Teoria das Ideias e a Alegoria da Caverna")
    md.append("")
    md.append("## Nível Básico (Questões 1 a 20)")
    md.append("")

    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: platao-mundo-ideias-caverna -->")
        md.append(f"### Questão {num}")
        md.append("")
        md.append(enunc)
        md.append("")
        md.append(f"a) {a}")
        md.append(f"b) {b}")
        md.append(f"c) {c}")
        md.append(f"d) {d}")
        md.append(f"e) {e}")
        md.append("")
        md.append(f"**Gabarito:** {gab}")
        md.append(f"**Resolução:** {res}")
        md.append("")

    md.append("## Nível Intermediário (Questões 21 a 40)")
    md.append("")

    for q in questoes[20:40]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: platao-mundo-ideias-caverna -->")
        md.append(f"### Questão {num}")
        md.append("")
        md.append(enunc)
        md.append("")
        md.append(f"a) {a}")
        md.append(f"b) {b}")
        md.append(f"c) {c}")
        md.append(f"d) {d}")
        md.append(f"e) {e}")
        md.append("")
        md.append(f"**Gabarito:** {gab}")
        md.append(f"**Resolução:** {res}")
        md.append("")

    md.append("## Nível Difícil (Questões 41 a 60)")
    md.append("")

    for q in questoes[40:]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: platao-mundo-ideias-caverna -->")
        md.append(f"### Questão {num}")
        md.append("")
        md.append(enunc)
        md.append("")
        md.append(f"a) {a}")
        md.append(f"b) {b}")
        md.append(f"c) {c}")
        md.append(f"d) {d}")
        md.append(f"e) {e}")
        md.append("")
        md.append(f"**Gabarito:** {gab}")
        md.append("**Resolução Detalhada:**")
        md.append(res)
        md.append("")

    md.append("## Referências")
    md.append("")
    md.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.")
    md.append("- CHAUÍ, Marilena. *Introdução à História da Filosofia: Dos Pré-Socráticos a Aristóteles*. 2. ed. São Paulo: Companhia das Letras, 2002. v. 1.")
    md.append("- JAEGER, Werner. *Paideia: A Formação do Homem Grego*. Tradução de Artur M. Parreira. 4. ed. São Paulo: Martins Fontes, 2001.")
    md.append("- MARCONDES, Danilo. *Iniciação à História da Filosofia: Dos Pré-Socráticos a Wittgenstein*. 11. ed. Rio de Janeiro: Jorge Zahar, 2007.")
    md.append("- PLATÃO. *A República*. Tradução de Maria Helena da Rocha Pereira. 9. ed. Lisboa: Fundação Calouste Gulbenkian, 2000.")
    md.append("- PLATÃO. *Mênon*. Tradução de Maura Iglesias. Rio de Janeiro: Editora PUC-Rio/Loyola, 2001.")
    md.append("- REALE, Giovanni. *História da Filosofia Antiga: Platão e Aristóteles*. Tradução de Henrique C. de Lima Vaz e Marcelo Perine. 3. ed. São Paulo: Loyola, 2007. v. 2.")
    md.append("- ROSS, David. *Plato's Theory of Ideas*. Westport: Greenwood Press, 1976.")
    md.append("")

    conteudo = "\n".join(md)

    # 1. Auditoria Preventiva de Gabaritos
    gabs = re.findall(r'\*\*Gabarito:\*\*\s*([A-E])', conteudo)
    print(f"Total de Gabaritos detectados: {len(gabs)}")
    counts = Counter(gabs)
    print(f"Contagem por letra: {counts}")
    if len(gabs) != 60:
        print(f"[ERRO CRÍTICO] Total de questões diferente de 60: {len(gabs)}")
        sys.exit(1)
    for letra in ['A', 'B', 'C', 'D', 'E']:
        qtd = counts.get(letra, 0)
        if qtd != 12:
            print(f"[ERRO CRÍTICO] Letra {letra} com {qtd} ocorrências (esperado 12)!")
            sys.exit(1)

    # 2. Auditoria Preventiva de R$
    if "R$" in conteudo:
        print("[ERRO CRÍTICO] Símbolo 'R$' detectado no conteúdo gerado!")
        sys.exit(1)

    # 3. Auditoria Preventiva de Termos Pedantes / Proibidos
    texto_sem_yaml = re.sub(r'^---.*?---\n', '', conteudo, flags=re.DOTALL) if conteudo.startswith('---') else conteudo
    corpo_questoes = texto_sem_yaml.split("## Referências")[0]
    padroes_pedantes = [
        r"\bsupracitad[oa]s?\b", r"\boutrossim\b", r"\bdestarte\b", r"\bprecípu[oa]s?\b",
        r"\bconsubstancia\w*\b", r"\bdepreende-se\b", r"\bassertiva\b", r"\bmormente\b",
        r"\bno\s+tocante\s+a\b", r"\batinente\w*\b", r"\bconcernente\w*\b", r"\bdirimir\b",
        r"\benseja\w*\b", r"\bauferir\b", r"\bprescind\w*\b", r"\bimprescind\w*\b",
        r"\binexor\w*\b", r"\bidiossincra\w*\b", r"\banátema\b", r"\bprerrogativa\w*\b",
        r"\bcorrobor\w*\b", r"\bintrínsec[oa]s?\b", r"\bextrínsec[oa]s?\b", r"\bdicotomi\w*\b",
        r"\bsubjacente\w*\b", r"\befêmer[oa]s?\b", r"\bmitigar\b", r"\bfomentar\b",
        r"\bhegemônic\w*\b", r"\bepistemológic\w*\b", r"\bontológic\w*\b", r"\baxiológic\w*\b",
        r"\bteleológic\w*\b", r"\bhermenêutic\w*\b", r"\bpropedêutic\w*\b", r"\bvernáculo\b"
    ]
    for pat in padroes_pedantes:
        m = re.search(pat, corpo_questoes, re.IGNORECASE)
        if m:
            print(f"[ERRO CRÍTICO] Termo proibido detectado: '{m.group(0)}'!")
            sys.exit(1)

    print("[AUDITORIA INTERNA APROVADA] Todas as 60 questões atendem rigorosamente às travas pedagógicas!")

    # Escrever no rascunho temporário
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"Rascunho temporário salvo com sucesso ({len(conteudo)} bytes).")

    # Invocar o validador educamob
    cmd = [sys.executable, "validador_educamob.py", temp_draft, dest_path]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 04 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    gerar_cap04()
