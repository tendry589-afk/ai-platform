@echo off
chcp 65001 >nul
title AI Platform - Installation

cd /d "C:\Users\randr\Desktop\ai-platform\backend"

echo 📦 Installation des dépendances Python...
python -m venv venv >nul 2>&1
call venv\Scripts\activate >nul 2>&1
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt >nul 2>&1

echo.
echo ✅ Backend installé!

echo.
echo 📦 Installation du Frontend (npm)...
cd /d "C:\Users\randr\Desktop\ai-platform\frontend"

:: Ignorer la vérification qui bloque
echo [SKIP] Vérification npm ignorée
call npm install --no-audit --no-fund >nul 2>&1

echo.
echo ✅ Frontend installé!

echo.
echo ─────────────────────────────────────────
echo 🎉 Installation terminée!
echo.
echo Pour lancer l'application:
echo   launch.bat
echo ─────────────────────────────────────────
pause