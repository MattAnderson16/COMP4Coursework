from PyQt4.QtSql import *
from PyQt4.QtGui import *

import sqlite3

class DisplayTable(QWidget):
    def __init__(self,path):
        super().__init__()
        self.path = path
        self.db = None
        
        self.model = QSqlQueryModel()
        self.create_table_layout()

    def create_table_layout(self):
        self.table_view = QTableView()
        self.select_table_label = QLabel("Select Table:")
        self.select_table = QComboBox()
        self.select_type_label = QLabel("Select Type:")
        self.select_type = QComboBox()

        self.select_table_layout = QHBoxLayout()
        self.select_table_layout.addWidget(self.select_table_label)
        self.select_table_layout.addWidget(self.select_table)

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.select_type_label)
        self.select_type_layout.addWidget(self.select_type)

        self.table_layout = QVBoxLayout()
        self.table_layout.addLayout(self.select_table_layout)
        self.table_layout.addLayout(self.select_type_layout)
        self.table_layout.addWidget(self.table_view)

        self.setLayout(self.table_layout)
        
        self.select_table.currentIndexChanged.connect(self.update_table_view)

    def open_database(self):
        if self.db:
            self.close_database()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        path = self.path
        self.db.setDatabaseName(path)
        ok = self.db.open()
        return ok

    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self, event):
        self.close_database()
    
    def get_types(self):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            types = cursor.fetchall()
        self.select_type.clear()
        for Type in types:
            self.select_type.addItem(Type[0])
    
    def get_tables(self):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        for table in tables:
            self.select_table.addItem(table[0])

    def display_table(self,table):
        model = QSqlTableModel()
        model.setTable(self.db.tables()[table])
        model.select()

        self.table_view.setModel(model)
        self.table_view.show()

    def update_table_view(self):
        table = self.select_table.currentIndex()
        self.display_table(table)
        
