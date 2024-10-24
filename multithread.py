# Continuar en Thread IO
import sys
import traceback
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSlot, QObject, pyqtSignal, QTimer

import time


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs["progress_callback"] = self.signals.progress

    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel("Empezar")
        layout.addWidget(self.label)

        b = QPushButton("Peligro!")
        b.pressed.connect(self.oh_no)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n * 100 / 4)
        return "Completado!"

    def thread_complete(self):
        print("Thread completado")

    def print_output(self, s):
        print(s)

    def oh_no(self):
        worker = Worker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)

        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec()

"""
    ADVERTENCIAS

    Es posible que hayas detectado la pequeña falla en este plan maestro: todavía estamos utilizando el bucle de eventos
    (y el hilo GUI) para procesar la salida de nuestros Workers.

    Esto no es un problema cuando sólo hacemos un seguimiento del progreso, la finalización o la devolución de metada. Sin embargo,
    si tenemos Workers que devuelven grandes cantidades de datos, pasarlos de nuevo a través del hilo GUI puede causar problemas de rendimiento
    y es mejor evitarlo.

    De manera similar, si la aplicación utiliza una gran cantidad de subprocesos y controladores de resultados de Python, puede encontrarse con las limitaciones
    de GIL. Cuando se utilizan subprocesos, la ejecución de Python está limitada a un solo subproceso a la vez. El código Python que maneja las señales de sus
    subprocesos puede ser bloqueado por los Workers y viceversa. Dado que el bloqueo de sus funciones de ranura bloquea el bucle de eventos, esto puede afectar
    directamente la capacidad de respuesta de la GUI.

    En estos casos, suele ser mejor investigar el uso de un grupo de subprocesos de Python puro para mantener el procesamiento y el manejo de eventos de subprocesos
    aún más aislados de la GUI. Sin embargo, hay que tener en cuenta que cualquier código de GUI de Python puede bloquear otro código de Python a menos que esté
    en un proceso separado.
"""
