import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        uic.loadUi("./UIs/CustomWidget.ui", self)

        self.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])

    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)
    
def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()