# Todo list comprehension

print(*[i**2 for i in [1,2,3,4,5,6] if i%2==0])

list5=[101,201,301,401,501]
list6=[]
for i in list5:
    if i%2!=0:
        result={f"{str(i)[0]}": i}
        list6.append(result)
print(*list6)


print(*[{str(i)[0]:i} for i in list5])



# Todo tuple comprehension
tuple2 = (i ** 2 for i in [1,2,3,4,5])
print(tuple2, type(tuple2))  # <generator object <genexpr> at 0x000001D56B2B8040> <class 'generator'>
for i in tuple2:
    print(i)
print("\n\n\n\n\n\n")



# Todo list функция yield-в Python используется для создания генераторов.
#  Генераторы - это специальный тип итерируемых объектов,
#  которые генерируют значения по мере необходимости, вместо того чтобы хранить все значения в памяти.
#  Это позволяет эффективно обрабатывать большие объемы данных или бесконечные последовательности.

def generator_numbers():
    for i in range(10):
        yield i

num=generator_numbers()
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print("\n\n\n\n\n\n")




# todo dict comprehension


# пример для генерации словаря из массива
list5 = [101, 201, 301, 401, 501]
dict6={}
for i in list5:
    dict6[str(i)[0]]=i
#print(dict6)


dict6={str(i)[0]:i for i in list5}
print(dict6)
print("\n\n\n\n\n\n")


# # новый словарь из пар значений

list10= [["key_1", 1], ["key_2", 2], ["key_3", 3]]
dict1={}
for k,v in list10:
    dict1[k]=v
#print(dict1)
print({k:v for k,v in list10})

