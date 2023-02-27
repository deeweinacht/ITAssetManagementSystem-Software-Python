import datetime

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QDialog, \
    QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
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
        self.setFixedSize(300, 500)

        layout = QVBoxLayout()

        # id
        id_label = QLabel('Asset ID: ')
        asset_id = QLineEdit()
        asset_id.setPlaceholderText('Automatically Generated')
        asset_id.setDisabled(True)
        layout.addWidget(id_label)
        layout.addWidget(asset_id)

        # brand
        brand_label = QLabel('Asset Brand:')
        self.brand = QComboBox()
        brands = ['brand1', 'brand2']
        self.brand.addItems(brands)
        layout.addWidget(brand_label)
        layout.addWidget(self.brand)

        # category
        category_label = QLabel('Asset Category:')
        self.category = QComboBox()
        categories = ['cat1', 'cat2']
        self.category.addItems(categories)
        layout.addWidget(category_label)
        layout.addWidget(self.category)

        # department
        department_label = QLabel('Asset Department:')
        self.department = QComboBox()
        departments = ['None', 'IT']
        self.department.addItems(departments)
        layout.addWidget(department_label)
        layout.addWidget(self.department)

        # status
        status_label = QLabel('Asset Status:')
        self.status = QComboBox()
        statuses = ['stat1', 'stat2']
        self.status.addItems(statuses)
        layout.addWidget(status_label)
        layout.addWidget(self.status)

        # submit button
        button = QPushButton('Add Asset')
        button.clicked.connect(self.add_asset)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_asset(self):
        brand = self.brand.currentText()
        category = self.category.currentText()
        department = self.department.currentText()
        status = self.status.currentText()
        acquired = datetime.datetime.now()
        print(brand, category, department, status, acquired)

