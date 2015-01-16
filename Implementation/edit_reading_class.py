from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditReading(QMainWindow):
    def __init__(self,consumption_type):
        super().__init__()

        self.setWindowTitle("Edit {0} reading".format(consumption_type))
        self.consumption_type = consumption_type

        self.create_edit_reading_layout()

        self.setCentralWidget(self.edit_reading_widget)

    def create_edit_reading_layout(self):
        self.select_reading = QComboBox()

        self.new_reading_label = QLabel("New Consumption Reading:")
        self.new_reading_input = QLineEdit()

        self.new_date_label = QLabel("New Reading Date:")
        self.new_date_input = QCalendarWidget()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.input_new_reading_layout = QGridLayout()
        self.input_new_reading_layout.addWidget(self.new_reading_label,1,1)
        self.input_new_reading_layout.addWidget(self.new_reading_input,1,2)
        self.input_new_reading_layout.addWidget(self.new_date_label,2,1)
        self.input_new_reading_layout.addWidget(self.new_date_input,2,2)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_reading_layout = QVBoxLayout()
        self.edit_reading_layout.addWidget(self.select_reading)
        self.edit_reading_layout.addLayout(self.input_new_reading_layout)
        self.edit_reading_layout.addLayout(self.button_layout)

        self.edit_reading_widget = QWidget()
        self.edit_reading_widget.setLayout(self.edit_reading_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_reading)
        
    def edit_reading(self):
        pass
