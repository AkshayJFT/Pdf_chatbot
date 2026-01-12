import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(
    filename="question.wav",
    duration=5,
    sample_rate=16000
):
    """
    Records microphone audio and saves to WAV file
    """
    print(f"\n🎤 Recording for {duration} seconds... Speak now.")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()
    write(filename, sample_rate, recording)

    print(f"✅ Audio saved to {filename}")
