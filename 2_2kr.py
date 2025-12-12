import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Основной вертикальный layout
        vlayout = QVBoxLayout()
        
        # Поле для логина
        login_label = QLabel("Логин:")
        self.login_edit = QLineEdit()
        
        # Поле для пароля
        password_label = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        # Горизонтальный layout для кнопок
        hlayout = QHBoxLayout()
        login_btn = QPushButton("Войти")
        register_btn = QPushButton("Регистрация")
        hlayout.addWidget(login_btn)
        hlayout.addWidget(register_btn)
        
        # Поясняющий Label
        info_label = QLabel("Введите ваши учетные данные")
        
        # Добавляем все в вертикальный layout
        vlayout.addWidget(login_label)
        vlayout.addWidget(self.login_edit)
        vlayout.addWidget(password_label)
        vlayout.addWidget(self.password_edit)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(info_label)
        
        self.setLayout(vlayout)
        self.setWindowTitle("Авторизация")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())