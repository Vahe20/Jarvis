from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QToolButton
from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtGui import QFont, QIcon

from gui.widgets.circular_widget import CircularWidget
from gui.widgets.system_info import SystemInfoWidget
from gui.widgets.weather_widget import WeatherWidget
from gui.widgets.AI_widget import AIWidget

class DraggableHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._mouse_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self._mouse_pos:
            diff = event.globalPosition().toPoint() - self._mouse_pos
            self.window().move(self.window().pos() + diff)
            self._mouse_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._mouse_pos = None


class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):  
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 650)
        MainWindow.setMinimumSize(QSize(550, 650))
        MainWindow.setMaximumSize(QSize(550, 650))
        icon = QIcon()
        icon.addFile(u"./assets/icons/reactor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jarvis", None))
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setStyleSheet(open("assets/styles.qss", "r").read())

        self.central = QWidget()
        self.root_layout = QVBoxLayout(self.central)
        self.root_layout.setContentsMargins(20, 0, 20, 0)

        self.header = DraggableHeader(MainWindow)
        self.header.setContentsMargins(20, 20, 20, 0)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setObjectName("header_layout")
        self.Logo = QLabel("JARVIS")
        self.Logo.setObjectName("Logo")
        self.Logo.setFont(QFont("Segoe UI", 32))
        self.Logo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.settings_btn = QPushButton()
        self.settings_btn.setIcon(QIcon("./assets/icons/settings.png"))
        self.quit_btn = QPushButton("✖")
        self.hide_btn = QPushButton("__")
        for btn in [self.settings_btn, self.quit_btn, self.hide_btn]:
            btn.setFixedSize(40, 40)
            self.header_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignRight)

        self.header_layout.insertWidget(0, self.Logo, 1)
        
        self.body_layout = QHBoxLayout()

        self.system_box = QGroupBox("система")
        self.system_box.setObjectName("system_box")
        self.system_box.setFixedWidth(120)
        self.system_box.setFixedHeight(120)

        self.system_info = SystemInfoWidget()
        self.system_info.setFixedWidth(90)
        self.system_info.setFixedHeight(90)
        
        self.box_layout = QVBoxLayout(self.system_box)
        self.box_layout.addWidget(self.system_info)
        self.body_layout.addWidget(self.system_box, alignment=Qt.AlignmentFlag.AlignBottom, stretch=1)

        self.startButton = CircularWidget()
        self.body_layout.addWidget(self.startButton, 2)
        
        self.right_layout = QVBoxLayout()
        
        self.Weather_box = QGroupBox("погода")
        self.Weather_box.setObjectName("Weather_box")
        self.Weather_box.setFixedWidth(110)
        self.Weather_box.setFixedHeight(110)
        
        self.Weather_info = WeatherWidget()
        self.Weather_info.setFixedWidth(90)
        self.Weather_info.setFixedHeight(90)
        
        self.Weather_box_layout = QVBoxLayout(self.Weather_box)
        self.Weather_box_layout.addWidget(self.Weather_info)
        self.right_layout.addWidget(self.Weather_box)
        
        self.AI_box = QGroupBox("AI статус")
        self.AI_box.setObjectName("AI_box")
        self.AI_box.setFixedWidth(110)
        self.AI_box.setFixedHeight(110)
        
        self.AI_info = AIWidget()
        self.AI_info.setFixedWidth(90)
        self.AI_info.setFixedHeight(90)
        
        self.AI_box_layout = QVBoxLayout(self.AI_box)
        self.AI_box_layout.addWidget(self.AI_info)
        self.right_layout.addWidget(self.AI_box)
        
        self.body_layout.addLayout(self.right_layout, 1)
        
        self.body_layout.setContentsMargins(0, 0, 0, 120)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setObjectName("footer_layout")
        self.footer_layout.setContentsMargins(0, 0, 20, 20)
        self.footer_box = QGroupBox()
        self.footer_box.setObjectName("footer_box")
        self.footer_box.setFixedHeight(70)
        self.footer_layout.addWidget(self.footer_box, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.footer_box_layout = QHBoxLayout(self.footer_box)
        
        self.Doc_btn = QToolButton()
        self.Doc_btn.setText("документация")
        self.Doc_btn.setIcon(QIcon(f"./assets/icons/{"doc"}.png"))
        self.Doc_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Doc_btn.setMinimumHeight(50)
        self.footer_box_layout.addWidget(self.Doc_btn, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.History_btn = QToolButton()
        self.History_btn.setText("история")
        self.History_btn.setIcon(QIcon(f"./assets/icons/{"history"}.png"))
        self.History_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.History_btn.setMinimumHeight(50)
        self.footer_box_layout.addWidget(self.History_btn, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.Timer_btn = QToolButton()
        self.Timer_btn.setText("таймер")
        self.Timer_btn.setIcon(QIcon(f"./assets/icons/{"Timer"}.png"))
        self.Timer_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Timer_btn.setMinimumHeight(50)
        self.footer_box_layout.addWidget(self.Timer_btn, alignment=Qt.AlignmentFlag.AlignRight)
    
        self.Tasks_btn = QToolButton()
        self.Tasks_btn.setText("задачи")
        self.Tasks_btn.setIcon(QIcon(f"./assets/icons/{"Tasks"}.png"))
        self.Tasks_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Tasks_btn.setMinimumHeight(50)
        self.footer_box_layout.addWidget(self.Tasks_btn, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.root_layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignTop)
        self.root_layout.addLayout(self.body_layout, 5)
        self.root_layout.addLayout(self.footer_layout)

        MainWindow.setCentralWidget(self.central)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jarvis", None))

