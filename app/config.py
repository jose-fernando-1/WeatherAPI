import os

class Config:
    API_URL = os.getenv('API_URL')
    REDIS_URL = os.getenv('REDIS_URL')