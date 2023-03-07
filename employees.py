import mysql.connector
from mysql.connector import errorcode

from utils import my_input, my_output


# mysql.connector.connection_cext.CMySQLConnection


class Employees:

    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add_emp(self):
        if not self.check_mgr():
            return

        print('Enter The details of new employees!!')
        name = my_input(str, 'Enter The name of the employee : ')
        addr_line1 = my_input(str, 'Enter the Address (in 2 lines) : ')
        addr_line2 = my_input(str, '')
        addr_city = my_input(str, 'Enter city : ')
        addr_state = my_input(str, 'Enter State : ')
        phn = my_input(int, 'Enter phone no. : ')
        salary = my_input(int, 'Enter salary : ')

        query = f'INSERT INTO EMPLOYEES (name, addr_line1, addr_line2, addr_city, addr_state, phn, date_of_joining, salary) VALUES("{name}", "{addr_line1}", "{addr_line2}", "{addr_city}", "{addr_state}", {phn}, curdate(), {salary});'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('Employee Added Succesfully!')
        cursor.close()

    def get_emp_details(self):
        id = my_input(int, 'Enter the id for searching an employee : ')

        query = f'SELECT * FROM EMPLOYEES WHERE id = {id};'
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
                my_output('Employee Not Found!!')
            else:
                msg = f'''
                    ID : {row[0]}
                    Name : {row[1]}
                    Address :   {row[2]}
                                {row[3]}
                                {row[4]}
                    State : {row[5]}
                    Contact no. : {row[6]}
                    Date of Joining : {row[7]} 
                    Salary : {row[8]}
                    '''
                my_output(msg)
        cursor.close()

    def assign_mgr_state(self):
        if not self.check_mgr():
            return

        id = my_input(int, 'Enter the employee id to grant Manager status : ')

        if not self.find_emp(id):
            return

        query = f'UPDATE EMPLOYEES SET mgr_status = "T" WHERE id = {id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('Manager Status granted')
        cursor.close()

    def display(self):
        query = f'SELECT * FROM EMPLOYEES;'
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
                    Address :   {row[2]}
                                {row[3]}
                                {row[4]}
                    State : {row[5]}
                    Contact no. : {row[6]}
                    Date of Joining : {row[7]} 
                    Salary : {row[8]}
                    '''
                my_output(msg)
        cursor.close()

    def update_salary(self):
        if not self.check_mgr():
            return

        id = my_input(
            int, 'Enter the id to update the salary of an employee : ')

        if not self.find_emp(id):
            return

        salary = my_input(int, 'Enter the updated salary : ')
        query = f'UPDATE EMPLOYEES SET salary = {salary} WHERE id = {id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            # print(cursor.stored_results())
            my_output('Salary update Successfully')
        cursor.close()

    def check_mgr(self):
        id = my_input(int, 'Enter Your Id for verification : ')

        query = f'SELECT mgr_status FROM EMPLOYEES WHERE id = {id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
            return False
        else:
            row = cursor.fetchone()
            if not row:
                my_output('Employee Not Found!!')
                cursor.close()
                return False
            else:
                mgr_status = row[0]
                if mgr_status == 'F':
                    my_output('You Do Not have Manager Rights!!!\n')
                    cursor.close()
                    return False
        return True

    def find_emp(self, id, display=False):
        query = f'SELECT * FROM EMPLOYEES WHERE id = {id};'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
            return False
        else:
            row = cursor.fetchone()
            if not row:
                my_output('Employee Not Found!!')
                cursor.close()
                return False
            elif display:
                msg = f'''
                    ID : {row[0]}
                    Name : {row[1]}
                    Address :   {row[2]}
                                {row[3]}
                                {row[4]}
                    State : {row[5]}
                    Contact no. : {row[6]}
                    Date of Joining : {row[7]} 
                    Salary : {row[8]}
                    '''
                my_output(msg)
        return True
