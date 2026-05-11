from transport.car import Car
from transport.electric_car import ElectricCar

if __name__ == "__main__":
    car = Car("Toyota", 180, 1500, 8, 50)
    print(car.start())
    print("Запас хода:", car.calculate_range())

    ecar = ElectricCar("Tesla", 200, 1800, 75, 15)
    print(ecar.start())
    print("Запас хода:", ecar.calculate_range())