from abc import ABC, abstractmethod
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QComboBox, QLabel, QLineEdit
)

class LineEditCreator(ABC):
    @abstractmethod
    def create_line_edit(self) -> QLineEdit:
        pass



class HighlightLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Подсветка (условно)")


class PasswordLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setEchoMode(QLineEdit.Password)
        self.setPlaceholderText("Пароль")


class FramedLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Рамка + placeholder")

class HighlightCreator(LineEditCreator):
    def create_line_edit(self):
        return HighlightLineEdit()


class PasswordCreator(LineEditCreator):
    def create_line_edit(self):
        return PasswordLineEdit()


class FramedCreator(LineEditCreator):
    def create_line_edit(self):
        return FramedLineEdit()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Factory QLineEdit (минимал)")

        self.creators = {
            "Highlight": HighlightCreator(),
            "Password": PasswordCreator(),
            "Framed": FramedCreator()
        }

        layout = QVBoxLayout(self)

        self.combo = QComboBox()
        self.combo.addItems(self.creators.keys())
        self.combo.currentTextChanged.connect(self.recreate_field)
        layout.addWidget(self.combo)

        self.field = None
        self.field_container = QVBoxLayout()
        layout.addLayout(self.field_container)

        self.label = QLabel("Поле создаётся фабрикой.")
        layout.addWidget(self.label)

        self.recreate_field("Highlight")

    def recreate_field(self, name):
        if self.field:
            self.field.deleteLater()

        creator = self.creators[name]
        self.field = creator.create_line_edit()
        self.field_container.addWidget(self.field)

        self.label.setText(f"Создано поле: {name}")


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
