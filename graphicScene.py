import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItem
from PyQt6.QtGui import QBrush, QPen, QPolygonF, QPixmap, QPainter
from PyQt6.QtCore import Qt, QPointF

app = QApplication(sys.argv)

# Definimos una Escena de 400x200 con un origen en 0,0
# Si no lo creamos en la creacion, se lo puede crear después con un .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)

# RECTANGULO
# Dibujamos un rectángulo, y seteamos el tamaño
rect = QGraphicsRectItem(0, 0, 200, 50)

# Seteamos la posición de origen del rectangulo en la escena
rect.setPos(50, 20)

# Definimos el Brush (relleno)
brush = QBrush(Qt.GlobalColor.red)
rect.setBrush(brush)

# Definimos el pen (contorno)
pen = QPen(Qt.GlobalColor.cyan)
pen.setWidth(10)
rect.setPen(pen)

# CIRCULO
ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
ellipse.setPos(75, 30)
brush = QBrush(Qt.GlobalColor.blue)
ellipse.setBrush(brush)
pen = QPen(Qt.GlobalColor.green)
pen.setWidth(5)
ellipse.setPen(pen)

# Ordenando los elementos
rect.setZValue(200)
ellipse.setZValue(500)

# Otra opción de ordenamiento
# ellipse.stackAfter(rect) <--- o .stackBefore()

scene.addItem(ellipse)
scene.addItem(rect)

# Permitimos que el círculo sea movible
ellipse.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

# Agrega Texto
textItem = scene.addText("QGraphics es divertido!")
textItem.setPos(100, 100)

# Agrega polígono
scene.addPolygon(
    QPolygonF([
        QPointF(30, 60),
        QPointF(270, 40),
        QPointF(400, 200),
        QPointF(20, 150),
    ]),
    QPen(Qt.GlobalColor.darkGreen)
)

# Agrega pixmap
pixmap = QPixmap("./icons/bug.png")
pixmapItem = scene.addPixmap(pixmap)
pixmapItem.setPos(250, 70)

view = QGraphicsView(scene)
view.setRenderHint(QPainter.RenderHint.Antialiasing)
view.show()
app.exec()