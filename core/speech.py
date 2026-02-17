"""
OmniBox - Speech Module

Handles Text-to-Speech and Speech-to-Text.
Uses Indian English accent for natural conversation.
"""

import pyttsx3
import speech_recognition as sr


def _init_engine():
    """Initialize speech engine with Indian English voice."""
    eng = pyttsx3.init('sapi5')
    
    voices = eng.getProperty("voices")
    
    # Try to find Indian English voice
    indian_voice = None
    female_voice = None
    
    for voice in voices:
        name = voice.name.lower()
        
        # Look for Indian voice
        if "india" in name or "hindi" in name:
            indian_voice = voice.id
        
        # Fallback to female voice
        if "zira" in name or "female" in name:
            female_voice = voice.id
    
    # Set voice priority: Indian > Female > Default
    if indian_voice:
        eng.setProperty("voice", indian_voice)
    elif female_voice:
        eng.setProperty("voice", female_voice)
    elif len(voices) > 1:
        eng.setProperty("voice", voices[1].id)
    
    # Speech settings
    eng.setProperty("rate", 160)
    eng.setProperty("volume", 1.0)
    
    return eng


# Initialize globally
engine = _init_engine()
recognizer = sr.Recognizer()


def speak(text: str) -> None:
    """
    Speak the given text out loud.
    
    Args:
        text: Text to speak
    """
    global engine
    
    if not text or not text.strip():
        return
    
    try:
        clean_text = text.strip()
        print(f"🔊 {clean_text}")  # Show what's being spoken
        engine.say(clean_text)
        engine.runAndWait()
    except:
        engine = _init_engine()
        engine.say(text.strip())
        engine.runAndWait()


def listen() -> str:
    """
    Listen for voice input.
    
    Returns:
        Recognized text or empty string
    """
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        
        text = recognizer.recognize_google(audio, language="en-IN")
        return text
    
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        return ""
    except:
        return ""


if __name__ == "__main__":
    print("Testing speech...")
    speak("Hello! I am OmniBox, your personal assistant.")
    print("Done!")