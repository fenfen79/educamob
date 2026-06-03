import { test, expect } from '@playwright/test';

test.describe('Integração Super Chat Mob.Me (Tutor)', () => {

  test('Interface estática deve carregar sem erros', async ({ page }) => {
    // Acesse o arquivo index.html servido localmente na pasta apps/tutor
    // Certifique-se de iniciar um servidor estático antes, ex: npx serve . -p 3000
    await page.goto('http://localhost:3000/apps/tutor/index.html');

    // Verifica se o título de boas-vindas carregou
    await expect(page.locator('.welcome-title')).toBeVisible({ timeout: 10000 });
    
    // Verifica se os botões de sugestão apareceram
    const suggestions = page.locator('.suggestion-chip');
    await expect(suggestions).toHaveCount(4);
  });

  test('Botão Voltar para o Portal deve estar presente', async ({ page }) => {
    await page.goto('http://localhost:3000/apps/tutor/index.html');
    
    // O botão deve ter o texto "Voltar para o Portal" e apontar para educamob.com.br
    const backBtn = page.locator('text=Voltar para o Portal');
    await expect(backBtn).toBeVisible();
    await expect(backBtn).toHaveAttribute('href', 'https://educamob.com.br');
  });

  test('Input de chat não deve estar bloqueado no carregamento', async ({ page }) => {
    await page.goto('http://localhost:3000/apps/tutor/index.html');
    
    const input = page.locator('textarea.input-textarea');
    await expect(input).toBeVisible();
    await expect(input).toBeEnabled();
  });
});
