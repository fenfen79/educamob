const fs = require('fs');
const path = require('path');

const now = Date.now();
const version = '2.0.1';

// 1. Write public/version.json
const publicDir = path.join(__dirname, '..', 'public');
if (!fs.existsSync(publicDir)) {
  fs.mkdirSync(publicDir, { recursive: true });
}
const versionJsonPath = path.join(publicDir, 'version.json');
fs.writeFileSync(
  versionJsonPath,
  JSON.stringify({ buildTime: now, version: version }, null, 2),
  'utf-8'
);
console.log(`[Version] public/version.json gerado: buildTime=${now}`);

// 2. Write app/version.ts
const appDir = path.join(__dirname, '..', 'app');
const versionTsPath = path.join(appDir, 'version.ts');
fs.writeFileSync(
  versionTsPath,
  `// Arquivo gerado automaticamente no build\nexport const APP_BUILD_TIME = ${now};\nexport const APP_VERSION = "${version}";\n`,
  'utf-8'
);
console.log(`[Version] app/version.ts gerado com sucesso.`);
