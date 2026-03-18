from fastapi import APIRouter
from app.models.schema import TextRequest, SpeechResponse
from app.services.emotions import EmotionService
from app.services.voice_mapper import VoiceMapper
from app.services.tts import TTSService

router = APIRouter()

emotion_service = EmotionService()
tts_service = TTSService()


@router.post("/speak", response_model=SpeechResponse)
async def generate_speech(data: TextRequest):

    text = data.text

    emotion = emotion_service.detect_emotion(text)

    voice_params = VoiceMapper.map_emotion(emotion)

    audio_file = await tts_service.generate_audio(text, voice_params)

    return SpeechResponse(
        emotion=emotion,
        audio_file=audio_file
    )