import inventory
import billing

def display_menu():
    print("""
===================================================
      PHARMACY MANAGEMENT & BILLING SYSTEM
===================================================
 [1] Create New Bill / Sale
 [2] View Medicine Inventory
 [3] Add / Restock Medicine
 [4] Check Low Stock Alerts
 [5] View Sales Transaction History
 [6] Exit Application
===================================================""")

def main():
    # Initialize files at start
    inventory.init_inventory()
    billing.init_sales()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            billing.process_billing()
        elif choice == "2":
            inventory.view_inventory()
        elif choice == "3":
            print("\n--- Add / Restock Medicine ---")
            med_id = input("Enter Medicine ID: ").strip()
            name = input("Enter Medicine Name: ").strip()
            try:
                quantity = int(input("Enter Quantity to Add: "))
                price = float(input("Enter Unit Price (INR): "))
                if quantity <= 0 or price <= 0:
                    print("[-] Quantity and price must be greater than zero.")
                    continue
                inventory.add_medicine(med_id, name, quantity, price)
            except ValueError:
                print("[-] Invalid input! Quantity must be integer and Price must be numeric.")
        elif choice == "4":
            inventory.check_low_stock(threshold=10)
        elif choice == "5":
            billing.view_sales_history()
        elif choice == "6":
            print("\n[+] Exiting Pharmacy Management System. Goodbye!")
            break
        else:
            print("[-] Invalid option selected. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
