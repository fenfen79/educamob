# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 22 de Filosofia EM:
Frantz Fanon e a Filosofia da Descolonização
Objeto: cap-22-frantz-fanon-filosofia-descolonizacao
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
        "Qual é a formação profissional e a origem geográfica do pensador Frantz Fanon, fundamentais para a criação de sua Filosofia da Descolonização?",
        "Engenheiro mecânico nascido na Inglaterra industrial vitoriana.",
        "Médico psiquiatra e ensaísta nascido na ilha caribenha da Martinica.",
        "Arquiteto urbanista nascido na capital imperial de Portugal.",
        "Advogado tributarista nascido na cidade portuária de Gênova.",
        "Professor de teologia medieval nascido nos Países Baixos.",
        "B",
        "Fanon nasceu na Martinica (colônia francesa caribenha) e formou-se médico psiquiatra na França, combinando a clínica psicológica e a luta política revolucionária."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Em qual conflito armado histórico Frantz Fanon atuou como combatente e diplomata da Frente de Libertação Nacional (FLN)?",
        "Na Guerra Civil Americana travada entre estados do norte e do sul.",
        "Na Guerra de Libertação da Argélia contra a dominação colonial francesa.",
        "Na Guerra dos Trinta Anos entre principados católicos e protestantes.",
        "Na Guerra do Peloponeso travada entre as cidades de Atenas e Esparta.",
        "Na Guerra da Crimeia entre impérios militares da Europa continental.",
        "B",
        "Fanon aderiu à Frente de Libertação Nacional (FLN) na Guerra da Argélia (1954-1962), tornando-se uma das vozes mais lúcidas da revolução anticolonial mundial."
    ))

    questoes_brutas.append((
        3, "EM13CHS601", "basico",
        "Ao trabalhar no Hospital Psiquiátrico de Blida-Joinville, qual diagnóstico clínico e político inovador Fanon estabeleceu sobre o sofrimento psíquico dos pacientes argelinos?",
        "Concluiu que as doenças mentais decorriam unicamente de carências vitamínicas alimentares.",
        "Compreendeu que a loucura e as perturbações mentais na Argélia eram sintomas clínicos diretos da violência estrutural e da desumanização da ocupação colonial.",
        "Afirmou que os distúrbios psiquiátricos eram causados por influências de climas áridos tropicais.",
        "Sustentou que os transtornos psíquicos resultavam da leitura excessiva de romances literários.",
        "Defendeu que as alucinações de pacientes eram originadas por disputas corporativas de artesãos.",
        "B",
        "Fanon diagnosticou que era impossível curar mentes oprimidas sem derrubar o colonialismo: a loucura era o efeito direto das torturas, da opressão e da humilhação racial imposta pela França."
    ))

    questoes_brutas.append((
        4, "EM13CHS602", "basico",
        "O que estabelece o conceito de 'Sociogênese' formulado por Frantz Fanon em Pele Negra, Máscaras Brancas (1952)?",
        "A tese de que o racismo decorre de determinantes genéticos e biológicos herdados da linhagem familiar.",
        "A demonstração de que a neurose e o complexo de inferioridade do homem negro são fabricados deliberadamente pela estrutura econômica e social racista do colonialismo.",
        "A ideia de que o preconceito social é uma ilusão linguística gerada por poetas medievais.",
        "A afirmação de que os conflitos étnicos decorrem de variações sazonais nas temperaturas continentais.",
        "A teoria de que as condutas humanas são reguladas exclusivamente por impulsos biológicos inatos.",
        "B",
        "A sociogênese fanoniana rompe com o biologismo e o individualismo: o complexo de inferioridade do negro não é congênito nem individual, mas gerado pela estrutura social e econômica da supremacia branca."
    ))

    questoes_brutas.append((
        5, "EM13CHS603", "basico",
        "Em Pele Negra, Máscaras Brancas, como Fanon conceitua a chamada 'Zona do Não-Ser' (*Zone de Non-Être*)?",
        "Um parque ecológico de preservação de espécies vegetais endêmicas em ilhas oceânicas.",
        "Uma região despojada em que o sistema racista nega ao negro o estatuto pleno de humanidade, razão e dignidade, reduzindo-o a mero corpo explorável.",
        "Um distrito comercial portuário isento de tributação sobre mercadorias estrangeiras.",
        "Uma câmara de debates diplomáticos instalada em palácios governamentais europeus.",
        "Um estágio místico alcançado por monges em práticas de meditação solitária nas montanhas.",
        "B",
        "A zona do não-ser representa o rebaixamento humano: na sociedade colonial eurocêntrica, apenas o branco é reconhecido como sujeito e cidadão de plenos direitos; o negro é empurrado para o vazio da desumanização."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "O que Fanon define como o fenômeno psíquico da 'Epidermalização da Inferioridade'?",
        "Uma doença de pele inflamatória comum a trabalhadores de lavouras canavieiras.",
        "A introjeção inconsciente, gravada no próprio corpo, de que a cultura e a estética brancas representam o padrão universal de beleza e humanidade, enquanto a cultura negra é associada ao atraso.",
        "A pigmentação artificial de tecidos de algodão para comercialização em bazares metropolitanos.",
        "A transmissão genética de características físicas adaptadas a climas equatoriais úmidos.",
        "O procedimento cirúrgico adotado por médicos para tratamento de queimaduras causadas por fogo.",
        "B",
        "A epidermalização da inferioridade é a colonização mental: o colonizado passa a sentir na própria pele uma suposta inferioridade, valorizando tudo o que é europeu e rejeitando suas raízes ancestrais."
    ))

    questoes_brutas.append((
        7, "EM13CHS102", "basico",
        "Qual é a trágica metáfora das 'Máscaras Brancas' adotadas por indivíduos colonizados na obra de Frantz Fanon?",
        "O uso obrigatório de máscaras de carnaval veneziano durante celebrações cívicas municipais.",
        "A tentativa angustiada e ilusória de indivíduos negros de assimilar a língua, a vestimenta e os costumes da elite metropolitana branca na esperança de escapar do desprezo racista.",
        "O disfarce utilizado por espiões militares para atravessar postos de fiscalização aduaneira.",
        "A proteção facial utilizada por mineradores de carvão para evitar a inalação de partículas tóxicas.",
        "O ritual religioso de pintura corporal praticado por congregações monásticas beneditinas.",
        "B",
        "Usar a máscara branca é o drama da assimilação colonial: o colonizado tenta falar francês polido e vestir-se como a burguesia europeia para ser respeitado, mas continua sendo discriminado pela cor de sua pele."
    ))

    questoes_brutas.append((
        8, "EM13CHS601", "basico",
        "Qual episódio doloroso vivenciado na França ilustra a destruição da subjetividade negra pelo olhar racista da criança metropolitana?",
        "A expulsão arbitrária de estudantes estrangeiros de salas de conferência universitária.",
        "O grito aterrorizado de uma criança branca ao apontar para Fanon na praça: 'Olhe, um preto! Mamãe, o preto vai me comer!', congelando o homem em objeto perigoso.",
        "A reprovação indevida de candidatos negros em testes escritos de admissão para os correios.",
        "A cobrança de tarifas inflacionadas para o embarque de passageiros antilhanos em trens suburbanos.",
        "A interdição de acesso a bibliotecas municipais durante feriados nacionais de comemoração cívica.",
        "B",
        "Fanon descreve a cena em que o olhar da criança branca o desumaniza: ele deixa de ser um médico e cidadão e é reduzido instantaneamente ao estereótipo do monstro negro devorador e selvagem."
    ))

    questoes_brutas.append((
        9, "EM13CHS602", "basico",
        "Na obra Os Condenados da Terra (1961), como Fanon descreve a estrutura física do 'Mundo Colonial Compartimentado'?",
        "Uma comunidade integrada de cidadãos que compartilham praças e teatros em perfeita fraternidade.",
        "Um espaço violentamente cindido em dois: a cidade rica, limpa e saciada do colono, e a cidade faminta, enlameada e confinada do colonizado, separadas por quartéis e baionetas.",
        "Uma federação pacífica de bairros autônomos governados por conselhos comunitários de artesãos.",
        "Um sistema de distritos rurais articulados por canais fluviais de navegação comercial livre.",
        "Uma vila ecológica planejada em torno de hortas comunitárias e bibliotecas populares abertas.",
        "B",
        "O mundo colonial é cindido: de um lado a cidade do colono (pedra, asfalto, fartura, guardada pela polícia) e do outro a cidade do nativo (lama, fome, amontoamento, cerca de arame e miséria)."
    ))

    questoes_brutas.append((
        10, "EM13CHS603", "basico",
        "Como a ideologia colonial opera a justificação de seu domínio através do chamado 'Maniqueísmo Desumanizador'?",
        "Apresentando os povos colonizados como parceiros comerciais iguais em tratados de livre navegação.",
        "Rotulando o colonizado não apenas como alguém sem valores morais, mas como a própria encarnação do Mal absoluto, preguiçoso e irracional por natureza, para legitimar a violência armada contínua.",
        "Ensinando línguas clássicas aos camponeses para integrá-los como parlamentares nos tribunais.",
        "Distribuindo terras férteis públicas para as famílias nativas com títulos de posse perpétua.",
        "Organizando torneios esportivos entre soldados metropolitanos e trabalhadores rurais locais.",
        "B",
        "O maniqueísmo colonial divide o mundo entre o Bem (o colonizador branco civilizado) e o Mal (o colonizado bestial e maligno); ao animalizar o nativo, o colonizador justifica o chicote e o canhão."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Por que, para Frantz Fanon, o colonialismo não pode ser derrubado unicamente através de debates retóricos amigáveis em mesas diplomáticas?",
        "Porque os representantes diplomáticos desconheciam os dialetos regionais dos países africanos.",
        "Porque o colonialismo não é uma máquina discursiva racional, mas a própria violência material armada em estado puro, que só recua quando confrontada por uma força revolucionária equivalente.",
        "Porque as salas consulares eram desprovidas de equipamentos de iluminação adequados para sessões noturnas.",
        "Porque as leis comerciais europeias proibiam a assinatura de acordos bilaterais com territórios ultramarinos.",
        "Porque os tratados de paz internacionais dependiam da anuência de comitês de navegadores marítimos mercantes.",
        "B",
        "O colonialismo entrou pela espada e pelo canhão e governa pelo medo da baioneta; pretender que ele saia por cortesias discursivas é uma ilusão burguesa: a libertação exige força real."
    ))

    questoes_brutas.append((
        12, "EM13CHS102", "basico",
        "Qual função libertadora individual Fanon atribui à práxis da violência revolucionária anticolonial em Os Condenados da Terra?",
        "A desintoxicação psíquica do colonizado, libertando-o do secular complexo de inferioridade e devolvendo-lhe a dignidade e a consciência de ser um homem livre e soberano.",
        "A celebração sádica de castigos corporais contra adversários desarmados capturados em campos rurais.",
        "A formação de corporações financeiras dedicadas à especulação imobiliária em praças litorâneas.",
        "A imposição de tributos extraordinários sobre a comercialização de grãos de cereais colhidos em aldeias.",
        "A criação de academias de oratória clássica para jovens aspirantes a carreiras burocráticas metropolitanas.",
        "A",
        "Fanon demonstra que, ao enfrentar o opressor na luta pela liberdade, o colonizado desintoxica sua alma: perde o medo paralisante, percebe que o colonizador não é um deus e refaz sua autoimagem de ser humano digno."
    ))

    questoes_brutas.append((
        13, "EM13CHS601", "basico",
        "Antes do início da revolta anticolonial armada, como se canalizava a agressividade reprimida das populações colonizadas subjugadas?",
        "Em investimentos bancários de poupança financeira depositados em cooperativas rurais.",
        "Em guerras tribais fratricidas entre vizinhos, disputas violentas internas e rituais de possessão mágica, voltando a raiva contra seus próprios irmãos.",
        "Na redação de petições pacíficas dirigidas anualmente aos monarcas das potências europeias.",
        "Na organização de festivais de teatro cômico encenados nos pátios de casernas militares.",
        "Na edificação de templos de pedra dedicados a divindades mitológicas do mar Mediterrâneo.",
        "B",
        "O colonizado, sem poder atingir o colonizador fortemente armado, descarregava a raiva acumulada em conflitos internos entre os próprios oprimidos; a luta de libertação redireciona essa energia contra o verdadeiro carrasco."
    ))

    questoes_brutas.append((
        14, "EM13CHS602", "basico",
        "No capítulo 'Desventuras da Consciência Nacional', qual advertência contundente Fanon faz a respeito da 'Burguesia Nacionalista Intermediária'?",
        "Elogia a classe como uma elite produtiva e criativa que moderniza as fábricas e promove a justiça social.",
        "Denuncia que essa burguesia nativa é uma casta parasitária e corrupta, desprovida de ideias, cujo único papel histórico é agir como gerente local submissa dos interesses das multinacionais e do neocolonialismo.",
        "Afirma que os comerciantes nativos deveriam assumir o controle total das escolas militares de aviação.",
        "Recomenda que os ministérios econômicos sejam chefiados exclusivamente por diretores de bancos europeus.",
        "Propõe que os sindicatos operários urbanos sejam extintos para acelerar as colheitas de grãos agrícolas.",
        "B",
        "Fanon profetizou a tragédia do neocolonialismo: a burguesia nacional herda o Estado colonial apenas para enriquecer suas famílias e servir de capataz do capital estrangeiro, traindo as esperanças do povo."
    ))

    questoes_brutas.append((
        15, "EM13CHS603", "basico",
        "O que caracteriza a chamada 'Falsa Independência' denunciada por Fanon nos processos de descolonização formal?",
        "A transformação imediata de todas as cidades periféricas em metrópoles industriais autônomas.",
        "A mera troca da cor da pele dos governantes nos palácios presidenciais e a troca de bandeiras, mantendo intactas a miséria do povo e a submissão financeira ao imperialismo europeu.",
        "A adoção de moedas cunhadas em barras de ouro puro para circulação nas feiras municipais.",
        "O fechamento obrigatório de todas as rotas marítimas que conectavam o continente africano à Ásia.",
        "A concessão de aposentadorias integrais a todos os camponeses e trabalhadores rurais das províncias.",
        "B",
        "Mudar a bandeira e colocar ministros negros de terno não é descolonização se as terras continuam nas mãos de estrangeiros e o povo na penúria; Fanon exige uma revolução social de raiz camponesa e popular."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Qual é a grande convocação ética e civilizatória final dirigida aos povos do Terceiro Mundo nas últimas páginas de Os Condenados da Terra?",
        "Imitar servilmente os padrões institucionais, a técnica militar e os costumes da Europa metropolitana.",
        "Abandonar a obsessão colonial de copiar a Europa (que ergueu seus monumentos sobre genocídios e massacres) e inventar um 'Homem Novo' e uma Nova Humanidade verdadeiramente emancipada.",
        "Submeter todas as decisões comunitárias à aprovação prévia de comitês bancários internacionais.",
        "Retornar a modos tribais ancestrais recusando qualquer contato com o conhecimento científico moderno.",
        "Transferir as capitais dos novos Estados independentes para colônias desabitadas na Groenlândia.",
        "B",
        "Fanon faz um apelo grandioso: a Europa falou em humanismo enquanto trucidava o mundo; os povos libertados não devem imitá-la, mas forjar um pensamento original e erguer um Homem Novo."
    ))

    questoes_brutas.append((
        17, "EM13CHS102", "basico",
        "De que modo a Lei Federal nº 10.639/2003 se relaciona diretamente com o estudo da obra e das teses de Frantz Fanon nas salas de aula brasileiras?",
        "Ao proibir a inclusão de autores estrangeiros em currículos escolares de ciências humanas.",
        "Ao tornar obrigatório o ensino da História e Cultura Afro-Brasileira e Africana, resgatando o pensamento de intelectuais negros fundamentais para o combate ao racismo estrutural.",
        "Ao determinar que os exames de vestibular devam conter exclusivamente questões sobre o direito romano.",
        "Ao estabelecer que a literatura moderna deva limitar-se ao estudo de poetas do classicismo grego.",
        "Ao restringir as pesquisas acadêmicas sobre relações étnico-raciais a centros de pós-graduação médica.",
        "B",
        "A Lei 10.639/03 repara a omissão racista dos currículos, inserindo mestres como Fanon para que os estudantes compreendam as raízes do colonialismo e a força emancipadora do pensamento negro mundial."
    ))

    questoes_brutas.append((
        18, "EM13CHS601", "basico",
        "Qual movimento político norte-americano dos anos 1960 adotou as obras de Frantz Fanon como guia teórico para organizar patrulhas de autodefesa contra a violência policial racista?",
        "O Partido dos Panteras Negras para Autodefesa (*Black Panther Party*), fundado por Huey Newton e Bobby Seale.",
        "A Associação de Comerciantes Varejistas de Madeira do estado de Nova York.",
        "A Liga de Veteranos da Marinha Mercante dos portos do Pacífico Norte.",
        "O Sindicato dos Mineradores de Carvão Betuminoso da Virgínia Ocidental.",
        "A Sociedade Protetora dos Museus de Belas Artes da Nova Inglaterra.",
        "A",
        "Os Panteras Negras leram Fanon nos guetos dos EUA: compreenderam que o gueto negro era uma colônia interna policiada por tropas armadas brancas e organizaram autodefesa e café comunitário para as crianças."
    ))

    questoes_brutas.append((
        19, "EM13CHS602", "basico",
        "Como a cisão colonial fanoniana entre 'a cidade do colono' e 'a cidade do colonizado' pode ser observada no espaço urbano das metrópoles brasileiras contemporâneas?",
        "Na completa ausência de disparidades de renda ou infraestrutura entre bairros nobres e favelas.",
        "Na drástica divisão entre bairros nobres litorâneos bem protegidos e as favelas e periferias negligenciadas pelo Estado, submetidas a incursões policiais armadas rotineiras e falta de saneamento.",
        "Na ocupação uniforme de todas as residências municipais por famílias de artesãos cooperados.",
        "Na proibição legal do tráfego de veículos automotores em áreas residenciais metropolitanas.",
        "Na concessão de isenção de impostos prediais exclusivamente para proprietários de edifícios antigos.",
        "B",
        "O Brasil reflete o modelo compartimentado de Fanon: bairros ricos cheios de asfalto, segurança privada e jardins floridos, enquanto a poucos quilômetros a favela negra vive sob tiroteios, lama e sem esgoto."
    ))

    questoes_brutas.append((
        20, "EM13CHS603", "basico",
        "Qual célebre filósofo existencialista francês assinou o inflamado prefácio da primeira edição de Os Condenados da Terra em 1961?",
        "Jean-Paul Sartre, que convocou os intelectuais europeus a escutarem a voz impetuosa da revolução anticolonial.",
        "René Descartes, que propôs o método dedutivo para o planejamento de estradas coloniais.",
        "Auguste Comte, que defendeu a aplicação de leis positivistas à administração hospitalar.",
        "Montesquieu, que sugeriu a tripartição de cargos consulares em províncias ultramarinas.",
        "Jean-Jacques Rousseau, que redigiu tratados sobre a educação campestre de jovens fidalgos.",
        "A",
        "Jean-Paul Sartre escreveu o célebre prefácio de Os Condenados da Terra, afirmando aos europeus que a violência que retornava das colônias era o espelho exato da violência com que a Europa as subjugou."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Como Frantz Fanon articula o marxismo e a questão racial em Os Condenados da Terra, subvertendo a ortodoxia eurocêntrica que reduzia todos os conflitos sociais unicamente à classe econômica?",
        "Afirmando que a economia é irrelevante e que apenas a cor da pele determina as disputas mundiais.",
        "Demonstrando que, no contexto colonial, a infraestrutura econômica é inseparável da raça: você é rico porque é branco, e você é branco porque é rico; a análise marxista precisa ser estendida para compreender a clivagem racial.",
        "Sustentando que os camponeses colonizados deveriam rejeitar greves em favor de petições de caridade.",
        "Provando que a luta operária industrial deve ser subordinada aos interesses da nobreza imperial.",
        "Defendendo que a distribuição de rendas deve ser administrada por companhias mercantis de navegação.",
        "B",
        "Fanon estende Marx: na colônia, raça e classe coincidem; o colono branco é o dono da terra e do capital, e o negro colonizado é o proletário explorado; não há como entender a economia colonial sem enxergar o racismo."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Em Pele Negra, Máscaras Brancas, Fanon analisa a assimilação linguística da língua francesa pelos antilhanos: qual é a armadilha psíquica e cultural oculta no domínio polido da língua da metrópole?",
        "A perda da capacidade de ler romances traduzidos de autores clássicos do Mediterrâneo.",
        "A crença ingênua de que falar perfeitamente a língua do colonizador concede ao homem negro o estatuto de homem branco igual, quando na verdade expressa a submissão ao imaginário cultural do dominador.",
        "O encarecimento das mensalidades cobradas por escolas particulares de gramática no Caribe.",
        "A dificuldade de comerciar gêneros agrícolas com portos mercantes do oceano Pacífico.",
        "A imposição de tributos postais extraordinários sobre cartas remetidas para o exterior.",
        "B",
        "Fanon alerta: dominar o francês é vestir o mundo do branco; o antilhano que fala a língua metropolitana pensa que se tornou igual ao europeu, mas o sistema racista o reduz à sua cor na primeira esquina."
    ))

    questoes_brutas.append((
        23, "EM13CHS601", "intermediario",
        "Por que Fanon adverte que os movimentos de 'Negritude', ao exaltarem a pureza mística da cultura ancestral negra, correm o risco de cair em uma armadilha essencialista se não avançarem para a luta política concreta?",
        "Porque as cerimônias poéticas exigiam a utilização de tecidos caros importados do Oriente.",
        "Porque o apego nostálgico e estético a um passado ancestral glorioso, desprovido de engajamento revolucionário no presente, transforma a identidade em fetiche inofensivo que não perturba a dominação colonial.",
        "Porque os livros de poemas africanos eram censurados por corporações de livreiros metropolitanos.",
        "Porque os governos coloniais subsidiavam companhias de teatro cômico itinerantes no interior.",
        "Porque as danças folclóricas dependiam da autorização de magistrados de comarcas provinciais.",
        "B",
        "Fanon admirava Aimé Césaire, mas alertava: poetizar um passado idílico não liberta a África do exército francês; a identidade negra deve ser uma faísca de luta política presente, não um museu estético passivo."
    ))

    questoes_brutas.append((
        24, "EM13CHS602", "intermediario",
        "Qual é a crítica contundente de Frantz Fanon ao papel dos intelectuais colonizados ocidentalizados no início dos processos de insurreição popular anticolonial?",
        "Acusa-os de terem estudado unicamente ciências exatas e esquecido a história das artes visuais.",
        "Denuncia que muitos intelectuais assimilados sentem horror à violência das massas camponesas, preferindo conciliações tíbias e reformas graduais que preservam seus privilégios de classe perante o colonizador.",
        "Mostra que os acadêmicos nativos desconheciam a língua oficial das capitais europeias metropolitanas.",
        "Comprova que os professores universitários eram remunerados em moedas metálicas desvalorizadas.",
        "Afirma que os escritores das colônias recusavam publicar livros em tipografias mecanizadas modernas.",
        "B",
        "O intelectual ocidentalizado teme o levante do povo: acostumado aos salões burgueses, ele prega prudência e moderação, enquanto o camponês empobrecido na aldeia sabe que só a força quebra o jugo do colono."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "Como a categoria fanoniana de 'Lumpemproletariado' difere da visão clássica marxista, assumindo um papel de vanguarda revolucionária em Os Condenados da Terra?",
        "Marx tratava os marginalizados urbanos desocupados com desconfiança e potencial reacionário, enquanto Fanon os enxerga como uma força explosiva indispensável, disposta a pegar em armas contra a colônia.",
        "Marx considerava os camponeses proprietários a única classe capaz de dirigir revoluções industriais.",
        "Fanon afirmava que os marinheiros mercantes deveriam constituir o comitê central do governo transitório.",
        "Marx defendia que os mendigos urbanos fossem deportados para colonizar províncias árticas desabitadas.",
        "Fanon sustentava que os banqueiros metropolitanos eram a classe mais generosa nas revoluções cívicas.",
        "A",
        "Marx via o lumpemproletariado (desempregados, marginalizados) como massa instável vendível; Fanon o resgata: nas cidades coloniais, essa massa sem nada a perder é ponta de lança da revolta armada."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Ao investigar os distúrbios psiquiátricos causados pela Guerra da Argélia, qual descoberta estarrecedora Fanon relata sobre o estado mental dos policiais e militares torturadores franceses?",
        "Verificou que os torturadores eram dotados de imunidade psicológica perfeita a qualquer sentimento de culpa.",
        "Constatou que os próprios algozes desenvolviam psicoses gravíssimas, insônia crônica, delírios persecutórios e acessos de agressividade doméstica contra esposas e filhos, provando que a tortura desumaniza quem a pratica.",
        "Comprovou que os oficiais do exército metropolitano recebiam treinamentos regulares de meditação budista.",
        "Observou que os interrogadores militares eram recrutados exclusivamente entre monges eremitas alpinos.",
        "Descobriu que as sessões de espancamento eram supervisionadas por comissões de filologia clássica.",
        "B",
        "A violência colonial é um bumerangue venenoso: Fanon atendeu os próprios torturadores franceses enlouquecidos pelo horror que causavam, provando clinicamente que a opressão corrói a humanidade do algoz."
    ))

    questoes_brutas.append((
        27, "EM13CHS102", "intermediario",
        "De que modo a denúncia fanoniana sobre as 'Desventuras da Consciência Nacional' antecipou o surgimento de ditaduras militares e o enriquecimento de oligarquias na África pós-colonial?",
        "Mostrando que os generais africanos eram formados em academias navais do mar Báltico.",
        "Evidenciando que a burguesia nacionalista sem base produtiva, incapaz de saciar as necessidades do povo, recorre à demagogia étnica e ao autoritarismo policial para se perpetuar no poder como ditadura neocolonial.",
        "Provando que as constituições pós-coloniais proibiam a existência de tribunais de justiça civis.",
        "Afirmando que a crise financeira dos novos países decorria da exportação desregulada de sal marinho.",
        "Demonstrando que os conflitos políticos surgiam de rivalidades esportivas entre cidades vizinhas.",
        "B",
        "Fanon profetizou: sem projeto socialista e popular, os libertadores de ontem viram os tiranos de hoje; a burguesia nacional, incapaz de gerar riqueza, transforma o partido único em instrumento de pilhagem do país."
    ))

    questoes_brutas.append((
        28, "EM13CHS601", "intermediario",
        "Qual é a distinção crucial estabelecida por Fanon entre o 'Camponês das Colônias' e o 'Proletário Urbano da Metrópole' na direção das revoluções de libertação?",
        "Nas colônias, o proletariado urbano é uma minoria relativamente privilegiada com empregos estáveis, enquanto os camponeses famintos do campo são a massa verdadeiramente revolucionária sem nada a perder.",
        "Na metrópole europeia, os camponeses dominavam as comissões de acionistas de ferrovias a vapor.",
        "Nas colônias ultramarinas, os operários fabris recebiam remunerações em lingotes de prata e joias.",
        "Na metrópole, os trabalhadores rurais lideravam os sindicatos de navegação fluvial em botes a remo.",
        "Nas possessões imperiais, os artesãos de cerâmica controlavam a totalidade dos postos de alfândega.",
        "A",
        "Ao contrário da Europa onde a fábrica liderava, na colônia o camponês espoliado pela metrópole é o motor da revolução; o pequeno operário da cidade colonial muitas vezes teme perder o pouco que tem."
    ))

    questoes_brutas.append((
        29, "EM13CHS602", "intermediario",
        "Como a crítica de Fanon à modernidade europeia desconstrói o discurso colonial de que a Europa estava cumprindo uma 'Missão Civilizadora' na África e na Ásia?",
        "Afirmando que as ferrovias e escolas construídas pelo império compensavam as mortes acidentais de nativos.",
        "Evidenciando que a dita 'missão civilizadora' foi a máscara hipócrita para pilhagens massivas, destruição de línguas nativas, imposição de trabalhos forçados e assassinato em massa dos povos subjugados.",
        "Provando que os governadores coloniais eram orientados por diretrizes formuladas por conselhos de astrônomos.",
        "Demonstrando que os manuais escolares franceses ensinavam com fidelidade a história das monarquias africanas.",
        "Sustentando que as epidemias que dizimaram populações nativas foram causadas por eventos meteorológicos solares.",
        "B",
        "A civilização foi uma farsa: por trás de belos discursos de liberdade e direitos do homem, a Europa usou trabalho escravo, tortura e pilhagem para enriquecer suas metrópoles e pauperizar o Terceiro Mundo."
    ))

    questoes_brutas.append((
        30, "EM13CHS603", "intermediario",
        "Por que, para Fanon, a solidariedade revolucionária entre os povos do Terceiro Mundo (África, Ásia e América Latina) é essencial para resistir ao imperialismo ocidental?",
        "Porque os tratados de navegação fluvial dependiam da padronização de bandeiras marítimas.",
        "Porque o imperialismo atua como uma rede global de exploração econômica e militar; nações isoladas tornam-se presas fáceis de chantagens financeiras e invasões de potências dominantes metropolitanas.",
        "Porque os países periféricos precisavam unificar suas regras gramaticais para a impressão de jornais.",
        "Porque os comitês de embaixadores eram obrigados a falar fluentemente a língua grega clássica.",
        "Porque a exportação de grãos de café dependia da autorização de magistrados de comarcas alpinas.",
        "B",
        "Fanon defende o internacionalismo tricontinental: um país isolado não aguenta a pressão do capital estrangeiro e das armadas imperiais; a libertação autêntica exige aliança firme entre todos os oprimidos do planeta."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Em Pele Negra, Máscaras Brancas, qual é a crítica de Fanon à psicanálise ortodoxa freudiana e ao complexo de Édipo quando aplicados mecanicamente às populações colonizadas da Martinica?",
        "Afirma que os livros de Sigmund Freud eram redigidos em língua de difícil tradução para idiomas caribenhos.",
        "Demonstra que o sofrimento psíquico do antilhano não nasce da rivalidade com a figura paterna no lar, mas do choque traumático com o mundo branco colonizador que o rotula como inferior e perigoso.",
        "Sustenta que as consultas psicanalíticas deveriam ser realizadas ao ar livre em praias tropicais.",
        "Comprova que os sonhos dos colonizados continham exclusivamente menções a tempestades marítimas.",
        "Determina que a psicanálise só pode ser aplicada a cidadãos que possuam patentes de oficiais da marinha.",
        "B",
        "A neurose antilhana não vem do pai, vem do colonialismo: o drama psíquico de um jovem negro caribenho é deflagrado quando a sociedade racista branca o rejeita, tornando Freud insuficiente sem a sociogênese política."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Qual é a denúncia de Frantz Fanon sobre a cumplicidade de certos ramos da Igreja e de missionários religiosos na consolidação da dominação colonial?",
        "Mostra que os missionários dedicavam suas manhãs à catalogação botânica de sementes silvestres.",
        "Evidencia que certas instituições religiosas atuaram como ponta de lança da pacificação dos nativos, pregando a resignação passiva perante o sofrimento terreno enquanto as terras eram confiscadas pelos colonos.",
        "Comprova que os edifícios de mosteiros eram construídos com pedras importadas de montanhas nórdicas.",
        "Afirma que as congregações religiosas incentivavam a criação de milícias armadas de trabalhadores rurais.",
        "Determina que as orações em capelas coloniais eram pronunciadas em línguas tribais sem censura.",
        "B",
        "Fanon lembra a célebre verdade colonial: quando o branco chegou, ele tinha a Bíblia e o negro tinha a terra; os missionários ensinaram o negro a fechar os olhos e orar; quando abriu os olhos, o branco tinha a terra e o negro a Bíblia."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "De que modo as teorias de Fanon sobre a libertação armada influenciaram líderes das guerras de descolonização nas colônias portuguesas da África nas décadas de 1960 e 1970?",
        "Estimulando a assinatura de pactos de vassalagem voluntária com os monarcas de Lisboa.",
        "Inspirando líderes como Amílcar Cabral (Guiné-Bissau), Samora Machel (Moçambique) e Agostinho Neto (Angola) a unirem a guerrilha camponesa, a alfabetização popular e a construção de uma nova sociedade sem classes.",
        "Promovendo a importação compulsória de manuais didáticos de teologia escolástica medieval.",
        "Incentivando a criação de empresas de exportação de azeite chefiadas por fidalgos metropolitanos.",
        "Exigindo que os exércitos guerrilheiros utilizassem unicamente uniformes de seda branca nas matas.",
        "B",
        "FRELIMO, MPLA e PAIGC colocaram Fanon em prática: a luta anticolonial contra o fascismo português educou o povo, integrou mulheres na liderança e refundou a soberania de Moçambique, Angola e Guiné-Bissau."
    ))

    questoes_brutas.append((
        34, "EM13CHS602", "intermediario",
        "Como a categoria fanoniana de 'Alienação Cultural' explica o menosprezo que indivíduos colonizados sentem por suas próprias tradições ancestrais e culinárias?",
        "Como uma preferência gastronômica espontânea e livre motivada pelo paladar individual de cada cidadão.",
        "Como o efeito planejado da hegemonia cultural colonizadora, que convence o oprimido de que seus costumes ancestrais são primitivos e vergonhosos, fazendo-o desejar imitar a cultura do opressor para ser aceito.",
        "Como uma determinação biológica regulada pelo funcionamento de glândulas salivares humanas.",
        "Como uma consequência da carência de sal marinho nas feiras comerciais de províncias agrícolas.",
        "Como um fenômeno decorrente da ausência de fornos industriais em aldeias tradicionais de pescadores.",
        "B",
        "A alienação cultural destrói a autoestima: o colonizado tem vergonha de seu prato, de sua dança e de sua fé ancestral, sonhando em consumir o que vem da Europa para sentir-se pertencente ao mundo 'civilizado'."
    ))

    questoes_brutas.append((
        35, "EM13CHS603", "intermediario",
        "Ao proclamar a necessidade de criar um 'Homem Novo', qual modelo civilizatório Fanon rejeita de modo absoluto e enfático?",
        "O modelo comunista de conselhos operários organizados em cooperativas rurais autônomas.",
        "O modelo eurocêntrico capitalista, que proclamou os direitos humanos em seus parlamentos metropolitanos enquanto promovia o massacre, o racismo e a escravização nas terras do Sul Global.",
        "O modelo astronômico heliocêntrico desenvolvido por cientistas do Renascimento científico.",
        "O modelo de tribunais arbitrais comunitários praticado por aldeias pesqueiras tradicionais.",
        "O modelo de conservação ecológica adotado por guardas florestais em reservas naturais.",
        "B",
        "O Homem Novo não nasce de imitar a Europa burguesa: Fanon alerta que tentar copiar a Europa levará ao mesmo cinismo, à mesma crueldade imperialista e à desumanização que os povos colonizados sofreram."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Como a teoria pós-colonial de Edward Said, expressa em Orientalismo (1978), dá continuidade às teses de Frantz Fanon sobre a fabricação do colonizado pelo dominador?",
        "Provando que os mercadores árabes dominavam as rotas comerciais de especiarias no mar Cáspio.",
        "Demonstrando como o Ocidente construiu discursivamente e academicamente o 'Oriente' como um espaço exótico, irracional e bárbaro, justificando a intervenção militar imperialista sob a capa de estudos científicos.",
        "Sustentando que as pinturas renascentistas representavam fielmente os desertos do Oriente Médio.",
        "Comprovando que as traduções da literatura árabe foram realizadas exclusivamente por monges copistas.",
        "Determinando que o comércio de tapetes artesanais dependia da chancela de conselhos consulares britânicos.",
        "B",
        "Said bebe diretamente em Fanon: o império inventa o 'oriental' ou o 'negro' como seres inferiores para justificar sua invasão e pilhagem; o saber acadêmico do colonizador serve à sua geopolítica de dominação."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "Qual é o significado da célebre afirmação de Fanon em Os Condenados da Terra: 'A descolonização é verdadeiramente a criação de homens novos'?",
        "Que os novos governantes republicanos deveriam receber títulos honoríficos de cavalaria medieval.",
        "Que o processo de libertação transforma radicalmente a subjetividade do colonizado: a criatura humilhada e passiva morre na luta, e em seu lugar nasce um cidadão ativo, confiante e senhor de seu próprio destino.",
        "Que as certidões de nascimento emitidas nas províncias ultramarinas deveriam conter selos em ouro.",
        "Que as crianças nascidas após a independência deveriam prestar serviços em marinhas mercantes mercenárias.",
        "Que os jovens estudantes deveriam memorizar códigos jurídicos em línguas mortas do Mediterrâneo.",
        "B",
        "Descolonização não é evento burocrático no cartório: é o parto do homem novo; ao pegar o leme da própria história, o colonizado enterra o servo covarde e levanta-se como cidadão soberano e altivo."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Por que, segundo Fanon, as massas populares colonizadas sentem profunda aversão aos acordos de 'compromisso pacífico' costurados nos bastidores pelas elites metropolitanas e burguesas nativas?",
        "Porque os acordos eram redigidos em folhas de papel fabricadas com fibras vegetais ásperas.",
        "Porque esses conchavos de cúpula negociam a independência formal por cima do povo, mantendo intactas as fazendas coloniais, a exploração do trabalho e a subordinação bancária do país.",
        "Porque as cerimônias de assinatura de tratados ocorriam em salões de baile com ingressos caros.",
        "Porque os governadores coloniais exigiam o pagamento de tributos em caravelas de madeira maciça.",
        "Porque as leis eleitorais aprovadas nos parlamentos concediam isenções tributárias a tecelões.",
        "B",
        "O povo sabe que o 'acordo de paz' das elites é traição: os ricos nativos ganham os ministérios e as mansões dos colonos, enquanto os camponeses que sangraram na lavoura continuam na mesma miséria sem terra."
    ))

    questoes_brutas.append((
        39, "EM13CHS602", "intermediario",
        "De que modo a psiquiatria praticada por Fanon em Blida prefigurou os princípios fundamentais da Luta Antimanicomial contemporânea?",
        "Ao trancar os internos em celas de pedra escuras e proibir a realização de atividades coletivas.",
        "Ao derrubar as correntes, respeitar as referências linguísticas e culturais árabes dos pacientes, introduzir a terapia ocupacional e associar a saúde mental à conquista da liberdade e dos direitos civis.",
        "Ao prescrever tratamentos farmacêuticos experimentais em doses massivas a todos os enfermos internados.",
        "Ao transferir os hospitais psiquiátricos para fortalezas militares desativadas nas ilhas costeiras.",
        "Ao exigir que os pacientes realizassem marchas em formação militar antes das refeições comunitárias.",
        "B",
        "Fanon foi pioneiro da antipsiquiatria e da reforma manicomial: em Blida, ele humanizou o asilo, aboliu maus-tratos e mostrou que a loucura não se cura com jaulas, mas com dignidade, escuta e liberdade social."
    ))

    questoes_brutas.append((
        40, "EM13CHS603", "intermediario",
        "Como a crítica fanoniana à burguesia nacionalista auxilia a compreensão das desigualdades regionais e do subdesenvolvimento persistente na América Latina?",
        "Demonstrando que os países latino-americanos enriqueceram graças à exportação de tecidos finos para a Europa.",
        "Evidenciando que as elites locais latino-americanas historicamente atuaram como sócias menores do imperialismo, exportando matérias-primas baratas e explorando a classe trabalhadora sem projeto nacional.",
        "Provando que as constituições republicanas do continente foram redigidas por generais prussianos.",
        "Sustentando que as crises econômicas regionais decorrem unicamente da ausência de minas de carvão vegetal.",
        "Afirmando que a estabilidade social foi alcançada com a abolição definitiva de tarifas alfandegárias.",
        "B",
        "A análise de Fanon se aplica à perfeição à América Latina: nossas elites agroexportadoras e financeiras sempre preferiram mandar o dinheiro para a Suíça e explorar o povo a construir uma nação soberana e justa."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Examine a tese existencial e estrutural da 'Zona do Não-Ser' formulada em Pele Negra, Máscaras Brancas: de que maneira o colonialismo estrutura uma linha de fratura humana e política na modernidade ocidental, onde a plenitude do estatuto de Sujeito de Direito é negada ao corpo racializado?",
        "Provando que as faculdades de direito medievais realizavam audiências unicamente em dias ensolarados.",
        "Demonstrando que a concepção moderna eurocêntrica de humanidade se ergueu sobre uma exclusão originária: o homem branco é definido como o paradigma universal da Razão e da Moralidade (a Zona do Ser), enquanto o sujeito negro é despojado de agência e empurrado para a Zona do Não-Ser, onde a lei constitucional não se aplica e a violência soberana opera sem cometer crime nem escândalo ético.",
        "Determinando que os contratos comerciais ultramarinos deveriam ser arquivados em baús de mogno maciço.",
        "Afirmando que as teorias filosóficas clássicas foram formuladas exclusivamente por navegadores de caravelas.",
        "Comprovando que as distinções sociais das colônias dependiam de certificados de pontualidade burocrática.",
        "B",
        "- **Etapa 1:** Compreender a cartografia humana e existencial do mundo moderno: na Zona do Ser habitam os sujeitos metropolitanos brancos, protegidos por garantias legais, contratos e direitos humanos universais.\n- **Etapa 2:** Desvelar a Zona do Não-Ser de Fanon: para que a Zona do Ser exista, cria-se a margem desumanizada do colonizado; na Zona do Não-Ser, a vida é descartável, o trabalho é superexplorado e a violência policial é a norma invisível que sustenta a ordem."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Analise a dialética do reconhecimento em Frantz Fanon em contraponto à clássica 'Dialética do Senhor e do Escravo' de G. W. F. Hegel: por que, no contexto da escravidão colonial racializada, a superação dialética hegeliana do reconhecimento mútuo fracassa redondamente?",
        "Porque os operários têxteis alemães recusavam produzir uniformes para os generais da corte prussiana.",
        "Porque na dialética de Hegel o senhor deseja o reconhecimento humano da consciência do escravo, ao passo que no colonialismo racista o colono branco não quer o reconhecimento do negro, quer unicamente o seu trabalho servil gratuito; não havendo desejo de reconhecimento mútuo, a libertação não vem do trabalho dócil, mas da ruptura armada radical.",
        "Comprovando que os tratados filosóficos hegelianos foram traduzidos incorretamente por tipógrafos parisienses.",
        "Determinando que as disputas de terras rurais eram resolvidas por torneios de esgrima entre mestres e alunos.",
        "Afirmando que os exércitos imperiais europeus eram compostos unicamente por marinheiros veteranos mercenários.",
        "B",
        "- **Etapa 1:** Relembrar a tese de Hegel: senhor e escravo travam uma luta até a morte por reconhecimento, e o escravo liberta-se pelo domínio técnico do trabalho transformador da matéria.\n- **Etapa 2:** Revelar a ruptura fanoniana: no racismo colonial, o senhor não vê uma 'consciência' no negro, mas uma besta de carga; o trabalho não liberta o escravo negro, apenas o desgasta até a morte; por isso, a libertação exige a revolta violenta que força o opressor a reconhecer a humanidade do outro."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Ao dissecar o primeiro capítulo de Os Condenados da Terra ('Da Violência'), Fanon estabelece a fórmula dialética: 'O colonialismo não é uma máquina pensante, é a violência em estado puro; logo, só pode vergar diante de uma violência maior.' Analise os fundamentos materiais e históricos dessa proposição para refutar a tese liberal da 'transição pacífica negociada'.",
        "Mostrando que os armamentos militares metropolitanos eram construídos com ligas metálicas deterioráveis.",
        "Evidenciando que o colonialismo é um sistema edificado e sustentado exclusivamente pela coerção armada (invasões, canhões, polícias e prisões); pretender que essa máquina de dominação material abdique espontaneamente de seus lucros e de sua hegemonia por persuasão moral é uma fantasia alienante: a violência anticolonial é a contra-violência necessária para desmantelar a opressão.",
        "Determinando que as assembleias parlamentares metropolitanas fechavam suas portas em períodos de seca fluvial.",
        "Afirmando que as rebeliões camponesas eram financiadas por companhias mercantis de exportação de seda.",
        "Comprovando que as disputas coloniais territoriais decorriam da escassez de cavalos de corrida nas metrópoles.",
        "B",
        "- **Etapa 1:** Analisar a natureza intransigente do império: o colonizador não ocupa a África por engano moral ou desinformação, mas por sede de matérias-primas e exploração capitalista armada.\n- **Etapa 2:** Desmistificar a conciliação liberal pacífica: a metrópole jamais entrega o poder por gentileza diplomática; a contra-violência revolucionária atua como a única força capaz de romper a cerca do colono e forçar o fim do império."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Examine a tese psicológica revolucionária de Fanon sobre a função desintoxicante da violência anticolonial no nível dos indivíduos: de que maneira o ato de pegar em armas contra o colonizador opera uma cura terapêutica da alienação e da neurose colonial?",
        "Comprovando que as substâncias químicas da pólvora possuíam propriedades medicinais ansiolíticas.",
        "Demonstrando que a repressão secular inculcou no colonizado um sentimento de impotência, paralisia e temor reverencial perante o dominador branco; ao engajar-se na luta e ver a vulnerabilidade física do opressor, o oprimido expulsa o medo introjetado, recupera a autoestima destruída e renasce psiquicamente como ser humano soberano e audaz.",
        "Determinando que os soldados revolucionários deviam jejuar antes das marchas pelas florestas equatoriais.",
        "Afirmando que as táticas de guerrilha foram ensinadas por conselhos de astrônomos de mosteiros medievais.",
        "Provando que as patrulhas camponesas utilizavam unicamente instrumentos musicais de percussão nas batalhas.",
        "B",
        "- **Etapa 1:** Compreender a patologia da servidão colonial: séculos de chicote fazem o oprimido acreditar que o branco é invencível e quase sobrenatural, gerando depressão, raiva autodestrutiva e passividade.\n- **Etapa 2:** Desvelar a cura pela práxis libertadora: ao disparar contra a tropa colonial, o combatente vê o dominador sangrar e tombar; o mito do semideus branco cai por terra e o colonizado cura sua mente, tornando-se um homem livre de pé."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Analise a anatomia sociológica do 'Mundo Colonial Compartimentado' e seu maniqueísmo desumanizador: de que forma a produção espacial de cidades segregadas antecipa a lógica dos estados de segregação racial (como o Apartheid sul-africano) e a segregação socioespacial contemporânea?",
        "Provando que os planos urbanos metropolitanos eram projetados por arquitetos de caravelas mercantes.",
        "Evidenciando que a segregação colonial não é mera disparidade acidental de rendimentos, mas uma partição institucionalizada pela força das armas: erguem-se barreiras intransponíveis que confinam o negro na zona de precarização e violência, enquanto o branco desfruta de segurança e privilégios, naturalizando a divisão do gênero humano em espécies biológicas e morais irreconciliáveis.",
        "Determinando que os muros de contenção das cidades coloniais deviam ser pintados de tintas amarelas.",
        "Afirmando que a divisão dos bairros obedecia a critérios de classificação astronômica das constelações.",
        "Comprovando que as ruas asfaltadas eram reservadas exclusivamente a funcionários dos correios imperiais.",
        "B",
        "- **Etapa 1:** Analisar a geografia de classes e raças na colônia: o mundo fanoniano é dividido fisicamente pelo fuzil policial; não há passagem livre entre a casbah e os bulevares do colonizador.\n- **Etapa 2:** Conectar ao Apartheid e às cidades atuais: essa cisão materializou-se nas leis do Apartheid e segue viva nas metrópoles de hoje, onde a favela periférica é cercada por operações policiais violentas para proteger os bairros ricos."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Investigue a advertência fanoniana sobre as 'Desventuras da Consciência Nacional': por que a tomada do poder pela burguesia nacionalista sem um projeto socialista e sem a mobilização permanente das massas camponesas converte fatalmente o novo Estado em uma ditadura neocolonial burocrática e corrupta?",
        "Comprovando que os ministros de finanças pós-coloniais desconheciam o funcionamento de calculadoras mecânicas.",
        "Demonstrando que a burguesia nacionalista periférica não tem vocação industrial nem capital produtivo acumulado; ela é meramente intermediária e compradora, usando a máquina do Estado para desviar recursos públicos, manter o monopólio familiar dos negócios e reprimir o povo insatisfeito, atuando como capitão-do-mato a serviço das corporações imperialistas metropolitanas.",
        "Determinando que os embaixadores africanos deveriam prestar juramentos de obediência a generais prussianos.",
        "Afirmando que a crise de alimentos resultava unicamente da proliferação de pragas de gafanhotos migratórios.",
        "Provando que os parlamentos das nações independentes realizavam reuniões em palácios de madeira frágil.",
        "B",
        "- **Etapa 1:** Descrever o perfil raquítico da burguesia nacional: ao contrário da burguesia europeia do século XIX que construiu indústrias e estradas de ferro, a elite local pós-colonial é parasita e preguiçosa.\n- **Etapa 2:** Diagnosticar o golpe neocolonial: sem base econômica real, essa burguesia vira sócia de bancos estrangeiros; para abafar os protestos da população esfomeada, militariza o governo e instaura uma ditadura de partido único corrupta."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Examine o manifesto final de Os Condenados da Terra: 'Não prestemos homenagem à Europa criando estados, instituições e sociedades que nela se inspirem.' Como essa recusa radical do eurocentrismo lança as bases para as epistemologias descoloniais contemporâneas e a superação do pensamento colonial universalizante?",
        "Afirmando que as universidades europeias deveriam ser transferidas compulsoriamente para florestas equatoriais.",
        "Evidenciando que o universalismo abstrato europeu é falso e cúmplice da barbárie: a Europa ergueu suas catedrais e discursos de liberdade ao mesmo tempo em que massacrava civilizações inteiras pelo mundo; superar o colonialismo exige criar novos caminhos civilizatórios, fundados em saberes ancestrais, soberania popular e na dignidade emancipada de todos os povos.",
        "Determinando que os manuais didáticos de ciências exatas devam ser eliminados de todas as escolas públicas.",
        "Comprovando que os tratados diplomáticos internacionais deveriam ser escritos unicamente em pergaminhos de couro.",
        "Afirmando que a ciência moderna foi inventada por navegadores solitários em travessias oceânicas sem bússola.",
        "B",
        "- **Etapa 1:** Desmascarar o humanismo abstrato da Europa: Fanon aponta a contradição insolúvel: a Europa fala de direitos humanos em Paris e pratica torturas e estupros na Argélia e no Congo.\n- **Etapa 2:** Compreender a desobediência descolonial: a verdadeira libertação não é se tornar uma 'cópia de segunda mão' da França ou da Inglaterra; os povos descolonizados precisam pensar com a própria cabeça e refundar o humanismo em bases comunitárias e fraternas."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Analise a relação entre a 'Epidermalização da Inferioridade' e a alienação estética no Brasil contemporâneo: de que modo o alisamento químico de cabelos, a busca por procedimentos de clareamento e a ausência histórica de representatividade negra nos meios de comunicação corporativos confirmam as análises de Fanon?",
        "Provando que as tendências de moda capilar são geradas unicamente por variações sazonais de umidade do ar.",
        "Demonstrando como a ideologia do branqueamento e o mito da democracia racial brasileira operam a introjeção psíquica de que os traços fenotípicos negros são indesejáveis ou feios, impelindo os sujeitos a mascararem seus corpos e identidades para atender ao padrão eurocêntrico dominante, reproduzindo a neurose da máscara branca analisada por Fanon.",
        "Determinando que os produtos cosméticos sejam formulados exclusivamente com extratos minerais marinhos.",
        "Afirmando que as emissoras de televisão comerciais foram criadas por congregações religiosas beneditinas.",
        "Comprovando que as campanhas publicitárias do século XX eram fiscalizadas por comitês de tecelões industriais.",
        "B",
        "- **Etapa 1:** Identificar o mecanismo psíquico das 'máscaras brancas': a sociedade racista emite o sinal contínuo de que a beleza e a civilidade são privilégios brancos, ensinando o negro a odiar seu reflexo.\n- **Etapa 2:** Diagnosticar os reflexos corporais no Brasil: o alisamento forçado e o embranquecimento estético foram estratégias dolorosas de aceitação social; o movimento contemporâneo de valorização da estética afro desfaz essa neurose, recuperando o orgulho fanoniano."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Examine o conceito de 'Maniqueísmo Colonial' em articulação com a criminalização das religiões de matriz africana (Candomblé e Umbanda) no Brasil: como o discurso colonialista que associava a cultura negra à feitiçaria e ao diabo continua operando na violência contemporânea contra terreiros?",
        "Comprovando que os terreiros religiosos foram construídos com materiais cerâmicos de baixa resistência física.",
        "Evidenciando que a partição maniqueísta construída pelo colonizador classificava a fé europeia branca como sagrada e racional, rebaixando as práticas espirituais africanas à condição de demoníacas e primitivas; esse estigma secular é mobilizado hoje por fundamentalismos religiosos e grupos armados que atacam e incendeiam terreiros, reproduzindo o ódio colonial.",
        "Determinando que os sacerdotes religiosos devam registrar suas liturgias em cartórios judiciais civis.",
        "Afirmando que os conflitos teológicos surgiram da escassez de velas artesanais em feiras metropolitanas.",
        "Provando que os rituais ancestrais dependiam de autorização prévia concedida por magistrados de cortes navais.",
        "B",
        "- **Etapa 1:** Descrever o maniqueísmo religioso colonial: para justificar a escravização e a destruição das culturas africanas, a Igreja e o Estado colonizador rotularam os Orixás e as divindades ancestrais como demônios e feitiçaria.\n- **Etapa 2:** Reconhecer a permanência da violência racista hoje: a perseguição e depredação de terreiros no Brasil atual não é disputa teológica isolada, mas a reativação viva do racismo religioso fanoniano, que busca erradicar a memória e a dignidade negra."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Analise a crítica de Frantz Fanon ao 'Nacionalismo Burguês Chauvinista': por que, após a independência formal, o nacionalismo que não se aprofunda em uma consciência social e política internacionalista degenera facilmente em racismo interétnico, xenofobia e perseguição a minorias vizinhas?",
        "Mostrando que as emissoras de rádio estatais transmitiam músicas gravadas em discos de cera frágeis.",
        "Evidenciando que, quando a independência formal não melhora a vida material do povo e a miséria persiste, a burguesia nacional manipuladora desvia a frustração das massas elegendo bodes expiatórios: incita o ódio contra trabalhadores migrantes vizinhos e minorias étnicas locais, substituindo a luta de libertação por um ultranacionalismo tribal reacionário e sangrento.",
        "Determinando que as fronteiras nacionais deveriam ser delimitadas por cercas de bambu entrelaçado.",
        "Afirmando que as desavenças geopolíticas africanas decorriam da ausência de linhas telefônicas transcontinentais.",
        "Comprovando que os tratados de comércio de carnes dependiam de aprovação por tribunais arbitrais marítimos.",
        "B",
        "- **Etapa 1:** Identificar o esgotamento da euforia da independência: passada a festa da bandeira nova, o povo percebe que o estômago continua vazio e os hospitais continuam sem remédios.\n- **Etapa 2:** Revelar a manobra divisionista das oligarquias: para escapar da fúria popular, os governantes culpam os estrangeiros do país ao lado ou uma etnia minoritária; o nacionalismo vazio vira xenofobia fratricida, exatamente como Fanon anteviu em sua crítica premonitória."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Investigue a tese de Frantz Fanon sobre a 'Cultura Nacional' em Os Condenados da Terra: de que maneira o filósofo desmistifica a ideia de que a cultura de um povo liberto se reduz a costumes folclóricos imutáveis, definindo-a como a própria práxis viva de luta pela emancipação?",
        "Comprovando que as danças festivas tradicionais deveriam ser ensinadas exclusivamente por acadêmicos da corte.",
        "Demonstrando que a cultura nacional autêntica não é um relicário congelado no passado nem peças de museu folclóricas para turistas europeus admirarem; ela é o conjunto vivo dos esforços de um povo para afirmar sua soberania, recriando artes, canções, literatura e pensamento no próprio calor do combate diário por sua liberdade e sobrevivência digna.",
        "Determinando que as festas populares municipais fossem financiadas unicamente por companhias mercantis de sal.",
        "Afirmando que os instrumentos musicais de sopro eram fabricados com chifres de animais silvestres extintos.",
        "Provando que as lendas orais eram transcritas por conselhos de escrivães de alfândegas portuárias.",
        "B",
        "- **Etapa 1:** Afastar a visão reificada e folclorizada da cultura: o colonizador adora transformar a cultura negra em dança exótica e batuque inofensivo para consumo de entretenimento burguês.\n- **Etapa 2:** Resgatar a definição revolucionária de Fanon: cultura é ação histórica; a canção, o teatro e a literatura colonial só ganham vida verdadeira quando cantam e organizam a resistência do povo contra a opressão."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Analise a influência das reflexões fenomenológicas de Maurice Merleau-Ponty sobre a corporalidade na obra Pele Negra, Máscaras Brancas: como Fanon adapta a ideia de 'Esquema Corporal' para forjar o conceito de 'Esquema Histórico-Racial'?",
        "Sustentando que os movimentos dos membros superiores dependem do equilíbrio hídrico em climas secos.",
        "Demonstrando que, ao passo que Merleau-Ponty descrevia o corpo como uma experiência fenomenológica espacial de abertura ao mundo, no sujeito negro esse esquema corporal é quebrado e sobreposto por um 'esquema histórico-racial' construído pelo branco, onde o negro é compelido a se perceber através de lendas racistas, medos e narrativas desumanizadoras pré-fabricadas pelo colonizador.",
        "Determinando que os reflexos musculares humanos eram medidos por cronômetros mecânicos em hospitais.",
        "Afirmando que os exames neurológicos eram conduzidos unicamente por astrônomos de cortes imperiais.",
        "Comprovando que as sensações táteis dos trabalhadores rurais eram reduzidas pelo calor das lavouras.",
        "B",
        "- **Etapa 1:** Relembrar o esquema corporal de Merleau-Ponty: o ser humano comum navega no espaço de forma fluida, com o corpo sendo a âncora natural e imediata de sua percepção do mundo.\n- **Etapa 2:** Revelar a fratura do corpo negro em Fanon: o racismo destrói essa harmonia; o negro entra numa sala e não é apenas um corpo no espaço, mas um corpo cercado por séculos de estigmas e preconceitos brancos, sentindo o peso esmagador do olhar do outro."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "Examine a relação entre as reflexões de Frantz Fanon e o pensamento de Achille Mbembe em Crítica da Razão Negra: de que modo Mbembe retoma a análise fanoniana da desumanização do homem negro para denunciar a 'Universalização da Condição Negra' no capitalismo neoliberal global?",
        "Comprovando que as rotas de comércio marítimo de café foram desativadas por acordos alfandegários mundiais.",
        "Evidenciando que a condição que no colonialismo clássico era reservada quase exclusivamente ao homem negro (corpo sem direitos, vida descartável, força de trabalho precarizada e exposta à morte violenta) generaliza-se hoje para parcelas gigantescas da humanidade empobrecida pelo neoliberalismo, transformando multidões de trabalhadores de todas as cores em vidas nuas descartáveis.",
        "Determinando que os bancos centrais devam emitir moedas unicamente com efígies de filósofos gregos.",
        "Afirmando que as teorias de Mbembe foram copiadas de códigos militares de infantaria da Guerra da Crimeia.",
        "Provando que as perseguições trabalhistas decorriam de disputas corporativas de carpinteiros navais.",
        "B",
        "- **Etapa 1:** Resgatar a base fanoniana da desumanização: o negro foi a primeira mercadoria humana viva do capitalismo, explorado até o bagaço nos canaviais e minas coloniais sem qualquer direito cidadão.\n- **Etapa 2:** Analisar a tese contemporânea de Mbembe: com a precarização neoliberal, a uberização e a destruição de direitos sociais, o sistema trata hoje milhões de seres humanos como tratava o escravo de ontem: corpos descartáveis substituíveis a qualquer instante."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "Ao investigar os perigos da alienação religiosa nas colônias, de que maneira Fanon explica o recurso obsessivo a rituais de transe, possessão e mitos mágicos entre populações profundamente subjugadas?",
        "Mostrando que os sacerdotes locais eram remunerados por companhias mercantis de navegação transatlântica.",
        "Demonstrando que, diante da impossibilidade de combater abertamente as metralhadoras e a polícia do colonizador, o colonizado descarrega a angústia titânica e a energia muscular acumulada em transes espirituais catárticos, lutando contra espíritos invisíveis e zumbis para não enfrentar a terrível realidade material do opressor de carne e osso.",
        "Determinando que as cerimônias espirituais deviam ocorrer exclusivamente em noites de lua cheia de verão.",
        "Afirmando que as práticas mágicas foram ensinadas por navegadores espanhóis em expedições marítimas.",
        "Comprovando que as oferendas rituais consistiam unicamente em ferramentas metálicas agrícolas desgastadas.",
        "B",
        "- **Etapa 1:** Descrever o sofrimento psíquico da impotência diante da força militar: o colono tem fuzis e canhões; o colonizado vive acuado e aterrorizado pela violência diária do Estado colonial.\n- **Etapa 2:** Compreender o transe mágico como fuga compensatória: o colonizado canaliza a fúria em brigas contra fantasmas e demônios sobrenaturais; ao ingressar na luta política real, os mitos desvanecem e o colonizado enfrenta o carrasco humano real."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Analise a crítica de Frantz Fanon ao 'Pacifismo Abstrato' das elites liberais ocidentais: por que, segundo o autor, os apelos ocidentais à não-violência dirigidos aos povos do Terceiro Mundo constituem uma hipocrisia descarada?",
        "Comprovando que os tratados de desarmamento naval eram redigidos por comissões de mercadores têxteis.",
        "Evidenciando que a Europa usou a violência mais brutal e desenfreada durante séculos para invadir, pilhar, escravizar e reprimir as colônias; exigir que os oprimidos sejam pacíficos e cordiais diante do genocídio que sofrem equivale a exigir que aceitem a escravidão eterna de cabeça baixa, desarmando moralmente a legítima resistência dos povos.",
        "Determinando que as bandeiras de paz internacional fossem tecidas com fios de algodão cru colhidos no outono.",
        "Afirmando que os congressos pacifistas eram financiados exclusivamente por ordens monásticas contemplativas.",
        "Provando que as leis de neutralidade bélica dependiam de aval de magistrados de comarcas alpinas isoladas.",
        "B",
        "- **Etapa 1:** Recordar o histórico sanguinário da Europa imperialista: canhoneiras, massacres de aldeias, decapitações e pilhagens foram os métodos com que o Ocidente dominou os continentes.\n- **Etapa 2:** Desnudar o duplo padrão ético liberal: quem usou fuzis para roubar terras não tem autoridade moral para pregar não-violência para o espoliado; o pacifismo pregado pelo senhor só serve para manter o escravo de joelhos."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Examine o papel político das mulheres argelinas na Guerra de Libertação Nacional narrado por Fanon na obra Sociologia de uma Revolução (Ano V da Revolução Argelina): de que maneira a participação feminina na guerrilha revolucionou as relações tradicionais de gênero no interior da sociedade colonizada?",
        "Provando que as mulheres argelinas atuavam unicamente na preparação de alimentos para os soldados em casernas.",
        "Demonstrando que as mulheres quebraram a clausura do lar tradicional e ingressaram na linha de frente como mensageiras, estrategistas, combatentes e operadoras da clandestinidade armada urbana (transportando explosivos sob o véu ou vestidas à moda ocidental), desestabilizando tanto o patriarcado tradicional quanto a vigilância colonial francesa.",
        "Determinando que os pelotões femininos deviam realizar juramentos cívicos em capelas católicas metropolitanas.",
        "Afirmando que a adesão das mulheres decorreu de decretos de alistamento compulsório baixados pelo parlamento.",
        "Comprovando que as combatentes eram remuneradas em moedas de prata emitidas por bancos mercantis britânicos.",
        "B",
        "- **Etapa 1:** Descrever o duplo jugo da mulher colonizada: ela estava subjugada pela opressão militar francesa e enclausurada pelas normas patriarcais tradicionais no ambiente familiar.\n- **Etapa 2:** Analisar a revolução de costumes na guerra: a necessidade da luta de libertação colocou as mulheres no comando das ações operacionais mais perigosas da FLN; ao lado dos homens na guerrilha, elas conquistaram autonomia, voz política e respeito histórico."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Analise a advertência de Frantz Fanon sobre o 'Complexo de Édipo Revertido' e o fetiche de assimilação nas relações afetivas inter-raciais em colônias: em Pele Negra, Máscaras Brancas, por que a busca compulsiva pelo casamento com pessoas brancas pode expressar uma forma trágica de alienação racial?",
        "Comprovando que as certidões de matrimônio civil eram emitidas com selos fiscais de altos valores monetários.",
        "Evidenciando que, sob a tirania do racismo estrutural que desvaloriza a humanidade negra, alguns sujeitos colonizados acreditam que unir-se afetivamente a uma pessoa branca lhes conferirá branquitude simbólica, redenção social e fuga do desprezo coletivo, utilizando o parceiro como passaporte para ser aceito na Zona do Ser dominante.",
        "Determinando que as cerimônias de bodas rurais deveriam contar com apresentações de corais de monges beneditinos.",
        "Afirmando que os dotes nupciais eram calculados com base na cotação internacional de grãos de cevada.",
        "Provando que as uniões conjugais eram decididas por sorteios anuais realizados em feiras municipais.",
        "B",
        "- **Etapa 1:** Investigar a psicologia da alienação amorosa colonial: o racismo penetra na intimidade, nos desejos inconscientes e na escolha de parceiros amorosos.\n- **Etapa 2:** Desvelar a ilusão de embranquecimento afetivo: Fanon demonstra que buscar casar-se com uma pessoa branca apenas para 'clarear a linhagem' ou ser aceito pela sociedade racista é o ápice da máscara branca; a cura reside em valorizar a própria negritude e destruir o padrão eurocêntrico."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "Como a tese de Frantz Fanon de que 'A Europa é literalmente a criação do Terceiro Mundo' fundamenta as reivindicações contemporâneas de Reparações Históricas pelos séculos de escravidão e pilhagem colonial?",
        "Mostrando que os barcos pesqueiros europeus utilizavam bússolas marítimas desenhadas por artífices asiáticos.",
        "Evidenciando que a opulência material, as indústrias, os palácios, as universidades e os capitais acumulados da Europa ocidental foram construídos com o sangue de milhões de escravizados africanos e o roubo das riquezas minerais e agrícolas do Sul Global; as reparações não são caridade benevolente, mas pagamento de uma dívida histórica concreta.",
        "Determinando que as obras de arte clássicas dos museus europeus deveriam ser leiloadas em praças mercantis.",
        "Afirmando que os orçamentos educacionais das metrópoles eram financiados unicamente por taxas de correios.",
        "Comprovando que as rotas fluviais de carvão mineral foram desativadas por acordos de trégua diplomática.",
        "B",
        "- **Etapa 1:** Desmascarar o mito da riqueza europeia autossuficiente: a narrativa liberal afirma que a Europa enriqueceu unicamente por sua genialidade científica e virtudes do trabalho protestante.\n- **Etapa 2:** Expor o sangue da acumulação primitiva: Fanon desnuda a verdade: a riqueza da Europa é o outro lado da moeda da miséria africana; todo tijolo de ouro dos bancos europeus foi arrancado da mina e da senzala; as reparações históricas são exigência elementar de justiça ética e econômica."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Analise a crítica de Frantz Fanon à 'Espontaneidade Revolucionária' em Os Condenados da Terra: por que o filósofo adverte que o ódio cego e a fúria visceral das massas camponesas contra o opressor, se não forem educados por uma sólida formação política emancipatória, podem se esgotar ou ser manipulados por caudilhos reacionários?",
        "Comprovando que os camponeses revoltados recusavam utilizar sapatos de couro em suas marchas rurais.",
        "Demonstrando que o ressentimento explosivo e a cólera espontânea são necessários como estopim de revolta, mas insuficientes para sustentar a revolução a longo prazo; sem uma pedagogia política lúcida que ensine o povo a distinguir o colono inimigo de classe daquele que pode ser aliado e sem um projeto nacional de reorganização econômica, o movimento corre o risco de cair no fanatismo destrutivo ou na anarquia estéril.",
        "Determinando que os líderes revolucionários deviam receber pensões vitalícias em barras de cobre fundido.",
        "Afirmando que as reuniões de comitês populares deviam ocorrer unicamente em cavernas montanhosas profundas.",
        "Provando que as estratégias militares eram formuladas por adivinhos e astrólogos de feiras provinciais.",
        "B",
        "- **Etapa 1:** Reconhecer o papel indispensável da fúria popular inicial: a raiva do explorado é o combustível vital que desafia a cavalaria e os fuzis coloniais com bravura incomparável.\n- **Etapa 2:** Enfatizar a necessidade da educação e consciência política: Fanon não é apologista cego do caos; ele exige que os combatentes compreendam o sistema, organizem hospitais de campanha, escolas e planos agrícolas; sem clareza teórica, a rebelião queima depressa e o povo volta à servidão sob novos mestres."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Examine a atualidade e a fecundidade do pensamento de Frantz Fanon para a formulação de uma Pedagogia Antirracista emancipatória no Brasil: de que maneira as categorias de 'Pele Negra, Máscaras Brancas' e 'Os Condenados da Terra' instrumentalizam educadores e estudantes na superação do racismo estrutural?",
        "Provando que os currículos escolares modernos devem priorizar exclusivamente o estudo de guerras imperiais antigas.",
        "Demonstrando que Fanon fornece ferramentas críticas para desmascarar a falsa neutralidade dos currículos eurocêntricos, desconstruir a naturalização da desigualdade socioespacial brasileira, conscientizar estudantes sobre os impactos psíquicos da discriminação racial e inspirá-los a protagonizarem a construção de uma sociedade democrática, justa e fraterna onde todos os seres humanos tenham reconhecida sua plena e inviolável dignidade humana e social.",
        "Determinando que os estabelecimentos de ensino devam suspender as aulas durante os períodos de solstício de verão.",
        "Afirmando que os manuais didáticos de filosofia devem conter unicamente biografias de monarcas absolutistas.",
        "Comprovando que as avaliações pedagógicas devem consistir unicamente em testes de memorização de datas cívicas.",
        "B",
        "- **Etapa 1:** Reconhecer o impacto de Fanon na prática docente: ele ensina a enxergar como o preconceito molda a autoestima da criança negra e como a arquitetura das cidades perpetua a exclusão colonial.\n- **Etapa 2:** Consolidar a emancipação cidadã: aplicar Fanon na escola brasileira cumpre a Lei 10.639/03, arranca as máscaras da desigualdade e forma jovens conscientes, altivos e comprometidos em refundar a humanidade na terra do Homem Novo."
    ))

    return questoes_brutas

def balancear_e_gerar_markdown(questoes_brutas):
    padrao = ['A', 'B', 'C', 'D', 'E']
    questoes_balanceadas = []

    for i, q in enumerate(questoes_brutas):
        num, hab, dif, enunciado, opt_a, opt_b, opt_c, opt_d, opt_e, gab_orig, resolucao = q
        gabarito_desejado = padrao[i % 5]

        correta_texto = opt_b
        distratores = [opt_a, opt_c, opt_d, opt_e]

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
    linhas.append('eixo: "Eixo III: Filosofia Política, Poder, Resistência e Necropolítica"')
    linhas.append('capitulo: "Capítulo 22: Frantz Fanon e a Filosofia da Descolonização"')
    linhas.append('objeto_de_conhecimento: "A fenomenologia do colonialismo, a epidermalização da inferioridade em Pele Negra, Máscaras Brancas, a violência descolonizadora em Os Condenados da Terra, a crítica à burguesia nacional e a criação do Homem Novo"')
    linhas.append('ebook_fonte: "em-fil-c22-frantz-fanon-filosofia-descolonizacao.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('  - "EM13CHS606"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")
    linhas.append("# Lista de Exercícios: Frantz Fanon e a Filosofia da Descolonização\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-22-frantz-fanon-filosofia-descolonizacao -->"
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
    linhas.append("- FANON, Frantz. *Os condenados da terra*. Tradução de Enid Abreu Dobránszky. Juiz de Fora: Editora UFJF, 2005.")
    linhas.append("- FANON, Frantz. *Pele negra, máscaras brancas*. Tradução de Renato da Silveira. Salvador: EDUFBA, 2008.")
    linhas.append("- CÉSAIRE, Aimé. *Discurso sobre o colonialismo*. Tradução de Noémia de Sousa. Lisboa: Livraria Sá da Costa Editora, 1978.")
    linhas.append("- MBEMBE, Achille. *Crítica da razão negra*. Tradução de Marta Lança. São Paulo: n-1 edições, 2018.")
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
    print(f"Rascunho salvo em {temp_draft} ({tamanho} bytes)")

    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-22-frantz-fanon-filosofia-descolonizacao/ebooks/em-fil-c22-frantz-fanon-filosofia-descolonizacao-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 22 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
