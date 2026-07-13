import sqlite3

conn = sqlite3.connect('CH-3/Sales_DB/sales.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS orders(
                   customer_name TEXT NOT NULL,
                   product_name TEXTT NOT NULL,
                   quantity INTEGER NOT NULL,
                   price REAL NOT NULL,
                   total REAL NOT NULL
               )
            """)

cursor.execute("""
               INSERT INTO orders(
                   customer_name, product_name, quantity, price, total
               )
               VALUES("john doe", "Laptop", 10, 1000.00, 1000.00),
               ("john smith", "Keyboard", 3, 4000.00, 4000.00)
            """)
    
conn.commit()
conn.close()
