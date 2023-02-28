import mysql.connector

HOST = 'localhost'
USERNAME = 'root'
PASSWORD = 'passw0rd!'
DATABASE_NAME = 'it_asset_management.db'


class DatabaseConnection:
    def __init__(self,
                 host=HOST,
                 username=USERNAME,
                 password=PASSWORD,
                 database_name=DATABASE_NAME):
        self.host = host
        self.username = username
        self.password = PASSWORD
        self.database_name = database_name

    def connect(self):
        connection = mysql.connector.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             database=self.database_name)
        return connection


def load_asset_data(database_name: str):
    pass


def insert_asset():
    pass