# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daysafter.ui'
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

class Ui_daysafter(object):
    def setupUi(self, daysafter):
        if not daysafter.objectName():
            daysafter.setObjectName(u"daysafter")
        daysafter.resize(564, 257)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(daysafter.sizePolicy().hasHeightForWidth())
        daysafter.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(daysafter)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lTitle = QLabel(daysafter)
        self.lTitle.setObjectName(u"lTitle")
        self.lTitle.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(17)
        self.lTitle.setFont(font)
        self.lTitle.setWordWrap(False)

        self.verticalLayout.addWidget(self.lTitle, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(-1)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lYear = QLabel(daysafter)
        self.lYear.setObjectName(u"lYear")

        self.gridLayout.addWidget(self.lYear, 0, 2, 1, 1)

        self.lMonth = QLabel(daysafter)
        self.lMonth.setObjectName(u"lMonth")

        self.gridLayout.addWidget(self.lMonth, 0, 1, 1, 1)

        self.lAfter = QLabel(daysafter)
        self.lAfter.setObjectName(u"lAfter")

        self.gridLayout.addWidget(self.lAfter, 0, 3, 1, 1)

        self.lDay = QLabel(daysafter)
        self.lDay.setObjectName(u"lDay")

        self.gridLayout.addWidget(self.lDay, 0, 0, 1, 1)

        self.leDay = QLineEdit(daysafter)
        self.leDay.setObjectName(u"leDay")

        self.gridLayout.addWidget(self.leDay, 1, 0, 1, 1)

        self.leMonth = QLineEdit(daysafter)
        self.leMonth.setObjectName(u"leMonth")

        self.gridLayout.addWidget(self.leMonth, 1, 1, 1, 1)

        self.leYear = QLineEdit(daysafter)
        self.leYear.setObjectName(u"leYear")

        self.gridLayout.addWidget(self.leYear, 1, 2, 1, 1)

        self.leNoOfDays = QLineEdit(daysafter)
        self.leNoOfDays.setObjectName(u"leNoOfDays")

        self.gridLayout.addWidget(self.leNoOfDays, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.layoutOutput = QHBoxLayout()
        self.layoutOutput.setSpacing(5)
        self.layoutOutput.setObjectName(u"layoutOutput")
        self.layoutOutput.setContentsMargins(5, 5, 5, 5)
        self.lOutput = QLabel(daysafter)
        self.lOutput.setObjectName(u"lOutput")

        self.layoutOutput.addWidget(self.lOutput)

        self.leOutput = QLineEdit(daysafter)
        self.leOutput.setObjectName(u"leOutput")
        self.leOutput.setStyleSheet(u":read-only {}")
        self.leOutput.setReadOnly(True)

        self.layoutOutput.addWidget(self.leOutput)


        self.verticalLayout.addLayout(self.layoutOutput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setSpacing(5)
        self.layoutButtons.setObjectName(u"layoutButtons")
        self.layoutButtons.setContentsMargins(5, 5, 5, 5)
        self.pbCancel = QPushButton(daysafter)
        self.pbCancel.setObjectName(u"pbCancel")
        self.pbCancel.setMinimumSize(QSize(0, 30))

        self.layoutButtons.addWidget(self.pbCancel)

        self.pbOk = QPushButton(daysafter)
        self.pbOk.setObjectName(u"pbOk")
        self.pbOk.setMinimumSize(QSize(0, 30))

        self.layoutButtons.addWidget(self.pbOk)


        self.verticalLayout.addLayout(self.layoutButtons)


        self.retranslateUi(daysafter)

        QMetaObject.connectSlotsByName(daysafter)
    # setupUi

    def retranslateUi(self, daysafter):
        daysafter.setWindowTitle(QCoreApplication.translate("daysafter", u"Form", None))
        self.lTitle.setText(QCoreApplication.translate("daysafter", u"Determine what day/month/year it would be if N days pass from date D", None))
        self.lYear.setText(QCoreApplication.translate("daysafter", u"Year", None))
        self.lMonth.setText(QCoreApplication.translate("daysafter", u"Month", None))
        self.lAfter.setText(QCoreApplication.translate("daysafter", u"No. of days", None))
        self.lDay.setText(QCoreApplication.translate("daysafter", u"Day", None))
        self.lOutput.setText(QCoreApplication.translate("daysafter", u"Output:", None))
        self.pbCancel.setText(QCoreApplication.translate("daysafter", u"Cancel", None))
        self.pbOk.setText(QCoreApplication.translate("daysafter", u"Determine", None))
    # retranslateUi

