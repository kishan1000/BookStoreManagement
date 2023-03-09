
-- books table
CREATE TABLE books (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    auth VARCHAR(255),
    price INT,
    qty INT,
    PRIMARY KEY (id)
);

-- some data to insert in books table
INSERT INTO books (name, auth, price, qty) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 10, 100),
('To Kill a Mockingbird', 'Harper Lee', 12, 50),
('Pride and Prejudice', 'Jane Austen', 8, 75),
('1984', 'George Orwell', 15, 25),
('The Catcher in the Rye', 'J.D. Salinger', 9, 60);



-- employees table
CREATE TABLE employees (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    addr_line1 VARCHAR(255),
    addr_line2 VARCHAR(255),
    addr_city VARCHAR(255),
    addr_state VARCHAR(255),
    phn MEDIUMTEXT,
    date_of_joining DATE,
    salary MEDIUMTEXT,
    mgr_status CHAR(1) DEFAULT 'F',
    PRIMARY KEY (id)
);

-- some data to insert into employees table
INSERT INTO employees (name, addr_line1, addr_line2, addr_city, addr_state, phn, date_of_joining, salary, mgr_status) 
VALUES 
("John Smith", "123 Main St", "Apt 4B", "Anytown", "NY", "555-1234", "2022-01-01", "50000", "F"),
("Jane Doe", "456 Elm St", "Suite 200", "Othertown", "CA", "555-5678", "2021-06-15", "75000", "T"),
("Bob Johnson", "789 Maple Ave", NULL, "Somewhere", "TX", "555-9012", "2020-03-01", "60000", "F");



-- members table
CREATE TABLE members (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    addr_line1 varchar(255),
    addr_line2 varchar(255),
    addr_city varchar(255),
    addr_state varchar(255),
    phn mediumtext,
    beg_date date,
    end_date date,
    valid varchar(10),
    PRIMARY KEY (id)
);

-- some data to insert into members table
INSERT INTO members (name, addr_line1, addr_line2, addr_city, addr_state, phn, beg_date, end_date, valid) VALUES
('John Doe', '123 Main St', '', 'Anytown', 'CA', '555-1234', '2020-01-01', NULL, 'valid'),
('Jane Smith', '456 Oak Ave', '', 'Smallville', 'TX', '555-5678', '2021-05-01', NULL, 'valid'),
('Bob Johnson', '789 Maple Blvd', '', 'Bigtown', 'NY', '555-9012', '2022-02-15', NULL, 'valid');



-- suppliers table
CREATE TABLE suppliers (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    phn MEDIUMTEXT,
    addr_line1 VARCHAR(255),
    addr_line2 VARCHAR(255),
    addr_city VARCHAR(255),
    addr_state VARCHAR(255)
);

-- some data to insert into members table
INSERT INTO suppliers (name, phn, addr_line1, addr_line2, addr_city, addr_state) VALUES
('Supplier 1', '1234567890', '123 Main St', '', 'City 1', 'State 1'),
('Supplier 2', '2345678901', '456 Oak Ave', '', 'City 2', 'State 2'),
('Supplier 3', '3456789012', '789 Elm Blvd', '', 'City 3', 'State 3');



-- purchases table
CREATE TABLE purchases (
    ord_id int NOT NULL AUTO_INCREMENT,
    book_id int,
    sup_id int,
    qty int,
    dt_ordered date,
    eta date,
    received char(1) DEFAULT 'F',
    inv int,
    PRIMARY KEY (ord_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (sup_id) REFERENCES suppliers(id)
);

-- some data to insert into purchases table
INSERT INTO purchases (book_id, sup_id, qty, dt_ordered, eta, received, inv) VALUES
    (1, 1, 10, '2021-01-01', '2021-01-15', 'T', 101),
    (2, 2, 5, '2021-02-01', '2021-02-10', 'T', 102),
    (3, 3, 20, '2021-03-01', '2021-03-31', 'F', 100),
    (4, 1, 15, '2021-04-01', '2021-04-20', 'F', 200),
    (5, 2, 8, '2021-05-01', '2021-05-12', 'F', 300);



-- sales table
CREATE TABLE sales (
    invoice_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    book_id INT,
    qty INT,
    amount INT,
    date_s DATE,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- some data to insert into sales table
INSERT INTO sales (member_id, book_id, qty, amount, date_s) VALUES
(1, 2, 3, 1200, '2023-02-20'),
(1, 3, 1, 300, '2023-02-20'),
(2, 1, 2, 1500, '2023-02-21'),
(3, 4, 1, 800, '2023-02-22'),
(2, 5, 4, 2400, '2023-02-23');
