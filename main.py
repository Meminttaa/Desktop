import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем интерфейс из файла dialog.ui
        uic.loadUi('mainwindow.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())