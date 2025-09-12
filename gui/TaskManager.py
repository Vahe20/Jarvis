from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QScrollArea,
    QHBoxLayout, QPushButton, QLabel, QLineEdit
)
from PySide6.QtGui import QPainter, QColor, QRadialGradient, QIcon
from PySide6.QtCore import Qt, QSize
import json
import os


class Task:
    def __init__(self, description, status="в процессе"):
        self.description = description
        self.status = status

    def to_dict(self):
        return {"description": self.description, "status": self.status}

    @staticmethod
    def from_dict(data):
        return Task(data["description"], data["status"])


class TaskWidget(QWidget):
    def __init__(self, task, on_status_change, on_delete):
        super().__init__()
        self.task = task

        layout = QHBoxLayout(self)

        self.description_label = QLabel(task.description)
        self.status_label = QLabel(task.status)

        self.status_btn = QPushButton("Изменить статус")
        self.status_btn.clicked.connect(lambda: on_status_change(self.task, self.status_label))

        self.delete_btn = QPushButton("Удалить")
        self.delete_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete_btn.clicked.connect(lambda: on_delete(self.task))

        layout.addWidget(self.description_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_btn)
        layout.addWidget(self.delete_btn)


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager")
        self.resize(800, 500)
        self.setStyleSheet(open("assets/styles.qss", "r").read())
        icon = QIcon()
        icon.addFile(u"./assets/icons/reactor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)

        self.Tasks = []
        self.loadTasks()

        # === Центральный виджет ===
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        # === Скролл для задач ===
        self.scroll_area = QScrollArea()
        # self.scroll_area.setStyleSheet("background-color: transparent; border: none;")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName("tasks_container")
        self.scroll_widget.setAttribute(Qt.WA_StyledBackground, True)
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)

        self.main_layout.addWidget(self.scroll_area)

        # === Нижняя панель ===
        self.bottom_layout = QHBoxLayout()
        self.task_description_input = QLineEdit()
        self.task_description_input.setPlaceholderText("Введите задачу...")
        self.create_task_btn = QPushButton("Создать задачу")
        self.create_task_btn.clicked.connect(self.handle_add_task)

        self.bottom_layout.addWidget(self.task_description_input)
        self.bottom_layout.addWidget(self.create_task_btn)
        self.bottom_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.main_layout.addLayout(self.bottom_layout)

        # Первичная отрисовка
        self.render_tasks()
        
    

    # === Работа с задачами ===
    def handle_add_task(self):
        text = self.task_description_input.text().strip()
        if text:
            self.create_task(text)
            self.task_description_input.clear()

    def create_task(self, description, status="в процессе"):
        task = Task(description, status)
        self.Tasks.append(task)
        self.saveTasks()
        self.render_tasks()

    def delete_task(self, task):
        self.Tasks.remove(task)
        self.saveTasks()
        self.render_tasks()

    def handle_status_change(self, task, status_label):
        task.status = "выполнено" if task.status == "в процессе" else "в процессе"
        status_label.setText(task.status)
        self.saveTasks()

    # === Рендер ===
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def render_tasks(self):
        self.clear_layout(self.scroll_layout)
        for task in self.Tasks:
            task_widget = TaskWidget(
                task,
                on_status_change=self.handle_status_change,
                on_delete=self.delete_task
            )
            self.scroll_layout.addWidget(task_widget)

    # === Сохранение / Загрузка ===
    def loadTasks(self):
        if not os.path.exists("tasks.json"):
            self.Tasks = []
            return
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.Tasks = [Task.from_dict(t) for t in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.Tasks = []

    def saveTasks(self):
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.Tasks], f, ensure_ascii=False, indent=2)

    # === Фон ===
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QRadialGradient(
            self.width() / 2, self.height() / 2,
            max(self.width(), self.height()) / 2
        )
        gradient.setColorAt(0.0, QColor(6, 6, 107))
        gradient.setColorAt(1.0, QColor(0, 0, 0))
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())
