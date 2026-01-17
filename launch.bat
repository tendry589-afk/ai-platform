@echo off
chcp 65001 >nul
title AI Platform - Serveurs
color 0A

echo ╔══════════════════════════════════════════════════════════════╗
echo ║              AI PLATFORM - LANCEMENT DES SERVEURS             ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

set "PROJECT_DIR=%USERPROFILE%\ai-platform"

:: Vérifier que le projet existe
if not exist "%PROJECT_DIR%" (
    echo ❌ ERREUR: Le dossier du projet n'existe pas!
    echo.
    echo Veuillez d'abord exécuter install.bat pour installer l'application.
    echo.
    pause
    exit /b 1
)

:: Vérifier que le backend existe
if not exist "%PROJECT_DIR%\backend\venv\Scripts\activate.bat" (
    echo ❌ ERREUR: Backend non installé!
    echo.
    echo Veuillez d'abord exécuter install.bat pour installer l'application.
    echo.
    pause
    exit /b 1
)

:: Vérifier que le frontend existe
if not exist "%PROJECT_DIR%\frontend\package.json" (
    echo ❌ ERREUR: Frontend non installé!
    echo.
    echo Veuillez d'abord exécuter install.bat pour installer l'application.
    echo.
    pause
    exit /b 1
)

echo ✅ Vérification terminée - tout est prêt!
echo.

echo 🎯 Lancement des serveurs...
echo.
echo Pour arrêter les serveurs: appuyez sur Ctrl+C dans chaque terminal
echo.

:: Lancer le backend
start "AI Platform - Backend (http://localhost:8000)" cmd /k "cd /d %PROJECT_DIR%\backend && venv\Scripts\activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

:: Attendre que le backend démarre
timeout /t 5 /nobreak >nul

:: Lancer le frontend
start "AI Platform - Frontend (http://localhost:3000)" cmd /k "cd /d %PROJECT_DIR%\frontend && npm run dev"

echo ──────────────────────────────────────────────────────────────
echo ✅ Serveurs lancés avec succès!
echo.
echo 🌐 ACCÈS À L'APPLICATION:
echo    Frontend: http://localhost:3000
echo    Backend:  http://localhost:8000/docs
echo ──────────────────────────────────────────────────────────────
echo.

echo Appuyez sur une touche pour ouvrir les URLs dans le navigateur...
pause >nul

:: Ouvrir les URLs dans le navigateur
start http://localhost:3000
start http://localhost:8000/docs

echo.
echo 🎉 Bon utilisation de AI Platform!
echo.

pause
exit /b 0
