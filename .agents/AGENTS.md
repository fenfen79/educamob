# Regras do Projeto - Educamob Escola Digital

Este arquivo define as regras e diretrizes comportamentais globais para todos os agentes trabalhando neste workspace.

## Manutenção do Diário de Bordo Técnico (`diario.md`)

- **REGRA CRÍTICA:** Após o término da construção de qualquer nova "Fase" ou "Sprint" do projeto Educamob Escola Digital, você deve **OBRIGATORIAMENTE** atualizar o arquivo `diario.md` localizado na raiz do projeto.
- O arquivo `diario.md` deve receber toda a documentação técnica consolidada, decisões de design, arquiteturais e detalhes operacionais do módulo recém-construído.
- O objetivo dessa regra é garantir a centralização contínua do conhecimento, assegurando que o arquivo nunca fique defasado em relação ao estado atual do software e que sirva como "fonte de verdade" para futuras implementações.

## Manutenção do Plano Mestre (`plano_educamob_escola_digital.md`)

- **REGRA CRÍTICA:** O plano estratégico geral do projeto agora reside no arquivo `plano_educamob_escola_digital.md`, na raiz do repositório (Workspace).
- Sempre que houver qualquer modificação, redefinição de rota, alteração de escopo, ou nova meta adicionada ao "plano mestre", o agente deve **OBRIGATORIAMENTE** atualizar o arquivo físico `plano_educamob_escola_digital.md`.
- **Da mesma forma, ao finalizar a execução de um Sprint ou Fase, o agente DEVE atualizar o status correspondente dentro do plano mestre (ex: mudando para "✅ Concluído").**
- Sob nenhuma hipótese o plano estratégico da conversa deve divergir do documento oficial salvo no código-fonte.

## Sincronia de Múltiplos Agentes (Leitura Obrigatória)

- **REGRA CRÍTICA:** Como há múltiplos agentes trabalhando neste mesmo projeto em conversas paralelas (ex: Planejamento, Execução de Sprints, etc.), o seu contexto de chat pode estar **desatualizado** em relação ao que já foi construído fisicamente no código ou nos arquivos Markdown.
- **Antes de fazer qualquer plano, assumir que uma tarefa está pendente ou propor a criação de arquivos**, você deve **OBRIGATORIAMENTE** ler o arquivo `plano_educamob_escola_digital.md` e o `diario.md` usando a ferramenta de leitura de arquivos.
- Eles são a única **"Fonte da Verdade"** em tempo real do que já está concluído. Apenas após ler o status atualizado nesses arquivos você poderá determinar quais são os próximos passos reais.

## Adesão Estrita ao Plano de Execução (Tolerância Zero para Burlas)

- **REGRA CRÍTICA DRACONIANA:** Sob nenhuma hipótese o Agente tem autorização para "pular", "simplificar" ou "omitir" etapas explícitas definidas nos protocolos do `plano_educamob_escola_digital.md` com o objetivo de ganhar tempo, otimizar tokens ou acelerar entregas (exemplo: gerar conteúdos sem passar pela skill de validação mandatória).
- O agente não deve priorizar velocidade em detrimento da arquitetura. Se o plano dita a execução de um processo envolvendo o uso encadeado de Skills ou Validações (ex: *Gerar na Skill A -> Validar na Skill B*), **esta cadeia deve ser executada passo a passo rigorosamente.**
- Qualquer otimização arquitetural ou alteração no fluxo do protocolo requer **aprovação explícita e prévia** do usuário antes de ser colocada em prática.

## Padronização de Moeda (Supressão do Cifrão R$)

- **REGRA CRÍTICA:** Durante a geração ou formatação de E-books teóricos e Listas de Exercícios, é estritamente PROIBIDO utilizar o símbolo do cifrão (`R$`) para valores financeiros.
- Todos os valores em Real devem ser escritos com o número seguido da palavra "reais" (ou "centavos"). Exemplo: Em vez de `R$ 50,00`, escreva `50,00 reais`. Em vez de `R$ 0,50`, escreva `0,50 reais` ou `50 centavos`.
- **Motivo:** O símbolo `$` conflita diretamente com a sintaxe de demarcação do MathJax/LaTeX nos SPAs, gerando erros crônicos de renderização nas fórmulas matemáticas da plataforma.

## ⚠️ HARD-GUARDRAIL SISTÊMICO DE ISOLAMENTO DE AMBIENTES E BLOQUEIO DE DEPLOY

- **REGRA CRÍTICA DRACONIANA DE NÃO-PROLIFERAÇÃO EM PRODUÇÃO:**
  1. **PROIBIÇÃO ABSOLUTA DE `git push origin master`:** Sob nenhuma hipótese qualquer agente de IA ou script automatizado tem autorização para executar `git push origin master` durante tarefas de teste, laboratório, prototipação ou validação preliminar.
  2. **ISOLAMENTO MANDATÓRIO DE AMBIENTE DE TESTES (BRANCHES DEDICADAS):** Todo e qualquer trabalho solicitado pelo usuário sob a diretriz de "Ambiente de Testes", "Laboratório", "Ajustes Experimentais" ou "Validação Prévia" DEVE ser realizado OBRIGATORIAMENTE em branch separada (ex: `feature/...`, `testes/...` ou `laboratorio`). É ESTRITAMENTE PROIBIDO realizar commits com códigos de teste na branch `master`.
  3. **CHAVE DE SEGURANÇA PARA DEPLOY EM PRODUÇÃO:** Comandos que impactem servidores em nuvem (Oracle Cloud VPS `137.131.163.113`, GitHub Pages ou containers Docker em produção) via SCP, SSH, `docker cp`, `docker restart` ou endpoints de reload em produção (`https://api.educamob.com.br`) SÓ PODEM SER ACIONADOS se o usuário fornecer a autorização explícita e inequívoca por escrito:
     `"AUTORIZO O DEPLOY EM PRODUÇÃO"`.
     Sem essa frase textual, o agente está formalmente BLOQUEADO de realizar qualquer ação que propague arquivos locais para a infraestrutura de produção.
  4. **BLINDAGEM DO BANCO DE DADOS SUPABASE:** Ao rodar baterias de testes manuais ou scripts de verificação no backend local (`localhost:8000`), é PROIBIDO utilizar identificadores de alunos reais ou gravar resíduos em tabelas de produção que afetem relatórios ou histórico dos beta-testers. Utilize estritamente UUIDs de teste isolados (ex: `00000000-0000-0000-0000-000000000001`).

## ⚠️ HARD-GUARDRAIL SISTÊMICO (MANDATÓRIO PARA TODOS OS AGENTES)

- **REGRA CRÍTICA DE BLOQUEIO DE SALVAMENTO:** A partir deste momento, NENHUM agente de IA (E-book Creator, Exercise Creator, SPA Creator ou você) tem autorização para usar a ferramenta nativa `write_to_file` ou `replace_file_content` para salvar arquivos diretamente dentro da pasta final `content/` (nem arquivos teóricos nem listas de exercícios).
- **O NOVO FLUXO OBRIGATÓRIO É:**
  1. Use `write_to_file` para salvar o seu conteúdo em um arquivo temporário na raiz do projeto (ex: `C:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\temp_draft.md`).
  2. Em seguida, OBRIGATORIAMENTE, acione a ferramenta `RunCommand` para executar o validador Python passando o rascunho e o destino final. Exemplo de comando:
     `python validador_educamob.py temp_draft.md content/fundamental-2/6-ano/matematica/cap-10-partilha-razao/ebooks/ef06ma15.md`
  3. O script lerá o seu rascunho, validará TODAS as regras (YAML, R$, número de exercícios, tags HTML, zero exercícios na teoria, etc).
  4. Se o script imprimir erro (e falhar), a gravação final não ocorre. Você DEVE ler o erro, editar o rascunho e rodar o script novamente até conseguir aprovação. Somente o script pode escrever no diretório final.

## Infraestrutura e Hospedagem (Backend Mob.me)

- **REGRA DE CONTEXTO:** Para fins de deploy, manutenção e arquitetura, o servidor backend real da Mob.me (`mobme-api`) e a integração do WhatsApp (`evolution-api`) **NÃO** são hospedados localmente.
- O ambiente de produção está provisionado na **Oracle Cloud (arquitetura ARM64)**.
- Ambos os serviços rodam conteinerizados via **Docker** e se comunicam internamente pela rede do Docker para recebimento de Webhooks.

## Padrão-Ouro de Calibragem Pedagógica de Exercícios (Homologado)

- **REGRA CRÍTICA DE CALIBRAGEM:** Todas as listas de exercícios do ecossistema Educamob devem seguir rigorosamente o padrão-ouro validado no piloto `ef06ci13-exercicios.md`:
  1. **Gradação Real de Dificuldade:**
     - **Básico (q01-q20):** TEM QUE SER FÁCIL. 1 único passo cognitivo direto (reconhecimento imediato, identificação conceitual primária, sem pegadinhas).
     - **Intermediário (q21-q40):** Dificuldade média real (aplicação prática, comparação entre hipóteses e modelos, relação de causa e efeito).
     - **Difícil (q41-q60):** Desafio estimulante, NÃO impossível (situações-problema investigativas resolvidas em duas etapas lógicas com Etapa 1 e Etapa 2, cálculos proporcionais simples e acessíveis para a série).
  2. **Proibição Absoluta de Decorebas e Curiosidades Inúteis:** Foco 100% no método científico e nas habilidades BNCC. Proibido cobrar nomes secundários de pessoas, datas de viagem/nascimento, termos de conversão arcaicos ou números isolados decorados.
  3. **Tom Humanizado e Acolhedor (Padrão Mob.me e SPA):** Linguagem clara, concisa e compatível com a faixa etária da série. Distratores baseados em dúvidas conceituais reais dos alunos; proibido criar alternativas absurdas, cômicas ou caricatas (ex: "animais comem ondas de rádio").
  4. **Balanceamento Obrigatório de Gabarito (A-E):** As 60 questões devem distribuir as respostas corretas de forma equilibrada entre as alternativas (~12 A, ~12 B, ~12 C, ~12 D e ~12 E). Proibido concentrar o gabarito na letra A ou repetir a mesma letra mais de 3 vezes consecutivas.
