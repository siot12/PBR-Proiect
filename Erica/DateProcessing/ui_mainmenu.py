# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmenu.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        if not mainmenu.objectName():
            mainmenu.setObjectName(u"mainmenu")
        mainmenu.resize(400, 300)
        self.verticalLayout = QVBoxLayout(mainmenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pbDaysFrom = QPushButton(mainmenu)
        self.pbDaysFrom.setObjectName(u"pbDaysFrom")

        self.verticalLayout.addWidget(self.pbDaysFrom)

        self.pbDaysBetween = QPushButton(mainmenu)
        self.pbDaysBetween.setObjectName(u"pbDaysBetween")

        self.verticalLayout.addWidget(self.pbDaysBetween)

        self.pbEpoch = QPushButton(mainmenu)
        self.pbEpoch.setObjectName(u"pbEpoch")

        self.verticalLayout.addWidget(self.pbEpoch)


        self.retranslateUi(mainmenu)

        QMetaObject.connectSlotsByName(mainmenu)
    # setupUi

    def retranslateUi(self, mainmenu):
        mainmenu.setWindowTitle(QCoreApplication.translate("mainmenu", u"mainwindow", None))
        self.pbDaysFrom.setText(QCoreApplication.translate("mainmenu", u"Determine what day/month/year it would be if N days pass", None))
        self.pbDaysBetween.setText(QCoreApplication.translate("mainmenu", u"Compute the distance in days between two dates", None))
        self.pbEpoch.setText(QCoreApplication.translate("mainmenu", u"Compute the corresponding epoch timestamp", None))
    # retranslateUi

