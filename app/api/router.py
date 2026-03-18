from fastapi import APIRouter, Request
import os

from app.models.schema import TextRequest
from app.services.emotions import EmotionService
from app.services.voice_mapper import VoiceMapper
from app.services.tts import TTSService

router = APIRouter()

emotion_service = EmotionService()
tts_service = TTSService()

@router.post("/speak")
async def generate_speech(data: TextRequest, request: Request):

    text = data.text

    emotion = emotion_service.detect_emotion(text)

    voice_params = VoiceMapper.map_emotion(emotion)

    audio_file = await tts_service.generate_audio(text, voice_params)
    
    filename = os.path.basename(audio_file)
    
    audio_url = f"{request.base_url}audio/{filename}"

    return {
        "emotion": emotion,
        "audio_url": audio_url
    }