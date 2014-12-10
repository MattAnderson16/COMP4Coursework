from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

import sys

class add_data(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Data")

        self.table_label = QLabel("Data Table:")
        self.type_label = QLabel("Consumption Type:")
        self.select_table = QLabel("Drop down table selection")
        self.select_type = QLabel("Drop down consumption type selection")
        self.proceed_button = QPushButton("Proceed")
        self.back_button = QPushButton("Back")

        self.selection_layout = QGridLayout()
        self.selection_layout.addWidget(self.table_label,1,1)
        self.selection_layout.addWidget(self.type_label,1,2)
        self.selection_layout.addWidget(self.select_table,2,1)
        self.selection_layout.addWidget(self.select_type,2,2)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.proceed_button)
        self.button_layout.addWidget(self.back_button)

        self.add_data_layout = QVBoxLayout()
        self.add_data_layout.addLayout(self.selection_layout)
        self.add_data_layout.addLayout(self.button_layout)
        
        self.add_data_widget = QWidget()
        self.add_data_widget.setLayout(self.add_data_layout)

        self.setCentralWidget(self.add_data_widget)

        self.proceed_button.clicked.connect(self.create_new_data_layout)

        self.show()

    def create_new_data_layout(self):
        self.data_type_label = QLabel("Data type:")
        self.select_data_type = QLabel("Drop down for data type selection")
        self.data_label = QLabel("Data:")
        self.data_box = QLineEdit()

        self.input_layout = QGridLayout()
        self.input_layout.addWidget(self.data_type_label,1,1)
        self.input_layout.addWidget(self.select_data_type,1,2)
        self.input_layout.addWidget(self.data_label,2,1)
        self.input_layout.addWidget(self.data_box,2,2)

        self.new_data_layout = QVBoxLayout()
        self.new_data_layout.addLayout(self.input_layout)
