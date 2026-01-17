🚀 Guide de lancement - Windows 11
Fichiers créés
Trois fichiers .bat ont été créés pour faciliter l'utilisation :

Fichier	Description
install.bat	Installe tout automatiquement
launch.bat	Lance les serveurs
stop.bat	Arrête les serveurs
📋 Utilisation
1. Installation complète (une seule fois)
# Double-cliquer sur install.bat
# OU l'exécuter dans PowerShell:
.\install.bat

Ce que fait install.bat :

✅ Installe Git, Python 3.11, Node.js (si manquants)
✅ Crée le dossier C:\Users\[VotreNom]\ai-platform\
✅ Copie tous les fichiers du projet
✅ Installe les dépendances Python (backend)
✅ Installe les dépendances npm (frontend)
✅ Crée les fichiers de configuration
✅ Propose de lancer les serveurs
2. Lancer l'application
# Double-cliquer sur launch.bat
# OU l'exécuter dans PowerShell:
.\launch.bat

Ce que fait launch.bat :

✅ Lance le backend sur http://localhost:8000
✅ Lance le frontend sur http://localhost:3000
✅ Ouvre automatiquement les URLs dans le navigateur
3. Arrêter l'application
# Double-cliquer sur stop.bat
# OU faire Ctrl+C dans chaque terminal
.\stop.bat

Ce que fait stop.bat :

✅ Arrête le backend
✅ Arrête le frontend
✅ Libère les ports 8000 et 3000
🌐 URLs d'accès
Service	URL	Description
Frontend	http://localhost:3000	Interface web
Backend API	http://localhost:8000/docs	Documentation Swagger
Health Check	http://localhost:8000/health	Vérifier que l'API fonctionne
📁 Emplacement du projet
C:\Users\[VotreNom]\ai-platform\
│
├── install.bat      # Script d'installation
├── launch.bat       # Script de lancement
├── stop.bat         # Script d'arrêt
│
├── backend\         # API FastAPI
│   ├── app\         # Code source
│   ├── venv\        # Environnement Python
│   └── requirements.txt
│
├── frontend\        # Application React
│   ├── src\         # Code source
│   └── package.json
│
└── README.md        # Documentation principale

🔧 Dépannage
Problème : "Accès refusé"
→ Relancer PowerShell en tant qu'administrateur

Problème : Port déjà utilisé
→ Exécuter stop.bat puis launch.bat

Problème : Erreur Python
→ Vérifier que Python est dans le PATH:

python --version

Problème : Erreur Node.js
→ Redémarrer PowerShell après installation de Node.js

Réinstaller complètement
.\stop.bat
# Supprimer le dossier ai-platform
.\install.bat

✅ Checklist de vérification
 Les 3 fichiers .bat sont présents
 install.bat s'exécute sans erreur
 launch.bat lance les serveurs
 http://localhost:3000 s'ouvre dans le navigateur
 http://localhost:8000/docs affiche la documentation API
 stop.bat arrête les serveurs proprement
