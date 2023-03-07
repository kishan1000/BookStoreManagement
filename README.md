# This is a Book Store Management System Project

* ## It Uses MySQL as DBMS to Store All the information

* ## Database Details : -

    * DBMS : MySQL

    * DATABASE Name : `management`

    * Tables : -

        * `books`

            | Field | Type         | Null | Key | Extra          |
            |-------|--------------|------|-----|----------------|
            | id    | int          | NO   | PRI | auto_increment |
            | name  | varchar(255) | YES  |     |                |
            | auth  | varchar(255) | YES  |     |                |
            | price | int          | YES  |     |                |
            | qty   | int          | YES  |     |                |

        * `employees`

            | Column Name     | Data Type   | Null        | Key  | Extra          |
            | --------------- | ------------| ----------  | ---- | -------------- |
            | id              | int         | NO          | PRI  | auto_increment |
            | name            | varchar(255)| YES         |      |                |
            | addr_line1      | varchar(255)| YES         |      |                |
            | addr_line2      | varchar(255)| YES         |      |                |
            | addr_city       | varchar(255)| YES         |      |                |
            | addr_state      | varchar(255)| YES         |      |                |
            | phn             | mediumtext  | YES         |      |                |
            | date_of_joining | date        | YES         |      |                |
            | salary          | mediumtext  | YES         |      |                |
            | mgr_status      | char(1)     | YES         |      |                |

        * `members`

            | Column name | Data type    | Null     | Key       | Extra          |
            |-------------|--------------|----------|-----------|----------------|
            | id          | int          | NO       | PRI       | auto_increment |
            | name        | varchar(255) | YES      |           |                |
            | addr_line1  | varchar(255) | YES      |           |                |
            | addr_line2  | varchar(255) | YES      |           |                |
            | addr_city   | varchar(255) | YES      |           |                |
            | addr_state  | varchar(255) | YES      |           |                |
            | phn         | mediumtext   | YES      |           |                |
            | beg_date    | date         | YES      |           |                |
            | end_date    | date         | YES      |           |                |
            | valid       | varchar(10)  | YES      |           |                |

        * `purchases`

            | Column Name | Data Type | Null       |  Key                  | Extra          |
            | ----------- | --------- | ---------- | --------------------- | -------------- |
            | ord_id      | int       | NO         | PRI                   | auto_increment |
            | book_id     | int       | YES        | FK ref(books(id))     |                |
            | sup_id      | int       | YES        | FK ref(suppliers(id)) |                |
            | qty         | int       | YES        | NO                    |                |
            | dt_ordered  | date      | YES        | NO                    |                |
            | eta         | date      | YES        | NO                    |                |
            | received    | char(1)   | YES        | NO                    |                |
            | inv         | int       | YES        | NO                    |                |

        * `suppliers`

            | Field        | Type         | Null | Key | Extra          |
            |--------------|--------------|------|-----|----------------|
            | id           | int          | NO   | PRI | auto_increment |
            | name         | varchar(255) | YES  |     |                |
            | phn          | mediumtext   | YES  |     |                |
            | addr_line1   | varchar(255) | YES  |     |                |
            | addr_line2   | varchar(255) | YES  |     |                |
            | addr_city    | varchar(255) | YES  |     |                |
            | addr_state   | varchar(255) | YES  |     |                |

        * `sales`

            | Field       | Type        | Null | Key                 | Extra          |
            |-------------|-------------|------|-------------------- |----------------|
            | invoice_id  | int         | NO   | PRI                 | auto_increment |
            | member_id   | int         | YES  | FK ref(members(id)) |                |
            | book_id     | int         | YES  | FK ref(books(id))   |                |
            | qty         | int         | YES  |                     |                |
            | amount      | int         | YES  |                     |                |
            | date_s      | date        | YES  |                     |                |

