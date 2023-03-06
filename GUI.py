from PyQt6.QtWidgets import QMainWindow, QTableWidget, QDialog, \
    QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QToolBar, \
    QStatusBar, QTableWidgetItem, QGridLayout, QMessageBox
from PyQt6.QtGui import QAction, QIcon
from Database import DatabaseConnection


class MainWindow(QMainWindow):
    """
    Creates a main window for the GUI.
    """

    def __init__(self):
        """
        Constructor for MainWindow objects.
        """
        super().__init__()
        self.setWindowTitle("IT Asset Management System")
        self.setWindowIcon(QIcon('icons/computer.png'))
        self.setMinimumSize(800, 600)

        # Actions - create QActions and connect to methods
        add_asset_action = QAction(QIcon('icons/add.png'), 'New Asset', self)
        add_asset_action.triggered.connect(self.insert)
        exit_program_action = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exit_program_action.triggered.connect(self.close)
        about_program_action = QAction(QIcon('icons/info.png'), 'About', self)
        about_program_action.triggered.connect(self.about)
        edit_asset_action = QAction(QIcon('icons/edit.png'), 'Edit Asset',
                                    self)
        edit_asset_action.triggered.connect(self.edit)
        delete_asset_action = QAction(QIcon('icons/delete.png'),
                                      'Delete Asset', self)
        delete_asset_action.triggered.connect(self.delete)
        refresh_table_action = QAction(QIcon('icons/refresh.png'),
                                       'Refresh Assets Table', self)
        refresh_table_action.triggered.connect(self.load_table_data)

        # Menu Bar - create menu bar, add menus and actions
        file_menu = self.menuBar().addMenu('&File')
        file_menu.addActions([add_asset_action,
                              refresh_table_action,
                              exit_program_action])
        help_menu = self.menuBar().addMenu('&Help')
        help_menu.addAction(about_program_action)

        # Toolbar - create QToolbar and add actions
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addActions([add_asset_action, edit_asset_action,
                            delete_asset_action, refresh_table_action])

        # Status Bar - create QStatusBar and add label
        self.status_bar = QStatusBar()
        self.status_label = QLabel('')
        self.status_label.setMinimumWidth(800)
        self.status_bar.addWidget(self.status_label)
        self.setStatusBar(self.status_bar)

        # Asset Table - create QTableWidget and format table
        self.asset_table = QTableWidget()
        self.asset_table.setSortingEnabled(True)
        self.asset_table.setColumnCount(6)
        self.asset_table.verticalHeader().setVisible(False)
        self.asset_table.setHorizontalHeaderLabels(('ID',
                                                    'Brand',
                                                    'Category',
                                                    'Department',
                                                    'Status',
                                                    'Acquired'))
        self.asset_table.horizontalHeader().setStretchLastSection(True)
        self.setCentralWidget(self.asset_table)
        self.load_table_data()

    def load_table_data(self):
        """
        Uses a database connection to load all assets from the database
        and display them in the asset table.

        :return: None
        """
        db_connection = DatabaseConnection()
        asset_data = db_connection.load_all_assets()
        asset_data.sort()
        self.asset_table.setRowCount(0)
        for row_num, row_data in enumerate(asset_data):
            self.asset_table.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                self.asset_table.setItem(row_num, col_num,
                                         QTableWidgetItem(str(value)))
        self.status_label.setText('All assets loaded!')

    def insert(self):
        """
        Creates an 'insert' dialog window.

        :return: None
        """
        dialog = InsertDialog()
        dialog.exec()
        self.load_table_data()
        self.status_label.setText('New asset inserted!')

    def edit(self):
        """
        Creates an 'edit' dialog window, using data from the currently
        selected row in the asset table.

        :return: None
        """
        selected_row = self.asset_table.currentRow()
        selected_asset_ID = int(self.asset_table.item(selected_row, 0).text())
        dialog = EditDialog(selected_asset_ID)
        dialog.exec()
        self.load_table_data()
        self.status_label.setText('Asset updated!')

    def delete(self):
        """
        Creates a 'delete' dialog window, using data from the currently
        selected row in the asset table.

        :return: None
        """
        selected_row = self.asset_table.currentRow()
        selected_asset_ID = int(self.asset_table.item(selected_row, 0).text())
        dialog = DeleteDialog(selected_asset_ID)
        dialog.exec()
        self.load_table_data()
        self.status_label.setText('Asset deleted!')

    @staticmethod
    def about():
        """
        Creates an 'about' dialog window.

        :return: None
        """
        dialog = AboutDialog()
        dialog.exec()


class InsertDialog(QDialog):
    """
    Creates an 'insert' QDialog window.

    Attributes:
        brands
        categories
        departments
        statuses
    """
    def __init__(self):
        """
        Constructor for InsertDialog objects.
        """
        super().__init__()
        self.brands = []
        self.categories = []
        self.departments = []
        self.statuses = []
        self.load_values()

        self.setWindowTitle('Add New Asset')
        self.setFixedSize(300, 500)
        layout = QVBoxLayout()

        # ID section widgets
        id_label = QLabel('Asset ID: ')
        asset_id = QLineEdit()
        asset_id.setPlaceholderText('Automatically Generated')
        asset_id.setDisabled(True)
        layout.addWidget(id_label)
        layout.addWidget(asset_id)

        # brand section widgets
        brand_label = QLabel('Asset Brand:')
        self.brand = QComboBox()
        self.brand.addItems(dict(self.brands).values())
        layout.addWidget(brand_label)
        layout.addWidget(self.brand)

        # category section widgets
        category_label = QLabel('Asset Category:')
        self.category = QComboBox()
        self.category.addItems(dict(self.categories).values())
        layout.addWidget(category_label)
        layout.addWidget(self.category)

        # department section widgets
        department_label = QLabel('Asset Department:')
        self.department = QComboBox()
        self.department.addItems(dict(self.departments).values())
        layout.addWidget(department_label)
        layout.addWidget(self.department)

        # status section widgets
        status_label = QLabel('Asset Status:')
        self.status = QComboBox()
        self.status.addItems(dict(self.statuses).values())
        layout.addWidget(status_label)
        layout.addWidget(self.status)

        # submit button widget
        button = QPushButton('Add Asset')
        button.clicked.connect(self.add_asset)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_asset(self):
        """
        Inserts a new asset into the database with the values selected in
        the GUI widgets using a database connection.

        :return: None
        """
        brand_num = None
        category_num = None
        department_num = None
        status_num = None

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
        if brand_num and category_num and department_num and status_num:
            db_connection = DatabaseConnection()
            db_connection.insert_asset(brand_num, category_num,
                                       department_num, status_num)
        self.close()

    def load_values(self):
        """
        Loads asset description data using a database connection.

        :return: None
        """
        db_connection = DatabaseConnection()
        self.brands = db_connection.load_brands()
        self.categories = db_connection.load_categories()
        self.departments = db_connection.load_departments()
        self.statuses = db_connection.load_statuses()


class EditDialog(QDialog):
    """
    Creates an 'edit' QDialog dialog window.

    Attributes:
        brands
        categories
        departments
        statuses
        asset_ID
        asset_brand
        asset_category
        asset_department
        asset_status
    """
    def __init__(self, asset_ID: int):
        """
        Constructor for EditDialog objects.
        :param asset_ID: ID of the asset to edit
        """
        super().__init__()
        self.asset_ID = asset_ID
        self.brands = []
        self.categories = []
        self.departments = []
        self.statuses = []
        self.asset_brand = None
        self.asset_category = None
        self.asset_department = None
        self.asset_status = None
        self.load_values()

        self.setWindowTitle('Edit Asset')
        self.setFixedSize(300, 500)
        layout = QVBoxLayout()

        # ID section widgets
        id_label = QLabel('Asset ID: ')
        asset_id = QLineEdit(str(self.asset_ID))
        asset_id.setDisabled(True)
        layout.addWidget(id_label)
        layout.addWidget(asset_id)

        # brand section widgets
        brand_label = QLabel('Asset Brand:')
        self.brand = QComboBox()
        self.brand.addItems(dict(self.brands).values())
        self.brand.setCurrentText(self.asset_brand)
        layout.addWidget(brand_label)
        layout.addWidget(self.brand)

        # category section widgets
        category_label = QLabel('Asset Category:')
        self.category = QComboBox()
        self.category.addItems(dict(self.categories).values())
        self.category.setCurrentText(self.asset_category)
        layout.addWidget(category_label)
        layout.addWidget(self.category)

        # department section widgets
        department_label = QLabel('Asset Department:')
        self.department = QComboBox()
        self.department.addItems(dict(self.departments).values())
        self.department.setCurrentText(self.asset_department)
        layout.addWidget(department_label)
        layout.addWidget(self.department)

        # status section widgets
        status_label = QLabel('Asset Status:')
        self.status = QComboBox()
        self.status.addItems(dict(self.statuses).values())
        self.status.setCurrentText(self.asset_status)
        layout.addWidget(status_label)
        layout.addWidget(self.status)

        # submit button widget
        button = QPushButton('Update Asset')
        button.clicked.connect(self.update_asset)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_asset(self):
        """
        Updates an existing asset in the database with the values selected in
        the GUI widgets using a database connection.

        :return: None
        """
        brand_num = None
        category_num = None
        department_num = None
        status_num = None
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

        if brand_num and category_num and department_num and status_num:
            db_connection = DatabaseConnection()
            db_connection.update_asset(self.asset_ID, brand_num, category_num,
                                       department_num, status_num)

        self.close()

    def load_values(self):
        """
        Loads all asset description data and data on a specific asset by
        using a database connection.

        :return: None
        """
        db_connection = DatabaseConnection()
        self.brands = db_connection.load_brands()
        self.categories = db_connection.load_categories()
        self.departments = db_connection.load_departments()
        self.statuses = db_connection.load_statuses()

        asset_tuple = db_connection.load_asset(self.asset_ID)
        for num, name in self.brands:
            if num == asset_tuple[1]:
                self.asset_brand = name
                break
        for num, name in self.categories:
            if num == asset_tuple[2]:
                self.asset_category = name
                break
        for num, name in self.departments:
            if num == asset_tuple[3]:
                self.asset_department = name
                break
        for num, name in self.statuses:
            if num == asset_tuple[4]:
                self.asset_status = name
                break


class DeleteDialog(QDialog):
    """
    Creates a 'delete' QDialog dialog window.

    Attributes:
        asset_ID
    """
    def __init__(self, asset_ID: int):
        """
        Constructor for a 'delete' QDialog dialog window.

        :param asset_ID: ID of the asset to delete
        """
        super().__init__()
        self.asset_ID = asset_ID

        self.setWindowTitle('Delete Asset')
        layout = QGridLayout()

        # widgets for the window
        confirm_label = QLabel(f'Are you SURE you want to delete asset '
                               f'#{self.asset_ID}')
        yes_button = QPushButton('Yes')
        no_button = QPushButton('No')

        # add to the layout
        layout.addWidget(confirm_label, 0, 0, 1, 2)
        layout.addWidget(yes_button, 1, 0)
        layout.addWidget(no_button, 1, 1)
        self.setLayout(layout)

        # connect button actions
        yes_button.clicked.connect(self.delete_asset)
        no_button.clicked.connect(self.cancel_delete)

    def delete_asset(self):
        """
        Deletes an asset using a database connection.
        :return: None
        """
        db_connection = DatabaseConnection()
        db_connection.delete_asset(self.asset_ID)
        self.close()

    def cancel_delete(self):
        """
        Cancels delete an asset and closes the dialog window.
        :return: None
        """
        self.close()


class AboutDialog(QMessageBox):
    """
    Creates an 'about' QMessageBox window.
    """
    def __init__(self):
        """
        Constructor for AboutDialog objects.
        """
        super().__init__()
        self.setWindowTitle('About')
        about_text = '''
        This IT Asset Management System application was created using Python 3.10.
        UIcons by Flaticon.
        
        Copyright (C) 2023  Dee Weinacht
        '''
        self.setText(about_text)
