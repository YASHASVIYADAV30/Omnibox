from google import genai
from utils.config import GEMINI_KEY


client = genai.Client(api_key=GEMINI_KEY)


def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
