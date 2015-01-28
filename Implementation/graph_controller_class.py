import sqlite3

class GraphController:
    def __init__(self,path):
        self.path = path

    def query(self,sql,parameters=None):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            if parameters != None:
                cursor.execute(sql,parameters)
            else:
                cursor.execute(sql)
            results = cursor.fetchall()
            return results

    def consumption_averages(self,date):
        sql = """SELECT Type.ConsumptionType,avg(Reading.ConsumptionReading) as average
                 FROM Type, Reading
                 WHERE Type.TypeID = Reading.TypeID and
                 Reading.ReadingDate = ?
                 GROUP BY Type.ConsumptionType"""
        return self.query(sql,[date])

