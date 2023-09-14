from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QGridLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QTextEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
import sys
import sqlite3

class Candidate:
    def __init__(self, name, email, phone, skills):
        self.name = name
        self.email = email
        self.phone = phone
        self.skills = skills

class CandidateList(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setWindowTitle("Candidate Management")
        self.setGeometry(100, 100, 800, 600)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Input Form
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        self.skills_label = QLabel("Skills:")
        self.skills_input = QTextEdit()

        self.add_button = QPushButton("Add Candidate")
        self.add_button.clicked.connect(self.add_candidate)

        self.grid.addWidget(self.name_label, 0, 0)
        self.grid.addWidget(self.name_input, 0, 1)
        self.grid.addWidget(self.email_label, 1, 0)
        self.grid.addWidget(self.email_input, 1, 1)
        self.grid.addWidget(self.phone_label, 2, 0)
        self.grid.addWidget(self.phone_input, 2, 1)
        self.grid.addWidget(self.skills_label, 3, 0)
        self.grid.addWidget(self.skills_input, 3, 1)
        self.grid.addWidget(self.add_button, 4, 0, 1, 2)
        self.candidate_table = QTableWidget()
        self.candidate_table.setColumnCount(4)
        self.candidate_table.setHorizontalHeaderLabels(["Name", "Email", "Phone", "Skills"])
        self.grid.addWidget(self.candidate_table, 5, 0, 1, 2)

        self.candidates = []

    def init_db(self):
        self.conn = sqlite3.connect("candidates.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone TEXT,
                skills TEXT
            )
        ''')
        self.conn.commit()

    def add_candidate(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        skills = self.skills_input.toPlainText().strip()

        if not name or not email:
            QMessageBox.critical(self, 'Error', "Name and Email are required.")
            return

        candidate = Candidate(name, email, phone, skills)
        self.candidates.append(candidate)
        self.insert_candidate_to_db(candidate)
        self.update_candidate_table()
        self.clear_input_fields()

    def clear_input_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.skills_input.clear()

    def insert_candidate_to_db(self, candidate):
        self.cursor.execute('''
            INSERT INTO candidates (name, email, phone, skills)
            VALUES (?, ?, ?, ?)
        ''', (candidate.name, candidate.email, candidate.phone, candidate.skills))
        self.conn.commit()

    def update_candidate_table(self):
        self.candidate_table.setRowCount(len(self.candidates))

        for row, candidate in enumerate(self.candidates):
            self.candidate_table.setItem(row, 0, QTableWidgetItem(candidate.name))
            self.candidate_table.setItem(row, 1, QTableWidgetItem(candidate.email))
            self.candidate_table.setItem(row, 2, QTableWidgetItem(candidate.phone))
            self.candidate_table.setItem(row, 3, QTableWidgetItem(candidate.skills))

    def closeEvent(self, event):
        self.conn.close()

def main():
    app = QApplication(sys.argv)
    window = CandidateList()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

