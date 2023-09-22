import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QGridLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout, QDialog
from PyQt6.QtCore import Qt
from PyQt6 import uic


class Modal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 400)
        self.setWindowTitle("Вы ввели неверный номер заявки")
        self.grid = QGridLayout(self)
        self.button = QPushButton()
        self.button.setText("OK")
        self.grid.addWidget(self.button)


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()
        self.username_label = QLabel("Имя пользователя:", self)
        self.username_entry = QLineEdit(self)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_entry)

        self.password_label = QLabel("Пароль:", self)
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_entry)

        self.login_button = QPushButton("Войти", self)
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if username == "Nurdaulet" and password == "Manchester7":
            self.accept()
        else:
            QMessageBox.critical(self, 'Ошибка', "Неверное имя пользователя или пароль")


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('mydatabase.db')
        self.cursor = self.connection.cursor()

    def save_data(self, number, price):
        # Implement your database saving logic here
        pass

    def export_data(self):
        # Implement your database export logic here
        pass

    def __del__(self):
        self.connection.close()


class MainApplication(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.ui = uic.loadUi('hw28.ui', self)
        self.ui.pushButton_save.clicked.connect(self.save_to_database)
        self.ui.pushButton_export.clicked.connect(self.export_from_database)
        self.db_manager = db_manager
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Выход",
            "Вы точно хотите выйти?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def save_to_database(self):
        number = self.ui.lineEdit_number.text().strip()
        is_number = self.validate_number(value=number)
        if not is_number:
            QMessageBox.critical(self, 'Ошибка', "Вы ввели неправильный номер заявки")
            return

        price = self.ui.doubleSpinBox_price.value()
        if price <= 0:
            QMessageBox.critical(self, "Ошибка", "Вы ввели неправильную сумму!")
            return

        # Save data to the database
        self.db_manager.save_data(number, price)

        print(number, price)
        QMessageBox.information(self, "Успешно", "Заявка успешно добавлена в базу данных!")

    def export_from_database(self):
        # Export data from the database
        self.db_manager.export_data()
        print("Экспорт из базы данных!")
        QMessageBox.information(self, "Успешно", "Данные успешно экспортированы!")

    def validate_number(self, value):
        try:
            value = int(value)
            if value < 1:
                return False
        except Exception as error:
            print("Error:", error)
            return False
        return True


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_dialog = LoginDialog()
        if self.login_dialog.exec() == QDialog.DialogCode.Accepted:
            self.db_manager = DatabaseManager()
            self.main_window = MainApplication(self.db_manager)
            sys.exit(self.app.exec())


if __name__ == '__main__':
    my_app = Application()
