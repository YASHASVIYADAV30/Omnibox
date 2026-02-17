import requests
from utils.config import WEATHER_KEY


def get_weather(city: str = "delhi") -> str:
    
       

    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={WEATHER_KEY}&units=metric"
        )

        data = requests.get(url).json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"{city.title()} temperature is {temp}°C with {desc}"

    except:
        return "Sorry, couldn't fetch weather right now."
