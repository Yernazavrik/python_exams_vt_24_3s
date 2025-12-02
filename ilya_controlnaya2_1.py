#Вариант 1
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QFrame
from PyQt5.QtCore import Qt

class AddProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Добавление товара')
        self.setGeometry(100, 100, 450, 150) # Увеличиваем ширину для лучшего отображения двух колонок

        # --- Левая часть: Поля ввода ---
        self.name_input = QLineEdit(self)
        self.price_input = QLineEdit(self)

        form_layout = QFormLayout()
        form_layout.addRow('Название:', self.name_input)
        form_layout.addRow('Цена:', self.price_input)
        
        # Создаем контейнер для левой части
        left_container = QFrame()
        left_container.setLayout(form_layout)


        # --- Правая часть: Кнопка и метка ---
        self.save_button = QPushButton('Сохранить', self)
        self.status_label = QLabel('Заполните все поля', self)
        
        # Настройка метки статуса (красный цвет, выравнивание)
        self.status_label.setStyleSheet("color: red; padding: 10px;")
        self.status_label.setAlignment(Qt.AlignCenter)
        # self.status_label.setWordWrap(True) # Если текст может быть длинным
        self.status_label.hide() 

        # Создаем вертикальный макет для правой части
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.save_button)
        right_layout.addWidget(self.status_label)
        right_layout.setAlignment(Qt.AlignTop) # Прижимаем содержимое правой части к верху
        
        # Создаем контейнер для правой части
        right_container = QFrame()
        right_container.setLayout(right_layout)


        # --- Основной макет: Горизонтальный ---
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_container, 1) # 1 - растягиваемый фактор для левой части
        main_layout.addWidget(right_container, 1) # 1 - растягиваемый фактор для правой части

        self.setLayout(main_layout)

        # Подключение обработчика события к кнопке
        self.save_button.clicked.connect(self.on_save_button_clicked)

    def on_save_button_clicked(self):
        name = self.name_input.text()
        price = self.price_input.text()

        if not name or not price:
            self.status_label.setText('Заполните все поля')
            self.status_label.setStyleSheet("color: red; padding: 10px;")
            self.status_label.show()
        else:
            self.status_label.setText(f'Товар сохранен:\n"{name}", {price} р.')
            self.status_label.setStyleSheet("color: green; padding: 10px;")
            self.status_label.show()
            
            # Очистка полей
            self.name_input.clear()
            self.price_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddProductForm()
    ex.show()
    sys.exit(app.exec_())