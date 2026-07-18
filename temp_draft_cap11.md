---
série: "9º Ano"
disciplina: "Matemática"
unidade_temática: "Geometria"
objeto_de_conhecimento: "Semelhança de triângulos"
habilidades: "EF09MA12"
pré-requisitos: "N/A"
nível_dificuldade: "Intermediário"
tempo_estimado_de_leitura: "20 minutos"
status_de_revisao: "Produzido"
palavras_chave: ["Semelhança", "Triângulos", "Proporcionalidade", "Razão", "Geometria Euclidiana"]
fonte_bibliografica: "Base Nacional Comum Curricular (BNCC); Fundamentos de Matemática Elementar - Osvaldo Dolce e José Nicolau Pompeo"
---

# Semelhança de Triângulos

## Conceitos

A geometria euclidiana fundamenta-se fortemente nas noções de congruência e semelhança. Enquanto a congruência trata de figuras idênticas em forma e tamanho, a semelhança estuda figuras que possuem a mesma forma, mas não necessariamente o mesmo tamanho. Para os polígonos em geral, dizemos que dois polígonos são semelhantes quando seus ângulos correspondentes são congruentes (têm a mesma medida) e seus lados homólogos (correspondentes) são proporcionais. 

Quando focamos especificamente nos triângulos, a semelhança ganha contornos particulares e propriedades matemáticas incrivelmente robustas. O estudo da semelhança de triângulos não apenas simplifica a resolução de problemas métricos, mas também serve como pilar para a trigonometria e para o cálculo de distâncias inacessíveis.

**Definição Formal de Semelhança de Triângulos**
Dois triângulos, ABC e A'B'C', são considerados semelhantes (indicado por $\triangle ABC \sim \triangle A'B'C'$) se, e somente se, satisfazem simultaneamente a duas condições:
1. Seus ângulos correspondentes são congruentes: $\hat{A} \cong \hat{A}'$, $\hat{B} \cong \hat{B}'$ e $\hat{C} \cong \hat{C}'$.
2. Seus lados homólogos são proporcionais: $\frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{CA}{C'A'} = k$, onde $k$ é a constante de proporcionalidade ou razão de semelhança.

Diferentemente de polígonos com mais lados, nos triângulos as condições estão intrinsicamente ligadas. Se os ângulos de dois triângulos são congruentes, seus lados correspondentes serão inevitavelmente proporcionais, e vice-versa. Essa característica nos permite estabelecer os chamados **Casos de Semelhança**, que são critérios mínimos para garantir a semelhança sem precisar verificar todas as medidas de lados e ângulos.

**Casos de Semelhança de Triângulos**

1. **Caso AA (Ângulo-Ângulo):** 
Se dois ângulos de um triângulo são congruentes a dois ângulos correspondentes de outro triângulo, então esses dois triângulos são semelhantes. Este é o critério mais utilizado.
*Demonstração lógica:* Sabemos que a soma dos ângulos internos de qualquer triângulo é sempre 180°. Logo, se dois triângulos possuem dois ângulos com a mesma medida, o terceiro ângulo, sendo o suplemento da soma dos dois primeiros, obrigatoriamente também terá a mesma medida. Com os três ângulos congruentes, os triângulos são semelhantes.

2. **Caso LAL (Lado-Ângulo-Lado):**
Se as medidas de dois lados de um triângulo são proporcionais às medidas de dois lados correspondentes de outro triângulo, e os ângulos formados por esses lados são congruentes, então os triângulos são semelhantes.

3. **Caso LLL (Lado-Lado-Lado):**
Se as medidas dos três lados de um triângulo são proporcionais às medidas dos três lados correspondentes de outro triângulo, então eles são semelhantes.

**Teorema Fundamental da Semelhança**
Se uma reta é paralela a um dos lados de um triângulo e intercepta os outros dois lados em pontos distintos, então o triângulo que ela determina é semelhante ao triângulo original.
*Exemplo analítico:* No $\triangle ABC$, se traçarmos uma reta $r$ paralela ao lado $BC$, cortando $AB$ no ponto $D$ e $AC$ no ponto $E$, formamos um novo triângulo $\triangle ADE$. Pelo paralelismo, os ângulos correspondentes são iguais ($\hat{D} \cong \hat{B}$ e $\hat{E} \cong \hat{C}$). O ângulo $\hat{A}$ é comum a ambos. Pelo caso AA, $\triangle ADE \sim \triangle ABC$.

**Propriedades Adicionais (Razões entre Elementos Homólogos)**
Se dois triângulos são semelhantes com razão de semelhança $k$:
- A razão entre seus perímetros é igual a $k$.
- A razão entre suas alturas, medianas ou bissetrizes correspondentes também é igual a $k$.
- A razão entre suas áreas é igual ao quadrado da razão de semelhança, ou seja, $k^2$. Isso se deve ao fato de a área resultar do produto de duas dimensões lineares (base e altura, por exemplo), ambas multiplicadas por $k$.

## Exemplos (Na Prática)

**Exemplo 1: Cálculo de distância inacessível (O Método de Tales)**
Tales de Mileto calculou a altura da pirâmide de Quéops utilizando a sombra projetada pelo sol. Imagine que um bastão fincado verticalmente no chão tem 2 metros de altura e projeta, em determinado momento, uma sombra de 0,5 metros. No mesmo instante, uma torre projeta uma sombra de 15 metros. Qual a altura da torre?
*Resolução lógica:*
Como os raios solares podem ser considerados paralelos devido à imensa distância do sol, os ângulos formados entre os raios solares e o solo são congruentes. Tanto a torre quanto o bastão formam um ângulo de 90° com o solo. 
Assim, formamos dois triângulos semelhantes pelo caso AA.
Sendo $H$ a altura da torre e $h = 2$ a altura do bastão, $S = 15$ a sombra da torre e $s = 0,5$ a sombra do bastão, temos a proporção:
$\frac{H}{h} = \frac{S}{s} \implies \frac{H}{2} = \frac{15}{0,5} \implies \frac{H}{2} = 30 \implies H = 60$.
A altura da torre é de 60 metros.

**Exemplo 2: O Teorema Fundamental da Semelhança em Ação**
Em um triângulo $ABC$, o lado $BC$ mede 20 cm. Uma reta paralela a $BC$ corta os lados $AB$ e $AC$ nos pontos $D$ e $E$, respectivamente. Sabendo que $AD = 4$ cm e $DB = 6$ cm, qual é a medida do segmento $DE$?
*Resolução lógica:*
Pelo Teorema Fundamental da Semelhança, como $DE \parallel BC$, o triângulo $ADE$ é semelhante ao triângulo $ABC$.
O lado correspondente a $AD$ no triângulo maior é $AB$.
$AB = AD + DB = 4 + 6 = 10$ cm.
A razão de semelhança entre os lados é $\frac{AD}{AB} = \frac{DE}{BC}$.
Substituindo os valores conhecidos:
$\frac{4}{10} = \frac{DE}{20}$.
Multiplicando cruzado ou simplificando: $DE = \frac{4 \times 20}{10} = \frac{80}{10} = 8$ cm.
A medida do segmento $DE$ é 8 cm.

**Exemplo 3: Relação entre áreas de triângulos semelhantes**
Dois triângulos semelhantes têm razão de semelhança igual a 3. Se a área do menor triângulo é 15 cm², qual é a área do maior?
*Resolução lógica:*
Sabemos que a razão entre as áreas de dois polígonos semelhantes é o quadrado da razão de semelhança das medidas lineares ($k^2$).
Se $k = 3$, a razão entre as áreas será $3^2 = 9$.
Portanto, a área do triângulo maior ($A_2$) é 9 vezes a área do triângulo menor ($A_1$).
$A_2 = 9 \times 15 = 135$ cm².

## Erros Comuns

| Padrão de Erro | Explicação | Raciocínio Corretivo |
|----------------|------------|----------------------|
| Confundir semelhança com congruência. | O aluno presume que triângulos semelhantes possuem as mesmas medidas de lado. | Compreender que a semelhança garante apenas a mesma forma (ângulos congruentes) e lados proporcionais (expandidos ou reduzidos), enquanto a congruência exige tamanhos idênticos. |
| Montar a proporção incorretamente (lados não homólogos). | O aluno cria a razão $\frac{AB}{B'C'} = \dots$ misturando lados que não correspondem ao mesmo ângulo. | Identificar primeiro os ângulos iguais. Os lados homólogos estão sempre "de frente" (opostos) para ângulos congruentes nos dois triângulos. |
| Esquecer de elevar a razão ao quadrado ao lidar com áreas. | O aluno aplica a proporção linear ($k$) para calcular a área de triângulos semelhantes, em vez de $k^2$. | Lembrar que medidas lineares (lado, altura, perímetro) usam $k$; medidas bidimensionais (área) usam a proporção $k^2$. |

## Conexões Interdisciplinares

A semelhança de triângulos é amplamente aplicada na **Geografia e Cartografia** para a construção de mapas e escalas, permitindo a transposição de distâncias reais para representações planas mantendo as proporções (formas) rigorosamente idênticas ao terreno original. Na **Física**, em Óptica Geométrica, a semelhança de triângulos é o princípio matemático utilizado para calcular o tamanho de imagens projetadas em câmaras escuras, a formação de sombras e penumbras e o estudo de lentes e espelhos. Na **Arte e Arquitetura**, o uso da perspectiva cônica, fundamental para a representação tridimensional em telas bidimensionais (técnica dominada no Renascimento), baseia-se diretamente nas propriedades de proporção e semelhança.

## Resumo para Revisão

- Dois triângulos são semelhantes se seus ângulos correspondentes são congruentes e seus lados correspondentes são proporcionais.
- Os Casos de Semelhança (AA, LAL, LLL) permitem atestar a semelhança sem precisar verificar todos os seis elementos (lados e ângulos).
- Caso AA: Se dois ângulos de um triângulo são iguais a dois ângulos de outro, eles são semelhantes.
- Teorema Fundamental: Uma reta paralela a um lado de um triângulo, que corta os outros dois, forma um novo triângulo semelhante ao original.
- Lados homólogos são lados opostos a ângulos congruentes. Eles devem ser alinhados corretamente ao montar a proporção.
- A razão das áreas de dois triângulos semelhantes é o quadrado da razão de semelhança ($k^2$).

---
## Referências
- BRASIL. Ministério da Educação. Base Nacional Comum Curricular. Brasília: MEC, 2018.
- DOLCE, Osvaldo; POMPEO, José Nicolau. Fundamentos de Matemática Elementar 9: Geometria Plana. 9. ed. São Paulo: Atual, 2013.
- IEZZI, Gelson et al. Matemática: ciência e aplicações. 9. ed. São Paulo: Saraiva, 2016.

---
> **Nota do Arquiteto:** Este e-book é 100% teórico. Os 60 exercícios correspondentes a este Objeto de Conhecimento deverão ser gerados posteriormente em um arquivo separado (`[objeto-de-conhecimento]-exercicios.md`) utilizando a skill **Exercise Creator**.
