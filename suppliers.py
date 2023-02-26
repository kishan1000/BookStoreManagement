import mysql.connector
from utils import my_input, my_output


# mysql.connector.connection_cext.CMySQLConnection

class Suppliers:

    # int id; // Primary Key
    # string name;
    # long int phn; # takes as str
    # string addr_line1;
    # string addr_line2;
    # string addr_city;
    # string addr_state;

    def __init__(self, dbconnector:mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add_supplier(self):
        name = my_input(str, "Enter the Supplier Name : ")
        phn = my_input(int, "Enter Phone no. : ")
        addr_line1 = my_input(str, "Enter the address (in 2 lines) : ")
        addr_line2 = my_input(str, '')
        addr_city = my_input(str, 'Enter the city : ')
        addr_state = my_input(str, "Enter State : ")

        query = f'INSERT INTO SUPPLIERS(name, phn, addr_line1, addr_line2, addr_city, addr_state) VALUES("{name}", {phn}, "{addr_line1}", "{addr_line2}", "{addr_city}", "{addr_state}");'
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('\nSupplier Record Inserted Successfully\n')
        cursor.close()

    def remove_supplier(self):
        id = my_input(int, 'Enter the supplier id to remove the Supplier : ')

        query = f'SELECT * FROM SUPPLIERS WHERE id = {id};'
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
                my_output('\nNo Supplier Found\n')
                cursor.close()
                return
        cursor.close()

        query = f'DELETE FROM SUPPLIERS WHERE id = {id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('\nSupplier Removed\n')
        
        cursor.close()

    def search(self):
        id = my_input(int, 'Enter the supplier id to find the Supplier details : ')

        query = f'SELECT * FROM SUPPLIERS WHERE id = {id};'
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
                my_output('\nNo Supplier Found\n')
            else:
                msg = f'''
                ID : {row[0]}
                Name : {row[1]}
                Phone no. : {row[2]}
                Address Line 1 : {row[3]}
                Address Line 2 : {row[4]}
                City : {row[5]}
                State : {row[6]}\n
                '''
                my_output(msg)
        cursor.close()

    def display(self):
        query = f'SELECT * FROM SUPPLIERS;'
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
                my_output('\nNo Suppliers Found\n')
            else:
                i = 0
                msg = ''''''
                for row in rows:
                    i += 1
                    msg += f'''\n{i}:-
                    ID : {row[0]}
                    Name : {row[1]}
                    Phone no. : {row[2]}
                    Address Line 1 : {row[3]}
                    Address Line 2 : {row[4]}
                    City : {row[5]}
                    State : {row[6]}\n
                    '''
                my_output(msg)
        cursor.close()