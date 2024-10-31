from PyQt6.QtWidgets import QApplication
from power_bar import PowerBar

app = QApplication([])
#volume = PowerBar()
#volume = PowerBar(10)
# volume = PowerBar(["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f", "#9e0142"])
volume = PowerBar(["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
volume.setBarPadding(2)
volume.setBarSolidPercent(0.9)
volume.setBackgroundColor('gray')
volume.show()
app.exec()