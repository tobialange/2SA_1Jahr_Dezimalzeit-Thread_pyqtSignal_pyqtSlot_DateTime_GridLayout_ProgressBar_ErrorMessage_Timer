from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot, QDateTime

class ThreadWatchdog(QThread):
    error = pyqtSignal(str)
    time = pyqtSignal(str)

    setDecimalSecond = pyqtSlot(int)
    setDecimalMinute = pyqtSlot(int)
    setDecimalHour = pyqtSlot(int)

    def __init__(self, parent=None):
        super(ThreadWatchdog, self).__init__(parent)

        self.__decimalSecond = 0
        self.__decimalMinute = 0
        self.__decimalHour = 0

    def run(self) -> None:
        while True:
            self.sleep(1)

            currentTime = QDateTime.currentDateTime().time()

            dateTimeString = currentTime.toString("HH:mm:ss")

            self.time.emit(dateTimeString)

            si = currentTime.msecsSinceStartOfDay()
            dec = self.decimalTimeToMSecond()
            if si < dec:
                break

        self.error.emit("Something went wrong.")

    def setDecimalSecond(self, decimalSecond):
        self.__decimalSecond = decimalSecond

    def setDecimalMinute(self, decimalSecond):
        self.steepDecimalMinute = decimalSecond

    def setDecimalHour(self, decimalHour):
        self.__decimalHour = decimalHour

    def decimalTimeToMSecond(self):
        siSecond = self.__decimalSecond * 0.864
        siSecond += self.__decimalMinute * 1.44
        siSecond += self.__decimalHour * 2.4
        siSecond *= 1000

        return siSecond
