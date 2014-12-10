from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import*

from canvas_class import *
from sqlconnection_class import *
from add_data_class import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

        self.database_open = False

        self.tabs = QTabWidget()
        self.menu_bar = QMenuBar()
        self.tool_bar = QToolBar()
        self.status_bar = QStatusBar()

        self.database_menu = self.menu_bar.addMenu("Database")
        self.open_database = self.database_menu.addAction("Open Database")
        self.close_database = self.database_menu.addAction("Close Database")
        self.create_database = self.database_menu.addAction("Create Database")
        self.format_database = self.database_menu.addAction("Format Database")
        self.add_data = self.database_menu.addAction("Add Data")
        self.remove_data = self.database_menu.addAction("Remove Data")

        self.tool_bar.addAction(self.open_database)
        self.tool_bar.addAction(self.close_database)
        self.tool_bar.addAction(self.create_database)
        self.tool_bar.addAction(self.format_database)
        self.tool_bar.addAction(self.add_data)
        self.tool_bar.addAction(self.remove_data)

        self.setMenuWidget(self.menu_bar)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(self.status_bar)

        self.homeTab = QWidget()
        self.tab3 = QWidget()
        self.tab2 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()

        self.create_bar_layout()

        self.tabs.addTab(self.homeTab, "Home")
        self.tabs.addTab(self.tab2, "Graph 1")
        self.tabs.addTab(self.tab3, "Graph 2")
        self.tabs.addTab(self.tab4, "Graph 3")
        self.tabs.addTab(self.tab5, "Graph 4")
        self.tabs.addTab(self.tab6, "Graph 5")
        self.tabs.addTab(self.tab7, "Graph 6")
        self.tabs.addTab(self.tab8, "Graph 8")

        self.tabs.setTabShape(QTabWidget.Rounded)

        self.setCentralWidget(self.tabs)

        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.create_database.triggered.connect(self.new_database)
        self.format_database.triggered.connect(self.clear_database)
        self.add_data.triggered.connect(self.insert_data)
        self.remove_data.triggered.connect(self.delete_data)

    def create_bar_layout(self):
        if not hasattr(self,"bar_layout"):
            self.graph1_canvas = Canvas()
            self.graph1_layout = QVBoxLayout()
            self.graph1_layout.addWidget(self.graph1_canvas)
            self.tab2.setLayout(self.graph1_layout)

    def open_connection(self):
        self.status_bar.showMessage("Opening Database")
        Path = QFileDialog.getOpenFileName()
        self.SQLConnection = SQLConnection(Path)
        ok = self.SQLConnection.open_database()
        if ok:
            self.status_bar.showMessage("Database opened successfully")
            self.database_open = True
        else:
            self.status_bar.showMessage("Database failed to open")
            self.database_open = False

    def close_connection(self):
        if self.database_open == True:
            self.SQLConnection.close_database()
            self.status_bar.showMessage("Database closed successfully")
            self.database_open = False
        else:
            self.status_bar.showMessage("There is no database currently open")

    def new_database(self):
        pass

    def clear_database(self):
        pass

    def insert_data(self):
        if self.database_open == True:
            self.addData = add_data()
            self.addData
        else:
            self.status_bar.showMessage("There is no database currently open")

    def delete_data(self):
        pass
    
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

        
