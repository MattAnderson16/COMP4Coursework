from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import sqlite3

class AddData(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.database = db
        self.table = None
        self.type = None
        
        self.setWindowTitle("Add Data")

        self.stacked_layout = QStackedLayout()
        
        self.create_add_data_layout()
        self.stacked_layout.addWidget(self.add_data_widget)
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        self.stacked_layout.setCurrentIndex(0)
        
    def create_add_data_layout(self):
        if not hasattr(self, "add_data_layout"):
            self.table_label = QLabel("Data Table:")
            self.type_label = QLabel("Consumption Type:")
            self.data_type_label = QLabel("Data Type:")
            self.data_label = QLabel("Data:")
            self.select_table = QPushButton("None")
            self.select_consumption_type = QPushButton("None")
            self.select_data_type = QPushButton("None")
            self.data_input = QLineEdit()
            self.proceed_button = QPushButton("Proceed")
            self.back_button = QPushButton("Back")

            self.select_table_menu = QMenu()
            self.select_consumption_type_menu = QMenu()
            self.select_data_type_menu = QMenu()
            self.select_table.setMenu(self.select_table_menu)
            self.select_consumption_type.setMenu(self.select_consumption_type_menu)
            self.select_data_type.setMenu(self.select_data_type_menu)

            self.get_tables()
            self.get_consumption_types()
            self.get_table_data()

            self.consumption_a = self.consumption_types[0]
            self.consumption_b = self.consumption_types[1]
            self.consumption_c = self.consumption_types[2]

            self.select_consumption_a = self.select_consumption_type_menu.addAction(self.consumption_a[0])
            self.select_consumption_b = self.select_consumption_type_menu.addAction(self.consumption_b[0])
            self.select_consumption_c = self.select_consumption_type_menu.addAction(self.consumption_c[0])
            self.select_consumption_none = self.select_consumption_type_menu.addAction("None")

            self.user_table = self.tables[0]
            self.cost_table = self.tables[1]
            self.type_table = self.tables[4]
            self.reading_table = self.tables[5]

            self.select_user_table = self.select_table_menu.addAction(self.user_table[0])
            self.select_cost_table = self.select_table_menu.addAction(self.cost_table[0])
            self.select_type_table = self.select_table_menu.addAction(self.type_table[0])
            self.select_reading_table = self.select_table_menu.addAction(self.reading_table[0])

            self.selection_layout = QGridLayout()
            self.selection_layout.addWidget(self.table_label,1,1)
            self.selection_layout.addWidget(self.type_label,2,1)
            self.selection_layout.addWidget(self.select_table,1,2)
            self.selection_layout.addWidget(self.select_consumption_type,2,2)

            self.input_layout = QGridLayout()
            self.input_layout.addWidget(self.data_type_label,1,1)
            self.input_layout.addWidget(self.select_data_type,1,2)
            self.input_layout.addWidget(self.data_label,2,1)
            self.input_layout.addWidget(self.data_input,2,2)

            self.button_layout = QHBoxLayout()
            self.button_layout.addWidget(self.proceed_button)
            self.button_layout.addWidget(self.back_button)

            self.add_data_layout = QVBoxLayout()
            self.add_data_layout.addLayout(self.selection_layout)
            self.add_data_layout.addLayout(self.input_layout)
            self.add_data_layout.addLayout(self.button_layout)
            
            self.add_data_widget = QWidget()
            self.add_data_widget.setLayout(self.add_data_layout)

            self.proceed_button.clicked.connect(self.add_data)
            self.back_button.clicked.connect(self.close)
            
            self.select_consumption_a.triggered.connect(self.set_consumption_a)
            self.select_consumption_b.triggered.connect(self.set_consumption_b)
            self.select_consumption_c.triggered.connect(self.set_consumption_c)
            self.select_consumption_none.triggered.connect(self.set_consumption_none)

            self.select_user_table.triggered.connect(self.set_user_table)
            self.select_cost_table.triggered.connect(self.set_cost_table)
            self.select_type_table.triggered.connect(self.set_type_table)
            self.select_reading_table.triggered.connect(self.set_reading_table)           
        else:
            self.stacked_layout.setCurrentIndex(0)

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            self.tables = cursor.fetchall()

    def get_table_data(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA table_info({0})".format(self.table))
            self.data_types = cursor.fetchall()
        print(self.data_types)
    
    def get_consumption_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            self.consumption_types = cursor.fetchall()

    def add_data(self):
        pass
    
    def query(self,sql,data):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()

    def set_consumption_a(self):
        self.select_type.setText(self.consumption_a[0])
        self.type = self.consumption_a[0]

    def set_consumption_b(self):
        self.select_type.setText(self.consumption_b[0])
        self.type = self.consumption_b[0]

    def set_consumption_c(self):
        self.select_type.setText(self.consumption_c[0])
        self.type = self.consumption_c[0]

    def set_consumption_none(self):
        self.select_consumption_type.setText("None")
        self.type = None

    def set_user_table(self):
        self.select_table.setText(self.user_table[0])
        self.table = self.user_table[0]
        self.set_consumption_none()
        self.get_table_data()

    def set_cost_table(self):
        self.select_table.setText(self.cost_table[0])
        self.table = self.cost_table[0]
        self.get_table_data()

    def set_type_table(self):
        self.select_table.setText(self.type_table[0])
        self.table = self.type_table[0]
        self.set_consumption_none()
        self.get_table_data()

    def set_reading_table(self):
        self.select_table.setText(self.reading_table[0])
        self.table = self.reading_table[0]
        self.get_table_data()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddData("ConsumptionMeteringSystem.db")
    window.show()
    window.raise_()
    application.exec_()
    
