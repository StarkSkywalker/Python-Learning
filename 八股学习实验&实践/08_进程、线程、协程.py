import asyncio
import time


# 定义一个协程函数 (注意前面的 async 关键字)
async def fetch_data(task_name, delay):
    print(f"[{task_name}] 开始执行，预计耗时 {delay} 秒...")

    # ⚠️ 核心灵魂：遇到 I/O 阻塞（比如网络延迟），立刻使用 await 挂起当前任务！
    # 此时控制权会自动交还给 Event Loop，它会去安排执行其他任务
    await asyncio.sleep(delay)

    print(f"[{task_name}] 执行完毕！")
    return f"结果_{task_name}"


# 启动事件循环的入口
async def main():
    start_time = time.time()

    # 将多个协程任务打包在一起，并发执行
    tasks = [
        fetch_data("任务A", 2),
        fetch_data("任务B", 3),
        fetch_data("任务C", 1)
    ]

    # asyncio.gather 会统筹这些任务，谁好了就处理谁
    results = await asyncio.gather(*tasks)

    print(f"\n所有任务完成，总耗时: {time.time() - start_time:.2f} 秒")
    print(f"最终结果: {results}")


# 运行整个协程程序
if __name__ == "__main__":
    asyncio.run(main())