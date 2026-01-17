AI Platform - Plateforme IA Complète

Plateforme IA modulaire et open-source offrant 4 modules principaux :





💬 Chatbot NLP - Conversations intelligentes



⭐ Recommandations - Suggestions personnalisées



🔮 Analyse Prédictive - Prédictions ML



👁️ Vision par Ordinateur - Classification d'images

🚀 Démarrage Rapide

Prérequis





Docker & Docker Compose



Node.js 18+ (pour le développement frontend)



Python 3.11+ (pour le développement backend)

Installation avec Docker (Recommandé)

# Cloner le projet
git clone https://github.com/votre-repo/ai-platform.git
cd ai-platform

# Lancer les services
docker-compose up -d

# Accéder à l'application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000/docs


Installation Manuelle

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend (nouveau terminal)
cd frontend
npm install
npm run dev


📁 Structure du Projet

ai-platform/
├── frontend/              # Application React
│   ├── src/
│   │   ├── components/   # Composants réutilisables
│   │   ├── pages/        # Pages de l'application
│   │   ├── services/     # Services API
│   │   ├── store/        # Redux store
│   │   └── styles/       # Styles CSS
│   ├── package.json
│   └── Dockerfile
│
├── backend/               # API FastAPI
│   ├── app/
│   │   ├── api/         # Endpoints API
│   │   ├── core/        # Configuration & sécurité
│   │   ├── models/      # Modèles SQLAlchemy
│   │   ├── ai/          # Modules IA
│   │   │   ├── nlp/     # Chatbot NLP
│   │   │   ├── ml/      # Machine Learning
│   │   │   └── cv/      # Computer Vision
│   │   └── db/          # Base de données
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml     # Configuration Docker
└── README.md


🛠️ Stack Technologique

Frontend





Framework: React 18 + TypeScript



Build: Vite



State Management: Redux Toolkit



Styling: TailwindCSS



HTTP Client: Axios

Backend





Framework: FastAPI (Python 3.11)



ORM: SQLAlchemy



Validation: Pydantic



Auth: JWT + OAuth2



Base de données: PostgreSQL, MongoDB, Redis

IA/ML





NLP: Hugging Face Transformers, spaCy



ML Classique: Scikit-learn, XGBoost



Deep Learning: PyTorch, TensorFlow



Computer Vision: OpenCV, YOLO

📡 API Reference

Authentication

POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh


Chatbot

POST /api/v1/chatbot/chat
GET  /api/v1/chatbot/conversations
POST /api/v1/chatbot/conversations


Recommandations

GET /api/v1/recommendations/


Prédictions

POST /api/v1/predictions/


Images

POST /api/v1/images/classify


🔧 Configuration

Variables d'Environnement

Créez un fichier .env dans le dossier backend/:

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ai_platform
MONGODB_URL=mongodb://user:password@localhost:27017/ai_platform
REDIS_URL=redis://:password@localhost:6379/0

# Security
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# AI Models
HUGGINGFACE_API_KEY=your-hf-key


🧪 Tests

# Backend tests
cd backend
pytest -v

# Frontend tests
cd frontend
npm test


📦 Déploiement

Production avec Docker

# Build des images
docker-compose -f docker-compose.prod.yml build

# Déploiement
docker-compose -f docker-compose.prod.yml up -d


Cloud (Gratuit)





Frontend: Vercel, Netlify



Backend: Railway, Render, Fly.io



Database: Railway, Supabase, Neon

🤝 Contribution





Fork le projet



Créez une branche (git checkout -b feature/amazing-feature)



Committez (git commit -m 'Add amazing feature')



Push (git push origin feature/amazing-feature)



Ouvrez une Pull Request

📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.



⭐ Star our repo if you like it!