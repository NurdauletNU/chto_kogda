import tkinter as tk
import time
import threading
import random
import requests
import multiprocessing


# Синхронное программирование

def data():
    index=1
    while True:
        time.sleep(0.2)
        print(index)
        index+=1
        label.config(text=f"index:{index}")
        if index==30:
            break

root=tk.Tk()
root.title("Приложение на ткинтер")
root.geometry("400x300")
label=tk.Label(text="Hello Everyone")
label.pack()
btn=tk.Button(text="Кликните", command=data)
btn.pack()
#root.mainloop()






url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

def download_one_image():
    responce=requests.get(url=url, headers=headers)
    with open(f"temp/image{random.randint(1,1000000)}.jpg",mode="wb") as opened_file:
        opened_file.write(responce.content)


def download_mass_image():
    start = time.perf_counter()
    for i in range(10):
        download_one_image()
    print("Заняло время", time.perf_counter() - start)

#download_mass_image()







# Todo threading programming
def threading_download_mass_image1():
    start_time=time.perf_counter()
    new_thread=threading.Thread(target=download_one_image(),args=(),kwargs={})
    new_thread.start()
    new_thread.join()
    print(f"Времени заняло:", round(time.perf_counter()-start_time,5) )

#threading_download_mass_image1()



# Загрузка 10 картинок в дополнительных 10 потоках

def threading_download_mass_image2():
    start_time=time.perf_counter()
    thread_list=[]
    for i in range(10):
        thread_list.append(threading.Thread(target=download_one_image(),args=(),kwargs={}))
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
    print(f"Задача выполнена за {time.perf_counter()-start_time}")

# threading_download_mass_image2()


# Multiprocessing

def process_download_mass_image():
    start_time=time.perf_counter()
    process_list=[]
    for i in range(1):
        process_list.append(multiprocessing.Process(target=download_one_image(),args=(),kwargs={}))
        for process in process_list:
            process.start()
        for process in process_list:
            process.join()
    print(f"Задача выполнена за {time.perf_counter()-start_time}")






