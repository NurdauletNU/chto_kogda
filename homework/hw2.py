# 1. Напишите программу которая будет шифровать текст шифром Цезаря.
# В шифре Цезаря используется прописные буквы латинского алфавита и пробел
# ' abcdefghijklmnopqrstuvwxyz'
# Схема работы: Шифр Цезаря заключается в замене каждого символа входной строки на
# символ, находящийся на несколько позиций левее или правее его в алфавите.
# Для всех символов сдвиг один и тот же. Сдвиг циклический, если к последнему символу
# алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.
# Пользователь вводит число – сдвиг шифрования. Если число положительное сдвиг
# вправо, отрицательное влево. На второй строке вводится текст.
# Используйте функцию chr(),ord()
# chr(number) принимает в качестве аргумента число, и возвращает юникод.

def cesar_shrift(shrift,text):
    upgrade_text=""
    for i in text:
        if i.isalpha():
            if i.isupper():
                N=ord("A")
            else:
                N=ord("a")

            new=chr((ord(i) - N + shrift) % 26 + N)
            upgrade_text+=new

        else:
            upgrade_text+=i

    return upgrade_text



shrift=int(input("Введите шрифт: "))
text=input("Введите текст: ")

changed_text=cesar_shrift(shrift,text)

print(changed_text)

print()
print()
print()



# 2. Пользователь вводит с клавиатуры название фрукта. Необходимо вывести на экран
# количество раз, сколько фрукт встречается в кортеже в качестве элемента.


fruit=input("Введите фрукт: ")
fruits_tuple=("apple", "banana", "pear", "apple", "pineapple", "strawberry", "apple", "banana")
sk=fruits_tuple.count(fruit)
print(sk)

print()
print()
print()








# 3. Добавьте к заданию 1 подсчет количества раз, когда название фрукта является частью
# элемента. Например, banana, apple, bananamango, mango, strawberry-banana. В примере выше
# banana встречается три раза.


fruits_tp=("banana", "grape-banana", "mango", "kiwi", "strawberry-banana", "cherry")
c=[i for i in fruits_tp if "banana" in i]
print(len(c))
print()
print()
print()



# 4. Есть кортеж с названиями производителей автомобилей (название производителя
# может встречаться от 0 до N раз). Пользователь вводит с клавиатуры название производителя
# и слово для замены. Необходимо заменить в кортеже все элементы с этим названием на слово
# для замены. Совпадение по названию должно быть полным

cars=("Lexus", "Mercedes", "Honda", "Volkswagen", "Shevrolet", "Honda", "Toyota", "Hyindai", "Honda")
new_car=input("Введите новую марку машины для замены: ")   # Введите Audi
car_in_tuple=input("Введите заменяемую машину: ")          # Введите Honda
new_cars=[new_car if i==car_in_tuple else i for i in cars]
print(tuple(new_cars))


