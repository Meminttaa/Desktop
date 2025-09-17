import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        # Загружаем интерфейс из файла dialog.ui
        uic.loadUi('dialog.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())