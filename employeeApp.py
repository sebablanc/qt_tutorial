import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QDialog, QApplication
from UIs.employee import Ui_Dialog

class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.btn = QPushButton("Agregar empleado")

        self.btn.clicked.connect(self.onEmployeeBtnClicked)

        self.setCentralWidget(self.btn)

    def onEmployeeBtnClicked(self):
        """ Abre el Dialog de nuevo empleado """
        employee_dlg = EmployeeDlg(self)
        employee_dlg.exec()
    
class EmployeeDlg(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())