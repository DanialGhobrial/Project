import sqlite3
DATABASE = "pizza.db"
connect = sqlite3.connect("pizza.db")
c = connect.cursor()
pizzas = c.execute("SELECT * FROM Pizza;").fetchall()
bases = c.execute("SELECT * FROM Base;").fetchall()

name = input("Welcome to Dominos! Please enter your name: ")
address = input("Hey " + name + ". Enter your address or type Pick Up: ")

# Connect to the database
connect = sqlite3.connect(DATABASE)
cursor = connect.cursor()

# Insert new customer data
sql = "INSERT INTO Customer (Name, Address) VALUES (?, ?)"
cursor.execute(sql, (name, address))
connect.commit()

print(pizzas)

pizza = input("Please select what pizza you want from the list above: ")

sql = "INSERT INTO Customer_order (Pizza_id) VALUES (?)"
cursor.execute(sql, (pizza))
connect.commit()

print(bases)

base = input("Please select what base you want from the list above: ")

sql = "INSERT INTO Customer_order (Base_id) VALUES (?)"
cursor.execute(sql, (bases))
connect.commit()
