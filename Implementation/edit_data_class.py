from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class EditData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()

        self.create_data_selection_layout()
        self.create_edit_data_layout()
        self.create_confirmation_layout()

        self.stacked_layout.addWidget(self.data_selection_widget)
        self.stacked_layout.addWidget(self.edit_data_widget)
        self.stacked_layout.addWidget(self.confirmation_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_data_selection_layout(self):
        if not hasattr(self,"data_selection_layout"):
            self.data_table = QLabel("Data Table:")
            self.data_type = QLabel("Data Type:")
            self.data = QLabel("Data:")
            self.data_table_dropdown = QPushButton("None")
            self.data_type_dropdown = QPushButton("None")
            self.data_dropdown = QPushButton("None")
            self.proceed_button = QPushButton("Proceed")
            self.back_button_a = QPushButton("Back")

            self.data_table_menu = QMenu()
            self.data_type_menu = QMenu()
            self.data_menu = QMenu()
            self.data_table_dropdown.setMenu(self.data_table_menu)
            self.data_type_dropdown.setMenu(self.data_type_menu)
            self.data_dropdown.setMenu(self.data_menu)

            self.data_table_layout = QHBoxLayout()
            self.data_table_layout.addWidget(self.data_table)
            self.data_table_layout.addWidget(self.data_table_dropdown)

            self.data_type_layout = QHBoxLayout()
            self.data_type_layout.addWidget(self.data_type)
            self.data_type_layout.addWidget(self.data_type_dropdown)

            self.data_layout = QHBoxLayout()
            self.data_layout.addWidget(self.data)
            self.data_layout.addWidget(self.data_type_dropdown)

            self.button_layout = QHBoxLayout()
            self.button_layout.addWidget(self.proceed_button)
            self.button_layout.addWidget(self.back_button)

            self.data_selection_layout = QVBoxLayout()
            self.data_selection_layout.addLayout(self.data_table_layout)
            self.data_selection_layout.addLayout(self.data_type_layout)
            self.data_selection_layout.addLayout(data_layout)
            self.data_selection_layout.addLayout(button_layout)
            
            self.data_selection_widget = QWidget()
            self.data_selection_widget.setLayout(self.data_selection_layout)
        else:
            self.stacked_layout.setCurrentIndex(0)

    def create_edit_data_layout(self):
        pass

    def create_confirmation_layout(self):
        pass
        
