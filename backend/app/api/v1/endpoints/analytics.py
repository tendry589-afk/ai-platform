# backend/app/api/v1/endpoints/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user, get_db
from app.models import User, Conversation, Message, Recommendation, Prediction

router = APIRouter()

@router.get("/dashboard")
async def get_analytics_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtenir le dashboard d'analytics"""
    
    conversations_count = db.query(Conversation).filter(
        Conversation.user_id == current_user.id,
        Conversation.deleted_at == None
    ).count()
    
    messages_count = db.query(Message).join(Conversation).filter(
        Conversation.user_id == current_user.id
    ).count()
    
    recommendations_count = db.query(Recommendation).filter(
        Recommendation.user_id == current_user.id,
        Recommendation.deleted_at == None
    ).count()
    
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
