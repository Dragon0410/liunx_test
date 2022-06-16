from multiprocessing import Pool
from tqdm import tqdm
import time
from demo import countimer


def myf(x):
    time.sleep(2)
    return x * x


@countimer
def main():

    value_x = range(10)
    p = Pool(processes=4)
    res = [p.apply_async(func=myf, args=(i, )) for i in value_x]
    result = [i.get() for i in tqdm(res)]

    print(result)


def main1():
    value_x = range(10)
    p = Pool(processes=4)
    pbar = tqdm(total=len(value_x))
    res = [p.apply_async(func=myf, args=(i, ), callback=lambda _: pbar.update(1)) for i in value_x]
    result = [i.get() for i in res]

    print(result)


if __name__ == "__main__":
    main1()
