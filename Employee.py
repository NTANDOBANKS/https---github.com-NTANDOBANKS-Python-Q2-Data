from PersonManager import PersonManager
class EmployeeManager(PersonManager):
    def insert_person(self, data_tuple):
        # data_tuple should be: (name, surname, cell, email)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "INSERT INTO Employee (employee_name, employee_surname, employee_cell_number, employee_email) VALUES (?, ?, ?, ?)"
        cursor.execute(query, data_tuple)
        conn.commit()
        conn.close()
        print("Employee added successfully!")

    def remove_person(self, person_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employee WHERE employee_id = ?", (person_id,))
        conn.commit()
        conn.close()
        print(f"Employee with ID {person_id} removed.")

    def display_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
        from PersonManager import PersonManager
import sqlite3