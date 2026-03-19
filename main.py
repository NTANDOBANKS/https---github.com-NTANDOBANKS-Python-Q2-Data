from Employee import EmployeeManager
from BillingAddress import CustomerManager
from Inventory import InventoryManager

def main_menu():
    emp_sys = EmployeeManager()
    cust_sys = CustomerManager()
    inv_sys = InventoryManager()

    while True:
        print("\n--- London Roots Management System ---")
        print("1. Add Employee")
        print("2. Add Customer")
        print("3. Add Product to Inventory")
        print("4. Sell a Product (Record Sale)")
        print("5. Display All Employees")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            surname = input("Surname: ")
            cell = input("Cell: ")
            email = input("Email: ")
            emp_sys.insert_person((name, surname, cell, email))

        elif choice == '2':
            name = input("Name: ")
            surname = input("Surname: ")
            cell = input("Cell: ")
            email = input("Email: ")
            address = input("Billing Address: ")
            cust_sys.insert_person((name, surname, cell, email, address))

        elif choice == '3':
            name = input("Product Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            inv_sys.add_product(name, price, qty)

        elif choice == '4':
            prod_id = int(input("Enter Product ID to sell: "))
            qty = int(input("Enter Quantity to sell: "))
            inv_sys.sell_product(prod_id, qty)

        elif choice == '5':
            print("\n--- Current Employees ---")
            emp_sys.display_all()

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()