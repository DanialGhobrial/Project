import sqlite3
DATABASE = "pizza.db"
connect = sqlite3.connect("pizza.db")
c = connect.cursor()
pizzas = c.execute("SELECT * FROM Pizza;").fetchall()
bases = c.execute("SELECT * FROM Base;").fetchall() 


# Getting user information
def get_user():
    name = input("Welcome to Dominos! Please enter your name: ")
    address = input("Hey " + name + ". Enter your address or type Pick Up: ")

    # Connect to the database
    connect = sqlite3.connect(DATABASE)
    cursor = connect.cursor()

    # Insert new customer data
    sql = "INSERT INTO Customer (Name, Address) VALUES (?, ?)"
    cursor.execute(sql, (name, address))
    customerid = cursor.lastrowid
    connect.commit()
    return customerid


# Getting pizza flavour from user
def get_pizza():

    print(pizzas)
    pizza = input("Please select what pizza you want from the list above: ")
    return pizza


# Getting Base flavour from user
def get_bases():
    print(bases)
    base = input("Please select what base you want from the list above: ")
    return base


if __name__ == "__main__":

    customerid = get_user()
    base = get_bases
    pizza = get_pizza

    sql = "INSERT INTO Customer_order (Pizza_id, Customer_id, Base_id) VALUES (?, ?, ?)"
    cursor.execute(sql, (pizza, customerid, base))
    connect.commit()
