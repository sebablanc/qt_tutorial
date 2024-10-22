import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QMessageBox
from dialogs_customDialog import CustomDialog

# Ejemplo Dialogs
# class MainWindow(QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.setWindowTitle("Dialogs App")

#         button = QPushButton("Click para abrir Dialog")
#         button.clicked.connect(self.button_clicked)
        
#         self.setCentralWidget(button)
    
#     def button_clicked(self):
#         dialog = CustomDialog(self)
        
#         if dialog.exec():
#             print("Exito!")
#         else:
#             print("Cancelado!")

# Ejemplo MessageBox
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Dialogs App")

        button = QPushButton("Click para abrir Dialog")
        button.clicked.connect(self.button_clicked_botones_personalizados)
        
        self.setCentralWidget(button)
    
    def button_clicked(self):
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Tengo una pregunta")
        messageBox.setText("Simple Dialog")
        
        messageBox.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        messageBox.setIcon(QMessageBox.Icon.Question)

        button = messageBox.exec()

        if button == QMessageBox.StandardButton.Yes:
            print("Sí!")
        else:
            print("No!")

    def button_clicked_mas_facil(self):
        button = QMessageBox.question(
            self,
            "Question Dialog",
            "El mensaje"
        )

        if button == QMessageBox.StandardButton.Yes:
            print("Sí!")
        else:
            print("No!")

    def button_clicked_botones_personalizados(self):
        button = QMessageBox.critical(
            self,
            "Cuidado!",
            "Algo fue realmente mal",
            buttons= QMessageBox.StandardButton.Discard
            | QMessageBox.StandardButton.NoToAll
            | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard
        )

        if button == QMessageBox.StandardButton.Discard:
            print("Descartar!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No a todo!")
        else:
            print("Ignorar!")
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()