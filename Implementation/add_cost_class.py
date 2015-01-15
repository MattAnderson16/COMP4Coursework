from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddCost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Cost")

        self.create_add_cost_layout()
        self.setCentralWidget(self.add_cost_widget)

    def create_add_cost_layout(self):
        self.select_consumption_label = QLabel("Consumption Type:")
        self.select_consumption_box = QComboBox()
        
        self.cost_per_unit_label = QLabel("Cost Per Unit:")
        self.cost_per_unit_input = QLineEdit()

        self.cost_start_date_label = QLabel("Cost Start Date:")
        self.cost_start_date_input = QCalendarWidget()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_consumption_layout = QHBoxLayout()
        self.select_consumption_layout.addWidget(self.select_consumption_label)
        self.select_consumption_layout.addWidget(self.select_consumption_box)

        self.cost_per_unit_layout = QHBoxLayout()
        self.cost_per_unit_layout.addWidget(self.cost_per_unit_label)
        self.cost_per_unit_layout.addWidget(self.cost_per_unit_input)

        self.cost_start_date_layout = QHBoxLayout()
        self.cost_start_date_layout.addWidget(self.cost_start_date_label)
        self.cost_start_date_layout.addWidget(self.cost_start_date_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.add_cost_layout = QVBoxLayout()
        self.add_cost_layout.addLayout(self.select_consumption_layout)
        self.add_cost_layout.addLayout(self.cost_per_unit_layout)
        self.add_cost_layout.addLayout(self.cost_start_date_layout)
        self.add_cost_layout.addLayout(self.button_layout)

        self.add_cost_widget = QWidget()
        self.add_cost_widget.setLayout(self.add_cost_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.add_data)

    def add_data(self):
        pass
