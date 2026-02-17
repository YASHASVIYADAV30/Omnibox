import requests
from utils.config import NEWS_KEY


def get_news() -> str:
    
        

    try:
        url = (
            f"https://newsapi.org/v2/top-headlines?"
            f"country=in&apiKey={NEWS_KEY}"
        )

        data = requests.get(url).json()

        articles = data.get("articles", [])[:5]

        headlines = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]

        return "\n".join(headlines)

    except:
        return "Sorry, couldn't fetch news right now."
