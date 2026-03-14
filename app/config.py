import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MODEL_NAME = os.getenv(
        "EMOTION_MODEL",
        "j-hartmann/emotion-english-distilroberta-base"
    )

settings = Settings()