# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 29 de Filosofia EM:
Indústria Cultural: Adorno e Horkheimer
Objeto: cap-29-industria-cultural-adorno-horkheimer
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
        "Em qual obra de 1944 Theodor W. Adorno e Max Horkheimer forjaram o célebre conceito de 'Indústria Cultural'?",
        "Em A Ideologia Alemã, que analisa as primeiras teses do materialismo histórico.",
        "Em Dialética do Esclarecimento, no capítulo dedicado à mistificação das massas.",
        "Em O Capital, na seção voltada para a mais-valia absoluta nas fábricas.",
        "Em Crítica da Razão Pura, que investiga as formas a priori da sensibilidade espacial.",
        "Em Admirável Mundo Novo, romance ficcional focado na manipulação genética estatal.",
        "B",
        "Dialética do Esclarecimento (1944) foi redigida no exílio nos Estados Unidos, diagnosticando como a cultura foi convertida em engrenagem capitalista de padronização e lucro."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Por que Adorno e Horkheimer recusaram deliberadamente o termo 'cultura de massas' ao criarem o conceito de Indústria Cultural?",
        "Porque pretendiam demonstrar que as massas urbanas eram compostas unicamente por colecionadores de moedas antigas.",
        "Porque o termo sugeria falsamente que se tratava de uma cultura brotada do povo, quando na verdade era uma produção industrial fabricada de cima para baixo por monopólios corporativos.",
        "Porque as leis eleitorais da Alemanha de Weimar proibiam o uso da palavra massa em títulos de publicações acadêmicas.",
        "Porque os fundadores da Escola de Frankfurt consideravam que as fábricas têxteis produziam peças de vestuário artesanais.",
        "Porque a expressão massa era utilizada com exclusividade por tratados de panificação e moagem de farinha de trigo.",
        "B",
        "Cultura popular vem do povo; indústria cultural vem dos grandes monopólios de entretenimento que impõem produtos padronizados para faturar alto e apaziguar a mente do público."
    ))

    questoes_brutas.append((
        3, "EM13CHS301", "basico",
        "Qual é a lógica econômica capitalista que governa o funcionamento da Indústria Cultural segundo a Teoria Crítica?",
        "A partilha voluntária de todos os bens materiais produzidos em cooperativas de trabalhadores rurais.",
        "A submissão integral da criação estética às leis de mercado, visando o lucro financeiro máximo e a supremacia do valor de troca.",
        "A proibição compulsória da cobrança de ingressos em espetáculos teatrais e sessões cinematográficas.",
        "A substituição do papel-moeda por escambos de sacos de cereais em feiras municipais públicas.",
        "A distribuição gratuita de aparelhos de rádio valvulados financiada por doações paroquiais beneditinas.",
        "B",
        "A indústria cultural fabrica músicas e filmes como se fossem sabonetes ou carros em linha de montagem: o que importa é o lucro, a bilheteria e a conversão de tudo em mercadoria de consumo rápido."
    ))

    questoes_brutas.append((
        4, "EM13CHS302", "basico",
        "Como se caracteriza o mecanismo estrutural da 'Padronização' (Standardization) na produção de bens culturais?",
        "Pela elaboração de obras enigmáticas e complexas que exigem semanas de estudo e reflexão filosófica.",
        "Pela aplicação repetitiva de fórmulas pré-fabricadas e clichês previsíveis que poupam o consumidor de qualquer esforço mental.",
        "Pela exigência de que todos os romances literários utilizem encadernações manuais em couro legítimo.",
        "Pelo sorteio público de roteiros cinematográficos entre os trabalhadores mais antigos de estúdios.",
        "Pela proibição do uso de instrumentos eletrônicos em gravações fonográficas comerciais.",
        "B",
        "As músicas e séries pop seguem receitas prontas de bolo: conflito fácil, refrão grudento repetido e final feliz mastigado; o cérebro do consumidor descansa passivo sem precisar pensar."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "O que significa o conceito de 'Pseudo-Individualidade' utilizado por Adorno para desmascarar o catálogo da indústria do entretenimento?",
        "A obrigatoriedade de adoção de pseudônimos artísticos por cantores que gravam discos de jazz.",
        "A criação de variações cosméticas e superficiais entre os produtos para dar a ilusão de novidade e escolha a mercadorias idênticas.",
        "A realização de censuras ministeriais aos roteiros teatrais para proteger segredos de Estado militar.",
        "O controle metrológico de chapas fotográficas por peritos de departamentos de polícia civil.",
        "A distribuição de números de matrícula fiscal a todos os espectadores de sessões de cinema.",
        "B",
        "Muda a cor do cabelo do herói ou o modelo do carro na cena de ação, mas o filme é rigorosamente igual ao anterior; a pseudo-individualidade é a ilusão de variedade para disfarçar o mesmo padrão."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "O que ocorre com a percepção estética musical naquilo que Adorno denominou de 'Regressão da Audição'?",
        "O aprimoramento do ouvido humano para a identificação precisa de harmonias polifônicas clássicas.",
        "A atrofia da sensibilidade musical, fazendo com que o ouvinte médio exija apenas batidas uniformes e melodias simplórias de consumo infantil.",
        "A perda biológica irreparável do tímpano causada pelo ruído de caldeiras industriais a vapor.",
        "A exigência de que os maestros de concertos utilizem unicamente partituras escritas em papiro antigo.",
        "O aprendizado compulsório de técnicas de afinação de órgãos tubulares em colégios públicos.",
        "B",
        "O ouvido acostumado ao rádio comercial não aguenta três minutos de música elaborada: ele quer refrão fácil e batida mecânica pronta; a sensibilidade regride e fica preguiçosa."
    ))

    questoes_brutas.append((
        7, "EM13CHS301", "basico",
        "Qual é o significado da célebre máxima de Adorno e Horkheimer 'Divertir-se significa estar de acordo'?",
        "Que as piadas de comédias teatrais devem ser aprovadas previamente por conselhos consultivos de bairros.",
        "Que o entretenimento alienado ensina o sujeito a esquecer as injustiças reais, rir do conformismo e aceitar a ordem opressiva vigente.",
        "Que os ingressos para espetáculos de circo garantiam descontos fiscais sobre compras de alimentos básicos.",
        "Que as plateias dos cinemas deviam aplaudir de pé a execução do hino nacional antes das projeções.",
        "Que os trabalhadores assalariados eram proibidos de sorrir durante o cumprimento de suas jornadas em fábricas.",
        "B",
        "O divertimento da indústria cultural é o calmante da exploração: a pessoa ri da piada tosca, esquece que o salário não dá para o aluguel e volta para a fábrica resignada na segunda-feira."
    ))

    questoes_brutas.append((
        8, "EM13CHS302", "basico",
        "De que modo o lazer e o tempo livre na sociedade administrada atuam como 'prolongamento do trabalho alienado'?",
        "Obrigando os operários a realizarem tarefas de manutenção mecânica de tornos mecânicos durante seus domingos.",
        "Estruturando o divertimento como um processo mecanizado e passivo cujo único fim é reciclar a força de trabalho para a próxima jornada fabril.",
        "Exigindo que os fins de semana sejam dedicados ao estudo de manuais de contabilidade de empresas comerciais.",
        "Proibindo o descanso domiciliar para estimular a frequência compulsória a praças esportivas municipais.",
        "Determinando que os cidadãos prestem relatórios semanais sobre suas atividades de lazer a fiscais do trabalho.",
        "B",
        "O lazer não é liberdade real: é uma pausa calculada para a máquina humana esfriar os circuitos; a pessoa consome o produto pré-digerido da tela para no dia seguinte aguentar mais oito horas de labuta."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "Como Adorno define a categoria sociológica e pedagógica de 'Semiformação' (Halbbildung)?",
        "O desconhecimento total da linguagem escrita por camponeses que vivem em comunidades florestais isoladas.",
        "A apropriação superficial, apressada e fragmentada de migalhas culturais e slogans mastigados, acompanhada da ilusão arrogante de saber tudo.",
        "A conclusão de cursos profissionalizantes de marcenaria sem a obtenção de certificados sindicais oficiais.",
        "A interrupção involuntária de estudos universitários em decorrência de convocações para serviços militares de infantaria.",
        "A recusa de estudantes secundaristas em memorizar datas de batalhas coloniais em provas escolares de história.",
        "B",
        "Semiformação não é ignorância pura: é a perversão do conhecimento; é quem lê resumo de três minutos na internet, decora jargões de autoajuda e se acha sábio para destilar preconceitos nas redes."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Qual é a diferença entre o ideal humanista de formação (Bildung) e a semiformação (Halbbildung) denunciada por Adorno?",
        "Bildung exige a posse de títulos nobiliares de cortes e Halbbildung refere-se ao estudo de línguas clássicas mortas.",
        "Bildung é o cultivo integral e crítico da mente autônoma e empática, enquanto Halbbildung é a assimilação de clichês para ostentação social e preconceito.",
        "Bildung destina-se exclusivamente a comerciantes de cidades portuárias e Halbbildung a operários de fábricas químicas.",
        "Bildung foi inventada por comissões de higiene militar e Halbbildung por congregações religiosas medievais.",
        "Bildung e Halbbildung são termos sinônimos utilizados indiferentemente por manuais de direito civil alemão.",
        "B",
        "Bildung educa o indivíduo para ser livre, ter compaixão e pensar com a própria cabeça; a semiformação transforma a cultura em produto de vitrine e slogan raso para alimentar a arrogância vazia."
    ))

    questoes_brutas.append((
        11, "EM13CHS301", "basico",
        "Quais características definem a 'Arte Autônoma' defendida por Adorno como o único refúgio de resistência contra a indústria cultural?",
        "A facilidade melódica, a simpatia comercial imediata e o desfecho consolador para agradar famílias nos fins de semana.",
        "A dissonância enigmática, a recusa radical do entretenimento fácil e a recusa em se converter em mercadoria amigável de consumo.",
        "O financiamento compulsório de suas produções por grandes corporações bancárias de investimento em Wall Street.",
        "A utilização de instrumentos musicais confeccionados unicamente com fibras vegetais da floresta tropical úmida.",
        "A aprovação prévia concedida por tabelionatos municipais de registros de títulos e documentos públicos.",
        "B",
        "A grande arte não faz cócegas nem bajula o público: ela é difícil (como Kafka ou Schoenberg), incomoda, é dissonante e berra contra a injustiça do mundo, recusando a coleira do mercado."
    ))

    questoes_brutas.append((
        12, "EM13CHS302", "basico",
        "Como os algoritmos contemporâneos de recomendação de plataformas de streaming (como o Spotify) atualizam a padronização adorniana?",
        "Oferecendo ao usuário músicas que desafiam suas preferências para forçá-lo a aprender história da ópera barroca italiana.",
        "Criando bolhas de consumo que entregam continuamente faixas idênticas às já escutadas, atrofiando o contato com a diversidade e o estranhamento.",
        "Bloqueando o acesso de ouvintes menores de idade a composições musicais gravadas em estúdios independentes.",
        "Exigindo que os assinantes de serviços digitais realizem testes de solfejo musical a cada trimestre de contrato.",
        "Distribuindo instrumentos sonoros de madeira aos consumidores que registram mais de cinquenta horas de audição mensal.",
        "B",
        "O algoritmo calcula o que você acabou de ouvir e joga mais dez músicas iguaizinhas em seguida; ele fecha o ouvinte numa bolha de mesmice lucrativa onde nada novo ou dissonante pode entrar."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "De que modo a indústria contemporânea do cinema de franquias e super-heróis personifica as críticas de Dialética do Esclarecimento?",
        "Produzindo filmes com roteiros filosóficos abertos que estimulam o debate ético sobre as contradições do capitalismo financeiro.",
        "Reciclando fórmulas dramatúrgicas previsíveis com piadas padronizadas a cada dez minutos para vender bonecos e produtos de merchandising corporativo.",
        "Obrigando os espectadores a permanecerem de olhos vendados durante a execução de trilhas sonoras instrumentais orquestrais.",
        "Eliminando o uso de efeitos especiais computadorizados para valorizar o trabalho manual de carpinteiros de cenários de estúdio.",
        "Destinando a totalidade dos lucros obtidos com bilheterias mundiais para a construção de habitações populares na periferia.",
        "B",
        "O filme de super-herói atual é o auge da indústria cultural: fórmula idêntica há 20 anos, piadinha a cada dez minutos para quebrar o drama e o objetivo real de vender brinquedo e lanche de fast-food."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Como a cultura das redes sociais com coaches que prometem 'ficar milionário em cinco passos' ilustra o fenômeno da semiformação?",
        "Incentivando os trabalhadores assalariados a cursarem faculdades de direito para exigir cumprimento de convenções sindicais coletivas.",
        "Reduzindo tradições filosóficas densas a slogans motivacionais toscos que mascaram a precarização trabalhista como suposto empreendedorismo individual.",
        "Exigindo que os usuários de plataformas virtuais leiam as obras completas de Aristóteles e Immanuel Kant em suas línguas originais.",
        "Determinando que os criadores de conteúdos de internet sejam fiscalizados semanalmente por comissões disciplinares de infantaria.",
        "Proibindo o uso de termos estrangeiros em postagens dedicadas à educação financeira de jovens estudantes secundaristas.",
        "B",
        "Pegam o estoicismo ou a filosofia grega, arrancam as páginas que falam de justiça e viram um manual de autoajuda barata para o jovem aceitar ser explorado sem direitos achando que é 'tubarão'."
    ))

    questoes_brutas.append((
        15, "EM13CHS301", "basico",
        "Qual foi o verdadeiro alvo da crítica de Theodor Adorno ao 'jazz comercial' dos anos 1930 e 1940 nos Estados Unidos?",
        "O preconceito racial contra a herança musical e as raízes do blues desenvolvidas pelas comunidades afro-americanas.",
        "A apropriação predatória da música popular pela indústria radiofônica comercial branca que pasteurizou o improviso livre em clichês mecânicos para o lucro corporativo.",
        "A presença de instrumentos de sopro de metal em orquestras sinfônicas dedicadas à execução de marchas cívicas nacionais.",
        "O volume sonoro elevado dos concertos musicais que provocava incômodos a vizinhanças de bairros residenciais abastados.",
        "A recusa dos músicos populares em registrarem suas composições autorais em tabelionatos públicos de títulos e patentes.",
        "B",
        "Adorno não tinha raiva do povo negro: ele tinha indignação de ver o blues e o jazz vivos serem capturados pelos barões do rádio de Nova York, que transformaram aquela dor sagrada em jingle de refrigerante."
    ))

    questoes_brutas.append((
        16, "EM13CHS302", "basico",
        "Por que é incorreto identificar a 'Indústria Cultural' com a existência física dos aparelhos de rádio, televisão ou câmeras em si?",
        "Porque os dispositivos de comunicação eletrônica foram declarados patrimônios da humanidade por convenções diplomáticas navais.",
        "Porque a indústria cultural não é o maquinário técnico em si, mas o modo de produção capitalista que o coloniza para transformar bens simbólicos em mercadorias de alienação.",
        "Porque as tecnologias de telecomunicações eram fabricadas exclusivamente por cooperativas operárias de autogestão solidária.",
        "Porque o termo indústria cultural refere-se unicamente ao setor de mineração de cobre e fundição de ligas para cabos elétricos.",
        "Porque os pensadores de Frankfurt consideravam que a televisão utilizava circuitos que impediam a manipulação psicológica dos telespectadores.",
        "B",
        "A televisão, a câmera ou o computador são apenas máquinas: poderiam servir para ensinar e libertar; o que faz deles 'indústria cultural' é o dono da empresa que manda no conteúdo para lucrar e alienar."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Por que, para Adorno, um acadêmico hiperespecializado com pós-doutorado pode personificar o ápice da 'Semiformação'?",
        "Porque ele desconhece as normas técnicas de catalogação bibliográfica de manuscritos em arquivos públicos de capitais.",
        "Porque ele pode dominar técnicas científicas complexas e, simultaneamente, ser moralmente complacente com o racismo, preconceitos autoritários e ideologias fascistas.",
        "Porque a legislação educacional da República de Weimar proibia a concessão de diplomas a pesquisadores de ciências exatas.",
        "Porque os doutores de universidades européias eram obrigados a exercer tarefas agrícolas temporárias durante períodos de colheita.",
        "Porque o exercício da docência em instituições superiores dependia de autorização formal expedida por comissões de marinha.",
        "B",
        "Ter diploma na parede não imuniza ninguém contra a estupidez: o cientista que calculava o gás em Auschwitz era um pós-doutor técnico que não tinha humanidade nenhuma; é a semiformação letrada."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "Qual pesquisa empírica de grande relevância psicossocial foi liderada por Adorno nos Estados Unidos no ano de 1950?",
        "A mensuração do nível de ruído em fábricas automobilísticas da cidade de Detroit durante o turno da madrugada.",
        "O estudo sobre A Personalidade Autoritária, investigando a Escala F e os traços neuróticos que alimentam tendências fascistas.",
        "A catalogação de espécies de fungos microscópicos que deterioravam os rolos de películas fotográficas de celulóide.",
        "O recenseamento demográfico das famílias de agricultores de trigo estabelecidas nas planícies centrais norte-americanas.",
        "A verificação do consumo calórico diário de operários da indústria de conservas de pescado no litoral da Califórnia.",
        "B",
        "Adorno liderou o estudo 'A Personalidade Autoritária' (com a Escala F para fascismo), provando cientificamente que a semiformação e a repressão geram sujeitos submissos ao chefe e agressivos contra minorias."
    ))

    questoes_brutas.append((
        19, "EM13CHS301", "basico",
        "Como a teoria dos 'Estudos Culturais de Birmingham' (Stuart Hall) complementa e tensiona a visão frankfurtiana da indústria cultural?",
        "Propondo a destruição de todas as salas de cinema comunitárias para incentivar a prática de esportes ao ar livre em parques municipais.",
        "Demonstrando através do modelo de codificação e decodificação que o público popular não é passivo, sendo capaz de leituras negociadas e subversivas das mensagens dominantes da mídia.",
        "Afirmando que a indústria cultural foi inventada por corporações mercantis de navegação para treinar tripulações de caravelas mercantes.",
        "Exigindo que os programas de televisão sejam gravados em dialetos arcaicos para dificultar o consumo por massas urbanas.",
        "Comprovando que as audiências populares aceitam de forma idêntica e sem qualquer resistência todo e qualquer produto da publicidade.",
        "B",
        "Stuart Hall lembra que o povo não é um saco vazio onde a TV joga o que quer: o morador da periferia pega a música da novela, muda a letra, faz funk, dança e cria resistência própria de classe e raça."
    ))

    questoes_brutas.append((
        20, "EM13CHS302", "basico",
        "Como a teoria do 'Capitalismo de Vigilância' de Shoshana Zuboff atualiza as teses de Dialética do Esclarecimento no século XXI?",
        "Comprovando que as empresas de tecnologia digital utilizam cabos de transmissão revestidos por cerâmicas refratárias de alto custo.",
        "Demonstrando que conglomerados como Meta e Google convertem as emoções, cliques e a atenção dos usuários em dados comportamentais monetizados em leilões publicitários bilionários.",
        "Exigindo que todos os usuários de redes virtuais façam doações monetárias semanais para fundações filantrópicas de pesquisa espacial.",
        "Provando que a circulação de mensagens eletrônicas é monitorada por comissões de generais reformados da infantaria naval.",
        "Determinando que os algoritmos de recomendação devam operar unicamente durante os períodos diurnos para economizar energia elétrica.",
        "B",
        "Zuboff mostra o estágio final de Adorno: a indústria cultural agora não vende só o filme; ela rouba a sua atenção, as suas curtidas e as suas lágrimas no celular para leiloar o seu futuro na bolsa de valores."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "De que maneira o conceito de 'Razão Instrumental' explica a regressão civilizatória analisada por Adorno e Horkheimer na primeira metade do século XX?",
        "Evidenciando que a Razão abandonou a reflexão crítica sobre os fins éticos da humanidade (justiça, liberdade, felicidade) para se degradar em mero cálculo técnico utilitário de eficácia, permitindo que a ciência mais avançada servisse à administração da barbárie em Auschwitz.",
        "Provando que os cientistas da era moderna utilizavam reagentes químicos de baixa qualidade na purificação de compostos minerais.",
        "Demonstrando que os tribunais de inquisição medievais foram os criadores dos primeiros manuais de contabilidade de fábricas de tecidos.",
        "Afirmando que a decadência do Iluminismo decorreu da substituição do carvão vegetal pelo óleo mineral na iluminação pública de capitais.",
        "Determinando que os filósofos da Escola de Frankfurt deviam apresentar certidões de antecedentes cívicos a ministérios do interior.",
        "A",
        "A razão virou cálculo cego: ela não pergunta 'isso é justo?', só pergunta 'como produzir mais rápido e mais barato?'; quando a razão vira instrumento cego, ela calcula tanto uma vacina quanto as câmaras de gás."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Como a mercadorização da arte opera o 'esvaziamento do seu valor de uso' em benefício absoluto do 'valor de troca' no mercado cultural?",
        "A obra deixa de ser apreciada pela sua capacidade singular de despertar reflexão e transformação interior para ser valorizada pelo seu preço monetário, número de cópias vendidas e posição no topo das paradas comerciais.",
        "Os pintores clássicos foram proibidos de aplicar vernizes sobre telas de linho por determinação de corporações de artesãos.",
        "As partituras musicais passaram a ser impressas em papéis especiais à prova de fogo importados de cidades do mar Báltico.",
        "As galerias comerciais de arte tornaram-se instituições de caridade dedicadas exclusivamente ao atendimento de desabrigados urbanos.",
        "Os governos democráticos estabeleceram tabelas compulsórias de preços fixos para todas as peças de escultura em mármore.",
        "A",
        "O consumidor não ouve a música porque ela é profunda; ele ouve porque 'tem 1 bilhão de views no YouTube e é a número 1 no Spotify!'; o sucesso financeiro engoliu a experiência estética da obra."
    ))

    questoes_brutas.append((
        23, "EM13CHS301", "intermediario",
        "Em que sentido a comédia comercial da indústria cultural promove o que Adorno chama de 'reconciliação cínica com a desgraça alheia'?",
        "Ao estimular o riso diante de personagens desastrados que levam bordoadas ou tropeçam na lama, o espetáculo acostuma o público a rir do sofrimento alheio e a aceitar que a dor é natural e que os fracos merecem ser humilhados.",
        "Ao exigir que os espectadores façam doações em moedas de cobre para asilos de idosos ao término de cada ato encenado no teatro.",
        "Ao transformar as salas de espetáculos em salas de julgamento público onde o público elege novos magistrados cívicos municipais.",
        "Ao demonstrar que as comédias populares foram redigidas por generais militares para treinar soldados no combate a motins.",
        "Ao proibir a utilização de figurinos engraçados por comediantes profissionais em festivais patrocinados por órgãos públicos.",
        "A",
        "Na comédia pastelão, o pobre leva uma torta na cara ou apanha do guarda e o público dá gargalhada; o riso da indústria cultural é sádico: ensina que quem apanha é bobo e que quem manda é quem tem razão."
    ))

    questoes_brutas.append((
        24, "EM13CHS302", "intermediario",
        "Como a tese da 'Semiformação' (Halbbildung) explica a facilidade com que multidões aderem a teorias da conspiração e discursos de ódio nas redes digitais?",
        "O indivíduo semiformado assimila fragmentos desconexos de informações sem método crítico; possuindo a ilusão arrogante de saber a verdade que a ciência supostamente oculta, ele canaliza sua angústia e impotência social na busca de bodes expiatórios fáceis.",
        "A adesão a notícias falsas decorre exclusivamente da ingestão continuada de alimentos industrializados com conservantes químicos.",
        "As teorias conspiratórias foram elaboradas por companhias mercantis de seguros marítimos para desestimular viagens de navios.",
        "O ódio digital foi criado por regulamentos disciplinares militares da Prússia para treinar regimentos de infantaria montada.",
        "A circulação de mentiras na internet foi proibida por decretos imperiais aprovados em convenções internacionais de telegrafia.",
        "A",
        "O sujeito semiformado viu um vídeo de três minutos no YouTube e acha que desmascarou toda a medicina e a física; como não tem método e tem medo do mundo, ele abraça a mentira fácil que culpa as minorias por sua vida ruim."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Por que as produções da 'Arte Autônoma' (como as composições atonais de Arnold Schoenberg) são consideradas insuportáveis pela indústria cultural?",
        "Porque ao recusarem melodias fáceis, ritmos dançantes e resoluções harmônicas consoladoras, elas provocam dissonância, estranhamento e desconforto, quebrando a passividade digestiva do consumidor de mercado.",
        "Porque as orquestras sinfônicas exigiam o pagamento de cachês astronômicos pagos unicamente em barras de ouro fundido.",
        "Porque os partituras atonais foram banidas por conselhos de medicina veterinária em razão de ruídos que assustavam cavalos.",
        "Porque a música de vanguarda foi declarada propriedade exclusiva de ministérios de defesa para uso em exercícios de artilharia.",
        "Porque os compositores da Segunda Escola de Viena recusavam-se a conceder entrevistas a jornais diários de grande circulação.",
        "A",
        "A música atonal de Schoenberg não serve para tocar no elevador nem para virar dancinha no TikTok; ela machuca o ouvido acomodado e obriga a mente a acordar para o horror e o enigma da nossa época."
    ))

    questoes_brutas.append((
        26, "EM13CHS102", "intermediario",
        "Qual é o impacto da 'Indústria Cultural' sobre a capacidade de imaginação autônoma das crianças e jovens contemporâneos?",
        "Ao entregar imagens prontas, enredos milimetricamente fechados e produtos de merchandising pré-fabricados, ela atrofia a capacidade da criança de criar suas próprias fantasias, submetendo o brincar ao consumo de mercadorias da moda.",
        "A exposição a desenhos animados estimula o aprendizado compulsório de gramática latina clássica em escolas maternais.",
        "Os fabricantes de brinquedos de plástico utilizavam resinas minerais que aumentavam a densidade óssea dos estudantes menores.",
        "As crianças das grandes metrópoles foram obrigadas a realizar estágios voluntários em ateliês de gravura e litografia manual.",
        "Os desenhos infantis foram classificados por tribunais consulares marítimos como documentos de interesse de frotas mercantes.",
        "A",
        "A criança de hoje não pega um toco de madeira para inventar um navio pirata com a imaginação livre: ela ganha o boneco oficial do filme do cinema já com a roupa pronta e a fala programada; o mercado matou a fantasia."
    ))

    questoes_brutas.append((
        27, "EM13CHS301", "intermediario",
        "De que modo a indústria cultural converte o 'Sofrimento Humano em Auschwitz' em mero espetáculo melodramático palatável no cinema comercial?",
        "Transformando a tragédia do Holocausto em narrativas comoventes de heroísmo individual com finais moralmente reconfortantes, permitindo que a plateia chore lágrimas purificadoras sem enfrentar a cumplicidade do sistema social com a barbárie.",
        "Obrigando os estúdios cinematográficos a doarem rolos de películas antigas para a queima em fornos de padarias comunitárias.",
        "Substituindo todos os atores profissionais por sobreviventes idosos de campos de concentração em produções ficcionais.",
        "Proibindo a filmagem de cenas dramáticas durante os períodos do ano em que se realizam festividades cívicas patrióticas.",
        "Exigindo que os filmes sobre conflitos bélicos utilizem unicamente trilhas sonoras compostas por instrumentos de percussão leve.",
        "A",
        "O cinemão de Hollywood pega o horror de Auschwitz e faz um filme lacrimejante com trilha de violino e final esperançoso; a pessoa chora no cinema, come pipoca e vai para casa aliviada achando que o monstro ficou no passado."
    ))

    questoes_brutas.append((
        28, "EM13CHS302", "intermediario",
        "Como a noção de 'Emancipação' (Mündigkeit) no pensamento de Adorno se vincula à tarefa primordial da Educação contra a barbárie?",
        "Adorno sustenta em Educação após Auschwitz que a escola pública tem como dever supremo educar para a autorreflexão crítica e desobediência a ordens desumanas, impedindo a formação de personalidades fascistas subservientes.",
        "O filósofo defendia que a formação escolar devesse priorizar unicamente a memorização mecânica de regras gramaticais clássicas.",
        "A emancipação foi definida como a obrigatoriedade de alistamento de todos os jovens em academias de cavalaria de infantaria.",
        "Adorno propôs a extinção de todas as instituições de ensino fundamental para reduzir despesas de orçamentos municipais.",
        "A educação emancipatória dependia de certidões de idoneidade moral expedidas por corporações mercantis de transporte fluvial.",
        "A",
        "Em 'Educação após Auschwitz', Adorno cravou: a primeira tarefa da educação é fazer com que Auschwitz nunca mais se repita! E isso se faz ensinando o aluno a dizer 'NÃO!' aos chefes tiranos e a pensar com autonomia."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "Por que, para Adorno e Horkheimer, o consumidor da indústria cultural 'não é o rei do mercado, mas o seu objeto inerte'?",
        "Porque embora a propaganda faça o consumidor acreditar que tudo foi feito para agradar aos seus desejos particulares, na verdade suas vontades e preferências foram previamente calculadas e fabricadas pelas engrenagens de marketing corporativo.",
        "Porque os cidadãos das repúblicas democráticas foram destituídos de seus direitos de propriedade imobiliária rural.",
        "Porque os fabricantes de discos de vinil utilizavam contratos comerciais registrados em alfândegas de cidades litorâneas.",
        "Porque o consumo de bens culturais dependia de autorizações concedidas por associações de médicos veterinários.",
        "Porque os estúdios cinematográficos eram administrados por descendentes de famílias nobiliárquicas da Prússia ocidental.",
        "A",
        "Você acha que escolheu a música que está ouvindo no fone? A indústria pesquisou o seu perfil, padronizou a fórmula e enfiou a música na sua cabeça; você não manda nada no mercado: você é a presa calculada por eles."
    ))

    questoes_brutas.append((
        30, "EM13CHS102", "intermediario",
        "Como a difusão de 'podcasts e vídeos curtos de resumos filosóficos' atualiza a profecia de Adorno sobre a degradação da cultura em bens de consumo rápido?",
        "Ao prometer entregar em dez minutos o conteúdo de obras que exigiram a vida inteira de um autor, ela mastiga a complexidade e produz a falsa certeza de conhecimento, eliminando a experiência da leitura paciente e do pensamento dialético.",
        "Ao demonstrar que as mídias sonoras transmitem ondas magnéticas que revitalizam a circulação sanguínea de ouvintes idosos.",
        "Ao exigir que os locutores de rádio devessem prestar juramentos de obediência perante congregações paroquiais de monges.",
        "Ao substituir todas as livrarias físicas por armazéns de estocagem de cereais agrícolas durante estações de seca.",
        "Ao determinar que os autores clássicos devessem ser reescritos em linguagem poética por comissões de generais navais.",
        "A",
        "O sujeito ouve 'Nietzsche em 5 minutos' lavando a louça e acha que entendeu a genealogia da moral; isso é a pura semiformação: o esforço de pensar foi substituído por uma pílula mastigada que não transforma ninguém."
    ))

    questoes_brutas.append((
        31, "EM13CHS301", "intermediario",
        "De que modo a publicidade comercial coloniza a vida cotidiana na sociedade administrada segundo a Teoria Crítica?",
        "A propaganda deixa de ser um mero anúncio informativo sobre as qualidades técnicas do produto para se tornar o padrão estético onipresente que dita estilos de vida, condutas morais, tipos de beleza e valores ideológicos para toda a coletividade.",
        "Os anúncios publicitários foram proibidos em vias públicas para evitar a distração de condutores de carruagens a cavalos.",
        "As marcas comerciais utilizavam caracteres tipográficos gravados exclusivamente em placas de bronze polido por artesãos.",
        "A publicidade dependia de autorizações expedidas por magistrados eclesiásticos em conferências diplomáticas de paz.",
        "Os cartazes ilustrados eram destruídos semanalmente por corporações de sapateiros para conter o acúmulo de papéis.",
        "A",
        "A publicidade hoje não diz se o sabão lava bem: ela vende um estilo de vida, diz quem é bonito, quem é bem-sucedido e como você deve se comportar; a publicidade virou a religião silenciosa da sociedade capitalista."
    ))

    questoes_brutas.append((
        32, "EM13CHS302", "intermediario",
        "Qual é a relação entre a 'Crítica do Iluminismo' em Adorno e a advertência contra a barbárie tecnológica no século XXI?",
        "A Teoria Crítica lembra que o avanço tecnológico desprovido de vigilância ética emancipatória não garante o progresso humano, podendo ser utilizado para aprimorar a vigilância algorítmica, a censura e a opressão de massas com eficácia sem precedentes.",
        "Os pensadores de Frankfurt defendiam o retorno compulsório ao modo de vida feudal camponês sem uso de eletricidade.",
        "A Escola de Frankfurt propunha a destruição de todas as universidades técnicas para preservar o estudo de teologia clássica.",
        "A crítica à razão instrumental foi formulada para justificar o monopólio comercial de companhias mercantis de sal marinho.",
        "Os filósofos críticos sustentavam que as máquinas a vapor possuíam almas conscientes dotadas de vontade e paixões.",
        "A",
        "Ter celular com 5G e inteligência artificial não nos faz mais sábios: se a razão for apenas instrumento cego de lucro e controle, ela cria a sociedade da vigilância total; a tecnologia sem ética vira barbárie com alta resolução."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Como a obra literária de Franz Kafka e Samuel Beckett encarna a 'Arte Autônoma' que resiste à indústria cultural?",
        "Expondo a angústia existencial, o absurdo das burocracias opressivas e a incomunicabilidade humana através de formas fragmentadas e enigmáticas que recusam finais felizes conciliadores e falsos consolos de mercado.",
        "Escrevendo folhetins cômicos para circulação gratuita em estações de trens urbanos patrocinados por companhias têxteis.",
        "Submetendo seus manuscritos literários à aprovação de comissões formadas por oficiais da infantaria armada prussiana.",
        "Produzindo romances comerciais destinados a alavancar a venda de passagens ferroviárias para regiões de montanhas.",
        "Utilizando unicamente tipografias mecânicas fundidas em ligas de chumbo fornecidas por guildas de ferreiros medievais.",
        "A",
        "Kafka (com o homem que vira inseto) e Beckett (com os mendigos esperando Godot que nunca chega) mostram a ferida da nossa vida sem maquiagem; eles não dão final feliz para agradar o leitor: mostram o abismo da realidade."
    ))

    questoes_brutas.append((
        34, "EM13CHS102", "intermediario",
        "De que maneira a 'Escala F' utilizada na pesquisa sobre A Personalidade Autoritária identificava traços de submissão cega nas sociedades democráticas?",
        "Medindo a concordância com afirmações que revelavam adoração incontestável por líderes fortes, aversão à reflexão introspectiva, ódio contra desviantes das normas e tendência a enxergar o mundo em termos de violência e conspirações.",
        "Avaliando a aptidão física de voluntários através de testes de corrida e saltos sobre cavaletes de madeira em estádios.",
        "Contabilizando a quantidade de livros didáticos adquiridos anualmente por famílias camponesas em feiras municipais.",
        "Verificando a frequência de comparecimento de eleitores a sessões plenárias de parlamentos estaduais e municipais.",
        "Calculando o tempo médio dedicado por operários à leitura de cartas astronômicas durante intervalos de almoço em fábricas.",
        "A",
        "A Escala F de Adorno pegava o autoritário no detalhe: quem acha que problema social se resolve na bala, que o chefe forte nunca erra, que artista é vagabundo e que a minoria tem que ser calada; a ciência desmascarou o fascista."
    ))

    questoes_brutas.append((
        35, "EM13CHS301", "intermediario",
        "Por que, para Adorno, a indústria cultural 'engana permanentemente seus consumidores a respeito daquilo que lhes promete'?",
        "Porque ela promete a felicidade, a liberdade e a aventura através do consumo de suas mercadorias, mas entrega unicamente a repetição do mesmo tédio, deixando o sujeito vazio e compelido a comprar o próximo produto na vã esperança de preenchimento.",
        "Porque os ingressos de espetáculos dramáticos continham erros de impressão tipográfica cometidos por linotipistas inexperientes.",
        "Porque os discos de vinil comercializados em lojas de conveniência apresentavam defeitos de fabricação em suas trilhas de áudio.",
        "Porque as salas de exibição cinematográfica eram fechadas antes do encerramento das histórias por ordem de autoridades sanitárias.",
        "Porque os contratos de prestação de serviços de telecomunicações eram redigidos em dialetos germânicos arcaicos e ilegíveis.",
        "A",
        "A indústria cultural vende o sonho e entrega o vento: ela promete que com aquele tênis, aquela série ou aquele celular você será pleno e livre; você consome, a euforia dura dez minutos, o vazio volta e você é forçado a comprar de novo."
    ))

    questoes_brutas.append((
        36, "EM13CHS302", "intermediario",
        "Como a homogeneização dos gostos pela indústria cultural ameaça a sobrevivência das manifestações culturais tradicionais e folclóricas autênticas?",
        "Substituindo o artesanato, os cantos comunitários e as festas de raiz que expressavam a memória viva dos territórios por produtos padronizados pela mídia comercial, erodindo a diversidade cultural em favor de mercadorias globais uniformes.",
        "Obrigando os mestres artesãos a utilizarem ligas metálicas importadas de minas de extração de ferro na Austrália.",
        "Exigindo que os grupos folclóricos registrem suas danças ancestrais em tabelionatos de patentes industriais da capital.",
        "Proibindo o uso de instrumentos de percussão de madeira em festividades realizadas em vilarejos do interior.",
        "Determinando que as festas comunitárias sejam supervisionadas por comissões de engenharia civil e tráfego urbano.",
        "A",
        "O maracatu e o reisado do interior são engolidos pelo hit sertanejo universitário genérico fabricado em estúdio; a riqueza viva das raízes do povo é esmagada pela bota da música comercial padronizada que toca em toda rádio."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Em que medida a crítica da Indústria Cultural preserva o legado do 'Fetichismo da Mercadoria' de Karl Marx no terreno das criações do espírito humano?",
        "Demonstrando que, assim como as mercadorias materiais ocultam as relações sociais de exploração humana que as produziram, os produtos culturais adquirem uma existência fantasmagórica no mercado onde o sucesso monetário aparece como valor natural do objeto.",
        "Provando que a circulação de obras de arte em feiras medievais dependia de autorizações concedidas por corporações de alfaiates.",
        "Exigindo que todos os livros de teoria sociológica sejam publicados sem menção aos nomes de seus respectivos autores.",
        "Submetendo as composições musicais clássicas a cálculos de amortização de juros bancários em tabelionatos públicos.",
        "Determinando que os artistas plásticos recebam seus proventos unicamente através do fornecimento de cotas de tecidos de algodão.",
        "A",
        "Marx mostrou o fetiche da mercadoria na fábrica; Adorno mostrou o fetiche na arte: a música de sucesso parece mágica caída do céu, ocultando o esquema sujo de marketing, jabá e manipulação que a enfiou na cabeça das pessoas."
    ))

    questoes_brutas.append((
        38, "EM13CHS102", "intermediario",
        "De que modo a recusa da 'reconciliação forçada' em Teoria Estética conecta a filosofia de Adorno com a memória das vítimas da barbárie histórica?",
        "Ao defender que a arte não pode pintar mundos harmoniosos e felizes enquanto houver tortura, miséria e injustiça no planeta; a arte séria deve permanecer como uma ferida aberta que preserva a dor das vítimas contra o esquecimento cúmplice.",
        "Ao exigir que todos os monumentos fúnebres de heróis de guerra sejam esculpidos exclusivamente em pedras de granito cinza.",
        "Ao propor que as galerias de arte fechem suas instalações durante os aniversários de tratados de rendição militar de exércitos.",
        "Ao proibir a pintura de flores e jardins botânicos em ateliês de formação profissional de desenhistas técnicos.",
        "Ao determinar que as sinfonias clássicas sejam executadas com metade dos instrumentos de cordas em períodos de luto cívico.",
        "A",
        "Se o artista pinta que o mundo está lindo num planeta cheio de favelas e campos de refugiados, ele mente e vira cúmplice da dor; a grande arte tem que ser ferida aberta e grito de indignação que recusa calar a boca perante os carrascos."
    ))

    questoes_brutas.append((
        39, "EM13CHS301", "intermediario",
        "Como a teoria adorniana desmascara a ideologia do 'Faça Você Mesmo' e do 'Trabalho por Amor' difundida no capitalismo de plataforma?",
        "Demonstrando que essas narrativas românticas servem para transferir os custos operacionais e os riscos econômicos para o próprio trabalhador precarizado, transformando a autodesumanização e a jornada contínua em suposta virtude moral voluntária.",
        "Provando que as plataformas digitais foram desenvolvidas com base em estatutos de guildas artesanais da Idade Média tardia.",
        "Exigindo que os trabalhadores por aplicativos sejam obrigados a residir nas dependências físicas dos servidores de internet.",
        "Determinando que as entregas de mercadorias urbanas sejam realizadas exclusivamente através de veículos com tração animal.",
        "Afirmando que a economia de bicos foi criada para financiar expedições científicas a sítios arqueológicos no Egito.",
        "A",
        "A indústria do Vale do Silício inventou a balela do 'trabalhe com o que ama e seja seu próprio chefe' para fazer o entregador de aplicativo trabalhar 14 horas de bicicleta sem previdência social e com um sorriso no rosto."
    ))

    questoes_brutas.append((
        40, "EM13CHS302", "intermediario",
        "Por que, para Theodor Adorno, a arte autônoma contemporânea precisa 'assumir a própria feiura e o grotesco' em sua estrutura formal?",
        "Porque em um mundo falso e reconciliado na propaganda comercial, a beleza tradicional harmoniosa virou farsa de vitrine; a feiura e a dissonância na forma artística tornam-se a única maneira honesta de registrar o horror real da sociedade administrada.",
        "Porque as academias de pintura do século XX enfrentavam escassez de pigmentos coloridos claros em decorrência de bloqueios navais.",
        "Porque os críticos de arte exigiam que as exposições públicas fossem montadas em porões úmidos de prédios industriais abandonados.",
        "Porque os escultores modernos utilizavam materiais reciclados de sucatas de trens a vapor para baratear custos de transporte.",
        "Porque a legislação sanitária municipal proibia a exibição de quadros que retratassem figuras humanas com corpos sadios e bem alimentados.",
        "A",
        "Num mundo que gerou Auschwitz e a fome, fazer quadros açucarados com anjinhos loiros é mentira desonesta; a grande arte tem que chocar com o grotesco de Guernica de Picasso para lembrar o espectador da barbárie que nos cerca."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a tese central do capítulo 'A Indústria Cultural' em Dialética do Esclarecimento (1944): de que maneira Adorno e Horkheimer articulam o conceito de 'Esclarecimento que se autodestrói', demonstrando que a Razão Instrumental convertida em técnica mercantil de dominação psíquica culmina na domesticação totalitária da imaginação humana na sociedade capitalista avançada?",
        "Provando que os ateliês tipográficos norte-americanos da década de 1940 utilizavam maquinários financiados por agências de crédito rural.",
        "Evidenciando que o Iluminismo, ao prometer a libertação do medo pela Razão, restringiu o pensamento ao cálculo instrumental de utilidade e controle prático; ao penetrar na cultura, essa lógica mercantil expropriou o sujeito de sua autonomia interior: a indústria cultural fabrica produtos pré-digeridos em série que adestram a mente do consumidor para o conformismo político, fechando o círculo de ferro da sociedade totalmente administrada na qual a técnica opera como instrumento supremo de servidão voluntária.",
        "Determinando que os manuscritos da Teoria Crítica devessem ser selados com ceras especiais aprovadas por cortes consulares suíças.",
        "Afirmando que a autodestruição da razão foi uma tese inspirada em manuais de adestramento de cavalos de infantaria militar germânica.",
        "Comprovando que a crítica à indústria cultural foi redigida para subsidiar tarifas aduaneiras contra a importação de filmes franceses.",
        "B",
        "- **Etapa 1:** Compreender a traição do Iluminismo: a Razão que prometeu libertar a humanidade virou ferramenta cega de dominação que só pensa em lucro, controle e linha de montagem industrial.\n- **Etapa 2:** Revelar a prisão da mente na Indústria Cultural: quando a fábrica toma conta do cinema, da música e da literatura, a imaginação humana é formatada de fábrica; o homem consome o clichê e perde a capacidade de pensar diferente do sistema."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a engrenagem dialética entre 'Padronização' e 'Pseudo-Individualidade' nos produtos do entretenimento de massa: por que a indústria cultural necessita produzir simultaneamente a identidade estrutural e a aparência cosmética de diferença, e de que modo essa dinâmica engendra a atrofia da espontaneidade reflexiva no público consumidor?",
        "Mostrando que as companhias de gravação fonográfica utilizavam agulhas de diamante em gramofones de teste em salas fechadas.",
        "Demonstrando que a padronização assegura a rentabilidade máxima e o controle econômico através de fórmulas repetitivas já testadas no mercado, enquanto a pseudo-individualidade introduz sutis variações superficiais (trocas de batidas, penteados de heróis, cenários digitais) para enganar o consumidor com uma ilusão de novidade e livre arbítrio; esse circuito fecha as portas à experiência autêntica, condicionando a psique a reagir mecanicamente a estímulos condicionados, anestesiando a consciência crítica.",
        "Determinando que as empresas de produção cinematográfica devam limitar seus orçamentos a montantes definidos por leis tributárias municipais.",
        "Afirmando que a padronização de roteiros dramáticos foi imposta por corporações de correios e telégrafos para economizar papel de celulose.",
        "Comprovando que a variação de produtos de entretenimento dependia de autorizações concedidas por congregações religiosas paroquiais.",
        "B",
        "- **Etapa 1:** Entender a segurança do lucro na padronização: o grande estúdio não arrisca dinheiro em ideias estranhas; ele pega a mesma fórmula de sucesso que vendeu bilhões e a repete mecanicamente.\n- **Etapa 2:** Desmascarar o golpe da pseudo-individualidade: para você não notar que está comendo a mesma comida requentada, eles mudam o tempero e a embalagem; a pessoa acha que é livre para escolher entre cem séries que são rigorosamente a mesma coisa."
    ))

    questoes_brutas.append((
        43, "EM13CHS301", "dificil",
        "Investigue o diagnóstico adorniano sobre o 'Fetiche da Mercadoria na Música' e a 'Regressão da Audição': de que maneira a subordinação do valor de uso ao valor de troca transforma o aplauso do consumidor em um ato de auto-alienação, no qual o público venera não a substância da obra, mas o seu próprio dinheiro e o sucesso comercial do produto?",
        "Comprovando que os instrumentos musicais de corda utilizados em estúdios de rádio eram afinados através de diapasões mecânicos de aço temperado.",
        "Demonstrando que, na sociedade de massas, o ouvinte alienado não escuta a música com sensibilidade formal autônoma; ele venera o fato de a canção ser a mais vendida, o disco mais caro ou o evento mais badalado pelas paradas de sucesso; o consumidor compra o ingresso caro para adorar a sua própria capacidade de gastar dinheiro, e essa dinâmica rebaixa a capacidade perceptiva do ouvido a reflexos condicionados infantis incapazes de apreender a complexidade estética real.",
        "Determinando que os conservatórios de música devam aplicar exames de aptidão rítmica aos compradores de ingressos de concertos.",
        "Afirmando que a regressão auditiva foi uma teoria médica formulada para justificar o tratamento de labirintite em operários de tecelagens.",
        "Provando que a medição do sucesso de canções populares dependia de relatórios lavrados por fiscais alfandegários portuários.",
        "B",
        "- **Etapa 1:** Desvendar o fetiche do sucesso comercial: as pessoas lotam o estádio e pagam mil reais no ingresso não pela harmonia da canção, mas porque 'é o evento do ano e todo mundo está falando'; adora-se a etiqueta de preço e a marca.\n- **Etapa 2:** Sentir a regressão da audição humana: acostumado a essa papinha comercial pronta, o ouvido do cidadão médio não aguenta dez segundos de um prelúdio ou de um jazz livre; a mente virou criança que só aceita pirulito auditivo mastigado."
    ))

    questoes_brutas.append((
        44, "EM13CHS302", "dificil",
        "Analise a tese adorniana de que 'o entretenimento é o prolongamento do trabalho sob o capitalismo tardio': por que a aparente liberdade do tempo livre e do divertimento opera, na realidade, como um dispositivo disciplinar de reprodução da força de trabalho mecanizada e de inculcação do conformismo político?",
        "Mostrando que os operários das indústrias automotivas participavam de torneios esportivos de futebol amador organizados por sindicatos de fábrica.",
        "Evidenciando que a indústria cultural programa o tempo livre com mercadorias culturais pré-digeridas cuja fruição exige a mesma passividade, atenção mecânica e ausência de pensamento requeridas pelo trabalho fabril e burocrático; longe de ser libertador, o lazer educa o trabalhador a aceitar a monotonia, a rir de sua própria impotência e a renovar suas energias unicamente para que possa se submeter novamente à exploração no dia seguinte sem se rebelar.",
        "Determinando que os estabelecimentos de diversão noturna devam encerrar suas atividades nos mesmos horários de fechamento de fábricas.",
        "Afirmando que a teoria do tempo livre alienado foi copiada de regulamentos disciplinares militares da marinha mercante prussiana.",
        "Comprovando que o divertimento operário era fiscalizado por comissões sanitárias municipais para conter contágios de cólera morbo.",
        "B",
        "- **Etapa 1:** Quebrar a ilusão do 'tempo livre sagrado': achamos que ao bater o ponto e ir para o sofá ver televisão estamos livres do patrão; mas o sofá virou a continuação da linha de montagem da fábrica.\n- **Etapa 2:** Reconhecer o adestramento para o conformismo: a série e o programa de auditório ensinam a não pensar, a achar que o mundo é assim mesmo e a rir da própria miséria; o trabalhador é recarregado passivamente para produzir lucro amanhã."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Examine o conceito de 'Semiformação' (Halbbildung) formulado por Theodor Adorno em 1959: por que a semiformação não deve ser compreendida como ignorância ou ausência de instrução formal, mas sim como a 'socialização alienada da cultura' que opera como o húmus fértil para o autoritarismo, preconceitos e fascismos contemporâneos?",
        "Provando que as escolas de ensino fundamental da República Federal da Alemanha utilizavam cartilhas impressas em prensas tipográficas a vapor.",
        "Demonstrando que o indivíduo semiformado não é o analfabeto desprovido de escolaridade, mas o cidadão escolarizado que consome vorazmente informações mastigadas, resumos rápidos e chavões midiáticos sem assimilação crítica ou dialética; esse acúmulo superficial de migalhas culturais produz a ilusão de onisciência arrogante, deixando o sujeito vulnerável à demagogia autoritária e inclinado a projetar sua angústia em teorias conspiratórias e ódio contra minorias.",
        "Determinando que os diplomados em cursos universitários devessem prestar novos exames gerais a cada cinco anos de atividade profissional.",
        "Afirmando que a teoria da semiformação foi elaborada para subsidiar cortes orçamentários em secretarias estaduais de educação pública.",
        "Comprovando que a proliferação de slogans decorreu do encarecimento das matérias-primas utilizadas na fabricação de tintas tipográficas.",
        "B",
        "- **Etapa 1:** Separar o analfabeto humilde do semiformado perigoso: o trabalhador simples sabe que não teve oportunidade de estudar e tem a humildade da terra; o semiformado tem diploma ou lê resumos na internet e se acha dono da verdade absoluta.\n- **Etapa 2:** Revelar a fábrica de fascistas na semiformação: cheia de certezas toscas e arrogância vazia, a pessoa semiformada não tolera a dúvida nem o diferente; quando o demagogo grita na TV culpando os imigrantes ou os professores pela crise, o semiformado aplaude com ódio cego."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Investigue a proposição lapidar de Adorno em Educação após Auschwitz: de que maneira o imperativo moral de que 'Auschwitz não se repita' exige uma pedagogia orientada para a desbarbarização da sociedade, a emancipação crítica (Mündigkeit) e a recusa da submissão cega ao coletivo administrado?",
        "Comprovando que os currículos escolares alemães do pós-guerra foram elaborados por oficiais reformados das forças aliadas de ocupação.",
        "Demonstrando que a prevenção de novos genocídios não depende de pregações moralistas piegas nem de exaltação patriótica cega, mas do cultivo rigoroso da autorreflexão crítica individual; educar contra a barbárie significa emancipar o estudante da subserviência psicológica à autoridade de chefes e corporações, capacitando-o a dizer 'não' a ordens criminosas e a resistir à tentação sádica de integrar massas enfurecidas que perseguem os mais vulneráveis.",
        "Determinando que os estudantes devessem realizar marchas cênicas em formação militar antes do início das aulas de matemática.",
        "Afirmando que a educação pós-Auschwitz foi concebida por companhias mercantis de carvão para garantir a disciplina em minas subterrâneas.",
        "Provando que a tese pedagógica de Adorno foi formulada para justificar a extinção de todas as instituições de ensino profissionalizante.",
        "B",
        "- **Etapa 1:** Enfrentar a sombra eterna de Auschwitz: o assassinato industrial de milhões de pessoas não foi acidente: foi cometido por homens comuns que apenas 'cumpriam ordens' de seus superiores sem pensar.\n- **Etapa 2:** Erigir a muralha da desobediência emancipada: educar de verdade na escola é ensinar a pensar por si mesmo; o jovem que aprende a questionar o chefe e a ter empatia pelo sofrimento do outro nunca vestirá a bota do carrasco fascista."
    ))

    questoes_brutas.append((
        47, "EM13CHS301", "dificil",
        "Analise o papel da 'Dissonância' e do 'Enigma' na Teoria Estética de Adorno como trincheiras de resistência da Arte Autônoma: por que a beleza harmoniosa tradicional tornou-se ideologicamente cúmplice da barbárie após a Segunda Guerra Mundial, exigindo que a arte contemporânea assuma a negatividade e a fratura?",
        "Provando que os ateliês de vanguarda artística utilizavam solventes químicos de alta toxicidade na diluição de vernizes sintéticos.",
        "Evidenciando que, após as cinzas de Auschwitz e o horror atômico de Hiroshima, qualquer obra que se apresente como totalidade límpida, reconciliada e consoladora mente sobre o estado real da humanidade, funcionando como anestesia ideológica; para manter sua verdade e dignidade, a arte séria (como na literatura de Beckett ou Celan) deve incorporar em sua forma a dor, o despedaçamento e a dissonância, preservando o protesto mudo contra a sociedade opressora.",
        "Determinando que os museus de arte moderna devam cobrir suas paredes com tecidos pretos durante períodos de solstício de inverno.",
        "Afirmando que a recusa da harmonia clássica decorreu de instruções normativas emitidas por tribunais marítimos de navegação portuária.",
        "Comprovando que a dissonância estética foi inventada por corporações têxteis para incentivar a comercialização de tecidos desfiados.",
        "B",
        "- **Etapa 1:** Sentir a vergonha da harmonia adocicada pós-Auschwitz: depois que o ser humano foi queimado em fornos industriais, escrever poesia de rima fácil fingindo que o mundo é lindo é uma mentira covarde e imoral.\n- **Etapa 2:** Celebrar o grito mudo da arte dissonante: a arte autônoma de Beckett e Paul Celan é torta, difícil e sangra na forma; ela recusa a simpatia fácil da prateleira do mercado para que ninguém esqueça o tamanho do sofrimento humano na história."
    ))

    questoes_brutas.append((
        48, "EM13CHS302", "dificil",
        "Examine o paralelismo entre o diagnóstico da Indústria Cultural em Adorno e a operação dos 'Algoritmos de Engajamento e Bolhas Digitais' no Capitalismo de Plataforma contemporâneo: como a mercantilização da atenção radicaliza a padronização e o conformismo previstos pela Escola de Frankfurt?",
        "Mostrando que os data centers das redes sociais consomem energia elétrica produzida unicamente por usinas termelétricas a carvão mineral.",
        "Demonstrando que, ao submeter o fluxo comunicacional à métrica dos cliques, do tempo de retenção e da monetização publicitária, as plataformas digitais aperfeiçoaram a indústria cultural: o algoritmo não expande horizontes, mas entrega torrencialmente o mesmo conteúdo pré-fabricado que excita os preconceitos do usuário, transformando o consumo em vício dopamínico e o debate público em arenas polarizadas e acríticas a serviço de monopólios corporativos.",
        "Determinando que os servidores de telecomunicações devam ser desligados compulsoriamente durante os feriados cívicos nacionais.",
        "Afirmando que os algoritmos de recomendação foram programados com base em tabelas de juros compostos de bancos mercantis renascentistas.",
        "Comprovando que a polarização de redes sociais decorre de diretrizes pedagógicas formuladas por academias militares prussianas.",
        "B",
        "- **Etapa 1:** Reconhecer a evolução da armadilha frankfurtiana: Adorno viu o rádio e o cinema empurrando a mesma música para todo mundo; o algoritmo de hoje foi além: ele pesquisa a sua fraqueza mental individual para empurrar o clichê que vicia você.\n- **Etapa 2:** Denunciar o cativeiro de dopamina lucrativa: você rola o feed por horas achando que está se informando, mas está apenas alimentando o cofre de Wall Street; a mente fica presa numa bolha de ódio e futilidade que mata o pensamento livre."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "Investigue o diálogo crítico entre a Teoria Crítica de Adorno e os 'Estudos Culturais Britânicos' (Stuart Hall e Raymond Williams): de que maneira o modelo de 'Codificação/Decodificação' refina e confronta a premissa frankfurtiana de uma receptividade popular passiva e indefesa perante as mensagens da mídia dominante?",
        "Comprovando que os pesquisadores de Birmingham realizavam pesquisas de campo utilizando formulários impressos em papéis coloridos de linho.",
        "Evidenciando que, enquanto Adorno enfatizava o poder esmagador e unilateral da indústria cultural sobre massas alienadas e desarmadas, Stuart Hall demonstrou que os receptores não são receptáculos inertes; as classes trabalhadoras e as juventudes periféricas realizam leituras negociadas e de oposição às narrativas dominantes da mídia, ressignificando criticamente os produtos culturais a partir de suas próprias vivências, ancestralidades e lutas concretas de classe e de raça.",
        "Determinando que os centros de estudos culturais devam ser subordinados à fiscalização de comissões disciplinares de infantaria armada.",
        "Afirmando que a tradição dos estudos culturais britânicos foi financiada por monopólios corporativos de navegação comercial marítima.",
        "Provando que a distinção entre leituras dominantes e negociadas decorreu de tratados diplomáticos assinados entre monarquias da Escandinávia.",
        "B",
        "- **Etapa 1:** Reconhecer o limite do pessimismo de Adorno: Adorno olhava o povo e achava que todo mundo era engolido passivamente pelas mensagens da TV e do rádio sem qualquer defesa mental.\n- **Etapa 2:** Resgatar a malícia subversiva de Stuart Hall: Hall mostrou que quem mora na favela não é bobo; ele assiste à TV, mas ri do patrão, pega a batida do pop e faz um funk que denuncia a violência policial; a recepção popular é viva, inteligente e briga de volta."
    ))

    questoes_brutas.append((
        50, "EM13CHS102", "dificil",
        "Analise a relevância dos achados da obra A Personalidade Autoritária (1950) de Theodor Adorno para a compreensão da ascensão de tendências fascistas e movimentos autoritários no cenário contemporâneo: de que maneira a repressão psicológica familiar, o moralismo hipócrita e a semiformação estruturam o perfil do indivíduo intolerante?",
        "Provando que os questionários da Escala F foram arquivados em caixas de madeira vedadas e depositadas em bibliotecas universitárias da Califórnia.",
        "Demonstrando que Adorno comprovou que tendências fascistas não brotam de loucuras individuais repentinas, mas de processos sociais e educacionais repressivos que geram indivíduos inseguros, rígidos e intelectualmente semiformados; esses sujeitos encontram alívio psíquico submetendo-se a figuras políticas autoritárias e descarregando sua agressividade reprimida contra minorias sociais, direitos humanos e liberdades democráticas.",
        "Determinando que as investigações de psicologia social devam ser conduzidas exclusivamente por médicos psiquiatras vinculados a tribunais militares.",
        "Afirmando que a personalidade autoritária foi uma patologia clínica restrita a veteranos de guerra do primeiro conflito mundial europeu.",
        "Comprovando que as conclusões da pesquisa de 1950 foram adotadas por corporações de navegação naval para selecionar marinheiros mercantes.",
        "B",
        "- **Etapa 1:** Desmistificar a lenda de que o fascista 'é um monstro doido': Adorno provou que o autoritário é o cidadão comum educado na base da pancada, da culpa moralista e do medo da liberdade; ele parece pacato por fora, mas guarda ódio por dentro.\n- **Etapa 2:** Compreender a explosão do neofascismo de hoje: quando esse indivíduo se sente ameaçado e consome fake news na internet, ele se apaixona pelo político truculento que promete armas e violência contra os fracos; o fascismo é a vingança dos medíocres."
    ))

    questoes_brutas.append((
        51, "EM13CHS301", "dificil",
        "Examine a crítica contundente de Adorno ao conceito burguês de 'Gênio Criador e Obra-Prima Individual' à luz do fetichismo cultural: por que a exaltação romântica do artista como ser divinamente inspirado e intocável atua como ideologia de encobrimento das condições materiais e históricas de produção da arte?",
        "Comprovando que os artistas plásticos renascentistas utilizavam cavaletes de madeira construídos com madeiras de demolição de portos.",
        "Demonstrando que a ideologia do gênio genializa o indivíduo isolado para esconder a dependência da arte em relação às forças produtivas, às relações de classe e ao trabalho acumulado de gerações inteiras; ao tratar a obra-prima como milagre inexplicável de uma mente iluminada, o mercado converte a arte em fetiche sagrado de ostentação para colecionadores ricos, apagando a história concreta de sua fatura social.",
        "Determinando que as assinaturas de pintores em cantos de telas devessem ser autenticadas por tabelionatos municipais de registros civis.",
        "Afirmando que a crítica à genialidade romântica foi copiada de regulamentos disciplinares militares da infantaria britânica.",
        "Provando que a exaltação do artista divino decorreu de decretos de imperadores romanos para justificar subsídios concedidos a escultores.",
        "B",
        "- **Etapa 1:** Desmascarar o mito romântico do 'gênio divino': a propaganda burguesa adora dizer que o grande pintor é um ser mágico que recebe luz do céu sozinho no quarto e faz uma obra que paira acima da história humana.\n- **Etapa 2:** Resgatar a raiz material da criação em Adorno: a arte é fruto da história de um povo, da técnica de sua época e do suor de gerações de artesãos anônimos; idolatrar o gênio serve apenas para o ricaço comprar o quadro por milhões e ostentar nas paredes de seu palácio."
    ))

    questoes_brutas.append((
        52, "EM13CHS302", "dificil",
        "Investigue o papel pedagógico do conceito de 'Semiformação' nas diretrizes da BNCC para o Ensino Médio (EM13CHS102 e EM13CHS302): de que maneira o aprendizado da Teoria Crítica em Filosofia capacita os estudantes a combaterem a superficialidade intelectual, a cultura de cancelamento e o consumo acrítico de conteúdos em redes digitais?",
        "Provando que as matrizes curriculares escolares devem limitar-se à memorização de definições lexicográficas de vocábulos filosóficos clássicos.",
        "Evidenciando que a formação filosófica crítica emancipa o jovem da ilusão de que pequenos fragmentos de vídeos e manchetes sensacionalistas constituem conhecimento autêntico; mune-o de ferramentas metodológicas para analisar as contradições socioeconômicas, desconfiar de discursos fáceis e assumir uma postura ética de paciência reflexiva e rigor analítico, transformando-o em um cidadão consciente e imune à sedução de autoritarismos.",
        "Determinando que os estudantes devessem realizar avaliações pedagógicas unicamente através de provas de memorização mecânica de datas.",
        "Afirmando que o ensino de filosofia contemporânea deve ser suspenso nas escolas públicas para reduzir custos de material didático impresso.",
        "Comprovando que o combate à semiformação depende de laudos periciais expedidos por comissões disciplinares militares de quartéis.",
        "B",
        "- **Etapa 1:** Notar o perigo da pressa e do raso na juventude: na era do clique, o estudante é tentado a achar que sabe tudo porque viu um reel de 15 segundos ou leu um tweet irônico; o debate vira tribunal de cancelamento tóxico.\n- **Etapa 2:** Despertar a mente com Adorno na BNCC: estudar Teoria Crítica ensina o jovem a respirar fundo, ler a história inteira e perguntar pelas raízes materiais do problema; o aluno aprende a não ser massa de manobra de ninguém."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Analise a relação entre a 'Indústria Cultural e a Indústria da Moda (Fashion System)': de que maneira o ciclo ininterrupto de coleções, tendências sazonais e obsolescência estética forçada reproduz a lógica da pseudo-individualidade e da alienação do corpo sob o capitalismo tardio?",
        "Mostrando que as fábricas têxteis da Europa ocidental utilizavam teares mecânicos movidos por caldeiras alimentadas com carvão de turfa.",
        "Demonstrando que a moda industrializada cria uma permanente sensação de inadequação e atraso no consumidor; ao decretar anualmente que certas cores, cortes e tecidos estão ultrapassados, ela força a compra compulsiva de novas peças estruturalmente idênticas, vendendo a ilusão de personalidade individual através da submissão rigorosa aos ditames uniformizadores do mercado corporativo global.",
        "Determinando que as lojas de comércio de vestuário devam manter registros contábeis auditados por comissões disciplinares de marinhas.",
        "Afirmando que as tendências de moda foram criadas por generais militares para padronizar os fardamentos de tropas de infantaria montada.",
        "Comprovando que a renovação de coleções têxteis dependia de autorizações concedidas por congregações paroquiais de monges franciscanos.",
        "B",
        "- **Etapa 1:** Olhar a crueldade da 'obsolescência da moda': a sua roupa está perfeita, limpa e dura dez anos; mas a vitrine diz 'esta cor é do ano passado e você é um cafona se continuar usando'; cria-se a vergonha do próprio corpo.\n- **Etapa 2:** Revelar a farsa da originalidade: a pessoa gasta metade do salário para comprar a calça rasgada da estação achando que é 'única e descolada'; na rua, ela encontra dez mil pessoas vestidas rigorosamente iguais a ela; a moda é a farda do consumo."
    ))

    questoes_brutas.append((
        54, "EM13CHS102", "dificil",
        "Examine a advertência de Theodor Adorno sobre a 'Neutralização Crítica dos Clássicos' pela Indústria Cultural: por que a transformação de quadros de Van Gogh em estampas de guarda-chuvas ou sinfonias de Beethoven em toques de telefone celular anula a carga explosiva e subversiva originária dessas obras de arte?",
        "Comprovando que as fábricas de sombrinhas utilizavam hastes metálicas confeccionadas com sobras de aços de estaleiros navais.",
        "Demonstrando que, ao retirar a obra de sua atmosfera de estranhamento e integrá-la pacificamente ao cotidiano de consumo decorativo vulgar, a indústria cultural domestica seu potencial de protesto; a Quinta Sinfonia ou os girassóis deixam de ser gritos de desespero e revolta existencial para se tornarem enfeites inofensivos de salão que reconciliam o burguês com a ordem estabelecida sem perturbar sua digestão.",
        "Determinando que as sinfonias clássicas devessem ser executadas unicamente em auditórios universitários com isolamento acústico de cortiça.",
        "Afirmando que a reprodução de pinturas clássicas dependia de pagamentos de royalties a fundações filantrópicas de dinastias reais.",
        "Provando que a adaptação de partituras para sinos de telefone foi uma invenção de engenheiros de telégrafos da República de Weimar.",
        "B",
        "- **Etapa 1:** Recordar o sangue e o grito de Beethoven e Van Gogh: Beethoven batia no piano surdo de ódio contra os tiranos e Van Gogh cortava a própria orelha de dor e solidão pintando a fome dos camponeses; a obra original era um terremoto.\n- **Etapa 2:** Sentir o nojo da domesticação comercial: a indústria cultural pega a tela de Van Gogh e estampa numa canequinha fofa de shopping; o grito de revolta foi anestesiado e virou brinde inofensivo que não incomoda ninguém."
    ))

    questoes_brutas.append((
        55, "EM13CHS301", "dificil",
        "Investigue o conceito adorniano de 'Catarse Enganosa e Apaziguadora': por que a experiência do choro comovido ou do riso fácil em salas de cinema de entretenimento comercial atua como dispositivo psicológico de desoneração moral que desmobiliza a revolta social na vida real?",
        "Provando que as poltronas de salas de cinema comerciais utilizavam forrações de couro sintético importado de fábricas da Baviera.",
        "Demonstrando que, ao chorar copiosamente pela desgraça do personagem na tela ou ao rir com alívio do final feliz pré-fabricado, o espectador descarrega sua indignação e culpa de forma vicária e inócua na escuridão da sala; ele sai do cinema sentindo-se uma pessoa 'sensível e moralmente purificada', o que o desonera psicologicamente da obrigação real de lutar concretamente contra a miséria e a injustiça em seu cotidiano.",
        "Determinando que os cinemas devam distribuir lenços de papel higienizados aos frequentadores de sessões vespertinas de dramas.",
        "Afirmando que a catarse cinematográfica foi desenvolvida por comissões de saúde pública para tratar quadros de histeria coletiva urbana.",
        "Comprovando que as reações emocionais em salas de espetáculos eram registradas em livros contábeis por fiscais de tesouros provinciais.",
        "B",
        "- **Etapa 1:** Desmascarar o 'choro barato' do cinema comercial: a pessoa vai ao shopping, assiste ao filme triste, molha três lenços de lágrimas pelo sofrimento do personagem e sai com o peito leve.\n- **Etapa 2:** Descobrir a anestesia da ação política: na porta do cinema a pessoa passa reto pelo mendigo que está dormindo no chão frio sem dar um real; o choro no cinema serviu apenas como desodorante de consciência para ela continuar vivendo no egoísmo sem se revoltar."
    ))

    questoes_brutas.append((
        56, "EM13CHS302", "dificil",
        "Analise a relação entre o diagnóstico frankfurtiano e o surgimento do fenômeno dos 'Influenciadores Digitais e Creators': de que maneira a mercantilização da própria intimidade particular e do cotidiano doméstico eleva a indústria cultural a um estágio de invasão psíquica total nunca antes testemunhado na história humana?",
        "Mostrando que os equipamentos de transmissão de vídeo utilizados por influenciadores utilizam baterias de lítio recarregáveis em tomadas residenciais.",
        "Evidenciando que, enquanto a indústria cultural tradicional operava através de atores profissionais em estúdios distantes, os criadores digitais contemporâneos convertem seus lares, almoços, casamentos e dores pessoais em mercadorias visuais contínuas; o fetiche da autenticidade cotidiana é explorado para vender produtos publicitários e estilos de vida padronizados, transformando o próprio sujeito humano e sua privacidade em empresa publicitária viva ininterrupta.",
        "Determinando que os produtores de conteúdo de internet devessem assinar termos de responsabilidade cívica em cartórios de registros públicos.",
        "Afirmando que a monetização da intimidade foi uma estratégia criada por corporações mercantis têxteis para alavancar a venda de pijamas.",
        "Comprovando que a circulação de vlogs domésticos dependia de autorizações sanitárias concedidas por comissões disciplinares de marinhas.",
        "B",
        "- **Etapa 1:** Lembrar do limite da Indústria Cultural antiga: na época de Adorno, o filme acabava quando saía do cinema e o ator desligava a câmera; a vida privada na casa da pessoa ainda era um refúgio do mercado.\n- **Etapa 2:** Aterrorizar-se com a invasão do quarto hoje: o influenciador acorda filmando o café, filma a briga com o cônjuge e chora na câmera para ganhar engajamento e vender creme de pele; a própria vida íntima do ser humano virou vitrine e mercadoria."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Examine a crítica formulada em Dialética do Esclarecimento à 'Racionalidade Técnica da Produção de Desenhos Animados' (como nos clássicos de Walt Disney dos anos 1930 e 1940): de que maneira as peripécias de personagens como o Pato Donald e o camundongo Mickey educavam as massas para a resignação perante a violência social?",
        "Provando que as folhas de celulóide utilizadas na animação manual eram pintadas com tintas aquosas importadas de indústrias químicas suíças.",
        "Demonstrando que, ao retratar personagens que sofrem espancamentos brutais, quedas de penhascos e esmagamentos mecânicos sem morrer e sem reclamar, levantando-se imediatamente para continuar correndo na mesma roda viva, a animação comercial incute na psique das massas que a dor e a violência física do sistema econômico são normais e que o indivíduo deve se acostumar a ser esmagado sem jamais protestar.",
        "Determinando que os estúdios de animação de Hollywood devessem manter parcerias comerciais com zoológicos públicos municipais.",
        "Afirmando que as narrativas de desenhos animados foram elaboradas por generais militares para treinar soldados no salto com paraquedas.",
        "Comprovando que a produção de curtas de animação dependia de autorizações expedidas por tabelionatos consulares de portos mercantes.",
        "B",
        "- **Etapa 1:** Olhar além da fofura do desenho infantil: no desenho clássico, o personagem leva uma marretada na cabeça, vira um acordeão amassado, chacoalha o corpo e continua correndo como se nada tivesse acontecido.\n- **Etapa 2:** Descobrir o adestramento para a paulada da vida: Adorno mostrou que essa violência ensina a criança e o operário a aguentarem o tranco da exploração; 'a vida bate, você é amassado pelo patrão, mas levanta caladinho e continua trabalhando'."
    ))

    questoes_brutas.append((
        58, "EM13CHS102", "dificil",
        "Analise a dialética entre a 'Totalidade Falsa e a Fragmentação Crítica' na Teoria Estética de Theodor Adorno: por que a verdadeira obra de arte autônoma deve recusar a ilusão de um sistema fechado e perfeito, expondo em suas fendas e incompletudes a fratura irreconciliada do mundo contemporâneo?",
        "Mostrando que os escultores da vanguarda expressionista utilizavam ligas de bronze fundidas em temperaturas superiores a mil graus célsius.",
        "Evidenciando que a pretensão de harmonia e perfeição formal totalizante é uma mentira ideológica em uma sociedade dilacerada por guerras, exploração e catástrofes; para Adorno, a arte autêntica deve ser fragmento, fratura e enigma não resolvido, recusando a mentira de que tudo está em paz e desafiando o sujeito a encarar as contradições dolorosas de uma realidade que clama por transformação revolucionária radical.",
        "Determinando que as obras de arte inacabadas devam ser recolhidas compulsoriamente a depósitos municipais de entulhos de construção.",
        "Afirmando que a valorização do fragmento decorreu de instruções normativas emitidas por cortes dinásticas da Europa central no século XVIII.",
        "Comprovando que a técnica estética do fragmento foi inventada por corporações mercantis de carpintaria naval para reduzir o desperdício de madeira.",
        "B",
        "- **Etapa 1:** Desmascarar a perfeição redondinha da obra burguesa: a obra comercial tem começo, meio e fim perfeito onde todas as pontas se amarram sem deixar nenhuma dúvida; é a mentira de que o mundo faz sentido.\n- **Etapa 2:** Afirmar a honra da fratura em Adorno: em Kafka o processo não tem fim e o castelo nunca é alcançado; na grande arte a obra fica aberta e cheia de rachaduras porque o nosso mundo real é quebrado e injusto; a forma tem que doer para dizer a verdade."
    ))

    questoes_brutas.append((
        59, "EM13CHS301", "dificil",
        "Investigue o conceito de 'Semiformação como Bloqueio da Experiência Histórica Viva': de que modo a substituição da memória coletiva e da reflexão dialética pelo consumo instantâneo de manchetes e notícias de última hora gera uma sociedade amnésica e propensa a reeditar as tragédias do passado?",
        "Comprovando que os arquivos de jornais diários utilizavam encadernações de couro tratadas com substâncias repelentes de insetos em bibliotecas.",
        "Demonstrando que a velocidade febril e a fragmentação com que a indústria cultural despeja informações nas mídias anulam a capacidade de retenção temporal e de elaboração do luto histórico; o indivíduo consome a tragédia de hoje como mero entretenimento passageiro e a esquece amanhã diante do próximo escândalo, tornando a sociedade incapaz de aprender com seus erros passados e abrindo as portas para o retorno da barbárie sob novas roupagens.",
        "Determinando que os leitores de periódicos devam assinar termos de compromisso de guarda de exemplares antigos em seus domicílios.",
        "Afirmando que a amnésia histórica foi uma teoria neurológica formulada para justificar o consumo compulsório de vitaminas minerais por operários.",
        "Provando que a aceleração das notícias foi uma estratégia concebida por companhias de navegação a vapor para baratear fretes marítimos.",
        "B",
        "- **Etapa 1:** Diagnosticar a amnésia das telas contemporâneas: hoje acontece um massacre ou uma enchente devastadora e todo mundo posta; três dias depois ninguém lembra mais porque já surgiu a fofoca do jogador de futebol ou a nova dança da internet.\n- **Etapa 2:** Sofrer com a repetição da barbárie: quem não guarda memória e não reflete sobre a raiz da dor está condenado a repetir o desastre; a sociedade amnésica da semiformação esquece os erros e vota de novo no tirano que vai massacrá-la."
    ))

    questoes_brutas.append((
        60, "EM13CHS302", "dificil",
        "Ao concluirmos o Capítulo 29 com a demolição crítica da Indústria Cultural por Adorno e Horkheimer, analise como a transição histórica e filosófica para o Capítulo 30 operará uma virada radical da crítica europeia para as 'Poéticas da Negritude' de Aimé Césaire e Léopold Sédar Senghor, fechando com chave de ouro o Eixo IV de Estética e alcançando o MARCO HISTÓRICO DE 75% DE TODA A OBRA DE FILOSOFIA:",
        "Provando que as investigações de crítica cultural perderam sua validade teórica após a inauguração de fábricas automatizadas de montagem de automóveis.",
        "Demonstrando que, após percorrermos a estética antiga da mimesis (Cap 25), o cume moderno do gosto e do sublime em Kant e Hegel (Cap 26), a tragédia dionisíaca em Nietzsche (Cap 27), a reprodutibilidade técnica em Benjamin (Cap 28) e a indústria cultural frankfurtiana (Cap 29), o Capítulo 30 romperá os horizontes eurocêntricos para consagrar a arte, a poesia e o ritmo ancestral da Negritude como potências descolonizadoras da sensibilidade humana, coroando o Eixo IV e celebrando 30 de 40 capítulos homologados com rigor absoluto!",
        "Determinando que os currículos de filosofia do Ensino Médio devam ser substituídos unicamente pelo estudo de regulamentos de navegação comercial marítima.",
        "Afirmando que os fundadores do movimento da Negritude rejeitaram o estudo da filosofia europeia por considerá-la um compêndio de fábulas cômicas medievais.",
        "Comprovando que a transição entre capítulos teóricos depende de autorizações prévias expedidas por comissões disciplinares militares de fronteiras.",
        "B",
        "- **Etapa 1:** Sintetizar a marcha colossal do Eixo IV até aqui: navegamos por Platão e Aristóteles, pelo belo e o sublime de Kant e Hegel, pelo vulcão de Nietzsche, pela aura de Benjamin e pela lâmina crítica implacável de Adorno e Horkheimer.\n- **Etapa 2:** Abrir as portas da glória com Césaire e Senghor no Cap 30: fechamos o Cap 29 no topo da excelência e marchamos para as Poéticas da Negritude para descolonizar a mente com poesia, ritmo e ancestralidade negra, alcançando 30 capítulos e 75% de toda a coleção de Filosofia EM!"
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
    linhas.append('capitulo: "Capítulo 29: Indústria Cultural: Adorno e Horkheimer"')
    linhas.append('objeto_de_conhecimento: "O conceito de Indústria Cultural em Adorno e Horkheimer, a padronização e o fetiche da mercadoria na arte, a crítica à semiformação (Halbbildung), o entretenimento como conformismo e o potencial de resistência da arte autônoma"')
    linhas.append('ebook_fonte: "em-fil-c29-industria-cultural-adorno-horkheimer.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS301"')
    linhas.append('  - "EM13CHS302"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: Indústria Cultural: Adorno e Horkheimer\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-29-industria-cultural-adorno-horkheimer -->"
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
    linhas.append("- ADORNO, Theodor W.; HORKHEIMER, Max. *Dialética do esclarecimento: fragmentos filosóficos*. Tradução de Guido Antonio de Almeida. Rio de Janeiro: Jorge Zahar, 1985.")
    linhas.append("- ADORNO, Theodor W. Teoria da semiformação. In: PUCCI, Bruno et al. (Org.). *Teoria crítica e inconformismo: novas perspectivas de pesquisa*. Campinas: Autores Associados, 2010.")
    linhas.append("- DUARTE, Rodrigo. *Indústria cultural: uma introdução*. Rio de Janeiro: Jorge Zahar, 2010.")
    linhas.append("- FREITAS, Verlaine. *Adorno & a arte contemporânea*. Rio de Janeiro: Jorge Zahar, 2003.")
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
    print(f"Rascunho salvo em temp_draft.md ({tamanho} bytes)")

    destino_final = "content/medio/volume-unico/filosofia/eixo-4-estetica/cap-29-industria-cultural-adorno-horkheimer/ebooks/em-fil-c29-industria-cultural-adorno-horkheimer-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 29 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
