# Task 5
#
# Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self):
        self._title = 'Рисовалка :)'
    def draw(self):
        print(self._title, 'Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        self._title = 'Ручка'
        print('Объект ' + self._title + ' создан')

    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def __init__(self):
        self._title = 'Карандаш'
        print('Объект ' + self._title + ' создан')

    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self):
        self._title = 'Маркер'
        print('Объект ' + self._title + ' создан')

    def draw(self):
        print('Отрисовка маркером')


my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()
