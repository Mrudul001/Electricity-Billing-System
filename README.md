# ⚡ Electricity Bill Management System

A GUI-based desktop application to manage and automate electricity billing, built using **Python**, **Tkinter**, **MySQL**, and **FPDF**. This system supports customer and admin modules, including account management, billing computation, tariff application, and PDF bill generation.

---

## 📁 Project Structure

ElectricityBillSystem/
├── Adminpage.py # Admin dashboard for customer/account management
├── Customer Details.py # Customer dashboard for billing & invoice
├── DatabseDumping.py # Script to create and populate database from CSV
├── Frontend.py # Main GUI launcher with admin/customer login
├── Account.csv # Account table data
├── Admin.csv # Admin user data
├── Customer.csv # Customer data
├── Tariff.csv # Tariff rate info


## 🔧 Tech Stack

- **Python 3.x**
- **Tkinter / Themed Tkinter (ttkthemes)** – for GUI
- **MySQL** – for backend database
- **FPDF** – for generating bills in PDF format
- **CSV** – to load data into the database


## 🧩 Modules Overview

### 🔹 1. Frontend (`Frontend.py`)
- Entry point to the application.
- Contains:
  - **Admin login** (calls `Adminpage.py`)
  - **Customer login** (calls `Customer Details.py`)

### 🔹 2. Admin Dashboard (`Adminpage.py`)
- Full CRUD interface for:
  - Customers
  - Accounts
- Features:
  - Add/update/delete customer and account records
  - Search by customer ID
  - Tkinter `Treeview` to display data

### 🔹 3. Customer Dashboard (`Customer Details.py`)
- Input: Customer ID, Account ID, Meter Number
- Features:
  - View account details
  - Calculate bill based on meter reading and tariff
  - Tax & total bill calculation
  - Generate PDF invoice
  - Simulated payment
  - Option to request data update

### 🔹 4. Database Setup (`DatabseDumping.py`)
- Creates the following tables:
  - `admin`
  - `customer`
  - `account`
  - `tariff`
- Loads data from respective `.csv` files.
- Requires file paths to be updated based on your system (currently hardcoded).

---

## 🛠️ Setup Instructions

### 1. 📦 Requirements

Install required libraries:

pip install mysql-connector-python fpdf ttkthemes
Ensure MySQL is installed and running with:

user: root

password: admin (or update in code accordingly)

2. 🗂️ Load the Database
Update file paths in DatabseDumping.py if needed, then run:

python DatabseDumping.py
3. ▶️ Launch the App

python Frontend.py
🔐 Default Login
You can modify or check admin login credentials in Admin.csv.

Example:


Admin_ID, First_Name, Last_Name, Type, Password
admin01, Ravi, Kumar, Superadmin, admin123
💰 Billing Logic
Units Used = Current Reading - Previous Reading

Net Bill = Units × ₹0.13

Tax = 3% of Net Bill

Total Bill = Fixed Rate + Net Bill + Tax + (Tariff × Net Bill)

All this is displayed in the customer panel and exported to a PDF bill.

🧠 Future Enhancements
Add authentication hashing

Email/SMS integration for bill notifications

Web-based interface using Django or Flask

Monthly usage graph/chart

Mobile responsive UI
