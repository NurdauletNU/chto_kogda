#Реализовать программу с интерфейсом для загрузки выбранного количества файлов
# из https://jsonplaceholder.typicode.com/posts

import tkinter as tk
import asyncio
import aiohttp

url="https://jsonplaceholder.typicode.com/posts"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

async def load_file_async(file_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as responce:
            data= await responce.json()
            with open(f"temp/post_{file_id}.json", mode="w") as json_file:
                json_file.write(str(data))

#asyncio.run(load_file_async())

async def load_files_async(num_files):
    await asyncio.gather(*[load_file_async(file_id) for file_id in range(num_files)]
                         )
    print("Все файлы загружены!")


def load_files():
    num_files = int(num_files_entry.get())
    asyncio.run(load_files_async(num_files))


#load_files()




root = tk.Tk()
root.title("Загрузчик файла")
root.geometry("300x250")
num_files_label = tk.Label(root, text="Укажите какое количество файлов хотите загрузить:")
num_files_label.pack()
num_files_entry = tk.Entry(root)
num_files_entry.pack()
load_button = tk.Button(root, text="Загрузить",command=load_files)
load_button.pack()
root.mainloop()

