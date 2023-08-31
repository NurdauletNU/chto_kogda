import tkinter as tk
from tkinter import filedialog
import aiohttp
import asyncio

async def download_file(session, url, file_id):
    async with session.get(url) as response:
        content = await response.json()
        with open(f"file_{file_id}.json", "w") as file:
            file.write(str(content))
        print(f"File {file_id} downloaded")

async def download_files_async(num_files):
    base_url = "https://jsonplaceholder.typicode.com/posts"

    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, f"{base_url}/{file_id}", file_id) for file_id in range(1, num_files + 1)]
        await asyncio.gather(*tasks)
    print("All files downloaded")

def download_files():
    num_files = int(num_files_entry.get())    # Вот это надо вставить
    asyncio.run(download_files_async(num_files))

root = tk.Tk()
root.title("File Downloader")

num_files_label = tk.Label(root, text="Количество файлов:")
num_files_label.pack()
num_files_entry = tk.Entry(root)
num_files_entry.pack()
download_button = tk.Button(root, text="Загрузить", command=download_files)
download_button.pack()

root.mainloop()
