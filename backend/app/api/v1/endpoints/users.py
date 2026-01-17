# backend/app/api/v1/endpoints/users.py
"""Endpoints utilisateurs"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.security import get_current_user, get_db
from app.models import User, UserProfile

router = APIRouter()

class UserUpdateRequest(BaseModel):
    first_name: str = None
    last_name: str = None
    bio: str = None
    avatar_url: str = None

@router.get("/me")
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Obtenir les infos de l'utilisateur actuel"""
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "username": current_user.username,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "is_active": current_user.is_active,
        "is_verified": current_user.is_verified,
        "created_at": current_user.created_at.isoformat()
    }

@router.put("/me")
async def update_current_user(
    request: UserUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mettre à jour le profil utilisateur"""
    if request.first_name:
        current_user.first_name = request.first_name
    if request.last_name:
        current_user.last_name = request.last_name
    if request.bio:
        current_user.bio = request.bio
    if request.avatar_url:
        current_user.avatar_url = request.avatar_url
    
    db.commit()
    db.refresh(current_user)
    
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "username": current_user.username,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "bio": current_user.bio,
        "avatar_url": current_user.avatar_url
    }

# recommendations.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from app.core.security import get_current_user, get_db
from app.models import User, Recommendation

router_rec = APIRouter()

@router_rec.get("/")
async def get_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = 10
):
    """Obtenir les recommandations pour l'utilisateur"""
    recommendations = db.query(Recommendation).filter(
        Recommendation.user_id == current_user.id,
        Recommendation.deleted_at == None
    ).order_by(Recommendation.score.desc()).limit(limit).all()
    
    return [
        {
            "id": str(r.id),
            "item_id": r.item_id,
            "item_type": r.item_type,
            "item_title": r.item_title,
            "score": r.score,
            "confidence": r.confidence,
            "reason": r.reason,
            "algorithm": r.algorithm
        }
        for r in recommendations
    ]

# predictions.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.security import get_current_user, get_db
from app.models import User, Prediction

router_pred = APIRouter()

class PredictionRequest(BaseModel):
    model_name: str
    input_data: dict

@router_pred.post("/")
async def create_prediction(
    request: PredictionRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Créer une prédiction"""
    prediction = Prediction(
        user_id=current_user.id,
        model_name=request.model_name,
        input_data=request.input_data,
        prediction={"placeholder": "prediction_result"},
        confidence=0.85
    )
    
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    
    return {
        "id": str(prediction.id),
        "model_name": prediction.model_name,
        "prediction": prediction.prediction,
        "confidence": prediction.confidence,
        "created_at": prediction.created_at.isoformat()
    }

# images.py
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from app.core.security import get_current_user, get_db
from app.models import User, ImageClassification

router_img = APIRouter()

@router_img.post("/classify")
async def classify_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Classifier une image"""
    # Sauvegarder le fichier
    contents = await file.read()
    
    # Créer la classification
    classification = ImageClassification(
        user_id=current_user.id,
        image_url=f"uploads/{file.filename}",
        model_name="resnet50",
        classifications=[
            {"label": "cat", "confidence": 0.95},
            {"label": "animal", "confidence": 0.92}
        ]
    )
    
    db.add(classification)
    db.commit()
    db.refresh(classification)
    
    return {
        "id": str(classification.id),
        "image_url": classification.image_url,
        "classifications": classification.classifications,
        "created_at": classification.created_at.isoformat()
    }

# analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user, get_db
from app.models import User, Conversation, Message, Recommendation, Prediction

router_ana = APIRouter()

@router_ana.get("/dashboard")
async def get_analytics_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtenir le dashboard d'analytics"""
    
    # Compter les conversations
    conversations_count = db.query(Conversation).filter(
        Conversation.user_id == current_user.id,
        Conversation.deleted_at == None
    ).count()
    
    # Compter les messages
    messages_count = db.query(Message).join(Conversation).filter(
        Conversation.user_id == current_user.id
    ).count()
    
    # Compter les recommandations
    recommendations_count = db.query(Recommendation).filter(
        Recommendation.user_id == current_user.id,
        Recommendation.deleted_at == None
    ).count()
    
    # Compter les prédictions
    predictions_count = db.query(Prediction).filter(
        Prediction.user_id == current_user.id
    ).count()
    
    return {
        "conversations": conversations_count,
        "messages": messages_count,
        "recommendations": recommendations_count,
        "predictions": predictions_count,
        "total_interactions": conversations_count + messages_count + recommendations_count + predictions_count
    }
