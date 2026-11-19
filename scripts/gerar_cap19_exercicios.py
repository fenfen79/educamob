# -*- coding: utf-8 -*-
"""
Gerador das 60 questões atômicas de Filosofia EM - Capítulo 19:
O Contratualismo Moderno: Hobbes e Locke
Destino: content/medio/volume-unico/filosofia/eixo-3-politica/cap-19-contratualismo-hobbes-locke/ebooks/em-fil-c19-contratualismo-hobbes-locke-exercicios.md
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
        "Em contraposição ao pensamento clássico e medieval, como o Contratualismo moderno redefiniu a origem e a legitimidade do poder do Estado?",
        "A reafirmação de que os reis governam por decreto e bênção direta de Deus sobre a Terra.",
        "A compreensão de que o Estado não é um destino biológico natural nem uma dádiva divina, mas um artifício humano construído pela vontade deliberada dos indivíduos por meio de um pacto social.",
        "A tese de que os seres humanos devem retornar à vida isolada nas florestas primitivas.",
        "A proposta de que as assembleias municipais devam ser conduzidas exclusivamente por sacerdotes beneditinos.",
        "A determinação de que as cidades devam abolir os tribunais civis em favor de torneios de cavaleiros.",
        "B",
        "O contratualismo rompeu com a ideia do homem naturalmente político de Aristóteles e com o direito divino dos reis: o poder político é uma convenção artificial instituída para resolver os dilemas da convivência."
    ))

    questoes_brutas.append((
        2, "EM13CHS601", "basico",
        "Quais são os três momentos lógicos que estruturam o modelo jusnaturalista-contratualista moderno?",
        "Império feudal, Revolta camponesa e Monarquia constitucional.",
        "Estado de Natureza (condição pré-política hipotética), Contrato Social (pacto originário de fundação) e Estado Civil (ordem política legalmente estabelecida).",
        "Tribunal eclesiástico, Inquisição paroquial e Absolvição pontifícia.",
        "Corporação de artesãos, Feira mercantil e Banco de câmbio comercial.",
        "Aldeia tribal, Clã patriarcal e Cidade murada.",
        "B",
        "A tríade contratualista é a matriz teórica moderna: analisa-se a condição humana sem leis (natureza), o motivo da união deliberada (contrato) e a instituição da autoridade legal (estado civil)."
    ))

    questoes_brutas.append((
        3, "EM13CHS102", "basico",
        "Como a experiência histórica da Guerra Civil Inglesa (1642-1651) impactou a filosofia política de Thomas Hobbes expressa em O Leviatã?",
        "Hobbes tornou-se um pacifista ingênuo que defendia a extinção imediata de todos os exércitos europeus.",
        "O horror do conflito sangrento, da anarquia e da decapitação do rei Carlos I levou Hobbes a buscar uma ciência da política capaz de garantir a paz e evitar a guerra civil.",
        "Hobbes passou a defender a submissão dos parlamentos civis à autoridade monástica de bispos escoceses.",
        "A guerra motivou o filósofo a se alistar como comandante naval em expedições comerciais ultramarinas.",
        "O autor propôs que o poder temporal fosse transferido para comissões de comerciantes de tecidos.",
        "B",
        "Ao presenciar a carnificina fratricida e o colapso da autoridade, Hobbes sentenciou que o medo e ele eram gêmeos, projetando o Leviatã para sufocar o fantasma da guerra civil."
    ))

    questoes_brutas.append((
        4, "EM13CHS101", "basico",
        "De que modo a física mecanicista influenciou o diagnóstico antropológico de Thomas Hobbes sobre os indivíduos no estado de natureza?",
        "Os seres humanos são anjos benevolentes guiados unicamente pelo amor ao próximo.",
        "Os homens são corpos materiais em movimento contínuo, movidos por apetites, desejos de autopreservação e aversão à dor e à morte.",
        "Os indivíduos nascem com uma vocação espontânea e inata para a harmonia comunitária sem necessidade de regras.",
        "A humanidade é formada exclusivamente por sábios que renunciam a qualquer bem material.",
        "Os homens são seres místicos que obedecem a revelações espirituais anunciadas durante os sonhos.",
        "B",
        "Inspirado na física mecanicista de Galileu, Hobbes via o ser humano como um complexo de apetites e aversões; sem um freio comum, a busca individual de sobrevivência gera colisão constante."
    ))

    questoes_brutas.append((
        5, "EM13CHS602", "basico",
        "Por que Hobbes argumenta que a 'Igualdade Natural' entre os seres humanos no estado de natureza é uma das fontes fundamentais da insegurança coletiva?",
        "Porque todos os homens recebem o mesmo salário mensal pago pelo tesouro público.",
        "Porque mesmo o indivíduo mais fraco tem força ou astúcia suficiente para tirar a vida do mais forte, gerando uma condição em que ninguém se encontra seguro.",
        "Porque os cidadãos usam trajes uniformes que impedem o reconhecimento visual nas ruas.",
        "Porque as assembleias cívicas distribuíam ferramentas agrícolas idênticas a todos os camponeses.",
        "Porque as leis municipais proibiam que as residências particulares tivessem dimensões desiguais.",
        "B",
        "Para Hobbes, a igualdade não é harmonia, mas vulnerabilidade partilhada: o mais vulnerável pode usar uma emboscada ou alianças para matar o mais robusto, espalhando o medo constante."
    ))

    questoes_brutas.append((
        6, "EM13CHS102", "basico",
        "Quais são as três paixões capitais identificadas por Thomas Hobbes como causas permanentes da discórdia entre os homens?",
        "A caridade, a humildade e a penitência silenciosa.",
        "A Competição (pelo ganho material), a Desconfiança (pela segurança preventiva) e a Glória (pela honra e reputação).",
        "A preguiça, a intemperança e o desprezo pelos estudos literários.",
        "A devoção mística, o apego a festividades populares e o cultivo de pomares.",
        "A fidelidade cega, a obediência eclesiástica e a reverência aos antepassados.",
        "B",
        "No estado pré-político, essas três forças psicológicas empurram os indivíduos para o confronto: luta-se por recursos escassos, ataca-se antes para não ser atacado e disputa-se o prestígio perante os pares."
    ))

    questoes_brutas.append((
        7, "EM13CHS601", "basico",
        "O que Thomas Hobbes sintetiza através do antigo adágio latino 'Homo homini lupus' (o homem é o lobo do homem)?",
        "Que os seres humanos descendem biologicamente de canídeos selvagens das montanhas alpinas.",
        "Que, na ausência de leis civis e de um poder estatal soberano comum, os indivíduos agem como predadores impiedosos uns contra os outros em busca de sobrevivência.",
        "Que os governantes devem criar reservas florestais para a preservação de alcateias silvestres.",
        "Que os tratados internacionais exigem que os exércitos usem insígnias com desenhos de feras.",
        "Que as punições criminais na Inglaterra medieval eram executadas em florestas boreais.",
        "B",
        "Sem a autoridade soberana para manter a ordem, a ausência de freios morais objetivos converte o ser humano em um perigo mortal para o seu próprio semelhante."
    ))

    questoes_brutas.append((
        8, "EM13CHS101", "basico",
        "Como Hobbes descreve a condição existencial da vida humana no estado de natureza no célebre capítulo XIII de O Leviatã?",
        "Uma existência festiva, farta, repleta de delícias pastoris e amizade espontânea entre vizinhos.",
        "Uma vida solitária, miserável, sórdida, animalesca e curta, marcada pelo medo contínuo e perigo de morte violenta.",
        "Um período de iluminação intelectual no qual todos se dedicavam à astronomia de precisão.",
        "Uma sociedade cooperativa administrada por corporações beneficentes de artesãos urbanos.",
        "Um estado de transe religioso no qual os cidadãos não precisavam se alimentar de colheitas.",
        "B",
        "Sem paz e sem garantias jurídicas, não florescem as artes, o comércio ou a agricultura: o indivíduo passa os dias em vigília angustiada tentando não ser assassinado."
    ))

    questoes_brutas.append((
        9, "EM13CHS602", "basico",
        "Qual é o estatuto da 'Propriedade Privada' e da 'Justiça' no estado de natureza concebido por Thomas Hobbes?",
        "A propriedade é um direito sagrado eterno protegido por sacerdotes de ordens monásticas.",
        "Não existe propriedade privada nem justiça ou injustiça: a posse dura apenas enquanto alguém puder mantê-la pela força, pois onde não há lei civil nem poder comum, não há injustiça.",
        "A propriedade é dividida em partes matematicamente idênticas por agrimensores públicos.",
        "A justiça decorre de sentenças lavradas em pergaminhos selados por magistrados reais itinerantes.",
        "As leis de mercado garantem contratos mercantis firmados em feiras de lã e trigo.",
        "B",
        "Para Hobbes, justiça e direito de posse são criações exclusivas da ordem civil: onde inexiste soberano para ditar e impor as regras, tudo pertence a todos e a posse é mera ocupação precária pela força."
    ))

    questoes_brutas.append((
        10, "EM13CHS102", "basico",
        "Dentre as diversas inclinações humanas, que sentimento primordial impele os homens a abandonarem o estado de natureza hobbesiano para instituir o Estado civil?",
        "A ambição de viajar para colônias ultramarinas em frotas de veleiros.",
        "O medo desesperador da morte violenta, aliado ao anseio racional de uma vida segura e confortável.",
        "O desejo de construir pirâmides cerimoniais para abrigar governantes falecidos.",
        "A inclinação piedosa para fazer doações financeiras a templos e oratórios paroquiais.",
        "A paixão esportiva pela realização de torneios anuais de arco e flecha.",
        "B",
        "O medo de perder a própria vida brutalmente é a força motriz que dobra o egoísmo humano e faz a razão sugerir a renúncia às armas e a união em um pacto de paz."
    ))

    questoes_brutas.append((
        11, "EM13CHS601", "basico",
        "Por que Hobbes afirma categoricamente que 'os pactos sem a espada não passam de meras palavras'?",
        "Porque os documentos oficiais do governo britânico deveriam ser autenticados com lâminas de ferro.",
        "Porque compromissos e promessas verbais de não agressão são inócuos se não houver um poder soberano dotado de força física real para punir exemplarmente quem violar o acordo.",
        "Porque as cerimônias de posse de ministros exigiam desfiles com armaduras de cavaleiros.",
        "Porque os cidadãos que firmavam acordos comerciais recebiam adagas como comprovante contratual.",
        "Porque os tribunais criminais eram instalados em oficinas de forjamento de armas brancas.",
        "B",
        "Sem a ameaça crível do castigo soberano (a espada da justiça), a palavra é frágil e qualquer indivíduo rompe o pacto assim que vislumbrar vantagem particular."
    ))

    questoes_brutas.append((
        12, "EM13CHS101", "basico",
        "Qual é a natureza jurídica do 'Pacto de Submissão' que institui o soberano absolutista (o Leviatã) em Thomas Hobbes?",
        "Um contrato celebrado diretamente entre os cidadãos e o rei, prevendo obrigações recíprocas e penalidades iguais para ambas as partes.",
        "Um pacto firmado pelos indivíduos entre si, no qual cada um transfere o direito de governar a si mesmo a um terceiro (o Soberano), que não é parte do contrato e recebe poder supremo.",
        "Um acordo comercial no qual a sociedade vende títulos do tesouro público a banqueiros estrangeiros.",
        "Uma assembleia de clérigos que submete as forças policiais da capital ao controle papal.",
        "Um decreto militar emitido por generais de artilharia pesada após a ocupação de portos.",
        "B",
        "Como o soberano não firmou o pacto com os súditos (foram estes que pactuaram reciprocamente em favor dele), ele não comete quebra de contrato nem pode ser destituído sob alegação de ilegalidade."
    ))

    questoes_brutas.append((
        13, "EM13CHS603", "basico",
        "Quais são os atributos fundamentais do Poder Soberano instituído no Estado hobbesiano?",
        "Um poder temporário, rotativo e fiscalizado semanalmente por comitês de bairro.",
        "Um poder absoluto, supremo e indivisível, que concentra o monopólio da coerção armada, a elaboração das leis civis e o julgamento dos conflitos.",
        "Um mandato honorário sem capacidade de impor sanções materiais ou privações de liberdade.",
        "Uma federação descentralizada na qual cada paróquia religiosa estabelece seus próprios impostos.",
        "Uma junta parlamentar que depende da aprovação unânime de todos os agricultores do reino.",
        "B",
        "Para Hobbes, dividir o poder soberano é abrir as portas para a guerra civil; a soberania precisa ser indivisível e suprema para garantir que nenhuma facção rival confronte o Estado."
    ))

    questoes_brutas.append((
        14, "EM13CHS102", "basico",
        "Qual é o único direito residual e inalienável que o súdito hobbesiano conserva perante o poder soberano do Leviatã?",
        "O direito de recusar o pagamento de taxas aduaneiras sobre mercadorias têxteis.",
        "O direito natural à legítima defesa da própria vida física, caso o soberano ordene a ele que se mate ou que não resista à execução de sua pena de morte.",
        "O direito de escolher seus próprios juízes através de sorteio em feiras municipais.",
        "A faculdade de fundar partidos políticos clandestinos para derrubar o regime civil.",
        "A faculdade de imprimir moeda própria para custear empreendimentos agrícolas.",
        "B",
        "A preservação da vida foi a única razão que levou o homem ao pacto; ordenar a sua autodestruição desfaz o sentido da autoridade para aquele indivíduo específico, que readquire o direito à autodefesa."
    ))

    questoes_brutas.append((
        15, "EM13CHS601", "basico",
        "Qual acontecimento histórico do século XVII inspirou e legitimou a reflexão política liberal de John Locke em oposição ao absolutismo dos Stuart?",
        "A Revolução Francesa e a Tomada da Bastilha em 1789.",
        "A Revolução Gloriosa de 1688 na Inglaterra, que depôs Jaime II e consolidou a monarquia parlamentar através da Declaração de Direitos (Bill of Rights de 1689).",
        "A unificação dos principados germânicos sob o comando da Prússia militar.",
        "A expulsão das frotas holandesas do porto litorâneo de Recife pelos colonos locais.",
        "A descoberta de jazidas de prata em montanhas do império espanhol no Peru.",
        "B",
        "Locke foi o filósofo da Revolução Gloriosa: seu pensamento legitima a vitória do Parlamento contra o absolutismo régio, fundando o constitucionalismo moderno."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Em contraste com a visão de Hobbes, como John Locke descreve a condição dos indivíduos no Estado de Natureza no Segundo Tratado sobre o Governo Civil?",
        "Um estado de guerra total, selvageria animalesca e carnificina ininterrupta entre todos os seres humanos.",
        "Um estado de relativa paz, concórdia e liberdade, no qual os seres humanos vivem orientados pela Lei da Natureza e gozam de direitos fundamentais.",
        "Um vácuo social em que os seres humanos não possuíam linguagem articulada nem capacidade racional.",
        "Uma colônia penitenciária internacional administrada por marinheiros de potências comerciais.",
        "Um império burocrático altamente tributário que cobrava taxas sobre a circulação de pescados.",
        "B",
        "Para Locke, o estado de natureza não é um pandemônio hobbesiano; a razão humana e a lei natural ensinam que ninguém deve prejudicar o semelhante em sua vida, liberdade ou posses."
    ))

    questoes_brutas.append((
        17, "EM13CHS602", "basico",
        "Quais são os três 'Direitos Naturais Inalienáveis' que todo indivíduo possui desde o nascimento na teoria política de John Locke?",
        "O direito de comerciar especiarias, o direito de navegar em alto-mar e a isenção de impostos alfandegários.",
        "O direito à Vida, o direito à Liberdade e o direito de Propriedade (em sentido amplo, englobando a pessoa e seus bens).",
        "A liberdade de voto parlamentar, o soldo militar e o acesso gratuito a bibliotecas de conventos.",
        "O porte de adagas de aço, a caça de cervos reais e a cobrança de juros mercantis.",
        "O direito de cunhar moedas de ouro, o monopólio da mineração e a posse de escravizados no campo.",
        "B",
        "Para Locke, esses direitos não decorrem de concessão de governos ou de leis civis: são direitos naturais inatos outorgados por Deus e pela razão, sendo invioláveis pelo Estado."
    ))

    questoes_brutas.append((
        18, "EM13CHS102", "basico",
        "De acordo com John Locke (Capítulo V do Segundo Tratado), qual é o fundamento legítimo que gera a 'Propriedade Privada' a partir dos bens que a natureza ofereceu em comum à humanidade?",
        "A força das armas de guerra e a aniquilação física de populações nativas desarmadas.",
        "O Trabalho humano: ao misturar o esforço de seu corpo e o suor de suas mãos com a matéria natural bruta, o homem anexa aquele bem à sua propriedade particular legítima.",
        "A autorização formal concedida por conselhos de bispos e teólogos da corte.",
        "O sorteio de lotes de terra realizado por magistrados municipais no início da primavera.",
        "O pagamento pontual de tributos de vassalagem a senhores feudais proprietários de castelos.",
        "B",
        "O trabalho é a fonte da posse legítima: quem ara a terra inculta, planta trigo e colhe o grão transforma a natureza e cria riqueza, tornando justa a apropriação do fruto de seu esforço."
    ))

    questoes_brutas.append((
        19, "EM13CHS601", "basico",
        "Se o estado de natureza lockeano é pacífico e os direitos naturais já existem, por que os indivíduos decidem celebrar o pacto social e instituir o Estado civil?",
        "Porque os cidadãos desejam construir palácios monumentais para ostentação pública perante reinos vizinhos.",
        "Para superar a insegurança e as inconveniências decorrentes da ausência de leis civis claras, de juízes imparciais conhecidos e de um poder público para executar as sentenças justas.",
        "Porque as assembleias cívicas exigiam a contratação obrigatória de marinheiros estrangeiros.",
        "Porque a Igreja ordenava que todos os agricultores familiares deveriam doar suas terras a abadias.",
        "Porque as tempestades marítimas impediam o comércio de carnes secas com portos do mar do Norte.",
        "B",
        "A grande falha do estado de natureza é cada um ser o próprio juiz: a paixão cega faz o homem punir com vingança o vizinho e relevar seus próprios erros, exigindo juízes imparciais."
    ))

    questoes_brutas.append((
        20, "EM13CHS603", "basico",
        "Qual é a meta fundamental que justifica a criação e a manutenção do governo civil na teoria de John Locke?",
        "Impor uma única fé religiosa e converter os cidadãos mediante perseguição espiritual institucional.",
        "Atuar como fiador da sociedade, tendo como missão exclusiva preservar e proteger os direitos naturais à vida, à liberdade e à propriedade dos cidadãos sob o império da lei.",
        "Controlar diretamente toda a produção manufatureira e determinar os preços de todos os tecidos no mercado.",
        "Substituir as residências familiares particulares por dormitórios comunais administrados por soldados.",
        "Cobrar tributos confiscatórios para financiar expedições coloniais em busca de minas de ouro.",
        "B",
        "O governo é um servidor da cidadania: sua única razão de existir é atuar como árbitro imparcial que protege a liberdade e os bens dos indivíduos contra o arbítrio e a violência."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Em que consiste a natureza 'Fiduciária' (*trust*) do poder de governo na teoria política de John Locke?",
        "Na garantia de que os magistrados recebem empréstimos automáticos de banqueiros da cidade.",
        "No princípio de que o governo recebe um mandato de confiança pública para cumprir fins estritos de proteção dos direitos cidadãos; caso descumpra esse dever, o poder retorna legitimamente às mãos do povo.",
        "Na obrigatoriedade de que os governantes façam depósitos em ouro nos cofres de cartórios de notas.",
        "Na determinação de que os ministros de Estado devam pertencer a ordens maçônicas secretas.",
        "No regulamento de que os títulos nobiliárquicos devam ser transmitidos unicamente a sobrinhos distantes.",
        "B",
        "O governante é um administrador fiduciário: ele não é dono do poder, mas depositário de uma procuração social; se atraiçoar a confiança dos governados, comete quebra do mandato e perde a autoridade."
    ))

    questoes_brutas.append((
        22, "EM13CHS601", "intermediario",
        "Como John Locke articula a divisão de poderes no governo civil e qual órgão ele define como o poder supremo da república?",
        "Subordinando todos os poderes aos comandos de uma corte marcial de generais de brigada.",
        "Separando o Poder Legislativo (o poder supremo da república, encarregado de criar as leis gerais) do Poder Executivo (responsável por aplicá-las), além do Poder Federativo para a diplomacia e segurança externa.",
        "Concedendo o poder absoluto e ilimitado de veto aos conselhos eclesiásticos da paróquia.",
        "Determinando que os juízes de tribunais civis devam nomear os membros do parlamento municipal.",
        "Entregando a administração da segurança pública a companhias privadas de navegação mercante.",
        "B",
        "Para evitar a tirania da concentração, o Legislativo faz as leis e o Executivo as cumpre; o Legislativo é supremo porque emana diretamente do consentimento dos representantes do povo soberano."
    ))

    questoes_brutas.append((
        23, "EM13CHS602", "intermediario",
        "Qual é o papel atribuído por John Locke ao 'Princípio da Maioria' na dinâmica deliberativa do corpo político constituído?",
        "A maioria deve agir para aniquilar sumariamente os bens patrimoniais de todas as minorias étnicas.",
        "Como a sociedade política é um corpo coletivo que necessita se mover em uma única direção, o consenso majoritário dos cidadãos é o motor legítimo que comanda as decisões do Estado civil.",
        "As deliberações parlamentares exigem a unanimidade absoluta de 100% dos cidadãos em todas as votações.",
        "A maioria é obrigada por decretos monárquicos a acatar sem questionar os votos dos nobres de sangue.",
        "O critério numérico deve ser substituído pelo peso físico das armaduras dos representantes eleitos.",
        "B",
        "A unanimidade é impossível na diversidade social: para que a comunidade política possa agir e promulgar leis com eficácia, a força motriz legítima reside na deliberação da maioria dos votantes."
    ))

    questoes_brutas.append((
        24, "EM13CHS102", "intermediario",
        "Sob quais condições os cidadãos adquirem o legítimo 'Direito de Resistência e Revolta Armada' contra os governantes, segundo John Locke?",
        "Sempre que os governantes aumentarem as taxas cobradas pelo estacionamento de carroças no porto.",
        "Quando o governo violar de forma sistemática a confiança nele depositada, atentando contra a vida, a liberdade civil e os bens da população através de atos de tirania e despotismo arbitrário.",
        "Sempre que o parlamento aprovar a construção de pontes de pedra sobre rios navegáveis.",
        "Quando os magistrados exigirem o uso de perucas brancas nas sessões de tribunais de justiça.",
        "Sempre que as chuvas atrasarem a colheita anual de maçãs e trigo nos condados rurais.",
        "B",
        "O tirano que governa sem lei declara guerra contra o seu próprio povo; rompida a confiança fiduciária, a cidadania tem o direito sagrado de insurreição para destituir o usurpador e restaurar a república."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "O que significa a emblemática expressão 'Apelo aos Céus' (*Appeal to Heaven*) utilizada por John Locke no Segundo Tratado?",
        "A obrigação de os cidadãos se reunirem em templos para orar pedindo a conversão piedosa de tiranos.",
        "O direito supremo de recorrer à insurreição, às armas e à revolta física para derrubar governantes despóticos quando já não existem tribunais civis imparciais na Terra para remediar a opressão.",
        "A leitura obrigatória de cartas astrológicas antes de qualquer declaração de guerra a reinos vizinhos.",
        "A interrupção das atividades legislativas sempre que ocorrerem eclipses lunares ou tempestades solares.",
        "O protocolo diplomático de solicitar a mediação de monges eremitas em disputas tributárias.",
        "B",
        "Quando o governante fecha os tribunais e usa a violência contra a sociedade, não resta juiz humano imparcial no mundo: o povo faz seu apelo a Deus (ao Céu) empunhando as armas em legítima defesa de seus direitos."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Qual é a divergência basilar entre Hobbes e Locke sobre a origem e a natureza da 'Propriedade Privada'?",
        "Para ambos os pensadores, a propriedade foi criada por monges beneditinos na Idade Média.",
        "Para Hobbes, a propriedade é uma criação posterior da lei civil do Estado Soberano; para Locke, a propriedade é um direito natural pré-político gerado pelo trabalho antes mesmo de o Estado existir.",
        "Para Hobbes, a propriedade é comunal e coletiva; para Locke, ela pertence exclusivamente à nobreza de sangue.",
        "Para Hobbes, a terra pertence a quem vence duelos de espada; para Locke, ela é distribuída por loterias públicas.",
        "Para ambos, o direito de posse é ilegítimo e deve ser abolido em favor da anarquia pura.",
        "B",
        "Em Hobbes, você só tem propriedade porque o Leviatã existe e a protege com leis; em Locke, o indivíduo já tem propriedade legítima pelo seu trabalho, e o Estado é fundado para preservá-la."
    ))

    questoes_brutas.append((
        27, "EM13CHS601", "intermediario",
        "Ao comparar o modelo de soberania entre os dois contratualistas, qual é a diferença essencial entre o soberano hobbesiano e o governo lockeano?",
        "O soberano de Hobbes é eleito anualmente por sufrágio universal, enquanto o de Locke é vitalício e hereditário.",
        "O soberano de Hobbes é absoluto, indivisível e paira acima da lei; o governo de Locke é limitado pelo império da lei, subordinado ao Legislativo e sujeito à destituição popular caso viole direitos.",
        "O governante hobbesiano deve abdicar de qualquer força armada; o de Locke detém poder militar irrestrito.",
        "Hobbes propõe a criação de uma teocracia clerical; Locke defende uma monarquia absoluta despótica.",
        "Ambos defendem que os cidadãos devem eleger conselhos militares permanentes para julgar os monarcas.",
        "B",
        "Hobbes sacrifica a liberdade individual no altar da segurança contra a anarquia; Locke concebe um Estado sob as leis, onde a autoridade existe apenas para garantir e expandir a liberdade cidadã."
    ))

    questoes_brutas.append((
        28, "EM13CHS602", "intermediario",
        "De que modo a Declaração de Independência dos Estados Unidos de 1776, redigida por Thomas Jefferson, traduz a teoria política de John Locke?",
        "Proclamando a lealdade eterna e incondicional das treze colônias à autoridade do monarca britânico.",
        "Consagrando a tese de que todos os homens possuem direitos inalienáveis à vida, à liberdade e à busca da felicidade, e que, se o governo destruir esses fins, é direito do povo aboli-lo e fundar uma nova ordem.",
        "Exigindo que todos os fazendeiros norte-americanos adotem os preceitos do absolutismo hobbesiano.",
        "Estabelecendo que a posse de terras depende do consentimento direto de bispos da Igreja Anglicana.",
        "Defendendo que a escravidão seja imediatamente extinta em todas as partes do continente europeu.",
        "B",
        "Jefferson reproduziu o contrato lockeano: governos derivam seus justos poderes do consentimento dos governados; quando o rei George III violou esses direitos, o povo exerceu o Apelo aos Céus para criar sua república."
    ))

    questoes_brutas.append((
        29, "EM13CHS102", "intermediario",
        "Como a sociologia contemporânea correlaciona o colapso de 'Estados Falidos' (onde milícias armadas e facções criminosas disputam territórios) com a tese de Hobbes?",
        "Demonstrando que a ausência de autoridade estatal gera um paraíso de igualdade pacífica entre cidadãos.",
        "Evidenciando que a perda do monopólio estatal da violência legítima empurra a sociedade de volta para o estado de natureza, onde a vida dos cidadãos comuns fica à mercê da extorsão armada e do medo contínuo da morte violenta.",
        "Provando que a ausência de polícia e tribunais estimula o desenvolvimento de indústrias automobilísticas.",
        "Mostrando que as populações periféricas preferem pagar tributos a milícias em vez de terem escolas públicas.",
        "Comprovando que os grupos paramilitares governam orientados por preceitos de filósofos aristotélicos.",
        "B",
        "Sem o poder comum do Leviatã para manter todos em respeito à lei, o vácuo é preenchido pelo crime organizado: cada um tenta sobreviver armado contra o vizinho, recriando a guerra de todos contra todos."
    ))

    questoes_brutas.append((
        30, "EM13CHS603", "intermediario",
        "De que maneira o artigo 5º da Constituição Federal brasileira de 1988 combina a matriz liberal de Locke com a exigência da justiça social e do bem comum?",
        "Proibindo categoricamente qualquer indivíduo de possuir imóveis ou terras produtivas no país.",
        "Assegurando no inciso XXII que 'é garantido o direito de propriedade' (Locke), e subordinando-o no inciso XXIII ao princípio de que 'a propriedade atenderá a sua função social'.",
        "Determinando que todas as fazendas particulares devem ser entregues a corporações militares de infantaria.",
        "Estabelecendo que os contratos de compra e venda de imóveis devem ser autenticados em cartórios da Europa.",
        "Exigindo que os proprietários de imóveis urbanos prestem serviços voluntários de vigília noturna.",
        "B",
        "A Carta de 1988 acolhe a tradição liberal de Locke protegendo a posse e a iniciativa individual, mas introduz um limite republicano moderno: a propriedade deve gerar empregos, utilidade coletiva e respeito ambiental."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Qual é o equívoco metodológico mais comum de estudantes a respeito do conceito de 'Estado de Natureza' em Hobbes e Locke?",
        "Acreditar que os pensadores foram membros de comitês parlamentares britânicos de reforma urbana.",
        "Imaginar que o estado de natureza foi um período histórico arqueológico real, quando na verdade ele é uma hipótese lógica e um experimento mental contrafactual sobre a vida sem leis civis.",
        "Pensar que os autores defendiam a abolição da moeda e a troca direta de peles de animais selvagens.",
        "Supor que os textos contratualistas foram concebidos originalmente para regular o transporte fluvial de carvão.",
        "Julgar que Hobbes e Locke se recusavam a utilizar a escrita impressa em suas comunicações epistolares.",
        "B",
        "O estado de natureza não é antropologia pré-histórica; é um experimento hipotético: o que ocorreria conosco se o poder coercitivo desaparecesse hoje? É essa pergunta que legitima o contrato social."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Por que é um erro confundir o Absolutismo proposto por Thomas Hobbes com uma tirania sádica ou ilegal?",
        "Porque o soberano hobbesiano não possui forças armadas e governa apenas declamando versos líricos.",
        "Porque o poder absoluto no Leviatã é outorgado unicamente para garantir a paz pública, a segurança e a proteção da vida dos cidadãos; o soberano que promove a desordem destrói a própria finalidade de sua soberania.",
        "Porque as decisões do soberano eram revisadas anualmente por plebiscitos populares em anfiteatros.",
        "Porque o monarca do Leviatã era obrigado por votos religiosos a viver em extrema pobreza material.",
        "Porque a legislação civil da Inglaterra exigia que os reis dividissem suas terras com os servos do campo.",
        "B",
        "Hobbes não defende a violência gratuita de tiranos: o soberano recebe poder ilimitado por necessidade funcional, para que tenha força suficiente para deter bandos armados e impedir a anarquia sangrenta."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "Ao sentenciar no Segundo Tratado que 'onde não há lei, não há liberdade', qual equívoco sobre o liberalismo político John Locke refuta antecipadamente?",
        "A ideia de que as leis civis devam ser suprimidas para permitir o comércio irrestrito de tecidos no mar.",
        "O equívoco de supor que a liberdade consiste na anarquia em que cada indivíduo faz tudo o que lhe convém sem limites, demonstrando que a verdadeira liberdade civil exige leis claras que nos protejam do arbítrio do outro.",
        "A tese de que a cobrança de tributos municipais deve ser realizada mediante confisco de animais domésticos.",
        "O pressuposto de que os parlamentos nacionais devem fechar suas portas durante períodos de recessão fabril.",
        "A proposta de que os magistrados de tribunais penais devam emitir sentenças baseadas em adivinhação oracular.",
        "B",
        "Para Locke, sem a lei que limita a agressão do vizinho, o homem vira escravo do medo e da força bruta do mais forte; a liberdade civil floresce justamente sob o império de leis estáveis e conhecidas por todos."
    ))

    questoes_brutas.append((
        34, "EM13CHS602", "intermediario",
        "Em seu livro Patriarcha, o teórico absolutista Robert Filmer defendia que os reis governam por autoridade paternal natural herdada diretamente de Adão. Como John Locke demoliu essa tese no Primeiro Tratado sobre o Governo Civil?",
        "Provando que Adão era um general de brigada militar que desconhecia os preceitos do cristianismo.",
        "Demonstrando que o poder paterno sobre os filhos é temporário e fundado no dever de educar, sendo inteiramente diferente do poder político sobre cidadãos adultos livres, que só pode nascer do consentimento contratual.",
        "Afirmando que a monarquia britânica descendia geneticamente de faraós do antigo império egípcio.",
        "Defendendo que a guarda dos filhos deveria ser transferida compulsoriamente a corporações de tecelões.",
        "Sustentando que os reis da Inglaterra deveriam governar utilizando títulos honoríficos de bispos canônicos.",
        "B",
        "Filmer confundia família com política; Locke provou que filhos devem obediência aos pais até atingirem a razão, mas cidadãos adultos e livres não são crianças eternas e só devem obediência a leis consentidas."
    ))

    questoes_brutas.append((
        35, "EM13CHS603", "intermediario",
        "Por que John Locke argumenta que submeter-se a um 'Monarca Absoluto' é, na verdade, uma condição pior do que permanecer no próprio Estado de Natureza?",
        "Porque os monarcas absolutos proibiam a realização de feiras mercantis de grãos nas capitais.",
        "Porque no estado de natureza cada indivíduo tem o direito de defender a sua vida e lutar contra quem o ataca, enquanto sob o déspota absoluto o homem é desarmado e colocado à mercê de um tirano que comanda exércitos e não responde a lei alguma.",
        "Porque as cortes monárquicas consumiam vinhos franceses que geravam deficits na balança comercial.",
        "Porque os reis absolutistas obrigavam todos os cidadãos a aprenderem a tocar alaúdes renascentistas.",
        "Porque a nobreza de sangue recusava-se a participar de julgamentos realizados em praças públicas.",
        "B",
        "Locke formula uma ironia célebre: seria a tolice de pensar que os homens seriam tão loucos a ponto de se protegerem de doninhas e raposas (seus vizinhos) jogando-se na cova de um leão (o soberano absolutista)."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Como a teoria das Relações Internacionais aplica o modelo hobbesiano para caracterizar o sistema interestatal contemporâneo a partir da Paz de Vestfália (1648)?",
        "Definindo a arena internacional como um império pacífico administrado por ordens monásticas unificadas.",
        "Compreendendo que os Estados soberanos convivem entre si em um estado de natureza latente, pois não existe um governo mundial supremo dotado de espada e tribunais compulsórios sobre todas as nações.",
        "Provando que as fronteiras territoriais foram delimitadas por acordos verbais entre marinheiros mercantes.",
        "Mostrando que os tratados bilaterais dispensam qualquer preparo militar ou diplomático dos governos.",
        "Exigindo que os exércitos nacionais sejam dissolvidos para dar lugar a tribunais de comércio fluvial.",
        "B",
        "No plano internacional, os países vivem o dilema do estado de natureza de Hobbes: na falta de um soberano global que imponha a lei a todos, as potências garantem sua segurança pela diplomacia e pelas armas."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "Qual é a posição de Thomas Hobbes sobre a relação entre o Estado Soberano e a Autoridade Religiosa em O Leviatã?",
        "O soberano civil deve se ajoelhar e receber suas ordens executivas diretamente do Papa em Roma.",
        "O Soberano civil deve ser a autoridade suprema tanto no âmbito temporal quanto no eclesiástico, controlando os dogmas públicos e as nomeações de bispos para evitar que profetas gerem guerras civis.",
        "A religião deve ser banida compulsoriamente e todos os templos devem ser demolidos nas cidades.",
        "As congregações religiosas devem possuir exércitos particulares para patrulhar os bairros operários.",
        "Os sacerdotes devem ser sorteados anualmente entre os carpinteiros navais do porto litorâneo.",
        "B",
        "Hobbes via na divisão entre poder temporal e espiritual a receita da guerra civil: na gravura do Leviatã, o monarca segura a espada civil em uma mão e o báculo pastoral na outra, unificando a autoridade."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Em sua obra 'Carta sobre a Tolerância' (1689), como John Locke delimita as esferas de atuação do Magistrado Civil e da Igreja?",
        "Autorizando os magistrados a prenderem cidadãos que se recusem a fazer orações matinais em templos.",
        "Estabelecendo que o Estado cuida exclusivamente de bens civis exteriores (vida, liberdade, integridade física e posses), não tendo competência nem direito de coagir a fé interna das consciências, que é o campo livre da Igreja.",
        "Defendendo que as corporações religiosas de monges administrem os tribunais de cobrança de dívidas civis.",
        "Determinando que a Bíblia deva ser adotada como o único código penal vigente em cidades portuárias.",
        "Propondo a extinção de todas as seitas cristãs em favor da adoração exclusiva aos deuses romanos antigos.",
        "B",
        "Locke formula os pilares da laicidade moderna: o Estado usa a força para proteger direitos externos materiais; mas a salvação da alma é matéria da consciência individual, onde a espada estatal não pode entrar."
    ))

    questoes_brutas.append((
        39, "EM13CHS602", "intermediario",
        "De acordo com Locke, qual é o papel desempenhado pela introdução da 'Moeda' (ouro e prata) na expansão da propriedade e da desigualdade material legítima entre os homens?",
        "A moeda foi inventada por tiranos absolutistas para confiscar o gado leiteiro dos pequenos agricultores.",
        "Como a moeda é um metal durável que não se corrompe nem estraga com o tempo, o consentimento tácito em seu uso permitiu aos homens acumular posses além do consumo imediato sem violar o desperdício da lei natural.",
        "A moeda causou a destruição imediata de todas as ferramentas agrícolas utilizadas nas colheitas rurais.",
        "Os comerciantes foram proibidos por decretos municipais de utilizarem moedas em contratos mercantis.",
        "A circulação de prata determinou a transferência compulsória de indústrias fabris para áreas litorâneas.",
        "B",
        "No estado de natureza inicial, colher mais maçãs do que se pode comer era pecado (estragar comida); mas a moeda não apodrece, permitindo aos homens acumular riquezas e terras pelo trabalho e pelo comércio justo."
    ))

    questoes_brutas.append((
        40, "EM13CHS603", "intermediario",
        "Como a distinção entre o 'Consentimento Expresso' e o 'Consentimento Tácito' em John Locke fundamenta o dever de obedecer às leis em sociedades consolidadas?",
        "Exigindo que todos os jovens ao completarem dezoito anos assinem termos notariais em folhas de pergaminho.",
        "Estabelecendo que qualquer indivíduo que desfrute pacificamente das estradas, da proteção civil, dos hospitais ou das propriedades de um Estado consente tacitamente em se submeter às suas leis enquanto ali residir.",
        "Provando que a cidadania britânica dependia da participação comprovada em regimentos de infantaria leve.",
        "Determinando que os estrangeiros residentes devam ser expulsos compulsoriamente durante anos de eleição.",
        "Mostrando que o pagamento de tributos dispensa os cidadãos de respeitarem as normas de trânsito urbano.",
        "B",
        "Locke explica por que quem não assinou o contrato original ainda deve obediência: ao usar a infraestrutura pública e viver sob a paz garantida pelas leis, o indivíduo dá seu consentimento tácito à ordem legal."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60 - Com Etapas 1 e 2)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a ruptura entre o paradigma da sociabilidade natural de Aristóteles (*zoon politikon*) e a concepção artificialista do Estado inaugurada pelo modelo jusnaturalista-contratualista (Hobbes e Locke): de que modo essa mutação redefiniu a relação entre o Indivíduo e a Comunidade política?",
        "Subordinando a vida dos cidadãos aos ditames corporativos das corporações monásticas medievais.",
        "Deslocando a Pólis do centro de gravidade originário anterior ao indivíduo para instituir o indivíduo singular, autônomo e portador de vontades e direitos subjetivos como o dado originário fundamental, sendo a comunidade política um instrumento artificial derivado, criado para servir aos interesses e à segurança dos indivíduos contratantes.",
        "Provando que as democracias antigas foram desenhadas por marinheiros mercantes que navegavam no mar Egeu.",
        "Determinando que os governantes devam realizar rituais divinatórios antes de convocarem assembleias deliberativas.",
        "Estabelecendo que as forças de segurança pública devam ser geridas por conselhos tribais de anciãos rurais.",
        "B",
        "- **Etapa 1:** Identificar o naturalismo comunitário aristotélico: na Grécia antiga, a cidade era anterior ao indivíduo; quem vivesse fora da pólis não era considerado plenamente humano, mas besta ou deus.\n- **Etapa 2:** Evidenciar a revolução individualista moderna do contrato: no contratualismo, o indivíduo livre e soberano no estado de natureza vem primeiro; o Estado é uma ferramenta criada artificialmente pelo pacto social para servir à vida e à proteção do cidadão."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "No capítulo XIV de O Leviatã, Thomas Hobbes estabelece a rigorosa distinção técnica entre o 'Direito de Natureza' (*Jus Naturale*) e a 'Lei de Natureza' (*Lex Naturalis*). Analise as implicações conceituais dessa distinção para a dinâmica da autopreservação humana.",
        "Autorizando os cidadãos civis a portarem armamentos pesados de guerra dentro de edifícios parlamentares.",
        "Definindo o Direito de Natureza como a liberdade irrestrita que cada homem possui de usar o seu poder particular como quiser para preservar a própria vida, e a Lei de Natureza como um preceito ou regra geral estabelecida pela razão que proíbe o homem de praticar o que destrói a sua própria vida ou privá-lo dos meios para preservá-la.",
        "Comprovando que as normas jurídicas das cidades britânicas foram copiadas de códigos agrários bizantinos.",
        "Determinando que os contratos civis de compra e venda devam ser autenticados em cerimônias religiosas solenes.",
        "Exigindo que os tribunais criminais municipais realizem julgamentos mediante leitura de pergaminhos antigos.",
        "B",
        "- **Etapa 1:** Definir a liberdade pura do Jus Naturale: no estado de natureza, o direito do indivíduo a todas as coisas não tem barreiras legais, permitindo inclusive o ataque físico preventivo contra terceiros.\n- **Etapa 2:** Definir a contenção racional da Lex Naturalis: a razão descobre que o direito ilimitado de todos a tudo anula a segurança de todos; a lei natural impõe o dever prudencial de buscar a paz e abrir mão da violência mútua em nome da sobrevivência."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Analise a famosa gravura da folha de rosto da primeira edição de O Leviatã (1651), desenhada por Abraham Bosse sob a supervisão direta de Thomas Hobbes: qual é a mensagem teórica expressa na representação do corpo do monarca gigante que empunha a espada e o báculo sobre a cidade pacificada?",
        "A celebração da superioridade estética das fortificações de pedra construídas durante a Idade Média.",
        "A personificação do Estado Soberano como um gigante artificial e imortal cujo corpo colossal é integralmente composto pelos milhares de corpos dos cidadãos que renunciaram aos seus poderes particulares para forjar a unidade suprema e indivisível da ordem pública temporal e espiritual.",
        "A demonstração de que os reis da Inglaterra deveriam governar utilizando vestimentas tecidas com lã de exportação.",
        "O regulamento de que as cidades litorâneas deveriam construir estátuas monumentais na entrada de seus portos.",
        "A comprovação de que as epidemias infecciosas eram causadas pela ausência de muralhas militares defensivas.",
        "B",
        "- **Etapa 1:** Interpretar os detalhes iconográficos da gravura: o torso e os braços do monarca são formados por cidadãos microscópicos olhando para o soberano, unificando a pluralidade anárquica em uma só pessoa representativa.\n- **Etapa 2:** Decifrar o simbolismo político dos atributos: a espada (monopólio da força civil) e o báculo (monopólio da doutrina espiritual) nas mãos do Leviatã proclamam a soberania indivisível e incontestável necessária para calar as guerras de religião."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Ao examinar a teoria lockeana do 'Trabalho como Título Originário de Propriedade', qual é o papel da chamada 'Cláusula de Sobra Suficiente e de Igual Qualidade' (*Lockean Proviso*) como imperativo ético da apropriação dos recursos da Terra?",
        "Exigir que todos os comerciantes de trigo doem metade de suas colheitas para armazéns da corte real.",
        "Estabelecer que a apropriação privada da terra e dos recursos naturais pelo esforço individual só é moralmente legítima e justa se for deixado o bastante e de igual qualidade para os demais seres humanos, proibindo o monopólio espoliador que condena outros à miséria ou à morte pela fome.",
        "Determinar que as ferramentas agrícolas devam ser confeccionadas com ligas de ferro fundido padronizadas.",
        "Comprovar que as propriedades rurais deveriam ser delimitadas exclusivamente por cercas de arbustos floridos.",
        "Afirmar que a fertilidade do solo agrícola decorre unicamente de orações realizadas durante a semeadura.",
        "B",
        "- **Etapa 1:** Resgatar o fundamento teológico-moral lockeano: Deus deu o mundo em comum aos homens para a sua subsistência coletiva; cercar um pedaço não pode tirar o pão do vizinho.\n- **Etapa 2:** Aplicar a cláusula restritiva (proviso): a apropriação legítima pressupõe abundância; enquanto houver terra fértil de sobra e igual para outros, o trabalho não lesa ninguém; essa cláusula é o alicerce moral contra o latifúndio especulativo e a espoliação predatória."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Em O Leviatã, Thomas Hobbes assevera: 'A soberania é a alma pública que dá vida e movimento ao Estado; se ela morrer, os membros são desgovernados por seu desfalecimento.' Como esse postulado fundamenta a proibição hobbesiana da 'Separação e Divisão dos Poderes' do Estado?",
        "Defendendo que as corporações religiosas devam administrar o orçamento das forças de cavalaria.",
        "Sustentando que dividir o poder supremo da república entre facções ou órgãos autônomos (como um Legislativo independente de um Executivo) divide a própria autoridade do Estado, semeando facções conflitantes e conduzindo fatalmente a sociedade de volta à anarquia e à guerra civil sangrenta.",
        "Provando que os parlamentos municipais devem aprovar normas orçamentárias por unanimidade absoluta.",
        "Exigindo que os tribunais criminais sejam presididos exclusivamente por generais reformados da infantaria.",
        "Determinando que os tratados diplomáticos devam ser redigidos em dialetos anglo-saxões medievais.",
        "B",
        "- **Etapa 1:** Diagnosticar o terror da soberania fragmentada: para Hobbes, onde dois poderes discordam e têm a espada, quem decide? Se houver um terceiro para arbitrar, este é o verdadeiro soberano; se não houver, a decisão é tomada pelas armas da guerra civil.\n- **Etapa 2:** Consagrar a tese da indivisibilidade: a soberania precisa ser concentrada em um único polo decisório (homem ou assembleia) para manter a coerção unificada, desarmar disputas de facções e blindar a estabilidade pública."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Considere a crítica de John Locke ao absolutismo em oposição direta a Thomas Hobbes: 'O fim maior e principal dos homens se unirem em repúblicas e se submeterem a governos é a preservação de sua propriedade; o que, no estado de natureza, é deficiente sob muitos aspectos.' Como essa formulação lockeana subverte o ideal absolutista de segurança cega?",
        "Proclamando que o bem-estar dos cidadãos decorre da submissão passiva a decretos imperiais secretos.",
        "Evidenciando que submeter-se a um governante absoluto e ilimitado não traz segurança verdadeira, mas apenas a troca de perigos difusos de homens comuns pela ameaça concentrada e incontrolável de um déspota armado que possui o poder de espoliar e assassinar súditos sem prestar contas a tribunal algum.",
        "Comprovando que os tratados de comércio internacional dispensam a existência de cláusulas de arbitragem jurídica.",
        "Determinando que as assembleias deliberativas das repúblicas devam aprovar códigos penais unânimes.",
        "Afirmando que a riqueza nacional depende da proibição da circulação de moedas de prata no mercado interno.",
        "B",
        "- **Etapa 1:** Confrontar a ilusão de segurança sob o Leviatã: Hobbes promete a paz sob um rei absoluto, mas Locke pergunta: quem protegerá o súdito contra a arbitrariedade, ganância e loucura do próprio rei?\n- **Etapa 2:** Concluir com a exigência liberal de legalidade: um governo legítimo precisa estar ele próprio submetido à lei que proclama; trocar o estado de natureza pelo absolutismo é como fugir do lobo para se jogar na boca do leão."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Analise o paradoxo da 'Inconveniência de Ser Juiz em Causa Própria' formulado por John Locke como o principal motivo da saída do Estado de Natureza. De que maneira esse argumento funda a exigência da imparcialidade judiciária no moderno Estado Democrático de Direito?",
        "Autorizando os litigantes em tribunais civis a nomearem seus próprios parentes para julgar recursos judiciais.",
        "Demonstrando que, quando o próprio lesado atua como investigador, juiz e carrasco de uma ofensa, a parcialidade, a cegueira afetiva, o rancor e a sede de vingança desvirtuam a justiça, multiplicando as violências desmedidas e convertendo a desavença particular em um estado de guerra desregrado, o que exige tribunais impessoais de magistrados imparciais e leis preestabelecidas.",
        "Comprovando que os códigos de leis escritas eram dispensados pelos cidadãos das treze colônias britânicas.",
        "Exigindo que as audiências judiciais sejam suspensas durante os períodos de festas carnavalescas urbanas.",
        "Determinando que os jurados de tribunais populares devam ser escolhidos exclusivamente entre sacerdotes de ordens monásticas.",
        "B",
        "- **Etapa 1:** Revelar a falha psicológica do juiz próprio: o homem não tem distanciamento ético para avaliar sua própria querela; o egoísmo o faz enxergar uma ofensa leve como crime mortal e seus próprios atos abusivos como virtude.\n- **Etapa 2:** Fundar a jurisdição estatal independente: a saída civilizada da barbárie é transferir o poder de punir para um terceiro neutro e desinteressado (o juiz estatal sob leis públicas), garantindo o devido processo legal e a paz na república."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "No capítulo XXI de O Leviatã, Hobbes formula a célebre definição de 'Liberdade dos Súditos': 'A liberdade dos súditos reside apenas nas coisas que, ao regular suas ações, o soberano omitiu.' Analise a profundidade dessa tese para a teoria jurídica moderna do Princípio da Legalidade.",
        "Proclamando que os súditos britânicos eram livres para desobedecer a ordens emanadas de tribunais penais.",
        "Fundamentando o cânone moderno de que o cidadão desfruta de plena liberdade de ação em tudo aquilo que a lei civil pública expressamente não proíbe, estabelecendo o império normativo das leis como demarcação objetiva entre a ordem coercitiva do Estado e a esfera de autonomia civil particular.",
        "Provando que as ordenações jurídicas das monarquias europeias deviam ser redigidas em versos cômicos rimados.",
        "Exigindo que as forças policiais da capital realizem revistas domiciliares noturnas sem ordem judicial.",
        "Determinando que os cidadãos devam assinar contratos anuais de fidelidade aos comandantes de regimento.",
        "B",
        "- **Etapa 1:** Interpretar o silêncio da lei como esfera de liberdade em Hobbes: onde o soberano não legislou (comércio particular, escolha da profissão, residência familiar, educação dos filhos), o súdito age conforme seu desejo.\n- **Etapa 2:** Conectar com o Direito Constitucional moderno: essa tese é a certidão de batismo do princípio liberal da legalidade (Art. 5º, II da CF/88): 'ninguém será obrigado a fazer ou deixar de fazer algo senão em virtude de lei'; a liberdade civil é o espaço preservado pela lei."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Analise a crítica sociológica que autores contemporâneos dirigem à teoria da 'Propriedade Privada pelo Trabalho' de John Locke: de que modo a legitimação da apropriação originária da terra serviu historicamente para justificar a expropriação violenta de territórios indígenas nas Américas e o cercamento dos campos (*Enclosures*) na Inglaterra mercantil?",
        "Demonstrando que os povos originários das Américas foram acolhidos como sócios paritários em companhias mercantis britânicas.",
        "Evidenciando que a definição lockeana de trabalho legítimo baseava-se na agricultura intensiva, no cercamento de terras e na extração comercial europeia, permitindo classificar os modos de vida caçadores, coletores e de posse comunal das terras indígenas como terras incultas e vazias (terra nullius), legitimando juridicamente a invasão e espoliação colonial de territórios ancestrais.",
        "Comprovando que os tratados de paz firmados entre colonizadores e nativos foram redigidos em línguas maias clássicas.",
        "Determinando que as terras comunais britânicas deveriam ser reservadas exclusivamente para santuários florestais alpinos.",
        "Afirmando que a expansão colonial decorreu exclusivamente de desvios orçamentários cometidos por governadores ultramarinos.",
        "B",
        "- **Etapa 1:** Identificar o viés eurocêntrico da teoria do valor-trabalho: Locke associava trabalho produtivo ao cercamento agrário e cultivo comercial aos moldes ingleses; a terra sem cerca era considerada terra inculta e desperdiçada.\n- **Etapa 2:** Expor o uso colonial da teoria: colonizadores britânicos usaram o Segundo Tratado para desapropriar povos indígenas, alegando que, por não lavrarem o solo no modelo mercantil, não tinham propriedade real, desvelando a contradição imperial do liberalismo inicial."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Ao examinar a relação entre o Contratualismo e a Teoria do Monopólio da Violência Legítima formulada por Max Weber no século XX, como a doutrina da 'Espada Soberana' de Hobbes antecipa a definição moderna de Estado?",
        "Afirmando que o Estado contemporâneo deve descentralizar as forças armadas em cooperativas de voluntários.",
        "Consagrando a constatação pioneira de que uma ordem política só existe como Estado soberano se detiver com exclusividade e eficácia o controle dos instrumentos físicos de coerção e coação armada sobre um determinado território, sem concorrentes internos armados que desafiem as suas leis civis.",
        "Provando que as monarquias constitucionais modernas operam sem necessidade de delegacias de polícia.",
        "Exigindo que os tribunais de segurança nacional sejam presididos exclusivamente por ministros paroquiais.",
        "Determinando que a arrecadação de tributos aduaneiros seja terceirizada a conselhos de marinheiros fluviais.",
        "B",
        "- **Etapa 1:** Reconhecer a intuição hobbesiana fundamental: se outros grupos na cidade tiverem armas para impor sua própria lei, não há Estado, mas guerra civil latente e anarquia.\n- **Etapa 2:** Articular com a ciência social de Weber: o Estado moderno caracteriza-se precisamente pela reinvindicação bem-sucedida do monopólio do uso legítimo da força física; foi Hobbes quem primeiro demonstrou que sem esse monopólio soberano a paz civil é impossível."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Considere o problema da 'Dissolução do Governo' em John Locke: qual distinção crucial o autor estabelece entre a 'Dissolução da Sociedade' e a 'Dissolução do Governo', e qual é o impacto dessa distinção para a estabilidade constitucional durante revoluções?",
        "Locke afirma que toda vez que um governo é destituído pelos cidadãos, a sociedade regressa imediatamente à barbárie e à selvageria desordenada.",
        "Locke estabelece que a dissolução do governo (provocada pela tirania ou quebra do pacto de confiança) não destrói a sociedade política civil constituída, mantendo o povo unido como corpo coletivo soberano plenamente capacitado a eleger e instituir um novo Poder Legislativo sem cair no caos anárquico do estado de natureza.",
        "Locke defende que a sociedade só se dissolve quando ocorre a invasão militar de corsários piratas em cidades do interior.",
        "Locke argumenta que a dissolução de uma assembleia exige o cancelamento de todos os contratos civis de casamento.",
        "Locke sustenta que a destituição de ministros reais depende de autorizações concedidas por tribunais papais romanos.",
        "B",
        "- **Etapa 1:** Superar o terror hobbesiano da anarquia: Hobbes sustentava que derrubar o soberano destruía tudo, jogando a população de volta à guerra de todos contra todos.\n- **Etapa 2:** Fundar a maturidade republicana em Locke: a sociedade foi criada antes do governo; se o governante vira tirano, apenas o governo é desfeito; o povo continua organizado como sociedade soberana, podendo instituir um novo parlamento com serenidade cívica."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Analise a tensão dramática na teoria de Hobbes no caso limite em que um súdito é legalmente condenado à pena de morte pelo soberano: por que, segundo o próprio Hobbes, esse condenado readquire legitimamente o 'Direito Natural de Resistência Física' e fuga contra os carrascos do Estado?",
        "Porque o condenado à morte adquire uma licença especial lavrada em pergaminhos pelo comandante de regimento.",
        "Porque o pacto social foi celebrado unicamente com a finalidade de proteger e preservar a própria vida biológica do contratante; logo, quando o soberano ordena a sua execução física, o vínculo contratual deixa de operar para aquele indivíduo em particular, que retorna instantaneamente ao estado de natureza em relação ao soberano e tem o direito natural sagrado de lutar por sua sobrevivência.",
        "Porque a legislação civil da Inglaterra exigia que os condenados à forca disputassem torneios de corrida descalços.",
        "Porque os tribunais criminais de Londres eram presididos por juízes que não sabiam ler cartas latinas antigas.",
        "Porque as execuções capitais deveriam ser precedidas por consultas oraculares sobre o movimento dos mares.",
        "B",
        "- **Etapa 1:** Compreender a lógica de sustentação do pacto hobbesiano: ninguém pode alienar o direito de se defender da morte, pois ninguém renuncia a nada exceto na esperança de um bem para si (a sua própria vida).\n- **Etapa 2:** Concluir com a fratura radical da soberania no cadafalso: o soberano tem o direito legítimo de tentar matar o criminoso em defesa da ordem pública, mas o condenado tem o direito natural incontestável de resistir e fugir; o pacto entre eles ruiu."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "Em sua crítica ao pensamento contratualista, o filósofo escocês David Hume (1711-1776) argumentou que quase todos os governos históricos reais nasceram de guerras de conquista militar, usurpação e violência física, e não de pactos contratuais voluntários pacíficos. De que maneira os teóricos do contratualismo contemporâneo respondem a essa objeção histórica?",
        "Concordando que os contratos sociais foram assinados exclusivamente por corporações marítimas de mercadores.",
        "Demonstrando que o contrato social nunca teve a pretensão de ser um relato histórico arqueológico do passado, mas sim um modelo conceitual normativo e contrafactual formulado para responder à questão da 'Legitimidade Ética e Política': quais normas e termos de convivência cidadãos livres e racionais aceitariam em consenso para justificar a sua obediência à autoridade do Estado?",
        "Provando que as constituições modernas foram redigidas por soldados camponeses após revoltas de fome.",
        "Afirmando que a legitimidade dos governantes depende unicamente de ritos de coroação e unção sagrada por bispos.",
        "Defendendo que as disputas de poder devem ser resolvidas mediante a abolição definitiva de tribunais constitucionais.",
        "B",
        "- **Etapa 1:** Acolher a precisão do fato empírico de Hume: na história empírica real, a espada, a usurpação e a pilhagem criaram a maioria das fronteiras e dos reinos mundiais.\n- **Etapa 2:** Resgatar a força normativa transcendental do contrato: o contratualismo não narra o passado, projeta a justiça ideal; ele nos oferece a régua moral para julgar o presente: 'este governo respeita os direitos que homens racionais e livres pactuariam?' Se não respeita, é tirania ilegítima."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "De que modo a filosofia política de John Locke influenciou a formulação dos 'Três Poderes' desenvolvida posteriormente pelo filósofo iluminista francês Barão de Montesquieu em O Espírito das Leis (1748)?",
        "Determinando que o Poder Judiciário fosse subordinado a comandos de guarnições militares costeiras.",
        "Evoluindo a separação funcional originária de Locke (Legislativo, Executivo e Federativo) para o clássico sistema tripartite autônomo e equilibrado entre Legislativo, Executivo e Judiciário, regulado pelo mecanismo de freios e contrapesos (*checks and balances*) para impedir que qualquer poder se torne tirânico.",
        "Exigindo que as leis penais fossem elaboradas por comitês secretos de banqueiros e embaixadores estrangeiros.",
        "Provando que a divisão de poderes provoca o encarecimento orçamentário dos salários de servidores públicos.",
        "Afirmando que os magistrados de tribunais superiores deveriam ser nomeados exclusivamente por reis da Europa.",
        "B",
        "- **Etapa 1:** Resgatar a intuição pioneira de Locke: o perigo da concentração de quem faz a lei ser quem a executa, criando a cisão entre o Legislativo (elaborador da norma) e o Executivo (aplicador).\n- **Etapa 2:** Conectar com a formulação madura de Montesquieu: Montesquieu erige o Judiciário como terceiro poder independente e funda a teoria dos freios e contrapesos; o poder freia o poder, consagrando a arquitetura institucional das democracias constitucionais modernas."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Analise a relação entre o pessimismo antropológico de Hobbes e o realismo das agências contemporâneas de controle, inteligência e segurança pública: por que as instituições de persecução penal operam sob o pressuposto implícito de que 'a ausência de fiscalização estimula a transgressão'?",
        "Porque as leis cívicas modernas exigem que todos os cidadãos prestem juramentos matinais de honestidade.",
        "Porque a criminologia e o direito penal moderno acolhem a advertência hobbesiana de que a moral individual desprovida de sanções críveis e fiscalização eficaz cede facilmente à tentação do ganho ilícito, exigindo aparatos impessoais de controle e dissuasão para desestimular a corrupção e preservar a integridade da ordem pública.",
        "Porque os tribunais criminais municipais foram criados para satisfazer a vaidade oratória de promotores públicos.",
        "Porque a legislação civil impõe o uso de armaduras de ferro forjado por todos os guardas prisionais de plantão.",
        "Porque as agências de controle estatal devem terceirizar suas perícias técnicas a companhias de navegação fluvial.",
        "B",
        "- **Etapa 1:** Reconhecer o princípio da dissuasão hobbesiano: o homem não cumpre a regra por santidade espontânea, mas pelo cálculo racional das consequências e custos do descumprimento.\n- **Etapa 2:** Projetar na gestão pública moderna: sistemas de compliance, controladorias e auditorias operam com a premissa de que a confiança ingênua convida ao abuso; o controle impessoal e a certeza da sanção garantem a probidade do Estado e a paz coletiva."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Ao examinar a teoria da 'Tolerância Religiosa' em John Locke, qual é a grave restrição que o filósofo impõe em relação aos 'Ateus' e aos 'Católicos' (*Papistas*) no contexto do século XVII, e como a Filosofia Política contemporânea supera esses limites históricos?",
        "Locke defendia que os católicos deveriam pagar tributos dobrados sobre o cultivo de trigo no campo.",
        "Locke negava tolerância aos católicos porque estes deviam lealdade política e militar a um soberano estrangeiro (o Papa de Roma), e aos ateus porque acreditava que quem não teme a Deus não pode prestar juramentos válidos; limites que o constitucionalismo democrático contemporâneo superou ao consagrar a liberdade irrestrita de consciência e a laicidade plena do Estado.",
        "Locke propunha que os ateus fossem condenados a trabalhos forçados em embarcações de pesca oceânica.",
        "Locke sustentava que as congregações religiosas deveriam ser chefiadas exclusivamente por generais reformados.",
        "Locke exigia que todas as cerimônias de batismo fossem supervisionadas por magistrados de tribunais civis.",
        "B",
        "- **Etapa 1:** Contextualizar historicamente as exceções de Locke: no século XVII das guerras de religião, o católico era visto como súdito do rival geopolítico da Inglaterra (o Vaticano), e o juramento perante a Bíblia era o único laço que garantia a verdade nos tribunais.\n- **Etapa 2:** Avaliar a evolução da cidadania laica: o pensamento democrático contemporâneo depurou essas amarras históricas; hoje a liberdade de crença e de não crença é direito universal inalienável, e o Estado laico acolhe crentes e ateus sob a mesma dignidade jurídica."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Considere a antítese conceitual estrutural entre Thomas Hobbes e John Locke: enquanto o primeiro sustenta que a renúncia aos direitos em favor do soberano absoluto é o único caminho para a paz contra a anarquia, o segundo afirma que o poder político só é legítimo sob consentimento condicionado e respeito aos direitos naturais. Analise como esse confronto funda os dois grandes ramos do pensamento político moderno sobre a autoridade do Estado.",
        "Comprovando que os tratados internacionais de navegação marítima dependem da aprovação de conselhos monásticos.",
        "Evidenciando o embate histórico e teórico entre o absolutismo securitário (onde a paz é obtida pela alienação da liberdade a um soberano absoluto acima das leis civis) e o constitucionalismo liberal (onde o poder do Estado é limitado pelo império da lei, pela divisão de poderes e pela soberania do povo com direito sagrado de resistência à tirania).",
        "Determinando que os governantes devam prestar juramentos de fidelidade militar a companhias de comércio naval.",
        "Exigindo que as disputas entre cidadãos sobre divisas de imóveis devam ser resolvidas mediante duelos de espada.",
        "Provando que as constituições modernas devem prever o fechamento de parlamentos durante períodos de estiagem no campo.",
        "B",
        "- **Etapa 1:** Analisar o modelo hobbesiano do Leviatã: a garantia de ordem e proteção à vida exige a concentração absoluta do poder soberano, sem possibilidade de contestação legal pelos súditos.\n- **Etapa 2:** Analisar a resposta liberal lockeana: o poder não pode ser absoluto nem pairar acima das leis; o governo civil é um pacto fiduciário de consentimento voltado a proteger os direitos naturais à vida, à liberdade e à propriedade, sob pena de legítima revolta popular."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "Analise a relação entre o conceito hobbesiano de 'Guerra de Todos contra Todos' e o dilema contemporâneo da 'Segurança Pública versus Liberdades Individuais' no contexto da vigilância digital em massa e estados policiais:",
        "Comprovando que os cidadãos modernos preferem viver em anarquia sem qualquer tecnologia de comunicação.",
        "Demonstrando que o medo disseminado da violência urbana e do terrorismo internacional é frequentemente manipulado por governos contemporâneos para justificar o fortalecimento de aparatos hipertrofiados do Leviatã estatal (como câmeras de reconhecimento facial, espionagem digital e repressão armada), levando os cidadãos a sacrificarem direitos civis fundamentais em troca da promessa de segurança física.",
        "Provando que as leis penais contemporâneas devem ser aplicadas unicamente em dias de solstício de verão.",
        "Determinando que as empresas de tecnologia digital devem fechar seus servidores em períodos eleitorais municipais.",
        "Afirmando que o uso de redes de internet dispensa a existência de órgãos de inteligência e segurança pública.",
        "B",
        "- **Etapa 1:** Atualizar o mecanismo hobbesiano do medo: quando a sociedade é tomada pelo pânico da criminalidade ou da violência, o instinto primário de sobrevivência clama pela autoridade firme que prometa ordem a qualquer preço.\n- **Etapa 2:** Diagnosticar o perigo totalitário contemporâneo: o Leviatã digital moderno oferece segurança vigiando cada passo do cidadão; a vigilância excessiva sufoca a liberdade democrática; o desafio da cidadania reside em exigir segurança sem aceitar o arbítrio despótico."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Ao examinar a formulação de John Locke sobre o 'Consentimento dos Governados', de que modo essa tese estabelece o alicerce fundamental para a soberania do 'Voto Popular' e da 'Democracia Representativa' moderna?",
        "Autorizando os governantes eleitos a fecharem o Congresso Nacional sempre que houver greves sindicais.",
        "Estabelecendo que nenhuma autoridade política é legítima em si mesma por tradição, nascimento nobre ou poderio bélico, decorrendo exclusivamente da delegação temporária e revogável de poder conferida pelos cidadãos através do sufrágio periódico e da representação parlamentar legalmente instituída.",
        "Comprovando que os deputados de assembleias legislativas devem exercer seus mandatos de forma vitalícia e hereditária.",
        "Exigindo que os eleitores depositem seus votos em urnas confeccionadas exclusivamente com cerâmica vermelha.",
        "Determinando que os cidadãos devam prestar juramentos de fidelidade militar a líderes de partidos políticos.",
        "B",
        "- **Etapa 1:** Desconstruir a legitimidade arcaica: antes de Locke, reis mandavam porque tinham sangue nobre, espada ou bênção papal; o povo era súdito passivo sem direito a voz.\n- **Etapa 2:** Fundar a democracia representativa: para Locke, o governo só tem legitimidade se houver consentimento livre dos governados; essa intuição funda as eleições periódicas, o voto e a responsabilidade dos governantes perante a soberania popular."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Síntese conclusiva do Capítulo 19: por que a compreensão crítica comparada entre Thomas Hobbes e John Locke é uma ferramenta indispensável para que o estudante do Ensino Médio atue com consciência cidadã no Século XXI?",
        "Porque o estudo desses filósofos ensina técnicas de manipulação partidária e propaganda ideológica eleitoral.",
        "Porque instrumentaliza a juventude com as categorias mestras da modernidade política para discernir a importância da estabilidade das leis e da ordem pública (Hobbes) sem jamais renunciar à vigilância ativa na defesa intransigente dos direitos humanos, das liberdades civis, da divisão de poderes e da resistência democrática contra qualquer forma de opressão autoritária (Locke).",
        "Porque estabelece a obrigatoriedade da inclusão de línguas britânicas arcaicas em vestibulares nacionais.",
        "Porque comprova que os conflitos políticos contemporâneos perdem a validade perante inovações robóticas fabris.",
        "Porque determina que as escolas de ensino médio devam substituir o estudo de filosofia por treinos de tiro ao alvo.",
        "B",
        "- **Etapa 1:** Integrar as duas faces da moeda política moderna: de Hobbes aprendemos que a anarquia é devastadora e que sem uma ordem legal firme a vida torna-se um inferno violento.\n- **Etapa 2:** Coroar com o imperativo liberal e democrático de Locke: aprendemos que a ordem não pode custar a alma da liberdade; a cidadania madura do jovem exige defender o Estado de Direito que protege a comunidade, mantendo acesa a chama do direito de resistir a qualquer tirano."
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
    linhas.append('eixo: "Eixo III: Filosofia Política, Poder, Resistência e Necropolítica"')
    linhas.append('capitulo: "Capítulo 19: O Contratualismo Moderno: Hobbes e Locke"')
    linhas.append('objeto_de_conhecimento: "O modelo jusnaturalista-contratualista, o estado de natureza, o pacto de submissão e o absolutismo em Hobbes, os direitos naturais, o governo representativo e o direito de resistência em Locke"')
    linhas.append('ebook_fonte: "em-fil-c19-contratualismo-hobbes-locke.md"')
    linhas.append('habilidades:')
    linhas.append('  - "EM13CHS101"')
    linhas.append('  - "EM13CHS102"')
    linhas.append('  - "EM13CHS601"')
    linhas.append('  - "EM13CHS602"')
    linhas.append('  - "EM13CHS603"')
    linhas.append('total_exercicios: 60')
    linhas.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    linhas.append("---\n")

    linhas.append("# Lista de Exercícios: O Contratualismo Moderno: Hobbes e Locke\n")

    for q in questoes_rotacionadas:
        num, hab, dif, enunc, a, b, c, d, e_alt, gab, resol = q
        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-19-contratualismo-hobbes-locke -->"
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
    linhas.append("- HOBBES, Thomas. *Leviatã: ou matéria, forma e poder de um Estado eclesiástico e civil*. Tradução de João Paulo Monteiro e Maria Beatriz Nizza da Silva. São Paulo: Martins Fontes, 2003.")
    linhas.append("- LOCKE, John. *Segundo tratado sobre o governo civil: ensaio sobre a verdadeira origem, extensão e fim do governo civil*. Tradução de Magda Lopes e Marisa Lobo da Costa. Petrópolis: Vozes, 1994.")
    linhas.append("- BOBBIO, Norberto. *Thomas Hobbes*. Tradução de Carlos Nelson Coutinho. Rio de Janeiro: Campus, 1991.")
    linhas.append("- WEFFORT, Francisco C. (Org.). *Os clássicos da política: Maquiavel, Hobbes, Locke, Montesquieu, Rousseau, O Federalista*. São Paulo: Ática, 2001. v. 1.")
    linhas.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")

    conteudo_md = "\n".join(linhas) + "\n"

    # Salvar em temp_draft.md
    with open("temp_draft.md", "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"Rascunho salvo em temp_draft.md ({len(conteudo_md.encode('utf-8'))} bytes)")

    # Acionar o validador Educamob
    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-19-contratualismo-hobbes-locke/ebooks/em-fil-c19-contratualismo-hobbes-locke-exercicios.md"
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
        print("\n[SUCESSO TOTAL] Cap 19 validado e homologado com Exit Code 0!")

if __name__ == "__main__":
    main()
