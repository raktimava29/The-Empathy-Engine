import edge_tts
import uuid
import os
import asyncio

OUTPUT_DIR = "generated_audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class TTSService:

    async def generate_audio(self, text: str, voice_params: dict):

        rate = voice_params["rate"]

        # Map rate to speech speed
        if rate > 170:
            rate_mod = "+20%"
        elif rate < 130:
            rate_mod = "-20%"
        else:
            rate_mod = "0%"

        file_id = str(uuid.uuid4())
        filepath = os.path.join(OUTPUT_DIR, f"{file_id}.mp3")

        communicate = edge_tts.Communicate(
            text,
            voice="en-US-JennyNeural",
            rate=rate_mod
        )

        await communicate.save(filepath)

        return filepath