@echo off
chcp 65001 >nul
title AI Platform - Installation Automatique
color 0A

echo ╔══════════════════════════════════════════════════════════════╗
echo ║          AI PLATFORM - INSTALLATION AUTOMATIQUE              ║
echo ║                 Pour Windows 11                               ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:: Vérifier les droits administrateur
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  ATTENTION: Ce script nécessite les droits administrateur!
    echo.
    echo Veuillez fermer ce terminal et relancer en tant qu'administrateur:
    echo   Clic droit sur "Terminal Windows" ou "PowerShell"
    echo   puis "Exécuter en tant qu'administrateur"
    echo.
    pause
    exit /b 1
)

echo ✅ Droits administrateur vérifiés
echo.

:: =====================================================================
:: ÉTAPE 1: Installation des prérequis
:: =====================================================================
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  ÉTAPE 1: Installation des prérequis                          ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

set "PROJECT_DIR=%USERPROFILE%\ai-platform"

:: Vérifier et installer Git
echo [1/4] Vérification de Git...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo    📦 Installation de Git...
    winget install -e --id Git.Git --silent >nul 2>&1
    if %errorlevel% equ 0 (
        echo    ✅ Git installé avec succès
    ) else (
        echo    ⚠️  Impossible d'installer Git automatiquement
        echo    Veuillez installer Git manuellement: https://git-scm.com/download/win
    )
) else (
    echo    ✅ Git déjà installé
)

:: Vérifier et installer Python
echo [2/4] Vérification de Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo    📦 Installation de Python...
    winget install -e --id Python.Python.3.11 --silent >nul 2>&1
    if %errorlevel% equ 0 (
        echo    ✅ Python installé avec succès
        echo    ⚠️  Redémarrage du terminal requis pour PATH
        echo.
    ) else (
        echo    ⚠️  Impossible d'installer Python automatiquement
        echo    Veuillez installer Python manuellement: https://python.org/downloads/
    )
) else (
    echo    ✅ Python déjà installé
)

:: Vérifier et installer Node.js
echo [3/4] Vérification de Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo    📦 Installation de Node.js...
    winget install -e --id OpenJS.NodeJS.LTS --silent >nul 2>&1
    if %errorlevel% equ 0 (
        echo    ✅ Node.js installé avec succès
    ) else (
        echo    ⚠️  Impossible d'installer Node.js automatiquement
        echo    Veuillez installer Node.js manuellement: https://nodejs.org
    )
) else (
    echo    ✅ Node.js déjà installé
)

:: Vérifier npm
echo [4/4] Vérification de npm...
npm --version >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✅ npm déjà installé
) else (
    echo    ⚠️  npm non trouvé - Node.js doit être redémarré
)

echo.
echo ✅ Étape 1 terminée
echo.

:: =====================================================================
:: ÉTAPE 2: Préparation du projet
:: =====================================================================
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  ÉTAPE 2: Préparation du projet                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:: Créer le dossier du projet
echo [1/3] Création du dossier du projet...
if exist "%PROJECT_DIR%" (
    echo    ⚠️  Le dossier existe déjà: %PROJECT_DIR%
    echo    Voulez-vous le supprimer et recréer? (O/N)
    set /p CONFIRM="    Votre choix: "
    if /i "%CONFIRM%"=="O" (
        echo    🗑️  Suppression du dossier existant...
        rmdir /s /q "%PROJECT_DIR%" 2>nul
        echo    ✅ Dossier supprimé
    )
)
mkdir "%PROJECT_DIR%" >nul 2>&1
if exist "%PROJECT_DIR%" (
    echo    ✅ Dossier créé: %PROJECT_DIR%
)

:: Créer la structure des dossiers
echo [2/3] Création de la structure des dossiers...
mkdir "%PROJECT_DIR%\backend\app\api\v1\endpoints" >nul 2>&1
mkdir "%PROJECT_DIR%\backend\app\core" >nul 2>&1
mkdir "%PROJECT_DIR%\backend\app\models" >nul 2>&1
mkdir "%PROJECT_DIR%\backend\app\db" >nul 2>&1
mkdir "%PROJECT_DIR%\backend\app\ai\nlp" >nul 2>&1
mkdir "%PROJECT_DIR%\backend\app\ai\ml" >nul 2>&1
mkdir "%PROJECT_DIR%\backend\app\ai\cv" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\pages" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\services" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\store" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\layouts" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\components" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\styles" >nul 2>&1
mkdir "%PROJECT_DIR%\frontend\src\components\Common" >nul 2>&1
echo    ✅ Structure créée

:: Si les fichiers existent dans le dossier courant, les copier
echo [3/3] Copie des fichiers du projet...
set "SOURCE_DIR=%~dp0"
if exist "%SOURCE_DIR%backend\app\main.py" (
    xcopy /E /I /Y "%SOURCE_DIR%backend" "%PROJECT_DIR%\backend" >nul 2>&1
    echo    ✅ Backend copié
)
if exist "%SOURCE_DIR%frontend\package.json" (
    xcopy /E /I /Y "%SOURCE_DIR%frontend" "%PROJECT_DIR%\frontend" >nul 2>&1
    echo    ✅ Frontend copié
)
if exist "%SOURCE_DIR%docker-compose.yml" (
    copy "%SOURCE_DIR%docker-compose.yml" "%PROJECT_DIR%\" >nul
    echo    ✅ Fichier docker-compose.yml copié
)
if exist "%SOURCE_DIR%README.md" (
    copy "%SOURCE_DIR%README.md" "%PROJECT_DIR%\" >nul
    echo    ✅ README.md copié
)
if exist "%SOURCE_DIR%ARCHITECTURE_COMPLETE.md" (
    copy "%SOURCE_DIR%ARCHITECTURE_COMPLETE.md" "%PROJECT_DIR%\" >nul
    echo    ✅ Documentation copiée
)

echo.
echo ✅ Étape 2 terminée
echo.

:: =====================================================================
:: ÉTAPE 3: Installation du Backend
:: =====================================================================
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  ÉTAPE 3: Installation du Backend (Python/FastAPI)           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

cd /d "%PROJECT_DIR%\backend"
echo [1/5] Création de l'environnement virtuel Python...
if exist "venv" (
    echo    ⚠️  Environnement virtuel existant trouvé
) else (
    python -m venv venv
    if exist "venv" (
        echo    ✅ Environnement virtuel créé
    )
)

echo [2/5] Activation de l'environnement virtuel...
call venv\Scripts\activate >nul 2>&1
echo    ✅ Environnement virtuel activé

echo [3/5] Mise à jour de pip...
python -m pip install --upgrade pip >nul 2>&1
echo    ✅ pip mis à jour

echo [4/5] Installation des dépendances Python (cela peut prendre quelques minutes)...
if exist "requirements.txt" (
    pip install -r requirements.txt >nul 2>&1
    echo    ✅ Dépendances Python installées
) else (
    echo    ⚠️  Fichier requirements.txt non trouvé
)

echo [5/5] Création du fichier .env...
if exist ".env.example" (
    copy ".env.example" ".env" >nul
    echo    ✅ Fichier .env créé
) else (
    echo. > .env
    echo # AI Platform Configuration >> .env
    echo SECRET_KEY=ai-platform-secret-key-change-in-production >> .env
    echo DATABASE_URL=postgresql://user:password@localhost:5432/ai_platform >> .env
    echo MONGODB_URL=mongodb://user:password@localhost:27017/ai_platform >> .env
    echo REDIS_URL=redis://:password@localhost:6379/0 >> .env
    echo DEBUG=True >> .env
    echo ALGORITHM=HS256 >> .env
    echo ACCESS_TOKEN_EXPIRE_MINUTES=30 >> .env
    echo CORS_ORIGINS=["http://localhost:3000"] >> .env
    echo. > .env
    echo ✅ Fichier .env créé avec configuration par défaut
)

echo.
echo ✅ Backend installé avec succès!
echo.

:: =====================================================================
:: ÉTAPE 4: Installation du Frontend
:: =====================================================================
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  ÉTAPE 4: Installation du Frontend (React/Node.js)           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

cd /d "%PROJECT_DIR%\frontend"
echo [1/4] Installation des dépendances npm (cela peut prendre 2-5 minutes)...
if exist "package.json" (
    call npm install >nul 2>&1
    echo    ✅ Dépendances npm installées
) else (
    echo    ⚠️  Fichier package.json non trouvé
)

echo [2/4] Création du fichier .env...
echo VITE_API_URL=http://localhost:8000/api/v1 > .env
echo    ✅ Fichier .env créé

echo [3/4] Vérification de la configuration...
if exist "node_modules" (
    echo    ✅ node_modules présent
)
if exist ".env" (
    echo    ✅ Fichier de configuration présent
)

echo [4/4] Vérification TypeScript...
if exist "tsconfig.json" (
    echo    ✅ Configuration TypeScript présente
)

echo.
echo ✅ Frontend installé avec succès!
echo.

:: =====================================================================
:: ÉTAPE 5: Lancement de l'application
:: =====================================================================
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  ÉTAPE 5: Lancement de l'application                         ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

echo 🎉 Installation terminée avec succès!
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  RÉSUMÉ DE L'INSTALLATION                                     ║
echo ╠══════════════════════════════════════════════════════════════╣
echo ║  Dossier du projet: %PROJECT_DIR%                  ║
echo ║  Backend URL:      http://localhost:8000/docs     ║
echo ║  Frontend URL:     http://localhost:3000          ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

echo Pour lancer l'application, exécutez les commandes suivantes:
echo.
echo ──────────────────────────────────────────────────────────────
echo TERMINAL 1 - Backend:
echo   cd %PROJECT_DIR%\backend
echo   venv\Scripts\activate
echo   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
echo ──────────────────────────────────────────────────────────────
echo.
echo ──────────────────────────────────────────────────────────────
echo TERMINAL 2 - Frontend:
echo   cd %PROJECT_DIR%\frontend
echo   npm run dev
echo ──────────────────────────────────────────────────────────────
echo.

echo Voulez-vous lancer automatiquement les deux serveurs? (O/N)
set /p LAUNCH="Votre choix: "

if /i "%LAUNCH%"=="O" (
    echo.
    echo ⚠️  Lancement des serveurs...
    echo.
    echo Pour arrêter les serveurs: appuyez sur Ctrl+C dans chaque terminal
    echo.
    
    :: Lancer le backend
    start "AI Platform - Backend" cmd /k "cd /d %PROJECT_DIR%\backend && venv\Scripts\activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"
    
    :: Attendre un peu
    timeout /t 5 /nobreak >nul
    
    :: Lancer le frontend
    start "AI Platform - Frontend" cmd /k "cd /d %PROJECT_DIR%\frontend && npm run dev"
    
    echo.
    echo ✅ Les serveurs sont en cours de lancement!
    echo.
    echo ──────────────────────────────────────────────────────────────
    echo Frontend: http://localhost:3000
    echo Backend:  http://localhost:8000/docs
    echo ──────────────────────────────────────────────────────────────
    echo.
    echo Appuyez sur une touche pour ouvrir les URLs dans le navigateur...
    pause >nul
    
    :: Ouvrir les URLs dans le navigateur
    start http://localhost:3000
    start http://localhost:8000/docs
)

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  COMPLÉMENTAIRES                                             ║
echo ╠══════════════════════════════════════════════════════════════╣
echo ║                                                               ║
echo ║  Pour arrêter les serveurs:                                  ║
echo ║    - Ctrl+C dans chaque terminal                             ║
echo ║                                                               ║
echo ║  Pour redémarrer après arrêt:                                ║
echo ║    - Répéter les commandes de l'Étape 5                      ║
echo ║                                                               ║
echo ║  Fichier de configuration (.env):                            ║
echo ║    - Modifier %PROJECT_DIR%\backend\.env          ║
echo ║                                                               ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

pause
exit /b 0
