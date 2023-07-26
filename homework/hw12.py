# Напишите программу, в которой есть главный класс с текстовым полем. В главное классе
# должен быть метод для присваивания значения полю: без аргументов и с одним текстовым
# аргументом. Объект главного класса создаётся передачей одного текстового аргумента
# конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно
# добавить числовое поле. У конструктора класса-потомка два аргумента


class MyClass:
    def __init__(self,text):
        self.text=text

    def set_text(self,text=None):
        if text is not None:
            self.text=text
        else:
            self.text="something1"

class ExtraClass(MyClass):
    def __init__(self,text,number):
        super().__init__(text)
        self.number=number
m1=MyClass("anything1")
print(m1.text)


e1=ExtraClass("anything2",25)
print(e1.text)
print(e1.number)

# Пересмотрите алгоритм решения прошлой практической работы, с использованием
# инкапсуляции. Реализуйте старый алгоритм с использованием полиморфизма.
# Напишите программу, в которой есть главный класс с текстовым полем. В главное
# классе должен быть метод для присваивания значения полю: без аргументов и с одним
# текстовым аргументом. Объект главного класса создаётся передачей одного текстового
# аргумента конструктору. На основе главного класса создается класса потомок.
# В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента


class MainClass:
    def __init__(self,speech):
        self._speech=speech

    def make_text(self,speech=None):
        if self._speech is not None:
            self._speech=speech
        else:
            self._speech="something2"

class SubClass(MainClass):
    def __init__(self,speech,num):
        super().__init__(speech)
        self._num=num

m2=MainClass("Hello bro")
print(m2._speech)

s2=SubClass("Hi bro", 14)
print(s2._num)
print(s2._speech)



# Создайте класс Roman (РимскоеЧисло), представляющий римское число и
# поддерживающий операции +, -, *, /.
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы
# методы преобразования как статические методы

class Roman:
    def __init__(self, value):
        self.value = self.from_roman(value)

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self.to_roman(self.value + other.value)
            return Roman(result)
        elif isinstance(other, int):
            result = self.to_roman(self.value + other)
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.to_roman(self.value - other.value)
            return Roman(result)
        elif isinstance(other, int):
            result = self.to_roman(self.value - other)
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self.to_roman(self.value * other.value)
            return Roman(result)
        elif isinstance(other, int):
            result = self.to_roman(self.value * other)
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.to_roman(self.value // other.value)
            return Roman(result)
        elif isinstance(other, int):
            result = self.to_roman(self.value // other)
            return Roman(result)
        else:
            raise TypeError("Unsupported operand type for /")

    @staticmethod
    def to_roman(number):
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        roman = ""
        for value, symbol in roman_map:
            while number >= value:
                roman += symbol
                number -= value
        return roman

    @staticmethod
    def from_roman(roman):
        roman_map = {
            "M": 1000, "D": 500, "C": 100, "L": 50,
            "X": 10, "V": 5, "I": 1
        }
        number = 0
        prev_value = 0
        for numeral in reversed(roman):
            value = roman_map.get(numeral, 0)
            if value >= prev_value:
                number += value
            else:
                number -= value
            prev_value = value
        return number



roman1 = Roman("XV")
roman2 = Roman("III")
print(roman1.value+roman2.value)
print(roman1.value-roman2.value)
print(roman1.value*roman2.value)
print(roman1.value/roman2.value)



