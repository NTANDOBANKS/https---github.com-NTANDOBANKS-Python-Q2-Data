import sqlite3
from PersonManager import PersonManager

class EmployeeManager(PersonManager):
    def insert_person(self, data_tuple):
   
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = """INSERT INTO Employee 
                   (employee_name, employee_surname, employee_cell_number, employee_email) 
                   VALUES (?, ?, ?, ?)"""
        cursor.execute(query, data_tuple)
        conn.commit()
        conn.close()
        print("Employee added successfully.")

    def remove_person(self, employee_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employee WHERE employee_id = ?", (employee_id,))
        conn.commit()
        conn.close()
        print(f"Employee ID {employee_id} removed.")

    def display_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        rows = cursor.fetchall()
        print("\n--- Employee List ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Email: {row[4]}")
        conn.close()