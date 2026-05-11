from transport.transport import Transport


class Truck(Transport):
    """
    @brief Класс грузового автомобиля.
    """

    def __init__(self, name: str, max_speed: float, weight: float,
                 load_capacity: float):
        """
        @brief Конструктор грузовика.
        @param load_capacity Грузоподъемность (кг).
        """
        super().__init__(name, max_speed, weight)
        self.load_capacity = load_capacity

    def load_cargo(self):
        """
        @brief Загрузка груза.
        """
        return f"Грузовик {self.name} загружен."