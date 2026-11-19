# -*- coding: utf-8 -*-
"""
Script de Geração e Validação das 60 Questões de Filosofia - Cap 12
Objeto: A Ética Utilitarista: Consequencialismo e Bem-Estar Coletivo
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
        "A ética utilitarista é classificada fundamentalmente como uma teoria 'Consequencialista'. Qual é o critério definidor dessa abordagem ética?",
        "Avaliar a moralidade de um ato pelo cumprimento cego de rituais religiosos antigos.",
        "Julgar a moralidade de qualquer ação humana exclusivamente pelas suas consequências práticas reais e pelos efeitos produzidos no mundo.",
        "Determinar o valor moral de um ato pela posição social e pelos títulos de nobreza do agente.",
        "Calcular a correção moral pela quantidade de páginas de tratados jurídicos memorizadas pelo indivíduo.",
        "Avaliar as ações pela conformidade com os mapas astrais desenhados no momento do nascimento.",
        "B",
        "Para o consequencialismo utilitarista, não são as intenções puras ou regras abstratas prévias que determinam a moralidade, mas o resultado concreto de bem-estar gerado pela ação."
    ))

    questoes_brutas.append((
        2, "EM13CHS101", "basico",
        "Na famosa abertura de sua obra de 1789, Jeremy Bentham afirma que a natureza colocou a humanidade sob o domínio de dois soberanos absolutos. Quais são eles?",
        "O medo e a ganância por moedas de ouro.",
        "A Dor e o Prazer.",
        "A tradição familiar e o dever patriarcal.",
        "O comércio marítimo e a agricultura irrigada.",
        "A força física e a velocidade atlética.",
        "B",
        "Bentham assenta sua ética no hedonismo psicológico naturalista: a humanidade é movida pela busca do prazer (o Bem) e pela repulsa à dor (o Mal)."
    ))

    questoes_brutas.append((
        3, "EM13CHS501", "basico",
        "Qual é a formulação clássica do 'Princípio da Maior Felicidade' (Princípio da Utilidade) proposto por Jeremy Bentham?",
        "Garantir a salvação espiritual exclusiva de sacerdotes e monges em mosteiros.",
        "Promover a maior quantidade líquida de felicidade para o maior número possível de indivíduos afetados pela ação.",
        "Impor que todos os cidadãos adotem o mesmo ofício profissional exercido por seus pais.",
        "Concentrar a totalidade das riquezas financeiras nas mãos de generais de infantaria militar.",
        "Proibir a realização de feiras populares de tecidos durante as estações chuvosas do ano.",
        "B",
        "O princípio da utilidade aprova toda ação cuja tendência seja maximizar o bem-estar e o prazer coletivo e minimizar o sofrimento de todos os envolvidos."
    ))

    questoes_brutas.append((
        4, "EM13CHS501", "basico",
        "O que foi o 'Cálculo Felicífico' (Felicific Calculus) idealizado por Jeremy Bentham?",
        "Uma fórmula astronômica para prever o alinhamento de constelações visíveis no céu noturno.",
        "Um método analítico quantitativo destinado a mensurar e comparar o saldo de prazer e dor de ações concorrentes por meio de variáveis objetivas.",
        "Um sistema contábil para calcular tributos alfandegários sobre a importação de trigo e cevada.",
        "Um teste de resistência física aplicado aos recrutas de guarnições militares costeiras.",
        "Um compêndio de receitas culinárias para banquetes servidos em palácios reais.",
        "B",
        "Bentham pretendia conferir rigor científico e quantitativo à moralidade através de sete variáveis (intensidade, duração, certeza, proximidade, fecundidade, pureza e extensão)."
    ))

    questoes_brutas.append((
        5, "EM13CHS501", "basico",
        "No cálculo utilitário de Bentham, o que estabelece o célebre princípio democrático de que 'cada homem conta por um, e ninguém por mais de um'?",
        "Que apenas as pessoas que possuem propriedades de terra têm o direito de votar em eleições parlamentares.",
        "A igualdade estrita na ponderação moral: o prazer e o sofrimento de um governante ou nobre têm exatamente o mesmo peso que os de um operário simples ou camponês.",
        "A determinação de que todas as famílias devem morar em casas construídas com o mesmo número de cômodos.",
        "A exigência de que os contratos de aluguel sejam assinados na presença de dois juízes togados.",
        "A proibição de que os cidadãos exerçam mais de uma atividade remunerada ao longo da semana.",
        "B",
        "O utilitarismo clássico rejeita privilégios de casta ou linhagem: na balança do bem-estar social, a dor e a felicidade de cada ser humano entram com valor equitativo idêntico."
    ))

    questoes_brutas.append((
        6, "EM13CHS504", "basico",
        "Ao debater a extensão da consideração moral para além da espécie humana, qual pergunta pioneira Jeremy Bentham formulou sobre os animais?",
        "'Eles sabem tocar instrumentos musicais de percussão?'",
        "'Eles podem sofrer?'",
        "'Eles conseguem ler tratados jurídicos impressos em papel de linho?'",
        "'Eles pagam tributos fiscais sobre pastagens agrícolas?'",
        "'Eles prestam juramentos de lealdade a monarcas soberanos?'",
        "B",
        "Bentham fundou a ética animalista moderna: o critério de inclusão moral não é a razão discursiva nem a linguagem alfabética, mas a senciência (a capacidade biológica de sentir dor e sofrimento)."
    ))

    questoes_brutas.append((
        7, "EM13CHS101", "basico",
        "Por que os críticos conservadores da Inglaterra vitoriana rotularam pejorativamente o utilitarismo quantitativo de Bentham de 'Filosofia de Porcos'?",
        "Porque os filósofos utilitaristas criavam animais suínos nos jardins de suas residências em Londres.",
        "Porque, ao avaliar os prazeres apenas pela quantidade e intensidade bruta, a teoria parecia sugerir que a vida de um animal saciado de comida no chiqueiro seria moralmente equivalente à de um ser humano virtuoso.",
        "Porque as reuniões dos pensadores utilitaristas eram realizadas em feiras de gado no interior do país.",
        "Porque Bentham defendia que os alimentos consumidos por operários deveriam ser temperados com banha de porco.",
        "Porque as leis sanitárias de Manchester proibiam o descarte de resíduos de açougues em canais de água.",
        "B",
        "A acusação apontava que o utilitarismo rebaixava a dignidade humana ao prazer sensorial cego; John Stuart Mill respondeu a essa crítica reformulando a teoria."
    ))

    questoes_brutas.append((
        8, "EM13CHS501", "basico",
        "Para responder à crítica da 'filosofia de porcos', John Stuart Mill introduziu qual inovação decisiva na teoria utilitarista?",
        "A proibição do consumo de carnes e derivados de animais em todo o território britânico.",
        "A distinção qualitativa entre prazeres superiores (intelectuais, morais e estéticos) e prazeres inferiores (puramente sensoriais e corporais).",
        "A obrigação de que todos os cidadãos ingleses frequentassem cursos noturnos de latim clássico.",
        "A substituição do Parlamento por um conselho de médicos especialistas em doenças infecciosas.",
        "A exigência de que os operários fabris dormissem doze horas por noite para evitar a fadiga mental.",
        "B",
        "Mill sofisticou o utilitarismo: prazeres diferem na sua qualidade nobre; faculdades intelectuais e sentimentos morais proporcionam um bem-estar superior aos apetites meramente biológicos."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "Em seu ensaio O Utilitarismo, John Stuart Mill sintetizou a superioridade dos prazeres intelectuais através de qual célebre aforismo?",
        "'Mais vale um pássaro na mão do que dois voando na floresta.'",
        "'É melhor ser um ser humano insatisfeito do que um porco satisfeito; é melhor ser Sócrates insatisfeito do que um tolo satisfeito.'",
        "'Apressa-te devagar e colhe os frutos doces da árvore da sabedoria.'",
        "'O dinheiro não traz felicidade para quem não sabe construir carruagens velozes.'",
        "'Quem cedo madruga encontra terras férteis prontas para o cultivo do trigo.'",
        "B",
        "Mill demonstra que uma existência que mobiliza a razão, a arte e a consciência crítica possui dignidade incomparável, sendo preferida por quem experimentou ambos os lados."
    ))

    questoes_brutas.append((
        10, "EM13CHS502", "basico",
        "Na obra Sobre a Liberdade (1859), John Stuart Mill formula o célebre 'Princípio do Dano' (Harm Principle). O que esse princípio prescreve?",
        "Que o governo imperial tem o direito de fiscalizar os horários de sono de todos os operários industriais.",
        "Que a única justificativa legítima para o Estado ou a sociedade coagir um indivíduo contra a sua vontade é impedir que ele cause dano a terceiros.",
        "Que os cidadãos que professam crenças religiosas heterodoxas devem ser confinados em colônias penais distantes.",
        "Que todas as pessoas adultas devem pagar tributos proporcionais à quantidade de animais domésticos que possuem.",
        "Que as publicações jornalísticas devem ser aprovadas previamente por bispos de ordens religiosas oficiais.",
        "B",
        "O Princípio do Dano é a salvaguarda da liberdade individual: sobre seu próprio corpo e mente, o indivíduo é soberano; o Estado só pode intervir para evitar agressão a outras pessoas."
    ))

    questoes_brutas.append((
        11, "EM13CHS502", "basico",
        "De acordo com John Stuart Mill, por que a sociedade não tem o direito de proibir um adulto lúcido de praticar condutas que prejudiquem unicamente a si mesmo (como hábitos nocivos à saúde privada)?",
        "Porque os hospitais das cidades industriais cobram taxas muito baratas pelos atendimentos médicos.",
        "Porque o bem-estar físico ou moral do próprio indivíduo não autoriza a coerção externa; ele é o melhor juiz de sua própria vida e o livre desenvolvimento da individualidade beneficia o progresso social.",
        "Porque as leis civis deixam de ter validade quando o sujeito se encontra dentro de sua residência particular.",
        "Porque o governo nacional não possui funcionários suficientes para patrulhar as ruas durante os feriados cívicos.",
        "Porque as opiniões da maioria parlamentar devem ser acatadas sem qualquer questionamento crítico.",
        "B",
        "Mill defende que a tutela paternalista excessiva sufoca a autonomia e a experimentação de modos de vida, que são vitais para a inovação e o bem-estar de toda a civilização."
    ))

    questoes_brutas.append((
        12, "EM13CHS501", "basico",
        "Qual é a diferença fundamental entre o 'Utilitarismo de Ato' e o 'Utilitarismo de Regra'?",
        "O utilitarismo de ato aplica-se apenas a marinheiros e o de regra aplica-se a comerciantes terrestres.",
        "O utilitarismo de ato calcula o saldo imediato de cada ação pontual; o de regra avalia quais normas gerais de conduta produzem o melhor saldo de bem-estar se forem universalmente seguidas.",
        "O utilitarismo de ato exige o uso de planilhas de papelão e o de regra utiliza computadores eletrônicos.",
        "O utilitarismo de regra foi inventado na Idade Média e o de ato surgiu na Grécia clássica de Platão.",
        "Ambos defendem que as leis da sociedade devem ser sorteadas em praças públicas a cada início de mês.",
        "B",
        "O utilitarismo de regra protege direitos e instituições: ao demonstrar que regras estáveis (como 'não matar inocentes') maximizam a segurança coletiva no longo prazo, evita aberrações pontuais."
    ))

    questoes_brutas.append((
        13, "EM13CHS501", "basico",
        "Em situações trágicas de emergência médica de catástrofe com escassez de recursos (como a falta de respiradores em pandemias), qual método utilitarista os médicos aplicam?",
        "Sorteio aleatório jogando dados em mesas de enfermagem.",
        "O protocolo de Triagem (como o método START), alocando recursos nos pacientes com maior probabilidade clínica de recuperação para salvar o maior número de vidas.",
        "Atendimento exclusivo de acordo com a ordem rigorosa de chegada física ao pronto-socorro.",
        "Prioridade absoluta para os cidadãos que possuem maiores saldos financeiros em contas bancárias.",
        "Transferência obrigatória de todos os pacientes para hospitais localizados fora do território nacional.",
        "B",
        "A triagem em medicina de catástrofe opera pela maximização do bem coletivo: avalia quem tem maior chance de sobrevida para evitar que recursos escassos sejam perdidos sem resultado."
    ))

    questoes_brutas.append((
        14, "EM13CHS501", "basico",
        "No caso histórico do automóvel Ford Pinto na década de 1970, qual erro moral grave cometido pela montadora foi denunciado por filósofos contemporâneos como Michael Sandel?",
        "A fábrica utilizou tintas inflamáveis na pintura externa dos espelhos retrovisores dos veículos.",
        "A diretoria fez um cálculo financeiro de custo-benefício atribuindo um valor monetário à vida humana, preferindo pagar indenizações por mortes do que consertar o tanque defeituoso.",
        "Os engenheiros da empresa recusaram-se a instalar aparelhos de rádio transmissores nos painéis dos automóveis.",
        "A montadora vendeu os veículos exclusivamente para motoristas que não possuíam carteira de habilitação formal.",
        "Os testes de impacto em pistas de asfalto foram realizados apenas em dias ensolarados de outono.",
        "B",
        "O caso do Ford Pinto demonstrou a perversidade de monetizar a vida humana: colocar preço em mortes transforma a dignidade humana em mera planilha comercial descartável."
    ))

    questoes_brutas.append((
        15, "EM13CHS504", "basico",
        "O filósofo contemporâneo Peter Singer atualizou o utilitarismo global propondo o movimento do 'Altruísmo Eficaz'. Qual é a tese central desse movimento?",
        "Incentivar que todas as pessoas doem suas residências para que governantes instalem postos de fiscalização militar.",
        "Usar a razão e evidências empíricas para direcionar recursos financeiros a causas humanitárias com maior capacidade real de salvar vidas e aliviar o sofrimento global.",
        "Obrigar as famílias de países ricos a realizarem compras de supermercado apenas uma vez a cada três meses.",
        "Determinar que os estudantes de colégios públicos passem as férias escolares trabalhando em oficinas mecânicas.",
        "Proibir o envio de doações em dinheiro para instituições que atuem fora dos limites da cidade natal do doador.",
        "B",
        "O altruísmo eficaz não é filantropia sentimental ingênua: calcula onde cada real doado produz o maior alívio mensurável da miséria e de enfermidades curáveis no planeta."
    ))

    questoes_brutas.append((
        16, "EM13CHS504", "basico",
        "Na analogia de Peter Singer sobre a 'Criança que se Afoga no Lago Raso', qual dever moral se impõe a quem caminha pelo parque calçando sapatos caros?",
        "Afastar-se apressadamente para não molhar as meias de algodão cru nas águas do lago.",
        "Pular imediatamente na água para salvar a criança, pois o valor incomparável da vida humana sobrepõe-se à perda material passageira de sapatos caros.",
        "Aguardar a chegada de autoridades policiais para lavrar uma certidão de ocorrência formal.",
        "Cobrar dos pais da criança uma indenização monetária equivalente ao preço de compra dos sapatos.",
        "Negociar com outros pedestres para que eles assumam a responsabilidade pelo resgate da vítima.",
        "B",
        "A analogia prova que salvar uma vida tem primazia inegociável sobre perdas materiais fúteis; Singer estende essa obrigação à doação para salvar crianças morrendo de fome no mundo."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "O projeto do 'Panóptico' (Panopticon), concebido por Jeremy Bentham para a reforma do sistema penitenciário, baseava-se em qual princípio arquitetônico e psicológico?",
        "Uma fortaleza subterrânea sem janelas onde os presos permaneciam no escuro total durante anos.",
        "Uma torre central de vigilância de onde um único guarda podia observar todas as celas dispostas em círculo, gerando a sensação de monitoramento perpétuo e disciplina interior.",
        "Um navio-prisão ancorado em alto-mar sem remos ou velas de navegação.",
        "Uma tenda de couro instalada em praça pública onde os infratores realizavam trabalhos de tecelagem manual.",
        "Um labirinto de pedras rochosas onde os detentos competiam em corridas com obstáculos de madeira.",
        "B",
        "O Panóptico pretendia usar a visibilidade permanente para reformar o comportamento dos presos pelo menor custo e menor uso de violência física direta."
    ))

    questoes_brutas.append((
        18, "EM13CHS501", "basico",
        "Na distopia literária Admirável Mundo Novo de Aldous Huxley, como o Estado futurista aplica um utilitarismo hedonista tecnocrático radical aos seus cidadãos?",
        "Obrigando a população a trabalhar dezesseis horas diárias sob ameaça de chicotes em lavouras de arroz.",
        "Eliminando todo sofrimento, luto e dúvida existencial por meio do condicionamento genético e da distribuição em massa da pílula do prazer anestesiante (Soma).",
        "Proibindo o uso de aparelhos de som e instrumentos musicais em todas as cidades industriais.",
        "Exigindo que os jovens usem roupas cerimoniais brancas em todas as refeições comunitárias de domingo.",
        "Destruindo todas as fábricas para forçar os seres humanos a viverem como caçadores nômades em florestas.",
        "B",
        "Huxley adverte contra a distopia do prazer superficial garantido: quando a felicidade se reduz à ausência de dor anestesiada pela química, a verdade, a liberdade e a dignidade humana são liquidadas."
    ))

    questoes_brutas.append((
        19, "EM13CHS504", "basico",
        "Por que o utilitarismo influenciou profundamente o nascimento dos movimentos contemporâneos de Defesa dos Animais e do Vegetarianismo Ético?",
        "Porque os animais domésticos foram declarados cidadãos com direito a voto em eleições municipais europeias.",
        "Porque, sendo os animais dotados de senciência (capacidade de sentir dor, pavor e sofrimento), o sofrimento imposto na pecuária industrial entra diretamente no cálculo moral utilitário.",
        "Porque os animais consomem pastagens naturais que deveriam ser vendidas para fábricas de papel de celulose.",
        "Porque as leis comerciais de países desenvolvidos proíbem o transporte rodoviário de cargas de gado bovino.",
        "Porque os filósofos utilitaristas acreditavam na transmigração mágica das almas humanas para corpos de aves silvestres.",
        "B",
        "Com Singer e Bentham, o utilitarismo recusa o especismo cego: infligir dor desnecessária a bilhões de animais para prazer gustativo supérfluo é uma monstruosidade no cálculo da utilidade global."
    ))

    questoes_brutas.append((
        20, "EM13CHS501", "basico",
        "Qual é um dos erros comuns mais frequentes cometidos por quem desconhece os fundamentos do Utilitarismo?",
        "Achar que o utilitarismo exige que todos os cidadãos aprendam a falar a língua grega clássica fluentemente.",
        "Confundir o utilitarismo com o egoísmo mesquinho de 'levar vantagem em tudo', ignorando que a teoria exige imparcialidade estrita e busca a felicidade de todos os afetados.",
        "Acreditar que os utilitaristas defendem o retorno às práticas econômicas feudais da Idade Média.",
        "Supor que Jeremy Bentham foi um general de cavalaria que lutou em guerras napoleônicas.",
        "Imaginar que o utilitarismo proíbe a realização de cirurgias médicas em hospitais públicos.",
        "B",
        "O utilitarismo exige desprendimento pessoal: o agente deve avaliar as consequências como um observador desinteressado e benevolente, colocando o bem coletivo acima de caprichos egoístas."
    ))

    # ----------------------------------------------------
    # NÍVEL INTERMEDIÁRIO (Questões 21 a 40)
    # ----------------------------------------------------
    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Ao contrastar o utilitarismo com a deontologia kantiana no célebre 'Dilema do Bonde' (Trolley Problem), qual conduta o utilitarista clássico aprova na situação básica em que desviar a alavanca mata um operário para salvar cinco?",
        "O utilitarista recusa tocar na alavanca e deixa o bonde atropelar e matar os cinco operários na linha principal.",
        "O utilitarista aciona a alavanca para desviar o bonde para o desvio lateral, pois cinco vidas salvas geram um saldo líquido de bem-estar muito superior a uma morte.",
        "O utilitarista pula nos trilhos de ferro para que o bonde descarrile antes de atingir os trabalhadores.",
        "Ele consulta o código de trânsito ferroviário aprovado por magistrados de cortes civis da capital.",
        "Ele telefona para as famílias dos trabalhadores pedindo que decidam o destino da viagem por sorteio.",
        "B",
        "No cálculo quantitativo de consequências empíricas puras, salvar cinco vidas ao custo trágico de uma maximiza a utilidade social agregada e minimiza o saldo total de sofrimento humano."
    ))

    questoes_brutas.append((
        22, "EM13CHS501", "intermediario",
        "Por que John Stuart Mill rejeitou a equivalência quantitativa estrita de Bentham, que afirmava que 'o jogo de empurrar alfinetes é tão bom quanto a poesia se der a mesma quantidade de prazer'?",
        "Porque os alfinetes de metal podiam enferrujar com a umidade do ar e causar acidentes nos jogadores.",
        "Porque Mill sustentava que as faculdades intelectuais, estéticas e morais humanas produzem prazeres qualitativamente superiores e de maior dignidade do que meros passatempos mecânicos ou apetites corporais.",
        "Porque os livros de poesia dramática eram vendidos a preços muito caros em livrarias de Londres.",
        "Porque as leis civis da Inglaterra proibiam a fabricação de brinquedos metálicos para crianças da classe trabalhadora.",
        "Porque Bentham era sócio de fábricas industriais que produziam alfinetes de costura em larga escala.",
        "B",
        "Mill defende que a fruição estética e o cultivo da razão têm valor intrinsecamente mais elevado: quem desenvolve a mente prefere a poesia, mesmo que ela venha com a inquietude da reflexão."
    ))

    questoes_brutas.append((
        23, "EM13CHS502", "intermediario",
        "Como o 'Teste dos Juízes Competentes' formulado por John Stuart Mill comprova empiricamente que os prazeres intelectuais são superiores aos prazeres corporais inferiores?",
        "Por meio de exames de sangue realizados em laboratórios químicos com amostras de camponeses idosos.",
        "Consultando aqueles indivíduos que experimentaram plenamente tanto os prazeres sensoriais do corpo quanto os prazeres do espírito: eles dão preferência unânime e decidida ao modo de vida que mobiliza suas faculdades mais nobres.",
        "Pela contagem do número de páginas de romances lidos por estudantes universitários durante o período de férias.",
        "Por votação aberta realizada nas assembleias de trabalhadores rurais em feiras municipais de gado.",
        "Pela medição do volume de batimentos cardíacos de voluntários que participam de competições atléticas.",
        "B",
        "O veredito dos juízes competentes que conhecem ambos os lados é inequívoco: ninguém com dignidade aceitaria ser transformado em um animal irracional satisfeito em troca de perder a razão humana."
    ))

    questoes_brutas.append((
        24, "EM13CHS502", "intermediario",
        "Na obra Sobre a Liberdade, qual advertência crucial John Stuart Mill formula contra o risco da chamada 'Tirania da Maioria' nas democracias modernas?",
        "O perigo de as frotas de navios pesqueiros serem monopolizadas por cooperativas de pescadores do litoral.",
        "O perigo de que uma maioria numérica, mobilizada por preconceitos ou dogmas religiosos, use o poder do voto ou a pressão social para esmagar opiniões dissidentes, liberdades individuais e estilos de vida minoritários.",
        "A ameaça de que os parlamentos municipais aprovem calendários anuais com mais de quatrocentas datas cívicas.",
        "O risco de que as indústrias têxteis fechem as portas por falta de matéria-prima de algodão cru importado.",
        "A possibilidade de que os jovens abandonem as cidades industriais para se dedicarem exclusivamente à caça florestal.",
        "B",
        "A democracia não se resume à vontade despótica da maioria; se uma maioria esmaga uma minoria que não causa dano a terceiros, a sociedade perde a diversidade e comete tirania intolerável."
    ))

    questoes_brutas.append((
        25, "EM13CHS501", "intermediario",
        "Considere o problema do 'Cirurgião Utilitarista de Ato': um médico tem em seu pronto-socorro cinco pacientes influentes à beira da morte necessitando de transplantes urgentes e, na sala de espera, um jovem saudável solitário sem parentes. Por que o Utilitarismo de Regra proíbe terminantemente que o médico mate o jovem para salvar os cinco?",
        "Porque os bisturis e ferramentas cirúrgicas do hospital poderiam perder o corte durante a operação.",
        "Porque a regra geral 'os médicos podem assassinar pacientes saudáveis para retirar órgãos' destruiria a confiança pública em todos os hospitais, gerando pânico social massivo e um prejuízo gigantesco de bem-estar no longo prazo.",
        "Porque as certidões de óbito emitidas por cartórios municipais exigem o pagamento de taxas em moedas de ouro.",
        "Porque os cinco pacientes enfermos eram devedores de tributos fiscais sobre propriedades agrícolas no interior.",
        "Porque as salas de cirurgia hospitalar devem funcionar exclusivamente nas primeiras horas da manhã ensolarada.",
        "B",
        "O utilitarismo de regra prevê as consequências sistêmicas de longo prazo: a segurança jurídica e a confiança na medicina são pilares que maximizam a felicidade coletiva, vetando o homicídio arbitrário."
    ))

    questoes_brutas.append((
        26, "EM13CHS504", "intermediario",
        "No debate contemporâneo sobre a 'Tortura em Casos de Bomba-Relógio' (Ticking Time Bomb), qual argumento consequencialista utilitário é frequentemente mobilizado por defensores de medidas extremas em interrogatórios?",
        "O argumento de que os instrumentos mecânicos de tortura foram desenhados por artesãos em oficinas de ferro da Antiguidade.",
        "O argumento de que infligir dor física a um único terrorista capturado que se recusa a falar seria justificável para obter a localização da bomba e salvar milhares de vidas inocentes prestes a serem incineradas.",
        "A alegação de que as leis penais de países desenvolvidos proíbem a leitura de tratados filosóficos em celas de presídios.",
        "A tese de que os terroristas detidos em bases militares devem receber auxílios financeiros mensais em moeda estrangeira.",
        "A comprovação de que as explosões de bombas químicas não afetam a temperatura do solo de áreas urbanas densas.",
        "B",
        "O cenário da bomba-relógio é o argumento utilitário clássico da excepcionalidade: sopesar a dor de um agressor contra a preservação de milhares de vidas civis, gerando intenso debate sobre direitos humanos."
    ))

    questoes_brutas.append((
        27, "EM13CHS504", "intermediario",
        "Qual é a resposta contundente que defensores dos Direitos Humanos e teóricos do Utilitarismo de Regra formulam contra a aceitação da tortura no caso da bomba-relógio?",
        "Eles afirmam que as bombas de dinamite perdem a capacidade de explosão quando guardadas em porões úmidos.",
        "Eles demonstram que autorizar a tortura cria um precedente institucional perverso que normaliza o arbítrio policial e corrói o Estado de Direito, além de produzir confissões falsas de pessoas desesperadas para cessar a dor.",
        "Eles sustentam que os interrogadores militares deveriam ser escolhidos por meio de sorteios em praças públicas.",
        "Eles exigem que as prisões de segurança máxima sejam construídas no topo de montanhas rochosas isoladas.",
        "Eles defendem que os suspeitos de crimes bélicos devem ser libertados imediatamente sem prestar depoimentos formais.",
        "B",
        "Institucionalizar a tortura corrói a integridade moral da sociedade e abre portas para abusos infinitos; ademais, a tortura é ineficaz para obter informações confiáveis, gerando danos sistêmicos maiores."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "Ao conectar o utilitarismo à Economia do Bem-Estar Social (Welfare Economics), qual contribuição o Princípio da Maior Felicidade ofereceu para as políticas públicas do Estado contemporâneo?",
        "A obrigatoriedade de que todos os produtos comerciais sejam embalados em caixas de madeira reciclada.",
        "A fundamentação teórica para justificar investimentos estatais em saúde pública universal, saneamento básico, educação obrigatória e redes de seguridade social voltadas a maximizar a utilidade agregada dos cidadãos.",
        "O fechamento das estradas de ferro para incentivar o transporte de cargas em carroças de tração animal.",
        "A proibição de que as empresas industriais contratem trabalhadores que não possuam propriedades rurais.",
        "A cobrança de pedágios em ouro sobre navios que cruzam canais artificiais construídos em lagos de água doce.",
        "B",
        "A teoria econômica do bem-estar aplica a lógica utilitária: o Estado deve agir onde o mercado falha, alocando recursos públicos para reduzir doenças e miséria e elevar o nível de bem-estar da população."
    ))

    questoes_brutas.append((
        29, "EM13CHS501", "intermediario",
        "Em sua teoria da punição penal, por que Jeremy Bentham se opôs frontalmente à teoria retributiva tradicional do 'Olho por Olho, Dente por Dente' (Lex Talionis)?",
        "Porque os artesãos de Londres tinham dificuldades para forjar correntes de ferro para os calabouços.",
        "Porque Bentham sustentava que impor dor ao criminoso por mera vingança passada é acrescentar um mal inútil ao mundo; a punição só é moral se visar consequências futuras úteis: prevenir novos crimes e ressocializar o sentenciado.",
        "Porque os códigos penais da Inglaterra foram redigidos por monges que viviam em internatos religiosos isolados.",
        "Porque os tribunais de justiça deveriam funcionar exclusivamente aos domingos após as cerimônias religiosas.",
        "Porque ele defendia que todos os réus deveriam ser absolvidos mediante a doação de pães de trigo aos pobres.",
        "B",
        "Para o utilitarismo, o castigo por si só é dor (um mal); ele só se justifica racionalmente como remédio profilático para dissuadir delitos futuros e proteger a segurança da coletividade."
    ))

    questoes_brutas.append((
        30, "EM13CHS502", "intermediario",
        "No livro Sobre a Liberdade, John Stuart Mill defende a Liberdade de Expressão de modo irrestrito, sustentando que até mesmo as opiniões comprovadamente falsas ou minoritárias devem ser toleradas. Qual o argumento utilitário de Mill?",
        "Ele afirma que as gráficas de editoras precisam imprimir panfletos para pagar os salários dos tipógrafos.",
        "Ele argumenta que silenciar uma opinião priva a humanidade: se a opinião for verdadeira, perde-se a oportunidade de corrigir o erro; se for falsa, perde-se a chance de confrontar a verdade com o erro, evitando que a verdade vire um dogma morto e sonolento.",
        "Ele sustenta que as pessoas que expressam opiniões falsas devem ser premiadas com moedas de prata pelo governo.",
        "Ele defende que os debates públicos devem ser realizados em línguas estrangeiras para treinar a diplomacia cívica.",
        "Ele comprova que os jornais diários perdem leitores quando publicam matérias sobre descobertas científicas.",
        "B",
        "A verdade só se mantém viva e revigorada através do debate aberto e livre com o contraditório; silenciar vozes dissidentes gera conformismo dogmático e estagnação intelectual para toda a sociedade."
    ))

    questoes_brutas.append((
        31, "EM13CHS504", "intermediario",
        "Na reflexão de Peter Singer em Libertação Animal, o conceito de 'Especismo' é comparado diretamente ao racismo e ao sexismo. Qual é a analogia estabelecida pelo filósofo utilitarista?",
        "A de que os animais silvestres deveriam pagar passagens de trem ao cruzarem reservas florestais.",
        "A de que discriminar seres sencientes apenas pelo critério da espécie biológica a que pertencem constitui um preconceito moral injustificável equivalente a discriminar humanos pela cor da pele ou pelo gênero.",
        "A comprovação de que as vacas e porcos possuem inteligência linguística superior à de estudantes do ensino médio.",
        "A exigência de que os zoológicos públicos distribuam uniformes confeccionados com tecidos de lã aos animais.",
        "A determinação de que as indústrias farmacêuticas substituam testes laboratoriais por pesquisas arqueológicas.",
        "B",
        "O especismo é a exclusão moral arbitrária: se um ser é capaz de sentir dor e sofrer, seu sofrimento deve ter peso moral idêntico; a espécie não confere licença ética para torturar ou explorar cruamente."
    ))

    questoes_brutas.append((
        32, "EM13CHS501", "intermediario",
        "Ao examinar a máxima utilitarista 'A maior felicidade para o maior número', qual risco ético tradicionalmente apontado por críticos de direitos humanos pode ocorrer se não houver salvaguardas institucionais?",
        "O risco de as fábricas industriais aumentarem a produção de ferramentas agrícolas de ferro fundido.",
        "O risco de justificar a escravização, o encarceramento arbitrário ou o sacrifício injusto de pequenas minorias indefesas sob a alegação de que isso aumentaria o bem-estar ou o prazer da imensa maioria da população.",
        "A possibilidade de que os livros de poesia dramática sejam distribuídos gratuitamente em bibliotecas escolares.",
        "A obrigação de que todos os cidadãos adultos consumam alimentos preparados exclusivamente com farinha de milho.",
        "O perigo de que as eleições parlamentares sejam realizadas com votações secretas em urnas de madeira lacrada.",
        "B",
        "Se o utilitarismo for aplicado sem limites deontológicos de direitos inalienáveis, a maioria pode oprimir a minoria; por isso Mill formulou o princípio do dano e a defesa dos direitos individuais."
    ))

    questoes_brutas.append((
        33, "EM13CHS504", "intermediario",
        "No debate sobre a Alocação de Recursos Governamentais, como o utilitarismo justifica a cobrança de Impostos Progressivos sobre grandes fortunas para financiar programas sociais de transferência de renda?",
        "Afirmando que os cidadãos ricos devem ser punidos por terem estudado matemática em universidades do exterior.",
        "Demonstrando que, em virtude da utilidade marginal decrescente do dinheiro, retirar mil reais de um bilionário afeta minimamente seu bem-estar, enquanto transferir essa mesma quantia para uma família miserável salva vidas e gera um imenso ganho de utilidade social agregada.",
        "Exigindo que as mansões de famílias ricas sejam transformadas em estábulos de cavalaria militar.",
        "Comprovando que a circulação de moedas bancárias perde velocidade quando guardada em cofres de ferro fundido.",
        "Determinando que os herdeiros de grandes fortunas devam trabalhar em plantações de cana-de-açúcar durante o verão.",
        "B",
        "A utilidade marginal decrescente prova o valor redistributivo: o dinheiro traz muito mais felicidade e alívio do sofrimento para quem não tem comida do que para quem já tem tudo em abundância supérflua."
    ))

    questoes_brutas.append((
        34, "EM13CHS502", "intermediario",
        "Em sua vida parlamentar no Reino Unido, John Stuart Mill foi pioneiro em 1867 ao apresentar uma proposta de lei histórica no Parlamento britânico. Qual era o conteúdo dessa proposta?",
        "A declaração de guerra imediata contra nações que cultivavam lavouras de arroz no continente asiático.",
        "A concessão do Direito de Voto às Mulheres (sufrágio feminino), defendida com brilhantismo em sua obra A Sujeição das Mulheres, coescrita com Harriet Taylor Mill.",
        "A obrigatoriedade de que todos os operários de fábricas residissem em acomodações construídas dentro das empresas.",
        "A extinção definitiva de todas as universidades que ensinavam matérias de ciências naturais na Europa.",
        "O tabelamento do preço de tecidos de linho importados de colônias comerciais da América do Norte.",
        "B",
        "Mill foi o primeiro deputado britânico a exigir o sufrágio feminino: argumentou que negar direitos cívicos e educação a metade da humanidade é uma injustiça estúpida que atrasa o progresso de toda a sociedade."
    ))

    questoes_brutas.append((
        35, "EM13CHS501", "intermediario",
        "Na análise do 'Dilema do Bonde', na variação conhecida como 'O Homem Gordo na Passarela' (empurrar um homem corpulento da ponte para travar o bonde e salvar cinco operários), por que a maioria das pessoas recusa essa ação, mesmo gerando o mesmo saldo numérico de 5 vidas salvas contra 1 morte?",
        "Porque as passarelas de pedestres foram construídas com corrimãos de madeira muito altos para serem escalados.",
        "Porque usar ativamente o corpo de um inocente como barreira física de impacto atinge a repulsa moral deontológica à instrumentalização direta de um ser humano como mero objeto descartável.",
        "Porque as rodas de ferro dos bondes urbanos funcionam com motores a vapor que não podem ser travados por corpos humanos.",
        "Porque os policiais municipais poderiam apreender os sapatos dos passageiros que observavam a cena da rua.",
        "Porque as leis de trânsito ferroviário proibiam o tráfego de bondes de passageiros em dias chuvosos de inverno.",
        "B",
        "Embora o utilitarismo de ato tosco veja o mesmo saldo numérico (5 por 1), a mente moral humana recusa empurrar fisicamente um inocente: a violação ativa da pessoa como escudo quebra o limite da dignidade."
    ))

    questoes_brutas.append((
        36, "EM13CHS504", "intermediario",
        "Como a abordagem utilitarista de Peter Singer responde à objeção comum de quem diz: 'Eu não tenho obrigação de ajudar crianças famintas na África porque existem pessoas ricas muito mais capacitadas do que eu para fazer doações'?",
        "Singer concorda com a desculpa e recomenda que as pessoas gastem suas economias financeiras em restaurantes de luxo.",
        "Ele argumenta que a omissão alheia não anula a nossa capacidade causal real de evitar uma tragédia: se você vê uma criança se afogando e outros pedestres olham indiferentes, a inércia deles não diminui o seu dever pessoal imediato de salvá-la.",
        "Ele determina que os cidadãos de países desenvolvidos devem pagar impostos tributários exclusivamente em sacas de grãos.",
        "Ele afirma que as transferências financeiras internacionais devem ser proibidas para incentivar o cultivo de mandioca local.",
        "Ele comprova que as doenças tropicais curáveis desaparecem espontaneamente quando a temperatura da água sobe no mar.",
        "B",
        "A omissão coletiva não serves de álibi moral: se tenho os recursos supérfluos para evitar a morte de um ser humano inocente sem sacrificar nada de comparável importância moral, o dever utilitário de agir permanece integral."
    ))

    questoes_brutas.append((
        37, "EM13CHS501", "intermediario",
        "No campo das Políticas Públicas de Vacinação em Massa, como a ética utilitarista justifica a obrigatoriedade da imunização de toda a população contra vírus letais?",
        "Obrigando as famílias que recusam vacinas a pagarem multas em barras de ferro fundido a empresas farmacêuticas.",
        "Demonstrando que a imunização coletiva cria a imunidade de rebanho que protege os vulneráveis e erradica epidemias, gerando um saldo esmagadoramente positivo de saúde e preservação da vida para toda a sociedade.",
        "Exigindo que os postos de saúde pública funcionem exclusivamente nas primeiras horas da madrugada de sábado.",
        "Determinando que os frascos de vacina sejam armazenados em caixas de papelão pintadas com figuras geométricas.",
        "Comprovando que os vírus infecciosos perdem a capacidade de transmissão quando as pessoas viajam para praias litorâneas.",
        "B",
        "A vacinação compulsória repousa no cálculo de utilidade pública: a leve picada da agulha e o risco residual mínimo são incomparavelmente inferiores à catástrofe coletiva de milhares de mortes evitáveis."
    ))

    questoes_brutas.append((
        38, "EM13CHS502", "intermediario",
        "De acordo com John Stuart Mill em Sobre a Liberdade, qual é a única exceção legítima em que o Estado pode aplicar a coerção paternalista sobre um indivíduo para o seu próprio bem?",
        "Quando o indivíduo for um estudante universitário que não queira matricular-se em matérias de literatura clássica.",
        "Quando se tratar de crianças, jovens que ainda não atingiram a maioridade da razão, ou pessoas temporariamente privadas de suas faculdades mentais de discernimento lúcido.",
        "Quando o cidadão adulto se recusar a consumir alimentos temperados com azeite de oliva em suas refeições.",
        "Quando os trabalhadores rurais decidirem trocar de residência sem avisar previamente as autoridades municipais.",
        "Quando os moradores de cidades industriais preferirem caminhar a pé em vez de utilizarem bondes elétricos.",
        "B",
        "O princípio da liberdade pressupõe agentes com maturidade de faculdades mentais: crianças e incapazes exigem a proteção pedagógica da sociedade para não se autodestruírem antes da plena autonomia."
    ))

    questoes_brutas.append((
        39, "EM13CHS504", "intermediario",
        "Na análise da indústria do entretenimento e das mídias digitais contemporâneas sob a ótica de John Stuart Mill, como ele classificaria os aplicativos de vídeos curtos viciantes que prendem a atenção por horas sem gerar reflexão crítica?",
        "Como a mais sublime expressão dos prazeres superiores de fruição artística da história da humanidade.",
        "Como prazeres inferiores de estimulação sensorial imediata e passiva, que geram dependência passageira e entorpecem as faculdades intelectuais nobres em vez de promover o desenvolvimento integral do ser humano.",
        "Como instrumentos diplomáticos indispensáveis para negociar acordos de paz entre países do hemisfério norte.",
        "Como ferramentas mecânicas utilizadas por agricultores para calcular a quantidade de sementes colhidas no campo.",
        "Como métodos pedagógicos recomendados para o treinamento de soldados de infantaria em batalhas militares.",
        "B",
        "Mill criticaria o entretenimento anestesiante: o consumo passivo de estímulos fáceis satisfaz como o jogo dos alfinetes de Bentham, mas empobrece a imaginação, o espírito crítico e a autonomia do sujeito."
    ))

    questoes_brutas.append((
        40, "EM13CHS501", "intermediario",
        "Por que, para a teoria utilitarista sofisticada, o cumprimento de promessas e a honestidade contratual devem ser rigorosamente preservados na vida cotidiana?",
        "Porque os bancos municipais cobram taxas muito elevadas para registrar contratos comerciais de compra e venda.",
        "Porque a quebra reiterada de promessas destrói a segurança jurídica e a confiança mútua na sociedade, gerando um ambiente de incerteza, medo e paralisia que reduz drasticamente o bem-estar coletivo de todos.",
        "Porque os cidadãos que descumprem contratos são obrigados a doar metade de suas roupas para famílias de camponeses.",
        "Porque as leis civis dos países europeus proibiam a realização de casamentos entre membros de classes sociais distintas.",
        "Porque as promessas não cumpridas provocam quedas no rendimento de lavouras de trigo e cevada nas fazendas.",
        "B",
        "No utilitarismo de regra, a honestidade tem imenso valor de utilidade: sociedades onde a palavra e os contratos são honrados geram prosperidade, paz e cooperação mútua muito superiores ao caos da desconfiança."
    ))

    # ----------------------------------------------------
    # NÍVEL DIFÍCIL (Questões 41 a 60)
    # ----------------------------------------------------
    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Analise a clássica objeção formulada pela filósofa norte-americana Judith Jarvis Thomson ao consequencialismo estrito no célebre experimento do 'Violinista Famoso': 'Você acorda em um hospital ligado por tubos a um violinista renomado inconsciente com insuficiência renal. O médico explica que apenas os seus rins podem filtrar o sangue dele pelos próximos nove meses; se você desconectar os tubos, o violinista morrerá imediatamente.' De que maneira essa analogia desafia a premissa utilitarista de que a maximização da vida alheia anula a soberania do corpo individual?",
        "Provando que os concertos de violino realizados em teatros municipais consomem muita energia elétrica gerada por hidrelétricas.",
        "Evidenciando que, mesmo que manter a conexão salve a vida de um gênio da música que gerará imensa felicidade a milhões de pessoas, ninguém tem o dever moral de ceder compulsoriamente seu próprio corpo para sustentar a vida de outrem sem consentimento voluntário soberano.",
        "Afirmando que os médicos de hospitais públicos devem cobrar ingressos em dinheiro de quem deseja ouvir ensaios musicais.",
        "Sustentando que os instrumentos musicais de corda devem ser confeccionados apenas com madeiras nobres de florestas temperadas.",
        "Defendendo que os pacientes que sofrem de doenças nos rins devem ser transferidos para ilhas oceânicas no mar Mediterrâneo.",
        "B",
        "**Etapa 1:** Analisar o experimento do violinista de Judith Jarvis Thomson: o choque entre a maximização da utilidade (salvar uma vida sublime) e o direito fundamental à autodeterminação corpórea.\n**Etapa 2:** Concluir com a barreira aos direitos individuais: a soberania do próprio corpo é inegociável; o utilitarismo tosco que exigisse a escravização corporal de um sujeito para benefício coletivo cometeria uma tirania intolerável."
    ))

    questoes_brutas.append((
        42, "EM13CHS501", "dificil",
        "Em seu livro Justiça: O que é Fazer a Coisa Certa, Michael Sandel apresenta o caso real dos quatro náufragos ingleses do iate Mignonette (1884), que, perdidos no oceano sem água e comida há semanas, decidiram assassinar e comer o jovem taifeiro órfão Richard Parker, que estava agonizante, para garantir a sobrevivência dos outros três marinheiros casados e com filhos. Ao julgar o caso, por que a Suprema Corte britânica condenou os marinheiros por assassinato, recusando a defesa utilitarista?",
        "Porque os marinheiros utilizaram facas de cozinha fabricadas em oficinas de ferro que não possuíam alvará municipal.",
        "Porque a corte estabeleceu que o assassinato deliberado de um inocente vulnerável é categoricamente intolerável, firmando que uma vida humana possui dignidade inviolável que não pode ser extinta sob o pretexto de cálculo numérico de utilidade ou benefício da maioria faminta.",
        "Porque o bote salva-vidas pertencia a uma companhia marítima que cobrava seguros em moedas de ouro sobre naufrágios.",
        "Porque os marinheiros deveriam ter aguardado a chegada de navios cargueiros da frota naval francesa no canal da Mancha.",
        "Porque o jovem Richard Parker era parente distante de almirantes condecorados em batalhas marítimas passadas.",
        "B",
        "**Etapa 1:** Analisar o caso clássico de canibalismo por necessidade (*R v Dudley and Stephens*): a tentativa de justificar o homicídio pela balança de sobrevivência de 3 contra 1.\n**Etapa 2:** Concluir com o marco civilizatório dos tribunais ocidentais: o dever de não matar inocentes é incondicional; a necessidade biológica extrema ou a vantagem de três marinheiros não conferem licença jurídica ou moral para canibalizar o mais indefeso."
    ))

    questoes_brutas.append((
        43, "EM13CHS502", "dificil",
        "Considere o experimento mental da 'Máquina de Experiências' (Experience Machine) formulado pelo filósofo norte-americano Robert Nozick em 1974: 'Imagine que pesquisadores construíram uma máquina de computador capaz de estimular o cérebro humano por eletrodos, fazendo o indivíduo vivenciar sensações simuladas perfeitas de qualquer prazer ou sucesso que desejar, sem nunca saber que está dentro de um tanque no laboratório.' Por que Nozick argumenta que a imensa maioria dos seres humanos recusaria conectar-se a essa máquina para o resto da vida?",
        "Porque as contas de luz para manter o computador funcionando seriam muito caras para as famílias pagarem no fim do mês.",
        "Porque os seres humanos não desejam apenas experimentar estados mentais subjetivos agradáveis ou sensações passivas de prazer; nós desejamos realizar ações concretas reais, ser uma pessoa autêntica de caráter nobre e estabelecer contatos verdadeiros com a realidade exterior e com os outros.",
        "Porque os eletrodos de metal colocados no couro cabeludo provocam irritações e quedas de cabelo nos usuários.",
        "Porque os computadores eletrônicos da década de 1970 utilizavam válvulas a vácuo que superaqueciam com facilidade no verão.",
        "Porque as leis civis de países desenvolvidos proibiam a venda de aparelhos de informática sem manuais de instrução impressos.",
        "B",
        "**Etapa 1:** Compreender a crítica radical de Robert Nozick ao hedonismo psicológico e utilitarista estrito.\n**Etapa 2:** Evidenciar que a felicidade humana é inseparável da verdade e da agência real: conectar-se à máquina seria uma forma de anulação da própria existência e ilusão anestesiada; preferimos a dor da vida real à fantasia de um prazer programado."
    ))

    questoes_brutas.append((
        44, "EM13CHS504", "dificil",
        "Ao examinar a relação entre o Utilitarismo de John Stuart Mill e a defesa da Emancipação Feminina em A Sujeição das Mulheres (1869), como Mill utiliza o argumento da utilidade social para demonstrar a irracionalidade do patriarcado?",
        "Afirmando que as mulheres que trabalham fora de casa consomem menos água potável durante o expediente fabril.",
        "Evidenciando que confinar metade da população da Terra ao ambiente doméstico e privá-las de educação e cidadania priva a sociedade do dobro de talentos intelectuais, invenções científicas e lideranças virtuosas, gerando um prejuízo colossal para o progresso moral e econômico de toda a humanidade.",
        "Determinando que os maridos deveriam receber pagamentos mensais em barras de ferro para cuidarem de afazeres domésticos.",
        "Propondo que as eleições parlamentares fossem reservadas a mulheres que comprovassem posse de propriedades agrícolas.",
        "Sustentando que a submissão das mulheres nas leis civis decorria de decretos emitidos por navegadores da frota marítima.",
        "B",
        "**Etapa 1:** Analisar a estratégia argumentativa de Mill e Harriet Taylor: articular justiça moral com cálculo de utilidade civilizatória.\n**Etapa 2:** Concluir com a denúncia do desperdício de potencial humano: o machismo patriarcal não é apenas tirania injusta contra as mulheres, mas estupidez coletiva que atrasa o bem-estar e o florescimento cultural de todo o planeta."
    ))

    questoes_brutas.append((
        45, "EM13CHS501", "dificil",
        "No clássico debate da filosofia moral sobre a 'Incomensurabilidade dos Valores', qual crítica autores contemporâneos formulam contra a pretensão de Bentham de reduzir todas as dores e prazeres a uma única escala monetária ou matemática?",
        "A de que os termômetros de mercúrio não possuem graduações numéricas suficientes para medir febres corporais altas.",
        "A de que é moralmente impossível e falacioso tentar traduzir bens qualitativamente incomparáveis — como a vida humana, a beleza da arte, a integridade ambiental e a amizade pura — em um denominador monetário comum ou moeda de troca sem cometer uma distorção desumanizadora.",
        "A de que os governos de cidades industriais utilizavam moedas cunhadas em cobre que sofriam oxidação química no inverno.",
        "A de que as tabelas de cálculo aritmético eram impressas com tintas pretas de má qualidade que borravam os papéis.",
        "A de que os matemáticos que trabalhavam em universidades públicas recusavam-se a ensinar equações a comerciantes.",
        "B",
        "**Etapa 1:** Interpretar o conceito de incomensurabilidade de valores: nem tudo tem preço que possa ser pesado em uma balança contábil única.\n**Etapa 2:** Concluir com a denúncia da coisificação mercantil: tentar quantificar o luto, a honra ou o amor na mesma régua que mede o preço de sapatos é desvirtuar a natureza profunda da dignidade e da experiência humana."
    ))

    questoes_brutas.append((
        46, "EM13CHS504", "dificil",
        "Em seu livro Ética Prática, Peter Singer aborda o dilema da 'Pobreza Extrema Global' e desconstrói a distinção moral tradicional entre 'Matar Alguém Diretamente' e 'Deixar Morrer por Omissão'. Qual a tese central sustentada por Singer nessa provocação ética?",
        "Que as pessoas que moram em países ricos devem ser presas pela polícia caso comprem sapatos novos em feiras comerciais.",
        "Que, em um mundo globalizado e interconectado, gastar fortunas supérfluas com futilidades sabendo com certeza absoluta que doar esse mesmo dinheiro salvaria a vida de crianças morrendo de fome equivale moralmente a uma negligência fatal, exigindo que o dever de assistência seja tratado como obrigação de justiça e não mera caridade opcional.",
        "Que as organizações de socorro humanitário deveriam comprar navios cargueiros para transportar água potável entre continentes.",
        "Que as crianças que passam fome em regiões áridas deveriam ser matriculadas em internatos agrícolas localizados no litoral.",
        "Que as leis internacionais de comércio deveriam fixar o preço de alimentos básicos exclusivamente em moedas de ouro maciço.",
        "B",
        "**Etapa 1:** Analisar a desconstrução da distinção entre comissão (matar) e omissão deliberada (deixar morrer quando se pode evitar com facilidade).\n**Etapa 2:** Concluir com o imperativo do altruísmo eficaz: quem possui abundância e assiste passivamente à agonia de inocentes sem socorrê-los falha gravemente no dever moral utilitário de prevenir a dor extrema do mundo."
    ))

    questoes_brutas.append((
        47, "EM13CHS502", "dificil",
        "Considere a aplicação do Princípio do Dano de Mill ao debate contemporâneo sobre a 'Liberdade de Expressão vs. Discurso de Ódio'. De acordo com a teoria de John Stuart Mill, em qual momento exato o Estado tem o poder legítimo de silenciar ou punir uma manifestação pública de discurso?",
        "Sempre que o orador defender ideias políticas que desagradem à maioria dos parlamentares da câmara de deputados.",
        "Quando o discurso ultrapassar o debate intelectual livre e se transformar em incitação direta, iminente e concreta à violência física ou à agressão aos direitos de terceiros (como gritar 'ponham fogo na casa do comerciante' diante de uma turba enfurecida armada com tochas).",
        "Toda vez que as pessoas utilizarem megafones ou aparelhos de som em praças públicas durante os finais de semana.",
        "Sempre que os artigos de jornal publicarem denúncias de corrupção fiscal envolvendo ministros da corte imperial.",
        "Quando os cidadãos decidirem discursar vestindo roupas confeccionadas com tecidos sintéticos importados da Ásia.",
        "B",
        "**Etapa 1:** Distinguir a livre circulação de ideias (mesmo as mais polêmicas ou ofensivas à maioria) da incitação à violência direta.\n**Etapa 2:** Concluir com o limite milliano: o Estado só pode proibir a fala quando ela opera como gatilho causal direto e iminente de dano físico e violação da segurança dos cidadãos (o célebre exemplo dos comerciantes de milho em *Sobre a Liberdade*)."
    ))

    questoes_brutas.append((
        48, "EM13CHS501", "dificil",
        "Em sua obra Panóptico (1791), Jeremy Bentham propôs um modelo arquitetônico no qual 'o poder deve ser visível e inverificável'. Qual crítica política contemporânea autores como Michel Foucault formularam contra essa tecnologia utilitária de disciplina social?",
        "A de que os materiais de construção utilizados nas torres de vigilância eram muito pesados para terrenos arenosos litorâneos.",
        "A denúncia de que o panoptismo transformou-se no paradigma sombrio da sociedade de vigilância moderna, onde a racionalidade utilitária de controle e eficiência é utilizada por governos e corporações para domesticar corpos, docilizar mentes e aniquilar a privacidade humana.",
        "A comprovação de que as prisões circulares consumiam muito carvão vegetal nos aquecedores durante os meses de inverno.",
        "A crítica de que os guardas das torres de observação deveriam trabalhar desarmados para não assustar os sentenciados.",
        "A afirmação de que os presos deveriam receber aulas diárias de poesia dramática grega ministradas por magistrados da corte.",
        "B",
        "**Etapa 1:** Interpretar a leitura foucaultiana do Panóptico em *Vigiar e Punir*.\n**Etapa 2:** Evidenciar o risco da engenharia social utilitária: o sonho benthamiano da transparência e disciplina técnica transformou-se na arquitetura invisível do monitoramento moderno das massas, solapando a liberdade individual sob o pretexto da segurança coletiva."
    ))

    questoes_brutas.append((
        49, "EM13CHS504", "dificil",
        "No debate sobre a Bioética e o 'Dilema dos Transplantes com Morte Cerebral', como o Utilitarismo de Regra sustenta a legitimidade moral e a confiança pública nos protocolos oficiais de doação de órgãos pós-morte no Sistema Único de Saúde (SUS)?",
        "Permitindo que os médicos vendam os órgãos para pacientes estrangeiros que paguem em barras de ouro maciço.",
        "Garantindo que a retirada de órgãos ocorra apenas após o diagnóstico estrito, transparente e irreversível de morte encefálica com autorização formal familiar, assegurando que o sistema maximize o salvamento de vidas sem jamais comprometer a segurança ou gerar o pavor público de que doentes sejam sacrificados.",
        "Determinando que os transplantes cirúrgicos sejam realizados exclusivamente em dias em que o céu esteja sem nuvens de tempestade.",
        "Obrigando as famílias dos doadores falecidos a pagarem as despesas de internação de quem recebe o órgão transplantado.",
        "Proibindo o uso de anestésicos químicos durante as operações de retirada de órgãos em salas de cirurgia hospitalar.",
        "B",
        "**Etapa 1:** Analisar o funcionamento do transplante como instituição que maximiza a utilidade pública de salvar milhares de pessoas.\n**Etapa 2:** Concluir com a garantia do utilitarismo de regra: a confiança absoluta no protocolo de morte encefálica é a condição de sobrevivência do sistema; sem regras inegociáveis de proteção, o pavor destruiria a doação e ceifaria vidas."
    ))

    questoes_brutas.append((
        50, "EM13CHS101", "dificil",
        "Considere o embate filosófico entre o Utilitarismo e a Teoria da Justiça como Equidade de John Rawls (1971). Qual é a crítica demolidora que Rawls formula contra o princípio da utilidade coletiva agregada?",
        "Rawls afirma que os filósofos utilitaristas desconheciam as técnicas de navegação a vela utilizadas por marinheiros no mar Báltico.",
        "Rawls demonstra que o utilitarismo não leva a sério a distinção entre as pessoas, pois soma as preferências de todos como se a sociedade fosse um único grande indivíduo, permitindo sacrificar as liberdades fundamentais e os direitos de uns em nome do saldo de prazer da maioria.",
        "Rawls sustenta que as eleições democráticas deveriam ser substituídas por sorteios anuais realizados em praças municipais.",
        "Rawls defende que os impostos tributários deveriam ser recolhidos exclusivamente em sacas de trigo colhidas no campo.",
        "Rawls comprova que as leis econômicas deixam de funcionar quando os tribunais de justiça fecham suas portas no verão.",
        "B",
        "**Etapa 1:** Analisar a crítica rawlsiana em *Uma Teoria da Justiça* sobre a sacralidade dos direitos individuais invioláveis.\n**Etapa 2:** Concluir com a refutação da fusão coletiva: a dignidade de cada indivíduo é inviolável pela justiça; um pacto social justo jamais pode autorizar o sofrimento de um ser humano sob o álibi de que outros usufruirão de maior prazer agregado."
    ))

    questoes_brutas.append((
        51, "EM13CHS504", "dificil",
        "Ao abordar os 'Dilemas da Mobilidade Urbana e Veículos Autônomos', se um carro sem motorista humano for programado com uma ética estritamente utilitarista de ato quantitativa e se deparar com a escolha entre colidir contra um ônibus lotado com 40 passageiros ou desviar contra uma calçada matando um ciclista inocente que usava capacete, qual será a decisão algorítmica?",
        "O carro tentará saltar sobre o ônibus utilizando molas de propulsão mecânica de alta potência.",
        "O algoritmo desviará para a calçada e sacrificará o ciclista solitário, pois salvar 40 passageiros do ônibus gera um saldo numérico de perdas de vidas infinitamente menor do que a morte de 40 pessoas na colisão frontal.",
        "O veículo desligará os freios e deixará as leis da física decidirem o resultado por inércia mecânica pura.",
        "O computador de bordo consultará o mapa astral dos 40 passageiros para verificar quem tem maior expectativa de vida.",
        "O veículo acionará a buzina em frequências ultrassônicas para dispersar os pássaros que voam na rodovia.",
        "B",
        "**Etapa 1:** Interpretar a lógica do consequencialismo estrito em softwares de inteligência artificial de trânsito.\n**Etapa 2:** Evidenciar o cálculo bruto de consequências: 40 vidas salvas versus 1 morte na calçada; a tragédia expõe a tensão ética entre a frieza do cálculo utilitário e o direito de inocentes não serem alvejados."
    ))

    questoes_brutas.append((
        52, "EM13CHS501", "dificil",
        "No conto clássico Os Que se Afastam de Omelas (The Ones Who Walk Away from Omelas) de Ursula K. Le Guin, descreve-se uma cidade resplandecente de perfeita felicidade e prosperidade onde a condição inegociável para essa felicidade é manter uma única criança inocente trancada em um porão escuro e imundo vivendo em perpétuo terror e agonia. Qual lição filosófica antiutilitarista essa fábula imortaliza?",
        "Que as crianças que moram em cidades litorâneas devem aprender a nadar antes de ingressarem em escolas de primeiras letras.",
        "Que nenhuma abundância material, beleza estética ou felicidade de milhões de cidadãos pode justificar moralmente a tortura e a desumanização deliberada de uma única vida indefesa, expondo a crueldade inaceitável de um utilitarismo sem limites éticos de direitos inalienáveis.",
        "Que as cidades que realizam festivais de primavera devem utilizar tochas de azeite para iluminar as vias públicas.",
        "Que as construções urbanas devem ser fiscalizadas por arquitetos formados em academias de engenharia da capital.",
        "Que a população de uma cidade deve doar anualmente moedas de prata para financiar reparos em muralhas defensivas.",
        "B",
        "**Etapa 1:** Analisar a alegoria de Omelas como a mais perfeita representação do cálculo utilitário puro levado às últimas consequências.\n**Etapa 2:** Concluir com a indignação moral dos que partem: a felicidade construída sobre o tormento deliberado de um inocente é indigna e corrompida; certos atos violam a humanidade de forma tão atroz que nenhuma utilidade coletiva pode redimi-los."
    ))

    questoes_brutas.append((
        53, "EM13CHS502", "dificil",
        "Em sua obra Sobre a Liberdade, John Stuart Mill defende que 'a originalidade é a única coisa que os espíritos não originais não conseguem sentir a utilidade'. De que maneira a proteção aos excêntricos, aos rebeldes e às minorias inovadoras é justificada pela utilidade coletiva de longo prazo?",
        "Porque os cidadãos excêntricos costumam gastar mais moedas de ouro comprando roupas de linho em alfaiatarias.",
        "Porque todo progresso histórico, científico, moral e cultural da humanidade nasceu da audácia de minorias e indivíduos heterodoxos que ousaram desafiar a mediocridade e o conformismo da maioria de sua época; sufocar a excentricidade é esterilizar o futuro da civilização.",
        "Porque as leis civis dos governos democráticos exigem que os cidadãos apresentem certidões de registro em cartórios municipais.",
        "Porque as tropas do exército nacional necessitam de soldados com temperamentos agressivos para patrulharem as fronteiras.",
        "Porque a realização de festividades populares atrai comerciantes estrangeiros que compram sacas de trigo e cevada.",
        "B",
        "**Etapa 1:** Interpretar a apologia milliana da excentricidade e da experimentação individual (*Experiments in Living*).\n**Etapa 2:** Concluir com o utilitarismo progressista: a sociedade precisa de gênios e dissidentes para abrir novas trilhas de verdade e justiça; a tolerância à diferença é o combustível vital da evolução da humanidade."
    ))

    questoes_brutas.append((
        54, "EM13CHS504", "dificil",
        "Ao examinar a questão da Mudança Climática Global sob a ótica utilitarista, por que o Princípio da Maior Felicidade impõe o dever moral estrito de transição energética urgente e cessação de combustíveis fósseis para a geração atual?",
        "Porque as jazidas de carvão mineral provocam terremotos em áreas costeiras desabitadas do hemisfério sul.",
        "Porque o cálculo de utilidade deve abranger não apenas os humanos vivos hoje, mas as bilhões de futuras gerações humanas e seres sencientes que sofrerão secas extremas, fome, pandemias e colapso de ecossistemas caso a temperatura do planeta continue subindo.",
        "Porque as turbinas eólicas e painéis solares geram empregos manuais exclusivos para trabalhadores rurais aposentados.",
        "Porque os governos de países desenvolvidos devem pagar tributos alfandegários sobre a queima de madeira em lareiras domésticas.",
        "Porque as companhias de aviação comercial são obrigadas por leis civis a transportar passageiros apenas durante o dia.",
        "B",
        "**Etapa 1:** Estender a variável benthamiana da 'extensão' ao tempo futuro (justiça intergeracional utilitarista).\n**Etapa 2:** Evidenciar o saldo de dor planetária: o lucro e o conforto momentâneos da geração presente são insignificantes comparados ao sofrimento catastrófico de séculos infligido a bilhões de seres vivos futuros; a inércia climática é imoral."
    ))

    questoes_brutas.append((
        55, "EM13CHS501", "dificil",
        "Na reflexão filosófica de Bernard Williams em sua crítica ao Utilitarismo, o autor apresenta o dilema de 'Jim e os Índios': Jim chega a uma aldeia onde um capitão militar está prestes a fuzilar vinte indígenas inocentes, mas oferece a Jim o poder de fuzilar um indígena com as próprias mãos para que os outros dezenove sejam libertados vivos. Por que Williams afirma que o utilitarismo anula a 'Integridade Moral' do indivíduo ao ordenar que Jim mate?",
        "Porque as armas de fogo utilizadas pelos soldados militares estavam descalibradas para tiros de precisão a curta distância.",
        "Porque o utilitarismo trata o sujeito como um canal passivo de cálculo de consequências numéricas, ignorando que o dever moral envolve a integridade de sua própria consciência e projetos de vida, tornando o agente refém moral das chantagens de criminosos.",
        "Porque os indígenas da aldeia deveriam ter sido consultados por meio de votação secreta com conchas marinhas.",
        "Porque o capitão militar pertencia a uma corporação que recolhia tributos fiscais para a coroa estrangeira.",
        "Porque as leis civis da aldeia proibiam a entrada de viajantes que não soubessem falar línguas nativas da floresta.",
        "B",
        "**Etapa 1:** Compreender a crítica de Bernard Williams ao utilitarismo focada na integridade da agência moral (*Integrity Critique*).\n**Etapa 2:** Concluir com a fratura da subjetividade: para o utilitarismo tosco, Jim 'deve' puxar o gatilho sem hesitar (1 morte contra 20); mas essa ordem transforma o homem bom em assassino e carrasco forçado, ignorando a fratura de sua alma."
    ))

    questoes_brutas.append((
        56, "EM13CHS502", "dificil",
        "Em Sobre a Liberdade, John Stuart Mill adverte que a censura governamental a ideias heréticas gera a 'Atrofia Intelectual' dos próprios defensores da verdade oficial. Qual o mecanismo pedagógico que sustenta esse argumento?",
        "A comprovação de que os professores universitários perdem a capacidade de escrever em quadros-negros de madeira.",
        "A constatação de que, sem o estímulo vigoroso da controvérsia e a necessidade de responder a objeções duras de adversários vivos, os defensores da verdade deixam de compreender os fundamentos racionais de suas próprias crenças, repetindo-as como fórmulas mortas e preconceitos vazios.",
        "A exigência de que todos os livros de filosofia teórica sejam encadernados com tecidos sintéticos importados da Ásia.",
        "A determinação de que os exames vestibulares cobrem apenas questões sobre datas de fundação de cidades industriais.",
        "O aumento do número de páginas em branco nos cadernos escolares distribuídos a estudantes do ensino fundamental.",
        "B",
        "**Etapa 1:** Analisar a dialética da verdade em John Stuart Mill: a verdade precisa ser defendida ativamente para continuar viva e lúcida.\n**Etapa 2:** Concluir com a pedagogia do contraditório: banir o erro por censura não fortalece a verdade, mas a debilita; a verdade vira superstição mecânica que os cidadãos repetem sem saber por que a defendem, destruindo a vitalidade da razão."
    ))

    questoes_brutas.append((
        57, "EM13CHS504", "dificil",
        "No debate sobre a Experimentação Animal na Indústria de Cosméticos (testes de xampus e maquiagens em olhos e peles de coelhos e ratos), como o utilitarismo contemporâneo de Peter Singer julga essa prática?",
        "Como um procedimento industrial louvável que garante a beleza estética das mulheres em capitais metropolitanas.",
        "Como uma aberração moral inaceitável, pois submeter seres sencientes a torturas físicas atrozes e cegueira permanente para satisfazer a vaidade fútil e supérflua de cosméticos humanos gera um saldo grotesco de sofrimento desnecessário.",
        "Como um problema puramente contábil que deve ser resolvido pela redução dos impostos cobrados sobre produtos de beleza.",
        "Como uma atividade científica meritória que deveria ser financiada com recursos de bancos de desenvolvimento econômico.",
        "Como uma rotina laboratorial indispensável que não possui qualquer alternativa de testes em tecidos celulares in vitro.",
        "B",
        "**Etapa 1:** Ponderar a balança utilitária de sofrimento versus prazer na indústria da beleza humana.\n**Etapa 2:** Concluir com a indignidade do especismo: o interesse vital do animal em não sofrer dores lancinantes supera em infinitas ordens de magnitude o interesse trivial e supérfluo do consumidor por uma nova tonalidade de batom ou xampu."
    ))

    questoes_brutas.append((
        58, "EM13CHS501", "dificil",
        "Considere a crítica formulada pelo filósofo Robert Goodin sobre o 'Utilitarismo como Filosofia Pública': por que o utilitarismo, apesar de apresentar limitações quando aplicado à vida pessoal íntima (onde imperam amores e promessas), revela-se a teoria ética mais poderosa e adequada para a Gestão de Governos e Políticas de Estado?",
        "Porque os ministros de Estado e prefeitos são obrigados por lei a ler a obra completa de Jeremy Bentham em suas posses.",
        "Porque o governante republicano administra recursos públicos de milhões de cidadãos desconhecidos e não pode agir por simpatias privadas ou preferências de amizade; ele deve adotar a imparcialidade impessoal e calcular quais leis e investimentos geram o maior bem-estar e o menor sofrimento para toda a população.",
        "Porque os orçamentos fiscais dos governos democráticos devem ser elaborados por oficiais de infantaria militar.",
        "Porque os tratados de direito internacional exigem que os governantes morem em tendas de couro durante o expediente público.",
        "Porque as companhias de transporte ferroviário perdem passageiros caso não distribuam jornais diários nas estações centrais.",
        "B",
        "**Etapa 1:** Diferenciar ética pessoal privada (amizade, lealdade individual) da ética pública institucional do Estado.\n**Etapa 2:** Concluir com Robert Goodin: o Estado republicano não pode privilegiar amigos; seu dever moral supremo é a imparcialidade e a maximização da saúde, educação e segurança para a totalidade dos cidadãos, legitimando o utilitarismo público."
    ))

    questoes_brutas.append((
        59, "EM13CHS504", "dificil",
        "Na reflexão sobre a Justiça Intergeracional e o Esgotamento de Recursos Naturais Não Renováveis, qual acusação de miopia moral o utilitarismo contemporâneo formula contra os modelos econômicos de crescimento infinito baseados exclusivamente no PIB anual?",
        "A de que os economistas neoclássicos desconheciam as técnicas de extração de sal marinho em praias litorâneas.",
        "A denúncia de que esses modelos operam com uma taxa de desconto temporal imoral, queimando recursos finitos e gerando riqueza rápida para a minoria viva hoje às custas da desertificação, do caos climático e da miséria de bilhões de seres humanos que habitarão o planeta no futuro.",
        "A afirmação de que as empresas mineradoras deveriam utilizar pás manuais de madeira para extrair minério de ferro.",
        "A exigência de que os tratados comerciais internacionais sejam assinados exclusivamente nas primeiras horas da manhã de domingo.",
        "A tese de que a queima de petróleo em indústrias químicas melhora a fertilidade de solos agrícolas em planícies alagadas.",
        "B",
        "**Etapa 1:** Criticar o consumismo imediatista e o produtivismo predatório sob a ótica da extensão temporal da utilidade.\n**Etapa 2:** Concluir com a sustentabilidade planetária: a vida e a capacidade de ser feliz de quem nascerá daqui a cem anos têm valor moral idêntico ao de quem vive hoje; destruir o futuro para enriquecer no presente é uma monstruosidade utilitária."
    ))

    questoes_brutas.append((
        60, "EM13CHS502", "dificil",
        "Analise a seguinte passagem de John Stuart Mill em O Utilitarismo: 'A moral utilitarista reconhece no ser humano o poder de sacrificar o seu próprio maior bem pelo bem dos outros. Ela recusa apenas admitir que o sacrifício seja em si mesmo um bem. Um sacrifício que não aumente nem tenda a aumentar a soma total da felicidade é considerado um desperdício inútil.' Qual síntese sobre o altruísmo e o valor do sacrifício essa passagem consagra?",
        "Que as pessoas que praticam atos heróicos devem ser punidas pelos tribunais civis com o confisco de suas propriedades.",
        "Que o autêntico heroísmo moral não reside na exaltação mórbida do martírio ou da dor pela dor, mas na eficácia prática do sacrifício em aliviar o sofrimento real e expandir a felicidade coletiva de outros seres conscientes no mundo.",
        "Que os governantes de cidades industriais devem proibir a doação de sangue em hospitais públicos municipais.",
        "Que os jovens que estudam em escolas públicas devem trabalhar dezoito horas diárias em plantações de cana-de-açúcar.",
        "Que o valor de uma vida humana deve ser calculado pela quantidade de moedas de prata que o indivíduo gasta em banquetes.",
        "B",
        "**Etapa 1:** Interpretar a recusa do ascetismo mórbido e da dor gratuita na ética utilitarista de Mill.\n**Etapa 2:** Concluir com a nobreza do altruísmo eficaz: o sacrifício de dar a vida pelo próximo é o mais sublime ato de generosidade moral, mas seu valor repousa exclusivamente no fato de que salva vidas e gera felicidade real, e não no culto doentio do sofrimento."
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
capitulo: "cap-12-utilitarismo-bentham-mill"
objeto_de_conhecimento: "A Filosofia Consequencialista: Jeremy Bentham e o Princípio da Maior Felicidade para o Maior Número; O Cálculo Felicífico e o Princípio da Utilidade; A Revisão Qualitativa de John Stuart Mill: Prazeres Superiores (Intelectuais e Morais) vs. Inferiores (Sensoriais); O Princípio do Dano (Harm Principle); Dilemas Éticos Contemporâneos."
ebook_fonte: "em-fil-c12-utilitarismo-bentham-mill.md"
habilidades: "EM13CHS101, EM13CHS501, EM13CHS502, EM13CHS504, H1, H2, H16, H17, H18"
total_exercicios: 60
distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"
---

# Exercícios: A Ética Utilitarista: Consequencialismo e Bem-Estar Coletivo

"""

    corpo = header
    slug_cap = "cap-12-utilitarismo-bentham-mill"

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

- BENTHAM, Jeremy. *Uma Introdução aos Princípios da Moral e da Legislação*. Tradução de Luiz João Baraúna. São Paulo: Abril Cultural, 1984. (Coleção Os Pensadores).
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/Secretaria de Educação Básica, 2018.
- CHAUÍ, Marilena. *Convite à Filosofia*. 13. ed. São Paulo: Ática, 2002.
- MARCONDES, Danilo. *Textos Básicos de Ética: De Platão a Foucault*. 2. ed. Rio de Janeiro: Jorge Zahar, 2007.
- MILL, John Stuart. *O Utilitarismo*. Tradução de Pedro Galvão. Porto: Porto Editora, 2005.
- MILL, John Stuart. *Sobre a Liberdade*. Tradução de Alberto da Rocha Barros. São Paulo: Hedra, 2002.
- SANDEL, Michael J. *Justiça: O que é Fazer a Coisa Certa*. Tradução de Heloísa Matias e Maria Alice Máximo. 3. ed. Rio de Janeiro: Civilização Brasileira, 2011.
- SINGER, Peter. *Ética Prática*. Tradução de Jefferson Luiz Camargo. 3. ed. São Paulo: Martins Fontes, 2002.
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

    dest_rel = "content/medio/volume-unico/filosofia/eixo-2-etica/cap-12-utilitarismo-bentham-mill/ebooks/em-fil-c12-utilitarismo-bentham-mill-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_path, dest_rel]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("[SUCESSO TOTAL] Cap 12 validado e homologado com Exit Code 0!")
    else:
        print(f"[FALHA NA VALIDAÇÃO] Exit code: {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
