import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget

from layout_colorwidget import Color

# Layout Vertical
# class MainWindowVBoxLayout(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("App Layouts")

#         layout = QVBoxLayout()
#         layout.addWidget(Color("red"))
#         layout.addWidget(Color("yellow"))
#         layout.addWidget(Color("orange"))
#         layout.addWidget(Color("green"))
#         layout.addWidget(Color("blue"))

#         widget = QWidget()
#         widget.setLayout(layout)
        
#         self.setCentralWidget(widget)

# Layout Horizontal
# class MainWindowHBoxLayout(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("App Layouts")

#         layout = QHBoxLayout()
#         layout.addWidget(Color("gray"))
#         layout.addWidget(Color("black"))
#         layout.addWidget(Color("orange"))
#         layout.addWidget(Color("green"))
#         layout.addWidget(Color("blue"))

#         widget = QWidget()
#         widget.setLayout(layout)
        
#         self.setCentralWidget(widget)

# Layout anidado
# class MainWindowNestedLayout(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("App Layouts")

#         layout1 = QHBoxLayout()
#         layout2 = QVBoxLayout()
#         layout3 = QVBoxLayout()

#         layout2.addWidget(Color("gray"))
#         layout2.addWidget(Color("black"))
#         layout2.addWidget(Color("orange"))
        
#         layout1.addLayout(layout2)
#         layout1.addWidget(Color("green"))
        
#         layout3.addWidget(Color("blue"))
#         layout3.addWidget(Color("purple"))
        
#         layout1.addLayout(layout3)

#         layout1.setContentsMargins(0, 0, 0, 0)
#         layout1.setSpacing(20)

#         widget = QWidget()
#         widget.setLayout(layout1)
        
#         self.setCentralWidget(widget)

# Grid Layout
# class MainWindowGridLayout(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("App Layouts")

#         layout = QGridLayout()

#         layout.addWidget(Color("gray"), 0, 3)
#         layout.addWidget(Color("black"), 1, 1)
#         layout.addWidget(Color("orange"), 2, 2)
#         layout.addWidget(Color("green"), 3, 0)

#         widget = QWidget()
#         widget.setLayout(layout)
        
#         self.setCentralWidget(widget)

# Pila layout
# class MainWindowStackedLayout(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("App Layouts")

#         pagelayout = QVBoxLayout()
#         button_layout = QHBoxLayout()
#         self.stacklayout = QStackedLayout()

#         pagelayout.addLayout(button_layout)
#         pagelayout.addLayout(self.stacklayout)

#         btn = QPushButton("red")
#         btn.pressed.connect(self.activate_tab_1)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("red"))

#         btn = QPushButton("green")
#         btn.pressed.connect(self.activate_tab_2)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("green"))

#         btn = QPushButton("yellow")
#         btn.pressed.connect(self.activate_tab_3)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("yellow"))

#         widget = QWidget()
#         widget.setLayout(pagelayout)
#         self.setCentralWidget(widget)

#     def activate_tab_1(self):
#         self.stacklayout.setCurrentIndex(0)

#     def activate_tab_2(self):
#         self.stacklayout.setCurrentIndex(1)

#     def activate_tab_3(self):
#         self.stacklayout.setCurrentIndex(2)

# QTabWidget
class MainWindowQTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Layouts")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindowQTabWidget()
window.show()
app.exec()