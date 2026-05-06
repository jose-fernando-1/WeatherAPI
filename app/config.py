import os

class Config:
    API_URL = os.getenv(
        'API_URL',
        'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
    )
    API_KEY = os.getenv('API_KEY')
    UNIT_GROUP = "metric"
    CONTENT_TYPE = "json"
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    CACHE_TTL = int(os.getenv('CACHE_TTL', '600'))