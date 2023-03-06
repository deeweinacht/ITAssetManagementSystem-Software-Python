# ITAssetManagement-Software-Python

**This GUI-based software application interacts with a MySQL database to 
provide management of IT assets.**

    Copyright (C) 2023  Dee Weinacht

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

**Description:**  
This software is an IT Asset Management System (IAMS). It provides a graphical
interface for a MySQL database to provide management of IT assets. It includes
functionality to view, add, edit, and delete IT assets, such as monitors,
laptops, etc. 

**User's Guide:**

*Configuration*

To function properly the software needs access to a configured MySQL Server 8.0
instance. By default, the software expects the server to be running on the local
machine with the following attributes:
- HOST = 'localhost'
- USERNAME = 'root'
- PASSWORD = 'passw0rd!'
- DATABASE_NAME = 'it_asset_management'

If the server is configured differently, the constants in the Database.py file
can be changed. 

The expected schema for the database and some example entries are provided in
the database directory as 'it_assets_database.sql'. This is a MySQL Workbench
Dump and can be run as a SQL command on the MySQL Server to populate the
database.

Once the MySQL Server is running with the database and the IAMS is configured
to connect properly, the software can be started by running main.py.

*Navigating the GUI*

When the main window opens it will automatically load all entries from the
Server into the table. New asset entries can be added with the plus(+) button 
on the toolbar, which will open a new window to do so. An existing asset can be 
modified or deleted by selecting an asset in the table and clicking the 
appropriate button in the toolbar (Edit Asset or Delete Asset) to open a new
window. The table of assets can be refreshed with current data from the server 
using the Refresh button.

**Dependencies:**
- UIcons by <a href="https://www.flaticon.com/uicons">Flaticon</a>
- PyQt6 used under the GNU GPL v3 license
- MySQL Connector/Python used under the GNU GPL v2 license