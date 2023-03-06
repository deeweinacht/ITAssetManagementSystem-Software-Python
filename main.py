"""
This GUI-based application interacts with a MySQL database to provide
management of IT assets.

Copyright (C) 2023  Dee Weinacht
"""

from PyQt6.QtWidgets import QApplication
import sys
from GUI import MainWindow


application = QApplication(sys.argv)
asset_manager = MainWindow()
asset_manager.show()
sys.exit(application.exec())
