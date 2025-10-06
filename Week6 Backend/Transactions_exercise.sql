-- 1. Plan a database with products users and invoices and add columns necessary
DROP SCHEMA IF EXISTS sales CASCADE;
CREATE SCHEMA sales;
SET search_path TO sales;

-- ===========================
-- Table: users
-- ===========================
CREATE TABLE users (
    user_id       BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name     TEXT        NOT NULL,
    username      TEXT        NOT NULL UNIQUE,
    email         TEXT        NOT NULL UNIQUE
);

-- ===========================
-- Table: products
-- ===========================
CREATE TABLE products (
    product_id    BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku           TEXT        NOT NULL UNIQUE,
    name          TEXT        NOT NULL,
    description   TEXT,
    unit_price    NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
    stock_qty     INTEGER     NOT NULL DEFAULT 0 CHECK (stock_qty >= 0),
    is_active     BOOLEAN     NOT NULL DEFAULT TRUE,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ===========================
-- Table: invoices (header)
-- Status examples: 'PAID','RETURNED','CANCELLED'
-- ===========================
CREATE TABLE invoices (
    invoice_id    BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    invoice_no    TEXT        NOT NULL UNIQUE,
    user_id       BIGINT      NOT NULL REFERENCES users(user_id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    status        TEXT        NOT NULL DEFAULT 'PAID'
                              CHECK (status IN ('PAID','RETURNED','CANCELLED')),
    total_amount  NUMERIC(14,2) NOT NULL DEFAULT 0,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_invoices_user   ON invoices(user_id);
CREATE INDEX idx_invoices_status ON invoices(status);

-- ===========================
-- Table: invoice_items (detail)
-- ===========================
CREATE TABLE invoice_items (
    item_id      BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    invoice_id   BIGINT      NOT NULL REFERENCES invoices(invoice_id) ON UPDATE RESTRICT ON DELETE CASCADE,
    product_id   BIGINT      NOT NULL REFERENCES products(product_id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    quantity     INTEGER     NOT NULL CHECK (quantity > 0),
    unit_price   NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
    subtotal     NUMERIC(14,2) NOT NULL CHECK (subtotal >= 0)
);

CREATE INDEX idx_items_invoice  ON invoice_items(invoice_id);
CREATE INDEX idx_items_product  ON invoice_items(product_id);

-- Users
INSERT INTO users (full_name, username, email) VALUES
('Anna Gomez',     'annag',   'anna@example.com'),
('Charles Perez',  'charlesp','charles@example.com'),
('Lisa Rogers',    'lrogers', 'lisa@example.com');

-- Products
INSERT INTO products (sku, name, description, unit_price, stock_qty) VALUES
('SKU-001', 'Mechanical Keyboard', 'Keyboard with red switches',     45000.00, 25),
('SKU-002', 'Wireless Mouse',      'Optical mouse 16000 DPI',        22000.00, 40),
('SKU-003', '27" Monitor 144Hz',   'QHD 144Hz IPS panel',           185000.00, 10),
('SKU-004', 'Headphones',          'Over-ear with noise cancelling', 52000.00, 18),
('SKU-005', 'USB-C Cable',         '1m fast charging cable',          6500.00, 80);


-- 2. Create a transaction to create a sale (This is a sale for Anna Gomez, Products: 1 Headphone and 2 USB-C cables)
BEGIN TRANSACTION;

-- Check the product exists and has stock
IF EXISTS (
	SELECT 1 FROM products
	WHERE sku = 'SKU-004'
	AND stock_qty < 0
) THEN RETURN;
END IF;


-- Check if user exists
IF NOT EXISTS (
	SELECT 1 FROM users WHERE username = 'annag'
) THEN RETURN;
END IF;


-- Create the invoce
INSERT INTO invoices (invoice_no, user_id, status, total_amount) VALUES
('INV-001', 1, 'PAID', 0)


-- Add invoice lines
INSERT INTO invoice_items (invoice_id, product_id, quantity, unit_price, subtotal) 
SELECT i.invoice_id, p.product_id, 1, p.unit_price, (1 * p.unit_price)
FROM invoices i JOIN products p ON p.sku = 'SKU-004'
WHERE i.invoice_no = 'INV-001'


INSERT INTO invoice_items (invoice_id, product_id, quantity, unit_price, subtotal) 
SELECT i.invoice_id, p.product_id, 2, p.unit_price, (2 * p.unit_price)
FROM invoices i JOIN products p ON p.sku = 'SKU-005'
WHERE i.invoice_no = 'INV-001'


-- Update the total amount of the invoice
UPDATE invoices inv
SET total_amount = (
    SELECT COALESCE(SUM(it.subtotal),0)
    FROM invoice_items it
    WHERE it.invoice_id = inv.invoice_id
)
WHERE inv.invoice_no = 'INV-0001';


-- Reduce stock for the items sold
UPDATE products
SET stock_qty = stock_qty - 1
WHERE sku = 'SKU-004'


UPDATE products
SET stock_qty = stock_qty - 2
WHERE sku = 'SKU-005'

COMMIT;


