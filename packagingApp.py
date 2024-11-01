import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QIcon

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = 'com.sebablanc.packagingapp.100'
except ImportError:
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hola mundo!")
        layout = QVBoxLayout()
        
        label = QLabel("Mi primera app empaquetada")
        label.setMargin(10)
        layout.addWidget(label)

        button = QPushButton("Push")
        button.setIcon(QIcon(os.path.join(basedir, "icons", "lightning.png")))
        button.pressed.connect(self.close)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, "icons", 'hand.ico')))
    window = MainWindow()
    app.exec()

# COMANDO PARA COMPILAR EL PROYECTO
# pyinstaller -n "Hello World" -w --icon=icons/hand.ico --add-data="icons;icons" packagingApp.py