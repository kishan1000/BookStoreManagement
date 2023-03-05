import mysql.connector
from mysql.connector import errorcode
from utils import my_input, my_output


# mysql.connector.connection_cext.CMySQLConnection


class Purchases:

    # int ord_id;  // Primary Key
    # int book_id; // FK ref (books)
    # int sup_id;  // FK ref (suppliers)
    # int qty;
    # date dt_ordered;
    # int eta;
    # char received; // Check(T or C or F) def (F)
    # int inv;

    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def new_order(self):
        book_id = my_input(int, 'Enter the book Id : ')
        sup_id = my_input(int, 'Enter Supplier Id : ')
        qty = my_input(int, 'Enter the Quantity : ')
        eta = my_input(int, 'Estimated expected Delivery (in days) : ')

        query = f'INSERT INTO PURCHASES (book_id, sup_id, qty, dt_ordered, eta) VALUES ({book_id}, {sup_id}, {qty}, curdate(), DATE_ADD(curdate(), INTERVAL {eta} DAY));'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            if err.errno == 1452:
                my_output('Wrong book Id or supplier Id')
            else:
                print(err.msg)
                my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('\nNew order Added\n')
        cursor.close()

    def display(self):
        menu = '''Select an Option
        1. View orders not Received
        2. View orders Cancelled
        3. View orders Received'''
        my_output(menu)
        while True:
            c = my_input(int, 'Enter Your choice : ')
            if c == 1:
                received = 'F'
                break
            elif c == 2:
                received = 'C'
                break
            elif c == 3:
                received = 'T'
                break
            else:
                print('Please Select correct option.')
                continue

        query = f'SELECT * FROM PURCHASES WHERE received = "{received}";'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            rows = cursor.fetchall()
            msg = ''''''
            if c == 1:
                msg += f'''Orders not received are:-
                '''
            elif c == 2:
                msg += f'''Orders Cancelled are:-
                '''
            elif c == 3:
                msg += f'''Orders received are:-
                '''

            for row in rows:
                msg += f'''
                Order Id : {row[0]}
                Book Id : {row[1]}
                Suppliers Id : {row[2]}
                Quantity : {row[3]}
                Date Ordered : {row[4]}
                Estimated Delivery date : {row[5]}
                '''
            my_output(msg)
        cursor.close()

    def mark_canceled(self):
        ord_id = my_input(int, 'Enter the order id for order cancelled : ')
        query = f'UPDATE PURCHASES SET received = "C" WHERE ord_id = {ord_id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('Cancelled Marked successfully')
        cursor.close()

    def mark_recieved(self):
        ord_id = my_input(int, 'Enter the order id for order received : ')
        query = f'UPDATE PURCHASES SET received = "T" WHERE ord_id = {ord_id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('Received Marked successfully')
        cursor.close()
