# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QIntValidator
from PySide6 import QtCore
from PySide6 import QtWidgets
from pyswip import Prolog

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
        QtCore.QObject.connect(self.ui.pbOk, QtCore.SIGNAL("clicked()"), lambda: self.compute_date(self.ui.leDay.text(), self.ui.leMonth.text(), self.ui.leYear.text(), self.ui.leNoOfDays.text()))

    def compute_date(self, day, month, year, no_of_days):
        prolog = Prolog()
        prolog.consult("Sabin/ProiectPBR.pl")
        rez = list(prolog.query("adauga_zile_la_data('{0}-{1}-{2}', {3}, Rezultat)".format(day, month, year, no_of_days)))[0]['Rezultat']
        self.ui.leOutput.setEnabled(True)
        self.ui.leOutput.setText("{0}-{1}-{2}".format(rez[0], rez[1], rez[2]))
