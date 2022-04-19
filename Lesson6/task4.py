# Task 4
#
# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
from enum import Enum


class Turn(Enum):
    Left = 100
    Right = 200
    Back = 1000


class Car:
    def __init__(self, name, color, speed, is_police: bool):
        self._name = name
        self._color = color
        self._speed = speed
        if speed > 0:
            self._running = True
        self._is_police = is_police

    def go(self, add_speed):
        print("The car is moving.", end="")
        self._speed += add_speed
        print(" New speed is", self._speed, 'Mph')

    def stop(self):
        self._speed = 0
        print("The car has stopped")

    def turn(self, direction: Turn):
        if self._speed > 0:
            print("The car turn to the " + direction.name)
        else:
            print("Can't turn. Car is parked.")

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def show_speed(self):
        print('Current speed: ', self._speed)


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, False)

    def show_speed(self):
        print('Current speed: ', self._speed)
        if self._speed > 60:
            print('Attention! Speeding! Slow down!')


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, False)


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, False)

    def show_speed(self):
        print('Current speed: ', self._speed)
        if self._speed > 40:
            print('Attention! Speeding! Slow down!')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


car1 = TownCar('Ford Galaxy', 'Blue', 80)
print('\n', car1.get_name(), car1.get_color())
car1.go(20)
car1.show_speed()
car1.turn(Turn.Left)
car1.stop()
car1.turn(Turn.Back)

car2 = PoliceCar('Interceptor', 'Black', 0)
print('\n', car2.get_name(), car2.get_color())
car2.show_speed()
car2.go(120)
car2.turn(Turn.Right)
car2.go(20)
car2.turn(Turn.Left)
car2.show_speed()
car2.stop()

car3 = WorkCar('VW Caddy', 'White/Red', 0)
print('\n', car3.get_name(), car3.get_color())
car3.show_speed()
car3.go(40)
car3.turn(Turn.Right)
car3.show_speed()
car3.go(15)
car3.turn(Turn.Left)
car3.show_speed()
car3.stop()

car4 = SportCar('McLaren f1', 'Orange', 200)
print('\n', car4.get_name(), car4.get_color())
car4.show_speed()
car4.go(40)
car4.turn(Turn.Right)
car4.show_speed()
car4.go(15)
car4.turn(Turn.Left)
car4.show_speed()
car4.stop()
