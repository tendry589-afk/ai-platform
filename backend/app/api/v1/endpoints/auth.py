# backend/app/api/v1/endpoints/auth.py
"""
Endpoints d'authentification
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from pydantic import BaseModel, EmailStr
import logging

from app.core.security import SecurityUtils, get_db
from app.models import User
from app.core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

# Schémas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str = None
    last_name: str = None

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    first_name: str = None
    last_name: str = None
    is_active: bool
    is_verified: bool

# Endpoints
@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """Enregistrer un nouvel utilisateur"""
    
    # Vérifier si l'utilisateur existe
    existing_user = db.query(User).filter(
        (User.email == request.email) | (User.username == request.username)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )
    
    # Créer l'utilisateur
    user = User(
        email=request.email,
        username=request.username,
        password_hash=SecurityUtils.hash_password(request.password),
        first_name=request.first_name,
        last_name=request.last_name
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    logger.info(f"User registered: {user.email}")
    
    # Créer les tokens
    access_token = SecurityUtils.create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = SecurityUtils.create_refresh_token(
        data={"sub": str(user.id)}
    )
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Connexion utilisateur"""
    
    # Trouver l'utilisateur
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user or not SecurityUtils.verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    
    logger.info(f"User logged in: {user.email}")
    
    # Créer les tokens
    access_token = SecurityUtils.create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = SecurityUtils.create_refresh_token(
        data={"sub": str(user.id)}
    )
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str):
    """Rafraîchir le token d'accès"""
    
    try:
        payload = SecurityUtils.decode_token(refresh_token)
        user_id = payload.get("sub")
        
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        # Créer un nouveau token d'accès
        access_token = SecurityUtils.create_access_token(
            data={"sub": user_id},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    except Exception as e:
        logger.error(f"Token refresh error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )

@router.post("/logout")
async def logout():
    """Déconnexion utilisateur"""
    # Dans une implémentation réelle, on invaliderait le token
    return {"message": "Logged out successfully"}
