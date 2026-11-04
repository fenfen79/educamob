const fs = require('fs');
const path = require('path');

const projectRoot = path.resolve(__dirname, '../../..');
const pagePath = path.join(projectRoot, 'apps/mobme-source/app/page.tsx');
const katexPath = path.join(projectRoot, 'apps/mobme-source/node_modules/katex');

const katex = require(katexPath);
const pageContent = fs.readFileSync(pagePath, 'utf8');

// Extrai sanitizeContent real do page.tsx
const fnMatch = pageContent.match(/const sanitizeContent = \([\s\S]*?\n\};\n/);
if (!fnMatch) {
  console.error("Failed to extract sanitizeContent from page.tsx");
  process.exit(1);
}

let jsCode = fnMatch[0]
  .replace("const sanitizeContent =", "global.sanitizeContent =")
  .replace(/\(content:\s*string\)/, "(content)")
  .replace(/:\s*string\[\]/g, "")
  .replace(/:\s*string/g, "")
  .replace(/:\s*any/g, "")
  .replace(/:\s*Record<string,\s*string>/g, "");

eval(jsCode);

function validateMessage(rawText) {
  const sanitized = global.sanitizeContent(rawText || "");
  const errors = [];

  // 1. Extração e Compilação Real KaTeX
  const mathRegex = /(\$\$[\s\S]*?\$\$|\$(?:\\.|[^\$\n])+\$)/g;
  const mathMatches = sanitized.match(mathRegex) || [];
  const katexErrors = [];

  for (const m of mathMatches) {
    const isDisplay = m.startsWith('$$') && m.endsWith('$$');
    const inner = isDisplay ? m.slice(2, -2).trim() : m.slice(1, -1).trim();

    if (!inner) continue;

    // Verifica cifrão aninhado dentro da expressão matemática (ex: \frac{S - $S_0$}{t})
    if (/(?<!\\)\$/.test(inner)) {
      katexErrors.push(`Nested dollar sign inside math: ${m}`);
    }

    try {
      katex.renderToString(inner, {
        displayMode: isDisplay,
        throwOnError: true,
        strict: false
      });
    } catch (err) {
      katexErrors.push(`KaTeX error in [${m}]: ${err.message}`);
    }
  }

  // 2. Verificação de Alternativas de Múltipla Escolha (Uma por Linha)
  // Detecta se a mensagem apresenta alternativas a) e b)
  const hasOptionA = /(?:^|\n|[ \t])[aA]\)[ \t]+\S/.test(rawText);
  const hasOptionB = /(?:^|\n|[ \t])[bB]\)[ \t]+\S/.test(rawText);
  const hasAlternatives = hasOptionA && hasOptionB;

  let rawAlternativesOnePerLine = true;
  let sanitizedAlternativesOnePerLine = true;
  const altErrors = [];

  if (hasAlternatives) {
    // No texto bruto (LLM output): verifica se há duas ou mais alternativas (a) ... b) ...) agrupadas na mesma linha
    const inlineRawMatch = rawText.match(/[a-dA-D]\)[ \t]+[^\n]+?[ \t]+[b-eB-E]\)[ \t]+\S/);
    if (inlineRawMatch) {
      rawAlternativesOnePerLine = false;
      altErrors.push(`Raw LLM output grouped alternatives on same line: "${inlineRawMatch[0]}"`);
    }

    // No texto sanitizado (Frontend render): verifica se há duas ou mais alternativas na mesma linha ou sem linha em branco (\n\n)
    const inlineSanitizedMatch = sanitized.match(/[a-dA-D]\)[ \t]+[^\n]+?[ \t]+[b-eB-E]\)[ \t]+\S/);
    if (inlineSanitizedMatch) {
      sanitizedAlternativesOnePerLine = false;
      altErrors.push(`Sanitized text still has inline alternatives: "${inlineSanitizedMatch[0]}"`);
    }

    const singleNewlineSanitized = sanitized.match(/(^[ \t]*[a-eA-E]\)[^\n]+)\n([ \t]*[a-eA-E]\))/m);
    if (singleNewlineSanitized) {
      sanitizedAlternativesOnePerLine = false;
      altErrors.push(`Sanitized alternatives separated by single \\n instead of \\n\\n`);
    }
  }

  // 3. Verificação de Cifrão Financeiro Proibido (R$)
  const hasCurrencySymbol = /R\$\s*\d/i.test(rawText);

  // 4. Verificação de Fórmulas Químicas em Negrito Cru ou Unicode Subscript no Texto Bruto
  const hasUnicodeSubscripts = /[₀₁₂₃₄₅₆₇₈₉]/.test(rawText);
  const hasRawBoldChem = /\*\*(?:HCl|HBr|HI|HF|H2SO4|H_2SO_4|HNO3|HNO_3|H2S|H_2S|NaOH|KOH|Ca\(OH\)2|Ca\(OH\)_2|NaCl|H2O|H_2O|CO2|CO_2|NH3|NH_3)\*\*/.test(rawText);

  // 5. Verificação de Tabelas Markdown (se houver tabela)
  const tableLines = sanitized.split('\n').filter(l => l.trim().startsWith('|') && l.trim().includes('|', 1));
  let tableValid = true;
  if (tableLines.length >= 2) {
    const hasBlockMathInTable = tableLines.some(l => l.includes('$$'));
    if (hasBlockMathInTable) {
      tableValid = false;
      errors.push("Table contains block math $$...$$ inside cell");
    }
  }

  return {
    sanitized_text: sanitized,
    math_count: mathMatches.length,
    katex_valid: katexErrors.length === 0,
    katex_errors: katexErrors,
    has_alternatives: hasAlternatives,
    raw_alternatives_one_per_line: rawAlternativesOnePerLine,
    sanitized_alternatives_one_per_line: sanitizedAlternativesOnePerLine,
    alt_errors: altErrors,
    no_currency_symbol: !hasCurrencySymbol,
    no_unicode_subscripts: !hasUnicodeSubscripts,
    no_raw_bold_chem: !hasRawBoldChem,
    table_valid: tableValid
  };
}

let inputData = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => { inputData += chunk; });
process.stdin.on('end', () => {
  try {
    const payload = JSON.parse(inputData);
    if (Array.isArray(payload)) {
      const results = payload.map(item => validateMessage(item));
      process.stdout.write(JSON.stringify(results));
    } else {
      const result = validateMessage(payload.raw_text || "");
      process.stdout.write(JSON.stringify(result));
    }
  } catch (e) {
    process.stderr.write(`Validator JSON error: ${e.message}\n`);
    process.exit(1);
  }
});
