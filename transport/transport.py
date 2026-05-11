class Transport:
    """
    @brief Базовый класс транспорта.

    Представляет общее транспортное средство.
    """

    def __init__(self, name: str, max_speed: float, weight: float):
        """
        @brief Конструктор транспорта.
        @param name Название транспорта.
        @param max_speed Максимальная скорость (км/ч).
        @param weight Вес (кг).
        """
        self.name = name
        self.max_speed = max_speed
        self.weight = weight

    def start(self):
        """
        @brief Запуск транспорта.
        """
        return f"{self.name} запущен."

    def stop(self):
        """
        @brief Остановка транспорта.
        """
        return f"{self.name} остановлен."