import datetime

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QDialog, \
    QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QToolBar, \
    QStatusBar, QTableWidgetItem
from PyQt6.QtGui import QAction, QIcon
from Database import DatabaseConnection


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IT Asset Management System")
        self.setWindowIcon(QIcon('icons/computer.png'))
        self.setMinimumSize(800, 600)

        # Actions
        add_asset_action = QAction(QIcon('icons/add.png'), 'New Asset', self)
        add_asset_action.triggered.connect(self.insert)
        exit_program_action = QAction(QIcon('icons/exit.png'), 'Exit', self)
        about_program_action = QAction(QIcon('icons/info.png'), 'About', self)
        edit_asset_action = QAction(QIcon('icons/edit.png'), 'Edit Asset',
                                    self)
        delete_asset_action = QAction(QIcon('icons/delete.png'),
                                      'Delete Asset', self)
        refresh_table_action = QAction(QIcon('icons/refresh.png'),
                                       'Refresh Assets Table', self)
        refresh_table_action.triggered.connect(self.load_table_data)

        # Menu Bar
        file_menu = self.menuBar().addMenu('&File')
        file_menu.addActions([add_asset_action, exit_program_action])
        help_menu = self.menuBar().addMenu('&Help')
        help_menu.addAction(about_program_action)

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addActions([add_asset_action, edit_asset_action,
                            delete_asset_action, refresh_table_action])

        # Asset Table
        self.asset_table = QTableWidget()
        self.asset_table.setColumnCount(6)
        self.asset_table.setHorizontalHeaderLabels(('ID',
                                                    'Brand',
                                                    'Category',
                                                    'Department',
                                                    'Status',
                                                    'Acquired'))
        self.asset_table.horizontalHeader().setStretchLastSection(True)
        self.setCentralWidget(self.asset_table)
        self.load_table_data()

        # Status Bar
        self.status_bar = QStatusBar()
        self.status_label = QLabel('')
        self.status_label.setMinimumWidth(800)
        self.status_bar.addWidget(self.status_label)
        self.setStatusBar(self.status_bar)

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
        self.load_table_data()
        self.status_label.setText('New Asset Inserted!')

    def load_table_data(self):
        db_connection = DatabaseConnection()
        asset_data = db_connection.load_all_assets()
        self.asset_table.setRowCount(0)
        for row_num, row_data in enumerate(asset_data):
            self.asset_table.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                self.asset_table.setItem(row_num, col_num,
                                         QTableWidgetItem(str(value)))


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add New Asset')
        self.setFixedSize(300, 500)
        self.brands = []
        self.categories = []
        self.departments = []
        self.statuses = []
        self.load_values()

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
        self.brand.addItems(dict(self.brands).values())
        layout.addWidget(brand_label)
        layout.addWidget(self.brand)

        # category
        category_label = QLabel('Asset Category:')
        self.category = QComboBox()
        self.category.addItems(dict(self.categories).values())
        layout.addWidget(category_label)
        layout.addWidget(self.category)

        # department
        department_label = QLabel('Asset Department:')
        self.department = QComboBox()
        self.department.addItems(dict(self.departments).values())
        layout.addWidget(department_label)
        layout.addWidget(self.department)

        # status
        status_label = QLabel('Asset Status:')
        self.status = QComboBox()
        self.status.addItems(dict(self.statuses).values())
        layout.addWidget(status_label)
        layout.addWidget(self.status)

        # submit button
        button = QPushButton('Add Asset')
        button.clicked.connect(self.add_asset)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_asset(self):
        for num, name in self.brands:
            if name == self.brand.currentText():
                brand_num = num
                break
        for num, name in self.categories:
            if name == self.category.currentText():
                category_num = num
                break
        for num, name in self.departments:
            if name == self.department.currentText():
                department_num = num
                break
        for num, name in self.statuses:
            if name == self.status.currentText():
                status_num = num
                break
        db_connection = DatabaseConnection()
        db_connection.insert_asset(brand_num, category_num,
                                   department_num, status_num)
        self.close()

    def load_values(self):
        db_connection = DatabaseConnection()
        self.brands = db_connection.load_brands()
        self.categories = db_connection.load_categories()
        self.departments = db_connection.load_departments()
        self.statuses = db_connection.load_statuses()


class EditDialog(QDialog):
    def __init__(self, asset_ID: int):
        super().__init__()
        self.setWindowTitle('Edit Asset')
        self.setFixedSize(300, 500)
        self.brands = []
        self.categories = []
        self.departments = []
        self.statuses = []
        self.asset_ID = asset_ID
        self.asset_brand = None
        self.asset_category = None
        self.asset_department = None
        self.asset_status = None
        self.load_values()

        layout = QVBoxLayout()

        # id
        id_label = QLabel('Asset ID: ')
        asset_id = QLineEdit()
        asset_id.setPlaceholderText(asset_ID)
        asset_id.setDisabled(True)
        layout.addWidget(id_label)
        layout.addWidget(asset_id)

        # brand
        brand_label = QLabel('Asset Brand:')
        self.brand = QComboBox()
        self.brand.addItems(dict(self.brands).values())
        layout.addWidget(brand_label)
        layout.addWidget(self.brand)

        # category
        category_label = QLabel('Asset Category:')
        self.category = QComboBox()
        self.category.addItems(dict(self.categories).values())
        layout.addWidget(category_label)
        layout.addWidget(self.category)

        # department
        department_label = QLabel('Asset Department:')
        self.department = QComboBox()
        self.department.addItems(dict(self.departments).values())
        layout.addWidget(department_label)
        layout.addWidget(self.department)

        # status
        status_label = QLabel('Asset Status:')
        self.status = QComboBox()
        self.status.addItems(dict(self.statuses).values())
        layout.addWidget(status_label)
        layout.addWidget(self.status)

        # submit button
        button = QPushButton('Add Asset')
        button.clicked.connect(self.add_asset)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_asset(self):
        for num, name in self.brands:
            if name == self.brand.currentText():
                brand_num = num
                break
        for num, name in self.categories:
            if name == self.category.currentText():
                category_num = num
                break
        for num, name in self.departments:
            if name == self.department.currentText():
                department_num = num
                break
        for num, name in self.statuses:
            if name == self.status.currentText():
                status_num = num
                break
        db_connection = DatabaseConnection()
        db_connection.insert_asset(brand_num, category_num,
                                   department_num, status_num)

        self.close()

    def load_values(self):
        db_connection = DatabaseConnection()
        self.brands = db_connection.load_brands()
        self.categories = db_connection.load_categories()
        self.departments = db_connection.load_departments()
        self.statuses = db_connection.load_statuses()


