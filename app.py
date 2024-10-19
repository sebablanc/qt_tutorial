import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

window_title_error = 'Something went wrong'
window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    window_title_error
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setea el título de la ventana
        self.setWindowTitle("Mi aplicación")

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
    
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))
        
    # def contextMenuEvent(self, event):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(event.globalPos())
        
    #     self.label = QLabel("Cliqueá en la ventana")
        
    #     self.setCentralWidget(self.label)

    #     self.setMouseTracking(True)

    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEvent")
    
    # def mousePressEvent(self, e):
    #     self.label.setText("mousePressEvent")

    # def mouseReleaseEvent(self, e):
    #     self.label.setText("mouseReleaseEvent")

    # def mouseDoubleClickEvent(self, e):
    #     self.label.setText("mouseDoubleClickEvent")
        # self.label = QLabel()

        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)

        # container = QWidget()
        # container.setLayout(layout)

        # self.setCentralWidget(container)
#         # Crea un boton
#         self.button = QPushButton("Cliqueame!")
#         self.windowTitleChanged.connect(self.the_window_title_changed)
#         self.button.clicked.connect(self.the_button_was_clicked)
        
#         # Cambia el tamaño de la ventana
#         self.setFixedSize(QSize(400, 300))

#         # Posiciona el boton cmo objeto principal
#         self.setCentralWidget(self.button)

#     def the_window_title_changed(self, window_title):
#         print('Window title changed: %s' % window_title)
#         if window_title == window_title_error:
#             self.button.setDisabled(True)
    
#     def the_button_was_clicked(self):
#         print("Clicked")
#         new_window_title = choice(window_titles)
#         print("Setting title:  %s" % new_window_title)
#         self.setWindowTitle(new_window_title)

#     def the_button_was_toggled(self, checked):
#         self.isButtonChecked = checked
#         print('Toggled - Checked?:', checked)
#  
#      def the_button_was_released(self):
#         self.isButtonChecked = self.button.isChecked()
#         print('Released - Checked?:', self.isButtonChecked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()