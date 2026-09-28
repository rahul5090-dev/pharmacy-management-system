import csv
import os
from datetime import datetime
import inventory

SALES_FILE = "sales.csv"
SALES_HEADERS = ["bill_id", "date", "customer", "subtotal", "gst_amount", "net_payable"]

def init_sales():
    """Create sales log CSV if non-existent."""
    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(SALES_HEADERS)

def generate_bill_id():
    """Create a unique incremental bill ID."""
    init_sales()
    with open(SALES_FILE, mode="r") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            return "BILL-1001"
        last_id = reader[-1][0]
        number = int(last_id.split("-")[1]) + 1
        return f"BILL-{number}"

def process_billing():
    """Interactive loop to scan items, calculate GST, print tax invoice, and save sale."""
    customer_name = input("Enter Customer Name: ").strip()
    if not customer_name:
        customer_name = "Walk-in Customer"

    cart = []
    
    while True:
        inventory.view_inventory()
        med_id = input("\nEnter Medicine ID to add to cart (or 'done' to finish): ").strip()
        
        if med_id.lower() == 'done':
            break

        med = inventory.get_medicine(med_id)
        if not med:
            print("[-] Invalid Medicine ID. Please try again.")
            continue

        try:
            qty = int(input(f"Enter quantity for '{med['name']}' (Available: {med['quantity']}): "))
            if qty <= 0:
                print("[-] Quantity must be greater than 0.")
                continue
            if qty > med["quantity"]:
                print(f"[-] Insufficient stock! Only {med['quantity']} available.")
                continue

            # Check if medicine is already added to cart
            already_in_cart = False
            for item in cart:
                if item["med_id"] == med_id:
                    if item["qty"] + qty > med["quantity"]:
                        print("[-] Cannot add. Exceeds available inventory.")
                    else:
                        item["qty"] += qty
                        item["total"] = item["qty"] * item["price"]
                        print(f"[+] Updated quantity in cart for {med['name']}.")
                    already_in_cart = True
                    break

            if not already_in_cart:
                cart.append({
                    "med_id": med_id,
                    "name": med["name"],
                    "qty": qty,
                    "price": med["price"],
                    "total": qty * med["price"]
                })
                print(f"[+] Added {qty} x {med['name']} to cart.")

        except ValueError:
            print("[-] Invalid input. Please enter numbers for quantity.")

    if not cart:
        print("\n[-] Cart is empty. Billing cancelled.")
        return

    # Calculate Totals
    subtotal = sum(item["total"] for item in cart)
    gst_rate = 0.12  # 12% GST standard on medicines
    gst_amount = subtotal * gst_rate
    net_payable = subtotal + gst_amount
    bill_id = generate_bill_id()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update Inventory CSV
    for item in cart:
        inventory.update_stock(item["med_id"], item["qty"])

    # Log to Sales CSV
    with open(SALES_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([bill_id, date_str, customer_name, f"{subtotal:.2f}", f"{gst_amount:.2f}", f"{net_payable:.2f}"])

    # Print Formatted Receipt
    print("\n" + "="*60)
    print("                HEALTHCARE PHARMACY INVOICE")
    print("="*60)
    print(f" Bill No : {bill_id:<20} Date: {date_str}")
    print(f" Customer: {customer_name}")
    print("-" * 60)
    print(f"{'Item Name':<25}{'Qty':<8}{'Unit Price':<12}{'Total':<10}")
    print("-" * 60)
    for item in cart:
        print(f"{item['name']:<25}{item['qty']:<8}{item['price']:<12.2f}{item['total']:<10.2f}")
    print("-" * 60)
    print(f"{'Subtotal:':<45} INR {subtotal:>8.2f}")
    print(f"{'GST (12%):':<45} INR {gst_amount:>8.2f}")
    print(f"{'Net Payable Amount:':<45} INR {net_payable:>8.2f}")
    print("="*60)
    print("          Thank you for visiting! Get well soon.")
    print("="*60 + "\n")

def view_sales_history():
    """Display past transaction records from sales.csv."""
    init_sales()
    print("\n" + "="*70)
    print(f"{'Bill ID':<12}{'Date & Time':<22}{'Customer':<18}{'Net Amount (INR)':<15}")
    print("="*70)
    with open(SALES_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        total_revenue = 0.0
        count = 0
        for row in reader:
            print(f"{row['bill_id']:<12}{row['date']:<22}{row['customer']:<18}{float(row['net_payable']):<15.2f}")
            total_revenue += float(row['net_payable'])
            count += 1
    print("="*70)
    print(f"Total Transactions: {count} | Total Sales Revenue: INR {total_revenue:.2f}")
    print("="*70)
