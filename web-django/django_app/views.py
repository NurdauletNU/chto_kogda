
"""
views - контроллеры(вью) - т.е. бизнес логика
"""


from django.shortcuts import render
from django_app import utils, models
import random

cache: utils.MyCache = utils.MyCache()



def home(request):
    key = 'home'
    data = cache.get(key)
    if data is None:
        data: str = f" Nurik {random.randint(1,10000)}"
        cache.set(key, data)
    # возврат HTML страницы
    return render(request, "home.html", context={"name": data})






def letter(request):
    if request.method == "GET":
        print("Привет")
        return render(request, "letter.html", context={})
    elif request.method == "POST":
        print("Request POST")
        print(request.POST)
        print(request.FILES)
        return render(request, "letter.html", context={})

    recipient = request.POST['email']
    message = request.POST['message']

    utils.execute_sql(_query="""
       CREATE TABLE IF NOT EXISTS item (
       id INTEGER PRIMARY KEY UNIQUE NOT NULL,
       recipient TEXT NOT NULL,
       message TEXT default 0;)""", is_many=True, _source="database.db")

    # todo ЧТЕНИЕ
    _users = utils.execute_sql(_query="""
           SELECT id, recipient, message FROM item; """, is_many=True, _source="database.db")

    # todo вставка
    _users = utils.execute_sql(is_many=False, _source="database.db", _query=f"""
        INSERT INTO item (recipient, message)
        VALUES (:recipient,:message);""")

    return render(request, "letter.html", context={})


def database():
    # todo СОЗДАНИЕ ТАБЛИЦЫ
    utils.execute_sql(_query="""
    CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    recipient TEXT NOT NULL,
    message TEXT default 0;)""", is_many=True, _source="database.db")

    # todo ЧТЕНИЕ
    _users = utils.execute_sql(_query="""
        SELECT id, recipient, message FROM item; """, is_many=True, _source="database.db")

    # todo вставка
    _users = utils.execute_sql(is_many=False, _source="database.db", _query=f"""
     INSERT INTO item (recipient, message)
     VALUES (:recipient,:message);""")

