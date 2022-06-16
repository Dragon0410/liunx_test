from multiprocessing import Process, Manager, Pool
import os, time
import pandas as pd
from tqdm import tqdm


def worker(id, save_data):
    time.sleep(1)
    save_data[id] = {
        '子进程': [os.getpid()],
        '父进程': [os.getppid()],
        '进程id': [id],
    }


def main():
    finaldata = Manager().dict()
    subprocess_list = []

    for i in tqdm(range(200)):
        p = Process(target=worker, args=(i, finaldata))
        subprocess_list.append(p)
        p.start()

    for p in tqdm(subprocess_list):
        p.join()

    finaldata = pd.concat(
        [pd.DataFrame(value) for (key, value) in finaldata.items()])
    print("==", finaldata)


def main1():
    finaldata = Manager().dict()
    p = Pool(processes=4)
    reslist = [
        p.apply_async(func=worker, args=(i, finaldata)) for i in range(200)
    ]
    [i.get() for i in tqdm(reslist)]
    finaldata = pd.concat(
        pd.DataFrame(value) for key, value in finaldata.items())
    print(finaldata)


if __name__ == "__main__":
    main1()