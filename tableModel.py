from datetime import datetime
import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtGui import QColor, QIcon

COLORS = [
    "#053061",
    "#2166ac",
    "#4393c3",
    "#92c5de",
    "#d1e5f0",
    "#f7f7f7",
    "#fddbc7",
    "#f4a582",
    "#d6604d",
    "#b2182b",
    "#67001f",
]


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        value = self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            if isinstance(value, datetime):
                value = value.strftime("%Y-%m-%d")
            elif isinstance(value, float):
                value = "%.2f" % value
            elif isinstance(value, str):
                value = '"%s"' % value

            return value

        # Inserta color al background de la celda
        #elif role == Qt.ItemDataRole.BackgroundRole:
        #    if isinstance(value, int) or isinstance(value, float):
        #        value = int(value)
        #        value = max(-5, value)
        #        value = min(5, value)
        #        value = value + 5
        #        return QColor(COLORS[value])

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

        elif (
            role == Qt.ItemDataRole.ForegroundRole
            and (isinstance(value, int) or isinstance(value, float))
            and value < 0
        ):
            return QColor("red")
        
        elif role == Qt.ItemDataRole.DecorationRole:
            if isinstance(value, datetime):
                return QIcon("icons/bug.png")
            elif isinstance(value, bool):
                if value:
                    return QIcon("icons/tick.png")
                return QIcon("icons/cross.png")
            elif isinstance(value, int) or isinstance(value, float):
                value = int(value)
                value = max(-5, value)
                value = min(5, value)
                value = value + 5

                return QColor(COLORS[value])

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019, 5, 4), 8, 9],
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
