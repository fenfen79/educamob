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

def gerar_cap03():
    dest_path = "content/medio/volume-unico/filosofia/eixo-1-epistemologia/cap-03-virada-antropologica-socrates-sofistas/ebooks/em-fil-c03-virada-antropologica-socrates-sofistas-exercicios.md"
    temp_draft = "temp_draft.md"

    questoes_brutas = []

    # ----------------------------------------------------
    # NÍVEL BÁSICO (Questões 1 a 20)
    # ----------------------------------------------------
    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "A Virada Antropológica na filosofia grega do século V a.C. consistiu em qual deslocamento temático central?",
        "Do estudo da física cósmica da natureza para a reflexão sobre o ser humano, a ética e a política na cidade.",
        "Da investigação da matemática pura para a prática de sacrifícios religiosos fúnebres.",
        "Do comércio marítimo no Mediterrâneo para a agricultura familiar isolada no campo.",
        "Das leis escritas da democracia para o retorno a regimes de tirania militar absoluta.",
        "Da astronomia jônica para a cartografia de minas subterrâneas de ouro.",
        "A",
        "A virada antropológica transferiu o foco da natureza (physis) para o ser humano, a justiça e a vida cívica."
    ))

    questoes_brutas.append((
        2, "EM13CHS603", "basico",
        "Na democracia ateniense da Época de Ouro, qual era a principal habilidade ensinada pelos sofistas aos jovens da elite?",
        "A observação empírica de eclipses e astros celestes.",
        "A arte da retórica e da oratória para persuadir cidadãos na assembleia e nos tribunais.",
        "A composição de cantos líricos em louvor aos atletas dos jogos olímpicos.",
        "A fabricação artesanal de ânforas de cerâmica para exportação de azeite.",
        "A engenharia de pontes militares para campanhas no território persa.",
        "B",
        "Os sofistas ensinavam a eloquência e a argumentação persuasiva para garantir o sucesso político na pólis."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Qual princípio filosófico é sintetizado pela famosa máxima de Protágoras: 'O homem é a medida de todas as coisas'?",
        "O dogmatismo religioso absoluto.",
        "O relativismo moral e do conhecimento.",
        "O determinismo biológico dos temperamentos.",
        "O materialismo atomista mecanicista.",
        "A defesa do governo de reis divinos.",
        "B",
        "A tese de Protágoras consagra o relativismo: a verdade depende do sujeito e das circunstâncias de cada cultura."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "Górgias de Leontinos defendia que a palavra falada exercia sobre o espírito humano um poder comparável a:",
        "Um cálculo numérico exato que encerra qualquer dúvida.",
        "Um feitiço ou fármaco capaz de produzir alegria, afastar a dor e seduzir a alma.",
        "Uma pedra pesada que impede qualquer tipo de movimento corporal.",
        "Uma sentença divina imutável gravada no céu estrelado.",
        "Uma regra contábil restrita ao pagamento de mercadorias no porto.",
        "B",
        "Em seu Elogio de Helena, Górgias descreve a palavra como uma força soberana que encanta e manipula os afetos humanos."
    ))

    questoes_brutas.append((
        5, "EM13CHS103", "basico",
        "Diferentemente dos sofistas, Sócrates praticava a filosofia em Atenas adotando qual postura profissional?",
        "Cobrando valores elevados por consultas filosóficas privadas.",
        "Sem cobrar honorários, dialogando gratuitamente nas praças e oficinas da cidade.",
        "Abrindo academias fechadas exclusivas para filhos de generais condecorados.",
        "Escrevendo tratados enciclopédicos vendidos nas livrarias de cidades vizinhas.",
        "Exigindo que seus discípulos realizassem juramentos de segredo militar.",
        "B",
        "Sócrates não cobrava por seus ensinamentos, não escreveu livros e dialogava abertamente com qualquer cidadão."
    ))

    questoes_brutas.append((
        6, "EM13CHS103", "basico",
        "Ao consultar o Oráculo de Delfos, Querofonte recebeu da sacerdotisa Pítia qual resposta sobre Sócrates?",
        "Que Sócrates deveria assumir o comando dos exércitos de infantaria de Atenas.",
        "Que nenhum homem vivo era mais sábio do que Sócrates.",
        "Que Sócrates seria condenado ao desterro nas ilhas distantes do mar Egeu.",
        "Que as ideias socráticas deviam ser transformadas em poemas rimados.",
        "Que Atenas sofreria uma derrota naval caso Sócrates continuasse a filosofar.",
        "B",
        "A resposta do oráculo de que ninguém era mais sábio que Sócrates desencadeou a busca socrática pelo sentido do saber."
    ))

    questoes_brutas.append((
        7, "EM13CHS103", "basico",
        "A célebre declaração atribuída a Sócrates 'Só sei que nada sei' expressa qual atitude perante a sabedoria?",
        "O desprezo definitivo pela ciência e o abandono de qualquer estudo moral.",
        "A consciência lúcida dos próprios limites intelectuais como ponto de partida para o aprendizado.",
        "A certeza de que a mentira é o único meio eficaz para obter vantagens eleitorais.",
        "A afirmação de que os homens são incapazes de formular pensamentos claros.",
        "A tentativa de enganar os juízes para evitar condenações em processos civis.",
        "B",
        "Reconhecer a própria ignorância é o primeiro passo para se libertar de preconceitos e buscar o saber autêntico."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "O método dialógico de Sócrates é composto por dois momentos fundamentais e complementares, conhecidos como:",
        "A Retórica e a Poética teatral.",
        "A Dedução silogística e a Indução matemática.",
        "A Ironia (refutação) e a Maiêutica (parto das ideias).",
        "A Astronomia observacional e a Geometria sagrada.",
        "O Discurso fúnebre e o Julgamento penal.",
        "C",
        "O método socrático inicia-se pela desconstrução irônica das certezas falsas e culmina no parto das ideias pela maiêutica."
    ))

    questoes_brutas.append((
        9, "EM13CHS101", "basico",
        "No primeiro momento do diálogo socrático, a Ironia tinha como função pedagógica principal:",
        "Ridicularizar o debatedor perante a multidão com ofensas pessoais.",
        "Conduzir o interlocutor a admitir a insuficiência e as contradições de suas certezas iniciais.",
        "Ensinar fórmulas gramaticais para impressionar os jurados do tribunal popular.",
        "Distrair os ouvintes com anedotas para desviar a atenção do tema central.",
        "Impor uma resposta pronta decorada dos manuais de conduta de Esparta.",
        "B",
        "A ironia finge ignorância para fazer o interlocutor perceber as contradições de suas opiniões e atingir a aporia."
    ))

    questoes_brutas.append((
        10, "EM13CHS101", "basico",
        "Ao buscar saber o que é a coragem ou a justiça, Sócrates recusava meros exemplos particulares porque exigia:",
        "O relato detalhado de uma batalha heroica vencida por marinheiros.",
        "A definição universal da essência comum que caracteriza aquela virtude.",
        "Uma lista de leis civis redigidas por reis de dinastias antigas.",
        "O testemunho de adivinhos que interpretavam o voo de pássaros migratórios.",
        "Um poema dramático encenado no teatro da cidade durante festividades.",
        "B",
        "Sócrates não buscava casos particulares de atos corajosos, mas o conceito universal que define a essência da coragem."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "O estado de perplexidade e paralisia reflexiva gerado pela refutação socrática recebia o nome grego de:",
        "Logos.",
        "Physis.",
        "Aporia.",
        "Daimonion.",
        "Pólemos.",
        "C",
        "Aporia é o impasse cognitivo no qual o sujeito percebe que não sabe aquilo que julgava saber com certeza."
    ))

    questoes_brutas.append((
        12, "EM13CHS103", "basico",
        "A Maiêutica socrática foi inspirada no ofício materno de Fenareta, que trabalhava em Atenas como:",
        "Costureira de túnicas cerimoniais.",
        "Escultora de mármore para monumentos.",
        "Parteira responsável por auxiliar no nascimento de bebês.",
        "Vendedora de cereais no porto de Pireu.",
        "Sacerdotisa do templo da deusa Atena.",
        "C",
        "Sócrates afirmava ser um 'parteiro de almas', ajudando os discípulos a darem à luz os conceitos de sua própria razão."
    ))

    questoes_brutas.append((
        13, "EM13CHS103", "basico",
        "No ano de 399 a.C., Sócrates foi formalmente acusado e levado a julgamento em Atenas sob quais imputações centrais?",
        "Suborno de magistrados públicos e deserção em combate naval.",
        "Não crer nos deuses da cidade, introduzir novas divindades e corromper a juventude.",
        "Roubo de verbas destinadas à reforma das muralhas de proteção costeira.",
        "Cobrança ilegal de juros em empréstimos concedidos a navegadores estrangeiros.",
        "Traição militar por fornecer informações estratégicas a governantes persas.",
        "B",
        "A queixa apresentada por Meleto, Ânito e Lícon acusava Sócrates de impiedade religiosa e de desviar os jovens da tradição."
    ))

    questoes_brutas.append((
        14, "EM13CHS103", "basico",
        "Em sua autodefesa registrada na Apologia de Sócrates, o filósofo comparou sua atuação na cidade de Atenas à figura de um:",
        "General valente que conquista novas colônias para o comércio.",
        "Tavão (moscardo) que aguilhoa um cavalo nobre e vigoroso, mas indolente.",
        "Navegador prudente que desvia de recifes de coral em noites escuras.",
        "Médico que receita xaropes doces para acalmar as queixas do povo.",
        "Arquiteto encarregado de desenhar colunatas de mármore na ágora.",
        "B",
        "Sócrates via-se como um moscardo colocado pelos deuses para despertar Atenas de sua sonolência moral e comodismo."
    ))

    questoes_brutas.append((
        15, "EM13CHS103", "basico",
        "Conforme relatado no diálogo Críton de Platão, por qual razão Sócrates recusou a proposta de fugir da prisão antes de sua execução?",
        "Porque acreditava que os soldados o matariam a flechadas logo na saída dos portões.",
        "Porque violar as leis e sentenças da pólis destruiria a base da convivência cívica que ele respeitou a vida inteira.",
        "Porque não confiava na lealdade dos amigos que organizaram o plano de resgate.",
        "Porque pretendia liderar uma revolta popular armada dentro dos muros da prisão.",
        "Porque esperava receber uma anistia formal assinada pelo rei de Esparta.",
        "B",
        "Sócrates sustentou que a desobediência individual à decisão judicial minaria o respeito às leis da cidade que o acolheu por 70 anos."
    ))

    questoes_brutas.append((
        16, "EM13CHS103", "basico",
        "Qual substância tóxica foi ingerida por Sócrates para cumprir a sentença de pena de morte determinada pelo tribunal ateniense?",
        "Arsênico líquido.",
        "Veneno de escorpião do deserto.",
        "Extrato de cicuta.",
        "Chumbo derretido.",
        "Óleo de rícino concentrado.",
        "C",
        "A execução de penas capitais em Atenas para cidadãos livres era habitualmente realizada pela ingestão de veneno de cicuta."
    ))

    questoes_brutas.append((
        17, "EM13CHS603", "basico",
        "O comediógrafo Aristófanes satirizou Sócrates na peça cômica As Nuvens (423 a.C.), retratando-o injustamente como:",
        "Um general severo que impunha castigos físicos aos jovens recrutas.",
        "Um sofista charlatão que ensinava a vencer causas injustas e vivia pendurado em um cesto.",
        "Um sacerdote devoto que passava os dias fazendo oferendas aos deuses.",
        "Um marinheiro beberrão que contava lorotas sobre monstros marinhos.",
        "Um rei autoritário que pretendia fechar a assembleia popular da cidade.",
        "B",
        "Aristófanes ajudou a criar o estereótipo popular errôneo de que Sócrates era um sofista ganancioso e zombeteiro."
    ))

    questoes_brutas.append((
        18, "EM13CHS101", "basico",
        "As três teses céticas de Górgias sobre o Não-Ser estabeleciam sucessivamente que:",
        "Nada existe; se existisse, não poderia ser conhecido; se conhecido, não poderia ser comunicado.",
        "Tudo se move; o movimento é divino; a linguagem é a morada sagrada da verdade eterna.",
        "O Ser é água; a água evapora no calor; o calor é produzido pela fricção de pedras.",
        "As leis são justas; a justiça é eterna; os magistrados devem governar com mãos de ferro.",
        "O número governa o mundo; a música expressa os números; as notas agudas curam a alma.",
        "A",
        "Górgias levou o ceticismo ao extremo: nada existe, o intelecto não capta o real e a linguagem não transmite o saber."
    ))

    questoes_brutas.append((
        19, "EM13CHS103", "basico",
        "A voz interior que Sócrates afirmava ouvir desde a infância, alertando-o para não cometer atos injustos, era denominada por ele de:",
        "Logos.",
        "Physis.",
        "Daimonion.",
        "Nous.",
        "Ápeiron.",
        "C",
        "O Daimonion era a presença espiritual interior que desaconselhava Sócrates a agir de forma contrária à virtude e à verdade."
    ))

    questoes_brutas.append((
        20, "EM13CHS103", "basico",
        "As últimas palavras de Sócrates dirigidas ao seu amigo Críton ('Devemos um galo a Asclépio') faziam alusão a qual divindade?",
        "Ao deus da guerra e das disputas sangrentas.",
        "Ao deus da cura e da medicina, agradecendo pela libertação da alma.",
        "Ao deus dos mares e dos terremotos destrutivos.",
        "Ao deus do comércio e dos navegadores mercantes.",
        "Ao deus do vinho e das festividades de embriaguez.",
        "B",
        "Asclépio era o deus da medicina; Sócrates agradece simbolicamente pela morte entendida como a cura final das limitações do corpo."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao diferenciar a pedagogia dos sofistas do método socrático, constata-se uma divergência fundamental quanto à natureza do saber, pois:",
        "Os sofistas consideravam a verdade como algo a ser transmitido de fora, enquanto Sócrates guiava a razão a descobri-la por si mesma.",
        "Os sofistas recusavam o uso de argumentos verbais, ensinando apenas exercícios atléticos corporais aos jovens.",
        "Sócrates prometia aos seus alunos o enriquecimento rápido e o domínio dos cargos administrativos municipais.",
        "Os sofistas defendiam leis eternas gravadas na natureza, e Sócrates afirmava que a justiça é uma convenção passageira.",
        "Sócrates exigia a leitura de longos textos escritos, enquanto os sofistas proibiam qualquer registro em pergaminho.",
        "A",
        "Para Sócrates, o saber não se transfere mecanicamente de uma mente para outra; ele deve ser gerado pelo próprio sujeito no diálogo."
    ))

    questoes_brutas.append((
        22, "EM13CHS603", "intermediario",
        "A concepção de justiça desenvolvida pelos sofistas antecipou vertentes da teoria do Direito contemporânea ao sustentar que:",
        "As leis civis decorrem da vontade irrevogável de divindades míticas do Olimpo.",
        "As normas jurídicas (nómos) são acordos históricos e convenções humanas sujeitas a reformas e aperfeiçoamentos.",
        "A pena de talião é a única fórmula justa e aplicável para julgar delitos comerciais.",
        "O cumprimento das leis deve ser dispensado sempre que um cidadão enriquecer no comércio exterior.",
        "O direito de propriedade pertence exclusivamente aos generais encarregados da defesa da cidade.",
        "B",
        "Os sofistas laicizaram a norma jurídica, concebendo a lei como pacto social humano contingente, e não como decreto divino eterno."
    ))

    questoes_brutas.append((
        23, "EM13CHS101", "intermediario",
        "Quando Sócrates dialogava com os cidadãos que tinham fama de sábios em Atenas (políticos, poetas e artesãos), ele constatou que:",
        "Todos eles dominavam perfeitamente a definição conceitual de virtude e justiça.",
        "Os políticos governavam amparados em noções confusas, e os artesãos achavam que sabiam tudo apenas por dominarem um ofício prático.",
        "Os poetas trágicos eram os únicos capazes de explicar racionalmente suas próprias metáforas em audiências públicas.",
        "A juventude ateniense recusava acompanhar seus debates por preferirem assistir a corridas de bigas na praia.",
        "Os generais militares recusavam dialogar por considerarem o estudo moral uma fraqueza de caráter cívico.",
        "B",
        "Sócrates descobriu que a ilusão de sabedoria cegava os poderosos: sabiam detalhes práticos, mas ignoravam a essência da virtude."
    ))

    questoes_brutas.append((
        24, "EM13CHS603", "intermediario",
        "Em campanhas eleitorais modernas, marqueteiros utilizam pesquisas de grupos focais para calibrar discursos com slogans emocionais. Essa prática reflete:",
        "A busca socrática por definições rigorosas e universais sobre os valores éticos republicanos.",
        "A técnica retórica dos sofistas, voltada a produzir adesão emocional imediata e vitória do argumento sobre o eleitorado.",
        "A adoção de princípios matemáticos pitagóricos para determinar o orçamento da educação municipal.",
        "A exigência de que todo candidato renuncie ao debate televisivo para dialogar nas feiras livres.",
        "A tentativa de eliminar a persuasão das propagandas para apresentar apenas relatórios contábeis frios.",
        "B",
        "O marketing político opera no registro da retórica sofística: produzir convencimento (peithó) e vitória eleitoral pela linguagem sedutora."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "A analogia socrática da Maiêutica estabelece que, assim como a parteira não gera o bebê no próprio ventre, o filósofo:",
        "Não injeta o saber na mente alheia, mas ajuda o interlocutor a formular a verdade a partir de sua reflexão interior.",
        "Deve abandonar o ensino após o primeiro erro cometido pelo estudante durante o debate.",
        "Precisa consultar os sacerdotes de templos sagrados antes de iniciar qualquer conversação na ágora.",
        "Exige que o discípulo pague mensalidades proporcionais ao número de dúvidas esclarecidas na aula.",
        "Ensina que os conceitos verdadeiros foram inventados por governantes de Esparta.",
        "A",
        "O parteiro de almas estimula a gestação da verdade na razão do próprio interlocutor, sem impor dogmas pré-fabricados."
    ))

    questoes_brutas.append((
        26, "EM13CHS103", "intermediario",
        "Ao propor ser sustentado no Pritaneu como sua contraposta de pena perante o tribunal ateniense, Sócrates expressava:",
        "Uma atitude de zombaria vulgar motivada pelo desespero financeiro de sua família.",
        "Sua dignidade inegociável e a convicção de que dedicara a vida a despertar os concidadãos para a virtude moral.",
        "A tentativa de subornar os magistrados com promessas de apoio a reformas tributárias futuras.",
        "O medo de enfrentar o veneno da cicuta e o desejo de fugir clandestinamente para Tebas.",
        "A crença de que os generais da cidade deviam pagar pensões vitalícias aos filósofos aposentados.",
        "B",
        "Sócrates considerava seu chamado filosófico o maior benefício prestado a Atenas, recusando admitir que cometeu qualquer crime cívico."
    ))

    questoes_brutas.append((
        27, "EM13CHS101", "intermediario",
        "O método socrático opera uma distinção lógica fundamental entre 'dar exemplos particulares' e 'definir o conceito universal', demonstrando que:",
        "Uma lista de ações corajosas não esclarece o que faz com que todas elas compartilhem a essência da coragem.",
        "Os exemplos concretos são suficientes para encerrar qualquer investigação científica sobre a matéria viva.",
        "A definição conceitual deve mudar a cada estação do ano para acompanhar o clima do Mediterrâneo.",
        "As palavras abstratas devem ser eliminadas da linguagem jurídica em benefício de desenhos simbólicos.",
        "O debate racional dispensa a coerência interna desde que o orador fale com tom de voz imponente.",
        "A",
        "Apresentar exemplos circunstanciais não equivale a definir a essência comum (Katholou) que torna uma virtude aquilo que ela é."
    ))

    questoes_brutas.append((
        28, "EM13CHS603", "intermediario",
        "No campo da educação escolar contemporânea, as metodologias ativas que utilizam problemas para estimular o raciocínio dos alunos conectam-se à maiêutica porque:",
        "Obriga o estudante a memorizar passivamente as conclusões prontas fornecidas pela apostila escolar.",
        "Colocam o professor como mediador que formula questões desafiadoras para que os próprios estudantes construam o saber.",
        "Proíbem o trabalho em grupo e exigem que cada jovem responda a exames orais em isolamento total.",
        "Substituem o estudo de humanidades por aulas práticas de tiro esportivo e marcha cívica.",
        "Eliminam os livros didáticos para ensinar unicamente técnicas de oratória eleitoral aos adolescentes.",
        "B",
        "A aprendizagem ativa retoma o espírito socrático: o docente guia por questionamentos, incentivando o aluno a pensar por si mesmo."
    ))

    questoes_brutas.append((
        29, "EM13CHS101", "intermediario",
        "A acusação de impiedade lançada contra Sócrates baseava-se em parte na menção ao seu Daimonion. Essa entidade era compreendida pelo filósofo como:",
        "Um espírito maligno invocado em rituais noturnos para prejudicar colheitas de trigo da cidade.",
        "Uma advertência interior da consciência moral que o desviava de condutas indignas ou desonestas.",
        "Um código militar secreto transmitido por espiões vindos de nações rivais da Grécia.",
        "Uma divindade estrangeira que ordenava a queima de templos públicos dedicados a Apolo.",
        "Um truque de ventriloquia utilizado para iludir jovens reunidos nos mercados da cidade.",
        "B",
        "O Daimonion socrático não era uma seita herética, mas o testemunho de uma consciência ética atenta aos deveres da retidão."
    ))

    questoes_brutas.append((
        30, "EM13CHS103", "intermediario",
        "No diálogo Críton, as Leis da Cidade personificadas dialogam com Sócrates na prisão, argumentando que a desobediência do filósofo implicaria:",
        "Uma atitude louvável que incentivaria os jovens a desafiar a cobrança de tributos municipais.",
        "A anulação prática da soberania judicial da pólis, destruindo o pacto de convivência cívica que permitiu sua existência.",
        "A comprovação de que as sentenças dos jurados nunca precisavam ser cumpridas por cidadãos instruídos.",
        "A transferência imediata do tribunal de Atenas para colônias agrícolas estabelecidas no sul da Itália.",
        "O aumento do prestígio da cidade perante as cortes de generais do Império Persa.",
        "B",
        "A cidade argumenta que o cidadão desfrutou de suas leis e instituições; desobedecer quando a decisão é contrária destrói a ordem pública."
    ))

    questoes_brutas.append((
        31, "EM13CHS603", "intermediario",
        "Na clínica psicológica e na psicanálise, o terapeuta escuta as contradições do discurso do paciente sem impor conselhos prontos. Essa conduta retoma:",
        "A técnica de oratória sofística que visa convencer o cliente a mudar de religião imediatamente.",
        "A maiêutica socrática, permitindo que o próprio sujeito alcance a autoconsciência de seus conflitos e desejos.",
        "O isolamento pitagórico que impunha cinco anos de silêncio absoluto aos novos iniciados.",
        "A oratória fúnebre que louvava os antepassados para afastar sentimentos de tristeza cotidiana.",
        "O método atomista de colisão mecânica entre partículas sólidas que viajam pelo espaço vazio.",
        "B",
        "A escuta analítica que questiona e aponta incoerências para que o paciente gere sua própria cura espelha o método de Sócrates."
    ))

    questoes_brutas.append((
        32, "EM13CHS101", "intermediario",
        "A célebre distinção grega entre Physis (natureza) e Nómos (lei humana) foi aprofundada pelos sofistas ao defenderem que:",
        "As leis da cidade são fixas e eternas como o curso do sol no céu de verão.",
        "As normas morais e políticas são convenções sociais históricas que podem ser reformadas pelas comunidades humanas.",
        "A natureza física deve obedecer às ordens aprovadas pelos senadores reunidos na assembleia popular.",
        "Os costumes sociais devem ser copiados sem alterações das tradições de tribos nômades da Ásia.",
        "Os contratos comerciais só adquirem validade se forem abençoados por sacerdotes em altares sagrados.",
        "B",
        "A separação entre natureza e convenção social libertou as leis humanas da tutela mítica, tornando a política um campo de deliberação cívica."
    ))

    questoes_brutas.append((
        33, "EM13CHS103", "intermediario",
        "Em seu discurso de julgamento, Sócrates declarou que 'uma vida sem autoexame não vale a pena ser vivida'. Essa afirmação resume o ideal socrático de:",
        "Acúmulo de bens materiais e terrenos agrícolas para garantir tranquilidade aos herdeiros.",
        "Compromisso permanente com a reflexão moral e a coerência ética entre pensamento e ação cotidiana.",
        "Busca ininterrupta de honras militares em guerras de invasão contra cidades costeiras vizinhas.",
        "Treinamento diário de oratória para derrotar qualquer adversário em disputas de tribunal.",
        "Renúncia total à vida comunitária para viver em cavernas isoladas no alto de montanhas rochosas.",
        "B",
        "Para Sócrates, a existência humana só adquire dignidade e valor quando submetida ao questionamento moral e ao cultivo da virtude."
    ))

    questoes_brutas.append((
        34, "EM13CHS603", "intermediario",
        "O filósofo Michel Foucault associou a postura de Sócrates no julgamento ao conceito de Parrhesía, que designa a virtude de:",
        "Falar com disfarces e ambiguidades calculadas para agradar aos poderosos de ocasião.",
        "Ter a coragem cívica de pronunciar toda a verdade diante dos concidadãos, mesmo correndo o risco da própria morte.",
        "Usar recursos cênicos melodramáticos para fazer os jurados chorarem durante a votação da sentença.",
        "Defender causas judiciais por meio da cobrança de propinas pagas por familiares de réus confessos.",
        "Escrever textos anônimos em praça pública para criticar generais militares da cidade.",
        "B",
        "A Parrhesía é a fala franca e destemida de quem coloca a fidelidade à verdade e ao bem comum acima da própria sobrevivência física."
    ))

    questoes_brutas.append((
        35, "EM13CHS101", "intermediario",
        "Ao interrogar o general Laques sobre o que é a coragem, Sócrates refutou a resposta de que 'coragem é não fugir da trincheira' apontando que:",
        "Os generais nunca devem descer às trincheiras durante as batalhas travadas em campos abertos.",
        "A retirada tática pode ser um ato sábio de bravura e existe coragem diante de doenças, dores e mares revoltos.",
        "A coragem pertence exclusivamente aos guerreiros que montam a cavalo com armaduras pesadas de bronze.",
        "Os soldados de Esparta desconheciam o significado da palavra coragem em sua língua oficial.",
        "A fuga de um pelotão de infantaria comprova sempre a covardia moral de todos os seus membros.",
        "B",
        "Sócrates demonstra que o exemplo particular de Laques é restrito: a coragem manifesta-se em múltiplos cenários e exige definição conceitual ampla."
    ))

    questoes_brutas.append((
        36, "EM13CHS103", "intermediario",
        "A condenação de Sócrates por um tribunal popular democrático revelou um risco histórico próprio dos regimes de assembleia, a saber:",
        "A impossibilidade de realizar julgamentos rápidos sem a autorização prévia de generais da marinha.",
        "A vulnerabilidade da multidão a discursos demagógicos que manipulam medos coletivos para perseguir vozes críticas incômodas.",
        "A falta de urnas de madeira lacradas para garantir o segredo dos votos depositados pelos cidadãos.",
        "A proibição do uso de venenos naturais na execução de condenados por crimes de ordem pública.",
        "A obrigatoriedade de que todos os juízes pertencessem a famílias proprietárias de terras agrícolas.",
        "B",
        "O processo socrático expôs o perigo da tirania da maioria quando manipulada por líderes demagogos para silenciar pensadores livres."
    ))

    questoes_brutas.append((
        37, "EM13CHS101", "intermediario",
        "Na linguística moderna de Roman Jakobson, a retórica sofística de Górgias enfatizava qual função da linguagem ao buscar convencer o ouvinte?",
        "A função referencial, centrada exclusivamente na veracidade empírica dos fatos descritos.",
        "A função conativa ou apelativa, voltada a mobilizar emoções e orientar o comportamento do receptor da mensagem.",
        "A função metalinguística, dedicada a explicar as regras gramaticais da língua falada.",
        "A função fática, preocupada apenas em testar se o canal de áudio da praça está funcionando.",
        "A função emotiva pura, restrita a manifestar a dor de dentes sofrida pelo próprio orador.",
        "B",
        "A retórica sofística privilegia a persuasão do interlocutor (função apelativa), subordinando a exatidão factual à conquista da adesão da plateia."
    ))

    questoes_brutas.append((
        38, "EM13CHS103", "intermediario",
        "O comediógrafo Aristófanes e os acusadores formais de Sócrates (Meleto, Ânito e Lícon) representavam setores de Atenas incomodados com:",
        "A recusa do filósofo em pagar os tributos cívicos devidos pela importação de grãos do mar Negro.",
        "O questionamento incômodo que o filósofo fazia das tradições consagradas, desmascarando a falsa sabedoria das elites.",
        "A aliança política formal que Sócrates teria firmado com reis de cidades rivais da Macedônia.",
        "A proposta socrática de fechar o porto de Pireu para impedir o desembarque de tecidos estrangeiros.",
        "O projeto pedagógico de substituir os deuses por estudos de navegação a vela com caravelas.",
        "B",
        "A elite conservadora ressentiu-se da humilhação pública sofrida em debates com Sócrates, que revelavam sua real ignorância moral."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "A refutação socrática (Élenkhos) não deve ser entendida como uma derrota humilhante para o interlocutor, mas como:",
        "Um espetáculo cênico destinado a arrecadar moedas dos jovens que assistiam à conversa na praça.",
        "Uma libertação intelectual indispensável que limpa a mente de ilusões e abre caminho para a verdade cooperativa.",
        "Um procedimento formal preliminar exigido pelos juízes antes de iniciar julgamentos de homicídio.",
        "Um teste de memória voltado a verificar se o cidadão decorou todos os cantos da Ilíada de Homero.",
        "Uma demonstração de força verbal destinada a intimidar marinheiros recém-chegados à cidade.",
        "B",
        "O Élenkhos é uma catarse do intelecto: ao desfazer o falso saber, o indivíduo cura-se da arrogância e torna-se apto a buscar a sabedoria."
    ))

    questoes_brutas.append((
        40, "EM13CHS103", "intermediario",
        "Ao ingerir a taça de cicuta com serenidade e recusar lágrimas entre os amigos, Sócrates consagrou na história ocidental a imagem do filósofo como:",
        "Um guerreiro impulsivo que prefere morrer em duelos armados para ser cantado pelos poetas rapsodos.",
        "Aquele que mantém fidelidade absoluta aos princípios da razão e da virtude, colocando a coerência moral acima do medo da morte.",
        "Um burocrata prudente que calcula os riscos financeiros antes de emitir qualquer parecer sobre leis civis.",
        "Um orador pragmático que adapta suas teses às preferências dos juízes para garantir sua integridade corporal.",
        "Um místico solitário que foge do convívio comunitário para contemplar as estrelas no alto de penhascos.",
        "B",
        "A morte de Sócrates coroou sua vida: a filosofia não era um discurso retórico vazio, mas uma prática existencial vivida com dignidade até o fim."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # Com resolução detalhada: - **Etapa 1:** ... - **Etapa 2:** ...
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Considere a afirmação de Protágoras: 'O homem é a medida de todas as coisas.' No plano das deliberações democráticas da pólis, essa tese implica que as leis aprovadas pela assembleia popular:",
        "Refletem mandamentos divinos imutáveis gravados na própria natureza física do cosmos.",
        "São convenções históricas humanas contingentes, validadas pelo consenso e pela utilidade para a cidade.",
        "Constituem decretos autoritários que não admitem revisões por parte das gerações futuras.",
        "Dependem da aprovação unânime de sacerdotes de santuários oraculares para entrarem em vigor.",
        "Têm como objetivo único preparar os soldados de infantaria para guerras de conquista territorial.",
        "B",
        "- **Etapa 1:** Interpretação da tese relativista de Protágoras. Ao postular o homem como medida, Protágoras rejeita a existência de leis morais e políticas transcendentes ou divinas dadas a priori.\n- **Etapa 2:** Aplicação ao campo do Direito e da política. Disso resulta que as leis da pólis (nómos) são construções coletivas humanas pactuadas entre os cidadãos, cuja legitimidade reside na utilidade pública e na capacidade de garantir a convivência harmoniosa."
    ))

    questoes_brutas.append((
        42, "EM13CHS103", "dificil",
        "Analise a passagem da Apologia de Sócrates: 'Reconheci que os homens de maior renome eram quase os mais desprovidos de juízo, ao passo que outros tidos como inferiores eram homens mais capazes quanto ao bom senso.' O método investigativo socrático desnudou qual realidade social de Atenas?",
        "A superioridade moral dos generais de cavalaria sobre todos os cidadãos que trabalhavam no comércio.",
        "A dissociação entre a reputação de autoridade pública e a posse autêntica do saber moral e conceitual.",
        "A impossibilidade de encontrar pessoas de bom senso em cidades dedicadas à navegação marítima.",
        "A obrigação cívica de entregar a chefia do governo aos poetas trágicos que escreviam para o teatro.",
        "O acerto das acusações formuladas por Meleto contra a presença de filósofos na praça da cidade.",
        "B",
        "- **Etapa 1:** Análise do relato socrático sobre o exame dos cidadãos ilustres. Ao interrogar figuras proeminentes, Sócrates constatou que a celebridade política e social encobria uma imensa vacuidade conceitual.\n- **Etapa 2:** Conclusão crítica sobre o poder constituído. O método dialógico revelou que o prestígio público não garantia o conhecimento da virtude, desmascarando a arrogância das elites dirigentes perante a juventude da pólis."
    ))

    questoes_brutas.append((
        43, "EM13CHS603", "dificil",
        "Diante de discursos políticos polarizados que utilizam termos vagos como 'defesa da liberdade' para justificar atos autoritários, a atitude socrática prescreveria qual procedimento reflexivo prioritário?",
        "A adesão imediata à narrativa com maior número de curtidas e compartilhamentos digitais.",
        "A exigência de exame rigoroso e de definição conceitual precisa do que é a liberdade em si mesma.",
        "O silenciamento violento de todos os oradores que discordarem da posição partidária oficial.",
        "O repasse de frases de efeito em grupos virtuais para acelerar o convencimento de indecisos.",
        "A renúncia à participação cidadã em favor da submissão cega a decisões de tribunais militares.",
        "B",
        "- **Etapa 1:** Diagnóstico do problema discursivo contemporâneo. A propaganda ideológica recorre a termos polissêmicos e slogans apelativos para suscitar engajamento emocional acrítico sem clareza teórica.\n- **Etapa 2:** Aplicação do método socrático. O antídoto contra a sedução retórica consiste na interpelação dialética ('O que é isso?'), exigindo a explicitação dos fundamentos lógicos e a recusa de definições circulares ou convenientes."
    ))

    questoes_brutas.append((
        44, "EM13CHS101", "dificil",
        "Górgias formulou que 'a palavra é uma grande senhora que, com o menor e mais invisível dos corpos, realiza as obras mais divinas'. Essa concepção da linguagem contrapõe-se diretamente à exigência socrática de que a fala humana deve:",
        "Subordinar a forma poética à busca desinteressada da verdade objetiva e da coerência moral.",
        "Encantar a multidão recorrendo a rimas sonoras e gestos dramáticos calculados no palanque.",
        "Impedir que os juízes do tribunal examinem as certidões e recibos anexados aos autos do processo.",
        "Servir exclusivamente para fechar contratos de aluguel de navios de carga no porto de Pireu.",
        "Reproduzir fielmente as orações transmitidas por sacerdotes em festas cívicas da primavera.",
        "A",
        "- **Etapa 1:** Compreensão da tese gorgiana sobre a soberania da palavra. Para Górgias, a linguagem é autônoma em relação aos fatos, atuando como um poderoso instrumento de manipulação dos afetos humanos e do poder político.\n- **Etapa 2:** Confronto com a exigência socrática. Em oposição ao artifício da retórica sofística, Sócrates exige a função referencial da palavra: a linguagem não deve encantar com artimanhas, mas revelar a verdade e comprometer o sujeito com a virtude."
    ))

    questoes_brutas.append((
        45, "EM13CHS103", "dificil",
        "A recusa de Sócrates em fugir de Atenas (narrada no Críton) não significou que ele concordava com a justiça moral da sentença, mas sim que ele:",
        "Considerava as prisões atenienses locais confortáveis para passar a velhice na companhia de servos.",
        "Reconhecia que a autoridade do Estado de Direito e a ordem jurídica da pólis exigem a aceitação cívica das sentenças dos tribunais legítimos.",
        "Pretendia constranger os juízes a renunciarem aos seus cargos por meio de uma greve de fome coletiva.",
        "Tinha esperança de que generais de Esparta invadissem Atenas e anulassem a votação dos jurados.",
        "Estava desprovido de recursos materiais para pagar as passagens de carruagem até a Tessália.",
        "B",
        "- **Etapa 1:** Distinção entre o teor substantivo da sentença e a autoridade do sistema legal. Sócrates sabia que seus acusadores mentiram e que os jurados erraram, mas compreendia que a sentença emanara de um tribunal institucional legítimo.\n- **Etapa 2:** Julgamento da coerência cívica. Escapar da prisão representaria agir com arbítrio próprio contra as instituições que sustentaram sua existência por 70 anos; para não destruir a ordem comum da pólis, Sócrates aceitou a pena legal, mantendo sua honra imaculada."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Ao contrastar a maiêutica socrática com o modelo de educação tradicional (criticado como 'educação bancária' por Paulo Freire), constata-se que a maiêutica:",
        "Trata o aluno como um recipiente passivo no qual o professor deposita informações já concluídas.",
        "Concebe o estudante como um sujeito racional capaz de gestar o saber por meio da reflexão dialógica guiada.",
        "Limita o ensino ao treinamento de técnicas de memorização de datas históricas e decretos civis.",
        "Proíbe qualquer intervenção do professor durante as etapas de resolução de problemas em sala.",
        "Exige que o aprendizado seja avaliado unicamente por meio de provas de múltipla escolha cronometradas.",
        "B",
        "- **Etapa 1:** Caracterização pedagógica da maiêutica socrática. O filósofo-educador não despeja conteúdos prontos, mas interroga, estimula e atua como facilitador do parto intelectual.\n- **Etapa 2:** Síntese educacional moderna. Isso fundamenta a pedagogia crítica e libertadora: a aprendizagem autêntica é uma conquista ativa da consciência reflexiva do próprio sujeito em cooperação com seus pares."
    ))

    questoes_brutas.append((
        47, "EM13CHS603", "dificil",
        "A perseguição e execução de pensadores críticos em contextos de intolerância institucionalizada repete a lógica do julgamento de Sócrates porque:",
        "Os regimes autoritários não toleram vozes que desestabilizem a inércia social e desmascarem os discursos de propaganda oficial.",
        "As leis de proteção à liberdade de cátedra foram revogadas por tratados de direito internacional.",
        "Os cientistas recusam o diálogo com o poder público em benefício de pesquisas puramente teóricas.",
        "A juventude das universidades exige o cancelamento de todas as aulas que utilizem textos escritos.",
        "Os juízes populares têm a obrigação constitucional de seguir fielmente a vontade de líderes carismáticos.",
        "A",
        "- **Etapa 1:** Análise sociopolítica do processo judicial de Sócrates. As acusações de impiedade e corrupção mascaravam o incômodo das elites com a capacidade de Sócrates de fazer a juventude pensar por conta própria.\n- **Etapa 2:** Conexão com a defesa do Estado Democrático de Direito. A história demonstra que democracias adoecem quando criminalizam seus 'tavões' sociais; a vitalidade da cidadania depende da garantia inegociável do pensamento divergente e do debate aberto."
    ))

    questoes_brutas.append((
        48, "EM13CHS101", "dificil",
        "No diálogo Laques, Sócrates conduz o general a uma situação de Aporia. Esse estado de paralisia cognitiva deve ser compreendido pedagogicamente como:",
        "O fracasso definitivo da inteligência humana em alcançar qualquer tipo de conceito razoável.",
        "A indispensável limpeza da mente que desmonta os preconceitos acríticos para preparar a gestação da verdade.",
        "Uma humilhação estratégica arquitetada para afastar o general do comando dos batalhões de infantaria.",
        "Um procedimento retórico ensinado por Górgias para vencer debates sem apresentar provas empíricas.",
        "A prova de que a coragem é uma ilusão poética criada por autores teatrais de comédias satíricas.",
        "B",
        "- **Etapa 1:** Interpretação da aporia no método dialético. Quando o interlocutor percebe que suas respostas caem em contradição insolúvel, ele perde a falsa segurança de suas certezas consagradas.\n- **Etapa 2:** Avaliação da função pedagógica da aporia. Essa desconstrução não é niilismo, mas purificação: apenas quem se liberta do falso saber herdado da tradição torna-se consciente de sua carência e disposto a investigar a definição universal verdadeira."
    ))

    questoes_brutas.append((
        49, "EM13CHS103", "dificil",
        "Ao examinar a obra As Nuvens de Aristófanes, historiadores apontam que a comédia desempenhou um papel nocivo contra Sócrates porque:",
        "Revelou documentos secretos que comprovavam o recebimento de propinas persas pelo filósofo.",
        "Fixou no imaginário popular ateniense a imagem caricata e distorcida de Sócrates como um sofista corruptor e ímpio.",
        "Incentivou os jovens da cidade a queimarem todos os rolos de papiro guardados na biblioteca de Delfos.",
        "Obrigou os magistrados a fecharem as oficinas de escultura mantidas pelo pai de Sócrates na cidade.",
        "Conduziu à prisão imediata de todos os atores e poetas trágicos que encenavam tragédias em Atenas.",
        "B",
        "- **Etapa 1:** Avaliação do impacto midiático do teatro cômico na Atenas democrática. O teatro era o meio de comunicação de massas da época, assistido por milhares de cidadãos que depois atuariam como jurados.\n- **Etapa 2:** Consequência histórica para o julgamento de 399 a.C. Ao ridicularizar Sócrates como um charlatão perigoso, Aristófanes alimentou preconceitos populares que décadas depois sustentaram as acusações fatais de Meleto perante o tribunal da Helieia."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "O relativismo moral de Protágoras, ao declarar que a justiça é mera convenção humana (nómos), foi combatido por Sócrates porque este último temia que tal postura gerasse:",
        "A cobrança de juros excessivos pelos comerciantes que vendiam trigo no porto de Pireu.",
        "A dissolução de qualquer parâmetro universal de virtude, tornando a justiça um mero instrumento da vontade do mais forte.",
        "O aumento do número de navios atenienses destruídos em tempestades durante viagens comerciais.",
        "A proibição do uso de moedas de prata nas transações financeiras realizadas dentro da cidade.",
        "A substituição do cultivo da oliveira por plantações de trigo em terras áridas da Península Ática.",
        "B",
        "- **Etapa 1:** Análise do desdobramento ético do relativismo sofístico. Se o homem particular é a medida de tudo e não há verdade objetiva em si, a justiça torna-se arbitrária e subserviente aos interesses de grupos dominantes circunstanciais.\n- **Etapa 2:** Fundamentação da reação socrática. Para Sócrates, a ética exige princípios universais fundados na razão e no bem comum; sem conceitos estáveis sobre o justo e o injusto, a vida política degenera na lei da força bruta e da dominação retórica."
    ))

    questoes_brutas.append((
        51, "EM13CHS103", "dificil",
        "A recusa de Sócrates em adotar ardis cênicos habituais no tribunal (como trazer familiares em prantos para comover os jurados) fundamentou-se no princípio de que:",
        "Os jurados atenienses tinham problemas de visão e não enxergariam as lágrimas derramadas na tribuna.",
        "O dever do réu e do filósofo é convencer a corte pela força demonstrativa dos argumentos justos, e não manipular emoções passionais.",
        "O suborno financeiro dos juízes era um método muito mais rápido e seguro para garantir a absolvição do que o choro.",
        "Os acusadores haviam prometido retirar a denúncia caso o réu permanecesse em silêncio durante a sessão.",
        "As leis da pólis proibiam terminantemente a presença de crianças com menos de dez anos em audiências públicas.",
        "B",
        "- **Etapa 1:** Exame da postura de Sócrates perante a corte popular. O costume ateniense prescrevia o uso de teatralizações sentimentais e oratórias piedosas para conseguir o perdão dos jurados.\n- **Etapa 2:** Julgamento moral da atitude filosófica. Sócrates recusou a chantagem emocional sofística porque acreditava que a justiça exige o discernimento da razão serena; rebaixar a dignidade da lei para obter a salvação física seria uma traição à sua missão educadora."
    ))

    questoes_brutas.append((
        52, "EM13CHS101", "dificil",
        "A proposição socrática de que 'a virtude é conhecimento' (intelectualismo moral) conduz à conclusão teórica de que aquele que comete uma injustiça:",
        "Age de forma perversa por ter nascido com predisposições genéticas irreparáveis para o crime violento.",
        "Age por ignorância do verdadeiro bem, acreditando falsamente que o ato desonesto lhe trará vantagens reais.",
        "Deve ser punido com suplícios corporais permanentes para servir de exemplo nas praças públicas da cidade.",
        "Demonstra uma coragem invejável que deve ser premiada com cargos de comando nos batalhões navais.",
        "Está isento de qualquer tipo de julgamento cívico caso pertença a famílias nobres tradicionais.",
        "B",
        "- **Etapa 1:** Compreensão do intelectualismo moral socrático. Sócrates sustenta que nenhum ser humano erra deliberadamente desejando o próprio mal; o sujeito busca sempre o que julga ser vantajoso ou bom.\n- **Etapa 2:** Conclusão sobre o erro moral. Quem pratica a injustiça é vítima de uma ilusão cognitiva: ignora que a corrupção da alma traz desgraça ao próprio indivíduo. Portanto, o remédio contra o delito é a educação moral e o despertar da razão."
    ))

    questoes_brutas.append((
        53, "EM13CHS603", "dificil",
        "Em debates jurídicos sobre direitos humanos, o confronto entre o relativismo cultural extremo e o universalismo dos direitos fundamentais reedita o debate entre:",
        "Os marinheiros da Jônia que buscavam rotas mercantis e os agricultores que cultivavam cevada no interior.",
        "O relativismo convencionalista dos sofistas e a busca socrática por valores universais fundados na dignidade humana.",
        "Os generais espartanos que defendiam a infantaria e os almirantes atenienses que comandavam trirremes navais.",
        "Os poetas líricos que cantavam nas festas da primavera e os comediógrafos que encenavam sátiras cívicas.",
        "Os sacerdotes do templo de Delfos e os adivinhos que liam o futuro em vísceras de ovelhas sacrificadas.",
        "B",
        "- **Etapa 1:** Identificação das raízes do debate contemporâneo dos Direitos Humanos. O relativismo cultural afirma que os valores dependem dos costumes locais; o universalismo defende garantias inalienáveis para qualquer pessoa em qualquer lugar.\n- **Etapa 2:** Conexão com os clássicos gregos. Essa disputa reproduz a tensão entre os sofistas (leis como nómos particular e transitório) e Sócrates (existência de virtudes e conceitos universais que transcendem o capricho das convenções regionais)."
    ))

    questoes_brutas.append((
        54, "EM13CHS103", "dificil",
        "A postura de Sócrates ao ouvir as advertências de seu Daimonion comprova que, ao contrário da acusação de ateísmo formulada por Meleto, o filósofo:",
        "Fundou uma seita secreta de marinheiros encarregada de desviar navios comerciais persas.",
        "Possuía uma profunda e sincera religiosidade interiorizada, subordinando suas escolhas cívicas ao mandato moral do sagrado.",
        "Utilizava técnicas mágicas de encantamento aprendidas em viagens proibidas pelo deserto oriental.",
        "Buscava consolidar um golpe de Estado para coroar seu discípulo Platão como rei supremo de Atenas.",
        "Pretendia substituir o culto dos deuses olímpicos pela adoração de estátuas de bronze esculpidas por seu pai.",
        "B",
        "- **Etapa 1:** Desconstrução da acusação de ateísmo na Apologia. Meleto acusava Sócrates de não crer nos deuses e, contraditoriamente, de seguir novas entidades espirituais (Daimonion).\n- **Etapa 2:** Julgamento da religiosidade socrática. A obediência de Sócrates ao oráculo de Apolo e à sua voz interior demonstra uma fé madura e laicizada, onde o sagrado se manifesta como imperativo ético da consciência, e não como idolatria cega."
    ))

    questoes_brutas.append((
        55, "EM13CHS101", "dificil",
        "No método socrático, o parto das ideias (Maiêutica) pressupõe que o conhecimento verdadeiro não é inventado pelo filósofo no momento do debate, mas:",
        "Comprado em manuscritos raros guardados nos templos de sacerdotes egípcios no Vale do Nilo.",
        "Descoberto pelo próprio sujeito ao tomar consciência das verdades racionais adormecidas em sua mente.",
        "Ditado diretamente por generais de cavalaria que supervisionavam os exercícios físicos dos jovens.",
        "Calculado por meio de fórmulas matemáticas restritas aos iniciados na confraria de Crotona.",
        "Transmitido por meio de encantamentos rítmicos entoados por poetas rapsodos nas praças da cidade.",
        "B",
        "- **Etapa 1:** Análise da natureza do conhecimento na teoria socrático-platônica. A alma humana (Psyché) possui em si mesma a capacidade de discernir o verdadeiro quando devidamente estimulada pelo diálogo.\n- **Etapa 2:** Síntese conceitual da maiêutica. O papel do parteiro filosófico é orientar a alma para que ela mesma reconheça as definições essenciais, superando as impressões sensíveis transitórias para atingir o conceito universal."
    ))

    questoes_brutas.append((
        56, "EM13CHS103", "dificil",
        "A margem estreita de votos na condenação inicial de Sócrates (cerca de 280 contra 221) e o posterior agravamento para a pena de morte evidenciam que:",
        "Os jurados votaram de forma aleatória por estarem cansados após uma longa sessão judicial no calor.",
        "A postura altiva de Sócrates ao propor o Pritaneu foi interpretada pela maioria como uma provocação intolerável à autoridade do tribunal.",
        "Os amigos de Sócrates subornaram metade dos juízes para adiar a execução da sentença por vários meses.",
        "O poeta Meleto desistiu das acusações de impiedade durante o discurso de réplica perante o arconte.",
        "A cidade de Atenas estava sob intervenção militar macedônia que exigia a libertação de todos os filósofos.",
        "B",
        "- **Etapa 1:** Interpretação da dinâmica da votação em duas etapas na Helieia. Na primeira votação sobre a culpa, a margem foi muito apertada; na segunda votação sobre a pena, os votos pela condenação à morte aumentaram consideravelmente.\n- **Etapa 2:** Explicação histórica da reação dos jurados. Ao recusar rebaixar-se e ao propor a maior honra da cidade (o Pritaneu) como recompensa por sua conduta, Sócrates confrontou o orgulho dos cidadãos, que preferiram condená-lo a tolerar sua independência."
    ))

    questoes_brutas.append((
        57, "EM13CHS603", "dificil",
        "Na análise foucaultiana sobre o 'cuidado de si' (*epimeleia heautou*), a filosofia socrática não se restringe a uma teoria acadêmica abstrata, mas se define como:",
        "Um conjunto mecânico de regras jurídicas voltadas ao recolhimento de tributos portuários em Pireu.",
        "Uma arte da existência e uma prática ética contínua de autotransformação e coragem moral na pólis.",
        "Um manual de etiqueta palaciana para preparar diplomatas em viagens oficiais pelo mar Egeu.",
        "Uma técnica mágica de meditação que exige o isolamento total em florestas afastadas da cidade.",
        "Um treinamento esportivo destinado a quebrar recordes em corridas de estádio nos jogos cívicos.",
        "B",
        "- **Etapa 1:** Exame da interpretação de Michel Foucault em A Coragem da Verdade. Foucault investiga Sócrates não apenas pelas teses lógicas, mas pela unidade indissociável entre seu discurso (logos) e sua conduta de vida (bios).\n- **Etapa 2:** Conclusão sobre o sentido da filosofia antiga. A missão socrática é uma 'estética da existência': cuidar da alma, examinar as próprias ações e sustentar a verdade com a própria vida perante a comunidade cívica."
    ))

    questoes_brutas.append((
        58, "EM13CHS101", "dificil",
        "A distinção sofística entre o 'discurso forte' e o 'discurso fraco' (ensinado por Protágoras) demonstra que, para a retórica pragmática:",
        "O valor de uma tese mede-se pela sua eficácia persuasiva perante o público, independentemente de sua veracidade real.",
        "Os discursos fortes são unicamente aqueles proferidos por generais armados de lanças de bronze.",
        "A escrita em folhas de pergaminho possui maior durabilidade do que as palavras faladas em praça aberta.",
        "As leis da geometria são fracas porque não despertam aplausos entusiasmados nas arquibancadas.",
        "A verdade das ciências da natureza depende do número de rimas poéticas contidas em cada parágrafo.",
        "A",
        "- **Etapa 1:** Análise do propósito pedagógico do ensino de Protágoras. O mestre sofista ensinava a 'tornar forte o argumento mais fraco' por meio do manejo hábil das antíteses e da comoção oratória.\n- **Etapa 2:** Julgamento do relativismo retórico. Essa técnica consagra a supremacia da eficácia política: o que importa no plenário é vencer a disputa e obter o voto, dissociando a habilidade verbal do compromisso com a justiça e com a verdade."
    ))

    questoes_brutas.append((
        59, "EM13CHS103", "dificil",
        "A tranquilidade de Sócrates ao ingerir a cicuta decorria de sua convicção filosófica de que nenhum mal real pode atingir o homem de bem, porque:",
        "Ele acreditava que os deuses enviariam uma águia mágica para transportá-lo para a ilha de Delos.",
        "O corpo físico e as riquezas materiais são secundários, e o verdadeiro bem reside na integridade incorruptível da alma.",
        "Os guardas da prisão haviam substituído o veneno por um caldo de legumes preparado por seus discípulos.",
        "A condenação à morte seria revogada imediatamente após a assembleia receber notícias de vitórias navais.",
        "Ele planejava fingir a própria morte para fugir com documentos de identidade falsos para a Sicília.",
        "B",
        "- **Etapa 1:** Interpretação da serenidade socrática perante a morte na Apologia e no Fédon. Sócrates afirma categoricamente aos jurados: 'Não há mal possível para o homem de bem, nem em vida nem após a morte'.\n- **Etapa 2:** Síntese da metafísica moral socrática. O mal autêntico não é o sofrimento imposto ao corpo biológico pela injustiça dos homens, mas a prática da injustiça que corrompe e adoece a alma de quem a comete."
    ))

    questoes_brutas.append((
        60, "EM13CHS101", "dificil",
        "Ao sintetizar a Virada Antropológica e o confronto entre Sócrates e os sofistas, conclui-se que esse debate legou à modernidade ocidental a tensão perpétua entre:",
        "O comércio de cerâmicas e a construção de navios de guerra para frotas marítimas.",
        "A instrumentalização pragmática da linguagem para o poder e a busca ética da verdade como fundamento da emancipação humana.",
        "A disciplina corporal dos atletas olímpicos e o repouso absoluto dos sacerdotes nos templos.",
        "A cobrança de tributos aduaneiros e a isenção de impostos para generais de cavalaria.",
        "O teatro cômico de sátira política e a pintura mural em templos dedicados à deusa Atena.",
        "B",
        "- **Etapa 1:** Exame do cerne histórico do conflito socrático-sofístico. De um lado, os sofistas representam a sofisticação da técnica retórica e o pragmatismo político; de outro, Sócrates defende o autoexame moral e a verdade universal.\n- **Etapa 2:** Legado contemporâneo da reflexão. Essa encruzilhada permanece no centro de nossas instituições democráticas: a palavra deve servir como instrumento de dominação e propaganda sedutora de interesses particulares ou como espaço de esclarecimento mútuo e compromisso com o bem comum?"
    ))

    # Balanceamento perfeito
    questoes = balancear_questoes(questoes_brutas)

    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('objeto_de_conhecimento: "O Deslocamento do Eixo Filosófico da Natureza para a Cidade, a Ética e o Ser Humano; Os Sofistas (Protágoras e Górgias): O Relativismo Moral e Epistemológico (\'O homem é a medida de todas as coisas\') e o Ensino da Retórica na Democracia Ateniense; Sócrates e a Busca pelo Conceito Universal: A Consciência da Própria Ignorância (\'Só sei que nada sei\'); O Método Dialógico: Ironia (Refutação dos Preconceitos) e Maiêutica (O Parto das Ideias); O Julgamento de Sócrates e a Fidelidade à Vida Filosófica."')
    md.append('ebook_fonte: "em-fil-c03-virada-antropologica-socrates-sofistas.md"')
    md.append('habilidades: "EM13CHS101, EM13CHS103, EM13CHS501, EM13CHS603, H1, H2, H21"')
    md.append("total_exercicios: 60")
    md.append("distribuicao:")
    md.append("  basico: 20")
    md.append("  intermediario: 20")
    md.append("  dificil: 20")
    md.append("---")
    md.append("")
    md.append("# Exercícios — A Virada Antropológica: Sócrates e os Sofistas")
    md.append("")
    md.append("## Nível Básico (Questões 1 a 20)")
    md.append("")

    for q in questoes[:20]:
        num, hab, dif, enunc, a, b, c, d, e, gab, res = q
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: virada-antropologica-socrates-sofistas -->")
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
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: virada-antropologica-socrates-sofistas -->")
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
        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: virada-antropologica-socrates-sofistas -->")
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
    md.append("- HADOT, Pierre. *O que é a Filosofia Antiga?* Tradução de Dionísio da Silva Mourão. São Paulo: Loyola, 2002.")
    md.append("- JAEGER, Werner. *Paideia: A Formação do Homem Grego*. Tradução de Artur M. Parreira. 4. ed. São Paulo: Martins Fontes, 2001.")
    md.append("- MARCONDES, Danilo. *Iniciação à História da Filosofia: Dos Pré-Socráticos a Wittgenstein*. 11. ed. Rio de Janeiro: Jorge Zahar, 2007.")
    md.append("- PLATÃO. *Diálogos: Apologia de Sócrates e Críton*. Tradução de Carlos Alberto Nunes. Belém: EDUFPA, 1999.")
    md.append("- STONE, I. F. *O Julgamento de Sócrates*. Tradução de Paulo Henriques Britto. São Paulo: Companhia das Letras, 2005.")
    md.append("- VERNANT, Jean-Pierre. *Mito e Pensamento entre os Gregos: Estudos de Psicologia Histórica*. Tradução de Haiganuch Sarian. 2. ed. Rio de Janeiro: Paz e Terra, 2006.")
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
        print("[SUCESSO TOTAL] Cap 03 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    gerar_cap03()
