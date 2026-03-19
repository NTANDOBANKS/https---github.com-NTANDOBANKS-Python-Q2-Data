from Employee import EmployeeManager
from BillingAddress import CustomerManager
from Store import Store

def main():
    # Initialize our management classes
    emp_sys = EmployeeManager()
    cust_sys = CustomerManager()
    store_sys = Store()

    while True:
        print("\nWelcome to the Store Management System!")
        print("1. Manage Employees")
        print("2. Manage Customers")
        print("3. Manage Products")
        print("4. Manage Sales")
        print("0. Exit")
        
        main_choice = input("\nselect an option: ")

        if main_choice == '1':
            while True:
                print("\n\t1. Add employee")
                print("\t2. Remove employee")
                print("\t3. Display employees")
                print("\t0. Return to main menu")
                sub_choice = input("\nselect an option: ")
                
                if sub_choice == '1':
                    data = (input("Name: "), input("Surname: "), input("Cell: "), input("Email: "))
                    emp_sys.insert_person(data)
                elif sub_choice == '2':
                    emp_id = int(input("Enter Employee ID to remove: "))
                    emp_sys.remove_person(emp_id)
                elif sub_choice == '3':
                    emp_sys.display_all()
                elif sub_choice == '0':
                    break

        elif main_choice == '2':
            while True:
                print("\n\t1. Add customer")
                print("\t2. Remove customer")
                print("\t3. Display customers")
                print("\t0. Return to main menu")
                sub_choice = input("\nselect an option: ")
                
                if sub_choice == '1':
                    data = (input("Name: "), input("Surname: "), input("Cell: "), input("Email: "), input("Billing Address: "))
                    cust_sys.insert_person(data)
                elif sub_choice == '2':
                    cust_id = int(input("Enter Customer ID to remove: "))
                    cust_sys.remove_person(cust_id)
                elif sub_choice == '3':
                    cust_sys.display_all()
                elif sub_choice == '0':
                    break

        elif main_choice == '3':
            while True:
                print("\n\t1. Add a product")
                print("\t2. Remove a product")
                print("\t3. Update a product")
                print("\t4. Display all products")
                print("\t5. Sell a product")
                print("\t0. Return to main menu")
                sub_choice = input("\nselect an option: ")
                
                if sub_choice == '1':
                    store_sys.add_product(input("Name: "), float(input("Price: ")), int(input("Qty: ")))
                elif sub_choice == '2':
                    store_sys.remove_product(int(input("Product ID: ")))
                elif sub_choice == '3':
                    store_sys.update_product(int(input("ID: ")), float(input("New Price: ")), int(input("New Qty: ")))
                elif sub_choice == '4':
                    store_sys.display_products()
                elif sub_choice == '5':
                    store_sys.sell_product(int(input("Product ID: ")), int(input("Qty to sell: ")))
                elif sub_choice == '0':
                    break

        elif main_choice == '4':
            while True:
                print("\n\t1. Sell a product")
                print("\t2. Display all sales")
                print("\t0. Return to main menu")
                sub_choice = input("\nselect an option: ")
                
                if sub_choice == '1':
                    store_sys.sell_product(int(input("Product ID: ")), int(input("Qty to sell: ")))
                elif sub_choice == '2':
                    store_sys.display_sales()
                elif sub_choice == '0':
                    break

        elif main_choice == '0':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()