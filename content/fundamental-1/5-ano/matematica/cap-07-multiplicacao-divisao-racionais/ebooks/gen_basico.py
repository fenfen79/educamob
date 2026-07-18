import os

path = r'c:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\content\fundamental-1\5-ano\matematica\cap-07-multiplicacao-divisao-racionais\ebooks\ef05ma08-exercicios.md'

content = """---
série: "5º Ano"
disciplina: "Matemática"
objeto_de_conhecimento: "Problemas: multiplicação e divisão de números racionais cuja representação decimal é finita por números naturais"
ebook_fonte: "ef05ma08.md"
habilidades: "EF05MA08"
total_exercicios: 60
distribuicao:
  basico: 20
  intermediario: 20
  dificil: 20
---

# Exercícios — Problemas: Multiplicação e Divisão de Números Racionais Decimais por Números Naturais

## Nível Básico (Questões 1-20)

<!-- id: q01 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 1
Efetue a multiplicação: $3 \\times 1,5$.

a) 4,5
b) 45
c) 0,45
d) 3,15
e) 1,53

**Gabarito:** A
**Resolução:** Multiplicamos ignorando a vírgula: $3 \\times 15 = 45$. Como o fator $1,5$ possui 1 casa decimal, o resultado deve ter 1 casa decimal. Logo, $4,5$. A alternativa (b) representa o erro comum de ignorar a vírgula no resultado.

<!-- id: q02 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 2
O resultado da divisão de $12,4$ por $4$ é:

a) 0,31
b) 3,1
c) 31
d) 3,01
e) 1,24

**Gabarito:** B
**Resolução:** Dividimos a parte inteira: $12 \\div 4 = 3$. Ao baixar o algarismo da parte decimal (4), inserimos a vírgula no quociente. Em seguida, $4 \\div 4 = 1$. Portanto, o resultado é $3,1$. A alternativa (a) reflete o erro comum de posicionamento incorreto da vírgula.

<!-- id: q03 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 3
Calcule: $0,25 \\times 8$.

a) 2,0
b) 20
c) 0,2
d) 0,02
e) 200

**Gabarito:** A
**Resolução:** Ignorando a vírgula: $25 \\times 8 = 200$. O fator $0,25$ tem 2 casas decimais. Deslocando a vírgula 2 casas para a esquerda no 200, obtemos $2,00$ ou $2,0$. O erro comum de ignorar a vírgula levaria à opção (b).

<!-- id: q04 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 4
Se dividirmos $1,5$ por $5$, encontraremos:

a) A divisão não é possível
b) 3
c) 0,03
d) 0,3
e) 30

**Gabarito:** D
**Resolução:** O dividendo $1,5$ tem a parte inteira 1, que é menor que 5. Portanto, o quociente inicia com $0$. Inserimos a vírgula e passamos a usar os 15 décimos. $15 \\div 5 = 3$. O resultado é $0,3$. A alternativa (a) ilustra a concepção errônea de que o dividendo deve ser maior que o divisor.

<!-- id: q05 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 5
Ao multiplicar $3,4$ por $100$, o valor obtido é:

a) 34
b) 0,034
c) 340
d) 3400
e) 3,400

**Gabarito:** C
**Resolução:** Multiplicar por 100 exige deslocar a vírgula 2 casas para a direita. Deslocando 1 casa, temos 34. A próxima ordem deve ser preenchida com um zero posicional, gerando 340. A alternativa (a) ocorre quando o aluno desloca a vírgula mas não acrescenta o zero.

<!-- id: q06 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 6
Resolva a operação: $45,2 \\div 10$.

a) 452
b) 0,452
c) 4,52
d) 4520
e) 45,20

**Gabarito:** C
**Resolução:** Dividir por 10 desloca a vírgula 1 casa decimal para a esquerda. Assim, $45,2$ torna-se $4,52$. A alternativa (a) mostra o erro de inverter o sentido (para a direita, como na multiplicação).

<!-- id: q07 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 7
Qual é o resultado de $5 \\times 2,4$?

a) 120
b) 12
c) 0,12
d) 1,2
e) 10,4

**Gabarito:** B
**Resolução:** $5 \\times 24 = 120$. Como há 1 casa decimal no número $2,4$, colocamos 1 casa decimal no resultado: $12,0$, que é $12$. A alternativa (a) reflete o erro de ignorar a vírgula.

<!-- id: q08 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 8
Calcule $5,3 \\div 2$.

a) 2,15
b) 2,6
c) 2,65
d) 26,5
e) 2,5

**Gabarito:** C
**Resolução:** $5 \\div 2 = 2$ com resto 1. Colocamos a vírgula. O resto de 1 unidade equivale a 10 décimos, que somados aos 3 décimos dão 13 décimos. $13 \\div 2 = 6$ com resto 1 décimo. Esse 1 décimo equivale a 10 centésimos, $10 \\div 2 = 5$. O quociente é $2,65$. A alternativa (b) é o erro de parar a divisão no primeiro resto.

<!-- id: q09 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 9
Efetue: $1000 \\times 0,058$.

a) 5,8
b) 0,58
c) 58
d) 580
e) 0,000058

**Gabarito:** C
**Resolução:** Multiplicar por $1000$ implica em mover a vírgula 3 posições para a direita. $0,058 \\rightarrow 0,58 \\rightarrow 5,8 \\rightarrow 58$. O resultado é $58$.

<!-- id: q10 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 10
Divida 7 por 4. O resultado exato em decimal é:

a) 1,3
b) 1,75
c) 1,5
d) 17,5
e) 0,175

**Gabarito:** B
**Resolução:** $7 \\div 4 = 1$ com resto 3. Inserimos a vírgula no quociente e acrescentamos um zero ao resto: $30 \\div 4 = 7$ com resto 2. Acrescentamos zero: $20 \\div 4 = 5$, com resto 0. O resultado é $1,75$.

<!-- id: q11 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 11
Qual é o valor de $12 \\times 0,04$?

a) 4,8
b) 0,48
c) 48
d) 0,048
e) 0,12

**Gabarito:** B
**Resolução:** Multiplica-se como naturais: $12 \\times 4 = 48$. Como há 2 casas decimais no fator $0,04$, o resultado deve ter 2 casas decimais. Contando da direita para a esquerda: $0,48$. A alternativa (c) é um erro clássico de tratar ambos como inteiros.

<!-- id: q12 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 12
Calcule o valor de $2,05 \\times 6$.

a) 12,3
b) 12,03
c) 123
d) 1,23
e) 12,30

**Gabarito:** A
**Resolução:** Ignorando a vírgula: $205 \\times 6 = 1230$. Com 2 casas decimais, temos $12,30$, que é o mesmo que $12,3$. A alternativa (b) decorre de erro na multiplicação dos zeros intermediários.

<!-- id: q13 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 13
Resolva $136,5 \\div 5$.

a) 2,73
b) 273
c) 27,3
d) 27,03
e) 0,273

**Gabarito:** C
**Resolução:** Iniciamos a divisão na parte inteira: $136 \\div 5 = 27$ (resto 1). Ao baixar o 5, passamos para a ordem dos décimos, portanto a vírgula é colocada no quociente. $15 \\div 5 = 3$. O resultado é $27,3$. A alternativa (a) reflete o erro de posicionamento antecipado da vírgula.

<!-- id: q14 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 14
O valor da operação $0,007 \\times 100$ é:

a) 0,07
b) 0,7
c) 7
d) 70
e) 700

**Gabarito:** B
**Resolução:** A multiplicação por 100 desloca a vírgula 2 posições à direita. Portanto, de $0,007$ passa para $0,07$ (uma) e $0,7$ (duas). O resultado é $0,7$. A alternativa (c) indica o deslocamento de 3 casas decimais.

<!-- id: q15 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 15
Qual das alternativas apresenta o resultado correto de $9,6 \\div 3$?

a) 32
b) 0,32
c) 3,2
d) 3,02
e) 32,0

**Gabarito:** C
**Resolução:** Dividimos a parte inteira: $9 \\div 3 = 3$. Baixamos o 6 da parte decimal e colocamos a vírgula no quociente. $6 \\div 3 = 2$. O quociente é $3,2$. A alternativa (a) representa o erro de não colocar a vírgula.

<!-- id: q16 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 16
Multiplique $15 \\times 0,2$.

a) 3
b) 30
c) 0,3
d) 300
e) 1,52

**Gabarito:** A
**Resolução:** $15 \\times 2 = 30$. Como há 1 casa decimal, posicionamos a vírgula gerando $3,0$, que equivale a 3. A alternativa (b) é o erro comum de ignorar as casas decimais.

<!-- id: q17 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 17
Calcule $4 \\div 8$. O resultado decimal é:

a) A operação não é possível
b) 0,5
c) 5
d) 0,05
e) 2

**Gabarito:** B
**Resolução:** $4 \\div 8$ tem quociente inteiro 0. Coloca-se a vírgula e acrescenta-se um zero: $40 \\div 8 = 5$. Resultado $0,5$. A alternativa (a) seria marcada pelo aluno que acredita que um dividendo menor que o divisor inviabiliza a conta.

<!-- id: q18 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 18
Qual é o resultado de $24 \\times 0,125$?

a) 30
b) 0,3
c) 3
d) 300
e) 3,125

**Gabarito:** C
**Resolução:** $24 \\times 125 = 3000$. Com 3 casas decimais no fator, aplicamos ao produto: $3,000 = 3$. A alternativa (a) resulta de contar apenas 2 casas decimais.

<!-- id: q19 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 19
Divida $61,5$ por $5$.

a) 1,23
b) 12,3
c) 123
d) 12,03
e) 1,3

**Gabarito:** B
**Resolução:** $61 \\div 5 = 12$ (resto 1). Atingiu-se a vírgula. Baixa o 5, ficando 15 décimos. $15 \\div 5 = 3$. Resultado: $12,3$. A alternativa (a) exibe um posicionamento antecipado da vírgula.

<!-- id: q20 | tipo: multipla-escolha | habilidade: EF05MA08 | dificuldade: basico | objeto: multiplicacao-divisao-racionais-decimais-naturais -->
### Questão 20
Efetue a operação: $0,09 \\times 10000$.

a) 9
b) 90
c) 900
d) 9000
e) 0,000009

**Gabarito:** C
**Resolução:** Multiplicar por $10000$ é deslocar a vírgula 4 posições à direita. O número $0,09$ passa para $0,9$ (1), $9$ (2), $90$ (3) e $900$ (4). O erro (b) decorre da falta de um zero de preenchimento posicional.

"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
