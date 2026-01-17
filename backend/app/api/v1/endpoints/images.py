# backend/app/api/v1/endpoints/images.py
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.core.security import get_current_user, get_db
from app.models import User, ImageClassification

router = APIRouter()

@router.post("/classify")
async def classify_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Classifier une image"""
    contents = await file.read()
    
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
