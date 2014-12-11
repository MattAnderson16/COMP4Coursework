from PyQt4.QtGui import *
from PyQt4.QtCore import *


class HomeToolBar(QToolBar):
    def __init__(self):
        super().__init__()
        
        self.open_database = self.addAction("Open Database")
        self.close_database = self.addAction("Close Database")
        self.create_database = self.addAction("Create Database")
        self.format_database = self.addAction("Format Database")
        self.add_data = self.addAction("Add Data")
        self.remove_data = self.addAction("Remove Data")

if __name__ == "__main__":
    print("Hello")
    test = HomeToolBar()
    print(test)
