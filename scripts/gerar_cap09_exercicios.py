# -*- coding: utf-8 -*-
"""
Script de Geração e Validação das 60 Questões de Filosofia - Cap 09
Objeto: Fundamentos da Ética e da Moral: Liberdade e Responsabilidade
Habilidades BNCC: EM13CHS101, EM13CHS501, EM13CHS502, EM13CHS504
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
        "Etimologicamente, o termo 'moral' tem sua raiz no vocábulo latino mos (cujo plural é mores). Qual é o significado original dessa palavra latina?",
        "Cálculo matemático de medidas geométricas.",
        "Costume, hábito coletivo ou maneira tradicional de agir consagrada pelo uso social.",
        "Comércio de especiarias e tecidos finos em portos marítimos.",
        "Decreto militar promulgado por governantes em épocas de guerra.",
        "Trabalho artesanal de escultura em blocos de mármore branco.",
        "B",
        "A palavra latina 'mos/mores' designa os costumes, hábitos e tradições que orientam a conduta coletiva em uma sociedade histórica concreta."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "A palavra grega êthos (com eta inicial longo), que dá origem ao conceito filosófico de ética, possuía qual significado fundamental na Grécia antiga?",
        "A velocidade de barcos a remo durante competições náuticas.",
        "A morada, o abrigo seguro e, por extensão, o caráter, o modo de ser e a disposição interna da alma.",
        "A quantidade de moedas de prata guardadas em cofres municipais.",
        "A colheita de cereais realizada após o período das chuvas de primavera.",
        "A construção de muralhas defensivas ao redor de templos sagrados.",
        "B",
        "Para os filósofos gregos (como Heráclito e Aristóteles), êthos representa a habitação interna, o caráter construído e o modo de ser do agente moral."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Na reflexão filosófica rigorosa, qual é a principal diferença entre Moral e Ética?",
        "A moral proíbe a prática de esportes e a ética obriga o uso de roupas cerimoniais brancas.",
        "A moral é o conjunto prático e histórico de regras de conduta de uma sociedade; a ética é a reflexão teórica e crítica sobre essas regras e seus princípios.",
        "A moral é uma invenção de marinheiros e a ética foi criada por comerciantes de vinho.",
        "A moral trata exclusivamente de impostos tributários e a ética organiza o trânsito urbano.",
        "A moral é imutável em todos os séculos e a ética muda diariamente de acordo com o clima.",
        "B",
        "A moral é o objeto prático e normativo vivido pelo grupo; a ética é a investigação filosófica teórica de segunda ordem sobre os alicerces desse agir."
    ))

    questoes_brutas.append((
        4, "EM13CHS501", "basico",
        "Por que as pedras que rolam morro abaixo ou os rios que transbordam durante tempestades não são julgados como moralmente bons ou maus pela filosofia?",
        "Porque eles não sabem ler livros de poesia dramática nas escolas públicas.",
        "Porque são seres inanimados que atuam impulsionados por leis causais físicas e mecânicas cegas, sem consciência, razão ou liberdade de escolha.",
        "Porque os tribunais de justiça funcionam apenas no período da tarde nas capitais.",
        "Porque a água da chuva é considerada sagrada por sacerdotes de ordens religiosas.",
        "Porque as tempestades duram menos de vinte e quatro horas em regiões litorâneas.",
        "B",
        "O juízo moral exige um sujeito ético consciente e livre; forças naturais operam pela necessidade causal mecânica da matéria, desprovidas de agência moral."
    ))

    questoes_brutas.append((
        5, "EM13CHS501", "basico",
        "A concepção filosófica do 'Determinismo' sustenta que todos os atos, escolhas e decisões humanas decorrem de:",
        "Sorteios aleatórios feitos por astrólogos em feiras públicas municipais.",
        "Causas antecedentes necessárias (sejam biológicas, físicas, históricas ou sociais) que produzem seus efeitos de modo inescapável.",
        "Sonhos noturnos que se transformam magicamente em matéria visível ao amanhecer.",
        "Vontades caprichosas de governantes que alteram as leis gramaticais do idioma.",
        "Poderes sobrenaturais concedidos apenas a navegadores que viajam por mares gelados.",
        "B",
        "O determinismo afirma o princípio de causalidade universal: todo fenômeno humano é o resultado inevitável de causas antecedentes físicas, biológicas ou sociais."
    ))

    questoes_brutas.append((
        6, "EM13CHS501", "basico",
        "Ao defender o determinismo em sua obra Ética, o filósofo Baruch Espinosa declarou que os seres humanos se consideram livres principalmente porque:",
        "Possuem asas invisíveis que lhes permitem voar sobre cidades industriais.",
        "Têm consciência de seus desejos e ações imediatas, mas ignoram completamente as causas reais que os determinam a agir.",
        "Lêem os poemas épicos de Homero antes de dormirem durante os meses de verão.",
        "Compram propriedades rurais em planícies férteis no interior de seus países.",
        "São capazes de prever a data exata em que ocorrerão eclipses solares.",
        "B",
        "Para Espinosa, a crença ingênua no livre-arbítrio absoluto decorre da ignorância humana sobre os apetites e causas causais inconscientes que movem o corpo e a mente."
    ))

    questoes_brutas.append((
        7, "EM13CHS501", "basico",
        "O 'Livre-Arbítrio Indeterminista' clássico defende qual modelo de agência humana perante as leis do mundo físico?",
        "A certeza de que as decisões humanas são calculadas por computadores eletrônicos gigantes.",
        "O poder da vontade racional de escolher e agir com total independência em relação a qualquer coação exterior ou causa antecedente necessária.",
        "A obrigação cívica de obedecer cegamente aos decretos editados por generais militares.",
        "A impossibilidade de praticar qualquer ato voluntário sem autorização de magistrados públicos.",
        "A tese de que a mente humana é uma máquina movida a vapor de água quente.",
        "B",
        "O livre-arbítrio pleno postula a faculdade de autodeterminação absoluta da vontade racional, desvinculada do mecanicismo causal material exterior."
    ))

    questoes_brutas.append((
        8, "EM13CHS502", "basico",
        "Para a corrente existencialista de Jean-Paul Sartre, o ser humano é caracterizado por qual princípio basilar sobre sua existência e sua essência?",
        "Sua essência é fabricada antes do nascimento por artesãos em oficinas de ferro.",
        "A existência precede a essência: o ser humano primeiro existe no mundo e depois se define livremente por meio de suas ações e escolhas concretas.",
        "Sua vida é guiada exclusivamente por mapas astrológicos desenhados em couro animal.",
        "Seu destino profissional é determinado pela quantidade de moedas de ouro de seus pais.",
        "Sua mente é um espelho passivo que apenas reflete imagens de florestas tropicais.",
        "B",
        "Em 'O Existencialismo é um Humanismo', Sartre afirma que o homem não nasce com uma essência prévia fixada: ele primeiro surge no mundo e se constrói pelas escolhas que faz."
    ))

    questoes_brutas.append((
        9, "EM13CHS502", "basico",
        "Em contraposição tanto ao determinismo fatalista quanto à onipotência irreal, o conceito de 'Liberdade Situada' afirma que:",
        "O indivíduo só consegue ser livre quando vive isolado no topo de uma geleira deserta.",
        "O ser humano vive condicionado por sua situação real (história, corpo, classe social), mas é plenamente livre para decidir qual sentido dará a essa realidade.",
        "A liberdade consiste em poder atravessar paredes de tijolos sólidos sem se machucar.",
        "A liberdade é um prêmio concedido apenas aos estudantes que obtêm nota dez em exames de física.",
        "O sujeito livre nunca precisa comer alimentos nem beber líquidos ao longo da semana.",
        "B",
        "A liberdade situada (Sartre e Merleau-Ponty) reconhece a facticidade concreta da vida, sustentando que a liberdade reside na capacidade de agir e projetar-se a partir dessas condições reais."
    ))

    questoes_brutas.append((
        10, "EM13CHS501", "basico",
        "Quais são os dois requisitos fundamentais exigidos pela ética filosófica para que uma pessoa seja considerada moralmente responsável por suas ações?",
        "Força muscular atlética e facilidade para falar línguas estrangeiras arcaicas.",
        "Consciência do ato (saber o que está fazendo e suas consequências) e voluntariedade (ausência de coação externa irresistível).",
        "Posse de terras agricultáveis e registro de nascimento expedido na capital do país.",
        "Hábito diário de caminhar ao ar livre e habilidade em tocar tambores de madeira.",
        "Vínculo familiar comprovado com dinastias de monarcas absolutistas da Europa.",
        "B",
        "A imputabilidade moral exige consciência (discernimento da ação e seus desdobramentos) e liberdade/voluntariedade (agir sem ser forçado fisicamente ou psicologicamente por terceiros)."
    ))

    questoes_brutas.append((
        11, "EM13CHS502", "basico",
        "Na filosofia existencialista de Jean-Paul Sartre, o conceito de 'Má-Fé' (mauvaise foi) descreve qual atitude humana?",
        "A realização de transações bancárias fraudulentas para fugir de cobranças de impostos.",
        "A tentativa inautêntica de mentir para si mesmo e culpar fatores externos ou o destino para escapar da angústia da escolha e da responsabilidade.",
        "A recusa em responder perguntas sobre matemática durante uma prova escolar.",
        "O hábito de cantar canções populares em tom muito alto durante passeios públicos.",
        "A decisão de não comparecer a banquetes oficiais organizados por autoridades municipais.",
        "B",
        "A má-fé é o fingimento existencial: o indivíduo livre comporta-se como se fosse um objeto passivo determinado pelas coisas para fugir do peso angustiante de suas próprias escolhas."
    ))

    questoes_brutas.append((
        12, "EM13CHS504", "basico",
        "O 'Relativismo Moral' defende qual tese sobre as normas, virtudes e valores éticos praticados na humanidade?",
        "Que todos os valores éticos foram escritos em placas de granito no topo de montanhas sagradas.",
        "Que as regras morais são invenções puramente locais e contingentes de cada cultura, sendo impossível estabelecer um critério ético universal válido para todas as sociedades.",
        "Que as leis de trânsito em cidades litorâneas são idênticas às regras de navegação fluvial.",
        "Que todas as civilizações humanas possuem os mesmos rituais funerários desde o período Neolítico.",
        "Que a verdade moral é determinada pela cotação do preço do trigo em bolsas mercantis.",
        "B",
        "O relativismo moral sustenta que nenhum sistema moral pode reivindicar validade universal superior, pois cada sociedade constrói seus próprios costumes locais particulares."
    ))

    questoes_brutas.append((
        13, "EM13CHS504", "basico",
        "Qual é uma das principais críticas filosóficas feitas contra o relativismo moral radical?",
        "Ele encarece a impressão de livros de contos de fadas para crianças do ensino infantil.",
        "Ao afirmar que toda moral local é intocável, ele anula a possibilidade de denunciar atrocidades históricas como o nazismo, a escravidão e o apartheid como crimes contra a humanidade.",
        "Ele proíbe os agricultores de cultivarem lavouras de arroz e feijão durante o outono.",
        "Ele obriga os juízes a usarem togas vermelhas confeccionadas com tecidos importados da Ásia.",
        "Ele diminui a velocidade de rotação do planeta Terra ao redor do Sol nos meses de frio.",
        "B",
        "Se o relativismo for levado ao extremo, regimes opressores e genocidas estariam protegidos de qualquer juízo crítico externo apenas por estarem de acordo com seus costumes locais."
    ))

    questoes_brutas.append((
        14, "EM13CHS504", "basico",
        "A filósofa espanhola Adela Cortina propõe uma superação do relativismo moral por meio de qual formulação ética?",
        "A imposição forçada de decretos militares sobre todas as escolas de educação básica do continente.",
        "A Ética de Mínimos Compartilhados, que estabelece princípios inegociáveis de justiça cívica e direitos humanos aplicáveis a todas as culturas do planeta.",
        "A obrigatoriedade de que todos os cidadãos aprendam a falar a língua grega clássica fluente.",
        "O fechamento das fronteiras nacionais para impedir o trânsito de pessoas entre cidades vizinhas.",
        "A distribuição gratuita de roupas de linho azul para trabalhadores de fábricas têxteis.",
        "B",
        "Adela Cortina defende que, em sociedades plurais, deve haver uma base de mínimos éticos compartilhados (justiça, igualdade e dignidade humana) sem impedir a diversidade cultural."
    ))

    questoes_brutas.append((
        15, "EM13CHS504", "basico",
        "A Declaração Universal dos Direitos Humanos, promulgada pela ONU em 1948, representa um marco histórico da ética universalista porque:",
        "Determinou que todos os navios de carga devem navegar com bandeiras pintadas em amarelo e verde.",
        "Consagrou que todo ser humano, independentemente de nacionalidade, raça, etnia ou gênero, possui direitos fundamentais inalienáveis à vida, à liberdade e à dignidade.",
        "Exigiu que todos os professores de universidades públicas usem relógios de bolso de prata maciça.",
        "Proibiu o cultivo de cana-de-açúcar em propriedades rurais localizadas próximas ao mar.",
        "Fixou o valor das passagens de trem urbano em todas as cidades da América do Sul e Europa.",
        "B",
        "A DUDH de 1948 consolida a dignidade humana como um imperativo universal e inalienável, superando o arbítrio de regimes soberanos locais após os horrores da Segunda Guerra."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "No clássico 'Dilema de Heinz', formulado pelo psicólogo Lawrence Kohlberg, Heinz enfrenta qual conflito ético fundamental?",
        "Escolher se deve viajar de carruagem a vapor ou de barco à vela para a cidade vizinha.",
        "Decidir entre respeitar a lei da propriedade privada do farmacêutico ou roubar o medicamento exorbitante para salvar a vida de sua esposa moribunda.",
        "Optar por pagar seus tributos municipais em moedas de cobre ou em cestas de grãos de cevada.",
        "Avaliar se seus filhos devem frequentar colégios militares ou trabalhar em oficinas de ferro.",
        "Decidir se deve pintar a fachada de sua casa de amarelo claro ou de azul escuro.",
        "B",
        "O dilema de Heinz põe em conflito dois valores: o respeito estrito à legalidade/propriedade material versus a preservação inegociável da vida humana em perigo iminente."
    ))

    questoes_brutas.append((
        17, "EM13CHS501", "basico",
        "Quando um carro autônomo sem motorista humano precisa tomar uma decisão de emergência no trânsito urbano, por que essa programação envolve uma questão ética e não puramente técnica?",
        "Porque o veículo consome combustíveis derivados de petróleo que poluem o ar atmosférico.",
        "Porque o algoritmo decide quem vive ou quem morre em um acidente inevitável, exigindo escolhas morais calibradas previamente pelos programadores humanos.",
        "Porque os pneus de borracha sintética perdem aderência quando as pistas de asfalto estão molhadas.",
        "Porque as baterias elétricas dos automóveis precisam de recargas diárias em garagens fechadas.",
        "Porque as leis de trânsito exigem que todos os automóveis transitem com luzes brancas acesas.",
        "B",
        "A decisão de um algoritmo de desviar para salvar pedestres ou poupar o ocupante é um juízo moral de valor, cuja responsabilidade ética e jurídica recai sobre os humanos que o programaram."
    ))

    questoes_brutas.append((
        18, "EM13CHS504", "basico",
        "A ativista e modelo somali Waris Dirie combate a prática tradicional da Mutilação Genital Feminina argumentando que:",
        "O ritual consome muito tempo e atrasa o início das aulas de matemática de meninas do campo.",
        "Nenhuma tradição cultural ou religiosa pode ser usada como justificativa para violar a integridade corporal, a saúde e os direitos inalienáveis de crianças e mulheres.",
        "As facas utilizadas nos procedimentos cirúrgicos devem ser fabricadas com ligas de ouro puro.",
        "A prática deveria ser transferida exclusivamente para hospitais localizados na América do Norte.",
        "As mulheres submetidas ao corte corporal deveriam receber medalhas comemorativas de prata.",
        "B",
        "Waris Dirie demonstra que a defesa dos direitos humanos universais não é arrogância colonial, mas a proteção inegociável de corpos vulneráveis contra agressões físicas permanentes."
    ))

    questoes_brutas.append((
        19, "EM13CHS501", "basico",
        "Na obra Eichmann em Jerusalém, Hannah Arendt cunhou a célebre expressão 'A Banalidade do Mal'. O que Arendt identificou no comportamento do burocrata nazista Adolf Eichmann?",
        "Um indivíduo acometido por alucinações febris que agia motivado por delírios mágicos incontroláveis.",
        "Um cidadão comum e burocrático que cometeu atrocidades em massa simplesmente por cumprir ordens de modo acrítico, renunciando ao exercício reflexivo do pensamento próprio.",
        "Um criminoso solitário que realizava assaltos a agências bancárias nas noites de lua cheia.",
        "Um filósofo dedicado ao estudo da lógica formal que se recusava a participar de reuniões de trabalho.",
        "Um soldado rebelde que desafiava diariamente as instruções de seus superiores hierárquicos.",
        "B",
        "Arendt revelou que o mal extremo pode ser cometido por pessoas burocráticas e ordinárias que abdicam da capacidade de pensar criticamente e se tornam peças cegas de engrenagens de extermínio."
    ))

    questoes_brutas.append((
        20, "EM13CHS502", "basico",
        "No romance Crime e Castigo de Fiódor Dostoiévski, por que o protagonista Rodion Raskólnikov entra em colapso psicológico após assassinar a velha usurária?",
        "Porque os sapatos que usava na noite do crime eram muito apertados para seus pés.",
        "Porque, mesmo tentando se convencer de que estava acima da moral comum, a voz de sua própria consciência humana e o peso da responsabilidade moral o atormentam implacavelmente.",
        "Porque as moedas roubadas na residência da vítima perderam seu valor de compra no comércio local.",
        "Porque o tribunal público de São Petersburgo foi destruído por um incêndio acidental na mesma semana.",
        "Porque ele foi impedido de matricular-se em cursos de línguas orientais na faculdade de direito.",
        "B",
        "Raskólnikov descobre que nenhum homem pode escapar do tribunal da consciência: a responsabilidade moral do ato cometido queima por dentro, desfazendo a ilusão do homem extraordinário acima da ética."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao contrastar a atuação da Moral com a reflexão da Ética em uma comunidade concreta, constata-se uma diferença de postura do sujeito perante a tradição, pois:",
        "A moral estimula a queima pública de documentos fiscais e a ética exige o pagamento de taxas portuárias.",
        "A moral opera no plano da obediência espontânea ou conformista a costumes herdados, enquanto a ética convoca o exame racional crítico sobre a validade e a justiça desses costumes.",
        "A moral proíbe o casamento civil entre adultos e a ética determina a idade de aposentadoria de pescadores.",
        "Ambas defendem que a verdade moral deve ser revelada exclusivamente através de sorteios feitos em templos.",
        "A moral é estudada apenas por astrônomos e a ética é regulamentada por empresas fabricantes de calçados.",
        "B",
        "A moral é transmitida pela cultura e internalizada como costume social; a ética rompe o automatismo tradicional para questionar os princípios que legitimam ou deslegitimam essas regras."
    ))

    questoes_brutas.append((
        22, "EM13CHS501", "intermediario",
        "Qual é a distinção teórica fundamental entre o 'Determinismo Científico-Filosófico' e a crença religiosa no 'Fatalismo Místico'?",
        "O determinismo afirma que as estrelas do céu decidem a profissão dos jovens nascidos no inverno.",
        "O fatalismo sustenta que o destino humano já está traçado por forças mágicas ou divinas inalteráveis; o determinismo afirma que os atos decorrem de causas naturais antecedentes, que podem ser alteradas se modificarmos as condições reais.",
        "O fatalismo utiliza aparelhos de eletroencefalograma e o determinismo recorre a oráculos com conchas marinhas.",
        "Ambos afirmam que a conduta humana é definida unicamente pelo signo do zodíaco no momento do nascimento.",
        "O determinismo afirma que não existem leis causais no universo material e que tudo ocorre por puro acaso cego.",
        "B",
        "O fatalismo crê em um destino imutável e fixo independente de nossas ações; o determinismo opera pela causalidade natural: conhecendo e alterando as causas materiais, podemos modificar os efeitos práticos."
    ))

    questoes_brutas.append((
        23, "EM13CHS501", "intermediario",
        "Ao analisar os experimentos de neurofisiologia conduzidos por Benjamin Libet na década de 1980 sobre a tomada de decisões motoras, qual questão sobre o livre-arbítrio emergiu para o debate contemporâneo?",
        "A constatação de que os cérebros humanos funcionam mais rápido quando a temperatura da sala está abaixo de zero.",
        "A detecção de um potencial de prontidão motor cerebral antes da consciência subjetiva de decidir mover o dedo, levantando o debate sobre se a ação é biologicamente determinada ou se mantemos poder de veto consciente.",
        "A prova definitiva de que as decisões humanas são tomadas por espíritos que habitam florestas temperadas.",
        "A demonstração de que o cérebro humano só toma decisões corretas se o indivíduo estiver em jejum alimentar há vários dias.",
        "A comprovação de que as crianças não possuem neurônios funcionais antes de completarem dezesseis anos.",
        "B",
        "Libet identificou o potencial de prontidão neural centenas de milissegundos antes da sensação de escolha, gerando o debate entre determinismo biológico rígido e a hipótese do livre-arbítrio como 'veto consciente'."
    ))

    questoes_brutas.append((
        24, "EM13CHS502", "intermediario",
        "Em O Existencialismo é um Humanismo, Jean-Paul Sartre cunhou a célebre fórmula: 'O homem está condenado a ser livre'. Qual é o fundamento filosófico dessa aparente contradição?",
        "O homem cometeu crimes militares no passado e por isso deve cumprir penas de trabalhos forçados no campo.",
        "O ser humano não escolheu ser lançado no mundo, mas, uma vez lançado na existência, é absolutamente responsável por tudo o que faz, sendo incapaz de se desvencilhar da necessidade de fazer escolhas.",
        "A liberdade humana é uma ilusão que só existe dentro de celas de prisões subterrâneas fechadas com cadeados.",
        "Os governantes de cidades industriais obrigam os trabalhadores a escolherem novos nomes civis anualmente.",
        "A mente humana perde a capacidade de pensar quando as leis do Estado são votadas democraticamente.",
        "B",
        "Não escolhemos nascer, mas somos forçados a existir; e existir como ser consciente significa estar compelido a escolher continuamente. Mesmo a recusa a escolher já constitui uma escolha livre e responsável."
    ))

    questoes_brutas.append((
        25, "EM13CHS502", "intermediario",
        "Como a perspectiva da Liberdade Situada de Jean-Paul Sartre desqualifica a desculpa comum de quem afirma 'eu fiz isso porque não tive nenhuma outra escolha na vida'?",
        "Provando que a pessoa possuía barras de ouro escondidas no assoalho de seu quarto para pagar despesas.",
        "Demonstrando que essa declaração é um artifício de má-fé, pois o sujeito sempre tem a opção de dizer não, resistir, assumir riscos ou reconfigurar sua postura existencial diante da situação limite vivida.",
        "Exigindo que o tribunal de justiça confisque os bens materiais de todos os parentes daquele que agiu mal.",
        "Afirmando que a pessoa deveria ter consultado as cartas de tarô antes de tomar qualquer decisão financeira.",
        "Sustentando que os seres humanos perdem a capacidade de raciocínio lógico em situações de crise climática.",
        "B",
        "A má-fé consiste em fingir que se é um objeto sem agência para escapar do peso da responsabilidade: Sartre argumenta que sempre temos escolhas, inclusive a de recusar submeter-se a ordens injustas."
    ))

    questoes_brutas.append((
        26, "EM13CHS501", "intermediario",
        "Em quais circunstâncias a ética filosófica e o direito penal moderno reconhecem que a responsabilidade moral de um indivíduo por um determinado ato lesivo é atenuada ou completamente excluída?",
        "Quando o agente mora em uma casa pintada de cinza e trabalha em repartições públicas municipais.",
        "Quando o indivíduo agiu em situação de ignorância invencível (era impossível prever o dano), sob coação física externa irresistível ou acometido por grave transtorno psíquico involuntário que aboliu sua consciência moral.",
        "Quando o agente cometeu o ato vestindo sapatos fabricados com tecidos sintéticos importados de outro país.",
        "Quando o ato foi realizado durante o período em que a maré oceânica estava subindo em cidades do litoral.",
        "Quando o réu comprova que leu menos de dez páginas de romances literários durante a sua adolescência.",
        "B",
        "Sem discernimento racional (consciência) ou sem liberdade de autodeterminação (ausência de coação externa irresistível), o sujeito não age como agente moral pleno, excluindo a imputabilidade moral do ato."
    ))

    questoes_brutas.append((
        27, "EM13CHS504", "intermediario",
        "Na análise do dilema de Heinz segundo os três níveis de maturidade moral de Lawrence Kohlberg, como se posiciona um sujeito que se encontra no 'Nível Pós-Convencional ou Principiológico'?",
        "Ele defende que Heinz deve ser enforcado em praça pública para que os farmacêuticos possam vender remédios com lucros ilimitados.",
        "Ele reconhece a colisão entre a lei positiva da propriedade privada e o valor supremo da vida humana, concluindo que o direito sagrado à vida sobrepõe-se à preservação de lucros materiais mercantis.",
        "Ele afirma que Heinz errou simplesmente porque os policiais usam fardas escuras e possuem armas de fogo pesadas.",
        "Ele sustenta que a esposa de Heinz deveria ter recorrido a feitiços mágicos para se curar da enfermidade grave.",
        "Ele propõe que o farmacêutico seja nomeado prefeito da cidade em razão de seus conhecimentos em química orgânica.",
        "B",
        "No estágio pós-convencional, o indivíduo fundamenta seu juízo em princípios éticos universais autônomos (como a primazia da vida humana e da justiça), reconhecendo que normas legais podem ser injustas."
    ))

    questoes_brutas.append((
        28, "EM13CHS504", "intermediario",
        "Ao distinguir o 'Pluralismo Cultural' do 'Relativismo Indiferente', a ética contemporânea defende qual orientação para as sociedades democráticas modernas?",
        "A imposição de uma única religião oficial e a proibição de todas as línguas regionais faladas no interior.",
        "O acolhimento respeitoso da diversidade de costumes, crenças e manifestações culturais dos povos, desde que essas práticas não violem a integridade física, a dignidade e os direitos humanos fundamentais dos indivíduos.",
        "A determinação de que todas as famílias consumam os mesmos alimentos durante as refeições matinais de domingo.",
        "O cancelamento das eleições parlamentares em cidades que possuam mais de duas etnias diferentes em seus bairros.",
        "A exigência de que todos os cidadãos adotem o mesmo corte de cabelo aprovado por decretos governamentais.",
        "B",
        "O pluralismo legítimo valoriza as ricas diferenças culturais que enriquecem a convivência humana, mas traça um limite ético firme: a dignidade e os direitos inalienáveis da pessoa humana não são relativizáveis."
    ))

    questoes_brutas.append((
        29, "EM13CHS501", "intermediario",
        "Na tragédia da Alemanha nazista, Adolf Eichmann alegou em seu julgamento que nunca havia odiado os judeus e que apenas cumpria as leis e ordens de seus superiores. Qual denúncia moral emerge dessa constatação de Hannah Arendt?",
        "A de que as leis de trânsito em cidades portuárias devem ser fiscalizadas por soldados do exército nacional.",
        "A de que a obediência cega à ordem legal vigente, desprovida de reflexão ética e de exame de consciência crítica individual, é o mecanismo pelo qual cidadãos comuns se tornam cúmplices de crimes monstruosos.",
        "A de que os documentos administrativos de governos europeus eram assinados com tintas pretas de má qualidade.",
        "A de que os trens de ferro deveriam ter seus trilhos lubrificados com óleos vegetais de fazendas agrícolas.",
        "A de que os juízes de tribunais internacionais não entendem as regras de comércio de trigo e cevada.",
        "B",
        "Arendt alerta para o perigo extremo do conformismo burocrático: a lei e o dever positivo não se confundem com a justiça moral; cumprir ordens cegamente não isenta o sujeito da responsabilidade ética pelos seus atos."
    ))

    questoes_brutas.append((
        30, "EM13CHS504", "intermediario",
        "Como a 'Ética de Mínimos Compartilhados' formulada por Adela Cortina responde ao desafio de construir uma convivência justa em um mundo de culturas plurais e conflitantes?",
        "Proibindo os jovens de ouvirem canções populares compostas em línguas faladas em outros continentes.",
        "Propondo uma separação entre os 'mínimos de justiça' (leis cívicas e direitos humanos universais obrigatórios a todos) e os 'máximos de felicidade' (projetos de vida, crenças e ideais pessoais que cada um é livre para seguir).",
        "Obrigando os cidadãos a morarem em edifícios de apartamentos construídos com o mesmo número de andares.",
        "Exigindo que os livros de história publicados em escolas públicas omitam o período das guerras mundiais.",
        "Determinando que os casamentos civis sejam celebrados apenas na presença de generais do exército.",
        "B",
        "Adela Cortina articula universais de justiça (direitos fundamentais que vinculam a todos igualmente) com o respeito aos projetos de realização pessoal e felicidade de cada indivíduo ou tradição particular."
    ))

    questoes_brutas.append((
        31, "EM13CHS501", "intermediario",
        "Ao debater a aplicação do 'Dilema do Bonde' no desenvolvimento de carros autônomos, qual problema de engenharia ética se coloca perante a responsabilidade dos fabricantes?",
        "Calcular a quantidade de combustível que o motor gasta quando os faróis estão acesos à noite.",
        "Decidir se os algoritmos de emergência devem priorizar a proteção da vida do comprador do carro ou a minimização do número total de vítimas pedestres na rua, definindo a responsabilidade civil e moral das empresas.",
        "Avaliar se os bancos dos veículos devem ser estofados com couro legítimo ou tecidos de algodão cru.",
        "Verificar se as janelas de vidro dos automóveis conseguem resistir à queda de granizo em rodovias rurais.",
        "Escolher se as buzinas devem reproduzir sons de instrumentos de corda ou melodias eletrônicas de flauta.",
        "B",
        "Veículos autônomos transferem a tomada de decisões morais trágicas para o software: os critérios de proteção do passageiro versus pedestres exigem regulação ética clara da sociedade sobre as montadoras."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Na história das ideias éticas, por que a pergunta socrática 'Qual é a vida que vale a pena ser vivida?' inaugura uma ruptura com a moral puramente tradicional da Grécia arcaica?",
        "Porque Sócrates exigiu que os guerreiros atenienses parassem de comer carne de carneiro antes de batalhas navais.",
        "Porque Sócrates deslocou a autoridade moral dos mitos e dos costumes tribais cegos para o exame racional da consciência individual, afirmando que uma vida sem reflexão crítica não é digna de um ser humano.",
        "Porque ele proibiu os jovens de caminharem pelas praças públicas da cidade durante as noites de lua cheia.",
        "Porque ele exigiu que os cidadãos atenienses pagassem impostos tributários exclusivamente em moedas de ouro persas.",
        "Porque Sócrates pretendia que todas as esculturas de deuses fossem retiradas dos templos de Atenas.",
        "B",
        "Sócrates introduz a atitude propriamente ética: não basta seguir os costumes dos antepassados por inércia; é preciso examinar pela razão se as condutas são justas, fundando a autonomia moral do sujeito."
    ))

    questoes_brutas.append((
        33, "EM13CHS502", "intermediario",
        "Considere a célebre formulação de Sartre: 'Não importa o que fizeram de você; o que importa é o que você faz com o que fizeram de você.' O que essa sentença expressa sobre o papel da agência moral?",
        "Ela afirma que as pessoas podem mudar de altura física e cor dos olhos apenas praticando exercícios de respiração.",
        "Ela rejeita o vitimismo fatalista e afirma que, mesmo condicionado pela história, pela família e pelas violências sociais sofridas, o indivíduo é responsável pela resposta criativa e pelo sentido que dará ao seu destino.",
        "Ela sustenta que os ricos e os pobres nascem com os mesmos recursos financeiros em suas contas correntes bancárias.",
        "Ela determina que as escolas primárias não devem ensinar disciplinas de geografia aos estudantes do campo.",
        "Ela comprova que as leis econômicas deixam de funcionar quando os cidadãos decidem viajar de férias para o litoral.",
        "B",
        "Sartre sintetiza a liberdade situada: os traumas e condicionamentos materiais do passado são dados reais, mas a identidade moral do sujeito é definida pelo projeto de superação e ação que ele constrói no presente."
    ))

    questoes_brutas.append((
        34, "EM13CHS504", "intermediario",
        "No debate sobre direitos humanos, pensadores universalistas refutam o argumento de que a Declaração da ONU de 1948 seria um 'instrumento de colonização ocidental' ao apontarem que:",
        "As reuniões da ONU foram realizadas em salões decorados com tapetes de seda importados de fábricas europeias.",
        "A Declaração foi redigida com a colaboração ativa de representantes de países de todos os continentes e consagra anseios universais de libertação contra o arbítrio de tiranos e ditaduras de qualquer parte do mundo.",
        "Os países signatários do documento foram obrigados a mudar suas capitais para cidades da América do Norte.",
        "O texto da Declaração proíbe os cidadãos de praticarem religiões que não possuam livros sagrados escritos.",
        "Todos os artigos do documento foram aprovados exclusivamente por votação secreta de generais de cavalaria.",
        "B",
        "A DUDH contou com contribuições intelectuais globais (árabes, chinesas, latino-americanas) e atua como instrumento de defesa dos oprimidos contra a opressão de seus próprios governos tirânicos locais."
    ))

    questoes_brutas.append((
        35, "EM13CHS501", "intermediario",
        "Qual é a contradição prática em que incorre um defensor do 'Determinismo Radical Absoluto' quando ele exige perante um juiz que um ladrão que furtou sua casa seja punido pelo tribunal?",
        "Ele esquece que os juízes de direito vestem togas pretas confeccionadas com tecidos de lã durante as audiências.",
        "Se todas as ações são necessárias e inevitáveis e o livre-arbítrio inexiste, o ladrão não teve qualquer poder de escolha para não furtar, tornando ilógico e injusto censurá-lo moralmente como culpado pelo ato.",
        "Ele gasta moedas de prata para pagar advogados de defesa que deveriam trabalhar de forma voluntária.",
        "Os policiais que prenderam o suspeito não possuíam registros de nascimento expedidos em cidades litorâneas.",
        "As portas de madeira da residência arrombada poderiam ter sido consertadas por marceneiros locais em poucas horas.",
        "B",
        "Se o determinismo for absoluto e o livre-arbítrio for uma ilusão, a culpa e o mérito moral deixam de fazer sentido racional: ninguém pode ser responsabilizado por agir do único modo que suas causas materiais impuseram."
    ))

    questoes_brutas.append((
        36, "EM13CHS502", "intermediario",
        "Em sua obra O Ser e o Nada, Jean-Paul Sartre utiliza o exemplo clássico do 'Garçom de Café' para ilustrar a dinâmica da Má-Fé. O que revela o comportamento do garçom que imita perfeitamente os gestos de sua profissão?",
        "Que o funcionário pretende ser promovido a gerente do restaurante para aumentar seus ganhos mensais em dinheiro.",
        "Que ele se reduz voluntariamente ao papel mecânico de uma coisa ou autômato (o 'ser-garçom'), representando uma função social para fugir de sua liberdade assustadora de homem consciente que pode mudar de rumo a qualquer instante.",
        "Que as bandejas de metal utilizadas nos cafés de Paris eram muito pesadas para serem transportadas com uma mão só.",
        "Que os clientes dos restaurantes franceses exigiam que os funcionários recitassem poesias clássicas ao servirem água.",
        "Que o café servido nas mesas continha açúcar em excesso e prejudicava a saúde das crianças da vizinhança.",
        "B",
        "O garçom de Sartre representa um papel para escapar da angústia da liberdade: ele finge ser uma coisa pronta e programada (um objeto em-si), escondendo de si mesmo que é um sujeito livre (para-si) dotado de agência."
    ))

    questoes_brutas.append((
        37, "EM13CHS504", "intermediario",
        "Ao examinar práticas tradicionais violentas contra mulheres em certas sociedades, por que filósofas africanas e latino-americanas recusam a alegação relativista de que 'isso é da cultura de nosso povo'?",
        "Porque elas defendem que todas as mulheres devem trabalhar exclusivamente em fábricas de montagem de calçados.",
        "Porque a cultura não é um bloco estático sagrado, mas um espaço histórico de disputas de poder; muitas vezes, a 'tradição' é manipulada por elites patriarcais dominantes para justificar a submissão e o controle sobre corpos vulneráveis.",
        "Porque as leis civis de países desenvolvidos proíbem a leitura de tratados filosóficos em aldeias rurais.",
        "Porque as cerimônias tradicionais consomem muitos recursos financeiros que deveriam ser guardados em bancos públicos.",
        "Porque as danças folclóricas locais deveriam ser apresentadas apenas em teatros das capitais metropolitanas.",
        "B",
        "As pensadoras feministas descoloniais mostram que a tradição não é neutra nem intocável: apelar para o relativismo cultural para proteger práticas violentas equivale a apoiar a dominação patriarcal local contra grupos subalternizados."
    ))

    questoes_brutas.append((
        38, "EM13CHS501", "intermediario",
        "A tese do 'Determinismo Psíquico' formulada por vertentes da psicanálise freudiana aponta que a conduta consciente do indivíduo é fortemente influenciada por:",
        "Cálculos de juros compostos realizados por bancários durante o fechamento de contas comerciais.",
        "Pulsões inconscientes reprimidas, conflitos afetivos infantis e imperativos morais internalizados que atuam nos bastidores da mente, desfazendo a ilusão de controle racional absoluto do Ego sobre suas ações.",
        "Movimentos de marés oceânicas e tempestades de vento que ocorrem em praias litorâneas.",
        "Decretos governamentais que fixam o horário de funcionamento de lojas de tecidos nas cidades.",
        "Histórias em quadrinhos e romances de cavalaria lidos por jovens em bibliotecas municipais.",
        "B",
        "Para a psicanálise, o sujeito consciente (Ego) não é o senhor absoluto de suas vontades, sendo constantemente tensionado por forças pulsionais inconscientes (Id) e censuras morais internalizadas (Superego)."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Qual é a relação entre a 'Consciência Moral' e o desenvolvimento da autonomia ética do cidadão perante o Estado?",
        "A consciência moral exige que os cidadãos prestem continência diária a oficiais militares em praças públicas.",
        "A autonomia ética capacita o indivíduo a julgar com discernimento crítico se as ordens e leis do Estado são justas e legítimas, permitindo a recusa de obediência a leis que violem a dignidade humana fundamental.",
        "A consciência moral proíbe a participação de jovens em debates políticos organizados por grêmios escolares.",
        "A autonomia ética impede que os trabalhadores rurais assinem contratos de trabalho em épocas de colheita.",
        "A consciência moral é adquirida apenas por pessoas que estudaram jurisprudência romana em academias de direito.",
        "B",
        "A autonomia ética (conforme pensada por Kant e pela teoria crítica) é a maturidade do cidadão que julga as leis pela razão, assumindo a coragem moral de resistir a ordens estatais injustas e autoritárias."
    ))

    questoes_brutas.append((
        40, "EM13CHS504", "intermediario",
        "Na reflexão contemporânea sobre a bioética e os limites da manipulação genética humana, por que o livre-arbítrio e a dignidade das futuras gerações tornaram-se questões centrais?",
        "Porque as vacinas contra gripe comum são produzidas com água destilada em laboratórios públicos.",
        "Porque a seleção deliberada de características genéticas, estéticas ou comportamentais de embriões pode programar o destino biológico de futuros seres humanos, ameaçando sua liberdade e autonomia como sujeitos de seu próprio projeto de vida.",
        "Porque as empresas de biotecnologia utilizam microscópios ópticos que consomem muita energia elétrica.",
        "Porque os hospitais das cidades industriais enfrentam dificuldades para comprar seringas descartáveis de plástico.",
        "Porque os pesquisadores de genética molecular são obrigados a registrar suas patentes em línguas estrangeiras.",
        "B",
        "Filósofos como Jürgen Habermas alertam que a eugenia liberal e a programação genética de embriões reduzem a pessoa a um produto fabricado com expectativas de terceiros, comprometendo sua autodeterminação existencial."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS501", "dificil",
        "Analise a célebre passagem de Baruch Espinosa na Carta a G. H. Schuller: 'Conceba uma pedra que recebe de uma causa exterior um impulso de movimento. Se essa pedra pudesse pensar e estar consciente de seu esforço para se mover, ela acreditaria firmemente que é totalmente livre e que persevera no movimento apenas pela sua própria vontade.' Como essa alegoria desconstrói o livre-arbítrio absoluto?",
        "Provando que as rochas minerais possuem neurônios cerebrais capazes de formular teorias geométricas no escuro.",
        "Evidenciando que os seres humanos ignoram as causas materiais antecedentes que determinam seus desejos e decisões, confundindo a mera consciência do agir imediato com uma suposta autonomia causal desvinculada das leis da natureza.",
        "Afirmando que a gravidade terrestre deixa de atuar sobre corpos rochosos que caem no interior de florestas úmidas.",
        "Sustentando que os artesãos de cantaria devem esculpir estátuas apenas com pedras roladas pelas águas de rios.",
        "Exigindo que os filósofos da natureza abandonem o estudo da física mecânica para se dedicarem à poesia dramática.",
        "B",
        "**Etapa 1:** Analisar a metáfora da pedra consciente de Espinosa: a pedra tem consciência do movimento, mas não conhece a força mecânica externa que a lançou.\n**Etapa 2:** Concluir com o determinismo de Espinosa: a ilusão do livre-arbítrio repousa na assimetria cognitiva humana — conhecemos nossos desejos e decisões, mas permanecemos cegos às causas naturais determinantes que os produzem."
    ))

    questoes_brutas.append((
        42, "EM13CHS502", "dificil",
        "Em O Existencialismo é um Humanismo, Jean-Paul Sartre apresenta o dilema trágico de um de seus alunos durante a ocupação nazista da França: 'O jovem hesitava entre partir para a Inglaterra e engajar-se nas Forças Francesas Livres para combater o invasor ou ficar com sua mãe viúva idosa, cujo consolo e sobrevivência dependiam inteiramente dele.' Por que Sartre sustenta que nenhuma moral doutrinária prévia (religiosa, kantiana ou utilitarista) pode resolver esse dilema?",
        "Porque o aluno era analfabeto e não conseguia ler os capítulos das cartilhas de instrução do exército nacional.",
        "Porque todas as doutrinas éticas abstratas falham na contingência da escolha concreta: cada opção envolve a violação de um dever sagrado, forçando o jovem a assumir a angústia da escolha autônoma e inventar sua própria moral sem garantias externas.",
        "Porque os trens de passageiros com destino ao porto de desembarque estavam com as passagens esgotadas na bilheteria.",
        "Porque as leis municipais de Paris proibiam os jovens solteiros de viajarem para cidades litorâneas desacompanhados.",
        "Porque o jovem pretendia consultar um oráculo em Atenas para decidir qual carreira profissional deveria seguir no futuro.",
        "B",
        "**Etapa 1:** Identificar o impasse trágico no caso do aluno de Sartre: a moral cristã manda amar o próximo (a mãe ou a nação?), e a kantiana proíbe usar a mãe como meio (mas lutar pela pátria é dever cívico).\n**Etapa 2:** Concluir com a liberdade radical sartreana: não há sinais no céu nem bússolas morais predeterminadas; o indivíduo é compelido a criar seu valor através do ato deliberado de sua escolha, assumindo a responsabilidade solitária pelo caminho adotado."
    ))

    questoes_brutas.append((
        43, "EM13CHS501", "dificil",
        "Considere o embate entre a tese do Determinismo Radical e a tese da Responsabilidade Moral. Se uma corte de justiça aceitasse integralmente o princípio de que 'todo comportamento criminoso decorre necessariamente de anomalias neuroquímicas, condicionamento social e traumas infantis incontroláveis', qual transformação estrutural ocorreria no sistema jurídico e ético?",
        "Os juízes de direito passariam a distribuir medalhas comemorativas de ouro a todos os reincidentes em delitos graves.",
        "O conceito clássico de culpa, censura moral e castigo retributivo perderia a sustentação racional, transformando o direito penal em mera engenharia social de proteção da coletividade, tratamento terapêutico e reabilitação técnica.",
        "As prisões públicas seriam fechadas para serem transformadas em bibliotecas dedicadas ao estudo do latim arcaico.",
        "As leis constitucionais seriam revogadas para permitir que sacerdotes de ordens religiosas julgassem os crimes de trânsito.",
        "Os cidadãos seriam proibidos de instalar trancas e fechaduras de metal nas portas de suas residências urbanas.",
        "B",
        "**Etapa 1:** Avaliar as consequências do determinismo neurobiológico e sociológico para a teoria da punição e imputabilidade.\n**Etapa 2:** Evidenciar que, extinto o livre-arbítrio, o castigo baseado em 'mérito e culpa moral' perde o fundamento: o infrator não 'escolheu o mal', mas atuou como efeito de causas antecedentes, restando à sociedade adotar medidas profiláticas, preventivas e de reintegração social."
    ))

    questoes_brutas.append((
        44, "EM13CHS504", "dificil",
        "Ao debater a fundamentação da Declaração Universal dos Direitos Humanos perante a diversidade antropológica, a filósofa Adela Cortina propõe a distinção entre 'Ética de Justiça' e 'Ética de Felicidade'. Qual o fundamento dessa distinção para superar o relativismo sem cair no imperialismo cultural?",
        "Exigir que todos os governos democráticos distribuam o mesmo valor de auxílio financeiro para famílias de camponeses.",
        "A ética de justiça abrange os mínimos éticos universalizáveis (direitos humanos inegociáveis para qualquer ser racional), enquanto a ética de felicidade acolhe a pluralidade irredutível de caminhos culturais, morais e religiosos particulares de vida plena.",
        "Proibir que os cidadãos adultos escolham suas próprias profissões no comércio de mercadorias importadas.",
        "Determinar que todas as escolas de educação básica utilizem livros impressos com letras de tamanho milimétrico.",
        "Impor que os cidadãos adotem dietas alimentares estritas supervisionadas por agentes de vigilância sanitária municipal.",
        "B",
        "**Etapa 1:** Compreender a distinção cortiniana entre mínimos morais universais (o justo) e máximos morais particulares (o bom/a felicidade).\n**Etapa 2:** Concluir que a ética de mínimos universais garante a dignidade da vida e a convivência justa entre todos os povos sem sufocar as variadas concepções de felicidade e sabedorias culturais que não firam os direitos humanos fundamentais."
    ))

    questoes_brutas.append((
        45, "EM13CHS501", "dificil",
        "No julgamento de Adolf Eichmann em 1961, a defesa do burocrata nazista argumentou que ele nunca havia matado diretamente um ser humano e que se limitara a seguir rigorosamente a lei positiva de seu país ('eu apenas cumpri ordens legais vigentes'). De que maneira a análise de Hannah Arendt desmantela essa linha de defesa jurídica?",
        "Demonstrando que Eichmann possuía passaportes diplomáticos falsos emitidos por governos de ilhas oceânicas do Pacífico.",
        "Evidenciando que a política e a ética exigem o discernimento moral autônomo: a obediência cega é um ato de cumplicidade que transforma o sujeito em cúmplice de assassinatos em massa, pois a razão prática jamais pode se subordinar à legalidade criminosa de um Estado totalitário.",
        "Afirmando que o acusado deveria ter sido perdoado caso comprovasse ter participado de feiras de artesanato com madeira.",
        "Provando que os trens da Alemanha nazista circulavam com velocidades reguladas por leis de proteção ambiental litorâneas.",
        "Sustentando que os comandantes militares de campos de concentração desconheciam o funcionamento de armas de fogo.",
        "B",
        "**Etapa 1:** Interpretar o conceito arendtiano de recusa ao pensamento (*Gedankenlosigkeit*): a incapacidade ou recusa deliberada de Eichmann de pensar a partir da perspectiva de suas vítimas.\n**Etapa 2:** Concluir com a responsabilidade cívica e moral: em matéria de ética e dignidade humana, a palavra 'obediência' é imprópria para adultos; obedecer a ordens desumanas é sustentá-las e partilhar a culpa pelo crime."
    ))

    questoes_brutas.append((
        46, "EM13CHS502", "dificil",
        "Ao examinar a tese existencialista de Sartre sobre a 'Responsabilidade Absoluta', como o filósofo conecta a escolha individual de cada sujeito com o destino de toda a humanidade em O Existencialismo é um Humanismo?",
        "Ele afirma que cada pessoa que trabalha na agricultura deve doar metade de suas colheitas para governantes europeus.",
        "Ele sustenta que, ao escolher um determinado caminho de vida ou ação, o indivíduo não escolhe apenas para si, mas projeta uma imagem do que ele acredita que o homem deve ser, engajando toda a humanidade no valor de sua escolha.",
        "Ele demonstra que as escolhas dos jovens são gravadas em placas metálicas depositadas no fundo de poços de petróleo.",
        "Ele exige que os indivíduos que desejam se casar peçam a autorização prévia por escrito de todos os seus vizinhos de rua.",
        "Ele defende que as decisões humanas são comunicadas por ondas de rádio secretas captadas por astrônomos do hemisfério sul.",
        "B",
        "**Etapa 1:** Analisar o conceito existencialista de engajamento (*engagement*): o homem é um projeto que se escolhe permanentemente.\n**Etapa 2:** Concluir com a universalidade da responsabilidade moral sartreana: ao escolher ser honesto ou traidor, covarde ou livre, estou afirmando o valor supremo dessa conduta para todos os seres humanos, transformando meu ato em responsabilidade cósmico-social angustiante."
    ))

    questoes_brutas.append((
        47, "EM13CHS504", "dificil",
        "Considere a colisão entre a tese do Relativismo Cultural e a defesa universalista da igualdade de gênero perante o tribunal de Haia. Quando defensores de governos autoritários alegam que 'a proibição de mulheres estudarem em universidades faz parte de nossa identidade cultural soberana', qual resposta a ética dos direitos humanos articula?",
        "Ela concorda com o governo autoritário e fecha as portas de todas as escolas femininas para evitar conflitos bélicos na fronteira.",
        "Ela denuncia que alegar 'identidade cultural' para silenciar, oprimir e excluir violentamente metade de sua população constitui uma dominação tirânica e patriarcal ilegítima, pois a educação é um direito humano universal inegociável de todo ser consciente.",
        "Ela determina que as jovens excluídas de faculdades devem receber pagamentos mensais em barras de ferro fundido.",
        "Ela proíbe os diplomatas internacionais de utilizarem ternos escuros durante as sessões plenárias de negociação de paz.",
        "Ela determina que as bibliotecas escolares de capitais estrangeiras devem retirar de suas prateleiras todos os livros de matemática.",
        "B",
        "**Etapa 1:** Desconstruir a falácia da soberania cultural que encobre violações de direitos civis básicos.\n**Etapa 2:** Concluir com a universalidade dos Direitos Humanos: nenhum costume, soberania de Estado ou regra religiosa possui autoridade moral legítima para anular a dignidade, a educação e a liberdade dos sujeitos sob sua jurisdição."
    ))

    questoes_brutas.append((
        48, "EM13CHS501", "dificil",
        "Ao investigar os dilemas morais da Inteligência Artificial e dos veículos autônomos, qual perigo ético se estabelece caso os humanos deleguem inteiramente aos algoritmos computacionais a tomada de decisões extremas sobre quem deve viver ou morrer em situações de emergência?",
        "O perigo de as telas de computadores de hospitais sofrerem superaquecimento elétrico em dias chuvosos de verão.",
        "A erosão da responsabilidade moral e humana, uma vez que algoritmos não possuem consciência, empatia ou deliberação ética autêntica, criando um vácuo de imputabilidade onde ninguém responde pelas mortes causadas.",
        "A perda de dados numéricos que estavam salvos em pastas de papelão guardadas nos armários de enfermagem.",
        "A exigência de que os pacientes internados decorem fórmulas químicas antes de receberem medicações receitadas.",
        "O fechamento de salas de cirurgia hospitalares para realizar reformas nas portas de entrada e saída de funcionários.",
        "B",
        "**Etapa 1:** Compreender as limitações de sistemas preditivos artificiais: máquinas computam correlações estatísticas, mas são desprovidas de intencionalidade moral, sofrimento ou consciência de dever.\n**Etapa 2:** Evidenciar que delegar decisões trágicas sobre a vida a softwares opacos dilui a responsabilidade ética: a agência moral deve permanecer nas mãos de profissionais humanos conscientes e passíveis de prestação de contas perante a sociedade."
    ))

    questoes_brutas.append((
        49, "EM13CHS101", "dificil",
        "No romance Crime e Castigo de Fiódor Dostoiévski, o estudante Raskólnikov formula a teoria dos 'Homens Ordinários vs. Homens Extraordinários', segundo a qual certas personalidades excepcionais (como Napoleão Bonaparte) teriam o direito moral de violar as leis e cometer crimes para o progresso do mundo. De que maneira o desenlace trágico do romance refuta essa teoria?",
        "Mostrando que Napoleão foi derrotado em batalhas navais porque seus marinheiros não sabiam nadar em rios profundos.",
        "Demonstrando que ninguém escapa à lei moral inscrita na dignidade da pessoa humana: o assassinato destrói a própria alma do agressor pela culpa lancinante, provando que nenhuma utilidade coletiva ou vaidade intelectual justifica desumanizar e matar outro ser humano.",
        "Evidenciando que a polícia de São Petersburgo possuía carruagens de ferro com cavalos treinados para caçar fugitivos da justiça.",
        "Comprovando que a usurária assassinada era parente distante de generais militares condecorados na corte do czar russo.",
        "Defendendo que as pessoas que cometem assassinatos devem ser perdoadas caso paguem tributos em moedas de ouro aos templos religiosos.",
        "B",
        "**Etapa 1:** Analisar a pretensão soberana de Raskólnikov de se colocar acima da moral comum por meio de uma racionalização instrumental egoísta.\n**Etapa 2:** Concluir com a lição humanista e ética de Dostoiévski: a moralidade não é um cálculo de conveniência de homens poderosos; a vida humana é um valor absoluto sagrado e a violação desse imperativo moral gera o colapso existencial da consciência do infrator."
    ))

    questoes_brutas.append((
        50, "EM13CHS502", "dificil",
        "Na reflexão filosófica de Paul Ricoeur em O Si-Mesmo como um Outro, como a constituição da 'Identidade Moral' do indivíduo articula a relação indissociável entre o 'Si-Mesmo' e o 'Outro'?",
        "Afirmando que as pessoas só conseguem pensar livremente quando moram sozinhas em fazendas agrícolas isoladas.",
        "Sustentando que a estima e o respeito por si mesmo dependem constitutivamente do reconhecimento do Outro como um sujeito igualmente digno, formulando a ética como o desejo de uma 'vida boa, com e para os outros, em instituições justas'.",
        "Demonstrando que os tribunais civis devem aprovar sentenças baseadas apenas em cartas anônimas enviadas pelo correio.",
        "Exigindo que os cidadãos prestem juramentos militares de fidelidade eterna a reis absolutistas da Europa.",
        "Provando que a identidade moral das crianças é definida pela quantidade de livros de matemática que seus pais possuem.",
        "B",
        "**Etapa 1:** Interpretar a clássica formulação ética de Paul Ricoeur: *viver bem, com e para os outros, em instituições justas*.\n**Etapa 2:** Concluir que a agência moral não é um solipsismo isolado e egoísta: a responsabilidade pelo Outro vulnerável é o alicerce indispensável da própria dignidade e estima moral do sujeito ético consciente."
    ))

    questoes_brutas.append((
        51, "EM13CHS501", "dificil",
        "Ao examinar a relação dialética entre Liberdade e Necessidade em Hegel e Marx, como a consciência das leis objetivas da história e da natureza expande o poder de ação do ser humano?",
        "Ela permite que os agricultores façam chover sobre as plantações apenas cantando hinos religiosos ao meio-dia.",
        "Ela demonstra que a verdadeira liberdade não é o desconhecimento cego das leis causais, mas o conhecimento rigoroso dessas leis para dominá-las conscientemente e transformar o mundo material por meio da práxis humana emancipatória.",
        "Ela estabelece que os trabalhadores urbanos devem trabalhar catorze horas por dia sem receber salários em dinheiro.",
        "Ela comprova que as leis da economia capitalista deixam de funcionar quando o comércio internacional fecha seus portos marítimos.",
        "Ela determina que as ferrovias de passageiros devem transportar apenas cargas de minério de ferro durante o inverno.",
        "B",
        "**Etapa 1:** Compreender a tese de Hegel e Friedrich Engels retomada por Marx: a liberdade é a consciência da necessidade (*die Freiheit ist die Einsicht in die Notwendigkeit*).\n**Etapa 2:** Concluir que a ilusão de poder sem regras é impotente; a liberdade genuína e eficaz manifesta-se quando a humanidade compreende as leis naturais e socioeconômicas para planejar coletivamente a emancipação social através do trabalho e da política."
    ))

    questoes_brutas.append((
        52, "EM13CHS504", "dificil",
        "No caso contemporâneo da Mutilação Genital Feminina combatido por Waris Dirie, como a teoria dos Direitos Humanos desmascara o argumento de que a proibição penal dessa prática por tribunais internacionais violaria a 'liberdade de crença religiosa' das famílias?",
        "Exigindo que os hospitais públicos utilizem apenas lâmpadas fluorescentes em salas de parto de cidades litorâneas.",
        "Evidenciando que a liberdade religiosa e cultural tem como limite insuperável a integridade física e a vida de terceiros, não podendo ser invocada para impor violência irreversível e mutilação sobre crianças incapazes de consentir livremente.",
        "Provando que as meninas submetidas ao ritual eram registradas em cartórios municipais com nomes civis masculinos.",
        "Determinando que os governos de países africanos devem pagar indenizações em moedas de ouro a todos os curandeiros tradicionais.",
        "Defendendo que as crianças devem ser proibidas de frequentar aulas de educação física em escolas públicas de capitais metropolitanas.",
        "B",
        "**Etapa 1:** Analisar o princípio da ponderação de direitos e os limites da liberdade de culto perante a integridade corporal.\n**Etapa 2:** Concluir com a primazia inegociável da dignidade humana: a liberdade de manifestação cultural e religiosa jamais confere licença moral ou jurídica para lesionar, torturar ou violar o corpo de pessoas vulneráveis e crianças indefesas."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Em sua obra Ética, o filósofo hispano-mexicano Adolfo Sánchez Vázquez alerta para o perigo do 'Moralismo Abstrato'. Em que consiste essa distorção e de que maneira ela aliena a reflexão moral real?",
        "Em exigir que os professores de filosofia utilizem apenas giz de cor branca durante as aulas em salas de escolas públicas.",
        "Em julgar e condenar o comportamento dos indivíduos por meio de preceitos e mandamentos morais desincorporados da história, ignorando as condições materiais, socioeconômicas e políticas concretas que limitam e condicionam as opções reais do sujeito.",
        "Em permitir que os operários de indústrias automotivas escolham o modelo dos uniformes que vestem durante o trabalho.",
        "Em determinar que os livros de matemática aplicada sejam encadernados com tecidos sintéticos importados da Ásia.",
        "Em proibir a circulação de moedas bancárias em feiras livres de produtos hortifrutigranjeiros durante os finais de semana.",
        "B",
        "**Etapa 1:** Compreender o conceito de Moralismo Abstrato em Adolfo Sánchez Vázquez: o juízo puramente formal e moralista desligado da estrutura social objetiva.\n**Etapa 2:** Evidenciar que o moralismo abstrato funciona como ideologia desmobilizadora: ao culpar apenas o indivíduo desprovido de pão ou de trabalho, camufla a opressão sistêmica e a desigualdade material que determinam grande parte dos conflitos sociais reais."
    ))

    questoes_brutas.append((
        54, "EM13CHS502", "dificil",
        "Considere o conceito sartreano de 'Facticidade' em tensão com o 'Projeto Existencial'. Como Sartre demonstra que a liberdade humana não é uma fuga mágica da realidade, mas uma relação dialética com os obstáculos do mundo?",
        "Afirmando que as montanhas rochosas só existem na imaginação de alpinistas que treinam com cordas de cânhamo.",
        "Evidenciando que um obstáculo natural (como uma rocha gigante no caminho) só adquire o significado de 'obstáculo intransponível' ou 'desafio a ser escalado' em virtude do projeto consciente que o indivíduo traçou livremente para si.",
        "Sustentando que os governantes de cidades industriais devem desviar os cursos dos rios para facilitar o trânsito de carroças.",
        "Provando que as pessoas que nascem em climas frios não conseguem aprender a tocar instrumentos musicais de percussão.",
        "Defendendo que as regras gramaticais da língua francesa foram criadas para beneficiar comerciantes de tecidos finos.",
        "B",
        "**Etapa 1:** Analisar a relação entre facticidade (a rocha em seu peso bruto no caminho) e o projeto humano consciente.\n**Etapa 2:** Concluir com a ontologia existencialista: a rocha em si mesma é apenas matéria neutra; ela só se torna um obstáculo ou uma escada para a vista panorâmica em função do projeto livre que o homem escolheu perseguir no mundo."
    ))

    questoes_brutas.append((
        55, "EM13CHS504", "dificil",
        "No debate sobre o Relativismo Moral contemporâneo, qual contradição performativa comete o cético radical quando afirma enfaticamente: 'Não existem valores universais válidos; todas as normas morais são puramente relativas e devem ser toleradas'?",
        "Ele esquece que as canções folclóricas cantadas em praças públicas de cidades litorâneas utilizam melodias em escalas pentatônicas.",
        "Ao afirmar como princípio absoluto que todos 'devem tolerar' as culturas alheias, ele acaba formulando um imperativo ético universal (o dever da tolerância), desmentindo pela própria fala a sua premissa de que nenhum universal ético existe.",
        "Ele gasta folhas de papel de celulose para escrever frases curtas que poderiam ser pronunciadas oralmente em conversas casuais.",
        "Ele desconsidera que os relógios de sol perdem a precisão de cálculo em dias em que o céu permanece nublado por tempestades.",
        "Ele impede que os jovens de escolas municipais participem de competições esportivas de corrida de revezamento.",
        "B",
        "**Etapa 1:** Identificar a autocontradição lógica e performativa do relativismo moral absoluto.\n**Etapa 2:** Concluir com a filosofia analítica e discursiva: ao reivindicar a tolerância universal perante as diferenças culturais, o próprio relativista ergue a tolerância à categoria de norma universal inegociável, destruindo sua própria pretensão de neutralidade relativista total."
    ))

    questoes_brutas.append((
        56, "EM13CHS501", "dificil",
        "Ao examinar o papel das Redes Sociais e dos Algoritmos de Engajamento sob a ótica da liberdade moral, qual alerta filósofos contemporâneos formulam sobre o 'Determinismo Algorítmico'?",
        "O alerta de que os cabos de fibra óptica submarinos sofrem interferências climáticas causadas por baleias migratórias.",
        "O alerta de que o monitoramento do comportamento digital e a modulação hiperpersonalizada de conteúdos aprisionam a consciência dos usuários em bolhas de confirmação e vícios dopaminérgicos, solapando a autonomia e a capacidade de deliberação crítica livre dos cidadãos.",
        "A comprovação de que as baterias de aparelhos celulares descarregam com maior rapidez em locais de grande altitude montanhosa.",
        "A tese de que os servidores de armazenamento de dados em nuvem consomem muita água tratada em seus sistemas de refrigeração.",
        "A exigência de que os jovens estudantes desativem suas caixas de correio eletrônico aos domingos e feriados cívicos.",
        "B",
        "**Etapa 1:** Compreender a mecânica do capitalismo de vigilância e a captura da atenção por modelos preditivos comportamentais.\n**Etapa 2:** Concluir que a autonomia moral requer espaço para a dúvida, o contraditório e o pensamento independente; os algoritmos de recomendação geram uma ilusão de escolha livre enquanto programam sutilmente os desejos e condutas políticas da massa."
    ))

    questoes_brutas.append((
        57, "EM13CHS502", "dificil",
        "Em sua crítica à 'Sociedade da Desresponsabilização', como teóricos da ética social apontam que a burocracia corporativa e estatal moderna facilita a ocorrência de crimes ecológicos de grande escala (como o rompimento de barragens de rejeitos de mineração)?",
        "Obrigando os engenheiros de minas a assinarem contratos de trabalho redigidos em línguas faladas na Antiguidade clássica.",
        "Pela fragmentação extrema das decisões em múltiplos departamentos e comitês anônimos, onde cada funcionário alega apenas 'cumprir sua meta burocrática particular', diluindo a consciência moral individual e gerando um vácuo em que ninguém se sente responsável pela tragédia humana e ambiental coletiva.",
        "Pela proibição de que as empresas mineradoras utilizem tratores e escavadeiras mecânicas movidas a motores elétricos.",
        "Pelo fechamento de estradas de ferro que transportam minério de ferro para portos de exportação durante o período das chuvas de verão.",
        "Pela exigência de que os gerentes de fábricas industriais façam exames físicos semestrais em hospitais do interior do estado.",
        "B",
        "**Etapa 1:** Analisar o fenômeno da 'irresponsabilidade organizada' (Ulrich Beck e Hannah Arendt) nas megaestruturas corporativas modernas.\n**Etapa 2:** Concluir que a divisão técnica hiperespecializada do trabalho aliena o sujeito do resultado global de seu agir: a burocracia técnica neutraliza a bússola ética do indivíduo, viabilizando desastres socioambientais brutais sob o álibi de rotinas formais cumpridas."
    ))

    questoes_brutas.append((
        58, "EM13CHS504", "dificil",
        "Ao articular o pensamento de Jürgen Habermas sobre a 'Ação Comunicativa' e a ética do discurso com a questão dos Direitos Humanos, como a legitimidade universal de uma norma moral é justificada?",
        "Pela contagem do número de bandeiras que tremulam nas fachadas dos palácios governamentais durante festas nacionais.",
        "Pela submissão da norma a um diálogo público racional, livre e igualitário entre todos os sujeitos potencialmente afetados por ela, no qual apenas a força do melhor argumento convence e fundamenta o consenso ético democrático.",
        "Pela imposição de decisões tomadas por magistrados que se reúnem em sigilo absoluto em salas fechadas de tribunal.",
        "Pela obrigação de que todos os cidadãos declarem fidelidade a credos religiosos aprovados por maiorias parlamentares.",
        "Pela realização de exames admissionais obrigatórios em escolas públicas de ensino médio em cidades do litoral.",
        "B",
        "**Etapa 1:** Compreender o princípio discursivo 'D' de Habermas: válidas são as normas que encontram a anuência de todos os concernidos como participantes de um discurso racional.\n**Etapa 2:** Concluir que o universalismo ético habermasiano não é autoritário nem imperialista: ele não impõe verdades acabadas, mas estabelece o procedimento democrático e simétrico de argumentação livre e horizontal entre iguais."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "No clássico 'Dilema de Heinz', considere um sujeito que responde que 'Heinz agiu de forma reprovável porque a lei contra o roubo é necessária para a estabilidade da sociedade civil e, se todos roubassem quando achassem justo, a ordem coletiva desmoronaria no caos'. De acordo com Lawrence Kohlberg, em qual estágio de desenvolvimento moral esse sujeito se encontra?",
        "No Estágio Pré-Convencional de medo do castigo físico e obediência a chicotes.",
        "No Nível Convencional, especificamente no estágio de manutenção da ordem social e cumprimento formal do dever e da lei instituída.",
        "No Nível Pós-Convencional de formulação autônoma de princípios universais de justiça cósmica.",
        "No Estágio Mágico-Ancestral de consulta a sacerdotes de templos dedicados a deuses do fogo.",
        "No Estágio Hedonista Instrumental de busca de satisfação imediata de desejos corporais egoístas.",
        "B",
        "**Etapa 1:** Interpretar o raciocínio centrado na preservação da lei positiva e da estabilidade institucional coletiva.\n**Etapa 2:** Classificar conforme a taxonomia de Kohlberg: trata-se do Nível Convencional (Estágio 4 - Lei e Ordem), em que o indivíduo enxerga a moralidade pela ótica da preservação das regras do sistema social, sem ainda atingir a reflexão principiológica autônoma superior."
    ))

    questoes_brutas.append((
        60, "EM13CHS502", "dificil",
        "Analise a seguinte reflexão da filósofa brasileira Marilena Chaui em Convite à Filosofia: 'O sujeito ético não é um ser passivo que se deixa arrastar pela força cega das paixões nem um ser abstrato desvinculado do mundo. A conduta ética exige a soberania da razão sobre as paixões desmedidas, aliada à capacidade de compreender o sentido da convivência intersubjetiva.' Qual síntese sobre a liberdade e a virtude moral essa passagem expressa?",
        "Que a virtude moral consiste em isolar-se completamente em mosteiros rurais para não ter contato com seres humanos.",
        "Que a liberdade autêntica não é ausência de freios ou mero capricho irracional, mas a autonomia deliberada pela qual o sujeito governa a si mesmo com lucidez e responsabilidade na vida compartilhada em comunidade.",
        "Que as paixões humanas devem ser eliminadas por meio de intervenções cirúrgicas no cérebro de jovens estudantes.",
        "Que a vida ética só pode ser alcançada por quem possui patentes de oficial de marinha e grandes fortunas bancárias.",
        "Que as regras morais de uma sociedade devem ser calculadas por equações matemáticas de física quântica avançada.",
        "B",
        "**Etapa 1:** Analisar a concepção de sujeito ético em Marilena Chaui: recusa do espontaneísmo inconsequente e do intelectualismo árido.\n**Etapa 2:** Concluir com a síntese clássica da filosofia prática: a liberdade ética é autogoverno (autonomia da razão) e respeito recíproco; o sujeito moral realiza sua dignidade no equilíbrio interior e no compromisso consciente com o bem comum da pólis."
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
capitulo: "cap-09-fundamentos-etica-moral-liberdade"
objeto_de_conhecimento: "A Distinção entre Moral (Costumes e Regras Sociais) e Ética (Reflexão Teórica dos Princípios); O Debate sobre o Determinismo (Biológico, Histórico e Social) vs. Livre-Arbítrio; A Liberdade Situada e a Inseparabilidade entre Escolha e Responsabilidade Moral; O Problema do Relativismo Cultural e a Universalidade dos Direitos Humanos."
ebook_fonte: "em-fil-c09-fundamentos-etica-moral-liberdade.md"
habilidades: "EM13CHS101, EM13CHS501, EM13CHS502, EM13CHS504, H1, H2, H16, H17"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: Fundamentos da Ética e da Moral: Liberdade e Responsabilidade

"""

    corpo = header
    slug_cap = "cap-09-fundamentos-etica-moral-liberdade"

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

- ARENDT, Hannah. *Eichmann em Jerusalém: Um Relato sobre a Banalidade do Mal*. Tradução de José Rubens Siqueira. São Paulo: Companhia das Letras, 1999.
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.
- CHAUÍ, Marilena. *Convite à Filosofia*. 13. ed. São Paulo: Ática, 2002.
- CORTINA, Adela. *Cidadãos do Mundo: Para uma Teoria da Cidadania*. Tradução de Silvana Cobucci Leite. São Paulo: Loyola, 2005.
- MARCONDES, Danilo. *Textos Básicos de Ética: De Platão a Foucault*. 2. ed. Rio de Janeiro: Jorge Zahar, 2007.
- RICOEUR, Paul. *O Si-Mesmo como um Outro*. Tradução de Ivone C. Benedetti. Campinas: Papirus, 1995.
- SARTRE, Jean-Paul. *O Existencialismo é um Humanismo*. Tradução de Vergílio Ferreira. 3. ed. Petrópolis: Vozes, 2007.
- VÁZQUEZ, Adolfo Sánchez. *Ética*. Tradução de João Dell'Anna. 22. ed. Rio de Janeiro: Civilização Brasileira, 2002.
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

    dest_rel = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-09-fundamentos-etica-moral-liberdade/ebooks/em-fil-c09-fundamentos-etica-moral-liberdade-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_path, dest_rel]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 09 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
