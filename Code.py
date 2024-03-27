import sqlite3
DATABASE = "pizza.db"


# Getting user information
def get_user():
    connect = sqlite3.connect("pizza.db")
    name = input("Please enter your name: ")
    address = input("Hey " + name + ". Enter your address or type Pick Up: ")

    # Connect to the database
    connect = sqlite3.connect(DATABASE)
    cursor = connect.cursor()

    # Insert new customer data
    sql = "INSERT INTO Customer (Name, Address) VALUES (?, ?)"
    cursor.execute(sql, (name, address))
    customerid = cursor.lastrowid
    connect.commit()
    connect.close
    return customerid


# Getting pizza flavour from user
def get_pizza():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    pizzas = c.execute("SELECT * FROM Pizza;").fetchall()
    print(pizzas)
    pizza = input("Please select what pizza you want from the list above: ")
    connect.close
    return pizza


# Getting Base flavour from user
def get_bases():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    bases = c.execute("SELECT * FROM Base;").fetchall() 
    print(bases)
    base = input("Please select what base you want from the list above: ")
    connect.close
    return base


# Inserting the data into the database
def insert_data():
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    sql = "INSERT INTO Customer_order (Pizza_id, Customer_id, Base_id) VALUES (?, ?, ?)"
    cursor.execute(sql, (pizza, customerid, base))
    connect.commit()
    return insert_data


# Printing all of the pizzas
def grabpizza():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    pizzas = c.execute("SELECT Type FROM Pizza;").fetchall()
    print(pizzas)


# Printing all of the bases
def grabbase():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    bases = c.execute("SELECT Name FROM Base;").fetchall()
    print(bases)


def admin():
    verify = input("Please Enter Admin Password: ")
    if verify == "1234":
        print("welcome Admin")
    else:
        print("Wrong Password try again")


if __name__ == "__main__":

    while True:
        menu = input("Welcome To Dominos! \n Type 1 to place and order \n Type 2 to view our pizza flavours \n Type 3 to view the types of bases \n Type 4 for Admin: \n Type 5 To Leave :( \n ")

        if menu == "1":
            customerid = get_user()
            pizza = get_pizza()
            base = get_bases()
            insert_datas = insert_data()

        if menu == "2":
            pizzas = grabpizza()

        if menu == "3":
            bases = grabbase()

        if menu == "4":
            admins = admin()
        
        if menu == "5":
            break
