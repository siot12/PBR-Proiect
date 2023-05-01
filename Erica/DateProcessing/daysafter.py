# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from ui_daysafter import Ui_daysafter

class daysafter(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_daysafter()
        self.ui.setupUi(self)
        if(not self.ui.leOutput.text()):
            self.ui.leOutput.setDisabled(True)
