from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSize, QSequentialAnimationGroup, QParallelAnimationGroup


class WindowSequentialAnimation(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color: red; border-radius: 15px")
        self.child.resize(100, 100)

        # Creando la animación
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1500)

        # Agregando curva de animación
        self.anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        # self.anim.setEasingCurve(QEasingCurve.Type.OutInCubic)
        # self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)

        # Creando multiples animaciones
        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(250, 150))
        self.anim_2.setDuration(2000)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        
        self.anim_group.start()

class WindowParallelAnimation(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)

        effect = QGraphicsOpacityEffect(self.child)

        self.child.setGraphicsEffect(effect)
        self.child.setStyleSheet("background-color: red; border-radius: 15px")
        self.child.resize(100, 100)

        # Creando la animación
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1500)


        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(2500)

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        
        self.anim_group.start()
    

app = QApplication([])
window = WindowParallelAnimation()
window.show()
app.exec()
