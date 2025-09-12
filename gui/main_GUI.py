import struct
import time
import asyncio
import winreg

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QSystemTrayIcon, QMenu, QFileDialog
from PySide6.QtGui import QAction, QIcon, QPainter, QRadialGradient, QColor
from PySide6.QtCore import Qt

from gui.Jarvis import Ui_MainWindow
from gui.Settings import Ui_Dialog
from gui.TaskManager import TaskManager

import core.recognizer as recognizer
import core.speaker as speaker
import core.jarvis as jarvis

from plagins.window import get_active_window_name


import config.commands as commands
import config.program_finder as program_finder

APP_NAME = "Jarvis"
APP_PATH = commands.dirPath + "\\Jarvis.bat"

def is_autorun_enabled():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                                    0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(reg_key, APP_NAME)
        return value == APP_PATH
    except FileNotFoundError:
        return False

def enable_autorun(enable: bool):
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                0, winreg.KEY_WRITE)
    if enable:
        winreg.SetValueEx(reg_key, APP_NAME, 0, winreg.REG_SZ, APP_PATH)
    else:
        try:
            winreg.DeleteValue(reg_key, APP_NAME)
        except FileNotFoundError:
            pass
    reg_key.Close()
    
        


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        
        self.ui.saveButton.clicked.connect(lambda: self.accept())
        
        self.settings = commands.load_settings()
        
        self.ui.autoStartBtn.setChecked(is_autorun_enabled())

        self.ui.autoStartBtn.toggled.connect(enable_autorun)
        
        self.ui.checkBox_1.setChecked(self.ui.checkBox_1.text() in commands.START_WORD)
        self.ui.checkBox_2.setChecked(self.ui.checkBox_2.text() in commands.START_WORD)
        self.ui.checkBox_3.setChecked(self.ui.checkBox_3.text() in commands.START_WORD)
        self.ui.checkBox_4.setChecked(self.ui.checkBox_4.text() in commands.START_WORD)
        self.ui.checkBox_5.setChecked(self.ui.checkBox_5.text() in commands.START_WORD)
        self.ui.checkBox_6.setChecked(self.ui.checkBox_6.text() in commands.START_WORD)
        self.ui.checkBox_7.setChecked(self.ui.checkBox_7.text() in commands.START_WORD)
        self.ui.checkBox_8.setChecked(self.ui.checkBox_8.text() in commands.START_WORD)
        self.ui.checkBox_9.setChecked(self.ui.checkBox_9.text() in commands.START_WORD)
        self.ui.checkBox_10.setChecked(self.ui.checkBox_10.text() in commands.START_WORD)
        self.ui.checkBox_11.setChecked(self.ui.checkBox_11.text() in commands.START_WORD)
        self.ui.checkBox_12.setChecked(self.ui.checkBox_12.text() in commands.START_WORD)
        self.ui.checkBox_13.setChecked(self.ui.checkBox_13.text() in commands.START_WORD)
        self.ui.checkBox_14.setChecked(self.ui.checkBox_14.text() in commands.START_WORD)
        self.ui.checkBox_15.setChecked(self.ui.checkBox_15.text() in commands.START_WORD)
                
        
        self.ui.steamLine.setText(program_finder.get_program_path("steam", "steam.exe"))
        self.ui.epicLine.setText(program_finder.get_program_path("epicGames", "EpicGamesLauncher.exe"))
        self.ui.discordLine.setText(program_finder.get_program_path("discord", "Update.exe"))
        self.ui.gtaLine.setText(program_finder.get_program_path("gtaRp", "GTA5.exe"))
        self.ui.mineLine.setText(program_finder.get_program_path("minecraft", "TLauncher.exe"))
        self.ui.vsCodeLine.setText(program_finder.get_program_path("vsCode", "Code.exe"))
        

        self.ui.steamButton.clicked.connect(lambda: self.choose_path(self.ui.steamLine))
        self.ui.epicButton.clicked.connect(lambda: self.choose_path(self.ui.epicLine))
        self.ui.discordButton.clicked.connect(lambda: self.choose_path(self.ui.discordLine))
        self.ui.gtaButton.clicked.connect(lambda: self.choose_path(self.ui.gtaLine))
        self.ui.mineButton.clicked.connect(lambda: self.choose_path(self.ui.mineLine))
        self.ui.vsCodeButton.clicked.connect(lambda: self.choose_path(self.ui.vsCodeLine))
        
        
        self.ui.openAI_API.setText(self.settings["API"].get("openAI_API"))
        self.ui.groqAI_API.setText(self.settings["API"].get("groqAI_API"))
        
        self.ui.eleven_API.setText(self.settings["API"].get("eleven_API"))
        
    def paintEvent(self, event):
        painter = QPainter(self)

        # создаём радиальный градиент
        gradient = QRadialGradient(self.width() / 2, self.height() / 2,
                                    max(self.width(), self.height()) / 2)

        # центр = #06066b, края = черные
        gradient.setColorAt(0.0, QColor(6, 6, 107))   # rgba(6, 6, 107, 1)
        gradient.setColorAt(1.0, QColor(0, 0, 0))     # rgba(0, 0, 0, 1)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

    def choose_path(self, name):
        exe = QFileDialog.getOpenFileName(self, "Выберите исполняемый файл", "", "Исполняемый файл (*.exe)")[0]
        if exe:
            name.setText(exe)

    def accept(self):
        self.settings["directories"]["steam"] = self.ui.steamLine.text()
        self.settings["directories"]["epicGames"] = self.ui.epicLine.text()
        self.settings["directories"]["discord"] = self.ui.discordLine.text()
        self.settings["directories"]["gtaRp"] = self.ui.gtaLine.text()
        self.settings["directories"]["minecraft"] = self.ui.mineLine.text()
        self.settings["directories"]["vsCode"] = self.ui.vsCodeLine.text()
        
        self.settings["wake word"]["hey google"] = str(self.ui.checkBox_1.isChecked())
        self.settings["wake word"]["hey siri"] = str(self.ui.checkBox_2.isChecked())
        self.settings["wake word"]["americano"] = str(self.ui.checkBox_3.isChecked())
        self.settings["wake word"]["hey barista"] = str(self.ui.checkBox_4.isChecked())
        self.settings["wake word"]["computer"] = str(self.ui.checkBox_5.isChecked())
        self.settings["wake word"]["grapefruit"] = str(self.ui.checkBox_6.isChecked())
        self.settings["wake word"]["grasshopper"] = str(self.ui.checkBox_7.isChecked())
        self.settings["wake word"]["jarvis"] = str(self.ui.checkBox_8.isChecked())
        self.settings["wake word"]["terminator"] = str(self.ui.checkBox_9.isChecked())
        self.settings["wake word"]["picovoice"] = str(self.ui.checkBox_10.isChecked())
        self.settings["wake word"]["bumblebee"] = str(self.ui.checkBox_11.isChecked())
        self.settings["wake word"]["porcupine"] = str(self.ui.checkBox_12.isChecked())
        self.settings["wake word"]["alexa"] = str(self.ui.checkBox_13.isChecked())
        self.settings["wake word"]["blueberry"] = str(self.ui.checkBox_14.isChecked())
        self.settings["wake word"]["ok google"] = str(self.ui.checkBox_15.isChecked())
        
        self.settings["API"]["openAI_API"] = self.ui.openAI_API.text()
        self.settings["API"]["groqAI_API"] = self.ui.groqAI_API.text()
        
        self.settings["API"]["eleven_API"] = self.ui.eleven_API.text()

        commands.save_settings(self.settings)
        super().accept()

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.jarvis_task = None

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("./assets/icons/reactor.png"))
        
        self.ui.startButton.clicked.connect(self.toggle_jarvis)
        self.ui.settings_btn.clicked.connect(self.open_settings)
        self.ui.quit_btn.clicked.connect(QApplication.quit)
        self.ui.hide_btn.clicked.connect(self.close)
        
        self.ui.Tasks_btn.clicked.connect(self.open_TaskManager)
        
        tray_menu = QMenu()
        restore_action = QAction("Открыть", self)
        quit_action = QAction("Выход", self)
        
        tray_menu.addAction(restore_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        
        
        restore_action.triggered.connect(self.showNormal)
        quit_action.triggered.connect(QApplication.quit)
        self.tray_icon.activated.connect(self.on_tray_click)

        self.tray_icon.show()
        
        speaker.speak_async("Доброе утро")
        
        
    def paintEvent(self, event):
        painter = QPainter(self)

        gradient = QRadialGradient(self.width() / 2, self.height() / 2,
                                    max(self.width(), self.height()) / 2)

        gradient.setColorAt(0.0, QColor(6, 6, 107))
        gradient.setColorAt(1.0, QColor(0, 0, 0))

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())
        
        
    def closeEvent(self, event):
        self.hide()
        event.ignore()
        

    def on_tray_click(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.showNormal()
            
        
    def open_settings(self):
        self.settings_window = SettingsDialog()
        self.settings_window.show()
        
    def open_TaskManager(self):
        self.task_manager = TaskManager()
        self.task_manager.show()

    async def run_jarvis(self):
        commands.wake_word_update()

        while True:            
            pcm = recognizer.stream.read(
                recognizer.porcupine.frame_length,
                exception_on_overflow=False
            )
            pcm = struct.unpack_from("h" * recognizer.porcupine.frame_length, pcm)

            keyword_index = recognizer.porcupine.process(pcm)
            if keyword_index >= 0:
                speaker.speak_async("Да сэр")
                activeWindow = get_active_window_name()

                start_time = time.time()
                while time.time() - start_time < 10:
                    query = recognizer.listen()
                    
                    for alt in query.get("alternatives", []):
                        text = alt["text"].lower()
                        result = await jarvis.handle_command(text)
                        if result == "break":
                            start_time -= 15
                            break
                        elif result == "continue":
                            break
                        elif result == "exit":
                            self.toggle_jarvis()
                            return

            await asyncio.sleep(0.01)

    def toggle_jarvis(self):
        loop = asyncio.get_event_loop()
        self.ui.startButton.toggle_animation()

        if self.jarvis_task is None or self.jarvis_task.done():
            self.jarvis_task = loop.create_task(self.run_jarvis())
        else:
            self.jarvis_task.cancel()
            self.jarvis_task = None