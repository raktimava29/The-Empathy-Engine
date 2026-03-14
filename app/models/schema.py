from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str


class SpeechResponse(BaseModel):
    emotion: str
    audio_file: str