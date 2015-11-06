__author__ = 'mertsalik'

from huey import Huey
from huey.backends.redis_backend import RedisBlockingQueue
from huey.backends.redis_backend import RedisDataStore

queue = RedisBlockingQueue('test-queue', host='localhost', port=6379)
results_store = RedisDataStore('results', host='localhost', port=6379)

huey = Huey(queue, result_store=results_store)
# or , huey = RedisHuey('test-queue', host='localhost', port=6379)
