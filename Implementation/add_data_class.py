from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

import sys

class AddData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Data")
        self.stacked_layout = QStackedLayout()
        
        self.create_add_data_layout()
        self.create_new_data_layout()

        self.stacked_layout.addWidget(self.add_data_widget)
        self.stacked_layout.addWidget(self.new_data_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)

        self.setCentralWidget(self.central_widget)

        self.stacked_layout.setCurrentIndex(0)
        
    def create_add_data_layout(self):
        if not hasattr(self, "add_data_layout"):
            self.table_label = QLabel("Data Table:")
            self.type_label = QLabel("Consumption Type:")
            self.select_table = QPushButton("None")
            self.select_type = QPushButton("None")
            self.proceed_button = QPushButton("Proceed")
            self.back_button = QPushButton("Back")

            self.select_table_menu = QMenu()
            self.select_type_menu = QMenu()
            self.select_table.setMenu(self.select_table_menu)
            self.select_type.setMenu(self.select_type_menu)


            self.selection_layout = QGridLayout()
            self.selection_layout.addWidget(self.table_label,1,1)
            self.selection_layout.addWidget(self.type_label,2,1)
            self.selection_layout.addWidget(self.select_table,1,2)
            self.selection_layout.addWidget(self.select_type,2,2)

            self.button_layout = QHBoxLayout()
            self.button_layout.addWidget(self.proceed_button)
            self.button_layout.addWidget(self.back_button)

            self.add_data_layout = QVBoxLayout()
            self.add_data_layout.addLayout(self.selection_layout)
            self.add_data_layout.addLayout(self.button_layout)
            
            self.add_data_widget = QWidget()
            self.add_data_widget.setLayout(self.add_data_layout)

            self.proceed_button.clicked.connect(self.create_new_data_layout)
            self.back_button.clicked.connect(self.close)
        else:
            self.stacked_layout.setCurrentIndex(0)

    def create_new_data_layout(self):
        if not hasattr(self, "new_data_widget"):
            self.data_type_label = QLabel("Data type:")
            self.select_data_type = QPushButton("None")
            self.data_label = QLabel("Data:")
            self.data_selection = QPushButton("None")

            self.select_data_type_menu = QMenu()
            self.data_selection_menu = QMenu()
            self.select_data_type.setMenu(self.select_data_type_menu)
            self.data_selection.setMenu(self.data_selection_menu)

            self.confirm_button = QPushButton("Confirm")
            self.back_button_2 = QPushButton("Back")

            self.input_layout = QGridLayout()
            self.input_layout.addWidget(self.data_type_label,1,1)
            self.input_layout.addWidget(self.select_data_type,1,2)
            self.input_layout.addWidget(self.data_label,2,1)
            self.input_layout.addWidget(self.data_selection,2,2)

            self.create_data_button_layout = QHBoxLayout()
            self.create_data_button_layout.addWidget(self.confirm_button)
            self.create_data_button_layout.addWidget(self.back_button_2)

            self.new_data_layout = QVBoxLayout()
            self.new_data_layout.addLayout(self.input_layout)
            self.new_data_layout.addLayout(self.create_data_button_layout)
            self.new_data_widget = QWidget()
            self.new_data_widget.setLayout(self.new_data_layout)

            self.back_button_2.clicked.connect(self.create_add_data_layout)
        else:   
            self.stacked_layout.setCurrentIndex(1)
        
