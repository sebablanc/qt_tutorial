from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from animatedToggle import AnimatedToggle

app = QApplication([])
window = QWidget()

mainToggle = AnimatedToggle()
secondaryToggle = AnimatedToggle(
    checked_color="#FFB000",
    pulse_checked_color="#44FFB000"
)

mainToggle.setFixedSize(mainToggle.sizeHint())
secondaryToggle.setFixedSize(mainToggle.sizeHint())

window.setLayout(QVBoxLayout())
window.layout().addWidget(QLabel("Opcion principal"))
window.layout().addWidget(mainToggle)

window.layout().addWidget(QLabel("Opcion secundaria"))
window.layout().addWidget(secondaryToggle)

mainToggle.stateChanged.connect(secondaryToggle.setChecked)

window.show()
app.exec()
