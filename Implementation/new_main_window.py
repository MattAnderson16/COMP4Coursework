from PyQt4.QtGui import *
from PyQt4.QtCore import *

from add_reading_class import *
from edit_reading_class import *
from remove_reading_class import *
from add_user_class import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

        self.menu_bar = QMenuBar()
        self.status_bar = QStatusBar()

        self.profile_menu = self.menu_bar.addMenu("Profile")
        self.reading_menu = self.menu_bar.addMenu("Readings")
        self.preferences_menu = self.menu_bar.addMenu("Preferences")
        self.graphs_menu = self.menu_bar.addMenu("Graphs")

        self.new_profile = self.profile_menu.addAction("New Profile")
        self.edit_profile = self.profile_menu.addAction("Edit Profile")
        self.remove_profile = self.profile_menu.addAction("Remove Profile")
        self.logout = self.profile_menu.addAction("Logout")

        self.add_reading = self.reading_menu.addMenu("Add Reading")
        self.edit_reading = self.reading_menu.addMenu("Edit Reading")
        self.remove_reading = self.reading_menu.addMenu("Remove Reading")
        
        self.add_electric = self.add_reading.addAction("Add Electric")
        self.add_gas = self.add_reading.addAction("Add Gas")
        self.add_water = self.add_reading.addAction("Add Water")
        
        self.edit_electric = self.edit_reading.addAction("Edit Electric")
        self.edit_gas = self.edit_reading.addAction("Edit Gas")
        self.edit_water = self.edit_reading.addAction("Edit Water")
        
        self.remove_electric = self.remove_reading.addAction("Remove Electric")
        self.remove_gas = self.remove_reading.addAction("Remove Gas")
        self.remove_water = self.remove_reading.addAction("Remove Water")

        self.cost_preferences = self.preferences_menu.addMenu("Costs")
        self.type_preferences = self.preferences_menu.addMenu("Types")

        self.electricity_cost = self.cost_preferences.addAction("Add Electricity Cost")
        self.gas_cost = self.cost_preferences.addAction("Add Gas Cost")
        self.water_cost = self.cost_preferences.addAction("Add Water Cost")

        self.add_type = self.type_preferences.addAction("Add Type")
        self.edit_type = self.type_preferences.addAction("Edit Type")
        self.remove_type = self.type_preferences.addAction("Remove Type")

        self.bar_chart = self.graphs_menu.addAction("Bar Chart")
        self.pie_chart = self.graphs_menu.addAction("Pie Chart")
        self.scatter_graph = self.graphs_menu.addAction("Scatter Graph")
        self.graph_4 = self.graphs_menu.addAction("Graph 4")
        self.graph_5 = self.graphs_menu.addAction("Graph 5")

        self.setMenuWidget(self.menu_bar)
        self.setStatusBar(self.status_bar)

        self.add_electric.triggered.connect(self.add_electric_reading)
        self.add_gas.triggered.connect(self.add_gas_reading)
        self.add_water.triggered.connect(self.add_water_reading)

        self.edit_electric.triggered.connect(self.edit_electric_reading)
        self.edit_gas.triggered.connect(self.edit_gas_reading)
        self.edit_water.triggered.connect(self.edit_water_reading)

        self.new_profile.triggered.connect(self.new_user)
        self.remove_electric.triggered.connect(self.remove_electric_reading)
        self.remove_gas.triggered.connect(self.remove_gas_reading)
        self.remove_water.triggered.connect(self.remove_water_reading)

    def add_electric_reading(self):
        self.insert_reading = AddReading("Electric")
        self.insert_reading.show()
        self.insert_reading.raise_()

    def add_gas_reading(self):
        self.insert_reading = AddReading("Gas")
        self.insert_reading.show()
        self.insert_reading.raise_()

    def add_water_reading(self):
        self.insert_reading = AddReading("Water")
        self.insert_reading.show()
        self.insert_reading.raise_()

    def edit_electric_reading(self):
        self.change_reading = EditReading("Electric")
        self.change_reading.show()
        self.change_reading.raise_()

    def edit_gas_reading(self):
        self.change_reading = EditReading("Gas")
        self.change_reading.show()
        self.change_reading.raise_()

    def edit_water_reading(self):
        self.change_reading = EditReading("Water")
        self.change_reading.show()
        self.change_reading.raise_()

    def remove_electric_reading(self):
        self.delete_reading = RemoveReading("Electric")
        self.delete_reading.show()
        self.delete_reading.raise_()

    def remove_gas_reading(self):
        self.delete_reading = RemoveReading("Gas")
        self.delete_reading.show()
        self.delete_reading.raise_()

    def remove_water_reading(self):
        self.delete_reading = RemoveReading("Gas")
        self.delete_reading.show()
        self.delete_reading.raise_()

    def new_user(self):
        self.new_user_window = NewProfile()
        self.new_user_window.show()
        self.new_user_window.raise_()
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
