import psycopg2
import csv
from psycopg2 import Error

pattern_value = ""
connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mydb")

cursor = connection.cursor()

def hello():
    print("What you want?(1 - Insert, 2 - Update, 3 - Delete, 4 - Query, 5 - Pattern, 6 - Pagination):")
    way = input()
    if way == "1":
        print("What way to insert?(C - Console, F - CSV)")
        ins = input()
        return ins
    elif way == "2":
        return "U"
    elif way == "3":
        return "D"
    elif way == "4":
        return "Q"
    elif way == "5":
        global pattern_value
        print("What's pattern?")
        pattern_value = input()
        return "P"
    elif way == "6":
        return "limit"

def find_by_pattern(pattern_value):
    sql = '''SELECT find_in_phonebook(%s);'''
    cursor.execute(sql, (pattern_value,))
    record = cursor.fetchall()
    for row in record:
        print(row)

def insert_from_console():
    print("Введите данные:")
    username = input()
    phone = input()
    sql  = f'''CALL insert_or_update_user('{username}', '{phone}')'''
    cursor.execute(sql)

def insert_from_csv():
    with open('file.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            sql = f"INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)"
            cursor.execute(sql, row)

def query_phonebook(limit, offset):
    with connection.cursor() as cursor:
        query = """
        SELECT username, phone
        FROM PhoneBook
        ORDER BY username
        LIMIT %s
        OFFSET %s
        """
        cursor.execute(query, (limit, offset))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

def delete():
    print("By what u want delete?(username, phone)")
    whhh = input()
    if whhh == "username":
        user = input()
        sql = f'''DELETE FROM PhoneBook WHERE username = '{user}';'''
    elif whhh == "phone":
        phone = input()
        sql = f'''DELETE FROM PhoneBook WHERE phone = '{phone}';'''
    cursor.execute(sql)

def update():
    print("What do u want update? (1 - username, 2 - phone)")
    if input() == "1":
        print("What's old username")
        old_user = input()
        print("What's new username?")
        new_user = input()
        sql = f'''UPDATE PhoneBook SET username = '{new_user}' WHERE username = '{old_user}'; '''
    elif input() == "2":
        print("What's old phone")
        old_phone = input()
        print("What's new phone?")
        new_phone = input()
        sql = f'''UPDATE PhoneBook SET phone = '{new_phone}' WHERE phone = '{old_phone}'; '''
    cursor.execute(sql)

def query():
    print("What's column do u want? (1 - username, 2 - phone, 3 - all)")
    select = input()
    print("Do u have filter for query? (1 - YES, 2 - NO)")
    isFilter = input()
    if isFilter == "1":
        print("What's filter?")
        condition = input()
    else:
        condition = None
    if condition:
        if select == "1":
            sql = f'''SELECT username FROM PhoneBook WHERE {condition};'''
        elif select == "2":
            sql = f'''SELECT phone FROM PhoneBook WHERE {condition};'''
        else:
            sql = f'''SELECT * FROM PhoneBook WHERE {condition};'''
    else:
        if select == "1":
            sql = f'''SELECT username FROM PhoneBook;'''
        elif select == "2":
            sql = f'''SELECT phone FROM PhoneBook;'''
        else:
            sql = f'''SELECT * FROM PhoneBook;'''
    cursor.execute(sql)
    answer = cursor.fetchall()
    for row in answer:
        print(row)

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
elif what == "P":
    find_by_pattern(pattern_value)
elif what == "limit":
    print("What's limit and offset?")
    lim = int(input())
    offset = int(input())
    query_phonebook(lim, offset)


connection.commit()
print("Succes!")


if connection:
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")
