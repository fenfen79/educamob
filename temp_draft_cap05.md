---
série: "9º Ano"
disciplina: "Matemática"
unidade_temática: "Álgebra"
objeto_de_conhecimento: "Funções: representações numérica, algébrica e gráfica"
habilidades: "EF09MA06"
pré-requisitos: "N/A"
nível_dificuldade: "Intermediário"
tempo_estimado_de_leitura: "25 minutos"
status_de_revisao: "Produzido"
palavras_chave: ["Função", "Domínio", "Imagem", "Representação Gráfica", "Expressão Algébrica", "Plano Cartesiano", "Variável Independente", "Variável Dependente"]
fonte_bibliografica: "Base Nacional Comum Curricular (BNCC)"
---

# Funções: representações numérica, algébrica e gráfica

## Conceitos

O conceito de função é o epicentro do pensamento matemático moderno, servindo como a ponte suprema entre a álgebra pura, a geometria analítica e a modelagem do mundo real. Na essência, a Matemática abandonou o estudo estático de números e formas isoladas para focar no dinamismo das relações de interdependência, perguntando-se como grandezas se comportam quando submetidas à alteração contínua de outras grandezas correlacionadas. A formalização desse comportamento dinâmico é a própria fundação do Cálculo Diferencial. O primeiro passo estrutural para esse panorama é a consolidação do objeto matemático chamado Função.

Em termos rigorosos, dados dois conjuntos não vazios $A$ e $B$, uma função $f$ de $A$ em $B$ (notação: $f: A \to B$) é uma regra matemática inexorável que associa a **cada** elemento $x$ pertencente ao conjunto $A$, **um, e somente um**, elemento $y$ pertencente ao conjunto $B$. 
Essa definição aparentemente simples esconde duas condições vitais de existência. A primeira condição exige a totalidade de domínio: todos os elementos no conjunto de partida ($A$) devem disparar uma associação; não é permitido que haja um valor de entrada para o qual a função "não saiba" o que fazer ou falhe (desde que esse valor esteja no domínio definido). A segunda condição restringe a unicidade do resultado: um elemento $x$ de entrada não pode apontar para múltiplos elementos no conjunto de chegada; para uma mesma causa determinística, deve haver um único efeito correspondente.

Nesta arquitetura relacional, o elemento $x$ é a *variável independente*, a causa fundamental; o conjunto $A$ recebe a nomenclatura técnica de Domínio da Função ($D$). O elemento associado $y$, também escrito como $f(x)$ (lê-se "efe de x"), é a *variável dependente*, o efeito mensurado. O conjunto de chegada amplo é o Contradomínio ($CD$), enquanto o subconjunto exato dos elementos de $B$ que efetivamente foram atingidos pelas setas disparadas por $x$ constitui o conjunto Imagem ($Im$). 

A compreensão plena de uma função não ocorre pela fixação em um único prisma estrutural, mas sim pela transição orgânica e bidirecional entre suas múltiplas facetas de representação. O domínio sólido deste objeto demanda fluidez em três diferentes registros, onde cada representação fornece uma camada de inteligência distinta, superando as limitações intrínsecas das outras:

**1. Representação Numérica (Tabelas e Pares Ordenados):**
A abstração teórica muitas vezes tem origem em medições experimentais diretas, que geram catálogos e tabulações de dados (como aferições temporais e posições em um laboratório). Organizar os dados em colunas de $x$ e colunas de $y$ (ou pares ordenados $(x, y)$) estabelece a visão elementar da função. A tabela evidencia de forma tangível a relação ponto a ponto, permitindo inspeções discretas. Contudo, essa abordagem é limitada por amostragem: não é possível tabular os infinitos pontos de um domínio real, perdendo-se o comportamento inter-dados.

**2. Representação Algébrica (Lei de Formação):**
Para solucionar o hiato da infinitude, a álgebra cria a Lei de Formação ou Regra Geral. Em vez de registrar todos os cruzamentos e retornos, elabora-se uma expressão matemática concisa, uma "máquina de processamento", que ditará exatamente o que ocorrerá com qualquer $x$ genérico injetado nela, como $f(x) = 2x + 5$. A lei algébrica condensa o padrão infinito em uma formulação manipulável pelas ferramentas operatórias (fatorações, igualdades, derivadas), viabilizando previsões de comportamentos para eventos que estão no escopo do infinito ou do irreal, mas mantendo certa aridez interpretativa para perfis complexos.

**3. Representação Gráfica (Plano Cartesiano):**
O apogeu da cognição humana na compressão de funções foi cunhado por René Descartes: a tradução da lei algébrica para a geometria euclidiana do plano cartesiano. Transformando a variável independente ($x$) no eixo horizontal das abcissas e a dependente ($f(x)$) no eixo vertical das ordenadas, todo par ordenado constrói um ponto no espaço. O conjunto integral desses infinitos pontos funde-se em uma curva contínua geométrica. O gráfico proporciona visualização instantânea de tendências globais do fenômeno. Sem calcular número algum, ao lançar os olhos sobre uma curva, um analista extrai as taxas de crescimento (crescente/decrescente), os vértices (pontos de máximos ou mínimos limites) e raízes reais da equação (onde o gráfico quebra o eixo abcissal $x$).

## Exemplos (Na Prática)

**Exemplo 1: Do Tabular e Experimental à Lei Algébrica Universal**

Um motorista de aplicativo analisa as planilhas financeiras semanais para calcular seu rendimento mensal previsível. Ao cruzar dados sobre as corridas feitas, ele monta a seguinte representação numérica reduzida:
- Viagem de 5 km (x=5) -> Pagamento de 15,00 reais (y=15)
- Viagem de 10 km (x=10) -> Pagamento de 25,00 reais (y=25)
- Viagem de 15 km (x=15) -> Pagamento de 35,00 reais (y=35)

Para ir do ambiente numérico para a formulação algébrica que generaliza todas as infinitas distâncias possíveis, o motorista precisa discernir o padrão iterativo da mudança. 
Observando o avanço na tabela, constatamos que sempre que a distância $x$ cresce em 5 km de volume fixo, o pagamento $y$ sofre um acréscimo de exatos 10,00 reais. Isso indica que cada 1 km rodado acrescenta isoladamente 2,00 reais (taxa contínua de variação: 10 / 5).
Porém, se a taxa por km é 2,00 reais, para 5 km o valor seria de apenas 10,00 reais, e o motorista cobrou 15,00 reais. Restam 5,00 reais não associados à distância. Da mesma forma, em 10 km rodados seriam devidos 20,00 reais, e constam 25,00 reais (reaparecendo o saldo não justificado de 5,00 reais fixos). 

Logo, ele constrói a Lei de Formação (representação algébrica): $f(x) = 2x + 5$, onde 2 é a taxa por quilômetro rodado (coeficiente angular da variância dinâmica) e 5 é o valor da tarifa fixa inicial ou bandeirada (termo constante e coeficiente linear). Essa função polinomial do primeiro grau engloba todo o fenômeno de precificação perfeitamente e permite que o sistema compute distâncias altamente específicas, como 12,4 km rodados.

**Exemplo 2: Interpretação Avançada na Representação Gráfica**

Dada a representação algébrica de uma função de segundo grau clássica da balística: $h(t) = -5t^2 + 20t$, onde $h$ seria a altura final de uma pequena peça balística lançada do solo (em metros) num instante futuro medido no tempo $t$ (em segundos).

A análise através de representações numéricas tabuladas ($t=1$, $t=2$) seria imprecisa para determinar perfeitamente o comportamento completo do evento. O recurso à representação gráfica no plano cartesiano trará luzes imediatas.
Plotando os infinitos pontos da equação sobre o eixo cartesiano, o gráfico revelará a figura geométrica de uma parábola simétrica com a concavidade estrutural voltada diretamente para baixo (devido à constante negativa do fator $t^2$). 
Olhando o eixo horizontal das abscissas do plano (Tempo $t$), observaremos que o traçado denso da curva cruzará o eixo do tempo nos pontos 0 e 4 ($t = 0$ e $t = 4$). O que essa representação extrai analiticamente? Que as raízes reais informam o momento singular e exato do lançamento inicial no chão e também o evento pontual em que a peça cruza a altura 0 impactando o solo no retorno (4 segundos da balística inteira). 
Ao mirar no ápice alto e isolado da parábola, situado temporalmente em $t = 2$, com cruzamento na ordenada em $y = 20$, o engenheiro colhe o vértice isolado da função, atestando rapidamente que a altura máxima intransponível do objeto na trajetória percorrida será rigorosamente de 20 metros. A curva entrega a totalidade relacional da física contida no evento.

## Erros Comuns

| Padrão de Erro | Explicação | Raciocínio Corretivo |
|----------------|------------|----------------------|
| Desvio da Unicidade de Imagem | Traçar figuras aleatórias (como circunferências puras no plano) e assumi-las funcionalmente como gráficos. | Círculos ou ovais violam a restrição primária de função, pois um único ponto fixo no eixo $x$ terá correspondência com dois eixos $y$ (acima e abaixo). O Teste Geométrico da Reta Vertical exige que, em funções reais, nenhuma linha perpendicular ao eixo das abcissas possa interceptar a linha curva gráfica funcional do gráfico mais que uma única vez na extensão total do desenho cartesiano. |
| Tratamento confuso entre o zero da função e o termo independente | Acreditar que a raiz da função e a interseção do gráfico com o eixo Y são idênticas, trocando os locais físicos de ocorrência. | A raiz (o zero da equação) é o exato momento onde $f(x) = 0$, quebrando cruzado no eixo horizontal. A interseção autônoma do termo de $y$ (como no ponto 5 do táxi) acontece no cruzamento exato e único do eixo vertical, quando $x$ é anulado a 0. |

## Conexões Interdisciplinares

As funções operam a maior parte dos arcabouços de tecnologia pesada civilizacional:
- **Biomedicina (Epidemiologia):** As funções formam a barreira analítica contra pragas, desenhando e plotando as curvas matemáticas famosas ("achatar a curva") que refletem variações numéricas diárias na incidência. Gráficos sigmoidais (em formato de S prolongado) ou puramente exponenciais definem a velocidade exata temporal de contágio ou extinção biológica em hospedeiros de vírus.
- **Microeconomia:** Todo o arranjo teórico de Oferta vs. Demanda materializa-se como o confronto explícito e gráfico de duas funções no plano: uma reta decrescente de demanda frente aos consumidores contrapondo-se à curva rígida progressiva dos estoques; o ponto final de interseção entre ambas as leis algébricas marca analiticamente o preço de equilíbrio absoluto do item num mercado estável e perfeito do capital comercial.
- **Análise Computacional, Big Data e Machine Learning:** Máquinas extraem inteligência oculta regressiva tabulando quantidades exaustivas em Big Data e gerando de modo reversível uma "função de aproximação" profunda de pesos iterativos (deep learning) que dita os pesos visuais gráficos na construção vetorial exata para o comportamento do bot ou algoritmo financeiro corporativo das redes. 

## Resumo para Revisão

- Funções são estruturas correlacionais diretas determinísticas, associando um, e somente um, resultado dependente a cada entrada estrita independente.
- O Domínio representa as "entradas admissíveis", e a Imagem abrange integralmente os "resultados atingidos" na realidade matemática.
- A representação Numérica ou Tabular é a catalogação bruta e primária experimental dos dados interligados observados isoladamente.
- A representação Algébrica impõe condensação universal infinitiva na fórmula de cálculo ($f(x)$) abrangendo comportamentos ilimitados não tabuláveis.
- A representação Gráfica sobre o plano Cartesiano permite extração de inteligência visual instantânea (curvas, máximos, pontos mortos) da totalidade cinemática ou estática subjacente, superando o peso e o cansaço lógico dos exames numéricos pontuais no papel físico isolado.

---
## Referências
- IEZZI, Gelson; MURAKAMI, Carlos. Fundamentos de Matemática Elementar: Conjuntos e Funções. 9. ed. São Paulo: Atual, 2013.
- DANTE, Luiz Roberto. Matemática: Contexto & Aplicações. 3. ed. São Paulo: Ática, 2017.
- LIMA, Elon Lages. A Matemática do Ensino Médio: Volume 1. 9. ed. Rio de Janeiro: SBM, 2006.
- BRASIL. Ministério da Educação. Base Nacional Comum Curricular. Brasília: MEC/SEB, 2018.

---
> **Nota do Arquiteto:** Este e-book é 100% teórico. Os 60 exercícios correspondentes a este Objeto de Conhecimento deverão ser gerados posteriormente em um arquivo separado (`funcoes-representacoes-exercicios.md`) utilizando a skill **Exercise Creator**.
