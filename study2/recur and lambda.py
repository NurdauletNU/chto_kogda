# Занятие за 16.08.23
# Todo анонимные функции (lambda функции)

l_summary= lambda a,b,c: a+b+c
print(l_summary(4,-5,2))


peoples=[{"name":"Nurdaulet", "age":29},
         {"name":"Zhibek", "age":25},
         {"name":"Rumia", "age":2}]

def by_age(d):
    return d["age"]

print(*sorted(peoples,key=by_age,reverse=False))
# тоже самое выдаст lambda-функция
print(*sorted(peoples,key=lambda d: d["age"],reverse=False))



peoples2=[
          [-4, True,6,2],
          (1,"Java",6,3),
          [0, 8, 2.2 ,1,5]
          ]
print(sorted(peoples2,key=lambda x: x[0],reverse=True))


# Todo рекурсивные функции (рекурсия)

def is_factorial(n):
    if n==0:
        return 1
    return n*is_factorial(n-1)

print(is_factorial(4))

def factorial_for(n):
    c=1
    for j in range(1,n+1):
        c*=j
    return c

print(factorial_for(4))




def rec_(num):
    if num==0:
        return 0
    return num+rec_(num-1)


print(f"rec_(4):", rec_(4))

# Todo функция filter
list1=[1,2,3,9,8,7,6,5,4,0]
print(list(filter(lambda x: x%2==0,list1)))


# Таймер с обратным отсчетом
import time
def countdown_timer(seconds):
    while seconds>0:
        hours_remaining=seconds//3600
        minutes_remaining=(seconds%3600)//60
        seconds_remaining=seconds%60
        time.sleep(0.0001)
        seconds-=1
        print(f"Осталось времени {hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}")

    print("Время вышло")


# Таймер вперед

def oclock(timer_forward):
    total_seconds=0
    while timer_forward>=total_seconds:
        hours_passed=timer_forward//3600
        minutes_passed=(timer_forward%3600)//60
        seconds_passed=timer_forward%60
        time.sleep(0.000001)
        total_seconds+=1
        print(f"Прошло времени {hours_passed:02d}:{minutes_passed:02d}:{seconds_passed:02d}")
    print("Время вышло")

oclock(380)