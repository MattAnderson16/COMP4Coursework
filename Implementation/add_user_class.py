from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3
import re

class NewProfile(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database

        self.setWindowTitle("New Profile")

        self.create_new_user_layout()
        self.setCentralWidget(self.new_user_widget)
        self.name_pattern = "[A-Za-z]"
        self.password_pattern = "[A-Za-z0-9@#$%^&+=]{4,16}" #Regular Expression from stack overflow - http://stackoverflow.com/questions/2990654/how-to-test-a-regex-password-in-python 

    def create_new_user_layout(self):
        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()
        
        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit()
        
        self.password_label = QLabel("Password: ")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(2)

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.first_name_layout = QHBoxLayout()
        self.first_name_layout.addWidget(self.first_name_label)
        self.first_name_layout.addWidget(self.first_name_input)

        self.last_name_layout = QHBoxLayout()
        self.last_name_layout.addWidget(self.last_name_label)
        self.last_name_layout.addWidget(self.last_name_input)

        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.new_user_layout = QVBoxLayout()
        self.new_user_layout.addLayout(self.first_name_layout)
        self.new_user_layout.addLayout(self.last_name_layout)
        self.new_user_layout.addLayout(self.password_layout)
        self.new_user_layout.addLayout(self.button_layout)

        self.new_user_widget = QWidget()
        self.new_user_widget.setLayout(self.new_user_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.add_user)
        self.password_input.textChanged.connect(self.check_password)
        self.first_name_input.textChanged.connect(self.check_first_name)
        self.last_name_input.textChanged.connect(self.check_last_name)

    def check_password(self):
        password = self.password_input.text()
        if re.match(self.password_pattern,password):
            self.password_input.setStyleSheet("border: 1px solid green;")
        else:
            self.password_input.setStyleSheet("border: 1px solid red;")

    def check_first_name(self):
        name = self.first_name_input.text()
        if re.match(self.name_pattern,name):
            self.first_name_input.setStyleSheet("border: 1px solid green;")
        else:
            self.first_name_input.setStyleSheet("border: 1px solid red;")

    def check_last_name(self):
        name = self.last_name_input.text()
        if re.match(self.name_pattern,name):
            self.last_name_input.setStyleSheet("border: 1px solid green;")
        else:
            self.last_name_input.setStyleSheet("border: 1px solid red;")

    def add_user(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        password = self.password_input.text()
        if re.match(self.password_pattern,password) and re.match(self.name_pattern,first_name) and re.match(self.name_pattern,last_name):
            sql = "INSERT INTO User(FirstName,LastName,UserPassword) VALUES(?,?,?)"
            data = [first_name,last_name,password]
            self.query(data,sql)
            self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
