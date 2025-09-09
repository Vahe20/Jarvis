from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QTimer, QSize


class CircularWidget(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(200, 200))
        self.setStyleSheet("""
            QPushButton {
                border-radius: 100px;
                background-color: #00c8ff;
                color: black;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #0090cc;
            }
        """)
        
        self.status = False
        
        self.ripples = []  # список активных колец
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)

    def toggle_animation(self):
        if self.timer.isActive():
            self.status = False
            if len(self.ripples) == 0:
                self.timer.stop()
        else:
            self.status = True
            self.timer.start(50)
    def update_animation(self):
        if not self.status and len(self.ripples) == 0:
            self.toggle_animation()
        
        # добавляем новое кольцо каждые 15 кадров
        if len(self.ripples) == 0 or self.ripples[-1]['radius'] > 60 and self.status:
            self.ripples.append({'radius': 30, 'alpha': 255})

        # обновляем все кольца
        for ripple in self.ripples:
            ripple['radius'] += 1      # скорость расширения
            ripple['alpha'] -= 2.5       # скорость исчезновения

        # удаляем полностью прозрачные кольца
        self.ripples = [r for r in self.ripples if r['alpha'] > 0]

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center = self.rect().center()

        # рисуем все активные кольца
        for ripple in self.ripples:
            color = QColor(0, 200, 255, ripple['alpha'])
            pen = QPen(color, 3)
            painter.setPen(pen)
            painter.setBrush(QColor(0, 0, 0, 0))  # пустой внутри
            painter.drawEllipse(center, ripple['radius'], ripple['radius'])

        # центральный пустой круг
        central_radius = 90  # увеличенный радиус
        pen = QPen(QColor(0, 200, 255), 3)
        painter.setPen(pen)
        painter.setBrush(QColor(0, 0, 0, 0))  # пустой внутри
        painter.drawEllipse(center, central_radius, central_radius)
        
        pen = QPen(QColor(0, 200, 255), 3)
        painter.setPen(pen)
        painter.setBrush(QColor(0, 0, 0, 0))  # пустой внутри
        painter.drawEllipse(center, 60, 5)

        # рисуем центральный кружок
        pen = QPen(QColor(0, 200, 255), 3)
        painter.setPen(pen)
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.drawEllipse(center, 30, 30)
        
        


