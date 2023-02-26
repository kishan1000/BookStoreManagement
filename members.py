import mysql.connector
from mysql.connector import errorcode


# mysql.connector.connection_cext.CMySQLConnection



class Members:
    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add_mem(self):
        pass

    def refresh(self):
        pass

    def search_mem(self):
        pass