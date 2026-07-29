# Script para arreglar autenticacion PostgreSQL

Write-Host "Reparando autenticacion PostgreSQL..." -ForegroundColor Yellow

# Ruta del archivo de configuracion
$pgConfigPath = "C:\Program Files\PostgreSQL\18\data\pg_hba.conf"

# Verificar que existe
if (-not (Test-Path $pgConfigPath)) {
    Write-Host "ERROR: No encontrado $pgConfigPath" -ForegroundColor Red
    exit 1
}

Write-Host "Archivo encontrado: $pgConfigPath" -ForegroundColor Green

# Leer el contenido
$content = Get-Content $pgConfigPath -Raw

# Reemplazar scram-sha-256 por trust (solo para conexiones locales)
$newContent = $content -replace "host\s+all\s+all\s+127\.0\.0\.1/32\s+scram-sha-256", "host    all             all             127.0.0.1/32            trust"
$newContent = $newContent -replace "host\s+all\s+all\s+::1/128\s+scram-sha-256", "host    all             all             ::1/128                 trust"

# Guardar
Set-Content -Path $pgConfigPath -Value $newContent -Encoding UTF8

Write-Host "OK pg_hba.conf actualizado" -ForegroundColor Green

# Reiniciar PostgreSQL
Write-Host "Reiniciando servicio PostgreSQL..." -ForegroundColor Yellow
try {
    Restart-Service -Name "postgresql-x64-18" -Force -ErrorAction Stop
    Write-Host "OK PostgreSQL reiniciado" -ForegroundColor Green
} catch {
    Write-Host "ERROR: No se pudo reiniciar. Intenta manualmente:" -ForegroundColor Red
    Write-Host "  Abre Services (services.msc) y reinicia 'postgresql-x64-18'" -ForegroundColor Yellow
}

Write-Host "`nAhora intenta conectar de nuevo en Power BI" -ForegroundColor Cyan
Write-Host "Haz clic en 'Reintentar'" -ForegroundColor Cyan
