# Task 1
#
# Создать класс TrafficLight (светофор).
#
#     определить у него один атрибут color (цвет) и метод running (запуск);
#     атрибут реализовать как приватный;
#     в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#     продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
#     третьего (зелёный) — на ваше усмотрение;
#     переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#     проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle


class TrafficLight:
    __state = {'red': {'state': ' Красный ', 'time': 0, 'color': '\x1b[0;30;41m'},
               'yellow': {'state': ' Желтый  ', 'time': 0, 'color': '\x1b[0;30;43m'},
               'green': {'state': ' Зеленый ', 'time': 0, 'color': '\x1b[0;30;42m'}}
    __END = '\x1b[0m'

    def __init__(self, t_red=7, t_yellow=3, t_green=2):
        if t_red != 0:
            self.__state['red']['time'] = t_red
        if t_red != 0:
            self.__state['yellow']['time'] = t_yellow
        if t_red != 0:
            self.__state['green']['time'] = t_green

    def running(self):
        for key in cycle(self.__state):
            state = self.__state[key]
            output = state['color'] + state['state'] + self.__END
            print('\r', output, end='')
            sleep(state['time'])


TrafficLight = TrafficLight(7, 3, 6)
TrafficLight.running()

