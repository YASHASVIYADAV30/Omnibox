"""
OmniBox - Configuration
Environment variables and API keys management.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Central configuration manager for OmniBox.
    Loads API keys and settings from environment variables.
    """
    
    def __init__(self):
        """Initialize configuration by loading environment variables."""
        self.gemini_key = os.getenv("GEMINI_KEY")
        self.weather_key = os.getenv("WEATHER_KEY")
        self.news_key = os.getenv("NEWS_KEY")
        
        # Validate required keys
        self._validate_keys()
    
    def _validate_keys(self):
        """Check if essential API keys are present."""
        missing_keys = []
        
        if not self.gemini_key:
            missing_keys.append("GEMINI_KEY")
        if not self.weather_key:
            missing_keys.append("WEATHER_KEY")
        if not self.news_key:
            missing_keys.append("NEWS_KEY")
        
        if missing_keys:
            print(f"⚠️  Warning: Missing API keys: {', '.join(missing_keys)}")
            print("💡 Add them to your .env file for full functionality.")
    
    def is_valid(self) -> bool:
        """Check if all required keys are configured."""
        return all([self.gemini_key, self.weather_key, self.news_key])


# Legacy support - direct imports (backward compatibility)
GEMINI_KEY = os.getenv("GEMINI_KEY")
WEATHER_KEY = os.getenv("WEATHER_KEY")
NEWS_KEY = os.getenv("NEWS_KEY")