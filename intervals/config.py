__author__ = 'mertsalik'

from huey import RedisHuey

huey = RedisHuey('test-queue', host='localhost', port=6379)
