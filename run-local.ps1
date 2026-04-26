$ErrorActionPreference = "Stop"

Set-Location -Path $PSScriptRoot
$env:PYTHONIOENCODING = "utf-8"

$pythonPath = ".\.venv\Scripts\python.exe"

Write-Host "Starting Rocedg Física Bach locally..."
Write-Host ""

if (-not (Test-Path $pythonPath)) {
    Write-Host "Could not find .\.venv\Scripts\python.exe."
    Write-Host ""
    Write-Host "Create the virtual environment first:"
    Write-Host "  py -m venv .venv"
    Write-Host "  .\.venv\Scripts\python.exe -m pip install -r requirements.txt"
    Write-Host ""
    Write-Host "Then run:"
    Write-Host "  .\run-local.ps1"
    Write-Host ""
    Write-Host "Local URL:"
    Write-Host "  http://127.0.0.1:5000"
    exit 1
}

Write-Host "Open http://127.0.0.1:5000 in your browser."
Write-Host "Press CTRL+C to stop the server."
Write-Host ""

& $pythonPath app.py
