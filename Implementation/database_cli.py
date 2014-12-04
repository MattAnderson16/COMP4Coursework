from create_database import *

def display_menu():
    print("Main Menu")
    print()
    print("1. (Re)Create database")
    print("2. Edit Type Table")
    print("3. Edit Reading Table")
    print("4. Edit User Table")
    print("5. Edit Cost Table")
    print("0. Quit.")
    print()

def get_menu_choice():
    display_menu()
    choice = input("Please select an option from the menu [1-5 or 0 to Quit]: ")
    if choice == "1":
        create_type_table(database)
        create_reading_table(database)
        create_user_table(database)
        create_cost_table(database)
        create_userreading_table(database)
        create_typecost_table(database)

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "0":
        Quit = True

if __name__ == "__main__":
    database = "ConsumptionMeteringSystem.db"
    Quit = False
    while not Quit:
        get_menu_choice()
