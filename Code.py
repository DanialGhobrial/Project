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
    grabpizza()
    pizza = input("Please select the ID of the pizza you want from the list above: ")
    connect.close
    return pizza


# Getting Base flavour from user
def get_bases():
    connect = sqlite3.connect("pizza.db")
    grabbase()
    base = input("Please select the ID of the base you want from the list above: ")
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
    pizzas = c.execute("SELECT ID, Type, Price FROM Pizza;").fetchall()
    print("\nPizza ID            Pizza Flavour       Price\n")
    for pizza in pizzas:
        print(f"{pizza[0]:<20}{pizza[1]:<20}${pizza[2]:.2f}")
    connect.close()
    return pizza


# Printing all of the bases
def grabbase():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    bases = c.execute("SELECT ID, Name, Price FROM Base;").fetchall()
    print("\nBase ID            Base Flavour                            Price\n")
    for base in bases:
        print(f"{base[0]:<20}{base[1]:<40}${base[2]:.2f}")
    connect.close()
    return base


def admin():
    verify = input("Please Enter Admin Password: ")
    if verify == "1234":
        adminin()
    else:
        print("Wrong Password try again")
        admin()


# Printing all of the orders
def orders():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    orders = c.execute("SELECT * FROM Customer_order;").fetchall()
    print("\nOrder ID            Customer ID       Pizza Id      Base ID\n")
    for order in orders:
        print(f"{order[0]:<20}{order[2]:<20}{order[1]:<20}{order[3]:<20}")
    connect.close()
    return orders


# Admin Page
def adminin():
    adminmenu = input("\n Welcome To Admin Page! \n Type 1 to View All Orders \n Type 2 to add a pizza flavour \n Type 3 to add a Base Flavour")
    if adminmenu == "1":
        orders()


if __name__ == "__main__":

    while True:
        menu = input("\n Welcome To Dominos! \n Type 1 to place and order \n Type 2 to view our pizza flavours \n Type 3 to view the types of bases \n Type 4 for Admin: \n Type 5 To Leave :( \n ")

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
