import datetime


def is_recursia(n):
    if n==0:
        return 1
    return n*is_recursia(n-1)

#print(is_recursia(7))


class Mother1:
    eyes="blue"   # атрибут класса

class Child(Mother1):
    eyes = "black"
    height=1.85



    def jump(self):                # метод (функция внутри класса называется методом)
        return "My name is Joe"




m1=Mother1()      # инициализация экземпляра класса
c1=Child()


print(m1.eyes)
print(c1.eyes)
print(c1.height)
print(c1.jump())



class Figure:
    circle=10

    @staticmethod                # статический метод не имеет никакого отношения самому классу
    def square(r):
        return 3.14*(r**2)


    def square_1(self):            # динамический метод всегла имеет ссылку на себя
        return self.circle**2


    def perimetr(self,width):
        return width*self.circle


print(Figure.square(10))
f1=Figure()
print(f1.square_1())
print(f1.perimetr(7))



class Utils:
    class DateTime:

        @staticmethod
        def get_year():
            return datetime.datetime.now().strftime("%Y")

print(Utils.DateTime.get_year())