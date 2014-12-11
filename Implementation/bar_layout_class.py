from PyQt4.QtGui import *
from PyQt4.QtCore import *
from canvas_class import *

class create_bar_layout:
    def __init__(self):
        self.bar_canvas = Canvas()

    def create_bar_layout(self):
        if not hasattr(self,"bar_layout"):
            self.bar_layout = QVBoxLayout()
            self.bar_layout.addWidget(self.bar_canvas)
            return self.bar_layout
