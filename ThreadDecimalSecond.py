from PyQt6.QtCore import QThread, pyqtSignal


class ThreadDecimalSecond(QThread):
    decimalSecond = pyqtSignal(int)
    raiseDecimalMinute = pyqtSignal()

    def __init__(self, parent=None):
        super(ThreadDecimalSecond, self).__init__(parent)

        self.__decimalSecond = 0

    def setSiSecond(self, siSecond):
        self.__decimalSecond = int(siSecond * 1000 / 864)

        self.decimalSecond.emit(self.__decimalSecond)

    def run(self) -> None:
        while True:
            self.usleep(864*1000)

            self.__decimalSecond += 1

            if self.__decimalSecond > 99:
                self.__decimalSecond = 0

                self.raiseDecimalMinute.emit()

            self.decimalSecond.emit(self.__decimalSecond)
