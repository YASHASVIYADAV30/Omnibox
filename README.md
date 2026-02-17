<div align="center">

# 📦 OmniBox

### *One Tool, Infinite Possibilities*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

**Your Personal AI-Powered Assistant with Voice Support**

*Control your computer, search the web, play music, get information - all with simple commands or your voice!*

[📥 Download](#-quick-start) • [📖 Features](#-features) • [🎯 Examples](#-usage-examples) • [🐛 Report Bug](https://github.com/YASHASVIYADAV30/Omnibox/issues)

</div>

---

## 🌟 Why OmniBox?

OmniBox is your **intelligent companion** that understands natural language, speaks multiple languages, and makes your daily tasks effortless.

### ✨ What Makes It Special?

| Feature | Description |
|---------|-------------|
| 🎙️ **Natural Voice Commands** | Speak in Hindi or English, naturally |
| 🧠 **AI-Powered** | Uses Google Gemini for intelligent responses |
| 🔧 **Smart & Forgiving** | Understands typos and multiple phrasings |
| 🚀 **Zero Configuration** | Works out of the box (just add API keys) |
| 🎨 **Beautiful CLI** | Colorful, interactive terminal interface |
| 🔒 **Privacy First** | All processing happens locally |

---

## 🎯 Features

<table>
<tr>
<td width="50%">

### 🌐 Web & Search
- Open any website instantly
- Search Google, YouTube, GitHub
- Play videos and music online
- Smart URL handling

### 🎵 Media & Entertainment
- Play music by mood (Lofi, Bollywood, etc.)
- YouTube integration
- Spotify support
- Voice-controlled playback

</td>
<td width="50%">

### ⚙️ System Control
- Open apps & folders
- Take screenshots
- System power controls
- Task management

### 🌦️ Information Hub
- Real-time weather updates
- Latest news headlines
- Time & date queries
- AI-powered Q&A

</td>
</tr>
</table>

---

## 📥 Quick Start

### 🖥️ Method 1: Download ZIP (Easiest)

[![Download ZIP](https://img.shields.io/badge/📥_Download-ZIP_File-blue?style=for-the-badge)](https://github.com/YASHASVIYADAV30/Omnibox/archive/refs/heads/main.zip)

1. Click the **Download** button above
2. Extract the ZIP file to any folder
3. Follow [Setup Instructions](#-setup) below

---

### 💻 Method 2: Clone with Git

```bash
git clone https://github.com/YASHASVIYADAV30/Omnibox.git
cd Omnibox
⚙️ Setup
📋 Prerequisites
Before you begin, make sure you have:

Python 3.8+ - Download here
Windows OS (for full voice features)
Microphone (optional, for voice commands)
Internet connection (for API features)
🔧 Installation Steps
Step 1: Install Dependencies
Open terminal/command prompt in the project folder:

Bash

pip install -r requirements.txt
💡 Tip: If you get "pip not found" error, try: python -m pip install -r requirements.txt

Step 2: Get API Keys (Free!)
You need 3 free API keys:

Service	Purpose	Get Free Key
🤖 Gemini AI	Intelligent responses	Get Key →
🌦️ OpenWeather	Weather updates	Get Key →
📰 NewsAPI	News headlines	Get Key →
All are 100% FREE for personal use!

Step 3: Configure API Keys
Create a file named .env in the project folder and add:

env

GEMINI_KEY=your_gemini_key_here
WEATHER_KEY=your_weather_key_here
NEWS_KEY=your_news_key_here
Example:

env

GEMINI_KEY=AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXX
WEATHER_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
NEWS_KEY=1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7
Step 4: Run OmniBox! 🚀
Bash

python main.py
That's it! OmniBox is now running! ✨

💻 Usage
Text Mode (Default)
Bash

python main.py
Voice Mode
Bash

python main.py --voice
Get Help
Bash

python main.py --help
💡 Usage Examples
🎯 Basic Commands
Bash

# Websites
open youtube
open github
open whatsapp

# Search
search python tutorials
play lofi music on youtube

# System
screenshot
open downloads
open vscode

# Information
weather mumbai
news
time
date
🎙️ Voice Commands
Start voice mode:

text

voice on
Speak naturally:

"YouTube pe Arijit Singh chalao"
"What's the weather in Delhi?"
"Open WhatsApp"
"Play some chill music"
Stop voice mode:

text

voice off
📖 All Commands
<details> <summary><strong>🌐 Web & Search</strong> (Click to expand)</summary><br>
Bash

# Open Websites
youtube, google, github, linkedin, whatsapp, spotify

# Dynamic websites
open facebook
open amazon.in

# Search
search <query>                  # Google search
play <video> on youtube         # YouTube playback
</details><details> <summary><strong>🎵 Media & Music</strong></summary><br>
Bash

# Mood-based music
play music
play lofi
play bollywood
play study music
play instrumental

# Search songs
play <song name>
search song <song name>
</details><details> <summary><strong>💻 System</strong></summary><br>
Bash

# Applications
notepad, calculator, vscode, chrome
task manager

# Folders
downloads, documents, desktop

# Actions
screenshot
shutdown
restart
lock
</details><details> <summary><strong>🌦️ Information</strong></summary><br>
Bash

# Weather
weather
weather <city>

# News
news

# Time & Date
time
date
today
what day is it
</details><details> <summary><strong>🎙️ Voice Control</strong></summary><br>
Bash

voice on      # Start continuous listening
voice off     # Stop listening
voice         # Single voice command
</details><details> <summary><strong>⚡ General</strong></summary><br>
Bash

help          # Show commands
clear         # Clear screen
exit          # Quit OmniBox
</details>
🛠️ Tech Stack
<div align="center">
Category	Technology
Language	Python
AI	Gemini
Speech	pyttsx3, SpeechRecognition
APIs	OpenWeatherMap, NewsAPI
UI	Colorama
</div>
📁 Project Structure
text

OmniBox/
├── 📁 apis/              # API integrations
│   ├── gemini.py         # AI responses
│   ├── weather.py        # Weather data
│   └── news.py           # News headlines
├── 📁 commands/          # Command handlers
│   ├── browser.py        # Web commands
│   ├── music.py          # Music playback
│   └── system.py         # System controls
├── 📁 core/              # Core functionality
│   ├── assistant.py      # Main brain
│   └── speech.py         # Voice I/O
├── 📁 utils/             # Utilities
│   └── config.py         # Configuration
├── 📄 main.py            # Entry point
├── 📄 requirements.txt   # Dependencies
└── 📄 README.md          # Documentation
🔧 Troubleshooting
<details> <summary><strong>❓ No audio output / OmniBox not speaking</strong></summary><br>
Solution:

Check system volume is not muted
Reinstall speech libraries:
Bash

pip uninstall pyttsx3
pip install pyttsx3 pywin32
</details><details> <summary><strong>❓ Module not found error</strong></summary><br>
Solution:

Bash

pip install -r requirements.txt
Make sure you're in the project directory.

</details><details> <summary><strong>❓ Voice recognition not working</strong></summary><br>
Solution:

Check microphone permissions in Windows Settings
Test microphone: Settings → Privacy → Microphone
Reinstall:
Bash

pip install SpeechRecognition pyaudio
</details><details> <summary><strong>❓ API errors (429, 401, quota exceeded)</strong></summary><br>
Solution:

Check your .env file has correct API keys
Verify keys are still valid on respective websites
For Gemini quota errors, wait 60 seconds or get a new key
</details><details> <summary><strong>❓ Python not recognized</strong></summary><br>
Solution:

Download Python from python.org
During installation, check "Add Python to PATH"
Restart terminal/computer
</details>
🤝 Contributing
Contributions are welcome! Here's how you can help:

🐛 Report bugs - Open an issue
💡 Suggest features - Share your ideas
🔧 Submit fixes - Send a pull request
⭐ Star the repo - Show your support!
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Special thanks to:

Google Gemini - For powerful AI capabilities
OpenWeatherMap - For weather data
NewsAPI - For news headlines
Python community - For amazing libraries
👨‍💻 Author
<div align="center">
Yashasvi Yadav

GitHub
LinkedIn

Building solutions that make technology accessible to everyone 🚀

</div>
📊 Project Stats
<div align="center">
GitHub stars
GitHub forks
GitHub watchers

</div>
<div align="center">
⭐ If OmniBox made your life easier, give it a star!
Made with ❤️ by Yashasvi Yadav

© 2024 OmniBox. All rights reserved.

</div> ```