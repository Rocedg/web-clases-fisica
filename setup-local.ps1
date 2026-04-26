$ErrorActionPreference = "Stop"

Set-Location -Path $PSScriptRoot
$env:PYTHONIOENCODING = "utf-8"

$pythonPath = ".\.venv\Scripts\python.exe"

Write-Host "Setting up Rocedg Física Bach for local development..."
Write-Host ""

if (-not (Test-Path $pythonPath)) {
    Write-Host "Creating .venv..."
    py -m venv .venv
}
else {
    Write-Host ".venv already exists."
}

Write-Host ""
Write-Host "Installing dependencies from requirements.txt..."
& $pythonPath -m pip install -r requirements.txt

Write-Host ""
Write-Host "Setup complete."
Write-Host "Now run .\run-local.ps1 or double-click start-web.bat"
Write-Host "Local URL: http://127.0.0.1:5000"
