import os
from huggingface_hub import InferenceClient
from app.config import settings
class EmotionService:

    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=os.getenv("HF_TOKEN"),
        )
        self.model = settings.MODEL_NAME

    def detect_emotion(self, text: str) -> str:

        result = self.client.text_classification(
            text,
            model=self.model
        )

        emotion = max(result, key=lambda x: x["score"])["label"]

        return emotion