# pharmacy-management-system
A modular CLI-based pharmacy management and billing system in Python featuring inventory tracking, automated GST billing, low stock alerts, and CSV sales logging.
##  Project Overview

The *Pharmacy Management & Billing System* streamlines daily operations for pharmaceutical stores. Built with core Python standard libraries, it eliminates manual stockkeeping errors by automating inventory updates, applying standard tax (12% GST) on medicine bills, generating formatted receipts, and tracking critical inventory shortages.

---

##  Features

- *Interactive CLI Menu*: Intuitive menu-driven control panel for seamless navigation.
- *Inventory Management*:
  - View current medicine stock, unit price, and IDs.
  - Add new medicines or restock existing stock items dynamically.
  - Automatic persistent synchronization with inventory.csv.
- *Automated Billing & Tax Calculation*:
  - Multi-item shopping cart with stock availability checks.
  - Auto-calculation of 12% GST and total net payable amount.
  - Formatted receipt output printed directly to the terminal.
- *Low-Stock Alerting System*:
  - Instant filtering for items with stock levels at or below critical threshold (<= 10 units).
- *Sales Analytics & Audit Log*:
  - Unique incremental bill generation (BILL-1001, BILL-1002, etc.).
  - Detailed sale history logging in sales.csv with total revenue summary.

---

##  Technologies Used

- *Language*: Python 3.x
- *Standard Libraries*:
  - csv — Persistent file storage for inventory and sales records.
  - os — File existence checks and path verification.
  - datetime — Timestamping sales transactions.

---

##  Repository Structure

```text
pharmacy-management-system/
│
├── main.py             # Application entry point & main menu loop
├── inventory.py        # Inventory operations (add, view, update, low-stock alert)
├── billing.py          # Cart management, GST calculation, receipt generation
├── inventory.csv       # CSV database for stock records
├── sales.csv           # CSV database for transaction logs
├── statement.md        # Problem statement & scope documentation
└── README.md           # Setup & execution instructions
