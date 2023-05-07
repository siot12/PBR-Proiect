# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QIntValidator
from PySide6 import QtWidgets

from ui_distancebetweendates import Ui_distancebetweendates

class distancebetweendates(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_distancebetweendates()
        self.ui.setupUi(self)
        if(not self.ui.leNoDays.text()):
            self.ui.leNoDays.setDisabled(True)
        self.ui.leDayFirst.setValidator(QIntValidator(self))
        self.ui.leMonthFirst.setValidator(QIntValidator(self))
        self.ui.leYearFirst.setValidator(QIntValidator(self))
        self.ui.leDaySecond.setValidator(QIntValidator(self))
        self.ui.leMonthSecond.setValidator(QIntValidator(self))
        self.ui.leYearSecond.setValidator(QIntValidator(self))
