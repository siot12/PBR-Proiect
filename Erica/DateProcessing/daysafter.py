# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QIntValidator
from PySide6 import QtWidgets

from ui_daysafter import Ui_daysafter

class daysafter(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_daysafter()
        self.ui.setupUi(self)
        if(not self.ui.leOutput.text()):
            self.ui.leOutput.setDisabled(True)
        self.ui.leDay.setValidator(QIntValidator(self))
        self.ui.leMonth.setValidator(QIntValidator(self))
        self.ui.leYear.setValidator(QIntValidator(self))
        self.ui.leNoOfDays.setValidator(QIntValidator(self))
