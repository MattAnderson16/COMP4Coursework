from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditCost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Cost")

        self.create_edit_cost_layout()
        self.setCentralWidget(self.edit_cost_widget)

    def create_edit_cost_layout(self):
        self.select_cost_label = QLabel("Select Cost:")
        self.select_cost_box = QComboBox()

        self.new_cost_label = QLabel("New Cost Per Unit:")
        self.new_cost_input = QLineEdit()

        self.new_cost_date_label = QLabel("New Cost Start Date:")
        self.new_cost_date_selection = QCalendarWidget()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_cost_layout = QHBoxLayout()
        self.select_cost_layout.addWidget(self.select_cost_label)
        self.select_cost_layout.addWidget(self.select_cost_box)

        self.new_cost_layout = QHBoxLayout()
        self.new_cost_layout.addWidget(self.new_cost_label)
        self.new_cost_layout.addWidget(self.new_cost_input)

        self.new_date_layout = QHBoxLayout()
        self.new_date_layout.addWidget(self.new_cost_date_label)
        self.new_date_layout.addWidget(self.new_cost_date_selection)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_cost_layout = QVBoxLayout()
        self.edit_cost_layout.addLayout(self.select_cost_layout)
        self.edit_cost_layout.addLayout(self.new_cost_layout)
        self.edit_cost_layout.addLayout(self.new_date_layout)
        self.edit_cost_layout.addLayout(self.button_layout)

        self.edit_cost_widget = QWidget()
        self.edit_cost_widget.setLayout(self.edit_cost_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_data)

    def edit_data(self):
        pass
