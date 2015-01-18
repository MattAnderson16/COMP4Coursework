from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DeleteCost(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Delete Cost Data")

        self.create_delete_cost_data_layout()
        self.setCentralWidget(self.delete_cost_data_widget)

    def create_delete_cost_data_layout(self):
        self.select_cost_label = QLabel("Select Cost:")
        self.select_cost_button = QComboBox()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_cost_layout = QHBoxLayout()
        self.select_cost_layout.addWidget(self.select_cost_label)
        self.select_cost_layout.addWidget(self.select_cost_button)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.delete_cost_data_layout = QVBoxLayout()
        self.delete_cost_data_layout.addLayout(self.select_cost_layout)
        self.delete_cost_data_layout.addLayout(self.button_layout)

        self.delete_cost_data_widget = QWidget()
        self.delete_cost_data_widget.setLayout(self.delete_cost_data_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.delete_data)

    def delete_data(self):
        pass
        
