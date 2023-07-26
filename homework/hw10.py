



import sqlite3

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [line.strip().split(',') for line in data]

def write_data_to_database(data, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER
                    )''')
    cursor.executemany('INSERT INTO my_table VALUES (?,?,?)', data)
    conn.commit()
    conn.close()

def read_data_from_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    data = cursor.fetchall()
    conn.close()
    return data

def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        for row in data:
            file.write(','.join(str(cell) for cell in row) + '\n')


file_data = read_data_from_file('input.txt')
write_data_to_database(file_data, 'my_database.db')

database_data = read_data_from_database('my_database.db')
write_data_to_file(database_data, 'output.txt')
