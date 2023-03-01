import mysql.connector

HOST = 'localhost'
USERNAME = 'root'
PASSWORD = 'passw0rd!'
DATABASE_NAME = 'it_asset_management'


class DatabaseConnection:
    def __init__(self,
                 host=HOST,
                 username=USERNAME,
                 password=PASSWORD,
                 database_name=DATABASE_NAME):
        self.host = host
        self.username = username
        self.password = password
        self.database_name = database_name

    def connect(self):
        connection = mysql.connector.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             database=self.database_name)
        return connection

    def load_all_assets(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM assets_combined')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def load_brands(self):
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

    def insert_asset(self, brand, category, department, status):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('INSERT into assets '
                       '(assetID, brand, category, department, status, acquiredDate) '
                       'VALUES (default, %s, %s, %s, %s, default)',
                       (brand, category, department, status))
        connection.commit()
        cursor.close()
        connection.close()

    def load_asset(self, asset_id):
        pass


    def update_asset(self):
        pass

    def delete_asset(self):
        pass