import json

# txt
#txt_file=open("data1.txt", mode="r", encoding="utf-8")         # r w a rb wb
#print(txt_file.readlines()[2])                                 # массив с строками
# print(txt_file.readline())                                    # редко пользуется
#txt_file.close()



# todo TXT-файл
with open("data1.txt", mode="r",encoding="utf-8") as file:
    # todo Контекстный менеджер "with" обязательно закрывает файл в любых случаях
    print(file.readlines())


print(123)
print()
print()





# todo JSON-файл
# читать
with open("new.json", mode="r", encoding="utf-8") as file:
    data=json.load(file)
    # load-десериализация (JSON -> Python Dict)
    print(data)
    print(type(data))


# запись
with open("data.json", mode="w", encoding="utf-8") as file:
    dict1 = {"Mansur": 4.9, "Meiram": 4.8}
    print(type(dict1))

    json.dump(dict1,file)
    # dump - сериализация (Python Dict-> JSON)
