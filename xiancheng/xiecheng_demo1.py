import asyncio
import time
from random import randint

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main1():
    await say_after(2, '2s')
    await say_after(1, '1s')

async def main2():
    await asyncio.gather(say_after(2, '2s'), say_after(1, '1s'))

def main():
    asyncio.get_event_loop().run_until_complete(say_after)
    asyncio.run()


if __name__ == "__main__":
    main()