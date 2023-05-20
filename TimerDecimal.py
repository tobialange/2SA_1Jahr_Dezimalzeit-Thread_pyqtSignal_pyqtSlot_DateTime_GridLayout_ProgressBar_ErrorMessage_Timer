from PyQt6.QtCore import QTimer, pyqtSignal, pyqtSlot, QDateTime


class TimerDecimal(QTimer):
    time = pyqtSignal(str)

    update = pyqtSlot()

    def __init__(self, parent=None):
        super(TimerDecimal, self).__init__(parent)

        self.timeout.connect(self.update)
        self.start(864)

    def update(self):
        currentTime = QDateTime.currentDateTime().time()

        decimalSecond = int(currentTime.second() / 0.864)
        decimalMinute = int(currentTime.minute() / 1.44)
        decimalHour = int(currentTime.hour() / 2.4)

        decimalTime = "{:01d}:{:02d}:{:02d}".format(decimalHour, decimalMinute, decimalSecond)

        self.time.emit(decimalTime)
