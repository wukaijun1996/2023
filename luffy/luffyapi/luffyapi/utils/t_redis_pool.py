import redis

# pool必须是单例的
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=100)

r = redis.Redis(connection_pool=POOL, )

ret = r.keys()
print(ret)
ret = r.get('name')
print(ret.decode())


