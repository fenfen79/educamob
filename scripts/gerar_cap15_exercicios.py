# -*- coding: utf-8 -*-
"""
Script de geração e validação da Lista de Exercícios - Capítulo 15: Ética da Alteridade e Responsabilidade: Lévinas e Hans Jonas
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
        "Por que o filósofo Emmanuel Lévinas propõe que a Ética deve ocupar o lugar de 'Filosofia Primeira' na história do pensamento?",
        "Porque os tratados de lógica formal foram proibidos por decretos acadêmicos na França.",
        "Porque o ser humano é interpelado pela presença viva e pela vulnerabilidade do outro antes mesmo de construir teorias racionais abstratas sobre a totalidade do mundo.",
        "Porque a astronomia grega antiga considerava o sol o centro imóvel de todo o universo visível.",
        "Porque as leis cívicas de Atenas proibiam os cidadãos de debaterem sobre a natureza física das coisas.",
        "Porque os filósofos medievais exigiam que todos os livros começassem com orações em latim clássico.",
        "B",
        "Para Lévinas, a relação com o outro não é um ramo secundário da filosofia, mas o ponto de partida fundador de toda a consciência e de todo o sentido humano."
    ))

    questoes_brutas.append((
        2, "EM13CHS501", "basico",
        "O que representa conceitualmente o 'Rosto' (le Visage) na filosofia da alteridade de Emmanuel Lévinas?",
        "O formato anatômico do crânio e a cor dos olhos descritos em manuais de medicina.",
        "A manifestação da vulnerabilidade e da nudez do outro ser humano, que me olha indefeso e me impõe o mandamento supremo 'Não matarás!'.",
        "A máscara de madeira utilizada por atores em apresentações de teatro dramático antigo.",
        "A pintura a óleo com o retrato oficial de governantes exposta em palácios reais da capital.",
        "O contorno geométrico das feições humanas medido com réguas e compassos de precisão técnica.",
        "B",
        "O Rosto em Lévinas é uma revelação ética: sua fraqueza desarmada me proíbe a violência e me convoca à responsabilidade incondicional pelo seu cuidado."
    ))

    questoes_brutas.append((
        3, "EM13CHS502", "basico",
        "Qual é o significado da 'Assimetria Ética' defendida por Lévinas nas relações interpessoais?",
        "A obrigação de dividir os custos de refeições coletivas em partes rigorosamente iguais.",
        "O fato de que minha responsabilidade pelo outro é absoluta e incondicional, não dependendo de reciprocidade, de troca comercial ou de que ele me retribua o favor.",
        "A regra de que os juízes de tribunais civis devem dar sentenças favoráveis aos parentes próximos.",
        "A determinação de que os contratos bancários devem conter juros proporcionais ao tempo de empréstimo.",
        "A exigência de que os tratados de paz internacional sejam assinados em duas vias de papel carbono.",
        "B",
        "A ética levinasiana rompe com a lógica contratual: eu sou responsável pelo outro gratuitamente, mesmo diante da ingratidão ou do silêncio alheio."
    ))

    questoes_brutas.append((
        4, "EM13CHS102", "basico",
        "Em sua crítica à tradição filosófica ocidental, como Lévinas caracteriza a tendência histórica de assimilar a alteridade à 'Totalidade'?",
        "Como uma prática saudável que estimula a navegação de frotas comerciais em alto-mar.",
        "Como um impulso de dominação intelectual que anula a diferença do outro, reduzindo o estranho e o singular aos conceitos fechados do próprio sujeito pensante.",
        "Como uma teoria biológica sobre a rotação das células durante a divisão embrionária animal.",
        "Como uma regra gramatical para a tradução de poemas épicos escritos na Grécia antiga.",
        "Como um plano pedagógico para o ensino de geometria nas academias de oficiais de infantaria.",
        "B",
        "Lévinas denuncia que o pensamento ocidental tradicional muitas vezes tentou englobar e domesticar a alteridade, abrindo caminho para a intolerância e para o totalitarismo."
    ))

    questoes_brutas.append((
        5, "EM13CHS501", "basico",
        "Qual diagnóstico central o filósofo Hans Jonas apresenta em O Princípio Responsabilidade sobre as éticas do passado?",
        "Que elas foram escritas em dialetos que ninguém mais conseguia ler com fluência gramatical.",
        "Que elas se tornaram insuficientes porque foram pensadas para o curto alcance entre contemporâneos, não prevendo o poder destrutivo global da tecnologia moderna sobre o futuro.",
        "Que elas proibiam a construção de relógios mecânicos nas torres das catedrais europeias.",
        "Que elas determinavam que todos os cidadãos adultos deveriam plantar árvores frutíferas no quintal.",
        "Que elas consideravam os mares e oceanos entidades divinas intocáveis pela navegação naval.",
        "B",
        "Jonas demonstra que as éticas tradicionais regulavam apenas o contato imediato entre vizinhos, pressupondo uma natureza inesgotável que a técnica moderna passou a ameaçar."
    ))

    questoes_brutas.append((
        6, "EM13CHS502", "basico",
        "Como Hans Jonas formula o novo 'Imperativo Ético' para a civilização tecnológica contemporânea?",
        "Age sempre para acumular o maior volume de moedas de prata e ouro antes da velhice.",
        "Age de tal modo que os efeitos de tua ação sejam compatíveis com a permanência de uma autêntica vida humana sobre a Terra.",
        "Age de acordo com as ordens emitidas pelos generais condecorados em tempos de combate armado.",
        "Age buscando a velocidade máxima na produção industrial sem prestar atenção aos resíduos sólidos.",
        "Age obedecendo cegamente aos costumes ancestrais sem questionar as leis civis do parlamento.",
        "B",
        "O imperativo de Jonas impõe um limite existencial: nenhuma inovação técnica ou proveito imediato tem legitimidade se colocar em perigo a continuidade da vida futura na Terra."
    ))

    questoes_brutas.append((
        7, "EM13CHS503", "basico",
        "Em que consiste o método da 'Heurística do Medo' formulado por Hans Jonas?",
        "Em um sentimento de pavor paralisante que faz as pessoas abandonarem seus postos de trabalho no campo.",
        "Em uma prudência preventiva metódica: diante da incerteza sobre os impactos de uma nova tecnologia, deve-se dar prioridade ao prognóstico mais cauteloso para proteger a vida.",
        "No medo que as crianças sentem de tempestades com raios e trovões durante as noites de inverno.",
        "Na proibição do ensino de física e de biologia em escolas públicas de primeiras letras da capital.",
        "Na exigência de que os cientistas assinem termos de silêncio sobre descobertas médicas em laboratórios.",
        "B",
        "A heurística do medo jonasiana é lucidez preventiva: não é covardia cega, mas a sabedoria de frear a técnica quando houver risco de catástrofe irreversível para a humanidade."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "Por que, para Hans Jonas, a humanidade atual tem uma obrigação moral unilateral para com as 'Gerações Futuras'?",
        "Porque as futuras gerações assinaram contratos bancários de empréstimo financeiro no presente.",
        "Porque os seres que ainda vão nascer dependem inteiramente das condições ecológicas que deixarmos, sendo incapazes de votar ou de se defender de nossas ações presentes.",
        "Porque as leis eleitorais municipais reservam vagas parlamentares para os descendentes de prefeitos.",
        "Porque os tratados internacionais exigem que os nascituros paguem impostos sobre propriedades rurais.",
        "Porque a história humana se repete ciclicamente em períodos exatos de duzentos e cinquenta anos.",
        "B",
        "A relação com os que virão é puramente assimétrica e vulnerável: eles não têm como exigir seus direitos hoje; nossa responsabilidade para com o amanhã é um dever moral irrecusável."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "Como a ética de Hans Jonas concebe o valor da 'Natureza não humana' e da biosfera planetária?",
        "Como uma matéria-prima inerte e descartável criada unicamente para ser explorada pelo comércio.",
        "Como um sistema vivo de teias integradas que possui valor próprio e que deve ser preservado para que a própria dignidade humana continue a existir no planeta.",
        "Como um obstáculo físico perigoso que deve ser pavimentado com camadas de asfalto e concreto.",
        "Como uma fonte inesgotável de combustíveis fósseis que jamais sofrerá desgaste ou poluição química.",
        "Como um conjunto de forças hostis que devem ser domesticadas pelo uso contínuo de pesticidas industriais.",
        "B",
        "Jonas rompe com o mecanicismo antropocêntrico: a natureza não é mero almoxarifado do ser humano; ela abriga a teia sagrada da vida e exige cuidado ético reverente."
    ))

    questoes_brutas.append((
        10, "EM13CHS502", "basico",
        "Quais categorias de pessoas fragilizadas Lévinas resgata da tradição antiga como arquétipos da vulnerabilidade ética do Outro?",
        "Os generais comandantes de exércitos que retornam vitoriosos de batalhas marítimas.",
        "O estrangeiro desterrado, o órfão sem amparo e a viúva desvalida, que encarnam a nudez social que clama por acolhimento e proteção.",
        "Os banqueiros enriquecidos pelo comércio de moedas de prata em feiras portuárias.",
        "Os magistrados de tribunais superiores que redigem sentenças em livros encadernados em couro.",
        "Os proprietários de fazendas que empregam dezenas de colonos no cultivo de cana-de-açúcar.",
        "B",
        "Lévinas recupera esses arquétipos clássicos para ilustrar a alteridade radical: aqueles que não possuem poder social, armas ou escudos para se defender de nosso arbítrio."
    ))

    questoes_brutas.append((
        11, "EM13CHS503", "basico",
        "Qual princípio fundamental do Direito Ambiental contemporâneo foi diretamente inspirado pelo pensamento de Hans Jonas?",
        "O princípio do livre comércio marítimo sem inspeção aduaneira de produtos agrícolas.",
        "O Princípio da Precaução, que determina a prevenção contra ameaças de danos ambientais graves mesmo antes de haver certeza científica definitiva.",
        "O princípio da imunidade tributária para empresas que constroem represas hidrelétricas.",
        "O princípio da soberania absoluta do governante sobre todas as florestas da nação.",
        "O princípio de que os recursos hídricos devem pertencer exclusivamente aos donos das terras ribeirinhas.",
        "B",
        "A precaução ecológica (presente na Declaração do Rio - ECO-92 e na lei brasileira) deriva da heurística do medo de Jonas: agir preventivamente antes que a destruição se torne irreversível."
    ))

    questoes_brutas.append((
        12, "EM13CHS102", "basico",
        "Diante de traumas históricos do século XX como os campos de extermínio de Auschwitz, qual conclusão ética Emmanuel Lévinas e Hans Jonas compartilharam?",
        "Que as fábricas de armamentos deveriam aumentar a produção diária de munições de chumbo.",
        "Que as filosofias abstratas que ignoram a dor humana e o cuidado com a vida tornam-se cúmplices da barbárie e precisam ser superadas por uma ética da responsabilidade.",
        "Que os tratados de diplomacia internacional só deveriam ser redigidos no idioma alemão arcaico.",
        "Que as universidades deveriam substituir as aulas de humanidades por treinamentos de hipismo militar.",
        "Que os conflitos armados entre nações vizinhas decorrem unicamente de desavenças comerciais de tecelagem.",
        "B",
        "Ambos os autores viveram a tragédia do nazismo e romperam com a indiferença teórica: a filosofia só tem sentido se colocar a defesa do vulnerável no centro do pensamento."
    ))

    questoes_brutas.append((
        13, "EM13CHS501", "basico",
        "Como a situação dos refugiados que chegam às fronteiras internacionais exemplifica a 'epifania do Rosto' em Lévinas?",
        "Comprovando que os guardas de fronteira devem cobrar tarifas alfandegárias em moedas estrangeiras.",
        "Mostrando que o olhar vulnerável e desamparado de famílias exaustas rasga as convenções burocráticas e impõe um apelo ético universal de acolhimento e proteção da vida.",
        "Exigindo que os migrantes apresentem certificados de proficiência em matemática avançada.",
        "Determinando que os navios de resgate marítimo retornem aos portos de origem sem descarregar mantimentos.",
        "Demonstrando que os passaportes diplomáticos devem ser impressos em papel com marcas d'água especiais.",
        "B",
        "O rosto do refugiado expõe a precariedade humana pura: antes de qualquer barreira legal ou nacionalista, há um ser humano cuja fragilidade me proíbe a rejeição e me cobra socorro."
    ))

    questoes_brutas.append((
        14, "EM13CHS502", "basico",
        "Qual é um erro comum e recorrente na compreensão do conceito de 'Rosto' na obra de Emmanuel Lévinas?",
        "Achar que o Rosto é apenas um vocábulo hebraico para designar o nascer do sol nas montanhas.",
        "Reduzir o Rosto à aparência física visual ou à beleza estética dos traços corporais, quando se trata da revelação ética da fragilidade humana.",
        "Acreditar que o Rosto se refere exclusivamente a estátuas de mármore esculpidas em praças municipais.",
        "Sustentar que o conceito só se aplica a indivíduos que exercem cargos de liderança no parlamento.",
        "Afirmar que o Rosto foi uma teoria anatômica sobre a circulação do sangue na musculatura facial.",
        "B",
        "O Rosto levinasiano não é estética; é ética profunda: mesmo um rosto coberto ou desfigurado emite a exigência inegociável de respeito e dignidade."
    ))

    questoes_brutas.append((
        15, "EM13CHS503", "basico",
        "Por que é incorreto acusar Hans Jonas de ser um autor 'tecnofóbico' que odiava o progresso e a ciência?",
        "Porque ele trabalhava como piloto de locomotivas em empresas de transporte ferroviário de passageiros.",
        "Porque ele reconhecia plenamente as conquistas da ciência para a saúde e o saneamento, alertando unicamente contra a desregulamentação cega de técnicas com poder de autodestruição planetária.",
        "Porque ele defendia a substituição de todos os medicamentos por rezas comunitárias em praça pública.",
        "Porque ele patenteou invenções mecânicas de moagem de trigo durante sua juventude acadêmica.",
        "Porque ele afirmava que os computadores eletrônicos deveriam ser operados exclusivamente por crianças.",
        "B",
        "Jonas não prega a volta à barbárie pré-histórica; sua ética é uma bússola para que a ciência continue a salvar vidas sem destruir os alicerces futuros da própria vida."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Como a problemática das mudanças climáticas globais se articula diretamente com o Princípio Responsabilidade?",
        "Determinando que as medições de temperatura atmosférica sejam realizadas com termômetros de mercúrio.",
        "Evidenciando que as emissões de gases poluentes do presente sacrificam o bem-estar e a segurança dos seres humanos que habitarão a Terra nas próximas décadas e séculos.",
        "Afirmando que a queima de carvão mineral melhora a fertilidade dos solos agrícolas no inverno.",
        "Propondo que as usinas nucleares sejam construídas nas margens de praias com intensa visitação de turistas.",
        "Comprovando que os animais marinhos aumentam sua taxa reprodutiva quando as águas se tornam mais ácidas.",
        "B",
        "O aquecimento global é o caso exemplar de Jonas: a ganância do presente impõe custos catastróficos aos que ainda não nasceram, exigindo freios éticos imediatos."
    ))

    questoes_brutas.append((
        17, "EM13CHS502", "basico",
        "O que afirma a ética de Lévinas a respeito de quem exige 'garantias de gratidão' antes de prestar auxílio a alguém vulnerável?",
        "Que essa exigência comprova o mais alto grau de sabedoria prática e maturidade moral da pessoa.",
        "Que ela rebaixa a obrigação ética a um mero cálculo contábil e mercantil de troca egoísta, desvirtuando a gratuidade da responsabilidade pelo outro.",
        "Que essa atitude é obrigatória segundo os tratados de direito internacional civil do continente.",
        "Que ela fortalece a solidariedade fraterna entre vizinhos de um mesmo conjunto residencial.",
        "Que ela confirma as regras tradicionais de doação de mantimentos estabelecidas por corporações de ofício.",
        "B",
        "Se ajudo esperando retribuição, não estou sendo ético no sentido levinasiano; estou fazendo negócios com a carência do irmão."
    ))

    questoes_brutas.append((
        18, "EM13CHS501", "basico",
        "No debate sobre Inteligência Artificial autônoma em armamentos militares (drones que decidem disparar sem controle humano), qual postura a heurística do medo preconiza?",
        "Liberar a comercialização imediata das armas para aumentar as receitas fiscais do Ministério da Fazenda.",
        "Adotar uma moratória preventiva rigorosa, dando prioridade ao risco de massacres e desumanização para vetar a delegação de decisões vitais a algoritmos mecânicos.",
        "Incentivar que os jovens programadores realizem competições de ataque digital contra hospitais públicos.",
        "Transferir o comando de todas as guarnições militares para companhias privadas de segurança patrimonial.",
        "Substituir o treinamento de soldados de infantaria por partidas de jogos eletrônicos de entretenimento.",
        "B",
        "Diante de riscos de catástrofe ética irreversível, o princípio de Jonas exige a interdição preventiva: uma máquina não possui Rosto nem empatia e jamais pode ter o poder sobre a vida humana."
    ))

    questoes_brutas.append((
        19, "EM13CHS503", "basico",
        "Como as pesquisas sobre os 'Nove Limites Planetários' no campo da biologia confirmam empiricamente as teses de Hans Jonas?",
        "Mostrando que os oceanos podem absorver qualquer quantidade de lixo plástico sem sofrerem desequilíbrio biológico.",
        "Demonstrando que a biosfera possui limites físicos concretos de regeneração e que ultrapassar esses limites pode desestabilizar irreversivelmente as condições de vida segura na Terra.",
        "Provando que as florestas equatoriais crescem mais rápido quando expostas a secas prolongadas no verão.",
        "Afirmando que a camada de ozônio atmosférica se recupera espontaneamente em contato com gases industriais tóxicos.",
        "Comprovando que a perda de espécies de insetos polinizadores não afeta a produção de alimentos agrícolas.",
        "B",
        "A ciência contemporânea valida o aviso de Jonas: a natureza não tem capacidade infinita de amortecer agressões; o planeta tem pontos de não retorno que ameaçam a nossa existência."
    ))

    questoes_brutas.append((
        20, "EM13CHS102", "basico",
        "Qual é o mandamento silencioso, mas imperativo, que emana da nudez do Rosto na filosofia levinasiana?",
        "Acumula bens materiais para garantir a tranquilidade de teus herdeiros diretos.",
        "Não matarás! Tu não cometerás o assassinato nem aniquilarás a dignidade daquele que está desarmado diante de ti.",
        "Obedece fielmente aos governantes que possuem mais armas em seus arsenais militares.",
        "Procura vencer todas as disputas verbais para demonstrar a superioridade de tua inteligência.",
        "Trabalha durante todas as horas do dia para merecer o descanso nas noites de lua cheia.",
        "B",
        "O mandamento primordial que o Outro me impõe com seu simples olhar indefeso é a interdição total da violência: tu não tens o poder moral de me destruir."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao contrastar o imperativo categórico de Immanuel Kant ('Age de modo que a máxima de tua vontade possa valer como lei universal') com o imperativo de Hans Jonas, qual é o deslocamento ético fundamental operado pelo autor contemporâneo?",
        "Kant focava na velocidade da produção fabril, enquanto Jonas se preocupa com os salários pagos aos trabalhadores operários.",
        "Kant formulou um dever formal voltado à coerência racional do ato no presente entre contemporâneos, enquanto Jonas elabora um dever voltado aos efeitos físicos de longo prazo sobre a continuidade da vida futura na Terra.",
        "Kant defendia que a moralidade dependia exclusivamente das leis do parlamento civil, enquanto Jonas defende o regresso às leis feudais.",
        "Kant considerava que os animais tinham direitos políticos superiores aos humanos, enquanto Jonas rejeita qualquer preocupação ecológica.",
        "Kant negava a existência da razão prática na vida civil, enquanto Jonas afirma que a ciência mecânica resolve todas as dúvidas éticas.",
        "B",
        "Jonas atualiza o imperativo ético para a era da tecno-ciência: a moral não pode ficar presa à intenção desincorporada do presente; ela deve responder pelas consequências ecológicas no tempo geológico."
    ))

    questoes_brutas.append((
        22, "EM13CHS501", "intermediario",
        "Por que, para Emmanuel Lévinas, a ontologia tradicional ocidental praticou uma 'violência conceitual' contra a alteridade?",
        "Porque ela queimava livros de matemática aplicada em praças públicas de cidades gregas.",
        "Porque ela reduziu o que é diferente e singular a categorias gerais do 'Mesmo', subordinando a pessoa concreta a sistemas teóricos fechados e universais que anulam sua dignidade única.",
        "Porque os filósofos clássicos se recusavam a traduzir seus textos para as línguas faladas por marinheiros.",
        "Porque os tratados de lógica formal exigiam pagamentos em barras de prata para serem copiados à mão.",
        "Porque a metafísica helênica proibia a prática de esportes atléticos durante as festas cívicas.",
        "B",
        "A ontologia da totalidade devora a diferença: trata o outro não como um ser infinito e misterioso, mas como uma peça a ser encaixada e manipulada pelo sistema do sujeito pensante."
    ))

    questoes_brutas.append((
        23, "EM13CHS502", "intermediario",
        "No horizonte do Princípio Responsabilidade, qual é a contradição insolúvel das éticas utilitaristas do cálculo de prazer e dor diante dos dilemas contemporâneos?",
        "O fato de que os instrumentos mecânicos de medição térmica sofrem dilatação com o calor intenso do meio-dia.",
        "O fato de que calcular a felicidade imediata da maioria da população presente pode justificar a exaustão predatória dos recursos da Terra, condenando as gerações futuras à miséria e à morte ecológica.",
        "A obrigatoriedade de que as empresas privadas publiquem seus balanços financeiros semestrais em jornais de bairro.",
        "A exigência de que os tribunais criminais convoquem os cidadãos para participarem de júris populares obrigatórios.",
        "A premissa de que a matemática não deve ser aplicada na contabilidade de estoques de grãos nas cooperativas.",
        "B",
        "O utilitarismo tradicional é míope temporalmente: a maioria que vive hoje pode decidir queimar petróleo e lucrar no curto prazo, transferindo o desastre para os que não podem votar hoje."
    ))

    questoes_brutas.append((
        24, "EM13CHS503", "intermediario",
        "Como a distinção levinasiana entre o 'Mesmo' e o 'Outro' explica a facilidade com que discursos xenófobos desumanizam populações imigrantes em países desenvolvidos?",
        "Demonstrando que os imigrantes desconhecem as técnicas de carpintaria naval utilizadas na construção de veleiros.",
        "Evidenciando que a sociedade dominante enxerga a si mesma como o padrão normal (o Mesmo) e classifica o estrangeiro diferente como uma anomalia perigosa que ameaça a pureza da totalidade cultural estabelecida.",
        "Afirmando que as línguas de povos migrantes não possuem pronomes pessoais para indicar a primeira pessoa do singular.",
        "Sustentando que os tratados de comércio de tecidos exigem certificados de origem sanitária das mercadorias.",
        "Provando que as fronteiras geográficas entre países europeus foram desenhadas exclusivamente pelo curso natural dos rios.",
        "B",
        "O nacionalismo xenófobo encarna a totalidade opressora: quem não se molda ao 'Mesmo' é demonizado e rotulado como invasor, apagando a humanidade de seu Rosto."
    ))

    questoes_brutas.append((
        25, "EM13CHS102", "intermediario",
        "Por que Hans Jonas rejeitou veementemente as utopias tecno-otimistas modernas (como o marxismo de Ernst Bloch ou o fetiche do progresso liberal ilimitado)?",
        "Porque ele defendia que as ferrovias deveriam ser desmanteladas para o restabelecimento do transporte por mulas de carga.",
        "Porque essas utopias apostam todas as fichas em um futuro radiante artificial alcançado pela aceleração tecnológica e pelo domínio da natureza, correndo o risco fatal de destruir o planeta antes de atingir sua meta.",
        "Porque ele sustentava que as universidades deveriam suspender a publicação de teses acadêmicas de economia política.",
        "Porque ele acreditava que os governantes republicanos deveriam adotar títulos nobiliárquicos concedidos por imperadores.",
        "Porque ele considerava que a energia elétrica causava alterações irreversíveis no comportamento de animais domésticos.",
        "B",
        "Para Jonas, prometer um paraíso tecnológico futuro que custa a exaustão da Terra é leviandade criminosa: o dever supremo não é alcançar utopias perfeitas, mas garantir que a vida humana continue a ser viável."
    ))

    questoes_brutas.append((
        26, "EM13CHS501", "intermediario",
        "Na fenomenologia do Rosto de Lévinas, qual é o paradoxo ético entre a 'vulnerabilidade física' do Outro e a sua 'autoridade moral'?",
        "O Outro possui músculos corporais treinados para combate corpo a corpo, mas sua linguagem verbal é excessivamente tímida.",
        "Fisicamente o Outro é frágil, indefeso e mortal (eu tenho o poder material de aniquilá-lo), mas moralmente ele se ergue como uma autoridade sagrada que paralisa minha força e me proíbe a agressão.",
        "O Outro comanda batalhões militares em alto-mar, mas não possui autorização legal para assinar cheques comerciais.",
        "O Outro domina as fórmulas da geometria plana euclidiana, mas desconhece os métodos de plantio de milho no outono.",
        "O Outro possui certidões civis autenticadas em cartórios municipais, mas recusa-se a prestar juramento perante a bandeira.",
        "B",
        "Esse é o coração de Lévinas: a altura do outro não emana de canhões ou poder econômico, mas de sua extrema indigência ética que comanda 'Não matarás!' à minha força."
    ))

    questoes_brutas.append((
        27, "EM13CHS502", "intermediario",
        "De que maneira a decisão da comunidade médica internacional de aplicar o Princípio da Precaução sobre a edição genética germinativa em humanos (CRISPR-Cas9) reflete o pensamento de Hans Jonas?",
        "Substituindo todos os medicamentos sintéticos por xaropes fitoterápicos produzidos com folhas secas.",
        "Freando a aplicação clínica em embriões diante do risco irreversível de gerar anomalias genéticas hereditárias e criar castas biológicas segregadas, priorizando a segurança da linhagem humana futura sobre a vaidade científica.",
        "Obrigando os hospitais públicos a transferirem seus pacientes para clínicas situadas em ilhas marítimas distantes.",
        "Determinando que os tratamentos de quimioterapia oncológica devam ser autorizados por votação em praça pública.",
        "Proibindo o uso de microscópios eletrônicos em laboratórios universitários de biologia molecular.",
        "B",
        "A bioética contemporânea incorpora Jonas: alterar o genoma germinativo humano sem conhecer os desdobramentos de longo prazo ameaça a essência da humanidade; na dúvida, o dever é prevenir e frear."
    ))

    questoes_brutas.append((
        28, "EM13CHS503", "intermediario",
        "Ao romper com o filósofo Martin Heidegger após 1933, qual crítica profunda Emmanuel Lévinas direcionou à ontologia existencial de seu antigo mestre?",
        "A de que Heidegger utilizava canetas de pena de ganso em vez de instrumentos de escrita mecânicos modernos.",
        "A de que a ontologia heideggeriana subordinava a relação humana com o outro a um 'Ser' abstrato e impessoal, permanecendo cega à dor do indivíduo de carne e osso e conivente com a violência totalitária.",
        "A de que as aulas de filosofia proferidas nas universidades da Alemanha consumiam muito carvão para aquecer as salas.",
        "A de que a interpretação filosófica do sentido recusava a leitura de romances poéticos escritos por autores franceses clássicos.",
        "A de que a metafísica alemã desconhecia as equações da termodinâmica aplicadas em motores a vapor industriais.",
        "B",
        "Lévinas denunciou que a fascinação pelo Ser anônimo esqueceu o Rosto humano: quando a filosofia coloca a teoria do ser acima do mandamento de não matar o irmão, ela se torna cúmplice do nazismo."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Como a metáfora bíblica do 'órfão, da viúva e do estrangeiro' em Lévinas ressignifica o conceito de Cidadania nas democracias contemporâneas?",
        "Exigindo que apenas pessoas que perderam os pais possam concorrer a mandatos no poder legislativo municipal.",
        "Definindo a solidez democrática não pelo poder econômico dos mais fortes, mas pela capacidade real da sociedade de acolher, proteger e garantir dignidade àqueles que estão à margem dos privilégios sociais.",
        "Determinando que as famílias rurais recebam o dobro de sementes para o plantio durante as estações chuvosas do ano.",
        "Propondo que os tribunais civis devam funcionar exclusivamente durante o período diurno em dias úteis da semana.",
        "Afirmando que a cidadania política depende do pagamento prévio de taxas aduaneiras sobre o comércio de tecidos.",
        "B",
        "A verdadeira cidadania levinasiana é medida pelo atendimento ao vulnerável: uma sociedade justa não é a que ostenta arranha-céus, mas a que não deixa o desamparado perecer na solidão."
    ))

    questoes_brutas.append((
        30, "EM13CHS502", "intermediario",
        "Por que Hans Jonas sustenta que a responsabilidade dos pais para com os filhos recém-nascidos é o 'arquétipo primordial de toda responsabilidade ética'?",
        "Porque os pais são obrigados por contratos comerciais a pagar as despesas de alimentação dos filhos até a vida adulta.",
        "Porque o bebê é a encarnação viva da total vulnerabilidade e da pura dependência: diante de sua fragilidade que não pode retribuir nem se defender, impõe-se aos pais o dever natural e incondicional de zelar pela sua vida.",
        "Porque as leis cívicas de herança patrimonial exigem certidões de nascimento registradas em cartórios de imóveis.",
        "Porque as famílias numerosas recebiam títulos de condecoração militar em regimes absolutistas da Europa.",
        "Porque o recém-nascido possui direitos eleitorais assegurados por constituições republicanas federais.",
        "B",
        "O bebê é o modelo da responsabilidade jonasiana: sua fragilidade me intima a cuidar dele sem exigir nada em troca; é essa mesmíssima obrigação assimétrica que a humanidade atual tem para com as gerações que virão."
    ))

    questoes_brutas.append((
        31, "EM13CHS503", "intermediario",
        "Em processos judiciais movidos por jovens ativistas ambientais contra governos por inação climática, qual tese de Hans Jonas é mobilizada nos tribunais?",
        "A de que os ministros de Estado devem prestar contas financeiras semanais aos presidentes dos bancos centrais.",
        "A de que as decisões políticas do presente não podem destruir o direito das gerações futuras de herdarem um planeta biologicamente habitável e com equilíbrio ecológico preservado.",
        "A de que as florestas de pinheiros produzem excesso de oxigênio prejudicial à respiração de operários industriais.",
        "A de que os veículos de transporte coletivo devem ser fabricados com ligas de cobre importadas do exterior.",
        "A de que os tratados de comércio naval perdem a validade jurídica quando ocorrem tufões em mares tropicais.",
        "B",
        "O litígio climático é a materialização jurídica de Jonas: as cortes constitucionais reconhecem que o presente comete crime intergeracional quando consome os recursos e lega uma Terra tóxica aos jovens."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Como a noção de 'Infinito' em Totalidade e Infinito de Lévinas se contrapõe à ideia de totalização e fechamento da realidade?",
        "O Infinito é a contagem numérica de grãos de areia acumulados nas praias litorâneas durante a maré baixa.",
        "O Infinito representa aquilo que transcende qualquer tentativa de apreensão ou controle racional do sujeito: o Outro é infinito porque jamais pode ser domesticado ou plenamente conhecido pelo meu pensamento.",
        "O Infinito é uma fórmula de astronomia aplicada para calcular a distância entre cometas que cruzam o sistema solar.",
        "O Infinito é uma metáfora poética sobre a profundidade de minas subterrâneas de extração de carvão vegetal.",
        "O Infinito é o tempo gasto por navegadores para contornar os cabos meridionais dos oceanos polares.",
        "B",
        "O Outro escapa à totalidade: por mais que eu o estude ou catalogue, ele é sempre um mistério que transborda meus conceitos; essa irredutibilidade é o Infinito que me convoca ao respeito."
    ))

    questoes_brutas.append((
        33, "EM13CHS501", "intermediario",
        "Qual é o impacto da constatação de Hans Jonas de que 'o homem tornou-se uma ameaça para o seu próprio futuro' na crítica ao ideal moderno de Progresso?",
        "Ela confirma que os motores a vapor têm rendimento térmico superior ao das caldeiras a lenha nos moinhos rurais.",
        "Ela desmistifica a crença cega e linear do Iluminismo e do Positivismo de que todo avanço científico e tecnológico traria automaticamente emancipação moral e bem-estar à humanidade.",
        "Ela prova que as estradas de ferro deveriam ser construídas com dormentes de madeira de lei certificada.",
        "Ela afirma que as companhias de eletricidade deveriam desligar as turbinas durante todos os finais de semana festivos.",
        "Ela determina que as cidades industriais devem proibir a realização de feiras livres de alimentos hortifrutigranjeiros.",
        "B",
        "A técnica sem limites gerou Hiroshima e a crise ecológica: Jonas desconstrói o mito de que o progresso técnico é neutro ou benevolente por si mesmo; ele pode ser o carrasco da humanidade se não for domado pela ética."
    ))

    questoes_brutas.append((
        34, "EM13CHS502", "intermediario",
        "De que modo a ética de Lévinas oferece alternativas ao individualismo atomista dominante nas sociedades capitalistas contemporâneas?",
        "Propondo que todos os trabalhadores assinados em carteira dividam suas roupas íntimas com colegas de trabalho.",
        "Demonstrando que a identidade do indivíduo não se funda no isolamento egoísta ou no consumo possessivo de mercadorias, mas na capacidade de ser tocado pelo sofrimento alheio e de responder com acolhimento e partilha.",
        "Exigindo que as lojas comerciais fechem suas portas durante todas as terças-feiras do calendário civil nacional.",
        "Defendendo que as construções residenciais urbanas devem possuir paredes de vidro transparentes sem cortinas.",
        "Determinando que os cidadãos adultos devem realizar tarefas diárias de capina em canteiros de praças municipais.",
        "B",
        "Lévinas resgata o sujeito da prisão do ego: ser plenamente humano não é acumular coisas para si no solipsismo burguês, mas estar disponível para socorrer e amparar o irmão que sofre."
    ))

    questoes_brutas.append((
        35, "EM13CHS503", "intermediario",
        "Por que Hans Jonas defende que o medo preventivo deve ser despertado pela imaginação ética antes que a catástrofe tecnológica concreta aconteça?",
        "Porque o medo irracional incentiva a venda de apólices de seguro contra acidentes pessoais nas metrópoles.",
        "Porque esperar que o desastre ecológico ou biológico ocorra no mundo real para só então tentar corrigi-lo é tarde demais, pois certas destruições tecnológicas de grande escala são completamente irreversíveis.",
        "Porque as patrulhas de infantaria militar necessitam de estados de alerta para realizarem exercícios de marcha no campo.",
        "Porque as emissoras de rádio obtêm maior audiência quando transmitem boletins informativos sobre tempestades marinhas.",
        "Porque os governantes autoritários utilizam o pânico popular para promulgarem leis de censura sobre livros de ficção.",
        "B",
        "A irreversibilidade do dano tecnológico muda as regras: não podemos esperar os oceanos acidificarem totalmente para criar regras; a imaginação ética do perigo (heurística do medo) deve agir antes do ponto de não retorno."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Qual é a relação entre a noção de 'Responsabilidade como Acolhimento' em Lévinas e o tratamento conferido a pessoas em situação de rua nas grandes cidades?",
        "A determinação de que as autoridades policiais utilizem viaturas blindadas para retirar pertences pessoais de calçadas.",
        "A exigência moral de não desviar o olhar nem transformar o morador de rua em estorvo urbanístico invisível, reconhecendo a epifania de seu Rosto que clama por dignidade, abrigo e reconhecimento humano incondicional.",
        "A recomendação de que as prefeituras construam muros de concreto armado ao redor de praças públicas para evitar aglomerações.",
        "O incentivo para que as empresas de segurança privada instalem grades de ferro nas marquises de prédios comerciais.",
        "A certeza de que as refeições servidas em albergues públicos devem ser cobradas por meio de moedas de prata.",
        "B",
        "A aporofobia (rejeição ao pobre) é a recusa do Rosto: Lévinas exige que olhemos nos olhos do homem na calçada e sintamos a interpelação de sua humanidade ferida, superando a indiferença cúmplice."
    ))

    questoes_brutas.append((
        37, "EM13CHS502", "intermediario",
        "Em que sentido o Princípio Responsabilidade de Hans Jonas transforma a relação tradicional entre Ciência e Sociedade?",
        "Subordinando a atividade científica aos comandos emitidos por generais condecorados de infantaria.",
        "Exigindo que a pesquisa científica e a inovação técnica não se escondam sob o biombo da suposta neutralidade de valores, devendo prestar contas públicas e éticas de seus impactos futuros sobre a biosfera e a humanidade.",
        "Proibindo a compra de reagentes químicos importados por laboratórios de universidades federais.",
        "Determinando que os cientistas devam prestar juramentos de obediência a ordens religiosas internacionais.",
        "Exigindo que todos os artigos científicos sejam publicados exclusivamente na língua latina clássica.",
        "B",
        "A ciência não pode ser um império isolado do bem e do mal: quem desenvolve biotecnologia ou armas deve responder perante a sociedade civil pelos riscos que joga sobre o futuro coletivo."
    ))

    questoes_brutas.append((
        38, "EM13CHS503", "intermediario",
        "Qual paralelo ético pode ser estabelecido entre a ética comunitária africana do Ubuntu (Capítulo 14) e a ética da alteridade de Lévinas (Capítulo 15)?",
        "Ambas defendem que a economia de mercado desregulada é o único modelo compatível com a paz cívica entre os povos.",
        "Ambas rompem com o solipsismo do indivíduo autosuficiente ocidental, sustentando que a condição humana só se realiza plenamente no encontro, no cuidado e na responsabilidade viva para com o outro.",
        "As duas correntes afirmam que as decisões judiciais criminais devem prever sentenças de desterro marítimo em ilhas distantes.",
        "Ambas sustentam que as leis tributárias devem isentar os comerciantes de grãos do pagamento de taxas municipais.",
        "As duas visões concordam que os tratados de diplomacia internacional perdem o valor em períodos de geada no inverno.",
        "B",
        "Tanto no Ubuntu ('Eu sou porque nós somos') quanto em Lévinas (a ética como filosofia primeira), o sujeito não é uma ilha: minha humanidade é tecido compartilhado que depende da alteridade."
    ))

    questoes_brutas.append((
        39, "EM13CHS102", "intermediario",
        "Como a Declaração Universal sobre Bioética e Direitos Humanos da UNESCO reflete a herança intelectual de Hans Jonas?",
        "Incentivando o uso de armamentos convencionais pesados em treinamentos militares de fronteira terrestre.",
        "Incorporando explicitamente o dever de proteção das futuras gerações e a consideração dos impactos das ciências da vida sobre a biosfera e sobre a diversidade genética da espécie humana.",
        "Determinando que as patentes de medicamentos genéricos devam pertencer perpetuamente a laboratórios multinacionais.",
        "Exigindo que os comitês de bioética hospitalar sejam compostos exclusivamente por oficiais reformados das forças armadas.",
        "Proibindo a realização de transfusões sanguíneas em pacientes atendidos em prontos-socorros de emergência.",
        "B",
        "A bioética global da UNESCO bebe na fonte de Jonas: protege as gerações que virão contra os excessos da engenharia genética e afirma o compromisso de manter a Terra como lar comum da vida."
    ))

    questoes_brutas.append((
        40, "EM13CHS501", "intermediario",
        "O que significa afirmar que, na filosofia de Lévinas, 'o ser humano é refém ético do Outro'?",
        "Que o cidadão civil deve ser mantido sob custódia prisional por guardas municipais até pagar suas dívidas bancárias.",
        "Que a interpelação da dor alheia me atinge de modo tão profundo e irrevogável que não posso simplesmente ignorá-la ou escapar de minha responsabilidade pessoal de prestar socorro.",
        "Que as empresas de navegação marítima podem reter as bagagens dos passageiros que perderem passagens de viagem.",
        "Que os jovens que concluem o ensino médio devem prestar três anos de serviços obrigatórios na construção de estradas de ferro.",
        "Que os magistrados de tribunais de justiça estão proibidos de viajar para o exterior sem autorização do Ministério da Defesa.",
        "B",
        "Ser refém do outro é uma metáfora poética e radical de Lévinas: a vulnerabilidade alheia me desestabiliza e me desaloja da minha tranquilidade egoísta, exigindo de mim resposta e compromisso."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a célebre passagem de Emmanuel Lévinas em Totalidade e Infinito: 'A relação ética não é uma relação simétrica em que eu e o outro nos pesamos na mesma balança. Eu sou responsável pelo outro sem esperar a sua reciprocidade, mesmo que isso me custe a própria vida.' De que maneira essa formulação rompe com a tradição dos contratos sociais liberais de Hobbes, Locke e Rousseau?",
        "Negando que os astrônomos do século XVII utilizassem lunetas de observação ótica para estudar os cometas celestes.",
        "Demonstrando que, ao passo que o contratualismo liberal funda a justiça em um cálculo prudencial de troca mútua e garantias recíprocas entre iguais soberanos (eu renuncio à violência se o outro também renunciar), Lévinas estabelece a obrigação ética como uma dádiva pura, desinteressada e prévia a qualquer contrato ou cálculo utilitário de conveniência.",
        "Provando que as leis comerciais da Inglaterra colonial foram redigidas por marinheiros da frota mercante da cidade de Liverpool.",
        "Afirmando que os cidadãos republicanos deveriam entregar todas as suas propriedades rurais aos cofres públicos municipais.",
        "Sustentando que os governantes civis devem cobrar impostos proporcionais à quantidade de cavalos utilizados nas lavouras.",
        "B",
        "**Etapa 1:** Compreender a estrutura do contrato social liberal: ele repousa na simetria, na reciprocidade de interesses e no cálculo de segurança própria.\n**Etapa 2:** Concluir com a radicalidade de Lévinas: a obrigação ética para com o vulnerável precede e transcende qualquer contrato jurídico; eu não cuido do outro por um acordo vantajoso, mas porque sua fraqueza sagrada me intima de modo incondicional."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em O Princípio Responsabilidade, Hans Jonas formula a seguinte tese teórica e moral: 'A promessa da técnica moderna converteu-se em ameaça. O Prometeu definitivamente desacorrentado, a quem a ciência confere forças nunca antes imaginadas e a economia um impulso infatigável, clama por uma ética que, por meio de freios voluntários, impeça seu poder de se transformar na desgraça do homem.' Como essa reflexão desmonta a premissa moderna da neutralidade da técnica?",
        "Fazendo com que as escolas de engenharia substituam o estudo da física teórica pelo ensino de cantos litúrgicos em latim.",
        "Evidenciando que a tecno-ciência contemporânea não é um instrumento neutro ou passivo à disposição do ser humano, mas uma força estrutural dotada de dinamismo expansivo autônomo que, ao se aliar à lógica da acumulação econômica, adquire poder de destruição biológica e planetária irreversível caso não seja submetida a limites éticos categóricos.",
        "Provando que as caldeiras a vapor utilizadas nas tecelagens britânicas consumiam muito carvão vegetal das florestas do norte.",
        "Afirmando que os médicos da corte prussiana desconheciam os princípios elementares da circulação sanguínea no corpo humano.",
        "Determinando que os juízes de tribunais constitucionais devam usar togas confeccionadas exclusivamente com lã de ovelhas rurais.",
        "B",
        "**Etapa 1:** Desconstruir a tese ingênua da neutralidade técnica: ferramentas simples eram neutras, mas a megatécnica moderna molda o mundo e possui escala geológica.\n**Etapa 2:** Concluir com o imperativo jonasiano: a técnica desacorrentada devora seu próprio criador; o freio voluntário e preventivo é a única garantia de que o poder técnico não aniquilará a própria possibilidade da vida humana futura."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Considere a crítica levinasiana à 'Totalidade' como a raiz teórica do totalitarismo do século XX. De que maneira a tentativa de englobar todo o real sob uma única categoria homogênea (como a Razão burguesa, a Luta de Classes dogmatizada ou a Pureza Racial ariana) desembocou historicamente na aniquilação física do Outro em regimes autoritários?",
        "Mostrando que os generais de cavalaria militar utilizavam sabres de aço fundido em oficinas rurais de armamento.",
        "Demonstrando que, quando um sistema ideológico ou filosófico declara ter capturado a totalidade da verdade e da história, qualquer indivíduo, povo ou minoria que resista à homogeneização é visto como um obstáculo intolerável e impuro que precisa ser expurgado, normalizado ou fisicamente destruído nos campos de concentração para preservar a integridade do sistema.",
        "Afirmando que os operários das indústrias químicas parisienses realizavam marchas festivas durante as comemorações da primavera.",
        "Provando que as bibliotecas universitárias da cidade de Viena foram organizadas por monges beneditinos no século XVIII.",
        "Defendendo que as regras processuais dos tribunais criminais deveriam prever a execução de peças teatrais nas audiências.",
        "B",
        "**Etapa 1:** Analisar a lógica teórica e política da totalidade: a pretensão de fechar o cosmos em um único princípio absoluto do 'Mesmo'.\n**Etapa 2:** Evidenciar a tragédia histórica: o totalitarismo nazista e soviético aplicou politicamente a totalidade; quem era diferente (o judeu, o dissidente, o estrangeiro) foi assassinado porque não cabia na fôrma do sistema; daí a necessidade vital de Lévinas resgatar o Infinito da alteridade."
    ))

    questoes_brutas.append((
        44, "EM13CHS502", "dificil",
        "Em sua obra O Princípio Responsabilidade, Hans Jonas estabelece o contraste entre o dever para com os contemporâneos e o dever para com as Gerações Futuras: 'O direito daqueles que virão depois de nós não é um direito reivindicado por sujeitos presentes, mas um dever estrito que recai unicamente sobre a nossa consciência moral atual.' Por que essa obrigação intergeracional desafia os alicerces da teoria jurídica clássica baseada em direitos subjetivos?",
        "Porque os tribunais cíveis internacionais cobram taxas judiciais calculadas na moeda corrente do país demandado.",
        "Porque a teoria jurídica tradicional exige a existência de sujeitos de direito determinados, concretos e presentes para postular direitos e celebrar pactos; as gerações futuras não existem hoje, não podem ajuizar ações nem negociar, transformando a responsabilidade atual em um dever ético puramente unilateral e assimétrico de preservação da Terra.",
        "Porque as leis eleitorais proíbem que pessoas com menos de dezoito anos exerçam cargos no corpo diplomático governamental.",
        "Porque os contratos bancários de financiamento imobiliário perdem a eficácia jurídica caso o devedor mude de cidade.",
        "Porque os magistrados dos tribunais constitucionais necessitam de assinaturas lavradas em pergaminhos de couro animal.",
        "B",
        "**Etapa 1:** Identificar o impasse do direito positivo clássico: sem sujeito vivo presente, a teoria tradicional não sabe como tutelar o amanhã.\n**Etapa 2:** Concluir com a virada ética de Jonas: a responsabilidade com o futuro rompe o molde da reciprocidade processual; o dever nasce não da pressão do outro, mas de nossa capacidade soberana de não legar um deserto ecológico aos nossos descendentes."
    ))

    questoes_brutas.append((
        45, "EM13CHS503", "dificil",
        "Analise a aplicação da 'Heurística do Medo' de Hans Jonas na deliberação internacional sobre a Geoengenharia Solar (propostas de dispersar aerossóis de enxofre na estratosfera terrestre para resfriar artificialmente o planeta e conter a crise climática). Por que o imperativo de Jonas impõe uma postura de extrema cautela e recusa a essa intervenção climática massiva?",
        "Porque os aviões a jato utilizados na dispersão de gases consomem querosene que deveria abastecer navios cargueiros.",
        "Porque os efeitos de longo prazo da geoengenharia em escala planetária sobre o regime global de chuvas, a produção agrícola e a integridade da camada de ozônio são profundamente incertos e potencialmente catastróficos; na dúvida entre o risco de colapso climático irreversível e o fetiche de uma correção tecnológica fácil, a ética nos obriga a priorizar a cautela e focar na descarbonização real da economia.",
        "Porque as indústrias químicas que fabricam compostos de enxofre são obrigadas a pagar tributos aduaneiros nas fronteiras.",
        "Porque os tratados internacionais de meteorologia exigem que as nuvens artificiais tenham tonalidades exclusivamente azuladas.",
        "Porque os agricultores do hemisfério sul preferem utilizar fertilizantes orgânicos produzidos com esterco bovino seco.",
        "B",
        "**Etapa 1:** Aplicar a regra central da heurística do medo: dar maior peso ao prognóstico desfavorável quando a escala da tecnologia pode destruir a biosfera.\n**Etapa 2:** Concluir com a lucidez jonasiana: a geoengenharia solar pode alterar monções e gerar secas fatais para bilhões de seres humanos sem conserto posterior; a ética da responsabilidade exige atacar a raiz do problema (frear combustíveis fósseis) em vez de apostar a sobrevivência da Terra em roletas russas tecnológicas."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Ao examinar a relação entre a Ética da Alteridade e o Direito Internacional Humanitário, de que modo o filósofo Philippe Nemo, em seus diálogos com Lévinas (Ética e Infinito), destaca a ruptura promovida pelo mandamento 'Não matarás!' diante da razão de Estado militar?",
        "Sustentando que os batalhões de infantaria deveriam utilizar fardamentos confeccionados com tecidos de seda importada.",
        "Evidenciando que a razão de Estado historicamente subordina a vida humana a objetivos geopolíticos de soberania territorial e segurança nacional (autorizando o assassinato do inimigo em guerras), enquanto Lévinas afirma que o mandamento do Rosto é absoluto e anterior a qualquer soberania estatal, deslegitimando a matança em nome de bandeiras ou ideologias.",
        "Afirmando que os generais dos exércitos deveriam consultar os sacerdotes de ordens monásticas antes de aprovarem planos de marcha militar.",
        "Provando que as leis de navegação de rios internacionais foram redigidas por mercadores holandeses da Companhia das Índias Orientais.",
        "Defendendo que as armas de cerco mecânicas utilizadas na Idade Média eram superiores em precisão balística aos canhões de ferro fundido.",
        "B",
        "**Etapa 1:** Confrontar a razão de Estado (que relativiza a vida humana em nome do poder e da nação) com a ética levinasiana.\n**Etapa 2:** Concluir com a radicalidade de Lévinas: nenhum interesse nacional, estatal ou ideológico tem autoridade para suspender a santidade do Rosto; o mandamento de não matar está acima das ordens dos reis e generais, fundando a resistência ética contra o crime institucionalizado."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Considere o diálogo intelectual entre a tese da 'Banalidade do Mal' formulada por Hannah Arendt em Eichmann em Jerusalém e a ética do Rosto de Emmanuel Lévinas. Qual é o ponto de convergência fundamental entre esses dois pensadores judeus do pós-Segunda Guerra?",
        "Ambos os autores defendiam que os julgamentos de crimes contra a humanidade deveriam ocorrer na cidade de Genebra.",
        "Ambos diagnosticam que a monstruosidade do totalitarismo e do Holocausto não brotou de vilões demoníacos excepcionais, mas da incapacidade assustadora de indivíduos burocratizados de enxergarem o outro ser humano como pessoa de carne e osso, operando sob o torpor da totalidade administrativa que anula a escuta do Rosto da vítima.",
        "As duas perspectivas afirmam que as ordens dos superiores hierárquicos em tempos de guerra militar devem ser sempre obedecidas cegamente.",
        "Ambos sustentam que as pesquisas acadêmicas sobre crimes de guerra deveriam ser financiadas exclusivamente por companhias ferroviárias.",
        "Os dois autores propõem que as sentenças dos tribunais internacionais deveriam prever a leitura obrigatória de manuais de direito civil romano.",
        "B",
        "**Etapa 1:** Analisar a tese arendtiana da banalidade do mal: Eichmann não era um monstro shakespeariano, mas um burocrata incapaz de pensar a partir do ponto de vista do outro.\n**Etapa 2:** Conectar com a ética levinasiana: o mal banal triunfa quando o sujeito se refugia nas normas do sistema (o 'Mesmo') e recusa a epifania do Rosto; quando o olhar da vítima é reduzido a um número de ficha burocrática, a máquina do assassinato opera sem atrito moral."
    ))

    questoes_brutas.append((
        48, "EM13CHS501", "dificil",
        "Em O Princípio Responsabilidade, Hans Jonas formula uma crítica demolidora ao antropocentrismo cartesiano que concebia os animais e a natureza como meros 'autômatos mecânicos sem alma' (res extensa). Como a tese jonasiana de que a biosfera possui teleologia imanente e valor próprio transforma a ética ambiental contemporânea?",
        "Negando que os animais marinhos respirem por meio de brânquias banhadas por correntes de água salgada.",
        "Demonstrando que todo organismo vivo exibe uma luta afirmativa e contínua para manter a sua própria existência contra a entropia e a morte (o 'sim à vida' afirmativo da matéria orgânica), o que confere a todos os seres vivos um estatuto de dignidade existencial própria que nos obriga a reconhecer o dever moral de não destruir a teia planetária.",
        "Afirmando que os relógios mecânicos das catedrais foram construídos a partir de desenhos de anatomia de mamíferos marinhos.",
        "Sustentando que as pesquisas de laboratório sobre vacinas devem ser suspensas durante as estações chuvosas do ano civil.",
        "Provando que as florestas equatoriais produzem excesso de madeira vegetal que prejudica o desenvolvimento da agricultura comercial.",
        "B",
        "**Etapa 1:** Desconstruir o mecanicismo cartesiano: os animais e as florestas não são engrenagens mortas sem valor ético.\n**Etapa 2:** Concluir com a fundamentação de Jonas: a própria vida na Terra afirma a si mesma como valor contra o nada; essa teleologia imanente da natureza impõe ao ser humano o papel de guardião responsável da biosfera, e não de seu explorador tirânico e predatório."
    ))

    questoes_brutas.append((
        49, "EM13CHS502", "dificil",
        "Ao refletir sobre os dilemas éticos das catástrofes climáticas e humanitárias contemporâneas, como a síntese articulada entre a Ética da Alteridade de Lévinas e o Princípio Responsabilidade de Hans Jonas oferece uma bússola moral completa para a cidadania no século XXI?",
        "Afirmando que os estudantes de ensino médio devem memorizar os códigos fiscais que regulam a tributação do comércio internacional de tecidos.",
        "Oferecendo uma resposta em duas dimensões complementares e inseparáveis: Lévinas nos orienta a acolher com responsabilidade infinita e incondicional a dor do vulnerável no presente histórico (os excluídos, os refugiados e as vítimas imediatas da desigualdade), enquanto Hans Jonas nos orienta a conter a voracidade tecno-econômica para preservar as bases biológicas e ecológicas do futuro planetário, garantindo a dignidade de quem vive hoje e a possibilidade de existência para os que ainda vão nascer.",
        "Defendendo que as assembleias legislativas estaduais devem ser compostas exclusivamente por diplomados em cursos de engenharia química.",
        "Determinando que os bancos comerciais devam fechar suas agências durante todos os períodos de estiagem prolongada no interior.",
        "Comprovando que os tratados de diplomacia internacional perdem sua eficácia jurídica caso não sejam assinados em duas vias de papel de linho.",
        "B",
        "**Etapa 1:** Articular o eixo levinasiano da alteridade no presente: o cuidado direto e desinteressado com o Rosto do que sofre aqui e agora.\n**Etapa 2:** Integrar com o eixo jonasiano da responsabilidade no futuro: a tutela preventiva da biosfera para as próximas gerações; a síntese dos dois autores forja uma ética integral: solidariedade humana no presente e sustentabilidade ecológica para a posteridade."
    ))

    questoes_brutas.append((
        50, "EM13CHS503", "dificil",
        "Em Totalidade e Infinito, Lévinas afirma que 'a linguagem autêntica não é a transmissão mecânica de informações, mas o acolhimento do outro na hospitalidade da conversa'. Como essa tese critica a redução contemporânea da comunicação humana a algoritmos digitais e bolhas informacionais?",
        "Provando que as redes de transmissão de dados via cabos submarinos sofrem desgaste corrosivo pelo sal marinho.",
        "Evidenciando que a comunicação algorítmica das plataformas digitais foi desenhada para nos manter fechados no 'Mesmo' (interagindo apenas com perfis semelhantes e consumindo conteúdos confortáveis), eliminando o atrito salutar e transformador da epifania do Rosto concreto, que exige presença viva, escuta atenta da dor e acolhimento da diferença real.",
        "Afirmando que os aparelhos de telefonia celular consomem excesso de energia elétrica em estações de alta temperatura.",
        "Sustentando que os livros didáticos impressos devem ser substituídos exclusivamente por gravações em fitas magnéticas de áudio.",
        "Determinando que os provedores de acesso à internet devam proibir o uso de letras maiúsculas em mensagens de correio eletrônico.",
        "B",
        "**Etapa 1:** Analisar a dinâmica do algoritmo digital: ele cria bolhas identitárias fechadas que operam como a totalidade do Mesmo.\n**Etapa 2:** Concluir com a hospitalidade levinasiana: a conversa ética autêntica exige sair da bolha do ego e acolher o desconhecido; transformar o outro em avatar descartável na tela é a morte da comunicação e o triunfo da indiferença moral."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "No debate sobre o Estatuto dos Refugiados da ONU e as políticas migratórias de países europeus, como a tensão entre Soberania Territorial e a Ética do Rosto de Lévinas se manifesta nas crises de acolhimento em alto-mar?",
        "Levando os comandantes de navios de cruzeiro de turismo a cobrarem passagens mais baratas para passageiros idosos.",
        "Revelando o choque frontal entre a soberania jurídica estatal (que fecha portos, constrói cercas de arame e criminaliza o resgate de náufragos alegando proteção da ordem pública interna) e a exigência ética incondicional do Rosto (que demonstra que nenhuma lei burocrática tem o direito moral de deixar seres humanos inocentes afundarem nas águas marinhas).",
        "Determinando que os marinheiros de frotas pesqueiras devam utilizar coletes salva-vidas confeccionados com cortiça natural.",
        "Obrigando as embaixadas de nações desenvolvidas a realizarem exames médicos de audiometria em todos os diplomatas estrangeiros.",
        "Comprovando que os tratados de comércio marítimo celebrados no século XIX previam a isenção de tarifas sobre farinha de trigo.",
        "B",
        "**Etapa 1:** Descrever o argumento da soberania estatal: o Estado alega o direito de proteger suas fronteiras e filtrar quem entra.\n**Etapa 2:** Evidenciar a denúncia de Lévinas: a vida humana em perigo destrona a frieza burocrática das fronteiras; quando a polícia ou a guarda costeira nega socorro ao afogado, a totalidade do Estado comete assassinato institucionalizado contra o Rosto humano."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Ao examinar a tese do filósofo Hans Jonas sobre o perigo da 'Engenharia Biológica e da Clonagem Reprodutiva Humana', por que o autor sustenta que o direito de cada pessoa a uma 'identidade aberta e desconhecida' é uma condição essencial da liberdade ética?",
        "Porque as leis civis de registro de nascimento proíbem que pais escolham nomes compostos para seus filhos em cartórios municipais.",
        "Porque clonar ou programar geneticamente um ser humano para replicar talentos ou feições pré-determinadas pelos pais impõe àquela criança um destino previamente fixado por terceiros, violando o direito sagrado à incerteza da própria vida, à singularidade pessoal e à construção livre de sua própria história no mundo.",
        "Porque as clínicas médicas de fertilização utilizam refrigeradores que dependem de combustíveis fósseis para manterem temperaturas baixas.",
        "Porque os tratados internacionais de biologia celular exigem que os laboratórios sejam construídos em altitudes superiores a mil metros.",
        "Porque as pesquisas genéticas com animais de pequeno porte demonstraram que o pelo dos mamíferos clona-se em padrões geométricos rígidos.",
        "B",
        "**Etapa 1:** Compreender a crítica jonasiana à tirania eugênica: o desejo dos pais de fabricar geneticamente o filho perfeito à sua imagem e semelhança.\n**Etapa 2:** Concluir com o direito ético à incerteza: o ser humano tem o direito inalienável de ser o autor de seu próprio destino; transformar a prole em produto sob encomenda da tecnologia é escravizar a liberdade da nova geração aos caprichos egoístas do presente."
    ))

    questoes_brutas.append((
        53, "EM13CHS501", "dificil",
        "Em Ética e Infinito, Lévinas afirma: 'O Rosto do outro me interpela em sua indigência radical; diante dele, eu sou responsável por tudo e por todos, e eu mais do que todos os outros.' Qual é a fundamentação do autor para sustentar que a minha responsabilidade individual é única e não pode ser delegada ou transferida para o coletivo?",
        "A comprovação de que as firmas de auditoria contábil exigem a assinatura de um único contador nos relatórios fiscais anuais.",
        "A percepção de que, se eu esperar que o Estado, a sociedade ou o próximo assumam o cuidado do vulnerável para só então agir, eu me refugio na covardia da massa anônima; diante do sofrimento concreto que está perante os meus olhos, a responsabilidade é intransferível e ninguém pode me substituir no dever de acolher e socorrer.",
        "A regra de que os motoristas de caminhão de carga são os únicos responsáveis pela calibragem dos pneus dos veículos nas estradas.",
        "A determinação de que as receitas médicas emitidas em hospitais públicos devam conter carimbos com tinta vermelha indelével.",
        "A premissa de que os tratados de diplomacia internacional perdem o vigor quando um dos diplomatas signatários entra em aposentadoria civil.",
        "B",
        "**Etapa 1:** Analisar a tentação da desresponsabilização social: a desculpa confortável de que 'alguém ou o governo cuidará disso'.\n**Etapa 2:** Concluir com a radicalidade ética de Lévinas: a ética não é tarefa de comitês burocráticos anônimos; diante do Rosto ferido, eu sou pessoal e insubstituivelmente chamado a responder; transferir a culpa para a coletividade é a forma clássica de covardia moral."
    ))

    questoes_brutas.append((
        54, "EM13CHS502", "dificil",
        "De acordo com a teoria de Hans Jonas, de que maneira a crescente dependência civilizatória em relação a sistemas de Inteligência Artificial e automação de decisões críticas (como finanças globais, diagnósticos clínicos e defesa militar) configura uma 'abdicação da responsabilidade humana'?",
        "Obrigando os operadores de computadores eletrônicos a realizarem cursos de datilografia em máquinas mecânicas do século passado.",
        "Evidenciando que, ao delegar a algoritmos fechados e opacos o julgamento sobre a vida, a liberdade e o destino coletivo, a sociedade moderna transfere o poder decisório para dispositivos que não possuem consciência moral, capacidade empática nem responsabilidade penal, dissolvendo o dever humano de responder perante as futuras gerações pelos rumos da história.",
        "Afirmando que os servidores de bancos de dados consomem muita água potável para o resfriamento de circuitos eletrônicos na capital.",
        "Sustentando que as empresas de tecnologia digital deveriam proibir o uso de monitores de vídeo coloridos em ambientes corporativos.",
        "Provando que as leis de compensação trabalhista deixam de ter eficácia quando os trabalhadores utilizam softwares de planilha eletrônica.",
        "B",
        "**Etapa 1:** Mapear o perigo da delegação tecnocrática: esconder-se atrás da decisão algorítmica para evitar o peso do julgamento moral.\n**Etapa 2:** Concluir com a lucidez jonasiana: a máquina não tem culpa, não sofre e não projeta o amanhã; quando o ser humano abre mão de deliberar eticamente sobre o futuro e terceiriza suas escolhas para o cálculo automático, ele assina o atestado de falência da própria dignidade humana."
    ))

    questoes_brutas.append((
        55, "EM13CHS503", "dificil",
        "No campo da Filosofia Social e da Crítica Cultural contemporânea, como a ética levinasiana da alteridade desmonta a cultura do 'Cancelamento Digital' que vigia e pune desvios de conduta nas redes virtuais?",
        "Comprovando que as plataformas digitais utilizam satélites de telecomunicação que orbitam a baixa altitude da atmosfera terrestre.",
        "Demonstrando que os linchamentos virtuais operam como tribunais implacáveis da totalidade do 'Mesmo', onde o sujeito que errou é reduzido sumariamente a um monstro descartável e desprovido de Rosto, negando-se-lhe a escuta, a vulnerabilidade do diálogo e a possibilidade real de redenção humana e reconciliação comunitária.",
        "Afirmando que os computadores portáteis perdem a velocidade de processamento quando conectados a redes públicas sem fio em aeroportos.",
        "Determinando que os bancos comerciais devam bloquear as contas financeiras de usuários que publicam comentários agressivos em blogs.",
        "Defendendo que as regras de etiqueta social deveriam ser ensinadas em aulas de caligrafia manual em colégios públicos do interior.",
        "B",
        "**Etapa 1:** Interpretar o mecanismo psicológico e ético do cancelamento: o tribunal sumário que rotula e desumaniza sem olhar nos olhos.\n**Etapa 2:** Concluir com a exigência de Lévinas: a verdadeira ética não é apedrejar o outro a partir do púlpito da própria pureza fingida; o Rosto do que errou continua sendo um apelo de alteridade que exige conversa, responsabilidade e restauração da humanidade ferida."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Analise a seguinte formulação de Hans Jonas a respeito da fragilidade biológica da Terra: 'A vulnerabilidade da natureza submetida à intervenção tecnológica do homem desvela uma responsabilidade que não buscamos, mas que não podemos recusar: a natureza tornou-se nossa pupila sob custódia.' Qual é o significado ético dessa metáfora da tutela da natureza?",
        "A exigência de que os proprietários rurais registrem seus animais de pasto em livros de cartórios de títulos civis municipais.",
        "A demonstração de que o ser humano não é o dono tirânico autorizado a saquear o mundo conforme seus desejos, mas o tutor legal e moral responsável por cuidar, proteger e prestar contas do bem-estar de um ser vulnerável (a Terra) que não possui defesas suficientes contra o poderio descomunal de nossa técnica.",
        "A determinação de que as florestas de pinheiros sejam cercadas com arames farpados para evitar a circulação de operários de ferrovias.",
        "A afirmação de que os tratados de comércio naval devam prever o transporte obrigatório de sementes nativas em porões de carga.",
        "A certeza de que as pesquisas sobre fertilizantes sintéticos devem ser supervisionadas por juízes de varas de família da capital.",
        "B",
        "**Etapa 1:** Interpretar a metáfora jurídica e moral da tutela: a pupila é a criança órfã que depende integralmente da probidade de seu guardião.\n**Etapa 2:** Concluir com o papel ético da humanidade: antes a Terra era a mãe que nos abrigava e parecia indestrutível; hoje nós temos a força de matá-la; por isso ela é nossa pupila sob custódia, e qualquer negligência egoísta de nossa parte torna-se um crime hediondo contra a vida."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Em Totalidade e Infinito, Emmanuel Lévinas formula a distinção entre a 'Necessidade' e o 'Desejo Metafísico'. Como essa distinção conceitual fundamenta a primazia da ética sobre o egoísmo biológico natural?",
        "Afirmando que as necessidades calóricas diárias dos seres humanos dependem da quantidade de carne consumida nas refeições.",
        "Mostrando que a 'necessidade' é centrada no ego e busca preencher uma carência para retornar a si mesmo (como a fome que come o pão para se satisfazer), enquanto o 'desejo metafísico' autêntico não quer preencher vazios egoístas, mas transborda em direção ao Outro sem esperar retorno, consagrando-se na generosidade incondicional do cuidado.",
        "Provando que as academias científicas da Europa central realizavam medições precisas do volume de água em cisternas urbanas.",
        "Defendendo que as leis comerciais devem proibir a venda de produtos manufaturados a cidadãos que não tenham emprego formal.",
        "Determinando que os viajantes que cruzam fronteiras territoriais devam apresentar declarações de bens lavradas em papel timbrado.",
        "B",
        "**Etapa 1:** Contrastar a dinâmica da necessidade (centrípeta, que devora o mundo para alimentar o eu) com o desejo metafísico (centrífugo, que vai ao outro).\n**Etapa 2:** Concluir com a fundação da ética: a moralidade não é um instinto animal de sobrevivência; ela é a capacidade sublime e sublime do espírito humano de transcender suas próprias necessidades para se doar generosamente ao acolhimento do vulnerável."
    ))

    questoes_brutas.append((
        58, "EM13CHS501", "dificil",
        "Ao examinar a relação entre o Princípio Responsabilidade e a Democracia Contemporânea, por que Hans Jonas adverte que as instituições parlamentares ocidentais enfrentam uma 'limitação estrutural congênita' para lidar com a crise ecológica de longo alcance?",
        "Porque os membros do parlamento utilizam cadeiras de madeira de carvalho que sofrem desgaste em ambientes climatizados.",
        "Porque os governos e parlamentares em democracias representativas são reféns do ciclo eleitoral de curto prazo (eleições a cada quatro ou cinco anos), tendendo a aprovar medidas que agradam o eleitorado presente imediato e adiando os sacrifícios ecológicos exigidos para proteger as gerações futuras que não votam nem financiam campanhas.",
        "Porque as sessões plenárias de assembleias legislativas devem ser transmitidas em frequências de rádio de alcance restrito.",
        "Porque as constituições democráticas exigem que todos os projetos de lei sejam lidos na íntegra por funcionários públicos concursados.",
        "Porque os partidos políticos de centro recusam a filiação de cidadãos que trabalham em cooperativas agrícolas de agricultura familiar.",
        "B",
        "**Etapa 1:** Diagnosticar o vício do curto prazo na política democrática de massas: o governante pensa nas próximas eleições, não nos próximos séculos.\n**Etapa 2:** Evidenciar o desafio de Jonas: como as futuras gerações não têm voto nem representação partidária hoje, a política tradicional empurra o colapso com a barriga; Jonas adverte que a sobrevivência da Terra exige órgãos constitucionais de tutela de longo alcance imunes às pressões populistas imediatas."
    ))

    questoes_brutas.append((
        59, "EM13CHS502", "dificil",
        "De que modo a constatação de Primo Levi em É Isto um Homem? — sobre a desumanização deliberada dos prisioneiros em Auschwitz — dialoga de modo trágico com a filosofia do Rosto de Emmanuel Lévinas?",
        "Mostrando que os uniformes distribuídos aos internos nos campos de concentração eram confeccionados com tecidos de algodão grosso.",
        "Evidenciando que o primeiro passo metódico dos carrascos nazistas para viabilizar o genocídio industrial consistiu em raspar os cabelos, tatuar números nos braços e apagar sistematicamente todas as expressões singulares de humanidade dos prisioneiros, pois sabiam que, uma vez ocultado ou destruído o 'Rosto', a barreira moral do 'Não matarás!' deixa de atuar na consciência do algoz.",
        "Afirmando que os médicos que prestavam serviços nos campos de triagem utilizavam termômetros de vidro confeccionados na cidade de Berlim.",
        "Provando que as cercas eletrificadas consumiam muita energia gerada por usinas termoelétricas alimentadas com carvão betuminoso.",
        "Determinando que os arquivos administrativos de campos de prisioneiros militares devam ser encadernados em couro bovino legítimo.",
        "B",
        "**Etapa 1:** Conectar o testemunho histórico de Primo Levi com a categoria fenomenológica de Lévinas: a mútua elucidação do horror.\n**Etapa 2:** Concluir com a anatomia da barbárie: para assassinar milhões sem remorso, os nazistas precisaram assassinar o Rosto antes do corpo; ao transformar o ser humano em coisa inominada (número), a totalidade assassina calou o apelo ético da vulnerabilidade; a filosofia de Lévinas ergue-se para impedir que o homem esqueça essa lição sangrenta."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "Síntese conclusiva: por que a Ética da Alteridade de Emmanuel Lévinas e o Princípio Responsabilidade de Hans Jonas constituem o alicerce filosófico indispensável para a superação das crises civilizatórias que ameaçam o século XXI?",
        "Porque essas teorias simplificam a redação de contratos comerciais internacionais de exportação de soja e milho híbrido.",
        "Porque elas respondem simultaneamente às duas maiores urgências da existência contemporânea: a exigência moral inegociável de acolher, cuidar e respeitar a dignidade sagrada e infinita de todo ser humano vulnerável no presente histórico (Lévinas) e o imperativo ecológico e existencial inadiável de frear a onipotência cega da técnica para garantir que a biosfera planetária continue a abrigar a vida das futuras gerações sobre a Terra (Hans Jonas).",
        "Porque elas determinam que todas as escolas de ensino médio devam substituir o estudo de história pelo aprendizado de idiomas clássicos.",
        "Porque elas comprovam que as leis da termodinâmica mecânica deixam de funcionar quando os astrônomos fecham seus telescópios de observação.",
        "Porque elas estabelecem que os governos republicanos devam transferir o comando das polícias municipais para comitês de vizinhança voluntária.",
        "B",
        "**Etapa 1:** Sintetizar o aporte de Lévinas: a ética do acolhimento radical do vulnerável contra o totalitarismo, a xenofobia e a indiferença social no presente.\n**Etapa 2:** Sintetizar o aporte de Jonas: a responsabilidade intergeracional e a precaução ecológica contra a autodestruição tecnológica no futuro; juntas, essas filosofias fundam o humanismo contemporâneo: cuidar do irmão hoje e salvar a Terra para amanhã."
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
    linhas.append('capitulo: "Capítulo 15: Ética da Alteridade e Responsabilidade: Lévinas e Hans Jonas"')
    linhas.append('objeto_de_conhecimento: "A ética da alteridade em Emmanuel Lévinas, a epifania do Rosto, a crítica à totalidade ontológica, o Princípio Responsabilidade em Hans Jonas e a ética para a civilização tecnológica"')
    linhas.append('ebook_fonte: "em-fil-c15-etica-alteridade-levinas-responsabilidade-jonas.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS501"')
    linhas.append('  - "EM13CHS502"')
    linhas.append('  - "EM13CHS503"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: Ética da Alteridade e Responsabilidade: Lévinas e Hans Jonas\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-15-etica-alteridade-levinas-responsabilidade-jonas -->"
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
    linhas.append("- LÉVINAS, Emmanuel. *Totalidade e infinito: ensaio sobre a exterioridade*. Tradução de José Pinto Ribeiro. Lisboa: Edições 70, 2008.")
    linhas.append("- LÉVINAS, Emmanuel. *Ética e infinito: diálogos com Philippe Nemo*. Tradução de João Gama. Lisboa: Edições 70, 2007.")
    linhas.append("- JONAS, Hans. *O princípio responsabilidade: ensaio de uma ética para a civilização tecnológica*. Tradução de Marijane Lisboa e Luiz Barros Montez. Rio de Janeiro: Contraponto/Editora PUC-Rio, 2006.")
    linhas.append("- PELIZZOLI, Marcelo L. *A relação ao outro em Lévinas: uma introdução*. Porto Alegre: EDIPUCRS, 2002.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Salvar em temp_draft.md
    with open("temp_draft.md", "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em temp_draft.md ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador Educamob
    destino_final = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-15-etica-alteridade-levinas-responsabilidade-jonas/ebooks/em-fil-c15-etica-alteridade-levinas-responsabilidade-jonas-exercicios.md"
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
        print("\n[SUCESSO TOTAL] Cap 15 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {resultado.returncode}")
        sys.exit(resultado.returncode)

if __name__ == "__main__":
    main()
