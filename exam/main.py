# Интерполяция строк
str1="Carl"
int1=30
print(f"Hi! My name is {str1}. I`am {int1} years old")


# Объединение список
list1=[1,2,3,4,5]
list2=[6,7,8,9]
list1.extend(list2)
print(list1)


# Проверить что в строке толька числа

def is_digit(str2):
    if str2.isdigit():
        return "Числа"
    else:
        return "Не только числы"

print(is_digit("14f"))



# Какие циклы есть в питон и чем они отличаются
for i in range(5):
    print(i)

j=0
while j<=5:
    print(j)
    j+=1


# Что делает метод split() и join()
str3="Привет! Как дела?"
print(str3.split("!"))
list3=["Яблоко", "Банан", "Виноград"]
print(",".join(list3))


# узнать версию питона python -V


# узнать длину строки
str4="Виноград"
print(len(str4))


# Преобразуйте цикл for в генератор (list comprehension)
list4=[i**2 for i in range(5)]
print(list4)


# функция yield
def generator_numbers(n):
    for _ in range(n):
        yield _

count=generator_numbers(5)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))


# Логические операторы в питоне AND OR NOT

# Разница между func и func() в Python заключается в том,
# что func - это сама функция, а func() - это вызов (выполнение) этой функции.


# какая разница между словарями и JSON
#Словари - это встроенная структура данных в Python, которая использует фигурные скобки {} для определения пар "ключ: значение".
#JSON - это текстовый формат, который использует фигурные скобки {} для определения объектов и квадратные скобки [] для определения массивов.


import json

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Сериализация словаря в JSON
json_data = json.dumps(person)
# Десериализация JSON в словарь
person_copy = json.loads(json_data)


# в чем разница между remove del pop

# remove удаляет элемент по значению
# del удаляет элемент по индексу
fruits = ['яблоко', 'банан', 'апельсин']
del fruits[1]  # Удаление элемента с индексом 1 ('банан')
print(fruits)  # ['яблоко', 'апельсин']


#где быстрее поиск в словарях или в списках


# В словарях (dict) поиск элемента выполняется значительно быстрее, чем в списках (list).
# Эффективность поиска в словарях обеспечивается хэшированием ключей, что позволяет быстро найти соответствующее значение.
# Время выполнения операции поиска в словаре в среднем O(1), то есть почти константное время.


# В списках (list) время поиска зависит от количества элементов в списке.
# В худшем случае (когда элемент находится в конце списка или отсутствует), время поиска может быть O(n),
# где n - это количество элементов в списке.





# что такое GIL
# GIL, или Global Interpreter Lock, - это механизм, используемый в интерпретаторе CPython (стандартная реализация Python) для управления одновременным доступом к объектам внутри Python. GIL представляет собой блокировку, которая позволяет только одному потоку Python выполняться в любой момент времени, даже на многозадачных многоядерных процессорах.
#
# Основные характеристики GIL:
#
# Ограничение на однопоточное выполнение: GIL гарантирует, что только один поток Python может выполняться в данный момент. Даже если ваш компьютер имеет несколько ядер процессора, Python может использовать только одно ядро одновременно.
#
# Избегание гонок за ресурсы: GIL предотвращает гонки за ресурсы, так как разделяемые объекты в Python, такие как списки и словари, могут использоваться только одним потоком одновременно.
#
# Ограничение многозадачности: GIL может ограничивать эффективность параллельной обработки в Python для некоторых видов задач. Это может сказаться на производительности многозадачных приложений.
#
# Важно отметить, что GIL спроектирован таким образом, чтобы облегчить работу с Python на многозадачных системах и обеспечить безопасность работы с разделяемыми данными. Однако это также ограничивает способность Python использовать полностью многозадачные вычисления на многозадачных процессорах.
#
# GIL не является проблемой для всех видов задач и приложений, но для определенных задач, таких как интенсивные вычисления или параллельная обработка, разработчики Python могут использовать альтернативные реализации Python, такие как Jython, IronPython или PyPy, которые не используют GIL, чтобы достичь лучшей многозадачности.




# Множественное наследование




class Parent1:
    eye="blue"

    def method(self):
        print("Method of Parent1")


class Parent2:
    eye="black"

class Child(Parent1,Parent2):
    height=185

child=Child()
print(child.eye)
child.method()



#if __name__ == "__main__":




class MyClass:
    def __new__(cls, *args, **kwargs):
        instance = super(MyClass, cls).__new__(cls)
        instance.attribute = "Новый атрибут"
        return instance

obj = MyClass()
print(obj.attribute)  # "Новый атрибут"

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(obj.value)  # 42


class Triangle:
    pi=3.14
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3

    @staticmethod
    def sqrt(value1, value2):
        return value1*value2

    @classmethod
    def sqrt2(cls,r):
        return cls.pi*(r**2)

res=Triangle.sqrt(4,5)
print(res)
r=Triangle.sqrt2(5)
print(r)


def my_decorator(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res**0.25 if res>0 else "Число меньше нуля"
    return wrapper

@my_decorator
def add(x,y):
    return x+y


add1=lambda x,y:x+y
itogo=add1(3,5)


dict1=[
       {"name":"Nurik","age":29,"IQ":100},
       {"name":"Zhibek","age":25,"IQ":111},
       {"name":"Rumia","age":2,"IQ":101}
       ]
d=sorted(dict1,key=lambda di:di["IQ"], reverse=False)




if __name__=="__main__":
    print(d)
    #print(itogo)
    # print(add(-7,11))



