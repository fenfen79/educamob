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

def gerar_cap05():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-05-aristoteles-empirismo-logica-quatro-causas/ebooks/em-fil-c05-aristoteles-empirismo-logica-quatro-causas-exercicios.md"
    temp_draft = "temp_draft.md"

    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Filho de médico e nascido em Estagira, Aristóteles desenvolveu uma postura investigativa marcante. Qual traço caracterizou seu método em comparação ao de Platão?",
        "A dedicação exclusiva à matemática abstrata e a total desconfiança em relação aos corpos físicos.",
        "O fascínio pela observação empírica, pela classificação biológica e pelo estudo da natureza concreta.",
        "A adoção de mitos poéticos como única fonte aceitável de conhecimento filosófico.",
        "A defesa do ceticismo absoluto que afirmava a impossibilidade de conhecer qualquer verdade.",
        "A recusa em aceitar que as coisas materiais possuem regras e ordens na natureza.",
        "B",
        "Aristóteles tinha uma forte formação biológica e valorizava a observação atenta dos seres vivos e a análise empírica dos fatos da natureza concreta."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "Ao retornar a Atenas em 335 a.C., Aristóteles fundou sua própria instituição de ensino nos bosques consagrados a Apolo Lício. Qual o nome dessa escola?",
        "Academia.",
        "Liceu.",
        "Jardim.",
        "Pórtico.",
        "Cinossargo.",
        "B",
        "Aristóteles fundou o Liceu, cujos alunos eram chamados de peripatéticos pelo hábito de aprender caminhando pelas alamedas arborizadas."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Na famosa obra 'A Escola de Atenas', Rafael Sanzio retrata Platão apontando para o céu e Aristóteles com a mão espalmada voltada para o chão. O que esse gesto de Aristóteles simboliza?",
        "O desprezo pelo estudo das ciências e a recusa da racionalidade.",
        "A defesa de que as essências das coisas existem no próprio mundo material em que vivemos.",
        "A submissão cega às ordens dos governantes políticos e militares da Macedônia.",
        "A crença de que os deuses habitam as profundezas cavernosas da terra.",
        "A condenação da observação dos animais e das plantas terrenas.",
        "B",
        "O gesto com a mão espalmada para a terra expressa o princípio da imanência: as essências e formas estão encarnadas nas coisas materiais deste mundo."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "Qual foi a principal crítica de Aristóteles contra a Teoria das Ideias de Platão?",
        "Criar um mundo inteligível separado duplicou os problemas sem explicar o movimento e a geração das coisas sensíveis.",
        "Achar que a geometria e o cálculo matemático eram totalmente inúteis para o raciocínio.",
        "Defender que a matéria bruta é eterna e anterior a qualquer divindade organizadora.",
        "Afirmar que as pessoas comuns podiam atingir a sabedoria sem estudar filosofia.",
        "Considerar que os poemas de Homero continham a verdade absoluta sobre a origem do cosmos.",
        "A",
        "Aristóteles argumentou que duplicar o mundo ao criar um reino ideal separado não explica como os seres nascem, se transformam e morrem no mundo físico."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "Na obra Metafísica, Aristóteles investiga o ser e destaca uma categoria que possui primazia sobre todas as outras. Qual é essa categoria fundamental?",
        "O Acidente passageiro.",
        "A Substância (Ousía).",
        "O Lugar geográfico.",
        "A Quantidade mensurável.",
        "A Paixão passiva.",
        "B",
        "A substância (Ousía) é a categoria fundamental do ser, servindo de sujeito primário sobre o qual todas as outras características se apoiam."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "Como Aristóteles define a chamada 'Substância Primeira' (Prote Ousia)?",
        "O conjunto de todas as ideias matemáticas perfeitas guardadas na memória divina.",
        "O indivíduo singular e concreto existente no espaço e no tempo, como este cavalo ou Sócrates.",
        "A espécie biológica universal pensada pelo cientista em seu gabinete de estudos.",
        "O ar invisível que mantém os seres humanos respirando durante o sono.",
        "A substância mítica original de onde brotaram as divindades olímpicas gregas.",
        "B",
        "A substância primeira é o indivíduo singular real existente na realidade física, que atua como sujeito de todas as propriedades e atributos."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "A teoria aristotélica do Hilemorfismo afirma que todo ser físico existente no mundo é composto por quais dois elementos inseparáveis?",
        "Matéria (Hylé) e Forma (Morphé).",
        "Fogo eterno e Água primordial.",
        "Corpo perecível e Alma imortal reencarnada.",
        "Luz solar e Sombra escura.",
        "Espaço vazio e Átomos indivisíveis.",
        "A",
        "Hilemorfismo vem da junção de hylé (matéria) e morphé (forma), que constituem uma unidade substancial inseparável em cada ser concreto."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "No Hilemorfismo de Aristóteles, qual é o papel desempenhado pela Matéria (Hylé)?",
        "Ela é a estrutura final perfeita e acabada de uma obra de arte.",
        "Ela é o substrato passivo e indeterminado que tem capacidade de receber uma forma.",
        "Ela é o pensamento puro que comanda o movimento dos planetas no céu.",
        "Ela é a regra de validade dedutiva que organiza as conclusões de um silogismo.",
        "Ela é o objetivo ético supremo buscado por todos os cidadãos da cidade.",
        "B",
        "A matéria é o suporte passivo, físico e indeterminado que recebe uma configuração estrutural dada pela forma."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "E no mesmo Hilemorfismo, o que representa a Forma (Morphé)?",
        "O pó residual que sobra após a queima da lenha em uma lareira.",
        "O princípio determinante e organizador que faz com que uma coisa seja exatamente o que ela é.",
        "A quantidade numérica de peças que formam uma carruagem desmontada.",
        "O peso bruto de um bloco de mármore recém-extraído da pedreira.",
        "A cor superficial que desaparece quando o objeto é colocado no escuro.",
        "B",
        "A forma é a estrutura essencial e organizadora que confere identidade inteligível à matéria, fazendo a coisa ser o que é."
    ))

    questoes_brutas.append((
        10, "EM13CHS101", "basico",
        "Para explicar a mudança e o devir na natureza sem contradição, Aristóteles desenvolveu o par de conceitos de:",
        "Ilusão e Realidade suprassensível.",
        "Ato (Enérgeia) e Potência (Dýnamis).",
        "Mito poético e Revelação dos oráculos.",
        "Tese afirmativa e Antítese contrária.",
        "Destino trágico e Vontade humana livre.",
        "B",
        "Aristóteles formulou a relação entre ato (a forma atualizada) e potência (a capacidade real de vir a ser) para explicar o movimento natural."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Como Aristóteles define o conceito de Potência (Dýnamis)?",
        "O resultado final e definitivo de uma transformação física completada.",
        "A capacidade real e a possibilidade estrutural que uma substância tem de se transformar em algo.",
        "Uma força mágica misteriosa que viola as regras conhecidas da biologia.",
        "O erro de raciocínio cometido por oradores que defendem premissas falsas.",
        "A fraqueza muscular de quem não pratica exercícios regulares no ginásio.",
        "B",
        "Potência é a capacidade real e objetiva contida na natureza de uma substância de alcançar uma nova forma (como a semente em relação à árvore)."
    ))

    questoes_brutas.append((
        12, "EM13CHS101", "basico",
        "Como Aristóteles define o Movimento (Kínesis) na sua obra Física?",
        "A destruição total da matéria que se desfaz no nada absoluto.",
        "A passagem contínua da potência ao ato enquanto a coisa está em potência.",
        "A subida permanente das almas em direção ao reino das Ideias imutáveis.",
        "Uma ilusão criada pelos órgãos dos sentidos que a razão deve ignorar.",
        "O deslocamento caótico de partículas atômicas no vácuo infinito.",
        "B",
        "Para Aristóteles, o movimento é a realização contínua da potência rumo ao ato, explicando como as coisas mudam sem brotarem do nada."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Segundo a Teoria das Quatro Causas, quantas e quais são as explicações causais necessárias para conhecer plenamente uma coisa?",
        "Duas causas: Causa Terrena e Causa Celeste.",
        "Quatro causas: Material, Formal, Eficiente e Final.",
        "Três causas: Passada, Presente e Futura.",
        "Cinco causas: Terra, Água, Ar, Fogo e Éter.",
        "Uma única causa: O Acaso fortuito da natureza.",
        "B",
        "Aristóteles afirma que conhecer cientificamente é saber a causa, estabelecendo quatro causas essenciais: material, formal, eficiente e final."
    ))

    questoes_brutas.append((
        14, "EM13CHS101", "basico",
        "Em uma escultura de bronze feita em homenagem a um herói grego, o que representa a Causa Material?",
        "O escultor que trabalhou com o cinzel e o fogo da forja.",
        "O metal bronze de que a estátua é constituída.",
        "O desenho e as feições do herói representadas na peça.",
        "A celebração cívica e a honra na praça da cidade.",
        "O preço pago pelo conselho dos anciãos de Atenas.",
        "B",
        "A causa material é o substrato físico com que o objeto é fabricado; no exemplo, o próprio bronze."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "Ao observar a oficina de um marceneiro que fabrica uma mesa de madeira para estudos, qual elemento exemplifica diretamente a Causa Eficiente?",
        "O tronco de árvore cortado e empilhado no depósito.",
        "O artesão que serra, aplaina e monta a madeira utilizando ferramentas de marcenaria.",
        "A estrutura retangular projetada para apoiar cadernos e livros.",
        "A finalidade de oferecer um local confortável para a leitura dos alunos.",
        "A camada de verniz transparente aplicada para evitar cupins.",
        "B",
        "A causa eficiente é o princípio ativo ou agente motor responsável por produzir a transformação e reunir a matéria à forma, encarnado no trabalho do marceneiro."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Qual é a definição da Causa Final (Telos) na filosofia de Aristóteles?",
        "O momento exato em que um ser vivo morre e deixa de respirar.",
        "O objetivo, propósito ou bem em vista do qual uma ação ou ser existe e se desenvolve.",
        "A última premissa escrita por um filósofo no encerramento de um tratado.",
        "O primeiro impulso mecânico que coloca um barco em movimento nas águas.",
        "O elemento químico mais pesado encontrado na composição de uma rocha.",
        "B",
        "A causa final (Telos) expressa a finalidade e o propósito para o qual a coisa é gerada ou atua, orientando seu desenvolvimento."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Por que Aristóteles afirma a necessidade da existência de um 'Primeiro Motor Imóvel' no cosmos?",
        "Porque os deuses olímpicos precisavam de um líder visível para guerrear contra os titãs.",
        "Porque a cadeia de motores que transmitem movimento não pode regredir ao infinito sem anular o início do movimento.",
        "Porque a matéria da terra se desgastaria e desapareceria em poucos anos sem esse calor.",
        "Porque o sol depende do vento marinho para completar sua órbita diária no horizonte.",
        "Porque os governantes de Atenas exigiam uma divindade protetora nas leis da cidade.",
        "B",
        "Se a regressão causal motora fosse infinita, não haveria um primeiro impulso, tornando impossível qualquer movimento subsequente no universo."
    ))

    questoes_brutas.append((
        18, "EM13CHS101", "basico",
        "Quais características fundamentais definem o Primeiro Motor Imóvel aristotélico?",
        "Ele é composto de ferro pesado e se movimenta em círculos velozes no centro do planeta.",
        "Ele é Ato Puro, incorpóreo, eterno, imóvel e move o mundo por atração final.",
        "Ele é uma semente gigante em potência que espera o tempo certo para florescer.",
        "Ele é um monarca humano sábio coroado pela assembleia de guerreiros peripatéticos.",
        "Ele é uma ilusão dos sentidos que o sábio deve abandonar ao estudar física.",
        "B",
        "O Primeiro Motor Imóvel é ato puro sem matéria nem potência, não se movimenta e move todas as coisas ao atraí-las por perfeição final."
    ))

    questoes_brutas.append((
        19, "EM13CHS101", "basico",
        "Os tratados lógicos de Aristóteles foram reunidos pela posteridade em um conjunto de obras clássicas. Como esse conjunto é denominado?",
        "República.",
        "Organon.",
        "Poética.",
        "Teeteto.",
        "Banquete.",
        "B",
        "O conjunto dos tratados de lógica de Aristóteles recebeu o título de Organon, que significa 'instrumento' do pensamento correto."
    ))

    questoes_brutas.append((
        20, "EM13CHS101", "basico",
        "Qual princípio da lógica clássica afirma que uma proposição não pode ser verdadeira e falsa simultaneamente sob o mesmo aspecto?",
        "Princípio da Incerteza Geral.",
        "Princípio de Não Contradição.",
        "Princípio da Dualidade Mítica.",
        "Princípio do Fluxo Perpétuo.",
        "Princípio da Causa Eficiente.",
        "B",
        "O Princípio de Não Contradição estabelece que é logicamente impossível que um predicado pertença e não pertença ao mesmo tempo e no mesmo sentido a um sujeito."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Enquanto Platão sustentava que conhecer é recordar essências contempladas antes do nascimento da alma, como Aristóteles compreendia a origem do conhecimento humano?",
        "O conhecimento nasce de sonhos divinos concedidos aos sacerdotes durante o sono.",
        "O conhecimento inicia-se na experiência sensível e na observação dos fatos, sendo depois estruturado pelo intelecto.",
        "O saber é uma criação arbitrária das leis civis sem nenhuma ligação com o mundo natural.",
        "A verdade só pode ser descoberta por meio de fórmulas matemáticas sem contato com coisas reais.",
        "Todo conhecimento é transmitido apenas pelo sangue de famílias nobres e reis sábios.",
        "B",
        "Para Aristóteles, nada está no intelecto que não tenha passado antes pelos sentidos; a experiência sensível fornece os dados para a abstração racional."
    ))

    questoes_brutas.append((
        22, "EM13CHS101", "intermediario",
        "O argumento do 'Terceiro Homem' formulado por Aristóteles tinha como objetivo demonstrar qual inconsistência lógica na teoria de Platão?",
        "Provar que os seres humanos descendiam de três deuses primitivos do mar Egeu.",
        "Mostrar que postular uma Ideia separada para explicar homens concretos exige uma terceira forma unificadora, gerando uma regressão infinita.",
        "Afirmar que três juízes eram necessários para julgar as falhas da Academia ateniense.",
        "Sustentar que o corpo humano possui três partes anatômicas totalmente independentes.",
        "Defender que a verdade depende de um consenso obtido entre três cidadãos sorteados na assembleia.",
        "B",
        "O argumento do Terceiro Homem aponta que se a semelhança entre dois indivíduos requer uma Ideia superior, a relação entre esses indivíduos e a Ideia exigirá outra Forma, ao infinito."
    ))

    questoes_brutas.append((
        23, "EM13CHS101", "intermediario",
        "No Hilemorfismo, por que Aristóteles afirma que a matéria desprovida de forma e a forma desprovida de matéria não existem de modo isolado no mundo sensível?",
        "Porque as leis da cidade de Atenas proibiam a separação de matérias nos ateliês de escultura.",
        "Porque todo ser concreto existente é uma união inseparável (Synolon) de um conteúdo material com uma estrutura formal.",
        "Porque a matéria e a forma foram banidas do universo pelo Primeiro Motor Imóvel.",
        "Porque a forma só pode existir se for desenhada no papel por geômetras experientes.",
        "Porque a matéria física é apenas uma ilusão que se dissolve com a luz do meio-dia.",
        "B",
        "No plano físico sensível, matéria e forma são coprincípios que constituem o composto substancial unitário (Synolon), sendo inseparáveis na realidade fática."
    ))

    questoes_brutas.append((
        24, "EM13CHS101", "intermediario",
        "Parmênides dizia que a mudança era impossível porque o Ser não pode vir do Não-Ser. Como a distinção entre Ato e Potência superou esse impasse lógico?",
        "Mostrando que as coisas surgem por pura magia sem nenhuma causa anterior explicável.",
        "Demonstrando que a mudança não brota do nada absoluto, mas da potência, que é uma capacidade real de vir a ser inscrita na natureza da coisa.",
        "Concordando com Parmênides e afirmando que todos os movimentos da física são meras ilusões dos olhos.",
        "Defendendo que o nada absoluto tem força física suficiente para criar novos planetas e estrelas.",
        "Afirmando que o ser e o não-ser são exatamente iguais e não possuem nenhuma diferença real.",
        "B",
        "Aristóteles superou Parmênides esclarecendo que o devir se dá a partir do 'não-ser relativo' (a potência real de um ser), e não do nada absoluto."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Por que, na doutrina aristotélica, a Potência (Dýnamis) não pode ser confundida com qualquer fantasia impossível ou delírio imaginário?",
        "Porque a potência só existe na mente dos filósofos que escrevem tratados de política.",
        "Porque a potência é uma inclinação real e determinada fundamentada na própria constituição material da substância.",
        "Porque qualquer matéria no universo pode se transformar instantaneamente em qualquer outro ser concebido.",
        "Porque as leis da física proíbem que árvores produzam novas sementes na primavera.",
        "Porque a potência depende de decretos dos generais para se manifestar nos animais de carga.",
        "B",
        "A potência aristotélica não é fantasia: uma semente de macieira tem potência para virar macieira, mas jamais tem potência para se transformar em cavalo ou pedra."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Considere o crescimento de uma oliveira a partir de uma semente no solo grego. Sob a ótica das Quatro Causas, o que representa a Causa Final da semente?",
        "A terra úmida e os sais minerais que alimentam a raiz da planta.",
        "A árvore adulta formada e capaz de produzir azeitonas e florescer, cumprindo seu ciclo natural.",
        "O agricultor ateniense que cavou o buraco na terra com uma enxada de ferro.",
        "O formato oval e a casca dura que envolve a polpa da semente.",
        "O preço do azeite comercializado nos portos do mar Mediterrâneo.",
        "B",
        "A causa final da semente é atingir a realização plena da sua natureza, tornando-se a árvore desenvolvida e produtiva (sua consumação natural)."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "Em um projeto de arquitetura bioclimática moderna, os engenheiros planejam janelas para ventilação natural e aproveitamento térmico. Qual causa aristotélica descreve a planta e o desenho geométrico do edifício?",
        "Causa Material.",
        "Causa Formal.",
        "Causa Eficiente.",
        "Causa Acidental.",
        "Causa Indeterminada.",
        "B",
        "A planta arquitetônica, a estrutura espacial e o desenho que dão configuração organizada ao edifício correspondem à causa formal."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "A famosa máxima aristotélica afirma que 'a natureza não faz nada em vão, nada faz pela metade nem de modo supérfluo'. Qual concepção sobre a natureza está expressa nessa frase?",
        "Uma visão caótica em que tudo ocorre por acidentes sem sentido.",
        "Uma visão orientada a fins (causa final), em que os órgãos e processos naturais possuem funções precisas.",
        "A crença de que as plantas sentem dor e pensam como seres humanos na floresta.",
        "A ideia de que o universo foi construído para servir exclusivamente aos desejos egoístas do homem.",
        "A defesa de que as leis biológicas mudam a cada estação do ano sem nenhuma estabilidade.",
        "B",
        "A afirmação sintetiza a perspectiva orientada a fins da natureza: os seres e seus órgãos desempenham funções direcionadas à preservação e ao pleno desenvolvimento de suas formas."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "De que maneira o Primeiro Motor Imóvel coloca todo o cosmos em movimento, segundo Aristóteles?",
        "Por meio de empurrões físicos sucessivos e contatos mecânicos violentos.",
        "Movendo o universo por atração, da mesma forma que o objeto amado atrai quem o ama.",
        "Disparando raios luminosos a partir de tempestades no topo do monte Olimpo.",
        "Girando manivelas de ferro ocultas atrás da esfera das estrelas fixas.",
        "Soprando ventos cósmicos que empurram os planetas para fora de suas órbitas.",
        "B",
        "Aristóteles esclarece que o Primeiro Motor move 'como o objeto amado atrai quem o ama' (kinei hos eromenon), atuando por atração de finalidade e suprema perfeição."
    ))

    questoes_brutas.append((
        30, "EM13CHS101", "intermediario",
        "No Livro XII da Metafísica, Aristóteles descreve a atividade eterna do Primeiro Motor Imóvel. Qual é essa atividade?",
        "Organizar os combates dos soldados e premiar os reis justos da Grécia.",
        "Pensar o próprio pensamento (Noesis Noeseos), contemplando eternamente a sua própria perfeição.",
        "Remodelar a matéria terrestre para corrigir defeitos nas espécies de animais.",
        "Registrar em livros de pedra as preces dos marinheiros que navegam no mar.",
        "Contar a quantidade exata de grãos de areia espalhados nas praias do mundo.",
        "B",
        "Sendo intelecto puro e a realidade suprema, o Primeiro Motor só pode ter por objeto o pensamento mais perfeito: Ele é o Pensamento do Pensamento (Noesis Noeseos)."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Qual distinção separa o Primeiro Motor Imóvel de Aristóteles da concepção bíblica cristã de Deus?",
        "O Primeiro Motor criou o mundo a partir do nada absoluto e intervém com milagres diários na história.",
        "O Primeiro Motor não criou a matéria (o cosmos é eterno), não realiza milagres e não ouve orações pessoais.",
        "O Primeiro Motor é mortal e morre junto com o desaparecimento das constelações estelares.",
        "O Primeiro Motor precisa de templos de pedra e sacrifícios de animais para se manter vivo.",
        "O Primeiro Motor é uma figura com corpo de homem idoso que caminha pelas ruas da cidade.",
        "B",
        "Para Aristóteles, o cosmos e a matéria são eternos; o Primeiro Motor atua como causa final do movimento cósmico e não como um Deus providente e criador histórico do nada."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "Por que a Lógica (Analítica) não é classificada por Aristóteles como uma ciência particular como a botânica ou a física?",
        "Porque a lógica foi inventada por poetas e não possui rigor demonstrativo de raciocínio.",
        "Porque ela é um instrumento preparatório comum que estabelece as regras de raciocínio válidas para todas as ciências.",
        "Porque ela só se aplica a debates eleitorais e não tem serventia nas ciências naturais.",
        "Porque Aristóteles considerava que o pensamento lógico era incapaz de alcançar conclusões verdadeiras.",
        "Porque ela depende de revelações oraculares para demonstrar suas premissas essenciais.",
        "B",
        "A lógica é a ciência instrumental e preparatória (Organon) que estabelece as condições formais de validade que qualquer ramo do saber deve seguir para ser demonstrativo."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Se alguém afirma: 'Esta folha de papel é totalmente branca e, ao mesmo tempo e sob o mesmo aspecto, é totalmente preta', essa pessoa fere qual regra da razão?",
        "O Princípio da Amizade Cívica.",
        "O Princípio de Não Contradição.",
        "A Lei da Atração Gravitacional.",
        "A Causa Formal da Geometria.",
        "O Silogismo Retórico dos Sofistas.",
        "B",
        "A afirmação viola diretamente o Princípio de Não Contradição, que proíbe afirmar e negar a mesma propriedade de um sujeito ao mesmo tempo e no mesmo sentido."
    ))

    questoes_brutas.append((
        34, "EM13CHS101", "intermediario",
        "Qual formulação resume corretamente o Princípio do Terceiro Excluído da lógica clássica?",
        "Toda proposição possui pelo menos três significados ocultos que precisam ser decifrados.",
        "Uma proposição ou é verdadeira ou é falsa, não havendo um meio-termo intermediário.",
        "Todo argumento deve ter três premissas menores antes de chegar a uma conclusão válida.",
        "O homem prudente deve sempre escolher a terceira opção em qualquer dilema político.",
        "Três testemunhas mentirosas anulam automaticamente o processo de um julgamento cívico.",
        "B",
        "O Princípio do Terceiro Excluído estabelece que não há meio-termo entre ser verdadeiro ou ser falso: uma proposição é ou não é."
    ))

    questoes_brutas.append((
        35, "EM13CHS101", "intermediario",
        "Qual é a estrutura canônica de um silogismo categórico dedutivo formulado por Aristóteles?",
        "Três afirmações poéticas que rimam entre si no final de cada estrofe.",
        "Duas premissas (maior e menor) que conduzem necessariamente a uma conclusão lógica.",
        "Quatro opiniões populares recolhidas nas ruas por meio de votação pública.",
        "Uma única tese dogmática proclamada pelo sacerdote da cidade sem justificativas.",
        "Várias perguntas sucessivas que terminam em dúvida insolúvel sobre o tema.",
        "B",
        "O silogismo categórico dedutivo organiza-se classicamente em premissa maior e premissa menor, das quais decorre forçosamente uma conclusão necessária."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "No silogismo: 'Todos os homens são mortais; Sócrates é homem; logo, Sócrates é mortal', qual é o Termo Médio e qual a sua regra essencial?",
        "Sócrates; ele deve ser repetido obrigatoriamente na conclusão final.",
        "Homem; ele faz a ligação nas duas premissas e nunca deve aparecer na conclusão.",
        "Mortal; ele deve ocupar a posição de sujeito na premissa menor.",
        "Todos; ele serve para anular a certeza da demonstração racional.",
        "Logo; ele indica que o argumento é uma hipótese sem comprovação formal.",
        "B",
        "O termo médio é 'homem'; ele articula os termos maior e menor nas premissas e, por regra lógica rígida, jamais pode figurar na conclusão."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Qual é a diferença fundamental entre a Validade Formal e a Verdade Material de um silogismo?",
        "A validade depende de fatos comprovados no laboratório, enquanto a verdade é uma regra gramatical do texto.",
        "A validade diz respeito à coerência do encadeamento das premissas, enquanto a verdade refere-se à correspondência dos fatos com a realidade.",
        "Não existe diferença: todo argumento válido é obrigatoriamente verdadeiro no mundo dos fatos.",
        "A verdade só pode ser alcançada pela poesia, ao passo que a validade é exclusiva da matemática platônica.",
        "A validade exige premissas falsas para testar a inteligência do debatedor na praça pública.",
        "B",
        "Validade formal é a correção lógica das deduções das regras do raciocínio; verdade material é a exatidão empírica factual das afirmações em relação ao mundo real."
    ))

    questoes_brutas.append((
        38, "EM13CHS101", "intermediario",
        "Analise o silogismo: 'Todos os répteis voam no céu; o jacaré é um réptil; logo, o jacaré voa no céu'. Como a lógica aristotélica classifica esse argumento?",
        "Formalmente inválido e materialmente verdadeiro.",
        "Formalmente válido, porém materialmente falso.",
        "Formalmente inválido e materialmente falso em sua dedução.",
        "Um sofisma que não possui premissas nem termos identificáveis.",
        "Uma demonstração científica perfeita que reflete a realidade da biologia.",
        "B",
        "A estrutura dedutiva é perfeita e válida (as regras do silogismo foram cumpridas), mas a premissa maior é materialmente falsa, gerando uma conclusão factualmente errônea."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Na tradição do Direito (Civil Law), a estruturação de uma sentença judicial pelo magistrado reflete a lógica do silogismo. O que funciona como Premissa Maior nesse processo?",
        "O depoimento gravado de uma testemunha convocada para depor na corte.",
        "A norma legal geral e abstrata prevista no código de leis aprovado.",
        "A opinião pessoal do juiz sobre o estilo de vida das famílias locais.",
        "O valor financeiro recolhido pelo tribunal em taxas de custas do processo.",
        "A notícia publicada nos jornais sobre a prisão em flagrante do acusado.",
        "B",
        "Na subsunção jurídica dedutiva, a premissa maior é o texto abstrato e geral da lei (por exemplo, a tipificação penal da conduta)."
    ))

    questoes_brutas.append((
        40, "EM13CHS101", "intermediario",
        "Um estudante que ingressa no Ensino Médio tem a capacidade de se tornar um cidadão crítico e produtivo. Sob os conceitos de Aristóteles, que papel o trabalho pedagógico dos professores desempenha nessa trajetória?",
        "Atua como causa material ao fornecer a estrutura física dos cadernos escolares.",
        "Atua como causa eficiente estimuladora que auxilia a passagem da potência para o ato.",
        "Funciona como causa acidental passageira que atrapalha o desenvolvimento natural do jovem.",
        "Opera como o Primeiro Motor que anula a necessidade de esforço individual do aluno.",
        "Serve como prova de que a inteligência humana não pode ser transformada pela educação.",
        "B",
        "O processo educativo e a ação docente atuam como agentes motores (causa eficiente) que promovem a atualização das potencialidades do estudante rumo à sua maturidade (ato)."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS103", "dificil",
        "Ao examinar a divergência entre Platão e Aristóteles, nota-se que ela não é mero detalhe estilístico, mas uma profunda oposição sobre o estatuto da realidade. Como a posição aristotélica da imanência resolve o problema da separação das Ideias?",
        "Negando a existência de qualquer ordem inteligível e aceitando que o universo opera em caos constante.",
        "Afirmando que a forma inteligível não habita um reino exterior transcendental, mas reside encarnada na matéria de cada substância individual concreta.",
        "Transferindo todas as ideias platônicas para o interior dos templos religiosos dedicados a Apolo.",
        "Proibindo os jovens de aprenderem geometria e cálculos matemáticos no currículo do Liceu.",
        "Defendendo que apenas os deuses possuem substância e que as coisas do mundo são alucinações passageiras.",
        "B",
        "**Etapa 1:** Identificar a divergência central entre a transcendência das Ideias em Platão e a tese aristotélica da imanência das formas na realidade sensível.\n**Etapa 2:** Concluir que, para Aristóteles, a forma existe no composto substancial concreto (Synolon), resolvendo o abismo da separação platônica ao fincar a essência no próprio ser terreno."
    ))

    questoes_brutas.append((
        42, "EM13CHS103", "dificil",
        "Considere a refutação aristotélica da teoria das Ideias por meio do 'Argumento do Terceiro Homem'. Qual consequência lógica necessária desmonta a pretensão de Platão ao usar esse raciocínio?",
        "A descoberta de que Sócrates nunca foi um cidadão de carne e osso na cidade de Atenas.",
        "A necessidade lógica de postular infinitos arquétipos intermediários para justificar a semelhança entre a forma inteligível e os indivíduos sensíveis, caindo em absurdo.",
        "A comprovação definitiva de que a espécie humana descende de três deuses primitivos do Olimpo.",
        "A constatação de que dois homens quaisquer não podem ter nenhuma característica física em comum.",
        "A aceitação tácita de que a dialética platônica é superior a qualquer silogismo demonstrativo.",
        "B",
        "**Etapa 1:** Analisar o encadeamento do argumento: se para justificar a semelhança entre dois indivíduos é preciso uma Forma transcendente comum, a relação entre esses indivíduos e essa Forma exigirá uma terceira Forma.\n**Etapa 2:** Evidenciar que essa cadeia gera uma regressão ao infinito insustentável, comprovando a inoperância lógica de duplicar o mundo para explicá-lo."
    ))

    questoes_brutas.append((
        43, "EM13CHS103", "dificil",
        "No Hilemorfismo, Aristóteles atribui à Forma a função de princípio organizador e determinante. Por que, mesmo assim, a Matéria não pode ser desconsiderada na explicação científica do mundo?",
        "Porque a matéria é a única coisa que tem inteligência e vontade própria na natureza.",
        "Porque sem o substrato material receptivo de determinações, a forma não teria suporte físico concreto para se manifestar no mundo dos seres particulares.",
        "Porque a matéria foi criada antes das formas por artesãos que viviam em oficinas na Beócia.",
        "Porque a ciência descarta as formas inteligíveis e se concentra exclusivamente no peso das pedras brutas.",
        "Porque as leis políticas atenienses exigiam o registro do peso dos metais em todos os tratados.",
        "B",
        "**Etapa 1:** Compreender a complementaridade indissolúvel entre matéria (substrato potencial passivo) e forma (princípio determinante ativo).\n**Etapa 2:** Reconhecer que no mundo físico não existe forma desencarnada; a matéria é a condição física indispensável para que a forma se corporifique em um indivíduo singular."
    ))

    questoes_brutas.append((
        44, "EM13CHS105", "dificil",
        "Na análise do desenvolvimento embriológico de um organismo vivo, a semente ou óvulo fertilizado sofre sucessivas transformações. Como a dinâmica de Ato e Potência articula esse processo contínuo de forma coerente?",
        "Provando que a matéria bruta do embrião não possui nenhuma relação causal com o animal adulto.",
        "Mostrando que o desenvolvimento é a atualização progressiva das potências reais contidas na forma específica do organismo até alcançar seu estado adulto pleno.",
        "Evidenciando que cada nova célula que surge brota do nada absoluto por meio de milagres inexplicáveis.",
        "Defendendo que o embrião já é um animal adulto em miniatura que apenas estica seus membros no útero.",
        "Demonstrando que o movimento biológico viola as regras lógicas e destrói o Princípio de Identidade.",
        "B",
        "**Etapa 1:** Caracterizar a potência como a capacidade real imanente que orienta a diferenciação e crescimento dos tecidos biológicos.\n**Etapa 2:** Constatar que o desenvolvimento embriológico é a transição contínua da potência ao ato (Entelécheia), culminando na maturidade funcional do ser vivo."
    ))

    questoes_brutas.append((
        45, "EM13CHS105", "dificil",
        "O biólogo evolucionista Ernst Mayr observou uma impressionante afinidade conceitual entre o pensamento biológico de Aristóteles e a genética contemporânea. A qual causa aristotélica a informação codificada na molécula de DNA mais se assemelha?",
        "À Causa Acidental, pois as bases nitrogenadas se combinam por acaso sem nenhuma regra biológica.",
        "À Causa Formal, pois o DNA atua como uma matriz informacional que direciona a organização da matéria celular.",
        "À Causa Material bruta, pois o DNA é apenas uma massa pesada de carbono inerte sem função biológica.",
        "À Causa Eficiente exterior, já que o DNA precisa ser empurrado por forças mecânicas fora do corpo.",
        "À Causa Retórica, porque o DNA serve exclusivamente para descrever metáforas em artigos médicos.",
        "B",
        "**Etapa 1:** Relacionar a Causa Formal aristotélica à estrutura configuradora e informacional que faz um ser ter determinada identidade.\n**Etapa 2:** Compreender que o programa genético (DNA) orienta a matéria celular indeterminada a assumir a anatomia e as funções próprias da espécie, exercendo o papel de causa formal e direcionadora."
    ))

    questoes_brutas.append((
        46, "EM13CHS103", "dificil",
        "Em uma grande ponte de concreto construída para ligar duas cidades, os engenheiros constatam que o cimento utilizado continha areia imprópria e ferro de baixa qualidade. Sob a teoria das Quatro Causas, como esse problema deve ser analisado?",
        "Uma falha na causa final que nada tem a ver com a resistência física dos materiais da obra.",
        "Uma deficiência grave na causa material que compromete a execução da causa formal e inviabiliza a realização da causa final segura da edificação.",
        "Um erro exclusivo do governo que pagou a obra com moedas de prata de valor alterado.",
        "Uma prova de que as pontes só dependem do traçado dos desenhos no papel para ficarem em pé.",
        "Uma confirmação de que as quatro causas agem de forma separada sem nenhuma relação recíproca.",
        "B",
        "**Etapa 1:** Analisar a interdependência entre os componentes causais: a causa material fornece o suporte de resistência para a estrutura da causa formal.\n**Etapa 2:** Concluir que materiais defeituosos (causa material corrompida) impedem a estabilidade estrutural (causa formal), provocando o colapso da finalidade de transporte seguro (causa final)."
    ))

    questoes_brutas.append((
        47, "EM13CHS103", "dificil",
        "No século XIII, São Tomás de Aquino realizou a síntese entre a filosofia de Aristóteles e o pensamento cristão medieval. Como a Quinta Via tomista para provar a existência de Deus se apropria da física aristotélica?",
        "Negando que os animais e plantas tenham funções ordenadas e sustentando que o mundo é governado pelo acaso.",
        "Apropriando-se da concepção orientada a fins da natureza para argumentar que os seres sem consciência operam para um fim por estarem orientados por uma inteligência suprema.",
        "Adotando a teoria platônica do Mundo das Ideias para combater o hilemorfismo aristotélico nas universidades.",
        "Condenando a observação empírica dos biólogos e defendendo que apenas revelações místicas são válidas.",
        "Afirmando que o silogismo dedutivo é incapaz de demonstrar proposições sobre a criação do cosmos.",
        "B",
        "**Etapa 1:** Recordar o princípio aristotélico de que na natureza os processos operam voltados a fins funcionais estáveis.\n**Etapa 2:** Identificar que Tomás de Aquino transpõe essa ordenação finalística (Quinta Via) como prova racional de que existe um Ordenador Cósmico Inteligente que guia seres irracionais ao seu fim."
    ))

    questoes_brutas.append((
        48, "EM13CHS101", "dificil",
        "Ao formular a Primeira Via da Suma Teológica, Tomás de Aquino baseia-se diretamente na teoria do Primeiro Motor Imóvel de Aristóteles. Qual premissa cosmológica sustenta essa via demonstrativa?",
        "A matéria pode se transformar em movimento perpétuo sem necessidade de nenhum princípio causal motor.",
        "Tudo o que se move no universo é movido por outro em ato; para evitar uma regressão causal impossível ao infinito, é forçoso admitir um Primeiro Motor.",
        "O movimento dos planetas resulta de uma colisão caótica de cometas sem nenhuma ordem observável.",
        "Os homens mais fortes devem governar as assembleias políticas para garantir a ordem moral nas cidades.",
        "O tempo teve início há poucos séculos e terminará assim que as órbitas dos planetas pararem de girar.",
        "B",
        "**Etapa 1:** Analisar a necessidade de que toda passagem da potência ao ato exige um agente anterior em ato.\n**Etapa 2:** Reconhecer que, se não houver um Primeiro Motor Imóvel para interromper a regressão infinita de motores subordinados, nenhum movimento do cosmos poderia existir no presente."
    ))

    questoes_brutas.append((
        49, "EM13CHS103", "dificil",
        "Por que o Primeiro Motor Imóvel aristotélico precisa ser concebido estritamente como Ato Puro, sem conter nenhuma mescla de matéria ou potência?",
        "Porque se contivesse matéria pesada, ele afundaria nas águas do oceano primordial grego.",
        "Porque se contivesse potência, ele estaria sujeito à mudança e precisaria de uma causa motora anterior a ele para movê-lo, anulando sua condição de princípio primeiro.",
        "Porque os sacerdotes da cidade exigiam que os deuses fossem feitos exclusivamente de ar transparente.",
        "Porque o silogismo categórico só aceita premissas que contenham substâncias materiais puras.",
        "Porque a potência é uma força mágica que só pertence aos animais de quatro patas da floresta.",
        "B",
        "**Etapa 1:** Compreender que onde há potência há possibilidade de mudança e, portanto, dependência de um motor exterior que a atualize.\n**Etapa 2:** Demonstrar que para ser a causa primeira e absoluta de todo o movimento perpétuo, o Primeiro Motor não pode mudar: deve ser Ato Puro, desprovido de potência e incorpóreo."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "No Direito moderno, imagine que um réu comprovou ter agido em legítima defesa estrita diante de um ataque injusto e iminente à sua vida. Como essa prova afeta a elaboração do silogismo judicial condenatório?",
        "Ela reforça a condenação porque confirma que o réu estava presente no local do fato no momento da ocorrência.",
        "Ela quebra a subsunção da premissa menor à premissa maior típica, impedindo que a conclusão condenatória seja legitimamente deduzida pelo magistrado.",
        "Ela obriga o tribunal a anular todas as leis penais escritas do país por contradição interna.",
        "Ela transfere automaticamente a condenação para os policiais que efetuaram a prisão do cidadão.",
        "Ela faz com que o juiz precise consultar os oráculos antes de proferir a sentença final nos autos.",
        "B",
        "**Etapa 1:** Identificar os papéis das proposições no silogismo judicial: premissa maior (crime e pena) e premissa menor (fato típico e ilícito comprovado).\n**Etapa 2:** Constatar que a legítima defesa exclui a ilicitude do fato, desarticulando a subsunção necessária entre a premissa menor e maior, tornando logicamente inviável a conclusão condenatória."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Nos Segundos Analíticos, Aristóteles trata da ciência demonstrativa (Episteme). Qual condição metodológica e de rigor distingue o silogismo demonstrativo da mera retórica persuasiva?",
        "O silogismo científico pode basear-se em boatos públicos, desde que a assembleia vote a favor da tese.",
        "O silogismo científico exige premissas que não sejam apenas válidas formalmente, mas verdadeiras, primeiras, necessárias e causais da conclusão.",
        "A demonstração científica só pode ser escrita em poemas com métrica regular ditados por mestres antigos.",
        "A retórica é superior à ciência porque convence mais rápido os cidadãos reunidos no tribunal da pólis.",
        "A ciência descarta a dedução lógica e baseia todas as suas conclusões em votações populares na praça.",
        "B",
        "**Etapa 1:** Diferenciar a validade formal puramente lógica da exigência de rigor da ciência demonstrativa (Episteme).\n**Etapa 2:** Explicitar que a ciência exige premissas verdadeiras, necessárias e anteriores (causais), enquanto a retórica contenta-se com premissas prováveis ou de opinião (doxa)."
    ))

    questoes_brutas.append((
        52, "EM13CHS101", "dificil",
        "Analise a falácia no seguinte argumento: 'Os cães latem; a constelação do Cão está no céu; logo, a constelação do Cão late'. Qual regra do silogismo clássico foi violada?",
        "A regra do Terceiro Excluído entre as constelações estelares.",
        "A regra de que o silogismo deve possuir apenas três termos; o termo 'Cão' foi usado em sentidos diferentes (equívoco), criando quatro termos reais.",
        "A proibição de mencionar animais domésticos em argumentos que tratem de astronomia.",
        "A obrigatoriedade de colocar a premissa menor antes da premissa maior em todas as deduções.",
        "A exigência de que todos os silogismos contenham números matemáticos em suas conclusões.",
        "B",
        "**Etapa 1:** Analisar a polissemia da palavra 'Cão' (o animal doméstico mamífero versus o agrupamento de estrelas no céu).\n**Etapa 2:** Identificar a falácia dos quatro termos (quaternio terminorum): ao usar o mesmo vocábulo com significados conceituais distintos, viola-se a estrutura básica de três termos unívocos."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "No Livro IV da Metafísica, Aristóteles defende que o Princípio de Não Contradição não pode ser demonstrado por uma prova direta anterior. Como ele refuta aquele que tenta negar esse princípio?",
        "Condenando o debatedor ao exílio político imediato e aplicando pesadas multas em prata.",
        "Mostrando que, ao pronunciar qualquer palavra que pretenda significar algo determinado, o próprio debatedor já pressupõe e confirma a Não Contradição para comunicar seu pensamento.",
        "Afirmando que os princípios da lógica só valem para pessoas que estudaram mais de dez anos no Liceu.",
        "Aceitando que a contradição total é o estado normal da mente de qualquer sábio ateniense.",
        "Recorrendo a adivinhos que lançam dados sagrados para decidir qual proposição é a correta.",
        "B",
        "**Etapa 1:** Compreender por que um primeiro princípio universal indemonstrável não pode ter premissas anteriores (sob pena de regressão infinita).\n**Etapa 2:** Reconhecer a famosa demonstração por refutação elênctica: quem nega o princípio precisa articular palavras com sentido determinado; se a palavra significa X e não não-X, ele acabou de aplicar o princípio que pretendia negar."
    ))

    questoes_brutas.append((
        54, "EM13CHS105", "dificil",
        "No século XIX, George Boole formulou uma álgebra lógica binária, e no século XX Claude Shannon projetou os circuitos digitais dos computadores baseados em portas lógicas (AND, OR, NOT). Como esses desenvolvimentos tecnológicos se ligam à lógica de Aristóteles?",
        "Substituindo o raciocínio humano pela força mecânica de engrenagens de ferro movidas a vapor.",
        "Traduzindo os princípios lógicos de Aristóteles (Identidade, Não Contradição e Terceiro Excluído) em estados elétricos binários (verdadeiro/falso, 1/0) nas arquiteturas de computação.",
        "Comprovando que a lógica formal grega estava completamente errada e não tinha nenhuma utilidade prática.",
        "Provando que os computadores são dotados de alma imortal como pretendiam os discípulos da Academia.",
        "Mostrando que a eletricidade é uma manifestação direta do fogo primordial proposto por Heráclito.",
        "B",
        "**Etapa 1:** Identificar os princípios do Terceiro Excluído e Não Contradição como base para a lógica bivalente (verdadeiro ou falso).\n**Etapa 2:** Relacionar essa estrutura lógica à álgebra booleana e às portas de transistores na eletrônica moderna, onde a computação repousa sobre a mecânica binária (0 e 1) decorrente da lógica clássica."
    ))

    questoes_brutas.append((
        55, "EM13CHS103", "dificil",
        "Durante a Revolução Científica do século XVII, Galileu Galilei e René Descartes criticaram a física aristotélica. Qual aspecto da Teoria das Quatro Causas foi rejeitado na explicação da mecânica dos corpos inanimados pela ciência moderna?",
        "A causa material, pois a física moderna dispensou o uso de átomos e elementos químicos.",
        "A causa final, sendo abandonada na mecânica dos corpos físicos inanimados em favor de relações estritamente mecânicas de causa e efeito.",
        "A causa eficiente, já que a ciência moderna não aceita forças ou agentes de contato nos movimentos.",
        "A causa formal, porque a geometria das órbitas planetárias deixou de ter relevância matemática.",
        "Todas as quatro causas, que foram banidas de todos os ramos das universidades europeias.",
        "B",
        "**Etapa 1:** Contrastar a física aristotélica de princípios finalísticos com o paradigma mecanicista inaugurado no século XVII.\n**Etapa 2:** Concluir que a ciência moderna abandonou o recurso às causas finais para explicar o movimento de pedras e projéteis (adotando forças e equações mecanicistas), embora a finalidade funcional persista como metáfora indispensável na biologia."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Se a demonstração científica silogística exige premissas verdadeiras anteriores para deduzir novas conclusões, como a mente humana atinge os primeiros princípios universais indemonstráveis segundo Aristóteles?",
        "Por meio de adivinhações astrológicas e revelações místicas durante rituais noturnos.",
        "Por meio da indução (Epagogé) a partir da experiência sensível repetida e da intelecção racional (Nous) que capta as essências universais.",
        "Copiando as leis de civilizações mais antigas sem submetê-las a qualquer exame de razão.",
        "Esperando que os reis da cidade determinem por lei quais princípios são verdadeiros.",
        "Aceitando que os primeiros princípios são inventados pelo hábito sem relação com a verdade.",
        "B",
        "**Etapa 1:** Entender o desafio teórico de fundar as premissas iniciais da ciência demonstrativa sem cair em regressão infinita.\n**Etapa 2:** Explicar que Aristóteles recorre à observação empírica reiterada articulada à indução (Epagogé) e à intuição intelectiva (Nous), que abstrai o universal a partir dos casos sensíveis particulares."
    ))

    questoes_brutas.append((
        57, "EM13CHS101", "dificil",
        "Na obra Categorias, Aristóteles afirma que a Substância Primeira possui prioridade sobre as outras nove categorias de acidentes (qualidade, quantidade, relação, lugar, tempo, posição, estado, ação e paixão). Qual é a razão dessa prioridade?",
        "Porque os acidentes são divindades superiores que habitam o topo das montanhas.",
        "Porque os acidentes não podem existir por si mesmos no mundo real; eles precisam obrigatoriamente se apoiar em um sujeito substancial concreto.",
        "Porque as leis da língua grega proibiam o uso de adjetivos em frases filosóficas formais.",
        "Porque a quantidade matemática é a única propriedade que não varia quando o tempo passa.",
        "Porque a substância primeira é uma abstração puramente mental desprovida de realidade física.",
        "B",
        "**Etapa 1:** Distinguir a existência primária da substância individual dos atributos que a caracterizam.\n**Etapa 2:** Demonstrar que atributos como cor, tamanho ou peso (acidentes) não existem 'flutuando sozinhos no espaço'; dependem de uma substância primeira concreta de que são predicados (Sócrates é quem é alto e ateniense)."
    ))

    questoes_brutas.append((
        58, "EM13CHS103", "dificil",
        "Em debates filosóficos, algumas pessoas confundem a visão orientada a fins de Aristóteles com animismo, imaginando que pedras ou rios possuem desejos conscientes. Como a filosofia peripatética corrige rigorosamente esse engano?",
        "Afirmando que os rios e rochas pensam e sonham, mas em uma velocidade muito mais lenta que a dos animais.",
        "Esclarecendo que a orientação para fins na natureza não supõe consciência psicológica em seres inanimados, mas expressa tendências funcionais e regularidades estruturais inscritas na matéria.",
        "Concordando que qualquer árvore possui vontade racional igual à de um filósofo formado no Liceu.",
        "Dizendo que os seres inanimados não participam da física e pertencem ao reino das lendas poéticas.",
        "Defendendo que a física deve abandonar a pesquisa sobre causas e estudar apenas poemas dramáticos.",
        "B",
        "**Etapa 1:** Desconstruir a falsa atribuição de intenções psicológicas e sentimentos antropomórficos a objetos inanimados.\n**Etapa 2:** Evidenciar que o conceito aristotélico de Causa Final na natureza opera como regularidade biológica e física imanente (estrutura que orienta o desenvolvimento), sem exigir volição consciente."
    ))

    questoes_brutas.append((
        59, "EM13CHS101", "dificil",
        "Analise a relação entre o silogismo em modo Barbara ('Todo ser humano é mortal; Sócrates é ser humano; logo, Sócrates é mortal') e a teoria da substância. Qual relação entre substância primeira e substância segunda sustenta a solidez dessa dedução?",
        "O argumento é falso porque Sócrates é uma substância cósmica que nunca esteve sujeita à mortalidade terrena.",
        "A espécie universal 'ser humano' (substância segunda) expressa a essência predicada necessariamente do indivíduo singular concreto Sócrates (substância primeira), garantindo a certeza dedutiva.",
        "A mortalidade é um acidente passageiro que pode ser revogado por decisões dos governantes na assembleia.",
        "O silogismo não tem nenhuma ligação com o estudo do ser e funciona como mero passatempo de retórica.",
        "O termo mortal não possui sentido lógico e deve ser retirado dos manuais de dedução analítica.",
        "B",
        "**Etapa 1:** Reconhecer os papéis conceituais de substância primeira (o indivíduo singular Sócrates) e substância segunda (a espécie universal ser humano).\n**Etapa 2:** Concluir que a dedução silogística rigorosa apoia-se no fato de que os atributos essenciais da substância segunda aplicam-se necessariamente à substância primeira nela contida."
    ))

    questoes_brutas.append((
        60, "EM13CHS103", "dificil",
        "Ao articular o empirismo observacional com a fundação da lógica formal dedutiva, qual síntese metodológica perene Aristóteles legou à história da ciência ocidental?",
        "A desvalorização completa do raciocínio metódico em favor de experiências místicas e sonhos proféticos.",
        "A integração harmoniosa entre a observação minuciosa dos fenômenos do mundo empírico e o tratamento lógico dedutivo rigoroso das premissas e demonstrações racionais.",
        "A separação permanente entre o estudo da biologia e o estudo da lógica, declarando-os incompatíveis.",
        "A subordinação da ciência às crenças míticas e aos decretos dos generais guerreiros de Atenas.",
        "A imposição de fórmulas matemáticas vazias sem nenhum contato com as substâncias materiais da natureza.",
        "B",
        "**Etapa 1:** Analisar os dois pilares fundantes do método aristotélico: a atenção empírica ao mundo concreto e o rigor das regras formais do pensamento demonstrativo.\n**Etapa 2:** Sintetizar que essa união entre dados empíricos observáveis e estrutura lógica dedutiva constitui a base histórica fundamental para o desenvolvimento do método científico e racional ocidental."
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
capitulo: "cap-05-aristoteles-empirismo-logica-quatro-causas"
objeto_de_conhecimento: "A Crítica ao Dualismo Platônico; A Metafísica Aristotélica: A Substância; O Hilemorfismo (Matéria e Forma como Unidade Inseparável); A Dialética entre Ato e Potência; A Teoria das Quatro Causas: Material, Formal, Eficiente e Final; O Primeiro Motor Imóvel; A Criação da Lógica Clássica (Organon): O Silogismo, Os Princípios da Identidade, Não Contradição e Terceiro Excluído."
ebook_fonte: "em-fil-c05-aristoteles-empirismo-logica-quatro-causas.md"
habilidades: "EM13CHS101, EM13CHS103, EM13CHS105, H1, H2, H11"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: Aristóteles: Crítica ao Idealismo, Lógica e as Quatro Causas

"""

    corpo = header
    gabaritos_finais = []

    # Nível Básico
    corpo += "## Nível Básico\n\n"
    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        gabaritos_finais.append(gab)
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-05-aristoteles-empirismo-logica-quatro-causas -->\n"
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
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-05-aristoteles-empirismo-logica-quatro-causas -->\n"
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
        corpo += f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-05-aristoteles-empirismo-logica-quatro-causas -->\n"
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

- ARISTÓTELES. *Metafísica*. Tradução, introdução e notas de Giovanni Reale. Tradução para o português de Marcelo Perine. 2. ed. São Paulo: Loyola, 2002. v. 1 e 2.
- ARISTÓTELES. *Órganon: Categorias, Da Interpretação, Analíticos Anteriores, Analíticos Posteriores, Tópicos, Refutações Sofísticas*. Tradução de Edson Bini. São Paulo: Edipro, 2010.
- BARNES, Jonathan. *Aristóteles*. Tradução de Adail Ubirajara Sobral e Maria Stela Gonçalves. São Paulo: Loyola, 1995.
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.
- CHAUÍ, Marilena. *Introdução à História da Filosofia: Dos Pré-Socráticos a Aristóteles*. São Paulo: Companhia das Letras, 2002. v. 1.
- MARCONDES, Danilo. *Iniciação à História da Filosofia: Dos Pré-Socráticos a Wittgenstein*. 11. ed. Rio de Janeiro: Jorge Zahar, 2007.
- REALE, Giovanni. *História da Filosofia Antiga: Das Origens a Sócrates*. São Paulo: Loyola, 1993. v. 1.
- ROSS, David. *Aristóteles*. Tradução de Luís Filipe Bragança S. S. Teixeira. Lisboa: Dom Quixote, 1995.
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
        print("\n[SUCESSO TOTAL] Cap 05 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA NA VALIDAÇÃO] Exit code: {res_val.returncode}")
        sys.exit(res_val.returncode)

if __name__ == "__main__":
    gerar_cap05()
