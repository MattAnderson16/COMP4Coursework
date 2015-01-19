from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3

class DisplayTable(QWidget):
    def __init__(self, db):
        super().__init__()
        self.database = db
        self.layout = QVBoxLayout()
        self.model = None
        self.display_table_layout()
        self.setLayout(self.layout)
        
    def display_table_layout(self):
        self.table_view = QTableView()
        self.select_table = QComboBox()

        self.layout.addWidget(self.select_table)
        self.layout.addWidget(self.table_view)

    def show_results(self):
        if not self.model or not isinstance(self.model,QSqlQueryModel):
            self.model = QSqlQueryModel()
        self.model.setQuery(self.query)
        self.table_view.setModel(self.model)
        self.table_view.show()

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        for table in tables:
            self.select_table.addItem(table[0])

    def update_results(self,db):
        self.database = db
        self.get_tables()
        self.show_results()
