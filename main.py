
import mysql.connector
from mysql.connector import errorcode
import os

from utils import my_input, my_output

from books import Books
from suppliers import Suppliers
from purchases import Purchases
from employees import Employees
from members import Members
from sales import Sales

HOST = 'localhost'
USER = 'Kishan'  # user name here
PASS = 'kishan'  # password
DATABASE = 'management'


def book_menu():
    os.system('cls')
    msg = '''
    *************************************************
                    BOOK MENU
    *************************************************
        1. ADD
        2. UPDATE PRICE
        3. SEARCH
        4. UPDATE STATUS
        5. DISPLAY ALL
        6. RETURN TO MAIN MENU
    '''
    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        books.add()
        input('Press Enter...')
    elif c == 2:
        books.update_price()
        input('Press Enter...')
    elif c == 3:
        books.search()
        input('Press Enter...')
    elif c == 4:
        books.update()
        input('Press Enter...')
    elif c == 5:
        books.display()
        input('Press Enter...')
    elif c == 6:
        main_menu()
        return
    else:
        print('Wrong input')
        input('Press Enter...')

    book_menu()


def suppliers_menu():
    os.system('cls')
    msg = '''
    *************************************************
                    SUPPLIERS MENU
    *************************************************
        1. ADD
        2. REMOVE
        3. SEARCH
        4. DISPLAY ALL
        5. RETURN TO MAIN MENU
    '''

    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        suppliers.add_supplier()
        input('Press Enter...')
    elif c == 2:
        suppliers.remove_supplier()
        input('Press Enter...')
    elif c == 3:
        suppliers.search()
        input('Press Enter...')
    elif c == 4:
        suppliers.display()
        input('Press Enter...')
    elif c == 5:
        main_menu()
        return
    else:
        print('Wrong input')
        input('Press Enter...')

    suppliers_menu()


def purchases_menu():
    os.system('cls')
    msg = '''
    *************************************************
                    PURCHASES MENU
    *************************************************
        1. NEW ORDER
        2. VIEW ALL
        3. CANCEL ORDER
        4. RECIEVED ORDER
        5. RETURN TO MAIN MENU
    '''

    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        purchases.new_order()
        input('Press Enter...')
    elif c == 2:
        purchases.display()
        input('Press Enter...')
    elif c == 3:
        purchases.mark_canceled()
        input('Press Enter...')
    elif c == 4:
        purchases.mark_recieved()
        input('Press Enter...')
    elif c == 5:
        main_menu()
        return
    else:
        print('Wrong input')
        input('Press Enter...')

    purchases_menu()


def employees_menu():
    os.system('cls')
    msg = '''
    *************************************************
                    EMPLOYEES MENU
    *************************************************
        1. NEW EMPLOYEE
        2. SEARCH EMPLOYEE
        3. ASSIGN MANAGER
        4. VIEW ALL
        5. UPDATE SALARY
        6. RETURN TO MAIN MENU
    '''

    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        employees.add_emp()
        input('Press Enter...')
    elif c == 2:
        id = my_input(int, 'Enter the ID of Employee : ')
        employees.find_emp()
        input('Press Enter...')
    elif c == 3:
        employees.assign_mgr_state()
        input('Press Enter...')
    elif c == 4:
        employees.display()
        input('Press Enter...')
    elif c == 5:
        employees.update_salary()
        input('Press Enter...')
    elif c == 6:
        main_menu()
        return
    else:
        print('Wrong input')
        input('Press Enter...')

    employees_menu()


def members_menu():
    os.system('cls')
    msg = '''
    *************************************************
                    MEMBERS MENU
    *************************************************
        1. NEW MEMBER
        2. SEARCH MEMBER
        3. REFRESH MEMBERS VALIDITY
        4. VIEW ALL
        5. RETURN TO MAIN MENU
    '''

    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        members.add_member()
        input('Press Enter...')
    elif c == 2:
        members.get_member_details()
        input('Press Enter...')
    elif c == 3:
        members.refresh()
        input('Press Enter...')
    elif c == 4:
        members.diaplay()
        input('Press Enter...')
    elif c == 5:
        main_menu()
        return
    else:
        print('Wrong input')
        input('Press Enter...')

    members_menu()


def sales_menu():
    os.system('cls')
    msg = '''
    *************************************************
                    SALES MENU
    *************************************************
        1. ADD NEW BILL
        2. TOTAL SALES OF THE YEAR
        3. RETURN TO MAIN MENU
    '''

    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        sales.add_bill()
        input('Press Enter...')
    elif c == 2:
        sales.find_total_sales()
        input('Press Enter...')
    elif c == 3:
        main_menu()
        return
    else:
        print('Wrong input')
        input('Press Enter...')

    sales_menu()


def password():
    pass


def main_menu():
    os.system('cls')
    msg = f'''
    *************************************************
                BOOKSHOP MANGEMENT SYSTEM
    *************************************************
        1. BOOKS
        2. SUPPLIERS
        3. PURCHASES
        4. EMPLOYEES
        5. MEMBERS
        6. SALES
        7. EXIT
    '''

    my_output(msg)
    c = my_input(int, 'Enter Your Choice : ')

    if c == 1:
        os.system('cls')
        book_menu()
        input('Press Enter...')
    elif c == 2:
        os.system('cls')
        suppliers_menu()
        input('Press Enter...')
    elif c == 3:
        os.system('cls')
        purchases_menu()
        input('Press Enter...')
    elif c == 4:
        os.system('cls')
        employees_menu()
        input('Press Enter...')
    elif c == 5:
        os.system('cls')
        members_menu()
        input('Press Enter...')
    elif c == 6:
        os.system('cls')
        sales_menu()
        input('Press Enter...')
    elif c == 7:
        exit(1)
    else:
        print('Wrong input')
    
    main_menu()



if __name__ == '__main__':

    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASS,
            database=DATABASE
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        exit(1)

    books = Books(mydb)

    suppliers = Suppliers(mydb)

    purchases = Purchases(mydb)

    employees = Employees(mydb)

    members = Members(mydb)

    sales = Sales(mydb)

    main_menu()
