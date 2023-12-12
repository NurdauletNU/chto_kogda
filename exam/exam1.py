# 1  В чем разница между списком и кортежем?
import sys

a=[1,2,3]
b=(1,2,3)
print(sys.getsizeof(a))
print(sys.getsizeof(b))

# 2  Как развернуть список
list1=[1,2,3,4,5,6]
# list1.reverse()
print(list(reversed(list1)))

print(list1[::-1])
reverse_list=[]
for i in range(len(list1)-1,-1,-1):
    reverse_list.append(list1[i])
print(reverse_list)

# Округление

float1=2.567
print(round(float1,2))


print(ord("a"))
print(ord("A"))

hh="154a"
ff=""
for i in hh:
    if i.isdigit():
        ff+=i
print(int(ff))



# Что такое DOCSTRING

def func():
    """Docstring"""

print(func.__doc__)

print(7%2)


# Как получить доступ к значениям словаря
dict1={1:"1",2:[True, False, None], 3:"Three"}
print(dict1.get(4, "Undefined"))
print(dict1[2])

import os
print(os.getcwd())

import time

# Что такое декоратор

def time_measuring(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        finish=time.time()
        execution_time=finish-start
        print(execution_time)
        return res
    return wrapper


@time_measuring
def add(a,b):
    time.sleep(1)
    return a+b

print(add(2,3))


a=(i for i in [1,2,3])
print(next(a))
print(next(a))


def is_palindrome(a):
    if a.lower()==a.lower()[::-1]:
        print("Это палиндром")
    else:
        print("Это не палиндром")


is_palindrome("оНО")


def palindrome(a):
    if len(a)<=1:
        return True
    if a[0]==a[-1]:
        return palindrome(a[1:-1])
    return False

# palindrome("мадам")
a="мадам"
print(a[1:-1])


def factrial(n):
    if n==0:
        return 1
    return n*factrial(n-1)
print(factrial(5))