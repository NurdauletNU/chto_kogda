import json
import requests


# Получите от пользователя число, затем загрузите с сайта https://jsonplaceholder.typicode.com/todos/№
# одну  «todo», и запишите её в текстовый файл с её индексом(id.json)


def load_todo_from_website(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    response = requests.get(url)
    if response.status_code == 200:
        todo = response.json()
        return todo
    else:
        return None

def save_todo_to_file(todo_id, todo):
    filename = f"{todo_id}.json"
    with open(filename, 'w') as file:
        json.dump(todo, file)

# Получаем число от пользователя
todo_id = input("Введите число для загрузки todo: ")

# Проверяем, является ли введенное значение числом
if todo_id.isdigit():
    todo_id = int(todo_id)

    # Загружаем todo с указанным ID
    todo = load_todo_from_website(todo_id)

    if todo:
        # Сохраняем загруженную todo в файл
        save_todo_to_file(todo_id, todo)
        print(f"Todo с ID {todo_id} успешно сохранена в файл {todo_id}.json")
    else:
        print(f"Todo с ID {todo_id} не найдена.")
else:
    print("Введено некорректное значение. Пожалуйста, введите целое число.")











# Функция plus_two() выполняет одну простую задачу — выводит результат сложения
# переданного в нее числа 2 и значения переменной number. В переменную number должно быть
# передано число. Обработайте ситуацию, если в эту переменную переданы данные какого-то
# другого типа. В случае ошибки напечатайте в консоли сообщение «Ожидаемый тип данных
# — число!».
# Запустите код и проверьте работу кода в консоли.
# Подсказка:
# Используйте конструкцию try/except.В процессе поиска решения попробуйте вывести в
# консоль сумму строки и числа, изучите сообщение об ошибке.В Python есть специальное
# исключение для ситуации, если тип переданного значения не соответствует ожиданиям.


def plus_two(n):

    try:
        result = 2 + n
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")



plus_two(5)
plus_two("Hi")

print()
print()


# Напишите программу, которая позволяет получить доступ к элементу массива, индекс
# которого выходит за границы, и обработаем соответствующее исключение


def get_index(list_a,index):

    try:
        print("Номер индекса:",list_a[index])
    except IndexError:

        print("Номер индекса вышел из-за границы")


get_index([8,5,-6,2],1)
get_index(["Python","Java", "Go", "Docker","R","C++"],10)



print()
print()










