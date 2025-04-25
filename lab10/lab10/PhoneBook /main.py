import psycopg2
import csv

# Connect to PostgreSQL database
connection = psycopg2.connect(
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432",
    database="phonebook"
)
cursor = connection.cursor()

# Menu prompt
def hello():
    print("What do you want to do?")
    print("1 - Insert\n2 - Update\n3 - Delete\n4 - Query")
    way = input("Choose: ")
    if way == "1":
        ins = input("How to insert? (C - Console, F - CSV): ")
        return ins
    elif way == "2":
        return "U"
    elif way == "3":
        return "D"
    elif way == "4":
        return "Q"
    else:
        print("Invalid option")
        return None

# Insert data manually via console
def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    sql = "INSERT INTO phonebook (username, phone) VALUES (%s, %s);"
    cursor.execute(sql, (username, phone))
    print("Inserted.")

    # Commit the transaction to make sure the data is saved
    connection.commit()

# Insert data from CSV file
def insert_from_csv():
    try:
        with open('file.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cursor.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", row)
            print("CSV Data Inserted.")
            # Commit the transaction to make sure the data is saved
            connection.commit()
    except FileNotFoundError:
        print("file.csv not found.")

# Delete a user
def delete():
    user = input("Enter username to delete: ")
    sql = "DELETE FROM phonebook WHERE username = %s;"
    cursor.execute(sql, (user,))
    print("Deleted if found.")
    # Commit the transaction
    connection.commit()

# Update username or phone
def update():
    print("What to update? (1 - Username, 2 - Phone)")
    choice = input("Choose: ")
    if choice == "1":
        old_user = input("Old username: ")
        new_user = input("New username: ")
        sql = "UPDATE phonebook SET username = %s WHERE username = %s;"
        cursor.execute(sql, (new_user, old_user))
    elif choice == "2":
        old_phone = input("Old phone: ")
        new_phone = input("New phone: ")
        sql = "UPDATE phonebook SET phone = %s WHERE phone = %s;"
        cursor.execute(sql, (new_phone, old_phone))
    else:
        print("Invalid option.")
        return
    print("Updated if match found.")
    # Commit the transaction
    connection.commit()

# Query data
def query():
    print("What to select? (1 - Username, 2 - Phone, 3 - All)")
    select = input("Choose: ")
    print("Filter? (1 - Yes, 2 - No)")
    isFilter = input("Choose: ")

    condition = None
    if isFilter == "1":
        condition = input("Enter condition (e.g., username = 'john'): ")

    if select == "1":
        sql = f"SELECT username FROM phonebook"
    elif select == "2":
        sql = f"SELECT phone FROM phonebook"
    else:
        sql = f"SELECT * FROM phonebook"

    if condition:
        sql += f" WHERE {condition}"

    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results.")

# Run operation
what = hello()
if what == "C":
    insert_from_console()
elif what == "F":
    insert_from_csv()
elif what == "D":
    delete()
elif what == "U":
    update()
elif what == "Q":
    query()

connection.commit()
print("✅ Success!")

# Close connection
cursor.close()
connection.close()
print("🔒 PostgreSQL connection closed.")
