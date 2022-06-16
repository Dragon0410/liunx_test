from multiprocessing import Pool, TimeoutError
from tqdm import tqdm
import time
from demo import countimer


def myf(x):
    if x % 5 == 0:
        time.sleep(5)
    else:
        time.sleep(2)
    return x * x


def safely_get(value, timeout=2):
    try:
        data = value.get(timeout=timeout)
    except TimeoutError:
        data = 0
    return data


@countimer
def main():

    value_x = range(100)
    p = Pool(processes=4)
    pbar = tqdm(total=len(value_x))
    res = [p.apply_async(func=myf, args=(i, ), callback=lambda _: pbar.update(1)) for i in value_x]
    result = [safely_get(i, timeout=1) for i in res]

    print(result)


if __name__ == "__main__":
    main()
