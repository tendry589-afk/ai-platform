# backend/app/main.py
"""
Application FastAPI principale - Plateforme IA Multi-Modules
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
from datetime import datetime

from app.core.config import settings
from app.core.security import get_current_user
from app.db.session import engine, SessionLocal
from app.models import Base
from app.api.v1.endpoints import auth, users, chatbot, recommendations, predictions, images, analytics

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Créer les tables
# Base.metadata.create_all(bind=engine)

# Lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestion du cycle de vie de l'application"""
    logger.info("🚀 Application démarrée")
    yield
    logger.info("🛑 Application arrêtée")

# Créer l'application FastAPI
app = FastAPI(
    title="AI Platform API",
    description="Plateforme IA complète avec Chatbot, Recommandations, Prédictions et Vision",
    version="1.0.0",
    lifespan=lifespan
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware Trusted Host
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

# Routes de santé
@app.get("/health", tags=["Health"])
async def health_check():
    """Vérifier la santé de l'application"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

@app.get("/", tags=["Root"])
async def root():
    """Route racine"""
    return {
        "message": "Bienvenue sur AI Platform API",
        "docs": "/docs",
        "version": "1.0.0"
    }

# Inclure les routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot"])
app.include_router(recommendations.router, prefix="/api/v1/recommendations", tags=["Recommendations"])
app.include_router(predictions.router, prefix="/api/v1/predictions", tags=["Predictions"])
app.include_router(images.router, prefix="/api/v1/images", tags=["Images"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])

# Exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Gestionnaire d'exceptions HTTP"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": datetime.utcnow().isoformat()
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Gestionnaire d'exceptions générales"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "status_code": 500,
            "timestamp": datetime.utcnow().isoformat()
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
