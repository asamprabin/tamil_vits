from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import soundfile as sf

# Path to your model or Hugging Face ID
model_path = "./outputs/tamil_vits-June-08-2025_11+16AM-0000000"  # Or "samprabin/tamil_vits" if hosted on Hugging Face
config_path = f"{model_path}/config.json"
vocoder_path = None

# Load the synthesizer
synthesizer = Synthesizer(
    tts_checkpoint=f"{model_path}/best_model.pth",
    tts_config_path=config_path,
    vocoder_checkpoint=vocoder_path,
    use_cuda=True  # Set to True if you have GPU
)

# Input text
text = "வணக்கம்! இது உங்கள் தனிப்பயன் தமிழ் TTS மாடல்."

# Run inference
wav = synthesizer.tts(text)

# Save as WAV file
sf.write("output.wav", wav, synthesizer.output_sample_rate)
print("✅ Audio saved as output.wav")
