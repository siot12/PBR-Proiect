# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QStackedWidget,
    QWidget)

from daysafter import daysafter
from distancebetweendates import distancebetweendates
from mainmenu import mainmenu
from timeepoch import timeepoch

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(300, 300)
        self.horizontalLayout = QHBoxLayout(mainwindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(mainwindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main = mainmenu()
        self.main.setObjectName(u"main")
        self.stackedWidget.addWidget(self.main)
        self.daysafter = daysafter()
        self.daysafter.setObjectName(u"daysafter")
        self.stackedWidget.addWidget(self.daysafter)
        self.distance = distancebetweendates()
        self.distance.setObjectName(u"distance")
        self.stackedWidget.addWidget(self.distance)
        self.epoch = timeepoch()
        self.epoch.setObjectName(u"epoch")
        self.stackedWidget.addWidget(self.epoch)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(mainwindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"Date Processing", None))
    # retranslateUi

