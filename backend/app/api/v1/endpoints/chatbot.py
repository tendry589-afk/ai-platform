from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional
import logging
import uuid

from app.ai.nlp.chatbot import ChatbotEngine

logger = logging.getLogger(__name__)
router = APIRouter()
chatbot_engine = ChatbotEngine()

class MessageCreate(BaseModel):
    content: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    intent: dict
    context_used: int
    processing_time_ms: int

@router.post("/chat", response_model=ChatResponse)
async def chat(request: MessageCreate):
    """Envoyer un message au chatbot (sans auth)"""
    try:
        result = await chatbot_engine.chat(
            user_id="anonymous",
            conversation_id=request.conversation_id or str(uuid.uuid4()),
            message=request.content,
            db_session=None
        )
        
        return {
            "response": result["response"],
            "intent": result["intent"],
            "context_used": result["context_used"],
            "processing_time_ms": result["processing_time_ms"]
        }
    
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing chat message"
        )