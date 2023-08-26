# Пишем программу для бухгалтерии, с интерфейсом(внешний вид)
# это windows 10, 1.exe и внутри папки есть некоторое количество json файлов
# по нажатию на кнопку "старт" программа должна "складывать" все эти файлы в один итоговый
# уникальность по id
# https://jsonplaceholder.typicode.com/todos

import json
import tkinter as tk
import os

def start():
    data=[]
    for root,dirs,files in os.walk("temp",topdown=True):
        for name in files:
            extensions=name.split(".")[-1]
            if extensions.lower()=="json":
                with open(f"temp/{name}",mode="r") as file:
                    data_new=json.load(file)
                    if isinstance(data_new,list):
                        data.extend(data_new)
                    else:
                        data.append(data_new)
    new_data=[]
    for d in data:
        is_new=True
        for n in new_data:
            if d["id"]==n["id"]:
                is_new=False
                break
        if is_new:
            new_data.append(d)
    for d in new_data:
        print(d)

    with open("temp/all.json", mode="w") as file2:
        json.dump(new_data,file2)

start()