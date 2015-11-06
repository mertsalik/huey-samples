__author__ = 'mertsalik'

from tasks import count_beans
import datetime

if __name__ == "__main__":
    res = count_beans.schedule(args=(100,), delay=5)  # five sec
    print res
    print res.get()  # will output None
    print res.get()  # will output None
    print res.get(blocking=True)  # lets block until its ready

    in_a_minute = datetime.datetime.now() + datetime.timedelta(seconds=60)
    res = count_beans.schedule(args=(100,), eta=in_a_minute)
    print res.get(blocking=True)  # estimated time of arrival usage