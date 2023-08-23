try:
    print("Начало операции")
    print(1)

except Exception as error:
    print(error)
    print("ОШИБКА")

else:
    print("Операция завершилась успешно!")

finally:
    print("Конец")


try:
    def div(a,b):
        if b==0:
            raise ZeroDivisionError   # вызов исключения
        result=a/b
        if result<0:
            raise ArithmeticError     # вызов исключения
        return result
except Exception as error:            # перехват исключения
    print(error)

print(div(4,4))



