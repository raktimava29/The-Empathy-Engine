from transformers import pipeline
from app.config import settings

class EmotionService:

    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model=settings.MODEL_NAME,
            return_all_scores=False
        )

    def detect_emotion(self, text: str) -> str:
        result = self.classifier(text)[0]
        emotion = result["label"]
        return emotion