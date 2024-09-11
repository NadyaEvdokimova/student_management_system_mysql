import mysql.connector
import os


class DatabaseConnection:
    def __init__(self, host='localhost', user='root', password=os.environ.get("PASSWORD"), database='school'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
        return connection
