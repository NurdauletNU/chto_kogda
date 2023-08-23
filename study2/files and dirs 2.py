# Todo работа с JSON  ФАЙЛАМИ
import json
import os

# Serialize obj as a JSON formatted (де-факто стандарт для веба)
# сериализация obj (Python)=>JSON
# десериализация JSON =>obj (Python)

dict1={"name":"Nurdaulet", "age":30,"married":True}

with open("data/new.json", mode="w") as file1:
    json.dump(dict1,file1)                        # сериализация obj (Python)=>JSON


# чтение
with open("data/new.json", mode="r") as f:
    dict2=json.load(f)                           # десериализация JSON =>obj (Python)
    print(dict2)

# Todo работа с папками
print(os.getcwd())        # текущая директория

second=r"C:\chto_kogda"
third="OOP"
path=os.path.join(second,third)          # СКЛЕИВАНИЕ ДВУХ ПУТЕЙ
print(f"path: {path}")