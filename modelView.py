import sys
import json
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic import loadUiType
from PyQt6.QtCore import Qt, QAbstractListModel

qt_creator_file = "./UIs/todoList.ui"
Ui_MainWindow, QtBasseClass = loadUiType(qt_creator_file)

tick = QImage('./icons/bug.png')

class TodoModel(QAbstractListModel):
    def __init__(self, *args, todos = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick
    
    def rowCount(self, index):
        return len(self.todos)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)

        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
    
    def add(self):
        text = self.todoEdit.text()
        if text:
            # Agrega a la lista el texto mediante el modelo
            self.model.todos.append((False, text))

            # Refresca la lista
            self.model.layoutChanged.emit()

            # Vacía el input
            self.todoEdit.setText("")
            
            self.save()
    
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            self.save()
    
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()
            self.save()
    
    def load(self):
        try:
            with open('todoList.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass
    
    def save(self):
        with open('todoList.json', 'w') as f:
            data = json.dump(self.model.todos, f)
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()