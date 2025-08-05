pip install mysql-connector-python

import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",             
    password="",             
    database="food_delivery"
)
cursor = conn.cursor()

# Register new user
def register_user():
    print("\n--- Register New User ---")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    cursor.execute("SELECT * FROM Users WHERE phone = %s", (phone,))
    if cursor.fetchone():
        print("User already registered!\n")
    else:
        cursor.execute("INSERT INTO Users (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("User registered successfully!\n")

# View menu
def view_menu():
    print("\n--- MENU ---")
    cursor.execute("SELECT * FROM Menu")
    menu = cursor.fetchall()
    for item in menu:
        print(f"{item[0]}. {item[1]} - ₹{item[2]}")
    print()

# Place an order
def place_order():
    print("\n--- Place an Order ---")
    phone = input("Enter your phone number: ")

    cursor.execute("SELECT user_id FROM Users WHERE phone = %s", (phone,))
    user = cursor.fetchone()

    if not user:
        print("User not found. Please register first.")
        return

    user_id = user[0]
    view_menu()
    item_id = int(input("Enter the Item ID you want to order: "))
    quantity = int(input("Enter quantity: "))

    cursor.execute("INSERT INTO Orders (user_id, item_id, quantity) VALUES (%s, %s, %s)",
                   (user_id, item_id, quantity))
    conn.commit()
    print("Order placed successfully!\n")

# View user orders
def view_my_orders():
    print("\n--- View My Orders ---")
    phone = input("Enter your phone number: ")

    cursor.execute("SELECT user_id FROM Users WHERE phone = %s", (phone,))
    user = cursor.fetchone()

    if not user:
        print("User not found.")
        return

    user_id = user[0]
    cursor.execute('''
        SELECT Orders.order_id, Menu.item_name, Orders.quantity, Menu.price,
               Orders.quantity * Menu.price AS total
        FROM Orders
        JOIN Menu ON Orders.item_id = Menu.item_id
        WHERE Orders.user_id = %s
    ''', (user_id,))

    orders = cursor.fetchall()
    if not orders:
        print("No orders found.")
    else:
        for o in orders:
            print(f"Order #{o[0]}: {o[2]} x {o[1]} → ₹{o[4]}")
    print()

# Main menu
def main():
    while True:
        print("==== FOOD DELIVERY APP ====")
        print("1. Register as New User")
        print("2. View Menu")
        print("3. Place an Order")
        print("4. View My Orders")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            view_menu()
        elif choice == '3':
            place_order()
        elif choice == '4':
            view_my_orders()
        elif choice == '5':
            print("Thank you for using the app. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
conn.close()

