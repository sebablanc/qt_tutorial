import sys
import matplotlib
matplotlib.use('QtAgg')

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from random import randint

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindowSimple(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindowSimple, self).__init__(*args, **kwargs)

        # Crea el objeto FigureCanvas de matplotlib
        # define un par de ejes en self.axes
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        
        # Creamos un toolbar
        toolbar = NavigationToolbar(sc, self)
        
        # Creamos un layout
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

class MainWindowDynamicPlot(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindowDynamicPlot, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [randint(0, 10) for i in range(n_data)]

        # Guardamos una referencia a la linea dibujada
        # de esta manera podemos aplicar la nueva información facilmente
        self._plot_ref = None
        self.update_plot()

        self.show()

        # Agregamos un temporizador para simular una acutalización
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Quitamos el primer elemento del eje "y", y agregamos uno nuevo
        self.ydata = self.ydata[1:] + [randint(0, 10)]

        # Nota: no necesitamos limpiar los ejes
        if self._plot_ref is None:
            # Primer uso, no tenemos ningún dibujo, así que se dibuja normalmente
            # .plot retorna una lista de lineas,
            # cómo sólo tomamos una, podemos obtener el primer elemento
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'r')
            self._plot_ref = plot_refs[0]
        else:
            # Tenemos una referencia, podemos usarla para actualizar la información de la línea.
            self._plot_ref.set_ydata(self.ydata)

        # Ejecutamos el canvas para actualizar y redibujar
        self.canvas.draw()


app = QApplication(sys.argv)
w = MainWindowDynamicPlot()
app.exec()