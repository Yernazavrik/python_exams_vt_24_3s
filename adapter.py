import PyQt5
import sys
from PyQt5 import QtWidgets
class TextGenerator:
    """Сторонний класс, который нельзя менять"""
    def __init__(self):
        self.counter = 0
        
    def generate(self):
        self.counter += 1
        return f"Сгенерированный текст #{self.counter}"
class Adapter(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.text_generator = TextGenerator()
        self.setText("111")
    def updateTextGenerator(self):
        generated_text = self.text_generator.generate()
        self.setText(generated_text)
        return generated_text
        
        
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.v_layout= QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.v_layout)
        self.send_button = QtWidgets.QPushButton("press")
        self.v_layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.onClicked)
        self.label = Adapter()
        self.v_layout.addWidget(self.label)
        self.setCentralWidget(self.widget) 
    def onClicked(self):
        self.label.updateTextGenerator()
        self.label.text()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()