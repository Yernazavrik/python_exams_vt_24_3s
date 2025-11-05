from PyQt5 import QtWidgets
import sys
from i_repo import IRepository
from data_repo import SqlServerRepository


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, repository: IRepository):
        super().__init__()
        self.repository = repository  # внедряем зависимость

        central_widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(central_widget)

        self.button_connect = QtWidgets.QPushButton("Проверить соединение")
        self.button_connect.clicked.connect(self.on_check_connection)
        self.layout.addWidget(self.button_connect)

        self.button_load = QtWidgets.QPushButton("Загрузить данные")
        self.button_load.clicked.connect(self.on_load_data)
        self.layout.addWidget(self.button_load)

        self.list_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_widget)

        self.setCentralWidget(central_widget)

    def on_check_connection(self):
        ok = self.repository.test_connection()
        msg = "✅ Соединение успешно!" if ok else "❌ Ошибка соединения."
        QtWidgets.QMessageBox.information(self, "Проверка соединения", msg)

    def on_load_data(self):
        try:
            data = self.repository.get_data()
            self.list_widget.clear()
            self.list_widget.addItems(data)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))


# === Точка входа ===
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # 🔧 Строка подключения
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=YE\\YERNAZAVR;"
        "Database=cash_transition;"
        "Trusted_Connection=yes;"
    )

    # Создаём конкретную реализацию репозитория
    repo = SqlServerRepository(connection_string)

    # Внедряем зависимость в окно
    window = MainWindow(repo)
    window.setWindowTitle("PyQt5 + SQL Server + Dependency Injection")
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())
