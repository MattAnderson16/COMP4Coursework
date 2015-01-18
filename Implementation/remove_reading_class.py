from PyQt4.QtGui import *
from PyQt4.QtCore import *

class RemoveReading(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Remove Reading")

        self.create_remove_reading_layout()

        self.setCentralWidget(self.remove_reading_widget)

    def create_remove_reading_layout(self):
        self.select_reading_label = QLabel("Select Reading:")
        self.select_reading = QComboBox()
        
        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_reading_layout = QHBoxLayout()
        self.select_reading_layout.addWidget(self.select_reading_label)
        self.select_reading_layout.addWidget(self.select_reading)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.remove_reading_layout = QVBoxLayout()
        self.remove_reading_layout.addLayout(self.select_reading_layout)
        self.remove_reading_layout.addLayout(self.button_layout)

        self.remove_reading_widget = QWidget()
        self.remove_reading_widget.setLayout(self.remove_reading_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.remove_reading)

    def remove_reading(self):
        pass
        
