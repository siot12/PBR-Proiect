# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeepoch.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_timeepoch(object):
    def setupUi(self, timeepoch):
        if not timeepoch.objectName():
            timeepoch.setObjectName(u"timeepoch")
        timeepoch.resize(400, 300)
        self.verticalLayout = QVBoxLayout(timeepoch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lTitle = QLabel(timeepoch)
        self.lTitle.setObjectName(u"lTitle")

        self.verticalLayout.addWidget(self.lTitle)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.leMonth = QLineEdit(timeepoch)
        self.leMonth.setObjectName(u"leMonth")

        self.gridLayout.addWidget(self.leMonth, 1, 1, 1, 1)

        self.leYear = QLineEdit(timeepoch)
        self.leYear.setObjectName(u"leYear")

        self.gridLayout.addWidget(self.leYear, 1, 2, 1, 1)

        self.lYear = QLabel(timeepoch)
        self.lYear.setObjectName(u"lYear")

        self.gridLayout.addWidget(self.lYear, 0, 2, 1, 1)

        self.lMonth = QLabel(timeepoch)
        self.lMonth.setObjectName(u"lMonth")

        self.gridLayout.addWidget(self.lMonth, 0, 1, 1, 1)

        self.leDay = QLineEdit(timeepoch)
        self.leDay.setObjectName(u"leDay")

        self.gridLayout.addWidget(self.leDay, 1, 0, 1, 1)

        self.lDay = QLabel(timeepoch)
        self.lDay.setObjectName(u"lDay")

        self.gridLayout.addWidget(self.lDay, 0, 0, 1, 1)

        self.lEpoch = QLabel(timeepoch)
        self.lEpoch.setObjectName(u"lEpoch")

        self.gridLayout.addWidget(self.lEpoch, 2, 0, 1, 1)

        self.leOutputTimestamp = QLineEdit(timeepoch)
        self.leOutputTimestamp.setObjectName(u"leOutputTimestamp")
        self.leOutputTimestamp.setReadOnly(True)

        self.gridLayout.addWidget(self.leOutputTimestamp, 2, 1, 1, 1)

        self.pbComputeEpoch = QPushButton(timeepoch)
        self.pbComputeEpoch.setObjectName(u"pbComputeEpoch")

        self.gridLayout.addWidget(self.pbComputeEpoch, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.lTitle2 = QLabel(timeepoch)
        self.lTitle2.setObjectName(u"lTitle2")

        self.verticalLayout.addWidget(self.lTitle2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.leTimestamp = QLineEdit(timeepoch)
        self.leTimestamp.setObjectName(u"leTimestamp")

        self.gridLayout_2.addWidget(self.leTimestamp, 0, 1, 1, 1)

        self.lDate = QLabel(timeepoch)
        self.lDate.setObjectName(u"lDate")

        self.gridLayout_2.addWidget(self.lDate, 1, 0, 1, 1)

        self.lTimeStamp = QLabel(timeepoch)
        self.lTimeStamp.setObjectName(u"lTimeStamp")

        self.gridLayout_2.addWidget(self.lTimeStamp, 0, 0, 1, 1)

        self.leOutputDate = QLineEdit(timeepoch)
        self.leOutputDate.setObjectName(u"leOutputDate")
        self.leOutputDate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.leOutputDate, 1, 1, 1, 1)

        self.pbComputeTimestamp = QPushButton(timeepoch)
        self.pbComputeTimestamp.setObjectName(u"pbComputeTimestamp")

        self.gridLayout_2.addWidget(self.pbComputeTimestamp, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pbCancel = QPushButton(timeepoch)
        self.pbCancel.setObjectName(u"pbCancel")

        self.verticalLayout.addWidget(self.pbCancel)


        self.retranslateUi(timeepoch)

        QMetaObject.connectSlotsByName(timeepoch)
    # setupUi

    def retranslateUi(self, timeepoch):
        timeepoch.setWindowTitle(QCoreApplication.translate("timeepoch", u"Form", None))
        self.lTitle.setText(QCoreApplication.translate("timeepoch", u"Compute the corresponding epoch timestamp", None))
        self.lYear.setText(QCoreApplication.translate("timeepoch", u"Year", None))
        self.lMonth.setText(QCoreApplication.translate("timeepoch", u"Month", None))
        self.lDay.setText(QCoreApplication.translate("timeepoch", u"Day", None))
        self.lEpoch.setText(QCoreApplication.translate("timeepoch", u"Epoch timestamp:", None))
        self.pbComputeEpoch.setText(QCoreApplication.translate("timeepoch", u"Compute", None))
        self.lTitle2.setText(QCoreApplication.translate("timeepoch", u"Compute the date from the corresponding epoch timestamp", None))
        self.lDate.setText(QCoreApplication.translate("timeepoch", u"Date:", None))
        self.lTimeStamp.setText(QCoreApplication.translate("timeepoch", u"Epoch timestamp", None))
        self.pbComputeTimestamp.setText(QCoreApplication.translate("timeepoch", u"Compute", None))
        self.pbCancel.setText(QCoreApplication.translate("timeepoch", u"Cancel", None))
    # retranslateUi

