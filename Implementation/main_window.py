from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

        self.tabs = QTabWidget()
        self.menu_bar = QMenuBar()
        self.tool_bar = QToolBar()

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

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()

        self.tabs.addTab(self.tab1, "Home")
        self.tabs.addTab(self.tab2, "Graph 1")
        self.tabs.addTab(self.tab3, "Graph 2")
        self.tabs.addTab(self.tab4, "Graph 3")
        self.tabs.addTab(self.tab5, "Graph 4")
        self.tabs.addTab(self.tab6, "Graph 5")
        self.tabs.addTab(self.tab7, "Graph 6")
        self.tabs.addTab(self.tab8, "Graph 8")

        self.tabs.setTabShape(QTabWidget.Rounded)

        self.setCentralWidget(self.tabs)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

        
