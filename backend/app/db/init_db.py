"""
Script d'initialisation de la base de données SQLite
"""
from app.db.session import engine, Base
from app.models import User, UserProfile, Conversation, Message, Recommendation, Prediction, ImageClassification

def init_db():
    """Créer toutes les tables"""
    print("Création des tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès!")

if __name__ == "__main__":
    init_db()