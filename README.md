# Smart AC (Raspberry Pi + ESP + OpenCV + Voice + Groq LLM)

A Smart Air Conditioner system built using **Raspberry Pi** + **ESP (ESP32/ESP8266)** with **OpenCV (Python server)** for live video streaming and presence detection.  
It works like a **CCTV + Smart Automation AC**: when nobody is in the room, AC stops automatically; when someone is present, AC runs and maintains room temperature.  
It also supports **voice command control** (“start”, “stop”) and a **Groq LLM assistant** that translates any language to English, gets an answer, and returns it back to the user.

> Status: ✅ Running smoothly (real hardware tested)

---

## ✨ Features

### ✅ Smart Automation
- **Auto OFF** when no one is in the room (presence detection)
- **Auto ON** when someone enters the room
- Maintains target **room temperature** (automatic control)

### 🎥 CCTV / Security Mode
- **Live video streaming** like CCTV
- Camera installed inside/near the AC
- Video feed can be viewed on a PC on the same network

### 🎙️ Voice Control
- Voice command file: `voice.py`
- Example: Owner says **"start"** → AC starts anyway
- Example: Owner says **"stop"** → AC stops

### 🔊 Speaker Support
- AC setup includes a speaker
- Can play responses / confirmations

### 🤖 LLM Assistant (Groq)
- User can ask questions in **any language**
- System translates to English → sends to **Groq LLM**
- Returns the answer (and can optionally translate back)

---

## 🧠 How It Works (Architecture)

**Camera → Raspberry Pi → OpenCV Python Server → PC Stream Viewer**  
**Presence Detection → ESP Relay/Control → AC Power Control**  
**Voice Input → voice.py → Override Control**  
**User Question → Translate → Groq LLM → Answer → Speaker/Terminal**

---

## 🧩 Hardware Requirements

- Raspberry Pi (3/4 recommended)
- ESP32 or ESP8266
- Camera module / USB camera (installed in/near AC)
- Relay module (AC control) / Smart IR blaster (optional)
- Temperature sensor (DHT11/DHT22/DS18B20 or similar)
- Speaker (USB / AUX / Bluetooth based on setup)
- PC/Laptop for monitoring the CCTV stream

---

## 🧰 Software Requirements

- Python 3.9+
- OpenCV
- Flask / FastAPI (any one used for streaming server)
- SpeechRecognition / Vosk / any STT library
- Translation library (Googletrans / Deep Translator / etc.)
- Groq API client
- ESP firmware (Arduino / PlatformIO)

---

## Clone the repository

git clone https://github.com/your-username/smart-ac.git
cd smart-ac/server
---
## Create venv & install packages

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---
## Live Stream Usage (PC)

http://<RPI_IP>:5000/video

---

### Voice Commands

python voice.py
---

