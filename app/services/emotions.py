from transformers import pipeline
from app.config import settings

class EmotionService:

    _classifier = None

    @classmethod
    def get_model(cls):
        if cls._classifier is None:
            print("🔥 Loading emotion model...")
            cls._classifier = pipeline(
                "text-classification",
                model=settings.MODEL_NAME,
                return_all_scores=False
            )
        return cls._classifier

    def detect_emotion(self, text: str) -> str:
        classifier = self.get_model()
        result = classifier(text)[0]
        return result["label"]