# Инициализатор __init__ и финализатор __del__
import datetime


class Mother1:
    eyes="blue"

m1=Mother1()      # инициализация класса (создание экземпляра)
print("цвет глаз матери: ",m1.eyes)


class Child(Mother1):    # Наследование класса от Mother1
    age=7
    eyes = "green"        # override-переопределение-перезапись


c1=Child()
print("цвет глаз ребенка:", c1.eyes)

print("\n\n\n\n\n")
class Figure:
    name="Квадрат"                     # Переменная(атрибут) класса - доступна без создания экземпляра
    pi=3.1415
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2

        # self.perimetr=(side1+side2)*2

        # self.area=side1*side2
        self.name="Прямоугольник"      # Переменная(атрибут) экземпляр класса - доступна при создании экземпляра


             # ИНКАПСУЛЯЦИЯ
        self.description="ПУБЛИЧНАЯ"          # Public
        self._description="ЗАЩИЩЕННАЯ"        # Protected
        self.__description="ПРИВАТНАЯ"        # Private

        # perimetr
        # area
        pass

    def get_perimetr(self):
        return (self.side1+self.side2)*2

    def get_area(self):
        return self.side1*self.side2

    def get_are_with_multiply(self,multiply):
        return self.get_area()*multiply






f1=Figure(4,5)
# print("Фигура1: ",f1.perimetr)
print("Фигура1: ",f1.get_perimetr())
print("Фигура1: ",f1.get_area())
print("Фигура1: ",f1.get_are_with_multiply(15))
# print("Фигура1:", f1.area)
print("Фигура1:", f1.name)
print(Figure.name)
print(f1.description)
print(f1._description)                       # не желательно
print(f1._Figure__description)               # нельзя (Доступ к приватным данным)


# Наследование
# Полиформизм
# Инкапсуляция

print("\n\n\n\n\n")


# Создаем калькулятор


class Calc:
    def __init__(self,val1,val2,action):
        self.val1=val1
        self.val2=val2
        self.action=action

    def get_result(self,action=None):
        if action is not None:
            self.action=action
        match self.action:
            case"+":
                return self.val1+self.val2
            case "-":
                return self.val1-self.val2
            case "*":
                return self.val1*self.val2
            case _:
                raise Exception("Unknown action")

calc1=Calc(7,8,"/")
print(calc1.get_result("-"))
print("\n\n\n\n\n")

# Статический метод-это когда используется декоратор @staticmethod, а функции не принимают аргумент self

class Utils:
    class DateTimeC:

        @staticmethod
        def get_time():
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        @staticmethod
        def get_difference_time():
            return 0

        @staticmethod                  # Статический метод не имеет отношения к экземпляру
        def get_value(a):
            return a**0.5


print(Utils.DateTimeC.get_time())
print(Utils.DateTimeC.get_difference_time())
print(Utils.DateTimeC.get_value(9))
print("\n\n\n\n\n")

# Множественное наследование
# TODO множественное наследование

class Mother2:
    val1 = 12

    def __init__(self, val1, name="Мама") -> None:
        self.name = name
        self.val = val1
        self._val = val1        # защищённый
        self.__val2 = val1 + 5  # приватный

    def get_value(self):
        return 777

    def __str__(self):
        return self.name





class Father2:
    val2 = 13

    def __init__(self, val1) -> None:
        self.val1 = val1

    def get_value(self):
        return 888

    def __str__(self):
        return self.val1


class Child2(Father2, Mother2):

    def __init__(self, val1) -> None:
        super().__init__(val1)

    # def get_value(self):
    #     return 666


print(Mother2.val1)
a1 = Mother2(10)
print(a1.val)
# print(a1._Mother__val2)

ch1 = Child2(10)
print("\n\n")
print(ch1.get_value())
print("\n\n\n\n\n")


# TODO classmethod and staticmethod
from datetime import date

class Person:
    def __init__(self, name: str, age: int | float):
        self.name = name
        self.age = age

    @classmethod  # - помогает конструировать класс
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @classmethod
    def difference_of_year(cls,name,year):
        return cls(name,year/5)

    @staticmethod  # - не требует экземпляра для вызова
    def is_adult(age: int | float) -> bool:
        return age > 18


person1 = Person('Maya', 21)
person2 = Person.from_birth_year('Maya', 1996)
person3=Person.difference_of_year("Ricky",20)

print(person1.age)
print(person2.age)
print(person3.age)

print(Person.is_adult(22))