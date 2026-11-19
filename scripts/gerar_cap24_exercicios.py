# -*- coding: utf-8 -*-
"""
Gerador e Validador de Exercícios para o Capítulo 24 de Filosofia EM:
O Quilombismo e a Resistência Negra: Abdias do Nascimento
Objeto: cap-24-quilombismo-resistencia-abdias-nascimento
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
        "Analise a multifacetada trajetória de Abdias do Nascimento (1914-2011), formulador da teoria política do Quilombismo:",
        "General militar monarquista que combateu na Guerra do Paraguai.",
        "Poeta, dramaturgo, artista plástico, professor universitário, deputado federal constituinte e senador da República.",
        "Comerciante cafeeiro paulista que defendeu a manutenção da monarquia absolutista.",
        "Engenheiro civil responsável pela pavimentação das primeiras rodovias federais.",
        "Magistrado de tribunais consulares marítimos em portos do Atlântico Norte.",
        "B",
        "Abdias do Nascimento foi um dos maiores líderes intelectuais e ativistas do Brasil: fundou o TEN, combateu o racismo no Parlamento e teorizou o Quilombismo no mundo acadêmico internacional."
    ))

    questoes_brutas.append((
        2, "EM13CHS102", "basico",
        "Em 1944, no Rio de Janeiro, qual companhia cultural inovadora foi fundada por Abdias do Nascimento para combater o 'blackface' e colocar atores negros como protagonistas nos palcos?",
        "O Conservatório Imperial de Canto Lírico Italiano.",
        "O Teatro Experimental do Negro (TEN).",
        "A Companhia Teatral Portuguesa de Autos Sacramentais.",
        "A Associação de Bailarinos Clássicos de Petrópolis.",
        "O Grêmio Recreativo de Operários Ferroviários da Leopoldina.",
        "B",
        "O Teatro Experimental do Negro (TEN) revolucionou as artes cênicas brasileiras em 1944, superando a vergonha do blackface e formando a primeira geração de grandes atores e dramaturgos negros do país."
    ))

    questoes_brutas.append((
        3, "EM13CHS601", "basico",
        "Em que consiste a tese política e civilizatória central do conceito de 'Quilombismo' formulado por Abdias do Nascimento?",
        "A proposta de isolamento territorial definitivo de comunidades rurais em cavernas montanhosas.",
        "A ressignificação do quilombo como filosofia política permanente, projeto de sociedade humanista, socialista, comunitária e antirracista para o Brasil e a diáspora pan-africana.",
        "A defesa do retorno do modelo econômico imperial de monoculturas cafeeiras voltadas à exportação.",
        "A exigência de subordinação das decisões comunitárias a conselhos de bispos eclesiásticos.",
        "A imposição de tributos extraordinários sobre a comercialização de mandioca e milho.",
        "B",
        "Quilombismo não é museu colonial: é um projeto civilizatório contemporâneo que propõe reforma agrária popular, uso comum da terra, democracia participativa e igualdade substantiva contra o capitalismo predatório."
    ))

    questoes_brutas.append((
        4, "EM13CHS602", "basico",
        "Em sua obra clássica de 1978, O Genocídio do Negro Brasileiro, qual narrativa oficial do Estado brasileiro Abdias do Nascimento desmascara implacavelmente?",
        "A tese de que o território nacional brasileiro foi colonizado exclusivamente por navegadores holandeses.",
        "O 'Mito da Democracia Racial', que alegava uma escravidão branda, cordial e a inexistência de conflito racial no Brasil.",
        "A teoria de que as ferrovias a vapor foram construídas unicamente com investimentos britânicos.",
        "A afirmação de que a culinária sertaneja foi inventada por cozinheiros de cortes imperiais austríacas.",
        "A alegação de que a abolição da escravidão ocorreu por votação unânime de lavradores camponeses.",
        "B",
        "Abdias demoliu a fábula da democracia racial: o Brasil nunca foi um paraíso cordial; a escravidão foi brutal e o racismo foi mascarado para desmobilizar os negros e perpetuar o domínio branco."
    ))

    questoes_brutas.append((
        5, "EM13CHS603", "basico",
        "Como Abdias do Nascimento interpreta as políticas estatais de incentivo financeiro à imigração europeia implementadas pelo Brasil a partir do final do século XIX?",
        "Como um plano desinteressado para incentivar o intercâmbio de técnicas de carpintaria naval.",
        "Como uma política calculada de branqueamento da população, visando à diluição e ao extermínio biológico e cultural da população negra no país.",
        "Como uma medida voltada exclusivamente para a criação de academias de ginástica olímpica.",
        "Como um acordo diplomático firmado para padronizar os uniformes de soldados de cavalaria.",
        "Como uma estratégia para conter o avanço do cultivo de cana-de-açúcar no litoral nordestino.",
        "B",
        "O Estado financiou a vinda de milhões de europeus com o objetivo confesso de eugenia e branqueamento: esperavam diluir o sangue negro até apagar a raça negra do mapa em poucas gerações."
    ))

    questoes_brutas.append((
        6, "EM13CHS101", "basico",
        "Qual experiência histórica pioneira do século XVII é resgatada por Abdias do Nascimento como a matriz originária do Quilombismo?",
        "A Guerra de Canudos travada no sertão baiano no final do século XIX.",
        "A República dos Palmares (o Quilombo dos Palmares), que floresceu por quase cem anos na Serra da Barriga.",
        "A Revolta da Vacina ocorrida na cidade do Rio de Janeiro em 1904.",
        "A Inconfidência Mineira liderada por poetas e mineradores em Ouro Preto.",
        "A Cabanagem travada nas províncias fluviais da Amazônia brasileira.",
        "B",
        "Palmares (1595-1695) foi a primeira república livre e pluricultural das Américas: uma confederação de cidades livres que resistiu por quase um século ao cerco militar de portugueses e holandeses."
    ))

    questoes_brutas.append((
        7, "EM13CHS102", "basico",
        "Por que Palmares não deve ser compreendido como um enclave exclusivo de pessoas negras, de acordo com as pesquisas de Abdias e Clóvis Moura?",
        "Porque a comunidade era administrada por magistrados enviados anualmente pela Coroa de Lisboa.",
        "Porque Palmares era uma sociedade aberta e pluricultural, que acolhia generosamente indígenas espoliados, brancos pobres, desertores militares e perseguidos pela Inquisição.",
        "Porque a população do quilombo dedicava-se unicamente ao trabalho de extração de madeira para exportação.",
        "Porque as decisões políticas dependiam da aprovação de sacerdotes missionários jesuítas.",
        "Porque os habitantes eram obrigados a pagar tributos em ouro para a Companhia das Índias Ocidentais.",
        "B",
        "Palmares foi refúgio fraterno para todos os oprimidos da colônia: acolheu indígenas sem-terra, brancos pobres fugitivos e judeus perseguidos; foi uma autêntica república de liberdade e solidariedade humana."
    ))

    questoes_brutas.append((
        8, "EM13CHS601", "basico",
        "Quais foram as grandes lideranças históricas que comandaram a resistência e a organização da República dos Palmares?",
        "Tiradentes, Joaquim Nabuco e José Bonifácio de Andrada e Silva.",
        "Ganga Zumba, Dandara e Zumbi dos Palmares.",
        "Duque de Caxias, Bento Gonçalves e Giuseppe Garibaldi.",
        "Padre Vieira, Gregório de Matos e Pero Vaz de Caminha.",
        "Marechal Deodoro da Fonseca, Floriano Peixoto e Rui Barbosa.",
        "B",
        "Ganga Zumba articulou a confederação dos mocambos, Dandara liderou a guerrilha e a agricultura livre, e Zumbi comandou a resistência inabalável contra o exército mercenário colonial até seu assassinato em 1695."
    ))

    questoes_brutas.append((
        9, "EM13CHS602", "basico",
        "Como o Quilombismo concebe a posse e a gestão da Terra e dos meios de produção?",
        "Como propriedade privada individual que deve ser leiloada para fundos de investimento especulativo.",
        "Como bem sagrado de uso comum e comunitário, onde a terra pertence à coletividade que nela trabalha e a economia se funda no cooperativismo e na soberania alimentar.",
        "Como posse exclusiva da Coroa governamental que cobra rendas senhoriais compulsórias dos camponeses.",
        "Como concessão estatal precária outorgada unicamente a empresas agropecuárias de grande porte.",
        "Como patrimônio administrado por comissões de mercadores estrangeiros de algodão.",
        "B",
        "No Quilombismo a terra não é mercadoria de especulação: é solo sagrado de sustento comum; a produção é gerida em economia solidária, garantindo que ninguém passe fome e todos colham os frutos do trabalho."
    ))

    questoes_brutas.append((
        10, "EM13CHS603", "basico",
        "Qual é o modelo de tomada de decisões políticas defendido pela proposta do Quilombismo?",
        "O domínio monárquico hereditário chefiado por imperadores coroados em templos solenes.",
        "A democracia participativa e o poder popular, inspirados em conselhos comunitários de base com escuta atenta dos mais velhos (griôs) e igualdade de gênero.",
        "A tecnocracia burocrática exercida exclusivamente por banqueiros e consultores financeiros privados.",
        "O governo oligárquico controlado pelos maiores proprietários de terras latifundiárias do país.",
        "A administração distrital militar chefiada por generais de infantaria armada de carreira.",
        "B",
        "O poder quilombista é circular e comunitário: assembleias de base decidem os rumos coletivos, respeitando a sabedoria ancestral dos mais velhos e garantindo voz e poder iguais às mulheres."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "De que modo a relação com a Natureza e a Espiritualidade é concebida no pensamento quilombista?",
        "Como recursos inanimados que devem ser explorados até a exaustão para gerar superávits comerciais.",
        "Como simbiose sagrada e harmônica em que os seres humanos integram o ecossistema cósmico, cultuando os Orixás e as forças vivas das matas e das águas com respeito inviolável.",
        "Como áreas desertas que precisam ser desmatadas para a construção de rodovias pavimentadas.",
        "Como propriedades subordinadas unicamente às leis de mercado de commodities agropecuárias.",
        "Como reservas minerais que devem ser concedidas sem restrições a companhias mineradoras estrangeiras.",
        "B",
        "A cosmovisão quilombista integra homem e natureza: o rio, a folha e o vento são sagrados e neles habitam os Orixás; destruir a floresta ou poluir as águas é um sacrilégio ético e espiritual intolerável."
    ))

    questoes_brutas.append((
        12, "EM13CHS102", "basico",
        "Qual movimento político internacional articula-se organicamente ao Quilombismo de Abdias do Nascimento?",
        "O Tratado da Santa Aliança entre monarquias absolutistas da Europa central.",
        "O Pan-Africanismo, que preconiza a união solidária e a libertação de todos os povos de ascendência africana do planeta contra o imperialismo e o racismo.",
        "A Liga Hanseática de corporações mercantis de portos do mar Báltico.",
        "O Pacto de Varsóvia entre nações do bloco militar do leste europeu.",
        "A Doutrina Monroe de hegemonia unilateral dos Estados Unidos sobre a América Latina.",
        "B",
        "Abdias integrou o Quilombismo ao Pan-Africanismo de Du Bois, C.L.R. James e Kwame Nkrumah: a luta do negro brasileiro é a mesma luta dos povos de África e do Caribe por soberania e dignidade."
    ))

    questoes_brutas.append((
        13, "EM13CHS601", "basico",
        "Qual artigo constitucional histórico da Carta Magna de 1988 consagrou formalmente o direito territorial das comunidades quilombolas brasileiras?",
        "O Artigo 5º que regulamenta a emissão de títulos de patentes industriais de invenção.",
        "O Artigo 68 do Ato das Disposições Constitucionais Transitórias (ADCT), que reconhece a propriedade definitiva das terras aos remanescentes dos quilombos.",
        "O Artigo 142 que define as atribuições de defesa externa e fronteiras das Forças Armadas.",
        "O Artigo 170 que estabelece as regras de tributação sobre exportações de grãos agrícolas.",
        "O Artigo 225 que autoriza o leilão público de áreas florestais para exploração de madeira.",
        "B",
        "Conquista gigante de Abdias e do Movimento Negro na Constituinte: o Artigo 68 do ADCT determinou que o Estado brasileiro emita os títulos definitivos de propriedade para as comunidades quilombolas."
    ))

    questoes_brutas.append((
        14, "EM13CHS602", "basico",
        "Em 1983, em seu mandato como Deputado Federal constituinte, qual pioneirismo histórico Abdias do Nascimento protagonizou no Parlamento brasileiro?",
        "Apresentou o primeiro projeto de lei de ação afirmativa e cotas raciais para negros nas universidades e serviços públicos (PL 1.332/1983).",
        "Defendeu o retorno do pagamento de indenizações aos antigos senhores proprietários de escravos.",
        "Propôs a extinção de todos os feriados civis que celebravam personalidades populares brasileiras.",
        "Reivindicou a privatização de todas as instituições públicas federais de ensino superior.",
        "Sugeriu a obrigatoriedade do ensino de língua latina clássica em creches municipais comunitárias.",
        "A",
        "Trinta anos antes da Lei de Cotas de 2012, Abdias subiu à tribuna da Câmara em 1983 e protocolou o primeiro projeto de ações afirmativas do Brasil; na época foi chamado de louco, hoje é reconhecido visionário."
    ))

    questoes_brutas.append((
        15, "EM13CHS603", "basico",
        "Por que o movimento negro substituiu a celebração tradicional do 13 de Maio pelo 20 de Novembro como o Dia da Consciência Negra?",
        "Porque o dia 13 de maio coincidia com datas de exames vestibulares em universidades federais.",
        "Porque o 13 de Maio celebra a figura da princesa branca benevolente, enquanto o 20 de Novembro resgata a morte em combate de Zumbi dos Palmares, afirmando a soberania e a luta autônoma do povo negro.",
        "Porque o mês de novembro apresenta temperaturas meteorológicas mais amenas para desfiles cívicos.",
        "Porque as associações comerciais exigiam a concentração de feriados no segundo semestre do ano.",
        "Porque a data de maio foi instituída por tratados de navegação fluvial assinados com a Inglaterra.",
        "B",
        "A virada do 20 de Novembro rompe com a ilusão do 'favor da princesa': a liberdade não foi doada no cartório em 13 de maio; foi conquistada com sangue e resistência liderada por Zumbi, Dandara e Palmares."
    ))

    questoes_brutas.append((
        16, "EM13CHS101", "basico",
        "Qual território quilombola, situado no norte de Goiás e tombado como patrimônio cultural, é o maior do Brasil em extensão contínua e exemplo de sustentabilidade?",
        "O Quilombo do Frechal no litoral do Maranhão.",
        "O Território Quilombola Kalunga, que abriga mais de 4 mil pessoas no Cerrado preservado.",
        "A Comunidade Quilombola de Campinho da Independência em Paraty.",
        "O Quilombo da Fazenda Picinguaba em Ubatuba.",
        "A Comunidade de Ivaporunduva no Vale do Ribeira paulista.",
        "B",
        "Os Kalungas preservam centenas de milhares de hectares no Cerrado goiano: cultivam a terra sem veneno, mantêm a posse coletiva secular e são reconhecidos pela ONU como guardiões da biodiversidade do planeta."
    ))

    questoes_brutas.append((
        17, "EM13CHS102", "basico",
        "Como Abdias do Nascimento critica a Lei de Terras de 1850 na história agrária e social do Brasil?",
        "Elogia a norma como uma lei distributiva que concedeu lotes rurais gratuitos a todos os lavradores.",
        "Denuncia que a lei proibiu o acesso à terra pelo trabalho, exigindo a compra em leilões financeiros e condenando os futuros libertos de 1888 à exclusão territorial absoluta e à miséria nas favelas.",
        "Afirma que a lei foi elaborada para incentivar a instalação de linhas telegráficas no interior.",
        "Sustenta que a legislação garantiu a demarcação antecipada de todas as terras tradicionais indígenas.",
        "Comprova que a norma eliminou as disputas agrárias entre fazendeiros de café e produtores de cana.",
        "B",
        "A Lei de Terras de 1850 preparou o golpe do pós-abolição: proibiu a posse pela ocupação e exigiu dinheiro vivo; quando a escravidão acabou, o negro não tinha onde plantar e foi empurrado para a favela e o cortiço."
    ))

    questoes_brutas.append((
        18, "EM13CHS601", "basico",
        "Como a sociologia de Clóvis Moura, parceiro intelectual de Abdias, define o conceito de 'Práxis Negra' nas rebeliões quilombolas?",
        "Como o hábito de memorizar provérbios orais durante as folgas de fins de semana nas senzalas.",
        "Como a ação consciente, organizada e revolucionária dos escravizados que, através de quilombos e revoltas, minou a segurança e as bases econômicas da ordem escravista mercantilista colonial.",
        "Como a realização voluntária de horas extras de trabalho agrícola para agradar os capatazes de engenho.",
        "Como a redação de petições cordiais solicitando a redução de castigos físicos aos tribunais reais.",
        "Como a organização de procissões religiosas católicas aos domingos nos pátios das casas-grandes.",
        "B",
        "Clóvis Moura e Abdias provam: o escravizado não era peça passiva; a 'Práxis Negra' dos quilombos e levantes armados foi a força motriz que quebrou a espinha dorsal do sistema escravocrata mercantilista."
    ))

    questoes_brutas.append((
        19, "EM13CHS602", "basico",
        "De que maneira o pensamento de Abdias do Nascimento orientou a delegação brasileira na III Conferência Mundial da ONU contra o Racismo, realizada em Durban (2001)?",
        "Incentivou a assinatura de acordos comerciais para a redução de tarifas de transporte aéreo internacional.",
        "Fundamentou a tese histórica da delegação brasileira de que a escravidão e o comércio transatlântico foram Crimes contra a Humanidade, exigindo reparações e ações afirmativas dos Estados.",
        "Propôs a transferência da sede das Nações Unidas para capitais de províncias agrícolas asiáticas.",
        "Defendeu que as reparações históricas fossem pagas exclusivamente através de doações de trigo.",
        "Sugeriu o cancelamento de debates étnicos em fóruns internacionais para priorizar o comércio marítimo.",
        "B",
        "Durban 2001 foi um marco planetário: a conferência da ONU declarou o tráfico de escravos Crime contra a Humanidade, exigindo cotas e reparações históricas, coroando décadas de luta de Abdias do Nascimento."
    ))

    questoes_brutas.append((
        20, "EM13CHS603", "basico",
        "Qual lei federal aprovada em 2023 converteu definitivamente o 20 de Novembro em feriado nacional em todo o território brasileiro?",
        "A Lei Federal nº 10.639 que tornou facultativo o ensino de ciências nas escolas rurais.",
        "A Lei Federal nº 14.759, que consagrou o Dia Nacional de Zumbi e da Consciência Negra no calendário cívico de todo o país.",
        "O Decreto-Lei nº 229 que regulamentou o horário de funcionamento de feiras livres municipais.",
        "A Emenda Constitucional nº 45 que reformou os procedimentos internos do Poder Judiciário federal.",
        "A Portaria Interministerial nº 89 que estabeleceu regras para o descarte de embalagens plásticas.",
        "B",
        "A Lei 14.759/2023 consagrou a vitória da consciência histórica: o 20 de Novembro é feriado em todo o Brasil, honrando a memória de Zumbi dos Palmares e a luta incansável do povo negro pela liberdade."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Como Abdias do Nascimento articula a crítica da cultura e a crítica política ao fundar o Teatro Experimental do Negro (TEN) em 1944?",
        "Separando rigorosamente a arte teatral de qualquer questionamento sobre desigualdades raciais e sociais.",
        "Demonstrando que a representação estética e o protagonismo negro nos palcos são trincheiras de desalienação, capazes de desmantelar o imaginário colonial que reduzia os afrodescendentes a papéis subalternos.",
        "Obrigando os atores da companhia a realizarem apresentações exclusivamente na língua francesa clássica.",
        "Financiando a montagem de peças através de empréstimos concedidos por bancos mercantis britânicos.",
        "Limitando o repertório teatral à encenação de comédias farsescas sobre a nobreza imperial europeia.",
        "B",
        "O TEN provou que a arte é combate descolonial: colocar atores negros para encenar tragédias de Shakespeare e peças autorais desmontou o racismo que reservava ao negro apenas os papéis de criado e serviçal."
    ))

    questoes_brutas.append((
        22, "EM13CHS102", "intermediario",
        "Como Abdias desmistifica a participação de João Batista de Lacerda no Congresso Universal das Raças de 1911 em Londres?",
        "Elogia Lacerda como um diplomata pioneiro que defendeu os direitos humanos de povos indígenas.",
        "Expõe que Lacerda apresentou oficialmente ao mundo a política do governo brasileiro de extinção biológica da raça negra em três gerações por meio da mestiçagem forçada e do influxo migratório europeu.",
        "Comprova que o cientista brasileiro defendeu a concessão imediata de títulos de terras aos libertos.",
        "Afirma que os discursos proferidos no congresso foram censurados por academias navais europeias.",
        "Demonstra que o cientista propôs a substituição de moedas metálicas por certificados de colheita agrícola.",
        "B",
        "Lacerda foi a Londres e apresentou um quadro eugênico vergonhoso: prometeu que em 100 anos o sangue negro desapareceria do Brasil pelo cruzamento com brancos; Abdias desnudou esse genocídio planejado."
    ))

    questoes_brutas.append((
        23, "EM13CHS601", "intermediario",
        "De que modo a experiência quilombola de Palmares refuta a tese eurocêntrica de que as sociedades africanas desconheciam formas complexas de governança e organização estatal?",
        "Comprovando que os líderes de mocambos utilizavam coroas forjadas por ourives venezianos.",
        "Evidenciando que Palmares articulou uma confederação confederada de povoados fortificados com agricultura diversificada, metalurgia do ferro, sistema judiciário comunitário e diplomacia militar por quase cem anos.",
        "Mostrando que as cidades livres palmarinas copiavam integralmente os códigos legislativos da corte de Roma.",
        "Afirmando que a subsistência do quilombo dependia unicamente da importação de gêneros alimentícios holandeses.",
        "Provando que a defesa dos mocambos era coordenada por generais mercenários contratados no exterior.",
        "B",
        "Palmares quebrou o preconceito colonial: os africanos ergueram uma federação de cidades soberanas com fundição de ferro, estoques alimentares e governança exemplar, derrotando exércitos coloniais armados."
    ))

    questoes_brutas.append((
        24, "EM13CHS602", "intermediario",
        "Como a categoria quilombista de 'Economia Solidária' contrapõe-se simultaneamente ao modelo liberal do latifúndio e ao modelo estatista autoritário?",
        "Propondo a extinção da moeda e o retorno compulsório à troca exclusiva de sementes silvestres.",
        "Sustentando a gestão coletiva e comunitária dos meios produtivos pelos próprios trabalhadores, preservando a autonomia das famílias e o respeito à terra sem a intermediação de patrões privados ou burocratas de Estado.",
        "Incentivando a criação de trustes corporativos transnacionais para a exportação de grãos de cereais.",
        "Defendendo a concessão de subsídios fiscais para latifundiários que compram maquinários industriais pesados.",
        "Exigindo que a comercialização de safras dependa de autorização prévia emitida por juizados alfandegários.",
        "B",
        "O socialismo quilombista é libertário e comunitário: não quer o latifundiário explorador nem o burocrata do Estado confiscando a safra; a terra e a ferramenta são do povo que produz e divide com fraternidade."
    ))

    questoes_brutas.append((
        25, "EM13CHS603", "intermediario",
        "Por que Abdias do Nascimento classifica o racismo brasileiro como um 'Racismo Mascarado e Dissimulado'?",
        "Porque os cidadãos utilizavam máscaras de linho durante manifestações esportivas municipais.",
        "Porque o racismo brasileiro opera sem a necessidade de leis formais de segregação jurídica, mantendo a exclusão social, econômica e política da população negra sob o manto hipócrita da cordialidade e da miscigenação.",
        "Porque as instituições públicas do país foram projetadas com paredes duplas em repartições fiscais.",
        "Porque as leis eleitorais proibiam o registro de certidões civis de nascimento em cartórios provinciais.",
        "Porque os tribunais de justiça funcionavam unicamente em horários noturnos para evitar protestos populares.",
        "B",
        "O racismo no Brasil é pérfido: não precisa de placas 'proibido negros' para impedir o negro de entrar em salas de diretoria ou conselhos de juízes; ele discrimina com sorrisos, olhares de desconfiança e tiros da polícia."
    ))

    questoes_brutas.append((
        26, "EM13CHS101", "intermediario",
        "Como o conceito de 'Pan-Africanismo' formulado por Marcus Garvey e W.E.B. Du Bois influenciou a formulação teórica do Quilombismo no exílio de Abdias?",
        "Incentivando os ativistas a adquirirem companhias de navegação a vapor nos portos do mar do Norte.",
        "Conectando a luta secular dos quilombolas brasileiros à resistência global de todos os povos de África e da diáspora negra contra o imperialismo, o neocolonialismo e a exploração transnacional do capital.",
        "Defendendo a adoção de regras gramaticais estritas para a redação de tratados diplomáticos bilaterais.",
        "Exigindo a subordinação de organizações comunitárias negras a diretrizes militares de potências aliadas.",
        "Propondo a padronização de bandeiras cívicas em todas as repúblicas da América Latina e do Caribe.",
        "B",
        "No exílio nos EUA e na Nigéria, Abdias viu a unidade da luta negra: o mesmo racismo que mata o jovem na favela do Rio oprime o mineiro na África do Sul e o camponês no Caribe; o Quilombismo é pan-africano."
    ))

    questoes_brutas.append((
        27, "EM13CHS102", "intermediario",
        "De que modo a perseguição policial e religiosa contra os terreiros de Candomblé no século XX é denunciada por Abdias como uma faceta do genocídio cultural?",
        "Comprovando que os edifícios religiosos utilizavam telhas de cerâmica importadas de cidades nórdicas.",
        "Evidenciando que a criminalização das práticas espirituais de matriz africana buscava erradicar a memória ancestral, a cosmovisão e a dignidade humana existencial da população negra para impor o padrão eurocêntrico cristão.",
        "Determinando que os sacerdotes deviam realizar liturgias exclusivamente nos salões de câmaras de comércio.",
        "Afirmando que os conflitos religiosos resultavam unicamente de disputas corporativas de artesãos têxteis.",
        "Mostrando que a polícia apreendia tambores sagrados para doá-los a orquestras de conservatórios imperiais.",
        "B",
        "Atacar os terreiros era tentar matar a alma negra: o Estado usava a polícia para invadir centros, apreender santos e prender babalorixás; Abdias denunciou que destruir a fé é parte do genocídio cultural."
    ))

    questoes_brutas.append((
        28, "EM13CHS601", "intermediario",
        "De que forma Abdias resgata o papel pioneiro desempenhado por mulheres guerreiras como Dandara e Aqualtune na edificação da sociedade palmarina?",
        "Afirma que as mulheres quilombolas atuavam unicamente na costura de fardamentos para tropas militares.",
        "Demonstra que as lideranças femininas exerciam funções vitais de comando estratégico militar, planejamento agrícola comunitário e liderança espiritual, antecipando em séculos a igualdade política de gênero.",
        "Comprova que as mulheres palmarinas eram proibidas de participar de conselhos comunitários de decisão.",
        "Sustenta que as lideranças femininas dependiam da autorização de magistrados de comarcas coloniais.",
        "Mostra que as tarefas agrícolas eram distribuídas com base em diretrizes monárquicas portuguesas.",
        "B",
        "Dandara pegou em armas, comandou tropas e recusou qualquer acordo que mantivesse irmãos escravizados, preferindo a morte à submissão; o Quilombismo resgata a mulher negra como pilar de comando e liberdade."
    ))

    questoes_brutas.append((
        29, "EM13CHS602", "intermediario",
        "Como a morosidade e a inação estatal na titulação definitiva das terras quilombolas pelo INCRA manifestam a continuidade do racismo institucional no Brasil pós-1988?",
        "Provando que os funcionários públicos de agências fundiárias desconheciam métodos de cálculo topográfico.",
        "Evidenciando que, apesar do imperativo do Artigo 68 do ADCT, a bancada ruralista e os interesses do agronegócio pressionam o Estado para travar as titulações, expondo comunidades quilombolas à violência de grileiros.",
        "Demonstrando que os territórios tradicionais são devolvidos voluntariamente pelos líderes comunitários.",
        "Afirmando que as comunidades quilombolas preferem habitar edifícios residenciais verticais em capitais.",
        "Sustentando que a ausência de títulos de terra é suprida pela concessão de passaportes diplomáticos consulares.",
        "B",
        "A promessa da Constituição de 1988 continua travada: o latifúndio faz lobby no governo para não titular as terras, e enquanto o INCRA enrola, fazendeiros armados e grileiros ameaçam as famílias quilombolas."
    ))

    questoes_brutas.append((
        30, "EM13CHS603", "intermediario",
        "De que maneira o pensamento quilombista dialoga com a preservação ecológica e o enfrentamento da crise climática global?",
        "Defendendo a drenagem de bacias hidrográficas para viabilizar pistas de pouso de aeronaves militares.",
        "Mostrando que os territórios quilombolas tradicionais funcionam como barreiras ecológicas contra o desmatamento, praticando agroecologia, manejo comunitário de sementes e proteção radical da biodiversidade dos biomas.",
        "Exigindo a substituição de florestas nativas por plantações homogêneas de eucalipto para papel e celulose.",
        "Propondo a utilização em larga escala de fertilizantes químicos sintéticos nas lavouras do Cerrado.",
        "Determinando que a conservação ambiental deva ser subordinada a leilões de créditos de carbono corporativos.",
        "B",
        "O Quilombismo é vanguarda ecológica: as terras quilombolas são as áreas mais preservadas do país; os quilombolas cuidam da água e da mata como parte de seu corpo e de seus deuses, barrando a devastação do capital."
    ))

    questoes_brutas.append((
        31, "EM13CHS101", "intermediario",
        "Em O Genocídio do Negro Brasileiro, como Abdias analisa o uso ideológico do conceito de 'Mestiçagem' pela elite brasileira?",
        "Como uma celebração genuína da riqueza das culturas africanas e indígenas que superou o racismo.",
        "Como uma arma biopolítica e retórica orientada para a assimilação compulsória e o desaparecimento gradual do negro, desmobilizando a identidade racial coletiva sob o falso pretexto de que 'somos todos iguais'.",
        "Como uma diretriz médica adotada para a prevenção de moléstias infectocontagiosas tropicais.",
        "Como um acordo diplomático assinado com monarquias europeias para a unificação de moedas comerciais.",
        "Como uma metodologia pedagógica empregada na alfabetização rural de jovens camponeses das províncias.",
        "B",
        "A mestiçagem na boca da elite foi veneno: serviu para dizer 'não há negro no Brasil, todos somos morenos', desarmando o movimento negro e escondendo que a meta real do Estado era o branqueamento eugênico."
    ))

    questoes_brutas.append((
        32, "EM13CHS102", "intermediario",
        "Como a experiência de resistência de Ganga Zumba e sua posterior substituição por Zumbi ilustram os dilemas éticos entre 'Pacto de Rendição' e 'Libertação Radical' em Palmares?",
        "Demonstrando que os comandantes palmarinos preferiram vender suas terras a companhias mercantis de fumo.",
        "Evidenciando que a proposta de paz do governador português (que concedia liberdade apenas aos nascidos no quilombo e devolvia os demais à escravidão) foi rejeitada por Zumbi, que defendeu a libertação incondicional de todos.",
        "Provando que as negociações diplomáticas foram coordenadas por comissões de mercadores de especiarias asiáticas.",
        "Mostrando que os guerreiros quilombolas decidiram abandonar o território para viver em naus mercantes.",
        "Afirmando que a liderança de Zumbi foi imposta por decretos emitidos pela corte imperial de Lisboa.",
        "B",
        "A grande lição de Zumbi contra a conciliação covarde: a Coroa ofereceu anistia só para quem estava no quilombo em troca de devolver os escravos fugidos recentes; Zumbi recusou trair seus irmãos e lutou até o fim."
    ))

    questoes_brutas.append((
        33, "EM13CHS601", "intermediario",
        "Em que medida as pinturas e artes plásticas produzidas por Abdias do Nascimento afirmam o resgate da memória e da espiritualidade afro-brasileira?",
        "Elas reproduziam fielmente cenas mitológicas greco-romanas para exibição em salões de baile aristocráticos.",
        "Elas transformaram telas em altares e manifestos visuais sagrados, representando símbolos litúrgicos dos Orixás (Ogum, Xangô, Oxum) como afirmação afirmativa da cosmovisão negra contra o epistemicídio.",
        "Elas eram utilizadas como plantas arquitetônicas para a construção de quartéis de infantaria militar.",
        "Elas ilustravam manuais de etiqueta social para estudantes de academias de jurisprudência clássica.",
        "Elas serviam como cartazes publicitários para a venda de produtos agrícolas em feiras municipais.",
        "B",
        "A arte de Abdias é sagrada e descolonial: ele pintava o machado de Xangô e os ferros de Ogum com cores vibrantes, afirmando que a beleza e a sabedoria africanas são faróis sagrados de libertação humana."
    ))

    questoes_brutas.append((
        34, "EM13CHS602", "intermediario",
        "De que modo a luta de Abdias do Nascimento e do Movimento Negro Unificado (MNU) preparou o caminho para a aprovação da Lei Federal nº 10.639/2003?",
        "Defendendo que as escolas deveriam banir os estudos de literatura e história de seus currículos.",
        "Construindo décadas de pressão política e pedagógica que demonstraram que o silenciamento da história e da cultura afro-brasileira nas escolas é o alicerce fundamental da perpetuação do racismo estrutural.",
        "Propondo a substituição dos livros didáticos escolares por manuais de direito comercial britânico.",
        "Exigindo que os exames vestibulares cobrassem exclusivamente conhecimentos sobre engenharia militar naval.",
        "Reivindicando a cobrança de mensalidades em todas as escolas públicas de educação básica do país.",
        "B",
        "A Lei 10.639/03 é fruto da semente plantada por Abdias: ele sempre ensinou que um país que esconde a história de seus ancestrais negros educa seus jovens no preconceito; a verdade histórica liberta a mente de todos."
    ))

    questoes_brutas.append((
        35, "EM13CHS603", "intermediario",
        "Como a crítica de Abdias do Nascimento à abolição de 13 de Maio de 1888 desconstrói o discurso comemorativo da monarquia brasileira?",
        "Elogiando a Lei Áurea como a mais perfeita reforma agrária já implementada nas Américas.",
        "Evidenciando que a abolição formal foi uma manobra jurídica que libertou o escravo do cativeiro mas o abandonou na miséria, sem terra, sem trabalho remunerado garantido, sem escola e sem cidadania.",
        "Afirmando que os libertos receberam indenizações financeiras astronômicas pagas pelo Tesouro imperial.",
        "Sustentando que a princesa Isabel concedeu títulos nobiliárquicos a todas as famílias negras do Império.",
        "Provando que os ex-escravizados assumiram imediatamente os cargos de ministros de Estado na corte.",
        "B",
        "A farsa da abolição sem terra: jogaram o negro na rua sem um tostão no bolso, sem onde morar e sem trabalho, enquanto davam terras e subsídios aos imigrantes europeus; a Lei Áurea foi papel sem justiça social."
    ))

    questoes_brutas.append((
        36, "EM13CHS101", "intermediario",
        "Qual é o significado da célebre advertência de Abdias: 'O quilombismo não é racismo ao contrário, mas a proposta de libertação de toda a sociedade brasileira'?",
        "Que o Quilombismo pretende estabelecer um tribunal de inquisição racial contra cidadãos de origem europeia.",
        "Que a superação do racismo estrutural e a construção de uma ordem fraterna, comunitária e justa beneficiam a todos os seres humanos, livrando opressores e oprimidos da desumanização da violência racial.",
        "Que as propriedades rurais privadas devem ser desapropriadas para a construção de presídios militares.",
        "Que os descendentes de europeus devem ser compulsoriamente deportados para portos do mar Mediterrâneo.",
        "Que as decisões judiciais devem priorizar a concessão de incentivos fiscais para bancos multinacionais.",
        "B",
        "O Quilombismo quer libertar o Brasil inteiro: uma nação que mantém 56% de seu povo na miséria e sob tiros nunca será livre nem democrática; Palmares ensina que a igualdade do negro é a redenção de todos."
    ))

    questoes_brutas.append((
        37, "EM13CHS102", "intermediario",
        "De que modo a defesa quilombista da figura do 'Griô' e da tradição oral desestabiliza a supremacia positivista do texto escrito na educação brasileira?",
        "Desvalorizando completamente o aprendizado da escrita e da leitura nas escolas públicas municipais.",
        "Reconhecendo que a memória oral dos anciãos, os cantos ancestrais e a transmissão comunitária da experiência são fontes legítimas, rigorosas e insubstituíveis de conhecimento e filosofia social.",
        "Exigindo que os exames acadêmicos de doutorado sejam realizados exclusivamente através de danças festivas.",
        "Propondo a eliminação de todas as bibliotecas universitárias e substituição por arquivos de áudio gravado.",
        "Afirmando que a ciência moderna foi inventada exclusivamente por marinheiros em travessias marítimas.",
        "B",
        "O saber não vive apenas na folha de papel: o Griô africano e quilombola é uma biblioteca viva que carrega séculos de ética, botânica, medicina tradicional e história oral que o eurocentrismo tentou apagar."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Como a atuação de Abdias do Nascimento no exílio demonstrou que a denúncia internacional do racismo brasileiro era temida pela ditadura militar?",
        "A ditadura militar subsidiou financeiramente as conferências e viagens internacionais de Abdias.",
        "O regime autoritário vigiava, censurava e tentava desacreditar Abdias perante governos estrangeiros e a ONU, pois suas denúncias destruíam a propaganda oficial de que o Brasil era um paraíso sem preconceito.",
        "Os generais do governo militar condecoraram Abdias com medalhas de mérito diplomático consular.",
        "O governo brasileiro aprovou resoluções internacionais elogiando a publicação de O Genocídio do Negro Brasileiro.",
        "As embaixadas brasileiras no exterior distribuíam cópias gratuitas dos livros de Abdias em universidades.",
        "B",
        "A ditadura tremia quando Abdias falava no exterior: ele desmontava nos EUA, na África e na ONU a mentira dos generais de que o Brasil não tinha racismo, expondo a covardia e o massacre que o regime escondia."
    ))

    questoes_brutas.append((
        39, "EM13CHS602", "intermediario",
        "De que maneira as comunidades quilombolas urbanas contemporâneas (como os quilombos situados em capitais e metrópoles) exercem a resistência quilombista?",
        "Submetendo seus bairros ao controle armado de corporações de segurança privada estrangeiras.",
        "Afirmando seus territórios ancestrais contra a especulação imobiliária predatória, preservando terreiros, espaços culturais comunitários e hortas agroecológicas em meio ao concreto das grandes cidades.",
        "Exigindo a demolição de todos os edifícios históricos vizinhos para a abertura de avenidas comerciais.",
        "Fechando suas ruas com muros de concreto armado e proibindo o trânsito de pedestres e moradores.",
        "Recusando o pagamento de tarifas de energia elétrica em protesto contra a poluição sonora metropolitana.",
        "B",
        "Quilombo também é cidade: em Porto Alegre, no Rio ou em Salvador, quilombos urbanos resistem a construtoras e prefeituras, preservando o samba, o terreiro, a agroecologia e a dignidade contra o asfalto predatório."
    ))

    questoes_brutas.append((
        40, "EM13CHS603", "intermediario",
        "Qual é a relação profunda entre o Quilombismo de Abdias do Nascimento e as lutas contemporâneas por 'Reparações Históricas' no Brasil e no mundo?",
        "Ambos sustentam que a justiça distributiva foi alcançada com a inauguração de ferrovias industriais.",
        "Ambos afirmam que a riqueza das elites escravocratas foi construída com o roubo de séculos de trabalho negro gratuito, tornando mandatórias políticas públicas de terras, cotas, investimentos e indenizações estruturais.",
        "Os dois movimentos defendem que as reparações devem consistir unicamente no envio de cartas de desculpas formais.",
        "Ambas as correntes sustentam que o pagamento de reparações financeiras depende da autorização da Igreja.",
        "Os dois projetos propõem que as dívidas históricas sejam saldadas através de isenções fiscais para bancos.",
        "B",
        "Reparação histórica é dever de justiça ética e material: o Brasil ergueu suas cidades e seus bancos nas costas dos escravizados; o Quilombismo exige devolver a terra, garantir a vaga na universidade e pagar a dívida histórica."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 obrigatórias
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a desconstrução radical do 'Mito da Democracia Racial' operada por Abdias do Nascimento em O Genocídio do Negro Brasileiro: de que maneira o autor demonstra que a apologia da mestiçagem e a retórica da cordialidade operaram como a tecnologia ideológica mais sofisticada para perpetuar a hegemonia da supremacia branca no Brasil sem necessidade de aparatos jurídicos formais de segregação?",
        "Provando que as academias de jurisprudência do século XIX utilizavam códigos processuais traduzidos do latim.",
        "Demonstrando que, ao contrário do modelo segregacionista aberto dos Estados Unidos (leis Jim Crow) ou da África do Sul (Apartheid), o racismo brasileiro mascara a opressão sob o manto da harmonia, culpabilizando o próprio negro por sua marginalidade socioeconômica, deslegitimando as denúncias de discriminação como 'revanchismo' e promovendo um genocídio silencioso por branqueamento populacional e letalidade seletiva.",
        "Determinando que os diplomatas brasileiros deveriam prestar juramentos de fidelidade perante cortes régias.",
        "Afirmando que a mestiçagem foi uma política concebida espontaneamente por líderes quilombolas do interior.",
        "Comprovando que as instituições políticas imperiais foram inspiradas em tratados diplomáticos bizantinos.",
        "B",
        "- **Etapa 1:** Contrastar os modelos de racismo no mundo: enquanto os EUA e a África do Sul criaram leis explícitas de apartheid fáceis de identificar e combater, o Brasil inventou a fábula da cordialidade racial.\n- **Etapa 2:** Desvelar a perversidade do racismo mascarado: dizer que 'todos são iguais e mestiços' impede o negro de se organizar contra a discriminação; quem reclama é chamado de racista, mantendo a branquitude no poder sem escândalo aparente."
    ))

    questoes_brutas.append((
        42, "EM13CHS102", "dificil",
        "Examine a tese historiográfica e sociológica de Abdias do Nascimento e Clóvis Moura sobre a 'República dos Palmares como Projeto Civilizatório': como a organização interna de Palmares, sua confederação de mocambos, policultura alimentar e acolhimento plurirracial subverteram a ordem mercantilista colonial escravocrata do século XVII?",
        "Mostrando que os armamentos utilizados pelos palmarinos eram importados de fundições de bronze da Escandinávia.",
        "Evidenciando que Palmares não foi apenas uma fuga reativa e isolada de cativos, mas a construção afirmativa e alternativa de uma sociedade socialista comunitária, democrática e multirracial que negou a monocultura latifundiária de exportação em favor da soberania alimentar e desafiou a ordem geopolítica dos impérios de Portugal e Holanda com incomparável eficácia militar e institucional.",
        "Determinando que os tratados comerciais palmarinos deviam receber a chancela de magistrados consulares de Lisboa.",
        "Afirmando que a Confederação dos Palmares foi estruturada a partir de modelos monárquicos da dinastia merovíngia.",
        "Comprovando que a agricultura do quilombo consistia unicamente na colheita mecanizada de cana-de-açúcar para refino.",
        "B",
        "- **Etapa 1:** Desmontar a visão colonial de que o quilombo era esconderijo de fugitivos covardes: Palmares reuniu mais de 20 mil pessoas livres em dez cidades confederadas organizadas com agricultura diversa e fundição de ferro.\n- **Etapa 2:** Reconhecer a superioridade ética e social de Palmares: enquanto o litoral português praticava monocultura da cana com fome crônica e chibatada, Palmares distribuía comida farta, abrigava índios e brancos pobres e praticava democracia comunitária real."
    ))

    questoes_brutas.append((
        43, "EM13CHS601", "dificil",
        "Analise a concepção econômica e ecológica do Quilombismo: de que forma a recusa tanto do latifúndio individualista capitalista quanto do coletivismo burocrático de Estado soviético fundamenta a proposta quilombista de propriedade comunitária da terra e economia solidária?",
        "Provando que as comunidades tradicionais utilizavam métodos contábeis copiados de companhias mercantis bálticas.",
        "Demonstrando que o Quilombismo postula que a terra é solo sagrado e patrimônio inalienável da comunidade, onde a posse decorre do trabalho compartilhado; a produção destina-se à satisfação das necessidades humanas e à soberania alimentar, rompendo a lógica mercantil predatória sem submeter o trabalhador a uma ditadura burocrática estatal distante.",
        "Determinando que os lucros das colheitas coletivas devam ser aplicados em ações de companhias ferroviárias a vapor.",
        "Afirmando que a economia quilombola foi inspirada em manuais de teologia escolástica medieval sobre o comércio.",
        "Comprovando que as trocas de mercadorias dependiam de tabelamentos fixados por tribunais de justiça marítima.",
        "B",
        "- **Etapa 1:** Diferenciar o Quilombismo dos modelos dominantes do século XX: Abdias recusa o veneno do latifúndio privado que transforma a terra em especulação e rejeita o estatismo soviético que oprime o camponês sob burocratas.\n- **Etapa 2:** Fundamentar a terceira via socialista libertária: a terra quilombista é comunitária e familiar; produz-se para alimentar e viver bem em cooperação mútua, respeitando os ritmos da natureza e o fruto do suor coletivo."
    ))

    questoes_brutas.append((
        44, "EM13CHS602", "dificil",
        "Investigue a tese de Abdias do Nascimento sobre a 'Dimensão Política da Espiritualidade de Matriz Africana': de que maneira a cosmologia dos Orixás, Voduns e Inquices opera no Quilombismo como uma trincheira de resistência descolonial e simbiose ecológica contra a destruição capitalista da natureza?",
        "Comprovando que as vestimentas rituais eram confeccionadas unicamente com fios de seda importados do Oriente Médio.",
        "Evidenciando que a cosmovisão africana não separa a humanidade da natureza: as divindades são a própria personificação das águas, florestas, trovões e da terra; assim, cultuar os Orixás é assumir a responsabilidade ética inviolável de preservar o equilíbrio ecológico, transformando o Candomblé e a religiosidade ancestral em forças políticas de resistência contra o agronegócio predatório e a mineração devastadora.",
        "Determinando que os sacerdotes religiosos devam registrar suas liturgias em atas de assembleias municipais.",
        "Afirmando que os mitos ancestrais foram formulados por navegadores solitários durante travessias marítimas equatoriais.",
        "Provando que a proteção dos mananciais fluviais decorria unicamente de imposições normativas de cortes imperiais.",
        "B",
        "- **Etapa 1:** Compreender a ontologia sagrada africana: o sagrado não está trancado em um céu distante; Oxum é a água doce que sacia a sede, Ogum é o ferro transformador e Oxóssi é a mata viva protetora.\n- **Etapa 2:** Articular a fé à ecologia política: quem entende que a mata é morada de divindade jamais aceitará passar a boiada do veneno e do desmatamento; o Candomblé é vanguarda da preservação do planeta Terra contra a ganância capitalista."
    ))

    questoes_brutas.append((
        45, "EM13CHS603", "dificil",
        "Examine o papel precursor de Abdias do Nascimento na Assembleia Nacional Constituinte de 1987-1988: como a mobilização em torno do Artigo 68 do ADCT e a defesa de ações afirmativas expressaram a transição da militância de denúncia para a conquista institucional de direitos territoriais e civis fundamentais para a população negra?",
        "Provando que os debates constitucionais foram restritos a juristas formados em universidades de direito canônico.",
        "Demonstrando que Abdias e o movimento negro romperam a secular omissão constitucional brasileira, inserindo na Carta Magna o direito imemorial à titulação das terras quilombolas e plantando as bases conceituais para as políticas de cotas e combate ao racismo estrutural, transformando o Quilombismo de manifesto teórico em imperativo jurídico do Estado democrático de direito.",
        "Determinando que os mandatos parlamentares de constituintes negros deveriam ser supervisionados por cortes marciais.",
        "Afirmando que as conquistas constitucionais foram outorgadas voluntariamente por lideranças partidárias conservadoras.",
        "Comprovando que as propostas sobre igualdade racial foram arquivadas sem votação em plenário parlamentar.",
        "B",
        "- **Etapa 1:** Contextualizar o vazio legal pré-1988: desde a Lei de Terras de 1850 e da abolição de 1888, nenhuma constituição brasileira jamais havia reconhecido o direito territorial ou a dívida histórica com o povo negro.\n- **Etapa 2:** Avaliar a vitória constitucional do Quilombismo: Abdias e o MNU forçaram o Estado a assinar o Artigo 68 do ADCT; o quilombo deixou de ser tratado como crime pelo código penal e virou direito de propriedade definitiva garantido pela Constituição."
    ))

    questoes_brutas.append((
        46, "EM13CHS101", "dificil",
        "Analise a relação teórica entre a 'Lei de Terras de 1850' e a conformação socioespacial das 'Favelas Brasileiras' à luz da crítica quilombista de Abdias do Nascimento: por que a impossibilidade de aquisição de terras pelo trabalho livre instituiu o apartheid fundiário brasileiro?",
        "Mostrando que as residências populares urbanas eram edificadas com pedras de cantaria extraídas de montanhas.",
        "Evidenciando que a legislação de 1850 foi concebida propositalmente pela elite escravocrata para impedir que os negros e os imigrantes pobres tivessem acesso à terra livre pelo cultivo, confinando o solo nas mãos do latifúndio; assim, quando ocorreu a abolição em 1888, a população negra liberta, desprovida de qualquer pedaço de chão rural, foi empurrada para os morros e periferias desprovidas de saneamento, originando as favelas como quilombos urbanos de sobrevivência.",
        "Determinando que os terrenos urbanos devolutos devam ser comercializados exclusivamente em leilões consulares navais.",
        "Afirmando que a ocupação dos morros cariocas decorreu de diretrizes de planejamento urbano traçadas por botânicos.",
        "Provando que as famílias periféricas recebiam pensões em barras de ouro fundido do Tesouro Nacional imperial.",
        "B",
        "- **Etapa 1:** Desnudar o objetivo cirúrgico da Lei de Terras de 1850: temendo a futura abolição da escravidão, os senhores de escravos garantiram que a terra só pudesse ser comprada com montanhas de dinheiro que nenhum negro liberto teria.\n- **Etapa 2:** Conectar a exclusão agrária à favelização: sem terra para plantar, milhões de ex-escravizados subiram os morros e criaram as favelas; a favela é o refúgio do trabalhador espoliado, a continuidade urbana do quilombo sob o cerco do latifúndio imobiliário."
    ))

    questoes_brutas.append((
        47, "EM13CHS102", "dificil",
        "Examine a tese de Clóvis Moura sobre a 'Dialética Radical do Brasil Negro' e sua convergência com o Quilombismo de Abdias: como a ação dos escravizados desfez a ilusão da estabilidade da ordem escravocrata mercantilista, revelando o quilombo como a verdadeira vanguarda de desmantelamento do colonialismo?",
        "Provando que as fugas de cativos eram motivadas exclusivamente por desavenças pontuais de alimentação rústica.",
        "Demonstrando que o escravismo colonial era sustentado pelo terror armado e pela vigilância de capitães-do-mato; ao desertar coletivamente, fundar mocambos e travar guerrilhas prolongadas, a população negra sabotou a taxa de lucro dos engenhos, encareceu a repressão militar e provou a inviabilidade do cativeiro, atuando como o sujeito revolucionário primordial da história brasileira.",
        "Determinando que os chefes de polícia colonial deviam prestar relatórios semestrais a tribunais paroquiais.",
        "Afirmando que a abolição foi conquistada através de doações financeiras voluntárias de fazendeiros monarquistas.",
        "Comprovando que os exércitos imperiais venciam todas as revoltas camponesas sem a necessidade de reforços bélicos.",
        "B",
        "- **Etapa 1:** Refutar a mentira da 'escravidão estável e pacífica': os historiadores da casa-grande diziam que os escravizados eram dóceis; Moura e Abdias provam que o Brasil colonial viveu em guerra civil permanente contra as insurreições negras.\n- **Etapa 2:** Compreender a força econômica da revolta: manter Palmares e centenas de outros quilombos acuou as capitanias; o quilombola armado desfez os lucros do açúcar e forçou o colapso do sistema colonial com sua coragem inabalável."
    ))

    questoes_brutas.append((
        48, "EM13CHS601", "dificil",
        "Investigue o impacto da fundação do 'Teatro Experimental do Negro' (1944) como uma ruptura epistêmica e estética no modernismo brasileiro: de que maneira o TEN desestabilizou o padrão eurocêntrico que relegava o corpo e a subjetividade negra à condição de exotismo folclórico ou caricatura cômica?",
        "Comprovando que as companhias teatrais utilizavam instrumentos musicais de corda fabricados com madeira nórdica.",
        "Demonstrando que, ao encenar textos autorais dramáticos e tragédias clássicas universais com elenco integralmente negro alfabetizado e formado politicamente no próprio teatro, Abdias arrancou o afrodescendente do lugar de objeto de escárnio racista ou objeto passivo de estudos antropológicos, alçando-o à condição plena de sujeito produtor de alta cultura, arte dramática refinada e reflexão filosófica.",
        "Determinando que os ingressos para as récitas deveriam ser pagos exclusivamente com moedas cunhadas em prata pura.",
        "Afirmando que o TEN foi fundado para atender a diretrizes de propaganda cívica estabelecidas pela ditadura varguista.",
        "Provando que as peças eram supervisionadas por conselhos de filologia clássica de academias europeias.",
        "B",
        "- **Etapa 1:** Diagnosticar o teatro brasileiro antes do TEN: o negro só aparecia nos palcos como palhaço estúpido em comédias pastelão ou interpretado por um ator branco pintado de graxa preta (*blackface*).\n- **Etapa 2:** Reconhecer a revolução do TEN: Abdias colocou operárias e empregadas domésticas negras para interpretar heroínas e imperatrizes; o TEN provou que a inteligência dramática negra é brilhante, universal e emancipatória."
    ))

    questoes_brutas.append((
        49, "EM13CHS602", "dificil",
        "Analise a articulação entre o 'Quilombismo' e as lutas feministas negras lideradas por pensadoras como Lélia Gonzalez e Sueli Carneiro: de que maneira o resgate de figuras ancestrais como Dandara e Aqualtune combate o duplo silenciamento sofrido pela mulher negra na sociedade brasileira?",
        "Provando que as mulheres quilombolas se dedicavam exclusivamente à tecelagem de peças artesanais para o lar.",
        "Evidenciando que a mulher negra no Brasil enfrenta a sobreposição estrutural da opressão de raça, de classe e de gênero (sendo a mais precarizada no mercado e a mais vulnerável à violência); ao resgatar rainhas e guerreiras que comandaram batalhas e conselhos em Palmares, o Quilombismo desmonta a subalternidade histórica e projeta as mulheres negras como protagonistas essenciais da emancipação coletiva.",
        "Determinando que as líderes comunitárias femininas devam receber pensões honorárias concedidas por tribunais navais.",
        "Afirmando que a luta das mulheres nas comunidades quilombolas dependia de aprovação emitida por conselhos paroquiais.",
        "Comprovando que a gestão comunitária era exercida unicamente por soldados veteranos de guerras imperiais.",
        "B",
        "- **Etapa 1:** Descrever o triplo jugo da mulher negra: explorada pelo patrão rico, precarizada nos salários mais baixos e oprimida pelo machismo e pelo racismo cotidiano.\n- **Etapa 2:** Resgatar o protagonismo quilombista feminino: o Quilombismo lembra que sem Dandara, Aqualtune e Luísa Mahin não haveria resistência; as mulheres negras sempre foram estrategistas de guerra e cabeças de comunidade, inspirando Lélia Gonzalez e o feminismo negro de hoje."
    ))

    questoes_brutas.append((
        50, "EM13CHS603", "dificil",
        "Examine a crítica de Abdias do Nascimento à substituição do 20 de Novembro pelo 13 de Maio no imaginário escolar tradicional: como a historiografia oficial utilizou a celebração da Princesa Isabel para apagar o protagonismo insurgente da população escravizada e forjar o mito da gratidão perpétua ao Estado brasileiro?",
        "Comprovando que os desfiles cívicos de maio utilizavam bandeiras tecidas com algodão colhido no Vale do Paraíba.",
        "Demonstrando que festejar a 'Redenção de 13 de Maio' educava gerações na mentira de que a liberdade foi uma dádiva caridosa e paternalista da monarquia branca aos servos submissos, ocultando deliberadamente que o fim da escravidão foi arrancado pela fuga massiva de escravizados, revoltas armadas de senzalas, quilombos e pela agitação revolucionária de abolicionistas negros como Luiz Gama e José do Patrocínio.",
        "Determinando que as festividades escolares devam ocorrer unicamente em auditórios municipais climatizados.",
        "Afirmando que a escolha das datas comemorativas foi decidida por conselhos de astrônomos de cortes europeias.",
        "Provando que os tratados abolicionistas previam o pagamento de pensões a todos os libertos em moedas de ouro.",
        "B",
        "- **Etapa 1:** Desmascarar o mito da princesa redentora: ensinar que a princesa Isabel 'deu a liberdade' por bondade é tratar o povo negro como mendigo passivo que precisou de uma caneta branca para existir.\n- **Etapa 2:** Afirmar a verdade histórica do 20 de Novembro: a escravidão caiu porque os escravizados tornaram o Brasil ingovernável através de quilombos, greves e fugas; Zumbi e Luiz Gama são os verdadeiros heróis libertadores da Pátria."
    ))

    questoes_brutas.append((
        51, "EM13CHS101", "dificil",
        "Analise a relevância do 'Território Quilombola Kalunga' para o cumprimento das metas internacionais de desenvolvimento sustentável e preservação da biodiversidade do Cerrado: como a posse comunitária e os saberes tradicionais agroecológicos quilombolas constituem uma barreira viva contra o avanço predatório da monocultura transgênica?",
        "Provando que os camponeses locais utilizam pesticidas organofosforados de alta toxicidade nas lavouras.",
        "Demonstrando que os Kalungas mantêm a terra como propriedade coletiva indivisível, praticando a agricultura de roça tradicional sem venenos, manejando sementes crioulas ancestrais e protegendo nascentes vitais de rios contra o agronegócio que seca e queima o bioma, comprovando que o Quilombismo é o modelo prático mais eficiente de convivência simbiótica entre sociedade humana e natureza.",
        "Determinando que as áreas de preservação devam ser cercadas por arames eletrificados com sensores de calor.",
        "Afirmando que a sustentabilidade comunitária depende da exportação compulsória de grãos para o continente asiático.",
        "Comprovando que os conflitos territoriais decorriam da escassez de ferramentas de carpintaria em vilarejos rurais.",
        "B",
        "- **Etapa 1:** Reconhecer a catástrofe da monocultura no Cerrado: fazendas gigantescas de soja usam aviões jogando veneno, desmatam a vegetação nativa e esgotam os aquíferos subterrâneos para irrigação predatória.\n- **Etapa 2:** Valorizar a ciência ancestral Kalunga: em centenas de milhares de hectares protegidos, o quilombo não usa veneno, colhe frutos nativos (pequi, baru), cuida das nascentes e mantém o Cerrado vivo, provando a tese quilombista de sustentabilidade."
    ))

    questoes_brutas.append((
        52, "EM13CHS102", "dificil",
        "Investigue a conexão teórica entre o 'Pan-Africanismo' de Abdias do Nascimento e as reivindicações de Reparações Históricas na Declaração de Durban da ONU (2001): de que maneira o enquadramento do tráfico transatlântico e da escravidão como 'Crimes contra a Humanidade' fundamenta a exigência ética e jurídica de ações compensatórias do Estado brasileiro?",
        "Comprovando que os tratados consulares marítimos do século XVIII proibiam a navegação de barcos a remo.",
        "Evidenciando que, ao classificar a escravização como crime contra a humanidade que produziu o subdesenvolvimento da África e a marginalização estrutural da diáspora, a comunidade internacional reconheceu que os Estados que enriqueceram sobre o genocídio negro têm o dever indeclinável de pagar indenizações, titular terras remanescentes e implementar políticas públicas afirmativas de reparação social e educacional.",
        "Determinando que as indenizações sejam quitadas através da remessa compulsória de safras de cereais colhidos.",
        "Afirmando que a declaração de Durban foi elaborada unicamente por diplomatas de países do bloco soviético.",
        "Provando que as ações compensatórias dependiam de aprovação por comitês de acionistas de companhias têxteis.",
        "B",
        "- **Etapa 1:** Compreender o impacto jurídico de Durban 2001: pela primeira vez na história da ONU, o sequestro e escravização de 12 milhões de africanos foi declarado formalmente 'Crime contra a Humanidade'.\n- **Etapa 2:** Vincular à responsabilidade do Estado brasileiro: se foi crime com lucro para o Estado e as elites, as reparações não são favor nem esmola; cotas universitárias, saneamento nas favelas e titulação de terras quilombolas são obrigação jurídica internacional."
    ))

    questoes_brutas.append((
        53, "EM13CHS601", "dificil",
        "Analise a crítica de Abdias do Nascimento ao 'Epistemicídio Curricular' praticado pelo sistema escolar brasileiro antes da aprovação da Lei nº 10.639/2003: como a exclusão das filosofias e saberes afro-brasileiros atuou como mecanismo deliberado de reprodução do complexo de inferioridade entre os estudantes negros?",
        "Provando que as matrizes curriculares das escolas utilizavam compêndios impressos com tintas vegetais perecíveis.",
        "Demonstrando que, ao ensinar unicamente a história dos monarcas e filósofos europeus enquanto retratava o negro apenas na condição humilhante de cativo açoitado no tronco, a escola operava a epidermalização da inferioridade (como denunciara Fanon), roubando a autoestima e o orgulho das crianças negras e ensinando os estudantes brancos a naturalizarem a desigualdade racial como fato biológico.",
        "Determinando que os manuais didáticos devam ser aprovados previamente por comissões de generais de marinha.",
        "Afirmando que a ausência de conteúdos sobre a África decorria da falta de linhas de transporte marítimo regulares.",
        "Comprovando que os estudantes recebiam cadernos de notas encadernados com couro bovino em feiras públicas.",
        "B",
        "- **Etapa 1:** Descrever a violência do currículo tradicional eurocêntrico: a criança negra entrava na escola e só via brancos como reis, poetas e cientistas, e o negro apenas sangrando na senzala sem voz nem história.\n- **Etapa 2:** Diagnosticar o efeito psíquico do epistemicídio: isso destruía a mente da criança negra, gerando vergonha da própria cor; a Lei 10.639/03 repara essa injustiça, mostrando a grandeza dos reinos africanos, de Palmares e de pensadores como Abdias."
    ))

    questoes_brutas.append((
        54, "EM13CHS602", "dificil",
        "Examine a realidade contemporânea das mais de 3.500 comunidades quilombolas ativas no Brasil: de que maneira a resistência dessas comunidades pela titulação de suas terras e a produção de alimentos saudáveis para a merenda escolar corporificam a práxis do Quilombismo no século XXI?",
        "Mostrando que as associações comunitárias utilizam ferramentas eletrônicas alimentadas por baterias de lítio importadas.",
        "Evidenciando que os quilombos contemporâneos mantêm viva a matriz emancipatória de Palmares: afirmam a soberania alimentar através da agricultura familiar sem venenos, protegem a sociobiodiversidade dos biomas contra o agronegócio predatório e exigem do Estado a efetivação do Artigo 68 do ADCT, provando que o quilombo não é relíquia do passado, mas projeto vivo e urgente de cidadania e sustentabilidade.",
        "Determinando que a produção agrícola das comunidades deva ser submetida a comissões consulares de alfândegas.",
        "Afirmando que a subsistência das famílias é financiada exclusivamente por corporações financeiras internacionais.",
        "Comprovando que a posse da terra dependia de autorização expressa de academias de jurisprudência clássica.",
        "B",
        "- **Etapa 1:** Reconhecer a vitalidade dos quilombos contemporâneos: há mais de 3.500 quilombos no país produzindo arroz, feijão, farinha e hortaliças para abastecer escolas públicas e cidades vizinhas.\n- **Etapa 2:** Confirmar a atualidade da teoria de Abdias: ao resistirem a grileiros e defenderem suas florestas e águas sagradas, os remanescentes de quilombos põem em prática o Quilombismo hoje, mostrando ao Brasil um caminho ético de respeito à vida e à Terra."
    ))

    questoes_brutas.append((
        55, "EM13CHS603", "dificil",
        "Analise a contundência profética do Projeto de Lei de Cotas protocolado por Abdias em 1983 (PL 1.332/1983) em contraste com a rejeição raivosa das elites parlamentares da época: como a alegação de 'Inconstitucionalidade' mobilizada pelos opositores reproduzia a farsa da igualdade formal perante a lei para blindar o privilégio branco?",
        "Provando que os projetos legislativos da década de 1980 eram digitados em máquinas de escrever manuais.",
        "Demonstrando que os setores conservadores defendiam uma igualdade meramente abstrata no papel ('todos são iguais perante a lei') para ignorar as três séculos de escravidão que deixaram a população negra na miséria material absoluta; alegar que criar cotas era 'discriminação inconstitucional' constituía o sofisma jurídico perfeito para impedir que o Estado promovesse a igualdade substantiva real.",
        "Determinando que os debates da Câmara dos Deputados fossem transmitidos em telões instalados em praças rurais.",
        "Afirmando que a oposição parlamentar decorria da carência de recursos financeiros no Banco Central do Brasil.",
        "Comprovando que as cotas nas universidades foram substituídas por prêmios em moedas metálicas de ouro fundido.",
        "B",
        "- **Etapa 1:** Desmascarar a farsa da 'igualdade formal': colocar na largada de uma corrida de 100 metros uma pessoa bem alimentada e treinada ao lado de alguém que passou séculos com correntes nos pés não é igualdade, é covardia.\n- **Etapa 2:** Consolidar a vitória da igualdade substantiva: Abdias já ensinava em 1983 que o Estado precisava de ações afirmativas para reparar séculos de exclusão; trinta anos depois, o STF confirmou que cotas são constitucionais e reparadoras."
    ))

    questoes_brutas.append((
        56, "EM13CHS101", "dificil",
        "Investigue o papel de Abdias do Nascimento na fundação do Partido Democrático Trabalhista (PDT) e do Secretariado do Movimento Negro em 1980: como o autor buscou articular a tradição do Trabalhismo getulista e brizolista com as reivindicações antirracistas estruturais do Quilombismo?",
        "Comprovando que os comícios partidários eram realizados unicamente em pátios de casernas de infantaria.",
        "Demonstrando que Abdias compreendeu que o trabalhismo clássico brasileiro padecia de uma cegueira eurocêntrica ao olhar a classe operária como homogênea; ao criar o Secretariado do Negro, ele obrigou o partido a reconhecer que a classe trabalhadora mais superexplorada e massacrada do país é a trabalhadora negra, inserindo a raça no centro das pautas socialistas.",
        "Determinando que os filiados partidários deviam usar distintivos bordados com fios de algodão cru nas roupas.",
        "Afirmando que a aliança política foi celebrada unicamente com corporações de comerciantes de caravelas a vapor.",
        "Provando que as diretrizes do partido eram redigidas por congregações religiosas beneditinas do interior.",
        "B",
        "- **Etapa 1:** Diagnosticar a limitação do trabalhismo tradicional: os velhos partidos de esquerda falavam em 'trabalhador' como se todo operário fosse homem branco de fábrica metalúrgica com carteira assinada.\n- **Etapa 2:** Revolucionar a política com o Quilombismo: Abdias mostrou que quem mais sofre no Brasil é a mulher negra diarista e o jovem negro precarizado; a libertação da classe trabalhadora exige colocar o antirracismo no comando."
    ))

    questoes_brutas.append((
        57, "EM13CHS102", "dificil",
        "Examine a tese de Abdias do Nascimento sobre a 'Invisibilidade da Intelectualidade Negra' na universidade brasileira: de que maneira o apagamento de pensadores como Luiz Gama, André Rebouças, Manoel Querino e Lélia Gonzalez nas bibliografias acadêmicas consolida o epistemicídio institucional?",
        "Provando que as editoras universitárias utilizavam impressoras manuais de madeira com baixa tiragem de livros.",
        "Evidenciando que a universidade elitista tradicional construiu a narrativa racista de que a reflexão teórica e a ciência são monopólios do homem branco europeu, silenciando os gigantes intelectuais negros que fundaram a sociologia, a engenharia e o direito no país, privando os estudantes de referências ancestrais emancipatórias e mantendo as faculdades como templos da branquitude.",
        "Determinando que os títulos de mestre e doutor fossem outorgados exclusivamente em sessões de corte naval.",
        "Afirmando que as pesquisas acadêmicas sobre relações raciais dependiam da aprovação de conselhos monásticos alpinos.",
        "Comprovando que os livros didáticos de filosofia eram distribuídos gratuitamente a tripulantes de barcos mercantes.",
        "B",
        "- **Etapa 1:** Desvelar o racismo epistêmico nas faculdades: por décadas, os cursos de Direito e Filosofia no Brasil formaram gerações sem nunca citar uma linha sequer de Luiz Gama ou de Abdias do Nascimento.\n- **Etapa 2:** Resgatar a linhagem dos mestres negros: os intelectuais negros não eram 'casos exóticos', foram os pioneiros do pensamento crítico e da liberdade no Brasil; resgatá-los no currículo descoloniza o saber e devolve a dignidade científica à nação."
    ))

    questoes_brutas.append((
        58, "EM13CHS601", "dificil",
        "Analise o valor ético e político do Quilombismo como modelo pedagógico para a formação cidadã na Educação Básica: de que maneira a filosofia de Abdias do Nascimento prepara os jovens do Ensino Médio para enfrentarem a violência urbana e defenderem a justiça socioambiental no Brasil?",
        "Comprovando que os currículos de ciências humanas devem priorizar unicamente a cronologia de impérios da Antiguidade.",
        "Demonstrando que o Quilombismo ensina que a cidadania não é obediência cega ao poder instituído, mas práxis ativa de solidariedade comunitária, combate intransigente ao preconceito, respeito sagrado à diversidade cultural e ecológica e construção coletiva de um país soberano onde a dignidade humana de negros, indígenas e trabalhadores seja sagrada e inviolável.",
        "Determinando que as avaliações pedagógicas escolares devam consistir unicamente em testes de memorização de datas.",
        "Afirmando que a reflexão política deve ser suspensa em salas de aula para preservar o sossego das famílias.",
        "Provando que a formação cívica dos estudantes depende unicamente do aprendizado de táticas de infantaria armada.",
        "B",
        "- **Etapa 1:** Afastar a educação passiva e domesticadora: ensinar apenas a obedecer leis injustas e aceitar a desigualdade como destino prepara jovens para a servidão conformista.\n- **Etapa 2:** Inspirar a juventude com a coragem de Palmares: o Quilombismo de Abdias acende a chama da esperança, ensinando o estudante a defender o meio ambiente, amar sua ancestralidade e lutar por uma sociedade democrática e fraterna."
    ))

    questoes_brutas.append((
        59, "EM13CHS602", "dificil",
        "Investigue a coerência dialética que une a fundação do TEN (1944), a denúncia em O Genocídio do Negro Brasileiro (1978) e a síntese em O Quilombismo (1980): como a trajetória de Abdias do Nascimento expressa a unidade inseparável entre Arte, Ciência e Práxis Revolucionária?",
        "Provando que o autor abandonou as artes plásticas para dedicar-se exclusivamente ao comércio de tecidos finos.",
        "Evidenciando que cada etapa de sua vida foi uma trincheira complementar do mesmo combate: a arte no TEN quebrou o racismo estético no palco; o rigor sociológico em O Genocídio demoliu o mito da harmonia racial no debate público; e a filosofia política em O Quilombismo apresentou a alternativa civilizatória concreta para a emancipação definitiva do povo brasileiro.",
        "Determinando que as obras teóricas de Abdias deviam ser redigidas unicamente em pergaminhos com selos consulares.",
        "Afirmando que a atuação do pensador decorreu de financiamentos concedidos por bancos mercantis britânicos.",
        "Comprovando que a militância antirracista foi encerrada voluntariamente com a decretação da anistia política de 1979.",
        "B",
        "- **Etapa 1:** Compreender a evolução orgânica do pensamento de Abdias: não foram fases contraditórias ou isoladas, mas os degraus de uma obra magistral construída ao longo de quase um século de vida.\n- **Etapa 2:** Coroar a síntese libertadora: no teatro ele libertou o corpo e a voz do ator negro; no livro denunciou o genocídio do racismo mascarado; e no Quilombismo entregou o mapa da nova sociedade comunitária, fraterna e socialista para o Brasil."
    ))

    questoes_brutas.append((
        60, "EM13CHS603", "dificil",
        "Ao concluirmos com o Quilombismo o Eixo III (Filosofia Política, Poder, Resistência e Necropolítica), examine como a teoria de Abdias do Nascimento oferece uma resposta afirmativa e emancipatória às crises contemporâneas de desumanização analisadas nos capítulos anteriores (o biopoder de Foucault, o estado de exceção de Agamben, a alienação colonial em Fanon e a necropolítica de Mbembe):",
        "Provando que a solução para as crises globais consiste na restauração de monarquias parlamentares do século XVIII.",
        "Demonstrando que, perante a barbárie do necropoder que mata os descartáveis e suspende a lei na exceção permanente, o Quilombismo contrapõe a afirmação radical da vida através da solidariedade comunitária, da posse comum da terra, do poder popular de base e da comunhão sagrada com a natureza ancestral, erguendo o quilombo como a utopia concreta mais vigorosa de refundação democrática e humanista do século XXI.",
        "Determinando que os tratados de paz internacional devam ser assinados unicamente por academias de ciências exatas.",
        "Afirmando que a convivência política harmônica depende da subordinação das decisões cívicas a corporações bélicas.",
        "Comprovando que as disputas de soberania mundial foram solucionadas com a introdução de moedas virtuais bancárias.",
        "B",
        "- **Etapa 1:** Amarrar o Eixo III de Filosofia Política: vimos como a soberania ocidental descambou para o panóptico (Foucault), o campo de exceção (Agamben), o inferno colonial (Fanon) e os mundos de morte (Mbembe).\n- **Etapa 2:** Celebrar a resposta luminosa do Quilombismo: contra a máquina da morte e do lucro desumanizador, Abdias resgata Palmares: terra para todos, comida farta na mesa, igualdade para as mulheres, respeito à floresta e democracia popular; o Quilombismo fecha o Eixo III como a grande luz de esperança e reconstrução da Humanidade."
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
    linhas.append('eixo: "Eixo III: Filosofia Política, Poder, Resistência e Necropolítica"')
    linhas.append('capitulo: "Capítulo 24: O Quilombismo e a Resistência Negra: Abdias do Nascimento"')
    linhas.append('objeto_de_conhecimento: "O conceito de Quilombismo em Abdias do Nascimento, a desmistificação do mito da democracia racial, a República dos Palmares como projeto civilizatório, o socialismo comunitário afro-brasileiro e o pan-africanismo"')
    linhas.append('ebook_fonte: "em-fil-c24-quilombismo-resistencia-abdias-nascimento.md"')
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
    linhas.append("# Lista de Exercícios: O Quilombismo e a Resistência Negra: Abdias do Nascimento\n")

    for q in questoes:
        num, hab, dif, enunciado, a, b, c, d, e, gab, res = q

        if num == 1:
            linhas.append("## Nível Básico\n")
        elif num == 21:
            linhas.append("## Nível Intermediário\n")
        elif num == 41:
            linhas.append("## Nível Difícil\n")

        q_id = f"q{num:02d}"
        tag_html = f"<!-- id: {q_id} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-24-quilombismo-resistencia-abdias-nascimento -->"
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
    linhas.append("- NASCIMENTO, Abdias do. *O quilombismo: documentos de uma militância pan-africanista*. 2. ed. Brasília/Rio de Janeiro: Fundação Palmares/OR Produtor Editorial, 2002.")
    linhas.append("- NASCIMENTO, Abdias do. *O genocídio do negro brasileiro: processo de um racismo mascarado*. Rio de Janeiro: Paz e Terra, 1978.")
    linhas.append("- MOURA, Clóvis. *Rebeliões da senzala: quilombos, insurreições, guerrilhas*. São Paulo: Zumbi Editora, 1959.")
    linhas.append("- GONZALEZ, Lélia. *Primavera para as rosas negras: Lélia Gonzalez em primeira pessoa*. São Paulo: Diáspora Africana, 2018.")
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

    destino_final = "content/medio/volume-unico/filosofia/eixo-3-politica/cap-24-quilombismo-resistencia-abdias-nascimento/ebooks/em-fil-c24-quilombismo-resistencia-abdias-nascimento-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 24 validado e homologado com Exit Code 0!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
