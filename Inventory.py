import sqlite3

class InventoryManager:
    def __init__(self, db_name="london_roots.db"):
        self.db_name = db_name

    def add_product(self, name, price, qty):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Product (product_name, product_price, product_quantity) VALUES (?, ?, ?)", (name, price, qty))
        conn.commit()
        conn.close()
        print(f"Product {name} added to inventory.")

    def sell_product(self, product_id, qty_to_sell):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # 1. Check if we have enough stock
        cursor.execute("SELECT product_name, product_price, product_quantity FROM Product WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()
        
        if product and product[2] >= qty_to_sell:
            new_qty = product[2] - qty_to_sell
            total_price = product[1] * qty_to_sell
            
            # 2. Update Product Stock
            cursor.execute("UPDATE Product SET product_quantity = ? WHERE product_id = ?", (new_qty, product_id))
            
            # 3. Record the Sale
            from datetime import date
            cursor.execute("INSERT INTO Sales (sale_date, product_name, sale_total) VALUES (?, ?, ?)", 
                           (date.today().strftime("%Y-%m-%d"), product[0], total_price))
            
            conn.commit()
            print(f"Sold {qty_to_sell} of {product[0]}. Total: R{total_price}")
        else:
            print("Error: Not enough stock or product not found.")
            
        conn.close()