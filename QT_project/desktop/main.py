import threading
import time
import datetime
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
import sys
import sqlite3
import requests


class Utils:
    @staticmethod
    def sql_execute(_query: str, _kwargs: dict, _source: str):
        try:
            _connection = sqlite3.connect(f"src/database/{_source}")
            _cursor = _connection.cursor()
            _cursor.execute(_query, _kwargs)
            _connection.commit()
            _data = _cursor.fetchall()
            _cursor.close()
            _connection.close()
            return _data
        except Exception as error:
            print(error)


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("src/main.ui", self)
        # self.ui.labelData.setText("Searching...")
        self.__params = {}
        self.ui.pushButton_temp_plan_plus.clicked.connect(self.push_button_temp_plan_plus)
        self.ui.pushButton_temp_plan_minus.clicked.connect(self.push_button_temp_plan_minus)

        self.show()
        # self.get_local_settings()
        threading.Thread(target=self.loop, args=()).start()

    def push_button_temp_plan_plus(self):
        print(f"{datetime.datetime.now()} start pushButton_temp_plan_plus ")

        # todo записываем в базу
        Utils.sql_execute(
            _query="""
           CREATE TABLE IF NOT EXISTS params (
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           key TEXT UNIQUE NOT NULL,
           value TEXT NOT NULL DEFAULT ''
                               );""",
            _kwargs={},
            _source="local_settings.db",
        )

        # todo берем старые
        _rows = Utils.sql_execute(
            _query="""
        SELECT key, value 
        FROM params;""",
            _kwargs={},
            _source="local_settings.db",
        )
        # print(_rows, type(_rows))
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        # _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        # print(_dict, type(_dict))
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]
        # print(_params, type(_params))

        # todo конвертируем и изменяем
        _temp_plan_high = int(_params.get("temp_plan_high", -7)) + 1
        _temp_plan_down = int(_params.get("temp_plan_down", -15)) + 1
        _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}


        # todo записываем в базу
        _connection = sqlite3.connect(f"src/database/local_settings.db")
        _cursor = _connection.cursor()

        try:
            with _connection:
                for k, v in _data.items():
                    _cursor.execute(
                        """
                        INSERT OR REPLACE INTO params (key, value) VALUES (:key, :value);
                        """,
                        {'key': k, 'value': v}
                    )

        except sqlite3.IntegrityError:

            print("Error: IntegrityError .")
            _connection.rollback()

        finally:
            _cursor.close()
            _connection.close()



    def push_button_temp_plan_minus(self):
        print(f"{datetime.datetime.now()} start pushButton_temp_plan_minus ")
        # todo записываем в базу
        Utils.sql_execute(
            _query="""
                  CREATE TABLE IF NOT EXISTS params (
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  key TEXT UNIQUE NOT NULL,
                  value TEXT NOT NULL DEFAULT ''
                                      );""",
            _kwargs={},
            _source="local_settings.db",
        )

        # todo берем старые
        _rows = Utils.sql_execute(
            _query="""
               SELECT key, value 
               FROM params;""",
            _kwargs={},
            _source="local_settings.db",
        )
        # print(_rows, type(_rows))
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        # _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        # print(_dict, type(_dict))
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]
        # print(_params, type(_params))

        # todo конвертируем и изменяем
        _temp_plan_high = int(_params.get("temp_plan_high", -7)) - 1
        _temp_plan_down = int(_params.get("temp_plan_down", -15)) - 1
        _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}

        # todo записываем в базу
        _connection = sqlite3.connect(f"src/database/local_settings.db")
        _cursor = _connection.cursor()

        try:
            with _connection:
                for k, v in _data.items():
                    _cursor.execute(
                        """
                        INSERT OR REPLACE INTO params (key, value) VALUES (:key, :value);
                        """,
                        {'key': k, 'value': v}
                    )

        except sqlite3.IntegrityError:

            print("Error: IntegrityError .")
            _connection.rollback()

        finally:
            _cursor.close()
            _connection.close()

    def get_local_settings(self):

        # print(f"{datetime.datetime.now()} start get_local_settings:")
        """
        # todo 1. Берем настройки с локальной БД
        # todo 2. Установка настройки в интерфейс
        """

        # todo 1. Берем настройки с локальной БД
        Utils.sql_execute(
            _query="""
        CREATE TABLE IF NOT EXISTS params (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     key TEXT  NOT NULL,
                     value TEXT NOT NULL DEFAULT '' 
        );""",
            _kwargs={},
            _source="local_settings.db",
        )
        _rows = Utils.sql_execute(
            _query="""
SELECT key, value 
FROM params;""",
            _kwargs={},
            _source="local_settings.db",
        )
        # print(_rows, type(_rows))
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        # _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        # print(_dict, type(_dict))
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]
        # print(_params, type(_params))

        # todo 2. Установка настройки в интерфейс
        self.__params["temp_plan_high"] = int(_params.get("temp_plan_high", -7))
        self.__params["temp_plan_down"] = int(_params.get("temp_plan_down", -15))

        self.ui.label_temp_plan_high.setText(str(self.__params["temp_plan_high"]))
        self.ui.label_temp_plan_down.setText(str(self.__params["temp_plan_down"]))

    @staticmethod
    def update_settings_from_web():
        _headers = {"Authorization": "Token=auth979"}
        _response = requests.get("http://127.0.0.1:8000/api/settings/get/", headers=_headers)
        if _response.status_code not in (200, 201):
            raise Exception(f"Fatal ERROR - {_response.status_code}")
        _data = _response.json().get("data", {})
        print({"_data ": _data}, type(_data))

        Utils.sql_execute(
            _query="""
    CREATE TABLE IF NOT EXISTS params (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL DEFAULT ''
                        );""",
            _kwargs={},
            _source="local_settings.db",
        )
        _connection = sqlite3.connect(f"src/database/local_settings.db")
        _cursor = _connection.cursor()

        try:
            with _connection:
                for k, v in _data.items():
                    _cursor.execute(
                        """
                        INSERT OR REPLACE INTO params (key, value) VALUES (:key, :value);
                        """,
                        {'key': k, 'value': v}
                    )

        except sqlite3.IntegrityError:

            print("Error: IntegrityError .")
            _connection.rollback()

        finally:
            _cursor.close()
            _connection.close()

    def loop(self):
        def loop_update_ui():
            while True:
                try:
                    threading.Thread(target=self.get_local_settings, args=()).start()
                except Exception as ERROR:
                    print(ERROR)
                time.sleep(1)

        def loop_update_settings_from_web():
            while 1:
                try:
                    threading.Thread(target=self.update_settings_from_web, args=()).start()
                except Exception as error:
                    print(error)
                time.sleep(6)

            # self.ui.label_temp_plan_high.setText(str(self.temp_plan_high))
            # self.ui.label_temp_plan_down.setText(str(self.temp_plan_down))

        threading.Thread(target=loop_update_ui, args=()).start()
        threading.Thread(target=loop_update_settings_from_web(), args=()).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
