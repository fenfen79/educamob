# Checklist de Qualidade — E-books Atômicos

Este é o checklist padrão para auditar cada E-book criado antes dele ser considerado "Aprovado" e pronto para entrar em um SPA ou no banco de dados RAG. O Agente Validador Acadêmico se baseia nos critérios abaixo.

## 1. Estrutura e Metadados (Frontmatter)
- [ ] O arquivo contém o **YAML Frontmatter** no topo (delimitado por `---`)?
- [ ] Os campos obrigatórios do Frontmatter estão preenchidos?
  - `série` / `disciplina` / `unidade_temática` / `objeto_de_conhecimento`
  - `habilidades` (ex: EF08MA01)
  - `pré-requisitos` (com links relativos)
  - `nível_dificuldade`
  - `palavras_chave`
  - `tempo_estimado`
  - `fonte_bibliografica`
  - `status_revisao`

## 2. Granularidade
- [ ] O arquivo aborda **apenas 1** Objeto de Conhecimento (não mistura temas não relacionados)?

## 3. Andaimes Cognitivos (Scaffolding)
- [ ] O E-book possui a seção estrutural **Na Prática** com exemplos guiados passo a passo?
- [ ] O E-book possui a **Tabela de Erros Comuns** evidenciando os equívocos normais de alunos?
- [ ] O E-book possui a seção **Resumo para Revisão** com 3 a 5 pontos-chave curtos?
- [ ] O E-book possui a seção **Conexões Interdisciplinares** com ao menos 1 relação?

## 4. Quizzes Interativos
- [ ] Cada questão do E-book possui **5 alternativas** de resposta (padrão ENEM/Escola)?
- [ ] Existem ao todo pelo menos **4 atividades/quizzes** no documento?
- [ ] **MUITO IMPORTANTE:** Toda questão do quiz possui as tags HTML em forma de comentário indicando telemetria?
  - Ex: `<!-- tipo: multipla-escolha | habilidade: EF08MA01 | dificuldade: basico -->`

## 5. Acessibilidade
- [ ] O texto utiliza linguagem direta e parágrafos curtos, otimizado para TDAH e Dislexia?
- [ ] Conceitos novos ou complexos estão em **negrito** e foram explicados antes do uso?

## 6. Veracidade e Referências
- [ ] Toda afirmação factual passou pelo crivo da triangulação (validada em ≥ 2 fontes ou provém de Nível 1)?
- [ ] As **Referências ABNT** estão presentes no rodapé (NBR 6023)?
- [ ] As **Citações ABNT** estão presentes no texto (NBR 10520) caso um conceito de Nível 2 seja importado diretamente?
