
class VoiceMapper:

    emotion_voice_map = {
        "joy": {"rate": 180, "pitch": 150, "volume": 1.0},
        "sadness": {"rate": 120, "pitch": 90, "volume": 0.7},
        "anger": {"rate": 200, "pitch": 170, "volume": 1.0},
        "fear": {"rate": 140, "pitch": 110, "volume": 0.8},
        "surprise": {"rate": 190, "pitch": 160, "volume": 1.0},
        "neutral": {"rate": 150, "pitch": 120, "volume": 0.9},
    }

    @classmethod
    def map_emotion(cls, emotion: str):

        return cls.emotion_voice_map.get(
            emotion.lower(),
            cls.emotion_voice_map["neutral"]
        )