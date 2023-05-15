# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'distancebetweendates.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_distancebetweendates(object):
    def setupUi(self, distancebetweendates):
        if not distancebetweendates.objectName():
            distancebetweendates.setObjectName(u"distancebetweendates")
        distancebetweendates.resize(400, 300)
        self.verticalLayout = QVBoxLayout(distancebetweendates)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lTitle = QLabel(distancebetweendates)
        self.lTitle.setObjectName(u"lTitle")

        self.verticalLayout.addWidget(self.lTitle)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.leDayFirst = QLineEdit(distancebetweendates)
        self.leDayFirst.setObjectName(u"leDayFirst")

        self.gridLayout.addWidget(self.leDayFirst, 2, 1, 1, 1)

        self.leYearSecond = QLineEdit(distancebetweendates)
        self.leYearSecond.setObjectName(u"leYearSecond")

        self.gridLayout.addWidget(self.leYearSecond, 3, 3, 1, 1)

        self.leDaySecond = QLineEdit(distancebetweendates)
        self.leDaySecond.setObjectName(u"leDaySecond")

        self.gridLayout.addWidget(self.leDaySecond, 3, 1, 1, 1)

        self.leYearFirst = QLineEdit(distancebetweendates)
        self.leYearFirst.setObjectName(u"leYearFirst")

        self.gridLayout.addWidget(self.leYearFirst, 2, 3, 1, 1)

        self.lFirstDate = QLabel(distancebetweendates)
        self.lFirstDate.setObjectName(u"lFirstDate")

        self.gridLayout.addWidget(self.lFirstDate, 2, 0, 1, 1)

        self.lSecondDate = QLabel(distancebetweendates)
        self.lSecondDate.setObjectName(u"lSecondDate")

        self.gridLayout.addWidget(self.lSecondDate, 3, 0, 1, 1)

        self.leMonthFirst = QLineEdit(distancebetweendates)
        self.leMonthFirst.setObjectName(u"leMonthFirst")

        self.gridLayout.addWidget(self.leMonthFirst, 2, 2, 1, 1)

        self.leMonthSecond = QLineEdit(distancebetweendates)
        self.leMonthSecond.setObjectName(u"leMonthSecond")

        self.gridLayout.addWidget(self.leMonthSecond, 3, 2, 1, 1)

        self.lDay = QLabel(distancebetweendates)
        self.lDay.setObjectName(u"lDay")

        self.gridLayout.addWidget(self.lDay, 1, 1, 1, 1)

        self.lMonth = QLabel(distancebetweendates)
        self.lMonth.setObjectName(u"lMonth")

        self.gridLayout.addWidget(self.lMonth, 1, 2, 1, 1)

        self.lYear = QLabel(distancebetweendates)
        self.lYear.setObjectName(u"lYear")

        self.gridLayout.addWidget(self.lYear, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lNoOfDays = QLabel(distancebetweendates)
        self.lNoOfDays.setObjectName(u"lNoOfDays")

        self.horizontalLayout_2.addWidget(self.lNoOfDays)

        self.leNoDays = QLineEdit(distancebetweendates)
        self.leNoDays.setObjectName(u"leNoDays")
        self.leNoDays.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.leNoDays)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbCancel = QPushButton(distancebetweendates)
        self.pbCancel.setObjectName(u"pbCancel")
        self.pbCancel.setMinimumSize(QSize(0, 30))
        self.pbCancel.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pbCancel)

        self.pbConfirm = QPushButton(distancebetweendates)
        self.pbConfirm.setObjectName(u"pbConfirm")
        self.pbConfirm.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.pbConfirm)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.leDayFirst, self.leMonthFirst)
        QWidget.setTabOrder(self.leMonthFirst, self.leYearFirst)
        QWidget.setTabOrder(self.leYearFirst, self.leDaySecond)
        QWidget.setTabOrder(self.leDaySecond, self.leMonthSecond)
        QWidget.setTabOrder(self.leMonthSecond, self.leYearSecond)
        QWidget.setTabOrder(self.leYearSecond, self.leNoDays)
        QWidget.setTabOrder(self.leNoDays, self.pbCancel)
        QWidget.setTabOrder(self.pbCancel, self.pbConfirm)

        self.retranslateUi(distancebetweendates)

        QMetaObject.connectSlotsByName(distancebetweendates)
    # setupUi

    def retranslateUi(self, distancebetweendates):
        distancebetweendates.setWindowTitle(QCoreApplication.translate("distancebetweendates", u"Form", None))
        self.lTitle.setText(QCoreApplication.translate("distancebetweendates", u"How many days are between two dates", None))
        self.lFirstDate.setText(QCoreApplication.translate("distancebetweendates", u"First date", None))
        self.lSecondDate.setText(QCoreApplication.translate("distancebetweendates", u"Second date", None))
        self.lDay.setText(QCoreApplication.translate("distancebetweendates", u"Day", None))
        self.lMonth.setText(QCoreApplication.translate("distancebetweendates", u"Month", None))
        self.lYear.setText(QCoreApplication.translate("distancebetweendates", u"Year", None))
        self.lNoOfDays.setText(QCoreApplication.translate("distancebetweendates", u"No. of days:", None))
        self.pbCancel.setText(QCoreApplication.translate("distancebetweendates", u"Cancel", None))
        self.pbConfirm.setText(QCoreApplication.translate("distancebetweendates", u"Confirm", None))
    # retranslateUi

