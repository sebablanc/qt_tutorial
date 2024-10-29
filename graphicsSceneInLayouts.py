import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QSlider,
    QGraphicsView,
)
from PyQt6.QtGui import QBrush, QPen, QPainter


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la escena
        self.scene = QGraphicsScene(0, 0, 400, 200)

        # Dibujamos un rectangulo
        rect = QGraphicsRectItem(0, 0, 200, 50)
        rect.setPos(50, 20)
        brush = QBrush(Qt.GlobalColor.red)
        rect.setBrush(brush)
        pen = QPen(Qt.GlobalColor.cyan)
        pen.setWidth(10)
        rect.setPen(pen)

        # Dibujamos un circulo
        ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
        ellipse.setPos(75, 30)
        brush = QBrush(Qt.GlobalColor.blue)
        ellipse.setBrush(brush)
        pen = QPen(Qt.GlobalColor.green)
        pen.setWidth(5)
        ellipse.setPen(pen)

        # Agregamos los elementos a la escena
        self.scene.addItem(ellipse)
        self.scene.addItem(rect)

        # Hacemos que todos los items sean movibles y seleccionables
        for item in self.scene.items():
            item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
            item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        # Definimos un layout vertical
        vbox = QVBoxLayout()

        # Definimos boton UP
        up = QPushButton("Up")
        up.clicked.connect(self.up)
        vbox.addWidget(up)

        # Definimos boton DOWN
        down = QPushButton("Down")
        down.clicked.connect(self.down)
        vbox.addWidget(down)

        # Definimos Slider
        rotate = QSlider()
        rotate.setRange(0, 360)
        rotate.valueChanged.connect(self.rotate)
        vbox.addWidget(rotate)

        # Definimos la vista Grafica
        view = QGraphicsView(self.scene)
        view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Definimos un layout horizontal
        hbox = QHBoxLayout(self)
        hbox.addLayout(vbox)
        hbox.addWidget(view)

        self.setLayout(hbox)
    
    def up(self):
        # Itera y mueve todos los elementos de la escena hacia adelante
        items = self.scene.selectedItems()
        for item in items:
            z = item.zValue()
            item.setZValue(z + 1)

    def down(self):
        # Itera y mueve todos los elementos de la escena hacia atras
        items = self.scene.selectedItems()
        for item in items:
            z = item.zValue()
            item.setZValue(z - 1)

    def rotate(self, value):
        # Rota los objetos segun los grados recibidos en value
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(value)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
