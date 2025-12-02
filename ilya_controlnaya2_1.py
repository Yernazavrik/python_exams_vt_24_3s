#Вариант 1
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt


"""Базовый класс кнопки с текстом"""
class BaseButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setMinimumHeight(30)

class DangerButton(BaseButton):
    """Красная опасная кнопка"""
    def __init__(self):
        super().__init__("Опасная кнопка (Danger)")
        self.setStyleSheet("background: #d9534f; color: white; border: none; padding: 5px;")

class SuccessButton(BaseButton):
    """Зеленая кнопка успеха"""
    def __init__(self):
        super().__init__("Кнопка успеха (Success)")
        self.setStyleSheet("background: #5cb85c; color: white; border: none; padding: 5px;")

class DefaultButton(BaseButton):
    """Обычная кнопка"""
    def __init__(self):
        super().__init__("Обычная кнопка (Default)")


class ButtonFactory:
    @staticmethod
    def create_button(button_type: str) -> QPushButton:

        button_type = button_type.lower().strip()
        if button_type == "danger":
            return DangerButton()
        elif button_type == "success":
            return SuccessButton()
        elif button_type == "default":
            return DefaultButton()
        else:

            return DefaultButton() 




class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.created_buttons_count = 0

    def initUI(self):
        self.setWindowTitle('Фабрика кнопок PyQt5')
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        controls_layout = QHBoxLayout()
        
        controls_layout.addWidget(QLabel("Тип (danger, success, default):"))
        self.type_input = QLineEdit(self)
        self.type_input.setPlaceholderText("Введите тип кнопки")
        controls_layout.addWidget(self.type_input)
        
        self.create_btn = QPushButton('Создать кнопку', self)
        self.create_btn.clicked.connect(self.create_new_button)
        controls_layout.addWidget(self.create_btn)

        main_layout.addLayout(controls_layout)


        main_layout.addStretch(1) 

        self.setLayout(main_layout)

    def create_new_button(self):
        button_type = self.type_input.text()
        
    
        new_button = ButtonFactory.create_button(button_type)
        
 
        main_layout = self.layout()
        main_layout.insertWidget(main_layout.count() - 1, new_button)
        
 
        new_button.clicked.connect(lambda ch, btn_type=new_button.text(): 
                                   QMessageBox.information(self, "Клик", f"Вы нажали на кнопку типа: {btn_type}"))

        self.type_input.clear()
        self.status_label = QLabel(f"Создано кнопок: {self.created_buttons_count}")
        self.created_buttons_count += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppWindow()
    ex.show()
    sys.exit(app.exec_())