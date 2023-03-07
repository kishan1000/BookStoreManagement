import mysql.connector
from utils import my_input, my_output


class Books:

    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    # add book to the store (book id not required)

    def add(self):
        name = my_input(str, "Enter the name of the book : ")
        auth = my_input(str, "Enter the name of the author : ")
        price = my_input(int, "Enter the Price : ")
        qty = my_input(int, "Enter the Qty Recived : ")

        query = f'INSERT INTO BOOKS(name, auth, price, qty) VALUES("{name}", "{auth}", {price}, {qty});'
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('\nBook Record Inserted Successfully\n')
        cursor.close()

    def update_price(self):
        id = my_input(int, "Enter the id of the book for update in price : ")

        query = f'SELECT name, price FROM BOOKS WHERE ID = {id};'
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            row = cursor.fetchone()
            if not row:
                my_output('No Book found!!!')
                return

            name, price = row
            msg = f'''\nThe Name of the book is : {name}
            The current price of the book is : {price}\n
            '''
            my_output(msg)
            choice = my_input(str, 'Do you Want to Update the Price [y/n] : ')
            if choice == 'Y' or choice == 'y':
                newPrice = my_input(int, "Enter the new price : ")
                newQuery = f'UPDATE BOOKS SET price = {newPrice} WHERE id = {id};'
                try:
                    cursor.execute(newQuery)
                    self.mydb.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
                    cursor.close()
                else:
                    my_output('\nBook Price Updated Successfully\n')
            else:
                my_output('\nNo changes Made!!\n')
        cursor.close()

    # search book by id only

    def search(self):
        id = my_input(int, "Enter book id for details : ")

        query = f'SELECT * FROM BOOKS WHERE id = {id};'
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            row = cursor.fetchone()
            if not row:
                my_output('\nNo record Found\n')
            else:
                msg = f'''\nID : {row[0]}
                Name : {row[1]}
                Author : {row[2]}
                Price : {row[3]}
                Inventory count : {row[4]}\n
                '''
                my_output(msg)
        cursor.close()

    # update the book after purchase

    def update(self):

        query = f'SELECT book_id, qty FROM PURCHASES WHERE received = "T" AND inv IS NULL;'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
            cursor.close()
            return
        else:
            rows = cursor.fetchall()

        query = f'UPDATE purchases SET inv = 1 WHERE received = "T" AND inv IS NULL;'

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
            cursor.close()
            return

        cursor.close()

        if not rows:
            my_output('No order found to update')
            return

        for row in rows:
            b_id = row[0]
            qty = row[1]
            query = f'UPDATE BOOKS SET qty = qty+{qty} WHERE id = {b_id};'
            cursor = self.mydb.cursor()

            try:
                cursor.execute(query)
                self.mydb.commit()
            except mysql.connector.Error as err:
                print(err.msg)
                my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
                cursor.close()
                return

            cursor.close()

        my_output('The orders recieved have been updated.')

    def display(self):
        query = f'SELECT * FROM BOOKS;'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                    Contact Technical Team \n')
        else:
            rows = cursor.fetchall()
            if len(rows) == 0:
                my_output('\nNo record Found\n')
            else:
                i = 0
                msg = ''''''
                for row in rows:
                    i += 1
                    msg += f'''\n{i}:-
                    ID : {row[0]}
                    Name : {row[1]}
                    Author : {row[2]}
                    Price : {row[3]}
                    Quantity : {row[4]} 
                    '''
                my_output(msg)
        cursor.close()
