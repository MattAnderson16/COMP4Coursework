from PyQt4.QtGui import *
from PyQt4.QtCore import *
from canvas_class import *

class CreateBarLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.bar_canvas = Canvas()
        if not hasattr(self,"bar_layout"):
            self.addWidget(self.bar_canvas)
