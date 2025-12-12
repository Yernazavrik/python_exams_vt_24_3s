import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit
)
from PyQt5.QtCore import Qt

class DisplayableButton:
    def get_widget(self) -> QPushButton:
        raise NotImplementedError

    def connect_click(self, func):
        raise NotImplementedError

class SimpleButton(DisplayableButton):
    def __init__(self, text: str):
        self.btn = QPushButton(text)

    def connect_click(self, func):
        self.btn.clicked.connect(func)

    def get_widget(self) -> QPushButton:
        return self.btn

class LoggingDecorator(DisplayableButton):
    def __init__(self, component: DisplayableButton):
        self.component = component

    def connect_click(self, func):
        def wrapper():
            print(f"[LOG] Кнопка нажата: '{self.component.get_widget().text()}'")
            func()
        self.component.connect_click(wrapper)

    def get_widget(self):
        return self.component.get_widget()

class CounterDecorator(DisplayableButton):
    def __init__(self, component: DisplayableButton, label: QLabel):
        self.component = component
        self.count = 0
        self.label = label

    def connect_click(self, func):
        def wrapper():
            self.count += 1
            self.label.setText(f"Всего нажатий: {self.count}")
            func()
        self.component.connect_click(wrapper)

    def get_widget(self):
        return self.component.get_widget()

class StyleDecorator(DisplayableButton):
    def __init__(self, component: DisplayableButton):
        self.component = component
        btn = component.get_widget()
        btn.setStyleSheet("""
            QPushButton {
                background-color: #white;
                color: white;
            }
        """)

    def connect_click(self, func):
        self.component.connect_click(func)

    def get_widget(self):
        return self.component.get_widget()


class ButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.button_obj = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        top = QHBoxLayout()
        top.addWidget(QLabel("Текст кнопки:"))
        self.text_input = QLineEdit()
        create_btn = QPushButton("Создать")
        create_btn.clicked.connect(self.create_button)
        top.addWidget(self.text_input)
        top.addWidget(create_btn)
        layout.addLayout(top)

        self.button_container = QVBoxLayout()
        self.button_container.setAlignment(Qt.AlignCenter)
        layout.addLayout(self.button_container, 1)

        self.counter_label = QLabel("Всего нажатий: 0")
        self.counter_label.setAlignment(Qt.AlignCenter)
        self.counter_label.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: orange;
            }
        """)
        layout.addWidget(self.counter_label)

        self.setLayout(layout)
        self.resize(500, 300)

        self.create_button()

    def create_button(self):
        if self.button_obj:
            self.button_obj.get_widget().deleteLater()

        text = self.text_input.text().strip() or "Кнопка"

        self.counter_label.setText("Всего нажатий: 0")

        btn = SimpleButton(text)
        btn = StyleDecorator(btn)
        btn = LoggingDecorator(btn)
        btn = CounterDecorator(btn, self.counter_label)

        btn.connect_click(lambda: None)

        self.button_obj = btn
        self.button_container.addWidget(btn.get_widget())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonDemo()
    window.show()
    sys.exit(app.exec_())