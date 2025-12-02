from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5
import sys

class BaseButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__(text)
        
class DangerButton(BaseButton):
    def __init__(self):
        super().__init__("danger button")
        self.setStyleSheet("background: #d9534f; color: white;")
        
class SuccessButton(BaseButton):
    def __init__(self):
        super().__init__("success")
        self.setStyleSheet("background: #5cb85c; color: white;")
        
class DefaultButton(BaseButton):
    def __init__(self):
        super().__init__("default Button")
        
class Selector():
    def choose_button(button_type:str):
        if button_type == "danger":
            return DangerButton()
        if button_type == "success":
            return SuccessButton()
        if button_type == "default":
            return DefaultButton

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.layout= QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.line_edit = QtWidgets.QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.button = QtWidgets.QPushButton("Нажми для выбора кнопки")
        self.layout.addWidget(self.line_edit)
        self.button.clicked.connect(self.onClick)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
