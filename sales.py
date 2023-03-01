import mysql.connector
from mysql.connector import errorcode

from utils import my_output, my_input

# mysql.connector.connection_cext.CMySQLConnection


class Sales:

    # invoice_id	int
    # member_id	    int
    # book_id	    int
    # qty	        int
    # amount	    int
    # date_s	    date

    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add_bill(self):
        member_id = my_input(int, 'Enter Member id : ')
        book_id = my_input(int, 'Enter the book id : ')
        qty = my_input(int, 'Enter the quantity : ')
        amount = 0

        query = f'SELECT price, qty FROM BOOKS WHERE id = {book_id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            row = cursor.fetchone()
            if len(row) == 0:
                my_output('No Book Found with book_id : ', book_id)
                cursor.close()
                return
            else:
                amount = row[0]*qty
                my_output(f'The bill amount : {amount}')

        query = f'INSERT INTO sales(member_id, book_id, qty, amount, date_s) VALUES({member_id}, {book_id}, {qty}, {amount}, curdate());'

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
            cursor.close()
            return

        # fetching invoice id
        query = f'SELECT invoice_id FROM sales WHERE member_id = {member_id} AND book_id = {book_id} AND qty = {qty} AND date_s = curdate();'

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            row = cursor.fetchone()
            if len(row) == 0:
                msg = '''
                The entered details maybe wrong.
                Please Recheck and Enter again
                '''
                my_output(msg)
            else:
                my_output(f'The Invoice id for the bill is {row[0]}')
        cursor.close()

    def find_total_sales(self):
        query = f'SELECT SUM(amount) FROM sales WHERE YEAR(date_s) = YEAR(CURDATE());'

        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            row = cursor.fetchone()
            my_output(f'Total sales this year : {row[0]}')
