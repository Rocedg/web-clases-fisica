@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo Starting Rocedg Física Bach locally...
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Could not find .venv\Scripts\python.exe.
    echo.
    echo Please create the virtual environment first:
    echo   py -m venv .venv
    echo   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    echo.
    echo You can also run setup-local.ps1 from PowerShell.
    echo.
    pause
    exit /b 1
)

set PYTHONIOENCODING=utf-8

echo Open http://127.0.0.1:5000 in your browser.
echo Press CTRL+C to stop the server.
echo.

".venv\Scripts\python.exe" app.py

echo.
echo Server stopped.
pause
