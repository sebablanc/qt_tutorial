import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from UIs.mainwindow import Ui_MainWindow

# Cargando archivo .ui directamente
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         uic.loadUi("UIs/mainwindow.ui", self)

# Con archivo mainwindow.py
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()