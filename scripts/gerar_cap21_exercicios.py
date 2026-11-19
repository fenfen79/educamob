# -*- coding: utf-8 -*-
"""
Gerador das 60 questões atômicas de Filosofia EM - Capítulo 21:
Poder, Disciplina e Biopolítica: Foucault e Agamben
Destino: content/medio/volume-unico/filosofia/eixo-3-politica/cap-21-poder-disciplina-biopolitica-foucault-agamben/ebooks/em-fil-c21-poder-disciplina-biopolitica-foucault-agamben-exercicios.md
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
        "Em contraposição ao modelo jurídico tradicional da soberania, qual é a tese inovadora formulada por Michel Foucault sobre a natureza do poder?",
        "O poder é uma propriedade material que os governantes guardam em cofres de ferro fundido.",
        "O poder não se possui como um título fixo de propriedade, exercendo-se como uma rede de relações móveis, tensas e capilares que atravessa todo o tecido da sociedade.",
        "O poder político reside unicamente no topo de fortificações militares erguidas em zonas de fronteira.",
        "O poder civil pertence com exclusividade a conselhos de monges e teólogos de ordens medievais.",
        "O poder estatal deve ser extinto para dar lugar a disputas oratórias semanais em anfiteatros.",
        "B",
        "Foucault supera a visão tradicional: o poder não é algo estático que um rei possui e os súditos não possuem; o poder é um exercício relacional presente em todas as instâncias da vida social."
    ))

    questoes_brutas.append((
        2, "EM13CHS601", "basico",
        "Por que Michel Foucault afirma que o poder nas sociedades modernas é 'Produtivo' e não meramente repressivo?",
        "Porque os governantes realizam doações de ferramentas agrícolas no início do calendário de plantio.",
        "Porque, se o poder apenas proibisse e punisse, seria frágil e derrubado; sua eficácia reside no fato de produzir saberes, induzir prazeres, moldar corpos e fabricar discursos de verdade.",
        "Porque as assembleias cívicas são obrigadas por decretos a aprovar investimentos em manufaturas têxteis.",
        "Porque a legislação tributária concede isenções fiscais a navegadores mercantes em portos litorâneos.",
        "Porque os tribunais civis realizam julgamentos através da leitura de poemas líricos rimados.",
        "B",
        "O poder moderno é eficiente porque atua de forma positiva: ele não apenas impede ações, mas cria identidades, estabelece normas do que é correto e educa os indivíduos para desejarem obedecer."
    ))

    questoes_brutas.append((
        3, "EM13CHS102", "basico",
        "Como Foucault caracteriza o exercício tradicional do 'Poder Soberano' próprio do Antigo Regime monárquico absolutista?",
        "Um modelo participativo no qual os camponeses decidiam as leis municipais em praças públicas.",
        "O poder fundado no direito arcaico de espada, sintetizado na célebre fórmula de 'fazer morrer e deixar viver' por meio de confiscos, tributos e suplícios públicos exemplares.",
        "Uma administração pacífica que dispensava a existência de forças policiais ou guarnições armadas.",
        "Um governo burocrático gerido exclusivamente por comissões de mercadores estrangeiros de seda.",
        "Uma confederação de cidades que resolvia conflitos territoriais mediante jogos olímpicos desportivos.",
        "B",
        "No absolutismo clássico, a soberania mostrava sua força punindo com a morte violenta quem desafiasse a lei do monarca; fora das cobranças e da punição, a vida cotidiana do súdito era pouco vigiada."
    ))

    questoes_brutas.append((
        4, "EM13CHS602", "basico",
        "Qual era a função política e simbólica do 'Suplício Público' executado nas praças das cidades no Antigo Regime?",
        "Entreter a população durante as tardes de feriados religiosos municipais.",
        "Restabelecer visualmente perante a multidão a majestade e a força física ferida do soberano através do esquartejamento e da destruição do corpo do criminoso.",
        "Testar a resistência física de condenados para recrutá-los para forças de cavalaria pesada.",
        "Garantir a cobrança pontual de taxas aduaneiras sobre a circulação de carnes defumadas.",
        "Distribuir esmolas públicas para os familiares de réus que confessassem delitos fiscais.",
        "B",
        "O suplício não era apenas vingança crua; era um espetáculo de poder: quem quebrava a lei feria o corpo do rei, e a destruição pública do corpo do réu reafirmava a autoridade absoluta da coroa."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "A partir da virada dos séculos XVIII e XIX, qual nova tecnologia política emergiu para disciplinar o corpo individual na modernidade?",
        "A teocracia pontifícia baseada em julgamentos inquisitoriais monásticos.",
        "O Poder Disciplinar (ou Anatomopolítica), que incide sobre o corpo individual para adestrá-lo, tornando-o dócil politicamente e útil economicamente.",
        "A anarquia agrária comunitária sem divisão social de funções fabris.",
        "O absolutismo imperial que transferiu o comando de quartéis para corporações de artesãos.",
        "O feudalismo militar que exigia juramentos de vassalagem em fortalezas de pedra.",
        "B",
        "A disciplina substituiu o machado do carrasco pelo adestramento contínuo: o objetivo não é mais destruir o corpo do infrator, mas torná-lo um trabalhador dócil e eficiente para a indústria."
    ))

    questoes_brutas.append((
        6, "EM13CHS601", "basico",
        "Quais instituições modernas partilham da mesma matriz disciplinar de confinamento e vigilância analisada em Vigiar e Punir?",
        "As companhias de teatro mambembe e as feiras itinerantes de tecidos.",
        "A prisão, a escola, a fábrica, o quartel militar, o hospital psiquiátrico e o asilo.",
        "Os clubes de tiro com arco e os ateliês de pintura renascentista.",
        "As ordens religiosas mendicantes e os conventos contemplativos rurais.",
        "Os consulados marítimos e as companhias de caravelas transatlânticas.",
        "B",
        "Foucault aponta o parentesco estrutural entre essas instituições: todas utilizam o confinamento, o isolamento dos corpos em filas ou celas e a vigilância contínua para fabricar indivíduos disciplinados."
    ))

    questoes_brutas.append((
        7, "EM13CHS102", "basico",
        "De que modo a disciplina moderna opera o adestramento dos corpos através do esquadrinhamento minucioso do tempo?",
        "Suspendendo os calendários de trabalho durante os períodos de festividades carnavalescas.",
        "Fragmentando o tempo em horários milimétricos, toques de sirene, controle de pausas e repetição padronizada de gestos mecânicos corporais.",
        "Permitindo que os operários definam livremente o início e o término de suas tarefas diárias.",
        "Adotando relógios de areia individuais para regular os debates em assembleias de bairro.",
        "Cancelando as atividades escolares sempre que ocorrerem tempestades marítimas costeiras.",
        "B",
        "O tempo da disciplina é decomposto até os segundos: da fila da escola à esteira da fábrica, cada movimento corporal é cronometrado para evitar distrações e maximizar a produtividade."
    ))

    questoes_brutas.append((
        8, "EM13CHS602", "basico",
        "O que foi o projeto arquitetônico do 'Panóptico' concebido pelo filósofo utilitarista britânico Jeremy Bentham em 1791?",
        "Um monumento público em mármore construído em praças para comemorar vitórias militares.",
        "Um edifício circular com celas na periferia e uma torre de vigia no centro, permitindo a um único observador inspecionar todos os indivíduos confinados sem ser visto.",
        "Um observatório astronômico para o mapeamento de constelações visíveis no hemisfério norte.",
        "Um terminal portuário destinado ao desembarque exclusivo de cargas de algodão egípcio.",
        "Um teatro de arena projetado para a encenação de peças cômicas clássicas ao ar livre.",
        "B",
        "O Panóptico de Bentham é o modelo arquitetônico da disciplina: celas iluminadas na periferia e uma torre central escura, permitindo enxergar tudo sem que ninguém saiba se o guarda está na torre."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Qual é o efeito psicológico e político mais refinado proporcionado pelo dispositivo do Panóptico nos indivíduos vigiados?",
        "Estimular a rebelião armada coletiva dos prisioneiros contra a administração da torre.",
        "Induzir no indivíduo a consciência de visibilidade permanente, fazendo com que ele assuma que é vigiado a todo instante e passe a policiar a si mesmo, automatizando o poder.",
        "Provocar sonolência contínua que dispensa o uso de trancas nas portas das celas periféricas.",
        "Incentivar o cultivo de amizades solidárias e laços comunitários entre os presos confinantes.",
        "Obrigar os detentos a memorizarem versos rimados de peças teatrais renascentistas.",
        "B",
        "A grande eficácia do panóptico é tornar o poder automático: como o vigiado nunca sabe se está sendo olhado naquele segundo, ele passa a se comportar como se estivesse sob olhar constante, vigiando a si mesmo."
    ))

    questoes_brutas.append((
        10, "EM13CHS603", "basico",
        "Como a escala do poder se transformou no final do século XVIII com o nascimento da chamada 'Biopolítica'?",
        "O poder deixou de utilizar forças policiais e passou a contratar navegadores mercantes particulares.",
        "O foco do poder deslocou-se do corpo individual anatômico para o corpo-espécie, isto é, para a gestão da População como um conjunto biológico vivo.",
        "As leis penais municipais foram substituídas por costumes tradicionais transmitidos oralmente.",
        "Os governantes civis foram depostos e substituídos por conselhos de sacerdotes eremitas.",
        "A administração financeira de cidades passou a ser controlada por corporações de agrimensores.",
        "B",
        "Ao lado da disciplina individual (escola, fábrica), nasce a biopolítica: o Estado passa a controlar a população como um todo biológico, monitorando nascimentos, mortes, doenças e vacinação."
    ))

    questoes_brutas.append((
        11, "EM13CHS102", "basico",
        "Qual é a fórmula lapidar que sintetiza a lógica de ação do Biopoder no mundo contemporâneo?",
        "Garantir a glória eterna dos soberanos e impor tributos de vassalagem ao povo.",
        "Fazer viver e deixar morrer (intervir para maximizar e proteger a vida biológica da população, abandonando à margem o que não interessa ao sistema).",
        "Submeter todas as disputas comerciais a torneios de esgrima naval entre comandantes.",
        "Proibir a circulação de moedas de prata em favor da troca direta de especiarias agrícolas.",
        "Obrigar todos os cidadãos a realizarem exercícios matinais de corrida em praias públicas.",
        "B",
        "Invertendo a fórmula soberana de 'fazer morrer e deixar viver', o biopoder cuida da vida (saúde, natalidade, longevidade), deixando morrer ou descartando quem é considerado indesejável."
    ))

    questoes_brutas.append((
        12, "EM13CHS601", "basico",
        "Quais fenômenos biológicos e sociais tornaram-se alvos centrais de regulação pelas políticas biopolíticas estatais?",
        "A cor das telhas utilizadas na construção de residências em cidades litorâneas.",
        "As taxas de natalidade e fertilidade, a longevidade média, a contenção de epidemias, o saneamento básico e as políticas de vacinação em massa.",
        "A quantidade de livros didáticos guardados nas estantes de mosteiros benedictinos.",
        "Os tipos de tecidos utilizados na confecção de fardamentos para soldados de cavalaria.",
        "Os protocolos de recepção consular dispensados a embaixadores de reinos estrangeiros.",
        "B",
        "A biopolítica é a gestão médica e estatística da vida: o Estado atua vacinando, construindo redes de esgoto, controlando natalidade e combatendo vírus para manter a população produtiva."
    ))

    questoes_brutas.append((
        13, "EM13CHS602", "basico",
        "Como Michel Foucault explica a função política do 'Racismo de Estado' no interior de uma sociedade regida pelo biopoder?",
        "Como um sentimento individual de antipatia psicológica entre cidadãos de etnias distintas.",
        "Como uma tecnologia estatal de corte biológico que divide a população entre a raça considerada sadia (que deve viver) e as consideradas degeneradas ou anormais (cuja eliminação é justificada como ato higiênico).",
        "Como uma regra jurídica que regulamenta a importação de especiarias do continente asiático.",
        "Como uma doutrina eclesiástica adotada para orientar a ordenação de novos padres paroquiais.",
        "Como uma convenção diplomática firmada para padronizar os uniformes de exércitos europeus.",
        "B",
        "Na biopolítica, matar não é mais por honra do rei, mas por 'higiene da raça': o racismo de Estado rotula o outro como uma ameaça biológica degenerada para justificar o massacre em nome da saúde da população."
    ))

    questoes_brutas.append((
        14, "EM13CHS101", "basico",
        "Qual distinção conceitual e existencial fundamental entre 'Zoé' e 'Bíos' no grego clássico é recuperada pelo filósofo Giorgio Agamben?",
        "Zoé é o estudo de animais marinhos e Bíos é a botânica de plantas terrestres cultivadas.",
        "Zoé é o simples fato biológico de viver (vida crua comum a animais e plantas); Bíos é a vida politicamente qualificada, ética e civil vivida pelo cidadão na pólis.",
        "Zoé é a poesia trágica encenada em teatros e Bíos é a retórica discursiva na assembleia popular.",
        "Zoé é a moeda de cobre do comércio varejista e Bíos é o lingote de prata do tesouro real.",
        "Zoé é a navegação fluvial em botes a remo e Bíos é a viagem oceânica em caravelas mercantes.",
        "B",
        "Agamben resgata os gregos: zoé era a vida nua animal no lar (oikos); bíos era a existência cidadã com direitos e voz política na cidade (pólis); a política moderna capturou a zoé para controlá-la."
    ))

    questoes_brutas.append((
        15, "EM13CHS102", "basico",
        "O que Giorgio Agamben define pelo conceito de 'Vida Nua' (*Nuda Vita*) em sua obra Homo Sacer?",
        "O hábito de populações ancestrais que viviam descalças em praias fluviais durante o verão.",
        "A condição humana rebaixada à mera existência biológica despida de qualquer estatuto jurídico, de proteção civil ou de direitos políticos perante a autoridade soberana.",
        "A prática de esportistas gregos que competiam em corridas despidos de vestimentas na arena.",
        "O rito religioso de penitência adotado por monges eremitas em desertos montanhosos.",
        "A obrigação legal de recém-nascidos serem pesados em balanças de cobre municipais.",
        "B",
        "A vida nua é o ser humano despido da cidadania: um corpo biológico biopoliticamente vigiado e desamparado pelo direito, que pode ser descartado ou violentado sem que a lei o proteja."
    ))

    questoes_brutas.append((
        16, "EM13CHS601", "basico",
        "Qual é a singularidade jurídica paradoxal que caracterizava a figura romana arcaica do 'Homo Sacer' investigada por Agamben?",
        "Ele era um magistrado supremo que acumulava as funções de sacerdote e general de legião.",
        "Ele era um sujeito banido que podia ser morto por qualquer pessoa sem que isso constituísse homicídio, mas cuja vida era insacrificável aos deuses em rituais sagrados.",
        "Ele recebia uma pensão vitalícia do Senado romano para compor versos de epopeias mitológicas.",
        "Ele era um comerciante de trigo isento do pagamento de tarifas alfandegárias portuárias.",
        "Ele tinha o direito exclusivo de acender as tochas do templo de Vesta na capital imperial.",
        "B",
        "O Homo Sacer habitava o vazio da lei: excluído da lei humana (quem o mata não comete crime) e excluído da religião (não serve nem para sacrifício aos deuses); ele é a vida nua que se pode matar impunemente."
    ))

    questoes_brutas.append((
        17, "EM13CHS602", "basico",
        "Como o jurista alemão Carl Schmitt definiu a Soberania política no início do século XX, tese retomada criticamente por Giorgio Agamben?",
        "Soberano é o povo que comparece bienalmente às urnas para eleger deputados parlamentares.",
        "Soberano é aquele que decide sobre o Estado de Exceção (aquele que tem o poder de suspender a própria lei para salvar a ordem).",
        "Soberano é o comandante militar que conquista novas províncias territoriais em alto-mar.",
        "Soberano é o tribunal arbitral que calcula as taxas de juros cobradas por bancos mercantis.",
        "Soberano é o monarca hereditário que comprova descendência de reis da dinastia merovíngia.",
        "B",
        "Para Schmitt e Agamben, a prova suprema da soberania não é fazer leis normais no parlamento, mas ter a autoridade de suspender a vigência das leis e direitos civis ao decretar a exceção."
    ))

    questoes_brutas.append((
        18, "EM13CHS603", "basico",
        "O que Agamben denuncia como o grande perigo institucional das democracias ocidentais no início do século XXI?",
        "O encarecimento das taxas cobradas pelos correios para o envio de cartas físicas.",
        "A transformação do Estado de Exceção de uma medida emergencial e temporária em uma técnica contínua e normalizada de governo sob pretextos de segurança e crises.",
        "A proibição parlamentar da transmissão radiofônica de sessões de julgamento criminal.",
        "O crescimento do número de diplomados em cursos universitários de filologia clássica.",
        "A redução orçamentária dos investimentos públicos na preservação de manuscritos antigos.",
        "B",
        "A exceção virou regra: governos democráticos usam decretos emergenciais, leis de segurança nacional e vigilância para suspender garantias individuais de modo rotineiro, enfraquecendo a democracia."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Qual espaço histórico e espacial é apontado por Giorgio Agamben como a verdadeira 'Matriz Biopolítica Oculta da Modernidade'?",
        "O anfiteatro grego clássico onde se encenavam tragédias de Sófocles em Atenas.",
        "O Campo de Concentração, local onde o estado de exceção se torna permanente e os seres humanos são despidos de todo direito e reduzidos a pura vida nua.",
        "A praça do mercado renascentista onde se trocavam moedas de prata por especiarias orientais.",
        "A biblioteca monástica medieval onde monges copistas traduziam pergaminhos em latim.",
        "O salão diplomático absolutista onde se assinavam tratados de aliança militar europeia.",
        "B",
        "Agamben sustenta que o paradigma da modernidade não é a pólis grega nem o parlamento, mas o campo de concentração: o espaço de anomia onde a lei é suspensa e a vida humana é gerida como pura matéria biológica."
    ))

    questoes_brutas.append((
        20, "EM13CHS102", "basico",
        "Como a categoria foucaultiana de 'Governamentalidade' sintetiza a gestão moderna das condutas humanas?",
        "Como a imposição violenta de decretos monárquicos através de patrulhas armadas de infantaria.",
        "Como o conjunto de instituições, cálculos, procedimentos e táticas que permitem exercer o governo sobre a população, operando a condução sutil das condutas através da economia política e da segurança.",
        "Como a terceirização de julgamentos penais municipais para companhias privadas de caravelas.",
        "Como a supressão definitiva de qualquer forma de tributação sobre mercadorias de consumo.",
        "Como o protocolo diplomático que regula o casamento de filhos primogênitos de reis europeus.",
        "B",
        "Governamentalidade é a 'arte de conduzir condutas': o Estado não precisa usar a chibata o tempo todo; ele governa gerindo a economia, a saúde, os fluxos urbanos e os hábitos cotidianos da sociedade."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Em seu célebre ensaio Post-scriptum sobre as Sociedades de Controle (1990), como Gilles Deleuze atualiza o diagnóstico do poder disciplinar de Michel Foucault?",
        "Afirmando que a humanidade retornará à servidão feudal medieval em feudos agrários isolados.",
        "Demonstrando que as instituições de confinamento fechado (fábrica, escola, prisão) estão em crise e sendo substituídas por mecanismos de controle contínuo a céu aberto em tempo real, viabilizados por cartões magnéticos, senhas, algoritmos e conectividade ininterrupta.",
        "Defendendo que as indústrias fabris devam substituir computadores por teares mecânicos a vapor.",
        "Comprovando que as decisões penais devem ser lavradas em folhas de linho cru por magistrados reais.",
        "Exigindo que os servidores públicos trabalhem exclusivamente durante a luz solar natural.",
        "B",
        "Deleuze viu a mutação: não precisamos mais estar trancados na fábrica ou na escola; a sociedade de controle nos monitora 24 horas por dia através do celular, do e-mail, dos dados digitais e dos cartões."
    ))

    questoes_brutas.append((
        22, "EM13CHS601", "intermediario",
        "De que modo a implementação de sistemas de reconhecimento facial com inteligência artificial nas ruas contemporâneas materializa o dispositivo do Panóptico?",
        "Substituindo os tribunais de justiça penal por assembleias comunitárias de moradores de bairro.",
        "Estabelecendo uma vigilância invisível, algorítmica e pervasiva sobre os transeuntes, induzindo a autocensura e a disciplina comportamental pela incerteza permanente de se estar sendo monitorado e escaneado por bancos de dados policiais.",
        "Obrigando os cidadãos que circulam pelo centro urbano a utilizarem máscaras de gesso branco.",
        "Garantindo que todos os passageiros de metrôs recebam passagens gratuitas custeadas por impostos.",
        "Eliminando a necessidade de códigos de trânsito em avenidas e rodovias metropolitanas.",
        "B",
        "O panóptico digital contemporâneo: as câmeras no poste são a nova torre de Bentham; mesmo sem saber se um policial está olhando nossa tela, mudamos nosso comportamento porque o olhar algorítmico pode estar ativo."
    ))

    questoes_brutas.append((
        23, "EM13CHS602", "intermediario",
        "Como a gestão das fronteiras e a criação da prisão de Guantánamo pelos Estados Unidos após o 11 de setembro exemplificam a produção do Homo Sacer agambeniano?",
        "Garantindo a todos os detentos o pleno acesso a advogados civis e julgamentos com júri popular.",
        "Criando a figura jurídica fictícia de 'combatentes inimigos ilegais' para afastar garantias constitucionais e as Convenções de Genebra, submetendo os presos à tortura e à anomia da vida nua desamparada.",
        "Transferindo a jurisdição do território para tribunais comerciais internacionais de navegação marítima.",
        "Concedendo cidadania norte-americana automática a todos os prisioneiros capturados no Oriente Médio.",
        "Exigindo que os oficiais militares prestem juramentos de lealdade perante autoridades religiosas locais.",
        "B",
        "Guantánamo é o campo do nosso tempo: indivíduos mantidos por décadas sem processo, sem direitos civis e sem Convenção de Genebra; a vida nua que o poder pode torturar e descartar sem punição legal."
    ))

    questoes_brutas.append((
        24, "EM13CHS102", "intermediario",
        "Por que as medidas sanitárias de emergência adotadas durante a pandemia de COVID-19 suscitaram debates filosóficos acalorados em torno da biopolítica e do estado de exceção?",
        "Porque as vacinas biológicas foram formuladas com compostos químicos extraídos de rochas marinhas.",
        "Porque a decretação de confinamentos residenciais forçados, passaportes vacinais e fechamento de fronteiras concentrou poderes extraordinários no Executivo em nome da preservação da vida biológica, reacendendo alertas de Agamben sobre a normalização da exceção.",
        "Porque os hospitais públicos suspenderam o atendimento médico a cidadãos que não usavam fardamentos.",
        "Porque as assembleias legislativas estaduais foram transferidas compulsoriamente para embarcações fluviais.",
        "Porque a fabricação de medicamentos fitoterápicos foi proibida por tratados diplomáticos da Europa.",
        "B",
        "A pandemia escancarou o dilema biopolítico: para salvar a vida biológica (fazer viver), governos suspenderam direitos constitucionais de ir e vir; pensadores debateram o risco de essa exceção virar rotina."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "De acordo com Michel Foucault, qual é a profunda e inseparável relação existente entre 'Saber' e 'Poder' na consolidação das ciências humanas no século XIX?",
        "O saber científico desenvolve-se de forma pura e independente, sem qualquer ponto de contato com disputas de autoridade política.",
        "Saber e poder produzem-se mutuamente: os discursos científicos da medicina, da psiquiatria, da criminologia e da pedagogia criam as verdades normativas que legitimam o confinamento, a classificação e a exclusão dos indivíduos.",
        "As universidades clássicas europeias eram administradas por comitês de tecelões industriais operários.",
        "A produção do saber acadêmico era financiada exclusivamente por guildas de ferreiros medievais.",
        "As sentenças de tribunais criminais municipais dependiam da aprovação de conselhos de astrônomos.",
        "B",
        "Não existe saber neutro para Foucault: a psiquiatria e o direito inventaram o conceito de 'anormal' para justificar trancar pessoas no hospício ou na cadeia; o saber legitima o poder e o poder financia o saber."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Como a noção agambeniana de 'Exclusão Inclusiva' explica a situação jurídica das pessoas mantidas em campos de refugiados nas fronteiras internacionais?",
        "Elas são acolhidas com plenos direitos civis e imediatas bolsas de subsistência habitacional urbana.",
        "Elas são incluídas na ordem soberana precisamente pela forma de sua exclusão: o Estado as reconhece e as cerca fisicamente com arame farpado, mas desprovendo-as de direitos de cidadania, transformando-as em vida nua exposta.",
        "Elas são nomeadas funcionárias consulares honorárias para a mediação de tratados alfandegários.",
        "Elas recebem títulos de propriedade imobiliária rural nas encostas férteis das montanhas vizinhas.",
        "Elas têm suas certidões de nascimento substituídas por diplomas acadêmicos em filologia clássica.",
        "B",
        "A exclusão inclusiva: o refugiado não está fora do poder; ele está preso dentro da cerca do campo pelo poder, mas desprovido de qualquer direito da lei; o poder o captura retirando sua humanidade legal."
    ))

    questoes_brutas.append((
        27, "EM13CHS102", "intermediario",
        "Qual é a advertência fundamental de Giorgio Agamben para evitar o erro comum de associar o Estado de Exceção unicamente a golpes militares com tanques nas ruas?",
        "Demonstrar que as ditaduras do século XX utilizavam uniformes militares confeccionados com tecidos de linho.",
        "Evidenciar que o estado de exceção moderno é gestado silenciosamente no interior das próprias democracias constitucionais, através de medidas provisórias de urgência, decisões judiciais atípicas e leis de exceção contra o crime e o terrorismo.",
        "Comprovar que as cartas constitucionais deixam de vigorar sempre que ocorrem eleições suplementares municipais.",
        "Provar que a estabilidade social depende da proibição da realização de reuniões comunitárias nas ruas.",
        "Afirmar que a repressão policial urbana decorre unicamente de orientações oraculares de sacerdotes.",
        "B",
        "A exceção não precisa de generais nas ruas: ela é aprovada pelo parlamento e chancelada por juízes através de leis 'de emergência' e mandados genéricos que suprimem garantias de certos grupos civis."
    ))

    questoes_brutas.append((
        28, "EM13CHS601", "intermediario",
        "Como Foucault analisa o surgimento da 'Delinquência' e a função real da Prisão moderna em Vigiar e Punir?",
        "A prisão tem como meta eliminar completamente os crimes e regenerar todos os infratores para a caridade cristã.",
        "A prisão não visa suprimir a infração, mas produzir e gerir a delinquência em um circuito controlado, isolando os criminosos perigosos e utilizando-os como justificativa contínua para ampliar a vigilância policial sobre toda a sociedade.",
        "Os estabelecimentos penais foram criados para fornecer mão de obra gratuita para colheitas agrícolas de uva.",
        "A arquitetura prisional renascentista foi concebida por monges para promover retiros silenciosos de oração.",
        "As penas de privação de liberdade foram inventadas por corporações de marinheiros mercantes no mar do Norte.",
        "B",
        "A prisão fracassou em regenerar, mas triunfou em seu objetivo real: produzir uma classe controlada de delinquentes que justifica a presença permanente de patrulhas e câmeras vigiando a cidade inteira."
    ))

    questoes_brutas.append((
        29, "EM13CHS602", "intermediario",
        "De que modo a decretação do Incêndio do Reichstag (1933) e as Leis Raciais de Nuremberg (1935) no regime nazista ilustram a análise de Agamben sobre o estado de exceção?",
        "Demonstrando que os tribunais alemães respeitavam integralmente a separação dos três poderes de Montesquieu.",
        "Evidenciando que o regime de Hitler utilizou a suspensão legal de direitos da Constituição de Weimar e a cassação da cidadania dos judeus para rebaixá-los à vida nua biopolítica, operando o extermínio sob a chancela da própria lei de exceção.",
        "Provando que as leis eleitorais germânicas eram formuladas por congregações religiosas beneditinas.",
        "Mostrando que as perseguições raciais decorreram exclusivamente de decisões de conselhos de carpinteiros.",
        "Afirmando que as autoridades nazistas proibiam o uso de medicamentos farmacêuticos em hospitais públicos.",
        "B",
        "Auschwitz foi construído pela legalidade da exceção: suspenderam a constituição em 1933 e tiraram os direitos civis em 1935; os judeus viraram vidas nuas e foram assassinados sob decretos de Estado."
    ))

    questoes_brutas.append((
        30, "EM13CHS603", "intermediario",
        "Como a máxima de Foucault 'Onde há poder, há resistência' desconstrói a ideia fatalista de que a disciplina e o biopoder formam um sistema totalitário inescapável?",
        "Afirmando que a resistência exige o isolamento do cidadão em mosteiros contemplativos nas montanhas.",
        "Demonstrando que, sendo o poder uma relação móvel e assimétrica de forças, ele engendra imediatamente focos múltiplos, capilares e móveis de contra-conduta, insubmissão e reinvenção da liberdade em cada ponto onde atua.",
        "Provando que a libertação dos corpos depende do fechamento compulsório de todas as escolas públicas.",
        "Exigindo que os movimentos sociais utilizem unicamente armas brancas em manifestações urbanas.",
        "Sustentando que a contestação política é inútil diante do avanço das tecnologias de vigilância digital.",
        "B",
        "O poder não é uma jaula estática: onde alguém tenta disciplinar, surgem frestas, recusas e novas formas de vida; a resistência não é um milagre externo, mas uma força que pulsa na própria teia relacional."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Qual é o significado do termo 'Dispositivo' (*Dispositif*) no vocabulário analítico de Michel Foucault?",
        "Uma ferramenta de metal utilizada para abrir e fechar portões de fortalezas militares.",
        "A rede heterogênea que articula discursos, instituições, arquiteturas, leis, medidas administrativas, enunciados científicos e morais para responder a uma urgência estratégica de controle social.",
        "Um modelo matemático utilizado para calcular a velocidade de escoamento de águas em aquedutos.",
        "Um aparelho telegráfico instalado em embaixadas para a comunicação de notícias de guerra.",
        "Uma insígnia bordada em fardamentos militares para identificar a hierarquia de oficiais na corte.",
        "B",
        "O dispositivo é o nó que amarra tudo: leis, paredes de prisão, teses médicas e moralidades articuladas estrategicamente para enfrentar um problema social (como a loucura, o crime ou a sexualidade)."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Por que, para Giorgio Agamben, a cidadania moderna carrega uma fragilidade estrutural diante das práticas do poder soberano?",
        "Porque as cédulas de identidade e certidões de nascimento eram impressas em tecidos perecíveis.",
        "Porque a cidadania é a inscrição da vida natural no ordenamento estatal; se o Estado decreta a exceção e cassa os direitos civis de um indivíduo ou grupo, a pessoa perde sua couraça cidadã e desce à vida nua matável.",
        "Porque os cidadãos das repúblicas democráticas são obrigados a prestar serviços em navios mercantes.",
        "Porque as cartas constitucionais contemporâneas proíbem a posse de imóveis residenciais por jovens.",
        "Porque a concessão do direito de voto depende da aprovação prévia em testes de genealogia nobre.",
        "B",
        "A lição de Agamben sobre a fragilidade dos direitos: os direitos do homem só nos protegem enquanto o Estado nos reconhece como cidadãos; basta um decreto de exceção para que qualquer um seja tratado como vida nua."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "Como a arquitetura das escolas tradicionais (carteiras enfileiradas, inspeção visual, divisão por séries e sinal sonoro) reflete a microfísica disciplinar?",
        "Garantindo que todos os alunos aprendam a tocar trompetes em desfiles cívicos nas praças.",
        "Espelhando a mesma anatomopolítica de adestramento dos corpos: imobilização física, sujeição ao olhar do professor e internalização da pontualidade e da hierarquia requeridas pelo mundo fabril e burocrático.",
        "Facilitando o cultivo de hortas comunitárias de vegetais no pátio dos estabelecimentos de ensino.",
        "Obrigando os estudantes a utilizarem uniformes confeccionados com couro de animais silvestres.",
        "Proibindo o uso de cadernos escolares encadernados com folhas de papel de celulose branca.",
        "B",
        "A escola tradicional não foi desenhada ao acaso: a carteira fixa no chão, a fila indiana e o sino que toca treinam o corpo da criança para passar a vida obedecendo às exigências mecânicas da fábrica e do escritório."
    ))

    questoes_brutas.append((
        34, "EM13CHS602", "intermediario",
        "De que modo as teses de Foucault sobre o 'Corpo Dócil' e a 'Anatomopolítica' dialogam com os padrões contemporâneos de estética corporal, dietas restritivas e cirurgias plásticas?",
        "Mostrando que os cidadãos contemporâneos abandonaram qualquer preocupação com a saúde física corporal.",
        "Demonstrando que a disciplina corporal foi internalizada pelos próprios sujeitos: o indivíduo vigia seus passos em relógios digitais, submete seu corpo a treinos extenuantes e modula sua aparência para adequar-se à norma do corpo produtivo e desejável.",
        "Provando que as academias de ginástica foram concebidas originalmente por corporações militares de arqueiros.",
        "Exigindo que os estabelecimentos desportivos sejam administrados por comitês de teólogos medievais.",
        "Determinando que a circulação de suplementos alimentares deva ser autorizada por embaixadas diplomáticas.",
        "B",
        "A disciplina não precisa mais de guardas com cassetete: o próprio sujeito vira vigia de seu corpo; contamos calorias em aplicativos, monitoramos passos no smartwatch e nos punimos quando falhamos na dieta."
    ))

    questoes_brutas.append((
        35, "EM13CHS603", "intermediario",
        "Como a distinção entre 'Lei Penal' e 'Norma Disciplinar' opera na diferenciação entre a sociedade de soberania e a sociedade de normalização em Foucault?",
        "A lei penal proíbe o casamento consanguíneo e a norma disciplinar regulamenta o comércio de café.",
        "A lei jurídica opera pela linha divisória formal entre o lícito e o ilícito (quem transgride é punido); a norma disciplinar opera pela gradação contínua entre o normal e o anormal, buscando corrigir, tratar e classificar o desvio.",
        "A lei penal aplica-se exclusivamente a generais de brigada e a norma disciplinar a marinheiros fluviais.",
        "Ambas as categorias são idênticas e foram formuladas por magistrados romanos da Antiguidade clássica.",
        "A lei penal exige o pagamento de multas em ouro e a norma disciplinar a doação de ferramentas de arado.",
        "B",
        "A soberania diz: 'o ato é legal ou ilegal'. A disciplina vai mais fundo e diz: 'você é normal ou anormal, perigoso ou são'; a norma invade a psicologia e a conduta para classificar e corrigir os indivíduos."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Qual é a relação que Giorgio Agamben estabelece entre o conceito de 'Estado de Sítio' e as chamadas 'Zonas de Anomia' nas cidades contemporâneas?",
        "Comprova que os bairros metropolitanos devem possuir muralhas de pedra com fossos de água ao redor.",
        "Demonstra que governos democráticos delimitam territórios urbanos (favelas, periferias, centros de detenção) onde as garantias constitucionais são tacitamente suspensas pelo aparato policial, criando verdadeiros bolsões onde a vida nua pode ser violentada impunemente.",
        "Afirma que os tribunais civis devem terceirizar os inquéritos criminais a guildas de navegadores costeiros.",
        "Exige que os prefeitos municipais prestem contas de seus mandatos a conselhos eclesiásticos de mosteiros.",
        "Determina que a segurança de bairros comerciais seja entregue a regimentos de cavalaria pesada.",
        "B",
        "A exceção geográfica nas cidades: enquanto nos bairros ricos o cidadão tem presunção de inocência e garantias plenas, na favela a polícia entra sem mandado à noite; cria-se a anomia onde o morador vira vida nua."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "De acordo com a genealogia foucaultiana da 'Confissão', como a prática pastoral cristã de revelar os pecados ao padre se transformou na moderna intimidade vigiada da medicina e da psicologia?",
        "Substituindo os confessionários religiosos por cabines de votação parlamentar secreta nas praças.",
        "Transpondo a obrigação de verbalizar a verdade secreta da alma para os consultórios médicos, sofás de analistas e tribunais, onde o sujeito é incitado a falar ininterruptamente sobre seus desejos e desvios para ser classificado e governado.",
        "Obrigando os pacientes de hospitais públicos a prestarem votos monásticos de penitência e jejum.",
        "Proibindo os cidadãos de conversarem com familiares sobre temas relacionados à saúde reprodutiva.",
        "Exigindo que os diagnósticos psiquiátricos fossem redigidos em dialetos latinos arcaicos do século IV.",
        "B",
        "O poder não cala, ele obriga a falar: a confissão religiosa migrou para a psiquiatria, para a pedagogia e para as redes sociais; incitar o sujeito a expor seus segredos íntimos é a melhor forma de mapeá-lo e dirigi-lo."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Como a noção agambeniana do 'Homo Sacer' nos permite compreender a vulnerabilidade extrema de 'Imigrantes Apátridas e Indocumentados' que naufragam no mar Mediterrâneo ou cruzam fronteiras militarizadas?",
        "Mostrando que os migrantes possuem passaportes diplomáticos emitidos por conselhos monásticos suíços.",
        "Evidenciando que, por estarem desprovidos de documentos e de vínculo de cidadania com qualquer Estado, esses seres humanos são reduzidos à condição de vida nua matável e insacrificável: deixados afundar nas águas ou encarcerados em gaiolas sem que governantes respondam por crime algum.",
        "Comprovando que as companhias de navegação marítima cobram tarifas reduzidas de famílias de refugiados.",
        "Determinando que os países de destino devem doar fazendas agrícolas produtivas a todos os imigrantes recém-chegados.",
        "Provando que as convenções internacionais de direitos humanos dispensam a ratificação por parlamentos nacionais.",
        "B",
        "O refugiado sem papéis encarna o Homo Sacer: se ele morre afogado no Mediterrâneo ou trancado numa jaula no deserto, ninguém vai preso por assassinato; a vida dele foi rebaixada a uma matéria descartável."
    ))

    questoes_brutas.append((
        39, "EM13CHS602", "intermediario",
        "Em que sentido o 'Racismo de Estado' em Foucault explica o surgimento do Apartheid sul-africano e das políticas de segregação racial nos Estados Unidos?",
        "Como um acidente conjuntural provocado pelo aumento dos preços internacionais de tecidos de algodão.",
        "Como a aplicação sistemática de dispositivos biopolíticos estatais que codificaram em leis civis e policiais a fragmentação da população, privando corpos negros de direitos fundamentais para assegurar a pureza, a riqueza e a supremacia biopolítica da minoria branca.",
        "Como o resultado de assembleias populares democráticas conduzidas por marinheiros em zonas portuárias.",
        "Como uma exigência de tratados diplomáticos bilaterais que regulamentavam a mineração de prata e carvão.",
        "Como uma herança mitológica nórdica adotada por governadores de províncias agrícolas coloniais.",
        "B",
        "O Apartheid e o Jim Crow foram biopolítica pura codificada em lei: o Estado usou a biologia, a segregação espacial e o racismo institucional para proteger a 'vida' dos brancos relegando corpos negros à morte social."
    ))

    questoes_brutas.append((
        40, "EM13CHS603", "intermediario",
        "Como as garantias processuais do 'Habeas Corpus' e as 'Cláusulas Pétreas' da Constituição brasileira de 1988 atuam como diques civilizatórios contra a lógica da Exceção de Agamben?",
        "Autorizando os generais de exército a fecharem os fóruns de justiça criminal durante emergências fiscais.",
        "Constituindo escudos jurídicos inderrogáveis que proíbem o Estado de suspender a liberdade física arbitrariamente, impedindo a anulação das garantias e barrando a conversão de cidadãos sob acusação em vida nua indefesa.",
        "Exigindo que os réus em processos penais sejam julgados exclusivamente por sacerdotes católicos.",
        "Determinando que as sentenças condenatórias sejam sorteadas anualmente por jurados de infantaria leve.",
        "Provando que as prisões cautelares devem ser realizadas mediante o confisco de animais domésticos.",
        "B",
        "O Habeas Corpus ('tenhas o teu corpo livre') é a grande invenção jurídica contra o biopoder: ele diz ao Estado que ninguém pode ter seu corpo encarcerado sem a lei e sem o devido processo civilizado."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60 - Com Etapas 1 e 2)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a ruptura entre a concepção jurídica clássica de Soberania (Hobbes e Bodin) e a 'Microfísica do Poder' de Michel Foucault: de que maneira o abandono da obsessão pelo Estado centralizado como fonte única de dominação transforma a compreensão das relações cotidianas de autoridade?",
        "Comprovando que as instituições prisionais operavam sem funcionários de carceragem ou guardas de muralha.",
        "Demonstrando que o poder não emana exclusivamente de um centro piramidal estatal por mandamentos de lei, mas constitui uma teia imanente, capilar e móvel de forças que se engendra e se reproduz nas práticas cotidianas, nos discursos científicos, nas normas corporais e nas relações intersubjetivas em cada ponto do tecido social.",
        "Provando que as monarquias europeias foram depostas por corporações de agrimensores municipais.",
        "Determinando que os cidadãos devam prestar juramentos de fidelidade militar a líderes de partidos políticos.",
        "Afirmando que a obediência às leis civis depende de rituais divinatórios realizados por sacerdotes paroquiais.",
        "B",
        "- **Etapa 1:** Desconstruir a miragem centralizadora da soberania: juristas e filósofos tradicionais olhavam apenas para o trono real e para o parlamento, reduzindo o poder à lei escrita e à polícia do Estado.\n- **Etapa 2:** Evidenciar a revolução microfísica de Foucault: o poder pulsa na família, na escola, no consultório e na fábrica; cortar a cabeça do rei na teoria política significa reconhecer que o poder opera de baixo para cima nas micropolíticas cotidianas do corpo e do saber."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em Vigiar e Punir, Foucault justapõe a execução dantesca do regicida Damiens em 1757 (esquartejado por cavalos em praça pública) ao regulamento rigoroso e silencioso da Casa de Detenção de Jovens de Paris em 1838. Analise a significação histórica dessa mutação penal para a economia política do poder punitivo:",
        "Demonstrando que as execuções sangrentas foram extintas devido à escassez de cavalos de tração na França.",
        "Evidenciando a passagem de uma economia punitiva arcaica e espetacular (que feria o corpo físico para proclamar a vingança do monarca ferido) para uma economia refinada, econômica e constante (que poupa a carne para adestrar a alma, controlar a mente e normalizar o tempo e os gestos de indivíduos úteis ao capitalismo industrial).",
        "Comprovando que os tribunais criminais parisienses substituíram o julgamento civil por duelos desportivos.",
        "Exigindo que os presídios do século XIX fossem construídos exclusivamente em ilhas fluviais do interior.",
        "Provando que as sentenças de prisão decorreram de decisões tomadas por conselhos de boticários fabris.",
        "B",
        "- **Etapa 1:** Analisar a obsolescência do suplício: o espetáculo sangrento de Damiens era desordenado, caro e perigoso, pois o povo na praça frequentemente se rebelava contra a crueldade do rei.\n- **Etapa 2:** Revelar a racionalidade da disciplina moderna: a prisão substitui a fúria pela técnica silenciosa da rotina; não se esquarteja mais o corpo, fabrica-se uma alma dócil e produtiva para a ordem social."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Considere a anatomia do Panóptico de Jeremy Bentham descrita por Michel Foucault: 'A visibilidade é uma armadilha. Aquele que está submetido a um campo de visibilidade, e que sabe disso, assume a responsabilidade pelas coações do poder; ele se torna o princípio de sua própria sujeição.' Analise como esse princípio estrutura a vigilância digital e a coleta de dados de usuários na internet contemporânea.",
        "Autorizando os provedores de redes sociais a suspenderem o envio de mensagens eletrônicas nas sextas-feiras.",
        "Demonstrando que, ao navegarem sob a constante coleta de dados, rastreamento de cliques e monitoramento de algoritmos, os usuários sabem que seu comportamento digital é escaneado ininterruptamente, internalizando a fiscalização algorítmica e moldando espontaneamente suas postagens e comportamentos para obter aprovação social e escapar de punições das plataformas.",
        "Comprovando que as plataformas de tecnologia foram concebidas por corporações de tipógrafos medievais.",
        "Exigindo que os computadores digitais sejam lacrados com cera de abelha em períodos de recesso legislativo.",
        "Determinando que os bancos de dados virtuais devam ser fiscalizados por conselhos de generais reformados.",
        "B",
        "- **Etapa 1:** Resgatar a essência do panóptico: a armadilha reside no fato de saber que pode ser visto a qualquer instante, o que faz o sujeito policiar seus próprios passos sem necessidade de coerção física direta.\n- **Etapa 2:** Projetar no ecossistema digital das redes: os algoritmos e curtidas são a nova torre invisível; nós mesmos nos expomos na cela iluminada da timeline, moldando nossa conduta para nos adaptarmos às métricas da plataforma, operando nossa própria sujeição."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Analise a articulação necessária entre a 'Anatomopolítica do Corpo' (século XVIII) e a 'Biopolítica da População' (século XIX): por que Foucault afirma que o desenvolvimento do Capitalismo industrial exigiu simultaneamente a intervenção sobre essas duas escalas distintas do biopoder?",
        "Porque as fábricas mecânicas consumiam carvão vegetal que necessitava de aprovação por corporações monásticas.",
        "Porque o capitalismo necessitava tanto de corpos individuais rigorosamente adestrados, disciplinados e cronometrados para o trabalho fabril contínuo (anatomopolítica), quanto da regulação biológica em massa dos processos da população (natalidade, vacinação, higiene urbana, fluxo de mão de obra) para garantir a reprodução estável da força de trabalho social (biopolítica).",
        "Comprovando que os tecidos manufaturados exigiam a utilização exclusiva de corantes de madeira tropical.",
        "Determinando que os operários da indústria têxtil deveriam prestar serviços em navios de guerra anualmente.",
        "Afirmando que a expansão industrial decorreu unicamente da celebração de alianças diplomáticas entre dinastias.",
        "B",
        "- **Etapa 1:** Analisar o polo anátomo-disciplinar: o capital precisava que cada operário chegasse no horário, operasse a máquina com gestos precisos e não fizesse greves (a disciplina do corpo individual).\n- **Etapa 2:** Analisar o polo bio-regulador: o capital precisava que a classe trabalhadora como espécie viva não fosse dizimada por cólera ou tuberculose e continuasse procriando trabalhadores saudáveis; a biopolítica assegurou a reprodução demográfica da força de trabalho."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Em seu curso Em Defesa da Sociedade, Michel Foucault formula a teoria do 'Racismo de Estado': se o biopoder opera sob o imperativo de 'fazer viver', como a introdução do racismo permite ao Estado moderno exercer o poder soberano de morte e o extermínio bélico em escala industrial?",
        "Comprovando que as disputas raciais eram causadas por conflitos de preços de sementes nas feiras rurais.",
        "Demonstrando que o racismo introduz uma cesura biológica no tecido da espécie humana, dividindo-a entre uma raça saudável e civilizada e uma sub-raça degenerada e contagiosa; assim, o ato de matar o 'outro' não é apresentado como crime militar, mas como ato sanitário preventivo, onde a eliminação do perigoso fortalece biologicamente a vida da população dominante.",
        "Determinando que os uniformes militares devam ser confeccionados exclusivamente com fios de lã escarlate.",
        "Afirmando que as teorias eugênicas do século XIX foram copiadas de códigos monásticos bizantinos antigos.",
        "Exigindo que as divisões de infantaria devam realizar testes de leitura poética antes de invasões armadas.",
        "B",
        "- **Etapa 1:** Revelar a contradição do biopoder: como um Estado que diz que sua missão é proteger e otimizar a vida pode mandar milhões de pessoas para a morte e o genocídio?\n- **Etapa 2:** Desvelar a engrenagem do racismo biopolítico: o racismo transforma o inimigo político em ameaça biológica degenerada; proclama-se que 'a morte deles é a garantia da nossa saúde e da nossa sobrevivência'; foi essa lógica higienista que legitimou Auschwitz e os massacres coloniais."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Analise a distinção grega entre 'Zoé' e 'Bíos' recuperada por Giorgio Agamben: de que maneira a tese de que a política ocidental se fundou sobre a 'Exclusão Inclusiva' da Zoé desvela que o Estado moderno tem como matéria fundante a produção da 'Vida Nua'?",
        "Provando que as assembleias cívicas gregas realizavam suas sessões em anfiteatros cobertos por telas de algodão.",
        "Evidenciando que a comunidade política dos cidadãos dotados de direitos (bíos) não se constituiu de forma autônoma e pacífica, mas pela captura forçada da simples vida biológica crua (zoé) que foi despojada de suas proteções naturais e enquadrada na soberania como matéria nua e vulnerável, sobre a qual o soberano pode exercer o arbítrio da violência de exceção.",
        "Determinando que os cidadãos das cidades democráticas eram obrigados a pagar impostos em cavalos de corrida.",
        "Afirmando que as distinções linguísticas clássicas foram esquecidas por tradutores andaluzes medievais.",
        "Comprovando que os magistrados da antiguidade romana realizavam audiências penais unicamente em dias úteis.",
        "B",
        "- **Etapa 1:** Compreender a separação originária grega: no mundo clássico, a zoé (vida biológica animal) ficava confinada ao lar privado e o bíos (vida ética do cidadão) brilhava na ágora pública.\n- **Etapa 2:** Descobrir a operação de captura soberana de Agamben: o Estado moderno politiza a zoé, transformando-a em vida nua; ao capturar o corpo biológico como refém da lei, o soberano ganha o poder de retirar os direitos de qualquer cidadão e reduzi-lo a mero alvo de violência estatal."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Examine o enigma jurídico do 'Homo Sacer' no Direito Romano arcaico: por que a conjunção de ser 'Insacrificável aos Deuses' e simultaneamente 'Matável Impunemente por Qualquer Homem' coloca esse indivíduo no limbo absoluto de desamparo normativo?",
        "Porque os cidadãos romanos que assassinavam banidos eram condecorados com moedas de prata no Senado.",
        "Porque o banido é duplamente expulso dos dois sistemas reguladores da existência social: ele é retirado do direito humano civil (sua morte não constitui homicídio nem mobiliza os tribunais) e é retirado do direito sagrado divino (sua morte não pode ser oferecida em sacrifício religioso aos deuses), encarnando a pura vida nua exposta à violência sem freios de ninguém.",
        "Porque as cerimônias de banimento romano exigiam a destruição física de templos dedicados a Júpiter.",
        "Porque os réus condenados a exílio eram transportados exclusivamente em galeras movidas a tração animal.",
        "Porque a legislação romana proibia que parentes de criminosos exercessem funções em oficinas de carpintaria.",
        "B",
        "- **Etapa 1:** Desvendar a dupla expulsão do Homo Sacer: se sua morte fosse homicídio, ele ainda estaria protegido pela lei dos homens; se pudesse ser sacrificado no altar, estaria acolhido pela lei dos deuses.\n- **Etapa 2:** Concluir sobre o desamparo total da vida nua: não sendo cidadão nem oferenda sagrada, ele é um nada jurídico; sua morte não tem valor ético nem custa pena a ninguém; ele é o homem despido de toda humanidade perante a força bruta."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Ao investigar a obra Estado de Exceção, Giorgio Agamben formula a tese de que o 'Estado de Exceção converteu-se no paradigma de governo dominante na política contemporânea'. Como a utilização contínua de medidas provisórias urgentes, leis antiterrorismo e decretações de emergência subverte a clássica separação dos Três Poderes?",
        "Transferindo a redação de normas processuais a comissões internacionais de marinheiros mercantes.",
        "Esvaziando o papel soberano do Parlamento e do debate legislativo plural ao concentrar a faculdade exclusiva de emitir normas com força de lei nas mãos do Poder Executivo e de órgãos de segurança sob o pretexto de emergências permanentes, normalizando a anomia e tornando indistinta a fronteira entre a legalidade e a ilegalidade estatal.",
        "Comprovando que os códigos de leis civis deixam de ter eficácia quando ocorrem tempestades fluviais.",
        "Exigindo que os magistrados de cortes superiores devam prestar exames anuais de filologia clássica.",
        "Determinando que os tratados diplomáticos devam ser ratificados por aclamação unânime de agricultores.",
        "B",
        "- **Etapa 1:** Relembrar o desenho constitucional do equilíbrio de poderes: o Legislativo debate e faz as leis, o Executivo administra sob a lei e o Judiciário julga.\n- **Etapa 2:** Revelar a mutação autoritária da exceção contínua: sob o pretexto de crises sem fim (crise fiscal, guerra ao crime, terrorismo), o Executivo governa por decretos de urgência; a exceção engole a separação de poderes e a democracia representativa vira administração burocrática por decretos."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Analise a perturbadora tese de Giorgio Agamben de que o 'Campo de Concentração é o Nômos do Moderno': por que, para o filósofo, o campo não deve ser compreendido como uma anomalia histórica monstruosa superada com a queda do nazismo em 1945?",
        "Porque os acampamentos militares do século XIX utilizavam tendas tecidas com fibras vegetais perecíveis.",
        "Porque o campo de concentração é a estrutura espacial em que o estado de exceção é permanentemente institucionalizado e a vida nua é produzida de forma rotineira; estrutura essa que ressurge e se multiplica hoje em centros de detenção de imigrantes indocumentados, aeroportos de deportação, prisões clandestinas e favelas sitiadas onde o direito do Estado de direito não vigora.",
        "Comprovando que os generais imperiais prussianos desconheciam as regras de administração civil territorial.",
        "Determinando que os monumentos memoriais do Holocausto devam ser construídos unicamente em áreas florestais.",
        "Afirmando que a solução para a crise de refugiados depende da criação de colônias agrárias na Antártida.",
        "B",
        "- **Etapa 1:** Afastar a ilusão de que o campo foi apenas loucura passageira de Hitler: historiadores liberais tratam Auschwitz como um ponto fora da curva da civilização iluminista.\n- **Etapa 2:** Revelar a presença viva da matriz do campo hoje: o campo é o lugar onde o direito é suspenso e o corpo vira vida nua; essa engrenagem opera na cerca dos centros de detenção de imigrantes na fronteira, nas prisões sem acusação de Guantánamo e nas periferias militarizadas do mundo."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Em Post-scriptum sobre as Sociedades de Controle, Gilles Deleuze afirma: 'Nas sociedades disciplinares sempre se estava recomeçando (da escola à caserna, da caserna à fábrica), ao passo que nas sociedades de controle nunca se termina nada.' Analise as implicações dessa tese para a precarização psíquica, o esgotamento (Burnout) e o trabalho imaterial no capitalismo digital.",
        "Mostrando que os trabalhadores contemporâneos dedicam suas tardes exclusivamente ao cultivo de hortas residenciais.",
        "Evidenciando que a superação dos muros fechados da fábrica não libertou o trabalhador, mas disseminou o controle contínuo sobre a totalidade de sua existência através de metas móveis, conexões digitais perpétuas, autogestão da ansiedade e perseguição pelo trabalho 24 horas por dia em dispositivos móveis, gerando a exaustão psíquica e a corrosão da fronteira entre o trabalho e o descanso.",
        "Comprovando que as empresas fabris modernas utilizam caldeiras a vapor com turbinas hidráulicas antigas.",
        "Determinando que os servidores públicos devam receber salários corrigidos pelo valor de mercado do cobre.",
        "Exigindo que os estabelecimentos industriais fechem suas portas durante períodos de solstício de inverno.",
        "B",
        "- **Etapa 1:** Contrastar a disciplina de confinamento de Foucault: na fábrica ou na escola, o sino tocava, o indivíduo saía e sua mente descansava até o dia seguinte.\n- **Etapa 2:** Analisar a perseguição contínua da sociedade de controle de Deleuze: com o celular e a internet, a empresa vai no bolso do trabalhador para a cama, para as férias e para o almoço; o controle a céu aberto nunca desliga, produzindo a epidemia de ansiedade e esgotamento psíquico do século XXI."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Analise a ambivalência do Biopoder na gestão da Saúde Pública e das Políticas de Vacinação em Massa: de que maneira a proteção coletiva da vida da população pode deslizar para mecanismos autoritários de controle social e estigmatização de minorias?",
        "Comprovando que as fórmulas químicas de vacinas dependem de aprovação prévia por conselhos de monges paroquiais.",
        "Demonstrando que, ao mesmo tempo em que a biopolítica viabiliza conquistas sanitárias indispensáveis (erradicação de epidemias mortais, aumento da expectativa de vida, saneamento das cidades), a lógica estatal de higienização da população pode ser pervertida para vigiar condutas individuais, justificar a exclusão social de grupos marginalizados rotulados como 'vetores de contaminação' e suprimir liberdades civis essenciais.",
        "Determinando que os hospitais públicos devam exigir juramentos militares de fidelidade de seus pacientes.",
        "Provando que as doenças infecciosas do século XIX decorriam unicamente da ausência de pavimentação em ruas.",
        "Afirmando que a erradicação de viroses depende do isolamento dos cidadãos em retiros espirituais alpinos.",
        "B",
        "- **Etapa 1:** Reconhecer o polo protetor e civilizatório da saúde pública: vacinas, esgotos e hospitais reduzem a mortalidade infantil e protegem os mais vulneráveis contra vírus mortais.\n- **Etapa 2:** Diagnosticar o risco autoritário do higienismo biopolítico: a obsessão por purificar o corpo social historicamente levou à eugenia, ao internamento forçado de loucos e prostitutas e à segregação de populações pobres rotuladas como focos de infecção; a biopolítica exige vigilância ética permanente."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Examine o conceito de 'Combatente Inimigo Ilegal' adotado pelo governo dos Estados Unidos para justificar as prisões na Baía de Guantánamo à luz da teoria de Giorgio Agamben: qual foi o estratagema jurídico mobilizado para suspender as Convenções de Genebra e a Constituição norte-americana?",
        "A celebração de um tratado de paz comercial entre generais do exército e marinheiros cubanos.",
        "A invenção de uma categoria jurídica aberrante e híbrida que não reconhece o detido nem como cidadão com garantias de devido processo legal perante tribunais civis, nem como prisioneiro de guerra com direitos humanitários sob tratados internacionais, criando um vácuo de exceção onde o preso é reduzido à vida nua descartável e torturável impunemente.",
        "A aplicação compulsória das regras de processo penal da Inglaterra do século XVII aos acusados de terrorismo.",
        "A determinação de que os prisioneiros deveriam disputar torneios de esgrima para conquistar alvarás de soltura.",
        "A transferência do controle do presídio militar para uma comissão de astrônomos de universidades públicas.",
        "B",
        "- **Etapa 1:** Analisar o dilema das categorias jurídicas existentes: se o terrorista é criminoso comum, tem direito a advogado, juiz e júri; se é militar inimigo, tem direito à proteção de prisioneiro de guerra das Convenções de Genebra.\n- **Etapa 2:** Desvelar a criação do Homo Sacer em Guantánamo: inventaram a palavra 'combatente ilegal' para negar ambos os direitos; fora do tribunal civil e fora da convenção de guerra, o sujeito vira vida nua num limbo territorial sem lei onde a tortura operou sem freios."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "No curso Nascimento da Biopolítica (1978-1979), Michel Foucault investiga o neoliberalismo e forja o conceito de 'Empresário de Si Mesmo'. Como essa formulação antecipa a internalização do poder na cultura contemporânea do empreendedorismo e da autoajuda corporativa?",
        "Provando que as empresas fabris modernas substituíram os salários fixos por doações de sementes de cereais.",
        "Evidenciando que o neoliberalismo não é apenas uma teoria econômica de livre mercado, mas uma tecnologia biopolítica de governo que molda a subjetividade humana, fazendo com que o próprio trabalhador precarizado se enxergue como uma 'empresa individual' responsável única pelo seu sucesso ou fracasso, canalizando todas as suas energias vitais para a autodisciplina produtiva do capital.",
        "Comprovando que as leis trabalhistas do século XX foram redigidas por congregações de religiosos mendicantes.",
        "Determinando que os profissionais liberais devem prestar contas financeiras a conselhos de artesãos urbanos.",
        "Afirmando que a competitividade comercial depende exclusivamente do alinhamento astronômico de constelações.",
        "B",
        "- **Etapa 1:** Desmontar a visão de que o neoliberalismo é apenas privatizar estatais: Foucault demonstrou que o neoliberalismo é uma forma de criar almas e governar vidas.\n- **Etapa 2:** Analisar a figura do 'empresário de si': o trabalhador não se vê mais como operário explorado, mas como 'empresa de um homem só'; se adoece ou fica pobre, a culpa é atribuída à sua falta de esforço pessoal; a disciplina é 100% internalizada na própria subjetividade."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "Ao examinar a violência armada e a letalidade policial nas periferias e favelas das metrópoles latino-americanas, de que modo as ferramentas teóricas de Agamben revelam que esses territórios funcionam como 'Espaços de Exceção Permanente'?",
        "Comprovando que as viaturas de polícia utilizam combustíveis derivados de óleos vegetais de exportação.",
        "Demonstrando que, embora a Constituição proclame a inviolabilidade da vida e do domicílio para todos, nas periferias e favelas a autoridade estatal atua sob uma suspensão tácita das garantias penais, onde invasões sem mandado, execuções sumárias e estigmatização de corpos negros e periféricos são naturalizadas, produzindo a vida nua que pode ser ceifada sem repercussão jurídica.",
        "Determinando que os moradores de áreas periféricas devam receber títulos de nobreza outorgados pelo Senado.",
        "Provando que as incursões policiais urbanas decorrem de deliberações em assembleias de estudantes universitários.",
        "Afirmando que a segurança pública municipal depende da celebração de alianças diplomáticas com cidades vizinhas.",
        "B",
        "- **Etapa 1:** Contrastar a promessa da igualdade constitucional com a geografia das cidades: a constituição diz que a casa é asilo inviolável e que ninguém será morto pelo Estado sem julgamento.\n- **Etapa 2:** Revelar a exceção territorializada de Agamben: quando o camburão sobe o morro, a lei é suspensa na prática; o jovem negro da periferia é tratado como Homo Sacer moderno: a bala perdida ou o disparo de fuzil o mata e o caso é arquivado como 'auto de resistência', naturalizando a morte da vida nua."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Analise a relação entre o conceito foucaultiano de 'Contra-Conduta' e as lutas sociais de minorias (como movimentos feministas, negros, LGBTQIA+ e antimanicomiais): como a resistência se afirma a partir do próprio terreno das normas que a tentam assujeitar?",
        "Exigindo que os movimentos sociais fechem todas as universidades públicas de formação humanística.",
        "Demonstrando que, ao se recusarem a ser governadas e classificadas da maneira como os discursos médicos, jurídicos e morais tradicionais impuseram, essas coletividades mobilizam o próprio saber e os corpos para ressignificar categorias estigmatizadas, afirmando novas formas de existência, de prazer e de cidadania emancipada.",
        "Comprovando que as reivindicações de gênero e raça foram concebidas por conselhos monásticos no século XII.",
        "Determinando que as assembleias de movimentos cívicos devam aprovar manifestos em dialetos latinos arcaicos.",
        "Afirmando que a conquista de direitos humanos depende da proibição da publicação de livros didáticos.",
        "B",
        "- **Etapa 1:** Definir contra-conduta em Foucault: a arte de não ser governado de tal modo, por tais pastores e com tais custos; a recusa em aceitar a identidade imposta pelo poder.\n- **Etapa 2:** Ilustrar com os movimentos contemporâneos: quando a psiquiatria rotulava a homossexualidade como doença, o movimento exigiu a despatologização; quando rotulavam corpos negros como inferiores, o movimento afirmou o orgulho e a potência da negritude; a resistência reescreve a norma."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Como a ascensão do chamado 'Capitalismo de Vigilância' e da 'Biopolítica Preditiva' (Shoshana Zuboff) aprofunda a tese foucaultiana sobre o controle invisível e a extração de dados comportamentais?",
        "Substituindo o uso de computadores industriais por calculadoras de engrenagens de ferro fundido.",
        "Expandindo o panóptico para a totalidade dos passos, buscas, curtidas, mensagens de voz e batimentos cardíacos dos usuários, convertendo a experiência humana privada em matéria-prima gratuita de dados que são processados por inteligência artificial para antecipar, modular e comercializar futuros comportamentos no mercado.",
        "Determinando que as plataformas de tecnologia digital devam fechar seus servidores em fins de semana.",
        "Comprovando que a mineração de dados na internet foi inventada por corporações marítimas mercantes.",
        "Exigindo que os usuários de redes virtuais façam juramentos notariais em cartórios de títulos e documentos.",
        "B",
        "- **Etapa 1:** Atualizar a escala do panóptico de Foucault: Bentham vigiava presidiários em celas; as big techs vigiam quatro bilhões de seres humanos livres em tempo real através do smartphone.\n- **Etapa 2:** Analisar a extração do superávit comportamental: nossos dados mais íntimos não são apenas vigiados, são minerados para treinar algoritmos que modulam o que compramos, em quem votamos e o que pensamos; o biopoder agora coloniza o inconsciente digital."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Examine a tese de Giorgio Agamben sobre a genealogia colonial dos 'Campos de Concentração': de que maneira os experimentos de confinamento e aniquilação praticados por impérios europeus em suas colônias ultramarinas (como os campos espanhóis em Cuba e britânicos na África do Sul) anteciparam o horror de Auschwitz?",
        "Demonstrando que os generais imperiais britânicos utilizavam armaduras de duelo de cavaleiros medievais.",
        "Evidenciando que os impérios coloniais europeus foram os primeiros a criar laboratórios espaciais onde o direito imperial não se aplicava e as populações nativas e camponesas colonizadas eram tratadas como corpos descartáveis de vida nua, sendo a barbárie de Auschwitz o retorno bumerangue das práticas de exceção coloniais para o próprio coração da Europa.",
        "Comprovando que as ferrovias africanas foram construídas exclusivamente para o transporte de trigo fino.",
        "Exigindo que as guerras coloniais fossem declaradas mediante leitura solene de epopeias mitológicas gregas.",
        "Afirmando que a dominação colonial dependia da celebração de alianças matrimoniosas entre reis africanos.",
        "B",
        "- **Etapa 1:** Descolonizar a história dos campos de extermínio: antes de Hitler fechar Auschwitz na Polônia, ingleses confinaram milhares de bôers e negros na África do Sul e espanhóis confinaram camponeses cubanos em campos de fome.\n- **Etapa 2:** Aplicar a tese do bumerangue imperial: os impérios europeus testaram a anomia e a vida nua nos corpos colonizados fora da Europa; quando o nazismo aplicou essa mesmíssima técnica dentro da própria Europa sobre cidadãos brancos e judeus, o Ocidente horrorizou-se com o monstro que ele próprio criara."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "No debate sobre o Direito Constitucional e os Direitos Humanos, como a formulação de Hannah Arendt sobre o 'Direito a Ter Direitos' se conecta de forma direta à teoria da Vida Nua de Giorgio Agamben?",
        "Autorizando os parlamentos nacionais a cancelarem a concessão de passaportes durante anos bissextos.",
        "Demonstrando que os chamados 'Direitos Humanos Universais' revelam-se uma ilusão ineficaz quando o ser humano perde a sua pertença a uma comunidade política soberana (como os refugiados e apátridas), pois sem um Estado que reconheça e faça valer suas leis, a pessoa humana é rebaixada à pura vida biológica desprovida de qualquer recurso jurídico real contra o arbítrio.",
        "Comprovando que as declarações de direitos foram assinadas unicamente por comandantes de frotas navais.",
        "Determinando que os cidadãos das repúblicas devam prestar serviços voluntários em colônias de plantio.",
        "Afirmando que a proteção aos direitos civis decorre da consulta a oráculos em templos religiosos antigos.",
        "B",
        "- **Etapa 1:** Resgatar a denúncia trágica de Hannah Arendt: quando os judeus e refugiados perderam a cidadania na Segunda Guerra, os direitos humanos proclamados na França em 1789 não os salvaram; ninguém defendeu quem não tinha Estado.\n- **Etapa 2:** Conectar com a vida nua de Agamben: sem o bíos da cidadania política, o homem vira mera zoé biológica; a Declaração de Direitos Humanos perde a força onde inexiste o direito fundamental de pertencer a uma comunidade com leis eficazes; o apátrida vira Homo Sacer exposto à fúria soberana."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Analise a crítica de Foucault à Psiquiatrização e à Medicalização da sociedade em História da Loucura (1961): como a demarcação científica entre a 'Razão' e o 'Desvario' serviu para higienizar e ordenar as cidades da modernidade burguesa?",
        "Provando que os hospitais psiquiátricos eram dirigidos por congregações de padeiros e artesãos municipais.",
        "Evidenciando que a loucura não foi simplesmente descoberta como uma patologia biológica neutra, mas construída socialmente através do grande internamento do século XVII, que encarcerou em massa loucos, vagabundos, mendigos, desempregados e dissidentes para limpar as ruas e impor a disciplina produtiva da nova ordem capitalista mercantil.",
        "Comprovando que as formulações farmacêuticas da época eram preparadas com substâncias extraídas de corais marinhos.",
        "Determinando que os juízes de tribunais civis deveriam emitir suas sentenças com base em posições planetárias.",
        "Exigindo que os estabelecimentos de saúde mental fossem transferidos para regiões montanhosas congeladas.",
        "B",
        "- **Etapa 1:** Desmascarar o mito da descoberta neutra da loucura: antes da modernidade, o louco andava nas aldeias e dialogava com a comunidade, visto muitas vezes como possuidor de uma verdade trágica.\n- **Etapa 2:** Revelar a operação política do 'Grande Internamento': no século XVII, criaram o Hospital Geral para trancar quem não trabalhava (o mendigo, o rebelde, o desajustado); a ciência psiquiátrica nasce para medicalizar e domesticar a dissidência em nome da ordem urbana burguesa."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Síntese formativa do Capítulo 21: por que o estudo crítico do Poder Disciplinar e da Biopolítica em Michel Foucault articulado à teoria do Estado de Exceção e da Vida Nua em Giorgio Agamben é indispensável para a formação ética e política da juventude no Século XXI?",
        "Ensinando aos estudantes técnicas de espionagem cibernética e sonegação de tributos corporativos.",
        "Instrumentalizando os jovens estudantes com um olhar analítico perspicaz para desmascarar as formas sutis, automáticas e invisíveis de vigilância, adestramento e controle algorítmico, capacitando-os a defender intransigentemente os direitos civis e o império da lei democrática contra a normalização do arbítrio do estado de exceção e a desumanização de vidas vulneráveis convertidas em descarte.",
        "Estabelecendo a obrigatoriedade da inclusão de línguas francesas e italianas arcaicas nos vestibulares nacionais.",
        "Comprovando que as transformações políticas contemporâneas perdem o sentido diante do avanço de tecnologias fabris.",
        "Exigindo que os concluintes do ensino médio façam votos de silêncio e renúncia a tecnologias de informação.",
        "B",
        "- **Etapa 1:** Municiar o estudante com o bisturi foucaultiano: enxergar o poder não apenas no palácio ou na viatura, mas nas telas do celular, nas academias, nas normas silenciosas e nas instituições que moldam nossos desejos e comportamentos cotidianos.\n- **Etapa 2:** Despertar a vigilância ética agambeniana: nunca aceitar que a segurança ou a emergência sirvam de desculpa para suspender a constituição e transformar seres humanos vulneráveis (periferias, imigrantes, dissidentes) em vida nua matável; defender uma sociedade onde toda vida humana seja plena de direitos, voz e dignidade política."
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
        "hermenêutic", "mormente", "precípu", "R$"
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
    linhas.append('capitulo: "Capítulo 21: Poder, Disciplina e Biopolítica: Foucault e Agamben"')
    linhas.append('objeto_de_conhecimento: "A microfísica do poder, o poder disciplinar e o panóptico em Foucault, a biopolítica e a governamentalidade, a vida nua (zoé vs. bíos), o Homo Sacer e o estado de exceção em Giorgio Agamben"')
    linhas.append('ebook_fonte: "em-fil-c21-poder-disciplina-biopolitica-foucault-agamben.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: Poder, Disciplina e Biopolítica: Foucault e Agamben\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-21-poder-disciplina-biopolitica-foucault-agamben -->"
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
    linhas.append("- FOUCAULT, Michel. *Vigiar e punir: nascimento da prisão*. Tradução de Raquel Ramalhete. Petrópolis: Vozes, 2014.")
    linhas.append("- FOUCAULT, Michel. *Em defesa da sociedade: curso no Collège de France (1975-1976)*. Tradução de Maria Ermantina Galvão. São Paulo: Martins Fontes, 1999.")
    linhas.append("- AGAMBEN, Giorgio. *Homo Sacer: o poder soberano e a vida nua I*. Tradução de Henrique Burigo. Belo Horizonte: Editora UFMG, 2002.")
    linhas.append("- AGAMBEN, Giorgio. *Estado de exceção*. Tradução de Iraci D. Poleti. São Paulo: Boitempo, 2004.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Salvar em temp_draft.md
    with open("temp_draft.md", "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em temp_draft.md ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador Educamob
    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-21-poder-disciplina-biopolitica-foucault-agamben/ebooks/em-fil-c21-poder-disciplina-biopolitica-foucault-agamben-exercicios.md"
    comando = f"{sys.executable} validador_educamob.py temp_draft.md {destino_final}"
    print(f"Executando validador: {comando}")
    res = subprocess.run([sys.executable, "validador_educamob.py", "temp_draft.md", destino_final], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode != 0:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)
    else:
        print("\n[SUCESSO TOTAL] Cap 21 validado e homologado com Exit Code 0!")

if __name__ == "__main__":
    main()
