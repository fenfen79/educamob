# -*- coding: utf-8 -*-
"""
Gerador das 60 questões atômicas de Filosofia EM - Capítulo 20:
Rousseau, Vontade Geral e a Crítica Marxista ao Estado Burguês
Destino: content/medio/volume-unico/filosofia/eixo-3-politica/cap-20-rousseau-vontade-geral-critica-marxista/ebooks/em-fil-c20-rousseau-vontade-geral-critica-marxista-exercicios.md
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
        "Qual tema desafiador foi proposto pela Academia de Dijon em 1754, cuja resposta consagrou Jean-Jacques Rousseau no debate iluminista europeu?",
        "A descoberta de novas rotas de navegação marítima para o comércio com as Índias Orientais.",
        "A investigação sobre qual é a origem da desigualdade entre os homens e se ela é autorizada pela lei natural.",
        "O aperfeiçoamento de técnicas agrícolas de arado para o cultivo intensivo de cereais de inverno.",
        "A demonstração geométrica das órbitas dos cometas em torno do sistema solar.",
        "A regulamentação dos salários pagos a sapateiros e carpinteiros em feiras municipais da França.",
        "B",
        "Rousseau respondeu ao concurso de Dijon com seu magistral Discurso sobre a Desigualdade, demonstrando que a desigualdade social não é natural nem divina, mas fruto da história humana e da propriedade privada."
    ))

    questoes_brutas.append((
        2, "EM13CHS601", "basico",
        "Qual crítica metodológica rigorosa Rousseau dirige a Thomas Hobbes e John Locke em relação à descrição do estado de natureza?",
        "Acusa os dois filósofos ingleses de terem utilizado mapas geográficos imprecisos de ilhas do mar Mediterrâneo.",
        "Denuncia que ambos projetaram no homem primitivo os vícios, a ganância mercantil, o egoísmo e a vaidade próprios do homem corrompido da sociedade civil do século XVII.",
        "Afirma que os autores desconheciam a língua latina clássica utilizada nos manuscritos medievais.",
        "Critica o fato de Hobbes e Locke defenderem a abolição da moeda e o retorno ao escambo comunitário.",
        "Sustenta que os pensadores deveriam ter consultado sacerdotes paroquiais antes de publicarem suas teses.",
        "B",
        "Rousseau percebeu o anacronismo dos contratualistas anteriores: pegaram o burguês civilizado com sua sede de acumulação e o colocaram nas florestas primitivas, chamando-o de homem natural."
    ))

    questoes_brutas.append((
        3, "EM13CHS102", "basico",
        "Quais são os dois princípios inatos e pré-racionais que governam a conduta do ser humano no verdadeiro estado de natureza rousseauniano?",
        "A ambição de enriquecimento rápido e a inveja corrosiva do sucesso material dos vizinhos.",
        "O Amor de Si (o instinto saudável de autopreservação) e a Piedade (a aversão inata e compadecida de presenciar o sofrimento do semelhante).",
        "A agressividade armada instintiva e a busca desenfreada pela glória militar nas guerras.",
        "A obediência cega a mandamentos eclesiásticos e o medo eterno de castigos infernais.",
        "O cálculo matemático das probabilidades de lucro comercial em feiras de lã e linho.",
        "B",
        "Antes da razão e da vaidade, o homem natural busca sobreviver sem fazer mal a ninguém (amor de si) e sente repulsa diante da dor de qualquer ser vivo semelhante (piedade)."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "Como a figura clássica do 'Bom Selvagem' caracteriza a existência do ser humano natural na concepção de Jean-Jacques Rousseau?",
        "Um ser cruel e sanguinário que caçava seus semelhantes para alimentar fogueiras tribais.",
        "Um indivíduo simples, saudável e autônomo, que saciava suas necessidades básicas sob as árvores e vivia livre de dependência social de outros homens.",
        "Um sábio iluminista que passava as tardes redigindo compêndios de botânica e mineralogia.",
        "Um trabalhador assalariado que buscava empregos temporários em companhias de carruagens urbanas.",
        "Um eremita penitente que professava votos perpétuos de silêncio e jejum no deserto.",
        "B",
        "O bom selvagem não é perverso porque desconhece os vícios sociais e a hipocrisia; ele não depende de ninguém para comer ou dormir, vivendo em equilíbrio com o meio natural."
    ))

    questoes_brutas.append((
        5, "EM13CHS602", "basico",
        "De acordo com Rousseau, qual evento histórico fundamental inaugurou a sociedade civil e aprofundou a desigualdade social e os conflitos humanos?",
        "A invenção de moinhos de vento para a moagem de grãos de cevada nas planícies.",
        "O surgimento da Propriedade Privada, simbolizado pelo ato de cercar um terreno e declarar 'isto é meu'.",
        "A celebração dos primeiros tratados de paz entre navegadores mercantes no mar do Norte.",
        "A criação de companhias de teatro cômico que viajavam por vilas e aldeias do interior.",
        "A proibição real da caça de lebres e cervos selvagens durante os meses de outono.",
        "B",
        "Para Rousseau, a cerca na terra foi o marco da tragédia humana: dividiu os homens entre proprietários e despossuídos, gerando a cobiça, as guerras e as misérias sociais."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Como Rousseau descreve a transformação psicológica que acompanhou a introdução da propriedade privada e da vida social sedentária?",
        "O aumento generalizado da generosidade altruísta e da caridade mútua entre os vizinhos.",
        "A degeneração do amor de si saudável no tóxico Amor-Próprio, marcado pela vaidade, pela comparação invejosa e pela obsessão pelo parecer sobre o ser.",
        "A conquista da sabedoria mística que libertou a mente humana de qualquer desejo mundano.",
        "A dedicação unânime de todas as famílias ao aprendizado de instrumentos de música de corda.",
        "A eliminação definitiva de disputas patrimoniais mediante o uso de dados de adivinhação.",
        "B",
        "Na sociedade civil corrompida, o homem passa a viver do olhar dos outros: surge a necessidade fútil de ostentar riquezas, a inveja do vizinho e o desprezo pelos mais pobres."
    ))

    questoes_brutas.append((
        7, "EM13CHS601", "basico",
        "Por que Rousseau classifica o primeiro pacto que deu origem aos governos e leis civis como um 'Falso Contrato Social'?",
        "Porque o documento foi redigido com tinta vegetal de baixa durabilidade que apagou com o sol.",
        "Porque foi uma armadilha forjada pelas elites ricas proprietárias para convencer os pobres despossuídos a aceitarem leis que eternizaram a desigualdade e a servidão.",
        "Porque as assembleias populares foram realizadas durante uma epidemia infecciosa na capital.",
        "Porque os governantes recusaram-se a pagar os soldos atrasados dos soldados de infantaria.",
        "Porque os camponeses desconheciam as regras de navegação fluvial em rios navegáveis.",
        "B",
        "Com medo de perderem suas posses para revoltas dos famintos, os ricos propuseram unir todos sob leis 'de paz'; os pobres correram aos grilhões achando que ganhavam a liberdade."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "Logo nas primeiras linhas de sua obra política capital de 1762, Jean-Jacques Rousseau formula um diagnóstico contundente a respeito da perda da autonomia natural pelo homem civilizado. Com quais palavras o filósofo expressa esse contraste entre o nascimento livre e o aprisionamento social?",
        "O homem nasce escravo por decreto divino e só encontra paz na obediência monástica.",
        "O homem nasce livre, e por toda a parte encontra-se a ferros.",
        "O homem é o lobo do homem e deve se submeter à espada do soberano supremo.",
        "O homem é um animal econômico guiado pela busca incessante de moedas de prata.",
        "O homem é um soldado destinado a defender fortificações de pedra nas fronteiras.",
        "B",
        "Rousseau parte dessa constatação dilacerante: a liberdade é nossa condição natural, mas as instituições corrompidas acorrentaram a humanidade sob a tirania e a servidão."
    ))

    questoes_brutas.append((
        9, "EM13CHS602", "basico",
        "Ao formular o problema fundamental que sua teoria política visa solucionar, Rousseau busca uma forma de vida republicana em que a cooperação mútua preserve a autonomia dos cidadãos. Qual é a meta central que orienta a constituição desse pacto associativo legítimo?",
        "Abolir todas as formas de tribunais civis e permitir a justiça pelas próprias mãos com armas.",
        "Encontrar uma forma de associação política que proteja a pessoa e os bens de cada associado e na qual cada um, unindo-se a todos, não obedeça senão a si mesmo, continuando tão livre como antes.",
        "Restaurar o modelo feudal medieval de vassalagem e dízimos eclesiásticos compulsórios.",
        "Transferir a administração das finanças estatais a companhias de navegação transatlântica.",
        "Obrigar todos os cidadãos a viverem em fazendas agrícolas coletivas em áreas montanhosas.",
        "B",
        "O desafio de Rousseau é conciliar ordem e liberdade: a lei não deve ser a imposição de um soberano externo, mas a expressão da própria vontade do cidadão que governa a si mesmo."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Em que consiste a chamada 'Alienação Total' de cada cidadão na celebração do legítimo contrato social rousseauniano?",
        "Na venda compulsória de todas as roupas e ferramentas de trabalho a mercadores do porto.",
        "Na doação integral de cada indivíduo com todos os seus direitos à comunidade coletiva, garantindo que, como a condição é igual para todos, ninguém tenha interesse em torná-la pesada aos demais.",
        "Na transferência de poderes governamentais a dinastias reais de sangue nobre estrangeiras.",
        "Na renúncia perpétua ao direito de emitir opiniões sobre os rumos orçamentários da república.",
        "Na submissão das forças policiais municipais ao controle de confrarias monásticas rurais.",
        "B",
        "Dando-se cada um a todos, não se dá a ninguém em particular: cria-se uma igualdade jurídica absoluta onde o poder pertence ao corpo coletivo dos cidadãos unidos."
    ))

    questoes_brutas.append((
        11, "EM13CHS601", "basico",
        "Como Rousseau distingue com precisão o conceito de 'Vontade Geral' do conceito de 'Vontade de Todos'?",
        "A Vontade Geral é decidida pelo monarca absolutista e a Vontade de Todos é a opinião do clero.",
        "A Vontade de Todos é a mera soma aritmética de interesses privados e egoístas; a Vontade Geral olha unicamente para o bem comum e o interesse coletivo indivisível.",
        "A Vontade Geral aplica-se exclusivamente a questões de diplomacia e a de Todos à cobrança de impostos.",
        "A Vontade Geral é sorteada anualmente e a de Todos é votada em assembleias de generais.",
        "Ambas as expressões são sinônimos perfeitos utilizados indiferentemente no texto da obra.",
        "B",
        "A Vontade de Todos é facciosa (cada um vota para enriquecer seu bolso); a Vontade Geral é ética e desinteressada (os cidadãos deliberam pensando no que é justo para a comunidade inteira)."
    ))

    questoes_brutas.append((
        12, "EM13CHS101", "basico",
        "Qual é a definição rousseauniana de 'Liberdade Civil' formulada em Do Contrato Social?",
        "A possibilidade de fazer qualquer coisa que se deseje sem prestar contas a autoridade alguma.",
        "A autonomia ética consistente na obediência voluntária à lei justa que nós mesmos nos prescrevemos como corpo soberano.",
        "O direito de comerciar especiarias nas praças municipais sem o pagamento de tributos.",
        "A permissão para residir em habitações construídas sobre terras comunais abandonadas.",
        "A faculdade de mudar de religião a cada estação do calendário astronômico anual.",
        "B",
        "A verdadeira liberdade não é o capricho instintivo dos animais; é a autonomia: quando obedecemos a uma lei que nós mesmos elaboramos democraticamente, estamos sendo livres."
    ))

    questoes_brutas.append((
        13, "EM13CHS603", "basico",
        "O que Jean-Jacques Rousseau expressa com a célebre e paradoxal frase de que o cidadão recalcitrante será 'forçado a ser livre'?",
        "Que os indivíduos desobedientes devem ser acorrentados e obrigados a remar em galeras navais.",
        "Que o cidadão que se recusa a obedecer à Vontade Geral será constrangido pela comunidade a seguir a lei justa, sendo resgatado da escravidão de seus impulsos egoístas particulares para viver sob a razão soberana.",
        "Que os jovens que concluem os estudos escolares devem prestar serviço militar obrigatório nas colônias.",
        "Que as assembleias deliberativas municipais devem cancelar suas sessões plenárias no inverno.",
        "Que os comerciantes de trigo devem vender suas sacas pelo preço fixado por magistrados reais.",
        "B",
        "O indivíduo que quer os benefícios da vida civil sem cumprir as leis está sendo escravo de seu apetite particular; a comunidade o força a agir como cidadão ético e soberano."
    ))

    questoes_brutas.append((
        14, "EM13CHS602", "basico",
        "Por que Rousseau rejeita veementemente a 'Democracia Representativa' e critica o sistema parlamentar da Inglaterra de sua época?",
        "Porque os parlamentares britânicos utilizavam perucas brancas bordadas com fios de seda caros.",
        "Porque a soberania popular é inalienável e não pode ser representada: o povo inglês pensa que é livre, mas é livre apenas durante a eleição; logo após votar, volta a ser escravo de deputados que fazem o que querem.",
        "Porque as sessões do parlamento eram realizadas em horários que coincidiam com cultos religiosos.",
        "Porque os eleitores eram obrigados a pagar taxas em ouro para ingressarem nas zonas eleitorais.",
        "Porque a legislação eleitoral britânica proibia que agricultores participassem de debates públicos.",
        "B",
        "Para Rousseau, a vontade soberana não se delega: quem transfere o poder de legislar para representantes aliena a própria liberdade; as leis devem ser ratificadas diretamente pelo povo reunido."
    ))

    questoes_brutas.append((
        15, "EM13CHS102", "basico",
        "Qual é o método filosófico e sociológico formulado por Karl Marx e Friedrich Engels para analisar as transformações das sociedades humanas?",
        "O Positivismo Comtiano baseado na observação de fenômenos meteorológicos e marítimos.",
        "O Materialismo Histórico e Dialético, que compreende a história a partir das condições materiais de produção e da luta de classes real.",
        "O Idealismo Especulativo hegeliano que deduz a realidade a partir das marchas do Espírito Absoluto.",
        "O Ceticismo Pirrônico que recusa a possibilidade de conhecer as causas dos eventos históricos.",
        "A Escolástica tomista que subordina a economia aos mandamentos do direito canônico medieval.",
        "B",
        "Marx e Engels viraram Hegel de cabeça para cima: não são as ideias que criam a história material, mas o modo como os seres humanos produzem e reproduzem seus meios de subsistência."
    ))

    questoes_brutas.append((
        16, "EM13CHS601", "basico",
        "No texto programático publicado por Karl Marx e Friedrich Engels às vésperas das revoluções europeias de 1848, os autores inauguram o Manifesto Comunista com uma afirmação categórica sobre o motor dos acontecimentos históricos. Qual postulado sintetiza essa dinâmica material dos conflitos humanos?",
        "A história da humanidade é o desdobramento pacífico da Providência Divina sobre os povos.",
        "A história de todas as sociedades até os nossos dias é a história da luta de classes.",
        "O Estado moderno é a realização definitiva da razão ética e da harmonia universal dos homens.",
        "A economia industrial floresce espontaneamente onde não existem leis civis restritivas.",
        "As guerras entre nações decorrem unicamente da vaidade de monarcas e generais militares.",
        "B",
        "De homens livres e escravos a patrícios e plebeus, e de burgueses e proletários: a história humana é impulsionada pelos conflitos entre classes opressoras e exploradas."
    ))

    questoes_brutas.append((
        17, "EM13CHS602", "basico",
        "Como a arquitetura conceitual marxista divide a estrutura da sociedade entre 'Infraestrutura' e 'Superestrutura'?",
        "Infraestrutura são os portos marítimos e Superestrutura são os veleiros de carga comercial.",
        "Infraestrutura é a base econômica material (forças produtivas e relações sociais de produção); Superestrutura é o edifício jurídico-político e ideológico (leis, Estado, moral, religião) erguido sobre ela.",
        "Infraestrutura são as residências rurais e Superestrutura são as catedrais de cidades urbanas.",
        "Infraestrutura são os canais de irrigação e Superestrutura são as estradas de ferro industriais.",
        "Infraestrutura são as fábricas têxteis e Superestrutura são os depósitos de carvão mineral.",
        "B",
        "A base econômica (quem é dono do quê e quem trabalha para quem) condiciona a política, o direito e as ideias dominantes da sociedade em cada época histórica."
    ))

    questoes_brutas.append((
        18, "EM13CHS101", "basico",
        "Qual é a célebre caracterização do Estado moderno apresentada por Marx e Engels no Manifesto Comunista?",
        "O Estado é o árbitro sagrado que assegura a justiça distributiva e a reconciliação moral de todos os cidadãos.",
        "O governo do Estado moderno não é mais do que um comitê para administrar os negócios comuns de toda a classe burguesa.",
        "O Estado é uma federação cooperativa gerida de forma autônoma por sindicatos operários.",
        "O Estado é um monumento arquitetônico que abriga relíquias religiosas de santos mártires.",
        "O Estado é um órgão neutro que atua para proteger exclusivamente os trabalhadores rurais desfavorecidos.",
        "B",
        "Marx arranca a máscara de imparcialidade do Estado burguês: as leis, a polícia e as cortes operam para garantir a propriedade privada e a extração ininterrupta de lucros pelos capitalistas."
    ))

    questoes_brutas.append((
        19, "EM13CHS102", "basico",
        "O que Karl Marx desmistifica em sua obra 'Sobre a Questão Judaica' (1844) ao comparar a 'Emancipação Política' com a 'Emancipação Humana'?",
        "Demonstra que o direito de voto foi concedido exclusivamente a navegadores de caravelas comerciais.",
        "Evidencia que a emancipação política do liberalismo concede igualdade puramente formal perante a lei, deixando intacta a escravidão e a desigualdade material real da vida social concreta.",
        "Afirma que os tribunais criminais europeus deveriam abolir a cobrança de custas processuais.",
        "Defende que os cidadãos franceses deveriam ser obrigados a prestar serviços em vinícolas públicas.",
        "Comprova que as leis eleitorais britânicas eram redigidas por comitês de monges cistercienses.",
        "B",
        "Na lei burguesa, o milionário e o mendigo têm o 'mesmo direito' formal de comer ou jejuar; a emancipação política é abstrata, enquanto a emancipação humana exige superar a exploração real."
    ))

    questoes_brutas.append((
        20, "EM13CHS603", "basico",
        "Qual é o horizonte final da sociedade emancipada no pensamento de Karl Marx e Friedrich Engels?",
        "A transformação do Estado em um império burocrático permanente dotado de forças policiais infinitas.",
        "A abolição progressiva das classes sociais, a superação da exploração e o consequente definhamento e extinção do Estado, surgindo uma livre associação de produtores emancipada.",
        "A restauração perpétua de assembleias corporativas de nobres de linhagem aristocrática.",
        "A divisão do globo terrestre em pequenas repúblicas agrárias isoladas sem comunicação tecnológica.",
        "A nomeação de filósofos acadêmicos como ministros perpétuos de planejamento industrial.",
        "B",
        "Como o Estado só existe para reprimir uma classe em benefício de outra, sem classes sociais ele perde sua função coercitiva: o Estado definha e morre de inanição histórica no comunismo."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "De que modo a experiência pioneira do 'Orçamento Participativo' (OP) em Porto Alegre e em outras cidades do mundo expressa os ideais de Rousseau?",
        "Transferindo todas as verbas municipais para o pagamento de dívidas a bancos estrangeiros.",
        "Possibilitando que os próprios cidadãos reunidos em assembleias populares debatam e deliberem diretamente sobre as prioridades de investimento público de sua cidade, resgatando a soberania direta contra a tecnocracia burocrática distante.",
        "Obrigando todos os moradores de bairros periféricos a assinarem termos notariais de vassalagem.",
        "Exigindo que os vereadores municipais aprovem planos de urbanização por aclamação unânime.",
        "Determinando que as obras públicas devam ser executadas exclusivamente por regimentos de infantaria.",
        "B",
        "O Orçamento Participativo corporifica a tese rousseauniana da soberania popular inalienável: a comunidade decide diretamente sobre o destino comum do dinheiro público."
    ))

    questoes_brutas.append((
        22, "EM13CHS601", "intermediario",
        "Como a decisão histórica do STF na ADI 4650 (que baniu o financiamento empresarial de campanhas no Brasil em 2015) dialoga com a crítica marxista ao Estado?",
        "Confirmando que as grandes corporações agiam por pura benevolência altruísta sem esperar retorno financeiro.",
        "Demonstrando empiricamente como as doações milionárias de bancos e empreiteiras funcionavam para colonizar os mandatos parlamentares e transformar o parlamento em comitê de negócios dos financiadores econômicos.",
        "Provando que as eleições presidenciais deveriam ser suspensas durante períodos de crise inflacionária.",
        "Estabelecendo que os partidos políticos brasileiros devem prestar contas a tribunais comerciais europeus.",
        "Mostrando que a cidadania política depende do patrimônio imobiliário registrado em cartório.",
        "B",
        "Ao banir a compra empresarial da política, o tribunal reconheceu o que Marx apontara no século XIX: quem financia a campanha captura o Estado para extrair lucros e isenções tributárias."
    ))

    questoes_brutas.append((
        23, "EM13CHS602", "intermediario",
        "De que maneira a precarização do trabalho por aplicativos (uberização) desvela o fosso entre a igualdade liberal formal e a realidade material diagnosticada por Marx?",
        "Mostrando que os entregadores ciclistas tornaram-se proprietários acionistas de empresas de tecnologia digital.",
        "Revelando que, sob a roupagem jurídica de 'empreendedor autônomo dono do seu tempo' (emancipação formal), o trabalhador é desprovido de meios de produção e submetido a jornadas degradantes sem direitos para enriquecer acionistas corporativos (exploração real).",
        "Comprovando que os aplicativos de entrega foram criados por associações cooperativas de padeiros.",
        "Demonstrando que os motoristas de transporte utilizam veículos doados por comitês sindicais estatais.",
        "Provando que os algoritmos de entrega operam orientados por princípios éticos rousseaunianos.",
        "B",
        "A ideologia liberal prega a falsa liberdade do trabalhador desregulamentado; o materialismo histórico expõe a dura realidade: jornadas extenuantes sem proteção e extração brutal de mais-valia."
    ))

    questoes_brutas.append((
        24, "EM13CHS102", "intermediario",
        "Por que é um erro primário atribuir a Jean-Jacques Rousseau a proposta de que a humanidade deveria destruir as cidades e voltar a viver nua nas florestas?",
        "Porque o filósofo defendia que todas as florestas europeias deveriam ser desmatadas para o cultivo de uvas.",
        "Porque Rousseau deixou evidente que o estado de natureza é irrecuperável na história e que a redenção da humanidade reside na construção de uma República justa e virtuosa pelo Contrato Social legítimo.",
        "Porque o autor foi contratado como arquiteto oficial de fortificações militares pelo rei da França.",
        "Porque as assembleias populares suíças proibiam o banho de rio em períodos de inverno rigoroso.",
        "Porque o pensador genebrino considerava a vida rural degradante e elogiava o luxo das cortes absolutistas.",
        "B",
        "Rousseau respondeu a Voltaire que não pretendia fazer ninguém andar de quatro patas: o remédio para os vícios da sociedade é a república democrática e a educação moral, não a barbárie primitiva."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "Como a experiência da 'Comuna de Paris de 1871' forneceu a Marx e Engels o laboratório histórico de uma nova forma política operária?",
        "Demonstrando a eficiência dos regimentos de infantaria imperial na manutenção de tributos alfandegários.",
        "Revelando medidas como a substituição do exército permanente pelo povo armado, a elegibilidade e revogabilidade de todos os cargos públicos e salários operários para os magistrados e representantes da comuna.",
        "Comprovando que a produção manufatureira deveria ser gerida por congregações religiosas beneditinas.",
        "Exigindo que os tratados diplomáticos fossem assinados unicamente em noites de lua cheia.",
        "Restaurando a monarquia absoluta tradicional da dinastia dos Bourbon no palácio de Versalhes.",
        "B",
        "Na Comuna de Paris, a classe operária mostrou pela primeira vez como desmantelar o Estado burguês: o poder foi descentralizado, desburocratizado e exercido diretamente pelos trabalhadores."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "De acordo com a teoria econômica de Marx desenvolvida em O Capital, o que é a 'Mais-Valia' e como ela alimenta o Estado burguês?",
        "É a soma dos juros cobrados por casas de penhores municipais sobre ferramentas agrícolas.",
        "É o excedente de valor produzido pelo trabalhador assalariado que não é remunerado no salário e é apropriado privadamente pelo capitalista, cuja reprodução é garantida pelas leis do Estado.",
        "É o imposto predial cobrado anualmente pelas prefeituras municipais sobre edifícios comerciais.",
        "É a taxa alfandegária paga por mercadores de especiarias na entrada de portos litorâneos.",
        "É o desconto financeiro concedido por indústrias fabris a clientes que compram mercadorias em atacado.",
        "B",
        "A mais-valia é o coração da exploração capitalista: o operário trabalha oito horas, seu salário cobre apenas quatro e as quatro restantes ficam de graça para o patrão, sob a proteção da lei do Estado."
    ))

    questoes_brutas.append((
        27, "EM13CHS601", "intermediario",
        "Como a ala radical da Revolução Francesa (os Jacobinos liderados por Robespierre) se inspirou diretamente no pensamento de Rousseau?",
        "Defendendo a restauração perpétua dos privilégios tributários de duques e príncipes de sangue.",
        "Invocando os conceitos de soberania popular inalienável, igualdade civil intransigente, culto à Vontade Geral e virtude republicana para justificar a abolição da monarquia e o terror revolucionário.",
        "Propondo a rendição militar imediata das forças republicanas aos exércitos da coroa britânica.",
        "Exigindo que os deputados da Convenção Nacional fossem escolhidos exclusivamente entre banqueiros parisienses.",
        "Determinando que a administração judiciária da capital francesa fosse entregue ao Papa de Roma.",
        "B",
        "Robespierre carregava Do Contrato Social debaixo do braço: para os jacobinos, a república devia ser o reino da virtude e da igualdade, onde a Vontade Geral aniquila a traição aristocrática."
    ))

    questoes_brutas.append((
        28, "EM13CHS602", "intermediario",
        "Qual é a crítica de Rousseau ao conceito de 'Representação Parlamentar' no que tange à corrupção da vontade soberana dos cidadãos?",
        "Afirma que os deputados parlamentares deveriam receber remunerações pagas exclusivamente em lingotes de prata.",
        "Sustenta que a representação transforma a cidadania ativa em comodismo preguiçoso: quando os cidadãos nomeiam deputados para cuidarem da pátria no lugar deles, a república está perdida e a liberdade é aniquilada.",
        "Comprova que os discursos oratórios proferidos em parlamentos prejudicam o rendimento de colheitas agrícolas.",
        "Exige que os edifícios legislativos sejam erguidos fora do perímetro urbano das cidades capitais.",
        "Determina que os votos parlamentares devam ser depositados em urnas lacradas com cera de abelha.",
        "B",
        "Para Rousseau, 'a soberania não pode ser representada pela mesma razão que não pode ser alienada': assim que um povo nomeia representantes, ele deixa de ser livre e perde sua dignidade cívica."
    ))

    questoes_brutas.append((
        29, "EM13CHS102", "intermediario",
        "Em que medida a crítica marxista diferencia o 'Socialismo Utópico' (Saint-Simon, Fourier e Owen) do 'Socialismo Científico' de Marx e Engels?",
        "Os utópicos defendiam o uso de bombas atômicas industriais contra parlamentos monárquicos.",
        "Os utópicos acreditavam ingenuamente que a justiça social brotaria da boa-vontade moral das elites burguesas através de modelos ideais abstratos; o socialismo científico analisa a luta de classes material real.",
        "Os utópicos propunham a privatização imediata de todas as ferrovias e canais fluviais da Europa.",
        "O socialismo científico defende o retorno à economia feudal e a restauração de corporações medievais.",
        "Ambas as correntes rejeitavam a industrialização e propunham o fim do uso de máquinas a vapor.",
        "B",
        "Marx zombou dos sonhos dos utópicos de convencer os ricos a serem bonzinhos: a emancipação humana não virá de caridade burguesa, mas da organização e insurreição consciente da classe trabalhadora."
    ))

    questoes_brutas.append((
        30, "EM13CHS603", "intermediario",
        "Como a construção histórica do 'Estado de Bem-Estar Social' (Welfare State) na Europa pós-1945 expressou um pacto defensivo diante da ameaça revolucionária marxista?",
        "Extinguindo totalmente a circulação de dinheiro e fechando todos os bancos privados da Europa.",
        "Concedendo direitos trabalhistas, saúde pública, previdência e educação universal financiada por tributos progressivos para aplacar a insurreição operária e preservar o capitalismo sob controle democrático.",
        "Obrigando todas as indústrias fabris a terceirizarem suas diretorias a conselhos militares da OTAN.",
        "Restaurando o poder imperial dos nobres de sangue na cobrança de dízimos territoriais feudais.",
        "Proibindo a fundação de sindicatos profissionais em todos os países do continente europeu.",
        "B",
        "Temendo que os operários seguissem o exemplo da Revolução Russa, a burguesia europeia aceitou dividir uma fatia da riqueza: o Welfare State garantiu direitos sociais para conter o fantasma comunista."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "De que modo a ofensiva 'Neoliberal' desencadeada nos anos 1980 (governos Margaret Thatcher e Ronald Reagan) desmontou as conquistas do Welfare State à luz da teoria de Marx?",
        "Substituindo os governos parlamentares por assembleias operárias de tipógrafos artesanais.",
        "Promovendo desregulamentações financeiras, privatizações de serviços públicos e cortes em direitos trabalhistas e sociais para recompor as taxas de lucro e desarmar o poder de negociação da classe trabalhadora.",
        "Determinando que as empresas transnacionais devam doar suas ações a comitês comunitários paroquiais.",
        "Exigindo que as universidades públicas fechem seus cursos de economia para abrir vagas em agronomia.",
        "Comprovando que o capitalismo fabril dispensa o uso de moedas de circulação fiduciária bancária.",
        "B",
        "O neoliberalismo representou o contra-ataque da burguesia: quando as taxas de lucro caíram, o Estado agiu como comitê de negócios para desmantelar os direitos sociais e privatizar os bens coletivos."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Por que Rousseau sustenta que em uma República virtuosa e bem constituída 'nenhum cidadão deve ser tão opulento a ponto de poder comprar outro, e nenhum tão pobre a ponto de ser forçado a se vender'?",
        "Porque os mercados municipais deveriam adotar preços tabelados por astrólogos da corte.",
        "Porque a extrema desigualdade econômica destrói a igualdade política formal: o super-rico compra os votos e a lealdade das leis, e o miserável faminto vende a sua liberdade e dignidade por comida.",
        "Porque as leis civis de Genebra proibiam o consumo de café importado de colônias ultramarinas.",
        "Porque as assembleias cívicas exigiam que todos os cidadãos tivessem armaduras de idêntico peso.",
        "Porque a cobrança de tributos municipais deveria ser realizada em tecidos de linho cru.",
        "B",
        "A igualdade jurídica vira farsa onde a desigualdade material é abissal: para Rousseau, a república exige moderação e dignidade para que a liberdade de todos seja respeitada sem compras de consciência."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "Para fortalecer o vínculo de fraternidade cívica e assegurar o respeito às leis da república sem recorrer ao fanatismo teocrático, o filósofo genebrino introduz a noção de 'Religião Civil'. Em que consiste essa formulação no desfecho de sua obra magna?",
        "A imposição forçada do catolicismo romano medieval com fogueiras inquisitoriais nas praças.",
        "Uma profissão de fé puramente cívica cujos dogmas simples (como a sacralidade do contrato social e das leis e a condenação da intolerância) reforçam o amor à pátria e o cumprimento dos deveres de cidadão.",
        "A adoração obrigatória aos deuses pagãos do panteão da Grécia arcaica durante festivais públicos.",
        "A extinção compulsória de todas as manifestações espirituais e o fechamento de templos e igrejas.",
        "A nomeação de generais de artilharia como bispos honorários de paróquias municipais.",
        "B",
        "Rousseau recusa o fanatismo teocrático e o cinismo materialista: a república precisa de uma religião civil que ensine a fraternidade, a tolerância e o respeito sagrado às leis que unem a comunidade."
    ))

    questoes_brutas.append((
        34, "EM13CHS602", "intermediario",
        "Como Karl Marx e Friedrich Engels caracterizam a 'Ideologia' em obras como A Ideologia Alemã (1846)?",
        "Um conjunto de técnicas de medição de terrenos agrícolas desenvolvido por engenheiros prussianos.",
        "Uma falsa consciência e um sistema de representações invertidas da realidade que apresenta os interesses particulares da classe dominante como se fossem o interesse universal e natural de toda a sociedade.",
        "Um manual de gramática clássica utilizado para padronizar a redação de despachos consulares.",
        "A devoção mística praticada por operários têxteis em templos de pequenas vilas fabris.",
        "Uma formulação matemática destinada a prever os movimentos de marés no oceano Atlântico.",
        "B",
        "A ideologia faz o explorado enxergar o mundo com os olhos do opressor: 'as ideias da classe dominante são, em todas as épocas, as ideias dominantes', naturalizando a exploração como se fosse destino justo."
    ))

    questoes_brutas.append((
        35, "EM13CHS603", "intermediario",
        "Em que sentido o conceito de 'Alienação' (*Entfremdung*) em Karl Marx supera a abordagem meramente filosófica de Hegel e Feuerbach?",
        "Deslocando a alienação do campo das especulações metafísicas para o terreno da produção material: no trabalho assalariado capitalista, o trabalhador é desapropriado do produto de seu esforço, do processo de produção, de sua humanidade genérica e de seus semelhantes.",
        "Demonstrando que os operários das fábricas britânicas sofriam de enfermidades visuais hereditárias.",
        "Provando que a alienação é causada exclusivamente pelo consumo excessivo de pães de farinha branca.",
        "Defendendo que a alienação pode ser curada mediante leituras silenciosas de poemas românticos nas praças.",
        "Exigindo que os proprietários industriais aumentem o número de janelas nas oficinas de tecelagem.",
        "B",
        "Para Marx, a alienação não é um desvio psicológico abstrato: o operário derrama sua vida no objeto que fabrica, mas esse objeto é roubado pelo patrão e se volta contra ele como mercadoria inatingível."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Por que, para Jean-Jacques Rousseau, a Vontade Geral 'é sempre reta e tende sempre à utilidade pública', embora as deliberações do povo possam por vezes se enganar?",
        "Porque os cidadãos recebem revelações místicas sopradas por profetas da igreja local.",
        "Porque o povo quer sempre o seu próprio bem, mas nem sempre o vê com clareza; se a comunidade for manipulada por facções políticas egoístas, a deliberação popular é iludida e desvia-se do bem comum.",
        "Porque as decisões assembleares são ratificadas por comissões de generais condecorados.",
        "Porque a legislação suíça exigia a aplicação de testes de lógica aos votantes nas urnas.",
        "Porque as urnas eleitorais eram abençoadas por sacerdotes de ordens monásticas antigas.",
        "B",
        "A Vontade Geral é a norma ética da justiça comum: ela nunca erra em sua essência; o que erra é o julgamento do povo quando este é ludibriado por demagogos e grupos de interesse privado."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "Qual é o papel da 'Classe Trabalhadora' (o Proletariado) como sujeito histórico revolucionário na teoria do materialismo histórico marxista?",
        "Atuar como eleitorado passivo que delega o poder político a dinastias industriais benevolentes.",
        "Por ser a classe que nada tem a perder a não ser seus próprios grilhões e que não possui privilégios de propriedade para defender, a emancipação do proletariado carrega em si a emancipação de toda a humanidade.",
        "Subordinar suas reivindicações salariais às diretrizes de exportação de companhias mercantis marítimas.",
        "Dedicar suas horas vagas à escultura de monumentos cívicos dedicados aos generais da pátria.",
        "Comprar ações em bolsas de valores internacionais para transformar os operários em banqueiros.",
        "B",
        "O proletariado é a classe universal: para libertar a si mesmo da escravidão assalariada, precisa abolir a própria propriedade privada dos meios de produção, libertando a humanidade inteira da exploração."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Ao confrontar o modelo de Rousseau com o de Karl Marx, qual é a divergência fundamental sobre a 'Propriedade Privada' como solução para a desigualdade?",
        "Rousseau defendia o capitalismo de corporações financeiras e Marx propunha a escravidão agrária.",
        "Rousseau propõe uma república de pequenos proprietários onde a posse seja moderada e justa, sem grandes desigualdades; Marx sustenta que a igualdade autêntica exige a abolição radical da propriedade privada dos meios de produção.",
        "Rousseau exigia a entrega de todas as terras aos bispos católicos e Marx a monges beneditinos.",
        "Ambos defendiam que a terra deveria pertencer exclusivamente aos comandantes de frotas navais.",
        "Ambos consideravam a propriedade privada sagrada e intocável, condenando qualquer reforma social.",
        "B",
        "Rousseau é um republicano democrático que quer frear a desigualdade limitando a riqueza para todos terem um pouco; Marx é o comunista radical que quer abolir a propriedade privada dos meios de produção."
    ))

    questoes_brutas.append((
        39, "EM13CHS602", "intermediario",
        "Como a crítica de Rousseau à Ciência e às Artes em seu primeiro Discurso (1750) já antecipava o diagnóstico da corrupção civilizatória moderna?",
        "Afirmando que a música lírica provocava epidemias infecciosas nas cidades costeiras da França.",
        "Denunciando que o progresso técnico, artístico e científico não tornou os homens mais virtuosos nem mais felizes, servindo apenas para cobrir de flores os grilhões da tirania e alimentar o luxo e a vaidade hipócrita.",
        "Exigindo que todos os livros de física e astronomia fossem queimados em praças públicas de Paris.",
        "Provando que as academias de ciências deveriam ser administradas por marinheiros mercantes.",
        "Defendendo que as esculturas em mármore deveriam ser substituídas por representações em bronze.",
        "B",
        "Rousseau escandalizou o Iluminismo: o avanço das ciências e das artes sofisticou o egoísmo e o luxo das elites sem melhorar a moral dos homens; a civilização avançou no saber, mas retrocedeu na ética."
    ))

    questoes_brutas.append((
        40, "EM13CHS603", "intermediario",
        "De que modo a crítica de Marx e Engels aos Direitos Humanos liberais na sociedade capitalista não representa a rejeição da liberdade, mas a exigência de sua realização concreta?",
        "Negando aos cidadãos o direito de lerem jornais e manifestarem opiniões dissidentes nas praças.",
        "Demonstrando que as liberdades civis liberais (de expressão, de ir e vir, de imprensa) permanecem como privilégios formais inacessíveis a quem padece na miséria, exigindo a superação da opressão econômica para que a liberdade se torne realidade tangível para todos.",
        "Afirmando que as cartas de direitos constitucionais deveriam ser lavradas em folhas de linho cru.",
        "Provando que a liberdade individual é um capricho que deve ser exterminado por tribunais militares.",
        "Defendendo que as decisões judiciais devam ser tomadas por comitês secretos de generais da corte.",
        "B",
        "Marx não é contra a liberdade; é contra a hipocrisia de chamar de 'livre' o trabalhador faminto que é obrigado a aceitar salários de miséria para não morrer de fome; a liberdade exige igualdade material real."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60 - Com Etapas 1 e 2)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a ruptura radical entre a justificativa lockeana da propriedade privada fundada no 'Trabalho Virtuoso' e a denúncia rousseauniana da 'Usurpação Originária': de que modo esse embate desconstrói a naturalização da desigualdade social na modernidade?",
        "Comprovando que os agricultores familiares deveriam pagar tributos reais sobre instrumentos de ferro.",
        "Evidenciando que, enquanto Locke apresenta a apropriação privada como um ato nobre que agrega valor à natureza e beneficia a humanidade, Rousseau desmascara esse gesto como o ato violento de apossamento de bens comuns a todos, gerador da servidão e da miséria que a lei burguesa posterior buscou blindar com o verniz da legitimidade.",
        "Determinando que os títulos de propriedade devam ser autenticados unicamente por tribunais eclesiásticos.",
        "Provando que os solos agrícolas britânicos foram cultivados por marinheiros mercantes que viajavam pelo mar Báltico.",
        "Afirmando que a expansão das fronteiras territoriais decorreu da celebração de alianças matrimoniosas dinásticas.",
        "B",
        "- **Etapa 1:** Resgatar a legitimação liberal de Locke: o trabalho individual misturado à terra virgem cria o direito sagrado de posse, beneficiando a todos pela abundância produtiva gerada.\n- **Etapa 2:** Evidenciar a desmistificação radical de Rousseau: cercar o solo que era de todos e dizer 'isto é meu' foi uma fraude histórica; quem lucrou privatizou o bem coletivo e empurrou os demais para a fome, instituindo a desigualdade civil contra a lei da natureza."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Em Do Contrato Social, Rousseau sentencia: 'Se considerarmos bem, veremos que a Vontade Geral é sempre reta; mas o julgamento que a guia nem sempre é esclarecido.' Analise as causas sociopolíticas que levam as assembleias populares democráticas a se desviarem do Bem Comum e a votarem contra os próprios interesses coletivos.",
        "A interferência de tempestades oceânicas nos calendários eleitorais de cidades litorâneas.",
        "A formação de facções corporativas, partidos facciosos e conluios de interesses privados que seduzem e desinformam a cidadania, fazendo com que o povo vote em benefício exclusivo de elites ambiciosas sob o engano de que está deliberando pela utilidade comum.",
        "A falta de uniformidade nas vestimentas dos magistrados durante as sessões plenárias de tribunais penais.",
        "A exigência de que os cidadãos prestassem juramentos de fidelidade militar a líderes de infantaria.",
        "A decisão de conselhos monásticos de suspender a circulação de livros didáticos encadernados em couro.",
        "B",
        "- **Etapa 1:** Definir a retidão em si mesma da Vontade Geral: o corpo do povo quer sempre a própria preservação, a justiça e o bem da comunidade inteira.\n- **Etapa 2:** Diagnosticar o veneno das facções e da desinformação: quando grupos de interesse particular financiam narrativas e criam associações parciais, o cidadão perde de vista o todo e vota pelo interesse de sua seita; a democracia degenera na vontade de todos manipulada."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "No capítulo XV de Do Contrato Social, Rousseau formula uma advertência severa: 'Assim que alguém diz dos negócios do Estado: Que me importa?, o Estado pode ser considerado perdido.' Como esse postulado funda a ética da 'Cidadania Ativa' e a crítica à apatia política e ao individualismo consumista contemporâneo?",
        "Exigindo que os parlamentos municipais cobrem multas em dinheiro de cidadãos que não assistem a desfiles cívicos.",
        "Demonstrando que a república democrática e a liberdade civil exigem a vigilância diária e a dedicação consciente de cada cidadão aos assuntos públicos; quando a sociedade é tomada pelo egoísmo individualista e delega tudo a burocratas e profissionais do voto, a liberdade se dissolve e a tirania se instala.",
        "Comprovando que os tratados de comércio internacional dispensam a aprovação por câmaras legislativas.",
        "Determinando que os cidadãos devam prestar serviços voluntários em oficinas de tecelagem da corte.",
        "Provando que a estabilidade social depende da proibição da realização de reuniões de vizinhança nas ruas.",
        "B",
        "- **Etapa 1:** Diagnosticar a patologia da apatia cívica: o cidadão que se tranca em seu bem-estar privado e se desinteressa do destino coletivo abre mão de seu estatuto de soberano.\n- **Etapa 2:** Concluir com a exigência rousseauniana da liberdade ativa: a democracia não é um espetáculo para ser assistido do sofá; ela é uma prática cotidiana de corresponsabilidade cívica; abandonar o espaço público é entregar a república de bandeja a tiranos e oligarcas."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Analise a crítica de Karl Marx ao 'Ilusionismo Jurídico do Estado Burguês': de que maneira a consagração solene da igualdade de todos perante a lei nas constituições liberais opera como mecanismo ideológico de legitimação da dominação de classe?",
        "Provando que os juízes de tribunais constitucionais recebiam salários pagos em especiarias da Índia.",
        "Evidenciando que a igualdade jurídica formal abstrai deliberadamente as desigualdades materiais de classe, tratando sujeitos economicamente desiguais (o proprietário do capital e o operário despossuído) como se fossem parceiros livres em um contrato comercial, ocultando a coação material que obriga o proletário a se vender para não perecer.",
        "Determinando que as cartas constitucionais devam prever a suspensão de assembleias populares no outono.",
        "Afirmando que a cobrança de tributos municipais decorre de sentenças lavradas por conselhos de monges.",
        "Exigindo que os operários de indústrias têxteis prestem juramentos de lealdade a comissões diplomáticas.",
        "B",
        "- **Etapa 1:** Revelar a abstração jurídica do cidadão formal: a lei liberal finge que a sociedade é composta por átomos iguais e livres que contratam voluntariamente no mercado.\n- **Etapa 2:** Desvelar a violência material oculta pelo direito burguês: a igualdade jurídica é o escudo que proíbe igualmente o milionário e o mendigo de furtar pão e dormir na ponte; na prática, protege a propriedade privada e chancela a exploração do trabalhador sem alternativas de sobrevivência."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Ao examinar a concepção materialista da história, Marx formula a célebre passagem no Prefácio de Para a Crítica da Economia Política (1859): 'Não é a consciência dos homens que determina o seu ser, mas, pelo contrário, o seu ser social que determina a sua consciência.' Analise as consequências dessa inversão dialética para a Filosofia Política e para a Teoria do Conhecimento.",
        "Afirmando que a criatividade humana decorre exclusivamente de transmissões genéticas hereditárias.",
        "Subvertendo o idealismo filosófico clássico ao demonstrar que os sistemas jurídicos, os valores éticos, as instituições políticas e as ideologias dominantes não são produtos puros da razão autônoma no vácuo, mas reflexos articulados das relações materiais de produção e das lutas de classes concretas de cada época histórica.",
        "Comprovando que as constituições democráticas antigas foram redigidas por marinheiros em alto-mar.",
        "Exigindo que os historiadores devam analisar os fatos sociais a partir da leitura de cartas astrológicas medievais.",
        "Determinando que a evolução científica depende da proibição da fabricação de máquinas a vapor fabris.",
        "B",
        "- **Etapa 1:** Identificar o paradigma idealista superado: Hegel e os contratualistas acreditavam que as ideias da mente humana criavam o Estado e organizavam as relações sociais de cima para baixo.\n- **Etapa 2:** Consagrar o fundamento materialista histórico de Marx: o modo como os seres humanos trabalham, produzem mercadorias e se dividem em classes na vida material concreta é o solo real onde brotam as leis, a moral, a política e a cultura da sociedade."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Em O 18 de Brumário de Luís Bonaparte (1852), Karl Marx investiga a ascensão autoritária de Napoleão III na França e formula o conceito de 'Autonomia Relativa do Estado'. Como essa obra complexifica a tese simplista de que o Estado é apenas um 'marionete mecânico' da burguesia?",
        "Provando que os governantes absolutistas agiam orientados por conselhos de astrônomos do império.",
        "Demonstrando que, em situações históricas de paralisia e empate de forças entre classes em conflito, a máquina burocrática e militar do Estado pode se autonomizar aparentemente perante as classes em luta, agindo como árbitro autocrático supremo para salvar a própria ordem capitalista da ameaça revolucionária proletária.",
        "Comprovando que as assembleias parlamentares francesas foram dissolvidas por corporações de sapateiros.",
        "Determinando que os generais de brigada militar deveriam prestar contas financeiras a conventos rurais.",
        "Afirmando que o golpe de Estado decorreu exclusivamente de desavenças linguísticas entre generais.",
        "B",
        "- **Etapa 1:** Afastar a leitura mecanicista vulgar de Marx: o Estado não é um mero fantoche que recebe ordens por telefone do banqueiro no dia a dia.\n- **Etapa 2:** Compreender o fenômeno bonapartista: quando a burguesia teme a revolução operária mas não consegue governar pelas vias parlamentares normais, ela abre mão de seu poder político direto em favor de um salvador da pátria autoritário (Luís Bonaparte) para preservar o seu poder econômico de classe."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Analise a relação teórica entre a 'Alienação Total' do indivíduo na Vontade Geral em Rousseau e as acusações de 'Totalitarismo' que pensadores liberais contemporâneos (como Isaiah Berlin e Karl Popper) dirigiram ao autor de Do Contrato Social:",
        "Comprovando que Rousseau propôs a extinção imediata de todos os tribunais de justiça penal da Europa.",
        "Evidenciando que os críticos liberais acusam a tese de 'forçar o cidadão a ser livre' e a supremacia absoluta da Vontade Geral de abrirem perigosos precedentes para regimes autoritários esmagarem as dissidências individuais e a liberdade negativa em nome de um Bem Comum abstrato imposto pelo Estado; enquanto os defensores de Rousseau sustentam que o pacto garante a igualdade radical contra a opressão dos poderosos.",
        "Determinando que as assembleias populares devam ser chefiadas exclusivamente por generais militares.",
        "Provando que as ordenações jurídicas das repúblicas suíças foram redigidas por marinheiros de galeras fluviais.",
        "Afirmando que a soberania popular democrática dispensa a realização de votações públicas nas cidades.",
        "B",
        "- **Etapa 1:** Apresentar a crítica liberal da liberdade negativa (Berlin/Popper): ao proclamar que quem discorda da Vontade Geral deve ser 'forçado a ser livre', Rousseau forneceria munição ideológica para déspotas e jacobinos justificarem o Terror em nome do povo.\n- **Etapa 2:** Apresentar a defesa republicana rousseauniana: para Rousseau, a Vontade Geral só é legítima se emanar do povo todo e aplicar-se a todos com rigorosa igualdade; não há déspota ou vanguarda: ser forçado a ser livre é simplesmente a garantia contra a tirania do mais forte."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Ao examinar a tese do 'Definhamento do Estado' (*Absterben des Staates*) em Friedrich Engels e Karl Marx, qual distinção conceitual fundamental separa a teoria comunista do projeto dos 'Anarquistas' (como Bakunin e Kropotkin)?",
        "Os anarquistas defendiam a monarquia absoluta e os marxistas a teocracia clerical de monges.",
        "Enquanto os anarquistas exigem a abolição imediata e voluntarista do Estado por decreto na manhã seguinte à insurreição armada, os marxistas sustentam que a classe trabalhadora precisa assumir temporariamente o poder de Estado (a fase de transição socialista) para desmantelar o poder da burguesia e socializar a produção, sendo o desaparecimento do Estado uma decorrência natural da abolição das classes.",
        "Os comunistas defendiam o uso exclusivo de cavalos em transportes públicos urbanos.",
        "Os anarquistas sustentavam que as fábricas deveriam ser terceirizadas a companhias de navegação marítima.",
        "Ambas as correntes propunham a entrega do comando militar de cidades a ordens eclesiásticas.",
        "B",
        "- **Etapa 1:** Identificar o decreto voluntarista anarquista: Bakunin queria acordar e abolir o Estado por decreto na insurreição, sem perceber que a burguesia ainda teria poder armado para esmagar os operários.\n- **Etapa 2:** Consagrar o realismo materialista marxista: destruir a dominação exige a fase socialista de transição (a ditadura do proletariado) para reorganizar a economia; o Estado não se abole artificialmente: ele definha e desaparece quando as classes sociais deixarem de existir."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "No debate sobre a 'Desigualdade Salarial e de Gênero' no mercado de trabalho contemporâneo, de que modo o conceito marxista de 'Exército Industrial de Reserva' explica a manutenção de baixos salários e da precarização laboral em países periféricos?",
        "Provando que as indústrias fabris modernas dependem exclusivamente de caldeiras a vapor de carvão vegetal.",
        "Demonstrando que a existência permanente de uma massa considerável de trabalhadores desempregados, informais ou subocupados atua como mecanismo estrutural de pressão e chantagem sobre os trabalhadores empregados, forçando a classe trabalhadora a aceitar salários deprimidos e condições degradantes sob a ameaça constante de demissão e substituição imediata.",
        "Comprovando que as taxas de juros cobradas por bancos comerciais decorrem de rituais astronômicos de inverno.",
        "Exigindo que os códigos penais municipais imponham o uso de uniformes de lã cinza aos desempregados.",
        "Determinando que os contratos de trabalho assalariado devam ser lavrados em pergaminhos notariais selados.",
        "B",
        "- **Etapa 1:** Definir o exército industrial de reserva em Marx: uma superpopulação relativa de trabalhadores sem emprego que o próprio sistema capitalista gera e reproduz constantemente.\n- **Etapa 2:** Analisar sua função de controle salarial e disciplina: o operário na fábrica pensa duas vezes antes de fazer greve ou reivindicar direitos porque sabe que há dez pessoas famintas no portão prontas para aceitar a sua vaga por menos; o desemprego estrutural é arma de contenção salarial."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Analise a relação entre a 'Crítica de Rousseau à Propriedade Privada' e os desafios contemporâneos da 'Justiça Climática' e do colapso ecológico planetário provocado pelo extrativismo predatório:",
        "Comprovando que os tratados internacionais sobre o clima devem ser assinados unicamente por embaixadores navais.",
        "Demonstrando que a advertência pioneira de Rousseau ('estais perdidos se esquecerdes que os frutos pertencem a todos e que a terra não pertence a ninguém') antecipa com agudeza a denúncia contemporânea contra a mercantilização predatória dos bens comuns planetários (água, florestas, ar e biodiversidade), cuja apropriação e destruição por corporações transnacionais condenam a humanidade a catástrofes climáticas globais.",
        "Provando que as enchentes fluviais ocorrem unicamente em países que adotam constituições monárquicas.",
        "Exigindo que as agências de proteção ambiental fechem seus laboratórios de monitoramento de satélite.",
        "Determinando que as reservas florestais devam ser geridas exclusivamente por corporações de caçadores alpinos.",
        "B",
        "- **Etapa 1:** Resgatar a intuição ecológica radical de Rousseau no Segundo Discurso: a terra não tem dono particular; transformar a natureza comum em mercadoria privatizada é a semente do desastre ético e civilizatório.\n- **Etapa 2:** Conectar com a crise ambiental do século XXI: o aquecimento global e o desmatamento resultam da ganância que trata o planeta como reserva de lucro privado; a sobrevivência da humanidade exige recuperar a ética rousseauniana da terra como casa comum de todos."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Em Do Contrato Social, Rousseau afirma que 'o ato pelo qual um povo se submete a um soberano não é um contrato; é uma comissão, um emprego no qual os governantes são meros oficiais do soberano'. Como essa formulação subverte radicalmente a teoria do pacto de submissão de Thomas Hobbes?",
        "Autorizando os magistrados de tribunais superiores a governarem utilizando títulos nobiliárquicos hereditários.",
        "Desfazendo a alienação perpétua de poder postulada por Hobbes ao estabelecer que o povo não se submete a governante algum: o Soberano é o próprio povo unido; o governo é apenas um corpo intermediário encarregado de executar a Vontade Geral, podendo seus membros ser nomeados, fiscalizados e destituídos pelo povo soberano a qualquer momento.",
        "Comprovando que as forças policiais da capital devem ser terceirizadas a companhias privadas de segurança armada.",
        "Determinando que as sessões legislativas republicanas devem aprovar decretos por unanimidade matemática.",
        "Exigindo que os governantes devam prestar juramentos de fidelidade canônica perante autoridades de Roma.",
        "B",
        "- **Etapa 1:** Confrontar com a submissão cega hobbesiana: em Hobbes, os cidadãos entregam irrevogavelmente todos os seus poderes ao Leviatã e tornam-se súditos sem direito a destituí-lo.\n- **Etapa 2:** Consagrar a soberania popular inalienável de Rousseau: o povo nunca renuncia à sua soberania; os governantes são empregados e servos da cidadania; o governo é mero poder Executivo comissionado, revogável a qualquer instante pelo povo reunido em assembleia."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Analise a crítica de Karl Marx e Friedrich Engels ao 'Trabalho Assalariado' no modo de produção capitalista: por que os autores sustentam que o salário não paga o valor integral da riqueza gerada pelo trabalhador, mas apenas o custo estrito de sua reprodução biológica e social?",
        "Porque os administradores fabris desconheciam as regras de contabilidade por partidas dobradas em seus livros.",
        "Demonstrando que, sob as leis de mercado do capitalismo, o valor da força de trabalho equivale unicamente à quantidade de bens de subsistência (alimento, vestuário, moradia) estritamente necessária para manter o operário vivo e apto a retornar à fábrica no dia seguinte e gerar filhos trabalhadores, retendo o capitalista todo o excedente produtivo não pago (mais-valia).",
        "Comprovando que os tecidos manufaturados consumiam muito carvão vegetal para secagem em estufas fabris.",
        "Determinando que os operários das indústrias deveriam receber salários pagos em ferramentas de ferro fundido.",
        "Afirmando que as oscilações salariais decorriam do alinhamento astronômico de constelações celestes.",
        "B",
        "- **Etapa 1:** Desmistificar o conceito liberal de salário: a economia clássica dizia que o salário paga 'o trabalho feito' como uma troca justa de equivalentes.\n- **Etapa 2:** Evidenciar a descoberta materialista de Marx: o capitalista compra a mercadoria 'força de trabalho'; o salário cobre apenas o mínimo para o operário não morrer de fome e gerar nova prole de operários; todo o valor a mais criado na jornada é mais-valia embolsada pelo patrão."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "De que modo a tese de Rousseau sobre a 'Dependência dos Homens versus Dependência das Coisas' no Emílio e em Do Contrato Social fundamenta a sua aversão à servidão pessoal e ao despotismo?",
        "Sustentando que os cidadãos devem ser obrigados por lei a trabalhar exclusivamente em lavouras de trigo.",
        "Explicando que a dependência das coisas (a natureza, a chuva, a morte física) não gera desonra moral nem ressentimento, pois não carrega maldade ou arbítrio; mas a dependência pessoal e humilhante de um homem em relação à vontade caprichosa de outro homem (como do servo ao senhor) é a fonte de toda a vileza e corrupção humana, exigindo a mediação impessoal e igualitária da lei pública.",
        "Comprovando que as carruagens urbanas consumiam cavalos que deveriam ser preservados para o pastoreio rural.",
        "Determinando que os juízes de tribunais civis devem emitir suas decisões a partir da leitura de oráculos clássicos.",
        "Afirmando que os cidadãos republicanos devem evitar o comércio de mercadorias com povos vizinhos.",
        "B",
        "- **Etapa 1:** Distinguir os dois tipos de dependência: a dependência da natureza é física e comum a todos; ninguém se sente moralmente ofendido porque choveu ou porque a pedra é pesada.\n- **Etapa 2:** Condenar a dependência interpessoal arbitrária: ser humilhado pela vontade mesquinha de outro ser humano destrói a dignidade; a lei civil justa substitui a dependência do homem pela dependência impessoal da lei coletiva, garantindo a dignidade de iguais."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "Analise a crítica que a historiografia marxista dirige à Revolução Francesa de 1789: por que, apesar de sua retórica universalista de 'Liberdade, Igualdade e Fraternidade', a revolução é caracterizada pelo materialismo histórico como uma 'Revolução Burguesa'?",
        "Porque os revolucionários parisienses exigiram que as fábricas adotassem máquinas movidas a tração animal.",
        "Porque, embora tenha mobilizado a massa popular de camponeses e artesãos (*sans-culottes*) para destruir os privilégios feudais da nobreza e do clero, a liderança e os frutos econômicos e institucionais da revolução consagraram a ascensão da burguesia ao poder de Estado, consolidando a propriedade privada irrestrita e o modo de produção capitalista.",
        "Comprovando que os deputados da Assembleia Nacional Constituinte foram indicados por imperadores da Áustria.",
        "Determinando que as terras rurais desapropriadas deveriam ser entregues a corporações monásticas beneditinas.",
        "Afirmando que a tomada da fortaleza da Bastilha decorreu unicamente de desentendimentos sobre comércio marítimo.",
        "B",
        "- **Etapa 1:** Reconhecer o papel de vanguarda e retórica popular: o povo das ruas lutou nas barricadas e derrubou a Bastilha em nome da igualdade universal contra o absolutismo feudal.\n- **Etapa 2:** Evidenciar o resultado de classe material: quem conquistou as leis, os bancos e o poder real foi a burguesia mercantil e industrial; o feudalismo foi destruído para abrir caminho ao livre mercado, aos contratos capitalistas e à exploração do trabalho assalariado."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Ao examinar a relação entre Ideologia e Ciência na obra de Karl Marx, de que maneira a 'Crítica da Economia Política' busca desconstruir a pretensa naturalidade das leis de mercado capitalistas anunciadas por economistas clássicos (como Adam Smith e David Ricardo)?",
        "Demonstrando que os economistas clássicos britânicos utilizavam tabelas estatísticas redigidas em latim arcaico.",
        "Evidenciando que a economia política burguesa tratava categorias históricas e transitórias (como a mercadoria, o dinheiro, a propriedade privada dos meios de produção e o trabalho assalariado) como se fossem leis naturais eternas e imutáveis da condição humana, desvelando Marx que o capitalismo é uma formação histórica contingente e perecível, nascida de lutas sociais e fadada a ser superada.",
        "Comprovando que as bolsas de valores mercantis foram inventadas por marinheiros que navegavam no mar Negro.",
        "Exigindo que os tratados econômicos internacionais devam ser assinados unicamente durante o solstício de verão.",
        "Determinando que os bancos comerciais devam terceirizar suas auditorias a corporações de artesãos urbanos.",
        "B",
        "- **Etapa 1:** Desmascarar o dogma da naturalização econômica: Adam Smith dizia que o homem tem 'propensão natural à troca e ao lucro', como se o capitalismo sempre tivesse existido e fosse a única ordem possível.\n- **Etapa 2:** Consagrar a historicidade das relações materiais de Marx: o capitalismo teve um começo violento (a acumulação primitiva) e terá um fim histórico; as leis de mercado não são leis da física: são relações sociais de poder e podem ser transformadas revolucionariamente."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Em Do Contrato Social, Rousseau postula que 'para que a Vontade Geral seja verdadeiramente tal, ela deve ser geral tanto em seu objeto quanto em sua essência'. O que essa exigência teórica implica para o princípio da 'Universalidade da Lei' em um Estado republicano?",
        "Exige que as leis civis sejam votadas por cidadãos que comprovem a posse de fazendas agrícolas no interior.",
        "Estabelece que a lei soberana só é legítima se partir de todos os cidadãos (igualdade na autoria) e aplicar-se igualmente a todos os cidadãos (universalidade na destinação), sendo estritamente vedado ao corpo soberano criar leis privilegiadas para indivíduos ou punições dirigidas a pessoas nomeadas.",
        "Determina que os tribunais criminais municipais devam realizar julgamentos exclusivamente a portas fechadas.",
        "Comprova que as decisões assembleares perdem a validade jurídica quando ocorrem eclipses lunares na capital.",
        "Afirma que os decretos governamentais devem ser redigidos em dialetos poéticos de difícil compreensão.",
        "B",
        "- **Etapa 1:** Analisar a autoria universal da lei: a lei deve partir de todos; se apenas uma classe ou facção faz a lei, ela vira decreto de interesse particular e opressão.\n- **Etapa 2:** Analisar o alcance abstrato e impessoal da lei: a lei deve aplicar-se a todos; a Vontade Geral não legisla sobre João ou Maria individualmente, mas sobre regras gerais abstratas; quando a regra é comum para todos, a justiça protege o cidadão contra perseguições seletivas."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Analise a denúncia de Karl Marx em O Capital sobre a 'Jornada de Trabalho e a Mais-Valia Absoluta': de que modo a luta dos sindicatos e operários pela redução da carga horária semanal desvenda o caráter coercitivo da extração de lucros capitalistas?",
        "Comprovando que as fábricas britânicas consumiam lâmpadas de óleo de baleia que prejudicavam os olhos dos operários.",
        "Demonstrando que, na ausência de limites legais e sindicais impostos pela resistência dos trabalhadores, a voracidade do capital por mais-valia absoluta estende a jornada até o esgotamento biológico e a destruição física do trabalhador, sendo a fixação de limites legais à jornada o resultado direto da luta de classes e não da benevolência de industriais.",
        "Exigindo que os operários industriais façam exames médicos administrados por congregações religiosas.",
        "Provando que as caldeiras a vapor deixavam de funcionar quando a jornada ultrapassava oito horas diárias.",
        "Determinando que os salários pagos aos tecelões deveriam ser corrigidos anualmente pela inflação da prata.",
        "B",
        "- **Etapa 1:** Desmistificar a bondade espontânea do mercado: se deixado sem freios, o capital suga o trabalho por 14, 16 ou 18 horas diárias, consumindo a saúde e a vida de homens, mulheres e crianças em nome do lucro.\n- **Etapa 2:** Consagrar a conquista da jornada pela luta de classes: a jornada de 8 horas, o descanso semanal e as férias não foram presentes de governantes ou patrões; foram conquistados com sangue, greves e pressão do movimento operário contra a espoliação capitalista."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "Ao examinar a dialética rousseauniana da 'Origem da Linguagem e da Razão', por que o filósofo sustenta que a fala e a reflexão sofisticada nasceram das necessidades sociais e das paixões, e não de uma razão pura abstrata preexistente?",
        "Afirmando que os primeiros seres humanos se comunicavam unicamente por sinais sonoros de apitos de madeira.",
        "Demonstrando que no estado de natureza primitivo o homem solitário não necessitava de palavras articuladas complexas, tendo a linguagem surgido a partir da convivência mútua, das emoções partilhadas e, subsequentemente, da divisão do trabalho e da fundação da sociedade civil, evidenciando que a razão humana é um produto histórico e social, e não uma faculdade inata imutável.",
        "Comprovando que os idiomas europeus foram criados por marinheiros que navegavam pelo canal da Mancha.",
        "Exigindo que as assembleias deliberativas das cidades utilizem unicamente línguas latinas arcaicas.",
        "Determinando que os tratados diplomáticos devam ser declamados em versos líricos em praças municipais.",
        "B",
        "- **Etapa 1:** Desmontar o mito da linguagem inata: os filósofos anteriores imaginavam o homem natural já formulando frases complexas na floresta deserta.\n- **Etapa 2:** Evidenciar o caráter histórico da linguagem em Rousseau: quem vive só não tem com quem falar; foram os afetos, a aproximação dos clãs e a cooperação no trabalho que forjaram a fala e desenvolveram a razão; nós nos tornamos humanos racionais através do convívio histórico e social."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Em sua análise sobre o 'Fetichismo da Mercadoria' no primeiro capítulo de O Capital, como Karl Marx desmascara a ilusão de que os preços e as relações entre mercadorias são propriedades materiais das coisas e não relações sociais humanas?",
        "Provando que as mercadorias industriais eram abençoadas por sacerdotes em armazéns portuários.",
        "Evidenciando que a sociedade mercantil capitalista oculta as relações sociais de exploração e trabalho humano que deram origem aos produtos, fazendo com que as mercadorias pareçam dotadas de valor mágico autônomo no mercado, como se os objetos comandassem o destino dos seres humanos que os produziram.",
        "Determinando que as etiquetas de preços devem ser impressas exclusivamente em tecidos de algodão egípcio.",
        "Afirmando que o valor dos tecidos de lã decorre do alinhamento astronômico de planetas do sistema solar.",
        "Exigindo que os comerciantes de cereais façam juramentos cívicos perante estátuas de deuses romanos.",
        "B",
        "- **Etapa 1:** Diagnosticar o feitiço da mercadoria: na loja, olhamos para um celular ou uma roupa e vemos apenas o preço em reais e a marca, esquecendo que aquilo é o produto do suor e da exploração de dezenas de operários.\n- **Etapa 2:** Desvelar a inversão alienada: na sociedade capitalista, as coisas parecem ter vida própria e mandar nos humanos ('o mercado está nervoso', 'o dólar subiu'); o fetichismo é a ilusão que esconde o trabalho humano sob a máscara mágica do preço."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Síntese conclusiva do Capítulo 20 e encerramento do Lote 4 de Filosofia do Ensino Médio: de que maneira o estudo integrado da Soberania Popular e da Vontade Geral em Rousseau com a Crítica Materialista ao Estado Burguês de Marx e Engels instrumentaliza a juventude contemporânea para a construção de uma cidadania emancipada, consciente e transformadora?",
        "Ensinando técnicas de especulação monetária em bolsas de valores internacionais e desvios fiscais.",
        "Capacitando o estudante a transcender as ilusões da igualdade meramente formal perante a lei e a desvendar as engrenagens econômicas e ideológicas de dominação, municiando a juventude com o imperativo republicano da participação direta e da defesa intransigente do bem comum coletivo (Rousseau), articulado à luta consciente pela superação real da exploração do trabalho e pela conquista de uma sociedade substantivamente justa, solidária e livre de classes (Marx e Engels).",
        "Determinando que as escolas de ensino médio substituam o currículo de ciências humanas por treinos militares.",
        "Provando que as disputas políticas contemporâneas perdem o sentido diante do avanço de tecnologias fabris.",
        "Exigindo que os jovens concluintes do ensino médio façam votos perpétuos de renúncia a bens patrimoniais.",
        "B",
        "- **Etapa 1:** Integrar a potência republicana de Rousseau: de Rousseau o jovem aprende que a verdadeira soberania pertence ao povo, que a democracia direta é o horizonte da dignidade cívica e que a Vontade Geral pelo bem comum deve triunfar sobre o egoísmo das corporações e elites.\n- **Etapa 2:** Coroar com a lucidez transformadora de Marx e Engels: de Marx e Engels o jovem aprende que não há liberdade política real sem igualdade econômica na produção da vida; a cidadania crítica desmistifica o Estado como comitê dos ricos e luta pela emancipação humana integral, concluindo com maestria o Lote 4 da coleção de Filosofia do Ensino Médio."
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
    linhas.append('capitulo: "Capítulo 20: Rousseau, Vontade Geral e a Crítica Marxista ao Estado Burguês"')
    linhas.append('objeto_de_conhecimento: "A gênese da desigualdade e a propriedade privada em Rousseau, a soberania popular e a vontade geral em Do Contrato Social, e a crítica materialista histórica de Marx e Engels ao Estado burguês"')
    linhas.append('ebook_fonte: "em-fil-c20-rousseau-vontade-geral-critica-marxista.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: Rousseau, Vontade Geral e a Crítica Marxista ao Estado Burguês\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-20-rousseau-vontade-geral-critica-marxista -->"
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
    linhas.append("- ROUSSEAU, Jean-Jacques. *Do contrato social: princípios do direito político*. Tradução de Lourdes Santos Machado. São Paulo: Nova Cultural, 1999.")
    linhas.append("- ROUSSEAU, Jean-Jacques. *Discurso sobre a origem e os fundamentos da desigualdade entre os homens*. Tradução de Paulo Neves. Porto Alegre: L&PM, 2008.")
    linhas.append("- MARX, Karl; ENGELS, Friedrich. *Manifesto do Partido Comunista*. Tradução de Álvaro Pina. São Paulo: Boitempo, 2005.")
    linhas.append("- MARX, Karl. *Sobre a questão judaica*. Tradução de Nélio Schneider. São Paulo: Boitempo, 2010.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Salvar em temp_draft.md
    with open("temp_draft.md", "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em temp_draft.md ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador Educamob
    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-20-rousseau-vontade-geral-critica-marxista/ebooks/em-fil-c20-rousseau-vontade-geral-critica-marxista-exercicios.md"
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
        print("\n[SUCESSO TOTAL] Cap 20 validado e homologado com Exit Code 0!")

if __name__ == "__main__":
    main()
