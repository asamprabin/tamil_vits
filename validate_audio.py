import os
import wave

folder = "datasets/tamil_speaker/wavs"

for filename in os.listdir(folder):
    if filename.endswith(".wav"):
        path = os.path.join(folder, filename)
        with wave.open(path, "rb") as wav_file:
            channels = wav_file.getnchannels()
            framerate = wav_file.getframerate()
            print(f"{filename}: {framerate} Hz, {channels} channel(s)")
