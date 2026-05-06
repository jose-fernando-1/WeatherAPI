import redis


class RedisRepository:
	def __init__(self, redis_url: str):
		self.client = redis.Redis.from_url(redis_url, decode_responses=True)
