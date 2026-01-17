"""
Module Chatbot NLP avec vraie IA (Hugging Face)
"""

import os
import logging
import requests
from typing import Dict, List
from datetime import datetime

logger = logging.getLogger(__name__)

class ChatbotEngine:
    """Moteur de chatbot avec IA réelle"""
    
    def __init__(self):
        """Initialiser le chatbot avec Hugging Face"""
        self.api_key = os.getenv("HUGGINGFACE_API_KEY", "")
        self.api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400m-distill"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        logger.info(f"Chatbot initialized with Hugging Face")
    
    def preprocess_text(self, text: str) -> Dict:
        """Prétraiter le texte"""
        return {
            "original": text.strip(),
            "token_count": len(text.split()),
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def query_huggingface(self, payload: str) -> str:
        """Appeler l'API Hugging Face"""
        if not self.api_key:
            return self.get_fallback_response(payload)
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={"inputs": payload},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get("generated_text", "Désolé, je n'ai pas compris.")
            elif response.status_code == 503:
                # Model loading, use fallback
                return self.get_fallback_response(payload)
            else:
                logger.error(f"Hugging Face API error: {response.status_code}")
                return self.get_fallback_response(payload)
                
        except Exception as e:
            logger.error(f"Error calling Hugging Face: {str(e)}")
            return self.get_fallback_response(payload)
    
    def get_fallback_response(self, text: str) -> str:
        """Réponse de fallback si pas de connexion"""
        text_lower = text.lower()
        
        salutations = ["bonjour", "hello", "hi", "salut", "coucou"]
        if any(greet in text_lower for greet in salutations):
            return "Bonjour! Je suis votre assistant IA. Comment puis-je vous aider aujourd'hui?"
        
        questions = ["comment", "pourquoi", "quoi", "qu'est-ce", "que"]
        if any(q in text_lower for q in questions):
            return "C'est une excellente question! Pouvez-vous me donner plus de détails pour que je puisse mieux vous aider?"
        
        if "merci" in text_lower:
            return "De rien! Je suis là pour vous aider. Y a-t-il autre chose?"
        
        if "au revoir" in text_lower or "bye" in text_lower:
            return "Au revoir! N'hésitez pas à revenir si vous avez d'autres questions. 👋"
        
        if "ton nom" in text_lower or "qui es-tu" in text_lower:
            return "Je suis un assistant IA alimenté par des modèles de langage avancés. Je peux discuter avec vous et répondre à vos questions!"
        
        if "météo" in text_lower or "temps" in text_lower:
            return "Je ne peux pas accéder à la météo en temps réel, mais je vous recommande de consulter un service météo pour obtenir cette information!"
        
        responses = [
            "Intéressant! Pouvez-vous m'en dire plus?",
            "Je vois. Comment puis-je vous aider davantage?",
            "Merci pour cette information. Y a-t-il autre chose?",
            "D'accord! Voulez-vous que je vous explique quelque chose de spécifique?",
            "Je comprends. N'hésitez pas si vous avez d'autres questions."
        ]
        
        import random
        return random.choice(responses)
    
    def classify_intent(self, text: str) -> Dict:
        """Classifier l'intention"""
        text_lower = text.lower()
        
        salutations = ["bonjour", "hello", "hi", "salut", "coucou"]
        if any(greet in text_lower for greet in salutations):
            return {"intent": "greeting", "confidence": 0.95}
        
        questions = ["comment", "pourquoi", "quoi", "qu'est-ce", "que"]
        if any(q in text_lower for q in questions):
            return {"intent": "question", "confidence": 0.85}
        
        if "merci" in text_lower:
            return {"intent": "gratitude", "confidence": 0.90}
        
        return {"intent": "general", "confidence": 0.60}
    
    async def chat(self, user_id: str, conversation_id: str, message: str, db_session) -> Dict:
        """Pipeline complet de chat avec vraie IA"""
        import time
        start_time = time.time()
        
        try:
            # Prétraitement
            preprocessed = self.preprocess_text(message)
            
            # Classification d'intention
            intent = self.classify_intent(message)
            
            # Génération de réponse via IA
            if self.api_key:
                response = self.query_huggingface(message)
            else:
                response = self.get_fallback_response(message)
            
            processing_time = int((time.time() - start_time) * 1000)
            
            logger.info(f"Chat processed for user {user_id} in {processing_time}ms")
            
            return {
                "response": response,
                "intent": intent,
                "context_used": 0,
                "processing_time_ms": processing_time
            }
        
        except Exception as e:
            logger.error(f"Chat error: {str(e)}")
            return {
                "response": "Désolé, une erreur s'est produite. Veuillez réessayer.",
                "intent": {"intent": "error", "confidence": 0},
                "context_used": 0,
                "processing_time_ms": 0
            }