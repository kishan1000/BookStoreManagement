import mysql.connector
from mysql.connector import errorcode


# mysql.connector.connection_cext.CMySQLConnection




class Sales:
    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add(self):
        pass

    def find_total_sales(self):
        pass