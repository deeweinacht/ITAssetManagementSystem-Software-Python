"""
This GUI application interacts with a MySQL database to provide management
of IT assets

Copyright (C) 2023  Dee Weinacht
"""

from PyQt6.QtWidgets import  QApplication
from PyQt6.QtGui import QAction
import sys
from GUI import MainWindow


application = QApplication(sys.argv)
iams = MainWindow()
iams.show()
sys.exit(application.exec())
