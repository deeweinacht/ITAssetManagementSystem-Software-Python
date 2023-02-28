import datetime

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QDialog, \
    QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QToolBar, \
    QStatusBar
from PyQt6.QtGui import QAction, QIcon


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
        self.asset_table.setColumnCount(5)
        self.asset_table.setHorizontalHeaderLabels(('ID',
                                                    'Description',
                                                    'Department',
                                                    'Status',
                                                    'Acquired'))
        self.setCentralWidget(self.asset_table)

        # Status Bar
        status_bar = QStatusBar()
        status_label = QLabel('')
        status_bar.addWidget(status_label)
        self.setStatusBar(status_bar)

    @staticmethod
    def insert():
        dialog = InsertDialog()
        dialog.exec()

    def edit(self):
        pass


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

