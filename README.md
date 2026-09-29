# Pharmacy Management & Billing System

## Overview
The **Pharmacy Management & Billing System** is a terminal-based Python application designed to automate medicine inventory control, point-of-sale billing, GST tax calculations, and sales tracking for small to medium-sized retail pharmacies. Built using standard Python libraries and persistent CSV storage, it eliminates manual register tracking, prevents unexpected stock-outs, and streamlines daily transaction management.

## Features
- **Automated Billing & Invoices**: Interactive cart management, real-time stock availability check, automatic 12% GST tax calculation, and formatted receipt output.
- **Inventory Control**: Real-time stock tracking, automatic quantity deduction upon purchase, and simple inventory restocking.
- **Low-Stock Alerts**: Automated scanning and alerting for medicines falling below a critical stock threshold ($\le 10$ units).
- **Sales Logging & Analytics**: Persistent transaction history tracking in `sales.csv` with total revenue and sales count summaries.
- **CSV Data Persistence**: Clean separation of inventory (`inventory.csv`) and transaction history (`sales.csv`).

## Technologies/Tools Used
- **Language**: Python 3.x
- **Standard Libraries**: `csv` (Data persistence), `os` (File verification), `datetime` (Transaction timestamping)
- **Data Files**: `inventory.csv`, `sales.csv`

## Steps to Install & Run the Project

### Prerequisites
- Python 3.8 or higher installed on your system.

### Setup
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/pharmacy-management-system.git](https://github.com/your-username/pharmacy-management-system.git)
   cd pharmacy-management-system
