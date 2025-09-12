from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import QThread, QObject, Signal, QTimer
import psutil


class SystemInfoWorker(QObject):
    updated = Signal(float, float, float)  # CPU, RAM, NET

    def __init__(self):
        super().__init__()
        self.prev_net = psutil.net_io_counters().bytes_recv
        self.timer = None

    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        net = psutil.net_io_counters().bytes_recv
        net_speed = (net - self.prev_net) / 1024  # KB/s
        self.prev_net = net

        self.updated.emit(cpu, ram, net_speed)

    def stop(self):
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None


class SystemInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.cpu_label = QLabel("CPU:")
        self.cpu_bar = QProgressBar()

        self.ram_label = QLabel("RAM:")
        self.ram_bar = QProgressBar()

        self.net_label = QLabel("NET:")
        self.net_bar = QProgressBar()

        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_bar)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_bar)
        layout.addWidget(self.net_label)
        layout.addWidget(self.net_bar)

        self.thread = QThread()
        self.worker = SystemInfoWorker()
        self.worker.moveToThread(self.thread)

        self.worker.updated.connect(self.update_info)

        self.thread.started.connect(self.worker.start)
        self.thread.start()

    def update_info(self, cpu, ram, net_speed):
        self.cpu_bar.setValue(int(cpu))
        self.ram_bar.setValue(int(ram))
        self.net_bar.setValue(int(net_speed))

        self.cpu_label.setText(f"CPU:\t {cpu:.1f}%")
        self.ram_label.setText(f"RAM:\t {ram:.1f}%")
        self.net_label.setText(f"NET:\t {net_speed:.2f} KB/s")
