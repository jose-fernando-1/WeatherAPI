import requests
from urllib.parse import quote

from app.config import Config

def fetch_weather_data(city: str) -> dict:
    encoded_city = quote(city)
    url = f"{Config.API_URL}/{encoded_city}"
    params = {
        'unitGroup': Config.UNIT_GROUP,
        'key': Config.API_KEY,
        'contentType': Config.CONTENT_TYPE,
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()