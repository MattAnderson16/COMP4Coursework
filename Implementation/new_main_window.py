from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

from sqlconnection_class import *
from format_database_class import *
from add_reading_class import *
from edit_reading_class import *
from remove_reading_class import *
from add_user_class import *
from edit_user_class import *
from remove_user_class import *
from add_cost_class import *
from edit_cost_class import *
from delete_cost_class import *
from add_type_class import *
from edit_type_class import *
from delete_type_class import *
from table_layout_class import *
from reading_canvas_class import *
from graph_controller_class import *

import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

        self.database_open = False
        self.database = None

        self.bar_canvas = ReadingCanvas()
        self.pie_canvas = ReadingCanvas()

        self.main_layout = QStackedLayout()
        self.show_table()
        self.show_bar_chart()
        self.show_pie_chart()
        
        self.main_layout_widget = QWidget()
        self.main_layout_widget.setLayout(self.main_layout)

        self.menu_bar = QMenuBar()
        self.status_bar = QStatusBar()
        
        self.database_menu = self.menu_bar.addMenu("Database")
        self.profile_menu = self.menu_bar.addMenu("Profile")
        self.reading_menu = self.menu_bar.addMenu("Readings")
        self.preferences_menu = self.menu_bar.addMenu("Preferences")
        self.graphs_menu = self.menu_bar.addMenu("Graphs")

        self.open_database = self.database_menu.addAction("Open Database")
        self.close_database = self.database_menu.addAction("Close Database")
        self.format_database = self.database_menu.addAction("Format Database")

        self.new_profile = self.profile_menu.addAction("New Profile")
        self.edit_profile = self.profile_menu.addAction("Edit Profile")
        self.remove_profile = self.profile_menu.addAction("Remove Profile")
        self.logout = self.profile_menu.addAction("Logout")

        self.add_reading = self.reading_menu.addAction("Add Reading")
        self.edit_reading = self.reading_menu.addAction("Edit Reading")
        self.remove_reading = self.reading_menu.addAction("Remove Reading")

        self.cost_preferences = self.preferences_menu.addMenu("Costs")
        self.type_preferences = self.preferences_menu.addMenu("Types")

        self.add_cost = self.cost_preferences.addAction("Add Cost")
        self.edit_cost = self.cost_preferences.addAction("Edit Cost")
        self.remove_cost = self.cost_preferences.addAction("Remove Cost")

        self.add_type = self.type_preferences.addAction("Add Type")
        self.edit_type = self.type_preferences.addAction("Edit Type")
        self.remove_type = self.type_preferences.addAction("Remove Type")

        self.display_bar_chart = self.graphs_menu.addAction("Bar Chart")
        self.display_pie_chart = self.graphs_menu.addAction("Pie Chart")
        self.display_scatter_graph = self.graphs_menu.addAction("Scatter Graph")
        self.display_line_graph = self.graphs_menu.addAction("Line Graph")
        self.display_table = self.graphs_menu.addAction("Table")

        self.setMenuWidget(self.menu_bar)
        self.setStatusBar(self.status_bar)

        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.format_database.triggered.connect(self.clear_database)

        self.add_reading.triggered.connect(self.new_reading)
        self.edit_reading.triggered.connect(self.modify_reading)
        self.remove_reading.triggered.connect(self.clear_reading)

        self.new_profile.triggered.connect(self.new_user)
        self.edit_profile.triggered.connect(self.edit_user)
        self.remove_profile.triggered.connect(self.remove_user)

        self.add_cost.triggered.connect(self.insert_cost)
        self.edit_cost.triggered.connect(self.change_cost)
        self.remove_cost.triggered.connect(self.delete_cost)

        self.add_type.triggered.connect(self.insert_type)
        self.edit_type.triggered.connect(self.change_type)
        self.remove_type.triggered.connect(self.delete_type)

        self.display_table.triggered.connect(self.show_table)
        self.display_bar_chart.triggered.connect(self.show_bar_chart)
        self.display_pie_chart.triggered.connect(self.show_pie_chart)

        self.setCentralWidget(self.main_layout_widget)
        self.main_layout.setCurrentIndex(0)

    def open_connection(self):
        Path = QFileDialog.getOpenFileName(caption="Open Database")
        self.SQLConnection = SQLConnection(Path)
        ok = self.SQLConnection.open_database()
        if ok:
            self.database_open = True
            self.database = Path
            self.status_bar.showMessage("Database successfully opened")
            self.table_widget.update_results(self.database)           
            self.graph_controller = GraphController(self.database)
            self.get_tables()
            self.graph_data("2015-01-26")           
        else:
            self.database_open = False
            self.status_bar.showMessage("Database failed to open")

    def close_connection(self):
        if self.database_open:
            self.SQLConnection.close_database()
            self.database = None
            self.database_open = False
            self.table_widget.select_table.clear()
            self.table_widget.select_type.clear()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def clear_database(self):
        if self.database_open:
            self.format_database_window = FormatDatabase()
            self.format_database_window.show()
            self.format_database_window.raise_()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def new_reading(self):
        if self.database_open:
            self.insert_reading = AddReading(self.database)
            self.insert_reading.show()
            self.insert_reading.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def modify_reading(self):
        if self.database_open:
            self.change_reading = EditReading(self.database)
            self.change_reading.show()
            self.change_reading.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def clear_reading(self):
        if self.database_open:
            self.delete_reading = RemoveReading(self.database)
            self.delete_reading.show()
            self.delete_reading.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def new_user(self):
        if self.database_open:
            self.new_user_window = NewProfile(self.database)
            self.new_user_window.show()
            self.new_user_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def edit_user(self):
        if self.database_open:
            self.edit_user_window = EditUser(self.database)
            self.edit_user_window.show()
            self.edit_user_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def remove_user(self):
        if self.database_open:
            self.remove_user_window = RemoveUser(self.database)
            self.remove_user_window.show()
            self.remove_user_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def insert_cost(self):
        if self.database_open:
            self.add_cost_window = AddCost(self.database)
            self.add_cost_window.show()
            self.add_cost_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def change_cost(self):
        if self.database_open:
            self.modify_cost_window = EditCost(self.database)
            self.modify_cost_window.show()
            self.modify_cost_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")        
    def delete_cost(self):
        if self.database_open:
            self.delete_cost_window = DeleteCost(self.database)
            self.delete_cost_window.show()
            self.delete_cost_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")
    def insert_type(self):
        if self.database_open:
            self.add_type_window = AddType(self.database)
            self.add_type_window.show()
            self.add_type_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")
    def change_type(self):
        if self.database_open:
            self.edit_type_window = EditType(self.database)
            self.edit_type_window.show()
            self.edit_type_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def delete_type(self):
        if self.database_open:
            self.remove_type_window = DeleteType(self.database)
            self.remove_type_window.show()
            self.remove_type_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def show_table(self):
        if not hasattr(self,"table_widget"):
            self.table_widget = DisplayTable(self.database)
            self.main_layout.addWidget(self.table_widget)
        else:
            self.main_layout.setCurrentIndex(0)
        if self.database != None:
            self.table_widget.update_results(self.database)

    def show_bar_chart(self):
        if not hasattr(self,"bar_widget"):
            self.select_date_label = QLabel("Date:")
            self.select_date = QComboBox()

            self.select_table_label = QLabel("Table:")
            self.select_table = QComboBox()

            self.refresh_button = QPushButton("Refresh")

            self.combo_box_layout = QGridLayout()
            self.combo_box_layout.addWidget(self.select_table_label,1,1)
            self.combo_box_layout.addWidget(self.select_table,1,2)
            self.combo_box_layout.addWidget(self.select_date_label,2,1)
            self.combo_box_layout.addWidget(self.select_date,2,2)
            
            self.bar_layout = QVBoxLayout()
            self.bar_layout.addLayout(self.combo_box_layout)
            self.bar_layout.addWidget(self.refresh_button)
            self.bar_layout.addWidget(self.bar_canvas)
            self.bar_widget = QWidget()
            self.bar_widget.setLayout(self.bar_layout)
            self.main_layout.addWidget(self.bar_widget)

            self.select_table.currentIndexChanged.connect(self.update_bar_chart)
            self.refresh_button.clicked.connect(self.update_bar_chart)
        else:
            self.main_layout.setCurrentIndex(1)

    def show_pie_chart(self):
        if not hasattr(self,"pie_widget"):
            self.pie_layout = QVBoxLayout()
            self.pie_layout.addWidget(self.pie_canvas)
            self.pie_widget = QWidget()
            self.pie_widget.setLayout(self.pie_layout)
            self.main_layout.addWidget(self.pie_widget)
        else:
            self.main_layout.setCurrentIndex(2)

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        for table in tables:
            self.select_table.addItem(table[0])

    def get_dates(self):
        table = self.select_table.currentText()
        if table == "Reading":
            date_entry = "ReadingDate"
            get_dates = True
        elif table == "Cost":
            date_entry = "CostStartDate"
            get_dates = True
        else:
            get_dates = False

        if get_dates:
            with sqlite3.connect(self.database) as db:
                cursor = db.cursor()
                cursor.execute("SELECT {0} FROM {1}".format(date_entry,table))
                dates = cursor.fetchall()
            self.select_date.clear()
            used_dates = []
            for date in dates:
                if date[0] not in used_dates:
                    self.select_date.addItem(date[0])
                    used_dates.append(date[0])

    def graph_data(self,date):
        totals = self.graph_controller.consumption_averages(date)
        self.pie_canvas.show_pie_chart(totals,date)
        self.bar_canvas.show_bar_graph(totals,date)

    def update_bar_chart(self):
        date = self.select_date.currentText()
        self.get_dates()
        self.graph_data(date)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
