import sqlite3
from PersonManager import PersonManager

class CustomerManager(PersonManager):
    def insert_person(self, data_tuple):
       
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = """INSERT INTO Customer 
                   (customer_name, customer_surname, customer_cell_number, customer_email, billing_address) 
                   VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, data_tuple)
        conn.commit()
        conn.close()
        print("Customer added successfully.")

    def remove_person(self, customer_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customer WHERE customer_id = ?", (customer_id,))
        conn.commit()
        conn.close()
        print(f"Customer ID {customer_id} removed.")

    def display_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        rows = cursor.fetchall()
        print("\n--- Customer List ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Address: {row[5]}")
        conn.close()