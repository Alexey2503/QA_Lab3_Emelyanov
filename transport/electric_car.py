from transport.car import Car


class ElectricCar(Car):
    """
    @brief Класс электромобиля.
    """

    def __init__(self, name: str, max_speed: float, weight: float,
                 battery_capacity: float, energy_consumption: float):
        """
        @brief Конструктор электромобиля.
        @param battery_capacity Емкость батареи (кВт⋅ч).
        @param energy_consumption Расход энергии (кВт⋅ч/100км).
        """
        super().__init__(name, max_speed, weight, 0, 0)
        self.battery_capacity = battery_capacity
        self.energy_consumption = energy_consumption

    def calculate_range(self) -> float:
        """
        @brief Расчет запаса хода электромобиля.

        Формула:
        @f$ Range = \\frac{BatteryCapacity}{EnergyConsumption} \\times 100 @f$
        """
        return (self.battery_capacity / self.energy_consumption) * 100

    def charge(self):
        """
        @brief Зарядка электромобиля.
        """
        return f"{self.name} заряжается."