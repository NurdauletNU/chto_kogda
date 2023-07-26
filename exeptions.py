

try:
    print("Деньги сняты с вашего счета")

    print(1/0)

    print("Пополняется счет друга")
except ZeroDivisionError as error:
    print(error)

except Exception as error:
    print(error)
    print("Возврвт средств на мой счет")




a=7
b=0
try:
    print(a/b)

except Exception as error:
    print(error)
print()
print()
print()

q="w"
d="f"
try:
    print("Снятие денег с счета")
    print(q*10)
except Exception as error:
    print(error)
    print("Ошибка")
else:
    print("Перевод денег успешно завершен")
finally:
    print("Уведомление пользователя")

print()
print()
print()


try:
    def div2(a,b):
        if b==0:
            raise Exception
        result=a/b
        if result<0:
            raise ArithmeticError
        return result

    print(div2(2,-2))
except Exception as error:
    print(error)
    print("ERROR")









