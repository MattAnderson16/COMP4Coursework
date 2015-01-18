from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DeleteType(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Consumption Type")

        self.create_delete_type_layout()
        self.setCentralWidget(self.delete_type_widget)

    def create_delete_type_layout(self):
        self.select_type_label = QLabel("Select Consumption Type:")
        self.select_type_box = QComboBox()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.select_type_label)
        self.select_type_layout.addWidget(self.select_type_box)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.delete_type_layout = QVBoxLayout()
        self.delete_type_layout.addLayout(self.select_type_layout)
        self.delete_type_layout.addLayout(self.button_layout)

        self.delete_type_widget = QWidget()
        self.delete_type_widget.setLayout(self.delete_type_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.delete_data)

    def delete_data(self):
        pass
