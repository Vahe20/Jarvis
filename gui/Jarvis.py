# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jarvis.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 550)
        MainWindow.setMinimumSize(QSize(500, 550))
        MainWindow.setMaximumSize(QSize(500, 550))
        icon = QIcon()
        icon.addFile(u"./icons/reactor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 550))
        self.centralwidget.setMaximumSize(QSize(500, 550))
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 40, 132, 235), stop:1 rgba(155, 40, 165, 255));\n"
"")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(150, 120, 201, 191))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet(u"border-radius:  90%;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 0, 135, 255), stop:0.427447 rgba(81, 40, 132, 235), stop:1 rgba(50, 40, 165, 255));\n"
"color: white;")
        self.startButton.setCheckable(True)
        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(400, 20, 75, 31))
        self.settingsButton.setStyleSheet(u"color: white;\n"
"border: solid 1px black;")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 420, 501, 111))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalGroupBox = QGroupBox(self.horizontalLayoutWidget)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalGroupBox.setStyleSheet(u"border: none")
        self.horizontalLayout = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalGroupBox_2 = QGroupBox(self.horizontalGroupBox)
        self.horizontalGroupBox_2.setObjectName(u"horizontalGroupBox_2")
        self.horizontalGroupBox_2.setStyleSheet(u"color: white;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.aiStatus = QLabel(self.horizontalGroupBox_2)
        self.aiStatus.setObjectName(u"aiStatus")
        self.aiStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.aiStatus)


        self.horizontalLayout.addWidget(self.horizontalGroupBox_2)


        self.horizontalLayout_3.addWidget(self.horizontalGroupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jarvis", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"On/Off", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.aiStatus.setText(QCoreApplication.translate("MainWindow", u"AI Off", None))
    # retranslateUi

