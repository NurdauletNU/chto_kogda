# 1.	Получите от пользователя два дня недели, выведите ему сколько осталось часов до
# наступления большей даты. Также запишите обе даты в json-файл.
import json
import datetime

current_date = datetime.datetime.now()

# Получение дней недели от пользователя
day1 = input("Введите первый день недели: ")
day2 = input("Введите второй день недели: ")

# Преобразование дней недели в объекты datetime
weekday1 = datetime.datetime.strptime(day1, '%A').replace(year=current_date.year, month=current_date.month, day=current_date.day)
weekday2 = datetime.datetime.strptime(day2, '%A').replace(year=current_date.year, month=current_date.month, day=current_date.day)

# Вычисление разницы во времени (в часах)
time_difference = abs(weekday1 - weekday2)
hours_left = time_difference.total_seconds() / 3600

# Вывод оставшихся часов
print(f"До наступления большей даты осталось {hours_left} часов.")

# Создание словаря с датами
dates = {
    "day1": weekday1.strftime("%Y-%m-%d %H:%M:%S"),
    "day2": weekday2.strftime("%Y-%m-%d %H:%M:%S")
}

# Запись словаря в JSON-файл
with open("dates.json", "w") as file:
    json.dump(dates, file)

print("Даты успешно записаны в файл 'dates.json'.")


print()
print()
print()








# 1. Напишите функцию superset(), которая принимает 2 множества. Результат работы
# функции: вывод в консоль одного из сообщений в зависимости от ситуации:
# 1 - «Супермножество не обнаружено»
# 2 – «Объект {X} является чистым супермножеством»
# 3 – «Множества равны»


def superset(set1,set2):
    if set1>set2:
        print(f"Обьект {set1} является чистым супермножеством")
    elif set1<set2:
        print(f"Обьект {set2} является чистым супермножеством")
    elif set1==set2:
        print("Множества равны")
    else:
        print("Супермножество не обнаружено")


superset({1,4}, {1})
superset({1,3}, {3,1})
superset({7,4},{5})

print()
print()
print()


# 2. Создайте программу «Англо-французский словарь». Нужно хранить слово на
# английском языке и его перевод на французский. Требуется реализовать возможность
# добавления, удаления, поиска, замены данных. Используйте словарь для хранения
# информации.

dictionary = {}

def add_word(english_word, french_word):
    dictionary[english_word] = french_word
    print("Слово добавлено в словарь.")

def remove_word(english_word):
    if english_word in dictionary:
        del dictionary[english_word]
        print("Слово удалено из словаря.")
    else:
        print("Слово не найдено в словаре.")

def search_word(english_word):
    if english_word in dictionary:
        french_word = dictionary[english_word]
        print(f"Французское слово для {english_word}: {french_word}")
    else:
        print("Слово не найдено в словаре.")

def replace_word(english_word, new_french_word):
    if english_word in dictionary:
        dictionary[english_word] = new_french_word
        print("Перевод слова обновлен.")
    else:
        print("Слово не найдено в словаре.")

# Пример использования

add_word("apple", "pomme")
add_word("banana", "banane")
add_word("car", "voiture")

search_word("apple")  # Французское слово для apple: pomme

remove_word("banana")
search_word("banana")  # Слово не найдено в словаре.

replace_word("car", "auto")
search_word("car")  # Французское слово для car: auto


print()
print()
print()


# 3. Предоставлен список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу: например, если
# число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка
# «44» (второе повторение, т.е. число дублируется в строке), строка «444» (третье повторение,
# т.е. строка множится на 3).
# Реализуйте вывод множества через функцию set_gen()


def set_gen(n):
    res=set()
    for i in n:
        if n.count(i)>1:
            res.add(str(i)*n.count(i))
        else:
            res.add(i)
    return res


n=[1,1,4,7,8,9,4,4,8]
gen=set_gen(n)
print(gen)



print()
print()
print()
