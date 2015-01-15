from PyQt4.QtGui import *
from PyQt4.QtCore import *

class RemoveUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove User")

        self.create_remove_user_layout()
        self.setCentralWidget(self.remove_user_widget)

    def create_remove_user_layout(self):
        self.select_user = QComboBox()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.remove_user_layout = QVBoxLayout()
        self.remove_user_layout.addWidget(self.select_user)
        self.remove_user_layout.addLayout(self.button_layout)

        self.remove_user_widget = QWidget()
        self.remove_user_widget.setLayout(self.remove_user_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.remove_user)

    def remove_user(self):
        pass
