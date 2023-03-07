import mysql.connector
from mysql.connector import errorcode

from utils import my_input, my_output


# mysql.connector.connection_cext.CMySQLConnection


class Members:	

    def __init__(self, dbconnector: mysql.connector.connection_cext.CMySQLConnection):
        self.mydb = dbconnector

    def add_member(self):
        name = my_input(str, 'Enter the name of the member : ')
        phn = my_input(int, 'Enter phone no. : ')
        addr_line1 = my_input(str, 'Enter the Address (in 2 lines) : ')
        addr_line2 = my_input(str, '')
        addr_city = my_input(str, 'Enter city : ')
        addr_state = my_input(str, 'Enter State : ')

        query = f'INSERT INTO MEMBERS (name, addr_line1, addr_line2, addr_city, addr_state, phn, beg_date, end_date) VALUES("{name}", "{addr_line1}", "{addr_line2}", "{addr_city}", "{addr_state}", {phn}, curdate(), date_add(curdate(), INTERVAL 1 YEAR));'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('Member Added successfully')
        cursor.close()

    def refresh(self):
        query = f'UPDATE MEMBERS SET valid = "invalid" WHERE end_date <= curdate();'
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            my_output('\nEntry ERROR !\n\
                        Contact Technical Team \n')
        else:
            my_output('Table Updated!!')
        cursor.close()

    def get_member_details(self):
        id = my_input(int, 'Enter member id : ')
        query = f'SELECT * FROM MEMBERS WHERE id = {id};'
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
                msg = f''':-
                    ID : {row[0]}
                    Name : {row[1]}
                    Address :   {row[2]}
                                {row[3]}
                                {row[4]}
                    State : {row[5]}
                    Contact no. : {row[6]}
                    Membership Begin Date : {row[7]} 
                    Membership End Date : {row[8]}
                    Membership Validity : {row[9]}
                    '''
                my_output(msg)
        cursor.close()


    def diaplay(self):
        query = f'SELECT * FROM MEMBERS;'
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
                msg = '''ALL MEMBERS ARE'''
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
                    Membership Begin Date : {row[7]} 
                    Membership End Date : {row[8]}
                    Membership Validity : {row[9]}
                    '''
                my_output(msg)
        cursor.close()
