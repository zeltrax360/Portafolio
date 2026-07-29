# Setup Automatico - Proyecto 1 Service Desk

Write-Host "================================" -ForegroundColor Cyan
Write-Host "SETUP AUTOMATICO - SERVICE DESK" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Variables
$dbUser = "postgres"
$dbName = "service_desk"
$dbHost = "localhost"
$projectPath = "Proyecto-1-Service-Desk"

# PASO 1: Verificar PostgreSQL
Write-Host "`n[1] Verificando PostgreSQL..." -ForegroundColor Yellow
$pgVersion = psql --version
if ($pgVersion) {
    Write-Host "OK PostgreSQL: $pgVersion" -ForegroundColor Green
} else {
    Write-Host "ERROR: PostgreSQL no encontrado" -ForegroundColor Red
    exit 1
}

# PASO 2: Crear Base de Datos
Write-Host "`n[2] Creando base de datos 'service_desk'..." -ForegroundColor Yellow
psql -U $dbUser -h $dbHost -c "DROP DATABASE IF EXISTS service_desk;" 2>$null
psql -U $dbUser -h $dbHost -c "CREATE DATABASE service_desk;" 2>$null
Write-Host "OK Base de datos creada" -ForegroundColor Green

# PASO 3: Cargar Scripts SQL
Write-Host "`n[3] Cargando esquema SQL..." -ForegroundColor Yellow

psql -U $dbUser -d $dbName -h $dbHost -f "$projectPath\sql\01_create_tables.sql" 2>$null
Write-Host "  OK Tablas creadas" -ForegroundColor Green

psql -U $dbUser -d $dbName -h $dbHost -f "$projectPath\sql\02_insert_data.sql" 2>$null
Write-Host "  OK Datos basicos" -ForegroundColor Green

psql -U $dbUser -d $dbName -h $dbHost -f "$projectPath\sql\03_analysis_queries.sql" 2>$null
Write-Host "  OK Queries cargadas" -ForegroundColor Green

# PASO 4: Generar Datos
Write-Host "`n[4] Generando 10,000 tickets (1-2 minutos)..." -ForegroundColor Yellow
psql -U $dbUser -d $dbName -h $dbHost -f "$projectPath\sql\04_generate_sample_data.sql" 2>$null
Write-Host "OK Datos generados" -ForegroundColor Green

# PASO 5: Verificar Datos
Write-Host "`n[5] Verificando datos..." -ForegroundColor Yellow
$count = psql -U $dbUser -d $dbName -h $dbHost -t -c "SELECT COUNT(*) FROM tickets;" 2>$null
Write-Host "OK Total tickets: $count" -ForegroundColor Green

# PASO 6: Configurar .env
Write-Host "`n[6] Configurando .env..." -ForegroundColor Yellow
$envFile = "$projectPath\.env"
$envContent = @"
DB_HOST=$dbHost
DB_PORT=5432
DB_NAME=$dbName
DB_USER=$dbUser
DB_PASSWORD=
RANDOM_STATE=42
TEST_SIZE=0.2
"@
Set-Content -Path $envFile -Value $envContent -Encoding UTF8
Write-Host "OK .env configurado" -ForegroundColor Green

# PASO 7: Instalar Dependencias Python
Write-Host "`n[7] Instalando dependencias Python..." -ForegroundColor Yellow
pip install -q -r "$projectPath\requirements.txt" 2>$null
Write-Host "OK Dependencias instaladas" -ForegroundColor Green

# PASO 8: Ejecutar Análisis
Write-Host "`n[8] Ejecutando análisis..." -ForegroundColor Yellow

Push-Location $projectPath

Write-Host "  > Exploración de datos..."
python scripts/01_data_exploration.py 2>$null
Write-Host "  OK Exploración completada" -ForegroundColor Green

Write-Host "  > Análisis descriptivo..."
python scripts/03_analysis.py 2>$null
Write-Host "  OK Análisis completado" -ForegroundColor Green

Write-Host "  > Machine Learning..."
python scripts/04_ml_prediction.py 2>$null
Write-Host "  OK ML completado" -ForegroundColor Green

Pop-Location

# PASO 9: Resumen Final
Write-Host "`n================================" -ForegroundColor Cyan
Write-Host "OK SETUP COMPLETADO" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan

Write-Host "`nDatos cargados:" -ForegroundColor Yellow
Write-Host "  - Base de datos: service_desk" -ForegroundColor White
Write-Host "  - Tablas: tecnicos, categorias, tickets, sla_policies" -ForegroundColor White
Write-Host "  - Registros: $count tickets" -ForegroundColor White

Write-Host "`nProximos pasos:" -ForegroundColor Yellow
Write-Host "  1. Abre Power BI Desktop" -ForegroundColor White
Write-Host "  2. Conecta a PostgreSQL (localhost, service_desk)" -ForegroundColor White
Write-Host "  3. Importa tablas y crea dashboard" -ForegroundColor White
Write-Host "  4. Haz git push a GitHub" -ForegroundColor White

Write-Host ""
