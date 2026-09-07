# Instalar PostgreSQL ODBC Driver para Power BI

Write-Host "Instalando PostgreSQL ODBC Driver..." -ForegroundColor Yellow

# Descargar PostgreSQL ODBC Driver
$url = "https://ftp.postgresql.org/pub/odbc/versions/msi/psqlodbc_14_02_0000-w64.msi"
$output = "$env:TEMP\psqlodbc_installer.msi"

Write-Host "Descargando PostgreSQL ODBC Driver..." -ForegroundColor Cyan
(New-Object System.Net.WebClient).DownloadFile($url, $output)

Write-Host "Instalando..." -ForegroundColor Cyan
Start-Process -FilePath msiexec.exe -ArgumentList "/i $output /quiet" -Wait

Write-Host "OK ODBC Driver instalado" -ForegroundColor Green

# Limpiar archivo temporal
Remove-Item $output -Force

Write-Host "`nAhora intenta conectar de nuevo en Power BI" -ForegroundColor Cyan
Write-Host "Server: localhost" -ForegroundColor White
Write-Host "Database: service_desk" -ForegroundColor White
Write-Host "Username: postgres" -ForegroundColor White
Write-Host "Password: (dejar vacío)" -ForegroundColor White
