import os

class Config:
    API_URL = os.getenv('API_URL')
    API_KEY = os.getenv('API_KEY')
    REDIS_URL = os.getenv('REDIS_URL')
    CACHE_TTL = int(os.getenv('CACHE_TTL', '600'))