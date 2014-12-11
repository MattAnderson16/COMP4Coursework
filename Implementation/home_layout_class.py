from PyQt4.QtGui import *
from PyQt4.QtCore import *

from home_tool_bar_class import *

class HomeLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.tool_bar = HomeToolBar()

        self.first_name_label = QLabel("First Name:")
        self.first_name = QLabel("-First Name-")
        self.last_name_label = QLabel("Last Name:")
        self.last_name = QLabel("-Last Name-")
        self.change_user = QPushButton("Change User")

        self.user_layout = QGridLayout()
        self.user_layout.addWidget(self.first_name_label,1,1)
        self.user_layout.addWidget(self.first_name,1,2)
        self.user_layout.addWidget(self.last_name_label,2,1)
        self.user_layout.addWidget(self.last_name,2,2)
        
        self.addWidget(self.tool_bar)
        self.addLayout(self.user_layout)
        self.addWidget(self.change_user)

if __name__ == "__main__":
    test = HomeLayout()
    print(test)
