def decorator_triangle_root(f):
    def wrapper(*args,**kwargs):
        print(type(args), args)              # <class 'tuple'> (7, 1)
        print(type(kwargs),kwargs)           # <class 'dict'> {'b': 1}
        r=f(*args,**kwargs)
        return r**(1/3)+1
    return wrapper

@decorator_triangle_root
def sum(a,b):
    return a+b

res=sum(a=7,b=1)
# print(res)



def convert_to_float(function):
    def wrapper(*args,**kwargs):
        try:
            res=float(function(*args,**kwargs))
            return res
        except Exception as error:
            print(error)
            raise error
    return wrapper




@convert_to_float
def sum1(a,b=1):
    return a+b


f=sum1(2)
# print(f)


# наслоение декораторов


def twice(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res*2
    return wrapper


def rounding(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return round(res,1)
    return wrapper

@twice
@rounding
def val(a,b):
    return a*b


q=val(7.1, 3.25)
# print(q)

# Todo *args & **kwargs
# *args - позиционный аргумент(tuple-кортеж)
# **kwargs- именнованные аргументы(dict-словарь)


dict1={"name":"Nurik", "age":30}
print(*dict1)  # когда * (одна звездочка) распакуется только ключи



def ex1(age,name):
    print("name", name)
    print("age",age)
ex1(**dict1)


def res2():
    return 2,25,30

c,d,e=res2()            #  autounpacking
print(c,d,e)

