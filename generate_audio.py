# generate_audio.py
from gtts import gTTS
import os

os.makedirs("audio", exist_ok=True)

def generate_audio():
    with open("story.txt", "r") as f:
        text = f.read()

    tts = gTTS(text)
    tts.save("audio/story.mp3")
    print("Audio saved to audio/story.mp3")

if __name__ == "__main__":
    generate_audio()
