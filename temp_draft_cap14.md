---
série: "9º Ano"
disciplina: "Matemática"
unidade_temática: "Geometria"
objeto_de_conhecimento: "Distância entre pontos no plano cartesiano"
habilidades: "EF09MA16"
pré-requisitos: "Relações métricas no triângulo retângulo e Teorema de Pitágoras"
nível_dificuldade: "Básico"
tempo_estimado_de_leitura: "15 minutos"
status_de_revisao: "Produzido"
palavras_chave: ["Plano Cartesiano", "Distância", "Coordenadas", "Geometria Analítica", "Pitágoras"]
fonte_bibliografica: "Base Nacional Comum Curricular (BNCC); Fundamentos de Matemática Elementar - Gelson Iezzi"
---

# Distância entre pontos no plano cartesiano

## Conceitos

A união brilhante da álgebra com a geometria ocorreu quando René Descartes formalizou o sistema de coordenadas retangulares, o chamado plano cartesiano. Por meio dele, figuras geométricas passam a ser descritas por equações algébricas e pontos tornam-se pares ordenados de números reais. O conceito inaugural que ancora a Geometria Analítica é, inevitavelmente, o cálculo da distância entre dois pontos. 

Compreender como a distância atua em um plano cartesiano é compreender a transição entre dimensões espaciais lineares e métricas matemáticas abstratas.

**Definição do Sistema de Coordenadas**
Um ponto genérico $P$ no plano é definido por um par ordenado $(x_P, y_P)$, onde:
- $x_P$ (abscissa) indica o distanciamento horizontal do ponto em relação ao eixo vertical (eixo das ordenadas, $y$).
- $y_P$ (ordenada) indica o distanciamento vertical do ponto em relação ao eixo horizontal (eixo das abscissas, $x$).

**Casos Específicos de Distância Unidimensional**
Antes de explorarmos a distância geral, devemos entender as distâncias paralelas aos eixos.
1. **Pontos alinhados horizontalmente:** Se dois pontos $A(x_A, y)$ e $B(x_B, y)$ possuem a mesma ordenada ($y$), o segmento de reta que os liga é paralelo ao eixo $x$. A distância entre eles é dada pela diferença absoluta (módulo) entre suas abscissas:
$d(A,B) = |x_B - x_A|$
2. **Pontos alinhados verticalmente:** Se dois pontos $A(x, y_A)$ e $B(x, y_B)$ possuem a mesma abscissa ($x$), o segmento de reta que os liga é paralelo ao eixo $y$. A distância entre eles é a diferença absoluta de suas ordenadas:
$d(A,B) = |y_B - y_A|$

**A Distância Geral: Dedução pela Geometria Plana**
O caso geral de distância ocorre quando dois pontos quaisquer, $A(x_A, y_A)$ e $B(x_B, y_B)$, não estão sobre a mesma linha horizontal nem sobre a mesma linha vertical.
O segmento que liga $A$ até $B$ será oblíquo aos eixos cartesianos. Para determinarmos a exata medida deste segmento $AB$ (a distância escalar $d(A,B)$), nós construímos um triângulo retângulo auxiliar cujos catetos sejam paralelos aos eixos coordenados.

1. Traçamos uma reta horizontal passando por $A$ e uma reta vertical passando por $B$. A interseção dessas retas forma um ponto $C$, cujas coordenadas serão obrigatoriamente $(x_B, y_A)$.
2. O triângulo $\triangle ACB$ resultante é, por construção, um triângulo retângulo em $C$.
3. A hipotenusa deste triângulo é exatamente o segmento de reta $AB$, que representa a distância que buscamos, $d(A,B)$.
4. O cateto horizontal $AC$ é paralelo ao eixo $x$, portanto mede $|x_B - x_A|$.
5. O cateto vertical $CB$ é paralelo ao eixo $y$, medindo $|y_B - y_A|$.

Aplicando o Teorema de Pitágoras no triângulo $\triangle ACB$, temos:
$(\text{Hipotenusa})^2 = (\text{Cateto}_1)^2 + (\text{Cateto}_2)^2$
$[d(A,B)]^2 = (x_B - x_A)^2 + (y_B - y_A)^2$

Para encontrar a distância escalar, extraímos a raiz quadrada, chegando à clássica **Fórmula da Distância entre Dois Pontos**:
$d(A,B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$

Esta fórmula, essencialmente pitagórica, é a métrica base de todos os cálculos de Geometria Analítica subsequentes e é universalmente válida para quaisquer dois pontos do plano, sejam eles positivos, negativos ou nulos.

## Exemplos (Na Prática)

**Exemplo 1: Aplicação direta da fórmula (Pontos no 1º Quadrante)**
Calcule a distância entre os pontos $A(2, 3)$ e $B(5, 7)$.
*Resolução lógica:*
Temos as abscissas: $x_A = 2$, $x_B = 5$. A diferença entre as coordenadas $x$ é $\Delta x = 5 - 2 = 3$.
Temos as ordenadas: $y_A = 3$, $y_B = 7$. A diferença entre as coordenadas $y$ é $\Delta y = 7 - 3 = 4$.
Aplicando a fórmula da distância deduzida via Pitágoras:
$d(A,B) = \sqrt{(\Delta x)^2 + (\Delta y)^2}$
$d(A,B) = \sqrt{(3)^2 + (4)^2}$
$d(A,B) = \sqrt{9 + 16}$
$d(A,B) = \sqrt{25} = 5$.
A distância entre os pontos é de 5 unidades. (Observe que isso formou um triângulo retângulo pitagórico 3, 4, 5).

**Exemplo 2: Pontos com coordenadas negativas (Jogo de sinais)**
Qual é a distância do ponto $C(-4, 1)$ à origem do sistema cartesiano $O(0, 0)$?
*Resolução lógica:*
Coordenadas do ponto $C$: $x_C = -4, y_C = 1$.
Coordenadas do ponto $O$: $x_O = 0, y_O = 0$.
Calculando a diferença para $x$: $\Delta x = x_O - x_C = 0 - (-4) = 0 + 4 = 4$.
Calculando a diferença para $y$: $\Delta y = y_O - y_C = 0 - 1 = -1$.
Aplicando a fórmula:
$d(C,O) = \sqrt{(4)^2 + (-1)^2}$
$d(C,O) = \sqrt{16 + 1}$
$d(C,O) = \sqrt{17}$.
A distância é $\sqrt{17}$ unidades.

**Exemplo 3: Provando que um triângulo é isósceles**
Os vértices de um triângulo são os pontos $P(1, 2)$, $Q(4, 5)$ e $R(1, 8)$. Prove que este triângulo é isósceles.
*Resolução lógica:*
Para provar que é isósceles, precisamos demonstrar que ele possui, pelo menos, dois lados de mesma medida. Devemos calcular a distância dos três lados:
Lado $PQ$: $d = \sqrt{(4-1)^2 + (5-2)^2} = \sqrt{3^2 + 3^2} = \sqrt{9+9} = \sqrt{18}$.
Lado $Qreais: $d = \sqrt{(1-4)^2 + (8-5)^2} = \sqrt{(-3)^2 + 3^2} = \sqrt{9+9} = \sqrt{18}$.
Lado $Preais: $d = \sqrt{(1-1)^2 + (8-2)^2} = \sqrt{0^2 + 6^2} = \sqrt{36} = 6$.
Como a distância $PQ$ é idêntica à distância $Qreais (ambas medem $\sqrt{18}$), provamos analiticamente que o triângulo $\triangle PQreais é isósceles.

## Erros Comuns

| Padrão de Erro | Explicação | Raciocínio Corretivo |
|----------------|------------|----------------------|
| Erro de sinal nas diferenças. | O aluno erra a aritmética ao subtrair coordenadas negativas: ex, ao calcular $(2 - (-3))$, acaba escrevendo $2 - 3 = -1$. | Sempre usar parênteses auxiliares: $2 - (-3)$ torna-se $2 + 3 = 5$. O quadrado anulará os sinais, mas o valor de $\Delta$ ficará correto. |
| Soma dos quadrados sem o parênteses correto. | Ao elevar diferenças negativas ao quadrado, ex: $-3^2$, o aluno anota como $-9$. | Qualquer número real (positivo ou negativo) elevado ao quadrado dentro da fórmula resultará em um valor **positivo**. $(-3)^2 = +9$. |
| Esquecer a raiz quadrada final. | O aluno calcula $(\Delta x)^2 + (\Delta y)^2$ e esquece de colocar o resultado na raiz. | O número encontrado sem a raiz é o **quadrado** da distância. Como o Teorema de Pitágoras define $d^2$, o passo final imutável é extrair a raiz quadrada. |

## Conexões Interdisciplinares

A geometria analítica fundamenta as tecnologias modernas. Na **Computação e Navegação**, os sistemas de GPS (Global Positioning System) utilizam o conceito de distância geométrica tridimensional para triangulação, mas, para mapas 2D (telas de aplicativos de mobilidade como Uber, Waze), a lógica de cálculo de rotas em linha reta usa a exata distância cartesiana abordada aqui. No **Desenvolvimento de Jogos Digitais (Programação)**, algoritmos de detecção de colisão entre objetos em uma tela 2D verificam frequentemente se a distância cartesiana entre os centros dos pixels de dois personagens é menor do que o raio do hitbox, acionando assim o evento de impacto no jogo.

## Resumo para Revisão

- O plano cartesiano possui um eixo das abscissas ($x$, horizontal) e das ordenadas ($y$, vertical), definindo pontos por pares ordenados $(x, y)$.
- Para segmentos paralelos aos eixos, a distância é a diferença absoluta das respectivas coordenadas (variação).
- Para a distância geral entre quaisquer dois pontos $A(x_A, y_A)$ e $B(x_B, y_B)$, a fórmula baseia-se diretamente na formação de um triângulo retângulo imaginário.
- A Fórmula é $d(A,B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.
- Sendo derivada de Pitágoras, o interior da raiz será sempre uma soma de números não negativos. Diferenças negativas tornam-se positivas ao quadrado.
- A Geometria Analítica permite comprovar propriedades de figuras, como o perímetro e a simetria de triângulos, através de rigor algébrico.

---
## Referências
- BRASIL. Ministério da Educação. Base Nacional Comum Curricular. Brasília: MEC, 2018.
- IEZZI, Gelson. Fundamentos de Matemática Elementar 7: Geometria Analítica. 6. ed. São Paulo: Atual, 2013.
- DANTE, Luiz Roberto. Matemática: projeto Teláris. 3. ed. São Paulo: Ática, 2018.

---
> **Nota do Arquiteto:** Este e-book é 100% teórico. Os 60 exercícios correspondentes a este Objeto de Conhecimento deverão ser gerados posteriormente em um arquivo separado (`[objeto-de-conhecimento]-exercicios.md`) utilizando a skill **Exercise Creator**.
