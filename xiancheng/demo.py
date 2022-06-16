import time
from tqdm import tqdm
from functools import wraps


def countimer(func):

    @wraps(func)
    def tt(*args, **kwargs):
        startime = time.time()
        value = func(*args, **kwargs)
        endtime = time.time()
        haotime = endtime - startime
        print(f"耗时：{haotime:.2f}")
        return value

    return tt


def myf(x):
    time.sleep(2)
    return x * x


@countimer
def main():
    listx = range(10)
    listy = []

    for i in tqdm(listx):
        temp_value = myf(i)
        listy.append(temp_value)

    print("final y:", listy)


if __name__ == "__main__":
    main()