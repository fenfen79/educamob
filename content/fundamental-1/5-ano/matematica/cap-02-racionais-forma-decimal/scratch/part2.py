def get_q_intermediarias():
    return [
        {
            "id": "q21", "dificuldade": "intermediario",
            "enunciado": "Ao comparar os números $0,47$ e $0,8$, um estudante afirmou que o primeiro é maior porque $47$ é maior que $8$. Qual a correção correta para esse erro?",
            "alternativas": [
                "a) O estudante está correto, $0,47$ é maior pois tem mais algarismos.",
                "b) O estudante errou, pois a parte inteira de $0,8$ é 8 e a de $0,47$ é 0.",
                "c) O estudante errou, pois deve-se igualar as casas decimais: $0,8$ é igual a $0,80$. Como $80 > 47$, logo $0,8 > 0,47$.",
                "d) O estudante errou porque $0,47$ é número par e $0,8$ é ímpar.",
                "e) O estudante está correto, pois na reta numérica o $47$ vem depois do $8$."
            ],
            "gabarito": "C",
            "resolucao": "Para comparar decimais com precisão, deve-se equalizar a quantidade de casas decimais. O número 0,8 equivale a 0,80 (oitenta centésimos), o que o torna visualmente comparável com 0,47 (quarenta e sete centésimos). Logo, 0,80 é maior."
        },
        {
            "id": "q22", "dificuldade": "intermediario",
            "enunciado": "Organize os números a seguir em ordem decrescente (do maior para o menor): $3,4$ ; $3,41$ ; $3,04$ ; $3,401$.",
            "alternativas": [
                "a) $3,04$ > $3,4$ > $3,401$ > $3,41$",
                "b) $3,41$ > $3,401$ > $3,4$ > $3,04$",
                "c) $3,401$ > $3,41$ > $3,4$ > $3,04$",
                "d) $3,41$ > $3,4$ > $3,401$ > $3,04$",
                "e) $3,04$ > $3,401$ > $3,41$ > $3,4$"
            ],
            "gabarito": "B",
            "resolucao": "Igualando as casas decimais para 3 casas (milésimos), temos: 3,400 ; 3,410 ; 3,040 ; 3,401. Comparando a parte decimal: 410 > 401 > 400 > 040. Assim, a ordem original é: 3,41 > 3,401 > 3,4 > 3,04."
        },
        {
            "id": "q23", "dificuldade": "intermediario",
            "enunciado": "O valor monetário de $R\\$ 2,50$ escrito sem o zero à direita é $2,5$. Como devemos interpretar matematicamente a leitura dessa quantidade no contexto do dinheiro?",
            "alternativas": [
                "a) Dois reais e cinco centavos.",
                "b) Dois reais e cinco décimos de centavo.",
                "c) Dois reais e cinquenta centavos, pois 5 décimos de real equivalem a 50 centésimos.",
                "d) Vinte e cinco reais.",
                "e) Vinte e cinco centavos."
            ],
            "gabarito": "C",
            "resolucao": "No sistema monetário, os centavos são a ordem dos centésimos. A forma 2,5 (2 inteiros e 5 décimos) é equivalente a 2,50 (2 inteiros e 50 centésimos). Logo, são dois reais e cinquenta centavos."
        },
        {
            "id": "q24", "dificuldade": "intermediario",
            "enunciado": "A balança da cozinha de Maria marca $1,200$ kg. Ela precisa de $1,2$ kg para uma receita. O que ela deve fazer?",
            "alternativas": [
                "a) Tirar ingredientes, pois ela tem muito mais que $1,2$ kg.",
                "b) Adicionar ingredientes, pois ela tem menos do que $1,2$ kg.",
                "c) Nada, pois as massas de $1,200$ kg e $1,2$ kg são exatamente iguais.",
                "d) Multiplicar os ingredientes por 10.",
                "e) Substituir a balança, pois ela está com defeito."
            ],
            "gabarito": "C",
            "resolucao": "O acréscimo de zeros à direita de um número decimal não altera o seu valor numérico. Portanto, 1,2 kg e 1,200 kg representam rigorosamente a mesma quantidade de massa."
        },
        {
            "id": "q25", "dificuldade": "intermediario",
            "enunciado": "A fração ordinária $\\frac{1}{4}$ pode ser transformada em número decimal encontrando uma fração equivalente com denominador 100. Qual é esse número decimal?",
            "alternativas": [
                "a) $0,14$",
                "b) $1,4$",
                "c) $0,25$",
                "d) $0,04$",
                "e) $0,4$"
            ],
            "gabarito": "C",
            "resolucao": "Multiplicando o numerador e o denominador da fração por 25, temos $(1 \\times 25) / (4 \\times 25) = 25/100$. Lida como vinte e cinco centésimos, sua forma decimal é 0,25."
        },
        {
            "id": "q26", "dificuldade": "intermediario",
            "enunciado": "Em uma corrida de 100 metros, o Atleta A terminou com o tempo de $9,58$ segundos e o Atleta B terminou com $9,6$ segundos. Quem foi o mais rápido e por quê?",
            "alternativas": [
                "a) O Atleta B foi mais rápido porque $6$ é menor que $58$.",
                "b) O Atleta A foi mais rápido porque $9,58$ é menor que $9,60$.",
                "c) Empataram, pois as partes inteiras são ambas $9$.",
                "d) O Atleta A foi mais rápido porque tem mais números no relógio.",
                "e) O Atleta B foi mais rápido porque $9,6$ tem menos casas decimais."
            ],
            "gabarito": "B",
            "resolucao": "O vencedor (mais rápido) é o que faz a corrida em menos tempo. Ao igualar as casas decimais de 9,6, obtemos 9,60. Comparando casa a casa, nos décimos temos 5 < 6. Logo, 9,58 s < 9,60 s, ou seja, o Atleta A completou em menos tempo."
        },
        {
            "id": "q27", "dificuldade": "intermediario",
            "enunciado": "Determine qual das alternativas apresenta uma relação verdadeira de desigualdade matemática.",
            "alternativas": [
                "a) $0,125 > 0,2$",
                "b) $1,500 < 1,5$",
                "c) $2,99 < 2,909$",
                "d) $7,4 > 7,395$",
                "e) $0,08 > 0,1$"
            ],
            "gabarito": "D",
            "resolucao": "Igualando as casas de 7,4 (3 casas decimais), temos 7,400. Comparando: 7,400 > 7,395, o que é verdadeiro. A alternativa A está errada porque 0,125 < 0,200. A B é igual. A C é 2,990 > 2,909. A E é 0,08 < 0,10."
        },
        {
            "id": "q28", "dificuldade": "intermediario",
            "enunciado": "O número $1,45$ está localizado exatamente no meio geométrico de quais números em uma reta numérica graduada em décimos?",
            "alternativas": [
                "a) $1,0$ e $1,5$",
                "b) $1,4$ e $1,5$",
                "c) $1,4$ e $1,6$",
                "d) $1,44$ e $1,46$",
                "e) $1,0$ e $2,0$"
            ],
            "gabarito": "B",
            "resolucao": "O número 1,45 possui parte inteira e casa dos décimos iguais a 1,4, com os 5 centésimos adicionados indicando que ele avançou metade do caminho em direção ao próximo décimo, que é o 1,5."
        },
        {
            "id": "q29", "dificuldade": "intermediario",
            "enunciado": "O aluno Carlos acredita que $7,30$ é maior que $7,3$, justificando que 'ter mais números escritos significa ser maior'. Qual alternativa melhor desconstrói esse raciocínio?",
            "alternativas": [
                "a) Afirmar que só importa a quantidade de dezenas e centenas.",
                "b) Mostrar que $7,3 = 7 + \\frac{3}{10}$ e $7,30 = 7 + \\frac{30}{100}$. Simplificando $\\frac{30}{100}$ (dividindo por 10), obtemos $\\frac{3}{10}$, provando que são iguais.",
                "c) Mostrar que todo número que termina em zero é obrigatoriamente menor.",
                "d) Explicar que a vírgula anula o valor do zero.",
                "e) Ele está correto; não há erro no seu raciocínio."
            ],
            "gabarito": "B",
            "resolucao": "A melhor desconstrução pedagógica da 'ilusão do comprimento' é recorrer às frações equivalentes. Dividir o numerador e o denominador de 30/100 por 10 mostra concretamente que a quantidade representada é a mesma (3/10)."
        },
        {
            "id": "q30", "dificuldade": "intermediario",
            "enunciado": "Se você precisa escrever a quantia monetária de 'quatro reais e cinco centavos', qual das anotações está absolutamente correta?",
            "alternativas": [
                "a) $4,5$",
                "b) $4,50$",
                "c) $4,05$",
                "d) $4,005$",
                "e) $0,45$"
            ],
            "gabarito": "C",
            "resolucao": "O real é o inteiro, e o centavo é o centésimo. Portanto, cinco centavos devem ocupar a segunda casa decimal, ficando a primeira casa (décimos) preenchida com zero: R$ 4,05."
        },
        {
            "id": "q31", "dificuldade": "intermediario",
            "enunciado": "Um estudante olhou para a reta numérica, observou o ponto exatamente na metade entre $0,6$ e $0,7$ e precisava registrar que valor era esse. O registro correto é:",
            "alternativas": [
                "a) $0,65$",
                "b) $0,605$",
                "c) $0,75$",
                "d) $0,61$",
                "e) $1,3$"
            ],
            "gabarito": "A",
            "resolucao": "Adicionando zeros para enxergar em centésimos, o intervalo é entre 0,60 e 0,70. O valor no meio exato entre 60 e 70 é 65. Logo, o número no ponto médio é 0,65."
        },
        {
            "id": "q32", "dificuldade": "intermediario",
            "enunciado": "Lendo o número $3,05$, podemos afirmar que a leitura correta e o algarismo na casa dos centésimos são, respectivamente:",
            "alternativas": [
                "a) Três inteiros e cinco décimos; algarismo 5.",
                "b) Três inteiros e cinco centésimos; algarismo 5.",
                "c) Três inteiros e cinco décimos; algarismo 0.",
                "d) Trinta e cinco centésimos; algarismo 3.",
                "e) Três inteiros e cinquenta milésimos; algarismo 0."
            ],
            "gabarito": "B",
            "resolucao": "A leitura é 'três inteiros e cinco centésimos'. O algarismo 5 ocupa a segunda casa após a vírgula, que é exatamente a ordem dos centésimos."
        },
        {
            "id": "q33", "dificuldade": "intermediario",
            "enunciado": "Ao decompor o número $23,456$, a expressão polinomial equivalente é:",
            "alternativas": [
                "a) $20 + 3 + 0,4 + 0,5 + 0,6$",
                "b) $20 + 3 + 4 + 5 + 6$",
                "c) $20 + 3 + 0,4 + 0,05 + 0,006$",
                "d) $20 + 3 + \\frac{456}{10}$",
                "e) $20 + 3 + \\frac{4}{100} + \\frac{56}{1000}$"
            ],
            "gabarito": "C",
            "resolucao": "Na parte decimal, o 4 é o décimo (0,4), o 5 é o centésimo (0,05) e o 6 é o milésimo (0,006). Somando às dezenas e unidades ($20 + 3$), temos $20 + 3 + 0,4 + 0,05 + 0,006$."
        },
        {
            "id": "q34", "dificuldade": "intermediario",
            "enunciado": "Para uma receita, foi solicitada a adição de $0,75$ litro de leite. Essa quantidade equivale a:",
            "alternativas": [
                "a) Sete litros e cinco décimos.",
                "b) Setenta e cinco décimos de litro.",
                "c) Setenta e cinco milésimos de litro.",
                "d) Setenta e cinco centésimos de litro.",
                "e) Sete inteiros e cinco centésimos de litro."
            ],
            "gabarito": "D",
            "resolucao": "Como a parte inteira é zero e o último algarismo (5) ocupa a casa dos centésimos (segunda após a vírgula), lê-se o número 75 acompanhado da última ordem: setenta e cinco centésimos."
        },
        {
            "id": "q35", "dificuldade": "intermediario",
            "enunciado": "Na tabela do Índice de Desenvolvimento Humano (IDH) hipotético, o país X tem $0,765$, o Y tem $0,76$, e o Z tem $0,756$. Qual é a ordem do país com MAIOR para o MENOR índice?",
            "alternativas": [
                "a) X, Y, Z",
                "b) X, Z, Y",
                "c) Y, X, Z",
                "d) Z, Y, X",
                "e) Y, Z, X"
            ],
            "gabarito": "A",
            "resolucao": "Equalizando as casas decimais de todos (3 casas): X = 0,765, Y = 0,760, Z = 0,756. Comparando os milésimos: 765 > 760 > 756. Portanto, a ordem do maior para o menor é X, Y, Z."
        },
        {
            "id": "q36", "dificuldade": "intermediario",
            "enunciado": "Numa fita métrica, um marceneiro registra três medidas em metros: $2,8$; $2,08$ e $2,18$. Posicionando-as na reta, quem ficará mais à direita?",
            "alternativas": [
                "a) $2,8$, pois possui 8 décimos, tornando-o o maior valor do conjunto.",
                "b) $2,08$, porque 08 é maior que 8.",
                "c) $2,18$, porque 18 é maior que 8 e 08.",
                "d) Todos ficarão no mesmo ponto, pois usam os mesmos algarismos.",
                "e) Nenhuma das medidas está na mesma reta numérica."
            ],
            "gabarito": "A",
            "resolucao": "Equalizando em centésimos: 2,80 ; 2,08 ; 2,18. O maior valor é 2,80. Na reta numérica, os valores crescem para a direita, logo o maior número ficará mais à direita."
        },
        {
            "id": "q37", "dificuldade": "intermediario",
            "enunciado": "Qual alternativa mostra um preenchimento adequado de zeros sem alterar o valor do número $8,4$?",
            "alternativas": [
                "a) $08,04$",
                "b) $8,004$",
                "c) $8,400$",
                "d) $80,4$",
                "e) $0,84$"
            ],
            "gabarito": "C",
            "resolucao": "O zero inserido à direita da última casa decimal não altera o valor do número (equivalência). Assim, 8,4 equivale a 8,40 e a 8,400."
        },
        {
            "id": "q38", "dificuldade": "intermediario",
            "enunciado": "O sucessor no conjunto dos números naturais para $5$ é $6$. Contudo, nos decimais, qual número vem imediatamente após $5,2$?",
            "alternativas": [
                "a) $5,3$",
                "b) $5,21$",
                "c) $5,201$",
                "d) $6,2$",
                "e) Não existe o conceito de sucessor imediato nos números racionais."
            ],
            "gabarito": "E",
            "resolucao": "Os números racionais na forma decimal possuem a propriedade da densidade. Não existe 'o' sucessor imediato, pois entre 5,2 e qualquer número posterior, existem infinitos outros números racionais."
        },
        {
            "id": "q39", "dificuldade": "intermediario",
            "enunciado": "O número expresso pela adição $3 + \\frac{2}{10} + \\frac{7}{1000}$ é igual a:",
            "alternativas": [
                "a) $3,27$",
                "b) $3,207$",
                "c) $3,027$",
                "d) $32,700$",
                "e) $3,270$"
            ],
            "gabarito": "B",
            "resolucao": "Temos 3 inteiros, 2 décimos (primeira casa) e 7 milésimos (terceira casa). A casa dos centésimos (segunda casa) está vazia e deve ser preenchida com um zero posicional. Logo, 3,207."
        },
        {
            "id": "q40", "dificuldade": "intermediario",
            "enunciado": "Um aluno tentou converter a fração $\\frac{5}{8}$ para decimal e ficou preso porque $10$ e $100$ não são múltiplos de $8$. Qual deve ser o próximo denominador decimal testado e qual o resultado final?",
            "alternativas": [
                "a) 1000; multiplicando ambos por 125, resulta em $\\frac{625}{1000} = 0,625$.",
                "b) 1000; multiplicando ambos por 100, resulta em $\\frac{500}{1000} = 0,500$.",
                "c) 200; multiplicando ambos por 25, resulta em $\\frac{125}{200} = 0,125$.",
                "d) 80; multiplicando ambos por 10, resulta em $\\frac{50}{80} = 0,50$.",
                "e) 1000; multiplicando ambos por 125, resulta em $\\frac{625}{100} = 6,25$."
            ],
            "gabarito": "A",
            "resolucao": "Buscando uma potência de 10 múltipla de 8, encontramos 1.000 ($1000 / 8 = 125$). Multiplicando 5 por 125, temos 625. A fração equivalente é 625/1000, que corresponde ao decimal 0,625."
        }
    ]
