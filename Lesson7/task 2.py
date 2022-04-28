# Task 2
#
# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self._name = name
        super().__init__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def get_quantity(self):
        pass

    def __str__(self):
        return f'{self.name}  {self.get_quantity():.2f} м.'


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    @property
    def size(self):
        return self._size

    def get_quantity(self):
        return self._size/6.5 + 0.5


class Jacket(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    @property
    def height(self):
        return self._height

    def get_quantity(self):
        return 2*self._height/6.5 + 0.3


jacket = Jacket("mega", 185)
print(jacket)

coat = Coat("cool", 45)
print(coat)

