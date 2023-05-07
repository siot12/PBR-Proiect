# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QIntValidator
from PySide6 import QtWidgets

from ui_timeepoch import Ui_timeepoch

class timeepoch(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_timeepoch()
        self.ui.setupUi(self)
        if(not self.ui.leOutputTimestamp.text()):
            self.ui.leOutputTimestamp.setDisabled(True)
        if(not self.ui.leOutputDate.text()):
            self.ui.leOutputDate.setDisabled(True)
        self.ui.leDay.setValidator(QIntValidator(self))
        self.ui.leMonth.setValidator(QIntValidator(self))
        self.ui.leYear.setValidator(QIntValidator(self))
        self.ui.leTimestamp.setValidator(QIntValidator(self))
