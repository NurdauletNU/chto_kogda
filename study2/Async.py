import aiohttp        # аналогия request
import asyncio
import random




                  # Асинхронное программирование



url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

async def async_t():
    await asyncio.sleep(1.0)
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as response:
            data=await response.read()  # тут поток начинает делать другие задачи, пока эта задача не закончится

            with open(f"temp/image{random.randint(1,100000)}.jpg", "wb") as opened_file:
                opened_file.write(data)



# asyncio.run(async_t())       # загрузка одной картинки





# Загрузка множества картинок

async def async_task_asyncio():
    await asyncio.gather(
        *[async_t()for _ in range(10)]
    )
# asyncio.run(async_task_asyncio())



# Или можно так сделать


async def async_with_list():
    list_async=[]
    for _ in range(10):
        list_async.append(async_t())
    await asyncio.gather(asyncio.gather(*list_async))

#asyncio.run(async_with_list())








