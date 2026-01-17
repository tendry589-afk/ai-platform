from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    APP_NAME: str = "AI Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # SQLite au lieu de PostgreSQL (fichier local)
    DATABASE_URL: str = "sqlite:///./ai_platform.db"
    
    MONGODB_URL: str = "mongodb://localhost:27017/ai_platform"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    SECRET_KEY: str = "ai-platform-secret-key-for-dev"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    HUGGINGFACE_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    MODEL_CACHE_DIR: str = "/models"
    
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET: str = ""
    AWS_REGION: str = "us-east-1"
    
    SENTRY_DSN: str = ""
    LOG_LEVEL: str = "INFO"
    
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()