import sqlite3


def execute_sql(_query: str, is_many: bool = True, _source: str = "database.db"):
    with sqlite3.connect(f"database/{_source}") as connection:
        cursor = connection.cursor()
        cursor.execute(_query)
        connection.commit()
        if is_many:
            _rows = cursor.fetchall()
        _rows = cursor.fetchone()