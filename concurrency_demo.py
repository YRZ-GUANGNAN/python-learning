import time
import threading
import multiprocessing


def cpu_task(n):
    """纯计算任务：累加 n 个数"""
    total = 0
    for i in range(n):
        total += i * i
    return total


if __name__ == "__main__":
    N = 20_000_000

    # ① 串行
    start = time.time()
    cpu_task(N)
    cpu_task(N)
    print(f"串行     : {time.time() - start:.2f} 秒")

    # ② 多线程
    start = time.time()
    t1 = threading.Thread(target=cpu_task, args=(N,))
    t2 = threading.Thread(target=cpu_task, args=(N,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"多线程   : {time.time() - start:.2f} 秒")

    # ③ 多进程
    start = time.time()
    p1 = multiprocessing.Process(target=cpu_task, args=(N,))
    p2 = multiprocessing.Process(target=cpu_task, args=(N,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"多进程   : {time.time() - start:.2f} 秒")