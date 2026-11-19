# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 33 de Filosofia EM:
As Raízes do Existencialismo: Kierkegaard e Sartre
Objeto: cap-33-raizes-existencialismo-kierkegaard-sartre
Total: 60 questões atômicas (20 básicas, 20 intermediárias, 20 difíceis)
Gabarito balanceado: 12 A, 12 B, 12 C, 12 D, 12 E
ABERTURA HISTÓRICA DO EIXO V: EXISTENCIALISMO, DIFERENÇA E SABERES TRADICIONAIS!
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
        "Qual filósofo dinamarquês do século dezenove é considerado o precursor do existencialismo ao defender o Indivíduo Singular contra o sistema hegeliano?",
        [
            ("Søren Kierkegaard, pensador que criticou a abstração lógica do idealismo e formulou a subjetividade como verdade.", True),
            ("Arthur Schopenhauer, filósofo que concebeu o universo como manifestação cega da Vontade cósmica irracional.", False),
            ("Friedrich Nietzsche, autor que anunciou a morte de Deus e proclamou a transvaloração dos valores morais.", False),
            ("Karl Marx, teórico que interpretou a história humana a partir do materialismo dialético e da luta de classes.", False),
            ("Auguste Comte, pensador francês que fundou a doutrina positivista da ciência social moderna.", False)
        ],
        "Søren Kierkegaard combateu o sistema hegeliano, resgatando a angústia e a singularidade da existência individual diante do Absoluto."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Como Kierkegaard denomina os três estádios no caminho da vida pelos quais a subjetividade humana pode transitar?",
        [
            ("O estádio mitológico, o estádio metafísico e o estádio positivo da ciência.", False),
            ("O estádio estético, o estádio ético e o estádio religioso da existência.", True),
            ("O estádio sensorial, o estádio conceitual e o estádio dialético do saber.", False),
            ("O estádio inconsciente, o estádio pré-consciente e o estádio consciente do ego.", False),
            ("O estádio pré-socrático, o estádio clássico ateniense e o estádio helenístico imperial.", False)
        ],
        "Kierkegaard estruturou as três esferas existenciais da experiência humana em: estádio estético, estádio ético e estádio religioso."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "Qual proposição central sintetiza o princípio fundamental do existencialismo ateu de Jean-Paul Sartre?",
        [
            ("A essência determina antecipadamente as ações concretas de todos os seres vivos no cosmos.", False),
            ("A razão pura precede os dados dos sentidos na estruturação do conhecimento transcendental.", False),
            ("A existência precede a essência, significando que o ser humano primeiro existe e depois se define por seus atos.", True),
            ("A matéria econômica condiciona de modo mecânico todas as escolhas espirituais da consciência.", False),
            ("A harmonia universal pré-estabelecida por Deus organiza o destino moral das sociedades terrenas.", False)
        ],
        "Para Sartre, a existência precede a essência: o ser humano surge no mundo sem uma natureza prévia e constrói quem ele é através de seus projetos."
    ))

    questoes_brutas.append((
        4, "EM13CHS502", "basico",
        "Na obra O Conceito de Angústia de Kierkegaard, qual é a diferença elementar entre o medo e a angústia?",
        [
            ("O medo é uma experiência mental irreal, enquanto a angústia decorre de lesões cerebrais diagnosticáveis.", False),
            ("O medo afeta apenas crianças pequenas, ao passo que a angústia se restringe a idosos solitários.", False),
            ("O medo decorre de pecados cometidos no passado, enquanto a angústia antecipa punições da justiça civil.", False),
            ("O medo possui um objeto empírico determinado, enquanto a angústia defronta-se com o Nada e com a pura possibilidade da liberdade.", True),
            ("O medo decorre do excesso de leituras acadêmicas, ao passo que a angústia resulta do isolamento físico prolongado.", False)
        ],
        "O medo dirige-se a um perigo concreto definido, enquanto a angústia é a vertigem da liberdade diante do abismo de possibilidades sem objeto fixo."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Qual metáfora de fabricação técnica é apresentada por Sartre para exemplificar a situação em que a essência precede a existência?",
        [
            ("A confecção de uma escultura clássica em mármore por um mestre da Renascença.", False),
            ("A fundição de uma moeda imperial em ouro em oficinas controladas pelo tesouro régio.", False),
            ("O plantio de uma semente de oliveira em solos agrícolas preparados para a colheita.", False),
            ("A navegação de uma caravela mercantil em rotas oceânicas previamente mapeadas.", False),
            ("A produção de um corta-papel por um artesão que concebe sua utilidade e forma antes de fabricá-lo.", True)
        ],
        "No caso de ferramentas inanimadas como o corta-papel, o conceito e a utilidade (essência) antecedem a produção material (existência)."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Como Sartre divide as regiões do ser em sua obra-prima O Ser e o Nada publicada em 1943?",
        [
            ("Entre o Ser Em-Si (as coisas opacas e estáticas) e o Ser Para-Si (a consciência humana livre e aberta ao futuro).", True),
            ("Entre o Mundo Sensível das sombras materiais e o Mundo Inteligível das Ideias imutáveis e eternas.", False),
            ("Entre a substância pensante espiritual e a substância extensa corpórea criadas por Deus.", False),
            ("Entre a infraestrutura econômica produtiva e a superestrutura ideológica e jurídica do Estado.", False),
            ("Entre o princípio apolíneo da ordem formal e o princípio dionisíaco da embriaguez desmedida.", False)
        ],
        "Sartre distingue o Ser Em-Si (o ser maciço dos objetos inanimados) do Ser Para-Si (a consciência reflexiva, que é um nada de ser e pura liberdade)."
    ))

    questoes_brutas.append((
        7, "EM13CHS501", "basico",
        "Qual figura mitológica personifica o homem no estádio estético em Ou-Ou de Kierkegaard?",
        [
            ("Prometeu, o titã rebelde que roubou o fogo divino para entregar aos mortais desamparados.", False),
            ("Don Juan, o sedutor que busca o prazer passageiro, a novidade e a fuga do tédio imediato.", True),
            ("Sísifo, o herói condenado pelos deuses a empurrar uma pedra até o cume da montanha.", False),
            ("Édipo, o rei tebano que decifrou o enigma da esfinge e enfrentou a profecia do destino.", False),
            ("Narciso, o jovem que se apaixonou pelo próprio reflexo contemplado nas águas de uma fonte.", False)
        ],
        "Don Juan simboliza o estádio estético em Kierkegaard: a busca constante por sensações fugazes e novas conquistas para evitar o tédio existencial."
    ))

    questoes_brutas.append((
        8, "EM13CHS502", "basico",
        "Em que consiste a atitude psíquica inautêntica denominada má-fé (mauvaise foi) no pensamento sartriano?",
        [
            ("Na fraude comercial planejada para lesar concorrentes financeiros em contratos mercantis.", False),
            ("Na falsificação deliberada de documentos públicos para enganar magistrados em audiências.", False),
            ("Na mentira que a consciência conta a si mesma para fugir da angústia, fingindo ser um objeto determinado sem liberdade.", True),
            ("Na pregação de doutrinas religiosas heréticas em desacordo com as encíclicas pontifícias.", False),
            ("Na espionagem militar realizada por diplomatas em tempo de guerras entre nações soberanas.", False)
        ],
        "A má-fé é o autoengano no qual o ser humano finge para si mesmo que é um ser determinado (em-si), esquivando-se da responsabilidade da liberdade."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Qual personagem bíblico é adotado por Kierkegaard em Temor e Tremor como o cavaleiro da fé do estádio religioso?",
        [
            ("Moisés, ao conduzir o povo hebreu durante a travessia pelo deserto em direção à terra prometida.", False),
            ("Davi, ao derrotar o guerreiro gigante Golias com uma funda nas planícies de Judá.", False),
            ("Salomão, ao proferir sentenças sábias no julgamento da disputa entre as duas mães.", False),
            ("Abraão, ao obedecer à ordem de sacrificar seu filho Isaque no monte Moriá em um salto da fé no absurdo.", True),
            ("Jó, ao suportar chagas corporais e perdas de bens materiais mantendo sua lealdade a Deus.", False)
        ],
        "Abraão é o arquétipo do estádio religioso em Temor e Tremor, realizando o salto da fé que transcende as leis morais humanas perante Deus."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Qual sentença célebre de Sartre expressa a impossibilidade de o ser humano renunciar à sua própria responsabilidade de escolha?",
        [
            ("O homem é o lobo do homem quando vive fora das leis civis do Estado soberano.", False),
            ("Penso, logo existo como substância racional dotada de ideias inatas indubitáveis.", False),
            ("O homem nasce bom, mas a sociedade burguesa e a propriedade privada o corrompem.", False),
            ("Conhece-te a ti mesmo e conhecerás o universo inteiro e a morada dos deuses imortais.", False),
            ("O homem está condenado a ser livre, pois uma vez lançado ao mundo é responsável por tudo o que faz.", True)
        ],
        "Sartre afirma que estamos condenados à liberdade: não podemos nos esquivar de escolher, pois a própria recusa em escolher já constitui uma escolha."
    ))

    questoes_brutas.append((
        11, "EM13CHS501", "basico",
        "Qual exemplo do cotidiano urbano é utilizado por Sartre em O Ser e o Nada para ilustrar a encenação teatral da má-fé?",
        [
            ("O garçom de café que se movimenta com passos rígidos e gestos mecânicos para encenar o papel de um objeto.", True),
            ("O motorista de ônibus que dirige em alta velocidade para cumprir os horários da linha metropolitana.", False),
            ("O carteiro que entrega correspondências em bairros distantes enfrentando chuvas torrenciais.", False),
            ("O alfaiate que costura tecidos de lã com agulhas finas seguindo moldes de revistas francesas.", False),
            ("O jornaleiro que grita as manchetes do dia nas esquinas das avenidas centrais movimentadas.", False)
        ],
        "O garçom de café sartriano exagera os gestos robóticos de sua função, transformando-se voluntariamente em autômato para mascarar sua liberdade de mudar de vida."
    ))

    questoes_brutas.append((
        12, "EM13CHS502", "basico",
        "Na peça Entre Quatro Paredes de Sartre, qual frase icônica sintetiza a experiência da objetificação pelo olhar alheio?",
        [
            ("Tudo o que é sólido desmancha no ar sob o ritmo veloz da produção moderna.", False),
            ("O inferno são os outros, revelando como o olhar alheio nos julga e nos congela em objetos exteriores.", True),
            ("Deus está morto e nós o matamos através da decadência dos nossos valores morais.", False),
            ("A história de todas as sociedades tem sido a história contínua da luta de classes.", False),
            ("A beleza salvará o mundo quando os homens reencontrarem a harmonia com o sagrado.", False)
        ],
        "A frase O inferno são os outros expressa como o olhar do outro nos despoja da soberania do para-si, transformando-nos em objeto julgado e vulnerável."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Como Kierkegaard ilustra a vertigem da angústia ao descrever a experiência de um indivíduo à beira de um abismo rochoso?",
        [
            ("A vertigem de perder bens financeiros acumulados ao longo de décadas de trabalho fabril.", False),
            ("O receio de ser devorado por feras carnívoras que habitam as cavernas profundas da montanha.", False),
            ("A angústia de descobrir que possui a liberdade absoluta de se lançar voluntariamente no precipício.", True),
            ("A dor física causada pela falta de oxigênio em altitudes elevadas nas cadeias de montanhas.", False),
            ("O desespero de perceber que a descida do penhasco exigirá equipamentos de ferro e cordas.", False)
        ],
        "A angústia no abismo decorre da súbita descoberta da própria liberdade: nada no universo impede a pessoa de se atirar no vazio se assim ela decidir."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "O que caracteriza a existência humana no estádio ético descrito por Kierkegaard através da figura do juiz Wilhelm?",
        [
            ("A vida guiada pela busca irresponsável de novidades sensuais e aventuras amorosas passageiras.", False),
            ("A submissão voluntária ao dever moral, às leis civis, ao casamento e às obrigações perante a comunidade.", True),
            ("A renúncia a qualquer regra social em favor de peregrinações místicas em ermos desérticos.", False),
            ("A dedicação exclusiva à pesquisa científica de laboratório sem contato com a vida social da cidade.", False),
            ("A aceitação cega de dogmas supersticiosos transmitidos por lendas orais sem respaldo racional.", False)
        ],
        "O estádio ético estrutura-se em torno do dever, da responsabilidade social, da constância do casamento e do respeito às normas civis comunitárias."
    ))

    questoes_brutas.append((
        15, "EM13CHS501", "basico",
        "Segundo Jean-Paul Sartre, por qual razão o ser humano, ao escolher a si mesmo, está simultaneamente escolhendo para toda a humanidade?",
        [
            ("Porque as escolhas individuais são votadas em plebiscitos universais supervisionados por embaixadores.", False),
            ("Porque os líderes políticos possuem o poder divino de transferir seus pecados para os cidadãos.", False),
            ("Porque os seres humanos assinam procurações jurídicas mútuas antes de ingressarem na fase adulta.", False),
            ("Porque os algoritmos digitais rastreiam cada ação humana para atualizar manuais de civilidade nas redes.", False),
            ("Porque cada ato livre afirma um valor sobre como o ser humano deve viver, legislando sobre a imagem humana no cosmos.", True)
        ],
        "Ao tomar uma decisão moral, o sujeito projeta uma imagem de homem ideal, assumindo a responsabilidade cósmica de afirmar um modelo para a humanidade."
    ))

    questoes_brutas.append((
        16, "EM13CHS502", "basico",
        "Identifique o título da célebre conferência parisiense de 1946 na qual Jean-Paul Sartre defendeu o existencialismo das acusações de pessimismo:",
        [
            ("O Existencialismo é um Humanismo, apresentando o existencialismo como doutrina de ação e compromisso.", True),
            ("A Náusea, descrevendo o diário de memórias de um historiador francês em crise existencial.", False),
            ("Crítica da Razão Dialética, analisando as lutas anticoloniais sob a ótica dos movimentos operários.", False),
            ("Entre Quatro Paredes, encenando o tormento de três pessoas trancadas no ambiente do inferno.", False),
            ("A Imaginação, investigando as imagens mentais a partir da fenomenologia de Edmund Husserl.", False)
        ],
        "Em O Existencialismo é um Humanismo (1946), Sartre demonstrou que o existencialismo não prega a inércia, mas a responsabilidade e o engajamento humano."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Em qual conceito Kierkegaard resume sua tese contra a pretensão hegeliana de construir um sistema filosófico objetivo e totalizante?",
        [
            ("A Verdade é a Subjetividade, afirmando que o sentido autêntico do real exige a apropriação singular e apaixonada do indivíduo.", True),
            ("A Matéria é a única Substância, postulando que as ideias são secreções fisiológicas do cérebro biológico.", False),
            ("O Belo é o Útil, sustentando que as obras de arte devem servir à produção fabril das cidades.", False),
            ("O Real é Racional, defendendo que todos os acontecimentos históricos ocorrem por necessidade lógica pura.", False),
            ("A História é o Progresso, concebendo a marcha dos povos como uma vitória contínua da civilização ocidental.", False)
        ],
        "Kierkegaard sentenciou que a verdade é a subjetividade, recusando a ilusão de uma verdade desinteressada e afirmando o engajamento vital do indivíduo."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "Qual sentimento inevitável atinge o indivíduo que permanece preso ao estádio estético, segundo a obra Ou-Ou de Kierkegaard?",
        [
            ("A tranquilidade imutável de quem alcançou a iluminação espiritual definitiva nos monastérios.", False),
            ("A satisfação cívica proporcionada pela aposentadoria remunerada após décadas de trabalho útil.", False),
            ("O Tédio e o Desespero, gerados pelo esgotamento da novidade e pelo vazio do prazer fugaz passageiro.", True),
            ("A alegria constante de quem vive em harmonia com todas as prescrições da moral burguesa tradicional.", False),
            ("O orgulho patriótico resultante da participação militar em batalhas históricas pela soberania da nação.", False)
        ],
        "Como as novidades sensuais se esgotam rapidamente, a vida do esteta termina no tédio existencial e no desespero de quem não construiu raízes duradouras."
    ))

    questoes_brutas.append((
        19, "EM13CHS501", "basico",
        "No vocabulário de Sartre em O Ser e o Nada, por que a consciência humana é caracterizada como um Nada de Ser?",
        [
            ("Porque a mente humana é incapaz de formular pensamentos lógicos ou calcular distâncias no espaço físico.", False),
            ("Porque a consciência não é uma coisa material rígida, mas um espaço de abertura temporal, distância crítica e liberdade.", True),
            ("Porque os cérebros biológicos são compostos por tecidos moles desprovidos de minerais pesados como o ferro.", False),
            ("Porque todos os seres humanos nascem com deficiências cognitivas que os impedem de memorizar fatos passados.", False),
            ("Porque as memórias da infância são esquecidas no momento em que o indivíduo atinge a fase da juventude.", False)
        ],
        "A consciência humana (para-si) é um nada de ser porque não possui substância sólida prévia; ela se define pela capacidade reflexiva de negar o determinismo."
    ))

    questoes_brutas.append((
        20, "EM13CHS502", "basico",
        "Em Temor e Tremor, o que representa a suspensão temporária e extraordinária da ética moral no relato bíblico do sacrifício de Abraão?",
        [
            ("A anulação legal das penas prisionais para cidadãos de famílias aristocráticas durante feriados cívicos.", False),
            ("A autorização concedida a governantes para descumprirem acordos internacionais de paz em tempos de crise.", False),
            ("A dispensa de estudantes do cumprimento de horários escolares durante competições esportivas municipais.", False),
            ("A superação extraordinária das regras morais humanas em nome de uma ordem direta e absoluta de Deus ao indivíduo singular.", True),
            ("O cancelamento de contratos comerciais em virtude de intempéries climáticas que afetem as colheitas agrícolas.", False)
        ],
        "Abraão atende ao mandamento divino que contraria a lei moral universal (não matar), subordinando o dever social humano à fé absoluta no Criador."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Na crítica à abstração filosófica, com que intuito Kierkegaard afirmava sarcasticamente que Hegel construiu um palácio monumental, mas morava em uma cabana ao lado?",
        [
            ("Porque o sistema idealista explicava tudo conceitualmente, mas ignorava a angústia, o pecado e a morte do homem real de carne e osso.", True),
            ("Porque o pensador alemão gastou todas as suas economias financeiras na reforma de propriedades rurais herdadas da família.", False),
            ("Porque as universidades da Prússia proibiram que professores residissem no interior dos campi acadêmicos oficiais.", False),
            ("Porque as obras de arquitetura clássica exigiam fundações de granito que a engenharia alemã não conseguia executar.", False),
            ("Porque a lógica hegeliana defendia que os intelectuais deviam renunciar a bens materiais e viver na pobreza monástica.", False)
        ],
        "A ironia kierkegaardiana critica o abismo entre o sistema filosófico totalizante e a experiência dramática, vulnerável e mortal do indivíduo concreto."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "No itinerário espiritual kierkegaardiano, como se manifesta a transição do estádio ético para o estádio religioso na consciência singular?",
        [
            ("Como um ganho de prestígio social resultante da posse em altos cargos da magistratura e do parlamento da capital.", False),
            ("Como a descoberta da própria culpa e da finitude perante a santidade divina, exigindo o salto da fé que transcende a lei civil.", True),
            ("Como a aceitação conformista de que o dever legal dos homens é a expressão suprema de toda a justiça possível no cosmos.", False),
            ("Como o retorno arrependido aos prazeres sensoriais do estádio estético para esquecer as exigências severas da virtude moral.", False),
            ("Como a renúncia definitiva a qualquer tipo de reflexão espiritual em favor do acúmulo de terras produtivas no campo.", False)
        ],
        "O homem ético percebe que seus esforços morais nunca alcançam a perfeição infinita, reconhecendo sua culpa e dando o salto de fé em direção a Deus."
    ))

    questoes_brutas.append((
        23, "EM13CHS501", "intermediario",
        "Ao afirmar a precedência da existência sobre a essência, de que forma Sartre inviabiliza o apelo à natureza humana como desculpa determinista?",
        [
            ("Porque sem um Deus para desenhar a essência humana, não há modelo pré-fixado: o indivíduo é integralmente autor de suas condutas.", True),
            ("Porque a biologia moderna comprovou que os comportamentos humanos são determinados unicamente pelo instinto de sobrevivência animal.", False),
            ("Porque os Estados constitucionais proibiram o ensino de teorias metafísicas em todas as escolas públicas e privadas da nação.", False),
            ("Porque as leis civis preveem indenizações pecuniárias obrigatórias para quem invocar termos filosóficos em tribunais criminais.", False),
            ("Porque as tradições religiosas do ocidente concordaram unanimemente em transferir a soberania moral para corporações de comércio.", False)
        ],
        "Se não há essência anterior, não há álibi determinista: não se pode culpar gênio, genes ou tentações, pois o ser humano é fruto de suas próprias escolhas."
    ))

    questoes_brutas.append((
        24, "EM13CHS502", "intermediario",
        "No exame da inautenticidade humana, que traço estrutural diferencia a mentira comum perante terceiros da dinâmica íntima da má-fé?",
        [
            ("A mentira comum ocorre apenas em contratos comerciais formais, enquanto a má-fé se restringe a desacordos familiares domésticos.", False),
            ("A mentira comum exige duas consciências (quem mente e quem é enganado), enquanto na má-fé a mesma consciência engana a si própria.", True),
            ("A mentira comum é punida pelo código penal dos países, ao passo que a má-fé é incentivada por todas as constituições liberais.", False),
            ("A mentira comum é praticada apenas por indivíduos corruptos, enquanto a má-fé afeta apenas crianças na fase pré-escolar.", False),
            ("A mentira comum utiliza documentos manuscritos em papel, enquanto a má-fé se manifesta exclusivamente em mensagens pela internet.", False)
        ],
        "Na mentira tradicional, um sujeito esconde a verdade de outro; na má-fé sartriana, ocorre a fratura íntima na qual a consciência mente para si mesma."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Sob a perspectiva existencialista, como a escolha de uma carreira profissional pode degenerar em um ato de má-fé da juventude contemporânea?",
        [
            ("Quando o estudante opta por uma profissão por pressão familiar ou status burguês, fingindo que não teve a liberdade soberana de escolher.", True),
            ("Quando o jovem decide estudar em cursos de universidades públicas após aprovação legítima em concursos vestibulares concorridos.", False),
            ("Quando o aluno dedica seus finais de semana para realizar trabalhos voluntários de apoio a moradores desabrigados de seu bairro.", False),
            ("Quando o estudante adquire livros didáticos de segunda mão em sebos comunitários para economizar recursos de sua mesada.", False),
            ("Quando o candidato consulta guias vocacionais oficiais elaborados por profissionais de psicologia escolar credenciados.", False)
        ],
        "A má-fé manifesta-se quando o estudante abdica de sua autonomia e culpa pais ou o mercado, transferindo sua responsabilidade para forças externas."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "No âmbito da justiça internacional, qual fundamentação filosófica levou os juízes de Nuremberg e de Jerusalém a rejeitarem a alegação de cumprimento de ordens?",
        [
            ("Porque entenderam que obedecer a ordens desumanas é um ato de má-fé radical, pois o sujeito nunca perde a liberdade de recusar o mal.", True),
            ("Porque os oficiais militares alemães possuíam salários muito elevados para terem direito a defesas jurídicas patrocinadas pelo Estado.", False),
            ("Porque as tropas aliadas vitoriosas haviam decretado a revogação de todos os tratados internacionais de direito penal de guerra.", False),
            ("Porque as leis da Alemanha nazista previam explicitamente que os soldados de patente baixa eram os únicos culpados pelos crimes.", False),
            ("Porque as câmaras de gás funcionavam com sistemas elétricos que dispensavam a intervenção de operadores humanos nas instalações.", False)
        ],
        "A jurisprudência histórica e o existencialismo rejeitaram a escusa do cumprimento de ordens: a decisão de obedecer ao extermínio é escolha moral punível."
    ))

    questoes_brutas.append((
        27, "EM13CHS501", "intermediario",
        "Na fenomenologia sartriana do Olhar do Outro, de que modo se explica a emergência do sentimento da vergonha na consciência?",
        [
            ("O olhar do outro nos flagra e nos objetifica, revelando que nos tornamos um ser exterior exposto ao julgamento alheio sem controle nosso.", True),
            ("O olhar do outro transmite radiações ópticas que afetam a circulação sanguínea no rosto, provocando calor muscular involuntário.", False),
            ("A vergonha é um erro comportamental que decorre da falta de treinamento militar durante os primeiros anos da infância nas cidades.", False),
            ("O olhar de terceiros só produz vergonha em indivíduos que praticam crimes fiscais comprovados pela receita tributária federal.", False),
            ("A sensação de embaraço resulta do descumprimento de regras de etiqueta em jantares diplomáticos de embaixadas estrangeiras.", False)
        ],
        "O olhar alheio me transforma em um em-si aos olhos do outro; ao me ver visto como objeto pelo outro, experimento a vulnerabilidade e a vergonha de ser."
    ))

    questoes_brutas.append((
        28, "EM13CHS502", "intermediario",
        "Ao proferir a conferência de 1946, com quais argumentos Sartre refutou a acusação de que o existencialismo seria uma filosofia de pessimismo inerte?",
        [
            ("Porque demonstrou que a ausência de um Deus e de sentidos prontos convoca o homem à ação lúcida e à construção livre de seu próprio destino.", True),
            ("Porque comprovou que o destino humano é governado por leis cósmicas benévolas que garantem a vitória final de todas as utopias terrenas.", False),
            ("Porque defendeu a subordinação de todas as decisões dos trabalhadores às diretrizes dogmáticas de bispos e teólogos da corte régia.", False),
            ("Porque propôs que os intelectuais devem se abster de qualquer participação em disputas políticas ou sindicais nas sociedades industriais.", False),
            ("Porque considerava que as injustiças sociais são inevitáveis e que a busca por igualdade de direitos é um sonho infantil descabido.", False)
        ],
        "Em O Existencialismo é um Humanismo, Sartre explicou que o existencialismo é uma filosofia de engajamento e esperança ativa: o sentido deve ser construído na ação."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Nas reflexões de Viktor Frankl sobre os campos de concentração, como o postulado do sentido da vida confirma o valor da liberdade interior?",
        [
            ("Ao mostrar que os prisioneiros que encontravam um sentido autônomo para sua dor resistiam com mais força às atrocidades do cativeiro.", True),
            ("Ao provar que a força física muscular era o único elemento decisivo para a sobrevivência em trabalhos forçados de mineração de carvão.", False),
            ("Ao evidenciar que as torturas desumanas eram esquecidas instantaneamente por prisioneiros que praticavam exercícios de ginástica diária.", False),
            ("Ao constatar que os guardas militares concediam regalias e alimentação farta para os cativos que dominavam a língua hebraica antiga.", False),
            ("Ao sugerir que o desespero absoluto é a atitude mais adequada diante de crises políticas que envolvam perseguições a minorias étnicas.", False)
        ],
        "Frankl fundou a Logoterapia a partir dessa constatação existencial: mesmo na barbárie extrema, o homem preserva a liberdade íntima de escolher sua atitude perante a dor."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "No Teatro do Absurdo, que correspondência existe entre os diálogos circulares de Esperando Godot e o sentimento do absurdo existencial?",
        [
            ("A peça encena o diálogo circular de dois vagabundos à espera de alguém que nunca chega, retratando a espera inútil por sentidos exteriores.", True),
            ("O drama teatral descreve a coroação gloriosa de um novo rei que resolve todos os conflitos agrários de camponeses do interior da Irlanda.", False),
            ("A montagem cênica exibe técnicas de combate corpo a corpo entre guerreiros medievais que disputavam o controle de feudos sagrados.", False),
            ("O enredo narra a fuga bem-sucedida de dois prisioneiros de guerra que cruzam fronteiras montanhosas com o auxílio de mapas secretos.", False),
            ("O texto dramático comprova que a história da humanidade caminha de forma necessária rumo à paz universal dos povos desarmados.", False)
        ],
        "Esperando Godot, marco do Teatro do Absurdo, ilustra a condição humana arremessada no mundo, aguardando redenções ou salvadores que nunca virão de fora."
    ))

    questoes_brutas.append((
        31, "EM13CHS501", "intermediario",
        "Em que sentido o romance A Náusea de Sartre traduz esteticamente a descoberta da contingência radical da matéria?",
        [
            ("Através do enjoo físico experimentado pelo protagonista Antoine Roquentin ao perceber a gratuidade injustificável de sua existência e das coisas.", True),
            ("Por meio do relato de um comerciante de vinhos que perdeu seus estoques em um naufrágio durante uma tempestade no mar mediterrâneo.", False),
            ("Mediante a descrição de epidemias bacterianas que assolaram as cidades portuárias do litoral francês no início do século vinte.", False),
            ("Através de um manual de primeiros socorros elaborado por médicos militares para combater enjoos em navios de passageiros civis.", False),
            ("Por intermédio da biografia heroica de generais que conquistaram territórios ultramarinos sob a bandeira da república francesa.", False)
        ],
        "Em A Náusea, a sensação física de náusea decorre da constatação desconcertante de que nada na realidade possui um porquê necessário prévio: tudo existe por acaso."
    ))

    questoes_brutas.append((
        32, "EM13CHS502", "intermediario",
        "No campo da reflexão antropológica, de que maneira a distinção entre angústia e ansiedade clínica resguarda o caráter irredutível da liberdade?",
        [
            ("Demonstrando que a angústia é uma dimensão existencial estrutural ligada à liberdade, que não pode ser extinta por pílulas calmantes.", True),
            ("Provando que os transtornos psiquiátricos não existem e que os hospitais devem ser fechados imediatamente pelas autoridades de saúde.", False),
            ("Afirmando que o uso de remédios laboratoriais é um pecado religioso imperdoável que condena as almas ao sofrimento no além.", False),
            ("Defendendo que apenas professores de filosofia possuem autorização legal para prescrever medicamentos controlados em farmácias.", False),
            ("Sustentando que os estudantes devem abandonar tratamentos de saúde para se dedicarem exclusivamente à leitura de tratados em latim.", False)
        ],
        "A ansiedade clínica exige cuidados médicos, mas a angústia existencial decorre da própria condição de ser livre e mortal; fugir dela é fugir da vida autêntica."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Por que Sartre afirma que mesmo o ato de calar-se diante de uma tirania ou não escolher nada é, em si mesmo, uma escolha?",
        [
            ("Porque a estrutura existencial da consciência humana é liberdade: recusar-se a tomar partido já constitui a escolha soberana pela cumplicidade.", True),
            ("Porque as leis eleitorais multam os cidadãos que não depositam cédulas de votação em urnas durante pleitos municipais regulares.", False),
            ("Porque os governos autoritários consideram que todo cidadão silencioso é um combatente revolucionário disfarçado nas fábricas.", False),
            ("Porque a inércia física queima tantas calorias corporais quanto a realização de marchas e comícios em praças públicas abertas.", False),
            ("Porque os tribunais de exceção obrigam todos os acusados a prestarem depoimentos sob juramento com a mão sobre a Bíblia sagrada.", False)
        ],
        "Não escolher é impossível para a consciência: o silêncio diante da opressão é a escolha de aceitar o status quo, pela qual o sujeito é moralmente responsável."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "Sob a ótica do existencialismo contemporâneo, como a exibição de perfis filtrados nas redes sociais digitais reflete a dinâmica da má-fé?",
        [
            ("Ao congelar o sujeito em um avatar bidimensional de consumo para agradar o olhar alheio, renunciando à densidade e aos conflitos reais da vida.", True),
            ("Ao permitir que todos os internautas se tornem autores diplomados de poesias líricas reconhecidas pela Academia de Letras.", False),
            ("Ao extinguir as contradições econômicas entre as classes sociais através da distribuição gratuita de computadores nas periferias.", False),
            ("Ao garantir a transparência absoluta de todas as ações dos parlamentares em sessões secretas de comissões legislativas da câmara.", False),
            ("Ao incentivar a prática do jejum espiritual e da oração solitária em monastérios encravados em regiões montanhosas remotas.", False)
        ],
        "O perfil filtrado no Instagram encena um papel rígido para capturar a aprovação dos outros, operando como fuga inautêntica da complexidade aberta do para-si."
    ))

    questoes_brutas.append((
        35, "EM13CHS501", "intermediario",
        "No terreno da ética da ação, que consequência decorre da proposição de que o homem não é nada além do conjunto de seus atos?",
        [
            ("Implode o refúgio das desculpas ilusórias baseadas em potenciais nunca realizados: o valor de uma vida se mede pelo que de fato foi construído.", True),
            ("Reduz a dignidade das pessoas com deficiência física por não poderem participar de competições olímpicas internacionais de atletismo.", False),
            ("Obriga os cidadãos a trabalharem em turnos ininterruptos de dezoito horas em linhas de montagem fabris sem direito a repouso semanal.", False),
            ("Determina que as crianças recém-nascidas recebam notas de avaliação escolar antes mesmo de aprenderem a falar a língua materna.", False),
            ("Proíbe que os aposentados desfrutem do convívio familiar, forçando-os a escrever relatórios autobiográficos em órgãos da previdência.", False)
        ],
        "Sartre desfaz a ilusão do 'gênio incompreendido que não realizou nada': o homem é seu projeto materializado em ações, e não intenções vazias não concretizadas."
    ))

    questoes_brutas.append((
        36, "EM13CHS502", "intermediario",
        "Na ontologia do Para-Si de Sartre, em que termos a relação do ser humano com a temporalidade rompe com a fixidez do passado?",
        [
            ("O para-si é um constante distanciar-se do passado através da negação, projetando-se livremente no futuro como possibilidade aberta.", True),
            ("A consciência humana permanece rigidamente fixada nos traumas da infância sem nenhuma capacidade de superação psicológica.", False),
            ("O tempo humano é uma linha estática desenhada nos astros celestes que pode ser lida com exatidão por astrólogos profissionais.", False),
            ("O futuro é uma ilusão dos sentidos que deve ser descartada pelos cientistas em favor da análise do presente imediato congelado.", False),
            ("A memória biológica dos indivíduos é apagada a cada dez anos pelas variações das marés e das correntes de ventos marítimos.", False)
        ],
        "O para-si nunca se reduz ao que já foi (passado); ele se define pelo dinamismo da liberdade, lançando-se incessantemente rumo ao porvir através de projetos."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Por que Kierkegaard defendia que a fé do estádio religioso não pode ser explicada nem justificada pela moralidade racional comum dos homens?",
        [
            ("Porque a fé apoia-se no paradoxo do Absurdo e no risco solitário perante o Absoluto, superando os limites da lei moral universal.", True),
            ("Porque os textos dos profetas bíblicos foram redigidos em dialetos que os linguistas modernos não conseguem traduzir com certeza.", False),
            ("Porque os líderes das congregações religiosas proibiam expressamente que os fiéis frequentassem cursos de direito e filosofia clássica.", False),
            ("Porque a lei penal da Dinamarca previa a prisão de todos os cidadãos que tentassem justificar suas orações diante de juízes de paz.", False),
            ("Porque a razão humana foi considerada pelos médicos do século dezenove como um veneno que causava dores de cabeça constantes.", False)
        ],
        "A fé kierkegaardiana repousa no escândalo do absurdo: Abraão não é um assassino vulgar nem um cidadão moral exemplar; ele é o homem do salto de fé no mistério."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "Em que sentido o existencialismo de maturidade de Sartre articula a liberdade individual com os compromissos das lutas coletivas?",
        [
            ("Reconhecendo que a libertação genuína de um indivíduo exige o engajamento concreto na emancipação de todos os povos oprimidos pelo colonialismo.", True),
            ("Exigindo que todos os escritores revolucionários entreguem suas propriedades rurais aos cofres centrais de bancos imperialistas.", False),
            ("Defendendo que a melhor forma de protesto político é o silêncio absoluto dos operários dentro de suas residências particulares.", False),
            ("Afirmando que a luta de classes foi inventada por corporações midiáticas para vender jornais diários aos trabalhadores urbanos.", False),
            ("Propondo que os sindicatos operários sejam extintos em favor de reuniões de oração conduzidas por capelães das forças militares.", False)
        ],
        "Sartre conclui que não posso desejar minha própria liberdade sem desejar a liberdade de todos; sua filosofia deságua no engajamento anticolonial e socialista."
    ))

    questoes_brutas.append((
        39, "EM13CHS501", "intermediario",
        "Em seus últimos escritos públicos, que acusação central dirigiu Kierkegaard contra a Igreja luterana oficial da Dinamarca?",
        [
            ("Acusou a instituição de ter burocratizado a fé e transformado a entrega radical a Cristo em uma comodidade burguesa pacificada e mundana.", True),
            ("Reclamou que os templos religiosos utilizavam órgãos musicais desafinados durante a celebração dos cultos dominicais solenes.", False),
            ("Exigiu que os pastores fossem substituídos por magistrados civis remunerados diretamente pelo tesouro público da coroa régia.", False),
            ("Afirmou que os fiéis deveriam abandonar o estudo das escrituras sagradas para aprenderem as teorias do socialismo científico nas fábricas.", False),
            ("Propôs que todos os edifícios eclesiásticos fossem demolidos para dar lugar a armazéns de trigo e celeiros de grãos no campo.", False)
        ],
        "Kierkegaard fustigou a cristandade oficial, demonstrando que ser cristão exige temor, tremor e sacrifício singular, e não o conforto complacente burguês."
    ))

    questoes_brutas.append((
        40, "EM13CHS502", "intermediario",
        "Ao proclamar que o homem é o que faz de si mesmo, em que sentido o existencialismo redefine a dignidade e a autonomia humanas?",
        [
            ("Afirma a soberania do ser humano como criador de sua história, recusando qualquer determinismo fatalista biológico, social ou astrológico.", True),
            ("Condiciona a honra dos indivíduos à quantidade de condecorações honoríficas recebidas de monarquias e academias militares.", False),
            ("Subordina a cidadania das pessoas à comprovação de descendência genealógica pura de famílias proprietárias de terras no campo.", False),
            ("Nega que os seres humanos tenham direitos fundamentais, admitindo a escravidão de trabalhadores que não consigam comprar imóveis.", False),
            ("Determina que o valor moral de um cidadão seja calculado pelo número de curtidas e seguidores acumulados em plataformas virtuais.", False)
        ],
        "A dignidade existencial repousa na liberdade criadora: o ser humano não é escravo de seu passado nem de seus genes, mas autor aberto de seu próprio ser."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Ao contrapor o indivíduo ao sistema hegeliano, de que modo Kierkegaard fundamenta a irredutibilidade da escolha trágica (Ou-Ou)?",
        [
            ("Demonstrando que a vida real exige escolhas dramáticas e irreconciliáveis no tempo, nas quais optar por um caminho implica a perda dolorosa do outro.", True),
            ("Provando que a lógica formal de Aristóteles era capaz de resolver todas as divergências doutrinárias da teologia cristã primitiva.", False),
            ("Sustentando que os seres humanos podem vivenciar simultaneamente todas as possibilidades morais sem sofrer nenhum conflito íntimo.", False),
            ("Argumentando que a história do espírito absoluto atinge a plenitude na organização militar dos exércitos dos impérios germânicos.", False),
            ("Mostrando que as decisões humanas devem ser tomadas com base em cálculos matemáticos de probabilidade estatística computadorizada.", False)
        ],
        "- **Etapa 1:** Hegel propunha a síntese dialética (*Aufhebung*), na qual as contradições aparentes se conciliam e se superam no progresso racional do Todo.\n- **Etapa 2:** Kierkegaard objeta que a existência concreta não é um sistema lógico pacificado; o homem defronta-se com encruzilhadas vitais absolutas (Ou isso, Ou aquilo), onde uma escolha anula a outra com sacrifício e risco, validando a alternativa A."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Ao dissecar o conceito de angústia como a vertigem da liberdade, de que modo Kierkegaard desconstrói o determinismo causal da moralidade tradicional?",
        [
            ("Afirmando que as escolhas humanas decorrem invariavelmente da herança genética dos antepassados registrada em livros civis.", False),
            ("Provando que a liberdade confronta o Nada: antes do ato de decisão moral, nada no cosmos determina necessariamente se o homem escolherá o bem ou o mal.", True),
            ("Sustentando que as ações dos cidadãos são programadas por forças astrológicas invisíveis que controlam as órbitas dos planetas solares.", False),
            ("Argumentando que a sociedade civil moderna eliminou completamente as possibilidades de erro e pecado dos indivíduos conscientes.", False),
            ("Demonstrando que a culpa moral é uma enfermidade corporal contagiosa transmitida pelo contato com águas de rios poluídos.", False)
        ],
        "- **Etapa 1:** As teorias deterministas buscam causas mecânicas (biológicas, ambientais, divinas) para explicar por que os homens agem de certa maneira.\n- **Etapa 2:** Kierkegaard demonstra que a angústia é a vertigem da pura possibilidade: a vontade depara-se com o nada causal; a decisão de saltar no abismo ou recuar repousa única e solitariamente na liberdade do sujeito, o que confirma a alternativa B."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Ao conceber a consciência como um Nada de Ser, como a ontologia fenomenológica sartriana supera o substancialismo da alma cartesiana?",
        [
            ("Afirmando que a mente humana é um órgão puramente muscular que bombeia sangue arterial para irrigar o sistema nervoso central.", False),
            ("Reafirmando a existência de uma alma eterna imutável dotada de ideias inatas que governa o corpo como um piloto comanda um navio.", False),
            ("Definindo a consciência não como substância sólida pensante (res cogitans), mas como ato dinâmico de negatividade, distância e projeto no tempo.", True),
            ("Subordinando a atividade psíquica às determinações químicas de hormônios produzidos exclusivamente pelas glândulas adrenais.", False),
            ("Comprovando que o espírito humano é um fluido magnético sutil que circula pelas veias e artérias das extremidades do corpo.", False)
        ],
        "- **Etapa 1:** René Descartes concebeu a consciência como substância pensante (*res cogitans*), ou seja, uma coisa sólida espiritual que existe em si.\n- **Etapa 2:** Sartre supera esse substancialismo: a consciência humana (*para-si*) não é coisa nem substância; é o nada, a fissura no ser das coisas materiais através da qual a liberdade, a negação temporal e a reflexão entram no mundo, legitimando a alternativa C."
    ))

    questoes_brutas.append((
        44, "EM13CHS502", "dificil",
        "Por que Jean-Paul Sartre sustenta que o ser humano não pode desculpar seus atos apelando para o império de paixões irresistíveis?",
        [
            ("Porque as paixões e emoções não são forças cegas exteriores que invadem o homem, mas são escolhas de engajamento do próprio Para-Si no mundo.", True),
            ("Porque o sistema penal dos países desenvolvidos prevê a execução sumária de qualquer cidadão que demonstre sentimentos afetivos públicos.", False),
            ("Porque a medicina psiquiátrica comprovou que os seres humanos não possuem hormônios nem reações sensoriais perante perigos iminentes.", False),
            ("Porque a razão humana opera de forma automática e impede que os indivíduos tomem decisões sob efeito de entusiasmo ou cólera.", False),
            ("Porque as tradições morais do iluminismo já haviam demonstrado que as emoções são ilusões provocadas por má alimentação na infância.", False)
        ],
        "- **Etapa 1:** A desculpa determinista tradicional afirma: 'fui tomado por uma paixão violenta incontrolável, não tive culpa'.\n- **Etapa 2:** Sartre refuta esse subterfúgio de má-fé: a emoção é uma conduta mágica escolhida pela consciência para lidar com uma situação dramática; entregar-se à paixão é um ato de consentimento da liberdade, pelo qual o homem responde inteiramente, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "No campo da moral contemporânea, de que forma a responsabilidade universal sartriana transforma a liberdade no mais exigente fundamento ético?",
        [
            ("Ao impor que o sujeito responda pelas perdas financeiras acumuladas por empresas estatais nas quais nunca trabalhou.", False),
            ("Ao transferir a obrigação de legislar as leis civis dos parlamentos eleitos para corporações internacionais de comércio privado.", False),
            ("Ao determinar que o homem pague tributos pecuniários para cobrir os custos judiciais de processos de outros continentes.", False),
            ("Ao prescrever que, ao escolher um curso de ação, o indivíduo está endossando e criando um padrão ético válido para toda a humanidade no cosmos.", True),
            ("Ao condicionar a validade dos votos eleitorais à aprovação unânime de comissões de juristas diplomados em academias régias.", False)
        ],
        "- **Etapa 1:** A liberdade existencial não é licença para o capricho hedonista egoísta ou para a irresponsabilidade cívica.\n- **Etapa 2:** Ao escolher agir de determinada maneira (seja na guerra, no amor ou na política), o indivíduo afirma publicamente que aquele é o modo como a humanidade deve viver, carregando nos ombros o peso insuportável de ser o legislador de toda a espécie humana, o que consagra a alternativa D."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Ao examinar a figura do garçom de café, qual é o núcleo do autoengano que Sartre desmascara no mecanismo psicológico da má-fé?",
        [
            ("O garçom acredita piamente que sua profissão é a única atividade econômica digna de remuneração nas capitais europeias.", False),
            ("O garçom sonha em comprar o estabelecimento comercial através de empréstimos concedidos por bancos de investimento internacionais.", False),
            ("O garçom tenta transformar sua liberdade viva e fluida em um papel mecânico de coisa, fingindo que é incapaz de mudar sua própria vida.", True),
            ("O garçom engana deliberadamente os clientes servindo café frio com a intenção explícita de prejudicar as vendas do patrão.", False),
            ("O garçom recusa o diálogo com os clientes por preconceito social contra pessoas que residem nos bairros da periferia da cidade.", False)
        ],
        "- **Etapa 1:** O garçom imita os gestos estereotipados de sua profissão com rigidez excessiva e subserviência mecânica milimetrada.\n- **Etapa 2:** Ele busca refúgio na ilusão de que é uma engrenagem inanimada (*em-si*), para sufocar a angústia de saber que possui a liberdade aberta (*para-si*) de abandonar aquela farsa a qualquer instante e inventar um novo projeto existencial, validando a alternativa C."
    ))

    questoes_brutas.append((
        47, "EM13CHS501", "dificil",
        "Ao substituir a natureza humana pela condição humana universal, de que maneira Sartre viabiliza a compreensão mútua entre culturas?",
        [
            ("A condição humana define a situação histórica comum de estar no mundo tendo de escolher, agir e morrer, sem impor uma essência biológica prévia.", True),
            ("A natureza humana foi preservada por Sartre como um código genético herdado dos patriarcas bíblicos que guia os instintos morais.", False),
            ("A condição humana exige que todas as sociedades adotem constituições monárquicas para garantir a ordem civil nos bairros operários.", False),
            ("A universalidade das escolhas repousa na identidade anatômica dos ossos do esqueleto humano catalogados em manuais de medicina forense.", False),
            ("A recusa da essência impede qualquer comunicação entre indivíduos de etnias e culturas distintas no planeta Terra.", False)
        ],
        "- **Etapa 1:** A tradição metafísica sempre buscou uma 'natureza humana' fixa desenhada por Deus ou inscrita na biologia para fundamentar a moral.\n- **Etapa 2:** Sartre substitui a natureza pela 'condição humana': embora não tenhamos essência dada, todos compartilhamos a mesma situação fundamental de sermos lançados ao mundo, sermos mortais, convivermos com o outro e termos de escolher nosso destino, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        48, "EM13CHS502", "dificil",
        "No plano da dramaturgia existencialista, como a peça Entre Quatro Paredes desconstrói as representações teológicas medievais do inferno?",
        [
            ("Demonstrando que o verdadeiro tormento eterno não exige caldeirões de fogo ou diabos armados, mas repousa no escrutínio mútuo e implacável das consciências.", True),
            ("Mostrando que as almas dos condenados podem retornar à Terra como fantasmas para rever seus parentes nas noites de lua cheia.", False),
            ("Provando que o inferno foi construído pelos deuses do panteão grego sob o sopé do monte Olimpo para punir criminosos marítimos.", False),
            ("Afirmando que a única salvação das chamas infernais decorre do pagamento de dízimos em moedas cunhadas em prata para conventos reais.", False),
            ("Sustentando que os três personagens falecidos conseguem escapar da prisão fechada escavando um túnel secreto com colheres de sopa.", False)
        ],
        "- **Etapa 1:** A iconografia medieval e barroca imaginava o inferno povoado de labaredas, demônios com tridentes e torturas corporais físicas.\n- **Etapa 2:** Sartre moderniza o inferno: três indivíduos trancados em uma sala comum, torturando-se mutuamente pela vigilância de seus olhares, revelando que a pior prisão e condenação é o julgamento e a dependência do olhar desmistificador do outro, o que consolida a alternativa A."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Como a experiência da contingência radical em A Náusea se relaciona à superação do modelo finalista clássico do cosmos?",
        [
            ("Mostrando que as coisas do mundo simplesmente existem de forma gratuita e sem uma razão final cósmica necessária que as justifique previamente.", True),
            ("Provando que os planetas do sistema solar orbitam o centro da galáxia para garantir que as colheitas de trigo ocorram no outono.", False),
            ("Defendendo que cada pedra, árvore ou rio foi desenhado por arquitetos divinos com uma utilidade moral imediata para o homem.", False),
            ("Confirmando as teorias físicas de Aristóteles sobre os quatro elementos que buscam espontaneamente seus lugares naturais de repouso.", False),
            ("Sustentando que o universo foi programado por inteligências artificiais extraterrestres para servir de campo de treinamento militar.", False)
        ],
        "- **Etapa 1:** O modelo cósmico clássico presumia que tudo na natureza existia para uma finalidade harmônica pré-ordenada.\n- **Etapa 2:** O existencialismo sartriano rompe com essa ilusão: a matéria é bruta, desprovida de finalidade prévia; a raiz do castanheiro é contingente, gratuita, sem razão de ser no cosmos. O sentido não está nas coisas; é o homem livre quem deve atribuir sentido ao mundo, validando a alternativa A."
    ))

    questoes_brutas.append((
        50, "EM13CHS102", "dificil",
        "Ao confrontar o julgamento de Adolf Eichmann com as teses de Sartre sobre a má-fé, que conclusão ética se impõe sobre a responsabilidade individual?",
        [
            ("O funcionário que opera as engrenagens burocráticas de um massacre não pode alegar neutralidade técnica, pois agir é legitimar a engrenagem.", True),
            ("A burocracia estatal anula a responsabilidade jurídica dos indivíduos que possuem diplomas emitidos por universidades alemãs.", False),
            ("Os crimes contra a humanidade só podem ser julgados se os réus confessarem voluntariamente suas culpas em canais de rádio.", False),
            ("A obediência estrita aos regulamentos de repartições públicas confere imunidade absoluta a militares de qualquer graduação de tropa.", False),
            ("O dever de cumprir ordens de governantes soberanos se sobrepõe a qualquer mandamento moral ou convenção internacional humanitária.", False)
        ],
        "- **Etapa 1:** Eichmann alegou em Jerusalém ser mero executor burocrático de ordens superiores, sem ódio pessoal contra os judeus transportados.\n- **Etapa 2:** O existencialismo sartriano refuta esse autoengano de má-fé: quem cumpre uma ordem desumana escolhe ser cúmplice e viabilizar o extermínio; a burocracia não dissolve a liberdade do sujeito, que responde pessoal e eticamente por seus atos, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        51, "EM13CHS501", "dificil",
        "Qual é a relação existencial estabelecida por Sartre entre o Ser Em-Si e o Ser Para-Si em O Ser e o Nada?",
        [
            ("O para-si necessita do em-si como fundo opaco do mundo sobre o qual exerce sua negação reflexiva e projeta seus sentidos livres.", True),
            ("O em-si é uma criação imaginária do para-si, desaparecendo completamente assim que o indivíduo fecha os olhos ou adormece.", False),
            ("O para-si funde-se pacificamente ao em-si após a realização de meditações solitárias em templos monásticos da antiguidade.", False),
            ("O em-si e o para-si são duas substâncias materiais idênticas que possuem o mesmo peso molecular medido em balanças de precisão.", False),
            ("O em-si possui consciência reflexiva plena e governa os desejos morais e escolhas vocacionais do para-si no tempo presente.", False)
        ],
        "- **Etapa 1:** O *em-si* é a matéria compacta, bruta e coincidente consigo mesma; o *para-si* é a consciência que não tem massa e vive de projetar.\n- **Etapa 2:** O para-si não flutua no vazio abstrato; ele emerge situado no interior do mundo das coisas materiais (*em-si*), conferindo-lhes significado, utilidade e direção através de sua liberdade encarnada, o que consagra a alternativa A."
    ))

    questoes_brutas.append((
        52, "EM13CHS502", "dificil",
        "Ao confrontar a dialética hegeliana da necessidade, de que modo a transição existencial entre as esferas da vida ocorre na perspectiva de Kierkegaard?",
        [
            ("A mudança de esfera existencial não se dá por dedução conceitual necessária, mas requer crises íntimas, rupturas e um salto voluntário de risco.", True),
            ("As transformações subjetivas ocorrem por processos biológicos automáticos que acompanham a maturação física do cérebro.", False),
            ("A passagem para a esfera de fé ocorre compulsoriamente para todo cidadão que receba o sacramento na igreja luterana oficial.", False),
            ("O desenvolvimento moral dos indivíduos é guiado por leis de mercado comercial estudadas pelos economistas liberais britânicos.", False),
            ("A esfera estética representa o ápice definitivo do espírito humano, tornando impossível qualquer avanço para outros modos de vida.", False)
        ],
        "- **Etapa 1:** No modelo dialético hegeliano, o avanço da história ocorre por necessidade racional interna, onde o novo estágio supera e absorve o anterior.\n- **Etapa 2:** Em Kierkegaard não há necessidade lógica: o homem pode definhar a vida inteira no desespero do estádio estético; ascender ao ético ou ao religioso demanda uma ruptura dolorosa e o salto livre e arriscado da vontade, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Em O Existencialismo é um Humanismo, com que justificativa Sartre sustenta que o existencialismo é a única teoria que confere dignidade integral ao homem?",
        [
            ("Porque não transforma o ser humano em um objeto determinado por causas exteriores biológicas ou econômicas, mas o reconhece como liberdade pura.", True),
            ("Porque garante que todos os trabalhadores recebam propriedades rurais e salários vitalícios pagos por bancos estatais centrais.", False),
            ("Porque comprova que as almas humanas foram criadas por anjos celestes para governarem todos os minérios e plantas da Terra.", False),
            ("Porque estabelece que os filósofos formados nas universidades francesas devem ocupar os ministérios do poder executivo mundial.", False),
            ("Porque proíbe que os cidadãos sejam submetidos a julgamentos criminais em tribunais civis presididos por magistrados togados.", False)
        ],
        "- **Etapa 1:** As doutrinas materialistas mecanicistas e deterministas reduzem o homem a produto cego de seus impulsos, hormônios ou classe social.\n- **Etapa 2:** Sartre rebate que tratar o homem como marionete de causas exteriores é aviltá-lo; o existencialismo o enobrece ao torná-lo senhor e responsável soberano por suas escolhas e por seu destino moral, validando a alternativa A."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "De que modo a filosofia da existência de Kierkegaard influenciou a moderna teologia dialética protestante do século vinte?",
        [
            ("Ao resgatar a distância infinita e qualitativa entre o Criador Divino e as limitações mortais da criatura humana contingente.", True),
            ("Ao defender que as igrejas cristãs deviam submeter suas doutrinas à aprovação de comitês parlamentares dos governos civis.", False),
            ("Ao provar que a fé religiosa pode ser explicada integralmente por teoremas de geometria plana e trigonometria esférica.", False),
            ("Ao propor a canonização oficial de todos os generais que comandaram tropas vitoriosas em conflitos territoriais europeus.", False),
            ("Ao sustentar que o sacrifício de bens materiais dispensa os fiéis da oração interior e da busca pelo perdão de seus pecados.", False)
        ],
        "- **Etapa 1:** A teologia liberal do século XIX tentara aproximar a fé da razão burguesa e do progresso científico triunfalista.\n- **Etapa 2:** Kierkegaard inspirou teólogos contemporâneos (como Karl Barth) ao restabelecer o escândalo da cruz: a distância qualitativa infinita entre Deus e o homem, exigindo fé desarmada em meio ao temor e tremor da finitude, o que legitima a alternativa A."
    ))

    questoes_brutas.append((
        55, "EM13CHS501", "dificil",
        "Na existência concreta, de que maneira a situação-limite analisada por Karl Jaspers e Sartre opera como catalisador de autenticidade?",
        [
            ("Ao confrontar o indivíduo com o sofrimento inescapável, a culpa e a morte, rompendo as ilusões cotidianas e exigindo decisões soberanas.", True),
            ("Ao garantir que os cidadãos consigam aprovações financeiras rápidas em concursos públicos organizados por prefeituras municipais.", False),
            ("Ao permitir que as pessoas transfiram suas dívidas comerciais para instituições de caridade mantidas por fundações privadas.", False),
            ("Ao incentivar os jovens a passarem a vida em sonos prolongados para evitar o desgaste físico causado pelo trabalho diário.", False),
            ("Ao exigir que os magistrados suspendam o julgamento de crimes comuns durante os períodos de festividades carnavalescas de rua.", False)
        ],
        "- **Etapa 1:** Na rotina diária pacificada, o ser humano costuma viver em estado de distração anestesiada, repetindo papéis sociais vazios.\n- **Etapa 2:** Diante de situações-limite (o diagnóstico de doença fatal, a guerra, a perda de um filho), as desculpas deterministas de má-fé ruem; o indivíduo depara-se com sua finitude nua e é forçado a assumir a coragem de ser livre, confirmando a alternativa A."
    ))

    questoes_brutas.append((
        56, "EM13CHS502", "dificil",
        "Na formulação do autoengano da má-fé, qual objeção teórica leva Sartre a recusar a teoria freudiana do Inconsciente?",
        [
            ("Porque sustenta que a consciência é transparente para si mesma e que colocar um censor inconsciente no cérebro é uma desculpa cômoda de má-fé.", True),
            ("Porque comprovou que os sonhos noturnos são reproduções de transmissões de rádio recebidas por aparelhos receptores vizinhos.", False),
            ("Porque considerava que as teorias de Sigmund Freud haviam sido plagiadas de manuscritos medievais guardados no museu do Vaticano.", False),
            ("Porque afirmava que as doenças mentais não possuem vínculos com as experiências afetivas vivenciadas na fase da infância.", False),
            ("Porque defendia que a psicanálise devia ser substituída por sessões diárias de caminhadas ao ar livre em bosques de pinheiros.", False)
        ],
        "- **Etapa 1:** Freud explicava o autoengano através da divisão do aparelho psíquico (Ego, Id e um Censor Inconsciente que reprime impulsos).\n- **Etapa 2:** Sartre objeta filosoficamente: para que o Censor inconsciente decida o que deve ser reprimido, ele próprio precisa saber o que está reprimindo! Logo, a consciência é una e sabe o que esconde; a tese do inconsciente atua como álibi determinista de má-fé, validando a alternativa A."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "No pensamento de Kierkegaard, como o salto da fé no absurdo redefine a fronteira entre a razão lógica e a entrega espiritual?",
        [
            ("Afirma que o compromisso supremo do homem perante Deus não pode ser deduzido por silogismos, exigindo a renúncia da soberania da razão lógica.", True),
            ("Demonstra que as orações religiosas devem ser redigidas sob a forma de equações diferenciais resolvidas por computadores quânticos.", False),
            ("Obriga os monges a abandonarem os claustros monásticos para trabalharem na montagem de ferrovias nos países em industrialização.", False),
            ("Condiciona a entrada nos templos de culto à apresentação de diplomas de bacharelado em física atômica e mecânica celeste.", False),
            ("Sustenta que as verdades da teologia cristã são idênticas aos postulados da geometria euclidiana ensinados no ensino secundário.", False)
        ],
        "- **Etapa 1:** A tradição escolástica e hegeliana buscou demonstrar racionalmente a existência de Deus e harmonizar fé e intelecto.\n- **Etapa 2:** Kierkegaard rompe com essa pretensão: o infinito não cabe na lógica finita da razão humana; crer em Deus diante do absurdo (como Abraão) exige o salto no escuro, arriscando toda a existência sem garantias intelectuais prévias, consolidando a alternativa A."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Como a máxima sartriana estamos condenados a ser livres impacta o problema filosófico da responsabilidade pelas crises sociais e políticas?",
        [
            ("Impede o homem de atribuir as tragédias da história a forças cegas do destino, exigindo a assunção lúcida das consequências de nossos atos.", True),
            ("Isenta os líderes mundiais de responderem por guerras civis, pois as decisões militares são votadas em assembleias de generais.", False),
            ("Determina que as catástrofes econômicas sejam explicadas unicamente pelas posições dos cometas e eclipses solares no céu.", False),
            ("Permite que os cidadãos justifiquem seus crimes culpando as influências negativas de telejornais sensacionalistas comerciais.", False),
            ("Desobriga as nações ricas de prestarem ajuda humanitária a países devastados por terremotos e desastres geológicos naturais.", False)
        ],
        "- **Etapa 1:** O comodismo moral busca bodes expiatórios: a crise é culpa da conjuntura, dos políticos, do passado ou dos deuses.\n- **Etapa 2:** Sartre não permite essa covardia: o homem está condenado a ser livre; o mundo em que vivemos é o mundo que escolhemos tolerar, construir ou combater; a responsabilidade por cada guerra, fome ou opressão repousa sobre a práxis humana no mundo, assegurando a alternativa A."
    ))

    questoes_brutas.append((
        59, "EM13CHS501", "dificil",
        "Nas análises de Kierkegaard em Ou-Ou sobre os limites do estádio estético, como se diagnostica a fratura íntima do Desespero (Fortvivlelse)?",
        [
            ("O desespero nasce do vazio inevitável de uma vida puramente sensorial, na qual a busca incessante por prazeres passageiros esgota-se no tédio.", True),
            ("O desespero é uma reação alérgica corporal causada pela inalação de esporos de fungos que crescem em livros guardados em bibliotecas.", False),
            ("O desespero afeta apenas marinheiros que passam longos períodos navegando por oceanos austrais sem comunicação pelo rádio.", False),
            ("O desespero resulta da perda de cargos públicos remunerados em virtude de derrotas eleitorais de partidos monarquistas.", False),
            ("O desespero é superado automaticamente quando os cidadãos participam de bailes de carnaval organizados por grêmios recreativos.", False)
        ],
        "- **Etapa 1:** Em Ou-Ou, Kierkegaard demonstra que a busca incessante de novidades imediatas pelo esteta esgota-se inevitavelmente no tédio existencial.\n- **Etapa 2:** O desespero revela o vazio de uma existência puramente sensorial desprovida de compromisso moral duradouro, forçando o sujeito a buscar uma esfera superior ou definhar na angústia, o que consagra a alternativa A."
    ))

    questoes_brutas.append((
        60, "EM13CHS502", "dificil",
        "Em síntese conclusiva, qual é a contribuição inegociável de Kierkegaard e Sartre para o pensamento filosófico contemporâneo?",
        [
            ("A afirmação destemida da soberania da existência individual e da responsabilidade da liberdade contra todas as formas de determinismo e abstração.", True),
            ("A defesa incontestável de que os avanços da engenharia robótica resolverão todos os conflitos éticos e espirituais da humanidade.", False),
            ("A restauração de regimes políticos autoritários onde as decisões individuais devem ser subordinadas a conselhos militares fechados.", False),
            ("A comprovação de que as artes plásticas clássicas devem substituir as ciências empíricas na formulação das políticas públicas de saúde.", False),
            ("O abandono definitivo de qualquer preocupação com o sofrimento humano em favor da contemplação estéril de fórmulas matemáticas puras.", False)
        ],
        "- **Etapa 1:** Tanto Kierkegaard contra Hegel quanto Sartre contra o determinismo metafísico colocaram o homem real no centro da filosofia.\n- **Etapa 2:** Suas obras proclamam que a existência humana não é fórmula matemática pronta: somos liberdade, abertura e responsabilidade; ao encarar a angústia com coragem, o homem assume a nobreza de inventar seu próprio ser e comprometer-se com o mundo, coroando a alternativa A com louvor absoluto!"
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
    md.append('eixo: "Eixo V: Existencialismo, Filosofias da Diferença e Saberes Tradicionais"')
    md.append('capitulo: "Capítulo 33: As Raízes do Existencialismo: Kierkegaard e Sartre"')
    md.append('objeto_de_conhecimento: "O indivíduo singular e os três estádios da existência em Kierkegaard, a angústia como vertigem da liberdade, a tese sartriana da existência precedente à essência, o em-si e o para-si, a má-fé e a responsabilidade radical"')
    md.append('ebook_fonte: "em-fil-c33-raizes-existencialismo-kierkegaard-sartre.md"')
    md.append('habilidades:')
    md.append('  - "EM13CHS101"')
    md.append('  - "EM13CHS102"')
    md.append('  - "EM13CHS501"')
    md.append('  - "EM13CHS502"')
    md.append('total_exercicios: 60')
    md.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    md.append("---\n")

    md.append("# Lista de Exercícios: As Raízes do Existencialismo: Kierkegaard e Sartre\n")
    md.append("## Nível Básico\n")

    letras = ["A", "B", "C", "D", "E"]

    for num, hab, dif, enunciado, alternativas, resolucao in questoes:
        if num == 21:
            md.append("## Nível Intermediário\n")
        elif num == 41:
            md.append("## Nível Difícil\n")

        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-33-raizes-existencialismo-kierkegaard-sartre -->")
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
    md.append("- KIERKEGAARD, Søren. *O conceito de angústia*. Tradução de Álvaro Ribeiro. Petrópolis: Vozes, 2013.")
    md.append("- KIERKEGAARD, Søren. *Temor e tremor*. Tradução de Torrieri Guimarães. São Paulo: Nova Cultural, 1988.")
    md.append("- SARTRE, Jean-Paul. *O ser e o nada: ensaio de ontologia fenomenológica*. Tradução de Paulo Perdigão. 13. ed. Petrópolis: Vozes, 2005.")
    md.append("- SARTRE, Jean-Paul. *O existencialismo é um humanismo*. Tradução de Vergílio Ferreira. Lisboa: Edições 70, 2004.")
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
            # Atualiza mencao de letra na resolucao se houver
            letras = ["A", "B", "C", "D", "E"]
            antiga_letra = letras[corr_idx]
            nova_letra = letras[target_idx]
            resolucao = re.sub(rf'alternativa {antiga_letra}\b', f'alternativa {nova_letra}', resolucao)
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
    destino_final = "content/medio/volume-unico/filosofia/eixo-5-existencialismo-diferenca/cap-33-raizes-existencialismo-kierkegaard-sartre/ebooks/em-fil-c33-raizes-existencialismo-kierkegaard-sartre-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 33 validado e homologado com Exit Code 0!")
        print("ABERTURA HISTÓRICA DO EIXO V COM 1.980 QUESTÕES HOMOLOGADAS NA COLEÇÃO!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
