# Реализовать бота для регистрации авиабилетов (список доступных билетов в базе данных).
import sqlite3
from aiogram import Bot, Dispatcher, executor, types


bot_instanse = Bot(token="6147855904:AAFlpBOv7-TMNEx04NxmQ8QAc2mBgYcVLWI")
bot= Dispatcher(bot_instanse)

class DataBase:

    @staticmethod
    def execcute_query_to_sqlite(query,args=(),many=True):
        with sqlite3.connect("database.db") as connection:
            cursor=connection.cursor()
            cursor.execute(query,args)
            if many:
                return cursor.fetchall()
            return cursor.fetchone()



    @staticmethod
    def create_data_table():
        DataBase.execcute_query_to_sqlite(query="""
        CREATE TABLE IF NOT EXIST tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        departure TEXT,
        destination TEXT,
        departure_date TEXT,
        departure_time TEXT,
        price REAL,
        available_seats INTEGER)""")




    @staticmethod
    def get_tickets(pk:int):
        data=DataBase.execcute_query_to_sqlite(query="""
        SELECT id,departure,destination,departure_date,departure_time,price,available_seats FROM tickets WHERE id==?""", args=(pk,))
        return data

    @staticmethod
    def insert_tickets(departure,destination,departure_date,departure_time,price,available_seats):
        DataBase.execcute_query_to_sqlite(query="""
        INSERT INTO tickets (departure,destination,departure_date,departure_time,price,available_seats)
        VALUES (?,?,?,?,?,?)""", args=(departure,destination,departure_date,departure_time,price,available_seats))
        if available_seats==0:
            raise Exception ("Нет доступных мест")


@bot.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать! Для регистрации авиабилета используйте команду /register.")

# @bot.message_handler()
# async def echo(message: types.Message):
#    await message.answer(str(message.text)[::-1])


@bot.message_handler(commands=["register"])
async def make_register(message:types.Message):
    tickets=DataBase.get_tickets(pk=3)
    buttons=[]
    for ticket in tickets:
        button = types.InlineKeyboardButton(
            text=f"#{ticket[2]} {ticket[5]} [{ticket[6]}] ",
            callback_data=f"get_ticket|{ticket[0]}",
        )
        buttons.append(button)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.reply("Выберите пункт назначения ",reply_markup=keyboard)

@bot.callback_query_handler(lambda callback_query:True)
async def handle_button_click(callback_query: types.CallbackQuery):
    query_data=callback_query.data.split("|")[0]
    if query_data=="get_ticket":
        args=callback_query.data.split("|")[1:]
        pk=int(args[0])
        print(args)
        print(DataBase.get_tickets(pk))
        await callback_query.answer(text="Button clicked")
    else:
        pass

    print(callback_query)





# executor.start_polling(bot, skip_updates=True)
# DataBase.create_data_table()
if __name__=="__main__":

    executor.start_polling(bot,skip_updates=True)

    # DataBase.insert_tickets(departure="Алматы", destination="Баку", departure_date="28.08.23", departure_time="01:40", price=50000, available_seats=50)
    # DataBase.insert_tickets(departure="Караганда", destination="Минск", departure_date="17.08.23", departure_time="13:45", price=80000, available_seats=85)
    # DataBase.insert_tickets(departure="Алматы", destination="Москва", departure_date="10.08.23", departure_time="14:05", price="52000",available_seats=15)
    # DataBase.insert_tickets(departure="Алматы",destination="Бишкек", departure_date="19.07.23",departure_time="11:44",price="40000", available_seats=33)
    # print(DataBase.get_tickets(2))

