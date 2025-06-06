import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS electricitybill")
mycursor.execute("CREATE DATABASE electricitybill")
mycursor.execute("USE electricitybill")

mycursor.execute("CREATE TABLE admin(Admin_ID varchar(10) primary key, Admin_First_Name varchar(30), Admin_Last_Name varchar(30), Admin_Type varchar(20), Admin_Password varchar(30))")
mycursor.execute("CREATE TABLE customer(Cust_ID int primary key, Customer_First_Name varchar(30), Customer_Last_Name varchar(30), Address_Line_1 varchar(40), Address_Line_2 varchar(40), Pincode int, Contact_Number bigint)")
mycursor.execute("CREATE TABLE account(Account_ID varchar(30) primary key, Cust_ID int, Account_Type varchar(30), Meter_No varchar(30), Cur_Meter_Reading int, Prev_Meter_Reading int)")
mycursor.execute("CREATE TABLE Tariff(Account_Type varchar(30), Tariff_Rate decimal(4,3), Fixed_Rate int)")

with open(r'C:\Users\kandu\OneDrive\Desktop\ElectricityBill\Admin.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar='|')
    for row in reader:
        mycursor.execute('INSERT INTO admin(Admin_ID, Admin_First_Name, Admin_Last_Name, Admin_Type, Admin_Password) VALUES(%s,%s,%s,%s,%s)', row)
mydb.commit()

with open(r'C:\Users\kandu\OneDrive\Desktop\ElectricityBill\Customer.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mycursor.execute('INSERT INTO customer(Cust_ID, Customer_First_Name, Customer_Last_Name, Address_Line_1, Address_Line_2, Pincode, Contact_Number) VALUES(%s,%s,%s,%s,%s,%s,%s)', row)
mydb.commit()

with open(r'C:\Users\kandu\OneDrive\Desktop\ElectricityBill\Account.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mycursor.execute('INSERT INTO account(Account_ID, Cust_ID, Account_Type, Meter_No, Cur_Meter_Reading, Prev_Meter_Reading) VALUES(%s,%s,%s,%s,%s,%s)', row)
mydb.commit()

with open(r'C:\Users\kandu\OneDrive\Desktop\ElectricityBill\Tariff.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mycursor.execute('INSERT INTO tariff(Account_Type, Tariff_Rate, Fixed_Rate) VALUES(%s,%s,%s)', row)
mydb.commit()
