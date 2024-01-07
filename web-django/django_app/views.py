"""
views - контроллеры(вью) - т.е. бизнес логика
"""
from urllib import request

from django.shortcuts import render
from django_app import utils, models
import random

cache: utils.MyCache = utils.MyCache()


def home(request):
    key = 'home'
    data = cache.get(key)
    if data is None:
        data: str = f" Nurik {random.randint(1, 10000)}"
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


def book(request):
    books = [
        {
            'id': 1,
            'title': 'Война и мир',
            'author': 'Лев Толстой',
            'price': 1000,
            'quantity': 20
        },
        {
            'id': 2,
            'title': 'Преступление и наказание',
            'author': 'Фёдор Достоевский',
            'price': 800,
            'quantity': 15
        },
        {
            'id': 3,
            'title': 'Гарри Поттер',
            'author': 'Джоан Роулинг',
            'price': 1200,
            'quantity': 25
        },
        {
            'id': 4,
            'title': 'Улисс',
            'author': 'Джеймс Джойс',
            'price': 900,
            'quantity': 18
        },
        {
            'id': 5,
            'title': '1984',
            'author': 'Джордж Оруэлл',
            'price': 950,
            'quantity': 20
        },
        {
            'id': 6,
            'title': 'Великий Гэтсби',
            'author': 'Фрэнсис Скотт Фицджеральд',
            'price': 1000,
            'quantity': 17
        },
        {
            'id': 7,
            'title': 'Мастер и Маргарита',
            'author': 'Михаил Булгаков',
            'price': 1050,
            'quantity': 17
        },
        {
            'id': 8,
            'title': 'Тысяча сияющих солнц',
            'author': 'Халед Хоссейни',
            'price': 1250,
            'quantity': 23
        },
        {
            'id': 9,
            'title': 'Тихий Дон',
            'author': 'Михаил Шолохов',
            'price': 850,
            'quantity': 14
        },
        {
            'id': 10,
            'title': 'Триумфальная арка',
            'author': 'Эрих Мария Ремарк',
            'price': 950,
            'quantity': 19
        },
        {
            'id': 11,
            'title': 'Маленький принц',
            'author': 'Антуан де Сент-Экзюпери',
            'price': 920,
            'quantity': 28
        },
        {
            'id': 12,
            'title': 'Лолита',
            'author': 'Владимир Набоков',
            'price': 1100,
            'quantity': 16
        },
        {
            'id': 13,
            'title': 'Бойцовский клуб',
            'author': 'Чак Паланик',
            'price': 980,
            'quantity': 20
        },
        {
            'id': 14,
            'title': 'Мастер с маргаритками',
            'author': 'Эрнест Хемингуэй',
            'price': 1050,
            'quantity': 15
        },
        {
            'id': 15,
            'title': 'О дивный новый мир',
            'author': 'Олдос Хаксли',
            'price': 1150,
            'quantity': 22
        },
        {
            'id': 16,
            'title': 'Тень горы',
            'author': 'Карлос Руис Сафон',
            'price': 980,
            'quantity': 17
        },
        {
            'id': 17,
            'title': 'Крестный отец',
            'author': 'Марио Пьюзо',
            'price': 900,
            'quantity': 19
        },
        {
            'id': 18,
            'title': 'Алиса в Стране чудес',
            'author': 'Льюис Кэрролл',
            'price': 850,
            'quantity': 25
        },
        {
            'id': 19,
            'title': 'Фауст',
            'author': 'Иоганн Вольфганг фон Гёте',
            'price': 990,
            'quantity': 18
        },
        {
            'id': 20,
            'title': 'Игра престолов',
            'author': 'Джордж Р. Р. Мартин',
            'price': 1200,
            'quantity': 15
        },
        {
            'id': 21,
            'title': 'Поток сознания',
            'author': 'Михаил Булгаков',
            'price': 1000,
            'quantity': 17
        },
        {
            'id': 22,
            'title': 'Франкенштейн',
            'author': 'Мэри Шелли',
            'price': 950,
            'quantity': 20
        },
        {
            'id': 23,
            'title': 'Дубровский',
            'author': 'Александр Пушкин',
            'price': 890,
            'quantity': 16
        },
        {
            'id': 24,
            'title': 'Маленькие женщины',
            'author': 'Луиза Мэй Олкотт',
            'price': 1100,
            'quantity': 22
        },
        {
            'id': 25,
            'title': 'Мартин Иден',
            'author': 'Джек Лондон',
            'price': 1050,
            'quantity': 19
        },
        {
            'id': 26,
            'title': 'Каменный уголь',
            'author': 'Кен Кизи',
            'price': 990,
            'quantity': 25
        },
        {
            'id': 27,
            'title': 'Мачо и ботан',
            'author': 'Джон Грин',
            'price': 930,
            'quantity': 23
        },
        {
            'id': 28,
            'title': 'Мачо и ботан',
            'author': 'Джон Грин',
            'price': 930,
            'quantity': 23
        },
        {
            'id': 29,
            'title': 'Чайка',
            'author': 'Антон Чехов',
            'price': 920,
            'quantity': 21
        },
        {
            'id': 30,
            'title': 'Молокососы',
            'author': 'Джером Д. Сэлинджер',
            'price': 1000,
            'quantity': 20
        },
        {
            'id': 31,
            'title': 'Одиссея',
            'author': 'Гомер',
            'price': 980,
            'quantity': 16
        },
        {
            'id': 32,
            'title': 'Чайка по имени Джонатан Ливингстон',
            'author': 'Ричард Бах',
            'price': 890,
            'quantity': 18
        },
        {
            'id': 33,
            'title': 'Приключения Шерлока Холмса',
            'author': 'Артур Конан Дойл',
            'price': 1100,
            'quantity': 15
        },
        {
            'id': 34,
            'title': 'Бессмертный',
            'author': 'Лайон Фейхтвангер',
            'price': 970,
            'quantity': 19
        },
        {
            'id': 35,
            'title': 'Поле брани',
            'author': 'Михаил Шолохов',
            'price': 950,
            'quantity': 18
        },
        {
            'id': 36,
            'title': 'Приключения Шерлока Холмса',
            'author': 'Артур Конан Дойл',
            'price': 1100,
            'quantity': 15
        },
        {
            'id': 37,
            'title': 'Бессмертный',
            'author': 'Лайон Фейхтвангер',
            'price': 970,
            'quantity': 19
        },
        {
            'id': 38,
            'title': 'Поле брани',
            'author': 'Михаил Шолохов',
            'price': 950,
            'quantity': 18
        },
        {
            'id': 39,
            'title': 'Мартин Иден',
            'author': 'Джек Лондон',
            'price': 1050,
            'quantity': 19
        },
        {
            'id': 40,
            'title': 'Каменный уголь',
            'author': 'Кен Кизи',
            'price': 990,
            'quantity': 25
        },
        {
            'id': 41,
            'title': 'Мачо и ботан',
            'author': 'Джон Грин',
            'price': 930,
            'quantity': 23
        },
        {
            'id': 42,
            'title': 'Чайка',
            'author': 'Антон Чехов',
            'price': 920,
            'quantity': 21
        },
        {
            'id': 43,
            'title': 'Молокососы',
            'author': 'Джером Д. Сэлинджер',
            'price': 1000,
            'quantity': 20
        },
        {
            'id': 44,
            'title': 'Одиссея',
            'author': 'Гомер',
            'price': 980,
            'quantity': 16
        },
        {
            'id': 45,
            'title': 'Чайка по имени Джонатан Ливингстон',
            'author': 'Ричард Бах',
            'price': 890,
            'quantity': 18
        },
        {
            'id': 46,
            'title': 'Приключения Шерлока Холмса',
            'author': 'Артур Конан Дойл',
            'price': 1100,
            'quantity': 15
        },
        {
            'id': 47,
            'title': 'Бессмертный',
            'author': 'Лайон Фейхтвангер',
            'price': 970,
            'quantity': 19
        },
        {
            'id': 48,
            'title': 'Поле брани',
            'author': 'Михаил Шолохов',
            'price': 950,
            'quantity': 18
        }, ]

    def get_date():
        return models.Book.objects.all()

    books = utils.get_cache("book", lambda: get_date, timeout=20)

    return render(request, 'book.html', context={'books': books})
