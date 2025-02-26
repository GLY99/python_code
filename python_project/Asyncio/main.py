import asyncio

async def task(num):
    await asyncio.sleep(num)
    return num

async def run_task():
    my_list = []
    tasks = [asyncio.create_task(task(i)) for i in range(5)]
    for future in asyncio.as_completed(tasks):
        result = await future
        print(result)
        my_list.append(result)
    return my_list


if __name__ == "__main__":
    my_list = asyncio.run(run_task())  # 运行异步主函数
    print(my_list)  # [0, 1, 2, 3, 4]