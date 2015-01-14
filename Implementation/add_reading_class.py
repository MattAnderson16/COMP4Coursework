from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddReading(QMainWindow):
    def __init__(self,consumption_type):
        super().__init__()

        self.setWindowTitle("Add {0} Reading".format(consumption_type))
        
        self.consumption_type = consumption_type

        self.create_add_reading_layout()
        self.setCentralWidget(self.add_reading_widget)

    def create_add_reading_layout(self):
        self.reading_label = QLabel("Consumption Reading:")
        self.reading_input = QLineEdit()

        self.date_label = QLabel("Reading Date:")
        self.date_input = QCalendarWidget()
        
        self.confirm_button = QPushButton("Confirm")
        self.back_button = QPushButton("Back")

        self.input_reading_layout = QGridLayout()
        self.input_reading_layout.addWidget(self.reading_label,1,1)
        self.input_reading_layout.addWidget(self.reading_input,1,2)
        self.input_reading_layout.addWidget(self.date_label,2,1)
        self.input_reading_layout.addWidget(self.date_input,2,2)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.add_reading_layout = QVBoxLayout()
        self.add_reading_layout.addLayout(self.input_reading_layout)
        self.add_reading_layout.addLayout(self.button_layout)

        self.add_reading_widget = QWidget()
        self.add_reading_widget.setLayout(self.add_reading_layout)

        self.confirm_button.clicked.connect(self.add_data)
        self.back_button.clicked.connect(self.close)

    def add_data(self):
        pass
