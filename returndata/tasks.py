__author__ = 'mertsalik'

from config import huey
from datetime import datetime


@huey.task()
def count_beans(num):
    print '-- counted {0} beans --'.format(num)
    return 'Counted {0} beans'.format(num)


@huey.task(retries=3, retry_delay=10)
def try_thrice():
    print "trying....{}".format(datetime.now())
    raise Exception('nope')
