# 🚀 Plano de Execução Mestre — Educamob Escola Digital

> **Planejador Estratégico** · Atualizado: 2026-11-05. **Muro de Contenção Geral Universal Homologado no `validador_educamob.py`**: Motor de Pareamento Teórico Universal (Princípio do Mundo Fechado / Closed-World Boundary com suporte a múltiplos e-books e tratamento de epônimos compostos), Trava Sistêmica de Balanceamento Obrigatório de Gabarito (~20% por letra de A a E, tolerância 8 a 16 e anti-repetição viciada), Trava Anti-Decoreba e Expansão da Blacklist de Jargões Universitários. **100% DAS 436 LISTAS DE EXERCÍCIOS DO REPOSITÓRIO HOMOLOGADAS E SINCRONIZADAS NO PGVECTOR (26.160 QUESTÕES ATÔMICAS ATIVAS)**:
> - **Ciências (5º ao 9º Ano):** 72/72 listas homologadas e indexadas ✅ (4.320 questões).
> - **Geografia (5º ao 9º Ano):** 40/40 listas homologadas e indexadas ✅ (2.400 questões).
> - **História (5º ao 9º Ano):** 62/62 listas homologadas e indexadas ✅ (3.720 questões).
> - **Língua Portuguesa (5º ao 9º Ano):** 75/100 listas homologadas (4.500 questões no Padrão-Ouro e Linguagem Adequada — 5º, 6º e 7º Anos 100% Concluídos [60/60 listas]; 8º Ano em 75% [15/20 listas]) ⏳.
> - **Matemática (Fundamental 1, Fundamental 2 e Médio):** 148/148 listas homologadas e indexadas ✅ (8.880 questões).
> - **Física (Ensino Médio):** 61/61 listas homologadas e indexadas ✅ (3.660 questões).
> - **Química (Ensino Médio):** 53/53 listas homologadas e indexadas ✅ (3.180 questões).
> **Fase 5 & Fase 6 Concluídas:** Acervo integral de teoria (585 e-books / 26.704 chunks) e exercícios (436 listas / 26.160 questões / ~23.500 chunks) 100% vetorizado e ativo via Supabase pgvector com índice HNSW para o ecossistema Mob.me e Revisa.

---

## Arquitetura Unificada (O "Grande Quadro")

Para garantir um ecossistema sem fragmentação de dados e com inteligência centralizada, **toda a plataforma (Dashboard, SPAs, Revisa e Mob.me) utiliza o Supabase** como espinha dorsal de Autenticação e Banco de Dados.

**O Ciclo de Vida do Aluno e da Família:**
1. O aluno faz o **Login via Supabase Auth**.
2. Ele resolve um **SPA** ou um teste do **Revisa** no GitHub Pages.
3. O GitHub Pages salva a nota dele e o histórico nas tabelas do **Supabase**.
4. Ele vai para o **Mob.me**. O backend em Python (FastAPI) puxa a "Memória do Aluno" do **Supabase** (que agora engloba as notas recentes dos SPAs somadas a **todo o histórico de conversas anteriores que o estudante teve com o próprio Mob.me**) e constrói um *contexto completo* dos estudos. Assim, a IA ajusta a didática sabendo exatamente o perfil, as dificuldades e as vitórias do aluno.
5. **Contato Sob Demanda (Famílias):** Não há uso de n8n. O contato é *pull*, não *push*. Caso a família queira saber como está o andamento dos estudos, ela envia uma mensagem de WhatsApp. O sistema de IA consulta as tabelas do **Supabase** e envia uma resposta precisa com o relatório de desempenho do aluno.
   > **🔮 Visão de Futuro (Mensagens Push Semanais):** É tecnicamente muito simples transformar esse modelo em *push* (ativo) no futuro. Como todos os dados e contatos estão centralizados no Supabase, basta criarmos uma rotina agendada (Cron Job) no nosso backend Python. Toda sexta-feira às 18h, por exemplo, o script varre o banco, a IA redige os resumos, e dispara via API de WhatsApp para cada família automaticamente.

## ⚠️ Integração SaaS: Pagamentos ↔ Supabase (Como as vendas dialogam com os acessos?)
Para que o seu sistema de vendas (seja WIX, Hotmart, Kiwify, Stripe ou Asaas) converse perfeitamente com a plataforma educacional (Supabase Auth), a arquitetura é totalmente agnóstica (independente de plataforma). O fluxo funciona assim:
1. A família entra na sua página de vendas (WIX, Link de Checkout, etc) e realiza o pagamento.
2. Qualquer gateway moderno de pagamento, ao aprovar a compra, permite cadastrar um **Webhook**. Esse webhook dispara um aviso silencioso para a nossa API em Python (FastAPI).
3. A nossa API recebe os dados brutos da compra (Nome, E-mail, Telefone) e **cria automaticamente a conta do aluno no Supabase Auth**, registrando o telefone da família nas tabelas.
4. O aluno recebe um e-mail com o link do Portal e uma senha (ou Magic Link) para entrar.
5. Se a assinatura for cancelada ou não paga no seu gateway de pagamentos, outro webhook avisa a nossa API, que bloqueia instantaneamente o acesso no Supabase.
*(O processo é universal e 100% no piloto automático, independente de qual solução financeira você escolher usar).*

---

## Faseamento Atualizado

### 🟢 Fase 1 — Fundações e Primeiros Apps [CONCLUÍDO]
| Sprint | Módulo | Status |
|--------|--------|--------|
| **0** | Estrutura completa + Design System + Componentes | ✅ Feito |
| **1** | Biblioteca de SPAs (funcional) | ✅ Feito |
| **2** | Chat Tutor (Frontend Mob.me) | ✅ Feito |

### 🔵 Fase 2 — Ferramentas de Estudo e Analytics Local [CONCLUÍDO]
| Sprint | Módulo | Status |
|--------|--------|--------|
| **3** | Biblioteca de Exercícios (Revisa) | ✅ Feito |
| **4** | Dashboard de Desempenho (Meu Desempenho) | ✅ Feito (UX Premium) |
| **5** | Hub de Lives | 🚧 Pendente |

### 🟠 Fase 3 — Integração Global Cloud (Supabase) [CONCLUÍDO]
> Conexão do front-end estático (GitHub Pages) ao banco de dados que alimenta a IA do Mob.me.

| Sprint | Módulo | Tokens Est. | Status |
|--------|--------|-------------|--------|
| **6** | Autenticação de Usuários (Supabase Auth) | ~10k | ✅ Feito |
| **7** | Sincronização de Banco de Dados (SPAs e Revisa no PostgreSQL) | ~15k | ✅ Feito |

### 🔴 Fase 4 — Inteligência Artificial & Automações (Python / FastAPI)
> O momento em que o cérebro da operação ganha vida no Backend.

| Sprint | Módulo | Tokens Est. | Status |
|--------|--------|-------------|--------|
| **8** | Backend Mob.Me (RAG, Histórico de Conversas, Respostas via Gemini + **Otimização de Latência e Fallback**) | ~20k | ✅ Feito |
| **9** | **Agente WhatsApp de Famílias** (Consulta sob demanda do desempenho via Z-API/Evolution API ligada ao FastAPI) | ~15k | ✅ Feito |
| **10** | Webhooks WIX (Criação automática de contas após a venda) | ~8k | 🚧 Pendente |

---

## Sprint 8 — Backend Mob.Me (IA, Streaming e High Availability) (Fase 4)

> **Status:** ✅ Concluído.  
> **Entregas Técnicas Realizadas:**
> 1. **Otimização Extrema de Latência (Streaming):** Substituição do retorno em bloco por `StreamingResponse` no FastAPI e leitura de `ReadableStream` no Next.js, gerando efeito de digitação em tempo real (reduziu a percepção de latência de 10s para <1s).
> 2. **Remoção de Gargalos Bloqueantes:** Supabase DB operations movidas para `Background Tasks` assíncronas em Python (`asyncio`).
> 3. **High Availability & Fallback:** Resiliência contra o erro 503 do Google implementando fallback nativo para `gemini-2.0-flash`. (Roteamento Multi-Provedor com OpenAI em backlog).
> 4. **UX Responsivo (Frontend Next.js):** Reconstrução completa do frontend SPA Mob.me em **Next.js (TailwindCSS)** após perda do código original, restaurando 100% da estética original. Correção definitiva do bug no mobile onde o teclado virtual bloqueava o botão de envio (resolvido através da semântica nativa `<form type="submit">`), e substituição de `crypto.randomUUID()` por `Date.now()` para plena compatibilidade mobile fora do HTTPS.
> 5. **Concorrência e RAG Assíncrono:** Substituição do `DeepInfraEmbeddings` bloqueante da biblioteca Langchain por chamadas nativamente assíncronas (`httpx`) conectando a interface `OpenAIEmbeddings` direto ao RPC do Supabase, derrubando a fila do Python e estabilizando a performance de RAG em cenários de stress intenso (50+ chamadas simultâneas). O gargalo final (13s) provou-se restrito unicamente à cota concorrente (rate-limit) da API Gemini.
> 6. **Injeção Dinâmica de Matérias e Guardião RAG:** Implementada barreira sistêmica no `main.py` e nos prompts para bloquear alucinações sobre disciplinas inexistentes. O backend lê dinamicamente da tabela `available_subjects` e injeta a lista no prompt do sistema. O `ingest.py` foi refatorado para operar de forma inteligente (Idempotente) usando hash local, zerando tempo e custo na inserção de novos conteúdos e excluindo automaticamente duplicatas do banco vetorial.

---

## Sprint 6 — Autenticação de Usuários (Fase 3)

> **Status:** ✅ Concluído.  
> O sistema agora conta com uma barreira global intransponível. Apenas alunos logados conseguem acessar os SPAs, Biblioteca e Dashboard.

---

## Sprint 7 — Sincronização Banco de Dados (Fase 3)

> **Prioridade:** 🔴 Crítica  
> **Status Atual:** ✅ Concluído. (Tabela `student_progress` criada e sincronização bidirecional operando via Supabase Client).

**Objetivo:** Persistir notas e interações na nuvem para uso da Inteligência Artificial (FastAPI/WhatsApp).

### Tarefas:
1. **Modelagem de Dados:** Criar no Supabase uma tabela (`student_progress`) para registrar `user_id`, `subject_id`, `score`, `timestamp` e `tipo` (SPA ou Revisa). *Ação requerida do usuário via SQL.*
2. **Upload (Gravação):** Refatorar o `shared/js/quiz.js`. Ao clicar em "Corrigir" ou "Finalizar", os dados são persistidos via inserção SQL no Supabase, abandonando a dependência do `localStorage`.
3. **Download (Leitura):** Refatorar o `shared/js/dashboard.js`. O painel fará um `SELECT` no Supabase filtrando pelo ID do aluno logado, populando a tabela em tempo real de qualquer dispositivo.

---

## Sprint 9 — Agente WhatsApp de Famílias (Fase 4)

> **Status:** ✅ Concluído.  
> **Entregas Técnicas Realizadas:**
> 1. **Setup de Infraestrutura Cloud:** Provisionamento de servidor Oracle ARM64 e deploy da Evolution API (versão 2.3.7 do Baileys para sanar incompatibilidades).
> 2. **Integração Webhook via Docker:** Conexão direta e segura do `mobme-api` e `evolution-api` através da rede interna do Docker, otimizando latência e segurança. Configuração de Webhooks globais para repassar eventos `MESSAGES_UPSERT`.
> 3. **Cérebro Analítico:** O webhook recebe o JID (telefone) e cruza os dados na tabela `users` do Supabase para verificar a identidade. O histórico escolar do aluno é analisado pela LLM (Gemini 1.5) e respondido em texto Socrático e Acolhedor.
> 4. **Resolução de Gargalos:** Adequação do payload de envio para o padrão V2 da Evolution API (substituição de `textMessage` por `text`) e desativação de webhooks redundantes para garantir envio em lote unitário e perfeito.

---

## 📚 Fase 5 — Produção de Conteúdos Educacionais [NOVO]

> **Objetivo:** Construir toda a base de conhecimento que alimenta os SPAs interativos e o tutor Mob.me. Ordem de execução rígida: Pesquisa → E-book → SPA.
>
> **Escopo Inicial:**
> - **Matemática** — Todas as séries (5º ao 9º Fundamental + 1ª a 3ª série do Ensino Médio)
> - **Física** — Ensino Médio (1ª a 3ª série) + ENEM
> - **Química** — Ensino Médio (1ª a 3ª série) + ENEM
>
> **Volume Estimado:** ~830 arquivos `.md` (4º EF ao 3º EM + ENEM, todas as disciplinas do escopo). Este número impacta diretamente o faseamento: os Sprints 12 e 13 **não são entregas únicas** — são **processos cíclicos e incrementais** que serão executados repetidamente ao longo de meses, 1 Objeto de Conhecimento por vez.
>
> **Bússolas Normativas:**
> - **BNCC (Base Nacional Comum Curricular)** → Âncora para todas as séries do Ensino Fundamental e Médio
> - **Matriz de Habilidades do INEP** → Âncora para todos os conteúdos voltados ao ENEM
>
> **Regra de Ouro Arquitetural:** Granularidade e Especialização.
> - **E-books** são blocos **atômicos e 100% teóricos**: `1 E-book = 1 Objeto de Conhecimento da BNCC`. Servem como Base de Conhecimento (RAG).
> - **Listas de Exercícios** são arquivos separados (`[objeto]-exercicios.md`) com 60 questões tagueadas HTML (20 básicas, 20 intermediárias, 20 difíceis).
> - **SPAs** são blocos **focados em microaprendizagem**: `1 SPA = 1 Objeto de Conhecimento`. Articula o e-book teórico + 30 exercícios selecionados (10 de cada nível). Duração aproximada de 100 minutos.
> - O SPA **NÃO é 100% offline**. Ele se conecta ao Supabase Client para persistir telemetria granular (`habilidade`, `dificuldade`, `objeto`).
>
> **Ciclo Completo da Plataforma:**
> 1. Aluno acessa o **SPA** (que articula 1 Objeto de Conhecimento teórico) e responde aos quizzes (selecionados da lista de 60 exercícios).
> 2. O SPA (ou `quiz.js`) envia o desempenho detalhado (`habilidade`, `dificuldade`, `objeto`) para o **Supabase** (`student_progress`).
> 3. Aluno vai ao **Mob.me**. O backend lê o histórico (`objeto`) no Supabase e usa o E-book correspondente (RAG) para explicar a teoria, ou sugere resolver até 15 exercícios restantes do arquivo `-exercicios.md`. Caso esses 15 se esgotem, o Mob.me poderá criar questões inéditas sob demanda.
> 4. O **Revisa** utiliza 15 exercícios restantes (5 de cada nível, não selecionados pelo SPA nem pelo Mob.me) para compor o banco de questões e evitar repetição.
> 5. **Agente WhatsApp** consulta a mesma tabela e envia relatório aos pais.
>
> **Rastreabilidade de Design — Cada seção do `.md` tem consumidor(es) no ecossistema:**
>
> | Seção | Mob.me (IA/RAG) | SPA (Microaprendizagem) | Revisa (Banco de Questões) |
> |---|---|---|---|
> | Frontmatter (E-book) | Busca arquivo por série/objeto | — | Seleciona tópicos por série |
> | Conceitos / Exemplos | Fundamenta respostas / deduções | Texto base de leitura do SPA | — |
> | Erros Comuns | Corrige o aluno proativamente | Base para criar distratores no SPA | — |
> | Resumo para Revisão | Sintetiza respostas rápidas | Conteúdo de fechamento | — |
> | **Arquivo: 60 Exercícios** | Sugere prática adicional (15 exc) + Inéditas sob demanda | Extrai 30 exercícios (10 de cada nível) | Extrai 15 exercícios (5 de cada nível) |

### Sprint 11 — Protocolo de Pesquisa Bibliográfica ✅ Concluído

> **Status:** ✅ Concluído.  
> **Complexidade:** 🔴 Alta  
> **Skill a acionar:** Execução Direta (Planejador Estratégico + Pesquisa Web)  
> **Pré-requisitos:** Nenhum

**Objetivo:** Criar o **protocolo padrão e replicável** de pesquisa de conteúdos em fontes confiáveis. 
**Regras de Ouro:**
1. Os arquivos base da BNCC e Matriz ENEM INEP devem ser os que estão na **pasta oficial do projeto**. NUNCA fazer essa busca online.
2. Cada e-book deverá conter ao menos **5 fontes distintas**.

**Entregas Esperadas:**

#### Entrega 1 — Documento-Protocolo (`protocolo_pesquisa_bibliografica.md`)

Contendo:
- Template de ficha bibliográfica **por Objeto de Conhecimento** (título, código da habilidade BNCC/INEP mapeada, fonte primária, fonte secundária, palavras-chave, nível cognitivo Bloom)
- Critérios de validação de fonte (autoria, atualização, alinhamento curricular)
- Fluxo operacional passo a passo: Como pesquisar → Como validar → Como documentar → Como entregar ao E-book Creator
- Regras de uso de PDFs próprios (livros do acervo pessoal) como fonte complementar
- Protocolo de Garantia de Veracidade (7 critérios obrigatórios por informação factual):
  1. Fonte identificada — autor, instituição, URL rastreável
  2. Triangulação — confirmada em ≥ 5 fontes independentes
  3. Atualidade — dados de ≤ 5 anos (exceto clássicos/históricos)
  4. Autoridade — autor com credenciais na área
  5. Revisão por pares — preferencialmente de periódico/repositório com revisão
  6. **Validação pelo Agente Validador Acadêmico** (substitui revisão humana — ver Entrega 5)
  7. Referenciamento ABNT — citação no texto + lista de referências

**Banco de Fontes Hierarquizado:**

**🟢 Nível 1 — Fontes Oficiais Governamentais (Máxima Confiabilidade):**

| Fonte | URL | Uso |
|---|---|---|
| BNCC Oficial | http://basenacionalcomum.mec.gov.br/ | ✅ Referência obrigatória |
| Domínio Público (MEC) | http://www.dominiopublico.gov.br/ | ✅ Livre |
| EduCAPES | https://educapes.capes.gov.br/ | ✅ Verificar CC por obra |
| MEC RED | https://plataformaintegrada.mec.gov.br/ | ✅ Verificar por recurso |
| INEP | https://www.gov.br/inep/ | ✅ Dados abertos |
| IBGE | https://www.ibge.gov.br/ | ✅ Dados abertos |
| Provas ENEM anteriores | https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem | ✅ Documento público |
| OBMEP | https://www.obmep.org.br/ | ✅ Material público |
| Currículo Nacional (Portugal) | https://www.dge.mec.pt/ | ✅ Referência comparativa lusófona |

**🔵 Nível 2 — Fontes Acadêmicas Revisadas por Pares:**

*🌎 Américas (Brasil + EUA):*

| Fonte | URL | Uso |
|---|---|---|
| SciELO Brasil | https://www.scielo.br/ | ✅ CC-BY |
| Portal Periódicos CAPES | https://www.periodicos.capes.gov.br/ | ✅ Verificar |
| Repositório USP | https://repositorio.usp.br/ | ✅ Verificar por obra |
| Repositório UNICAMP | https://repositorio.unicamp.br/ | ✅ Verificar por obra |
| LUME (UFRGS) | https://lume.ufrgs.br/ | ✅ Verificar por obra |
| BDTD | https://bdtd.ibict.br/ | ✅ Verificar |
| arXiv | https://arxiv.org/ | ✅ Preprints (Física/Matemática) — cruzar com publicação revisada |
| PubMed Central | https://www.ncbi.nlm.nih.gov/pmc/ | ✅ Artigos biomédicos — útil para Química/Ciências |
| ERIC | https://eric.ed.gov/ | ✅ Pesquisa educacional internacional |
| MIT OpenCourseWare | https://ocw.mit.edu/ | ✅ CC-BY-NC-SA — referência de abordagem para Física/Matemática |
| PhET Simulations (CU Boulder) | https://phet.colorado.edu/pt_BR/ | ✅ CC-BY — simuladores interativos (descrição em texto) |
| OpenStax (Rice University) | https://openstax.org/ | ✅ CC-BY — livros-texto completos e gratuitos de Matemática, Física, Química |

*🌍 Europa:*

| Fonte | URL | Uso |
|---|---|---|
| HAL (França) | https://hal.science/ | ✅ Arquivo aberto multidisciplinar francês — forte em Matemática e Física |
| CORE (Reino Unido) | https://core.ac.uk/ | ✅ Agregador de ~300M artigos open access de repositórios europeus |
| EuDML (Biblioteca Digital Europeia de Matemática) | https://eudml.org/ | ✅ Acervo digitalizado de periódicos europeus clássicos de Matemática |
| Europeana | https://www.europeana.eu/ | ✅ Patrimônio cultural e científico europeu — dados históricos e iconografia |
| Nuffield Foundation (Reino Unido) | https://www.nuffieldfoundation.org/ | ✅ Pesquisa educacional em STEM — referência de abordagem didática |
| RCAAP (Portugal) | https://www.rcaap.pt/ | ✅ Repositórios científicos de acesso aberto de Portugal — conteúdo em português |
| Numdam (França) | https://www.numdam.org/ | ✅ Digitalização de periódicos franceses de Matemática — acervo histórico e moderno |

*🌏 Ásia:*

| Fonte | URL | Uso |
|---|---|---|
| J-STAGE (Japão) | https://www.jstage.jst.go.jp/ | ✅ Periódicos acadêmicos japoneses — forte em Química e Engenharia (muitos artigos em inglês) |
| KISTI (Coreia do Sul) | https://www.kisti.re.kr/eng/ | ✅ Instituto de Ciência e Tecnologia — dados e pesquisa em STEM |
| CAS (Academia Chinesa de Ciências) | https://english.cas.cn/ | ✅ Publicações em Física e Química — referência para abordagens experimentais |
| NII (Instituto Nacional de Informática, Japão) | https://www.nii.ac.jp/en/ | ✅ Pesquisa em ciência da computação e informática educacional |
| Indian Academy of Sciences | https://www.ias.ac.in/ | ✅ Periódicos revisados de Física, Química e Matemática — acesso aberto |
| KOCW (Korea OpenCourseWare) | http://www.kocw.net/ | ✅ Cursos abertos universitários coreanos — referência de estrutura didática em STEM |

**🟡 Nível 3 — Referência Pedagógica (Inspiração, NÃO cópia):**

| Fonte | URL | Uso permitido |
|---|---|---|
| Khan Academy Brasil | https://pt.khanacademy.org/ | ❌ CC-NC — usar como referência de abordagem, não copiar |
| Nova Escola | https://novaescola.org.br/ | ⚠️ Consultar estrutura de planos de aula |
| Escola Digital | https://escoladigital.org.br/ | ⚠️ Referência de curadoria |
| GeoGebra | https://www.geogebra.org/ | ⚠️ CC-BY-NC-SA — referência para construções geométricas |
| Wolfram MathWorld | https://mathworld.wolfram.com/ | ⚠️ Referência matemática — cruzar com fonte primária |
| BBC Bitesize | https://www.bbc.co.uk/bitesize | ⚠️ Referência de didática acessível para jovens |

**🔴 Fontes PROIBIDAS:**

| Tipo | Motivo |
|---|---|
| Blogs sem autoria identificada | Sem verificação |
| Wikipedia (como fonte primária) | Editável por qualquer pessoa — pode ser usada como ponto de partida para localizar fontes primárias |
| Materiais de cursinhos piratas | Violação de direitos autorais |
| IA sem revisão pelo Agente Validador | Risco de alucinação |
| Redes sociais | Sem revisão por pares |

#### Entrega 2 — Mapas Curriculares Independentes (Por Matéria e Segmento)

Cada disciplina e segmento de ensino possuirá um arquivo físico individual `.md` (ex: `mapa_curricular_matematica_fundamental.md`, `mapa_curricular_matematica_medio.md`). A granularidade interna é por **Objetos de Conhecimento**:
- **Matemática Fundamental (5º ao 9º):** Lista de todos os Objetos de Conhecimento da BNCC, com habilidades mapeadas (códigos EFxxMAxx)
- **Matemática Ensino Médio (1ª a 3ª):** Objetos de Conhecimento BNCC + competências e habilidades específicas
- **Física Ensino Médio (1ª a 3ª):** Objetos de Conhecimento BNCC + habilidades
- **Química Ensino Médio (1ª a 3ª):** Objetos de Conhecimento BNCC + habilidades
- **ENEM (Matemática, Física, Química):** Competências e habilidades da Matriz de Referência INEP

#### Entrega 3 — Ordem de Produção (Sem Priorização Interna)

Documento formalizando que não há priorização entre conteúdos de uma mesma disciplina e que a produção obedecerá a demanda humana.

#### Entrega 4 — Arquivos de Infraestrutura da Base Teórica

| Arquivo | Função |
|---|---|
| `_index.md` | Índice geral com links para todos os arquivos da base teórica |
| `_fontes-verificadas.md` | Banco de fontes curadas (espelho do banco acima, atualizado conforme novas fontes são descobertas) |
| `_checklist-qualidade.md` | Checklist padrão operacional de qualidade para cada `.md` produzido |

#### Entrega 5 — Agente Validador Acadêmico (nova skill via Meta-Arquiteto)

Criação de uma skill especializada em **validação de conteúdos acadêmicos**, substituindo a revisão humana por professor licenciado. O agente deve:
- Verificar veracidade de toda afirmação factual (triangulação em ≥5 fontes)
- Validar alinhamento com habilidades BNCC/INEP declaradas no frontmatter
- Conferir conformidade do template (seções obrigatórias, YAML, tags HTML)
- Verificar adequação de linguagem à faixa etária
- Checar conformidade ABNT das referências
- Emitir parecer: `aprovado` | `revisão_necessária` (com apontamentos específicos)

**Checklist de Validação do Sprint 11:**
- [ ] Protocolo é autocontido e replicável por qualquer agente?
- [ ] Banco de fontes cobre 3 níveis (Governamental + Acadêmico + Pedagógico) + internacionais?
- [ ] Fontes proibidas documentadas?
- [ ] Mapa curricular cobre 100% dos Objetos de Conhecimento BNCC/INEP do escopo?
- [ ] Template de ficha bibliográfica é claro e preenchível?
- [ ] Granularidade atômica respeitada (1 ficha = 1 Objeto de Conhecimento)?
- [ ] Arquivos de infraestrutura criados (`_index.md`, `_fontes-verificadas.md`, `_checklist-qualidade.md`)?
- [ ] Agente Validador Acadêmico projetado (via Meta-Arquiteto)?
- [ ] Pilar Financeiro respeitado (zero fontes pagas)?

---

### Sprint 12 — Produção de E-books Educacionais (Granulares e Atômicos)
**✅ Concluído: Matemática do 6º Ano (100% Finalizado)**
**✅ Concluído: Matemática do 7º Ano (100% Finalizado)**
**✅ Concluído: Matemática do 8º Ano (100% Finalizado - 22 Capítulos Refatorados)**
**✅ Concluído: Matemática do 9º Ano (100% Finalizado - 21 Capítulos Refatorados)**
**✅ Concluído: Matemática do Ensino Médio (Batch 1 - Capítulos 01 ao 05)**
**✅ Concluído: Matemática do Ensino Médio (Batch 2 - Capítulos 06 ao 10)**
**✅ Concluído: Matemática do Ensino Médio (Batch 3 - Capítulos 11 ao 15)**
**✅ Concluído: Matemática do Ensino Médio (Batch 4 - Capítulos 16 ao 20)**
**✅ Concluído: Matemática do Ensino Médio (Batch 5 - Capítulos 21 ao 25)**
**✅ Concluído: Matemática do Ensino Médio (Batch 6 - Capítulos 26 ao 30)**
**✅ Concluído: Matemática do Ensino Médio (Batch 7 - Capítulos 31 ao 35)**
**✅ Concluído: Matemática do Ensino Médio (Batch 8 - Capítulos 36 ao 38 - CONCLUSÃO FINAL)**
**✅ Concluído: Física da 1ª Série (Física I - Mecânica e Fluidos - 21 Capítulos, 50 E-books 100% Homologados em Gemini Pro)**
**✅ Concluído: Física da 2ª Série (Física II - Termologia, Óptica, MHS e Ondulatória - 19 Capítulos, 41 E-books 100% Homologados em Gemini Pro)**
**✅ Concluído: Física da 3ª Série (Física III - Eletrostática, Eletrodinâmica, Eletromagnetismo, Física Moderna e Análise Dimensional - 21 Capítulos, 39 E-books 100% Homologados em Gemini Pro)**
**✅ Concluído: Química da 1ª Série (Química I - Química Geral - 18 Capítulos, 40 E-books Teóricos Atômicos 100% Homologados com Exit Code 0 no Validador Oficial)**
**✅ Concluído: Química da 2ª Série (Química II - Físico-Química - 16 Capítulos, 34 E-books Teóricos Atômicos 100% Homologados com Exit Code 0 no Validador Oficial)**
**✅ Concluído: Química da 3ª Série (Química III - Química Orgânica, Bioquímica e Polímeros - 19 Capítulos, 38 E-books Teóricos Atômicos 100% Homologados com Exit Code 0 no Validador Oficial)**
**🏆 CONCLUSÃO TOTAL: Química do Ensino Médio 100% Concluída (53 Capítulos | 112 E-books Teóricos Atômicos 100% Homologados)**
**🏆 CONCLUSÃO TOTAL: Geografia do Ensino Fundamental 100% Concluída (40 Capítulos | 40 E-books Teóricos Atômicos 100% Homologados - 126.021 Palavras)**
**🏆 CONCLUSÃO TOTAL: Língua Portuguesa do 5º Ano 100% Concluída (20 Capítulos | 20 E-books Teóricos Atômicos 100% Homologados - 60.960 Palavras)**
**🏆 CONCLUSÃO TOTAL: Língua Portuguesa do 6º Ano 100% Concluída (20 Capítulos | 20 E-books Teóricos Atômicos 100% Homologados - 67.664 Palavras)**
**🏆 CONCLUSÃO TOTAL: Língua Portuguesa do 7º Ano 100% Concluída (20 Capítulos | 20 E-books Teóricos Atômicos 100% Homologados - 57.190 Palavras)**
**🏆 CONCLUSÃO TOTAL: Língua Portuguesa do 8º Ano 100% Concluída (20 Capítulos | 20 E-books Teóricos Atômicos 100% Homologados - 52.228 Palavras)**
**🏆 CONCLUSÃO TOTAL: Língua Portuguesa do 9º Ano 100% Concluída (20 Capítulos | 20 E-books Teóricos Atômicos 100% Homologados - 50.522 Palavras)**
**🏆 MARCO HISTÓRICO: 100% DO ENSINO FUNDAMENTAL DE LÍNGUA PORTUGUESA CONCLUÍDO (5º AO 9º ANO — 100 CAPÍTULOS | 100 E-BOOKS HOMOLOGADOS | 288.564 PALAVRAS LIMPAS)**


> **Complexidade:** 🔴 Alta — Sprint **cíclico e incremental** (múltiplas conversas — 1 conversa por Objeto de Conhecimento recomendado). Este sprint será executado repetidamente ao longo de meses.  
> **Skill a acionar:** E-book Creator
> **Pré-requisitos:** Sprint 11 concluído (protocolo + mapa curricular + fichas bibliográficas preenchidas + Agente Validador criado)

**Objetivo:** Produzir e-books **atômicos** em Markdown — **1 e-book por Objeto de Conhecimento da BNCC** — utilizando as fichas bibliográficas como matéria-prima. Os e-books são a base de conteúdo para: (1) alimentar o RAG do Mob.me, (2) servir de matéria-prima para os SPAs interativos, e (3) alimentar futuras sessões de revisão.

**⚠️ Regra de Granularidade Estrita:**
- **1 E-book = 1 Objeto de Conhecimento da BNCC** (bloco atômico)
- O backend (FastAPI/Mob.me) precisa desses blocos separados para construir contextos RAG precisos

**Metadados Obrigatórios (por e-book):**
1. **YAML Frontmatter:** Cabeçalho com série, disciplina, unidade temática, objeto de conhecimento, habilidades BNCC/INEP (códigos), pré-requisitos (links relativos), nível de dificuldade, palavras-chave, tempo estimado de leitura, fonte bibliográfica, status de revisão
2. **Andaimes Cognitivos:** Blocos "Na Prática" e Tabela de Erros Comuns obrigatórios.
3. **Seção "Resumo para Revisão":** 3-5 pontos-chave concisos + link para próximo tópico na sequência. Alimenta futuras sessões de revisão.
4. **Referências ABNT:** Lista de referências no padrão NBR 6023 (não é necessário formatar citações no texto).

**Estrutura de Execução (por Objeto de Conhecimento):**
1. Consultar a ficha bibliográfica do Objeto (Sprint 11)
2. Acionar a skill **E-book Creator** com prompt contendo:
   - Série e disciplina alvo
   - Objeto de Conhecimento específico e habilidades BNCC/INEP a cobrir
   - Fontes validadas da ficha bibliográfica
   - Instrução de YAML Frontmatter obrigatório
   - Instrução de acessibilidade TDAH/Dislexia
   - Caminho absoluto de destino no workspace
3. Submeter o e-book ao **Agente Validador Acadêmico** (Sprint 11, Entrega 5)
4. Corrigir apontamentos até obter parecer `aprovado`

**Caminho de Destino:**
```
content/[nivel]/[serie]/[disciplina]/[capitulo]/ebooks/[objeto-de-conhecimento].md
```
> Nota: Cada capítulo agora contém uma subpasta `ebooks/` com N arquivos atômicos.

**Etapa de Piloto (sob demanda do usuário):**
Antes de escalar a produção, o usuário pode solicitar um **ciclo piloto** com 1 Objeto de Conhecimento completo (pesquisa → e-book → validação → SPA). O piloto serve para:
- Calibrar o template e o fluxo de produção
- Testar a integração com Mob.me (RAG encontra e cita o conteúdo?)
- Testar a extração de questões pelo SPA (tags HTML parseadas?)
- Ajustar o processo antes de escalar

**Ordem de Produção:**
Não há priorização entre conteúdos de uma mesma disciplina. A produção obedecerá a demanda humana:
1. **Matemática**: Todo o conteúdo do 5º ano do Ensino Fundamental até a 3ª série do Ensino Médio e ENEM. *(Avanço atual: **5º Ano, 6º Ano, 7º Ano, 8º Ano, 9º Ano e Ensino Médio Volume Único estão 100% finalizados** com teoria atômica e todas as listas de 60 exercícios concluídas e validadas).* **[Educação Básica Completa em Matemática: 5º ao 9º EF + Volume Único EM 100% CONCLUÍDOS]**
2. **Ciências (Ensino Fundamental)**:
   - **5º Ano**: **11 de 11 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 11, cobrindo 100% das 13 habilidades BNCC: `EF05CI01` a `EF05CI13`), totalizando mais de 35.000 palavras de teoria pura, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[5º Ano de Ciências 100% CONCLUÍDO]**
   - **6º Ano**: **13 de 13 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 13, cobrindo 100% das 14 habilidades BNCC: `EF06CI01` a `EF06CI14`), totalizando 41.133 palavras de teoria pura, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[6º Ano de Ciências 100% CONCLUÍDO]**
   - **7º Ano**: **15 de 15 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 15, cobrindo 100% das 16 habilidades BNCC: `EF07CI01` a `EF07CI16`), totalizando 72.911 palavras de teoria pura, densidade média de 4.861 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[7º Ano de Ciências 100% CONCLUÍDO]**
   - **8º Ano**: **16 de 16 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 16, cobrindo 100% das 16 habilidades BNCC: `EF08CI01` a `EF08CI16`), totalizando 47.680 palavras de teoria pura, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[8º Ano de Ciências 100% CONCLUÍDO]**
   - **9º Ano**: **17 de 17 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 17, cobrindo 100% das 17 habilidades BNCC: `EF09CI01` a `EF09CI17`), totalizando 46.964 palavras de teoria pura, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[9º Ano de Ciências 100% CONCLUÍDO]**
   - **TOTAL GERAL DE CIÊNCIAS (Ensino Fundamental - 5º ao 9º Ano)**: **72 de 72 e-books teóricos atômicos concluídos e homologados**, totalizando **244.061 palavras** de conteúdo acadêmico denso, 100% alinhado à BNCC, sem nenhum exercício nas bases teóricas, supressão rigorosa de `R$` e conformidade absoluta com ABNT NBR 6023. **[Ciências do Ensino Fundamental 100% CONCLUÍDO]**
3. **História (Ensino Fundamental - 5º ao 9º Ano)**:
   - **5º Ano**: **6 de 6 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 06, cobrindo 100% das 10 habilidades BNCC: `EF05HI01` a `EF05HI10`), totalizando **19.303 palavras** de teoria pura, densidade média de 3.217 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[5º Ano de História 100% CONCLUÍDO]**
   - **6º Ano**: **11 de 11 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 11, cobrindo 100% das 19 habilidades BNCC: `EF06HI01` a `EF06HI19`), totalizando **39.316 palavras** de teoria pura, densidade média de 3.574 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[6º Ano de História 100% CONCLUÍDO]**
   - **7º Ano**: **11 de 11 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 11, cobrindo 100% das 17 habilidades BNCC: `EF07HI01` a `EF07HI17`), totalizando **37.718 palavras** de teoria pura, densidade média de 3.429 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[7º Ano de História 100% CONCLUÍDO]**
   - **8º Ano**: **16 de 16 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 16, cobrindo 100% das 27 habilidades BNCC: `EF08HI01` a `EF08HI27`), totalizando 56.580 palavras de teoria pura, densidade média de 3.536 palavras por e-book, zero exercícios, zero "R$", progressão em espiral, conexões interdisciplinares, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[8º Ano de História 100% CONCLUÍDO]**
   - **9º Ano**: **18 de 18 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 18, cobrindo 100% das 36 habilidades BNCC: `EF09HI01` a `EF09HI36`), totalizando 66.190 palavras de teoria pura, densidade média de 3.677 palavras por e-book, zero exercícios, zero "R$", progressão em espiral, conexões interdisciplinares, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[9º Ano de História 100% CONCLUÍDO]**
   - **TOTAL GERAL DE HISTÓRIA**: **62 de 62 E-books Teóricos Atômicos Homologados (100% CONCLUÍDO)** cobrindo todas as **109 Habilidades BNCC (`EF05HI01` a `EF09HI36`)**, totalizando **221.298 palavras** de teoria pura, densidade média de 3.569 palavras por e-book, zero exercícios, zero "R$", e aprovação unânime com retorno 0 no `validador_educamob.py`. **[História do Ensino Fundamental 100% CONCLUÍDO]**
4. **Geografia (Ensino Fundamental - 5º ao 9º Ano)**:
   - **5º Ano**: **9 de 9 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 09, cobrindo 100% das 12 habilidades BNCC: `EF05GE01` a `EF05GE12`), totalizando 25.808 palavras de teoria pura, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[5º Ano de Geografia 100% CONCLUÍDO]**
   - **6º Ano**: **6 de 6 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 06, cobrindo 100% das 13 habilidades BNCC: `EF06GE01` a `EF06GE13`), totalizando 18.368 palavras de teoria pura, densidade média de 3.061 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[6º Ano de Geografia 100% CONCLUÍDO]**
   - **7º Ano**: **7 de 7 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 07, cobrindo 100% das 12 habilidades BNCC: `EF07GE01` a `EF07GE12`), totalizando 23.918 palavras de teoria pura, densidade média de 3.417 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[7º Ano de Geografia 100% CONCLUÍDO]**
   - **8º Ano**: **8 de 8 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 08, cobrindo 100% das 24 habilidades BNCC: `EF08GE01` a `EF08GE24`), totalizando 26.545 palavras de teoria pura, densidade média de 3.318 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[8º Ano de Geografia 100% CONCLUÍDO]**
   - **9º Ano**: **10 de 10 e-books teóricos atômicos concluídos e homologados** (Capítulos 01 ao 10, cobrindo 100% das 18 habilidades BNCC: `EF09GE01` a `EF09GE18`), totalizando 31.382 palavras de teoria pura, densidade média de 3.138 palavras por e-book, sem exercícios, com scaffolding cognitivo, tabelas de erros comuns e conformidade ABNT/BNCC via `validador_educamob.py`. **[9º Ano de Geografia 100% CONCLUÍDO]**
   - **TOTAL GERAL DE GEOGRAFIA**: **40 de 40 Capítulos Atômicos CONCLUÍDOS E HOMOLOGADOS (100%)** cobrindo 100% das **79 Habilidades BNCC** do 5º ao 9º Ano do Ensino Fundamental, totalizando **126.021 palavras** de teoria pura, densidade média de 3.150 palavras por e-book, sem exercícios nas bases teóricas, supressão rigorosa de `R$` e conformidade absoluta com ABNT NBR 6023. **[Geografia do Ensino Fundamental 100% CONCLUÍDA]**
5. **Língua Portuguesa (Ensino Fundamental - 5º ao 9º Ano)**:
   - **5º Ano: 20 de 20 e-books teóricos atômicos concluídos e homologados (100% CONCLUÍDO)** cobrindo a totalidade das habilidades BNCC dos Anos Iniciais/5º Ano, totalizando **60.960 palavras** de teoria pura, densidade média de 3.048 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT NBR 6023 e aprovação unânime no validador_educamob.py. **[5º Ano de Língua Portuguesa 100% CONCLUÍDO]**
     - **Eixo I: Análise Linguística / Semiótica (Gramática, Morfossintaxe, Ortografia e Semântica - 100% Concluído)**:
       - **Capítulo 01:** cap-01-sistema-escrita-ortografia (ef05lp01-ortografia.md - 3.493 palavras) ✅
       - **Capítulo 02:** cap-02-acentuacao-grafica-prosodia (ef05lp03-acentuacao.md - 3.314 palavras) ✅
       - **Capítulo 03:** cap-03-morfologia-substantivos-adjetivos (ef05lp05-substantivos-adjetivos.md - 3.253 palavras) ✅
       - **Capítulo 04:** cap-04-morfologia-verbos-flexoes (ef05lp06-verbos-tempos-modos.md - 3.503 palavras) ✅
       - **Capítulo 05:** cap-05-pronomes-adverbios-interjeicoes (ef05lp07-ef05lp08-pronomes-adverbios.md - 3.365 palavras) ✅
       - **Capítulo 06:** cap-06-pontuacao-sintaxe-frase (ef05lp04-pontuacao-sintaxe.md - 3.170 palavras) ✅
       - **Capítulo 07:** cap-07-coesao-articuladores-anaforicos (ef05lp27-coesao-articuladores.md - 2.608 palavras) ✅
       - **Capítulo 08:** cap-08-semantica-polissemia-dicionario (ef05lp02-semantica-polissemia.md - 3.178 palavras) ✅
     - **Eixo II: Leitura e Compreensão Textual nos Campos de Atuação (100% Concluído)**:
       - **Capítulo 09:** cap-09-estrategias-leitura-inferencia (ef15lp01-ef15lp04-estrategias-leitura.md - 3.455 palavras) ✅
       - **Capítulo 10:** cap-10-fluencia-fato-vs-opiniao (ef35lp05-fato-opiniao-apreciacao.md - 2.859 palavras) ✅
       - **Capítulo 11:** cap-11-textos-jornalisticos-midiaticos (ef05lp09-ef05lp10-generos-jornalisticos.md - 4.040 palavras) ✅
       - **Capítulo 12:** cap-12-textos-divulgacao-cientifica-graficos (ef05lp22-ef05lp23-divulgacao-cientifica.md - 2.762 palavras) ✅
       - **Capítulo 13:** cap-13-textos-reivindicatorios-vida-publica (ef05lp16-textos-reivindicatorios.md - 3.078 palavras) ✅
     - **Eixo III: Campo Artístico-Literário (100% Concluído)**:
       - **Capítulo 14:** cap-14-narrativas-ficcionais-cronica-conto (ef35lp21-ef35lp22-narrativas-ficcionais.md - 2.907 palavras) ✅
       - **Capítulo 15:** cap-15-discurso-direto-indireto-narrador (ef35lp22-discurso-direto-indireto.md - 2.877 palavras) ✅
       - **Capítulo 16:** cap-16-poesia-formas-estroficas-recursos-sonoros (ef35lp23-ef35lp27-poesia-versos.md - 2.542 palavras) ✅
       - **Capítulo 17:** cap-17-texto-dramatico-teatral-rubricas (ef05lp24-texto-dramatico-teatral.md - 2.615 palavras) ✅
     - **Eixo IV: Produção de Texto, Oralidade e Variação Linguística (100% Concluído)**:
       - **Capítulo 18:** cap-18-producao-texto-planejamento-revisao (ef15lp05-ef15lp06-producao-texto.md - 2.572 palavras) ✅
       - **Capítulo 19:** cap-19-oralidade-exposicao-argumentacao (ef15lp09-ef15lp13-oralidade-exposicao.md - 2.555 palavras) ✅
       - **Capítulo 20:** cap-20-variacao-linguistica-preconceito-linguistico (ef35lp11-variacao-linguistica.md - 2.814 palavras) ✅
   - **6º Ano: 20 de 20 e-books teóricos atômicos concluídos e homologados (100% CONCLUÍDO)** cobrindo a totalidade das habilidades BNCC dos Anos Finais / 6º Ano (EF06LP01 a EF06LP12, EF67LP e EF69LP), totalizando **67.664 palavras** de teoria pura, densidade média de 3.383 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT NBR 6023 e aprovação unânime no validador_educamob.py. **[6º Ano de Língua Portuguesa 100% CONCLUÍDO]**
     - **Eixo I: Análise Linguística / Semiótica e Morfossintaxe (100% Concluído)**:
       - **Capítulo 01:** cap-01-linguagem-signo-funcoes-comunicacao (ef69lp55-ef69lp56-signo-linguistico.md - 3.025 palavras) ✅
       - **Capítulo 02:** cap-02-fonetica-fonologia-encontros-acentuacao (ef06lp11-fonetica-acentuacao.md - 2.968 palavras) ✅
       - **Capítulo 03:** cap-03-estrutura-formacao-palavras (ef06lp03-formacao-palavras.md - 2.572 palavras) ✅
       - **Capítulo 04:** cap-04-morfologia-substantivos-flexoes (ef06lp04-substantivos-flexoes.md - 2.689 palavras) ✅
       - **Capítulo 05:** cap-05-morfologia-adjetivos-locucoes-graus (ef06lp04-adjetivos-graus.md - 2.789 palavras) ✅
       - **Capítulo 06:** cap-06-morfologia-artigos-numerais (ef06lp04-artigos-numerais.md - 2.866 palavras) ✅
       - **Capítulo 07:** cap-07-morfologia-verbos-tempos-modos (ef06lp05-verbos-tempos-modos.md - 2.488 palavras) ✅
       - **Capítulo 08:** cap-08-morfologia-pronomes-coesao (ef06lp12-pronomes-coesao.md - 2.735 palavras) ✅
     - **Eixo II: Sintaxe da Oração, Pontuação e Semântica (100% Concluído)**:
       - **Capítulo 09:** cap-09-sintaxe-frase-oracao-periodo (ef06lp07-ef06lp08-periodo-simples-composto.md - 4.465 palavras) ✅
       - **Capítulo 10:** cap-10-sintaxe-sujeito-predicado (ef06lp06-ef06lp11-sujeito-predicado.md - 4.137 palavras) ✅
       - **Capítulo 11:** cap-11-pontuacao-sintatica-expressiva (ef06lp07-ef06lp11-pontuacao-expressiva.md - 3.679 palavras) ✅
       - **Capítulo 12:** cap-12-semantica-sinonimia-polissemia-ambiguidade (ef06lp03-ef06lp12-semantica-ambiguidade.md - 3.926 palavras) ✅
     - **Eixo III: Campo Jornalístico-Midiático e Cultura Digital (100% Concluído)**:
       - **Capítulo 13:** cap-13-campo-jornalistico-centralidade-noticia (ef06lp01-ef06lp02-centralidade-noticia.md - 3.958 palavras) ✅
       - **Capítulo 14:** cap-14-hipertexto-hiperlinks-curadoria-digital (ef67lp01-ef67lp03-hipertexto-curadoria.md - 3.874 palavras) ✅
       - **Capítulo 15:** cap-15-opiniao-leitor-comentarios-redes-sociais (ef67lp02-ef67lp05-carta-leitor-comentarios.md - 3.649 palavras) ✅
       - **Capítulo 16:** cap-16-textos-publicitarios-propaganda-persuasao (ef67lp08-ef67lp13-publicidade-propaganda.md - 3.580 palavras) ✅
     - **Eixo IV: Campo de Estudo e Pesquisa, Vida Pública e Arte Literária (100% Concluído)**:
       - **Capítulo 17:** cap-17-estudo-pesquisa-resumo-infografico (ef67lp20-ef67lp21-divulgacao-cientifica-infografico.md - 3.324 palavras) ✅
       - **Capítulo 18:** cap-18-campo-vida-publica-textos-reivindicatorios-normativos (ef67lp15-ef67lp17-textos-reivindicatorios.md - 3.427 palavras) ✅
       - **Capítulo 19:** cap-19-campo-literario-mitos-lendas-narrativas-aventura (ef67lp27-ef67lp28-mitos-lendas-narrativas.md - 3.556 palavras) ✅
       - **Capítulo 20:** cap-20-poesia-formas-fixas-versos-livres-figuras (ef67lp32-ef69lp48-poesia-figuras-linguagem.md - 3.957 palavras) ✅
     - **Total Geral Homologado no 6º Ano (20 Capítulos):** **67.664 palavras** de teoria pura, densidade média de 3.383 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT NBR 6023 e aprovação unânime no validador_educamob.py.
   - **7º Ano (🏆 100% Concluído — 20 de 20 Capítulos Homologados — 57.190 Palavras Limpas)**:
     - **Eixo I: Sintaxe da Oração, Morfossintaxe e Coesão (Capítulos 01 ao 08 — 100% Concluído)**:
       - **Capítulo 01:** cap-01-predicacao-transitividade-verbal (ef07lp04-ef07lp05-transitividade-verbal.md - 3.263 palavras) ✅
       - **Capítulo 02:** cap-02-termos-integrantes-objeto-direto-indireto (ef07lp07-objetos-direto-indireto.md - 3.126 palavras) ✅
       - **Capítulo 03:** cap-03-termos-acessorios-adjunto-adnominal (ef07lp08-adjunto-adnominal.md - 2.832 palavras) ✅
       - **Capítulo 04:** cap-04-termos-acessorios-adjunto-adverbial (ef07lp09-adjunto-adverbial.md - 2.906 palavras) ✅
       - **Capítulo 05:** cap-05-vozes-verbais-ativa-passiva-reflexiva (ef07lp05-ef07lp06-vozes-verbais.md - 4.271 palavras) ✅
       - **Capítulo 06:** cap-06-concordancia-nominal-casos-especiais (ef07lp06-ef07lp10-concordancia-nominal.md - 3.482 palavras) ✅
       - **Capítulo 07:** cap-07-concordancia-verbal-casos-particulares (ef07lp06-ef07lp10-concordancia-verbal.md - 3.573 palavras) ✅
       - **Capítulo 08:** cap-08-semantica-hiperonimia-coesao-referencial (ef07lp11-ef07lp13-hiperonimia-coesao.md - 3.388 palavras) ✅
     - **Eixo II: Campo Jornalístico-Midiático e Humor Gráfico (Capítulos 09 ao 12 — 100% Concluído)**:
       - **Capítulo 09:** cap-09-campo-jornalistico-grande-reportagem (ef67lp08-ef07lp01-grande-reportagem.md - 2.877 palavras) ✅
       - **Capítulo 10:** cap-10-humor-grafico-charge-cartum (ef67lp08-ef69lp05-humor-grafico.md - 2.914 palavras) ✅
       - **Capítulo 11:** cap-11-genero-entrevista-jornalistica (ef67lp14-ef67lp15-entrevista-jornalistica.md - 2.589 palavras) ✅
       - **Capítulo 12:** cap-12-etica-editorial-analise-midia (ef67lp01-ef67lp03-etica-editorial-fake-news.md - 2.906 palavras) ✅
     - **Eixo III: Campo de Atuação na Vida Pública e Argumentação (Capítulos 13 ao 16 — 100% Concluído)**:
       - **Capítulo 13:** cap-13-campo-vida-publica-carta-reclamacao-ouvidoria (ef67lp16-ef67lp17-carta-reclamacao.md - 2.397 palavras) ✅
       - **Capítulo 14:** cap-14-debate-regrado-argumentacao-mesa-redonda (ef67lp14-ef69lp13-debate-regrado.md - 2.371 palavras) ✅
       - **Capítulo 15:** cap-15-textos-legais-estatuto-igualdade-racial (ef67lp17-ef67lp19-igualdade-racial-leis.md - 2.636 palavras) ✅
       - **Capítulo 16:** cap-16-liberdade-expressao-marco-civil-internet (ef67lp18-ef69lp21-marco-civil-internet.md - 2.654 palavras) ✅
     - **Eixo IV: Campo de Estudo e Pesquisa & Campo Artístico-Literário (Capítulos 17 ao 20 — 100% Concluído)**:
       - **Capítulo 17:** cap-17-estudo-pesquisa-relatorio-experimento-seminario (ef67lp20-ef67lp22-relatorio-experimento-seminario.md - 2.143 palavras) ✅
       - **Capítulo 18:** cap-18-campo-literario-conto-policial-terror-enigma (ef67lp27-ef67lp28-conto-policial-enigma.md - 2.203 palavras) ✅
       - **Capítulo 19:** cap-19-campo-literario-cronica-literaria-humoristica (ef67lp28-ef69lp46-cronica-literaria-humor.md - 2.137 palavras) ✅
       - **Capítulo 20:** cap-20-campo-literario-texto-dramatico-teatral (ef67lp29-ef69lp52-texto-dramatico-teatro.md - 2.522 palavras) ✅
     - **Total Geral Homologado no 7º Ano (20 Capítulos — 100% Concluído):** **57.190 palavras** de teoria pura, densidade média de 2.859 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT NBR 6023 e aprovação unânime no validador_educamob.py.
   - **8º Ano (🏆 100% Concluído — 20 de 20 Capítulos Homologados — 52.228 Palavras Limpas)**:
     - **Eixo I: Sintaxe do Período Composto, Morfossintaxe e Estilística (Capítulos 01 ao 08 — 100% Concluído)**:
       - **Capítulo 01:** cap-01-periodo-composto-coordenacao-oracoes-coordenadas (ef08lp11-ef08lp13-oracoes-coordenadas.md - 2.374 palavras) ✅
       - **Capítulo 02:** cap-02-periodo-composto-subordinacao-oracoes-substantivas (ef08lp11-ef08lp12-oracoes-substantivas.md - 2.350 palavras) ✅
       - **Capítulo 03:** cap-03-oracoes-subordinadas-adjetivas-pontuacao (ef08lp13-ef08lp14-oracoes-adjetivas.md - 2.519 palavras) ✅
       - **Capítulo 04:** cap-04-regencia-verbal-nominal-crase (ef08lp07-ef08lp08-regencia-crase.md - 2.519 palavras) ✅
       - **Capítulo 05:** cap-05-colocacao-pronominal-proclise-enclise-mesoclise (ef08lp06-ef08lp08-colocacao-pronominal.md - 3.490 palavras) ✅
       - **Capítulo 06:** cap-06-verbos-modos-tempos-subjuntivo-correlacao (ef08lp04-ef08lp05-modos-verbais-correlacao.md - 3.508 palavras) ✅
       - **Capítulo 07:** cap-07-morfologia-processos-derivacao-composicao (ef08lp04-ef08lp05-formacao-palavras.md - 3.122 palavras) ✅
       - **Capítulo 08:** cap-08-figuras-linguagem-pensamento-sintaxe (ef08lp15-ef89lp37-figuras-linguagem.md - 3.084 palavras) ✅
     - **Eixo II: Campo Jornalístico-Midiático e Opinião (Capítulos 09 ao 12 — 100% Concluído)**:
       - **Capítulo 09:** cap-09-artigo-opiniao-argumentacao-tese (ef08lp03-ef89lp03-artigo-opiniao.md - 2.517 palavras) ✅
       - **Capítulo 10:** cap-10-editorial-jornalistico-linha-editorial (ef08lp01-ef89lp04-editorial-jornalistico.md - 2.281 palavras) ✅
       - **Capítulo 11:** cap-11-carta-leitor-comentario-redes-debate (ef08lp02-ef89lp05-carta-leitor.md - 2.511 palavras) ✅
       - **Capítulo 12:** cap-12-resenha-critica-analise-cultural (ef08lp03-ef89lp06-resenha-critica.md - 2.466 palavras) ✅
     - **Eixo III: Campo de Atuação na Vida Pública (Capítulos 13 ao 16 — 100% Concluído)**:
       - **Capítulo 13:** cap-13-campo-vida-publica-estatuto-crianca-adolescente (ef89lp17-ef89lp18-estatuto-crianca-adolescente.md - 2.660 palavras) ✅
       - **Capítulo 14:** cap-14-textos-reivindicatorios-manifesto-peticao (ef89lp17-ef89lp20-manifesto-peticao.md - 2.272 palavras) ✅
       - **Capítulo 15:** cap-15-publicidade-propaganda-consumismo-adolescente (ef08lp03-ef89lp09-publicidade-consumo.md - 2.422 palavras) ✅
       - **Capítulo 16:** cap-16-direitos-humanos-liberdade-expressao-democracia (ef89lp17-ef89lp22-direitos-humanos-democracia.md - 2.363 palavras) ✅
     - **Eixo IV: Campo de Estudo e Pesquisa & Campo Artístico-Literário (Capítulos 17 ao 20 — 100% Concluído)**:
       - **Capítulo 17:** cap-17-estudo-pesquisa-artigo-divulgacao-cientifica (ef89lp24-ef89lp26-divulgacao-cientifica.md - 2.626 palavras) ✅
       - **Capítulo 18:** cap-18-campo-literario-conto-ficcao-cientifica-distopia (ef89lp32-ef89lp33-ficcao-cientifica-distopia.md - 2.414 palavras) ✅
       - **Capítulo 19:** cap-19-campo-literario-poesia-visual-concreta-slam (ef89lp33-ef89lp35-poesia-visual-slam.md - 2.262 palavras) ✅
       - **Capítulo 20:** cap-20-campo-literario-conto-psicologico-fluxo-consciencia (ef89lp32-ef89lp36-conto-psicologico.md - 2.468 palavras) ✅
     - **Total Geral Homologado no 8º Ano (20 Capítulos — 100% Concluído):** **52.228 palavras** de teoria pura, densidade média de 2.611 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT NBR 6023 e aprovação unânime no validador_educamob.py.
   - **9º Ano (🏆 100% Concluído — 20 de 20 Capítulos Homologados — 50.522 Palavras Limpas)**:
     - **Eixo I: Sintaxe Avançada, Coesão e Estilística (Capítulos 01 ao 08 — 100% Concluído)**:
       - **Capítulo 01:** cap-01-oracoes-subordinadas-adverbiais-circunstancias (ef09lp08-ef09lp11-oracoes-adverbiais.md - 2.585 palavras) ✅
       - **Capítulo 02:** cap-02-oracoes-reduzidas-infinitivo-gerundio-participio (ef09lp08-ef09lp11-oracoes-reduzidas.md - 2.350 palavras) ✅
       - **Capítulo 03:** cap-03-sintaxe-concordancia-verbal-casos-complexos (ef09lp04-ef09lp06-concordancia-verbal-avancada.md - 2.797 palavras) ✅
       - **Capítulo 04:** cap-04-pontuacao-sintatica-periodo-composto (ef09lp05-ef09lp07-pontuacao-periodo-composto.md - 2.797 palavras) ✅
       - **Capítulo 05:** cap-05-coesao-referencial-sequencial-operadores-argumentativos (ef09lp10-ef09lp11-coesao-operadores.md - 3.084 palavras) ✅
       - **Capítulo 06:** cap-06-semantica-polissemia-modalizacao-epistemica (ef09lp09-ef89lp37-semantica-modalizacao.md - 2.486 palavras) ✅
       - **Capítulo 07:** cap-07-variacao-linguistica-preconceito-norma-culta (ef09lp01-ef69lp56-variacao-linguistica.md - 2.591 palavras) ✅
       - **Capítulo 08:** cap-08-intertextualidade-parodia-parafrase-pastiche (ef09lp02-ef89lp33-intertextualidade.md - 2.560 palavras) ✅
     - **Eixo II: Campo Jornalístico-Midiático e Opinião (Capítulos 09 ao 12 — 100% Concluído)**:
       - **Capítulo 09:** cap-09-debate-regrado-mesa-redonda-retorica-persuasao (ef89lp12-ef89lp14-debate-regrado.md - 2.460 palavras) ✅
       - **Capítulo 10:** cap-10-reportagem-investigativa-cruzamento-fontes-fact-checking (ef09lp01-ef89lp02-reportagem-investigativa.md - 2.355 palavras) ✅
       - **Capítulo 11:** cap-11-artigo-divulgacao-midiatico-podcast-videocast (ef89lp08-ef89lp15-podcast-videocast.md - 2.382 palavras) ✅
       - **Capítulo 12:** cap-12-analise-discurso-midia-enquadramento-ideologia (ef89lp04-ef89lp07-analise-discurso-midia.md - 2.404 palavras) ✅
     - **Eixo III: Campo de Atuação na Vida Pública (Capítulos 13 ao 16 — 100% Concluído)**:
       - **Capítulo 13:** cap-13-textos-normativos-constituicao-leis-inclusao (ef89lp17-ef89lp18-legislacao-inclusao.md - 2.443 palavras) ✅
       - **Capítulo 14:** cap-14-projeto-intervencao-social-acao-comunitaria (ef89lp19-ef89lp20-projeto-intervencao-social.md - 2.166 palavras) ✅
       - **Capítulo 15:** cap-15-audiencia-publica-orcamento-participativo-ouvidoria (ef89lp17-ef89lp23-audiencia-publica-ouvidoria.md - 2.588 palavras) ✅
       - **Capítulo 16:** cap-16-cultura-paz-direitos-humanos-justica-restaurativa (ef89lp17-ef89lp22-cultura-paz-mediacao.md - 2.559 palavras) ✅
     - **Eixo IV: Campo de Estudo, Pesquisa e Arte Literária (Capítulos 17 ao 20 — 100% Concluído)**:
       - **Capítulo 17:** cap-17-estudo-pesquisa-artigo-academico-normas-abnt (ef89lp24-ef89lp29-artigo-academico-abnt.md - 2.496 palavras) ✅
       - **Capítulo 18:** cap-18-campo-literario-cronica-ensaio-metaficcao (ef89lp32-ef89lp36-cronica-ensaio-metaficcao.md - 2.484 palavras) ✅
       - **Capítulo 19:** cap-19-campo-literario-romance-moderno-vozes-sociais (ef89lp32-ef89lp37-romance-moderno-vozes.md - 2.443 palavras) ✅
       - **Capítulo 20:** cap-20-campo-literario-poesia-contemporanea-lirismo-engajamento (ef89lp33-ef89lp35-poesia-contemporanea.md - 2.492 palavras) ✅
     - **Total Geral Homologado no 9º Ano (20 Capítulos — 100% Concluído):** **50.522 palavras** de teoria pura, densidade média de 2.526 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT NBR 6023 e aprovação unânime no validador_educamob.py.
     - **🏆 TOTAL GERAL CONSOLIDADO DO ENSINO FUNDAMENTAL DE LÍNGUA PORTUGUESA (5º AO 9º ANO — 100% CONCLUÍDO):** **100 Capítulos | 100 E-books Teóricos Atômicos Homologados | 288.564 palavras limpas** de teoria pura de excelência acadêmica, densidade média de 2.885 palavras por e-book, zero exercícios, zero 'R$', rigor ABNT e 100% de aprovação no validador_educamob.py.


**Checklist de Validação (por e-book atômico):**
- [ ] Granularidade respeitada (1 e-book = 1 Objeto de Conhecimento)?
- [ ] E-book é 100% teórico (sem exercícios)?
- [ ] YAML Frontmatter presente e completo (todos os campos obrigatórios)?
- [ ] Conteúdo segue microaprendizagem (blocos curtos)?
- [ ] Acessibilidade TDAH/Dislexia contemplada?
- [ ] Scaffolding incluído (blocos "Na Prática" + Tabela de Erros Comuns)?
- [ ] Seção "Resumo para Revisão" com 3-5 pontos-chave + link próximo tópico?
- [ ] Conexões interdisciplinares presentes?
- [ ] Habilidades BNCC/INEP declaradas no frontmatter?
- [ ] Referências ABNT (apenas NBR 6023)?
- [ ] 100% das afirmações factuais com fonte rastreável?
- [ ] Agente Validador Acadêmico emitiu parecer `aprovado`?

---

### Sprint 12.5 — Produção de Exercícios (Exercise Creator) [NOVO]

> **Complexidade:** 🔴 Alta (Cíclico e incremental, atrelado ao Sprint 12)
> **Skill a acionar:** Exercise Creator
> **Pré-requisitos:** E-book teórico do Objeto de Conhecimento correspondente aprovado (Sprint 12)

**Objetivo:** Gerar baterias de exatos 60 exercícios de múltipla escolha para cada Objeto de Conhecimento (20 básicos, 20 intermediários, 20 difíceis). As questões devem estar rigorosamente alinhadas à teoria e seguir o "Protocolo de Telemetria".

**Metadados e Regras:**
1. **Tags HTML:** Imediatamente antes de cada questão, deve constar: `<!-- id: qXX | tipo: multipla-escolha | habilidade: [COD_BNCC] | dificuldade: [nivel] | objeto: [slug] -->`.
2. **Resoluções:** Gabaritos devem conter explicação detalhada (em etapas lógicas para as questões difíceis).
3. **Caminho de Destino:** `content/[nivel]/[serie]/[disciplina]/[capitulo]/ebooks/[objeto-de-conhecimento]-exercicios.md`.

**Estrutura de Execução (por Lista de Exercícios):**
1. Acionar a skill **Exercise Creator** fornecendo o e-book teórico aprovado (Sprint 12) como base.
2. Aguardar a geração das 60 questões tagueadas.
3. Submeter o arquivo `.md` resultante ao **Agente Validador de Exercícios**.
4. Corrigir apontamentos (se houver) solicitando refação parcial ao Exercise Creator até obter o parecer `aprovado`.

**Checklist de Validação (por Lista):**
- [ ] O arquivo contém exatas 60 questões (20 básicas, 20 intermediárias, 20 difíceis)?
- [ ] Todas as questões possuem 5 alternativas?
- [ ] As tags HTML `<!-- id: | tipo: | habilidade: | dificuldade: | objeto: -->` estão presentes e corretas antes de cada questão?
- [ ] Os gabaritos apresentam resoluções lógicas passo a passo (especialmente nas difíceis)?
- [ ] O Agente Validador de Exercícios emitiu parecer `aprovado` para cobertura temática, balanceamento e qualidade geral?

**Status Consolidado de Produção e Homologação (Sprint 12.5):**
| Segmento | Volume de Listas | Status |
|---|---|---|
| **Ensino Fundamental 1 (5º Ano)** | 19 listas (1.140 questões) | ✅ 100% Concluído |
| **Ensino Fundamental 2 (6º Ano)** | 23 listas (1.380 questões) | ✅ 100% Concluído e Higienizado (Estrutura Canônica Cap 01 a 23) |
| **Ensino Fundamental 2 (7º Ano)** | 25 listas (1.500 questões) | ✅ 100% Concluído (25 listas homologadas) |
| **Ensino Fundamental 2 (8º Ano)** | 22 listas (1.320 questões) | ✅ 100% Concluído (22 listas homologadas) |
| **Ensino Fundamental 2 (9º Ano)** | 21 listas (1.260 questões) | ✅ 100% Concluído (21 listas homologadas) |
| **Ensino Médio (Volume Único)** | 38 listas (2.280 questões) | ✅ 100% Concluído (38 listas homologadas) |
| **TOTAL GERAL DE MATEMÁTICA** | **148 listas (8.880 questões atômicas)** | 🏆 **Educação Básica 100% Concluída e Pareada** |
| **Ingestão Supabase (Mob.me RAG - Matemática)** | **148 e-books teóricos (6.304 chunks) + 148 listas (9.551 chunks)** | ✅ **100% Ingerido e Vetorizado no PostgreSQL (Fund 1 ao EM)** |
| **Física - 1ª Série (Física I)** | **21 de 21 listas (1.260 questões homologadas)** | 🏆 **100% Concluído e Homologado (Cap 01 ao 21)** |
| **Física - 2ª Série (Física II)** | **19 de 19 listas (1.140 questões homologadas)** | 🏆 **100% Concluído e Homologado (Cap 01 ao 19)** |
| **Física - 3ª Série (Física III)** | **21 de 21 listas (1.260 questões homologadas)** | 🏆 **100% Concluído e Homologado (Cap 01 ao 21)** |
| **TOTAL GERAL DE FÍSICA (Exercícios)** | **61 de 61 listas (3.660 questões homologadas)** | 🏆 **100% Homologado no Muro de Contenção (Exit Code 0, Gabarito 20% A-E, 0 Falhas)** |
| **Ingestão Supabase (Mob.me RAG - Física)** | **130 e-books teóricos (9.270 chunks) + 61 listas de exercícios (3.775 chunks)** | ✅ **100% Ingerido e Vetorizado no PostgreSQL (Teoria e Exercícios)** |
| **Química - 1ª Série (Química I - Exercícios)** | **18 de 18 listas (1.080 questões homologadas)** | 🏆 **100% Concluído e Homologado (Cap 01 ao 18)** |
| **Química - 2ª Série (Química II - Exercícios)** | **16 de 16 listas (960 questões homologadas)** | 🏆 **100% Concluído e Homologado (Cap 01 ao 16)** |
| **Química - 3ª Série (Química III - Exercícios)** | **19 de 19 listas (1.140 questões homologadas)** | 🏆 **100% Concluído e Homologado (Cap 01 ao 19)** |
| **TOTAL GERAL DE QUÍMICA (Exercícios)** | **53 de 53 listas (3.180 questões homologadas)** | 🏆 **100% Homologado no Muro de Contenção (Exit Code 0, Gabarito 20% A-E, 0 Falhas)** |
| **Ingestão Supabase (Mob.me RAG - Química)** | **112 e-books teóricos (3.197 chunks) + 53 listas de exercícios (3.077 chunks) + `quimica` em `available_subjects`** | ✅ **100% Ingerido e Vetorizado no PostgreSQL (Teoria e Exercícios)** |
| **Ciências - 5º Ano (Exercícios)** | **11 de 11 listas (660 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 10 anos)** |
| **Ciências - 6º Ano (Exercícios)** | **13 de 13 listas (780 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 11 anos)** |
| **Ciências - 7º Ano (Exercícios)** | **15 de 15 listas (900 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 12 anos)** |
| **Ciências - 8º Ano (Exercícios)** | **16 de 16 listas (960 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 13 anos)** |
| **Ciências - 9º Ano (Exercícios)** | **17 de 17 listas (1.020 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 14 anos)** |
| **TOTAL GERAL DE CIÊNCIAS (Exercícios)** | **72 de 72 listas (4.320 questões)** | 🏆 **Ensino Fundamental 100% Homologado no Padrão-Ouro (Equilíbrio Matemático 20% A-E, 0 Falhas)** |
| **Ingestão Supabase (Mob.me RAG - Ciências)** | **72 e-books teóricos (2.670 chunks) + `ciencias` em `available_subjects`** | ✅ **100% Ingerido e Vetorizado no PostgreSQL (5º ao 9º Ano)** |
| **Geografia - 5º Ano (Exercícios)** | **9 de 9 listas (540 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 10 anos)** |
| **Geografia - 6º Ano (Exercícios)** | **6 de 6 listas (360 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 11 anos)** |
| **Geografia - 7º Ano (Exercícios)** | **7 de 7 listas (420 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 12 anos)** |
| **Geografia - 8º Ano (Exercícios)** | **8 de 8 listas (480 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 13 anos)** |
| **Geografia - 9º Ano (Exercícios)** | **10 de 10 listas (600 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 14 anos)** |
| **TOTAL GERAL DE GEOGRAFIA (Exercícios)** | **40 de 40 listas (2.400 questões)** | 🏆 **Ensino Fundamental 100% Homologado no Padrão-Ouro (Equilíbrio Matemático 20% A-E, 0 Falhas)** |
| **Ingestão Supabase (Mob.me RAG - Geografia)** | **40 e-books teóricos (1.430 chunks) + `geografia` em `available_subjects`** | ✅ **100% Ingerido e Vetorizado no PostgreSQL (5º ao 9º Ano)** |
| **História - 5º Ano (Exercícios)** | **6 de 6 listas (360 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 10 anos)** |
| **História - 6º Ano (Exercícios)** | **11 de 11 listas (660 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 11 anos)** |
| **História - 7º Ano (Exercícios)** | **11 de 11 listas (660 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 12 anos)** |
| **História - 8º Ano (Exercícios)** | **16 de 16 listas (960 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 13 anos)** |
| **História - 9º Ano (Exercícios)** | **18 de 18 listas (1.080 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, 14 anos)** |
| **TOTAL GERAL DE HISTÓRIA (Exercícios)** | **62 de 62 listas (3.720 questões)** | 🏆 **Ensino Fundamental 100% Homologado no Padrão-Ouro (Equilíbrio Matemático 20% A-E, 0 Falhas)** |
| **Ingestão Supabase (Mob.me RAG - História)** | **62 e-books teóricos (2.356 chunks) + `historia` em `available_subjects`** | ✅ **100% Ingerido e Vetorizado no PostgreSQL (5º ao 9º Ano)** |
| **Língua Portuguesa - 5º Ano (Exercícios)** | **20 de 20 listas (1.200 questões)** | 🏆 **100% Homologado no Padrão-Ouro (20% A-E, sem decoreba, linguagem adequada aos 10 anos)** |
| **Língua Portuguesa - 6º Ano (Exercícios)** | **20 de 20 listas (1.200 questões homologadas - 100% Concluído)** | 🏆 **100% Homologado no Padrão-Ouro (Exit Code 0, 20% A-E, sem decoreba, linguagem para 11 anos)** |
| **Língua Portuguesa - 7º Ano (Exercícios)** | **10 de 20 listas (600 questões homologadas - Lotes 1 e 2 Concluídos)** | ⏳ **50% Homologado no Padrão-Ouro (Cap 01 ao 10 com Exit Code 0, 12 anos)** |
| **Língua Portuguesa - 8º Ano (Exercícios)** | **0 de 20 listas (Aguardando Lotes)** | ⏳ **Pendente** |
| **Língua Portuguesa - 9º Ano (Exercícios)** | **0 de 20 listas (Aguardando Lotes)** | ⏳ **Pendente** |
| **TOTAL GERAL DE LÍNGUA PORTUGUESA (Exercícios)** | **40 de 100 listas (2.400 de 6.000 questões)** | ⏳ **5º e 6º Anos 100% Concluídos e Homologados (Exit Code 0)** |
| **TOTAL GERAL NO SUPABASE (RAG)** | **585 e-books teóricos (26.704 chunks) + 436 listas (20.843+ chunks)** | 🏆 **7 Disciplinas Ativas: Matemática, Física, Química, Ciências, História, Geografia e Cálculo 1** |

---

### Sprint 13 — Produção de SPAs Interativos (Articulação de Trilhas)

> **Complexidade:** 🔴 Alta (múltiplas conversas — 1 conversa por SPA recomendado)  
> **Skill a acionar:** SPA Creator  
> **Pré-requisitos:** E-book teórico e Lista de Exercícios correspondentes concluídos (Sprints 12 e 12.5)

**Objetivo:** Transformar 1 E-book Teórico + 1 Lista de Exercícios em um SPA (Single Page Application) interativo e gamificado de microaprendizagem, com duração de ~100 minutos.

**⚠️ Regra de Articulação:**
- **Entrada:** 2 arquivos (Teoria `.md` + Exercícios `.md` do Objeto de Conhecimento)
- **Saída:** 1 Web App (`index.html` + `styles.css` + `script.js` + assets) em subdiretório próprio (`content/.../[capitulo]/[objeto-de-conhecimento]/`)
- O papel do SPA é **intercalar exercícios na teoria** para consolidar a microaprendizagem. Serão selecionados exatamente **30 exercícios** (10 básicos, 10 intermediários, 10 difíceis) para compor o SPA. Os 30 restantes ficam para revisões.

**⚠️ Conectividade:**
- O SPA Creator lê as **tags HTML** dos exercícios e as converte em atributos **`data-*`** no HTML.
- O `script.js` local do SPA gerencia a experiência de tela e salva a pontuação e a telemetria (`habilidade`, `dificuldade`, `objeto`) no Supabase.

**Estrutura de Execução (por Objeto de Conhecimento):**
1. Confirmar que o e-book teórico e a lista de exercícios estão aprovados
2. Acionar a skill **SPA Creator** com prompt contendo:
   - Caminhos absolutos dos **dois** arquivos fonte
   - Série, disciplina e capítulo
   - Instrução de selecionar exatamente 30 exercícios (10 de cada nível)
   - Instrução de conversão de tags para `data-*` e script de persistência Supabase
   - Geração de imagens via `generate_image` (zero placeholders)
3. Registrar o novo SPA no `window.EDUCAMOB_REGISTRY` da Biblioteca com `duration: '~100 min'`

**Caminho de Destino (Subdiretório Próprio):**
```
content/[nivel]/[serie]/[disciplina]/[capitulo]/[objeto-de-conhecimento]/index.html
content/[nivel]/[serie]/[disciplina]/[capitulo]/[objeto-de-conhecimento]/styles.css
content/[nivel]/[serie]/[disciplina]/[capitulo]/[objeto-de-conhecimento]/script.js
content/[nivel]/[serie]/[disciplina]/[capitulo]/[objeto-de-conhecimento]/*.png
```

**Checklist de Validação (por SPA):**
- [ ] 1 SPA focado inteiramente em 1 Objeto de Conhecimento (Duração ~100 min)?
- [ ] Exatamente 30 exercícios (10 básicos, 10 inter, 10 difíceis) integrados no texto?
- [ ] Leitura de tags HTML dos exercícios para `data-habilidade`, `data-dificuldade` e `data-objeto`?
- [ ] Persistência de notas e telemetria granular no Supabase (`student_progress`) via `script.js`?
- [ ] Zero CDN, zero libs externas (Supabase Client via `shared/` é permitido)?
- [ ] Paleta visual Educamob respeitada (fundo claro, destaque laranja #ff6b00)?
- [ ] Integrado ao `auth-guard.js` e `quiz.js`?
- [ ] Registrado no `EDUCAMOB_REGISTRY` da Biblioteca?
- [ ] Imagens geradas (sem placeholders)?
- [ ] Responsivo (desktop + mobile)?

## 🟢 Fase 6 — Lançamento Gradual (Estudantes Reais)
Esta fase marca o início das atividades oficiais da Escola Digital para estudantes de verdade. O lançamento (roll-out) seguirá uma progressão estrita em Sprints para garantir a estabilidade da plataforma e da telemetria:

### Sprint 14 — Roll-out Nível 1 (Mob.me Autônomo)
> **Status:** ✅ Concluído.  
> **Foco e Entregas Técnicas Consolidadas:**
> 1. **Ativação e Homologação do Índice HNSW no Supabase:** Criação do índice `documents_embedding_hnsw_idx` com pgvector (`m = 16, ef_construction = 32`) na tabela `documents`, eliminando sequential scans sobre 39.280 vetores de 1.024 dimensões e derrubando a latência da busca vetorial `match_documents` de 14,4s (com timeout 57014) para **2,2 segundos** estáveis.
> 2. **Ingestão Vetorial Massiva de Ciências:** Conclusão e ingestão de 72 e-books atômicos de Ciências do Ensino Fundamental (5º ao 9º Ano), adicionando 2.670 novos chunks e elevando a base consolidada do RAG para **39.280 chunks ativos** (Ciências, Matemática, Física, Química e Cálculo 1).
> 3. **Alinhamento Estrito do Ambiente de Testes ao RAG de Produção:**
>    - Extinta qualquer divergência entre laboratório (`prompt_lab.md`) e produção (`prompt_prod.md`). Revogada a permissão de "Ensino Multidisciplinar Aberto"; a Mob.me atende estritamente as matérias homologadas.
>    - Implementação do **Princípio do Mundo Fechado** (*Closed-World Assumption*): proibição absoluta de flashcards, questões ou desafios que cobrem fatos, fórmulas ou curiosidades externas que não constem na teoria apresentada ou no RAG da sessão.
>    - Otimização semântica nas seleções de menu no backend (`main.py`): chamadas numéricas ("1", "5", "6") agora geram queries sintéticas focadas no tópico da sessão (`first_user_topic`), evitando embeddings inflados com texto de menu.
> 4. **Padronização Universal de Menus e Opção 8 Mandatória:** Super Menu de 8 opções estruturado com isolamento vertical estrito (`\n\n`), proibição de opções em linha contínua e presença obrigatória da opção `8️⃣ **Encerrar a sessão de estudo** ⏸️` em 100% dos menus.
> 5. **Otimização de UX no Frontend (`page.tsx`):** Remoção do atributo `disabled={isTyping}` na caixa de texto e injeção de auto-refocus contínuo via `useEffect`, garantindo que o cursor de digitação nunca se perca após o envio de mensagens (Enter).
> 6. **Roteamento Dinâmico de Sub-Prompts por Modo e Padrão SPA na Teoria:** Desmembramento do prompt monolítico em 1 base compartilhada (`base_persona.md`) e 8 sub-prompts especialistas (`modes/`). A opção 1 ("Bora ler!") agora opera no padrão SPA (microaprendizagem, acessibilidade TDAH, blocos arejados e esqueleto pedagógico em 5 seções universais aplicáveis a Exatas, Humanidades e Linguagens). Ajustado o timeout do RAG para 5.0s com busca de 8 chunks densos para a teoria, elevando o output de 32 linhas para mais de 120 linhas aprofundadas com formatação LaTeX rigorosa e menu completo de escolha.
> 7. **Refinamento Pedagógico e UX de Laboratório (27/10/2026):** Blindagem contra falsos tópicos (`INVALID_TOPIC_WORDS`), novo modo de transição para nova conversa (`modo_novo_assunto.md`), tolerância pedagógica a typos e sinônimos nos flashcards, proibição estrita de relatórios precipitados em interrupções precoces de questionários, tipografia Markdown completa no CSS e rolagem automática suave para o topo do e-book teórico no frontend.
> 8. **Imutabilidade Canônica de Menus e Densidade de Leitura 10-15min (27/10/2026 - Rodada 2):** Fixação estrita do Super Menu de 8 opções (proibição de renumeração 1..7 ou omissão de opções), suporte a até 8192 tokens e 12 chunks no RAG para teorias de 10-15 minutos de leitura (~2.000 a 3.000 palavras) e supressão total de elogios artificiais em conclusões parciais.
> 9. **Blindagem e Reversão Mandatória da Sessão Monotemática (28/10/2026):** Reversão imediata de qualquer permissão de troca de assunto na mesma sessão. Sessões no Mob.me são estritamente monotemáticas (	opic imutável após definido). Proibição drástica de ceder a insistências de troca de tema ou de alegar ausência de conteúdo na base; o estudante é firme e polidamente orientado a abrir **+ Nova Conversa** no menu lateral para estudar outro tema, preservando a higienização do histórico e as métricas diagnósticas do portal.
> 10. **Aprimoramento de Formatação GFM e Flashcards Conceituais (28/10/2026 - Rodada 2):** Ativação de 
emark-gfm no frontend Next.js para renderização de tabelas Markdown ricas e reestruturação dos flashcards para foco 100% conceitual voltado à retenção mental (proibição absoluta de múltipla escolha).
> 11. **Teoria Expositiva Pura em 4 Seções e Layout Widescreen (28/10/2026 - Rodada 3):** Remoção da Seção 4 (Casos Práticos) do e-book teórico para preservar a teoria 100% expositiva e autossuficiente (exercícios concentrados nas opções 5 e 6), blindagem contra erros de duplo subscrito no KaTeX e expansão da janela de contexto para layout widescreen (max-w-6xl e IA em w-full), permitindo ampla respiração horizontal para tabelas e fórmulas.
> 12. **Layout Widescreen Seletivo para Teoria e Memorex (28/10/2026 - Rodada 4):** Implementação de renderização condicional de largura no frontend (`page.tsx`) via `isWidescreenContent`. A ampliação horizontal (`max-w-5xl md:max-w-6xl` e bolha `w-full`) é aplicada estritamente aos blocos densos do "Bora Ler!" e "Memorex", garantindo legibilidade perfeita para tabelas ricas e equações KaTeX. Todos os demais modos (Acolhida, menus, Trocando Ideias, Flashcards, Treino Básico, Desafio e SOS) retornaram à largura compacta original (`max-w-3xl`, bolhas a 75%/85% e rodapé em `max-w-4xl`).
> 13. **Blindagem Crítica da Memória de Longo Prazo (28/10/2026 - Rodada 5):** Solucionado vazamento de contexto da tabela `users.long_term_memory` no qual o LLM recitava anotações antigas de Biologia/Ecologia ao abrir uma nova conversa de Química ("Funções Inorgânicas"). A memória foi suprimida em 100% dos modos de navegação (`modo_menu`, `modo_acolhida` e `modo_novo_assunto`), classificada como "USO ESTRITAMENTE SILENCIOSO" nos demais fluxos e blindada por guardrail no `base_persona.md` (proibição absoluta de recitar notas de bastidores ou misturar disciplinas). Banco de dados higienizado no Supabase.
> 14. **Destaque Centralizado de Fórmulas e Desacoplamento do Menu em Janela Independente (28/10/2026 - Rodada 6):** Reações químicas e equações matemáticas elevadas para blocos destacados centralizados (`$$`) com card visual em `globals.css` e auto-promoção de setas de reação no `page.tsx`. Implementado desacoplamento arquitetural do Super Menu via `splitMessageMenu`: ao concluir o "Bora Ler!" ou "Memorex", o texto teórico finaliza em seu card Widescreen (`max-w-6xl`) e o Super Menu de 8 opções é renderizado como uma nova janela/balão de contexto independente no formato compacto padrão (`max-w-3xl`).
> 15. **Feedback Visual Lúdico de Progresso / Loading Interativo (28/10/2026 - Rodada 7):** Implementação de micro-mensagens dinâmicas temáticas no frontend (`page.tsx`) com transição a cada 2,4s enquanto o backend processa buscas vetoriais e inferência de IA. Mensagens contextuais por trilha (Bora ler, Flashcards, Memorex, Treino, Desafio e SOS) humanizam o tempo de espera e reduzem o atrito cognitivo do estudante.
> 16. **Blindagem contra Extrapolação de Pegadinhas e Proteção de Tabelas (28/10/2026 - Rodada 8):** Instituído guardrail drástico nos prompts (`base_persona.md` e `modo_teoria.md`) proibindo o LLM de extrapolar o tema ativo com pegadinhas de capítulos futuros ou físico-química avançada (como $K_w$ e pH a 100°C em aulas de Funções Inorgânicas). Corrigida quebra da tabela analítica no frontend (`page.tsx`): sanitizador agora protege células de tabelas Markdown contra quebras de linha `\n\n`, mantendo equações inline intactas dentro de colunas.
> 17. **Sincronia do Ciclo de Loading e Janela Mínima de Progresso (28/10/2026 - Rodada 9):** Identificado que a altíssima velocidade do DeepSeek (TTFB de ~270ms) desligava o `isTyping` antes do primeiro ciclo de 2,4s disparar. Implementada janela mínima garantida de 3,9s com rotação a cada 1,3s para seleção de trilhas pedagógicas, permitindo que o aluno veja a evolução de 3 mensagens temáticas enquanto o stream é bufferizado em segundo plano.

### Sprint 15 — Roll-out Nível 2 (Integração Mob.me + Revisa)
> **Foco:** Liberação do módulo de testes rápidos. Validação do consumo de exercícios curtos e diretos e sincronização primária de telemetria de notas no Supabase.

### Sprint 16 — Roll-out Nível 3 (Carga Pesada com Biblioteca de SPAs)
> **Foco:** Inserção da carga pesada. Integração dos aplicativos interativos longos (~100min) e verificação intensa de SLAs do banco de dados perante múltiplas requisições sequenciais.

### Sprint 17 — Roll-out Nível 4 (Ecossistema Completo + Dashboard)
> **Foco:** Liberação da última engrenagem. O painel "Meu Desempenho" entra no ar, validando a apresentação visual dos Analytics e fechando o ciclo pedagógico visível para o aluno.

---

## 🟣 Fase 7 — Melhorias Contínuas (Backlog Futuro) [SEMPRE ÚLTIMA]
> Repositório de ideias tecnológicas e aprimoramentos arquitetônicos que foram pontuados ao longo do projeto, mas que não são bloqueantes para o MVP (Mínimo Produto Viável). Esta fase é permanentemente a última do plano e recebe novos itens conforme surgem.

| Sprint | Módulo / Melhoria | Descrição Técnica |
|--------|-------------------|-------------------|
| **18** | ✅ Roteamento Multi-LLM | Fallback inteligente nativo implementado. Utiliza DeepSeek-V4-Flash via DeepInfra como redundância primária rápida para a API do Google Gemini. O "Teste do Fim do Mundo" (1000 RAGs únicos simultâneos com 100% de Cache Miss) atestou 1000/1000 sucessos (0 falhas) com TTFB médio das piores 100 requisições em apenas 5.09s. |
| **19** | Automação Ativa (Push) de Relatórios | Criar um "Cron Job" no FastAPI que rode toda sexta-feira às 18h, gere relatórios semanais de alunos automaticamente e dispare proativamente no WhatsApp das famílias (Evolution API). |
| **20** | Painel Administrativo de Prompts | Migrar os prompts base (o "Prompt Socrático" e o "Prompt de Relatórios") do código rígido (hardcoded) para uma tabela do Supabase, permitindo edição via interface web sem mexer no backend. |
| **21** | E-mail Customizado Oficial (SMTP) | Configurar um provedor SMTP (como Resend ou SendGrid) no Supabase Auth (*Enable Custom SMTP*) para que os e-mails de recuperação de senha usem a marca e domínio oficial da escola. |
| **22** | Hub de Lives | Retomar o Sprint 5 que foi paralisado. Construir a área de transmissões ao vivo dentro da plataforma principal para centralizar as aulas online. |
| **23** | Painel Pedagógico Institucional (Escolas) | Sistema completo (com controle de acesso para Professores, Coordenadores e Diretores) permitindo prescrever estudos e metas de revisão com prazos estabelecidos (para alunos individuais ou turmas inteiras), além de acompanhar dashboards de resultados em tempo real. |
| **24** | Painel Parental (Home Study) | Versão do painel dedicada aos pais/responsáveis. Permite designar tarefas e roteiros específicos de estudo para seus próprios filhos e visualizar gráficos claros dos resultados obtidos. |
| **25** | Script de Validação de YAML | Criar script automatizado (Python/Node) que valide todos os campos obrigatórios do YAML frontmatter, verifique links internos entre arquivos, confira cobertura de habilidades BNCC por disciplina/série e garanta contagem mínima de atividades por arquivo. |
| **26** | NPS do Aluno (Satisfação) | Implementar micro-survey (1 pergunta, escala 0-10) nos SPAs após conclusão de trilha. Resultado salvo em tabela `student_feedback` no Supabase (`user_id`, `score`, `touchpoint`, `comentario`, `timestamp`). Cálculo: `NPS = % Promotores (9-10) − % Detratores (0-6)`. Custo zero (popup CSS + INSERT no Supabase). |
| **27** | Manutenção Contínua da Base Teórica | Cadência de revisão: semestral (atualidade de dados e referências), anual (incorporar novas questões ENEM/provas oficiais), sob demanda (corrigir erros reportados por alunos via Mob.me, adicionar tópicos solicitados com frequência). |
| **28** | Códigos de Desbloqueio (Vouchers/Turmas) | Injeção de contexto RAG via código no Mob.me. O aluno digita uma chave (ex: '#REC-MAT-01'), o FastAPI valida no Supabase e carrega e-books específicos, alterando o system prompt da IA. Atua como MVP tático para prescrição pedagógica. |
| **29** | Refatoração Assíncrona e Connection Pooling | Converter todo o código do FastAPI (`main.py` e `memory.py`) para `async def / await`, implementando um cliente Supabase Assíncrono (`ClientAsync`) e Pool de Conexões para suportar milhões de acessos sem bloquear o Event Loop ou sobrecarregar a camada HTTP (Cloudflare). |
| **30** | Micro-UX Lúdica de Carregamento | Ciclo de feedback de progresso pedagógico com rotação a cada 3s exclusivo para trilhas densas (Bora ler, Flashcards e Memorex), amortecendo o tempo de geração com transparência sem atrasar interações curtas.
| **31** | Padrão-Ouro KaTeX e Memorex | Pipeline robusto de parser multi-camada para blocos display KaTeX (isolamento de reações em listas e parágrafos sem quebrar tabelas) e novo template arquitetural de alto padrão para o Memorex com Quadro Síntese Panorâmico obrigatório e Callouts de Dicas de Ouro.
| **32** | Badges Glassmorphism para Menus | Substituição dos emojis nativos azuis por botões numéricos com efeito glass sofisticado em laranja Educamob (#ff6b00), dotados de reflexo interno, blur translúcido e gatilho interativo ao clique direto.
| **33** | ✅ Desambiguação Curricular Prévia | Bloqueio rigoroso de Super Menu para termos amplos/polissêmicos ('Bernoulli', 'Newton', 'Cinemática'). Apresentação imediata de 3 ramificações didáticas na Acolhida e liberação do menu somente após a confirmação do foco exato, eliminando interrupções tardias na Teoria.
| **34** | ✅ Protocolo de Dupla Regra Independente para Desambiguação | Implementação do protocolo dual (Regra 1: Colisão Interdisciplinar; Regra 2: Sobrecarga Curricular >= 3 capítulos BNCC na mesma matéria). Ordenação decrescente por comprimento de trigger e analista curricular dinâmico via DeepSeek LLM em tempo real com bloqueio absoluto do Super Menu no Turno 1.
| **35** | ✅ Árbitro Curricular Semântico LLM-First e Dedução Automática de Disciplina | Substituição da busca cega por substrings pelo Árbitro Semântico DeepSeek em tempo real com cache exato (0ms). Avaliação universal de Regra 1 e Regra 2 sem manutenção de palavras-chave, dedução transparente de disciplina e títulos de sessão via DeepInfra.
| **36** | ✅ Protocolo de Desambiguação Curricular em Cascata e Blindagem de Match | Implementação do re-check recursivo de densidade curricular no Step 1.5, garantindo que temas ramificados (ex: "Funções Matemáticas") abram a desambiguação de Nível 2 em vez de liberar o Super Menu prematuramente. Expurgamento de palavras-pai no match de texto e tratamento de desistência de tema.
| **37** | ✅ Blindagem de Disciplinas Fora do Escopo, Aliases de Funções Químicas e Auto-Scroll ao Início da IA | Implementação do guardrail de Closed-World Assumption no Árbitro Curricular (recusa imediata e acolhedora de matérias fora do acervo oficial como Português/Humanas sem envenenar a sessão com topic indevido); inclusão de aliases canônicos para Funções Químicas no cache em memória; e auto-scroll inteligente no frontend para o início da resposta da IA ao término da digitação. |
| **38** | ✅ Auditoria Integral do System Prompt Modular (7 Correções) | Eliminação do loop infinito de desambiguação (fallthrough para o Árbitro Curricular), sincronia 100% dinâmica de disciplinas com available_subjects do Supabase, teto máximo de 2 níveis na cascata, stream de 0ms no Super Menu, sanitização de barras invertidas em cabeçalhos de tabela e uso estrito das listas oficiais -exercicios.md com reutilização de banco. |
| **39** | ✅ Auto-Heal e Formatação Estrita de Fórmulas Químicas ($, $, $, $) | Eliminação do underscore cru em fórmulas químicas exibidas em Markdown puro (ex: H_2S), auto-cura quádrupla no frontend para KaTeX inline math e diretriz mandatória em todos os sub-prompts proibindo negrito sem cifrão (**HCl**, **H_2S**). |
| **40** | ✅ Arquitetura de System Prompt — Menu Canônico de 6 Trilhas | Migração para o Menu Canônico de 6 Trilhas (1. Aprender/Microciclos, 2. Praticar 5+5+5, 3. Revisar/Flashcards, 4. Resumir/Memorex, 5. Resolve questão, 6. Finalizar), contrato de RAG como Fonte Única, aliases legados e carregamento RAG balanceado nos 3 níveis de dificuldade. |
| **41** | ✅ Proteção de Ambientes Matemáticos e Imunização KaTeX ($, $, Frações) | Tokenização preliminar de blocos  e $ no frontend, impedindo injeção indevida de cifrões aninhados dentro de equações display e blindando variáveis de física/matemática com índice zero contra falsos positivos químicos. |
| **42** | ✅ Calibração de Identidade e Tom de Voz da Mob.me (Conversacional e Empático) | Transição do tom estritamente formal/sóbrio para uma identidade de mentora e companheira de estudos paciente, com linguagem conversacional e didática ativa ("como no intervalo da escola"), equilibrando acolhimento caloroso com tolerância zero a bajulações ou elogios artificiais. |
| **43** | ✅ Blindagem de Respostas Pedagógicas contra Seletor de Menus e Formatação de Alternativas (Uma por Linha) | Correção de interceptação espúria onde respostas curtas de alunos (ex: número "5" ou letras) em modos de estudo ativos acionavam indevidamente opções de menu; distinção de estado para comandos de trilha; auto-heal quádruplo no frontend e diretriz estrita nos prompts garantindo que cada alternativa de múltipla escolha fique sempre isolada em sua própria linha com dupla quebra (`\n\n`). |
| **44** | ✅ Suíte de Avaliação Estatística Automatizada da Mob.me (`eval_suite`) e Ciclo de Evolução Orientado a Dados | Construção do motor de testes multi-turno (`services/mobme-api/evals/`) combinando validação determinística, compilador real KaTeX headless (`throwOnError: true`), auditoria LLM-as-a-Judge (DeepSeek-V4-Flash a T=0.0) e Intervalos de Confiança de Wilson (95%). Elevação comprovada da taxa de aprovação global de 66,67% (Baseline) para 97,37% (100% nas métricas determinísticas, KaTeX, alternativas 1 por linha, protocolo e integridade RAG) após identificação e correção de 5 casos de borda. |
| **45** | ✅ Suíte Avançada de Estresse: RAG Boundaries, Endurance em Sessões Longas e Multimodalidade | Implementação de bateria de 30 turnos de alta complexidade cobrindo os 3 riscos práticos residuais: (1) Teste de limites e lacunas do RAG com recusa graciosa e zero alucinação externa; (2) Endurance em sessões longas com criação do Orquestrador Determinístico de Progresso de Rodada no backend (garantindo monotonicidade estrita 1..15 e zero perda de contexto); (3) Visão computacional multimodal com gerador sintético de imagens via Pillow e fallback automático resiliente para Qwen-VL via DeepInfra. Homologação final com 30/30 aprovações (100,00%, IC 95% Wilson: `[88,65%, 100,00%]`). |
| **46** | ✅ Homologação do Lote 1 de Exercícios de História (5º Ano) | Produção e validação sistemática de 6 listas atômicas (360 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E e zero decoreba). |
| **47** | ✅ Homologação do Lote 2 de Exercícios de História (6º Ano) | Produção e validação sistemática de 11 listas atômicas (660 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E e zero decoreba). |
| **48** | ✅ Calibração e Refinamento do Menu Canônico de 6 Trilhas | Atualização e simplificação das nomenclaturas das 6 opções do Menu Canônico (1. Aprender📚, 2. Praticar📝, 3. Flashcards 🃏, 4. Resumo 🧠, 5. Enviar questão 🖼️, 6. Finalizar ⏸️) com sincronização no template mandatório, state machine do FastAPI, auto-heal de badges no frontend Next.js e suíte estatística de testes. |
| **49** | ✅ Homologação do Lote 3 de Exercícios de História (7º Ano) | Produção e validação sistemática de 11 listas atômicas (660 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E e zero decoreba). |
| **50** | ✅ Solução Híbrida Inteligente de Envio Multimodal e Retomada de Trilha | Roteamento automático de imagens enviadas fora da opção 5 do menu: detecção contextual de rascunhos de cálculo vs. novas dúvidas, preservação do estado de estudo ativo em `paused_track`, desvio transparente de fluxo sem reexibir menus redundantes (zero fricção) e retomada automática do progresso prévio ("voltar/continuar"). |
| **51** | ✅ Promoção Oficial do System Prompt v2.0.0 — Codinome: "Mob.me 6 Trilhas" | Promoção formal do novo system prompt e motor modular para o ambiente de produção após homologação de 100% (34/34 turnos) na Suíte Estatística Avançada. Compilação consolidada de `prompt_prod.md`, ativação de arquitetura modular para produção no FastAPI (`main.py`) e auditoria limpa contra o guardrail de pre-commit. |
| **52** | ✅ Ingestão Vetorial e Liberação de Geografia e História na Mob.me | Vetorização de 102 novos e-books teóricos (40 de Geografia [1.430 chunks] e 62 de História [2.356 chunks]), registro de `geografia` e `historia` em `available_subjects` no Supabase, sincronização da máquina de estados e do Árbitro Curricular no FastAPI (`main.py`) e reload em tempo real nos ambientes local e de produção (Oracle Cloud). |
| **53** | ✅ Aposentadoria Definitiva do Prompt Legado e Homologação do System Prompt Oficial v2.0.0 | Arquivamento formal do prompt monolítico legado (`prompt_lab.md`) e dos 7 modos v1 em `prompts/archive_v1/`, redação master coesa e unificada de `prompt_prod.md` (v2.0.0 — 'Mob.me 6 Trilhas'), unificação do motor de prompts no FastAPI (`main.py`) sem desvios legados e sincronização integral em produção (Oracle Cloud). |
| **54** | ✅ Sincronização do Frontend de Produção (GitHub Pages), Badges de Menu e Hierarquia Visual de Textos | Diagnóstico e correção do descompasso de build entre o código-fonte (`apps/mobme-source`) e o deploy estático servido pelo GitHub Pages (`apps/mobme/` defasado desde setembro/2026). Resolução da supressão de números em listas (`<ol>`) pelo reset do Tailwind CSS, estilização de títulos de microciclos (`###`), normalização de opções com negrito e exportação estática de produção com sincronização direta no repositório. |
| **55** | ✅ Padrão Editorial E-book para Microciclos, Cards de Objetivo/Checagem e Layout Widescreen Universal | Implementação da formatação visual rica de e-book para a Trilha Aprender: expansão widescreen incondicional para microciclos (`max-w-5xl md:max-w-6xl w-full`), banners de cabeçalho em largura total (`w-full`), cards estilizados para Objetivo (`🎯 Objetivo:`) e Checagem (`✍️ Checagem:`), suporte completo a tabelas e KaTeX display, e enriquecimento pedagógico do prompt da Trilha 1 (`prompt_prod.md` e `modo_aprender.md`) com padrão livro-texto Educamob. |
| **56** | ✅ Cards Interativos de Alternativas (A-E), Banners de Microciclo e Callouts Pedagógicos | Transformação das alternativas de múltipla escolha (`a)` a `e)`) em cards interativos clicáveis com efeito hover/active e badges de letras (`[ A ]` a `[ E ]`), resolução do isolamento visual da pergunta de checagem, estilização de notas pedagógicas (`💡`, `Pense assim:`, `Importante:`) e cabeçalho de microciclo em banner gradiente de abertura de capítulo. |
| **57** | ✅ Suíte de Formatação Premium e Interatividade Total (6 Trilhas, Microciclos e Alternativas) | Implementação dos cards interativos clicáveis para as 6 Trilhas do Menu (1️⃣ Aprender a 6️⃣ Finalizar) com subtítulos e badges de navegação em um toque; auto-heal robusto no sanitizador de texto para microciclos, objetivos, checagens e callouts pedagógicos; obrigatoriedade de 4 alternativas de múltipla escolha (a-d) em `modo_aprender.md` na Oracle Cloud; e compilação/deploy em produção no GitHub Pages. |
| **58** | ✅ Supressão de Jargão Pedagógico (Remoção da Palavra 'Microciclo') | Expurgamento total das palavras 'Microciclo' e 'Miniciclo' de todas as interfaces e textos voltados ao estudante na Trilha Aprender. Ajuste nos prompts (`modo_aprender.md`, `prompt_prod.md`, `modo_conclusao.md`) para usar cabeçalhos diretos de tópicos (`### [Título do Conceito]`), remoção de injeções forçadas de jargão no `main.py`, sanitização regex preventiva no frontend Next.js e banner visual renomeado para '● Tópico de Estudo', com deploy em produção no VPS e GitHub Pages. |
| **58** | ✅ Homologação do Lote 4 de Exercícios de História (8º Ano) | Produção e validação sistemática de 16 listas atômicas (960 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E e zero decoreba). |
| **59** | ✅ Homologação do Lote 5 de Exercícios de História (9º Ano) e Fechamento Integral da Disciplina (62 de 62 Listas / 3.720 Questões no Padrão-Ouro) | Produção e validação sistemática de 18 listas atômicas (1.080 questões no Padrão-Ouro). Conclusão de 100% das 62 listas de História do Ensino Fundamental (3.720 questões atômicas) cobrindo todas as 109 habilidades BNCC (`EF05HI01` a `EF09HI36`), com aprovação unânime e Exit Code 0 no `validador_educamob.py`. |
| **60** | ✅ Blindagem Determinística da Trilha Praticar (Orquestrador de Itens, Pré-Validação de Gabarito e Integridade RAG) | Resolução de anomalias no Modo Praticar da Mob.me: substituição da geração livre/alucinação de questões pelo extrator determinístico de 15 itens (`extract_round_items`: 5 Fáceis, 5 Médias e 5 Difíceis) diretamente dos arquivos RAG `-exercicios.md`; parser universal de respostas do aluno (`parse_student_answer`); eliminação do feedback esquizofrênico ("Quase lá... você acertou") através de pré-validação determinística no backend com injeção do veredito `[SISTEMA_AVALIACAO: ACERTOU/ERROU]`; injeção estrita da questão verbatim; e desambiguação de arquivos por série/maturidade curricular em `resolve_exercise_file_for_topic` (priorizando 9º Ano/Ensino Médio sobre capítulos introdutórios do 8º Ano). |
| **61** | ✅ Correção Crítica de Formatação de LaTeX, Imunização contra Picotamento de Sentenças e Distinção de Gabarito em Feedbacks | Resolução de anomalias visuais rastreadas na sessão de Tabela Periódica (`nepovski@gmail.com`): reposicionamento de normalizações de blocos pedagógicos no sanitizador global antes da segmentação por tokens math (eliminando quebras espúrias em fórmulas LaTeX inline como `$Z$`), implementação de verificação estrita `isGabarito` para transformar alternativas explicativas de erro em cards verdes de confirmação (evitando botões falsos de teste), supressão total residual do termo 'microciclo' em todos os prompts do backend e layout de e-book enriquecido. |
| **62** | ✅ Agente Auditor de Conversas Mob.me, Tratamento de Respostas Holísticas ("Todos") e Auto-Roteamento de Questões | Criação da skill oficial `auditor-conversas-mobme` e auditoria forense em 17 sessões (238 mensagens) da tarde de 05/11/2026. Correção dos 3 desvios sistêmicos identificados: (1) Tratamento determinístico de respostas holísticas (`is_holistic_selection`) durante a desambiguação ("todos", "tudo"), erradicando o fallthrough espúrio de disciplina 'Indefinida'; (2) Auto-roteamento de questões completas (`is_question_submission`) diretamente para a Trilha 5 (`modo_resolve_questao`), eliminando loops no menu; (3) Mandato de Progressão Pedagógica (do Fundamento ao Avançado) em `modo_aprender.md` e `prompt_prod.md`, impedindo que temas teóricos iniciem por associações avançadas antes do conceito elementar. |
| **63** | ✅ Implementação da Arquitetura Híbrida de Auditoria Noturna (Sentinela VPS 24/7 + Arquiteto Antigravity) | Construção do ecossistema de auditoria autônoma contínua: (1) Agente 1 (Sentinela Noturno em `sentinela_mobme.py`) com execução diária agendada via cron na Oracle VPS (02:00 BRT), auditando 100% das mensagens com pirâmide de prioridades (P0 Roteamento, P1 System Prompt Compliance, P2 KaTeX/Formatação, P3 Atrito Aluno) e cálculo de Intervalos de Confiança de Wilson 95%; (2) Endpoints REST `/api/audits/latest` e `/api/audits/summary` integrados ao FastAPI da Mob.me; (3) Agente 2 (Arquiteto Reparador) configurado no Antigravity via sidecar agendado (08:30 BRT) e skill oficial `auditor-conversas-mobme` com mandato de testes estatísticos de regressão. |
| **64** | ✅ Evolução do Agente 1 (Sentinela Noturno) — Auditoria Semântica, Detecção de Colisão em Desambiguações, RAG Cruzado e Integridade de Habilidades | Upgrade estrutural do Sentinela Noturno (`sentinela_mobme.py`): adição de detectores de prioridade P0 para colisão de menus em desambiguação de temas (`DESAMBIGUACAO_COLISAO_MENU`), falsos bloqueios de disciplinas homologadas (`FALSO_BLOQUEIO_DISCIPLINA`), injeção cruzada de acervo e habilidades incompatíveis com o tema (`RAG_DISCIPLINA_CRUZADA` - alertando quando questões de habilidades BNCC, prefixos curriculares ou acervo diferem da disciplina/tema da sessão) e abandono de sessões em cascata (`SESSAO_ABORTADA_CASCATA`); detectores P1 para "gaslighting" pedagógico (`GASLIGHTING_PEDAGOGICO`) e amnésia de temas ativos (`AMNESIA_TEMA_SESSAO`); e detector P2 para excesso de alternativas (`EXCESSO_ALTERNATIVAS_QUIZ` com 5 opções em vez de 4). Imunização de falsos positivos KaTeX em fórmulas de física/matemática e deploy em produção na Oracle Cloud VPS com 87 falhas mapeadas em tempo real. |
| **62** | ✅ Ingestão Vetorial Massiva e Sincronização Integral de 100% das Listas de Exercícios na Mob.me (436 de 436 Listas / 26.160 Questões no Supabase pgvector) | Desenvolvimento do pipeline unificado de ingestão de exercícios (`ingest_exercicios.py`), geração de embeddings em lote único via DeepInfra (`BAAI/bge-m3`) e inserção direta em micro-lotes com auto-retry contra timeouts de HNSW (código 57014). Ingestão completa de 174 novas listas de Ciências (72), Geografia (40) e História (62) somadas à atualização e sincronização das 262 listas recalibradas de Matemática (148), Física (61) e Química (53). 100% das 436 listas e 26.160 questões atômicas agora indexadas e ativas para recuperação semântica RAG em produção. |
| **65** | ✅ Resolução Sistêmica de Colisão de Menus, Blindagem Anti-Vazamento RAG Cruzado e Anti-Gaslighting (Agente 2) | Implementação cirúrgica de reparos pelo Agente 2 (Arquiteto Reparador): (1) Correção da colisão de números em badges no frontend (`page.tsx`) e backend (`main.py`), enviando estritamente o número da opção em desambiguações de temas sem sobrecarregar com rótulos de trilha; (2) Blindagem de disciplina e série em `resolve_exercise_file_for_topic`, impedindo categoricamente vazamento cruzado de acervo (ex: exercícios de Matemática do 5º ano em sessões de Física do Ensino Médio); (3) Sincronização e upload do acervo de Ensino Médio (`content/medio` com 433 arquivos) no disco da Oracle Cloud VPS; (4) Eliminação definitiva do falso bloqueio de disciplinas homologadas (Física, Matemática, etc.) em saudações informais e falas conversacionais; (5) Transição fluida e direta para a Teoria ("teoria", "sem flashcards, teoria") sem loops no menu; (6) Mandato estrito anti-gaslighting e de imutabilidade do tema ativo nos prompts (`prompt_prod.md`, `base_persona.md`, `modo_praticar.md`); (7) Recompilação do frontend Next.js com Turbopack (Exit Code 0), sincronização com `apps/mobme` e homologação em produção na Oracle VPS. |
| **66** | ✅ Banimento da Regra de 4 Alternativas e Padronização Mandatória de 5 Alternativas (A-E) em Todo o Ecossistema da Mob.me | Banimento definitivo da antiga regra de 4 alternativas (`a-d`) e estabelecimento do padrão único de 5 alternativas (`a, b, c, d, e`) para toda e qualquer questão ou checagem de múltipla escolha da plataforma: (1) Atualização dos prompts de sistema (`modo_aprender.md` e `prompt_prod.md`) para exigir 5 alternativas (A-E); (2) Evolução do Agente 1 (`sentinela_mobme.py`) com nova regra `DEFICIT_ALTERNATIVAS_PADRAO_5` autuando questões com menos de 5 alternativas e expurgando falso-positivos em exercícios homologados; (3) Atualização da skill oficial `auditor-conversas-mobme`; (4) Deploy sincronizado via SCP e Docker no container `mobme-api` na Oracle Cloud VPS (`137.131.163.113`) com 100.0% de conformidade estatística. |
| **67** | ✅ Diretriz Universal de Linguagem Simples, Direta e Adequada à Idade (5º Ano ao Ensino Médio) | Implementação das 3 Ações Estruturais para separação de papéis entre os e-books (fonte densa e acadêmica do RAG) e a camada do estudante (Mob.me + Exercícios): (1) Reforma dos System Prompts da Mob.me (`base_persona.md`, `prompt_prod.md`, `modo_aprender.md`, `modo_resumir.md`) com Regra de Tradução Pedagógica Obrigatória e injeção dinâmica de calibragem linguística por série no `main.py`; (2) Atualização das skills (`exercise-creator`, `agente-validador-exercicios`) e implantação das Travas 9.1, 9.2 e 9.3 no `validador_educamob.py` (bloqueando "concursês"/pedantismo do 5º Ano ao Ensino Médio e extrapolação etária por série no Fundamental e Médio); (3) Higienização global e homologação (Exit Code 0) de todas as 441 listas de exercícios do acervo + recalibragem integral das 5 listas do Lote 1 de Língua Portuguesa do 5º Ano para a faixa etária de 10 anos. |
| **68** | ✅ Homologação do Lote 2 de Exercícios de Língua Portuguesa (5º Ano — Capítulos 06 ao 10) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 10 anos de idade, fechando 50% do 5º Ano). |
| **69** | ✅ Homologação dos Lotes 3 e 4 de Exercícios de Língua Portuguesa (5º Ano — Capítulos 11 ao 20) e Fechamento Integral do 5º Ano (20 de 20 Listas / 1.200 Questões) | Produção e validação sistemática das 10 listas finais do 5º Ano (600 questões nos Lotes 3 e 4, totalizando 20 listas e 1.200 questões atômicas no 5º Ano), 100% aprovadas com Exit Code 0 no `validador_educamob.py` e linguagem calibrada para 10 anos de idade. |
| **70** | ✅ Homologação do Lote 1 de Exercícios de Língua Portuguesa (6º Ano — Capítulos 01 ao 05) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 11 anos de idade, cobrindo Fonética, Morfologia, Estrutura de Palavras, Substantivos e Adjetivos). |
| **71** | ✅ Homologação do Lote 2 de Exercícios de Língua Portuguesa (6º Ano — Capítulos 06 ao 10) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 11 anos de idade, cobrindo Artigos/Numerais, Verbos [Tempos/Modos], Pronomes/Coesão, Sintaxe I [Frase/Oração/Período] e Sintaxe II [Sujeito/Predicado/Concordância]). |
| **72** | ✅ Homologação do Lote 3 de Exercícios de Língua Portuguesa (6º Ano — Capítulos 11 ao 15) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 11 anos de idade, cobrindo Pontuação Sintática/Expressiva, Semântica [Sinonímia/Homonímia/Paronímia/Ambiguidade], Campo Jornalístico [Notícia/Lide/Pirâmide Invertida/Fato vs Opinião], Cultura Digital [Hipertexto/Multimodalidade/Curadoria] e Opinião do Leitor [Carta do Leitor/Comentários/Netiqueta/Moderação Ética]). |
| **73** | ✅ Homologação do Lote 4 de Exercícios de Língua Portuguesa (6º Ano — Capítulos 16 ao 20) e Fechamento Integral do 6º Ano (20 de 20 Listas / 1.200 Questões) | Produção e validação sistemática das 5 listas finais do 6º Ano (300 questões no Lote 4, totalizando 20 listas e 1.200 questões atômicas no 6º Ano), 100% aprovadas com Exit Code 0 no `validador_educamob.py`, linguagem calibrada para 11 anos de idade, cobrindo Textos Publicitários/Propaganda, Estudo e Pesquisa [Resumo/Infografia], Vida Pública [Reivindicatórios/Normativos], Narrativas Literárias [Mitos/Lendas/Aventura] e Poesia [Formas Fixas/Versos Livres/Figuras de Linguagem]. |
| **74** | ✅ Homologação do Lote 1 de Exercícios de Língua Portuguesa (7º Ano — Capítulos 01 ao 05) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 12 anos de idade, cobrindo Predicação/Transitividade Verbal, Termos Integrantes [Objeto Direto e Indireto], Termos Acessórios I [Adjunto Adnominal], Termos Acessórios II [Adjunto Adverbial] e Vozes Verbais [Ativa, Passiva e Reflexiva]). |
| **75** | ✅ Homologação do Lote 2 de Exercícios de Língua Portuguesa (7º Ano — Capítulos 06 ao 10) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 12 anos de idade, cobrindo Concordância Nominal [Casos Especiais], Concordância Verbal [Casos Particulares e Impessoais], Semântica [Hiperonímia, Hiponímia e Coesão Referencial], Grande Reportagem [Jornalismo Investigativo, Polifonia e Infografia] e Humor Gráfico [Charge, Cartum, Caricatura e Crítica Social]). |
| **76** | ✅ Atualização Cadastral dos Estudantes no Mob.me, Sincronização Curricular em `public.users` e Auto-Heal em `memory.py` | Importação e deduplicação da planilha de estudantes; cadastramento dos novos alunos no Supabase Auth com senhas padrão DDMMAAAA; enriquecimento de metadados; sincronização inédita do campo `grade_level` na tabela `public.users` para 100% dos alunos, habilitando a calibração curricular e reranking de RAG; atualização do `memory.py` com rotina resiliente de preenchimento automático de série; consolidação do `beta_testers.csv` com 33 alunos auditados e validados. |
| **77** | ✅ Homologação do Lote 3 de Exercícios de Língua Portuguesa (7º Ano — Capítulos 11 ao 15) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 12 anos de idade, cobrindo Gênero Entrevista Jornalística, Ética Editorial e Análise da Mídia, Campo da Vida Pública: Carta de Reclamação e Ouvidoria Cidadã, O Debate Regrado e a Mesa-Redonda, e Textos Legais: Estatuto da Igualdade Racial e Legislação Antidiscriminatória). Totalizando 15 de 20 listas e 900 questões homologadas no 7º Ano (75% da série). |
| **78** | ✅ Homologação do Lote 4 de Exercícios de Língua Portuguesa (7º Ano — Capítulos 16 ao 20) e Fechamento Integral do 7º Ano (20 de 20 Listas / 1.200 Questões) | Produção e validação sistemática de 5 listas atômicas (300 questões no Lote 4, totalizando 20 listas e 1.200 questões atômicas no 7º Ano), 100% aprovadas com Exit Code 0 no `validador_educamob.py`, linguagem calibrada para 12 anos de idade, cobrindo Liberdade de Expressão e Marco Civil da Internet, Relatório de Experimento e Seminário Científico, Campo Literário: Conto Policial/Terror/Enigma, Crônica Literária/Humorística e Texto Dramático/Teatral. Fechamento integral do 7º ano (60 de 100 listas de Língua Portuguesa homologadas). |
| **79** | ✅ Homologação do Lote 1 de Exercícios de Língua Portuguesa (8º Ano — Capítulos 01 ao 05) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 13 anos de idade, cobrindo Período Composto por Coordenação, Orações Subordinadas Substantivas, Orações Subordinadas Adjetivas e Pontuação, Regência Verbal e Nominal/Crase, e Colocação Pronominal: Próclise/Ênclise/Mesóclise). Totalizando 65 de 100 listas e 3.900 questões homologadas em Língua Portuguesa. |
| **80** | ✅ Homologação do Lote 2 de Exercícios de Língua Portuguesa (8º Ano — Capítulos 06 ao 10) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 13 anos de idade, cobrindo Sistema Verbal: Subjuntivo/Imperativo/Correlação, Morfologia e Formação de Palavras: Derivação e Composição, Figuras de Pensamento e de Sintaxe, O Artigo de Opinião e Persuasão Ética, e O Editorial Jornalístico e a Linha Editorial). Totalizando 70 de 100 listas e 4.200 questões homologadas em Língua Portuguesa (50% do 8º ano concluído). |
| **81** | ✅ Homologação do Lote 3 de Exercícios de Língua Portuguesa (8º Ano — Capítulos 11 ao 15) | Produção e validação sistemática de 5 listas atômicas (300 questões no Padrão-Ouro: 20 básicas, 20 intermediárias, 20 difíceis com Etapas 1 e 2, gabaritos matematicamente equilibrados em 20% A-E, zero decoreba e linguagem 100% adequada aos 13 anos de idade, cobrindo A Carta do Leitor e o Debate Público [Cap 11], A Resenha Crítica e a Mediação Cultural [Cap 12], O Estatuto da Criança e do Adolescente e a Linguagem Legal [Cap 13], Textos Reivindicatórios: Manifesto Cívico, Abaixo-Assinado e Petição [Cap 14], e Publicidade, Propaganda e Consumo Consciente [Cap 15]). Totalizando 75 de 100 listas e 4.500 questões homologadas em Língua Portuguesa (75% do 8º ano concluído). |
| **82** | ✅ Ciclo Diário de Monitoramento e Melhoria da Mob.me: Resolução de Loop de Menu, Rerank Curricular por Série e Imunização Térmica | Auditoria noturna e diurna homologada com o usuário: (1) Roteador flexível com suporte a delimitadores naturais e mapeamento de intenção em `main.py`, eliminando loops de menu quando o aluno digita números acompanhados de pontuação ou observações; (2) Algoritmo `grade_score_theo` no RAG de `main.py`, blindando estudantes do Ensino Fundamental contra a invasão de e-books do Ensino Médio; (3) Sanitização de unidades de temperatura no `sentinela_mobme.py`, eliminando falsos positivos em (0°C); (4) Deploy homologado na Oracle Cloud VPS com 86.96% de conformidade geral e zero falhas ativas P1, P2 e P3. |

---

## 🛠️ Operação, Suporte e E-mails (Configurações Administrativas)
Para garantir o pleno funcionamento do fluxo de autenticação e comunicação profissional com as famílias:

1. **Recuperação Manual de Contas (Perda Total):** 
   - Caso o aluno esqueça o e-mail *e* a senha, a equipe de suporte deverá buscar o aluno no painel do Supabase (*Authentication -> Users*) usando o nome ou número de telefone (que será enviado pelo WIX na Fase 4) para informar qual foi o e-mail cadastrado.
2. **E-mail Personalizado e Oficial (SMTP):** 
   - Para enviar os e-mails de recuperação de senha com a identidade da escola (`suporte@educamob.com.br`) ao invés do remetente genérico do Supabase, será configurado um provedor SMTP externo gratuito (como Resend ou SendGrid). 
   - *Ação Futura no Supabase:* Habilitar a configuração em *Authentication -> Providers -> Email -> Enable Custom SMTP*. Os textos e o visual do e-mail também serão customizados em *Authentication -> Email Templates*.
