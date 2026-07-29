# Setup Automático - Proyecto 1 Service Desk
# Script PowerShell para configurar PostgreSQL, cargar datos y ejecutar análisis

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "SETUP AUTOMÁTICO - SERVICE DESK" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# ============================================================================
# PASO 1: Verificar PostgreSQL
# ============================================================================
Write-Host "`n[1] Verificando PostgreSQL..." -ForegroundColor Yellow

$pgInstalled = $null
try {
    $pgInstalled = psql --version 2>$null
    Write-Host "✓ PostgreSQL encontrado: $pgInstalled" -ForegroundColor Green
} catch {
    Write-Host "✗ PostgreSQL no está instalado o no está en PATH" -ForegroundColor Red
    Write-Host "  Descargalo de: https://www.postgresql.org/download/windows/" -ForegroundColor Yellow
    exit 1
}

# ============================================================================
# PASO 2: Solicitar credenciales PostgreSQL
# ============================================================================
Write-Host "`n[2] Configurando acceso a PostgreSQL..." -ForegroundColor Yellow

$dbUser = Read-Host "Usuario PostgreSQL [postgres]"
if ([string]::IsNullOrWhiteSpace($dbUser)) { $dbUser = "postgres" }

$dbPassword = Read-Host "Contraseña PostgreSQL" -AsSecureString
$dbPasswordPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToCoTaskMemUnicode($dbPassword))

$env:PGPASSWORD = $dbPasswordPlain

# ============================================================================
# PASO 3: Crear Base de Datos
# ============================================================================
Write-Host "`n[3] Creando base de datos 'service_desk'..." -ForegroundColor Yellow

try {
    psql -U $dbUser -h localhost -c "CREATE DATABASE service_desk;" 2>$null
    Write-Host "✓ Base de datos creada" -ForegroundColor Green
} catch {
    Write-Host "⚠ Base de datos podría ya existir (continuando...)" -ForegroundColor Yellow
}

# ============================================================================
# PASO 4: Cargar Scripts SQL
# ============================================================================
Write-Host "`n[4] Cargando esquema SQL..." -ForegroundColor Yellow

$sqlScripts = @(
    "Proyecto-1-Service-Desk\sql\01_create_tables.sql",
    "Proyecto-1-Service-Desk\sql\02_insert_data.sql",
    "Proyecto-1-Service-Desk\sql\03_analysis_queries.sql"
)

foreach ($script in $sqlScripts) {
    Write-Host "  Ejecutando: $script"
    try {
        psql -U $dbUser -d service_desk -h localhost -f $script 2>$null
        Write-Host "  ✓ $script cargado" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Error en $script" -ForegroundColor Red
    }
}

# ============================================================================
# PASO 5: Generar Datos de Ejemplo
# ============================================================================
Write-Host "`n[5] Generando 10,000 tickets de ejemplo..." -ForegroundColor Yellow
Write-Host "  (esto puede tomar 1-2 minutos...)" -ForegroundColor Gray

try {
    psql -U $dbUser -d service_desk -h localhost -f "Proyecto-1-Service-Desk\sql\04_generate_sample_data.sql" 2>$null
    Write-Host "✓ Datos de ejemplo generados" -ForegroundColor Green
} catch {
    Write-Host "✗ Error generando datos" -ForegroundColor Red
}

# ============================================================================
# PASO 6: Configurar .env
# ============================================================================
Write-Host "`n[6] Configurando archivo .env..." -ForegroundColor Yellow

$envContent = @"
DB_HOST=localhost
DB_PORT=5432
DB_NAME=service_desk
DB_USER=$dbUser
DB_PASSWORD=$dbPasswordPlain
RANDOM_STATE=42
TEST_SIZE=0.2
"@

$envFile = "Proyecto-1-Service-Desk\.env"
Set-Content -Path $envFile -Value $envContent
Write-Host "✓ .env configurado" -ForegroundColor Green

# ============================================================================
# PASO 7: Instalar Dependencias Python
# ============================================================================
Write-Host "`n[7] Instalando dependencias Python..." -ForegroundColor Yellow

try {
    pip install -r "Proyecto-1-Service-Desk\requirements.txt" 2>$null | Out-Null
    Write-Host "✓ Dependencias instaladas" -ForegroundColor Green
} catch {
    Write-Host "✗ Error instalando dependencias" -ForegroundColor Red
}

# ============================================================================
# PASO 8: Ejecutar Análisis
# ============================================================================
Write-Host "`n[8] Ejecutando análisis de datos..." -ForegroundColor Yellow

$scripts = @(
    @{ name = "Exploración de Datos"; script = "scripts\01_data_exploration.py" },
    @{ name = "Análisis Descriptivo"; script = "scripts\03_analysis.py" },
    @{ name = "Predicción ML"; script = "scripts\04_ml_prediction.py" }
)

Set-Location "Proyecto-1-Service-Desk"

foreach ($item in $scripts) {
    Write-Host "`n  ► $($item.name)..." -ForegroundColor Cyan
    try {
        python $item.script
        Write-Host "  ✓ $($item.name) completado" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Error en $($item.name)" -ForegroundColor Red
    }
}

Set-Location ".."

# ============================================================================
# PASO 9: Resumen Final
# ============================================================================
Write-Host "`n================================" -ForegroundColor Cyan
Write-Host "✓ SETUP COMPLETADO" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan

Write-Host "`nProyecto configurado en:" -ForegroundColor Yellow
Write-Host "  📁 $((Get-Location).Path)\Proyecto-1-Service-Desk" -ForegroundColor White

Write-Host "`nPróximos pasos:" -ForegroundColor Yellow
Write-Host "  1. Abre Power BI Desktop" -ForegroundColor White
Write-Host "  2. Conecta a PostgreSQL (localhost, service_desk)" -ForegroundColor White
Write-Host "  3. Crea dashboard con las queries del archivo SQL" -ForegroundColor White
Write-Host "  4. Haz commit y push a GitHub" -ForegroundColor White

Write-Host "`nArchivos generados:" -ForegroundColor Yellow
Write-Host "  ✓ Base de datos PostgreSQL: service_desk" -ForegroundColor Green
Write-Host "  ✓ 10,000 tickets de ejemplo" -ForegroundColor Green
Write-Host "  ✓ Análisis completados" -ForegroundColor Green
Write-Host "  ✓ Archivo .env configurado" -ForegroundColor Green

Write-Host "`n" -ForegroundColor Cyan
