from app.services.emotions import EmotionService

service = EmotionService()

print(service.detect_emotion("I am very happy today"))
print(service.detect_emotion("This is extremely frustrating"))

# from app.services.voice_mapper import VoiceMapper

# print(VoiceMapper.map_emotion("joy"))
# print(VoiceMapper.map_emotion("sadness"))

# from app.services.tts import TTSService

# file = TTSService.generate_audio("Hello this is a test")

# print(file)