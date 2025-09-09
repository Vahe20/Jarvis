from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer
import re
import requests


class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Загрузка погоды...")
        layout.addWidget(self.label)

        def update_weather():
            try:
                city = "Yerevan"
                url = f"http://wttr.in/{city}?format=3"
                response = requests.get(url, timeout=5)
                response.raise_for_status()

                data = response.text.strip()

                # температура
                match_temp = re.search(r"(-?\d+)", data)
                temperature = match_temp.group(0) if match_temp else "?"

                # описание (первое слово после города)
                parts = data.split()
                description = parts[-1] if len(parts) > 1 else "Нет данных"

                self.label.setText(f"{temperature}°C\n")

            except requests.exceptions.RequestException as e:
                self.label.setText("Ошибка: нет соединения")
                print("Ошибка запроса погоды:", e)
            except Exception as e:
                self.label.setText("Ошибка при парсинге")
                print("Ошибка парсинга погоды:", e)

        # первый вызов
        update_weather()

        # обновление каждые 10 минут
        self.timer = QTimer(self)
        self.timer.timeout.connect(update_weather)
        self.timer.start(600000)
