# backend/app/api/v1/endpoints/recommendations.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.security import get_current_user, get_db
from app.models import User, Recommendation

router = APIRouter()

@router.get("/")
async def get_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = 10
):
    """Obtenir les recommandations"""
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
