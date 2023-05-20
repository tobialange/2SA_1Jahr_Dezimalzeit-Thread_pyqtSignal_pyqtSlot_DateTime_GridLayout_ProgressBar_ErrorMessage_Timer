from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class DecimalMinute(QObject):
    raiseDecimalHour = pyqtSignal()
    decimalMinute = pyqtSignal(int)

    steepDecimalMinute = pyqtSlot()

    def __init__(self, parent=None):
        super(DecimalMinute, self).__init__(parent)

        self.__decimalMinute = 0

    def setSiMinute(self, siMinute):
        self.__decimalMinute = int(siMinute * 100 / 144)

        self.decimalMinute.emit(self.__decimalMinute)

    def steepDecimalMinute(self):
        self.__decimalMinute += 1

        if self.__decimalMinute > 99:
            self.__decimalMinute = 0

            self.raiseDecimalHour.emit()

        self.decimalMinute.emit(self.__decimalMinute)
