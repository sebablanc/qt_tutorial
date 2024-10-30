from random import choice, randint
import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QBrush, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        canvas = QPixmap(700, 600)
        canvas.fill(Qt.GlobalColor.white)

        self.label = QLabel()
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.draw_text()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.drawLine(10, 10, 700, 600)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_point(self):
        colors = ["#FFD141", "#376F9F", "#0D1F2D", "#E9EBEF", "#EB5160"]

        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)

        for n in range(10000):
            pen.setColor(QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(0 + randint(-700, 700), 0 + randint(-600, 600))
        painter.end()
        self.label.setPixmap(canvas)

    def draw_line(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(15)
        pen.setColor(QColor("blue"))
        painter.setPen(pen)
        painter.drawLine(QPoint(100, 100), QPoint(300, 200))
        painter.end()
        self.label.setPixmap(canvas)
    
    def draw_rects(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#EB5160"))
        painter.setPen(pen)

        # Pintamos el rectangulo
        brush = QBrush()
        brush.setColor(QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)

        # Dibjuando rectangulos
        painter.drawRect(50, 50, 100, 100)
        painter.drawRect(60, 60, 150, 100)
        painter.drawRect(70, 70, 100, 150)
        painter.drawRect(80, 80, 150, 100)

        #Dibujamos un rectangulo redondeado
        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)

        # Otra forma
        # painter.drawRects(
            # QtCore.QRect(50, 50, 100, 100),
            # QtCore.QRect(60, 60, 150, 100),
            # QtCore.QRect(70, 70, 100, 150),
            # QtCore.QRect(80, 80, 150, 100),
            # QtCore.QRect(90, 90, 100, 150),
        # )

        painter.end()
        self.label.setPixmap(canvas)
    
    def draw_ellipse(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(204,0,0))  # r, g, b
        painter.setPen(pen)

        # Dibujando circulos
        painter.drawEllipse(10, 10, 100, 100)
        painter.drawEllipse(10, 10, 150, 200)
        painter.drawEllipse(10, 10, 200, 300)

        # Otra forma de dibujar circulos
        # painter.drawEllipse(QtCore.QPoint(100, 100), 10, 10)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 15, 20)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 20, 30)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 25, 40)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 30, 50)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 35, 60)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_text(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('green'))
        painter.setPen(pen)

        # Establecemos una fuente y sus caracteristicas
        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        # Escribimos el texto y la posicion en la que empieza
        painter.drawText(100, 100, 'Hola, mundo!')
        painter.end()
        self.label.setPixmap(canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
