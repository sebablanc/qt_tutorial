import sys
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget, QProgressBar
from PyQt6.QtCore import QProcess

progress_re = re.compile("Total complete: (\d+)%")

def simple_percent_parser(output):
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.process = None

        self.btn = QPushButton("Ejecutar")
        self.btn.pressed.connect(self.start_process)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.progress)
        layout.addWidget(self.text)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def message(self, text):
        self.text.appendPlainText(text)

    def start_process(self):
        if self.process is None:
            self.message("Ejecutando el proceso.")
            # Crea el proceso para ejecutar un programa externo
            self.process = QProcess()
            
            # Maneja los eventos de los procesos
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.stateChanged.connect(self.handle_state_changes)

            self.process.finished.connect(self.process_finished)
            self.process.start("python3", ["dummy_script.py"])
        '''
            Hay que tener en cuenta que se debe mantener una referencia al objeto QProcess creado mientras se ejecuta, 
            por ejemplo, en self.process. De lo contrario, el objeto se eliminará de forma prematura e indicará el error
            QProcess: Destroyed while process ("python3") is still running.
        '''

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("latin-1")
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)
    
    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("latin-1")
        self.message(stdout)
    
    def handle_state_changes(self, state):
        states = {
            QProcess.ProcessState.NotRunning: 'Detenido',
            QProcess.ProcessState.Starting: 'Comenzando',
            QProcess.ProcessState.Running: 'Corriendo',
        }

        state_name = states[state]
        self.message(f"El estado cambio a: {state_name}")

    def process_finished(self):
        self.message("Proceso finalizado")
        self.process = None

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()