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
    """
    请求了一个网站，是 http://httpbin.org/delay/1，这个网站模拟了一秒延迟，也就是请求之后它会在 1 秒之后才会返回响应。
    这里请求了 10 次，那就至少得需要 10 秒才能完全运行完毕。
    """
    session = requests.Session()
    for i in range(10):
        session.get('http://httpbin.org/delay/1')
        print(f"Finished {i + 1} requests")


@cost_time
def demo2():
    """
    这里我们声明了一个 CachedSession，将原本的 Session 对象进行了替换，还是请求了 10 次。
    执行完之后，这时候我们可以发现，在本地生成了一个 demo_cache.sqlite 的数据库
    """
    session = requests_cache.CachedSession('demo_cache')
    for i in range(10):
        session.get('http://httpbin.org/delay/1')
        print(f"Finished {i + 1} requests")

# 可以可以看到，这个 key-value 记录中的 key 是一个 hash 值，value 是一个 Blob 对象，里面的内容就是 Response 的结果。
# 可以猜到，每次请求都会有一个对应的 key 生成，然后 requests-cache 把对应的结果存储到了 SQLite 数据库中了，后续的请求和第一次请求的 URL 是一样的，经过一些计算它们的 key 也都是一样的，所以后续 2-10 请求就立马返回了。
# 是的，利用这个机制，我们就可以跳过很多重复请求了，大大节省爬取时间。

demo1()