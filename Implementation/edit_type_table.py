import sqlite3
from create_database import create_type_table

def display_type_menu():
    print("Edit Type Table")
    print()
    print("1. Recreate the type table")
    print("2. Add data to the type table")
    print("3. Remove data from the type table")
    print("4. Edit data in the type table")
    print("5. Go back")
    print("6. Quit")
    print()

def get_type_menu_choice(database):
    display_type_menu()
    choice = input("Please select an option from the menu [1-6]: ")
    if choice == "1":
        create_type_table(database)
