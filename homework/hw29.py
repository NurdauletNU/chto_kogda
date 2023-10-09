# Начать разработку собственного pet-проекта: «Систем ведения справочника по оборудованию», на PyQt6.

import sys
from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListView

class EquipmentCatalogApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Справочник по оборудованию')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.equipment_list_view = QListView()
        self.layout.addWidget(self.equipment_list_view)

        self.equipment_model = QStringListModel()
        self.equipment_list_view.setModel(self.equipment_model)

        self.input_layout = QHBoxLayout()
        self.layout.addLayout(self.input_layout)

        self.equipment_input = QLineEdit()
        self.input_layout.addWidget(self.equipment_input)

        self.add_button = QPushButton('Добавить')
        self.add_button.clicked.connect(self.add_equipment)
        self.input_layout.addWidget(self.add_button)

        self.remove_button = QPushButton('Удалить')
        self.remove_button.clicked.connect(self.remove_equipment)
        self.input_layout.addWidget(self.remove_button)

    def add_equipment(self):
        equipment_name = self.equipment_input.text()
        if equipment_name:
            equipment_list = self.equipment_model.stringList()
            equipment_list.append(equipment_name)
            self.equipment_model.setStringList(equipment_list)
            self.equipment_input.clear()
            self.equipment_input.setFocus(Qt.FocusReason.MouseFocusReason)

    def remove_equipment(self):
        selected_indexes = self.equipment_list_view.selectedIndexes()
        if selected_indexes:
            equipment_list = self.equipment_model.stringList()
            for index in selected_indexes:
                equipment_list.pop(index.row())
            self.equipment_model.setStringList(equipment_list)

def main():
    app = QApplication(sys.argv)
    window = EquipmentCatalogApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
