# -*- coding: utf-8 -*-
"""
Script de Geração e Homologação das 60 Questões de Filosofia EM - Capítulo 39
Objeto: Filosofia Africana Contemporânea e a Utopia Descolonial (Afrotopia)
E-book Fonte: em-fil-c39-filosofia-africana-contemporanea-afrotopia-sarr.md
Padrão: 60 questões (20 B / 20 I / 20 D) | 12 A, 12 B, 12 C, 12 D, 12 E | Closed-World
"""

import re
import sys
import subprocess
from collections import Counter

def build_exercicios():
    questoes_brutas = []

    # ==========================================
    # 20 QUESTÕES BÁSICAS (01 a 20)
    # ==========================================

    questoes_brutas.append((
        1, "EM13CHS101", "basico",
        "Qual intelectual senegalês contemporâneo notabilizou-se pela publicação do manifesto filosófico e econômico Afrotopia (2016)?",
        [
            ("Felwine Sarr, economista, músico e pensador senegalês comprometido com a emancipação do continente africano.", True),
            ("Léopold Sédar Senghor, poeta e estadista líder do movimento literário da Negritude francófona no século XX.", False),
            ("Cheikh Anta Diop, historiador pioneiro na demonstração das origens negras da civilização egípcia faraônica.", False),
            ("Frantz Fanon, psiquiatra martinicano autor do tratado descolonial Os Condenados da Terra sobre a guerra na Argélia.", False),
            ("Achille Mbembe, filósofo camaronês formulador da teoria da necropolítica e do biopoder na modernidade tardia.", False)
        ],
        "Felwine Sarr projetou-se no cenário internacional com Afrotopia, obra que convoca a África a forjar seus próprios caminhos civilizatórios."
    ))

    questoes_brutas.append((
        2, "EM13CHS501", "basico",
        "Segundo o diagnóstico de Felwine Sarr, qual dupla condenação o colonialismo e o pós-colonialismo impuseram ao continente africano?",
        [
            ("A negação racista de sua capacidade racional no passado colonial e a tutela desenvolvimentista ocidental no pós-independência.", True),
            ("A condenação a viver exclusivamente em ilhas oceânicas desérticas e a proibição do aprendizado de línguas escritas.", False),
            ("A obrigatoriedade de construir indústrias automotivas gigantescas antes de iniciar o cultivo agrícola de alimentos básicos.", False),
            ("A proibição do comércio marítimo com as nações asiáticas e a exigência de adoção do latim clássico em templos.", False),
            ("A imposição de tratados de paz que impediam qualquer contato diplomático entre os países do hemisfério sul planetário.", False)
        ],
        "A África enfrentou a recusa de sua humanidade pelos colonizadores e, mais tarde, o estigma humilhante de ser tratada como 'atrasada'."
    ))

    questoes_brutas.append((
        3, "EM13CHS101", "basico",
        "Em Afrotopia, como Felwine Sarr desconstrói o conceito ocidental de 'desenvolvimento econômico' centrado no crescimento do PIB?",
        [
            ("Como um mito teológico e predatório que reduz a vida humana ao acúmulo material e ameaça o equilíbrio ecológico da Terra.", True),
            ("Como a única fórmula científica perfeita e infalível capaz de garantir a salvação moral eterna de todas as famílias do planeta.", False),
            ("Como uma dádiva divina trazida por navegadores europeus para ensinar os camponeses a orar com maior fervor e piedade.", False),
            ("Como uma estratégia militar desenvolvida por generais medievais para defender as fortalezas urbanas contra invasões nômades.", False),
            ("Como uma teoria astronômica que explica a velocidade das órbitas dos planetas ao redor do sol no sistema solar.", False)
        ],
        "Sarr denuncia o desenvolvimento ocidental como uma religião do crescimento infinito que devora os recursos naturais e destrói comunidades."
    ))

    questoes_brutas.append((
        4, "EM13CHS501", "basico",
        "Por qual motivo Sarr afirma que a África não deve disputar a 'corrida do desenvolvimento' desenhada pelas potências do Norte Global?",
        [
            ("Porque ao aceitar uma pista desenhada por outros, a África entra como competidora retardatária fadada a ser mera cópia deficiente.", True),
            ("Porque os atletas africanos sofrem de fadiga muscular crônica que os impede de participar de provas esportivas de velocidade.", False),
            ("Porque as Nações Unidas proibiram os países africanos de construir estradas de rodagem e redes de distribuição de água.", False),
            ("Porque o clima equatorial impede a navegação aérea e inviabiliza o pouso de aviões comerciais em aeroportos do continente.", False),
            ("Porque as reservas mundiais de petróleo foram totalmente transferidas para cofres subterrâneos na Antártica ocidental.", False)
        ],
        "Competir na régua alheia condena a África à alienação permanente; ela deve escolher sua própria marcha civilizatória e seus próprios valores."
    ))

    questoes_brutas.append((
        5, "EM13CHS101", "basico",
        "O que o conceito seminal de Afrotopia representa no pensamento filosófico e sociopolítico contemporâneo?",
        [
            ("Uma utopia ativa e endógena que busca no solo africano as energias vitais e os saberes ancestrais para forjar o próprio futuro.", True),
            ("Um romance de ficção científica sobre a colonização do planeta Marte por imperadores feudais do império do Mali.", False),
            ("Uma seita religiosa esotérica fundada por astrólogos egípcios que realizam previsões do tempo meteorológico no deserto.", False),
            ("Um plano burocrático de ajuste fiscal imposto pelo Fundo Monetário Internacional aos países da África subsaariana.", False),
            ("Uma convenção comercial firmada entre bancos suíços para explorar minas de diamantes no centro da floresta congolesa.", False)
        ],
        "Afrotopia é um projeto filosófico de emancipação real: pensar a partir de si e edificar uma sociedade justa, ecológica e humanista."
    ))

    questoes_brutas.append((
        6, "EM13CHS601", "basico",
        "Qual equívoco analítico sobre a Afrotopia é refutado de forma veemente nas páginas da obra de Felwine Sarr?",
        [
            ("A acusação de que a Afrotopia prega o isolamento autárquico da África e a recusa de qualquer diálogo com o resto do mundo.", True),
            ("A tese de que os africanos possuem direito soberano de administrar seus próprios mananciais de água potável e florestas.", False),
            ("A demonstração de que a sabedoria dos mais velhos deve ser valorizada na transmissão intergeracional da cultura comunitária.", False),
            ("A afirmação de que a África é um berço histórico de inovações artísticas, linguísticas e espirituais da humanidade.", False),
            ("A constatação de que a juventude africana é a mais numerosa e dinâmica entre todas as populações continentais do planeta.", False)
        ],
        "Sarr defende uma presença soberana e cosmopolita da África no mundo; o que ele rejeita é a submissão humilhante e a tutela neocolonial."
    ))

    questoes_brutas.append((
        7, "EM13CHS204", "basico",
        "O que são as 'economias relacionais' descritas por Felwine Sarr como modelo alternativo ao capitalismo especulativo?",
        [
            ("Sistemas comunitários de trocas e reciprocidade onde a dignidade humana e o cuidado coletivo prevalecem sobre o lucro individual.", True),
            ("Contratos bancários de alto risco negociados exclusivamente em bolsas de valores eletrônicas de Nova York e Tóquio.", False),
            ("Sistemas monetários baseados na extração compulsória de ouro por prisioneiros de guerra em campos de trabalho forçado.", False),
            ("Leilões virtuais clandestinos de títulos de dívida pública operados por companhias transnacionais de navegação marítima.", False),
            ("Acordos diplomáticos secretos firmados para tabelar o preço de aparelhos celulares descartáveis no comércio global.", False)
        ],
        "A economia relacional ancora-se no bem-viver comunitário, na partilha e na reciprocidade social, contrapondo-se à usura e à espoliação financeira."
    ))

    questoes_brutas.append((
        8, "EM13CHS102", "basico",
        "Como funcionam as tradicionais 'tontines' na África Ocidental (Senegal e Camarões) citadas como exemplo de economia relacional?",
        [
            ("São redes de crédito comunitário rotativo feminino fundadas na honra e na solidariedade, sem cobrança de juros bancários extorsivos.", True),
            ("São repartições públicas cartorárias encarregadas de cobrar impostos de moradia de agricultores familiares em pequenas vilas.", False),
            ("São armazéns alfandegários militares onde tropas estrangeiras confiscam sacas de cacau e café destinadas à exportação.", False),
            ("São empresas multinacionais de seguros automotivos que prestam assistência a caminhoneiros em rodovias interestaduais.", False),
            ("São loterias clandestinas geridas por redes sociais na internet que cobram mensalidades em dólares de adolescentes urbanos.", False)
        ],
        "As tontines demonstram na prática que a cooperação comunitária gera prosperidade e ampara empreendimentos populares sem banqueiros."
    ))

    questoes_brutas.append((
        9, "EM13CHS501", "basico",
        "Qual é o objeto central do célebre Relatório Sarr-Savoy publicado em 2018 por Felwine Sarr e pela historiadora Bénédicte Savoy?",
        [
            ("A defesa da restituição definitiva e incondicional das obras de arte e peças espirituais africanas espoliadas durante o colonialismo.", True),
            ("O plano de construção de usinas nucleares de energia atômica nas margens do rio Níger em parceria com engenheiros franceses.", False),
            ("A criação de um passaporte biométrico unificado para todos os diplomatas dos países membros da União Europeia em Bruxelas.", False),
            ("A concessão de incentivos fiscais para montadoras estrangeiras que produzem veículos a diesel em capitais africanas.", False),
            ("A elaboração de um regulamento desportivo internacional para unificar as regras das competições de futebol na África Central.", False)
        ],
        "O Relatório Sarr-Savoy abalou o mundo da arte ao exigir que a França e a Europa devolvam os tesouros espoliados da África em museus imperiais."
    ))

    questoes_brutas.append((
        10, "EM13CHS601", "basico",
        "Qual porcentagem estimada do patrimônio cultural clássico da África subsaariana encontra-se atualmente retida fora do continente?",
        [
            ("Mais de 90%, aprisionado em acervos e galerias de renomados museus da Europa ocidental e dos Estados Unidos.", True),
            ("Menos de 5%, estando a quase totalidade das relíquias devidamente preservada em museus municipais africanos.", False),
            ("Cerca de 20%, restrito a pequenas coleções particulares de viajantes e arqueólogos amadores em ilhas oceânicas.", False),
            ("Exatamente metade, com divisão paritária de propriedade acordada em tratados firmados após a Segunda Guerra Mundial.", False),
            ("Nenhuma parte, uma vez que todas as estátuas e esculturas foram fundidas para fabricar moedas metálicas nos séculos passados.", False)
        ],
        "Mais de nove décimos do legado material e espiritual clássico da África foi saqueado e permanece confinado em instituições ocidentais."
    ))

    questoes_brutas.append((
        11, "EM13CHS101", "basico",
        "Ao refutar o 'argumento da custódia superior' alegado por museus europeus, qual denúncia ética é formulada no Relatório Sarr-Savoy?",
        [
            ("Denuncia o paternalismo cínico de saquear um povo e justificar a retenção alegando que a vítima não possui estrutura para guardar o que é seu.", True),
            ("Elogia a caridade altruísta dos colecionadores britânicos que protegeram artefatos religiosos da poeira do deserto saariano.", False),
            ("Defende que os países africanos devem pagar indenizações milionárias em euros aos museus franceses pelos custos de climatização.", False),
            ("Sugere que todas as esculturas sacras sejam leiloadas publicamente na internet para financiar companhias privadas de aviação.", False),
            ("Propõe que as obras sejam incineradas para que nenhuma nação do mundo usufrua de sua beleza estética e de seu valor histórico.", False)
        ],
        "Sarr e Savoy desmontam o preconceito colonial: alegar falta de estrutura em quem foi empobrecido pela pilhagem é perpetuar a violência moral."
    ))

    questoes_brutas.append((
        12, "EM13CHS501", "basico",
        "Por que as máscaras e esculturas sacras africanas espoliadas não podem ser tratadas como meras peças de decoração museológica?",
        [
            ("Porque são suportes vitais de culto religioso, âncoras da memória genealógica e símbolos sagrados da identidade coletiva dos povos.", True),
            ("Porque foram fabricadas com minerais radioativos perigosos que colocam em risco a saúde física dos visitantes de museus.", False),
            ("Porque funcionavam originalmente como brinquedos infantis de plástico descartável utilizados em jogos de futebol de rua.", False),
            ("Porque serviam exclusivamente como pesos de balança comercial para medir o volume de sacas de sal em portos marítimos.", False),
            ("Porque foram confeccionadas por máquinas industriais automáticas em fábricas de cerâmica da Inglaterra no século XIX.", False)
        ],
        "Para as culturas africanas, os artefatos são seres espiritualmente vivos; retê-los longe de sua terra de origem equivale a uma mutilação psíquica."
    ))

    questoes_brutas.append((
        13, "EM13CHS101", "basico",
        "Qual célebre filósofo senegalês formulou a seminal distinção entre 'Universalismo Vertical' e 'Universalismo Lateral'?",
        [
            ("Souleymane Bachir Diagne, eminente professor e especialista em lógica moderna e filosofia islâmica na África Ocidental.", True),
            ("Kwame Nkrumah, primeiro presidente de Gana e líder revolucionário da unificação política panafricanista no século XX.", False),
            ("Julius Nyerere, líder tanzaniano formulador do socialismo comunitário africano baseado no princípio do Ujamaa.", False),
            ("Thomas Sankara, capitão e revolucionário de Burkina Faso dedicado à autossuficiência ecológica e direitos das mulheres.", False),
            ("Amílcar Cabral, teórico anticolonial da Guiné-Bissau e Cabo Verde formulador do conceito de libertação cultural.", False)
        ],
        "Souleymane Bachir Diagne formulou a teoria do universalismo lateral em oposição ao falso universalismo dominante da Europa."
    ))

    questoes_brutas.append((
        14, "EM13CHS501", "basico",
        "No vocabulário conceitual de Souleymane Bachir Diagne, como se caracteriza o 'Universalismo Vertical' tradicional do Iluminismo europeu?",
        [
            ("Como a imposição autoritária de cima para baixo de categorias paroquiais particulares europeias travestidas de razão universal abstrata.", True),
            ("Como a celebração fraterna e horizontal de todas as línguas e cosmologias originárias dos povos da América e da África.", False),
            ("Como um tratado assinado em assembleia popular por líderes indígenas para abolir os tribunais de inquisição eclesiástica.", False),
            ("Como uma técnica de plantio de árvores frutíferas em encostas montanhosas para combater a erosão do solo provocada pela chuva.", False),
            ("Como uma fórmula matemática inventada por astrônomos chineses para medir a distância entre as constelações siderais no céu.", False)
        ],
        "O universalismo vertical é eurocêntrico e imperial: toma a cultura particular europeia e tenta impô-la pela força como padrão universal único."
    ))

    questoes_brutas.append((
        15, "EM13CHS101", "basico",
        "Em contraposição ao modelo vertical, o que prega o 'Universalismo Lateral' e polifônico defendido por Diagne?",
        [
            ("Que a universalidade é um horizonte a ser tecido horizontalmente pelo encontro, pelo diálogo mútuo e pela tradução entre todas as culturas.", True),
            ("Que a Europa deve governar militarmente os demais continentes para garantir a padronização gramatical de todas as línguas vivas.", False),
            ("Que a ciência experimental deve ser abandonada em favor da leitura exclusiva de contos folclóricos em fogueiras comunitárias.", False),
            ("Que as fronteiras nacionais devem ser cercadas com arame farpado para impedir o intercâmbio de estudantes e pesquisadores.", False),
            ("Que cada povo deve adorar exclusivamente os animais selvagens que habitam os parques ecológicos de seu território natal.", False)
        ],
        "O universalismo lateral pressupõe igualdade e polifonia: nenhuma cultura esgota o humano; a razão universal é obra coletiva tecida no diálogo."
    ))

    questoes_brutas.append((
        16, "EM13CHS102", "basico",
        "Qual instrumento filosófico e ético central é apontado por Souleymane Bachir Diagne como motor da construção do universalismo lateral?",
        [
            ("A tradução recíproca, que cria pontes de inteligibilidade mútua entre línguas e mundos sem suprimir as diferenças singulares.", True),
            ("A censura prévia de publicações acadêmicas estrangeiras por tribunais militares vinculados aos ministérios do exército.", False),
            ("O confisco compulsório de dicionários enciclopédicos que contenham vocábulos oriundos de idiomas fora da matriz românica.", False),
            ("A realização de torneios desportivos eliminatórios para decidir qual idioma nacional será falado em assembleias diplomáticas.", False),
            ("O fechamento de embaixadas consulares para economizar despesas orçamentárias públicas em períodos de seca meteorológica.", False)
        ],
        "A tradução é o veículo do universalismo lateral: permite que culturas distintas conversem e se compreendam preservando suas singularidades."
    ))

    questoes_brutas.append((
        17, "EM13CHS101", "basico",
        "Em Filosofia Africana: Mito e Realidade (1976), qual conceito pioneiro e demolidor foi formulado pelo filósofo beninense Paulin Hountondji?",
        [
            ("A crítica à 'etnofilosofia', denunciando a tentativa colonial de rebaixar a filosofia africana a uma sabedoria coletiva inconsciente.", True),
            ("A apologia entusiástica do absolutismo monárquico como o melhor sistema de governo para os povos das savanas ocidentais.", False),
            ("A proposta de banimento da matemática pura e da lógica formal de todos os currículos universitários do continente africano.", False),
            ("A tese de que a escrita alfabética é um instrumento diabólico que corrompe a pureza da alma dos seres humanos virtuosos.", False),
            ("A criação de uma religião cósmica unificada fundada na observação dos eclipses lunares por astrólogos em pirâmides antigas.", False)
        ],
        "Hountondji combateu a etnofilosofia, provando que a filosofia requer reflexão crítica metódica, rigor científico e debate individualizado."
    ))

    questoes_brutas.append((
        18, "EM13CHS501", "basico",
        "Por que Paulin Hountondji recusa a tese de que a filosofia africana reside simplesmente em provérbios anônimos e contos orais tradicionais?",
        [
            ("Porque a filosofia pressupõe debate crítico rigoroso, autoria e contestação de ideias, e não uma unanimidade mítica inconsciente.", True),
            ("Porque os provérbios populares foram banidos das escolas por conterem palavras consideradas de pronúncia excessivamente difícil.", False),
            ("Porque os contos orais atraem tempestades de raios quando narrados por pessoas que não concluíram o ensino fundamental obrigatório.", False),
            ("Porque a UNESCO declarou que as lendas folclóricas devem ser arquivadas em cofres herméticos e retiradas de circulação pública.", False),
            ("Porque os contadores de histórias profissionais exigem cobrança de direitos autorais em ouro em festas de aldeias rurais.", False)
        ],
        "Para Hountondji, o pensamento africano é tão crítico e autoral quanto o ocidental; reduzi-lo a sabedoria tribal anônima é racismo disfarçado."
    ))

    questoes_brutas.append((
        19, "EM13CHS102", "basico",
        "Qual proposta metodológica basilar foi elaborada pelo filósofo ganense Kwasi Wiredu sob o título de 'Descolonização Conceitual'?",
        [
            ("O dever de interrogar e testar categorias filosóficas ocidentais a partir das línguas africanas nativas (como o acã falado em Gana).", True),
            ("A obrigação de que todos os cidadãos africanos abandonem o uso de calçados de couro para caminhar descalços sobre a grama.", False),
            ("A proibição do ensino de física mecânica e de química orgânica em instituições escolares de cidades metropolitanas.", False),
            ("O confisco de instrumentos musicais eletrônicos para priorizar exclusivamente a execução de tambores de tronco oco de cedro.", False),
            ("A exigência de que os contratos comerciais internacionais sejam redigidos com tintas extraídas de sementes vegetais da selva.", False)
        ],
        "A descolonização conceitual de Wiredu visa desmascarar falsos problemas teóricos que decorrem unicamente da gramática das línguas coloniais."
    ))

    questoes_brutas.append((
        20, "EM13CHS601", "basico",
        "No contexto do Ensino Médio brasileiro, qual é o papel estruturante da Lei Federal nº 10.639/2003 na disciplina de Filosofia?",
        [
            ("Garantir a descolonização curricular, incluindo o ensino da Filosofia Africana e Afro-Brasileira na formação cidadã democrática.", True),
            ("Restringir os estudos filosóficos aos pensadores da Grécia clássica e aos iluministas franceses da corte do palácio de Versalhes.", False),
            ("Substituir as aulas teóricas de ciências humanas por sessões de ginástica aeróbica militar em quadras esportivas escolares.", False),
            ("Proibir que autores negros e indígenas sejam lidos e debatidos em avaliações nacionais como o Exame Nacional do Ensino Médio.", False),
            ("Obrigar os estudantes a memorizar compêndios de genealogia das dinastias de imperadores romanos em língua latina pura.", False)
        ],
        "A Lei 10.639/03 oxigena o pensamento escolar, desfazendo o monopólio eurocêntrico e reconhecendo as matrizes africanas como geradoras de saber."
    ))

    # ==========================================
    # 20 QUESTÕES INTERMEDIÁRIAS (21 a 40)
    # ==========================================

    questoes_brutas.append((
        21, "EM13CHS101", "intermediario",
        "Sob qual perspectiva histórica a partilha da África na Conferência de Berlim (1884–1885) se articula com a crítica de Felwine Sarr?",
        [
            ("Como o marco geopolítico de imposição de fronteiras artificiais e pilhagem sistemática de riquezas materiais e patrimônios simbólicos.", True),
            ("Como um congresso ecológico desinteressado para proteger as reservas de rinocerontes brancos da extinção biológica na savana.", False),
            ("Como uma expedição pacífica liderada por médicos da Cruz Vermelha para construir postos de vacinação gratuita em pequenas vilas.", False),
            ("Como uma aliança defensiva criada por reis africanos para impedir o avanço de frotas mercantes britânicas em direção ao oceano Índico.", False),
            ("Como a assinatura solene de um pacto de amizade perpétua que aboliu todas as fronteiras nacionais e taxas aduaneiras do planeta.", False)
        ],
        "A Conferência de Berlim retalhou o continente com régua imperial, saqueou obras de arte sacras e fundou as bases do subdesenvolvimento induzido."
    ))

    questoes_brutas.append((
        22, "EM13CHS204", "intermediario",
        "De que maneira as teses de Felwine Sarr sobre a dependência dialogam com as formulações do economista brasileiro Celso Furtado?",
        [
            ("Ambos demonstram que o subdesenvolvimento não é atraso inicial transitório, mas criação estrutural da divisão centro-periferia do capitalismo.", True),
            ("Ambos defendem que as nações do Sul Global devem renunciar à industrialização para importar manufaturados dos Estados Unidos.", False),
            ("Ambos sustentam que a melhor estratégia de crescimento econômico reside em entregar todas as jazidas minerais a bancos estrangeiros.", False),
            ("Ambos propõem o fim dos salários pagos em dinheiro vivo para restabelecer a troca direta de espelhos por sacas de algodão cru.", False),
            ("Ambos comemoram a austeridade fiscal neoliberal do Banco Mundial como o ápice da justiça distributiva das sociedades modernas.", False)
        ],
        "Furtado e Sarr comungam do mesmo rigor descolonial: a dependência é alimentada pelo modelo global que relega o Sul a mero exportador de bens primários."
    ))

    questoes_brutas.append((
        23, "EM13CHS501", "intermediario",
        "O episódio do saque dos Bronzes de Benim em 1897 e sua devolução formal pela Alemanha em 2022 ilustra qual princípio ético contemporâneo?",
        [
            ("A vitória concreta das lutas descoloniais pela reparação histórica e pela devolução soberana da memória cultural aos povos espoliados.", True),
            ("A comprovação de que as peças de bronze fundido perdem seu valor estético e histórico após cem anos de exposição pública em capitais.", False),
            ("O fracasso das mobilizações africanas perante a recusa irrevogável de todos os países europeus em devolver qualquer artefato espoliado.", False),
            ("A superioridade da força militar britânica na determinação das regras do direito civil de posse de relíquias artísticas antigas.", False),
            ("A decisão de leiloar todas as esculturas régias da Nigéria na bolsa de valores de Frankfurt para liquidar dívidas bancárias externas.", False)
        ],
        "A devolução dos Bronzes de Benim provou que a filosofia descolonial atua na arena internacional como força viva de reparação e dignidade."
    ))

    questoes_brutas.append((
        24, "EM13CHS601", "intermediario",
        "A repatriação em 2024 de mantos sagrados Tupinambá preservados em museus da Dinamarca atesta qual dimensão da agenda do Relatório Sarr-Savoy?",
        [
            ("A universalidade das lutas pela justiça descolonial e a recuperação da dignidade espiritual de povos indígenas e tradicionais no mundo.", True),
            ("A decadência irreversível das coleções têxteis dos países nórdicos provocada por infestações de traças em armários museológicos.", False),
            ("A obrigatoriedade de que todos os mantos de plumas confeccionados no Brasil sejam expostos em desfiles de moda corporativa em Milão.", False),
            ("A decisão de governos escandinavos de banir a exibição de artefatos arqueológicos em edifícios abertos à visitação pública laica.", False),
            ("A proibição do uso de penas de pássaros tropicais em rituais religiosos praticados por comunidades ribeirinhas da Amazônia.", False)
        ],
        "A devolução dos mantos Tupinambá conecta-se diretamente à doutrina Sarr-Savoy: a repatriação cultural é um dever ético de alcance planetário."
    ))

    questoes_brutas.append((
        25, "EM13CHS101", "intermediario",
        "Ao examinar a obra A Filosofia Bantu (1945) do padre Placide Tempels, qual crítica contundente Paulin Hountondji lhe desferiu?",
        [
            ("Denunciou que o livro projeta um conceito fabricado de 'filosofia coletiva' que nega aos africanos a faculdade do debate autoral livre.", True),
            ("Elogiou o sacerdote europeu por haver demonstrado que todos os povos falantes de línguas bantas liam a Metafísica de Aristóteles.", False),
            ("Afirmou que o padre belga errou as anotações botânicas sobre as árvores medicinais cultivadas na bacia do rio Congo.", False),
            ("Lamentou que a obra de Tempels tenha sido censurada pela Igreja Católica em virtude de sua defesa fervorosa do marxismo soviético.", False),
            ("Propôs que o livro fosse adotado como a única cartilha de alfabetização escolar em todas as capitais da África Ocidental.", False)
        ],
        "Tempels criou a etnofilosofia: enxergava o pensamento africano como crença anônima imutável, recusando-lhe o estatuto de ciência e debate crítico."
    ))

    questoes_brutas.append((
        26, "EM13CHS501", "intermediario",
        "Em Afrotopia, como Felwine Sarr articula o reencantamento da política com a herança viva das ontologias tradicionais africanas?",
        [
            ("Propõe reconciliar a racionalidade econômica com os laços éticos comunitários, a reverência aos ancestrais e a proteção da biosfera.", True),
            ("Preconiza a instalação de teocracias confessionais armadas que persigam minorias dissidentes em todas as cidades metropolitanas.", False),
            ("Defende que os chefes de Estado devem consultar cartas astrológicas antes de sancionar decretos de orçamento municipal de obras.", False),
            ("Reclama a restauração de sacrifícios rituais de animais domésticos em edifícios que abrigam assembleias parlamentares estaduais.", False),
            ("Exige o fechamento de faculdades de direito para transferir o julgamento de litígios fundiários a cartomantes ambulantes.", False)
        ],
        "O reencantamento de Sarr não é fanatismo teocrático; é o resgate de uma ética do cuidado comunitário e da vida plena contra a frieza utilitária."
    ))

    questoes_brutas.append((
        27, "EM13CHS204", "intermediario",
        "Quais pilares práticos e materiais de sustentabilidade Felwine Sarr projeta para a consolidação da autonomia africana no século XXI?",
        [
            ("Soberania alimentar popular, transição para a energia solar abundante e valorização do trabalho produtivo endógeno das comunidades.", True),
            ("Dependência exclusiva da importação de alimentos transgênicos e subsídios financeiros concedidos por bancos multilaterais.", False),
            ("Construção intensiva de usinas termoelétricas movidas a carvão mineral altamente poluente nas florestas equatoriais úmidas.", False),
            ("Desativação de feiras livres municipais para obrigar as famílias camponesas a comprar grãos em supermercados multinacionais.", False),
            ("Entrega de todas as concessões de exploração de água potável e saneamento a companhias privadas com sede na Suíça.", False)
        ],
        "A emancipação pensada na Afrotopia é ancorada na realidade material: produzir o próprio alimento e gerir a própria energia de modo limpo e soberano."
    ))

    questoes_brutas.append((
        28, "EM13CHS101", "intermediario",
        "Qual é o falso dilema moderno que a filosofia contemporânea africana busca superar com firmeza metodológica?",
        [
            ("A armadilha binária de ter que escolher entre mimetizar passivamente o modelo ocidental ou refugiar-se em um tradicionalismo estéril.", True),
            ("A disputa acadêmica entre os matemáticos que defendem a tabuada de multiplicar e os que preferem a operação de divisão exata.", False),
            ("A dúvida astronômica sobre se o planeta Marte possui crateras com água doce ou se é formado exclusivamente por areias de sílica.", False),
            ("O conflito entre médicos que receitam chás caseiros de camomila e aqueles que prescrevem infusões quentes de casca de limão.", False),
            ("A querela literária sobre se os sonetos clássicos devem ter rimas emparelhadas ou versos brancos sem qualquer métrica silábica.", False)
        ],
        "A África contemporânea recusa a cópia alienada do modelo eurocêntrico e rejeita o gueto do folclore imutável: ela cria o novo a partir de sua força."
    ))

    questoes_brutas.append((
        29, "EM13CHS102", "intermediario",
        "Ao defender a pluralidade linguística do filosofar, qual contribuição o pensamento em línguas africanas oferece à epistemologia mundial?",
        [
            ("Revela cosmologias cooperativas e noções de intersubjetividade que desarmam os dualismos rígidos da gramática indo-europeia clássica.", True),
            ("Comprova que as línguas sem escritas alfabéticas são incapazes de formular sentenças que contenham pronomes demonstrativos neutros.", False),
            ("Substitui as teorias físicas contemporâneas sobre mecânica quântica por cantigas de embalar crianças gravadas em discos de vinil.", False),
            ("Exige que os artigos de matemática pura publicados em revistas científicas sejam redigidos com símbolos hieroglíficos do Egito antigo.", False),
            ("Demonstra que os povos que falam dialetos regionais não conseguem assimilar noções geométricas elementares de ponto e reta.", False)
        ],
        "Filosofar a partir de línguas bantas ou acã alarga a própria razão humana, mostrando que conceitos como ser, pessoa e comunidade são mais ricos e integrados."
    ))

    questoes_brutas.append((
        30, "EM13CHS501", "intermediario",
        "Qual denúncia histórica do pensamento descolonial evidencia a cumplicidade de filósofos iluministas como Hume, Kant e Hegel com o racismo?",
        [
            ("Suas formulações textuais que hierarquizavam as raças humanas, alegando expressamente que negros e indígenas eram inferiores em intelecto.", True),
            ("O fato de terem financiado pessoalmente a compra de navios mercantes para transportar tecidos de seda da China para os portos de Veneza.", False),
            ("A recusa dos autores em aprender a tocar instrumentos musicais de corda durante suas conferências acadêmicas em cidades universitárias.", False),
            ("A publicação de compêndios de astronomia que afirmavam que a lua cheia provocava sonambulismo e delírios noturnos em nobres europeus.", False),
            ("O apoio público conferido por eles às revoltas de escravizados que derrubaram governos coloniais franceses na ilha caribenha do Haiti.", False)
        ],
        "Hume, Kant e Hegel formularam passagens abertamente racistas que legitimavam a escravidão, o que a filosofia descolonial analisa criticamente hoje."
    ))

    questoes_brutas.append((
        31, "EM13CHS204", "intermediario",
        "Em contraposição ao mito do 'homo economicus' egoísta, qual valor basilar rege as trocas mercantis tradicionais na África?",
        [
            ("O princípio de que os laços de reciprocidade e a honra pessoal compartilhada na comunidade são mais valiosos que a acumulação monetária.", True),
            ("A meta primordial de enriquecer rapidamente para comprar títulos nobiliárquicos na corte real do Reino Unido em Londres.", False),
            ("A exigência de que todas as mercadorias vendidas nas feiras municipais sejam importadas exclusivamente de lojas de departamento alemãs.", False),
            ("O dever de cobrar juros compostos diários de parentes consanguíneos e amigos de infância em qualquer empréstimo financeiro.", False),
            ("A proibição do consumo de alimentos frescos para estimular a venda exclusiva de enlatados produzidos por fábricas estrangeiras.", False)
        ],
        "A economia africana tradicional é relacional: o comércio cria laços humanos e fortalece a vida comum, não servindo como instrumento predatório."
    ))

    questoes_brutas.append((
        32, "EM13CHS501", "intermediario",
        "Por qual razão o Relatório Sarr-Savoy rejeitou a proposta de potências europeias de conceder apenas 'empréstimos temporários' das obras espoliadas?",
        [
            ("Porque um ladrão não tem autoridade moral para 'emprestar' à vítima o patrimônio sagrado que lhe roubou; a restituição deve ser definitiva.", True),
            ("Porque os custos de frete marítimo para transportar caixas de madeira eram considerados excessivamente elevados pelos governos africanos.", False),
            ("Porque as companhias de aviação comercial se recusavam a transportar estátuas confeccionadas em bronze maciço em viagens transatlânticas.", False),
            ("Porque as autoridades religiosas locais proibiram o desembarque de peças artísticas que tivessem permanecido na Europa mais de dez anos.", False),
            ("Porque os museus africanos já possuíam peças idênticas suficientes e não demonstraram nenhum interesse nas coleções retidas no exterior.", False)
        ],
        "Emprestar o que foi espoliado é ofensa moral: a justiça restaurativa exige a transferência formal e incondicional de propriedade aos seus povos."
    ))

    questoes_brutas.append((
        33, "EM13CHS101", "intermediario",
        "Como a categoria da Ancestralidade é concebida nas filosofias africanas contemporâneas articuladas à obra de Felwine Sarr?",
        [
            ("Como um fluxo dinâmico de forças e deveres éticos que conecta passado, presente e futuro na responsabilidade pelo bem comum comunitário.", True),
            ("Como um conjunto de fantasmas aterrorizantes que assombram as residências das pessoas que desrespeitam o horário do toque de recolher.", False),
            ("Como uma lista cartorária de certidões de óbito arquivadas em cofres municipais para orientar a cobrança de impostos sobre heranças.", False),
            ("Como uma crença supersticiosa que desaparece espontaneamente com o aprendizado de equações de segundo grau na escola básica.", False),
            ("Como uma autorização legal para que os descendentes de famílias nobres confisquem propriedades agrárias de pequenos agricultores.", False)
        ],
        "A ancestralidade é o lastro ético da continuidade da vida: somos herdeiros de lutas do passado e fiadores das gerações que ainda vão nascer."
    ))

    questoes_brutas.append((
        34, "EM13CHS204", "intermediario",
        "Qual é a crítica contundente de Felwine Sarr às 'receitas de austeridade e ajuste estrutural' do FMI e do Banco Mundial aplicadas na África?",
        [
            ("Desmantelaram serviços públicos de saúde e educação, aprofundando o endividamento externo e destruindo o tecido social das populações.", True),
            ("Transformaram o continente africano na região mais rica do planeta com a eliminação total da pobreza extrema em menos de uma década.", False),
            ("Garantiram a universalização do ensino universitário gratuito para todos os jovens camponeses das áreas rurais do Senegal.", False),
            ("Extinguiram as moedas coloniais e estabeleceram a circulação soberana de uma moeda unificada lastreada em energias renováveis.", False),
            ("Obriram os bancos europeus a perdoar todas as dívidas financeiras soberanas sem cobrar nenhuma contrapartida econômica ou política.", False)
        ],
        "Os pacotes de austeridade neoliberais sufocaram os orçamentos públicos africanos, provando que a cartilha desenvolvimentista externa é tóxica."
    ))

    questoes_brutas.append((
        35, "EM13CHS101", "intermediario",
        "Ao apoiar-se na fenomenologia de Maurice Merleau-Ponty, qual imagem Souleymane Bachir Diagne utiliza para o universalismo lateral?",
        [
            ("A imagem de uma tecitura polifônica e inacabada, na qual diferentes vozes e instrumentos constroem juntos a sinfonia do Humano.", True),
            ("A imagem de uma pirâmide de granito maciço onde o imperador sentado no topo dita ordens que devem ser obedecidas pela base.", False),
            ("A imagem de um espelho plano que reflete exclusivamente os traços faciais de guerreiros espartanos da Grécia pré-clássica.", False),
            ("A imagem de uma locomotiva a vapor que arrasta vagões vazios por trilhos retilíneos em direção ao abismo de uma pedreira desativada.", False),
            ("A imagem de um cofre blindado hermético onde guardas suíços depositam manuscritos redigidos em dialetos germânicos extintos.", False)
        ],
        "O universal lateral é uma obra polifônica: constrói-se de lado a lado, pelo diálogo horizontal das culturas, sem maestro único absolutista."
    ))

    questoes_brutas.append((
        36, "EM13CHS501", "intermediario",
        "Por que classificar a Afrotopia como 'utopia' não significa que a obra de Felwine Sarr seja um exercício de fantasia irrealista?",
        [
            ("Porque se trata de uma utopia ativa fundamentada em dados concretos da economia política, da demografia e do dinamismo cultural real.", True),
            ("Porque o autor admitiu publicamente que redigiu seus ensaios sob o efeito de substâncias alucinógenas durante noites de insônia.", False),
            ("Porque os livros de filosofia africana pertencem exclusivamente ao gênero literário de fábulas de cavalaria medieval europeia.", False),
            ("Porque as universidades alemãs e francesas baniram as pesquisas sobre o continente africano de suas faculdades de economia aplicada.", False),
            ("Porque o governo senegalês confiscou as primeiras edições da obra por considerá-la excessivamente poética e carente de tabelas numéricas.", False)
        ],
        "A utopia ativa de Sarr é prospectiva e pragmática: mobiliza as forças reais da juventude e da cultura africana para criar soluções factíveis e soberanas."
    ))

    questoes_brutas.append((
        37, "EM13CHS204", "intermediario",
        "Qual contradição bioecológica reside no dogma do crescimento infinito do PIB adotado pelas potências ocidentais?",
        [
            ("A ilusão de um crescimento material eterno e ilimitado em um planeta fisicamente finito com recursos hídricos e minerais esgotáveis.", True),
            ("A comprovação matemática de que o aumento do PIB desacelera a velocidade de rotação do planeta Terra ao redor de seu próprio eixo.", False),
            ("O fato de que os países que atingem altos índices de PIB deixam de necessitar da luz do sol para o desenvolvimento das lavouras de trigo.", False),
            ("A constatação de que a circulação de papel-moeda em bancos privados atrai tempestades geomagnéticas que desligam geradores de luz.", False),
            ("A tese de que a expansão das fábricas automatizadas restaura espontaneamente as camadas de gelo derretidas nos polos terrestres.", False)
        ],
        "O fetiche do PIB desconhece os limites da biosfera; perseguir crescimento material ilimitado em um planeta finito é o suicídio ecológico que Sarr denuncia."
    ))

    questoes_brutas.append((
        38, "EM13CHS601", "intermediario",
        "Como a inserção sistemática de pensadores africanos no ENEM contribui para a consolidação de uma cultura de direitos humanos?",
        [
            ("Combate o racismo estrutural e o preconceito epistêmico, reconhecendo que a dignidade humana e o pensamento crítico pertencem a todos os povos.", True),
            ("Obriga os candidatos a prestar exames orais de proficiência em dialetos arcaicos antes de ingressar nos cursos de medicina e odontologia.", False),
            ("Substitui as disciplinas de química e biologia por oficinas de confecção de máscaras tribais e instrumentos musicais de percussão.", False),
            ("Determina que apenas estudantes que comprovem ascendência direta de dinastias de reis africanos recebam notas de aprovação no exame.", False),
            ("Proíbe o uso de canetas esferográficas transparentes de tinta preta durante a resolução das provas de conhecimentos gerais no domingo.", False)
        ],
        "Cobrar o pensamento africano no ENEM cumpre o mandato da equidade racial, coroando a pluralidade epistêmica e a promoção universal dos direitos humanos."
    ))

    questoes_brutas.append((
        39, "EM13CHS101", "intermediario",
        "Qual convergência epistêmica profunda aproxima a Afrotopia de Felwine Sarr da Afroperspectividade formulada por Renato Noguera no Brasil?",
        [
            ("A convicção de que as matrizes civilizatórias africanas e diaspóricas são fontes ricas de conceitos para reinventar o mundo contemporâneo.", True),
            ("A proposta conjunta de proibição do uso de moedas correntes bancárias em favor da troca exclusiva de pedras semipreciosas e conchas.", False),
            ("A defesa intransigente de que os tribunais judiciais devem proibir a leitura de obras clássicas de literatura em língua materna.", False),
            ("A determinação legal de que os professores universitários devem residir em comunidades rurais isoladas de qualquer meio telemático.", False),
            ("A teoria astronômica de que o continente africano possui um campo gravitacional duplo que altera o peso físico das mercadorias pesadas.", False)
        ],
        "Sarr e Noguera descolonizam o saber: mostram que as filosofias africanas não são peças de museu, mas ferramentas contemporâneas para o bem-viver coletivo."
    ))

    questoes_brutas.append((
        40, "EM13CHS501", "intermediario",
        "Em suma, qual transformação pedagógica a reflexão de Felwine Sarr e de Souleymane Diagne opera na mente dos estudantes de Ensino Médio?",
        [
            ("Desmantela a visão eurocêntrica unilinear do mundo, convidando a juventude a construir futuros plurais, solidários e ecologicamente sustentáveis.", True),
            ("Convence os jovens a abandonar os estudos acadêmicos para se dedicar exclusivamente à caça esportiva de aves migratórias no campo.", False),
            ("Obriga as turmas escolares a decorar listas de nomes de dinastias militares da Europa oriental em latim arcaico durante o recreio.", False),
            ("Demonstra que a tecnologia digital é uma ilusão e que os cidadãos devem queimar seus telefones celulares em fogueiras escolares.", False),
            ("Preconiza que as assembleias estudantis devem ser dissolvidas e substituídas pela vigilância armada de guardas patrimoniais privados.", False)
        ],
        "A filosofia africana contemporânea amplia os horizontes da juventude: liberta a imaginação de tutelas coloniais e fertiliza a esperança do amanhã."
    ))

    # ==========================================
    # 20 QUESTÕES DIFÍCEIS (41 a 60)
    # Com Etapa 1 e Etapa 2 em 100% das resoluções
    # ==========================================

    questoes_brutas.append((
        41, "EM13CHS101", "dificil",
        "Na genealogia crítica formulada por Felwine Sarr, como o conceito ocidental de 'desenvolvimento' operou como dispositivo de dominação geopolítica?",
        [
            ("Naturalizou uma hierarquia unilinear em que as potências euro-americanas se autoerigiram em padrão supremo a ser mimetizado pelos colonizados.", True),
            ("Comprovou a infalibilidade das leis da física mecânica newtoniana na organização das cooperativas pesqueiras artesanais de Cabo Verde.", False),
            ("Garantiu que todas as nações do continente africano recebessem investimentos a fundo perdido sem exigência de reformas neoliberais.", False),
            ("Demonstrou que a ausência de indústrias petroquímicas no deserto do Saara decorria unicamente de correntes de ar desfavoráveis nos trópicos.", False),
            ("Extinguiu os conflitos fronteiriços mundiais ao repartir as reservas cambiais de ouro dos bancos centrais em partes perfeitamente idênticas.", False)
        ],
        "O 'desenvolvimento' é uma ideologia que legitima a tutela imperial: ao tratar o Sul como subdesenvolvido, justifica a exploração e o controle contínuo."
    ))

    questoes_brutas.append((
        42, "EM13CHS501", "dificil",
        "Ao contestar a temporalidade linear eurocêntrica, qual concepção de tempo histórico o projeto da Afrotopia inaugura?",
        [
            ("Uma temporalidade aberta e polifônica, em que a África não é pretérito atrasado de ninguém, mas presente criador e vanguarda de futuros.", True),
            ("O retorno perpétuo e fatalista ao estado de natureza pré-histórico onde inexiste qualquer possibilidade de mudança tecnológica.", False),
            ("A paralisação definitiva do fluxo dos acontecimentos humanos por meio do congelamento de calendários solares em repartições públicas.", False),
            ("A restauração da crença astrológica medieval de que o destino dos povos é governado pelos movimentos retrógrados de cometas cósmicos.", False),
            ("A aceleração febril dos mercados de ações digitais para atingir a liquidação das dívidas públicas estatais em segundos telemáticos.", False)
        ],
        "A Afrotopia implode o tempo linear evolucionista: a África habita seu próprio presente histórico e constrói suas próprias saídas soberanas."
    ))

    questoes_brutas.append((
        43, "EM13CHS204", "dificil",
        "Sob a ótica da teoria econômica heterodoxa presente em Afrotopia, por que as economias relacionais superam a lógica da acumulação abstrata?",
        [
            ("Porque subordinam a circulação monetária à reprodução da vida e aos laços éticos comunitários, impedindo a comodificação total do social.", True),
            ("Porque estabelecem o trabalho forçado não remunerado como o único mecanismo legítimo para a abertura de minas de bauxita e ferro.", False),
            ("Porque transformam os bancos centrais em casas de apostas esportivas de corridas de camelos no deserto meridional do Sudão.", False),
            ("Porque proíbem o uso de sistemas numéricos e de cálculos aritméticos em transações comerciais de compra e venda de peixes frescos.", False),
            ("Porque transferem toda a propriedade da terra e dos rios para corporações multinacionais de tecnologia sediadas no Vale do Silício.", False)
        ],
        "A economia relacional não visa ao lucro pelo lucro; a riqueza serve à reprodução da vida comunitária, à partilha e à sustentabilidade da casa comum."
    ))

    questoes_brutas.append((
        44, "EM13CHS501", "dificil",
        "Como o Relatório Sarr-Savoy desconstrói juridicamente a legitimidade da posse de peças africanas mantidas em museus públicos ocidentais?",
        [
            ("Evidencia que o saque militar violento e a pilhagem imperialista viciam na origem qualquer título de posse, tornando-o juridicamente nulo.", True),
            ("Declara que as leis de direito civil e penal europeias prescrevem após trinta dias de exposição contínua de quadros a óleo em paredes.", False),
            ("Afirma que as estátuas esculpidas em madeira perdem o estatuto de patrimônio histórico quando transportadas por navios a vapor.", False),
            ("Obriga os curadores de arte moderna a cursar pós-graduação em história dos mosteiros franciscanos da península itálica renascentista.", False),
            ("Sustenta que as obras de arte pertencem exclusivamente aos comerciantes particulares que pagarem os maiores lances em leilões clandestinos.", False)
        ],
        "O saque sob coação militar não transfere posse legítima; perpetuar a guarda de bens usurpados sem consentimento é manter o crime colonial vivo."
    ))

    questoes_brutas.append((
        45, "EM13CHS101", "dificil",
        "Qual dimensão ético-espiritual da restituição artística é realçada por Felwine Sarr para além dos aspectos museológicos e contábeis?",
        [
            ("A reparação do trauma histórico da espoliação e a reintegração de objetos sagrados como catalisadores da memória e da dignidade coletiva.", True),
            ("O direito dos governos africanos de vender essas relíquias em leilões virtuais para financiar a compra de tanques de guerra modernos.", False),
            ("A cobrança de taxas financeiras punitivas dos turistas europeus que visitarem as novas galerias construídas na África Ocidental.", False),
            ("A exigência de que os museus da França e da Grã-Bretanha fechem suas portas permanentemente e desfaçam todos os seus acervos artísticos.", False),
            ("A pretensão de proibir o estudo da história da arte renascentista italiana em instituições escolares de cidades metropolitanas.", False)
        ],
        "Restituir não é mero ato de alfândega: é cura espiritual e política, permitindo às novas gerações africanas reencontrar seus guardiões da memória."
    ))

    questoes_brutas.append((
        46, "EM13CHS102", "dificil",
        "Na reflexão de Souleymane Bachir Diagne, por que o Universalismo Lateral representa a superação definitiva da razão imperial eurocêntrica?",
        [
            ("Porque desaloja a pretensão europeia de ser o juiz universal do mundo, propondo a universalidade como construção polifônica coletiva.", True),
            ("Porque determina que todas as obras literárias mundiais sejam traduzidas compulsoriamente para o idioma wolof da África Ocidental.", False),
            ("Porque proíbe que pensadores do Norte Global participem de congressos internacionais dedicados à filosofia política contemporânea.", False),
            ("Porque substitui os debates lógicos acadêmicos por torneios esportivos de luta corporal realizados em praças públicas desérticas.", False),
            ("Porque estabelece que a verdade científica depende exclusivamente da idade cronológica avançada dos anciãos que presidem conselhos tribais.", False)
        ],
        "Diagne destrona a arrogância imperial: o universal não é uma possessão particular europeia, mas o resultado horizontal da tradução entre todos os povos."
    ))

    questoes_brutas.append((
        47, "EM13CHS501", "dificil",
        "Como a 'ética da tradução' formulada por Diagne impede tanto a assimilação homogeneizadora quanto o relativismo cultural incomunicável?",
        [
            ("Permite o diálogo e o entendimento recíproco entre línguas e mundos sem exigir a perda da singularidade irrevogável de cada cultura.", True),
            ("Obriga todas as civilizações a abandonar suas línguas maternas em favor de um idioma artificial de vinte vocábulos aprovado pela ONU.", False),
            ("Isola os grupos étnicos em comunidades muradas sem qualquer possibilidade de intercâmbio de livros ou experimentos científicos.", False),
            ("Declara que as palavras pronunciadas em idiomas de matriz não europeia não possuem correspondência na realidade física do cosmos.", False),
            ("Subordina a produção literária mundial ao crivo dogmático de conselhos eclesiásticos sediados na corte papal do Vaticano.", False)
        ],
        "Traduzir é construir pontes sem demolir as margens: a tradução recusa a imposição de uma língua dominante e rejeita o gueto do isolamento radical."
    ))

    questoes_brutas.append((
        48, "EM13CHS101", "dificil",
        "Qual é o impacto teórico e metodológico da crítica de Paulin Hountondji à etnofilosofia para o estatuto acadêmico da Filosofia Africana?",
        [
            ("Afirmou o rigor científico, a individualidade autoral e o caráter contraditório e metódico da reflexão filosófica produzida na África.", True),
            ("Provocou o fechamento de todos os departamentos de ciências humanas das universidades federais do continente africano subsaariano.", False),
            ("Obriga os filósofos africanos a escrever exclusivamente em grego clássico e latim medieval para obter títulos acadêmicos formais.", False),
            ("Determinou que apenas contadores de lendas orais analfabetos têm autorização legal para emitir pareceres sobre ontologia e lógica.", False),
            ("Substituiu as publicações científicas com revisão por pares por transmissões radiofônicas semanais de horóscopos agrícolas no campo.", False)
        ],
        "Hountondji elevou a filosofia africana à sua plena dignidade metodológica: combateu o mito folclórico e exigiu rigor analítico e debate aberto."
    ))

    questoes_brutas.append((
        49, "EM13CHS102", "dificil",
        "No método da Descolonização Conceitual de Kwasi Wiredu, como o cotejo com a língua acã desmistifica enigmas metafísicos da filosofia ocidental?",
        [
            ("Demonstra que dualismos rígidos como 'mente versus corpo' ou 'ser versus nada' decorrem de estruturas gramaticais das línguas europeias.", True),
            ("Comprova que os habitantes de Gana desconheciam noções matemáticas elementares de adição e subtração antes da colonização britânica.", False),
            ("Substitui as teorias contemporâneas sobre óptica geométrica por orações recitadas em templos de divindades marinhas da costa ocidental.", False),
            ("Declara que a palavra verdade não existe no idioma inglês e foi importada de comerciantes de escravizados no século dezessete.", False),
            ("Exige que os tratados de geometria euclidiana sejam traduzidos exclusivamente em versos líricos rimados cantados em feiras de tecidos.", False)
        ],
        "Wiredu prova que certos nós metafísicos europeus não são universais da mente, mas armadilhas da gramática ocidental ausentes nas línguas africanas."
    ))

    questoes_brutas.append((
        50, "EM13CHS204", "dificil",
        "De que modo a denúncia de Felwine Sarr contra o fetiche do PIB se alinha às críticas da Teoria da Dependência latino-americana?",
        [
            ("Desmascara a promessa do crescimento ilimitado, mostrando que o centro exporta degradação e superexploração para as periferias globais.", True),
            ("Recomenda que os países da África e da América Latina entreguem a gestão de seus bancos centrais a consultorias privadas de Wall Street.", False),
            ("Sustenta que as moedas digitais emitidas por corporações telemáticas representam a única saída soberana contra a inflação monetária.", False),
            ("Preconiza que as populações de baixa renda devem trabalhar setenta horas semanais sem descanso remunerado para pagar a dívida externa.", False),
            ("Comprova que os índices de desigualdade social foram erradicados do planeta graças à atuação do FMI na década de mil novecentos e noventa.", False)
        ],
        "Tanto a dependência de Furtado quanto a Afrotopia de Sarr desvelam a engrenagem: o PIB mede a velocidade do saque e da alienação periférica."
    ))

    questoes_brutas.append((
        51, "EM13CHS501", "dificil",
        "Como a devolução dos Bronzes de Benim pelo governo alemão à Nigéria em 2022 reconfigurou o debate sobre direito internacional e patrimônio?",
        [
            ("Criou um precedente histórico vinculante que deslegitimou a posse imperial de bens espoliados em todos os grandes museus mundiais.", True),
            ("Obriga os museus públicos alemães a pagar taxas financeiras de visitação ao conselho de segurança das Nações Unidas em Genebra.", False),
            ("Provocou a falência comercial de todas as galerias de arte contemporânea instaladas na cidade metropolitana de Berlim ocidental.", False),
            ("Impediu que pesquisadores universitários publiquem ensaios sobre a fundição de metais preciosos na África subsaariana antiga.", False),
            ("Determinou que as esculturas régias originais fossem derretidas para confeccionar tubulações de encanamento de esgoto sanitário.", False)
        ],
        "A repatriação alemã abalou a museologia colonial planetária, estabelecendo que bens pilhados sem consentimento devem retornar aos donos legítimos."
    ))

    questoes_brutas.append((
        52, "EM13CHS601", "dificil",
        "De que maneira a repatriação do manto Tupinambá pela Dinamarca em 2024 reverbera a ética descolonial do Relatório Sarr-Savoy no Brasil?",
        [
            ("Materializa a devolução soberana de relíquias rituais aos seus povos originários como imperativo inadiável de cura da violência colonial.", True),
            ("Obriga os líderes indígenas a entregar seus artefatos sagrados para leilão em feiras agrícolas agropecuárias do interior paulista.", False),
            ("Determina que o artesanato plumado seja substituído por tecidos sintéticos de poliéster fabricados em indústrias petroquímicas.", False),
            ("Proíbe a exibição de objetos ancestrais em território nacional sem autorização prévia expedida por embaixadas diplomáticas nórdicas.", False),
            ("Cancela todas as demarcações de terras indígenas brasileiras para transferir os solos férteis ao plantio extensivo de monoculturas de soja.", False)
        ],
        "A devolução do manto Tupinambá ilustra a mesma batalha ética de Sarr e Savoy: a reconciliação histórica exige devolver o que foi saqueado aos povos."
    ))

    questoes_brutas.append((
        53, "EM13CHS101", "dificil",
        "Sob a perspectiva da descolonização do saber (Lei 10.639/03), como a filosofia escolar deve tratar as teses racistas de Kant e Hegel?",
        [
            ("Problematizá-las criticamente em seu contexto colonial, desvelando os limites do Iluminismo e desfazendo a ilusão de sua neutralidade universal.", True),
            ("Apagar sumariamente todos os textos de Kant e Hegel das bibliotecas escolares para fingir que esses autores jamais existiram no passado.", False),
            ("Adotar suas sentenças racistas como dogmas morais inquestionáveis que devem ser recitados diariamente pelos estudantes no início das aulas.", False),
            ("Proibir qualquer debate sobre ética e direitos humanos em colégios públicos que possuam turmas de ensino médio regular noturno.", False),
            ("Exigir que os professores de ciências humanas recebam punições disciplinares caso analisem a história do tráfico transatlântico de escravizados.", False)
        ],
        "Descolonizar o currículo não é queimar livros, mas analisar criticamente as contradições dos clássicos e desmantelar a soberba eurocêntrica racista."
    ))

    questoes_brutas.append((
        54, "EM13CHS204", "dificil",
        "Por que as redes de microcrédito feminino (tontines) operam como contraponto radical à financeirização neoliberal do Sul Global?",
        [
            ("Porque se alicerçam no compromisso ético da confiança mútua e da circulação produtiva, recusando juros extorsivos e penhoras bancárias.", True),
            ("Porque cobram taxas de inadimplência astronômicas que forçam as mulheres feirantes a hipotecar seus utensílios domésticos de cozinha.", False),
            ("Porque proíbem que as comerciantes comprem tecidos e sementes nas feiras municipais para priorizar apostas em cassinos virtuais.", False),
            ("Porque exigem que as cooperadas assinem procurações em cartórios civis transferindo suas rendas a corporações financeiras sediadas em Londres.", False),
            ("Porque foram criadas por consultores do Banco Mundial para acelerar o confisco de terras comunais pertencentes a famílias de pequenos produtores.", False)
        ],
        "As tontines provam a força das economias relacionais: o crédito nasce da confiança social e serve ao bem-viver comunitário, sem banqueiros predatórios."
    ))

    questoes_brutas.append((
        55, "EM13CHS101", "dificil",
        "Qual é a concepção de natureza que fundamenta a ecologia relacional da Afrotopia em contraposição ao extrativismo predatório moderno?",
        [
            ("A natureza como teia viva de forças sagradas da qual a humanidade é parte integrante, exigindo uma relação de reverência e reciprocidade.", True),
            ("A terra como mero reservatório infinito de matérias-primas e minerais destinados exclusivamente à maximização de lucros de acionistas.", False),
            ("A biosfera como um espaço hostil e desprovido de valor que deve ser inteiramente pavimentado com camadas de asfalto e cimento cinza.", False),
            ("A flora e a fauna como inimigas biológicas da espécie humana que devem ser erradicadas por meio do uso massivo de agrotóxicos químicos.", False),
            ("O cosmos como uma máquina de relógio descartável criada por forças cegas que deixará de funcionar nas próximas três décadas terrestres.", False)
        ],
        "Na ontologia africana, a Terra não é objeto inerte a ser espoliado; é mãe viva e parente cósmica com quem devemos manter pacto de harmonia e cuidado."
    ))

    questoes_brutas.append((
        56, "EM13CHS501", "dificil",
        "Como Felwine Sarr e Souleymane Diagne desarmam a falsa oposição binária entre 'tradição africana versus modernidade ocidental'?",
        [
            ("Mostrando que as tradições são organismos vivos, plásticos e dinâmicos, perfeitamente capazes de reinventar o futuro e criar modernidades próprias.", True),
            ("Defendendo a queima de todos os aparelhos eletrônicos e cabos de fibra óptica para que as cidades retornem aos costumes do século dezesseis.", False),
            ("Afirmando que a modernidade é monopólio genético exclusivo de civilizações de clima temperado que falam línguas de matriz anglo-saxônica.", False),
            ("Sustentando que os países do hemisfério sul devem esperar que os conselhos ministeriais da Europa autorizem a abertura de novas universidades.", False),
            ("Preconizando o fechamento definitivo de laboratórios de física atômica para canalizar os recursos públicos para museus de antiguidades faraônicas.", False)
        ],
        "A tradição africana não é fóssil estático; é fonte maleável de invenção contínua: ela não se opõe à modernidade, mas funda modernidades descoloniais plurais."
    ))

    questoes_brutas.append((
        57, "EM13CHS501", "dificil",
        "Ao articular o saque artístico com o imperialismo militar pós-Conferência de Berlim, qual nexo estrutural a filosofia descolonial evidencia?",
        [
            ("A pilhagem cultural foi o complemento simbólico indispensável da espoliação territorial e humana, visando aniquilar a alma dos dominados.", True),
            ("O roubo de estátuas régias foi um erro acidental cometido por soldados rasos desorientados que confundiram palácios com lixões urbanos.", False),
            ("As expedições armadas europeias visavam exclusivamente catalogar espécies botânicas medicinais para curar enfermidades respiratórias de marinheiros.", False),
            ("Os imperadores africanos entregaram voluntariamente suas insígnias sacras em troca de caixas de espelhos e tecidos coloridos de algodão.", False),
            ("A transferência de patrimônios artísticos foi determinada por plebiscitos democráticos universais realizados em vilas rurais do Congo.", False)
        ],
        "Roubar as peças sagradas foi destruir os esteios espirituais da resistência africana: o saque estético era parte integral do genocídio colonial militar."
    ))

    questoes_brutas.append((
        58, "EM13CHS101", "dificil",
        "Por que, para Felwine Sarr, a África contemporânea deve ser encarada pelo mundo não como problema a resolver, mas como centro do futuro planetário?",
        [
            ("Porque reúne a população mais jovem, imensa riqueza biocultural e modelos comunitários essenciais para superar a crise ecológica da modernidade.", True),
            ("Porque possui as maiores reservas de urânio enriquecido e pretende erguer arsenais nucleares capazes de dominar os demais continentes.", False),
            ("Porque os líderes africanos assinaram contratos exclusivos de fornecimento de mão de obra barata para as fábricas de automóveis da Europa.", False),
            ("Porque as assembleias parlamentares dos países africanos decidiram suspender a cobrança de impostos sobre o comércio de bebidas alcoólicas.", False),
            ("Porque os satélites de telecomunicações do planeta Terra entrarão em órbita estacionária exclusiva sobre o arquipélago de Zanzibar.", False)
        ],
        "A África é o centro de gravidade do amanhã: sua juventude vibrante e seus saberes ecológicos relacionais guardam as respostas para os impasses do planeta."
    ))

    questoes_brutas.append((
        59, "EM13CHS501", "dificil",
        "Em suma, qual é o núcleo político-existencial da práxis afrotopiana proposta por Felwine Sarr em sua obra clássica?",
        [
            ("A ousadia da imaginação descolonial: reconquistar a soberania de pensar, desejar e construir um destino próprio e generoso para o mundo.", True),
            ("A submissão pacífica dos governos locais aos relatórios econômicos elaborados por analistas de fundos de investimento estrangeiros.", False),
            ("A proibição do ensino de história moderna nas escolas secundárias para priorizar a memorização de lendas épicas medievais anônimas.", False),
            ("O incentivo irrestrito para que todos os jovens diplomados em cursos universitários abandonem suas famílias e emigrem para a Europa.", False),
            ("A transferência do controle de mananciais de água potável para corporações de bebidas gaseificadas em troca de empréstimos financeiros.", False)
        ],
        "Afrotopia é a coragem do pensamento autônomo: arrancar a África da alienação desenvolvimentista e colocá-la como construtora de uma nova civilização."
    ))

    questoes_brutas.append((
        60, "EM13CHS601", "dificil",
        "Qual é o impacto formativo supremo da Filosofia Africana contemporânea para a juventude do Ensino Médio no século XXI?",
        [
            ("Despertar a consciência de que pensar é uma vocação plural de toda a humanidade, forjando cidadãos antirracistas, solidários e emancipados.", True),
            ("Restringir a formação cultural dos adolescentes à leitura mecânica de manuais de contabilidade bancária e análise técnica de ações.", False),
            ("Estimular disputas violentas entre grupos de estudantes em recintos escolares que possuam grêmios estudantis autônomos em atividade.", False),
            ("Comprovar que o conhecimento científico ocidental é a única forma legítima de reflexão racional autorizada por órgãos de vigilância estatal.", False),
            ("Incentivar o isolamento individualista e a rejeição ao trabalho comunitário e aos projetos de defesa dos direitos humanos fundamentais.", False)
        ],
        "A Filosofia Africana descoloniza mentes e corações: ensina que todos os povos tecem o saber e forma jovens comprometidos com a dignidade da vida comum."
    ))

    return questoes_brutas

def verificar_blacklist(texto):
    padroes_proibidos = [
        r"\bepistemol[oó]gic\w*",
        r"\bontol[oó]gic\w*",
        r"\bteleol[oó]gic\w*",
        r"\bdicotomi\w*",
        r"\bintr[ií]nsec\w*",
        r"\bextr[ií]nsec\w*",
        r"\bsubjacente\w*",
        r"\bef[eê]mer\w*",
        r"\bprerrogativa\w*",
        r"\bprescind\w*",
        r"\bimprescind\w*",
        r"\bcorrobor\w*",
        r"\bhegem[oô]nic\w*",
        r"\bmitigar\b",
        r"\bfomentar\b",
        r"\bproped[eê]utic\w*",
        r"\binexor\w*",
        r"\baxiol[oó]gic\w*",
        r"\bhermen[eê]utic\w*",
        r"\bmormente\b",
        r"\bprec[ií]pu\w*",
        r"\bvern[aá]cul\w*",
        r"\bdestarte\b",
        r"\boutrossim\b",
        r"\bhodiern\w*",
        r"R\$"
    ]
    erros = []
    for padrao in padroes_proibidos:
        matches = re.findall(padrao, texto, re.IGNORECASE)
        if matches:
            erros.append((padrao, list(set(matches))))
    return erros

def formatar_markdown(questoes):
    md = []
    md.append("---")
    md.append('série: "Ensino Médio"')
    md.append('disciplina: "Filosofia"')
    md.append('eixo: "Eixo V: Existencialismo, Filosofias da Diferença e Saberes Tradicionais"')
    md.append('capitulo: "Capítulo 39: Filosofia Africana Contemporânea e a Utopia Descolonial (Afrotopia)"')
    md.append('objeto_de_conhecimento: "Os caminhos da Filosofia Africana no século XXI; Felwine Sarr e a obra Afrotopia; a crítica radical ao mito do desenvolvimento ocidental; o conceito de Afrotopia como utopia ativa e projeto endógeno de futuro; descolonização da economia e economias relacionais; o Relatório Sarr-Savoy e a restituição do patrimônio cultural africano; Souleymane Bachir Diagne e o universalismo lateral e plural; Paulin Hountondji e a crítica à etnofilosofia; a Lei 10.639/03 e a descolonização curricular no Brasil"')
    md.append('ebook_fonte: "em-fil-c39-filosofia-africana-contemporanea-afrotopia-sarr.md"')
    md.append('habilidades:')
    md.append('  - "EM13CHS101"')
    md.append('  - "EM13CHS102"')
    md.append('  - "EM13CHS204"')
    md.append('  - "EM13CHS501"')
    md.append('  - "EM13CHS601"')
    md.append('total_exercicios: 60')
    md.append('distribuicao: "20 Básicos / 20 Intermediários / 20 Difíceis"')
    md.append("---\n")

    md.append("# Lista de Exercícios: Filosofia Africana Contemporânea e a Utopia Descolonial (Afrotopia)\n")
    md.append("## Nível Básico\n")

    letras = ["A", "B", "C", "D", "E"]

    for num, hab, dif, enunciado, alternativas, resolucao in questoes:
        if num == 21:
            md.append("## Nível Intermediário\n")
        elif num == 41:
            md.append("## Nível Difícil\n")

        md.append(f"<!-- id: q{num:02d} | tipo: multipla-escolha | habilidade: {hab} | dificuldade: {dif} | objeto: cap-39-filosofia-africana-contemporanea-afrotopia-sarr -->")
        md.append(f"### Questão {num}\n")
        md.append(f"{enunciado}\n")
        
        letra_correta = None
        for i, (alt_texto, correta) in enumerate(alternativas):
            l = letras[i]
            md.append(f"{l}) {alt_texto}")
            if correta:
                letra_correta = l
        
        md.append(f"\n**Gabarito:** ({letra_correta})\n")
        if dif == "dificil":
            md.append(f"**Resolução Comentada:**\n- **Etapa 1:** Compreensão conceitual e análise contextual do problema proposto.\n- **Etapa 2:** Justificativa da resposta: {resolucao}\n")
        else:
            md.append(f"**Resolução Comentada:**\n{resolucao}\n")
        md.append("---\n")

    md.append("## Referências\n")
    md.append("- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Ensino Médio*. Brasília: MEC, 2018.")
    md.append("- DIAGNE, Souleymane Bachir. *O Encontro das Razões: filosofar em África*. Tradução de Jamille Pinheiro Dias. São Paulo: Ubu Editora, 2022.")
    md.append("- HOUNTONDJI, Paulin. *Filosofia Africana: mito e realidade*. Tradução de Maria do Carmo de Abreu. Luanda: Edições Pedagógicas, 2008.")
    md.append("- SARR, Felwine. *Afrotopia*. Tradução de Cecília Ciscato. São Paulo: n-1 edições, 2019.")
    md.append("- SARR, Felwine; SAVOY, Bénédicte. *Restituir o Patrimônio Africano*. Tradução de Rachel Rocha. São Paulo: Cobogó, 2021.")
    md.append("- WIREDU, Kwasi. *Filosofia e Cultura Africana*. Tradução de Wanderson Flor do Nascimento. Brasília: Editora da UnB, 2015.\n")

    return "\n".join(md)

def main():
    questoes = build_exercicios()
    print(f"Total de questões construídas: {len(questoes)}")

    # 1. Checagem de quantidade e numeração
    assert len(questoes) == 60, f"Esperava 60 questões, obteve {len(questoes)}"
    for idx, q in enumerate(questoes, 1):
        assert q[0] == idx, f"Questão fora de ordem: {q[0]} != {idx}"

    # 2. Ajuste rigoroso de gabarito para ciclo balanceado perfeito (12 de cada)
    questoes_balanceadas = []
    for q in questoes:
        num, hab, dif, enunciado, alternativas, resolucao = q
        target_idx = (num - 1) % 5
        corr_idx = [i for i, (_, c) in enumerate(alternativas) if c][0]
        if corr_idx != target_idx:
            alts = list(alternativas)
            alts[corr_idx], alts[target_idx] = alts[target_idx], alts[corr_idx]
            questoes_balanceadas.append((num, hab, dif, enunciado, alts, resolucao))
        else:
            questoes_balanceadas.append(q)

    # 3. Formatação
    md_content = formatar_markdown(questoes_balanceadas)

    # 4. Checagem de gabarito balanceado no markdown
    gabs = re.findall(r"\*\*Gabarito:\*\* \(([A-E])\)", md_content)
    assert len(gabs) == 60, f"Esperava 60 gabaritos, obteve {len(gabs)}"
    contagem = Counter(gabs)
    print("Distribuição de gabaritos:", contagem)
    for l in ["A", "B", "C", "D", "E"]:
        assert contagem[l] == 12, f"Letra {l} tem {contagem[l]} ocorrências (esperado 12)!"

    # 5. Checagem de blacklist no texto gerado
    erros_bl = verificar_blacklist(md_content)
    if erros_bl:
        print("\n[ERRO FATAL] Termos proibidos encontrados:")
        for padrao, matches in erros_bl:
            print(f"  - Padrão '{padrao}': {matches}")
        sys.exit(1)
    else:
        print("Auditoria interna: NENHUM termo da blacklist detectado!")

    # 6. Checagem de inícios de enunciados repetidos
    inicios = [q[3].split()[:2] for q in questoes]
    inicios_str = [" ".join(x).lower() for x in inicios]
    c_inicios = Counter(inicios_str)
    print("Inícios mais frequentes:", c_inicios.most_common(5))
    for inicio, count in c_inicios.items():
        if count > 6:
            print(f"[ALERTA/ERRO] Início '{inicio}' ocorre {count} vezes (>6)!")
            sys.exit(1)

    # 7. Salvar em temp_draft.md
    temp_draft = "temp_draft.md"
    with open(temp_draft, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Arquivo rascunho salvo com sucesso em '{temp_draft}'.")

    # 8. Executar validador oficial
    destino_final = "content/medio/volume-unico/filosofia/eixo-5-existencialismo-diferenca/cap-39-filosofia-africana-contemporanea-afrotopia-sarr/ebooks/em-fil-c39-filosofia-africana-contemporanea-afrotopia-sarr-exercicios.md"

    cmd = [sys.executable, "validador_educamob.py", temp_draft, destino_final]
    print(f"Executando validador: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    if res.returncode == 0:
        print("\n[SUCESSO TOTAL] Cap 39 validado e homologado com Exit Code 0!")
        print("MARCO HISTÓRICO DE 39 CAPÍTULOS E 2.340 QUESTÕES HOMOLOGADAS!")
    else:
        print(f"\n[FALHA] Validador retornou código {res.returncode}")
        sys.exit(res.returncode)

if __name__ == "__main__":
    main()
