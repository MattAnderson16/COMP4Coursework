from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditType(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Consumption Type")

        self.create_edit_type_layout()
        self.setCentralWidget(self.edit_type_widget)
        
    def create_edit_type_layout(self):
        self.select_type_label = QLabel("Select Consumption Type:")
        self.select_type_box = QComboBox()

        self.new_type_label = QLabel("New Consumption Type:")
        self.new_type_input = QLineEdit()

        self.new_description_label = QLabel("New Consumption Type Description:")
        self.new_description_input = QLineEdit()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.select_type_label)
        self.select_type_layout.addWidget(self.select_type_box)

        self.new_type_layout = QHBoxLayout()
        self.new_type_layout.addWidget(self.new_type_label)
        self.new_type_layout.addWidget(self.new_type_input)

        self.new_description_layout = QHBoxLayout()
        self.new_description_layout.addWidget(self.new_description_label)
        self.new_description_layout.addWidget(self.new_description_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_type_layout = QVBoxLayout()
        self.edit_type_layout.addLayout(self.select_type_layout)
        self.edit_type_layout.addLayout(self.new_type_layout)
        self.edit_type_layout.addLayout(self.new_description_layout)
        self.edit_type_layout.addLayout(self.button_layout)

        self.edit_type_widget = QWidget()
        self.edit_type_widget.setLayout(self.edit_type_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_data)

    def edit_data(self):
        pass
    
