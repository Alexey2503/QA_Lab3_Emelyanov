from transport.transport import Transport


class Car(Transport):
    """
    @brief Класс легкового автомобиля.
    """

    def __init__(self, name: str, max_speed: float, weight: float,
                 fuel_consumption: float, fuel_tank_capacity: float):
        """
        @brief Конструктор автомобиля.
        @param fuel_consumption Расход топлива (л/100км).
        @param fuel_tank_capacity Объем топливного бака (л).
        """
        super().__init__(name, max_speed, weight)
        self.fuel_consumption = fuel_consumption
        self.fuel_tank_capacity = fuel_tank_capacity

    def calculate_range(self) -> float:
        """
        @brief Расчет запаса хода автомобиля.

        Формула:
        @f$ Range = \\frac{FuelTank}{FuelConsumption} \\times 100 @f$
        """
        return (self.fuel_tank_capacity / self.fuel_consumption) * 100

    def open_trunk(self):
        """
        @brief Открыть багажник.
        """
        return "Багажник открыт."