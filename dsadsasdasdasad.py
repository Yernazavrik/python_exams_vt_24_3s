from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
import sys

class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация (минимал)")

        layout = QVBoxLayout(self)


        self.login_creator = HighlightCreator()
        self.pass_creator = PasswordCreator()


        self.login = self.login_creator.create_line_edit()
        self.login.setPlaceholderText("Логин")

        self.password = self.pass_creator.create_line_edit()
        self.password.setPlaceholderText("Пароль")

        layout.addWidget(self.login)
        layout.addWidget(self.password)


        btn_row = QHBoxLayout()
        self.btn_login = QPushButton("Войти")
        self.btn_reg = QPushButton("Регистрация")
        btn_row.addWidget(self.btn_login)
        btn_row.addWidget(self.btn_reg)

        layout.addLayout(btn_row)


        self.label = QLabel("Введите логин и пароль.")
        layout.addWidget(self.label)



app = QApplication(sys.argv)
win = AuthWindow()
win.show()
sys.exit(app.exec_())
