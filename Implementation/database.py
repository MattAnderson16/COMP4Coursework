import sqlite3

def create_table(database,table_name,sql):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? [Y/N]: ".format(table_name))
            response = response.lower()
            if response == "y":
                keep_table = False
                print("The table {0} will be recreated - all existing data will be lost.".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table will be kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
            print("The table {0} has been created successfully!".format(table_name))    

def create_reading_table():
    sql = """create table Reading
             (ConsumptionID integer,
             ConsumptionType text,
             ConsumptionReading real,
             ReadingDate text,
             primary key(ConsumptionID)
             foreign key(ConsumptionType) references ConsumptionType(ConsumptionType))"""
    create_table(database, "Reading", sql)

def create_consumption_type_table():
    sql = """create table ConsumptionType
             (ConsumptionType text,
             ConsumptionCostID integer,
             ConsumptionTypeDescription text,
             primary key(ConsumptionType)
             foreign key(ConsumptionType) references ConsumptionTypeInfo(ConsumptionType)
             foreign key(ConsumptionCostID) references ConsumptionCost(ConsumptionCostID))"""
    create_table(database, "ConsumptionType", sql)

def create_consumption_type_info_table():
    sql = """create table ConsumptionTypeInfo
             (ConsumptionType text,
             ConsumptionTypeDescription text,
             primary key(ConsumptionType))"""
    create_table(database, "ConsumptionTypeInfo", sql)

def create_consumption_cost_table():
    sql = """create table ConsumptionCostTable
             (ConsumptionCostID integer,
             ConsumptionCostPerUnit real,
             ConsumptionCostStartDate text,
             primary key(ConsumptionCostID))"""
    create_table(database, "ConsumptionCostTable", sql)

def create_user_table():
    sql = """create table User
             (UserID integer,
             FirstName text,
             LastName text,
             UserPassword text)"""
    create_table(database, "User", sql)
    
if __name__ == "__main__":
    database = "ConsumptionMeteringSystem.db"
    create_consumption_cost_table()
    create_consumption_type_info_table()
    create_consumption_type_table()
    create_reading_table()
    create_user_table()
    
    
