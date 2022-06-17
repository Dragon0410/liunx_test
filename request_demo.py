import requests
import time
import requests_cache
from functools import wraps


def cost_time(func):

    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Cost Time: ", end_time - start_time)
        return func

    return inner

@cost_time
def demo1():
    session = requests.Session()
    for i in range(10):
        session.get('http://httpbin.org/delay/1')
        print(f"Finished {i + 1} requests")

@cost_time
def demo2():
    session = requests_cache.CachedSession('demo_cache')
    for i in range(10):
        session.get('http://httpbin.org/delay/1')
        print(f"Finished {i + 1} requests")
demo1()