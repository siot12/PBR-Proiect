# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QIntValidator
from PySide6 import QtWidgets
from pyswip import Prolog
from PySide6 import QtCore

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
        QtCore.QObject.connect(self.ui.pbConfirm, QtCore.SIGNAL("clicked()"), lambda: self.compute_distance(self.ui.leDayFirst.text(), self.ui.leMonthFirst.text(), self.ui.leYearFirst.text(), self.ui.leDaySecond.text(),  self.ui.leMonthSecond.text(),  self.ui.leYearSecond.text()))

    def compute_distance(self, day1, month1, year1, day2, month2, year2):
        prolog = Prolog()
        prolog.consult("Cosmin/Ex2_2.pl")
        rez = list(prolog.query("date_difference(date({0},{1},{2}), date({3},{4}, {5}), Difference)".format(year1, month1, day1, year2, month2, day2)))[0]['Difference']
        self.ui.leNoDays.setEnabled(True)
        self.ui.leNoDays.setText(str(rez))
