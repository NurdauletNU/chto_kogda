import asyncio
from functools import partial
import datetime
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSlot
import sys
import sqlite3
import requests


class Utils:
    @staticmethod
    async def sql_execute(_query: str, _kwargs: dict, _source: str):
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
        self.__params = {}
        self.ui.pushButton_temp_plan_plus.clicked.connect(self.handle_temp_plan_plus)
        self.ui.pushButton_temp_plan_minus.clicked.connect(self.handle_temp_plan_minus)
        self.show()


        self.loop = asyncio.get_event_loop()


        self.loop.create_task(self.loop_update_ui())
        self.loop.create_task(self.loop_update_settings_from_web())


        self.ui_timer = QTimer(self)
        self.ui_timer.timeout.connect(
            partial(self.loop.call_soon_threadsafe, self.loop.create_task, self.loop_update_ui()))
        self.ui_timer.start(1000)  # Every second


        self.web_timer = QTimer(self)
        self.web_timer.timeout.connect(
            partial(self.loop.call_soon_threadsafe, self.loop.create_task, self.loop_update_settings_from_web()))
        self.web_timer.start(6000)  # Every 6 seconds

    @pyqtSlot()
    def handle_temp_plan_plus(self):
        self.loop.create_task(self.handle_temp_plan_change(1))

    @pyqtSlot()
    def handle_temp_plan_minus(self):
        self.loop.create_task(self.handle_temp_plan_change(-1))

    async def handle_temp_plan_change(self, increment: int):
        try:
            await Utils.sql_execute(
                _query="""
                CREATE TABLE IF NOT EXISTS params (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL DEFAULT ''
                );""",
                _kwargs={},
                _source="local_settings.db",
            )

            _rows = await Utils.sql_execute(
                _query="""
                SELECT key, value 
                FROM params;""",
                _kwargs={},
                _source="local_settings.db",
            )

            _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
            _params = {i["key"]: i["value"] for i in _dict}

            _temp_plan_high = int(_params.get("temp_plan_high", -7)) + increment
            _temp_plan_down = int(_params.get("temp_plan_down", -15)) + increment
            _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}

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
                print("Error: IntegrityError.")
                _connection.rollback()

            finally:
                _cursor.close()
                _connection.close()
        except Exception as error:
            print(error)

    async def get_local_settings(self):
        try:
            await Utils.sql_execute(
                _query="""
                CREATE TABLE IF NOT EXISTS params (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL,
                value TEXT NOT NULL DEFAULT '' 
                );""",
                _kwargs={},
                _source="local_settings.db",
            )

            _rows = await Utils.sql_execute(
                _query="""
                SELECT key, value 
                FROM params;""",
                _kwargs={},
                _source="local_settings.db",
            )

            _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
            _params = {i["key"]: i["value"] for i in _dict}

            self.__params["temp_plan_high"] = int(_params.get("temp_plan_high", -7))
            self.__params["temp_plan_down"] = int(_params.get("temp_plan_down", -15))

            self.ui.label_temp_plan_high.setText(str(self.__params["temp_plan_high"]))
            self.ui.label_temp_plan_down.setText(str(self.__params["temp_plan_down"]))
        except Exception as error:
            print(error)

    async def update_settings_from_web(self):
        try:
            _headers = {"Authorization": "Token=auth979"}
            _response = await asyncio.to_thread(requests.get, "http://127.0.0.1:8000/api/settings/get/",
                                                headers=_headers)

            if _response.status_code not in (200, 201):
                raise Exception(f"Fatal ERROR - {_response.status_code}")

            _data = _response.json().get("data", {})
            print({"_data ": _data}, type(_data))

            await Utils.sql_execute(
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
                print("Error: IntegrityError.")
                _connection.rollback()

            finally:
                _cursor.close()
                _connection.close()
        except Exception as error:
            print(error)

    async def loop_update_ui(self):
        try:
            await self.get_local_settings()
        except Exception as error:
            print(error)

    async def loop_update_settings_from_web(self):
        try:
            await self.update_settings_from_web()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
