"""
OmniBox - Core Assistant Module

The brain of OmniBox. Handles command parsing, 
natural language understanding, and response generation.
"""

import re
import random
import webbrowser
from datetime import datetime
from typing import Optional

# API imports
from apis.gemini import ask_gemini
from apis.weather import get_weather
from apis.news import get_news

# System commands
from commands.system import (
    open_notepad, open_calculator, open_chrome, open_vscode,
    open_downloads, open_documents, open_desktop,
    shutdown_pc, restart_pc, lock_screen,
    take_screenshot, open_task_manager
)

# Browser commands
from commands.browser import (
    open_youtube, open_google, open_gmail, open_whatsapp,
    open_github, open_chatgpt, open_linkedin,
    open_stackoverflow, search_google, search_youtube,
    search_github, open_study_tabs
)

# Music commands
from commands.music import (
    play_music, play_spotify, play_youtube_music,
    play_lofi, play_study_music, play_bollywood,
    play_instrumental, search_song, play_spotify_search
)

# Speech
from core.speech import speak


class OmniBox:
    """Main assistant class that processes commands and generates responses."""
    
    def __init__(self, config=None):
        """Initialize OmniBox with optional configuration."""
        self.config = config
        self.user_name = ""
        self._setup_patterns()
        self._setup_responses()
    
    
    # ──────────────────────────────────────────────────────
    # SETUP METHODS
    # ──────────────────────────────────────────────────────
    
    def _setup_responses(self):
        """Setup all response templates."""
        
        # Time-based greetings (Professional)
        self.greetings = {
            "morning": [
                "Good morning! How can I assist you today?",
                "Good morning! Ready to help you.",
                "Good morning! What would you like me to do?",
            ],
            "afternoon": [
                "Good afternoon! How can I help you?",
                "Good afternoon! What can I do for you?",
                "Hello! How may I assist you?",
            ],
            "evening": [
                "Good evening! How can I assist you?",
                "Good evening! What would you like me to do?",
                "Hello! How can I help you tonight?",
            ],
            "night": [
                "Hello! How can I help you?",
                "Good evening! What can I do for you?",
                "Hello! Ready to assist you.",
            ]
        }
        
        # Action responses
        self.responses = {
            "opening": [
                "Opening {item} for you.",
                "Sure, opening {item}.",
                "Opening {item}.",
            ],
            "playing": [
                "Playing {item} for you.",
                "Sure, playing {item}.",
                "Now playing {item}.",
            ],
            "searching": [
                "Searching for {item}.",
                "Looking up {item}.",
                "Let me search {item} for you.",
            ],
        }
        
        # Casual conversation responses
        self.casual = {
            "how are you": [
                "I'm doing great, thank you for asking! How can I help you?",
                "I'm good! What can I do for you?",
                "All good here! How may I assist you?",
            ],
            "thank": [
                "You're welcome!",
                "Happy to help!",
                "Anytime!",
                "Glad I could help!",
            ],
            "hello": [
                "Hello! How can I help you?",
                "Hi there! What can I do for you?",
                "Hello! What would you like me to do?",
            ],
            "hi": [
                "Hello! How can I assist you?",
                "Hi! What can I do for you?",
                "Hey! How may I help?",
            ],
            "good morning": [
                "Good morning! How can I help you today?",
                "Good morning! What can I do for you?",
            ],
            "good afternoon": [
                "Good afternoon! How may I assist you?",
                "Good afternoon! What can I do for you?",
            ],
            "good evening": [
                "Good evening! How can I help you?",
                "Good evening! What can I do for you?",
            ],
            "good night": [
                "Good night! Take care!",
                "Good night! Have a good rest!",
            ],
            "who are you": [
                "I'm OmniBox, your personal AI assistant. I can open apps, play music, search the web, check weather, and much more!",
            ],
            "what can you do": [
                "I can open applications, search Google and YouTube, play music, tell you the weather and news, take screenshots, and have conversations with you. Type 'help' to see all commands.",
            ],
            "can you speak": [
                "Yes, I can speak! If you can't hear me, please check your volume settings.",
            ],
            "why are you not speaking": [
                "I am speaking! Please make sure your speakers are on and volume is up.",
            ],
            "bol kyon nahi": [
                "I am speaking! Please check your volume settings.",
            ],
            "nahi bol rahi": [
                "I am speaking! Please check if your speakers are working.",
            ],
        }
        
        # Common typo corrections
        self.typos = {
            "yoytube": "youtube",
            "youtub": "youtube",
            "youutube": "youtube",
            "utube": "youtube",
            "linkdin": "linkedin",
            "linkedn": "linkedin",
            "linkendin": "linkedin",
            "githab": "github",
            "gitub": "github",
            "guthub": "github",
            "whatsap": "whatsapp",
            "watsapp": "whatsapp",
            "whatapp": "whatsapp",
            "googl": "google",
            "gogle": "google",
            "goolge": "google",
            "spotyfy": "spotify",
            "spotfy": "spotify",
            "calender": "calendar",
            "calculater": "calculator",
            "notepadd": "notepad",
        }
    
    def _setup_patterns(self):
        """Setup command patterns and mappings."""
        
        # Website mappings
        self.websites = {
            "youtube": (open_youtube, "YouTube"),
            "google": (open_google, "Google"),
            "gmail": (open_gmail, "Gmail"),
            "whatsapp": (open_whatsapp, "WhatsApp"),
            "github": (open_github, "GitHub"),
            "chatgpt": (open_chatgpt, "ChatGPT"),
            "linkedin": (open_linkedin, "LinkedIn"),
            "stackoverflow": (open_stackoverflow, "Stack Overflow"),
            "stack overflow": (open_stackoverflow, "Stack Overflow"),
            "spotify": (play_spotify, "Spotify"),
        }
        
        # App mappings
        self.apps = {
            "notepad": (open_notepad, "Notepad"),
            "calculator": (open_calculator, "Calculator"),
            "calc": (open_calculator, "Calculator"),
            "chrome": (open_chrome, "Chrome"),
            "vscode": (open_vscode, "VS Code"),
            "vs code": (open_vscode, "VS Code"),
            "visual studio code": (open_vscode, "VS Code"),
            "task manager": (open_task_manager, "Task Manager"),
        }
        
        # Folder mappings
        self.folders = {
            "downloads": (open_downloads, "Downloads"),
            "download": (open_downloads, "Downloads"),
            "documents": (open_documents, "Documents"),
            "document": (open_documents, "Documents"),
            "desktop": (open_desktop, "Desktop"),
        }
        
        # Music mood mappings
        self.music_moods = {
            "lofi": (play_lofi, "lofi music"),
            "lo-fi": (play_lofi, "lofi music"),
            "chill": (play_lofi, "chill music"),
            "study music": (play_study_music, "study music"),
            "focus music": (play_study_music, "focus music"),
            "bollywood": (play_bollywood, "Bollywood music"),
            "hindi songs": (play_bollywood, "Hindi songs"),
            "hindi music": (play_bollywood, "Hindi music"),
            "instrumental": (play_instrumental, "instrumental music"),
            "piano": (play_instrumental, "piano music"),
        }
    
    
    # ──────────────────────────────────────────────────────
    # HELPER METHODS
    # ──────────────────────────────────────────────────────
    
    def _fix_typos(self, text: str) -> str:
        """Auto-correct common typos in user input."""
        words = text.lower().split()
        corrected = []
        for word in words:
            clean = word.strip('.,!?')
            fixed = self.typos.get(clean, clean)
            corrected.append(fixed)
        return ' '.join(corrected)
    
    def _get_response(self, category: str, item: str = "") -> str:
        """Get a random response from the given category."""
        if category in self.responses:
            template = random.choice(self.responses[category])
            return template.format(item=item)
        return ""
    
    def greet(self) -> str:
        """Generate a time-appropriate greeting."""
        hour = datetime.now().hour
        
        if 5 <= hour < 12:
            period = "morning"
        elif 12 <= hour < 17:
            period = "afternoon"
        elif 17 <= hour < 21:
            period = "evening"
        else:
            period = "night"
        
        return random.choice(self.greetings[period])
    
    def speak(self, text: str) -> None:
        """Speak the given text using TTS."""
        speak(text)
    
    
    # ──────────────────────────────────────────────────────
    # MAIN COMMAND PROCESSOR
    # ──────────────────────────────────────────────────────
    
    def process_command(self, text: str) -> str:
        """
        Process user input and return appropriate response.
        
        Args:
            text: User's input text
            
        Returns:
            Response string
        """
        if not text:
            return ""
        
        # Fix typos first
        text = self._fix_typos(text)
        t = text.lower().strip()
        
        # Check casual conversation first
        casual_response = self._handle_casual(t)
        if casual_response:
            return casual_response
        
        # Try each handler in order of priority
        handlers = [
            self._handle_system,
            self._handle_screenshot,
            self._handle_youtube,
            self._handle_search,
            self._handle_website,
            self._handle_app,
            self._handle_folder,
            self._handle_music,
            self._handle_weather,
            self._handle_news,
            self._handle_time_date,
            self._handle_dynamic_website,
            self._handle_ai,
        ]
        
        for handler in handlers:
            result = handler(t, text)
            if result:
                return result
        
        return "Sorry, I didn't understand that. Type 'help' to see available commands."
    
    
    # ──────────────────────────────────────────────────────
    # CASUAL CONVERSATION
    # ──────────────────────────────────────────────────────
    
    def _handle_casual(self, t: str) -> Optional[str]:
        """Handle casual conversation and greetings."""
        
        for trigger, responses in self.casual.items():
            if trigger in t:
                return random.choice(responses)
        
        # Handle name introduction
        name_match = re.search(r"(?:my name is|call me|i am|i'm)\s+(\w+)", t)
        if name_match:
            self.user_name = name_match.group(1).title()
            return f"Nice to meet you, {self.user_name}! How can I help you?"
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # SYSTEM COMMANDS
    # ──────────────────────────────────────────────────────
    
    def _handle_system(self, t: str, original: str) -> Optional[str]:
        """Handle system control commands like shutdown, restart, lock."""
        
        if any(x in t for x in ["shutdown", "shut down", "power off", "band karo"]):
            shutdown_pc()
            return "Shutting down the PC. Goodbye!"
        
        if any(x in t for x in ["restart", "reboot"]):
            restart_pc()
            return "Restarting the PC."
        
        if any(x in t for x in ["lock", "lock screen", "lock pc"]):
            lock_screen()
            return "Screen locked."
        
        return None
    
    def _handle_screenshot(self, t: str, original: str) -> Optional[str]:
        """Handle screenshot command."""
        
        if any(x in t for x in ["screenshot", "screen shot", "capture screen", "ss"]):
            take_screenshot()
            return "Screenshot captured and saved."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # YOUTUBE COMMANDS
    # ──────────────────────────────────────────────────────
    
    def _handle_youtube(self, t: str, original: str) -> Optional[str]:
        """Handle YouTube search and playback commands."""
        
        # Pattern: play/search <query> on youtube
        match = re.search(r"(play|search|find|open|watch|stream)\s+(.+?)\s+on\s+youtube", t)
        if match:
            query = match.group(2).strip()
            search_youtube(query)
            return f"Playing {query} on YouTube."
        
        # Pattern: youtube pe <query> chalao (Hindi)
        match = re.search(r"youtube\s+(?:pe|par|me|mein)?\s*(.+?)(?:\s+chalao|\s+bajao)?$", t)
        if match and "open youtube" not in t and "youtube" != t:
            query = match.group(1).strip()
            if query and query not in ["pe", "par", "me", "mein", ""]:
                search_youtube(query)
                return f"Playing {query} on YouTube."
        
        # Pattern: play <query> (assume YouTube)
        if t.startswith("play ") and "spotify" not in t and "music" not in t:
            query = t.replace("play", "").strip()
            query = re.sub(r'\b(chalao|bajao|sunao)\b', '', query).strip()
            if query and len(query) > 2:
                search_youtube(query)
                return f"Playing {query}."
        
        # Pattern: <query> chalao/bajao (Hindi)
        match = re.search(r"(.+?)\s+(chalao|bajao|sunao|play karo)", t)
        if match:
            query = match.group(1).strip()
            if query and len(query) > 2:
                search_youtube(query)
                return f"Playing {query}."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # SEARCH COMMANDS
    # ──────────────────────────────────────────────────────
    
    def _handle_search(self, t: str, original: str) -> Optional[str]:
        """Handle Google and GitHub search commands."""
        
        # Pattern: search <query> on google
        match = re.search(r"(search|google|find|look up)\s+(.+?)(?:\s+on\s+google)?$", t)
        if match and "youtube" not in t and "github" not in t:
            query = match.group(2).strip()
            if query:
                search_google(query)
                return f"Searching for {query}."
        
        # Pattern: search github for <query>
        if "github" in t and "search" in t:
            query = re.sub(r"search|github|on|for", "", t).strip()
            if query:
                search_github(query)
                return f"Searching GitHub for {query}."
        
        # Pattern: what is / who is
        match = re.search(r"(what is|who is|what are|define|kya hai)\s+(.+)", t)
        if match:
            query = match.group(2).strip()
            search_google(query)
            return f"Searching for {query}."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # WEBSITE COMMANDS
    # ──────────────────────────────────────────────────────
    
    def _handle_website(self, t: str, original: str) -> Optional[str]:
        """Handle opening known websites."""
        
        for name, (func, display) in self.websites.items():
            if name in t:
                func()
                return f"Opening {display}."
        
        if any(x in t for x in ["study mode", "study tabs"]):
            open_study_tabs()
            return "Opening study tabs."
        
        return None
    
    def _handle_dynamic_website(self, t: str, original: str) -> Optional[str]:
        """Handle opening any website dynamically."""
        
        # Remove filler words
        t_clean = re.sub(r'\b(my|the|please|pls)\b', '', t).strip()
        
        match = re.search(r"open\s+(?:website\s+)?([a-zA-Z0-9\-\.]+)", t_clean)
        if match:
            site = match.group(1).strip()
            
            # Skip if it's a known command
            skip = ["notepad", "calculator", "vscode", "downloads", 
                   "documents", "desktop", "chrome", "music"]
            
            if site in skip or site in self.websites:
                return None
            
            if "." not in site:
                site = f"{site}.com"
            
            webbrowser.open(f"https://{site}")
            return f"Opening {site}."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # APP & FOLDER COMMANDS
    # ──────────────────────────────────────────────────────
    
    def _handle_app(self, t: str, original: str) -> Optional[str]:
        """Handle opening system applications."""
        
        for name, (func, display) in self.apps.items():
            if name in t:
                func()
                return f"Opening {display}."
        
        return None
    
    def _handle_folder(self, t: str, original: str) -> Optional[str]:
        """Handle opening system folders."""
        
        for name, (func, display) in self.folders.items():
            if name in t:
                func()
                return f"Opening {display} folder."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # MUSIC COMMANDS
    # ──────────────────────────────────────────────────────
    
    def _handle_music(self, t: str, original: str) -> Optional[str]:
        """Handle music playback commands."""
        
        # Mood-based music
        for mood, (func, display) in self.music_moods.items():
            if mood in t:
                func()
                return f"Playing {display}."
        
        # YouTube Music
        if "youtube music" in t:
            play_youtube_music()
            return "Opening YouTube Music."
        
        # Search song on Spotify
        if any(x in t for x in ["search song", "find song"]):
            query = re.sub(r"search\s+song|find\s+song", "", t).strip()
            if query:
                play_spotify_search(query)
                return f"Searching for {query} on Spotify."
        
        # Generic play music
        if any(x in t for x in ["play music", "music chalao", "music"]) and t != "youtube music":
            play_music()
            return "Playing music."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # INFO COMMANDS (Weather, News, Time)
    # ──────────────────────────────────────────────────────
    
    def _handle_weather(self, t: str, original: str) -> Optional[str]:
        """Handle weather queries."""
        
        if "weather" not in t and "mausam" not in t:
            return None
        
        # Extract city name
        match = re.search(r"(?:weather|mausam)\s+(?:in\s+|of\s+|for\s+)?(\w+)", t)
        city = "delhi"
        
        if match:
            potential_city = match.group(1)
            if potential_city not in ["the", "today", "now", "current", "ka", "ki"]:
                city = potential_city
        
        result = get_weather(city)
        return result
    
    def _handle_news(self, t: str, original: str) -> Optional[str]:
        """Handle news queries."""
        
        if any(x in t for x in ["news", "headlines", "khabar"]):
            result = get_news()
            return f"Here are today's top headlines:\n{result}"
        
        return None
    
    def _handle_time_date(self, t: str, original: str) -> Optional[str]:
        """Handle time and date queries."""
        
        now = datetime.now()
        
        # Time
        if any(x in t for x in ["time", "samay", "kitne baje", "what time"]):
            time_str = now.strftime("%I:%M %p")
            return f"The current time is {time_str}."
        
        # Date
        if any(x in t for x in ["date", "tarikh", "tareekh"]):
            date_str = now.strftime("%A, %d %B %Y")
            return f"Today is {date_str}."
        
        # Day
        if any(x in t for x in ["day", "din", "what day", "today", "aaj"]):
            day_str = now.strftime("%A")
            return f"Today is {day_str}."
        
        return None
    
    
    # ──────────────────────────────────────────────────────
    # AI FALLBACK
    # ──────────────────────────────────────────────────────
    
    def _handle_ai(self, t: str, original: str) -> Optional[str]:
        """Fallback to Gemini AI for unknown commands."""
        response = ask_gemini(original)
        return response


# Legacy function for backward compatibility
def handle_command(text: str) -> str:
    """Process command using OmniBox instance."""
    return OmniBox().process_command(text)