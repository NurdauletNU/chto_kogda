#	Подготовить топ 20 вопросов по Python.


#1.Как создавать собственные исключения (custom exceptions) в Python?
#2.Что такое классы (classes) и объекты (objects) в Python?
#3.Как создать класс и методы в Python?
#4.Что такое наследование (inheritance) и полиморфизм (polymorphism) в Python?
#5.Как работает инкапсуляция (encapsulation) в Python?
#6.Как открывать, записывать и закрывать файлы в Python?
#7.Как читать и записывать данные в текстовые и бинарные файлы?
#8.Что такое контекстный менеджер (context manager) в Python, и как его использовать?
#9.Как работать со строками (strings) в Python (конкатенация, форматирование и др.)?
#10.Что такое регулярные выражения (regular expressions), и как их использовать в Python?
#11.Управление памятью и сборка мусора
#12.Как управляется память в Python?
#13.Что такое сборка мусора (garbage collection) в Python, и как она работает?
#14.Что такое виртуальное окружение (virtual environment), и зачем оно нужно?
#15.Как создавать и активировать виртуальное окружение в Python?
#16.Как устанавливать сторонние библиотеки (packages) с помощью pip?
#17.Что такое файл requirements.txt, и как им управлять?
#18.Что такое многозадачность (concurrency) и параллелизм (parallelism) в Python?
#19.Как создавать и управлять потоками (threads) и процессами (processes) в Python?
#20.Какие фреймворки (например, Flask и Django) используются для веб-разработки в Python?


#	Изучить пример всех функций в библиотеке functols.


from functools import partial,reduce,lru_cache,wraps
#functools.partial(func, *args, **keywords)
def add(x, y):
    return x + y

add_five = partial(add, 5)
result = add_five(3)
print(result)



# functools.reduce(function, iterable[, initializer])
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)




# functools.lru_cache(maxsize=128, typed=False)
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(12))





#functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Реализация декоратора
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    """Это документация функции say_hello."""
    print(f"Привет, {name}!")

say_hello("Alice")