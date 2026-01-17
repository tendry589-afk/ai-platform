@echo off
chcp 65001 >nul
title AI Platform - Lancement

set "PROJECT_DIR=%USERPROFILE%\ai-platform"

:: Verifier que le projet existe
if not exist "%PROJECT_DIR%" (
    echo [ERREUR] Le projet n'existe pas!
    echo Veuillez d'abord executer install.bat
    pause
    exit /b 1
)

echo [1/4] Verification Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python non trouve!
    pause
    exit /b 1
)
echo [OK] Python trouve

echo [2/4] Verification Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Node.js non trouve!
    pause
    exit /b 1
)
echo [OK] Node.js trouve

echo [3/4] Verification Backend...
if not exist "%PROJECT_DIR%\backend\venv" (
    echo [ERREUR] Backend non installe!
    pause
    exit /b 1
)
echo [OK] Backend trouve

echo [4/4] Verification Frontend...
if not exist "%PROJECT_DIR%\frontend\package.json" (
    echo [ERREUR] Frontend non installe!
    pause
    exit /b 1
)
echo [OK] Frontend trouve

echo.
echo [OK] Toutes les verifications passees!

:: Arreter les serveurs precedents
echo.
echo [INFO] Arret des serveurs precedents...
taskkill /FI "WINDOWTITLE *AI Platform - Backend*" /F >nul 2>&1
taskkill /FI "WINDOWTITLE *AI Platform - Frontend*" /F >nul 2>&1
echo [OK] Serveurs arretes

:: Lancer le BACKEND
echo.
echo [LANCEMENT] Backend (port 8000)...
cd /d "%PROJECT_DIR%\backend"
call venv\Scripts\activate >nul 2>&1
start "AI Platform - Backend (8000)" cmd /k "cd /d %PROJECT_DIR%\backend && venv\Scripts\activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
timeout /t 8 /nobreak >nul

:: Lancer le FRONTEND
echo.
echo [LANCEMENT] Frontend (port 3000)...
cd /d "%PROJECT_DIR%\frontend"
start "AI Platform - Frontend (3000)" cmd /k "cd /d %PROJECT_DIR%\frontend && npm run dev"
timeout /t 5 /nobreak >nul

echo.
echo ============================================
echo         SERVEURS LANCES AVEC SUCCES!
echo ============================================
echo.
echo    Frontend: http://localhost:3000
echo    Backend:  http://localhost:8000/docs
echo    Health:   http://localhost:8000/health
echo.
echo Appuyez sur une touche pour ouvrir...
pause >nul
start http://localhost:3000
start http://localhost:8000/docs
echo.
echo Bon utilisation!
pause