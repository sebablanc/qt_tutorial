from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QColorDialog

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Creamos el icono
icon = QIcon("./icons/bug.png")

clipboard = QApplication.clipboard()
dialog = QColorDialog()

def copy_color_hex():
    if dialog.exec():
        color = dialog.currentColor()
        clipboard.setText(color.name())

def copy_color_rgb():
    if dialog.exec():
        color = dialog.currentColor()
        clipboard.setText("rgb(%d, %d, %d)" % (
            color.red(), color.green(), color.blue()
        ))
    
def copy_color_hsv():
    if dialog.exec():
        color = dialog.currentColor()
        clipboard.setText("hsv(%d, %d, %d)" % (
            color.hue(), color.saturation(), color.value()
        ))

# Creamos el "tray"
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creamos el menu
menu = QMenu()

# Agregamos opción de color HEX
action1 = QAction("HEX")
action1.triggered.connect(copy_color_hex)
menu.addAction(action1)

# Agregamos opción de color RGB
action2 = QAction("RGB")
action2.triggered.connect(copy_color_rgb)
menu.addAction(action2)

# Agregamos opción de color HSV
action3 = QAction("HSV")
action3.triggered.connect(copy_color_hsv)
menu.addAction(action3)

# Agregamos opción de cierre al menu
quit = QAction("Cerrar")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Agregamos el menu al "Tray"
tray.setContextMenu(menu)

app.exec()