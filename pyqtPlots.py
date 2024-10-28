from pickle import TRUE
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QTimer
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Gráfico Temperatura vs. Tiempo
        self.plot_graph = pg.PlotWidget()
        
        # Seteando color de fondo
        # self.plot_graph.setBackground("#bbccaa")
        # self.plot_graph.setBackground((100, 50, 255))  # RGB each 0-255
        # self.plot_graph.setBackground((100, 50, 255, 25))  # RGBA (A = alpha opacity)
        # self.plot_graph.setBackground(QColor(100, 50, 254, 25)) #QtGui.QColor
        self.plot_graph.setBackground("w")

        # Line Color, Width, and Style
        pen = pg.mkPen(color=(255,0,0), width=5, style=Qt.PenStyle.DashLine)

        # Seteando el título
        self.plot_graph.setTitle("Temperartura Vs. Tiempo", color="b", size="20pt")

        # Etiqueta de los ejes (requiere posición y texto)
        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("left", "Temperatura (ºC)", **styles)
        self.plot_graph.setLabel("bottom", "Tiempo (min)", **styles)

        # Leyendas
        self.plot_graph.addLegend()

        # Fondo de grilla
        self.plot_graph.showGrid(x=True, y=True)

        # Rango de los ejes
        self.plot_graph.setXRange(1, 10)
        self.plot_graph.setYRange(20, 40)

        self.setCentralWidget(self.plot_graph)

        minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]

        self.plot_line("Sensor de temperatura 1", minutes, temperature_1, pen, "b")

        # Agregando segunda línea al gráfico
        temperature_2 = [32, 35, 40, 22, 38, 32, 27, 38, 32, 38]
        pen=pg.mkPen(color=(0, 0, 255))
        self.plot_line("Sensor de temperatura 2", minutes, temperature_2, pen, "r")

    def plot_line(self, name, minutes, temperature, pen, brush):
        self.plot_graph.plot(
            minutes,
            temperature,
            name=name,
            pen=pen,
            symbol="o",
            symbolSize=15,
            symbolBrush=brush,
        )

# Gráfico dinámico
class MainWindowDynamicPlot(MainWindow):
    def __init__(self):
        super().__init__()

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        self.plot_graph.setBackground("w")
        pen=pg.mkPen(color=(255, 0, 0))

        self.plot_graph.setTitle("Temperatura Vs. Tiempo", color="b", size="20pt")
        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("left", "Temperatura (°C)", **styles)
        self.plot_graph.setLabel("bottom", "Tiempo (min)", **styles)

        self.plot_graph.addLegend()
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setYRange(20, 40)
        self.time = list(range(10))
        self.temperature = [randint(20, 40) for _ in range(10)]

        # Obtiene una línea de referencia
        self.line = self.plot_graph.plot(
            self.time,
            self.temperature,
            name="Sensor de temperatura",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b",
        )

        # Agrega un temporizador para simular nuevas medidas de temperatura
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    
    def update_plot(self):
        self.time = self.time[1:]
        self.time.append(self.time[-1] + 1)
        self.temperature = self.temperature[1:]
        self.temperature.append(randint(20, 40))
        self.line.setData(self.time, self.temperature)

app = QApplication([])
main = MainWindowDynamicPlot()
main.show()
app.exec()