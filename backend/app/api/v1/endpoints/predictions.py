# backend/app/api/v1/endpoints/predictions.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.security import get_current_user, get_db
from app.models import User, Prediction

router = APIRouter()

class PredictionRequest(BaseModel):
    model_name: str
    input_data: dict

@router.post("/")
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
        prediction={"result": "prediction_placeholder"},
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
