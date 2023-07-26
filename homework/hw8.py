import tkinter as tk
from tkinter import filedialog
import requests
import os
import concurrent.futures
import multiprocessing
import asyncio
import random
import threading
import aiohttp

# Напишите программу с интерфейсом, которая по нажатию кнопки загружает 10 картинок в папку.
# Проверьте все способы: синхронный, многопоточный, мультипроцессорный, асинхронный


url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'}


def sync_download_one_image():
    response = requests.get(url=url, headers=headers)
    with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(response.content)



def sync_download_mass_image():

    # загрузка 10 картинок в этом потоке
    for i in range(1, 10 + 1):
        sync_download_one_image()

# sync_download_mass_image()





def threading_download_mass_image():


    thread_list = []
    for i in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=sync_download_one_image, args=(), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


# threading_download_mass_image()

def processing_download_mass_image():



    process_list = []
    for i in range(1, 10 + 1):
        process_list.append(multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()


# processing_download_mass_image()

async def async_download_one_image():
    # time.sleep(0.1)
    await asyncio.sleep(0.1)
    async with aiohttp.ClientSession() as session:
         async with session.get(url=url, headers=headers) as response:
             data = await response.read()
             async with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
                  opened_file.write(data)

def async_task():

    async def async_task_inline():  # coroutine - have promise (awaitable)
        await asyncio.gather(*[async_download_one_image() for _ in range(1, 100 + 1)])
    asyncio.run(async_task_inline())  # todo START TASK ON EVENT LOOP

# async_task()

def create_interface():
    window = tk.Tk()
    window.title("Загрузчик изображений")
    window.geometry("400x300")

    label = tk.Label(window, text="Нажмите кнопку для выбора папки")
    label.pack(pady=20)

    button = tk.Button(window, text="temp", command=async_task)
    button.pack()

    window.mainloop()


create_interface()

if __name__ == '__main__':
    create_interface()