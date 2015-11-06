__author__ = 'mertsalik'

from config import huey
from tasks import count_beans

if __name__ == "__main__":
    beans = raw_input("How many beans? \n")
    res = count_beans(beans)
    print res
    print res.get()  # will output None
    print res.get(blocking=True)  # will output Counted blabla beans
