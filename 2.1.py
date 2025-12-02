#5
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSizeF(30)
        self.label.setFont(font)

        self.pb_add = QPushButton('Старт')
        self.pb_add.clicked.connect(self._on_add)
        self.number = 0
        self.pb_add1 = QPushButton('Стоп')
        self.pb_add1.clicked.connect(self._on_add)
        self.number = 0

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pb_add)
        layout.addWidget(self.pb_add1)

        self.setLayout(layout)
        self._update_states()
    def _update_states(self):
        self.label.setNum(self.number)
    def _on_add(self):
        self.number += 1
        self._update_states()
if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()