import sqlite3

DATABASE = "pizza.db"

Name = input("Welcome to Dominos! Please enter your name: ")
Addy = input("Hey " + Name + ". Please enter your address or type Pick Up: ")

# Connect to the database
connect = sqlite3.connect(DATABASE)
cursor = connect.cursor()

# Insert new customer data
sql = "INSERT INTO Customer (Name, Address) VALUES (?, ?)"
cursor.execute(sql, (Name, Addy))
connect.commit()

pizza = input("Thanks for the info " + Name + ". From the list below please select what pizza you want")
