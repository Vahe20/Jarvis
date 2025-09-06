# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(487, 646)
        icon = QIcon()
        icon.addFile(u"../icons/reactor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 40, 132, 235), stop:1 rgba(155, 40, 165, 255));\n"
"color: white;\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_2 = QScrollArea(self.tabWidgetPage1)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.scrollArea_2.setAutoFillBackground(False)
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 449, 558))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.autoStartBtn = QCheckBox(self.scrollAreaWidgetContents_2)
        self.autoStartBtn.setObjectName(u"autoStartBtn")
        self.autoStartBtn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.autoStartBtn.setTristate(False)

        self.verticalLayout_12.addWidget(self.autoStartBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.StarWords = QGridLayout()
        self.StarWords.setObjectName(u"StarWords")
        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.StarWords.addWidget(self.checkBox_9, 2, 3, 1, 1)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.StarWords.addWidget(self.checkBox_6, 1, 3, 1, 1)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.StarWords.addWidget(self.checkBox_8, 2, 2, 1, 1)

        self.checkBox_12 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.StarWords.addWidget(self.checkBox_12, 3, 3, 1, 1)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.StarWords.addWidget(self.checkBox_3, 0, 3, 1, 1)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.StarWords.addWidget(self.checkBox_5, 1, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.StarWords.addWidget(self.checkBox_7, 2, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.StarWords.addWidget(self.checkBox_11, 3, 2, 1, 1)

        self.checkBox_1 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.StarWords.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.StarWords.addWidget(self.checkBox_10, 3, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.StarWords.addWidget(self.checkBox_4, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.StarWords.addWidget(self.checkBox_2, 0, 2, 1, 1)

        self.checkBox_13 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.StarWords.addWidget(self.checkBox_13, 4, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.StarWords.addWidget(self.checkBox_15, 4, 3, 1, 1)

        self.checkBox_14 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.StarWords.addWidget(self.checkBox_14, 4, 2, 1, 1)


        self.verticalLayout_12.addLayout(self.StarWords)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.tabWidgetPage2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.VLine)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 447, 556))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0)")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.discordButton = QPushButton(self.scrollAreaWidgetContents)
        self.discordButton.setObjectName(u"discordButton")
        self.discordButton.setStyleSheet(u"border: solid 5px black;\n"
"padding:   3px 20px;")

        self.horizontalLayout_2.addWidget(self.discordButton)

        self.discordLine = QLineEdit(self.scrollAreaWidgetContents)
        self.discordLine.setObjectName(u"discordLine")
        self.discordLine.setStyleSheet(u"border: solid 5px black;\n"
"")

        self.horizontalLayout_2.addWidget(self.discordLine)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0)")

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.steamButton = QPushButton(self.scrollAreaWidgetContents)
        self.steamButton.setObjectName(u"steamButton")
        self.steamButton.setStyleSheet(u"border: solid 5px black;\n"
"padding:   3px 20px;")

        self.horizontalLayout_3.addWidget(self.steamButton)

        self.steamLine = QLineEdit(self.scrollAreaWidgetContents)
        self.steamLine.setObjectName(u"steamLine")
        self.steamLine.setStyleSheet(u"border: solid 5px black;\n"
"")

        self.horizontalLayout_3.addWidget(self.steamLine)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0)")

        self.verticalLayout_7.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.epicButton = QPushButton(self.scrollAreaWidgetContents)
        self.epicButton.setObjectName(u"epicButton")
        self.epicButton.setStyleSheet(u"border: solid 5px black;\n"
"padding:   3px 20px;")

        self.horizontalLayout_4.addWidget(self.epicButton)

        self.epicLine = QLineEdit(self.scrollAreaWidgetContents)
        self.epicLine.setObjectName(u"epicLine")
        self.epicLine.setStyleSheet(u"border: solid 5px black;\n"
"")

        self.horizontalLayout_4.addWidget(self.epicLine)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0)")

        self.verticalLayout_8.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gtaButton = QPushButton(self.scrollAreaWidgetContents)
        self.gtaButton.setObjectName(u"gtaButton")
        self.gtaButton.setStyleSheet(u"border: solid 5px black;\n"
"padding:   3px 20px;")

        self.horizontalLayout_5.addWidget(self.gtaButton)

        self.gtaLine = QLineEdit(self.scrollAreaWidgetContents)
        self.gtaLine.setObjectName(u"gtaLine")
        self.gtaLine.setStyleSheet(u"border: solid 5px black;\n"
"")

        self.horizontalLayout_5.addWidget(self.gtaLine)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0)")

        self.verticalLayout_9.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mineButton = QPushButton(self.scrollAreaWidgetContents)
        self.mineButton.setObjectName(u"mineButton")
        self.mineButton.setStyleSheet(u"border: solid 5px black;\n"
"padding:   3px 20px;")

        self.horizontalLayout_6.addWidget(self.mineButton)

        self.mineLine = QLineEdit(self.scrollAreaWidgetContents)
        self.mineLine.setObjectName(u"mineLine")
        self.mineLine.setStyleSheet(u"border: solid 5px black;\n"
"")

        self.horizontalLayout_6.addWidget(self.mineLine)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 16))
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"")

        self.verticalLayout_10.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.vsCodeButton = QPushButton(self.scrollAreaWidgetContents)
        self.vsCodeButton.setObjectName(u"vsCodeButton")
        self.vsCodeButton.setStyleSheet(u"border: solid 5px black;\n"
"padding:   3px 20px;")

        self.horizontalLayout_7.addWidget(self.vsCodeButton)

        self.vsCodeLine = QLineEdit(self.scrollAreaWidgetContents)
        self.vsCodeLine.setObjectName(u"vsCodeLine")
        self.vsCodeLine.setStyleSheet(u"border: solid 5px black;\n"
"")

        self.horizontalLayout_7.addWidget(self.vsCodeLine)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_8.addWidget(self.saveButton)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.autoStartBtn.setText(QCoreApplication.translate("Dialog", u"auto start", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0441\u0442\u0430\u0440\u0442 \u0441\u043b\u043e\u0432\u0430", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"terminator", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"grapefruit", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"jarvis", None))
        self.checkBox_12.setText(QCoreApplication.translate("Dialog", u"porcupine", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"americano", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"computer", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"grasshopper", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"bumblebee", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"hey google", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"picovoice", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"hey barista", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"hey siri", None))
        self.checkBox_13.setText(QCoreApplication.translate("Dialog", u"alexa", None))
        self.checkBox_15.setText(QCoreApplication.translate("Dialog", u"ok google", None))
        self.checkBox_14.setText(QCoreApplication.translate("Dialog", u"blueberry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("Dialog", u"general", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Discord", None))
        self.discordButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Steam", None))
        self.steamButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Epic Games", None))
        self.epicButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"GtaRp", None))
        self.gtaButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Minecraft", None))
        self.mineButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"vsCode", None))
        self.vsCodeButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Dialog", u"directories", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

