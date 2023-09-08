# Скачать и установить базу данных, подключить psycopg2 и
# сделать несколько запросов на чтение и запись в базу данных
import psycopg2

connection=psycopg2.connect(
    user="postgres",
    password="Manchester7",
    host="127.0.0.1",
    port="5432",
    dbname="car_market"
)

# connection.autocommit=False


cursor=connection.cursor()
def select():

    query="""SELECT * FROM "Cars" """
    cursor.execute(query)
    rows=cursor.fetchall()
    print(rows)

select()



# Создание таблицы данных

query1="""CREATE TABLE public."Cars"
(
    "Id" serial NOT NULL,
    make character varying(255),
    model character varying(255),
    year integer,
    color character varying(255),
    price double precision NOT NULL,
    quantity integer,
    PRIMARY KEY ("Id")
);

ALTER TABLE IF EXISTS public."Cars"
    OWNER to postgres; """




# Вставлять в таблицу данных
def insert_to_table():
    query2="""INSERT INTO "Cars" (make, model, year, color, price,quantity)
              VALUES ('BMW', 'BMW X6', 2021, 'White', 65000000, 1)   """
    cursor.execute(query2)
    connection.commit()

#insert_to_table()

# Удалять из таблицы данных
def delete_from_table():
    query3="""DELETE FROM "Cars" 
              WHERE quantity<2018"""
    cursor.execute(query3)
    connection.commit()

#delete_from_table()



