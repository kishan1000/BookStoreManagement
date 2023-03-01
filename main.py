
import mysql.connector
from mysql.connector import errorcode

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
    sales.find_total_sales()