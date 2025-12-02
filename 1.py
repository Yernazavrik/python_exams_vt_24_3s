import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QTabWidget
from PyQt5 import QtCore, QtWidgets
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        btn = QPushButton('Войти', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 120)

        btn = QPushButton('Регистрация', self)
        btn.resize(btn.sizeHint())
        btn.move(150, 120)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(5, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.move(100,80)

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(5, 50, 100, 20))
        self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit")
        self.lineEdit2.move(100,50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()