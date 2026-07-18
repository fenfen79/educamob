---
série: "6º Ano"
disciplina: "Matemática"
unidade_temática: "Probabilidade e estatística"
objeto_de_conhecimento: "Diferentes tipos de representação de informações: gráficos e fluxogramas"
habilidades: "EF06MA34"
pré-requisitos: "EF06MA31, EF06MA32"
nível_dificuldade: "Básico"
tempo_estimado_de_leitura: "15 minutos"
status_de_revisao: "Produzido"
palavras_chave: ["Gráficos", "Fluxogramas", "Algoritmos", "Informação", "Lógica", "Representação Visual"]
fonte_bibliografica: "Base Nacional Comum Curricular (MEC); Code.org; IBGE"
---

# Mapas da Informação: De Gráficos Avançados a Fluxogramas

## Conceitos

Nos capítulos anteriores, desvendamos as tabelas e os gráficos clássicos da estatística: as barras para comparar categorias, as linhas para demonstrar o tempo, e os setores para dividir um total. No entanto, a era digital exige que sejamos fluentes em outras formas visuais e lógicas de transmitir a informação de maneira rápida e processável, tanto para o cérebro humano quanto para os computadores. 

Neste cenário avançado, destacam-se duas estruturas vitais: os **Infográficos** e os **Fluxogramas**.

### Infográficos
Um **Infográfico** transcende a fronteira entre a matemática pura e o design gráfico. Enquanto um gráfico de barras é estrito e focado apenas nos números, o infográfico é um pôster visual que mistura gráficos, textos explicativos breves, ilustrações artísticas, ícones e esquemas. Ele é desenhado especificamente para contar uma "história" completa.
Por exemplo, um infográfico sobre o aquecimento global pode exibir um grande termômetro derretendo gelo, acompanhado de setas apontando para um gráfico de linha sobre emissões de carbono, interligando a causa, a estatística e a consequência em uma única peça visual fluida e muito fácil de ser compreendida pelo público geral.

### Fluxogramas e o Pensamento Algorítmico
Enquanto tabelas relatam o que "já aconteceu" na pesquisa, os **Fluxogramas** relatam "como alguma coisa deve ser feita". Um fluxograma é a representação visual, passo a passo, de um **Algoritmo** (uma sequência lógica de instruções criadas para resolver um problema).

Para garantir que o fluxo de pensamento seja compreendido universalmente, o fluxograma obedece a um rigoroso código de formas geométricas padronizadas:
1. **Ovalo / Elipse (Terminal):** Usada unicamente no início e no fim do fluxograma (representa o "Início" e o "Fim" do programa).
2. **Retângulo (Processo):** Representa uma ação, um cálculo matemático ou uma ordem que deve ser executada. (ex: "Acenda a luz" ou "Some A + B").
3. **Losango (Decisão):** É a encruzilhada da lógica. Sempre contém uma pergunta (ex: "Está chovendo?"). Dele, sempre devem sair **duas setas** (geralmente uma para o "SIM" e outra para o "NÃO"), bifurcando o caminho e mudando o rumo do programa de acordo com a resposta.
4. **Paralelogramo (Entrada/Saída):** Indica que o sistema precisa que o usuário forneça uma informação externa (ex: "Digite sua idade").
5. **Setas (Linhas de Fluxo):** Indicam a direção obrigatória da leitura.

## Exemplos (Na Prática)

**Exemplo 1: O Fluxograma do Semáforo**
Ao tentar programar a lógica de funcionamento de um farol de trânsito em um fluxograma:
1. Começamos com uma **Elipse** escrito "INÍCIO". Uma seta desce para um **Retângulo** (Ação) escrito "Ligue a luz VERDE".
2. Uma seta desce para um **Retângulo** (Ação) "Aguarde 30 segundos".
3. Uma seta desce para um **Retângulo** (Ação) "Ligue a luz AMARELA".
4. Uma seta desce para um **Retângulo** (Ação) "Aguarde 5 segundos".
5. Uma seta desce para um **Retângulo** (Ação) "Ligue a luz VERMELHA".
6. Uma seta desce para um **Retângulo** (Ação) "Aguarde 30 segundos".
7. Neste momento, ao invés de ir para a elipse de "FIM", a seta fará um retorno por fora e subirá de volta até se conectar antes do passo 1 ("Ligue a luz VERDE"). Isso cria um ciclo eterno (chamado de *loop* na programação) que manterá o semáforo funcionando perfeitamente 24 horas por dia.

**Exemplo 2: A Encruzilhada da Decisão (O Losango)**
Você quer criar um algoritmo para acordar cedo.
- INÍCIO (Elipse).
- Ação (Retângulo): "O alarme toca".
- Decisão (Losango): "Estou muito atrasado?".
- **Seta do SIM:** Vai para uma Ação (Retângulo) "Pule da cama e troque de roupa".
- **Seta do NÃO:** Vai para uma Ação (Retângulo) "Aperte o botão Soneca e durma mais 10 min". Daqui, uma seta volta para a decisão inicial, criando um ciclo caso a pessoa continue não atrasada.

## Erros Comuns

| Padrão de Erro | Explicação | Raciocínio Corretivo |
|----------------|------------|----------------------|
| **Usar apenas caixas quadradas no fluxograma** | O aluno desenha todo o processo (início, perguntas e fim) em quadrados, ignorando as outras formas. | O formato da caixa não é enfeite, é a **sintaxe da linguagem visual**. Se um engenheiro ler um quadrado achará que é uma ação, mas se ali houver uma pergunta de SIM ou NÃO (que exige o Losango), a lógica entrará em colapso. |
| **Sair apenas uma seta do Losango** | O aluno coloca a pergunta "Choveu?", escreve apenas o que fazer se "Sim" e prossegue, deixando o programa "travado" se a resposta for "Não". | Todo Losango (Decisão) gera uma **bifurcação obrigatória**. Devem sair, no mínimo, duas setas (SIM e NÃO) prevendo os caminhos opostos para evitar falhas de lógica. |
| **Fluxogramas que não têm "Início" nem "Fim"** | O aluno começa com ações soltas no papel e termina o fluxo de forma abrupta. | Sem os marcos de limite (Elipses de Início/Fim), um computador tentará rodar aquele processo eternamente em "lixo de memória" sem saber que a tarefa acabou. |

## Conexões Interdisciplinares

A proficiência em leitura de infográficos e construções de fluxogramas é a habilidade-núcleo cobrada na **Ciência da Computação, Engenharia de Software e Robótica**. Todo código de Python, JavaScript ou C++ que dá vida aos videogames, inteligências artificiais e foguetes da SpaceX começou primeiro no papel branco, na forma de um grande e meticuloso fluxograma.
Na área da **Administração e Engenharia de Produção**, o diagrama de fluxo dita todo o padrão industrial. As empresas mapeiam como a matéria-prima chega, quem a transforma, a etapa de controle de qualidade (Losango de inspeção) e o empacotamento, garantindo rastreabilidade perfeita e eliminando desperdícios da fábrica.

## Resumo para Revisão

- As **representações visuais** vão muito além dos gráficos de barras. Elas podem ser mescladas em peças de design criativo chamadas de **Infográficos**.
- O **Fluxograma** é o desenho técnico da lógica, feito para mapear o passo a passo de um processo.
- **Ovalo/Elipse:** Sempre determina os limites e bordas do programa (INÍCIO e FIM).
- **Retângulo:** Indica uma ação que deve ser tomada.
- **Losango:** Representa uma tomada de decisão crítica, sempre contendo uma pergunta e bifurcando duas respostas (SIM e NÃO).
- A fluência em algoritmos e fluxogramas é a base direta da programação moderna.
- Você concluiu os tópicos do 6º Ano!

---
## Referências
- BRASIL. Ministério da Educação. Base Nacional Comum Curricular. Brasília: MEC, 2018.
- TAVARES, Luis. A Matemática da Computação. 2. ed. São Paulo: Edgard Blücher, 2019.
- IEZZI, Gelson; DOLCE, Osvaldo; MACHADO, Antonio. Matemática e Realidade: 6º Ano. 9. ed. São Paulo: Atual, 2018.
- DANTE, Luiz Roberto. Teláris Matemática - 6º Ano. 3. ed. São Paulo: Ática, 2019.
- CODE.ORG. Curriculum Framework for Computer Science. Seattle, 2021.
