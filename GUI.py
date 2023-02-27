

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QDialog, \
    QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IT Asset Management System")

        # Menu Bar
        file_menu = self.menuBar().addMenu('&File')
        file_menu_add = QAction('New Asset', self)
        file_menu_add.triggered.connect(self.insert)
        file_menu_exit = QAction('Exit', self)
        file_menu.addActions([file_menu_add, file_menu_exit])

        help_menu = self.menuBar().addMenu('&Help')
        help_menu_about = QAction('About', self)
        help_menu.addAction(help_menu_about)

        self.asset_table = QTableWidget()
        self.asset_table.setColumnCount(5)
        self.asset_table.setHorizontalHeaderLabels(('ID',
                                                    'Description',
                                                    'Department',
                                                    'Status',
                                                    'Acquired'))
        self.setCentralWidget(self.asset_table)

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add New Asset')
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        # Widgets
        brand = QLineEdit()
        category = QLineEdit()
        department = QLineEdit()
        status = QLineEdit()
        layout.addWidget(brand)
        layout.addWidget(category)
        layout.addWidget(department)
        layout.addWidget(status)
        self.setLayout(layout)