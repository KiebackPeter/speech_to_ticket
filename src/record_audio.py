import sounddevice as sd
from scipy.io.wavfile import write

def record_audio_file(filename, duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(f"./src/{filename}", fs, audio)
    print("Done recording.")
