from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def test_connection(self) -> bool:
        """Проверить соединение с базой"""
        pass

    @abstractmethod
    def get_data(self):
        """Получить пример данных из базы"""
        pass
