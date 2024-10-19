import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar,
    QCheckBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

class MainWindowToolbar(QMainWindow):

    def __init__(self):
        super(MainWindowToolbar, self).__init__()

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

    def onMyToolbarButtonClick(self, s):
        print("Click", s)


app = QApplication(sys.argv)
w = MainWindowToolbar()
w.show()
app.exec()