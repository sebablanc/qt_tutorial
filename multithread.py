
# Continuar en Threads and Processes
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget

import time


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel("Empezar")
        layout.addWidget(self.label)
        
        b = QPushButton("Peligro!")
        b.pressed.connect(self.oh_no)
        layout.addWidget(b)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)
        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()


    def change_message(self):
        self.message = "OH NO"

    def oh_no(self):
        self.message = "Pressed"
        for i in range(100):
            time.sleep(0.1)
            self.label.setText(self.message)
            QApplication.processEvents()

app = QApplication([])
window = MainWindow()
app.exec()
