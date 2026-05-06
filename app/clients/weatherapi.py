import requests
from app.config import Config

def fetch_weather_data(city: str) -> dict:
    url = f"{Config.API_URL}?q={city}&appid={Config.API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()