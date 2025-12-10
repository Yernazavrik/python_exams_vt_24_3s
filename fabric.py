#variant 1
from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5
import sys
class BaseButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__(text)
    def create_button(self, button_type:str) -> QtWidgets.QPushButton:
        pass
class DangerButton(BaseButton):
    def __init__(self):
        super().__init__("danger button")
        self.setStyleSheet("background: #d9534f; color: white;")
    def create_button(self, button_type:str) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton()
        button.setStyleSheet("background: #d9534f; color: white;")
        return button
        
class SuccessButton(BaseButton):
    def __init__(self):
        super().__init__("success")
        self.setStyleSheet("background: #5cb85c; color: white;")
    def create_button(self, button_type:str) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton()
        button.setStyleSheet("background: #5cb85c; color: white;")
        return button
class DefaultButton(BaseButton):
    def __init__(self):
        super().__init__("default Button")
    def create_button(self, button_type:str) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton()
        return button
        
class Selector():
    def choose_button(button_type:str):
        if button_type == "danger":
            return DangerButton()
        if button_type == "success":
            return SuccessButton()
        if button_type == "default":
            return DefaultButton()

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
        self.layout.addWidget(self.button)
        self.setCentralWidget(self.widget)
    def onClick(self):
            self.factory = Selector.choose_button(self.line_edit.text())
            self.buttonType = self.factory.create_button("")
            self.layout.addWidget(self.buttonType)
            self.buttonType.setText(self.line_edit.text())
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
