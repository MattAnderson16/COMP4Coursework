from PyQt4.QtGui import *
from PyQt4.QtCore import *

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

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

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

        self.bar_chart = self.graphs_menu.addAction("Bar Chart")
        self.pie_chart = self.graphs_menu.addAction("Pie Chart")
        self.scatter_graph = self.graphs_menu.addAction("Scatter Graph")
        self.graph_4 = self.graphs_menu.addAction("Line Graph")
        self.graph_5 = self.graphs_menu.addAction("Table")

        self.setMenuWidget(self.menu_bar)
        self.setStatusBar(self.status_bar)

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

    def new_reading(self):
        self.insert_reading = AddReading()
        self.insert_reading.show()
        self.insert_reading.raise_()

    def modify_reading(self):
        self.change_reading = EditReading()
        self.change_reading.show()
        self.change_reading.raise_()

    def clear_reading(self):
        self.delete_reading = RemoveReading()
        self.delete_reading.show()
        self.delete_reading.raise_()

    def new_user(self):
        self.new_user_window = NewProfile()
        self.new_user_window.show()
        self.new_user_window.raise_()

    def edit_user(self):
        self.edit_user_window = EditUser()
        self.edit_user_window.show()
        self.edit_user_window.raise_()

    def remove_user(self):
        self.remove_user_window = RemoveUser()
        self.remove_user_window.show()
        self.remove_user_window.raise_()

    def insert_cost(self):
        self.add_cost_window = AddCost()
        self.add_cost_window.show()
        self.add_cost_window.raise_()

    def change_cost(self):
        self.modify_cost_window = EditCost()
        self.modify_cost_window.show()
        self.modify_cost_window.raise_()
        
    def delete_cost(self):
        self.delete_cost_window = DeleteCost()
        self.delete_cost_window.show()
        self.delete_cost_window.raise_()

    def insert_type(self):
        self.add_type_window = AddType()
        self.add_type_window.show()
        self.add_type_window.raise_()

    def change_type(self):
        self.edit_type_window = EditType()
        self.edit_type_window.show()
        self.edit_type_window.raise_()

    def delete_type(self):
        self.remove_type_window = DeleteType()
        self.remove_type_window.show()
        self.remove_type_window.raise_()
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
