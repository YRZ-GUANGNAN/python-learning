import asyncio
import time


async def work(name, seconds):
    print(f"{name} 开始")
    await asyncio.sleep(seconds)
    print(f"{name} 结束")


async def main():
    start = time.time()

    await work("A", 2)
    await work("B", 1)
    await work("C", 3)

    print(f"总耗时 {time.time() - start:.2f} 秒")


asyncio.run(main())