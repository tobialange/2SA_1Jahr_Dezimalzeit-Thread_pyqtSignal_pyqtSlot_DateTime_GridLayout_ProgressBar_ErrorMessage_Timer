from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QProgressBar, QErrorMessage
from PyQt6.QtCore import pyqtSlot, QDateTime
from TimeEdit import TimeEdit
from TimerDecimal import TimerDecimal
from ThreadWatchdog import ThreadWatchdog
from ThreadDecimalSecond import ThreadDecimalSecond
from DecimalMinute import DecimalMinute
from DecimalHour import DecimalHour
from DecimalTimeProgressBar import DecimalTimeProgressBar

class WidgetDecimalTime(QWidget):
    errorMessage = pyqtSlot(str)

    def __init__(self, parent=None):
        super(WidgetDecimalTime, self).__init__(parent)

        decimalTime = TimeEdit(self)
        siTime = TimeEdit(self)

        decimalSecond = DecimalTimeProgressBar(0, 99, self)
        decimalMinute = DecimalTimeProgressBar(0, 99, self)
        decimalHour = DecimalTimeProgressBar(0, 9, self)

        layout = QGridLayout(self)
        layout.addWidget(siTime, 1, 1)
        layout.addWidget(QLabel("SI-Zeit"), 1, 2)
        layout.addWidget(decimalTime, 2, 1)
        layout.addWidget(QLabel("Dezimalzeit"), 2, 2)
        layout.addWidget(decimalHour, 3, 1)
        layout.addWidget(QLabel("Dezimalstunde"), 3, 2)
        layout.addWidget(decimalMinute, 4, 1)
        layout.addWidget(QLabel("Dezimalminute"), 4, 2)
        layout.addWidget(decimalSecond, 5, 1)
        layout.addWidget(QLabel("Dezimalsekunde"), 5, 2)
        self.setLayout(layout)

        timerDecimal = TimerDecimal(self)
        timerDecimal.time.connect(decimalTime.setText)

        watchdog = ThreadWatchdog(self)
        watchdog.time.connect(siTime.setText)
        watchdog.error.connect(self.errorMessage)

        now = QDateTime.currentDateTime().time()

        hour = DecimalHour(self)
        hour.decimalHour.connect(decimalHour.setValue)
        hour.decimalHour.connect(watchdog.setDecimalHour)
        hour.setSiHour(now.hour())

        minute = DecimalMinute(self)
        minute.decimalMinute.connect(decimalMinute.setValue)
        minute.decimalMinute.connect(watchdog.setDecimalMinute)
        minute.raiseDecimalHour.connect(hour.steepDecimalHour)
        minute.setSiMinute(now.minute())

        second = ThreadDecimalSecond(self)
        second.decimalSecond.connect(decimalSecond.setValue)
        second.decimalSecond.connect(watchdog.setDecimalSecond)
        second.raiseDecimalMinute.connect(minute.steepDecimalMinute)
        second.setSiSecond(now.second())

        second.start()
        watchdog.start()

    def errorMessage(self, message):
        errorMessage = QErrorMessage(self)
        errorMessage.showMessage(message)
