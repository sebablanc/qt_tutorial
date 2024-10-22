import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar,
    QCheckBox
)
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QSize

# Ejemplo Toolbar y Menu
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Toolbar App")

        label = QLabel("Hola")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('icons/bug.png'), '&La acción1', self)
        button_action.setStatusTip("Este es tu botón")
        button_action.triggered.connect(self.onMyToolbarButtonClick)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('icons/bug.png'), 'La &acción2', self)
        button_action2.setStatusTip("Este es tu botón 2")
        button_action2.triggered.connect(self.onMyToolbarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("hola"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        # Creando el menu
        menu = self.menuBar()

        # Creando opcion File
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        # Creando submenu
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolbarButtonClick(self, s):
        print("Click", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()