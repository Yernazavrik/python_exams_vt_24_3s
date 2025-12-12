import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Панель управления")
        self.is_running = False
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        left_column = QVBoxLayout()
        left_column.addStretch()

        self.start_btn = QPushButton("Старт")
        self.stop_btn = QPushButton("Стоп")
        self.stop_btn.setEnabled(False)

        self.start_btn.setFixedHeight(60)
        self.stop_btn.setFixedHeight(60)

        left_column.addWidget(self.start_btn)
        left_column.addSpacing(20)        
        left_column.addWidget(self.stop_btn)
        left_column.addStretch()

        main_layout.addLayout(left_column)

        right_column = QVBoxLayout()

        self.status_label = QLabel("Статус: ожидание")
        self.status_label.setAlignment(Qt.AlignCenter)

        right_column.addWidget(self.status_label)

        param_layout = QHBoxLayout()
        param_layout.addWidget(QLabel("Параметр:"))
        self.param_input = QLineEdit()
        self.param_input.setPlaceholderText("Введите число...")
        param_layout.addWidget(self.param_input)

        right_column.addLayout(param_layout)
        right_column.addStretch()

        main_layout.addLayout(right_column, stretch=1) 

        self.setLayout(main_layout)
        self.resize(600, 350)

 
        self.start_btn.clicked.connect(self.start_process)
        self.stop_btn.clicked.connect(self.stop_process)

    def start_process(self):
        param = self.param_input.text().strip()
        if not param.isdigit():
            QMessageBox.critical(self, "Ошибка", "Параметр должен быть целым числом!")
            return

        self.is_running = True
        self.status_label.setText("Статус: работает")

        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

    def stop_process(self):
        self.is_running = False
        self.status_label.setText("Статус: ожидание")

        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec_())