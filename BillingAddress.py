from PersonManager import PersonManager
class CustomerManager(PersonManager):
    def insert_person(self, data_tuple):
        # data_tuple: (name, surname, cell, email, address)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "INSERT INTO Customer (customer_name, customer_surname, customer_cell_number, customer_email, billing_address) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, data_tuple)
        conn.commit()
        conn.close()
        print("Customer added successfully!")

    def remove_person(self, person_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customer WHERE customer_id = ?", (person_id,))
        conn.commit()
        conn.close()
        print(f"Customer with ID {person_id} removed.")

    def display_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
        from PersonManager import PersonManager
import sqlite3