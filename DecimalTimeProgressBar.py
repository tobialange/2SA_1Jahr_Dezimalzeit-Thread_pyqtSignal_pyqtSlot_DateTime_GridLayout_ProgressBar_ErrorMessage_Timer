from PyQt6.QtWidgets import QProgressBar


class DecimalTimeProgressBar(QProgressBar):
    def __init__(self, minimum, maximum, parent=None):
        super(DecimalTimeProgressBar, self).__init__(parent)

        self.setRange(minimum, maximum)
        self.setFormat("%v")
