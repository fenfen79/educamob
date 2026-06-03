$backendDir = "C:\Users\nepov\.gemini\antigravity\worktrees\Nascedouro\mobme-rag-multimodal-tutor\backend"

Write-Host "Iniciando teste de build da imagem Docker do Backend..."

Push-Location $backendDir
try {
    # Testa a compilação da imagem Docker
    docker build -t educamob-backend-test .
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ SUCESSO: A imagem Docker do backend compilou perfeitamente." -ForegroundColor Green
    } else {
        Write-Host "❌ ERRO: Falha ao compilar a imagem Docker." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} finally {
    Pop-Location
}
