# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QIntValidator
from PySide6 import QtCore
from PySide6.QtCore import QStringConverter
from PySide6 import QtWidgets
from pyswip import Prolog
import datetime

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
        QtCore.QObject.connect(self.ui.pbComputeEpoch, QtCore.SIGNAL("clicked()"), lambda: self.compute_epoch(int(self.ui.leDay.text()), int(self.ui.leMonth.text()), int(self.ui.leYear.text())))
        QtCore.QObject.connect(self.ui.pbComputeTimestamp, QtCore.SIGNAL("clicked()"), lambda: self.compute_date(int(self.ui.leTimestamp.text())))

    def compute_epoch(self, day, month, year):
        prolog = Prolog()
        prolog.consult("Tudor/my_file.pl")
        rez = (list(prolog.query("date_to_epoch(date({0}, {1}, {2}), Epoch)".format(year, month, day)))[0])
        self.ui.leOutputTimestamp.setEnabled(True)
        self.ui.leOutputTimestamp.setText(str(rez['Epoch']))

    def compute_date(self, epoch):
        prolog = Prolog()
        prolog.consult("Tudor/my_file2.pl")
        rez = (list(prolog.query("epoch_to_date({0}, Date)".format(epoch)))[0])
        date_obj = datetime.datetime.strptime(rez['Date'], "date(%Y, %m, %d)")
        formatted_date = date_obj.strftime("%d-%m-%Y")
        self.ui.leOutputDate.setEnabled(True)
        self.ui.leOutputDate.setText(formatted_date)

