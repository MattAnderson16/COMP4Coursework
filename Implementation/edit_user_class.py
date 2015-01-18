from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EditUser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Edit Profile")

        self.create_edit_user_layout()
        self.setCentralWidget(self.edit_user_widget)

    def create_edit_user_layout(self):
        self.select_user_label = QLabel("User:")
        self.select_user = QComboBox()

        self.new_first_name_label = QLabel("New First Name:")
        self.new_first_name_input = QLineEdit()

        self.new_last_name_label = QLabel("New Last Name:")
        self.new_last_name_input = QLineEdit()

        self.new_password_label = QLabel("New Password: ")
        self.new_password_input = QLineEdit()
        self.new_password_input.setEchoMode(2)
        
        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_user_layout = QHBoxLayout()
        self.select_user_layout.addWidget(self.select_user_label)
        self.select_user_layout.addWidget(self.select_user)

        self.new_first_name_layout = QHBoxLayout()
        self.new_first_name_layout.addWidget(self.new_first_name_label)
        self.new_first_name_layout.addWidget(self.new_first_name_input)

        self.new_last_name_layout = QHBoxLayout()
        self.new_last_name_layout.addWidget(self.new_last_name_label)
        self.new_last_name_layout.addWidget(self.new_last_name_input)

        self.new_password_layout = QHBoxLayout()
        self.new_password_layout.addWidget(self.new_password_label)
        self.new_password_layout.addWidget(self.new_password_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_user_layout = QVBoxLayout()
        self.edit_user_layout.addLayout(self.select_user_layout)
        self.edit_user_layout.addLayout(self.new_first_name_layout)
        self.edit_user_layout.addLayout(self.new_last_name_layout)
        self.edit_user_layout.addLayout(self.new_password_layout)
        self.edit_user_layout.addLayout(self.button_layout)

        self.edit_user_widget = QWidget()
        self.edit_user_widget.setLayout(self.edit_user_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_user)

    def edit_user(self):
        pass
