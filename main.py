import asyncio
import sys

from PySide6.QtWidgets import QApplication
import qasync
from gui.main_GUI import ExpenseTracker

# from gui2.main_window import MainWindow

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    # window = MainWindow()
    window.show()

    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    with loop:
        loop.run_forever()