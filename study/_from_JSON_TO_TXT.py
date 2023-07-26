# .json to .txt
import json
# 1 прочитать json
# todo открытие файла на чтение с помощью контекстного менеджера
with open("data2.json", mode="r", encoding="utf-8") as file:
    # todo конвертация json-файла в "питоновский" словарь (list[dict])
    dictinoaries=json.load(file)
    # load-десериализация (JSON -> Python Dict)




# 2 записать txt
# todo открытие txt-файла на запись контекстного менеджера
with open("data2.txt", mode="w", encoding="utf-8") as txt_file:
    for dictionary in dictinoaries:
        user_id = dictionary['userId']
        _id = dictionary['id']
        title = dictionary['title']
        completed = dictionary['completed']

        new_string = f"{user_id} | {_id} | {title} | {completed}\n"
        txt_file.write(new_string)

# todo COMPACT
# with open("data2.json", mode="r", encoding="utf-8") as json_file:
#     with("data2.txt", mode="w", encoding="utf-8") as txt_file
#         for dictionary in json.load(json.file):
#             txt_file.write(f"dictionary["userId]} | {dictionary["id"]} | {dictionary["title"]} | {dictionary["completed"]}\n")
