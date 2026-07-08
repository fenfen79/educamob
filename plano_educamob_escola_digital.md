# 🚀 Plano de Execução Mestre — Educamob Escola Digital

> **Planejador Estratégico** · Atualizado: 2026-07-08. Fase 5 em execução (Sprint produzindo 9º Ano). Banco de Fontes global com 25+ fontes.

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
> 4. **UX Responsivo:** Menu mobile 100% funcional, contrastes de bolhas suavizados (Tom sobre Tom) e correção das "bolhas fantasmas".

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
> **Regra de Ouro Arquitetural:** Granularidade (para o RAG da IA) vs. Integração (para a Trilha do Aluno no Frontend).
> - **E-books** são blocos **atômicos**: `1 E-book = 1 Objeto de Conhecimento da BNCC`. O backend (FastAPI/Mob.me) precisa desses blocos separados para RAG preciso.
> - **SPAs** são blocos **integrados**: `1 SPA = N Objetos de Conhecimento articulados em trilha coesa`. O aluno consome uma experiência fluida de 15-20 minutos.
> - O SPA **NÃO é 100% offline**. Ele se conecta ao Supabase Client via `shared/js/quiz.js` para persistir telemetria por habilidade.
>
> **Ciclo Completo da Plataforma:**
> 1. Aluno acessa o **SPA** (que articulou objetos A, B e C) e responde aos quizzes (tagueados no E-book).
> 2. O SPA envia desempenho detalhado (habilidade errada/acertada) para o **Supabase** (`student_progress`).
> 3. Aluno vai ao **Mob.me**. O backend lê o histórico no Supabase e usa os E-books granulares (RAG) para explicar exatamente a habilidade com dificuldade.
> 4. **Agente WhatsApp** consulta a mesma tabela e envia relatório aos pais.
>
> **Rastreabilidade de Design — Cada seção do `.md` tem consumidor(es) no ecossistema:**
>
> | Seção do E-book | Mob.me (IA/RAG) | SPA (Quizzes) | Revisões (futuro) |
> |---|---|---|---|
> | YAML Frontmatter | Busca o arquivo certo por série/habilidade | Filtra questões por habilidade e dificuldade | Seleciona tópicos por série |
> | Conceitos Fundamentais | Fundamenta respostas com citação | — | Conteúdo de revisão |
> | Exemplos Resolvidos | Referencia ao explicar resolução | — | Relembrar procedimentos |
> | Erros Comuns | Corrige o aluno proativamente | Gera distratores realistas | Alerta preventivo |
> | Atividades (com tags HTML) | Sugere exercícios adicionais | **Extrai diretamente** para montar provas | Exercícios de fixação |
> | Resumo para Revisão | Sintetiza respostas rápidas | — | **Alimenta diretamente** sessões |
> | Referências | Cita fonte ao responder | — | — |

### Sprint 11 — Protocolo de Pesquisa Bibliográfica

> **Status:** ✅ Concluído.  
> **Complexidade:** 🔴 Alta  
> **Skill a acionar:** Execução Direta (Planejador Estratégico + Pesquisa Web)  
> **Pré-requisitos:** Nenhum

**Objetivo:** Criar o **protocolo padrão e replicável** de pesquisa de conteúdos em fontes confiáveis, alinhado às normativas brasileiras de educação. Este protocolo será o manual operacional usado em toda produção de e-books futura.

**Entregas Esperadas:**

#### Entrega 1 — Documento-Protocolo (`protocolo_pesquisa_bibliografica.md`)

Contendo:
- Template de ficha bibliográfica **por Objeto de Conhecimento** (título, código da habilidade BNCC/INEP mapeada, fonte primária, fonte secundária, palavras-chave, nível cognitivo Bloom)
- Critérios de validação de fonte (autoria, atualização, alinhamento curricular)
- Fluxo operacional passo a passo: Como pesquisar → Como validar → Como documentar → Como entregar ao E-book Creator
- Regras de uso de PDFs próprios (livros do acervo pessoal) como fonte complementar
- Protocolo de Garantia de Veracidade (7 critérios obrigatórios por informação factual):
  1. Fonte identificada — autor, instituição, URL rastreável
  2. Triangulação — confirmada em ≥ 2 fontes independentes
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

#### Entrega 2 — Mapa Curricular Completo por Disciplina (granularidade: Objetos de Conhecimento)

- **Matemática Fundamental (5º ao 9º):** Lista de todos os Objetos de Conhecimento da BNCC, com habilidades mapeadas (códigos EFxxMAxx)
- **Matemática Ensino Médio (1ª a 3ª):** Objetos de Conhecimento BNCC + competências específicas
- **Física Ensino Médio (1ª a 3ª):** Objetos de Conhecimento BNCC + habilidades
- **Química Ensino Médio (1ª a 3ª):** Objetos de Conhecimento BNCC + habilidades
- **ENEM (Matemática, Física, Química):** Competências e habilidades da Matriz de Referência INEP

#### Entrega 3 — Ordem de Produção (Sem Priorização Interna)

Documento formalizando que não há priorização entre conteúdos de uma mesma disciplina e que a produção seguirá a ordem completa sequencial.

#### Entrega 4 — Arquivos de Infraestrutura da Base Teórica

| Arquivo | Função |
|---|---|
| `_index.md` | Índice geral com links para todos os arquivos da base teórica |
| `_fontes-verificadas.md` | Banco de fontes curadas (espelho do banco acima, atualizado conforme novas fontes são descobertas) |
| `_checklist-qualidade.md` | Checklist padrão operacional de qualidade para cada `.md` produzido |

#### Entrega 5 — Agente Validador Acadêmico (nova skill via Meta-Arquiteto)

Criação de uma skill especializada em **validação de conteúdos acadêmicos**, substituindo a revisão humana por professor licenciado. O agente deve:
- Verificar veracidade de toda afirmação factual (triangulação em ≥2 fontes)
- Validar alinhamento com habilidades BNCC/INEP declaradas no frontmatter
- Conferir conformidade do template (seções obrigatórias, YAML, tags HTML)
- Verificar adequação de linguagem à faixa etária
- Checar conformidade ABNT das referências
- Emitir parecer: `aprovado` | `revisão_necessária` (com apontamentos específicos)

#### Entrega 6 — Atualização da Skill E-book Creator

A skill atual (`C:\Users\nepov\.gemini\config\skills\ebook-creator\SKILL.md`) **não possui**: YAML Frontmatter, Tags HTML nos quizzes, seção Erros Comuns, seção Conexões Interdisciplinares, seção Resumo para Revisão, nem referências ABNT. Deve ser atualizada para incorporar o template enriquecido antes do início do Sprint 12.

**Checklist de Validação do Sprint 11:**
- [ ] Protocolo é autocontido e replicável por qualquer agente?
- [ ] Banco de fontes cobre 3 níveis (Governamental + Acadêmico + Pedagógico) + internacionais?
- [ ] Fontes proibidas documentadas?
- [ ] Mapa curricular cobre 100% dos Objetos de Conhecimento BNCC/INEP do escopo?
- [ ] Template de ficha bibliográfica é claro e preenchível?
- [ ] Granularidade atômica respeitada (1 ficha = 1 Objeto de Conhecimento)?
- [ ] Arquivos de infraestrutura criados (`_index.md`, `_fontes-verificadas.md`, `_checklist-qualidade.md`)?
- [ ] Skill E-book Creator atualizada com template enriquecido?
- [ ] Agente Validador Acadêmico projetado (via Meta-Arquiteto)?
- [ ] Pilar Financeiro respeitado (zero fontes pagas)?

---

### Sprint 12 — Produção de E-books Educacionais (Granulares e Atômicos)

> **Complexidade:** 🔴 Alta — Sprint **cíclico e incremental** (múltiplas conversas — 1 conversa por Objeto de Conhecimento recomendado). Este sprint será executado repetidamente ao longo de meses.  
> **Skill a acionar:** E-book Creator (atualizada no Sprint 11)  
> **Pré-requisitos:** Sprint 11 concluído (protocolo + mapa curricular + fichas bibliográficas preenchidas + skill atualizada + Agente Validador criado)

**Objetivo:** Produzir e-books **atômicos** em Markdown — **1 e-book por Objeto de Conhecimento da BNCC** — utilizando as fichas bibliográficas como matéria-prima. Os e-books são a base de conteúdo para: (1) alimentar o RAG do Mob.me, (2) servir de matéria-prima para os SPAs interativos, e (3) alimentar futuras sessões de revisão.

**⚠️ Regra de Granularidade Estrita:**
- **1 E-book = 1 Objeto de Conhecimento da BNCC** (bloco atômico)
- O backend (FastAPI/Mob.me) precisa desses blocos separados para construir contextos RAG precisos
- Um "capítulo" do mapa curricular pode conter 3-5 Objetos de Conhecimento = 3-5 e-books
- **Desmembramento Específico de Habilidades Multitemáticas:** Habilidades abrangentes (ex: EF06MA24 e EF06MA25 que tratam de várias grandezas simultâneas) DEVEM ser desmembradas. O e-book deve focar estritamente no tipo de grandeza do capítulo em que está inserido (ex: Tempo, Massa, Capacidade) e usar sufixos explícitos no nome do arquivo (ex: `ef06ma24-tempo.md`, `ef06ma25-capacidade.md`) para não haver sobrescrição entre capítulos e para isolar o escopo semântico no RAG.

**Metadados Obrigatórios (por e-book):**
1. **YAML Frontmatter:** Cabeçalho com série, disciplina, unidade temática, objeto de conhecimento, habilidades BNCC/INEP (códigos), pré-requisitos (links relativos), nível de dificuldade, palavras-chave, tempo estimado de leitura, fonte bibliográfica, status de revisão
2. **Tags HTML nos Quizzes (CRUCIAL):** Cada questão deve conter comentário HTML invisível com metadados de telemetria:
   ```html
   <!-- tipo: multipla-escolha | habilidade: EF08MA01 | dificuldade: basico -->
   ```
   Essas tags são lidas pelo JavaScript do SPA para persistir desempenho **por habilidade** no Supabase.
3. **Andaimes Cognitivos:** Blocos "Na Prática" e Tabela de Erros Comuns obrigatórios.
4. **Seção "Resumo para Revisão":** 3-5 pontos-chave concisos + link para próximo tópico na sequência. Alimenta futuras sessões de revisão.
5. **Referências ABNT:** Lista de referências no padrão NBR 6023, com citações no texto no padrão NBR 10520.

**Estrutura de Execução (por Objeto de Conhecimento):**
1. Consultar a ficha bibliográfica do Objeto (Sprint 11)
2. Acionar a skill **E-book Creator** com prompt contendo:
   - Série e disciplina alvo
   - Objeto de Conhecimento específico e habilidades BNCC/INEP a cobrir
   - Fontes validadas da ficha bibliográfica
   - Instrução de YAML Frontmatter obrigatório
   - Instrução de Tags HTML nos quizzes (`<!-- tipo | habilidade | dificuldade -->`)
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
Não há priorização entre conteúdos de uma mesma disciplina. A produção ocorrerá abordando todo o conteúdo de forma sequencial:
1. **Matemática**: Todo o conteúdo sequencial do 5º ano do Ensino Fundamental até a 3ª série do Ensino Médio e ENEM.
2. **Física** e **Química** virão na sequência.

**Checklist de Validação (por e-book atômico):**
- [ ] Granularidade respeitada (1 e-book = 1 Objeto de Conhecimento)?
- [ ] YAML Frontmatter presente e completo (todos os campos obrigatórios)?
- [ ] Tags HTML nos quizzes (`<!-- tipo | habilidade | dificuldade -->`) inseridas em todas as questões?
- [ ] Conteúdo segue microaprendizagem (blocos curtos)?
- [ ] Acessibilidade TDAH/Dislexia contemplada?
- [ ] Scaffolding incluído (blocos "Na Prática" + Tabela de Erros Comuns)?
- [ ] Seção "Resumo para Revisão" com 3-5 pontos-chave + link próximo tópico?
- [ ] Quizzes com 5 alternativas e 3 níveis de dificuldade?
- [ ] Mínimo 4 atividades com metadados completos?
- [ ] Conexões interdisciplinares presentes?
- [ ] Habilidades BNCC/INEP declaradas no frontmatter?
- [ ] Referências ABNT (NBR 6023/10520)?
- [ ] 100% das afirmações factuais com fonte rastreável?
- [ ] Agente Validador Acadêmico emitiu parecer `aprovado`?

---

### Sprint 13 — Produção de SPAs Interativos (Articulação de Trilhas)

> **Complexidade:** 🔴 Alta (múltiplas conversas — 1 conversa por capítulo/assunto recomendado)  
> **Skill a acionar:** SPA Creator  
> **Pré-requisitos:** Todos os e-books atômicos do capítulo correspondente concluídos (Sprint 12)

**Objetivo:** Articular os e-books atômicos (Objetos de Conhecimento) de cada capítulo em um SPA (Single Page Application) interativo, cinematográfico e gamificado, criando uma **trilha de estudo unificada, coerente e harmônica** de 15-20 minutos.

**⚠️ Regra de Articulação:**
- **Entrada:** Múltiplos arquivos `.md` (Objetos de Conhecimento de um mesmo capítulo/assunto)
- **Saída:** 1 Web App (`index.html` + `styles.css` + `script.js` + assets)
- O papel do SPA **NÃO** é empilhar e-books. Ele deve **articulá-los magistralmente**, criando pontes narrativas para que o aluno não sinta a divisão entre os objetos atômicos. O aprendizado flui naturalmente.

**⚠️ Conectividade (NÃO É 100% OFFLINE):**
- O SPA deve estar conectado à estrutura `shared/js/quiz.js` e ao **Supabase Client**
- O JavaScript do SPA lê as **tags HTML secretas** dos quizzes (inseridas no Sprint 12)
- Ao finalizar exercícios, o SPA captura o resultado, cruza com as tags (Habilidade, Dificuldade) e **salva na tabela `student_progress` no Supabase**
- Zero CDN e zero libs externas continuam valendo — a única conexão externa é o Supabase Client (já presente em `shared/`)

**Estrutura de Execução (por capítulo/assunto):**
1. Confirmar que **todos** os e-books atômicos do capítulo estão aprovados
2. Acionar a skill **SPA Creator** com prompt contendo:
   - Caminhos absolutos de **todos** os e-books fonte do capítulo (`content/.../[capitulo]/ebooks/*.md`)
   - Série, disciplina e capítulo
   - Instrução explícita de **articulação harmônica** (pontes narrativas entre objetos)
   - Referência aos SPAs existentes como padrão visual (`content/fundamental-2/8-ano/matematica/cap-09-potenciacao/` e `cap-10-monomios-polinomios/`)
   - Instrução de leitura de tags HTML dos quizzes para telemetria por habilidade
   - Instrução de integração com `shared/js/quiz.js` (persistência Supabase por habilidade)
   - Instrução de integração com `shared/js/auth-guard.js` (autenticação)
   - Geração de imagens via `generate_image` (zero placeholders)
3. Registrar o novo SPA no `window.EDUCAMOB_REGISTRY` da Biblioteca

**Caminho de Destino:**
```
content/[nivel]/[serie]/[disciplina]/[capitulo]/index.html
content/[nivel]/[serie]/[disciplina]/[capitulo]/styles.css
content/[nivel]/[serie]/[disciplina]/[capitulo]/script.js
content/[nivel]/[serie]/[disciplina]/[capitulo]/*.png (imagens geradas)
content/[nivel]/[serie]/[disciplina]/[capitulo]/ebooks/*.md (e-books fonte — já existentes do Sprint 12)
```

**Checklist de Validação (por SPA):**
- [ ] Articulação harmônica entre objetos (transições narrativas fluidas)?
- [ ] Experiência de estudo de 15-20 minutos contínuos?
- [ ] Leitura de tags HTML dos quizzes para telemetria por habilidade?
- [ ] Persistência de notas por habilidade no Supabase (`student_progress`)?
- [ ] Zero CDN, zero libs externas (Supabase Client via `shared/` é permitido)?
- [ ] Paleta visual Educamob respeitada (fundo claro, destaque laranja #ff6b00)?
- [ ] Integrado ao `auth-guard.js` e `quiz.js`?
- [ ] Registrado no `EDUCAMOB_REGISTRY` da Biblioteca?
- [ ] Imagens geradas (sem placeholders)?
- [ ] Responsivo (desktop + mobile)?

---

## 🟣 Fase 6 — Melhorias Contínuas (Backlog Futuro) [SEMPRE ÚLTIMA]
> Repositório de ideias tecnológicas e aprimoramentos arquitetônicos que foram pontuados ao longo do projeto, mas que não são bloqueantes para o MVP (Mínimo Produto Viável). Esta fase é permanentemente a última do plano e recebe novos itens conforme surgem.

| Sprint | Módulo / Melhoria | Descrição Técnica |
|--------|-------------------|-------------------|
| **14** | Roteamento Multi-LLM | Implementar um fallback inteligente adicionando a OpenAI (GPT-4o / GPT-4o-mini) para trabalhar em redundância caso a API do Google Gemini sofra instabilidades. |
| **15** | Automação Ativa (Push) de Relatórios | Criar um "Cron Job" no FastAPI que rode toda sexta-feira às 18h, gere relatórios semanais de alunos automaticamente e dispare proativamente no WhatsApp das famílias (Evolution API). |
| **16** | Painel Administrativo de Prompts | Migrar os prompts base (o "Prompt Socrático" e o "Prompt de Relatórios") do código rígido (hardcoded) para uma tabela do Supabase, permitindo edição via interface web sem mexer no backend. |
| **17** | E-mail Customizado Oficial (SMTP) | Configurar um provedor SMTP (como Resend ou SendGrid) no Supabase Auth (*Enable Custom SMTP*) para que os e-mails de recuperação de senha usem a marca e domínio oficial da escola. |
| **18** | Hub de Lives | Retomar o Sprint 5 que foi paralisado. Construir a área de transmissões ao vivo dentro da plataforma principal para centralizar as aulas online. |
| **19** | Painel Pedagógico Institucional (Escolas) | Sistema completo (com controle de acesso para Professores, Coordenadores e Diretores) permitindo prescrever estudos e metas de revisão com prazos estabelecidos (para alunos individuais ou turmas inteiras), além de acompanhar dashboards de resultados em tempo real. |
| **20** | Painel Parental (Home Study) | Versão do painel dedicada aos pais/responsáveis. Permite designar tarefas e roteiros específicos de estudo para seus próprios filhos e visualizar gráficos claros dos resultados obtidos. |
| **21** | Script de Validação de YAML | Criar script automatizado (Python/Node) que valide todos os campos obrigatórios do YAML frontmatter, verifique links internos entre arquivos, confira cobertura de habilidades BNCC por disciplina/série e garanta contagem mínima de atividades por arquivo. |
| **22** | NPS do Aluno (Satisfação) | Implementar micro-survey (1 pergunta, escala 0-10) nos SPAs após conclusão de trilha. Resultado salvo em tabela `student_feedback` no Supabase (`user_id`, `score`, `touchpoint`, `comentario`, `timestamp`). Cálculo: `NPS = % Promotores (9-10) − % Detratores (0-6)`. Custo zero (popup CSS + INSERT no Supabase). |
| **23** | Manutenção Contínua da Base Teórica | Cadência de revisão: semestral (atualidade de dados e referências), anual (incorporar novas questões ENEM/provas oficiais), sob demanda (corrigir erros reportados por alunos via Mob.me, adicionar tópicos solicitados com frequência). |

---

## 🛠️ Operação, Suporte e E-mails (Configurações Administrativas)
Para garantir o pleno funcionamento do fluxo de autenticação e comunicação profissional com as famílias:

1. **Recuperação Manual de Contas (Perda Total):** 
   - Caso o aluno esqueça o e-mail *e* a senha, a equipe de suporte deverá buscar o aluno no painel do Supabase (*Authentication -> Users*) usando o nome ou número de telefone (que será enviado pelo WIX na Fase 4) para informar qual foi o e-mail cadastrado.
2. **E-mail Personalizado e Oficial (SMTP):** 
   - Para enviar os e-mails de recuperação de senha com a identidade da escola (`suporte@educamob.com.br`) ao invés do remetente genérico do Supabase, será configurado um provedor SMTP externo gratuito (como Resend ou SendGrid). 
   - *Ação Futura no Supabase:* Habilitar a configuração em *Authentication -> Providers -> Email -> Enable Custom SMTP*. Os textos e o visual do e-mail também serão customizados em *Authentication -> Email Templates*.
