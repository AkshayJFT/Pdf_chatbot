from openai import OpenAI
import os
import tempfile
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def text_to_speech(text, voice="coral"):
    """
    Convert narration text to speech using GPT-4o-mini TTS
    Returns path to audio file
    """
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_path = Path(tmp_file.name)
    tmp_file.close()

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text,
    ) as response:
        response.stream_to_file(tmp_path)

    return str(tmp_path)


def speech_to_text(audio_file_path):
    """
    Convert user audio (question) to text using GPT-4o transcription
    """
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file
        )

    return transcription.text
