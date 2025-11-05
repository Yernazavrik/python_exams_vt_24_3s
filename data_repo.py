import pyodbc
from i_repo import IRepository

class SqlServerRepository(IRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print("✅ Подключение к SQL Server установлено.")
        except Exception as e:
            print("❌ Ошибка подключения:", e)
            self.conn = None

    def test_connection(self) -> bool:
        if not self.conn:
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()[0]
            print("Версия SQL Server:", version)
            return True
        except Exception as e:
            print("Ошибка проверки соединения:", e)
            return False

    def get_data(self):
        if not self.conn:
            raise ConnectionError("Нет соединения с базой данных.")
        cursor = self.conn.cursor()
        cursor.execute("SELECT TOP 10 name FROM sys.databases")
        return [row.name for row in cursor.fetchall()]
