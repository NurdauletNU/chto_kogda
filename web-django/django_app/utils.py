import datetime
import sqlite3
from django.core.cache import cache, caches

RamCache = caches['default']
DatabaseCache = caches['special']

def execute_sql(_query: str, is_many: bool = True, _source: str = "database.db"):
    with sqlite3.connect(f"database/{_source}") as connection:
        cursor = connection.cursor()
        cursor.execute(_query)
        connection.commit()
        if is_many:
            _rows = cursor.fetchall()
        _rows = cursor.fetchone()


class MyCache:

    default_lifetime = 5
    def __init__(self):
        self.store = {}

    def set(self, key: str, value):
        self.store[key] = {'value': value, 'datetime': datetime.datetime.now()}

    def get(self, key: str, is_bool: bool = True):
        if is_bool:
            val = self.store.get(key, None)
            print("val: ", val)
            if val is None:
                return None
            return val.get("value", None)
        return self.store[key]['value']


def get_cache(key: str, query:callable=lambda:any, timeout:int=10, cache:any=RamCache):
    data = cache.get(key)
    if data is None:
        data = query()
        cache.set(key, data, timeout)
    return data