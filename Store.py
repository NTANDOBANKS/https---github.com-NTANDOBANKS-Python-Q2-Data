import sqlite3
from datetime import date

class Store:
    def __init__(self, db_name="london_roots.db"):
        self.db_name = db_name

    def add_product(self, name, price, qty):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Product (product_name, product_price, product_quantity) VALUES (?, ?, ?)", 
                       (name, price, qty))
        conn.commit()
        conn.close()
        print(f"Product '{name}' added.")

    def remove_product(self, product_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Product WHERE product_id = ?", (product_id,))
        conn.commit()
        conn.close()
        print(f"Product {product_id} removed.")

    def update_product(self, product_id, price, qty):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE Product SET product_price = ?, product_quantity = ? WHERE product_id = ?", 
                       (price, qty, product_id))
        conn.commit()
        conn.close()
        print("Product updated.")

    def display_products(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product")
        rows = cursor.fetchall()
        print("\n--- Inventory ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Price: R{row[2]} | Stock: {row[3]}")
        conn.close()

    def sell_product(self, product_id, qty_to_sell):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, product_price, product_quantity FROM Product WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        if not product:
            print("Error: Product not found.")
        elif product[2] <= 0:
            print(f"Error: {product[0]} is out of stock.")
        elif product[2] < qty_to_sell:
            print(f"Error: Not enough stock. Available: {product[2]}")
        else:
            new_qty = product[2] - qty_to_sell
            total = product[1] * qty_to_sell
            today = date.today().strftime("%Y-%m-%d")
            
            cursor.execute("UPDATE Product SET product_quantity = ? WHERE product_id = ?", (new_qty, product_id))
            cursor.execute("INSERT INTO Sales (sale_date, product_name, sale_total) VALUES (?, ?, ?)", 
                           (today, product[0], total))
            conn.commit()
            print(f"Sold {qty_to_sell}x {product[0]} for R{total}")
        conn.close()

    def display_sales(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sales")
        rows = cursor.fetchall()
        print("\n--- Sales History ---")
        for row in rows:
            print(f"Sale ID: {row[0]} | Date: {row[1]} | Item: {row[2]} | Total: R{row[3]}")
        conn.close()