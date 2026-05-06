from app.repositories.redis import RedisRepository
import json
from app.clients.weatherapi import fetch_weather_data

def get_weather_data(city: str, redis_repo: RedisRepository, cache_ttl: int) -> dict:
    cached_data = redis_repo.client.get(city)
    if cached_data:
        return json.loads(cached_data)

    weather_data = fetch_weather_data(city)
    redis_repo.client.setex(city, cache_ttl, json.dumps(weather_data))
    return weather_data