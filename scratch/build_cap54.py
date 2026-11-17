import os

def build_draft_c54():
    frontmatter = """---
série: "Ensino Médio"
disciplina: "História"
objeto_de_conhecimento: "As Mutações Socioculturais na Era da Internet e das Redes Sociais: A Passagem da Mídia Unidirecional de Massas para as Redes Hiperconectadas; O Modelo de Negócios do Capitalismo de Vigilância (Shoshana Zuboff: Extração de Dados dos Usuários e Modificação Comportamental); As Bolhas Algorítmicas de Informação, Polarização Afetiva e o Fenômeno da Pós-Verdade (Onde Apelos Emocionais e Crenças Pessoais Têm Mais Peso do que Fatos e Evidências Comprovadas); A Disseminação em Massa de Desinformação (Fake News), O Revisionismo Histórico Negacionista e os Riscos Reais para as Sociedades Democráticas no Século XXI."
ebook_fonte: "em-his-c54-cultura-digital-algoritmos-pos-verdade-crise-esfera-publica.md"
habilidades: "EM13CHS101, EM13CHS106, EM13CHS504, EM13CHS603, EM13CHS606"
total_exercicios: 60
distribuicao:
  basico: 20
  intermediario: 20
  dificil: 20
---

# Lista de Exercícios: Cultura Digital, Algoritmos, Pós-Verdade e a Crise da Esfera Pública

## Nível Básico (Questões 1-20)
"""

    questions_basic = [
        # q01 (A)
        """<!-- id: q01 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: basico | objeto: midia-massas-vs-redes-hiperconectadas -->
### Questão 1
A transformação comunicacional ocorrida com a passagem da mídia analógica de massas tradicional (rádio, televisão e jornais impressos) para o ecossistema das redes digitais hiperconectadas caracteriza-se pela:

a) Transição de um modelo de transmissão vertical e unidirecional (de um para muitos) para uma rede descentralizada e interativa (de muitos para muitos).
b) Centralização de toda a produção de notícias sob o controle exclusivo de estações de rádio estatais.
c) Extinção completa da publicidade comercial em páginas da internet e aplicativos móveis.
d) Proibição do compartilhamento de vídeos caseiros por pessoas comuns em plataformas digitais.
e) Obrigatoriedade de aprovação prévia governamental para envio de qualquer correio eletrônico.

**Gabarito:** A

**Resolução:**
A cultura digital rompeu o modelo tradicional do *broadcast*, no qual poucos conglomerados emitiam mensagens para receptores passivos, transformando os usuários em produtores e distribuidores de conteúdo em redes horizontais.
""",
        # q02 (B)
        """<!-- id: q02 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: basico | objeto: capitalismo-vigilancia-shoshana-zuboff -->
### Questão 2
Na obra *A Era do Capitalismo de Vigilância*, a pesquisadora Shoshana Zuboff afirma que a matéria-prima gratuita central extraída pelas grandes corporações de tecnologia (Big Techs) consiste:

a) No minério de ferro extraído de jazidas profundas em leitos submarinos.
b) Na experiência íntima humana diária, traduzida em dados comportamentais como cliques, localização e reações emocionais.
c) Na energia hidráulica gerada por quedas de água em áreas rurais isoladas.
d) Em blocos de madeira nativa colhidos em plantações florestais certificadas.
e) Nas cotas compulsórias de papel sulfite compradas por órgãos do funcionalismo público.

**Gabarito:** B

**Resolução:**
Shoshana Zuboff conceitua o capitalismo de vigilância demonstrando que as plataformas digitais capturam a vida privada dos usuários como matéria-prima gratuita para alimentar algoritmos e prever condutas futuras.
""",
        # q03 (C)
        """<!-- id: q03 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: basico | objeto: bolhas-de-informacao-eli-pariser -->
### Questão 3
O conceito de bolhas de informação (ou bolhas algorítmicas), formulado pelo ativista digital Eli Pariser, descreve a situação em que:

a) O sinal de internet sem fio é interrompido por chuvas tropicais frequentes.
b) As mensagens de texto são apagadas compulsoriamente após cinco minutos de envio.
c) Os algoritmos entregam apenas conteúdos que confirmam as preferências e vieses do usuário, isolando-o de pontos de vista divergentes.
d) Os usuários de redes sociais são impedidos de navegar na internet durante períodos eleitorais.
e) O governo estabelece limites rígidos para o número diário de fotografias postadas em murais virtuais.

**Gabarito:** C

**Resolução:**
As bolhas algorítmicas funcionam como câmaras de eco: ao personalizar a exibição de conteúdos com base em dados prévios de navegação, o sistema esconde ideias contrastantes e reforça convicções preexistentes.
""",
        # q04 (D)
        """<!-- id: q04 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: basico | objeto: definicao-pos-verdade-oxford -->
### Questão 4
O termo Pós-Verdade, eleito a palavra do ano em 2016 pelo Dicionário Oxford, define um contexto social e político no qual:

a) Os tribunais internacionais punem de forma imediata qualquer boato publicado em jornais matutinos.
b) As descobertas científicas de laboratório são aceitas de forma unânime e instantânea por todos os cidadãos.
c) Os computadores são programados para impedir o acesso a redes sociais durante o horário comercial.
d) Os fatos objetivos e as evidências comprovadas exercem menor influência na opinião pública do que os apelos às emoções e crenças pessoais.
e) Os jornais impressos voltam a ser a única fonte confiável de consulta de informações históricas.

**Gabarito:** D

**Resolução:**
A pós-verdade designa o enfraquecimento do compromisso coletivo com a verdade factual: convicções individuais, paixões ideológicas e medos passam a valer mais que dados objetivos e consensos científicos comprovados.
""",
        # q05 (E)
        """<!-- id: q05 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: basico | objeto: revisao-vs-negacionismo -->
### Questão 5
A distinção fundamental entre o trabalho legítimo de revisão histórica e a prática ideológica do negacionismo histórico reside no fato de que:

a) A revisão histórica é proibida em países democráticos dotados de constituições escritas.
b) O negacionismo é realizado exclusivamente por professores titulares de universidades públicas.
c) A revisão apoia-se em pesquisas orais sem qualquer análise de documentos oficiais arquivados.
d) O negacionismo busca ampliar o debate pacífico ao respeitar integralmente os depoimentos de vítimas de perseguição.
e) A revisão fundamenta-se em métodos rigorosos e novas fontes documentais, enquanto o negacionismo distorce deliberadamente ou nega fatos comprovados por motivos políticos.

**Gabarito:** E

**Resolução:**
A revisão faz parte da ciência histórica, aprimorando interpretações com base em novas evidências documentais; o negacionismo é uma fraude intencional que busca apagar crimes, torturas e genocídios para respaldar discursos autoritários.
""",
        # q06 (A)
        """<!-- id: q06 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: basico | objeto: conceito-prosumidor -->
### Questão 6
No contexto da cultura digital contemporânea, o termo 'prosumidor' (junção de produtor e consumidor) expressa o papel do indivíduo que:

a) Consome conteúdos e simultaneamente cria, publica e compartilha materiais em plataformas digitais e redes sociais.
b) Dedica-se exclusivamente à leitura de livros didáticos impressos sem utilizar aparelhos celulares.
c) Compra ações de empresas telefônicas estatais em pregões públicos de bolsa de valores.
d) Trabalha como revisor ortográfico concursado em editoras privadas de enciclopédias.
e) Recusa o acesso a redes de computadores por razões de preservação de segredos industriais.

**Gabarito:** A

**Resolução:**
O prosumidor representa a quebra da passividade da antiga audiência de rádio e TV: qualquer usuário com um celular pode produzir vídeos, textos e postagens, tornando-se ao mesmo tempo consumidor e criador nas redes.
""",
        # q07 (B)
        """<!-- id: q07 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: basico | objeto: economia-da-atencao-mecanismos -->
### Questão 7
A chamada Economia da Atenção estruturada pelas grandes plataformas de redes sociais apoia-se em recursos de design comportamental, tais como:

a) Cobrança de mensalidades em dinheiro para cada mensagem enviada a amigos próximos.
b) Mecanismos como rolagem contínua (infinite scroll), notificações sonoras frequentes e recompensas intermitentes com curtidas.
c) Desativação temporária dos aparelhos após trinta minutos ininterruptos de navegação diária.
d) Bloqueio permanente de vídeos com mais de dez segundos de duração em perfis de estudantes.
e) Substituição de telas coloridas por monitores monocromáticos com texto sem imagens.

**Gabarito:** B

**Resolução:**
Para prender os olhos do usuário na tela pelo maior tempo possível e ampliar a exibição de anúncios pagos, as plataformas empregam técnicas psicológicas de reforço intermitente similares às de jogos de azar.
""",
        # q08 (C)
        """<!-- id: q08 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: basico | objeto: polarizacao-afetiva -->
### Questão 8
A polarização afetiva, intensificada pelo funcionamento dos algoritmos de engajamento nas redes sociais, manifesta-se socialmente quando:

a) Os cidadãos debatem programas econômicos com tolerância e respeito aos acordos eleitorais.
b) Os integrantes de partidos concorrentes concordam com a partilha de cargos técnicos nos ministérios.
c) O debate político deixa de focar em propostas e passa a encarar o adversário como um inimigo moral perigoso a ser desumanizado e silenciado.
d) Os eleitores decidem anular os votos por desinteresse geral pelas eleições municipais.
e) As correntes ideológicas unem-se em campanhas solidárias para a construção de praças públicas.

**Gabarito:** C

**Resolução:**
Na polarização afetiva, a política deixa de ser um confronto legítimo de projetos entre concidadãos e vira um conflito de identidade emocional: o outro não é visto como adversário democrático, mas como inimigo moral indigno.
""",
        # q09 (D)
        """<!-- id: q09 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: basico | objeto: fake-news-industria -->
### Questão 9
As chamadas *fake news* caracterizam-se no cenário político contemporâneo não como meras fofocas casuais, mas como:

a) Exercícios literários poéticos protegidos pelo direito autoral internacional.
b) Traduções fiéis de pronunciamentos emitidos por embaixadas diplomáticas estrangeiras.
c) Erros involuntários de digitação cometidos por redatores apressados de cadernos de culinária.
d) Campanhas planejadas de desinformação produzidas de forma organizada com robôs e disparos em massa para manipular a opinião pública.
e) Crônicas bem-humoradas publicadas em revistas satíricas com aviso de paródia explícito.

**Gabarito:** D

**Resolução:**
A desinformação contemporânea é uma engrenagem industrial: equipes pagas, fazendas de cliques e contas automatizadas espalham mentiras intencionais desenhadas para inflamar tensões e interferir em eleições.
""",
        # q10 (E)
        """<!-- id: q10 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: basico | objeto: comissao-nacional-da-verdade-ditadura -->
### Questão 10
Em relação à Ditadura Militar brasileira (1964–1985), o Relatório Final da Comissão Nacional da Verdade (CNV), divulgado em 2014, cumpriu o papel histórico de:

a) Decretar o perdão automático e a promoção oficial de todos os agentes investigados por mortes.
b) Recomendar que as faculdades de história deixassem de lecionar o período republicano brasileiro.
c) Proibir o acesso de familiares aos registros policiais e certidões de óbito dos desaparecidos.
d) Estabelecer que o regime instaurado em 1964 não cometeu desvios nos direitos dos cidadãos.
e) Documentar com rigor factual as graves violações de direitos humanos, como torturas, assassinatos e ocultações de cadáveres pelo Estado.

**Gabarito:** E

**Resolução:**
A Comissão Nacional da Verdade investigou arquivos e colheu depoimentos comprovando a atuação sistemática do aparelho repressivo do Estado na prisão ilegal, tortura e morte de opositores políticos durante a ditadura.
""",
        # q11 (A)
        """<!-- id: q11 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: basico | objeto: papel-dos-gatekeepers -->
### Questão 11
No modelo tradicional de imprensa que predominou no século XX, os chamados *gatekeepers* (porteiros editoriais) exerciam a função de:

a) Filtrar, checar dados e selecionar as informações a serem publicadas com base em regras deontológicas e critérios jornalísticos profissionais.
b) Impedir a entrada física de leitores e assinantes nos edifícios sedes dos jornais.
c) Coletar dados privados de residências para revender a empresas de publicidade em outros países.
d) Censurar de forma armada qualquer texto que fizesse menção a inovações científicas.
e) Entregar exemplares de jornais de porta em porta nas periferias durante as madrugadas.

**Gabarito:** A

**Resolução:**
Jornalistas e editores profissionais funcionavam como guardiões da checagem: verificavam a procedência de fontes, corrigiam imprecisões e assumiam responsabilidade jurídica antes de as notícias chegarem ao público.
""",
        # q12 (B)
        """<!-- id: q12 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: basico | objeto: produtos-preditivos-zuboff -->
### Questão 12
Segundo a análise de Shoshana Zuboff, os 'produtos preditivos' gerados pelo capitalismo de vigilância têm como principal finalidade:

a) Aumentar a velocidade de download de arquivos escolares em áreas de preservação rural.
b) Antecipar e orientar comportamentos futuros dos indivíduos para comercializar essas certezas com anunciantes e operadores políticos.
c) Proteger o sigilo das comunicações pessoais contra invasões de programas maliciosos.
d) Fornecer previsões astronômicas sobre eclipses solares a centros de pesquisa física.
e) Estabelecer horários fixos de descanso para usuários de celulares inteligentes.

**Gabarito:** B

**Resolução:**
Ao cruzar trilhões de registros comportamentais, as plataformas elaboram perfis detalhados que preveem o que cada pessoa tem propensão a comprar ou em quem tende a votar, vendendo essa influência a mercados comerciais e políticos.
""",
        # q13 (C)
        """<!-- id: q13 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: basico | objeto: camaras-de-eco-efeitos -->
### Questão 13
As chamadas 'câmaras de eco' no ambiente das redes sociais digitais produzem como impacto sociocultural mais imediato:

a) O aprimoramento da tolerância com perspectivas políticas divergentes em fóruns abertos.
b) O desaparecimento de conflitos de opinião sobre temas do cotidiano urbano.
c) O reforço contínuo de preconceitos compartilhados pelo grupo e a redução da capacidade de diálogo com o contraditório.
d) O descarte em massa de aparelhos computacionais por obsolescência programada.
e) A diminuição no tempo médio de permanência dos jovens diante de telas iluminadas.

**Gabarito:** C

**Resolução:**
Em uma câmara de eco, os usuários ouvem apenas vozes que confirmam suas próprias opiniões, o que radicaliza posições, normaliza visões extremas e destrói a disposição para o debate com ideias diferentes.
""",
        # q14 (D)
        """<!-- id: q14 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: basico | objeto: esfera-publica-jurgen-habermas -->
### Questão 14
De acordo com a teoria social formulada pelo filósofo Jürgen Habermas, a saúde do regime democrático depende da vitalidade da Esfera Pública, compreendida como:

a) Um órgão militar encarregado de patrulhar fronteiras terrestres contra contrabandistas de peças de computador.
b) Um tribunal de exceção responsável por cassar mandatos de prefeitos de cidades litorâneas.
c) O conjunto de prédios onde funcionam os cartórios de registro de imóveis nos municípios.
d) Um espaço social comum de debate racional e livre entre cidadãos, baseado em fatos verificáveis para a formação do consenso político.
e) Um monopólio governamental sobre a totalidade das redes de telecomunicações do país.

**Gabarito:** D

**Resolução:**
Habermas demonstrou que a democracia representativa exige um espaço público de debate onde os cidadãos apresentem argumentos racionais e cheguem a decisões coletivas respaldadas em fatos partilhados pela sociedade.
""",
        # q15 (E)
        """<!-- id: q15 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: basico | objeto: negacionismo-do-holocausto -->
### Questão 15
O negacionismo do Holocausto, que busca contestar o genocídio de judeus e minorias perseguidas pelo regime nazista na Segunda Guerra Mundial, manifesta-se historicamente por meio de:

a) Descobertas comprovadas de laboratório que atestam a inexistência de ferrovias na Polônia.
b) Relatórios diplomáticos da ONU que declararam todos os campos de concentração como parques temáticos.
c) Decretos legislativos votados na Alemanha pós-guerra para encerrar tribunais de Nuremberg.
d) Acordos de paz firmados entre a resistência antifascista e governos colaboracionistas.
e) Tentativas deliberadas de apagar vestígios, negar o uso de câmaras de gás e tratar o assassinato em massa como invenção de propaganda.

**Gabarito:** E

**Resolução:**
O negacionismo do Holocausto é uma falsificação histórica criminosa: rejeita montanhas de provas documentais, fotos e testemunhos dos sobreviventes para tentar reabilitar a imagem do nazismo e disseminar o ódio.
""",
        # q16 (A)
        """<!-- id: q16 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: basico | objeto: leitura-lateral-fact-checking -->
### Questão 16
No aprendizado de métodos críticos de checagem de informações na internet (*fact-checking*), a prática da 'leitura lateral' consiste em:

a) Abrir abas complementares no navegador para verificar o que fontes independentes e órgãos confiáveis dizem sobre a notícia em análise.
b) Ler apenas o rodapé e as margens laterais esquerdas dos jornais impressos semanais.
c) Inclinar fisicamente o monitor do computador para reduzir reflexos solares nas letras.
d) Compartilhar a postagem imediatamente antes de ler o texto completo do artigo.
e) Consultar exclusivamente o perfil de rede social do autor da notícia duvidosa.

**Gabarito:** A

**Resolução:**
A leitura lateral ensina o internauta a sair da página suspeita e checar em outras abas o histórico do autor e o que agências de verificação reportam, em vez de se limitar a examinar a aparência interna daquele site.
""",
        # q17 (B)
        """<!-- id: q17 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: basico | objeto: modelo-de-negocio-big-techs -->
### Questão 17
O modelo de negócios predominante nas principais corporações proprietárias de redes sociais (como Meta, TikTok e X) sustenta-se principalmente por meio de:

a) Doações anônimas recolhidas em caixas postais comunitárias no interior dos continentes.
b) Venda de anúncios publicitários hipersegmentados e direcionados com base nos dados comportamentais dos usuários.
c) Venda de assinaturas de jornais de papel entregues semanalmente aos inscritos.
d) Repasses obrigatórios concedidos por sindicatos de operários metalúrgicos.
e) Cobrança de tarifas sobre a utilização de cabos telefônicos submarinos.

**Gabarito:** B

**Resolução:**
O serviço dessas plataformas é aparentemente gratuito para o usuário comum porque a mercadoria comercializada é a atenção e o perfil comportamental dos usuários, vendidos a anunciantes em leilões automatizados.
""",
        # q18 (C)
        """<!-- id: q18 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: basico | objeto: vies-de-confirmacao -->
### Questão 18
Na psicologia cognitiva aplicada à recepção de notícias nas redes, o 'viés de confirmação' atua como um fator que favorece a desinformação porque leva as pessoas a:

a) Questionar de forma imparcial qualquer informação que apoie suas ideias preferidas.
b) Recusar o uso de aparelhos celulares após a leitura de matérias científicas.
c) Buscar, aceitar e compartilhar conteúdos que reforcem convicções prévias, rejeitando evidências contrárias comprovadas.
d) Procurar amigos com visões opostas para reescrever publicações nas redes.
e) Desconfiar sistematicamente de boatos sensacionalistas com manchetes alarmistas.

**Gabarito:** C

**Resolução:**
O viés de confirmação é a tendência psicológica de acolher sem hesitar aquilo em que já se acredita e desacreditar friamente qualquer dado que aponte o contrário, facilitando a viralização de boatos convenientes.
""",
        # q19 (D)
        """<!-- id: q19 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: basico | objeto: bots-disparos-em-massa -->
### Questão 19
A utilização de contas automatizadas (robôs ou *bots*) e disparos programados em aplicativos de mensagens durante períodos de eleições tem como objetivo:

a) Enviar lembretes diários de vacinação infantil para famílias cadastradas em postos de saúde.
b) Reduzir o tráfego de dados nos servidores para baratear custos de internet aos usuários.
c) Aumentar a cobertura jornalística sobre projetos de reforma agrária em pequenas cidades.
d) Criar a falsa impressão de apoio popular maciço a determinadas teses e disseminar acusações contra concorrentes.
e) Promover concursos de redação e poesia entre estudantes da rede pública de ensino.

**Gabarito:** D

**Resolução:**
Os robôs simulam o comportamento humano em larga escala: ao retuitar, comentar e compartilhar conteúdos milhares de vezes por minuto, forjam tendências artificiais (*trending topics*) para enganar a opinião pública.
""",
        # q20 (E)
        """<!-- id: q20 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: basico | objeto: negacionismo-da-escravidao -->
### Questão 20
A manifestação do negacionismo histórico no que tange ao passado colonial da escravidão no Brasil caracteriza-se por tentativas ideológicas de:

a) Pesquisar livros de batismo e testamentos coloniais para reconstituir laços familiares de cativos.
b) Estudar a resistência dos quilombos e revoltas negras preservadas nos arquivos da capitania.
c) Destacar a atuação de advogados abolicionistas na libertação de escravizados no século XIX.
d) Reconhecer a violência e a exploração desumana que alicerçaram o sistema escravista no país.
e) Retratar a colonização como uma convivência cordial e pacífica, negando o racismo estrutural para enfraquecer políticas de reparação e cotas.

**Gabarito:** E

**Resolução:**
O negacionismo da escravidão busca suavizar ou negar o horror do cativeiro, propagando a lenda de uma "escravidão suave" no Brasil para justificar a desigualdade racial e se opor a ações afirmativas de inclusão.
"""
    ]

    questions_inter = [
        # q21 (A)
        """<!-- id: q21 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: intermediario | objeto: transformacao-esfera-publica-habermas -->
### Questão 21
Ao confrontar o modelo habermasiano de Esfera Pública burguesa do século XVIII com o espaço público digital do século XXI, pesquisadores da comunicação identificam que as plataformas de redes sociais fragmentaram o debate coletivo porque:

a) Criaram praças digitais hipersegmentadas orientadas pela lógica do lucro privado, onde o debate racional cedeu lugar ao consumo de conteúdos individualizados que confirmam preconceitos de grupos isolados.
b) Estabeleceram a obrigatoriedade da presença física de todos os votantes em praças municipais para validação de leis.
c) Eliminaram qualquer possibilidade de transmissão de mensagens escritas entre usuários de regiões metropolitanas.
d) Proibiram que cidadãos comuns formulassem críticas a autoridades judiciais em murais comunitários.
e) Transferiram o controle da infraestrutura de telecomunicações para agências públicas de rádio amador.

**Gabarito:** A

**Resolução:**
A esfera pública clássica pressupunha um espaço comum onde argumentos eram avaliados por seu valor de verdade. As redes sociais corporativas mercantilizaram essa arena, fragmentando a sociedade em nichos polarizados onde o lucro do engajamento supera o consenso racional.
""",
        # q22 (B)
        """<!-- id: q22 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: intermediario | objeto: modificacao-comportamental-zuboff -->
### Questão 22
Na formulação de Shoshana Zuboff, a etapa mais avançada do capitalismo de vigilância ultrapassa a simples coleta passiva de dados para alcançar a 'modificação do comportamento'. Esse processo opera mediante:

a) A distribuição de cartilhas pedagógicas com conselhos de boas maneiras nas salas de bate-papo.
b) O uso de estímulos algorítmicos imperceptíveis, intervenções em fluxos de postagens e recomendações personalizadas que conduzem o indivíduo a ações convenientes aos anunciantes.
c) O desligamento obrigatório dos sistemas de informática das empresas durante os finais de semana.
d) O pagamento direto de bonificações financeiras para cada leitor que demonstrar pensamento crítico nas redes.
e) A imposição de toques de recolher noturnos fiscalizados por forças de segurança municipal.

**Gabarito:** B

**Resolução:**
O capitalismo de vigilância não se contenta em prever: intervém ativamente por meio de arquiteturas de escolha (*nudges*), ajustando o que a pessoa vê para direcionar seus sentimentos, compras ou decisões políticas sem que ela perceba a manipulação.
""",
        # q23 (C)
        """<!-- id: q23 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: intermediario | objeto: neurociencia-computacional-odio -->
### Questão 23
Estudos empíricos sobre a circulação de notícias nas plataformas digitais comprovam que postagens contendo apelos de raiva, medo e indignação moral propagam-se com velocidade substantivamente superior à de matérias ponderadas. A explicação econômica para a promoção desse conteúdo reside no fato de que:

a) As empresas mantenedoras de redes sociais possuem cláusulas estatutárias que exigem a defesa de grupos extremistas.
b) As legislações eleitorais de países ocidentais proíbem a veiculação de notícias equilibradas durante os fins de semana.
c) Sentimentos viscerais retêm o usuário conectado por mais tempo, gerando mais cliques e visualizações de anúncios, o que torna o conflito altamente rentável para as plataformas.
d) O custo de transmissão de mensagens de conciliação é financeiramente mais elevado para os servidores em nuvem.
e) Os programadores de inteligência artificial são instruídos a silenciar publicações que apresentem dados comprovados de saúde pública.

**Gabarito:** C

**Resolução:**
As plataformas lucram com a economia da atenção: a indignação e o pânico geram reações viscerais imediatas, mantendo os olhos grudados na tela. Como mais tempo de tela gera mais receita publicitária, os algoritmos promovem o conflito.
""",
        # q24 (D)
        """<!-- id: q24 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: intermediario | objeto: cambridge-analytica-mecanismo -->
### Questão 24
O escândalo internacional envolvendo a consultoria política britânica Cambridge Analytica em 2016 revelou uma faceta perigosa da cultura digital para os regimes democráticos ao comprovar que:

a) Os cartórios eleitorais foram invadidos por espiões armados que subtraíram cédulas de votação em papel.
b) As empresas fornecedoras de energia desligaram servidores governamentais durante a contagem de votos.
c) As emissoras de televisão aberta recusaram a transmissão de propagandas partidárias previamente autorizadas.
d) Dados pessoais e perfis psicológicos colhidos nas redes sociais foram usados para direcionar propagandas manipuladas e personalizadas aos eleitores com base em seus medos e fragilidades.
e) A totalidade dos eleitores norte-americanos passou a utilizar moedas digitais não rastreáveis em compras cotidianas.

**Gabarito:** D

**Resolução:**
A Cambridge Analytica capturou dados privados de dezenas de milhões de perfis para mapear vulnerabilidades emocionais e disparar anúncios altamente direcionados (*dark posts*), explorando inseguranças para interferir em eleições democráticas.
""",
        # q25 (E)
        """<!-- id: q25 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: intermediario | objeto: marco-civil-e-lgpd -->
### Questão 25
No ordenamento jurídico brasileiro, a aprovação do Marco Civil da Internet (Lei nº 12.965/2014) e da Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018) representou um avanço importante na regulação do ambiente virtual ao buscar assegurar:

a) O confisco judicial imediato de aparelhos celulares de usuários que deixarem de votar em pleitos municipais.
b) A obrigatoriedade de instalação de câmeras de monitoramento estatal no interior de todas as residências urbanas.
c) A proibição permanente da criação de novas empresas de tecnologia da informação em território nacional.
d) O fim do sigilo de correspondência postal de famílias operárias de baixa renda.
e) A neutralidade de rede, a privacidade dos cidadãos, a transparência no tratamento de dados e limites à vigilância indiscriminada por corporações.

**Gabarito:** E

**Resolução:**
O Marco Civil e a LGPD definiram balizas republicanas na rede: asseguraram o princípio da neutralidade da internet (proibindo provedores de discriminar tráfego) e garantiram direitos ao cidadão sobre seus dados pessoais diante do poder corporativo.
""",
        # q26 (A)
        """<!-- id: q26 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: intermediario | objeto: desregulamentacao-e-responsabilidade-plataformas -->
### Questão 26
O debate contemporâneo em torno da responsabilização civil das plataformas digitais pela circulação de conteúdos criminosos (como apologia ao nazismo, racismo e ataques a escolas) contrapõe duas posições centrais:

a) As Big Techs argumentam ser meras intermediárias neutras que não produzem o conteúdo dos usuários, enquanto juristas e defensores da democracia sustentam que a recomendação algorítmica e a monetização impõem um dever de cuidado e responsabilidade editorial às empresas.
b) Os juízes federais exigem a desativação da internet em todo o país, enquanto as companhias de eletricidade pretendem ampliar torres de transmissão.
c) Os sindicatos patronais pedem a censura prévia de qualquer obra literária de ficção, enquanto professores exigem a abertura de arquivos militares.
d) Os governos municipais pretendem assumir o controle dos códigos de programação dos motores de busca das redes internacionais.
e) As empresas de satélite recusam-se a operar comunicações que envolvam aparelhos móveis pessoais de estudantes.

**Gabarito:** A

**Resolução:**
As plataformas tentam se esquivar alegando que funcionam como meras companhias de telecomunicação; contudo, como seus algoritmos selecionam ativamente o que viraliza e lucram com isso, recai sobre elas o dever de conter a propagação de crimes e desinformação mortal.
""",
        # q27 (B)
        """<!-- id: q27 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: intermediario | objeto: assimetria-de-poder-vigilancia -->
### Questão 27
Uma das características mais alarmantes da ordem do capitalismo de vigilância apontada por teóricos sociais é a 'assimetria radical de conhecimento e poder'. Essa assimetria decorre da circunstância em que:

a) As escolas públicas detêm mais informações sobre finanças do que as grandes instituições financeiras.
b) As megacorporações digitais acumulam um conhecimento detalhado e ininterrupto sobre a vida dos cidadãos, enquanto os indivíduos não têm acesso nem compreendem o funcionamento fechado de seus algoritmos proprietários.
c) Os servidores públicos recebem treinamentos semanais em programação avançada de inteligência artificial.
d) As cooperativas rurais conseguem interceptar sinais de satélite com aparelhos de rádio comunitário.
e) O público consumidor conhece integralmente as linhas de código dos sistemas operacionais dos celulares.

**Gabarito:** B

**Resolução:**
Zuboff sintetiza esse abismo na fórmula: eles sabem tudo sobre nós, mas nós não sabemos quase nada sobre eles. O conhecimento sobre as condutas humanas torna-se monopólio privado de poucas empresas, erodindo a soberania popular.
""",
        # q28 (C)
        """<!-- id: q28 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: intermediario | objeto: polarizacao-tribalismo-redes -->
### Questão 28
Ao analisar o impacto dos algoritmos de recomendação na dinâmica das campanhas eleitorais, sociólogos destacam que a formação de identidades políticas fechadas transformou a divergência cívica em tribalismo moral. Isso significa que os grupos passam a:

a) Construir alianças programáticas com partidos de centro para viabilizar investimentos em estradas vicinais.
b) Recusar o comparecimento aos comícios de seus próprios candidatos preferidos por medo de contágio viral.
c) Enxergar seus correligionários como os únicos representantes da decência e tratar os eleitores do campo oposto como seres perversos desprovidos de legitimidade política.
d) Priorizar a leitura de relatórios técnicos de órgãos estatísticos estatais antes de decidir o voto.
e) Renunciar ao uso de aplicativos de mensagens para discutir matérias de interesse coletivo.

**Gabarito:** C

**Resolução:**
O tribalismo político nas redes substitui o debate de ideias pela deslegitimação existencial do outro: o adversário não é alguém com quem se diverge sobre impostos ou políticas, mas uma personificação do mal que deve ser destruída.
""",
        # q29 (D)
        """<!-- id: q29 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: intermediario | objeto: desinformacao-e-pandemia-negacionismo -->
### Questão 29
Durante crises sanitárias globais recentes, a circulação em massa de desinformação científica e teorias da conspiração em redes sociais gerou impactos graves no mundo real porque:

a) Reduziu a procura de consultas odontológicas em bairros centrais das capitais.
b) Levou o Ministério da Educação a antecipar o calendário escolar em períodos de chuvas.
c) Provocou o fechamento temporário de agências bancárias nas capitais dos estados.
d) Estimulou a recusa de vacinas comprovadamente eficazes, promoveu o uso de remédios ineficazes e ampliou a mortalidade evitável de milhares de cidadãos.
e) Impediu a importação de termômetros manuais por hospitais universitários de referência.

**Gabarito:** D

**Resolução:**
A pós-verdade e o negacionismo científico cobram um preço em vidas humanas: desinformações sobre imunizantes e tratamentos milagrosos alimentaram a desconfiança pública, levando pessoas a recusar proteção e falecer por doenças evitáveis.
""",
        # q30 (E)
        """<!-- id: q30 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: intermediario | objeto: negacionismo-climatico-interesses -->
### Questão 30
O negacionismo da crise climática no século XXI articula interesses econômicos e discursos conspiratórios nas redes ao tentar desqualificar os relatórios do IPCC com a narrativa de que o aquecimento global:

a) Decorre unicamente do avanço de tecnologias solares instaladas em áreas residenciais.
b) É provocado pelo aumento no consumo de bicicletas por trabalhadores de grandes cidades.
c) Exige o fechamento de parques florestais mantidos por comunidades de pescadores artesanais.
d) É uma constatação óbvia confirmada por companhias exploradoras de petróleo e gás fóssil.
e) Seria uma invenção de cientistas e governos estrangeiros para frear a produção agropecuária e industrial, protegendo os lucros das indústrias fósseis poluidoras.

**Gabarito:** E

**Resolução:**
O negacionismo climático reproduz o método da indústria do tabaco: financia campanhas e propaga dúvidas artificiais nas redes para atrasar leis ambientais e preservar os lucros milionários da queima de combustíveis fósseis e do desmatamento.
""",
        # q31 (A)
        """<!-- id: q31 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: intermediario | objeto: deepfakes-desafios-provas -->
### Questão 31
O desenvolvimento de ferramentas de inteligência artificial generativa capazes de produzir *deepfakes* (vídeos, áudios e imagens sintéticas de altíssimo realismo) coloca novos desafios para a crítica documental histórica e para o jornalismo porque:

a) Permite forjar declarações comprometedoras e condutas inexistentes de figuras públicas com aparência verídica, tornando indispensável o domínio de métodos avançados de verificação pericial de mídias.
b) Garante que qualquer usuário de telefone celular possa identificar a autenticidade de gravações apenas olhando a tela sem programas auxiliares.
c) Impede a veiculação de reportagens investigativas sobre desvios de recursos públicos em canais de televisão.
d) Substitui de forma permanente o trabalho de juízes e promotores em audiências de conciliação judiciária.
e) Elimina a necessidade de consultar arquivos documentais em pesquisas de pós-graduação sobre a República Velha.

**Gabarito:** A

**Resolução:**
As *deepfakes* quebram a máxima popular de que "ver é crer": ao gerar áudios e vídeos forjados perfeitos, exigem que a sociedade desenvolva competências de perícia digital e checagem cruzada para impedir fraudes eleitorais e crimes de difamação.
""",
        # q32 (B)
        """<!-- id: q32 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: intermediario | objeto: governamentalidade-algoritmica -->
### Questão 32
Teóricos contemporâneos da cibernética e da sociologia do direito cunharam a expressão 'governamentalidade algorítmica' para descrever uma forma de exercício do poder que:

a) Substitui os parlamentos eleitos por reuniões semanais de líderes comunitários nas prefeituras.
b) Modela e antecipa as escolhas individuais por meio da análise estatística automatizada de fluxos de dados, sem recorrer necessariamente a ordens explícitas ou coerção física direta.
c) Devolve às comunidades camponesas a gestão autônoma das águas e das sementes nativas.
d) Proíbe o registro de patentes de softwares e algoritmos nos institutos nacionais de propriedade industrial.
e) Força a totalidade dos órgãos judiciais a utilizar máquinas de datilografia em suas sentenças.

**Gabarito:** B

**Resolução:**
A governamentalidade algorítmica opera silenciosamente: ela não precisa de polícia na porta; ao estruturar as opções visíveis, os preços, as recomendações e os resultados de busca, conduz suavemente as condutas da sociedade no rumo desejado pelo sistema.
""",
        # q33 (C)
        """<!-- id: q33 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: intermediario | objeto: polarizacao-e-ruptura-social -->
### Questão 33
A persistência da polarização afetiva alimentada por câmaras de eco nas redes digitais afeta a convivência cotidiana e as instituições republicanas na medida em que:

a) Facilita a aprovação unânime de emendas constitucionais voltadas à infraestrutura viária.
b) Fortalece a confiança dos cidadãos na integridade dos órgãos eleitorais e institutos de pesquisa estatística.
c) Rompe laços de amizade e relações familiares e estimula a recusa a aceitar os resultados legítimos de eleições decididas pelas urnas.
d) Elimina as disputas partidárias permitindo governos de coalizão permanentes nos municípios.
e) Estimula o hábito de leitura regular de fontes primárias históricas pelas famílias nos finais de semana.

**Gabarito:** C

**Resolução:**
A polarização extrema degrada o convívio social: divide famílias, destrói amizades e gera a recusa violenta a reconhecer a legitimidade de governos eleitos, abrindo caminho para tentativas de ruptura institucional e autoritarismo.
""",
        # q34 (D)
        """<!-- id: q34 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: intermediario | objeto: desinformacao-e-guerra-hibrida -->
### Questão 34
No âmbito das relações internacionais e da defesa da soberania nacional, o emprego de campanhas maciças de desinformação em redes sociais é enquadrado pela doutrina de segurança contemporânea como:

a) Um procedimento rotineiro de diplomacia cultural sem impactos em eleições soberanas.
b) Um serviço comercial voltado exclusivamente à divulgação de pontos turísticos nas capitais.
c) Uma troca espontânea de manifestações folclóricas entre juventudes de países vizinhos.
d) Uma modalidade de guerra híbrida destinada a enfraquecer a coesão social, desestabilizar adversários geopolíticos e minar a confiança nas instituições democráticas por dentro.
e) Uma atividade pacífica de pesquisa de opinião coordenada pela Assembleia Geral da ONU.

**Gabarito:** D

**Resolução:**
A guerra híbrida combina ações cibernéticas e desinformação sistemática: em vez de tanques e tropas, operadores patrocinados por potências utilizam redes e vazamentos seletivos para aprofundar divisões internas e paralisar nações rivais.
""",
        # q35 (E)
        """<!-- id: q35 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: intermediario | objeto: negacionismo-e-fascismo-historico -->
### Questão 35
O historiador Marcos Napolitano adverte que o negacionismo histórico não deve ser encarado como mera ignorância ingênua ou curiosidade exótica, mas sim como uma estratégia política que visa:

a) Atualizar o catálogo de fontes de arquivos públicos para facilitar pesquisas acadêmicas.
b) Incentivar a leitura de relatórios de comissões da verdade por estudantes do ensino fundamental.
c) Preservar monumentos e museus dedicados à memória das vítimas de regimes violentos.
d) Desestimular a publicação de panfletos anônimos com calúnias sobre personalidades históricas.
e) Reabilitar projetos autoritários e legitimar violências do presente ao deslegitimar a memória das vítimas e falsear o passado documentado.

**Gabarito:** E

**Resolução:**
O negacionismo tem um propósito político deliberado: ao apagar os crimes, perseguições e torturas de regimes do passado, busca retirar o estigma das ideias fascistas e autoritárias, abrindo espaço para a sua repetição no presente.
""",
        # q36 (A)
        """<!-- id: q36 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: intermediario | objeto: busca-reversa-de-imagens -->
### Questão 36
Na oficina de letramento digital contra boatos caça-cliques, a ferramenta de 'busca reversa de imagens' em motores de busca na internet revela-se fundamental porque permite:

a) Identificar o contexto original, a data e a localização real de uma fotografia utilizada de forma manipulada ou fora de contexto em postagens alarmistas.
b) Imprimir cópias de fotografias antigas em papel brilhante de alta gramatura sem custos de envio.
c) Deletar fotos postadas por adversários políticos em redes sociais de maneira imediata e secreta.
d) Alterar a resolução de imagens coloridas para exibi-las em televisores analógicos residenciais.
e) Traduzir textos inscritos em monumentos de pedra utilizando sistemas automáticos de reconhecimento de caracteres.

**Gabarito:** A

**Resolução:**
Desinformações frequentemente usam fotos autênticas, mas tiradas em outro país ou época, para ilustrar um boato recente. A busca reversa localiza as primeiras publicações da imagem, desmontando a fraude em segundos.
""",
        # q37 (B)
        """<!-- id: q37 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: intermediario | objeto: soberania-de-dados-e-dependencia-tecnologica -->
### Questão 37
A dependência estrutural dos países do Sul Global em relação aos serviços de armazenamento em nuvem, cabos submarinos e plataformas das Big Techs sediadas no Norte Global gera um problema de:

a) Excesso de oferta de equipamentos de rádio amador nas repartições públicas estaduais.
b) Perda de soberania digital e de dados, na medida em que as informações estratégicas da população e do Estado ficam armazenadas sob jurisdições e interesses corporativos estrangeiros.
c) Fechamento involuntário de fábricas de televisores instaladas em zonas francas de comércio.
d) Proibição do uso de correio postal físico para entrega de documentos alfandegários oficiais.
e) Transferência compulsória de reservas cambiais para consórcios de companhias de telecomunicação.

**Gabarito:** B

**Resolução:**
Quando dados pessoais, prontuários de saúde e comunicações governamentais de um país estão hospedados em servidores de corporações norte-americanas, a nação perde soberania, ficando vulnerável a espionagens e chantagens geopolíticas.
""",
        # q38 (C)
        """<!-- id: q38 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: intermediario | objeto: efeito-dunning-kruger-redes -->
### Questão 38
O fenômeno cognitivo conhecido como 'Efeito Dunning-Kruger', frequentemente observado em discussões acaloradas nas redes sociais sobre História e Medicina, caracteriza-se pela tendência de:

a) Especialistas com doutorado recusarem o debate acadêmico por desinteresse na docência.
b) Estudantes universitários abandonarem pesquisas laboratoriais para abrir perfis de entretenimento.
c) Indivíduos com pouco ou nenhum conhecimento técnico sobre um assunto superestimarem sua própria competência, opinando com arrogância e rejeitando diagnósticos consolidados da ciência.
d) Professores de escolas públicas concordarem unicamente com teses defendidas em congressos internacionais.
e) Jornalistas checadores aceitarem boatos como verdades irrefutáveis sem cruzamento de dados.

**Gabarito:** C

**Resolução:**
O efeito Dunning-Kruger explica a arrogância da ignorância: pessoas sem domínio sobre determinado campo têm dificuldade de avaliar a própria limitação, acreditando saber mais que cientistas, médicos e historiadores profissionais.
""",
        # q39 (D)
        """<!-- id: q39 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: intermediario | objeto: mensageria-privada-criptografia-desinformacao -->
### Questão 39
A disseminação de desinformação por meio de aplicativos de mensagens instantâneas privadas (como WhatsApp e Telegram) impõe obstáculos singulares às estratégias de checagem pública porque:

a) Os aparelhos celulares desligam as telas automaticamente caso detectem textos de conteúdo histórico.
b) As empresas responsáveis pelos aplicativos proíbem o envio de áudios gravados com a própria voz.
c) As mensagens são convertidas em arquivos de imagem monocromáticos ilegíveis para pessoas idosas.
d) A criptografia de ponta a ponta e a circulação em grupos fechados criam circuitos subterrâneos de difícil monitoramento, onde boatos circulam com selo de confiança interpessoal.
e) Os municípios aplicam tarifas postais sobre cada mensagem encaminhada para mais de três destinatários.

**Gabarito:** D

**Resolução:**
Nos aplicativos fechados com criptografia, não há como moderadores públicos checarem o boato. Além disso, a mentira chega enviada por familiares ou amigos de confiança, contornando defesas críticas com mais eficácia que postagens públicas.
""",
        # q40 (E)
        """<!-- id: q40 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: intermediario | objeto: memoria-historica-antidoto-ao-autoritarismo -->
### Questão 40
A preservação da memória histórica documentada e o combate rigoroso ao revisionismo negacionista constituem imperativos republicanos fundamentais no século XXI porque:

a) Garantem a cobrança pontual de taxas de visitação em museus de arte decorativa metropolitana.
b) Impedem a realização de congressos acadêmicos que debatam novas abordagens historiográficas.
c) Estabelecem que os livros didáticos não podem ser atualizados com pesquisas de pós-graduação.
d) Asseguram o monopólio estatal sobre todas as oficinas de tipografia e encadernação do país.
e) Funcionam como uma blindagem ética e cidadã contra a repetição de atrocidades e violações autoritárias, reafirmando o compromisso da sociedade com os direitos humanos e a democracia.

**Gabarito:** E

**Resolução:**
Um povo que esquece ou tolera a falsificação de seu próprio passado violento está condenado a repetir os mesmos erros. Manter a verdade factual sobre a escravidão, o Holocausto e a ditadura é a defesa da dignidade humana no presente.
"""
    ]

    questions_hard = [
        # q41 (A)
        """<!-- id: q41 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: dificil | objeto: habermas-crise-esfera-publica-algoritmos -->
### Questão 41
Na obra clássica *Mudança Estrutural da Esfera Pública*, Jürgen Habermas demonstra que o surgimento da esfera pública no século XVIII constituiu a base da legitimidade das democracias modernas, alicerçada no uso público da razão e no debate entre cidadãos livres em torno de fatos verificáveis. Ao confrontar essa teoria com o ecossistema digital contemporâneo regido por plataformas algorítmicas, constata-se uma fratura estrutural porque:

a) A mercantilização corporativa das redes e o isolamento informacional das bolhas algorítmicas destruíram o espaço compartilhado de debate racional, substituindo o princípio do melhor argumento pelo engajamento financeirizado e pela polarização afetiva.
b) Os governos democráticos substituíram os parlamentos representativos por sistemas diretos de votação telefônica aberta.
c) As plataformas de busca eliminaram por completo a possibilidade de pesquisas sobre filosofia iluminista em bibliotecas virtuais.
d) A totalidade das emissoras de rádio comunitário foi estatizada para impedir transmissões culturais nas cidades costeiras.
e) As empresas operadoras de telefonia desativaram a circulação de notícias escritas para privilegiar chamadas em voz analógica.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** A esfera pública idealizada por Habermas dependia da existência de um espaço comum onde cidadãos dialogavam racionalmente, avaliando proposições com base em fatos e evidências do mundo empírico compartilhado.
- **Etapa 2:** No ambiente digital do século XXI, o modelo de negócios das Big Techs não visa ao consenso cívico ou à verdade dos fatos, mas à monetização da atenção por meio de algoritmos de engajamento programados para priorizar o conflito e o ódio.
- **Etapa 3:** Como consequência, a esfera pública comum fragmentou-se em feudos informacionais polarizados e câmaras de eco, inviabilizando o debate racional e ameaçando o funcionamento das instituições democráticas republicanas.
""",
        # q42 (B)
        """<!-- id: q42 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: dificil | objeto: excedente-comportamental-zuboff-mecanismo -->
### Questão 42
Ao teorizar a dinâmica do Capitalismo de Vigilância, Shoshana Zuboff diferencia a prestação funcional de serviços digitais da extração oculta do chamado 'excedente comportamental' (*behavioral surplus*). A lógica operacional que sustenta essa nova fase de acumulação capitalista baseia-se no fato de que:

a) As empresas utilizam os lucros das assinaturas de computadores para subsidiar a merenda escolar de pequenas aldeias rurais.
b) Os dados comportamentais excedentes, capturados muito além do necessário para o aprimoramento dos serviços, são transformados por inteligência artificial em produtos preditivos vendidos no mercado futuro de certezas comportamentais.
c) As agências estatais de telefonia recolhem os dados dos cidadãos para imprimir listas telefônicas residenciais em papel reciclado.
d) Os usuários de navegadores recebem pagamentos mensais regulares pelo compartilhamento consciente de suas senhas de acesso bancário.
e) Os servidores em nuvem descartam automaticamente qualquer registro de navegação após quarenta e oito horas de armazenamento.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** No início da internet, os dados gerados pela navegação serviam apenas para melhorar o próprio serviço (como corrigir erros em mapas ou otimizar buscas de texto).
- **Etapa 2:** O salto do capitalismo de vigilância consistiu em perceber que o rastro digital excedente de cada indivíduo (pausas visuais, reações emocionais, trajetos de GPS) continha um valor econômico colossal se processado por inteligência de dados.
- **Etapa 3:** Esse excedente comporta mental alimenta fábricas de inteligência artificial que produzem previsões de conduta de alta acurácia, vendidas a corporações e operadores políticos interessados em influenciar e modificar as decisões humanas futuras.
""",
        # q43 (C)
        """<!-- id: q43 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: dificil | objeto: filtro-invisivel-eli-pariser-epistemologia -->
### Questão 43
Na obra *O Filtro Invisível*, o ativista e teórico digital Eli Pariser argumenta que a personalização algorítmica em motores de busca e murais sociais altera a própria relação dos cidadãos com a verdade e o conhecimento. As consequências epistêmicas e cívicas do funcionamento dessas bolhas caracterizam-se pelo fato de que:

a) As pesquisas em plataformas de busca passam a exibir resultados idênticos e padronizados para todos os indivíduos da Terra.
b) As escolas e faculdades são obrigadas a encerrar os cursos de licenciatura devido à gratuidade de artigos de jornal na rede.
c) A personalização opaca entrega a cada indivíduo apenas aquilo que o algoritmo deduz ser agradável ao seu perfil, privando o sujeito do acesso a fatos que desafiem suas crenças e corroendo o senso de uma realidade compartilhada.
d) Os usuários de aparelhos móveis adquirem capacidade plena de verificar se uma fonte jornalística é autêntica sem consultar outras páginas.
e) As plataformas de comércio encerram o envio de mensagens promocionais durante o período das eleições presidenciais.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** Eli Pariser demonstrou que dois indivíduos sentados lado a lado, ao digitarem o mesmo termo em um motor de busca, recebem respostas completamente diferentes com base em seus históricos pregressos.
- **Etapa 2:** Esse filtro invisível cria um ambiente cognitivo viciado: o algoritmo confirma permanentemente os preconceitos do usuário e esconde pontos de vista divergentes, impedindo o choque dialético saudável com o contraditório.
- **Etapa 3:** Em escala social, o resultado é a destruição da realidade objetiva comum: cada grupo passa a viver em seu próprio universo factual, tornando impossível qualquer consenso republicano em torno de problemas coletivos como a crise climática ou a saúde pública.
""",
        # q44 (D)
        """<!-- id: q44 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: dificil | objeto: pos-verdade-e-colapso-institucional -->
### Questão 44
A emergência da era da Pós-Verdade afeta diretamente o funcionamento do Estado Democrático de Direito ao desestabilizar o papel das instituições mediadoras e do consenso científico compartilhado. Sob a ótica da teoria política contemporânea, o perigo desse fenômeno reside no fato de que:

a) Os tribunais constitucionais passam a julgar causas criminais com base exclusiva em depoimentos colhidos em transmissões de rádio amador.
b) As assembleias legislativas estaduais deixam de discutir projetos de lei para se dedicar à redação de crônicas literárias.
c) As companhias privadas de engenharia civil recusam contratos com governos municipais por desconfiança em relação ao sistema métrico.
d) Quando os fatos verificáveis perdem sua autoridade pública em favor de mentiras convenientes e apelos emocionais, o diálogo cívico racional desaba e a política converte-se em mera guerra de narrativas manipulatórias sem limites éticos.
e) Os institutos públicos de meteorologia assumem o comando militar de postos de fronteira para conter o avanço de tempestades tropicais.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** A ordem republicana democrática apoia-se na separação entre opiniões legítimas (que podem ser plurais e diversas) e fatos empíricos objetivos (que formam o solo comum da realidade).
- **Etapa 2:** A dinâmica da pós-verdade opera o colapso dessa fronteira: lideranças populistas autoritárias tratam fatos comprovados como meras "conspirações da imprensa" e criam "fatos alternativos" desenhados para inflamar as paixões de suas bases.
- **Etapa 3:** Sem um terreno comum de fatos verificados pelo método científico e pelo jornalismo sério, a deliberação racional é aniquilada; a disputa política degenera em confronto sectário e violento, abrindo as portas para a tirania.
""",
        # q45 (E)
        """<!-- id: q45 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: dificil | objeto: negacionismo-da-ditadura-militar-brasileira -->
### Questão 45
Nas discussões historiográficas contemporâneas no Brasil, manifestações de negacionismo histórico sobre a Ditadura Militar (1964–1985) buscam reescrever o golpe civil-militar de 1964 como uma 'revolução democrática' e minimizar o terrorismo de Estado documentado nos arquivos oficiais. A refutação dessa falsificação ideológica pela ciência histórica fundamenta-se:

a) No cancelamento imediato de todos os concursos públicos para contratação de professores de história contemporânea.
b) Na proibição de pesquisas acadêmicas sobre governos militares anteriores à Proclamação da República de 1889.
c) Na declaração unilateral emitida por cortes arbitrais estrangeiras sem ouvir testemunhas nacionais do período.
d) Na substituição de livros didáticos por versões digitais editadas por sindicatos de empresas automobilísticas.
e) Na vasta base empírica e documental reunida por órgãos de Estado e pela Comissão Nacional da Verdade, que comprovou torturas, mortes e desrespeito sistemático à ordem constitucional republicana.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** O negacionismo do regime de 1964 não constitui uma corrente de interpretação historiográfica séria, mas uma falsificação deliberada do passado com objetivos de deslegitimar a Constituição cidadã de 1988.
- **Etapa 2:** A historiografia profissional e os relatórios oficiais do Estado brasileiro (como a Comissão de Mortos e Desaparecidos Políticos e a CNV) reuniram milhares de documentos do próprio aparato repressivo do Exército e da polícia.
- **Etapa 3:** Esses acervos provam categoricamente o caráter ditatorial do regime: fechamento do Congresso, cassação de mandatos, censura prévia da imprensa e uso de centros clandestinos de tortura contra opositores, desmentindo qualquer narrativa de preservação da democracia.
""",
        # q46 (A)
        """<!-- id: q46 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: dificil | objeto: psicologia-cognitiva-e-modelo-ocean-cambridge-analytica -->
### Questão 46
No escândalo da Cambridge Analytica em 2016, a consultoria cruzou dados extraídos das redes sociais com o modelo psicométrico dos 'Cinco Grandes Fatores' de personalidade (OCEAN: Abertura, Consciência, Extroversão, Agradabilidade e Neuroticismo). A aplicação dessa técnica na engenharia política digital representou um divisor de águas histórico porque:

a) Permitiu mapear fragilidades psíquicas e medos inconscientes de eleitores individuais para disparar propagandas políticas ocultas (dark posts) sob medida, manipulando o voto de forma personalizada e invisível aos demais cidadãos.
b) Determinou o cancelamento da votação presencial substituindo urnas por enquetes abertas em murais de fotos.
c) Forçou os partidos concorrentes a realizar seus debates eleitorais exclusivamente em programas de auditório de rádio matutino.
d) Assegurou que a totalidade dos dados eleitorais dos cidadãos fosse protegida por senhas sob tutela da Suprema Corte.
e) Impediu a circulação de notícias sobre pesquisas de intenção de voto durante os meses que antecederam a eleição.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** As campanhas políticas tradicionais usavam propagandas de massa em rádio e TV, visíveis a todos os cidadãos simultaneamente, o que permitia fiscalização jurídica e resposta dos adversários.
- **Etapa 2:** A combinação entre modelo OCEAN e dados de redes sociais permitiu o microdirecionamento invisível: um eleitor ansioso recebia vídeos de violência para induzi-lo a votar por medo, enquanto seu vizinho recebia postagens com apelos distintos.
- **Etapa 3:** Essa segmentação oculta destruiu a transparência do processo eleitoral: o debate público comum foi substituído por manipulações psicológicas sob medida, minando a autonomia de julgamento dos eleitores em regimes democráticos.
""",
        # q47 (B)
        """<!-- id: q47 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: dificil | objeto: extrativismo-digital-colonialismo-de-dados -->
### Questão 47
Pesquisadores que analisam as dinâmicas globais de tecnologia propõem o conceito de 'Colonialismo de Dados' para descrever a apropriação predatória de recursos informacionais no século XXI. A correlação histórica entre o colonialismo tradicional dos séculos XVI a XIX e o capitalismo de vigilância contemporâneo fundamenta-se no fato de que ambos:

a) Proíbem a circulação de embarcações marítimas de passageiros entre continentes vizinhos.
b) Operam pela apropriação não remunerada e ilegítima de matérias-primas cruciais (antes terras, corpos e minérios; hoje fluxos de vida e dados íntimos) para gerar riqueza e controle em favor de metrópoles corporativas globais.
c) Estabelecem a obrigatoriedade da adoção de idiomas europeus em todas as comunicações escolares municipais.
d) Destroem linhas telegráficas terrestres para evitar que comunidades camponesas enviem mensagens a órgãos públicos.
e) Delegam o controle fiscal de portos e aeroportos a cooperativas operárias de extração de seringais.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** O colonialismo histórico dos impérios europeus justificou a conquista territorial ao declarar a natureza e os povos originários do Sul Global como recursos gratuitos a serem despojados e colonizados.
- **Etapa 2:** O colonialismo de dados atua em uma nova fronteira: declara que os rastros digitais das pessoas são matérias-primas gratuitas que pertencem a quem tiver capacidade de capturá-las e refiná-las.
- **Etapa 3:** Assim como o velho modelo colonial concentrava a prata e o açúcar na Europa, as Big Techs concentram a riqueza dos dados e a inteligência algorítmica no Norte Global, mantendo o Sul em posição subalterna e vigiada.
""",
        # q48 (C)
        """<!-- id: q48 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: dificil | objeto: polarizacao-afetiva-e-desumanizacao -->
### Questão 48
Estudos em ciência política contemporânea apontam que a 'polarização afetiva' estimulada pelo engajamento nas redes sociais é muito mais nociva à convivência democrática do que a simples divergência programática sobre impostos ou políticas públicas. Essa distinção teórica apoia-se no fato de que a polarização afetiva:

a) Desperta desinteresse total pelas decisões dos poderes executivo e legislativo nos municípios do interior.
b) Estimula a formação de coalizões multipartidárias amplas em torno da defesa de direitos sociais básicos.
c) Constrói uma lógica tribal baseada em sentimentos de desprezo e ódio, onde o adversário é percebido não como concidadão com divergências legítimas, mas como ameaça moral absoluta a ser desumanizada e aniquilada.
d) Leva os membros de diferentes agremiações partidárias a assinar acordos formais de partilha de cargos técnicos em escolas públicas.
e) Obriga as emissoras de rádio a conceder espaço igualitário de fala para todas as tendências filosóficas em horários nobres.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** Em uma democracia sadia, a divergência ideológica sobre modelos econômicos e leis é normal e necessária para o aperfeiçoamento da sociedade por meio do debate de ideias.
- **Etapa 2:** A polarização afetiva, turbinada por algoritmos que lucram com emoções viscerais, transporta a disputa do plano das ideias para o campo da aversão existencial entre "nós contra eles".
- **Etapa 3:** Quando o pertencimento de grupo se transforma em tribo moral e o adversário é demonizado, o compromisso democrático com a alternância pacífica no poder é implodido, abrindo espaço para a violência política e o autoritarismo.
""",
        # q49 (D)
        """<!-- id: q49 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: dificil | objeto: desinformacao-e-ataques-a-instituicoes-democraticas -->
### Questão 49
A disseminação contínua de desinformação organizada contra o sistema eleitoral e cortes superiores de justiça em países como Brasil e Estados Unidos nas eleições de 2020 e 2022 culminou em episódios de violência política e tentativas de golpe de Estado. A análise histórica desses eventos evidencia que:

a) As sedes dos poderes foram ocupadas por grupos de ambientalistas que protestavam contra o uso de sacolas plásticas em supermercados.
b) As invasões foram incentivadas por editoras de livros didáticos interessadas em ampliar a venda de compêndios de história da república.
c) Os participantes dos ataques recusavam o acesso a aparelhos celulares e redes sociais por fidelidade a princípios de isolamento tecnológico.
d) A desinformação repetida e planejada de que as urnas eram fraudadas corroeu a fé na legitimidade dos resultados eleitorais, mobilizando cidadãos radicalizados em bolhas a praticar atos de insurreição contra a ordem constitucional.
e) As forças de segurança internacional assumiram o controle das comissões eleitorais para refazer a apuração dos votos manuais.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** A integridade das eleições apoia-se na confiança pública compartilhada nas regras do jogo e nos órgãos constitucionais encarregados de conduzir o pleito.
- **Etapa 2:** Campanhas industriais de desinformação propagadas por líderes políticos em redes sociais semearam sistematicamente mentiras infundadas sobre fraudes eletrônicas para justificar derrotas nas urnas.
- **Etapa 3:** Confinados em câmaras de eco e alimentados por pânico conspiratório, milhares de indivíduos acreditaram sinceramente que estavam diante de um roubo cívico, marchando contra parlamentos e tribunais para tentar derrubar a democracia legítima.
""",
        # q50 (E)
        """<!-- id: q50 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: dificil | objeto: metodologia-historica-e-combate-ao-negacionismo -->
### Questão 50
Diante da avalanche contemporânea de negacionismos históricos difundidos na internet, historiadores reafirmam a centralidade da 'crítica documental' como método de salvaguarda da verdade factual. O rigor desse procedimento metodológico fundamenta-se no dever de:

a) Descartar qualquer documento histórico produzido antes da virada do século XX por desconfiança na grafia de tintas antigas.
b) Aceitar como verídica qualquer gravação em áudio compartilhada em grupos de mensagens que contenha declarações alarmistas.
c) Proibir o uso de acervos públicos digitais por pesquisadores que não pertençam a conselhos editoriais internacionais.
d) Submeter a redação de livros didáticos à revisão prévia de empresas proprietárias de aplicativos de redes sociais.
e) Interrogar sistematicamente a autenticidade, a procedência, os interesses do autor e o contexto das fontes materiais primárias, confrontando-as com o acervo empírico e o diálogo com os pares da comunidade científica.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** A ciência histórica não trabalha com crenças cegas ou opiniões puras, mas com evidências documentais (textos, fotos, relatos, ruínas) submetidas a uma checagem metódica e transparente.
- **Etapa 2:** A crítica das fontes analisa de onde vem o documento, com que intenção foi produzido, se foi adulterado e como ele se articula aos outros testemunhos da mesma época.
- **Etapa 3:** Esse método rigoroso é a barreira intransponível contra as fraudes do negacionismo: diante de documentos autênticos e análises colegiadas, mentiras políticas desmoronam por falta de base empírica e científica.
""",
        # q51 (A)
        """<!-- id: q51 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: dificil | objeto: gatekeepers-vs-curadoria-algoritmica -->
### Questão 51
A substituição da mediação jornalística profissional dos antigos *gatekeepers* pela curadoria automatizada dos algoritmos de recomendação gerou uma mutação cultural profunda no acesso à informação pública. Essa mudança caracteriza-se pelo fato de que:

a) Os critérios profissionais de apuração e responsabilidade ética foram substituídos por métricas matemáticas que valorizam o volume de engajamento, priorizando o sensacionalismo e enfraquecendo os filtros de qualidade factual.
b) As plataformas digitais aumentaram a contratação de jornalistas investigativos em todas as cidades do interior do país.
c) Os algoritmos foram configurados para banir de forma definitiva qualquer matéria com teor político polêmico da internet.
d) O público deixou de consumir notícias sobre o cotidiano urbano para consultar enciclopédias médicas em bibliotecas públicas.
e) Os veículos impressos tradicionais passaram a decidir as manchetes diárias com base no sorteio de cartas de baralho.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** Os porteiros editoriais da imprensa histórica eram seres humanos regidos por normas éticas e jurídicas: deveriam ouvir ambos os lados, checar dados e responder judicialmente por calúnias.
- **Etapa 2:** Os sistemas de recomendação das Big Techs, por outro lado, operam sem preocupação ética com a verdade: seu único objetivo é reter a atenção dos internautas para vender anúncios publicitários.
- **Etapa 3:** Ao premiar aquilo que mais choca ou inflama sem verificar a autenticidade factual, a curadoria algorítmica abriu as comportas para a viralização em massa de teorias da conspiração e desinformação descontrolada.
""",
        # q52 (B)
        """<!-- id: q52 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: dificil | objeto: zuboff-ameaca-a-autonomia-e-soberania-individual -->
### Questão 52
Ao concluir sua obra sobre o capitalismo de vigilância, Shoshana Zuboff alerta que a modificação de condutas por tecnologias digitais ameaça a própria 'autonomia individual' e a vontade livre que alicerçam o conceito ocidental de liberdade democrática. O argumento central dessa denúncia baseia-se na constatação de que:

a) As pessoas são impedidas de desligar seus telefones celulares durante as noites por decretos executivos federais.
b) Ao prever e manipular escolhas antes mesmo que o sujeito tenha consciência de seus desejos, os algoritmos expropriam o direito do indivíduo a um futuro aberto e imprevisível, subordinando a subjetividade ao controle de interesses corporativos.
c) As companhias de eletricidade desligam as torres de internet durante as madrugadas para economizar água nas barragens.
d) Os aparelhos computacionais passam a exigir identificação com documentos originais para cada mensagem de texto trocada entre familiares.
e) As empresas privadas determinam compulsoriamente os locais de trabalho e os casamentos dos cidadãos em suas cidades.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** A liberdade humana e a cidadania democrática pressupõem sujeitos capazes de refletir, fazer escolhas morais autônomas e decidir seus caminhos sem coerção externa.
- **Etapa 2:** Os dispositivos do capitalismo de vigilância cercam o indivíduo de estímulos personalizados contínuos que exploram reflexos psicológicos automáticos e inseguranças emocionais.
- **Etapa 3:** Ao domesticar comportamentos futuros em favor de compradores de publicidade, essas tecnologias usurpam a espontaneidade e a soberania do querer humano, transformando a autonomia em uma ilusão programada.
""",
        # q53 (C)
        """<!-- id: q53 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: dificil | objeto: polarizacao-afetiva-e-quebra-da-empatia -->
### Questão 53
Pesquisas sociológicas sobre redes digitais apontam que a dinâmica das bolhas algorítmicas não apenas limita o acesso a dados plurais, mas produz um efeito psicossocial de 'anestesia da empatia' e hostilidade crônica. Esse fenômeno fundamenta-se no fato de que:

a) Os usuários de celulares perdem a capacidade física de audição devido ao volume excessivo de notificações sonoras.
b) As comunidades virtuais proíbem qualquer tipo de conversa entre pessoas com idades diferentes em redes públicas.
c) O confinamento prolongado em ambientes onde todos pensam igual estimula a intolerância com qualquer divergência mínima, transformando o outro em alvo aceitável de linchamentos morais e discursos odiosos.
d) As empresas operadoras de telefonia subsidiam a matrícula de estudantes em cursos de oratória e conciliação jurídica.
e) O convívio nas plataformas virtuais elimina as desconfianças históricas entre povos que disputavam fronteiras continentais.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** A convivência democrática exige exercitar a empatia: a capacidade de se colocar no lugar do diferente e compreender que divergências de opinião não anulam a humanidade do outro.
- **Etapa 2:** Nas câmaras de eco, o grupo se fecha em uma autoimagem de virtude moral absoluta e projeta sobre o restante da sociedade uma imagem caricata e desprezível.
- **Etapa 3:** A perda do contato com a alteridade gera radicalização: quando o indivíduo acredita que sua tribo é a única guardiã do bem, a empatia com o adversário se dissipa, legitimando agressões e linchamentos digitais.
""",
        # q54 (D)
        """<!-- id: q54 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: dificil | objeto: pos-verdade-e-cinismo-epistemologico -->
### Questão 4
Na análise filosófica da pós-verdade, autores contemporâneos destacam que o objetivo fundamental dos propagadores industriais de desinformação não é necessariamente convencer o público de que uma mentira específica é verdadeira, mas sim disseminar o cinismo generalizado. Esse cinismo produz efeitos políticos devastadores ao:

a) Obrigar todas as escolas do país a adotar cadernos sem pauta em avaliações escritas de redação.
b) Convencer a população de que todas as vacinas infantis são inteiramente gratuitas em unidades de saúde pública.
c) Fazer com que as cortes de justiça encerrem seus trabalhos judiciais às sextas-feiras nos meses de verão.
d) Fazer os cidadãos acreditarem que todos mentem, que a verdade factual não existe e que é impossível conhecer os fatos com precisão, levando à apatia cívica e à submissão a lideranças autoritárias.
e) Estimular os eleitores a votar massivamente em partidos tradicionais que defendam a reforma no código de trânsito.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** A desinformação sofisticada moderna frequentemente lança dezenas de versões contraditórias sobre o mesmo acontecimento (como se viu no caso de crimes políticos e guerras).
- **Etapa 2:** A meta central dessa saturação não é fazer com que todos acreditem na mesma mentira, mas sim exaurir a capacidade crítica do cidadão, que desiste de buscar a verdade perante tantas narrativas opostas.
- **Etapa 3:** Instalado o cinismo ("todos mentem, nada é real"), o cidadão abandona a participação informada e passa a votar ou agir apenas por fidelidade cega e emotiva ao seu líder populista, destruindo os alicerces da democracia.
""",
        # q55 (E)
        """<!-- id: q55 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: dificil | objeto: negacionismo-historico-como-fraude-politica -->
### Questão 55
Ao investigar a ascensão de correntes negacionistas contemporâneas na Europa e nas Américas, historiadores demonstram que essas narrativas não constituem um fenômeno acadêmico espontâneo, mas sim uma tecnologia de propaganda política que:

a) Traduz manuscritos medievais latinos para disponibilizá-los em plataformas de acesso aberto na internet.
b) Organiza viagens de intercâmbio cultural para que alunos visitem ruínas arqueológicas em áreas preservadas.
c) Cria museus dedicados a documentar o desenvolvimento de ferrovias nas regiões de colonização antiga.
d) Financia projetos de pesquisa independentes sobre a evolução da arquitetura colonial nas capitais litorâneas.
e) Falsifica intencionalmente o passado para destruir consensos éticos básicos da humanidade (como a proibição da tortura e do genocídio), normalizando práticas autoritárias e racistas no presente.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** O negacionismo histórico não é um debate teórico honesto; trata-se de um instrumento de guerra ideológica desenhado para retirar o opróbrio moral de regimes e crimes desumanos.
- **Etapa 2:** Ao negar que houve câmaras de gás na Alemanha nazista ou que houve torturas em celas da ditadura brasileira, essas narrativas buscam rehabilitar as ideologias autoritárias que cometeram essas atrocidades.
- **Etapa 3:** Ao desmoralizar a memória coletiva e as vítimas do passado, o negacionismo prepara o terreno para que a violência política, a perseguição e a supressão de direitos voltem a ser vistas como soluções legítimas no presente.
""",
        # q56 (A)
        """<!-- id: q56 | tipo: multipla-escolha | habilidade: EM13CHS101 | dificuldade: dificil | objeto: transicao-broadcast-redes-economia-de-plataforma -->
### Questão 56
A transição do modelo analógico de comunicação de massas para a era da economia de plataformas reconfigurou as relações de poder na cultura contemporânea. No que tange à circulação de saberes e à autonomia dos sujeitos, esse processo resultou:

a) Na ilusão de uma horizontalidade perfeita que escondeu uma nova e feroz concentração oligopólica do poder nas mãos de Big Techs globais, cujas arquiteturas invisíveis de código decidem quem fala, o que é visto e o que é silenciado.
b) Na democratização definitiva de todos os meios de produção com eliminação completa de intermediários comerciais de notícias.
c) Na proibição legal da veiculação de mensagens com fins lucrativos em telefones celulares nos países em desenvolvimento.
d) Na devolução da totalidade dos recursos gerados pela publicidade online às cooperativas de artistas plásticos locais.
e) Na substituição de todos os satélites de comunicação por redes subterrâneas de cabos trançados de cobre.

**Gabarito:** A

**Resolução Detalhada:**
- **Etapa 1:** A internet inicial dos anos 1990 e a Web 2.0 foram celebradas como promessas de autonomia: cada cidadão seria um comunicador sem chefes ou monopólios midiáticos.
- **Etapa 2:** A evolução histórica das últimas duas décadas, contudo, concentrou a quase totalidade do fluxo informativo em meia dúzia de megaplataformas privadas que dominam as redes e o mercado de publicidade.
- **Etapa 3:** Essa concentração criou um poder sem precedentes: sem passar por escrutínio democrático ou eleições, executivos dessas empresas e seus algoritmos regulam a comunicação planetária, definindo as regras do discurso social.
""",
        # q57 (B)
        """<!-- id: q57 | tipo: multipla-escolha | habilidade: EM13CHS106 | dificuldade: dificil | objeto: capitalismo-vigilancia-e-soberania-politica -->
### Questão 57
Na análise de Shoshana Zuboff, o perigo que o capitalismo de vigilância impõe às sociedades contemporâneas não se restringe à esfera do consumo comercial, mas afeta a própria soberania política e o autogoverno coletivo porque:

a) As empresas de satélite desativam o sinal de televisão aberta durante os meses de férias escolares.
b) O conhecimento preditivo e a capacidade de modificar condutas em massa concedem às corporações digitais um poder desregulamentado de gestão social que compete com os próprios governos e enfraquece o controle democrático popular.
c) As companhias de telecomunicação assumem formalmente a administração das forças armadas de nações soberanas.
d) Os aparelhos móveis passam a cobrar tributos alfandegários automáticos sobre compras em feiras de artesanato.
e) As cooperativas agrícolas perdem o direito de comercializar sacas de café em bolsas internacionais de mercadorias.

**Gabarito:** B

**Resolução Detalhada:**
- **Etapa 1:** As democracias modernas foram construídas sob a premissa de que a soberania emana do povo, expressa por meio de governantes eleitos e leis votadas em parlamentos públicos.
- **Etapa 2:** O capitalismo de vigilância acumulou um poder sem precedentes na história: a capacidade de rastrear a vida de bilhões de pessoas e influenciar seus sentimentos e votos sem qualquer controle da sociedade.
- **Etapa 3:** Esse poder privado gigantesco opera acima dos Estados e das fronteiras nacionais, esvaziando a capacidade das comunidades democráticas de decidirem autonomamente seus destinos e subordinando o bem comum ao lucro algorítmico.
""",
        # q58 (C)
        """<!-- id: q58 | tipo: multipla-escolha | habilidade: EM13CHS504 | dificuldade: dificil | objeto: bolhas-informacionais-e-radicalizacao-politica -->
### Questão 58
Estudos sobre o percurso de radicalização de indivíduos em redes sociais indicam que a arquitetura dos sistemas de recomendação conduz frequentemente usuários curiosos a conteúdos progressivamente extremistas. Esse processo de atração algorítmica apoia-se no fato de que:

a) Os computadores são programados para exibir apenas poesias clássicas aos internautas que navegam à noite.
b) As plataformas reduzem o preço da conexão de internet para aqueles que assistirem a aulas completas de sociologia.
c) Para manter a atenção do usuário por mais tempo e garantir que ele não mude de aplicativo, os algoritmos oferecem sugestões que elevam o teor de choque, conspiração e indignação a cada novo clique na trilha de vídeos.
d) Os provedores de internet fecham as contas de usuários que não compartilharem pronunciamentos sindicais.
e) O consumo de informações moderadas e equilibradas gera cobrança adicional em faturas de operadoras de telefonia.

**Gabarito:** C

**Resolução Detalhada:**
- **Etapa 1:** O algoritmo de recomendação aprende continuamente com o tempo de permanência do usuário na tela e com o que ele clica a seguir para não deixá-lo sair.
- **Etapa 2:** Como conteúdos ordinários e ponderados perdem o poder de atração rapidamente, o sistema oferece opções com doses mais altas de sensacionalismo, teorias conspiratórias e discursos de ódio.
- **Etapa 3:** Esse funil de radicalização empurra o indivíduo de vídeos inofensivos sobre saúde ou curiosidades para conteúdos conspiratórios graves e grupos extremistas, gerando uma radicalização que transborda para o mundo físico.
""",
        # q59 (D)
        """<!-- id: q59 | tipo: multipla-escolha | habilidade: EM13CHS603 | dificuldade: dificil | objeto: letramento-midiatico-como-politica-publica -->
### Questão 59
No campo das políticas públicas de educação para a cidadania no século XXI, a inserção do Letramento Midiático e Informacional (*Media Literacy*) no currículo escolar, conforme preconizado pela BNCC, justifica-se como estratégia prioritária porque:

a) Garante que todas as escolas públicas substituam bibliotecas de livros impressos por laboratórios de manutenção de placas de vídeo.
b) Determina que os alunos devem aprender técnicas de conserto mecânico de aparelhos de televisão e rádio transistorizado.
c) Proíbe que jovens com menos de dezoito anos acessem ferramentas de busca na internet durante o período letivo.
d) Capacita as novas gerações a analisar de forma crítica as mensagens recebidas, desvendar mecanismos algorítmicos, verificar a autenticidade de fontes e exercer sua cidadania digital com responsabilidade ética.
e) Obriga as crianças a se cadastrarem em conselhos municipais de fiscalização do tráfego de cargas pesadas nas estradas.

**Gabarito:** D

**Resolução Detalhada:**
- **Etapa 1:** A cultura digital contemporânea colocou um volume imenso de dados e desinformações na palma da mão dos jovens através de celulares conectados.
- **Etapa 2:** A simples habilidade técnica de mexer em aplicativos não significa capacidade crítica de leitura: navegar na internet sem critérios torna o estudante refém fácil de fraudes, golpes e discursos extremistas.
- **Etapa 3:** O letramento midiático ensina a pensar sobre a informação: avaliar quem financia o conteúdo, conferir dados em outras fontes e refletir antes de compartilhar, construindo a imunidade cognitiva e a responsabilidade cidadã no século XXI.
""",
        # q60 (E)
        """<!-- id: q60 | tipo: multipla-escolha | habilidade: EM13CHS606 | dificuldade: dificil | objeto: memoria-justica-e-defesa-democratica -->
### Questão 60
A articulação entre a preservação da memória histórica, a afirmação da verdade factual e a defesa das instituições republicanas diante dos negacionismos e da pós-verdade expressa o dever cívico da sociedade democrática no século XXI. Essa diretriz consolida-se na compreensão de que:

a) A história ensinada nas escolas deve desconsiderar conflitos e violências do passado para manter a coesão nacional.
b) As decisões dos tribunais e os registros de arquivos públicos devem ser revistos e adaptados periodicamente às preferências dos governantes de plantão.
c) Os direitos fundamentais dos cidadãos devem ser suspensos sempre que houver divergências ideológicas sobre projetos de desenvolvimento econômico.
d) A defesa da liberdade de expressão legitima a criação de empresas dedicadas à venda profissional de mentiras e discursos conspiratórios em períodos eleitorais.
e) Conhecer e respeitar a verdade histórica documentada sobre violências passadas é o pilar inegociável da justiça, da dignidade humana e da garantia de que o terrorismo de Estado e a barbárie jamais voltem a acontecer.

**Gabarito:** E

**Resolução Detalhada:**
- **Etapa 1:** A memória não é mero depósito do que passou; ela é a bússola ética que orienta as decisões presentes e a construção do futuro de uma sociedade democrática.
- **Etapa 2:** Os negacionismos históricos tentam relativizar os crimes contra a humanidade, abrindo espaço para que discursos de ódio e perseguições sejam normalizados novamente nas instituições.
- **Etapa 3:** Por conseguinte, defender a verdade factual, ensinar as dores e lutas da história e honrar a memória dos perseguidos e violentados pelo autoritarismo é o compromisso inegociável para garantir: ditadura nunca mais, barbárie nunca mais.
"""
    ]

    references_section = """
## Referências

- ABRIL, Florisbal de Souza; D’INCAO, Maria Angela (Orgs.). *A Esfera Pública Digital*. São Paulo: Hucitec, 2021.
- BRASIL. *Lei nº 12.965, de 23 de abril de 2014*. Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil (Marco Civil da Internet). Brasília: Presidência da República, 2014.
- BRASIL. Ministério da Educação. *Base Nacional Comum Curricular: Educação é a Base*. Brasília: MEC/SEB, 2018.
- D’ANCONA, Matthew. *Pós-Verdade: A Nova Guerra contra os Fatos em Tempos de Fake News*. Barueri: Faro Editorial, 2018.
- HABERMAS, Jürgen. *Mudança Estrutural da Esfera Pública*. São Paulo: Editora Unesp, 2014.
- NAPOLITANO, Marcos. *Negacionismo Histórico: A Falsificação do Passado*. In: SOUZA, Jessé (Org.). *O Brasil no Espelho dos Fatos*. São Paulo: Boitempo, 2020.
- PARISER, Eli. *O Filtro Invisível: O que a Internet Está Escondendo de Você*. Rio de Janeiro: Zahar, 2012.
- ROUVROY, Antoinette; BERNS, Thomas. *Governamentalidade Algorítmica e Perspectivas de Emancipação*. Eco-Pós, Rio de Janeiro, v. 18, n. 2, p. 36-56, 2015.
- ZUBOFF, Shoshana. *A Era do Capitalismo de Vigilância: A Luta por um Futuro Humano na Nova Fronteira do Poder*. Rio de Janeiro: Intrínseca, 2021.
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
    draft_path = os.path.join(project_root, "temp_draft_c54.md")

    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Draft c54 generated with {len(content)} characters at {draft_path}")

if __name__ == "__main__":
    build_draft_c54()
