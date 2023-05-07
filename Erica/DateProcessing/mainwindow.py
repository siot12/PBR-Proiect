# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, SIGNAL, SLOT
from PySide6 import QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_mainwindow

class mainwindow(QWidget):
    @Slot(int)
    def changepage(self, page):
        self.ui.stackedWidget.setCurrentIndex(page)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.main.ui.pbDaysFrom, QtCore.SIGNAL("clicked()"), lambda: self.changepage(1))
        QtCore.QObject.connect(self.ui.main.ui.pbDaysBetween, QtCore.SIGNAL("clicked()"), lambda: self.changepage(2))
        QtCore.QObject.connect(self.ui.main.ui.pbEpoch, QtCore.SIGNAL("clicked()"), lambda: self.changepage(3))
        QtCore.QObject.connect(self.ui.daysafter.ui.pbCancel, QtCore.SIGNAL("clicked()"), lambda: self.changepage(0))
        QtCore.QObject.connect(self.ui.distance.ui.pbCancel, QtCore.SIGNAL("clicked()"), lambda: self.changepage(0))
        QtCore.QObject.connect(self.ui.epoch.ui.pbCancel, QtCore.SIGNAL("clicked()"), lambda: self.changepage(0))
        self.ui.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = mainwindow()
    widget.show()
    sys.exit(app.exec())
