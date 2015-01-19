from PyQt4.QtGui import *

from canvas_class import *

class BarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.bar_canvas = Canvas()

        self.bar_layout = QVBoxLayout()
        self.bar_layout.addWidget(self.bar_canvas)
        self.setLayout(self.bar_layout)

    def display_graph(self,data,date):
        self.ax.clear()
        data_dict = dict(data)
        
