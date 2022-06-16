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
    value_y = p.map(func=myf, iterable=value_x)
    print(value_y)


if __name__ == "__main__":
    main()
