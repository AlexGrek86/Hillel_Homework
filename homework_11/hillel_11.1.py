class Vehicle:
    # TODO: make all attributes protected if you want to share them for child class
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed
        print('Было создано транспортное средство') # constractor just asign basic value for field and no more

    # TODO: I suggest rename x on something another and add annotations
    #  for example 'difference' tell me how much will be accelerated
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
    # TODO: add annotations
    def __init__(self, speed, max_speed):
        # TODO: Use super instead of class name since you have only 1 parent
        Vehicle.__init__(self, speed, max_speed)
        # TODO: if this fields would not be shared to child classes so made them private
        # Дополнительные поля
        self._front_tire_width = 95
        self._rear_tire_width = 95

    # TODO: add annotations
    def set_tires_width(self, front, rear):
        self._front_tire_width = front
        self._rear_tire_width = rear
        print('На мотоцикл были установлены новые шины')

    def print_tire_info(self):
        print(f'Ширина передней шины {self._front_tire_width} мм')
        print(f'Ширина задней шины {self._rear_tire_width} мм')


class Automobile(Vehicle):
    # TODO: Use super instead of class name since you have only 1 parent
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля
        # TODO: if this fields would not be shared to child classes so made them private
        self._gear = 0
        self._color = 'синий'

    # TODO: add annotations
    def set_gear(self, gear):
        self._gear = gear

    # TODO: use super instead of Vihicle
    def print_status(self):
        Vehicle.print_status(self)
        print(f'Автомобиль переключен на скорость № {self._gear}')
        print(f'Автомобиль покрашен в {self._color} цвет')

    # TODO: add annotations
    # TODO: maybe will be better to use properte instead of method ?
    def set_color(self, color):
        self._color = color

    # TODO: add annotations
    # TODO: maybe will be better to use properte instead of method ?
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
    # TODO: place all classes in different modules
