from transformers import pipeline
from app.config import settings
import torch

class EmotionService:

    _classifier = None

    @classmethod
    def get_model(cls):
        if cls._classifier is None:
            print("🔥 Loading emotion model...")
            cls._classifier = pipeline(
                "text-classification",
                model=settings.MODEL_NAME,
                device=-1 
            )
        return cls._classifier

    def detect_emotion(self, text: str) -> str:
        model = self.get_model()

        with torch.no_grad(): 
            result = model(text)[0]

        return result["label"]