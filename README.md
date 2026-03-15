# 📄 Empathy Engine — Emotion-Aware Text-to-Speech System

**FastAPI • HuggingFace Transformers • Edge Neural TTS • Emotion Detection • Speech Synthesis**

Empathy Engine is an AI-powered text-to-speech service that detects the **emotional tone of input text** and generates **expressive speech audio** accordingly.

The system analyzes user text using a **transformer-based emotion detection model**, maps detected emotions to **voice parameters such as speech rate and intensity**, and generates **emotion-aware speech output** using neural text-to-speech.

Unlike traditional monotone TTS systems, Empathy Engine adapts the speech characteristics to better reflect the emotional intent of the message.

---

# 🚀 Features

- 🧠 **Emotion Detection** using HuggingFace transformer models  
- 🎤 **Emotion-aware speech synthesis**  
- ⚡ **FastAPI REST API service**  
- 🔊 **Neural text-to-speech using Edge TTS**  
- 🎚 **Voice modulation based on emotion** (speed and tone adjustments)  
- 📁 **Automatic audio file generation**  
- 🧩 **Modular production-style architecture**

---

# 🏗 System Architecture

1. **Text Input**
2. **Emotion Detection (Transformer Model)**
3. **Emotion → Voice Parameter Mapping**
4. **Speech Generation (Neural TTS)**
5. **Audio File Output**

---

# 🛠 Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI / NLP
- HuggingFace Transformers
- DistilRoBERTa Emotion Model

## Speech Synthesis
- Edge Neural TTS

## Data Validation
- Pydantic

---

# 📂 Project Structure

```bash
empathy-engine/
│
├── app/
│ │
│ ├── main.py               # FastAPI application entry point
│ ├── config.py             # Environment configuration
│ ├── test.py               # Testing the services
│ ├── api/
│ │ └── router.py           # API endpoints
│ │
│ ├── models/
│ │ └── schema.py           # Request/response models
│ │
│ ├── services/
│ │ ├── emotions.py         # Emotion detection logic
│ │ ├── voice_mapper.py     # Emotion → voice parameter mapping
│ │ └── tts.py              # Speech generation
│
├── generated_audio/        # Output audio files
├── requirements.txt
└── README.md
```

---

# ⚙️ How It Works

## 1️⃣ Text Input

Users send text through the `/speak` API endpoint.

Example:

"I can't believe this happened, I'm really upset."

## 2️⃣ Emotion Detection

The text is processed using a **HuggingFace transformer model** trained for emotion classification.

Model used: 

**j-hartmann/emotion-english-distilroberta-base**

The model predicts emotions such as:

- joy
- sadness
- anger
- fear
- surprise
- neutral

## 3️⃣ Emotion → Voice Mapping

Detected emotions are mapped to speech parameters.

Example mapping:

| Emotion | Speech Behavior |
|------|------|
| Joy | Faster and energetic |
| Sadness | Slower and softer |
| Anger | Louder and intense |
| Neutral | Normal speech |


## 4️⃣ Speech Generation

The processed text and voice parameters are sent to the **Edge Neural TTS engine**, which generates expressive speech.

Output format: .mp3 audio file

Generated files are saved in: generated_audio/

---

# 🔌 API Endpoints

## 1. Health Check

### Endpoint
`GET /`


### Response

```json
{
  "message": "Empathy Engine API running"
}
```

## 2. Generate Speech

### Endpoint
`POST /speak`

### Description
Converts input text into emotion-aware speech audio.

### Request 
```json
{
  "text": "I am really happy today!"
}
```

### Response
```json
{
  "emotion": "joy",
  "audio_file": "generated_audio/abc123.mp3"
}
```
---
## 🖥 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/empathy-engine.git
cd The-Empathy-Engine-main
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

#### Activate Environment
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server

Start the FastAPI server:

```bash
uvicorn server:app --reload
```
Once the server is running, the API documentation will be available at:

http://127.0.0.1:8000/docs

---
