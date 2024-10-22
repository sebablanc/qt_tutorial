from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from random import randint

import sys

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel("Otra ventana % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

# Toggling Window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.w = None
#         self.button = QPushButton("Nueva ventana")
#         self.button.clicked.connect(self.show_new_window)
        
#         self.setCentralWidget(self.button)
    
#     def show_new_window(self):
#         if self.w is None:
#             self.w = AnotherWindow()
#             self.w.show()
#         else:
#             self.w.close() # Cierra la ventana
#             self.w = None # Ellimina la referencia

# Ventana persistente
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.w = AnotherWindow()
#         self.button = QPushButton("Nueva ventana")
#         self.button.clicked.connect(self.toggle_window)
        
#         self.setCentralWidget(self.button)
    
#     def toggle_window(self):
#         if self.w.isVisible():
#             self.w.hide()
#         else:
#             self.w.show()

# Multiples ventanas
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Nueva ventana 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Nueva ventana 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        
        self.setCentralWidget(w)
    
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    # def toggle_window1(self):
        # if self.window1.isVisible():
            # self.window1.hide()
        # else:
            # self.window1.show()
    # 
    # def toggle_window2(self):
        # if self.window2.isVisible():
            # self.window2.hide()
        # else:
            # self.window2.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()