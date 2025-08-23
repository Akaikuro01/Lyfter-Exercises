-- SQLite
CREATE TABLE Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(30) NOT NULL,
    prod_code varchar(10) NOT NULL,
    price float NOT NULL,
    brand varchar(20) NOT NULL,
    entered_date varchar(10) NOT NULL
);


CREATE TABLE Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name varchar(50) NOT NULL,
    user_mail varchar(50) NOT NULL,
    registration_date varchar(10) NOT NULL
);


CREATE TABLE Invoice_headers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number int NOT NULL,
    sale_date varchar(10) NOT NULL,
    total float NOT NULL,
    user_id varchar(50) REFERENCES Users(id)
);


CREATE TABLE Invoice_lines(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount SMALLINT NOT NULL,
    total float NOT NULL,
    prod_id int REFERENCES Products(id),
    invoice_id REFERENCES Invoice_headers(id)
);


CREATE TABLE Payment_methods(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type varchar(20),
    bank_name varchar(30)
);


CREATE TABLE Invoice_payment_methods(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id REFERENCES Invoice_headers(id),
    payment_method_id REFERENCES payment_methods(id),
    amount float NOT NULL
);


CREATE TABLE Shopping_cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id REFERENCES Users(id),
    date_created varchar(10)
);


CREATE TABLE Cart_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id REFERENCES Shopping_Cart(id),
    prod_id REFERENCES Products(id),
    quantity SMALLINT NOT NULL
);

CREATE TABLE Reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prod_id INTEGER REFERENCES Products(id),
    comment varchar(255) NULL,
    rating smallint NOT NULL,
    date varchar(10) NOT NULL,
    user_id REFERENCES Users(id)
);

CREATE TABLE Categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(30) NOT NULL UNIQUE 
);

ALTER TABLE Invoice_headers
ADD COLUMN phone_number BIGINT DEFAULT 12345678

ALTER TABLE Invoice_headers
ADD COLUMN employee_code INTEGER DEFAULT 0

ALTER TABLE Products
ADD COLUMN category_id INTEGER NULL