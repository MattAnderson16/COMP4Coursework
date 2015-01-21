from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class EditReading(QMainWindow):
    def __init__(self,db):
        super().__init__()
        self.database = db

        self.setWindowTitle("Edit reading")

        self.create_edit_reading_layout()

        self.setCentralWidget(self.edit_reading_widget)

    def create_edit_reading_layout(self):
        self.select_reading_label = QLabel("Select Reading")
        self.select_reading = QComboBox()

        self.get_data()

        self.new_reading_label = QLabel("New Consumption Reading:")
        self.new_reading_input = QLineEdit()

        self.new_date_label = QLabel("New Reading Date:")
        self.new_date_input = QCalendarWidget()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_reading_layout = QHBoxLayout()
        self.select_reading_layout.addWidget(self.select_reading_label)
        self.select_reading_layout.addWidget(self.select_reading)

        self.input_new_reading_layout = QGridLayout()
        self.input_new_reading_layout.addWidget(self.new_reading_label,1,1)
        self.input_new_reading_layout.addWidget(self.new_reading_input,1,2)
        self.input_new_reading_layout.addWidget(self.new_date_label,2,1)
        self.input_new_reading_layout.addWidget(self.new_date_input,2,2)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_reading_layout = QVBoxLayout()
        self.edit_reading_layout.addLayout(self.select_reading_layout)
        self.edit_reading_layout.addLayout(self.input_new_reading_layout)
        self.edit_reading_layout.addLayout(self.button_layout)

        self.edit_reading_widget = QWidget()
        self.edit_reading_widget.setLayout(self.edit_reading_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_reading)

    def get_data(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionReading FROM Reading")
            readings = cursor.fetchall()
        self.select_reading.clear()
        for reading in readings:
            self.select_reading.addItem(str(reading[0]))
        
    def edit_reading(self):
        Reading = str(self.select_reading.currentIndex + 1)
        new_reading = self.new_reading_input.text()
        new_date = self.new_date_input.selectedDate().toPyDate()
        
        sql = "UPDATE Reading SET ConsumptionReading=?,ReadingDate=? where ReadingID=?"
