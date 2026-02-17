<div align="center">

# 📦 OmniBox

**One Tool, Infinite Possibilities**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

Your AI-powered personal assistant with voice support.

[Features](#-features) • [Setup](#-setup) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 🌟 What is OmniBox?

A smart CLI assistant that lets you control your computer, search the web, play music, and get information — using **text or voice commands** in **Hindi & English**.

## ✨ Features

- 🎙️ **Voice Commands** — Speak naturally in Hindi or English
- 🧠 **AI-Powered** — Google Gemini for intelligent responses
- 🌐 **Web Control** — Open websites, search Google/YouTube
- 🎵 **Music** — Play by mood (Lofi, Bollywood, Study, etc.)
- 💻 **System Control** — Open apps, screenshots, shutdown
- 🌦️ **Live Info** — Weather, news, time & date

---

## 📥 Setup

**1. Clone the repo**

git clone https://github.com/YASHASVIYADAV30/Omnibox.git
cd Omnibox

**2. Install dependencies**

pip install -r requirements.txt

**3. Add API Keys**

Create a `.env` file in the project root:

GEMINI_KEY=your_gemini_key
WEATHER_KEY=your_weather_key
NEWS_KEY=your_news_key

Get free keys from: [Gemini](https://aistudio.google.com/app/apikey) | [OpenWeather](https://openweathermap.org/api) | [NewsAPI](https://newsapi.org/)

**4. Run**

python main.py

---

## 💡 Usage

python main.py          # Text mode
python main.py --voice  # Voice mode

**Example commands:**

open youtube
search python tutorials
play lofi music
weather mumbai
screenshot
news
voice on

---

## 📁 Project Structure

OmniBox/
├── apis/          # API integrations (Gemini, Weather, News)
├── commands/      # Command handlers (browser, music, system)
├── core/          # Assistant brain & speech engine
├── utils/         # Config & utilities
├── main.py        # Entry point
└── .env           # API keys (create this)

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| AI | Google Gemini |
| Speech | pyttsx3, SpeechRecognition |
| APIs | OpenWeatherMap, NewsAPI |

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit PRs.

## 📜 License

[MIT License](LICENSE)

---

<div align="center">

Made with ❤️ by [Yashasvi Yadav](https://github.com/YASHASVIYADAV30)

⭐ Star this repo if you found it useful!

</div>
