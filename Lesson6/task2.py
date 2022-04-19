# Task 2
#
# Реализовать класс Road (дорога).
#
#     определить атрибуты: length (длина), width (ширина);
#     значения атрибутов должны передаваться при создании экземпляра класса;
#     атрибуты сделать защищёнными;
#     определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#     использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
#     толщиной в 1 см*число см толщины полотна;
#     проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road():
    __UNIT_WEIGHT = 25
    _length = 0
    _width = 0

    def __init__(self, length, width):
        if not isinstance(length, (float, int)) or length == 0:
            raise ValueError('Неверно задано значение длины дорожного полотна')
        if not isinstance(width, (float, int)) or width == 0:
            raise ValueError('Неверно задано значение ширины дорожного полотна')
        self._length = length
        self._width = width

    def asphalt_quantity(self, thickness):
        if not isinstance(thickness, int):
            print('Неверно задано значение толщины дорожного полотна')
        else:
            m = self._width * self._length * self.__UNIT_WEIGHT * thickness / 1000
            print(f'Необходимая масса асфальта "песч. плот. тип Г м II" составит {m:.2f} т.')


my_road = Road(50000, 25)
my_road.asphalt_quantity(5)
