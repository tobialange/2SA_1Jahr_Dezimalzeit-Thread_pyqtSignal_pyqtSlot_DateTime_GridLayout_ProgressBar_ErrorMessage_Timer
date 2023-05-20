from PyQt6.QtWidgets import QMainWindow
from WidgetDecimalTime import WidgetDecimalTime


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        widget = WidgetDecimalTime(self)
        self.setCentralWidget(widget)

        self.setWindowTitle("Decimal Time Widget")
