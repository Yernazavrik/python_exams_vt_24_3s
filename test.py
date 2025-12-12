from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()

        self.h1layout = QHBoxLayout()
        self.h2layout = QHBoxLayout()
        self.vlayout = QVBoxLayout()

        self.line_price = QLineEdit()
        self.line_price.setPlaceholderText("Цена")
        self.h1layout.addWidget(self.line_price)

        self.line_proc = QLineEdit()
        self.line_proc.setPlaceholderText("% скидки")
        self.h1layout.addWidget(self.line_proc)

        self.button = QPushButton("Посчитать")
        self.h2layout.addWidget(self.button)

        self.label = QLabel("")
        self.h2layout.addWidget(self.label)

        self.vlayout.addLayout(self.h1layout)
        self.vlayout.addLayout(self.h2layout)

        self.widget.setLayout(self.vlayout)
        self.setCentralWidget(self.widget)

        self.button.clicked.connect(self.calculate)

        self.show()

    def price_getter(self):
        return self.line_price.text()

    def proc_getter(self):
        return self.line_proc.text()

    def calculate(self):
        price = float(self.price_getter())
        proc = float(self.proc_getter())
        result = price - (price * proc / 100)
        self.label.setText(f"Итог: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
