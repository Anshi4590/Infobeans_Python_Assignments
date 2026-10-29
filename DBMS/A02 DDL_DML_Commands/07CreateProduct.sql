-- QNO  7: Create and Insert into products Table
-- Columns:

-- product_id INT

-- product_name VARCHAR(100)

-- category VARCHAR(50)

-- price DECIMAL(7,2)

-- stock_quantity INT

-- supplier_name VARCHAR(100)

-- manufacture_date DATE

-- expiry_date DATE

-- Task:


USE Batch19;

CREATE TABLE product(product_id INT PRIMARY KEY AUTO_INCREMENT , product_name VARCHAR(50),category VARCHAR(50),price DECIMAL(7,2),stock_quantity INT,supplier_name VARCHAR(100),manufacture_date DATE , expiry_date DATE);


-- Insert 6 products (some with expiry dates, some without)

INSERT IGNORE INTO product( product_name,category,price,stock_quantity,supplier_name,manufacture_date,expiry_date) 
VALUES 
(1, 'Milk', 'Dairy', 60.00, 100, 'Amul Suppliers', '2026-10-01', '2026-10-20'),
(2, 'Shampoo', 'Personal Care', 180.50, 50, 'Beauty World', '2026-08-15', '2028-08-15'),
(3, 'Rice', 'Grocery', 75.00, 200, 'Fresh Farms', '2026-09-10', '2027-09-10'),
(4, 'Biscuits', 'Snacks', 30.00, 150, 'Britannia Distributors', '2026-09-20', '2027-03-20'),
(5, 'Cooking Oil', 'Grocery', 150.75, 80, 'Fortune Suppliers', '2026-07-01', '2027-07-01'),
(6, 'Toothpaste', 'Personal Care', 95.00, 60, 'Oral Care Traders', '2026-06-10', '2028-06-10');