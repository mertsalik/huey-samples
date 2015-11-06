__author__ = 'mertsalik'

from huey import crontab
from datetime import datetime

from config import huey


@huey.periodic_task(crontab(minute='*/5'))
def print_time_every_five_minutes():
    """Runs Every five minutes
    :return:
    """
    print datetime.now()


@huey.periodic_task(crontab(minute='*'))
def print_foo_every_minute():
    """Runs every 20 seconds
    :return:
    """
    print "foo"
