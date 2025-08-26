-- Table creation
-----------------------------------------------------
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    author_id INTEGER NULL REFERENCES authors(id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(90) NOT NULL UNIQUE
);

CREATE TABLE rents (
    id INTEGER PRIMARY KEY,
    book_id INTEGER REFERENCES books(id) 
    ON DELETE RESTRICT ON UPDATE CASCADE,
    customer_id INTEGER REFERENCES customers(id) 
    ON DELETE RESTRICT ON UPDATE CASCADE,
    state VARCHAR(10) NOT NULL
);
-----------------------------------------------------

-----------------------------------------------------
-- Data insertion
-----------------------------------------------------
INSERT INTO authors (id, name) VALUES
    (1, 'Miguel de Cervantes'),
    (2, 'Dante Alighieri'),
    (3, 'Takehiko Inoue'),
    (4, 'Akira Toriyama'),
    (5, 'Walt Disney');

INSERT INTO books (id, name, author_id) VALUES
    (1, 'Don Quijote',                 1),
    (2, 'La Divina Comedia',           2),
    (3, 'Vagabond 1-3',                3),
    (4, 'Dragon Ball 1',               4),
    (5, 'The Book of the 5 Rings',     NULL);

INSERT INTO customers (id, name, email) VALUES
    (1, 'John Doe',  'j.doe@email.com'),
    (2, 'Jane Doe',  'jane@doe.com'),
    (3, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO rents (id, book_id, customer_id, state) VALUES
    (1, 1, 2, 'Returned'),
    (2, 2, 2, 'Returned'),
    (3, 1, 1, 'On time'),
    (4, 3, 1, 'On time'),
    (5, 2, 2, 'Overdue');
-----------------------------------------------------

-----------------------------------------------------
-- Joins
-----------------------------------------------------
-- Get all books and their authors
SELECT a.name as book_name, b.name as author_name 
FROM books a JOIN authors b
WHERE a.author_id = b.id

-- Get all books without an author
SELECT a.*
FROM books AS a 
LEFT JOIN authors AS b
ON a.author_id = b.id
WHERE b.id IS NULL;

-- Get all authors which don't have books
SELECT a.*
FROM authors AS a 
LEFT JOIN books AS b
ON a.id = b.author_id
WHERE b.author_id IS NULL

-- Get all books that have been rented at some point
SELECT DISTINCT a.*
FROM books AS a
INNER JOIN rents AS b
ON a.id = b.book_id

-- Get all books that have never been rented
SELECT a.*
FROM books AS a
LEFT JOIN rents AS b
ON a.id = b.book_id
WHERE b.book_id IS NULL

-- Get all customers that have never rented a book
SELECT a.*
FROM customers AS a
LEFT JOIN rents AS b
ON a.id = b.customer_id
WHERE b.customer_id IS NULL

-- Get all books which have been rented and are in status "Overdue"
SELECT a.*, b.*
FROM books AS a
INNER JOIN rents AS b
ON a.id = b.book_id
WHERE b.state = 'Overdue'

-- Extra Exercises --

-- 1) Cross-mapping between sets and SQL
-- a) Analysis of the set operation All - Odd
-- - All = {1,2,3,4,5,6,7,8,9,10}
-- - Odd set: Odd = {1,3,5,7,9}
-- - Difference: All - Odd = {2,4,6,8,10} ← (the elements of All that are NOT in Odd)

-- b) Explain how a similar operation can be represented in SQL with JOINs
-- Using a LEFT JOIN:
-- Take all rows from the left set (All)
-- and “subtract” those that match in the right set (Odd).
-- Implementation: LEFT JOIN from All to Odd on the key,
-- and then keep the rows where the right side had no match (i.e., is NULL).

-- c) What type of JOIN would you use?
-- - LEFT JOIN + IS NULL filter on the right table.


-- 2) Grouping and cross-counting using Books, Customers, and Rents
-- Get the total number of times a customer has rented a book
SELECT a.id, a.name, COUNT(b.id) as times_rented
FROM customers AS a
INNER JOIN rents AS b
ON a.id = b.customer_id
GROUP BY a.id, a.name

-- Get the top 3 customers with more rents
SELECT a.id, a.name, COUNT(b.id) as times_rented
FROM customers AS a
INNER JOIN rents AS b
ON a.id = b.customer_id
GROUP BY a.id, a.name
ORDER BY times_rented DESC
LIMIT 3

-- 3) Queries with multiple JOINS
-- Write a SELECT with the following data: customer name, book name, author name and rent state
SELECT a.name AS customer_name, b.name AS book_name, c.name AS author_name, d.state AS rent_state
FROM rents AS d
JOIN customers AS a ON a.id = d.customer_id
JOIN books AS b ON b.id = d.book_id
LEFT JOIN authors AS c ON c.id = b.author_id;


