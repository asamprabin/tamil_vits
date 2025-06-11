from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from huggingface_hub import snapshot_download
import soundfile as sf
import os

# Replace this with your Hugging Face repo ID (e.g., "your-username/your-model-name")
repo_id = "samprabin/tamil_vits"

# Download the entire model repo from Hugging Face
model_path = snapshot_download(repo_id=repo_id)

# Construct paths (these may vary based on your model structure)
config_path = os.path.join(model_path, "config.json")
model_file_path = os.path.join(model_path, "best_model.pth")
vocoder_file_path = os.path.join(model_path, "vocoder.pth") if os.path.exists(os.path.join(model_path, "vocoder.pth")) else None
vocoder_config_path = os.path.join(model_path, "vocoder_config.json") if os.path.exists(os.path.join(model_path, "vocoder_config.json")) else None

# Initialize synthesizer
synthesizer = Synthesizer(
    tts_checkpoint=model_file_path,
    tts_config_path=config_path,
    vocoder_checkpoint=vocoder_file_path,
    vocoder_config=vocoder_config_path,
    use_cuda=True
)

# Input text
text = "வணக்கம்! இது என் தமிழ் உரை பேசும் மாதிரி."

# Synthesize
wav = synthesizer.tts(text)

# Save WAV to file
sf.write("output.wav", wav, synthesizer.tts_config.audio['sample_rate'])
print("Audio saved as output.wav")