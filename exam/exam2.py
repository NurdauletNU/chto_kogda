#  В чем разница между списком и кортежем?
import sys
a=[1,2,3]
b=(1,2,3)
print(sys.getsizeof(a))
print(sys.getsizeof(b))


# Как выполняется интерполяция строк?

name="Nurdaulet"
balamce=1700
print(f"Здраствуйте {name} ваш баланс {balamce}")

#  Как развернуть список?
list1=[1,2,3,4,5]
list1.reverse()
print(list1)


print(list1[::-1])


# Как работает умножение строк?

a="Привет"

print(a[0:len(a)//2])


# Как работает умножение списка?
list2=[1,2,3,40]
print(list2[-1])



# Как объединить списки в Python?
list3=[5,6,8,90]
list4=[80,50,60]
print(list3+list4)

# Как округлить число до трех десятичных знаков?
int1=5.6786
print(round(int1,3))

#  Как проверить, существует ли значение в списке?


list5=[70,80,90,100]
a=70 in list5
print(a)

# Как получить абсолютное значение целого числа?
# import math

int2=-40
print(abs(int2))


# Как реализуется наследование классов в Python?

class Animal:
    say="Meow"

class Cat(Animal):
    pass



a1=Animal()
c1=Cat()
print(c1.say)
print(a1.say)


# Проверьте, что в строке только числа
str1="hergx25"

# Получите список ключей из словаря

dict1={1:"1", 2:"two", 3:True}

# for i in dict1.keys():
#     print(i)

# Как перевести строку в верхний/нижний регистр?


a=12
b=a
print(a)
print(b)

a=15
print(a)
print(b)






a={"value":12}
b=a.copy()
print(a)
print(b)

a["value"]=15
print(a)
print(b)


# Какие циклы есть в python и чем отличаются

# Что такое распаковка кортежа?

tuple1=(1,2,3)
print(*tuple1)


#  Напишите лучший код для перестановки двух чисел местами.

a=12
b=13
temp=a
a=b
b=temp


print(a)
print(b)

a1=20
b1=30
c1=40
a1,b1,c1=c1,a1,b1
print(a1,b1,c1)

# 