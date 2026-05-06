from flask import Flask, jsonify, request

from app.config import Config
from app.repositories.redis import RedisRepository
from app.services.data_service import get_weather_data

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.get('/')
    def index():
        city = request.args.get('city')
        if not city:
            return jsonify({'error': 'city query parameter is required'}), 400

        redis_url = app.config.get('REDIS_URL')
        if not redis_url:
            return jsonify({'error': 'REDIS_URL is not configured'}), 500

        redis_repo = RedisRepository(redis_url)
        weather_data = get_weather_data(city, redis_repo, app.config['CACHE_TTL'])
        return jsonify(weather_data), 200

    return app