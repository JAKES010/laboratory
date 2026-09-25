-- 1. Create the table with a Primary Key
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_Name TEXT,
    Price REAL,
    Stock_Quantity INTEGER
);

-- 2. Insert our two products
INSERT INTO products (Product_Name, Price, Stock_Quantity) VALUES ('Laptop', 999.99, 15);
INSERT INTO products (Product_Name, Price, Stock_Quantity) VALUES ('Smartphone', 499.50, 30);

-- 3. Query the data
SELECT * FROM products WHERE id = 2;
