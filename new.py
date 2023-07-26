# Условный оператор
a1,b1,c1=map(int,input().split())
if c1>a1+b1:
    print("Да")
else:
    print("Нет")

print()
print()



# Тернарный оператор
a2,b2,c2=map(int,input().split())
print("Да" if c2>a2+b2 else "Нет")
print()
print()





# Функция (грязный код)


def count(a,b,c):
    print("Да" if c>a+b else "Нет")


count(*map(int,input().split()))


print()
print()




# Функция (Чистый код)
def count(a,b,c):
    return "Да" if c>a+b else "Нет"



print(count(*map(int,input().split())))