from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, QThread, Signal
from plagins.Ai import get_status_gpt


class AIThread(QThread):
    status_ready = Signal(bool, str)  # AI_ok, Ai_info

    def run(self):
        try:
            AI_ok, Ai_info = get_status_gpt()
            self.status_ready.emit(AI_ok, Ai_info)
        except Exception as e:
            self.status_ready.emit(False, "Ошибка подключения")
            print("Ошибка get_status_gpt:", e)


class AIWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.content = QLabel("Загрузка статуса AI...")
        layout.addWidget(self.content)

        # первый запуск
        self.update_info()

        # обновление каждые 10 секунд
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(10000)

    def update_info(self):
        self.thread = AIThread()
        self.thread.status_ready.connect(self.update_label)
        self.thread.start()

    def update_label(self, AI_ok, Ai_info):
        self.content.setText(f"{'✅' if AI_ok else '❌'} {Ai_info}")
