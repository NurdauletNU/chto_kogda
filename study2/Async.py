import aiohttp        # аналогия request
import asyncio
import random
import aiofiles



url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

async def async_t():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as response:
            data=await response.read()
            with open(f"temp/image{random.randint(1,100000)}.jpg", mode="wb") as opened_file:
                opened_file.write(data)



asyncio.run(async_t())

