import mysql.connector
from mysql.connector import errorcode


# mysql.connector.connection_cext.CMySQLConnection



class Employees:
    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add_emp(self):
        pass

    def search_emp(self):
        pass

    def assign_mgr_stat(self):
        pass

    def display(self):
        pass

    def update_salary(self):
        pass