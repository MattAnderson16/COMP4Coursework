import sqlite3
from create_database import create_type_table

def display_type_menu():
    print()
    print("Edit Type Table")
    print()
    print("1. Recreate the type table")
    print("2. Add data to the type table")
    print("3. Remove data from the type table")
    print("4. Edit data in the type table")
    print()

def get_type_menu_choice(database):
    display_type_menu()
    choice = input("Please select an option from the menu [1-4]: ")
    if choice == "1":
        create_type_table(database)
    
    elif choice == "2":
        data = input("What is the consumption type you would like to add into the table? ")
        description = input("What is the description of this consumption type? ")
        ID = input("What is the ID of this data? ")
        DataList = [(ID,data,description)]
        add_data(DataList,database)

    elif choice == "3":
        data = input("What is the data you would like to remove from the type table? ")
        datadouble = (data,)
        remove_data(datadouble,database)

    elif choice == "4":
        ID = input("What is the ID of the consumption type you would like to change? ")
        Data = input("What is the new consumption type? ")
        Description = input("What is the new description? ")
        DataList = [(Data,Description,ID)]
        update_data(DataList,database)

def add_data(DataList,database):
    sql = "insert into Type(TypeID,ConsumptionType,ConsumptionTypeDescription) values (?,?,?)"
    for record in DataList:
        query(sql,database,record)

def remove_data(data,database):
    sql = "delete from Type where ConsumptionType=?"
    query(sql,database,data)

def update_data(data,database):
    sql = "update Type set ConsumptionType=?, ConsumptionTypeDescription=? where TypeID=?"
    for record in data:
        query(sql,database,record)
    
def query(sql,database,data):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()
