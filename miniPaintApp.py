import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt, QSize

COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    "#000000",
    "#141923",
    "#414168",
    "#3a7fa7",
    "#35e3e3",
    "#8fd970",
    "#5ebb49",
    "#458352",
    "#dcd37b",
    "#fffee5",
    "#ffd035",
    "#cc9245",
    "#a15c3e",
    "#a42f3b",
    "#f45b7a",
    "#c24998",
    "#81588d",
    "#bcb0c2",
    "#ffffff",
]


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super().__init__()

        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)

        self.last_x, self.last_y = None, None

        self.pen_color = QColor("#000000")

        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.label)

        palette = QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def set_pen_color(self, color):
        self.pen_color = QColor(color)
    
    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.set_pen_color(c))
            layout.addWidget(b)

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = int(e.position().x())
            self.last_y = int(e.position().y())
            return

        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = painter.pen()
        pen.setWidth(4)
        pen.setColor(self.pen_color)
        painter.setPen(pen)
        painter.drawLine(
            self.last_x, self.last_y, int(e.position().x()), int(e.position().y())
        )
        painter.end()
        self.label.setPixmap(canvas)

        self.last_x = int(e.position().x())
        self.last_y = int(e.position().y())

    def mouseReleaseEvent(self, a0):
        self.last_x, self.last_y = None, None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
