import os

def build_draft_c53():
    frontmatter = """---
série: "Ensino Médio"
disciplina: "História"
objeto_de_conhecimento: "A Humanidade como Força Geológica de Alteração Planetária: O Conceito de Antropoceno (ou Capitaloceno); A Matriz Energética Fóssil (Carvão, Petróleo e Gás Natural) Consolidada pelas Revoluções Industriais e a Emissão Desenfreada de Gases de Efeito Estufa; O Aquecimento Global e seus Efeitos Extremos (Secas, Enchentes e Queimadas); A Desigualdade dos Impactos Ecológicos: O Conceito de Justiça Climática e o Racismo Ambiental (Populações Mais Pobres e Vulneráveis pagando a conta do consumo das elites); As Cúpulas da Terra (Eco-92, Rio+20), O Protocolo de Quioto e o Acordo de Paris de 2015."
ebook_fonte: "em-his-c53-emergencia-climatica-antropoceno-capitaloceno-justica-climatica.md"
habilidades: "EM13CHS301, EM13CHS302, EM13CHS304, EM13CHS305, EM13CHS306"
total_exercicios: 60
distribuicao:
  basico: 20
  intermediario: 20
  dificil: 20
---

# Lista de Exercícios: A Emergência Climática no Antropoceno: Capitaloceno, Justiça Climática e Acordos Globais

## Nível Básico (Questões 1-20)
"""

    questions_basic = [
        # q01 (A)
        """<!-- id: q01 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: conceito-antropoceno -->
### Questão 1
O conceito de Antropoceno, popularizado no ano 2000 pelo químico holandês Paul Crutzen e por Eugene Stoermer, define uma nova época geológica caracterizada pelo fato de que:

a) As atividades humanas tornaram-se a principal força geológica motriz na alteração do sistema biofísico e climático da Terra.
b) As forças tectônicas e o vulcanismo subaquático passaram a responder por todas as variações térmicas da atmosfera.
c) A humanidade conseguiu eliminar completamente as oscilações de temperatura global por meio de barragens fluviais.
d) Os ciclos climáticos do planeta voltaram a apresentar a estabilidade térmica típica das glaciações pré-históricas.
e) O ritmo de extinção de espécies biológicas atingiu o menor índice registrado nos últimos milhões de anos.

**Gabarito:** A

**Resolução:**
O termo Antropoceno expressa que a escala da intervenção humana sobre a atmosfera, oceanos e ciclos biogeoquímicos assumiu proporções de força geológica planetária, rompendo a relativa estabilidade do Holoceno.
""",
        # q02 (B)
        """<!-- id: q02 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: matriz-energetica-fossil -->
### Questão 2
A base material que impulsionou as Revoluções Industriais e desencadeou a atual emergência climática esteve assentada na consolidação de uma matriz energética dependente de:

a) Fontes limpas e renováveis, como a energia solar fotovoltaica e os parques eólicos marinhos.
b) Combustíveis fósseis altamente emissores de carbono, tais como o carvão mineral, o petróleo e o gás natural.
c) Reatores nucleares de fusão atômica instalados nos centros metropolitanos durante o século XIX.
d) Óleos vegetais biodegradáveis extraídos de florestas tropicais preservadas.
e) Energia geotérmica obtida exclusivamente de falhas geológicas da América do Sul.

**Gabarito:** B

**Resolução:**
A queima desenfreada de carvão mineral (Primeira Revolução Industrial) e posteriormente de derivados de petróleo e gás fóssil (Segunda Revolução) liberou na atmosfera o carbono aprisionado no subsolo por centenas de milhões de anos.
""",
        # q03 (C)
        """<!-- id: q03 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: efeito-estufa-natural -->
### Questão 3
Do ponto de vista físico e atmosférico, o efeito estufa natural é compreendido pela ciência como um processo:

a) Prejudicial e artificial, criado pelos motores a combustão para impedir a chegada de luz solar à crosta terrestre.
b) Tóxico para todas as espécies vivas, exigindo a eliminação total de qualquer gás aprisionador de calor da troposfera.
c) Vital e necessário para a manutenção da vida na Terra, sem o qual o planeta apresentaria temperaturas médias congelantes de cerca de dezoito graus negativos.
d) Inexistente na atmosfera antes do término da Segunda Guerra Mundial em 1945.
e) Restrito às regiões urbanas com grande circulação de automóveis particulares.

**Gabarito:** C

**Resolução:**
O efeito estufa é um mecanismo natural que retém parte da radiação infravermelha; sem ele, a Terra seria uma esfera congelada inóspita. O problema reside na sua intensificação antropogênica pelo excesso de gases poluentes.
""",
        # q04 (D)
        """<!-- id: q04 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: basico | objeto: concentracao-co2-mauna-loa -->
### Questão 4
As medições científicas da atmosfera realizadas no observatório de Mauna Loa no Havaí indicam que a concentração de dióxido de carbono (CO2), que era de aproximadamente 280 ppm durante o Holoceno, atingiu na atualidade níveis superiores a:

a) 50 ppm.
b) 120 ppm.
c) 200 ppm.
d) 420 ppm.
e) 900 ppm.

**Gabarito:** D

**Resolução:**
Os registros contínuos em Mauna Loa comprovam que a concentração de CO2 ultrapassou a barreira dos 420 ppm, um salto abrupto e inédito em comparação com o patamar pré-industrial de 280 ppm.
""",
        # q05 (E)
        """<!-- id: q05 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: basico | objeto: conceito-capitaloceno -->
### Questão 5
Autores como o historiador Jason Moore e o ecologista político Andreas Malm propõem substituir o termo Antropoceno por Capitaloceno. Essa crítica teórica tem como argumento central o fato de que:

a) Todos os seres humanos consomem exatamente a mesma quantidade de petróleo e eletricidade diariamente.
b) As populações indígenas e os povos tradicionais são os verdadeiros responsáveis pelas emissões industriais de carvão.
c) A geologia terrestre é imune às atividades produtivas das fábricas e usinas termoelétricas.
d) A exploração da natureza é fruto exclusivo de hábitos biológicos ancestrais de caçadores e coletores.
e) A crise ecológica não é gerada pela humanidade em abstrato, mas pela lógica histórica de acumulação, lucro e exploração da natureza pelo sistema capitalista.

**Gabarito:** E

**Resolução:**
O termo Capitaloceno destaca a assimetria histórica de poder: atribuir a culpa à humanidade genérica oculta que a crise decorre do modo de produção capitalista e dos interesses de corporações e nações ricas que mercantilizaram a biosfera.
""",
        # q06 (A)
        """<!-- id: q06 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: conceito-justica-climatica -->
### Questão 6
O conceito de Justiça Climática estabelece que a emergência ambiental planetária deve ser analisada como uma questão ética e de direitos humanos porque:

a) Os países ricos e as elites emitiram a maior parte dos gases poluentes, enquanto os impactos mais letais recaem sobre as populações empobrecidas e vulneráveis do Sul Global.
b) O aquecimento do ar atinge com mais intensidade as mansões fortificadas das grandes metrópoles do que as moradias periféricas.
c) Os custos de transição energética devem ser cobrados exclusivamente de países que não possuem parques fabris modernos.
d) A poluição das águas marinhas decorre unicamente de práticas agrícolas familiares de subsistência.
e) As nações industrializadas do Norte Global não possuem recursos tecnológicos para construir barragens fluviais.

**Gabarito:** A

**Resolução:**
A Justiça Climática evidencia a profunda desigualdade distributiva: quem menos contribuiu para as emissões históricas de carbono sofre os impactos mais severos (secas, inundações, mortes) e possui menos recursos para se adaptar.
""",
        # q07 (B)
        """<!-- id: q07 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: basico | objeto: racismo-ambiental-benjamin-chavis -->
### Questão 7
Cunhado na década de 1980 pelo sociólogo norte-americano Benjamin Chavis, o termo Racismo Ambiental refere-se à:

a) Criação de áreas de proteção florestal exclusiva para animais de grande porte em zonas desérticas.
b) Imposição desproporcional de cargas degradadas, depósitos de lixo tóxico e riscos climáticos sobre comunidades negras, indígenas e tradicionais.
c) Preferência de corporações internacionais por contratar engenheiros florestais de etnias minoritárias.
d) Cobrança de impostos aduaneiros idênticos para produtos agrícolas cultivados em diferentes continentes.
e) Expansão de áreas verdes urbanas voltadas unicamente para bairros de classe média baixa.

**Gabarito:** B

**Resolução:**
O racismo ambiental aponta como as estruturas institucionais de poder direcionam os piores impactos poluentes e riscos geológicos para comunidades não brancas e desprovidas de representação política.
""",
        # q08 (C)
        """<!-- id: q08 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: gases-efeito-estufa -->
### Questão 8
Além do dióxido de carbono (CO2), são considerados importantes gases de efeito estufa associados a atividades industriais e agropecuárias:

a) Oxigênio molecular e hélio radioativo.
b) Nitrogênio puro e argônio líquido.
c) Metano (CH4) e óxido nitroso (N2O).
d) Monóxido de ferro e hidrogênio gasoso.
e) Vapor de mercúrio e cloro elementar.

**Gabarito:** C

**Resolução:**
O metano (gerado na pecuária e na decomposição orgânica) e o óxido nitroso (utilizado em fertilizantes sintéticos) têm alto potencial de aquecimento global na atmosfera, ao lado do CO2 e do vapor de água.
""",
        # q09 (D)
        """<!-- id: q09 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: basico | objeto: conferencia-estocolmo-1972 -->
### Questão 9
A Conferência de Estocolmo de 1972, promovida pela ONU como a primeira grande cúpula ambiental internacional, ficou marcada pelo conflito entre:

a) Companhias de aviação civil que defendiam a eliminação imediata de aeroportos regionais.
b) Países produtores de petróleo que exigiam a queima obrigatória de carvão mineral nas cidades costeiras.
c) Movimentos pacifistas asiáticos que pediam o fechamento de portos marítimos no Atlântico.
d) Países ricos que propunham o crescimento zero e nações em desenvolvimento que defendiam crescer primeiro e tratar a poluição depois.
e) Mineradoras estatais que exigiam a privatização total de geleiras na Antártida.

**Gabarito:** D

**Resolução:**
Em Estocolmo (1972), manifestou-se a clássica polarização: nações do Norte Global pregavam o crescimento zero, enquanto governos de países periféricos (como o Brasil da Ditadura Militar) viam nisso uma barreira ao seu próprio desenvolvimento fabril.
""",
        # q10 (E)
        """<!-- id: q10 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: eco-92-desenvolvimento-sustentavel -->
### Questão 10
Realizada na cidade do Rio de Janeiro em 1992, a Conferência das Nações Unidas sobre Meio Ambiente e Desenvolvimento (Eco-92) consagrou no cenário internacional o conceito de:

a) Crescimento econômico predatório sem limites territoriais.
b) Desregulamentação completa de atividades fabris poluentes.
c) Isolamento das florestas tropicais com expulsão armada de moradores nativos.
d) Monopólio estatal da queima de carvão fóssil nas Américas.
e) Desenvolvimento Sustentável, definido como aquele que atende às necessidades do presente sem comprometer as gerações futuras.

**Gabarito:** E

**Resolução:**
A Rio-92 oficializou as diretrizes do Relatório Brundtland (1987), consagrando a ideia de sustentabilidade: o equilíbrio entre viabilidade econômica, equidade social e conservação biológica para o presente e o futuro.
""",
        # q11 (A)
        """<!-- id: q11 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: protocolo-de-quioto-1997 -->
### Questão 11
O Protocolo de Quioto, firmado em 1997, foi o primeiro tratado internacional a fixar metas juridicamente vinculantes de redução de emissões para países desenvolvidos, baseado no princípio de:

a) Responsabilidades comuns, porém diferenciadas.
b) Cobrança de tarifas punitivas exclusivamente sobre nações insulares.
c) Redução proporcional e idêntica de fábricas para todos os países sem exceção.
d) Financiamento obrigatório de usinas a carvão em territórios desérticos.
e) Troca compulsória de áreas florestais por ações em bancos privados europeus.

**Gabarito:** A

**Resolução:**
O princípio de responsabilidades comuns, porém diferenciadas, reconhecia que todos os países têm o dever de combater a crise climática, mas as nações industrializadas do Anexo I carregam a maior obrigação por terem causado o grosso do acúmulo histórico.
""",
        # q12 (B)
        """<!-- id: q12 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: basico | objeto: acordo-de-paris-2015-meta -->
### Questão 12
Aprovado durante a COP-21 em 2015, o Acordo de Paris estabeleceu como objetivo central coletivo para o planeta:

a) Permitir a elevação contínua da temperatura média em até seis graus Celsius até 2100.
b) Manter o aquecimento médio global bem abaixo de 2,0°C em relação aos níveis pré-industriais e buscar esforços para limitá-lo a 1,5°C.
c) Estabelecer uma cota mínima obrigatória de consumo de derivados de petróleo para transportes terrestres.
d) Transferir indústrias poluentes para ilhas do Pacífico que enfrentam subida do nível do mar.
e) Encerrar as conferências diplomáticas anuais sobre o clima organizadas pela ONU.

**Gabarito:** B

**Resolução:**
O Acordo de Paris fixou a meta clara de segurar o aumento da temperatura média global bem abaixo de 2,0°C e buscar atingir o patamar mais seguro de 1,5°C para evitar pontos de não retorno ecológicos.
""",
        # q13 (C)
        """<!-- id: q13 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: conceito-ndcs -->
### Questão 13
No âmbito do Acordo de Paris de 2015, a sigla NDC refere-se às Contribuições Nacionalmente Determinadas, que consistem em:

a) Tropas militares conjuntas enviadas pela ONU para fiscalizar fábricas desativadas.
b) Empréstimos compulsórios em moeda estrangeira contraídos por governos municipais.
c) Compromissos e metas voluntárias de corte de emissões de gases apresentados periodicamente por cada país signatário.
d) Prêmios financeiros pagos a corporações que ampliarem o abate de florestas tropicais.
e) Licenças de caça esportiva emitidas por agências multilaterais em áreas de manguezais.

**Gabarito:** C

**Resolução:**
As NDCs são planos nacionais apresentados individualmente pelos países com suas metas de redução de emissões, transição energética e recuperação de florestas, atualizadas periodicamente.
""",
        # q14 (D)
        """<!-- id: q14 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: basico | objeto: vila-sahy-caso-racismo-ambiental -->
### Questão 14
A tragédia socioambiental ocorrida na Vila Sahy, no litoral norte de São Paulo, em fevereiro de 2023, exemplifica o racismo ambiental porque:

a) Os deslizamentos de terra soterraram apenas imóveis de alto padrão construídos na beira da água.
b) Todos os moradores da região possuíam sistemas avançados de drenagem e muros de contenção de pedra.
c) A chuva intensa caiu de maneira localizada apenas sobre o topo das montanhas desabitadas.
d) A população trabalhadora de baixa renda residia nas encostas frágeis da serra sem saneamento, enquanto as mansões ocupavam a planície segura.
e) O governo federal havia construído abrigos de concreto armado para todos os trabalhadores da construção civil.

**Gabarito:** D

**Resolução:**
O caso da Vila Sahy revela a segregação socioespacial: o evento extremo de chuva afetou toda a área litorânea, mas os mortos foram operários e prestadores de serviços empurrados para as encostas instáveis sem infraestrutura de proteção.
""",
        # q15 (E)
        """<!-- id: q15 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: grande-aceleracao-1945 -->
### Questão 15
O fenômeno histórico e ambiental conhecido como 'Grande Aceleração' (Great Acceleration), apontado por cientistas como um marco do Antropoceno, teve início após:

a) A assinatura do Tratado de Tordesilhas em 1494 pelas coroas ibéricas.
b) A invenção da imprensa de tipos móveis por Gutenberg no século XV.
c) A queda do Império Romano do Ocidente em 476 da Era Comum.
d) As primeiras expedições terrestres portuguesas no sertão mineiro.
e) O fim da Segunda Guerra Mundial em 1945, marcado pela explosão no consumo de plásticos, queima de petróleo e testes nucleares.

**Gabarito:** E

**Resolução:**
A Grande Aceleração pós-1945 multiplicou em escala geométrica o consumo de materiais fósseis, produção de adubos sintéticos, represamento de rios e espalhou partículas radioativas de testes atômicos nos estratos sedimentares do planeta.
""",
        # q16 (A)
        """<!-- id: q16 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: basico | objeto: acidificacao-oceanica -->
### Questão 16
A queima acelerada de combustíveis fósseis afeta a química dos mares por meio da acidificação oceânica, um fenômeno gerado:

a) Pela absorção maciça de dióxido de carbono dissolvido nas águas marinhas, o que reduz o pH e compromete a formação de carapaças e corais.
b) Pelo aumento súbito de oxigênio gasoso nas profundezas abissais que impede a respiração das algas.
c) Pela proliferação de blocos de gelo doce nas faixas tropicais próximas à linha do Equador.
d) Pela diminuição do nível de salinidade das águas provocada exclusivamente pela evaporação dos portos fluviais.
e) Pelo acúmulo de partículas de calcário desprendidas de recifes artificiais de plástico.

**Gabarito:** A

**Resolução:**
Os oceanos absorvem cerca de um quarto do CO2 emitido; na água, forma-se ácido carbônico, que reduz o pH marinho e desgasta o carbonato de cálcio necessário para a sobrevivência de corais, moluscos e plâncton calcário.
""",
        # q17 (B)
        """<!-- id: q17 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: basico | objeto: ipcc-funcao -->
### Questão 17
O Painel Intergovernamental sobre Mudanças Climáticas (IPCC), criado sob a liderança das Nações Unidas, desempenha no debate internacional a função de:

a) Financiar a prospecção e a perfuração de poços de petróleo em plataformas continentais.
b) Sintetizar e avaliar com rigor as pesquisas científicas mundiais sobre as causas e impactos do aquecimento planetário.
c) Executar prisões imediatas de gestores públicos que permitirem queimadas florestais.
d) Proibir a circulação de veículos de carga movidos a eletricidade nas capitais.
e) Administrar a venda de quotas de exportação de soja e minério de ferro.

**Gabarito:** B

**Resolução:**
O IPCC não conduz pesquisas de campo próprias, mas reúne centenas de cientistas para elaborar relatórios abrangentes que consolidam o consenso científico internacional e subsidiam governos nas decisões climáticas.
""",
        # q18 (C)
        """<!-- id: q18 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: basico | objeto: pegada-de-carbono-desigualdade -->
### Questão 18
Estudos e relatórios divulgados por organizações como a Oxfam sobre a pegada de carbono global apontam que:

a) A parcela mais pobre do planeta emite metade de todos os gases industriais por causa do uso de fogões a gás.
b) Os operários da construção civil possuem pegada de carbono superior à dos passageiros de aviões executivos.
c) O 1% mais rico da população mundial é responsável por uma quantidade de emissões superior à de toda a metade mais pobre da humanidade somada.
d) Não existe diferença no volume de poluição gerado entre moradores rurais da Amazônia e milionários urbanos.
e) O padrão de consumo alimentar das famílias sem-terra causa a maior parte do aquecimento dos oceanos.

**Gabarito:** C

**Resolução:**
As análises estatísticas demonstram a enorme concentração de carbono nas mãos da elite: jatos privados, iates, mansões climatizadas e investimentos financeiros de bilionários poluem mais que bilhões de pessoas vulneráveis.
""",
        # q19 (D)
        """<!-- id: q19 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: basico | objeto: agenda-21-eco-92 -->
### Questão 19
Entre os principais documentos e compromissos resultantes da Eco-92 no Rio de Janeiro, destaca-se a Agenda 21, cuja proposta consistiu em:

a) Criar um plano militar de invasão de países que operavam minas de carvão vegetal.
b) Determinar que o cultivo de café e trigo fosse transferido inteiramente para estufas subterrâneas.
c) Estabelecer um calendário único para a privatização de nascentes e bacias hidrográficas.
d) Formular um plano abrangente de ação para governos e sociedade civil visando ao desenvolvimento sustentável local e global.
e) Decretar o fim do comércio marítimo de mercadorias entre a América do Sul e a Europa.

**Gabarito:** D

**Resolução:**
A Agenda 21 estruturou recomendações para que municípios, estados e países promovessem políticas públicas articulando conservação da natureza, erradicação da pobreza e participação social na gestão dos recursos.
""",
        # q20 (E)
        """<!-- id: q20 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: basico | objeto: holoceno-estabilidade -->
### Questão 20
A época geológica do Holoceno, que antecedeu o Antropoceno e compreendeu os últimos 11.700 anos da história terrestre, foi fundamental para as sociedades humanas por ter propiciado:

a) Secas ininterruptas e variações térmicas violentas a cada dois anos em todos os continentes.
b) O desaparecimento completo de rios de planície e florestas tropicais de grande porte.
c) Um clima polar congelante contínuo que impediu o surgimento de núcleos urbanos.
d) A total ausência de vapor de água e dióxido de carbono na composição atmosférica.
e) Uma estabilidade térmica e climática relativa que permitiu o desenvolvimento da agricultura e a fixação das cidades.

**Gabarito:** E

**Resolução:**
O Holoceno proporcionou condições ambientais estáveis que viabilizaram a Revolução Agrícola no Neolítico, a domesticação de plantas e animais e a florescência das civilizações sedentárias na história humana.
"""
    ]

    questions_inter = [
        # q21 (A)
        """<!-- id: q21 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: intermediario | objeto: transicao-geologica-sedimentos -->
### Questão 21
Na perspectiva da estratigrafia geológica, a formalização do Antropoceno como época distinta do Holoceno apoia-se na presença de marcadores materiais inéditos gravados nas camadas de sedimentos da Terra, conhecidos como tecno-fósseis. Entre esses marcadores, incluem-se:

a) Radionuclídeos resultantes de detonações atômicas, microplásticos sintéticos dispersos nos oceanos e depósitos de concreto armado.
b) Instrumentos líticos talhados em quartzo e pontas de flecha de osso polido do Paleolítico Superior.
c) Cerâmicas decoradas com tintas de terra crua fabricadas por comunidades do período neolítico.
d) Camadas profundas de gelo fóssil formadas exclusivamente durante o período Pré-Cambriano.
e) Pedaços de madeira de pau-brasil petrificados sem vestígios de processamento fabril.

**Gabarito:** A

**Resolução:**
Os cientistas identificam que a atividade industrial moderna imprimiu assinaturas físicas globais nos estratos rochosos: isótopos radioativos de plutônio, ligas de alumínio e trilhões de partículas de plástico que durarão milhões de anos.
""",
        # q22 (B)
        """<!-- id: q22 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: maquina-a-vapor-james-watt -->
### Questão 22
A invenção e o aperfeiçoamento da máquina a vapor por James Watt na década de 1770, no contexto da Primeira Revolução Industrial inglesa, alteraram profundamente a relação entre trabalho humano e natureza porque:

a) Eliminaram a necessidade de construir estradas de ferro e barcos no transporte de cargas pesadas.
b) Libertaram a produção manufatureira da dependência de fluxos hídricos e animais, inaugurando a queima maciça de carbono fóssil subterrâneo.
c) Forçaram os empresários a restringir o trabalho fabril apenas a períodos de ventos fortes e ensolarados.
d) Desestimularam a abertura de minas subterrâneas de carvão mineral nas bacias britânicas.
e) Transferiram a fundição de ferro exclusivamente para oficinas movidas a tração animal nas aldeias.

**Gabarito:** B

**Resolução:**
Antes do motor a vapor, os moinhos dependiam da força das águas ou do vento. O vapor a carvão desvinculou as fábricas do ritmo biológico e geográfico natural, permitindo trabalho fabril ininterrupto e concentrado nas cidades.
""",
        # q23 (C)
        """<!-- id: q23 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: intermediario | objeto: critica-ao-antropoceno-universalizante -->
### Questão 23
O filósofo indiano Dipesh Chakrabarty e ecologistas contemporâneos observam que o conceito de Antropoceno pode gerar um viés interpretativo inadequado quando utilizado de forma universalizante e acrítica, pois tende a:

a) Minimizar a importância da química atmosférica na quantificação de partículas poluentes.
b) Exagerar a capacidade de regeneração imediata de florestas equatoriais úmidas.
c) Diluir a responsabilidade histórica de impérios coloniais e corporações petrolíferas ao colocar o gênero humano abstrato como culpado homogêneo.
d) Desconsiderar os registros instrumentais de temperatura colhidos em estações terrestres e satélites.
e) Sugerir que os países em desenvolvimento foram os primeiros a construir ferrovias movidas a carvão.

**Gabarito:** C

**Resolução:**
A universalização sob o rótulo "a humanidade" apaga o abismo de classes e nações: um camponês de subsistência no sul da Ásia não teve qualquer participação nas decisões que montaram a matriz fóssil capitalista global.
""",
        # q24 (D)
        """<!-- id: q24 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: intermediario | objeto: cheap-nature-jason-moore -->
### Questão 24
Na obra *Anthropocene or Capitalocene?*, o teórico Jason Moore defende que a expansão histórica do capitalismo apoiou-se na apropriação sistemática de 'naturezas baratas' (*cheap nature*). Segundo essa teoria, o sistema mercantil acumulou riqueza:

a) Remunerando de forma justa todas as populações tradicionais pela manutenção dos ciclos hídricos.
b) Reinvestindo a totalidade dos lucros fabris no reflorestamento nativo de planícies costeiras.
c) Recusando o uso de matérias-primas minerais que demandassem trabalho escravizado ou degradado.
d) Tratando a energia, os alimentos, as matérias-primas e a vida humana como insumos de baixo custo a serem saqueados da biosfera sem reposição.
e) Estabelecendo que a atmosfera era um bem privado protegido por patentes jurídicas invioláveis.

**Gabarito:** D

**Resolução:**
Jason Moore argumenta que o capitalismo prosperou ao externalizar custos ecológicos: alimentos baratos, energia fóssil barata, matérias-primas baratas e vidas exploradas foram tratadas como recursos infinitos e gratuitos a serviço da acumulação.
""",
        # q25 (E)
        """<!-- id: q25 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: unfccc-e-cops -->
### Questão 25
A Convenção-Quadro das Nações Unidas sobre a Mudança do Clima (UNFCCC), originada na Cúpula da Terra no Rio de Janeiro em 1992, estabeleceu uma dinâmica multilateral periódica caracterizada pela realização anual das COPs (Conferências das Partes). Essas assembleias têm por finalidade primordial:

a) Fixar o preço internacional do barril de petróleo cru para empresas extrativistas privadas.
b) Centralizar o comando das forças de segurança militar em zonas de conflito agrário.
c) Autorizar a dragagem de estuários para instalação de portos carvoeiros no hemisfério sul.
d) Reduzir os investimentos globais em redes de transporte público sobre trilhos.
e) Avaliar o cumprimento de tratados climáticos, revisar compromissos de corte de gases e negociar termos de financiamento para adaptação e redução de impactos.

**Gabarito:** E

**Resolução:**
As COPs reúnem delegados de quase duzentos países para avaliar relatórios científicos do IPCC, atualizar compromissos de redução de emissões e acordar mecanismos de apoio para os países mais vulneráveis.
""",
        # q26 (A)
        """<!-- id: q26 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: intermediario | objeto: relatorio-brundtland-1987 -->
### Questão 26
O relatório 'Nosso Futuro Comum' (Relatório Brundtland), elaborado em 1987 pela Comissão Mundial sobre Meio Ambiente e Desenvolvimento da ONU, introduziu formalmente na agenda política dos governos a tese de que:

a) O crescimento econômico precisa estar subordinado à capacidade de suporte dos ecossistemas e à justiça distributiva entre presentes e futuras gerações.
b) A industrialização moderna deve paralisar totalmente o comércio internacional de alimentos para resguardar a soberania local.
c) Os países em desenvolvimento devem arcar com o pagamento de multas diárias pela preservação de suas florestas.
d) O esgotamento dos recursos minerais representa uma vantagem competitiva para economias baseadas em extrativismo.
e) O ritmo de emissões industriais independe da matriz energética adotada pelos transportes de carga.

**Gabarito:** A

**Resolução:**
O documento liderado por Gro Harlem Brundtland consolidou o termo "Desenvolvimento Sustentável", alertando que a exploração contínua e desregulada dos ecossistemas ameaçava a própria sobrevivência das futuras gerações de seres humanos.
""",
        # q27 (B)
        """<!-- id: q27 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: protocolo-quioto-recusa-eua -->
### Questão 27
A perda de força política e eficácia do Protocolo de Quioto no início dos anos 2000 decorreu principalmente da postura diplomática do governo dos Estados Unidos sob a presidência de George W. Bush, que:

a) Declarou guerra econômica aos países europeus que utilizavam energia eólica.
b) Recusou-se a ratificar o tratado alegando que as metas prejudicavam a economia norte-americana e que nações emergentes estavam isentas.
c) Exigiu que o tratado proibisse de forma imediata o uso de automóveis particulares no território norte-americano.
d) Propôs que a ONU dissolvesse o IPCC por desconfiar dos termômetros meteorológicos de superfície.
e) Assinou um decreto forçando todas as companhias petrolíferas norte-americanas a encerrar a produção de combustíveis.

**Gabarito:** B

**Resolução:**
Sendo os EUA o maior poluidor histórico e o maior emissor na época, a recusa de George W. Bush em ratificar Quioto (sob a alegação de prejuízo econômico e falta de metas para a China) esvaziou a pressão internacional sobre o tratado.
""",
        # q28 (C)
        """<!-- id: q28 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: intermediario | objeto: eventos-extremos-desigualdade -->
### Questão 28
Os relatórios mais recentes do IPCC alertam que o aumento de 1,2°C na temperatura média planetária já provocou uma mudança na frequência e intensidade de fenômenos meteorológicos extremos. Essa dinâmica afeta a sociedade de forma desigual porque:

a) A população de renda elevada habita regiões que não sofrem variações térmicas nas quatro estações.
b) As famílias camponesas possuem apólices de seguro rural financiadas por seguradoras internacionais.
c) Comunidades pobres e periféricas carecem de obras de contenção, redes de esgoto pluvial e habitações com isolamento térmico, tornando tempestades e ondas de calor fatais.
d) As secas severas beneficiam pequenos agricultores familiares que utilizam irrigação artesanal.
e) O aumento do nível dos oceanos afeta apenas plataformas de extração submarina de petróleo.

**Gabarito:** C

**Resolução:**
A vulnerabilidade climática é moldada por fatores sociais e econômicos: um temporal idêntico causa alagamento de garagens em bairros nobres, mas soterramento e perda total de lares em favelas e encostas sem infraestrutura.
""",
        # q29 (D)
        """<!-- id: q29 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: intermediario | objeto: limites-planetarios-economia-ecologica -->
### Questão 29
A Economia Ecológica questiona a utilização do Produto Interno Bruto (PIB) como indicador exclusivo de progresso social e riqueza nacional com base na constatação de que o PIB:

a) Deduz automaticamente dos lucros corporativos o custo da saúde pública provocado pela poluição do ar.
b) Considera apenas a quantidade de árvores nativas mantidas em pé em reservas extrativistas.
c) Pune tributariamente as empresas mineradoras que despejam lama tóxica em leitos de rios.
d) Trata a derrubada de florestas e a reconstrução após desastres climáticos mortais como aumento de atividade e crescimento econômico positivo.
e) Impede que bancos de investimento financiem projetos voltados à geração de energia termelétrica.

**Gabarito:** D

**Resolução:**
O cálculo convencional do PIB mede apenas o fluxo de dinheiro circulante: se uma floresta é arrasada e vendida como madeira, o PIB sobe; se uma encosta desaba e exige obras de socorro, o PIB cresce. Ele ignora a perda de patrimônio natural e humano.
""",
        # q30 (E)
        """<!-- id: q30 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: compromissos-ndcs-insuficiencia -->
### Questão 30
Embora o Acordo de Paris de 2015 tenha reunido quase duzentos países signatários, climatologistas e organizações não governamentais apontam um grave limite estrutural no seu funcionamento contemporâneo:

a) O texto do acordo obriga os países signatários a abandonar toda e qualquer atividade agrícola tradicional.
b) As metas de redução foram desenhadas exclusivamente para fechar usinas solares em regiões desérticas.
c) O tratado determinou a criação de um imposto mundial sobre a renda de todos os trabalhadores rurais.
d) A ONU assumiu o direito de desapropriar territórios soberanos que não atingirem neutralidade carbônica em cinco anos.
e) A soma das metas voluntárias (NDCs) apresentadas pelos governos permanece insuficiente, colocando o mundo na rota de um aquecimento perigoso superior a 2,5°C.

**Gabarito:** E

**Resolução:**
O grande calcanhar de Aquiles do Acordo de Paris é o descompasso entre a ciência e a diplomacia: as NDCs são voluntárias e não punitivas. Mesmo se todas forem cumpridas, a temperatura ainda subirá muito além da meta segura de 1,5°C.
""",
        # q31 (A)
        """<!-- id: q31 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: intermediario | objeto: transicao-energetica-metais-criticos -->
### Questão 31
A transição das matrizes energéticas fósseis para fontes renováveis (parques eólicos, usinas solares e veículos movidos a baterias) coloca novos dilemas ecológicos e geopolíticos no século XXI ao intensificar:

a) A disputa predatória pela extração mineral de lítio, cobalto, níquel e terras raras em territórios da periferia global.
b) A necessidade compulsória de reabrir minas de carvão mineral de superfície em países nórdicos.
c) A dependência de madeira de lei extraída de matas de galeria para a fabricação de geradores solares.
d) O fim completo do comércio internacional de cabos elétricos de cobre e turbinas eólicas.
e) A extinção imediata de todo tipo de transporte rodoviário de cargas no interior dos continentes.

**Gabarito:** A

**Resolução:**
A transição energética não é imaterial: requer grandes quantidades de minerais críticos (lítio, cobalto, terras raras). Sem salvaguardas sociais e ambientais, ela pode reproduzir novas formas de extrativismo predatório no Sul Global.
""",
        # q32 (B)
        """<!-- id: q32 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: ponto-de-nao-retorno-amazonia -->
### Questão 32
Cientistas alertam para o risco de a Amazônia atingir um 'ponto de não retorno' provocado pela combinação de desmatamento, queimadas e aquecimento global. Esse processo desencadearia:

a) O resfriamento imediato de toda a Bacia do Prata com formação de geleiras em São Paulo.
b) A savanização progressiva de vastas áreas florestais, com o colapso dos 'rios voadores' de vapor de água que irrigam a agricultura do centro-sul brasileiro.
c) A elevação súbita do nível de água dos rios locais impedindo a navegação de canoas ribeirinhas.
d) O aumento espontâneo da umidade relativa do ar em desertos da América do Norte.
e) A transformação da floresta densa em uma cobertura de tundra ártica desprovida de árvores.

**Gabarito:** B

**Resolução:**
Se a floresta perder entre 20% e 25% de sua cobertura, a perda de umidade compromete a reciclagem interna de chuvas; a mata entra em colapso e seca, enfraquecendo os rios voadores e secando o regime de chuvas do Sudeste e Centro-Oeste.
""",
        # q33 (C)
        """<!-- id: q33 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: intermediario | objeto: relatorio-oxfam-consumo-elites -->
### Questão 33
A análise da pegada de carbono sob a ótica da desigualdade social demonstra que as escolhas de consumo de luxo das elites mundiais têm um impacto desproporcional no clima porque:

a) As famílias de classe alta consomem apenas vegetais orgânicos que utilizam defensivos de alta intensidade.
b) O uso de transportes coletivos nas metrópoles consome mais derivados de petróleo que iates e jatos corporativos.
c) Práticas como aviação privada frequente, navegação de recreio e hiperconsumo intensivo de energia emitem centenas de vezes mais gases que a vida cotidiana de trabalhadores de baixa renda.
d) As empresas exportadoras de petróleo pertencem exclusivamente a cooperativas comunitárias do Sul Global.
e) O descarte de embalagens plásticas é inexistente nas residências de alta renda das capitais.

**Gabarito:** C

**Resolução:**
O hiperconsumo das classes ricas representa uma sobrecarga extrema na atmosfera: voos particulares, residências gigantescas climatizadas e bens de luxo demandam montantes elevados de energia fóssil per capita.
""",
        # q34 (D)
        """<!-- id: q34 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: intermediario | objeto: seguranca-alimentar-clima -->
### Questão 34
As alterações climáticas globais ameaçam a segurança alimentar no Brasil e no mundo de forma contundente ao provocarem:

a) A substituição compulsória de lavouras de grãos por florestas nativas em propriedades privadas.
b) O fim imediato do consumo de água potável pelos animais criados em fazendas pecuárias.
c) A queda contínua no custo dos alimentos básicos nos supermercados das grandes cidades.
d) A desestruturação dos calendários tradicionais de plantio decorrente de estiagens severas, ondas de calor e quebra de safras agrícolas.
e) O congelamento perene das várzeas férteis onde se cultiva o arroz irrigado no sul do país.

**Gabarito:** D

**Resolução:**
A instabilidade no ciclo de chuvas desregula as épocas de semeadura e colheita, quebrando safras de milho, soja, feijão e hortaliças, o que encarece a comida e amplia a fome entre os grupos sociais mais vulneráveis.
""",
        # q35 (E)
        """<!-- id: q35 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: convencao-diversidade-biologica-eco92 -->
### Questão 35
Além da convenção sobre o clima, a Eco-92 resultou na aprovação da Convenção sobre Diversidade Biológica (CDB), que teve como meta central:

a) Autorizar a exportação irrestrita de animais silvestres ameaçados para colecionadores estrangeiros.
b) Suprimir as unidades de conservação ambiental em áreas com potencial madeireiro comercial.
c) Delegar a corporações farmacêuticas privadas a soberania territorial sobre florestas indígenas.
d) Proibir que universidades públicas façam pesquisas científicas sobre botânica e zoologia em ecossistemas tropicais.
e) Estabelecer a conservação da biodiversidade, a utilização sustentável de seus componentes e a repartição justa dos benefícios decorrentes do uso de recursos genéticos.

**Gabarito:** E

**Resolução:**
A CDB assegurou a soberania dos países sobre seus recursos genéticos nativos e estabeleceu a obrigatoriedade da divisão justa de benefícios gerados a partir do conhecimento tradicional associado e da biotecnologia.
""",
        # q36 (A)
        """<!-- id: q36 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: intermediario | objeto: ditadura-militar-brasil-estocolmo -->
### Questão 36
Durante a Conferência de Estocolmo em 1972, a delegação brasileira, nomeada pela Ditadura Militar, defendeu uma posição de prioridade ao crescimento econômico sintetizada no lema 'desenvolver primeiro, pagar o custo da poluição depois'. Essa postura justificava-se pelo discurso oficial de que:

a) A preservação ambiental proposta pelos países ricos era uma tentativa externa para frear a expansão fabril e o crescimento nacional.
b) Os operários das fábricas brasileiras preferiam conviver com fumaça a receber melhorias salariais.
c) O território nacional não continha cursos de água ou biomas capazes de sofrer degradação química.
d) O governo pretendia desativar todas as usinas hidrelétricas para importar carvão fóssil da Europa.
e) A queima de combustíveis favorecia o florescimento de espécies nativas do Cerrado.

**Gabarito:** A

**Resolução:**
Os representantes militares viam o ambientalismo como um bloqueio dos países ricos para impedir que nações periféricas desenvolvessem indústrias de base, subordinando a ecologia às metas de crescimento do PIB da época.
""",
        # q37 (B)
        """<!-- id: q37 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: intermediario | objeto: mercado-de-carbono-limites -->
### Questão 37
O mecanismo de compensação de emissões por créditos de carbono recebe alertas de movimentos socioambientais porque:

a) Garante a preservação imediata de todos os manguezais sem necessidade de fiscalização pública.
b) Pode permitir que corporações e países ricos comprem autorizações para continuar emitindo poluentes em vez de realizarem cortes estruturais em suas operações.
c) Proíbe terminantemente qualquer investimento na recuperação de matas ciliares.
d) Força a desativação de ferrovias elétricas para substituição por frotas de caminhões pesados.
e) Estabelece que os pagamentos por carbono sejam distribuídos igualmente a todos os cidadãos da Terra.

**Gabarito:** B

**Resolução:**
A crítica ao mercado de carbono aponta o risco de comodificação da atmosfera: companhias petrolíferas compram créditos preservando florestas longe de suas refinarias, mantendo a queima de fósseis ativa.
""",
        # q38 (C)
        """<!-- id: q38 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: intermediario | objeto: refugo-toxico-racismo-ambiental -->
### Questão 38
Nos estudos pioneiros de sociologia urbana sobre racismo ambiental, observou-se que a instalação de depósitos de lixo tóxico, usinas poluentes e áreas de despejo ocorre com maior frequência:

a) Nos bairros residenciais arborizados de alta renda dotados de grande valorização imobiliária.
b) Em centros financeiros que concentram sedes corporativas de instituições bancárias.
c) Nas vizinhanças onde residem famílias de minorias étnicas, negras e operárias com menor renda e menor capacidade de pressão sobre o poder público.
d) Nos parques nacionais de proteção integral voltados ao turismo sustentável.
e) Nas proximidades de prédios governamentais e assembleias legislativas estaduais.

**Gabarito:** C

**Resolução:**
O zoneamento urbano desigual reflete a disparidade política: bairros de maior renda barram a instalação de lixões e fábricas poluentes em suas imediações, empurrando esses passivos para periferias e comunidades pobres.
""",
        # q39 (D)
        """<!-- id: q39 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: intermediario | objeto: permafrost-degelo-retroalimentacao -->
### Questão 39
O degelo rápido do *permafrost* (camada de solo congelado nas regiões árticas da Sibéria e do Canadá) é considerado pelos climatologistas um grave ciclo de retroalimentação térmica porque:

a) Libera grandes quantidades de oxigênio que apagam incêndios florestais nas estepes.
b) Converte as águas do Oceano Ártico em reservatórios de água potável desprovida de sais.
c) Permite o cultivo anual de trigo e café em regiões anteriormente cobertas por neves eternas.
d) Devolve à atmosfera volumes imensos de metano e CO2 aprisionados na matéria orgânica congelada há milênios, ampliando o aquecimento.
e) Provoca o resfriamento imediato do ar ao refletir toda a luz do sol de volta ao espaço.

**Gabarito:** D

**Resolução:**
O permafrost armazena muito carbono orgânico. Ao derreter com a subida das temperaturas, bactérias decompõem essa matéria vegetal antiga e liberam metano e CO2, criando um ciclo contínuo de aquecimento global.
""",
        # q40 (E)
        """<!-- id: q40 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: intermediario | objeto: papel-comunidades-tradicionais-preservacao -->
### Questão 40
Dados consolidados de imagens de satélite e censos florestais no Brasil comprovam que os territórios indígenas e as reservas extrativistas apresentam as menores taxas de desmatamento do país. Esse dado científico evidencia que:

a) A fiscalização do corte de madeira só funciona quando executada por tratores de esteira telecomandados.
b) Os povos da floresta não praticam qualquer tipo de caça, pesca ou manejo de espécies vegetais para seu sustento.
c) As florestas tropicais sobrevivem melhor quando completamente desprovidas de qualquer presença humana.
d) As cooperativas madeireiras privadas preservam a vegetação nativa com mais rigor que as comunidades tradicionais.
e) A garantia da demarcação de terras indígenas e da posse comunitária tradicional é a política socioambiental mais eficaz de conservação e combate à crise climática.

**Gabarito:** E

**Resolução:**
Os modos de vida tradicionais e as práticas dos povos indígenas convivem com a floresta mantendo-a viva. Onde há demarcação homologada e proteção aos povos originários, os índices de devastação e emissão de carbono caem drasticamente.
"""
    ]

    questions_hard = [
        # q41 (A)
        """<!-- id: q41 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: dificil | objeto: debate-marco-inicial-antropoceno -->
### Questão 41
O debate científico entre a geologia, a história ambiental e a climatologia sobre a fixação do marco inicial do Antropoceno contrapõe duas teses centrais: a primeira situa a virada na Revolução Industrial no século XVIII; a segunda localiza o limiar na Grande Aceleração iniciada por volta de 1945. Analisando as implicações teóricas dessa periodização, constata-se que a adoção de 1945 fundamenta-se:

a) Na sincronia global de assinaturas sedimentares físicas e químicas de escala planetária, como a deposição de partículas radioativas de plutônio dos testes atômicos e a proliferação em massa de resíduos plásticos sintéticos.
b) Na extinção completa dos ecossistemas de savana em todo o continente americano decorrente da expansão de culturas de trigo.
c) No momento exato em que as companhias mineradoras privadas interromperam a exploração de poços submarinos de petróleo na Europa.
d) Na aprovação unânime do primeiro código florestal internacional durante o governo republicano de Abraham Lincoln nos Estados Unidos.
e) Na substituição integral do carvão mineral pela energia eólica nas indústrias metalúrgicas de todo o hemisfério ocidental.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** A estratigrafia geológica requer uma assinatura física global clara, duradoura e sincrônica gravada nas rochas e sedimentos da Terra para definir uma nova época.
- **Etapa 2:** Embora a máquina a vapor aperfeiçoada por James Watt tenha inaugurado a queima do carvão fóssil na Grã-Bretanha no século XVIII, seus efeitos materiais foram inicialmente graduais e regionais.
- **Etapa 3:** A virada de 1945 forneceu um marcador global uniforme: as detonações atômicas espalharam uma camada mundial de plutônio nos solos, sincronizada à explosão do consumo de plásticos sintéticos e derivados de petróleo em todos os continentes.
""",
        # q42 (B)
        """<!-- id: q42 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: capitaloceno-separacao-sociedade-natureza -->
### Questão 42
Ao teorizar o Capitaloceno, o ecologista político Jason Moore argumenta que a gênese da crise ecológica planetária não se originou apenas com as máquinas a vapor do século XVIII, mas na formação da economia capitalista histórica. Para essa abordagem, o sistema mercantil moderno operou uma transformação estrutural e profunda ao:

a) Respeitar os ciclos de reprodução das espécies animais marinhas mediante leis de defeso estritas.
b) Romper a interdependência metabólica ancestral ao conceber a Natureza e a Sociedade como esferas separadas, tratando a biosfera como mera fonte de matérias-primas e sumidouro de dejetos a serviço do lucro.
c) Tratar os ecossistemas florestais como bens sagrados e intocáveis cuja exploração mercantil era proibida pelos governos.
d) Estabelecer que todo o valor das mercadorias manufaturadas deveria ser calculado pelo número de árvores replantadas pelas corporações.
e) Transferir o controle financeiro dos impérios marítimos ibéricos para conselhos indígenas de anciãos.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** As sociedades tradicionais e originárias compreendiam os seres humanos como partes integrantes da teia da vida, articulados aos ritmos orgânicos da terra e da água.
- **Etapa 2:** A ascensão do capitalismo instituiu uma separação conceitual e econômica: dividiu o mundo entre a esfera dos proprietários e uma "natureza exterior", concebida como repositório de recursos passivos.
- **Etapa 3:** Essa divisão legitimou o saque de recursos naturais e o tratamento da atmosfera como um depósito gratuito de resíduos, gerando um modelo de expansão infinita que colide com os limites materiais do planeta.
""",
        # q43 (C)
        """<!-- id: q43 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: dificil | objeto: mauna-loa-dinamica-curva-keeling -->
### Questão 43
Os dados de concentração de dióxido de carbono (CO2) monitorados no observatório de Mauna Loa no Havaí, conhecidos na climatologia como Curva de Keeling, revelam duas dinâmicas superpostas: uma oscilação sazonal contínua anual e uma curva ascendente permanente. A explicação para a oscilação anual de curto prazo e para a tendência contínua de longo prazo reside, respectivamente:

a) Na maré alta dos oceanos tropicais durante a primavera e no descarte de carcaças metálicas em estuários urbanos.
b) Na atividade vulcânica contínua de caldeiras submarinas no Pacífico e na substituição do ferro fundido por estruturas de alumínio.
c) No ciclo biológico das florestas do hemisfério norte (que realizam mais fotossíntese no verão e perdem folhas no inverno) e na queima maciça e ininterrupta de combustíveis fósseis pela civilização industrial.
d) Na alternância dos regimes de ventos alísios na Linha do Equador e na retração das lavouras de trigo na Europa mediterrânea.
e) No consumo de oxigênio por cardumes migratórios de baleias e na construção de barragens para contenção de sedimentos fluviais.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** A Curva de Keeling apresenta pequenas oscilações anuais regulares: o planeta absorve mais carbono durante a primavera e o verão do Hemisfério Norte (onde se concentra a maior massa continental e vegetal da Terra) e libera no outono e inverno.
- **Etapa 2:** No entanto, sob essas flutuações sazonais biológicas naturais, corre uma linha de fundo contínua, ascendente e acelerada, sem retorno aos níveis anteriores.
- **Etapa 3:** Essa subida contínua e ininterrupta de longo prazo é propulsionada pela emissão humana de CO2 fóssil (queima de carvão, petróleo e gás), rompendo o equilíbrio histórico e ultrapassando 420 ppm na atmosfera.
""",
        # q44 (D)
        """<!-- id: q44 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: dificil | objeto: racismo-ambiental-segregacao-urbana -->
### Questão 44
A análise do racismo ambiental no contexto da urbanização brasileira revela como o planejamento do poder público e o mercado de terras estruturam as cidades de forma seletiva. Diante de desastres provocados por chuvas torrenciais extremas em metrópoles como Rio de Janeiro, Recife e Salvador, o conceito de racismo ambiental fundamenta-se no fato de que:

a) Os deslizamentos de morros atingem de maneira matematicamente aleatória e uniforme todos os grupos de renda e etnias dos municípios.
b) As chuvas de tempestades afetam prioritariamente áreas de preservação ecológica sem moradores.
c) As famílias de operários escolhem residir em topos de encostas e várzeas alagáveis por preferências particulares sem relação com o valor da terra.
d) A segregação socioespacial empurrou famílias negras e de baixa renda para territórios de alto risco geológico sem drenagem e contenção, enquanto obras de segurança concentram-se em áreas nobres.
e) O poder público municipal executa desapropriações preventivas indenizando os moradores periféricos com apartamentos de alto padrão em bairros litorâneos.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** O racismo ambiental articula a desigualdade racial, a especulação de terrenos e a histórica negligência do Estado em prover habitação digna e segura.
- **Etapa 2:** Famílias negras e pobres, sem renda para morar em locais urbanizados e planos, ocupam encostas instáveis e margens de córregos que não interessam aos condomínios fechados e não recebem muros de arrimo.
- **Etapa 3:** Quando tempestades extremas decorrentes do aquecimento planetário atingem a cidade, o volume de água cai sobre todos os bairros, mas os desabamentos e mortes concentram-se nas encostas desprovidas de infraestrutura, expondo a seletividade social do perigo.
""",
        # q45 (E)
        """<!-- id: q45 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: impasse-diplomatico-norte-sul-responsabilidade -->
### Questão 45
Nas negociações da diplomacia climática internacional, desde a Rio-92 até as conferências recentes da ONU, o debate entre os países desenvolvidos do Norte Global e as nações em desenvolvimento do Sul Global gira em torno das responsabilidades históricas. Esse impasse estrutura-se pelo fato de que:

a) Os países do Sul Global defendem que todos os parques industriais da Europa sejam convertidos em reservas de caça.
b) As nações desenvolvidas exigem que as pequenas propriedades rurais do hemisfério sul paguem indenizações pelo uso de ferramentas manuais.
c) Os governos do hemisfério ocidental pretendem transferir o registro de patentes de sementes para bancos de investimento asiáticos.
d) As economias periféricas recusam qualquer modalidade de ajuda tecnológica que envolva painéis fotovoltaicos.
e) O Sul Global defende o reconhecimento da responsabilidade histórica dos países ricos pelo carbono acumulado no passado, enquanto o Norte Global pressiona por metas idênticas de corte para países em desenvolvimento sem garantir recursos suficientes para adaptação.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** Os países industrializados do Norte construíram sua riqueza ao longo de dois séculos emitindo a maior fatia do CO2 acumulado na atmosfera, sem pagar pelos danos ecológicos.
- **Etapa 2:** Nas negociações multilaterais, o Norte procura impor cortes homogêneos de emissões a países do Sul, desconsiderando as urgências de combate à pobreza e as carências de saneamento básico dessas populações.
- **Etapa 3:** O Sul Global reivindica que as nações enriquecidas repassem recursos financeiros e tecnologias limpas em respeito ao princípio de responsabilidades comuns porém diferenciadas, evitando que os mais vulneráveis arquem com os custos da transição.
""",
        # q46 (A)
        """<!-- id: q46 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: dificil | objeto: acidificacao-marinha-troficos -->
### Questão 46
A alteração química dos oceanos causada pelo aumento da concentração de dióxido de carbono na atmosfera compromete a base biológica das teias alimentares marinhas. A dinâmica que liga a emissão de CO2 fóssil à acidificação marinha e à subsistência humana caracteriza-se pelo fato de que:

a) O excesso de CO2 absorvido pelas águas marinhas forma ácido carbônico, reduzindo o pH e prejudicando a calcificação de corais e moluscos, o que ameaça a pesca artesanal de comunidades tradicionais costeiras.
b) A dissolução do gás fóssil transforma as bacias marinhas em águas doces ácidas que impedem a navegação de petroleiros de grande porte.
c) A quebra do equilíbrio salino acelera a reprodução desenfreada de caranguejos gigantes que devoram os leitos de algas marinhas das praias.
d) Os animais de concha calcária produzem substâncias venenosas espontâneas que tornam a água do mar inflamável nas proximidades de portos industriais.
e) A diminuição da temperatura profunda dos mares força os cardumes de peixes a migrar para lagos de água doce do interior continental.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** Os mares funcionam como grandes absorvedores de calor e de carbono, retendo entre 25% e 30% do dióxido de carbono lançado pelas indústrias humanas.
- **Etapa 2:** O CO2 dissolvido reage quimicamente com a água formando ácido carbônico, que reduz o pH e consome íons de carbonato, impedindo que corais, mariscos e pequenos organismos formem suas estruturas calcárias de sustentação.
- **Etapa 3:** O enfraquecimento dos recifes de corais desestabiliza os berçários naturais de peixes marinhos, colocando em risco a segurança alimentar e o sustento de milhões de famílias pesqueiras que dependem da pesca artesanal no litoral.
""",
        # q47 (B)
        """<!-- id: q47 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: protocolo-quioto-mecanismo-desenvolvimento-limpo -->
### Questão 47
O Protocolo de Quioto (1997) estabeleceu os Mecanismos de Flexibilidade, entre os quais o Mecanismo de Desenvolvimento Limpo (MDL). O funcionamento do MDL e as controvérsias em torno de seus resultados relacionam-se ao fato de que:

a) O MDL obrigava os países em desenvolvimento a importar carvão mineral produzido em minas europeias com desconto comercial.
b) O mecanismo permitia que países desenvolvidos comprassem créditos gerados por projetos limpos em países emergentes para abater de suas metas, gerando o risco de postergar transformações industriais profundas em seus próprios territórios.
c) O tratado determinou o fim de todas as taxas alfandegárias para maquinário pesado destinado à abertura de estradas em florestas tropicais.
d) Os créditos obtidos pelos países signatários eram convertidos em ações de estatais de petróleo para garantir o pagamento de dividendos a governos municipais.
e) As empresas que realizavam investimentos em despoluição eram excluídas dos mercados de ações das principais bolsas do mundo.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** O MDL permitia que nações industrializadas financiassem projetos de energia limpa ou recuperação florestal em países em desenvolvimento em troca de certificados de redução de emissões.
- **Etapa 2:** Esses papéis funcionavam como créditos que podiam ser usados para comprovar o cumprimento das metas de redução fixadas em Quioto.
- **Etapa 3:** Críticos socioambientais alertavam que a compra de créditos externos permitia a grandes corporações do Norte continuar queimando combustíveis fósseis em suas fábricas domésticas, contornando a necessidade de reformas energéticas estruturais.
""",
        # q48 (C)
        """<!-- id: q48 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: dificil | objeto: diferenca-meta-1-5-vs-2-0-graus -->
### Questão 48
Relatórios do IPCC que comparam os cenários de elevação da temperatura média da Terra em 1,5°C e 2,0°C acima dos níveis pré-industriais indicam que essa variação de meio grau não traz consequências graduais simples, mas multiplica riscos graves. Esse diagnóstico decorre do fato de que, em um cenário de 2,0°C:

a) As geleiras continentais da Groenlândia aumentam de espessura devido à queda de tempestades de granizo na primavera.
b) As áreas desérticas do Saara são totalmente transformadas em pântanos tropicais ricos em cana-de-açúcar.
c) A perda de recifes de corais salta para mais de 99%, eventos de calor extremo tornam-se frequentes e centenas de milhões de pessoas adicionais enfrentam escassez hídrica severa.
d) O regime de chuvas tropicais no hemisfério sul estabiliza-se em padrões idênticos aos do século XIX sem secas sazonais.
e) A capacidade de retenção de água pelos solos agricultáveis cresce espontaneamente devido ao fechamento dos estômatos vegetais.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** O equilíbrio climático do planeta opera com limiares críticos em que pequenos aumentos térmicos provocam rupturas profundas nos sistemas vivos.
- **Etapa 2:** Com um aquecimento de 1,5°C, estima-se que entre 70% e 90% dos corais sejam danificados; atingindo 2,0°C, a quase totalidade desses ecossistemas colapsa, acompanhada pelo aumento no degelo polar no verão ártico.
- **Etapa 3:** Além dos danos marinhos, esse meio grau a mais submete centenas de milhões de pessoas pobres a secas agrícolas devastadoras e ondas de calor fatais, justificando a urgência da meta de 1,5°C.
""",
        # q49 (D)
        """<!-- id: q49 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: dificil | objeto: justica-climatica-intergeracional-direitos -->
### Questão 49
A emergência climática motivou o crescimento de ações judiciais em diversos países em que jovens e entidades da sociedade civil processam governos por omissão em políticas ambientais. O fundamento ético e normativo dessas ações apoia-se no conceito de Justiça Intergeracional, o qual sustenta que:

a) As decisões econômicas presentes devem priorizar o lucro de curto prazo sem considerar impactos ecológicos posteriores.
b) Os tribunais de justiça só possuem autoridade para analisar obras públicas construídas no século passado.
c) As normas de preservação da natureza devem vigorar apenas durante o período de mandato dos presidentes em exercício.
d) A negligência estatal diante do aquecimento global e do desmatamento compromete os direitos fundamentais à vida, à saúde e a um ambiente equilibrado das gerações atuais e futuras.
e) A compensação de passivos ambientais deve ser realizada por meio de impostos recolhidos unicamente de crianças em fase escolar.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** Constituições democráticas e pactos de direitos humanos asseguram o direito a um meio ambiente equilibrado e seguro para a coletividade.
- **Etapa 2:** O princípio da Justiça Intergeracional expande essa proteção ao estabelecer que a geração presente não tem o direito de dilapidar recursos biológicos e desestabilizar o clima em prejuízo dos que viverão no futuro.
- **Etapa 3:** Assim, magistrados reconhecem que postergar o corte de emissões de carbono e tolerar o desmatamento fere compromissos jurídicos fundamentais com o futuro das crianças e jovens.
""",
        # q50 (E)
        """<!-- id: q50 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: contradicoes-ndcs-paris-combustiveis-fosseis -->
### Questão 50
Uma das discussões levantadas por cientistas e movimentos sociais acerca da redação final do Acordo de Paris de 2015 refere-se ao fato de que o texto oficial do documento:

a) Determina o fechamento imediato de todas as fábricas têxteis do planeta.
b) Exige a substituição das moedas nacionais por títulos de dívida internacional.
c) Estabelece multas sobre residências que utilizem coletores solares para banho quente.
d) Proíbe que dados de satélites meteorológicos sejam divulgados publicamente na imprensa.
e) Não inclui em seus artigos principais termos diretos como 'petróleo', 'carvão mineral' ou 'gás natural', refletindo pressões de produtores de energia fóssil nas negociações.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** A queima de carvão, derivados de petróleo e gás fóssil é a causa primária das emissões de carbono que geram o aquecimento planetário.
- **Etapa 2:** O processo de consenso diplomático da ONU exigiu a aprovação de países grandes produtores e exportadores de petróleo e carvão.
- **Etapa 3:** Para viabilizar a assinatura unânime, o tratado adotou termos gerais sobre redução de emissões líquidas, mas evitou listar expressamente a proibição e eliminação dos combustíveis fósseis pelo nome.
""",
        # q51 (A)
        """<!-- id: q51 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: dificil | objeto: limites-planetarios-centro-resiliencia-estocolmo -->
### Questão 51
O modelo científico dos Limites Planetários (Planetary Boundaries), formulado por pesquisadores do Centro de Resiliência de Estocolmo, estuda nove processos reguladores do equilíbrio da Terra. A análise desse quadro teórico indica que:

a) Limites fundamentais à estabilidade do planeta — como as mudanças climáticas, a perda de biodiversidade e as alterações nos ciclos do nitrogênio e fósforo — já ultrapassaram a zona de segurança.
b) A camada protetora de ozônio na estratosfera expandiu-se de forma descontrolada gerando frio contínuo na linha do Equador.
c) O consumo humano de água doce representa menos de cinco por cento do fluxo renovável das bacias hidrográficas.
d) O processo de acidificação dos mares foi completamente neutralizado por meio da adição de fertilizantes químicos nas praias.
e) O lançamento de partículas artificiais na atmosfera eliminou secas em florestas tropicais.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** O conceito de Limites Planetários avalia fronteiras biofísicas interdependentes que sustentaram a relativa estabilidade do clima durante os últimos dez mil anos.
- **Etapa 2:** As pesquisas mostram que a atividade industrial e o agronegócio intensivo ultrapassaram os níveis de segurança em vários pontos, especialmente no clima, nas taxas de extinção biológica e no excesso de fertilizantes agrícolas.
- **Etapa 3:** A extrapolação desses limites eleva o perigo de que ecossistemas inteiros entrem em colapso, criando condições adversas para a produção de alimentos e para a vida humana no planeta.
""",
        # q52 (B)
        """<!-- id: q52 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: retroalimentacao-albedo-gelo-polar -->
### Questão 52
O albedo polar exerce uma influência direta no equilíbrio térmico do planeta. O mecanismo de retroalimentação gerado pela retração do gelo marinho nas áreas árticas caracteriza-se pelo fato de que:

a) O degelo do mar eleva a salinidade superficial, aumentando a dispersão de raios luminosos de volta ao espaço.
b) O gelo claro e a neve possuem alto albedo e refletem a maior parte da luz solar; ao derreterem, revelam águas marinhas escuras de baixo albedo, que absorvem mais calor e aceleram o aquecimento subsequente.
c) A ausência temporária de geleiras cria barreiras de vapor espesso que bloqueiam ventos solares.
d) O recuo do gelo marinho estimula a germinação de pinheiros gigantes nos fundos rochosos dos oceanos.
e) O escoamento de água fria polar paralisa o vulcanismo ativo das cordilheiras oceânicas.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** O albedo representa a capacidade de reflexão da radiação solar: superfícies brancas de gelo devolvem a maior parte do calor ao espaço sem esquentar a água.
- **Etapa 2:** O aumento da temperatura do ar causa o degelo de calotas e mares congelados, substituindo a superfície branca por água marinha aberta e escura.
- **Etapa 3:** Essa água escura absorve calor em grande escala, esquentando as camadas marítimas superficiais e provocando derretimento ainda mais intenso nas estações seguintes.
""",
        # q53 (C)
        """<!-- id: q53 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: dificil | objeto: caso-sao-sebastiao-comparacao-juquehy-sahy -->
### Questão 53
No estudo do desastre socioambiental ocorrido em São Sebastião (SP) em 2023, a correlação entre geomorfologia, segregação urbana e racismo ambiental evidencia-se ao contrapor a ocupação de praias como Juquehy e Baleia à ocupação da Vila Sahy. Essa análise aponta que:

a) A faixa de Juquehy apresentava encostas frágeis desprovidas de qualquer cobertura florestal nativa.
b) Os moradores da Vila Sahy contavam com serviços particulares de engenharia e muros protetores de pedra.
c) Condomínios de veraneio e hotéis ocuparam a planície plana e protegida da orla, enquanto a população trabalhadora de menor renda instalou-se nas encostas íngremes da Serra do Mar sem saneamento e contenção de encostas.
d) As vítimas fatais da precipitação extrema encontravam-se abrigadas exclusivamente nas salas de resorts à beira-mar.
e) As autoridades locais haviam interditado a orla proibindo a entrada de prestadores de serviços de pousadas.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** A geomorfologia da Serra do Mar possui declives acentuados que sofrem deslizamentos de terra diante de chuvas excepcionalmente concentradas.
- **Etapa 2:** A especulação da terra no litoral reservou as faixas planas e protegidas para imóveis de veraneio; garçons, faxineiras e pedreiros que trabalham nesses locais precisaram habitar encostas de alto risco.
- **Etapa 3:** O volume extraordinário de água atingiu toda a cidade, mas as mortes e soterramentos concentraram-se na encosta desprotegida da Vila Sahy, comprovando que o risco geológico é agravado pela desigualdade social e racial.
""",
        # q54 (D)
        """<!-- id: q54 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: dificil | objeto: cupulas-da-terra-rio-mais-20-economia-verde -->
### Questão 54
Na Conferência Rio+20, realizada no Rio de Janeiro em 2012, debates internacionais abordaram a proposta da chamada 'Economia Verde no Contexto do Desenvolvimento Sustentável'. Setores de movimentos sociais e povos tradicionais reunidos na Cúpula dos Povos contestaram vertentes desse documento sob o argumento de que:

a) A proposta proibia a organização de cooperativas comunitárias de agricultura familiar.
b) O encontro previa o confisco militar de embarcações de pesca artesanal nos estuários.
c) As resoluções diplomáticas perdoavam as dívidas públicas externas de pequenas ilhas caribenhas.
d) A abordagem corria o risco de focar na criação de mercados financeiros sobre a natureza (precificação de serviços ecossistêmicos e papéis ambientais) sem alterar a dependência da matriz energética fóssil e o consumo predatório.
e) O texto determinava a suspensão do fornecimento de eletricidade para cidades com mais de cem mil habitantes.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** A Rio+20 propôs diretrizes para modernizar práticas produtivas sob a bandeira da sustentabilidade econômica e redução de danos.
- **Etapa 2:** Movimentos populares e ambientalistas críticos alertaram para a mercantilização da biosfera: transformar florestas e ciclos da água em títulos financeiros negociáveis não interrompe a queima de fósseis.
- **Etapa 3:** Para esses movimentos, saídas eficazes para a crise climática exigem transformações no modelo energético, reforma agrária, demarcação de terras indígenas e investimentos públicos em transporte coletivo limpo.
""",
        # q55 (E)
        """<!-- id: q55 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: ndcs-mecanismo-catraca-paris -->
### Questão 55
O Acordo de Paris de 2015 previu que as Contribuições Nacionalmente Determinadas (NDCs) fossem revistas e atualizadas a cada cinco anos com compromissos progressivamente maiores. O desafio diplomático e institucional dessa regra reside no fato de que:

a) Os países que não apresentarem novas metas perdem a soberania de seus portos marítimos.
b) A cada cinco anos as nações devem ampliar compulsoriamente a queima de carvão mineral de usinas antigas.
c) Tribunais comerciais têm poder de penhorar o patrimônio escolar de nações com metas atrasadas.
d) Os governos signatários devem colocar suas guardas costeiras sob a coordenação militar direta da ONU.
e) O tratado estabelece a revisão voluntária periódica para aumentar a ambição de cortes, mas não prevê sanções punitivas ou mecanismos judiciais para governos que cumprirem metas insuficientes.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** O modelo diplomático do Acordo de Paris aposta na construção voluntária de metas nacionais por cada país signatário.
- **Etapa 2:** O mecanismo de atualização quinquenal foi planejado para elevar de maneira contínua o rigor das metas de descarbonização em resposta aos relatórios da ciência.
- **Etapa 3:** Como o tratado não dispõe de poder coercitivo ou tribunais de sanção, o cumprimento efetivo depende da pressão política e diplomática internacional, criando o risco de que metas fiquem aquém do necessário.
""",
        # q56 (A)
        """<!-- id: q56 | tipo: multipla-escolha | habilidade: EM13CHS301 | dificuldade: dificil | objeto: efeito-estufa-balanco-radiativo-quimica -->
### Questão 56
O desequilíbrio na retenção de calor provocado pela concentração de gases como o dióxido de carbono e o metano relaciona-se às propriedades físicas dessas moléculas na troposfera. O aquecimento anômalo do ar ocorre porque esses gases:

a) Apresentam ligações que absorvem a radiação na faixa do infravermelho térmico emitida pela superfície terrestre e a reemitem em várias direções, retendo calor na baixa atmosfera acima dos padrões de equilíbrio natural.
b) Bloqueiam a chegada da luz solar nas camadas superiores gerando congelamento contínuo das águas tropicais.
c) Consomem o gás oxigênio disponível tornando o ar das grandes cidades rarefeito e sem pressão.
d) Desfazem as ligações de hidrogênio da água das chuvas gerando vapor corrosivo nos pastos.
e) Alteram as correntes de circulação magnética do núcleo terrestre desviando ventos marítimos.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** A energia vinda do Sol atravessa a atmosfera predominantemente em ondas curtas e aquece o solo e as massas de água.
- **Etapa 2:** A superfície da Terra emite calor sob a forma de radiação infravermelha de ondas longas em direção ao espaço; moléculas como CO2 e CH4 têm a capacidade de absorver essa faixa de frequência.
- **Etapa 3:** Ao absorverem e redistribuírem esse calor, os gases aumentam a energia térmica retida nas camadas inferiores do ar, intensificando o efeito estufa à medida que as emissões industriais elevam sua presença na atmosfera.
""",
        # q57 (B)
        """<!-- id: q57 | tipo: multipla-escolha | habilidade: EM13CHS302 | dificuldade: dificil | objeto: conceito-antropoceno-ruptura-estratigrafica -->
### Questão 57
Em suas pesquisas sobre a transição energética do século XIX, o historiador Andreas Malm argumenta que as primeiras indústrias britânicas não substituíram moinhos hidráulicos por máquinas a vapor devido à escassez de rios na Inglaterra. Em *Fossil Capital*, Malm demonstra que a opção pelo carvão fóssil decorreu principalmente do fato de que:

a) O carvão podia ser recolhido superficialmente sem necessidade de contratar operários.
b) A máquina a vapor permitiu deslocar as fábricas dos vales ribeirinhos rurais para centros urbanos, onde havia maior oferta de trabalhadores assalariados para compor turnos fabris contínuos.
c) As águas dos rios ingleses haviam evaporado completamente devido a alterações térmicas locais.
d) Leis estritas do Parlamento britânico proibiam qualquer tipo de roda d'água no processamento têxtil.
e) O vapor gerado por carvão não produzia fuligem em cidades densamente povoadas.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** Visões econômicas convencionais apontavam que os moinhos de água foram abandonados porque os rios britânicos não tinham mais capacidade de vazão para movimentar novas fábricas.
- **Etapa 2:** Pesquisas históricas recentes comprovaram que a Grã-Bretanha ainda dispunha de energia das águas em abundância e a custos inferiores aos do carvão durante o século XIX.
- **Etapa 3:** A máquina a vapor fóssil triunfou por sua mobilidade espacial: ela libertou o industrial do leito dos rios isolados e permitiu instalar as tecelagens nos centros das cidades, onde havia multidões de trabalhadores disponíveis para jornadas regulares de trabalho.
""",
        # q58 (C)
        """<!-- id: q58 | tipo: multipla-escolha | habilidade: EM13CHS304 | dificuldade: dificil | objeto: eco-92-unfccc-desenvolvimento-sustentavel -->
### Questão 58
A Conferência das Nações Unidas sobre Meio Ambiente e Desenvolvimento (Rio-92 ou Eco-92), realizada no Rio de Janeiro, representou um marco histórico na geopolítica contemporânea ao estabelecer a Convenção-Quadro das Nações Unidas sobre a Mudança do Clima (UNFCCC). O alcance institucional dessa cúpula multilateral caracterizou-se pelo fato de que:

a) Determinou o cancelamento de todos os voos comerciais entre capitais do hemisfério ocidental.
b) Proibiu a utilização de derivados de petróleo em geradores de eletricidade hospitalares.
c) Consagrou internacionalmente o conceito de Desenvolvimento Sustentável e instituiu as COPs anuais para negociar metas diplomáticas globais de contenção do aquecimento planetário.
d) Delegou a corporações privadas de navegação a soberania sobre o controle das águas fluviais amazônicas.
e) Extinguiu a atuação do IPCC transferindo a análise climática para bancos comerciais de investimento.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** A Eco-92 reuniu mais de cem chefes de Estado no Riocentro, projetando a temática ambiental para o topo da diplomacia global.
- **Etapa 2:** O encontro oficializou as diretrizes do Relatório Brundtland de 1987, definindo o Desenvolvimento Sustentável como a conciliação entre atendimento das necessidades presentes e preservação das condições vitais das futuras gerações.
- **Etapa 3:** A criação da UNFCCC na Rio-92 inaugurou o calendário das Conferências das Partes (COPs), constituindo o fórum permanente da ONU sob o qual seriam negociados tratados subsequentes como o Protocolo de Quioto (1997) e o Acordo de Paris (2015).
""",
        # q59 (D)
        """<!-- id: q59 | tipo: multipla-escolha | habilidade: EM13CHS305 | dificuldade: dificil | objeto: desmatamento-brasil-emissoes-diferenca-perfil -->
### Questão 59
Ao confrontar o perfil das emissões de gases de efeito estufa do Brasil com o dos países desenvolvidos do Norte Global (como Estados Unidos ou nações europeias), constata-se uma diferença marcante na origem dos poluentes. Essa divergência reside no fato de que:

a) O Brasil emite carbono prioritariamente por meio de seu transporte ferroviário de passageiros movido a carvão mineral.
b) As nações europeias dependem do corte sistemático de florestas temperadas para expandir a pecuária de corte.
c) A indústria pesada automobilística das cidades brasileiras queima a maior parte do gás natural extraído na América do Sul.
d) Enquanto nas economias ricas as emissões decorrem fortemente da queima fóssil nos setores de energia e transportes, no Brasil a maior parte das emissões provém da mudança no uso da terra, com ênfase no desmatamento e queimadas na Amazônia e no Cerrado.
e) As propriedades agrícolas familiares nos países desenvolvidos não utilizam tratores nem insumos industriais em suas rotinas.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** Em nações altamente industrializadas do Norte, as emissões de gases concentram-se na geração de eletricidade fóssil (carvão e gás) e no combustível consumido por frotas de automóveis e aquecimento doméstico.
- **Etapa 2:** O Brasil apresenta uma matriz elétrica com ampla presença de fontes renováveis como a hidrelétrica, biomassa, solar e eólica, o que reduz o peso relativo do setor energético em suas emissões.
- **Etapa 3:** O grande motor das emissões de gases no território brasileiro localiza-se na queima de vegetação nativa e na expansão agropecuária desordenada na Amazônia e no Cerrado, tornando a proteção das florestas a principal medida do país contra a crise do clima.
""",
        # q60 (E)
        """<!-- id: q60 | tipo: multipla-escolha | habilidade: EM13CHS306 | dificuldade: dificil | objeto: justica-climatica-e-povos-originarios-demarcacao -->
### Questão 60
A conexão entre Justiça Climática, Direitos Humanos e preservação de florestas no século XXI reforça a importância conferida à demarcação e proteção das Terras Indígenas e Territórios Quilombolas. A comprovação científica e social dessa diretriz apoia-se no fato de que:

a) As populações originárias e tradicionais devem ser transferidas para núcleos urbanos para facilitar programas de reciclagem de materiais.
b) As áreas manejadas por povos originários apresentam maior degradação do solo devido ao uso de ferramentas de ferro.
c) O avanço do garimpo de ouro em territórios tradicionais melhora a circulação hídrica em igarapés amazônicos.
d) As regras de zoneamento ecológico recomendam arrendar áreas florestais para culturas de eucalipto para celulose.
e) Povos indígenas e comunidades tradicionais atuam como protetores fundamentais da vegetação viva e de estoques de carbono, de modo que assegurar seus direitos territoriais é uma das estratégias mais seguras e justas de combate à emergência climática.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** Diagnósticos de organizações ambientais comprovam que os índices de desmatamento e perda de biodiversidade são substancialmente menores em áreas sob tutela e manejo de povos tradicionais.
- **Etapa 2:** Ao garantirem a permanência da floresta viva e combaterem a entrada de invasores ilegais, essas comunidades conservam imensas quantidades de carbono no solo e na vegetação arbórea.
- **Etapa 3:** Dessa maneira, o reconhecimento de direitos de posse da terra e a segurança física das lideranças tradicionais unem a justiça histórica aos direitos humanos e ao equilíbrio climático de toda a humanidade.
"""
    ]

    references_section = """
## Referências

- ALMEIDA, Silvio Luiz de. *Racismo Estrutural*. São Paulo: Pólen Livros, 2019.
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/SEB, 2018.
- CHAKRABARTY, Dipesh. *O Clima da História em uma Época Planetária*. Rio de Janeiro: Bazar do Tempo, 2023.
- CRUTZEN, Paul J. Geology of mankind. *Nature*, v. 415, p. 23, 2002.
- DANOWSKI, Déborah; VIVEIROS DE CASTRO, Eduardo. *Há Mundo por Vir? Ensaio sobre os Medos e os Fins*. Desterro [Florianópolis]: Cultura e Barbárie; Instituto Socioambiental, 2014.
- INTERGOVERNMENTAL PANEL ON CLIMATE CHANGE (IPCC). *Climate Change 2023: Synthesis Report*. Genebra: IPCC, 2023.
- MALM, Andreas. *Fossil Capital: The Rise of Steam Power and the Roots of Global Warming*. Londres: Verso, 2016.
- MOORE, Jason W. (Ed.). *Anthropocene or Capitalocene? Nature, History, and the Crisis of Capitalism*. Oakland: PM Press, 2016.
- ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). *Acordo de Paris sob a Convenção-Quadro das Nações Unidas sobre Mudança do Clima*. Paris: ONU, 2015.
"""

    output_lines = [frontmatter]
    output_lines.extend(questions_basic)
    output_lines.append("\n## Nível Intermediário (Questões 21-40)\n")
    output_lines.extend(questions_inter)
    output_lines.append("\n## Nível Difícil (Questões 41-60)\n")
    output_lines.extend(questions_hard)
    output_lines.append(references_section)

    content = "\n".join(output_lines)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    draft_path = os.path.join(project_root, "temp_draft_c53.md")

    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Draft c53 generated with {len(content)} characters at {draft_path}")

if __name__ == "__main__":
    build_draft_c53()
