class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"


    @staticmethod
    def agregate(num):
        return num*2

    def totol(self):
        return 1.1*self.age


person1 = Person("Alice", 30)
print(str(person1))  # Вывод: Person: Alice, Age: 30
print(person1.totol())
print(Person.agregate(7))

