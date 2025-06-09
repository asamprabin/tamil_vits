# 🗣️ Tamil Text-to-Speech (TTS) using VITS

This repository provides a complete step-by-step guide to training your own speech synthesizer using the **VITS (Variational Inference with Adversarial Learning for End-to-End Text-to-Speech)** model with a **custom Tamil dataset**, powered by [Coqui TTS](https://github.com/coqui-ai/TTS).

---

## 📂 Dataset Structure

```
dataset/
├── wavs/                  # Audio files (.wav)
├── metadata.csv           # Training metadata
└── metadata_val.csv       # Validation metadata
```

---

## 🛠️ Setup Instructions

### 1. Clone Coqui TTS

```bash
git clone https://github.com/coqui-ai/TTS.git
```

---

### 2. Configure `config.json`

Update your `config.json` with the dataset path:

```json
"datasets": [
  {
    "name": "speaker_data",
    "path": "datasets",
    "meta_file_train": "metadata.csv",
    "meta_file_val": "metadata_val.csv",
    "formatter": "ljspeech"
  }
]
```

---

### 3. Metadata Format

Each line in `metadata.csv` and `metadata_val.csv` must follow this format:

```
<file_name>|<speaker_name>|<text>
Example: 001|linda|Hi, How are you.
```

---

### 4. Train/Test Split

Automatically split your metadata into 90% training and 10% validation from metadata.csv:

```bash
python split_meta.py
```

---

### 5. Validate Audio Sample Rate

VITS requires audio sampled at **22050 Hz**. Check your files using:

```bash
python validate_audio.py
```

---

### 6. Convert Audio to 22050 Hz

Use the provided script (Linux only):

```bash
bash convert_audio_sample_rate.sh
```

> 💡 For Windows or macOS versions, consult [ChatGPT](https://chat.openai.com) or adapt the script accordingly.

---

### 7. Find Unique Characters in Dataset

To extract all unique Tamil characters used in your dataset:

```bash
python TTS/TTS/bin/find_unique_chars.py --config_path config.json
```

---

### 8. Update Character Set in `config.json`

Add the characters to the `characters` section:

```json
"characters": {
  "characters_class": "TTS.tts.models.vits.VitsCharacters",
  "pad": "_",
  "eos": "~",
  "bos": "^",
  "characters": "ஂஃஅஆஇஈஉஊஎஏஐஒஓஔகஙசஜஞடணதநனபமயரறலளழவஷஸஹாிீுூெேைொோௌ்",
  "punctuations": ".,!?; "
}
```

---

## 🚀 Training

Start training your model with:

```bash
python TTS/TTS/bin/train_tts.py --config_path config.json
```

---

## 🔊 Inference

Install the TTS CLI:

```bash
pip install TTS
```

Generate speech from text:

```bash
tts \
  --text "காதல் என்ற ஒன்று போதும். காலமெல்லாம் துணையாய் வாழ்வதற்கு" \
  --model_path ./outputs/tamil_vits-June-08-2025_11+16AM-0000000/best_model.pth \
  --config_path ./outputs/tamil_vits-June-08-2025_11+16AM-0000000/config.json \
  --out_path output.wav
```

---

## 💡 Tips

- ✅ **Python version**: 3.10 recommended
- ✅ **Learning Rate Scheduler**: `ExponentialLR` — gradually decreases the learning rate after each epoch or step.

---

## 🙏 Acknowledgements

- [Coqui TTS](https://github.com/coqui-ai/TTS) — Original VITS implementation
- Tamil open-source community for promoting regional language AI
