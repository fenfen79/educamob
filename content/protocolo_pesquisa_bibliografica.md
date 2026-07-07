# Protocolo de Pesquisa Bibliográfica e Produção de Conteúdo

Este documento estabelece o **protocolo padrão e replicável** de pesquisa de conteúdos em fontes confiáveis para a Educamob Escola Digital. Este é o manual operacional obrigatório para toda a produção de e-books da Base Teórica.

---

## 1. Ficha Bibliográfica (Template por Objeto de Conhecimento)

A Ficha Bibliográfica é a unidade de planejamento da pesquisa. Para cada **Objeto de Conhecimento** a ser produzido, preencha:

```yaml
---
# Ficha Bibliográfica
titulo: "Nome do Objeto de Conhecimento"
codigo_habilidade: "Ex: EF08MA01"
fonte_primaria: "Nome da Fonte e URL (Nível 1 ou 2)"
fonte_secundaria: "Nome da Fonte Alternativa (Nível 1 ou 2)"
palavras_chave: ["termo1", "termo2"]
nivel_cognitivo_bloom: "Lembrar / Entender / Aplicar / Analisar / Avaliar / Criar"
---
```

---

## 2. Fluxo Operacional Passo a Passo

O processo de pesquisa e validação ocorre na seguinte ordem:

1. **Como Pesquisar**:
   - Identifique o Objeto de Conhecimento e a Habilidade BNCC/INEP correspondente no `mapa_curricular.md`.
   - Consulte primeiro o **Banco de Fontes Hierarquizado** (abaixo). Priorize fontes de Nível 1. Se insuficiente, desça ao Nível 2.
2. **Como Validar**:
   - Aplique o *Protocolo de Garantia de Veracidade* em todas as afirmações e conceitos coletados.
   - Nenhuma informação pode ser considerada fato se estiver restrita a apenas uma fonte não-governamental.
3. **Como Documentar**:
   - Preencha a Ficha Bibliográfica e salve todas as URLs/PDFs utilizados. Formate as referências finais no padrão ABNT (NBR 6023).
4. **Como Entregar ao E-book Creator**:
   - No prompt de criação, entregue o texto de referência da fonte + a ficha bibliográfica preenchida para que a Skill aplique as diretrizes pedagógicas da Educamob.

---

## 3. Uso de PDFs Próprios (Acervo Pessoal)

Livros didáticos físicos e PDFs do acervo pessoal podem ser utilizados como fonte complementar sob as seguintes regras:
- **Apenas como Nível 2**: Mesmo que seja um livro famoso, ele será tratado com o peso acadêmico (Nível 2).
- **Citação Completa**: O ano, autor, edição e página devem estar documentados para rastreabilidade.
- **Triangulação Obrigatória**: Nenhuma definição pode vir *exclusivamente* do PDF próprio sem que seja validada (triangulada) por pelo menos uma fonte do Nível 1 (BNCC/MEC) ou outro Nível 2.

---

## 4. Protocolo de Garantia de Veracidade

Existem **7 critérios obrigatórios** para aprovação de qualquer informação factual na plataforma:

1. **Fonte identificada**: Autor, instituição e URL (ou DOI/ISBN) devem ser claramente rastreáveis.
2. **Triangulação**: A informação deve ser confirmada em **≥ 2 fontes independentes**.
3. **Atualidade**: Dados, estatísticas e normativas devem ter **≤ 5 anos** (exceto leis fundamentais, teoremas matemáticos clássicos e fatos históricos consolidados).
4. **Autoridade**: O autor ou a instituição da fonte deve ter credenciais comprovadas na área.
5. **Revisão por pares**: Preferência absoluta para artigos e repositórios submetidos à revisão.
6. **Validação pelo Agente Validador Acadêmico**: A inteligência artificial assumirá o papel da revisão final pedagógica (substituindo a revisão humana manual).
7. **Referenciamento ABNT**: Todas as referências devem constar no rodapé (lista) e com citação em texto apropriada.

---

## 5. Banco de Fontes Hierarquizado

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
| Repositório USP / UNICAMP / UFRGS | repositórios universitários | ✅ Verificar por obra |
| BDTD | https://bdtd.ibict.br/ | ✅ Verificar |
| arXiv | https://arxiv.org/ | ✅ Preprints (Física/Matemática) |
| PubMed Central | https://www.ncbi.nlm.nih.gov/pmc/ | ✅ Artigos biomédicos (Química/Ciências) |
| ERIC | https://eric.ed.gov/ | ✅ Pesquisa educacional |
| MIT OpenCourseWare | https://ocw.mit.edu/ | ✅ CC-BY-NC-SA (Abordagem STEM) |
| PhET Simulations (CU Boulder) | https://phet.colorado.edu/pt_BR/ | ✅ Simuladores (descrição textual) |
| OpenStax | https://openstax.org/ | ✅ CC-BY (Livros-texto gratuitos STEM) |

*🌍 Europa e 🌏 Ásia:*
Inclui portais como HAL (França), CORE (Reino Unido), EuDML, Europeana, Nuffield Foundation, RCAAP (Portugal), Numdam, J-STAGE (Japão), KISTI, CAS, NII, Indian Academy of Sciences e KOCW. Todos como ✅ Acesso Aberto / Referência.

**🟡 Nível 3 — Referência Pedagógica (Inspiração, NÃO cópia):**
| Fonte | URL | Uso permitido |
|---|---|---|
| Khan Academy Brasil | https://pt.khanacademy.org/ | ❌ CC-NC — usar como referência de abordagem, não copiar |
| Nova Escola | https://novaescola.org.br/ | ⚠️ Consultar estrutura de planos de aula |
| Escola Digital | https://escoladigital.org.br/ | ⚠️ Referência de curadoria |
| GeoGebra | https://www.geogebra.org/ | ⚠️ CC-BY-NC-SA — referência para construções |
| Wolfram MathWorld | https://mathworld.wolfram.com/ | ⚠️ Referência — cruzar com primária |
| BBC Bitesize | https://www.bbc.co.uk/bitesize | ⚠️ Referência de didática |

**🔴 Fontes PROIBIDAS:**
| Tipo | Motivo |
|---|---|
| Blogs sem autoria identificada | Sem verificação de autoridade |
| Wikipedia | Editável (Pode ser o ponto de partida, mas nunca fonte primária) |
| Materiais de cursinhos piratas | Violação de direitos autorais explícita |
| IA sem revisão pelo Agente Validador | Alto risco de alucinação |
| Redes sociais | Sem revisão por pares |
