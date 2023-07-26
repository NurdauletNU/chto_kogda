class Mother:
    eyes="blue"

m1=Mother()



class Child(Mother):
    age=15
    eyes = "green"

c1=Child()
print(c1.eyes)



class Figure:
    name="Квадрат"
    def __init__(self,side1,side2):
        self.name="Прямоугольник"
        self.side1=side1
        self.side2=side2
        self.perimetr=(side2+side1)*2
        self.area=side1*side2


    def get_perimetr(self):
        return self.side2-self.side1



f1=Figure(10,15)
print("Периметр:", f1.perimetr)
print("Площадь:", f1.area)
print(f1.name)
print(Figure.name)
print(f1.get_perimetr())
