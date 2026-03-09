# Real-Time AI Hotel Voice Agent

This project implements a real-time AI voice agent that simulates a hotel receptionist capable of handling booking and customer queries through voice interaction.

The system processes user speech, converts it to text, generates an AI response using a language model, converts the response back to speech, and plays the audio response.

---

# System Architecture

User Speech
↓
Speech-to-Text (SpeechRecognition)
↓
LLM Response Generation (Ollama – Llama3)
↓
Text-to-Speech (pyttsx3)
↓
Audio Response to User

---

# Features

• Real-time speech recognition  
• AI-generated hotel receptionist responses  
• Text-to-speech voice output  
• Modular architecture  
• Latency measurement  
• Simulated real-time conversation  

---

# Technologies Used

Python  
Ollama (Llama3) – Local LLM  
SpeechRecognition – Speech-to-text  
pyttsx3 – Text-to-speech  
pyaudio – Microphone input  

---

# Project Structure
ai-call-agent
│
├── app
│ ├── main.py # Main pipeline
│ ├── stt.py # Speech-to-text module
│ ├── llm.py # LLM response generator
│ ├── tts.py # Text-to-speech module
│ └── audio.py # Audio input handling
│
├── README.md
└── .gitignore

---

# Installation

Clone the repository
git clone https://github.com/saniashaju/ai-call-agent.git

cd ai-call-agent


Create virtual environment

python -m venv venv
source venv/bin/activate

Install dependencies

pip install speechrecognition pyaudio pyttsx3 ollama

Install Ollama
curl -fsSL https://ollama.com/install.sh | sh


Download Llama3 model
ollama pull llama3


---

# Run the Project

python app/main.py


You will see:

Listening...
Speak now

.......................................................

Example interaction:

User:
"I want to book a room tomorrow"

Assistant:
"Sure, I can help with that. What type of room would you prefer?"

The response will also be played as **voice output**.

---

# Latency Measurement

The system measures latency between user speech input and AI response generation.

Typical latency observed:

1. Speech recognition: ~1s  
2. LLM response generation: ~1–2s  
3. Text-to-speech: ~0.5s  

Total latency: **~2–3 seconds**

---

# Future Improvements

• Streaming audio responses  
• Multi-user concurrency  
• WebSocket integration  
• Web interface for voice calls  

---

# Demo

The system demonstrates an AI hotel receptionist capable of answering booking queries using real-time voice interaction.



### Demo Video
See the uploaded demo video for the working prototype.

### Screenshots
Execution Screenshot



