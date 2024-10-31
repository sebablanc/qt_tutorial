from math import log
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtGui import QPen, QBrush, QColor, QPainter
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup, QSize, QPoint, pyqtSlot, QRectF, QPointF, pyqtProperty

DEFAULT_CHECKED_COLOR = "#00B0FF"
DEFAULT_PULSE_UNCHECKED_COLOR = "#44999999"
DEFAULT_PULSE_CHECKED_COLOR = "#4400B0EE"

class AnimatedToggle(QCheckBox):
    _transparent_pen = QPen(Qt.GlobalColor.transparent)
    _light_gray_pen = QPen(Qt.GlobalColor.lightGray)

    def __init__(self, parent=None, bar_color=Qt.GlobalColor.gray, checked_color=DEFAULT_CHECKED_COLOR, handle_color=Qt.GlobalColor.white,
                 pulse_unchecked_color=DEFAULT_PULSE_UNCHECKED_COLOR, pulse_checked_color=DEFAULT_PULSE_CHECKED_COLOR):
        super().__init__(parent)

        self._bar_brush = QBrush(bar_color)
        self._bar_checked_brush = QBrush(QColor(checked_color).lighter())
        self._handle_brush = QBrush(handle_color)
        self._handle_checked_brush = QBrush(QColor(checked_color))

        self._pulse_unchecked_animation = QBrush(QColor(pulse_unchecked_color))
        self._pulse_checked_animation = QBrush(QColor(pulse_checked_color))

        self.setContentsMargins(8, 0, 8, 0)
        self._handle_position = 0

        self._pulse_radius = 0

        self.animation = QPropertyAnimation(self, b"handle_position", self)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.setDuration(200)

        self.pulse_anim = QPropertyAnimation(self, b"pulse_radius", self)
        self.pulse_anim.setDuration(350)
        self.pulse_anim.setStartValue(10)
        self.pulse_anim.setEndValue(20)

        self.animations_group = QSequentialAnimationGroup()
        self.animations_group.addAnimation(self.animation)
        self.animations_group.addAnimation(self.pulse_anim)

        self.stateChanged.connect(self.setup_animation)
    
    def sizeHint(self):
        return QSize(58, 45)
    
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)
    
    @pyqtSlot(int)
    def setup_animation(self, value):
        self.animations_group.stop()
        if value:
            self.animation.setEndValue(1)
        else:
            self.animation.setEndValue(0)
        
        self.animations_group.start()
    
    def paintEvent(self, a0):
        contRect = self.contentsRect()
        handleRadius = round(0.24 * contRect.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(self._transparent_pen)

        barRect = QRectF(
            0, 0,
            contRect.width() - handleRadius, 0.40 * contRect.height()
        )

        barRect.moveCenter(QPointF(contRect.center()))

        rounding = barRect.height() / 2

        trailLength = contRect.width() - 2 * handleRadius

        xPos = contRect.x() + handleRadius + trailLength * self._handle_position

        if self.pulse_anim.state() == QPropertyAnimation.State.Running:
            painter.setBrush(
                self._pulse_checked_animation if self.isChecked() else self._pulse_unchecked_animation)
            painter.drawEllipse(QPointF(xPos, barRect.center().y()), self._pulse_radius, self._pulse_radius)
        
        if self.isChecked():
            painter.setBrush(self._bar_checked_brush)
            painter.drawRoundedRect(barRect, rounding, rounding)
            painter.setBrush(self._handle_checked_brush)

        else:
            painter.setBrush(self._bar_brush)
            painter.drawRoundedRect(barRect, rounding, rounding)
            painter.setPen(self._light_gray_pen)
            painter.setBrush(self._handle_brush)

        painter.drawEllipse(QPointF(xPos, barRect.center().y()), handleRadius, handleRadius)

        painter.end()

    @pyqtProperty(float)
    def handle_position(self):
        return self._handle_position
    
    @handle_position.setter
    def handle_position(self, pos):
        self._handle_position = pos
        self.update()
    
    @pyqtProperty(float)
    def pulse_radius(self):
        return self._pulse_radius
    
    @pulse_radius.setter
    def pulse_radius(self, radius):
        self._pulse_radius = radius
        self.update()
