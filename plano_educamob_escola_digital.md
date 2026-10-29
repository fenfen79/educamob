# 🚀 Plano de Execução Mestre — Educamob Escola Digital

> **Planejador Estratégico** · Atualizado: 2026-10-21. **Muro de Contenção Geral Universal Homologado no `validador_educamob.py`**: Motor de Pareamento Teórico Universal (Princípio do Mundo Fechado / Closed-World Boundary com suporte a múltiplos e-books e tratamento de epônimos compostos), Trava Sistêmica de Balanceamento Obrigatório de Gabarito (~20% por letra de A a E, tolerância 8 a 16 e anti-repetição viciada), Trava Anti-Decoreba e Expansão da Blacklist de Jargões Universitários. **100% DAS 334 LISTAS DO REPOSITÓRIO AUDITADAS E HOMOLOGADAS COM EXIT CODE 0 (20.040 QUESTÕES)**:
> - **Ciências (5º ao 9º Ano):** 72/72 listas homologadas ✅ (4.320 questões).
> - **Química (Ensino Médio):** 53/53 listas homologadas ✅ (3.180 questões).
> - **Física (Ensino Médio):** 61/61 listas homologadas ✅ (3.660 questões).
> - **Matemática (Fundamental 1, Fundamental 2 e Médio):** 148/148 listas homologadas ✅ (8.880 questões).
> **Fase 5: Recalibração Pedagógica Padrão-Ouro 100% CONCLUÍDA PARA TODAS AS DISCIPLINAS DO ECOSSISTEMA EDUCAMOB.** Fase 6 (Sprint 14) com Ingestão Massiva (39.280 chunks) e Índice HNSW ativo no pgvector/Supabase.

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
| **TOTAL GERAL NO SUPABASE (RAG)** | **483 e-books teóricos (22.877 chunks) + 290 listas (18.083 chunks)** | 🏆 **Acervo Ativo e em Expansão Contínua** |

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

---

## 🛠️ Operação, Suporte e E-mails (Configurações Administrativas)
Para garantir o pleno funcionamento do fluxo de autenticação e comunicação profissional com as famílias:

1. **Recuperação Manual de Contas (Perda Total):** 
   - Caso o aluno esqueça o e-mail *e* a senha, a equipe de suporte deverá buscar o aluno no painel do Supabase (*Authentication -> Users*) usando o nome ou número de telefone (que será enviado pelo WIX na Fase 4) para informar qual foi o e-mail cadastrado.
2. **E-mail Personalizado e Oficial (SMTP):** 
   - Para enviar os e-mails de recuperação de senha com a identidade da escola (`suporte@educamob.com.br`) ao invés do remetente genérico do Supabase, será configurado um provedor SMTP externo gratuito (como Resend ou SendGrid). 
   - *Ação Futura no Supabase:* Habilitar a configuração em *Authentication -> Providers -> Email -> Enable Custom SMTP*. Os textos e o visual do e-mail também serão customizados em *Authentication -> Email Templates*.
