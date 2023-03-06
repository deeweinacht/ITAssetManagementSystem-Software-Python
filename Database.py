import mysql.connector

# Constants for default database operation
HOST = 'localhost'
USERNAME = 'root'
PASSWORD = 'passw0rd!'
DATABASE_NAME = 'it_asset_management'


class DatabaseConnection:
    """
    Class to represent database connections to MySQL databases.

    Attributes:
        host: str = HOST
        username: str = USERNAME
        password: str = PASSWORD
        database_name: str = DATABASE_NAME
    """
    def __init__(self,
                 host: str = HOST,
                 username: str = USERNAME,
                 password: str = PASSWORD,
                 database_name: str = DATABASE_NAME):
        """
        Constructor for DatabaseConnection objects.

        :param host: host system for the database
        :param username: login username for the database
        :param password: login password for the database
        :param database_name: name of the database
        """
        self.host = host
        self.username = username
        self.password = password
        self.database_name = database_name

    def connect(self):
        """
        Creates a mySQL connection objects and returns it.

        :return: a mySQLConnection object
        """
        connection = mysql.connector.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             database=self.database_name)
        return connection

    def load_all_assets(self):
        """
        Fetches all assets from the database, using a stored view.

        :return: list of rows, each item being one asset
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM assets_combined')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def load_brands(self):
        """
        Fetches all brands from the 'brands' table in the database.

        :return: list of brands
        """
        brands = []
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM brands')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        for entry in result:
            brands.append((entry[0], entry[1]))
        return brands
    
    def load_categories(self):
        """
        Fetches all categories from the 'categories' table in the database.

        :return: list of categories
        """
        categories = []
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM categories')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        for entry in result:
            categories.append((entry[0], entry[1]))
        return categories
    
    def load_departments(self):
        """
        Fetches all departments from the 'departments' table in the database.

        :return: list of departments
        """
        departments = []
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM departments')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        for entry in result:
            departments.append((entry[0], entry[1]))
        return departments
    
    def load_statuses(self):
        """
        Fetches all statuses from the 'statuses' table in the database.

        :return: list of statuses
        """
        statuses = []
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM statuses')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        for entry in result:
            statuses.append((entry[0], entry[1]))
        return statuses

    def insert_asset(self, brand: int, category: int, department: int,
                     status: int):
        """
        Inserts a new asset entry into the database.

        :param brand: brand of the asset
        :param category: category of the asset
        :param department: department the asset is assigned to
        :param status: status of the asset
        :return: None
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('INSERT into assets '
                       '(assetID, brand, category, department, status, '
                       'acquiredDate) '
                       'VALUES (default, %s, %s, %s, %s, default)',
                       (brand, category, department, status))
        connection.commit()
        cursor.close()
        connection.close()

    def load_asset(self, asset_ID: int):
        """
        Fetches a single asset from the database using the asset ID.

        :param asset_ID: ID of the asset
        :return: None
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('Select * FROM assets WHERE assetID = %s', (asset_ID,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result

    def update_asset(self, asset_ID: int, brand: int, category: int,
                     department: int, status: int):
        """
        Updates an existing asset in the database, using the asset ID as
        an identifier.

        :param asset_ID: ID of the asset
        :param brand: brand of the asset
        :param category: category of the asset
        :param department: department that the asset is assigned to
        :param status: status of the asset
        :return: None
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('UPDATE assets set brand = %s, category = %s, '
                       'department = %s, status = %s WHERE assetID = %s',
                        (brand, category, department, status, asset_ID))
        connection.commit()
        cursor.close()
        connection.close()

    def delete_asset(self, asset_ID: int):
        """
        Deletes an existing asset from the database using the asset ID
        as an identifier.

        :param asset_ID: ID of the asset
        :return: None
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM assets WHERE assetID = %s', (asset_ID,))
        connection.commit()
        cursor.close()
        connection.close()
