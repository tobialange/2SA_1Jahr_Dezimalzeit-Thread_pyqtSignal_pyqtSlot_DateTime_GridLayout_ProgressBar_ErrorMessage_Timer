from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class DecimalHour(QObject):
    decimalHour = pyqtSignal(int)

    steepDecimalHour = pyqtSlot()

    def __init__(self, parent=None):
        super(DecimalHour, self).__init__(parent)

        self.__decimalHour = 0

    def setSiHour(self, siHour):
        self.__decimalHour = int(siHour * 10 / 24)

        self.decimalHour.emit(self.__decimalHour)

    def steepDecimalHour(self):
        self.__decimalHour += 1

        if self.__decimalHour > 9:
            self.__decimalHour = 0

        self.decimalHour.emit(self.__decimalHour)
