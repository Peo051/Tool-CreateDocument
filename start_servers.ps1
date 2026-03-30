#!/usr/bin/env pwsh
# Start both backend and frontend servers

Write-Host "Starting Report Generator Web UI..." -ForegroundColor Green

# Check if backend dependencies are installed
Write-Host "`nChecking backend dependencies..." -ForegroundColor Yellow
$fastapi = pip list | Select-String "fastapi"
if (-not $fastapi) {
    Write-Host "Installing backend dependencies..." -ForegroundColor Yellow
    pip install -r requirements_api.txt
}

# Check if frontend dependencies are installed
Write-Host "`nChecking frontend dependencies..." -ForegroundColor Yellow
if (-not (Test-Path "web/node_modules")) {
    Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
    cd web
    npm install
    cd ..
}

Write-Host "`nStarting servers..." -ForegroundColor Green
Write-Host "Backend will run on: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend will run on: http://localhost:3000" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop both servers" -ForegroundColor Yellow

# Start backend in background
$backend = Start-Process -FilePath "python" -ArgumentList "run_api.py" -PassThru -NoNewWindow

# Start frontend in background
$frontend = Start-Process -FilePath "npm" -ArgumentList "run", "dev" -WorkingDirectory "web" -PassThru -NoNewWindow

Write-Host "`nServers started!" -ForegroundColor Green
Write-Host "Backend PID: $($backend.Id)" -ForegroundColor Cyan
Write-Host "Frontend PID: $($frontend.Id)" -ForegroundColor Cyan
Write-Host "`nWaiting for servers to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

Write-Host "`nTesting backend health..." -ForegroundColor Yellow
try {
    $health = Invoke-RestMethod -Uri "http://localhost:8000/api/health" -TimeoutSec 5
    Write-Host "Backend is healthy: $($health.status)" -ForegroundColor Green
} catch {
    Write-Host "Backend health check failed (may still be starting)" -ForegroundColor Yellow
}

Write-Host "`nOpen http://localhost:3000 in your browser to use the application" -ForegroundColor Green
Write-Host "`nPress any key to stop servers..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

Write-Host "`nStopping servers..." -ForegroundColor Yellow
Stop-Process -Id $backend.Id -Force -ErrorAction SilentlyContinue
Stop-Process -Id $frontend.Id -Force -ErrorAction SilentlyContinue
Write-Host "Servers stopped." -ForegroundColor Green
