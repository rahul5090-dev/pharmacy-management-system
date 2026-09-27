# Project Statement: Pharmacy Management & Billing System

## 1. Problem Statement
Small-scale local pharmacies often rely on manual paper logbooks or disjointed systems to track medicine inventory and generate sales receipts. This manual process leads to several critical issues:
- *Frequent Stockouts*: Lack of automated low-stock tracking leads to critical life-saving medicines unexpectedly running out of stock.
- *Inaccurate Invoicing*: Manual tax (GST) and total calculations increase the potential for human arithmetic errors during customer billing.
- *Data Loss & Disorganization*: Paper records or unorganized files make tracking daily sales performance and historical transactions difficult and unreliable.

The *Pharmacy Management & Billing System* solves these problems by providing a unified, lightweight, terminal-based application that automates inventory persistence, calculates tax invoices accurately, and logs sales data seamlessly.

---

## 2. Scope of the Project
The scope of this project includes the design and implementation of a CLI application built in Python for daily pharmaceutical store operations:

- *In-Scope*:
  - Persistent CSV-based inventory storage (inventory.csv) with full CRUD-style stock management (View, Add/Restock, Stock Update).
  - Automated low-stock warning system for items falling below critical safety thresholds (<= 10 units).
  - Interactive multi-item billing system with real-time inventory validation, 12% GST calculation, and terminal receipt rendering.
  - Persistent transaction history logging (sales.csv) with incremental bill numbers (BILL-1001) and automated sales summary metrics.
- *Out-of-Scope*:
  - Graphical User Interface (GUI) components (the app strictly follows CLI executable guidelines).
  - Integration with external web payment gateways or hardware barcode scanners.
  - Multi-user authentication/role-based access management.

---

## 3. Target Users
- *Independent Pharmacists & Chemists*: Store owners needing a lightweight tool to control inventory and monitor daily revenue.
- *Pharmacy Billing Clerks*: Sales staff requiring a quick and error-free checkout system to bill walk-in customers and generate tax receipts.
- *Inventory Managers*: Staff responsible for restocking medicines and checking critical stock shortages before supplies run out.

---

## 4. High-Level Features
1. *Interactive Command-Line Control Panel*: Clean, numeric menu interface driven by main.py for standard application workflows.
2. *Persistent Inventory Tracking*: Loads and updates medicine records (med_id, name, quantity, price) saved in inventory.csv.
3. *Restocking & Item Addition*: Supports updating existing medicine quantities or adding new pharmaceutical items on the fly.
4. *Critical Low-Stock Detection*: Dedicated monitoring module that filters and displays all medicines with 10 or fewer units available.
5. *Tax-Compliant Multi-Item Billing*: Interactive cart system that verifies stock levels, applies standard 12% GST, updates inventory automatically, and displays formatted tax invoices.
6. *Sales Audit Logging & Analytics*: Tracks past transactions in sales.csv with unique bill IDs, timestamps, customer details, and overall store revenue metrics.
