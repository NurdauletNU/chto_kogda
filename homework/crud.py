import sqlite3

def create_table():
    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

def insert_user(name, age):
    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
        conn.commit()

def get_users():
    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT id, name, age FROM users''')
        rows = cursor.fetchall()
        return rows

def update_user_age(name, new_age):
    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''UPDATE users SET age = ? WHERE name = ?''', (new_age, name))
        conn.commit()

def delete_user(name):
    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM users WHERE name = ?''', (name,))
        conn.commit()


create_table()

insert_user('Alice', 25)
insert_user('Bob', 30)


users = get_users()
for user in users:
    print(user)


update_user_age('Alice', 35)


delete_user('Bob')

updated_users = get_users()
for user in updated_users:
    print(user)
