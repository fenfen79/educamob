def get_q_basicas():
    return [
        {
            "id": "q01", "dificuldade": "basico",
            "enunciado": "Como se lê corretamente o número decimal $0,7$?",
            "alternativas": [
                "a) Sete inteiros.",
                "b) Sete dezenas.",
                "c) Sete décimos.",
                "d) Sete centésimos.",
                "e) Sete milésimos."
            ],
            "gabarito": "C",
            "resolucao": "O algarismo 7 está na primeira casa após a vírgula, que corresponde à ordem dos décimos. Logo, lê-se 'sete décimos'."
        },
        {
            "id": "q02", "dificuldade": "basico",
            "enunciado": "A professora ditou o número 'cinco inteiros e quatro centésimos'. Qual é a representação numérica correta desse valor?",
            "alternativas": [
                "a) $5,4$",
                "b) $5,04$",
                "c) $5,004$",
                "d) $0,54$",
                "e) $5,40$"
            ],
            "gabarito": "B",
            "resolucao": "A parte inteira é 5. 'Quatro centésimos' indica que o 4 deve estar na segunda casa decimal. Logo, a primeira casa decimal (décimos) deve ser preenchida com o zero, resultando em 5,04. A alternativa A representa cinco inteiros e quatro décimos, e a C, milésimos."
        },
        {
            "id": "q03", "dificuldade": "basico",
            "enunciado": "No número $12,389$, qual algarismo ocupa a ordem dos milésimos?",
            "alternativas": [
                "a) 1",
                "b) 2",
                "c) 3",
                "d) 8",
                "e) 9"
            ],
            "gabarito": "E",
            "resolucao": "A ordem dos milésimos é a terceira posição à direita da vírgula. A primeira é décimos (3), a segunda é centésimos (8) e a terceira é milésimos (9)."
        },
        {
            "id": "q04", "dificuldade": "basico",
            "enunciado": "Qual das alternativas apresenta o número 'cento e três milésimos' de forma correta?",
            "alternativas": [
                "a) $1,03$",
                "b) $0,130$",
                "c) $0,103$",
                "d) $10,3$",
                "e) $103,0$"
            ],
            "gabarito": "C",
            "resolucao": "Como não há parte inteira citada, começa-se com '0,'. 'Cento e três milésimos' significa que o último algarismo do número 103 deve ocupar a ordem dos milésimos (terceira casa). Assim, o número preenche as três casas: 0,103."
        },
        {
            "id": "q05", "dificuldade": "basico",
            "enunciado": "Em uma régua comum (reta numérica), cada centímetro é dividido em 10 partes menores chamadas milímetros. Cada milímetro corresponde a qual fração do centímetro?",
            "alternativas": [
                "a) Um milésimo",
                "b) Um décimo",
                "c) Um centésimo",
                "d) Uma unidade",
                "e) Uma dezena"
            ],
            "gabarito": "B",
            "resolucao": "Quando uma unidade inteira (neste caso, o centímetro) é dividida em exatamente 10 partes iguais, cada uma dessas partes é denominada um décimo ($0,1$)."
        },
        {
            "id": "q06", "dificuldade": "basico",
            "enunciado": "Decompondo o número $4,15$, encontramos:",
            "alternativas": [
                "a) 4 unidades e 15 décimos",
                "b) 4 unidades, 1 décimo e 5 milésimos",
                "c) 4 unidades, 1 décimo e 5 centésimos",
                "d) 4 unidades e 15 milésimos",
                "e) 4 centenas e 15 unidades"
            ],
            "gabarito": "C",
            "resolucao": "A parte inteira é o 4 (unidades). A parte decimal tem o 1 na primeira ordem (décimos) e o 5 na segunda ordem (centésimos). Logo, 4 unidades, 1 décimo e 5 centésimos."
        },
        {
            "id": "q07", "dificuldade": "basico",
            "enunciado": "Observe o número decimal $0,007$. A leitura correta desse número é:",
            "alternativas": [
                "a) Sete décimos",
                "b) Sete centésimos",
                "c) Sete milésimos",
                "d) Zero inteiros e sete dezenas",
                "e) Sete unidades"
            ],
            "gabarito": "C",
            "resolucao": "O algarismo 7 está na terceira ordem decimal (a direita da vírgula). Essa posição corresponde aos milésimos."
        },
        {
            "id": "q08", "dificuldade": "basico",
            "enunciado": "Uma fração com denominador 100 pode ser representada facilmente na forma decimal. A fração $\\frac{45}{100}$ equivale ao decimal:",
            "alternativas": [
                "a) $4,5$",
                "b) $0,45$",
                "c) $0,045$",
                "d) $45,0$",
                "e) $450,0$"
            ],
            "gabarito": "B",
            "resolucao": "A fração 45/100 é lida como 'quarenta e cinco centésimos'. Em decimal, os centésimos ocupam até a segunda casa após a vírgula: 0,45."
        },
        {
            "id": "q09", "dificuldade": "basico",
            "enunciado": "Se localizarmos o número $3,8$ em uma reta numérica, ele estará situado entre quais números inteiros consecutivos?",
            "alternativas": [
                "a) 0 e 1",
                "b) 1 e 2",
                "c) 2 e 3",
                "d) 3 e 4",
                "e) 4 e 5"
            ],
            "gabarito": "D",
            "resolucao": "A parte inteira do número é 3 e a parte decimal (8 décimos) acrescenta um valor a esse inteiro. Portanto, ele passou do 3, mas ainda não chegou no 4."
        },
        {
            "id": "q10", "dificuldade": "basico",
            "enunciado": "O número 'dois inteiros e cinco décimos' pode causar confusão se associado apenas ao som. Qual é a forma correta em numerais?",
            "alternativas": [
                "a) $2,05$",
                "b) $2,5$",
                "c) $2,005$",
                "d) $0,25$",
                "e) $20,5$"
            ],
            "gabarito": "B",
            "resolucao": "A palavra 'décimos' indica que o algarismo 5 deve ocupar a primeira casa após a vírgula. Logo, $2,5$. A alternativa A representaria dois inteiros e cinco centésimos."
        },
        {
            "id": "q11", "dificuldade": "basico",
            "enunciado": "A representação fracionária $\\frac{6}{10}$ equivale, em número decimal, a:",
            "alternativas": [
                "a) $0,06$",
                "b) $0,6$",
                "c) $6,0$",
                "d) $0,006$",
                "e) $60,0$"
            ],
            "gabarito": "B",
            "resolucao": "6 sobre 10 lê-se 'seis décimos'. Na forma decimal, décimos ocupam a primeira casa após a vírgula: 0,6."
        },
        {
            "id": "q12", "dificuldade": "basico",
            "enunciado": "Para converter $0,09$ em fração, devemos observar que o algarismo $9$ ocupa a casa dos:",
            "alternativas": [
                "a) Décimos, resultando em $\\frac{9}{10}$",
                "b) Centésimos, resultando em $\\frac{9}{100}$",
                "c) Milésimos, resultando em $\\frac{9}{1000}$",
                "d) Inteiros, resultando em $\\frac{9}{1}$",
                "e) Dezenas, resultando em $\\frac{90}{100}$"
            ],
            "gabarito": "B",
            "resolucao": "A segunda casa decimal corresponde aos centésimos. Portanto, 0,09 é igual a 9 centésimos, ou a fração 9/100."
        },
        {
            "id": "q13", "dificuldade": "basico",
            "enunciado": "A vírgula nos números decimais serve para:",
            "alternativas": [
                "a) Separar os milhares das centenas.",
                "b) Separar o número em duas metades iguais.",
                "c) Separar a parte inteira da parte decimal.",
                "d) Indicar que o número é sempre negativo.",
                "e) Mostrar onde termina a conta."
            ],
            "gabarito": "C",
            "resolucao": "No Sistema de Numeração Decimal, a vírgula atua como o separador entre a parte inteira (unidades simples, dezenas, etc.) e as ordens decimais (décimos, centésimos, etc.)."
        },
        {
            "id": "q14", "dificuldade": "basico",
            "enunciado": "Qual dos números abaixo possui a parte inteira nula (igual a zero)?",
            "alternativas": [
                "a) $1,05$",
                "b) $0,82$",
                "c) $2,0$",
                "d) $10,4$",
                "e) $5,55$"
            ],
            "gabarito": "B",
            "resolucao": "A parte inteira é o número antes da vírgula. No número 0,82, o algarismo à esquerda da vírgula é o 0."
        },
        {
            "id": "q15", "dificuldade": "basico",
            "enunciado": "Ao posicionar o número $5,5$ em uma reta numérica traçada entre 5 e 6, onde exatamente ele ficará?",
            "alternativas": [
                "a) Mais perto do 5",
                "b) Mais perto do 6",
                "c) Exatamente no meio entre 5 e 6",
                "d) Em cima do número 5",
                "e) Em cima do número 6"
            ],
            "gabarito": "C",
            "resolucao": "O número 5,5 é 'cinco inteiros e cinco décimos'. Como o intervalo de 5 a 6 pode ser dividido em 10 décimos, cinco décimos representa exatamente a metade do caminho."
        },
        {
            "id": "q16", "dificuldade": "basico",
            "enunciado": "João escreveu $2,10$, e Maria escreveu $2,1$. Sobre esses números, é correto afirmar que:",
            "alternativas": [
                "a) O número de João é muito maior.",
                "b) O número de Maria é maior.",
                "c) O número de João é menor.",
                "d) Ambos representam a mesma quantidade (são equivalentes).",
                "e) Não é possível comparar esses números."
            ],
            "gabarito": "D",
            "resolucao": "Acrescentar ou retirar zeros à direita da última casa decimal significativa não altera o valor do número (equivalência decimal). Portanto, 2,1 (dois décimos) é o mesmo que 2,10 (vinte centésimos)."
        },
        {
            "id": "q17", "dificuldade": "basico",
            "enunciado": "Qual alternativa apresenta a leitura do número $15,003$?",
            "alternativas": [
                "a) Quinze inteiros e três décimos.",
                "b) Quinze inteiros e três centésimos.",
                "c) Quinze inteiros e três milésimos.",
                "d) Cento e cinquenta e três milésimos.",
                "e) Quinze mil e três."
            ],
            "gabarito": "C",
            "resolucao": "A parte inteira é 15 (quinze inteiros). A parte decimal tem o 3 na terceira casa (ordem dos milésimos). Logo, lê-se 'quinze inteiros e três milésimos'."
        },
        {
            "id": "q18", "dificuldade": "basico",
            "enunciado": "Se dividirmos uma barra de chocolate inteira em $100$ partes iguais e pegarmos $3$ partes, qual decimal representa a porção que pegamos?",
            "alternativas": [
                "a) $0,3$",
                "b) $0,03$",
                "c) $3,0$",
                "d) $0,003$",
                "e) $3,100$"
            ],
            "gabarito": "B",
            "resolucao": "Ao dividir a unidade em 100 partes iguais, cada parte é um centésimo. Três dessas partes são três centésimos, cuja notação é 0,03."
        },
        {
            "id": "q19", "dificuldade": "basico",
            "enunciado": "Considere o número $0,250$. Se escrevermos sua forma simplificada sem alterar seu valor numérico, teremos:",
            "alternativas": [
                "a) $2,5$",
                "b) $0,025$",
                "c) $0,25$",
                "d) $25,0$",
                "e) $0,2$"
            ],
            "gabarito": "C",
            "resolucao": "O zero à direita na última posição da parte decimal não altera o valor do número. Assim, os 250 milésimos ($0,250$) podem ser reduzidos e simplificados para 25 centésimos ($0,25$)."
        },
        {
            "id": "q20", "dificuldade": "basico",
            "enunciado": "Em um termômetro digital, a marca é $36,8°C$. O algarismo 8 representa:",
            "alternativas": [
                "a) 8 unidades de grau.",
                "b) 8 centésimos de grau.",
                "c) 8 milésimos de grau.",
                "d) 8 décimos de grau.",
                "e) 8 dezenas de grau."
            ],
            "gabarito": "D",
            "resolucao": "O algarismo 8 ocupa a primeira posição após a vírgula. Portanto, ele representa décimos (neste caso, 8 décimos de grau)."
        }
    ]
