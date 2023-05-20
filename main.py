from PyQt6.QtWidgets import QApplication
from MyMainWindow import MyMainWindow
import sys

# See https://doc.qt.io/qtforpython/PySide6/
if __name__ == '__main__':
    application = QApplication(sys.argv)

    mainWindow = MyMainWindow()
    mainWindow.show()

    application.exec()