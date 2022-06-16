import asyncio
import arrow


def current_time():
    """获取指定时区 时间"""
    return arrow.now().to('Asia/Shanghai').format("YYYY-MM-DD HH:mm:ss")


async def func(sleep_time):
    func_name_suffix = sleep_time * 5
    print(f"[{current_time()}] 执行异步函数 {func.__name__} -> {func_name_suffix}")
    await asyncio.sleep(sleep_time)
    print(f"[{current_time()}] 函数 {func.__name__}-->{func_name_suffix} 执行完毕")
    return f"【[{current_time()}] 得到函数 {func.__name__}==> {func_name_suffix} 执行结果】"


async def run():
    task_list = []
    for i in range(10):
        task = asyncio.create_task(func(i))
        task_list.append(task)

    done, pending = await asyncio.wait(task_list, timeout=None)
    for done_task in done:
        print(f"[{current_time()}] 得到执行结果 {done_task.result()}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()