class Vehicle(object):
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed
        print('Было создано транспортное средство')

    def accelerate(self, x):
        self.speed = self.speed + x
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self, x):
        self.speed = self.speed - x
        if self.speed < 0:
            self.speed = 0

    def print_status(self):
        print(f'Скорость транспортного средства равна {self.speed} км/ч')


class Motorcycle(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля
        self._front_tire_width = 95
        self._rear_tire_width = 95

    def set_tires_width(self, front, rear):
        self._front_tire_width = front
        self._rear_tire_width = rear
        print('На мотоцикл были установлены новые шины')

    def print_tire_info(self):
        print(f'Ширина передней шины {self._front_tire_width} мм')
        print(f'Ширина задней шины {self._rear_tire_width} мм')


class Automobile(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля
        self._gear = 0
        self._color = 'синий'

    def set_gear(self, gear):
        self._gear = gear

    def print_status(self):
        Vehicle.print_status(self)
        print(f'Автомобиль переключен на скорость № {self._gear}')
        print(f'Автомобиль покрашен в {self._color} цвет')

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


if __name__ == "__main__":
    m = Motorcycle(40, 120)
    m.print_status()
    m.set_tires_width(90, 100)
    m.print_tire_info()

    a = Automobile(0, 150)
    a.accelerate(40)
    a.set_gear(2)
    a.print_status()
    a.set_color('красный')
    color = a.get_color()
