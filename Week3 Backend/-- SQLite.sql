-- Insert data into tables
INSERT INTO Products (name, prod_code, price, brand, entered_date)
VALUES
('Wireless Mouse', 'P1001', 25.99, 'Logitech', '2025-08-01'),
('Mechanical Keyboard', 'P1002', 89.50, 'Corsair', '2025-08-02'),
('Gaming Monitor 27"', 'P1003', 299.99, 'ASUS', '2025-08-05'),
('External SSD 1TB', 'P1004', 129.00, 'Samsung', '2025-08-07'),
('Noise Cancelling Headphones', 'P1005', 199.90, 'Sony', '2025-08-10');

-- Insert Users
INSERT INTO Users (full_name, user_mail, registration_date)
VALUES
('Alice Johnson', 'alice.johnson@example.com', '2025-07-15'),
('Bob Martinez', 'bob.martinez@example.com', '2025-07-20'),
('Charlie Smith', 'charlie.smith@example.com', '2025-07-22'),
('Diana Evans', 'diana.evans@example.com', '2025-07-25'),
('Ethan Carter', 'ethan.carter@example.com', '2025-07-28');

-- Insert Invoice Headers (5 sales)
INSERT INTO Invoice_headers (invoice_number, sale_date, total, user_id, phone_number, employee_code)
VALUES
(10001, '2025-08-12', 115.49, 1, 88812345, 101),
(10002, '2025-08-13', 299.99, 2, 88822345, 102),
(10003, '2025-08-14', 154.99, 3, 88832345, 103),
(10004, '2025-08-15', 199.90, 4, 88842345, 104),
(10005, '2025-08-16', 389.49, 5, 88852345, 105);

-- Insert Invoice Lines (link products to invoices)
INSERT INTO Invoice_lines (amount, total, prod_id, invoice_id)
VALUES
(1, 25.99, 1, 1),   -- Wireless Mouse
(1, 89.50, 2, 1),   -- Mechanical Keyboard
(1, 299.99, 3, 2),  -- Gaming Monitor
(1, 129.00, 4, 3),  -- External SSD
(1, 25.99, 1, 3),   -- Wireless Mouse
(1, 199.90, 5, 4),  -- Headphones
(1, 199.90, 5, 5),  -- Headphones
(1, 189.59, 2, 5);  -- Keyboard (discounted example)

-- Insert Payment Methods
INSERT INTO Payment_methods (method_type, bank_name)
VALUES
('Credit Card', 'Bank of America'),
('Debit Card', 'Chase'),
('PayPal', 'N/A'),
('Wire Transfer', 'Wells Fargo'),
('Cash', 'N/A');

-- Link Invoices to Payment Methods
INSERT INTO Invoice_payment_methods (invoice_id, payment_method_id, amount)
VALUES
(1, 1, 115.49),
(2, 2, 299.99),
(3, 3, 154.99),
(4, 4, 199.90),
(5, 5, 389.49);

-- Select all Products
SELECT * FROM Products;
-- Select all products which price is grater than 5000
SELECT * FROM Products WHERE price > 5000
-- All sales of one product bt ID
SELECT * FROM Invoice_lines WHERE prod_id = 5
-- Total of all sales per product
SELECT  b.id, b.name, count(b.name) as Quantity, SUM(a.total) as Total FROM Invoice_lines a JOIN Products b WHERE a.prod_id = b.id
GROUP BY B.id
-- Select all invoices by the same buyer
SELECT invoice_number, total, user_id FROM Invoice_headers 
WHERE user_id = 4
-- Select all invoices orderd by total desc
SELECT invoice_number, total FROM Invoice_headers
ORDER BY total DESC
-- Obtain one Invoce by Invoice number
SELECT * from Invoice_headers
WHERE invoice_number = 10005

-- Added Categories table and category_id in Products table
INSERT INTO Categories (name) VALUES
('Mice'),
('Keyboards'),
('Monitors'),
('Storage'),
('Headphones & Audio');

-- Updating existing products to have categories
UPDATE Products
SET category_id = (SELECT id FROM Categories WHERE name = 'Mice')
WHERE name = 'Wireless Mouse';

UPDATE Products
SET category_id = (SELECT id FROM Categories WHERE name = 'Keyboards')
WHERE name = 'Mechanical Keyboard';

UPDATE Products
SET category_id = (SELECT id FROM Categories WHERE name = 'Monitors')
WHERE name LIKE 'Gaming Monitor%';

UPDATE Products
SET category_id = (SELECT id FROM Categories WHERE name = 'Storage')
WHERE name LIKE 'External SSD%';

UPDATE Products
SET category_id = (SELECT id FROM Categories WHERE name = 'Headphones & Audio')
WHERE name = 'Noise Cancelling Headphones';

-- Verifying products now have their respective categories
SELECT * FROM Products

-- Adding 5 more rows to each table
INSERT INTO Categories (name) VALUES
('Laptops'),
('Printers'),
('Smartphones'),
('Tablets'),
('Accessories');

INSERT INTO Products (name, prod_code, price, brand, entered_date, category_id)
VALUES
('Gaming Laptop 15"', 'P1006', 1199.99, 'MSI', '2025-08-12', (SELECT id FROM Categories WHERE name='Laptops')),
('Inkjet Printer', 'P1007', 149.00, 'HP', '2025-08-12', (SELECT id FROM Categories WHERE name='Printers')),
('Smartphone X Pro', 'P1008', 899.50, 'Samsung', '2025-08-13', (SELECT id FROM Categories WHERE name='Smartphones')),
('Android Tablet 10"', 'P1009', 399.99, 'Lenovo', '2025-08-14', (SELECT id FROM Categories WHERE name='Tablets')),
('USB-C Charger 65W', 'P1010', 45.00, 'Anker', '2025-08-14', (SELECT id FROM Categories WHERE name='Accessories'));

INSERT INTO Users (full_name, user_mail, registration_date)
VALUES
('Fiona Adams', 'fiona.adams@example.com', '2025-08-01'),
('George Brown', 'george.brown@example.com', '2025-08-02'),
('Hannah Lee', 'hannah.lee@example.com', '2025-08-03'),
('Ian Wright', 'ian.wright@example.com', '2025-08-04'),
('Julia Clark', 'julia.clark@example.com', '2025-08-05');

INSERT INTO Users (full_name, user_mail, registration_date)
VALUES
('Fiona Adams', 'fiona.adams@example.com', '2025-08-01'),
('George Brown', 'george.brown@example.com', '2025-08-02'),
('Hannah Lee', 'hannah.lee@example.com', '2025-08-03'),
('Ian Wright', 'ian.wright@example.com', '2025-08-04'),
('Julia Clark', 'julia.clark@example.com', '2025-08-05');

INSERT INTO Invoice_headers (invoice_number, sale_date, total, user_id, phone_number, employee_code)
VALUES
(10006, '2025-08-17', 1244.99, 6, 88862345, 106), -- Fiona
(10007, '2025-08-18', 1048.50, 7, 88872345, 107), -- George
(10008, '2025-08-19', 899.50, 8, 88882345, 108),  -- Hannah
(10009, '2025-08-20', 444.99, 9, 88892345, 109),  -- Ian
(10010, '2025-08-21', 45.00, 10, 88902345, 110);  -- Julia

INSERT INTO Invoice_lines (amount, total, prod_id, invoice_id)
VALUES
(1, 1199.99, (SELECT id FROM Products WHERE prod_code='P1006'), 6), -- Laptop
(1, 45.00, (SELECT id FROM Products WHERE prod_code='P1010'), 6),  -- Charger
(1, 149.00, (SELECT id FROM Products WHERE prod_code='P1007'), 7), -- Printer
(1, 899.50, (SELECT id FROM Products WHERE prod_code='P1008'), 8), -- Smartphone
(1, 399.99, (SELECT id FROM Products WHERE prod_code='P1009'), 9), -- Tablet
(1, 45.00, (SELECT id FROM Products WHERE prod_code='P1010'), 10); -- Charger

INSERT INTO Payment_methods (method_type, bank_name)
VALUES
('Credit Card', 'CitiBank'),
('Debit Card', 'Santander'),
('Gift Card', 'Amazon'),
('Crypto', 'Coinbase'),
('Mobile Payment', 'Apple Pay');

INSERT INTO Invoice_payment_methods (invoice_id, payment_method_id, amount)
VALUES
(6, 6, 1244.99), -- Fiona, CitiBank
(7, 7, 1048.50), -- George, Santander
(8, 8, 899.50),  -- Hannah, Amazon Gift Card
(9, 9, 444.99),  -- Ian, Crypto
(10, 10, 45.00); -- Julia, Apple Pay

INSERT INTO Shopping_cart (user_id, date_created)
VALUES
(6, '2025-08-15'),
(7, '2025-08-16'),
(8, '2025-08-17'),
(9, '2025-08-18'),
(10, '2025-08-19');

INSERT INTO Cart_items (cart_id, prod_id, quantity)
VALUES
(6, (SELECT id FROM Products WHERE prod_code='P1006'), 1),
(7, (SELECT id FROM Products WHERE prod_code='P1007'), 1),
(8, (SELECT id FROM Products WHERE prod_code='P1008'), 2),
(9, (SELECT id FROM Products WHERE prod_code='P1009'), 1),
(10, (SELECT id FROM Products WHERE prod_code='P1010'), 3);

INSERT INTO Reviews (prod_id, comment, rating, date, user_id)
VALUES
((SELECT id FROM Products WHERE prod_code='P1006'), 'Great laptop for gaming, fast performance.', 5, '2025-08-17', 6),
((SELECT id FROM Products WHERE prod_code='P1007'), 'Decent printer, ink is expensive.', 3, '2025-08-18', 7),
((SELECT id FROM Products WHERE prod_code='P1008'), 'Excellent phone, love the camera.', 5, '2025-08-19', 8),
((SELECT id FROM Products WHERE prod_code='P1009'), 'Good tablet for reading and light work.', 4, '2025-08-20', 9),
((SELECT id FROM Products WHERE prod_code='P1010'), 'Charger works fast but gets warm.', 4, '2025-08-21', 10);

-- Select Product name wich contains "Apple" in its name
SELECT name from Products
WHERE name LIKE "%Apple%"

-- Select the 5 most expensive products
SELECT * FROM Products
ORDER BY price DESC LIMIT 5

-- Select Invoices where there are no phone number
SELECT * FROM Invoice_headers
WHERE phone_number = NULL

-- Select an invoice by ID
SELECT * FROM Invoice_headers
WHERE id = 4

-- Now I need to add quantity to table Products as per exercise requirements
ALTER TABLE Products
ADD COLUMN quantity INTEGER DEFAULT 100

SELECT * FROM Products

-- Update quantity to 0 for products which price <= 0
UPDATE Products
SET quantity = 0
WHERE price <= 0

-- Increase price by 100 for all products which quantity is lower than 10
UPDATE Products
SET price = price + 100
WHERE quantity < 10

-- Decrease the quantity of a specific product
UPDATE Products
SET quantity = quantity - 1
WHERE ID = 2


SELECT * FROM products ORDER BY id ASC LIMIT 10
