from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.layout= QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.textbox_name = QtWidgets.QLineEdit("Введите название")
        self.textbox_cost = QtWidgets.QLineEdit("Введите цену")
        self.button = QtWidgets.QPushButton("push me")
        self.label = QtWidgets.QLabel("Заполните все поля")
        self.layout.addWidget(self.textbox_name)
        self.layout.addWidget(self.textbox_cost)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.setCentralWidget(self.textbox_name)
        self.setCentralWidget(self.textbox_cost)
        self.setCentralWidget(self.button)
        self.setCentralWidget(self.label)
        self.button.clicked.connect(self.onClick)
    def onClick(self):
        print("button has been clicked")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())