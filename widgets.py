import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget
)

# class MainWindowLabel(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QLabel("Hola")
#         font = widget.font()
#         font.setPointSize(30)
#         widget.setFont(font)
#         widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         self.setCentralWidget(widget)

# class MainWindowImage(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QLabel("Hola")

#         widget.setPixmap(QPixmap('perrito.webp'))
#         widget.setScaledContents(True)

#         self.setCentralWidget(widget)

# class MainWindowCheckbox(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QCheckBox('Label')
#         widget.setCheckState(Qt.CheckState.Checked)
#         widget.stateChanged.connect(self.show_state)
#         # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
#         # Or: widget.setTristate(True)

#         self.setCentralWidget(widget)
    
#     def show_state(self, state):
#         print(state == Qt.CheckState.Checked.value)
#         print(state)

# class MainWindowCombobox(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QComboBox()
#         widget.addItems(["Uno", "Dos", "Tres"])

#         # Hace el combo editable
#         widget.setEditable(True)
#         widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

#         # Manda el indice del item seleccinado
#         widget.currentIndexChanged.connect(self.index_changed)

#         # Manda el texto del item seleccionado
#         widget.currentTextChanged.connect(self.text_changed)

#         self.setCentralWidget(widget)
    
#     def index_changed(self, index):
#         print(index)
    
#     def text_changed(self, text):
#         print(text)

# class MainWindowList(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QListWidget()
#         widget.addItems(["Uno", "Dos", "Tres"])

#         widget.currentItemChanged.connect(self.index_changed)
#         widget.currentTextChanged.connect(self.text_changed)

#         self.setCentralWidget(widget)

#     def index_changed(self, index):
#         print(index.text())
    
#     def text_changed(self, text):
#         print(text)

# class MainWindowLineEdit(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText("Ingresá un texto")

#         # widget.setReadOnly(True) --> Para sólo lectura
        
#         widget.setInputMask('0000 000000;_')

#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)

#         self.setCentralWidget(widget)

#     def return_pressed(self):
#         print("Return pressed")
#         self.centralWidget().setText("Boom!")
    
#     def selection_changed(self):
#         print("Selection changed")
#         print(self.centralWidget().selectedText())

#     def text_changed(self, text):
#         print("Text changed...")
#         print(text)

#     def text_edited(self, text):
#         print("Text edited...")
#         print(text)

# class MainWindowSpinAndDoubleSpinBox(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         # QSpinBox es para enteros y QDoubleSpinBox es para flotante
#         widget = QSpinBox()
        
#         widget.setMinimum(-9)
#         widget.setMaximum(3)
#         # O widget.setRange(-9, 3)

#         widget.lineEdit().setReadOnly(True) # --> Para sólo lectura

#         widget.setPrefix("$")
#         widget.setSuffix("c")
#         widget.setSingleStep(3)

#         widget.valueChanged.connect(self.value_changed)
#         widget.textChanged.connect(self.text_changed)

#         self.setCentralWidget(widget)


#     def value_changed(self, i):
#         print("Value changed...")
#         print(i)

#     def text_changed(self, text):
#         print("Text changed...")
#         print(text)

# class MainWindowSlider(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets")

#         widget = QSlider(Qt.Orientation.Horizontal)
#         # widget = QSlider(Qt.Orientation.Vertical) ---> Slider en posicion vertical
        
#         widget.setMinimum(-9)
#         widget.setMaximum(3)

#         widget.setSingleStep(3)

#         widget.valueChanged.connect(self.value_changed)
#         widget.sliderMoved.connect(self.slider_position)
#         widget.sliderPressed.connect(self.slider_pressed)
#         widget.sliderReleased.connect(self.slider_released)

#         self.setCentralWidget(widget)


#     def value_changed(self, i):
#         print("Value changed...")
#         print(i)

#     def slider_position(self, position):
#         print("Position changed...")
#         print(position)
    
#     def slider_pressed(self):
#         print("Slider Pressed!!")
    
#     def slider_released(self):
#         print("Slider Released!!")

class MainWindowDial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets")

        widget = QDial()
        
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.dial_position)
        widget.sliderPressed.connect(self.dial_pressed)
        widget.sliderReleased.connect(self.dial_released)

        self.setCentralWidget(widget)


    def value_changed(self, i):
        print("Value changed...")
        print(i)

    def dial_position(self, position):
        print("Position changed...")
        print(position)
    
    def dial_pressed(self):
        print("Dial Pressed!!")
    
    def dial_released(self):
        print("Dial Released!!")

app = QApplication(sys.argv)
window = MainWindowDial()
window.show()
app.exec()