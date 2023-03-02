
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
        input()
    elif c == 2:
        books.update_price()
        input()
    elif c == 3:
        books.search()
        input()
    elif c == 4:
        books.update()
        input()
    elif c == 5:
        books.display()
        input()
    elif c == 6:
        main_menu()
    else:
        print('Wrong input')
        input()
    
    book_menu()

def sup_menu():
    pass

def pur_menu():
    pass

def emp_menu():
    pass

def mem_menu():
    pass

def sal_menu():
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
        input()
    elif c == 2:
        os.system('cls')
        sup_menu()
        input()
    elif c == 3:
        os.system('cls')
        pur_menu()
        input()
    elif c == 4:
        os.system('cls')
        emp_menu()
        input()
    elif c == 5:
        os.system('cls')
        mem_menu()
        input()
    elif c == 6:
        os.system('cls')
        sal_menu()
        input()
    elif c == 7:
        exit(1)
    else:
        print('Wrong input')
        main_menu()
    
    return


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
    # books.display()
    # books.add()
    # books.display()
    # books.update_price()
    # books.display()
    # books.search()

    suppliers = Suppliers(mydb)
    # suppliers.display()
    # suppliers.add_supplier()
    # suppliers.display()
    # suppliers.remove_supplier()
    # suppliers.search()

    purchases = Purchases(mydb)
    # books.display()
    # books.update()
    # books.display()
    # suppliers.display()
    # purchases.new_order()
    # purchases.view()
    # purchases.mark_cancel()
    # purchases.mark_reciv()

    employees = Employees(mydb)
    # employees.display()
    # employees.add_emp()
    # employees.update_salary()
    # employees.assign_mgr_state()
    # employees.get_emp_details()
    # employees.display()


    members = Members(mydb)
    # members.add_member()
    # members.diaplay()
    # members.get_member_details()
    # members.refresh()

    sales = Sales(mydb)
    # books.display()
    # members.diaplay()
    # sales.add_bill()
    # sales.find_total_sales()

    main_menu()