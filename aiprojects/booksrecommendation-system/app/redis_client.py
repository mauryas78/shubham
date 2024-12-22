import redis

# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

# def get_redis_client():
#     return redis.Redis(connection_pool=pool)
KEY= 'shubhammourya'
USER='user'
BOOKS='books'
BOOKID='book_id'

class RedisClient:
    def __init__(self, 
                 host='localhost', 
                 port=6379, db=0):
        
        pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.redis_client=redis.Redis(connection_pool=pool)
        
    def get_next_id(self,key):
        return self.redis_client.incr(key)

    def get_value(self, key):
        value = self.redis_client.get(key)
        if value:
            return value.decode('utf-8')
        else:
            return None

    def upsert_value(self, key, value):
        self.redis_client.set(key, value)
