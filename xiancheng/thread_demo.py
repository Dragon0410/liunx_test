#!/usr/bin/python3

from threading import Thread, currentThread
import os, time
from random import randint

def myfunc(x):
    s = randint(1, 4)
    time.sleep(s)
    save_data = {
        'id': x,
        'sleep': s,
        'result': x * x,
        'tid': currentThread().ident,
        'tname': currentThread().getName(),
    }
    print("===", save_data)
    return x * x


def main():
    thread_list = []
    for i in range(10):
        t = Thread(target=myfunc, args=(i, ))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()


if __name__ == "__main__":
    main()