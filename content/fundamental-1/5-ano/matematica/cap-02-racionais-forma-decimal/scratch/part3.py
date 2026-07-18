def get_q_dificeis():
    return [
        {
            "id": "q41", "dificuldade": "dificil",
            "enunciado": "A propriedade da densidade dos racionais garante que entre dois números sempre há outros racionais. Qual dos seguintes números se encontra estritamente entre $5,7$ e $5,8$?",
            "alternativas": [
                "a) $5,65$",
                "b) $5,75$",
                "c) $5,85$",
                "d) $5,07$",
                "e) $5,08$"
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Equalizar as casas decimais para centésimos: $5,7 = 5,70$ e $5,8 = 5,80$.\n**Etapa 2:** Avaliar os números cujos centésimos estão entre 70 e 80.\n**Etapa 3:** A alternativa A ($5,65$) é menor que $5,70$. A alternativa B ($5,75$) atende à condição ($5,70 < 5,75 < 5,80$). A C ($5,85$) é maior. As D e E são menores."
        },
        {
            "id": "q42", "dificuldade": "dificil",
            "enunciado": "Durante uma aula de Geografia, as coordenadas de GPS de quatro marcadores foram registradas com as seguintes latitudes ao sul: Ponto A ($23,5505$), Ponto B ($23,55$), Ponto C ($23,551$) e Ponto D ($23,505$). Qual é a ordem crescente dessas medidas, ignorando o sinal negativo para a comparação numérica direta?",
            "alternativas": [
                "a) D < B < A < C",
                "b) B < D < C < A",
                "c) C < A < B < D",
                "d) D < A < B < C",
                "e) B < A < C < D"
            ],
            "gabarito": "A",
            "resolucao": "**Etapa 1:** Identificar o número máximo de casas decimais (4 casas).\n**Etapa 2:** Equalizar todos: A ($23,5505$), B ($23,5500$), C ($23,5510$), D ($23,5050$).\n**Etapa 3:** Comparar a parte decimal (milésimos e décimos de milésimos): $5050 < 5500 < 5505 < 5510$.\n**Etapa 4:** Concluir a ordem original: D ($23,505$) < B ($23,55$) < A ($23,5505$) < C ($23,551$)."
        },
        {
            "id": "q43", "dificuldade": "dificil",
            "enunciado": "Um aluno afirmou que o número $2,5$ deve ser lido como 'dois inteiros e cinco centésimos'. Qual é o número decimal que realmente corresponde à leitura 'dois inteiros e cinco centésimos', e como podemos comprovar o erro do aluno usando frações?",
            "alternativas": [
                "a) $2,05$. O erro ocorreu porque $2,5 = 2 + \\frac{5}{10}$ (cinco décimos), enquanto cinco centésimos exigem o algarismo $5$ na segunda casa decimal ($2 + \\frac{5}{100}$).",
                "b) $2,50$. O erro ocorreu porque faltava o zero à direita para transformar em centésimos.",
                "c) $0,25$. O erro ocorreu porque a parte inteira de centésimos deve ser zero.",
                "d) $2,005$. O erro ocorreu porque cinco centésimos possuem três casas decimais.",
                "e) $20,5$. O erro ocorreu porque ele esqueceu de multiplicar por 100."
            ],
            "gabarito": "A",
            "resolucao": "**Etapa 1:** Analisar a leitura do aluno: $2,5$ possui o algarismo 5 na primeira casa (décimos), logo a leitura dele está incorreta, o certo seria 'dois inteiros e cinco décimos'.\n**Etapa 2:** Traduzir a leitura proposta: 'dois inteiros e cinco centésimos'. A casa dos centésimos é a segunda após a vírgula. A casa dos décimos deve ser zero.\n**Etapa 3:** Montar o número: $2,05$, que corresponde a $2 + \\frac{5}{100}$."
        },
        {
            "id": "q44", "dificuldade": "dificil",
            "enunciado": "Ao realizarmos o 'zoom' na reta numérica entre os números $2,35$ e $2,36$, dividimos esse espaço em $10$ partes iguais. Qual valor corresponde à $4ª$ marcação após o número $2,35$?",
            "alternativas": [
                "a) $2,354$",
                "b) $2,39$",
                "c) $2,75$",
                "d) $2,3504$",
                "e) $2,4$"
            ],
            "gabarito": "A",
            "resolucao": "**Etapa 1:** Compreender a escala. O intervalo original é de centésimos ($2,35$ a $2,36$).\n**Etapa 2:** Dividir o intervalo de centésimos em 10 cria a escala de milésimos. Assim, $2,35$ é $2,350$ e $2,36$ é $2,360$.\n**Etapa 3:** Contar 4 subdivisões de milésimo a partir de $2,350$. Cada passo soma $0,001$.\n**Etapa 4:** Chega-se exatamente no ponto $2,354$."
        },
        {
            "id": "q45", "dificuldade": "dificil",
            "enunciado": "Qual dos conjuntos a seguir ordena corretamente, de forma crescente, a fração $\\frac{3}{4}$, e os decimais $0,7$ e $0,705$?",
            "alternativas": [
                "a) $0,7 < \\frac{3}{4} < 0,705$",
                "b) $0,7 < 0,705 < \\frac{3}{4}$",
                "c) $\\frac{3}{4} < 0,7 < 0,705$",
                "d) $0,705 < 0,7 < \\frac{3}{4}$",
                "e) $0,705 < \\frac{3}{4} < 0,7$"
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Transformar a fração em decimal para padronizar a comparação. $\\frac{3}{4}$ equivale a multiplicar por 25: $\\frac{75}{100} = 0,75$.\n**Etapa 2:** Equalizar todos os números decimais obtidos para a mesma quantidade de casas (três): $0,7$ vira $0,700$; $0,705$ já tem três; e $0,75$ vira $0,750$.\n**Etapa 3:** Ordenar os milésimos inteiros: $700 < 705 < 750$.\n**Etapa 4:** Relacionar aos originais: $0,7 < 0,705 < \\frac{3}{4}$."
        },
        {
            "id": "q46", "dificuldade": "dificil",
            "enunciado": "João realizou a seguinte decomposição: $50 + 4 + \\frac{0}{10} + \\frac{3}{100} + \\frac{8}{1000}$. Qual é o número decimal correspondente, e qual seria o erro mais comum cometido ao tentar escrevê-lo sem atenção à casa dos décimos?",
            "alternativas": [
                "a) $54,38$; Erro comum seria ignorar o zero e escrever $54,038$.",
                "b) $54,038$; Erro comum seria ignorar o zero posicional dos décimos e escrever $54,38$.",
                "c) $54,308$; Erro comum seria escrever os milésimos primeiro.",
                "d) $50,438$; Erro comum seria somar o $50$ com o $4$ incorretamente.",
                "e) $540,38$; Erro comum seria não saber usar a vírgula."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Montar a parte inteira: $50 + 4 = 54$.\n**Etapa 2:** Montar a parte decimal: $0$ nos décimos, $3$ nos centésimos e $8$ nos milésimos, formando $0,038$.\n**Etapa 3:** Juntar as partes: $54,038$.\n**Etapa 4:** Analisar o erro. O desvio cognitivo mais frequente, chamado 'Ignorar o zero intermediário', levaria o estudante a ler apenas os não nulos (3 e 8) e uni-los diretamente após a vírgula, resultando em $54,38$, o que alteraria a grandeza do número."
        },
        {
            "id": "q47", "dificuldade": "dificil",
            "enunciado": "Em uma competição de salto em distância, as marcas de três atletas foram: Marcos: $8,2 m$, Pedro: $8,205 m$, e Carlos: $8,025 m$. A classificação do 1º, 2º e 3º lugar, respectivamente (do maior para o menor salto), é:",
            "alternativas": [
                "a) Marcos, Pedro, Carlos.",
                "b) Pedro, Marcos, Carlos.",
                "c) Carlos, Pedro, Marcos.",
                "d) Pedro, Carlos, Marcos.",
                "e) Marcos, Carlos, Pedro."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Equalizar as marcações em milésimos para comparação justa: Marcos = $8,200 m$; Pedro = $8,205 m$; Carlos = $8,025 m$.\n**Etapa 2:** Ordenar de forma decrescente os valores decimais ignorando a parte inteira que é igual (8): $205$ (Pedro) $> 200$ (Marcos) $> 025$ (Carlos).\n**Etapa 3:** Estabelecer o pódio: 1º Pedro, 2º Marcos, 3º Carlos."
        },
        {
            "id": "q48", "dificuldade": "dificil",
            "enunciado": "Considere o intervalo entre $0,45$ e $0,46$. Se aplicarmos o conceito de densidade fracionando esse espaço, qual das alternativas apresenta uma lista de três números ordenados que cabem estritamente dentro desse intervalo?",
            "alternativas": [
                "a) $0,451 ; 0,455 ; 0,461$",
                "b) $0,449 ; 0,450 ; 0,451$",
                "c) $0,452 ; 0,456 ; 0,459$",
                "d) $0,450 ; 0,455 ; 0,460$",
                "e) $0,405 ; 0,406 ; 0,407$"
            ],
            "gabarito": "C",
            "resolucao": "**Etapa 1:** Equalizar os limites do intervalo original ($0,45$ e $0,46$) para três casas decimais (milésimos), resultando em $0,450$ e $0,460$.\n**Etapa 2:** Procurar números que estejam estritamente entre $450$ e $460$ (excluindo as extremidades).\n**Etapa 3:** Analisar a alternativa C: $0,452$, $0,456$ e $0,459$ atendem, pois $450 < 452 < 456 < 459 < 460$. A alternativa A ultrapassa no $0,461$. A alternativa B falha no $0,449$. A D inclui as pontas. A E está na grandeza errada."
        },
        {
            "id": "q49", "dificuldade": "dificil",
            "enunciado": "Um laboratório de química usa uma balança de precisão que mede até a ordem dos milésimos de grama. Três amostras foram pesadas: Amostra 1 ($1,003 g$), Amostra 2 ($1,03 g$) e Amostra 3 ($1,030 g$). Pode-se afirmar corretamente que:",
            "alternativas": [
                "a) A Amostra 1 é a mais pesada de todas.",
                "b) As Amostras 2 e 3 possuem exatamente a mesma massa, que é maior que a da Amostra 1.",
                "c) A Amostra 2 é menor que a Amostra 3 por não ter o algarismo zero no final.",
                "d) Todas as três amostras têm massas completamente diferentes e distintas.",
                "e) A Amostra 3 é a mais pesada, seguida pela Amostra 1 e, por fim, a Amostra 2."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Avaliar equivalência entre $1,03$ e $1,030$. Sabemos que um zero adicionado à direita na parte decimal não altera o valor numérico. Logo, $1,03 = 1,030$. As amostras 2 e 3 têm a mesma massa.\n**Etapa 2:** Comparar $1,030$ com $1,003$. Ambos têm 3 casas. Comparamos $030$ com $003$. Como $30 > 3$, a Amostra 2 (e a 3) são mais pesadas que a Amostra 1."
        },
        {
            "id": "q50", "dificuldade": "dificil",
            "enunciado": "Na reta numérica, o espaço entre $7,1$ e $7,2$ foi dividido em $100$ partes iguais (sub-subdivisões), atingindo a escala de milésimos. Qual a localização exata de um ponto situado $35$ marcações à direita do $7,1$?",
            "alternativas": [
                "a) $7,135$",
                "b) $7,45$",
                "c) $7,035$",
                "d) $7,10035$",
                "e) $7,235$"
            ],
            "gabarito": "A",
            "resolucao": "**Etapa 1:** O intervalo inicial é entre décimos ($7,1$ e $7,2$). Ao dividi-lo em 10 partes, obteríamos centésimos. Ao dividi-lo em 100 partes, chegamos a passos de milésimos ($0,001$).\n**Etapa 2:** O marco de partida é o $7,1$, que equalizado em milésimos é $7,100$.\n**Etapa 3:** Mover 35 marcações de milésimos ($0,035$) à direita é equivalente a somar essa grandeza: $7,100 + 0,035 = 7,135$."
        },
        {
            "id": "q51", "dificuldade": "dificil",
            "enunciado": "Um estudante comparou o número decimal $0,05$ com a fração $\\frac{1}{20}$. Ao representar a fração em decimal e realizar a comparação, a conclusão matematicamente exata foi que:",
            "alternativas": [
                "a) $0,05$ é muito menor, pois $\\frac{1}{20}$ equivale a $0,20$.",
                "b) $0,05$ é maior, pois a fração vale $0,02$.",
                "c) Ambos são perfeitamente equivalentes.",
                "d) $0,05$ e $\\frac{1}{20}$ não podem ser comparados pois pertencem a conjuntos matemáticos distintos.",
                "e) O aluno deve simplificar $0,05$ para $0,5$ antes de comparar."
            ],
            "gabarito": "C",
            "resolucao": "**Etapa 1:** Para comparar, devemos transformar a fração $\\frac{1}{20}$ para a base 100.\n**Etapa 2:** Multiplicamos o numerador e o denominador por 5, obtendo $\\frac{5}{100}$.\n**Etapa 3:** A fração $\\frac{5}{100}$ lê-se como 'cinco centésimos'.\n**Etapa 4:** O número decimal correspondente a cinco centésimos é $0,05$. Logo, as expressões são equivalentes."
        },
        {
            "id": "q52", "dificuldade": "dificil",
            "enunciado": "Sabendo que o número $4,07$ significa quatro inteiros e sete centésimos, analise a seguinte fala de um aluno virtual: 'Como sete centésimos é o mesmo que setenta milésimos, eu posso escrever esse número como $4,070$ ou até mesmo $4 + \\frac{70}{1000}$ e o valor não muda'. O aluno está:",
            "alternativas": [
                "a) Incorreto, pois a adição de um zero altera permanentemente o valor do número decimal.",
                "b) Correto, porque a relação de equivalência permite que $\\frac{7}{100}$ se transforme em $\\frac{70}{1000}$ ao multiplicarmos ambos por 10.",
                "c) Incorreto, pois a parte inteira deveria ter sido multiplicada por 10 também, resultando em $40,070$.",
                "d) Correto, mas apenas na escrita decimal, não sendo válido para a forma fracionária.",
                "e) Incorreto, porque os milésimos devem ter pelo menos dois zeros após a vírgula."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Avaliar a equivalência decimal citada. $4,07$ é igual a $4,070$. Ao acrescentar o zero à direita, o valor numérico é mantido.\n**Etapa 2:** Avaliar a equivalência fracionária citada. O aluno trocou $\\frac{7}{100}$ por $\\frac{70}{1000}$. Multiplicando numerador e denominador da primeira por 10, obtém-se a segunda. A igualdade matemática de ambas se sustenta perfeitamente.\n**Etapa 3:** Portanto, o raciocínio está integralmente correto em ambas as representações."
        },
        {
            "id": "q53", "dificuldade": "dificil",
            "enunciado": "Se a média aritmética entre dois números também é um número racional estritamente localizado entre eles, qual é a média decimal entre $8,4$ e $8,5$, e o que isso demonstra sobre a estrutura da reta numérica?",
            "alternativas": [
                "a) A média é $8,45$, demonstrando que a reta numérica é discreta.",
                "b) A média é $8,45$, demonstrando o conceito de densidade dos números racionais.",
                "c) A média é $8,50$, provando que não há números entre eles.",
                "d) A média é $8,41$, ilustrando o uso exclusivo de décimos.",
                "e) A média é $16,9$, evidenciando a soma de racionais."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Encontrar a média entre os valores: $\\frac{8,4 + 8,5}{2}$. Transformando em dinheiro/centésimos para facilitar: metade de R$ 16,90 é R$ 8,45.\n**Etapa 2:** Compreender o significado estrutural. O fato de sempre conseguirmos encontrar um número dividindo o intervalo ao meio demonstra a propriedade da 'Densidade' no conjunto dos racionais, o que contrasta com a natureza discreta dos inteiros."
        },
        {
            "id": "q54", "dificuldade": "dificil",
            "enunciado": "Observe o número decimal formado por 'dez inteiros, três décimos e nove milésimos'. Onde está o possível erro se um estudante registrar $10,39$?",
            "alternativas": [
                "a) O erro não existe, o registro está perfeitamente alinhado com a leitura.",
                "b) Ele omitiu o zero na casa dos décimos; o correto seria $10,039$.",
                "c) Ele alocou o $9$ na casa dos centésimos, ignorando o zero posicional que deveria ocupar a segunda ordem decimal; o correto seria $10,309$.",
                "d) Ele alocou o $3$ na casa dos centésimos; o correto seria $10,0039$.",
                "e) Ele esqueceu de multiplicar $10$ por $1000$."
            ],
            "gabarito": "C",
            "resolucao": "**Etapa 1:** Decompor a descrição: 10 unidades (parte inteira), 3 décimos (primeira casa) e 9 milésimos (terceira casa).\n**Etapa 2:** Avaliar as lacunas. A casa dos centésimos (segunda casa) não foi citada, logo, deve ser preenchida com um zero (marcador posicional).\n**Etapa 3:** Compor o número final e analisar o erro: O número correto é $10,309$. Ao escrever $10,39$, o aluno empurrou o 9 para os centésimos, alterando seu valor de 'nove milésimos' para 'noventa milésimos'."
        },
        {
            "id": "q55", "dificuldade": "dificil",
            "enunciado": "Dada a sequência decrescente: $X > 1,02 > 1,009 > Y$. Quais poderiam ser os valores corretos para ocupar os lugares de X e Y, respectivamente?",
            "alternativas": [
                "a) $1,1$ e $1,01$",
                "b) $1,2$ e $1,005$",
                "c) $1,01$ e $1,001$",
                "d) $1,03$ e $1,01$",
                "e) $1,005$ e $1,0$"
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Analisar o pré-requisito para X. Ele deve ser maior que $1,02$ ($1,020$). Nas alternativas: a) $1,1$ ($1,100$) serve; b) $1,2$ ($1,200$) serve; c) $1,01$ ($1,010$) não serve; d) $1,03$ ($1,030$) serve; e) $1,005$ não serve.\n**Etapa 2:** Analisar o pré-requisito para Y. Ele deve ser menor que $1,009$. Entre as alternativas válidas (a, b, d): a) Y=$1,01$ ($1,010 > 1,009$) não serve. b) Y=$1,005$ ($1,005 < 1,009$) serve. d) Y=$1,01$ não serve.\n**Etapa 3:** A única alternativa que fornece um par válido é a B ($1,2$ e $1,005$)."
        },
        {
            "id": "q56", "dificuldade": "dificil",
            "enunciado": "Para converter $0,004$ numa fração ordinária irredutível, os passos e o resultado final correto são:",
            "alternativas": [
                "a) O número tem 3 casas decimais, logo o denominador é 1000. Fica $\\frac{4}{1000}$. Simplificando por 4, temos $\\frac{1}{250}$.",
                "b) O número tem 3 casas, logo o denominador é 100. Fica $\\frac{4}{100}$. Simplificando por 4, temos $\\frac{1}{25}$.",
                "c) O número tem 4, logo o denominador é 400. Fica $\\frac{4}{400}$. Simplificando, $\\frac{1}{100}$.",
                "d) Fica $\\frac{4}{10}$, que se simplifica para $\\frac{2}{5}$.",
                "e) Apenas $\\frac{4}{1000}$, pois frações decimais não devem ser simplificadas em hipótese alguma."
            ],
            "gabarito": "A",
            "resolucao": "**Etapa 1:** Identificar a casa decimal limite. O algarismo 4 está na terceira posição após a vírgula (milésimos).\n**Etapa 2:** Escrever como fração decimal bruta: $\\frac{4}{1000}$.\n**Etapa 3:** Dividir numerador e denominador pelo máximo divisor comum, que é 4. O numerador torna-se $4 \\div 4 = 1$ e o denominador $1000 \\div 4 = 250$. O resultado irredutível é $\\frac{1}{250}$."
        },
        {
            "id": "q57", "dificuldade": "dificil",
            "enunciado": "Num projeto de biologia, o comprimento de um inseto foi registrado como $3,045 cm$. Um colega digitou erroneamente o valor no relatório lendo-o como 'três inteiros e quarenta e cinco centésimos'. Qual foi o número que ele efetivamente digitou no relatório e qual a diferença matemática em módulo entre os dois números?",
            "alternativas": [
                "a) Ele digitou $3,45$, o que gerou uma diferença de $0,405 cm$.",
                "b) Ele digitou $3,450$, o que gerou uma diferença de $0,005 cm$.",
                "c) Ele digitou $3,045$, sem cometer erros numéricos.",
                "d) Ele digitou $3,0045$, causando uma diferença de $0,0405 cm$.",
                "e) Ele digitou $3,405$, causando uma diferença de $0,36 cm$."
            ],
            "gabarito": "A",
            "resolucao": "**Etapa 1:** Analisar o número falado: 'três inteiros e quarenta e cinco centésimos' possui o último algarismo na segunda casa decimal. Logo, o número digitado foi $3,45$.\n**Etapa 2:** Comparar os valores. O correto era $3,045$ e o digitado foi $3,45$ ($3,450$). O número digitado é maior.\n**Etapa 3:** Subtrair para achar o erro (módulo): $3,450 - 3,045$. A diferença é exata e corresponde a $0,405 cm$."
        },
        {
            "id": "q58", "dificuldade": "dificil",
            "enunciado": "Em 1585, Simon Stevin sugeriu um modelo que eliminava os denominadores fracionários. Se fôssemos representar o número 'dois inteiros, sete décimos e três milésimos' usando o modelo polinomial atual estrito e a notação decimal posicional separada por vírgula, teríamos:",
            "alternativas": [
                "a) $2 + \\frac{7}{10} + \\frac{3}{1000}$, resultando em $2,73$.",
                "b) $2 + \\frac{7}{10} + \\frac{0}{100} + \\frac{3}{1000}$, resultando em $2,703$.",
                "c) $2 + \\frac{73}{100}$, resultando em $2,73$.",
                "d) $20 + 7 + 3$, resultando em $30$.",
                "e) $2 + \\frac{7}{100} + \\frac{3}{1000}$, resultando em $2,073$."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Montar as frações referidas: 2 inteiros ($2$), 7 décimos ($7/10$) e 3 milésimos ($3/1000$).\n**Etapa 2:** Perceber a ausência dos centésimos, cujo termo é $0/100$.\n**Etapa 3:** Juntar a notação polinomial, garantindo a posição vazia por um zero. A parte decimal fica com 7 na primeira casa, 0 na segunda e 3 na terceira, formando o decimal $2,703$."
        },
        {
            "id": "q59", "dificuldade": "dificil",
            "enunciado": "Em muitos países de língua inglesa, utiliza-se o ponto no lugar da vírgula. Considerando isso e a leitura internacional, como se traduz conceitualmente e se converte para fração o número escrito nos EUA como '0.012'?",
            "alternativas": [
                "a) Doze centésimos, escrito como $\\frac{12}{100}$.",
                "b) Doze décimos, escrito como $\\frac{12}{10}$.",
                "c) Doze milésimos, escrito como $\\frac{12}{1000}$.",
                "d) Cento e vinte milésimos, escrito como $\\frac{120}{1000}$.",
                "e) Zero e doze unidades, escrito como $\\frac{12}{1}$."
            ],
            "gabarito": "C",
            "resolucao": "**Etapa 1:** O '0.012' utiliza o ponto decimal que funciona da mesma maneira que a nossa vírgula. O número é equivalente a $0,012$.\n**Etapa 2:** O número $0,012$ possui a parte significativa '12' e atinge três casas decimais (milésimos).\n**Etapa 3:** Lê-se 'doze milésimos' e a correspondência em fração ordinária direta é $\\frac{12}{1000}$."
        },
        {
            "id": "q60", "dificuldade": "dificil",
            "enunciado": "Um professor propôs o desafio: 'Encontre a posição do número que é a soma entre três décimos e doze centésimos na reta numérica'. Onde exatamente ele se localiza e qual é o seu valor?",
            "alternativas": [
                "a) Valor $0,15$, situado exatamente no meio entre $0,1$ e $0,2$.",
                "b) Valor $0,42$, situado entre $0,4$ e $0,5$, sendo duas marcas de centésimos após o $0,4$.",
                "c) Valor $3,12$, situado após o inteiro $3$.",
                "d) Valor $0,312$, situado entre $0,3$ e $0,4$.",
                "e) Valor $0,42$, situado entre $4$ e $5$."
            ],
            "gabarito": "B",
            "resolucao": "**Etapa 1:** Converter os dados verbais para decimais ou frações numéricas: Três décimos é igual a $0,3$. Doze centésimos é igual a $0,12$.\n**Etapa 2:** Somar respeitando as ordens posicionais: $0,30 + 0,12 = 0,42$.\n**Etapa 3:** Localizar na reta. O número $0,42$ é maior que $0,40$ ($0,4$) e menor que $0,50$ ($0,5$). Na escala, ele recai perfeitamente na segunda subdivisão (centésimos) após passar da quarta divisão principal (décimos), marcando a posição correta."
        }
    ]
