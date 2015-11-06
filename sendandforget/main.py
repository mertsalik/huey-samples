__author__ = 'mertsalik'

from config import huey
from tasks import count_beans

if __name__ == "__main__":
    beans = raw_input("How many beans? \n")
    count_beans(beans)
    print 'Enqueued job to count %s beans' % beans
