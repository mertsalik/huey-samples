__author__ = 'mertsalik'

from huey import Huey
from huey.backends.redis_backend import RedisBlockingQueue

queue = RedisBlockingQueue('test-queue', host='localhost', port=6379)
huey = Huey(queue)
