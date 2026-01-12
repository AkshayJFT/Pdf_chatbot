# audio_player.py
import subprocess

def play_audio(file_path):
    subprocess.run(["mpg123", file_path])
