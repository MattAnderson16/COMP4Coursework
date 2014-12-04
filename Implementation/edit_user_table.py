import sqlite3
from create_database import create_user_table

def display_user_menu():
    print()
    print("Edit User Table")
    print()
    print("1. Recreate the user table")
    print("2. Add data to the reading table")
    print("3. Remove data from the reading table")
    print("4. Edit data in the type table")
    print()

def get_user_menu_choice(database):
    display_user_menu()
    choice = input("Please select an option from the menu [1-4]: ")
    if choice == "1":
        create_user_table(database)
    elif choice == "2":
        ID = input("What is the ID of the user you would like to add? ")
        FirstName = input("What is the first name of the user you would like to add? ")
        LastName = input("What is the last name of the user you would like to add? ")
        Password = input("What is the password of the user you would like to add? ")
        DataList = [(ID,FirstName,LastName,Password)]
        add_data(DataList,database)

    elif choice == "3":
        ID = input("What is the ID of the user you would like to remove? ")
        remove_data((ID,),database)

    elif choice == "4":
        ID =input("What is the ID of the user you would like to change? ")
        FirstName = input("What is the new first name of the user? ")
        LastName = input("What is the new last name of the user? ")
        Password = input("What is the new password of the user? ")
        DataList = [(FirstName,LastName,Password,ID)]

def add_data(DataList,database):
    sql = "insert into User(UserID,FirstName,LastName,UserPassword) values (?,?,?,?)"
    for record in DataList:
        query(sql,database,data)

def remove_data(data,database):
    sql = "delete from User where UserID=?"
    query(sql,database,data)

def update_data(data,database):
    sql = "update User set FirstName=?, LastName=?, UserPassword=? where UserID=?"
    for record in data:
        query(sql,database,record)

def query(sql,database,data):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()
