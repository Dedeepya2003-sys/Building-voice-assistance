# Building-voice-assistance
# 🗣️ Voice Assistant

A Python-based voice assistant capable of recognizing voice commands, processing natural language, and performing various tasks like searching the web, telling the time, opening applications, and more.

## 🚀 Features

- 🎤 Voice input using speech recognition
- 🧠 Natural language understanding
- 🔊 Text-to-speech feedback
- 🌐 Internet-based tasks (e.g., Wikipedia search, weather updates)
- 📁 Local system commands (e.g., open files, apps)
- 🕒 Tells time and date
- 💡 Extensible architecture for adding new commands

## 🛠️ Technologies Used

- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/) (Text-to-Speech)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- (Optional) [OpenAI GPT](https://openai.com) for enhanced conversational capabilities

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
2.Install dependencies
pip install -r requirements.txt
3. (optional) install pyaudio if issues occur
pip install pipwin
pipwin install pyaudio

## 🧪 Usage
1. Run the assistant:
   python main.py
2. Speak a command when prompted. Example commands:
- "What time is it?"
- "Search Wikipedia for Python"
- "Open Google Chrome"
- "Tell me a joke"

## 🧱 Project Structure
voice-assistant/
│
├── main.py               # Entry point for the assistant
├── speech/               # Speech recognition 
├── skills/               # Logic for commands and responses
├── config/               # Configuration and API keys
├── utils/                # Helper functions
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
