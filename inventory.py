import csv
import os

INVENTORY_FILE = "inventory.csv"
HEADERS = ["med_id", "name", "quantity", "price"]

def init_inventory():
    """Create inventory CSV file with headers if it does not exist."""
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
            # Pre-populate with sample medicines
            writer.writerow(["101", "Paracetamol 650mg", "50", "15.50"])
            writer.writerow(["102", "Amoxicillin 500mg", "8", "45.00"])
            writer.writerow(["103", "Cetirizine 10mg", "100", "8.00"])
            writer.writerow(["104", "Ibuprofen 400mg", "5", "22.00"])
            writer.writerow(["105", "Azithromycin 500mg", "20", "110.00"])

def load_inventory():
    """Load all medicines into a list of dictionaries."""
    init_inventory()
    medicines = []
    with open(INVENTORY_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["price"] = float(row["price"])
            medicines.append(row)
    return medicines

def save_inventory(medicines):
    """Write the full inventory list back to the CSV file."""
    with open(INVENTORY_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(medicines)

def add_medicine(med_id, name, quantity, price):
    """Add a new medicine or update quantity if ID already exists."""
    medicines = load_inventory()
    for med in medicines:
        if med["med_id"] == med_id:
            med["quantity"] += quantity
            med["price"] = price  # Update price if changed
            save_inventory(medicines)
            print(f"\n[+] Updated stock for '{med['name']}'. New Total: {med['quantity']} units.")
            return

    new_med = {
        "med_id": med_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }
    medicines.append(new_med)
    save_inventory(medicines)
    print(f"\n[+] Medicine '{name}' added successfully to inventory.")

def view_inventory():
    """Display all items in a formatted table."""
    medicines = load_inventory()
    print("\n" + "="*55)
    print(f"{'ID':<8}{'Medicine Name':<25}{'Stock':<10}{'Price (INR)':<10}")
    print("="*55)
    for med in medicines:
        print(f"{med['med_id']:<8}{med['name']:<25}{med['quantity']:<10}{med['price']:<10.2f}")
    print("="*55)

def get_medicine(med_id):
    """Find and return a single medicine by its ID."""
    medicines = load_inventory()
    for med in medicines:
        if med["med_id"] == med_id:
            return med
    return None

def check_low_stock(threshold=10):
    """Filter and print medicines whose quantity is below threshold."""
    medicines = load_inventory()
    low_stock = [m for m in medicines if m["quantity"] <= threshold]
    
    print("\n" + "!"*55)
    print(f"       CRITICAL LOW-STOCK REPORT (Below {threshold} units)")
    print("!"*55)
    if not low_stock:
        print(" All stock levels are sufficient.")
    else:
        print(f"{'ID':<8}{'Medicine Name':<25}{'Stock Left':<10}{'Price (INR)':<10}")
        print("-" * 55)
        for med in low_stock:
            print(f"{med['med_id']:<8}{med['name']:<25}{med['quantity']:<10}{med['price']:<10.2f}")
    print("!"*55)

def update_stock(med_id, reduce_by_qty):
    """Reduce stock count for a medicine after a successful sale."""
    medicines = load_inventory()
    for med in medicines:
        if med["med_id"] == med_id:
            med["quantity"] -= reduce_by_qty
            break
    save_inventory(medicines)
