import sqlite3

DATABASE = "pizza.db"

# Getting user information
def get_user(name=None, address=None):
    if name is None:
        name = input("Please enter your name: ")
    if address is None:
        address = input("Hey " + name + ". Enter your address or type Pick Up: ")

    # Connect to the database
    connect = sqlite3.connect(DATABASE)
    cursor = connect.cursor()

    # Insert new customer data
    sql = "INSERT INTO Customer (Name, Address) VALUES (?, ?)"
    cursor.execute(sql, (name, address))
    customerid = cursor.lastrowid
    connect.commit()
    connect.close()
    return customerid, name, address


# Getting pizza flavour from user
def get_pizza():
    connect = sqlite3.connect("pizza.db")
    grabpizza()
    pizza = input("Please select the ID of the pizza you want from the list above: ")
    connect.close()
    return pizza


# Getting Base flavour from user
def get_bases():
    connect = sqlite3.connect("pizza.db")
    grabbase()
    base = input("Please select the ID of the base you want from the list above: ")
    connect.close()
    return base


# Inserting the data into the database and returning the order ID
def insert_data(pizza, customerid, base):
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    sql = "INSERT INTO Customer_order (Pizza_id, Customer_id, Base_id) VALUES (?, ?, ?)"
    cursor.execute(sql, (pizza, customerid, base))
    order_id = cursor.lastrowid
    connect.commit()
    connect.close()
    return order_id


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


# Admin Page
def adminin():
    admin_password = input("Please Enter Admin Password: ")
    if admin_password == "1234":
        adminmenu = input("\n Welcome To Admin Page! \n Type 1 to View All Orders \n Type 2 to Add a Pizza Flavour \n Type 3 to Add a Base Flavour \n Type 4 to Change Pizza Price \n Type 5 to Change Base Price \n")
        if adminmenu == "1":
            orders()
        elif adminmenu == "2":
            add_pizza_flavour()
        elif adminmenu == "3":
            add_base_flavour()
        elif adminmenu == "4":
            change_pizza_price()
        elif adminmenu == "5":
            change_base_price()
    else:
        print("Wrong Password. Access Denied.")


# Displaying orders
def orders():
    connect = sqlite3.connect("pizza.db")
    c = connect.cursor()
    # Joining Customer_order with Customer to get customer names and addresses
    query = """
        SELECT co.ID, p.Type AS Pizza_Type, b.Name AS Base_Name, cu.Name AS Customer_Name, cu.Address AS Customer_Address
        FROM Customer_order co
        JOIN Pizza p ON co.Pizza_id = p.ID
        JOIN Base b ON co.Base_id = b.ID
        JOIN Customer cu ON co.Customer_id = cu.ID;
    """
    orders = c.execute(query).fetchall()
    print("\nOrder ID            Pizza Type          Base Name                               Customer Name        Customer Address\n")
    for order in orders:
        print(f"{order[0]:<20}{order[1]:<20}{order[2]:<40}{order[3]:<20}{order[4]:<20}")
    connect.close()
    return orders


# Adding a new pizza flavor
def add_pizza_flavour():
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    flavour = input("Enter the new pizza flavour: ")
    price = float(input("Enter the price of the new pizza flavour: "))
    cursor.execute("INSERT INTO Pizza (Type, Price) VALUES (?, ?)", (flavour, price))
    connect.commit()
    connect.close()
    print(f"{flavour} has been added to the menu.")


# Adding a new base flavour
def add_base_flavour():
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    flavour = input("Enter the new base flavour: ")
    price = float(input("Enter the price of the new base flavour: "))
    cursor.execute("INSERT INTO Base (Name, Price) VALUES (?, ?)", (flavour, price))
    connect.commit()
    connect.close()
    print(f"{flavour} has been added to the menu.")


# Changing the price of a pizza flavour
def change_pizza_price():
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    pizza_id = input("Enter the ID of the pizza flavour you want to change the price for: ")
    new_price = float(input("Enter the new price for the pizza flavour: "))
    cursor.execute("UPDATE Pizza SET Price = ? WHERE ID = ?", (new_price, pizza_id))
    connect.commit()
    connect.close()
    print("Price updated successfully.")


# Changing the price of a base flavour
def change_base_price():
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    base_id = input("Enter the ID of the base flavour you want to change the price for: ")
    new_price = float(input("Enter the new price for the base flavour: "))
    cursor.execute("UPDATE Base SET Price = ? WHERE ID = ?", (new_price, base_id))
    connect.commit()
    connect.close()
    print("Price updated successfully.")


# Calculate total price of the ordered items
def calculate_price(pizza_id, base_id):
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    cursor.execute("SELECT Price FROM Pizza WHERE ID = ?", (pizza_id,))
    pizza_price = cursor.fetchone()[0]
    cursor.execute("SELECT Price FROM Base WHERE ID = ?", (base_id,))
    base_price = cursor.fetchone()[0]
    connect.close()
    return pizza_price + base_price


# Cancel an order by order ID
def cancel_order(order_id):
    connect = sqlite3.connect("pizza.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Customer_order WHERE ID = ?", (order_id,))
    connect.commit()
    connect.close()
    print(f"Order {order_id} has been cancelled.")


if __name__ == "__main__":

    name = None
    address = None

    while True:
        menu = input("\n Welcome To Dominos! \n Type 1 to place and order \n Type 2 to view our pizza flavours \n Type 3 to view the types of bases \n Type 4 for Admin: \n Type 5 to Cancel Order \n Type 6 To Leave :( \n ")

        if menu == "1":
            total_price = 0
            order_items = []
            while True:
                customerid, name, address = get_user(name, address)
                pizza = get_pizza()
                base = get_bases()
                order_id = insert_data(pizza, customerid, base)
                order_items.append((pizza, base))
                total_price += calculate_price(pizza, base)

                print(f"\nThanks for your order {name}! It will be ready in 15 minutes. Your order number is {order_id}.")
                print(f"Total price so far: ${total_price:.2f}")

                order_another = input("Would you like to order another pizza? (y/n): ")
                if order_another == "y" or "Y" or "Yes" or "yes":
                    break
            print(f"Your total order price is: ${total_price:.2f}. Your order number is {order_id}.")
            

        if menu == "2":
            pizzas = grabpizza()

        if menu == "3":
            bases = grabbase()

        if menu == "4":
            admins = adminin()

        if menu == "5":
            order_id = input("Enter the order ID you want to cancel: ")
            cancel_order(order_id)

        if menu == "6":
            break
