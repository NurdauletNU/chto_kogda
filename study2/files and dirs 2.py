# Todo работа с JSON  ФАЙЛАМИ
import json
import os
import shutil

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
print(os.getcwd())                      # текущая директория

second=r"C:\chto_kogda"
third="OOP"
path=os.path.join(second,third)          # СКЛЕИВАНИЕ ДВУХ ПУТЕЙ
# print(f"path: {path}")


# Работа с файлами и директориями:

# os.getcwd(): Возвращает текущую рабочую директорию.
# os.listdir(path): Возвращает список файлов и директорий в указанной директории.
# os.mkdir(path): Создает новую директорию.
# os.makedirs(path): Создает директорию(и) рекурсивно (включая промежуточные директории).
# os.remove(path): Удаляет файл.
# os.rmdir(path): Удаляет пустую директорию.
# os.removedirs(path): Удаляет директорию(и) рекурсивно.
# os.rename(src, dst): Переименовывает файл или директорию.

# print(os.remove("znew.txt")) -удаление файла если файла нет произойдет ошибка
# print(os.rmdir("temp")) -удаление пустой папки
# print(shutil.rmtree("temp")) - удаление не пустой папки
# print(os.mkdir("data")) -создание папки
# print(os.makedirs(r"C:\chto_kogda\study2\file1")) -создание директории папки

#for file in os.listdir("data"):
#    print(file)


# os.walk() - это функция из модуля os, предназначенная для рекурсивного обхода директорий
# и поддиректорий в заданной корневой директории.
# Она возвращает генератор, который генерирует кортежи для каждой директории,
# которые включают путь к текущей директории, список поддиректорий и список файлов в этой директории.

for root,dirs,files in os.walk("."):
    for i in dirs:
        print(root,i)
    for file in files:
        print(root,file)



# Работа с переменными окружения:

# os.environ: Словарь с переменными окружения.
# os.environ.get(key): Получает значение переменной окружения по ключу.
# os.environ.putenv(key, value): Устанавливает значение переменной окружения.


# Работа с путями:

# os.path.join(path, *paths): Объединяет пути в один.
# os.path.abspath(path): Возвращает абсолютный путь.
# os.path.exists(path): Проверяет существование пути.
# os.path.isdir(path): Проверяет, является ли путь директорией.
# os.path.isfile(path): Проверяет, является ли путь файлом.

print(os.path.abspath("OOP"))                    # ВОЗВРАЩЕНИЕ АБСОЛЮТНОГО ПУТИ
print(os.path.exists("C:\chto_kogda\study2"))    # Проверяет уществует ли такой путь
# Управление процессами:

# os.system(command): Выполняет системную команду.
# os.spawnl(mode, path, ...args): Запускает новый процесс.
# os.kill(pid, signal): Посылает сигнал процессу.

# Другие полезные функции:

# os.name: Возвращает имя операционной системы.
# os.getpid(): Возвращает идентификатор текущего процесса.
# os.getlogin(): Возвращает имя пользователя, вошедшего в систему.
# os.chmod(path, mode): Изменяет права доступа к файлу.
