# Task 6
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
import datetime
from abc import ABC
from functools import reduce


class OutOfStockError(Exception):
    def __init__(self, item, message='на складе отсутствует.'):
        self.__item = item
        self.__message = message
        super().__init__(message)

    def __str__(self):
        return f'<{self.__item}> - {self.__message}'


class LogItem:
    def __init__(self, sku, quantity, action, place, date):
        self.__sku = sku
        self.__quantity = quantity
        self.__action = action
        self.__place = place
        self.__date = date

    @property
    def sku(self):
        return self.__sku

    @property
    def quantity(self):
        return self.__quantity

    @property
    def action(self):
        return self.__action

    @property
    def place(self):
        return self.__place

    @property
    def date(self):
        return self.__date


class Log:
    def __init__(self):
        self.__items = list()

    def insert(self, sku, quantity, action, place, date):
        item = LogItem(sku, quantity, action, place, date)
        self.__items.append(item)

    def __str__(self):
        result = "Logger:\n"
        for el in self.__items:
            result += f"{el.sku}, {el.quantity}, {el.action}, {el.place}, {str(el.date)} \n"
        return result


class Stock:
    def __init__(self, name, address, log):
        self.__storage = dict()
        self.__log = log
        self.name = name
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Total: {self.total_quantity()} "

    def equipment_in(self, equipment, place, quantity=1):
        if not isinstance(quantity, int):
            raise TypeError('Параметр "количество" содержит неверный тип данных.')
        if equipment.sku in self.__storage:
            self.__storage[equipment.sku]['quantity'] += quantity
        else:
            self.__storage[equipment.sku] = {'equipment': equipment, 'quantity': quantity}
        self.__log.insert(equipment.sku, quantity, 'in', place, datetime.datetime.now())

    def equipment_out(self, sku, quantity, place):
        if not isinstance(quantity, int):
            raise TypeError('Параметр "количество" содержит неверный тип данных.')
        if sku not in self.__storage:
            raise OutOfStockError(sku, "на складе отсутсвует.")
        if self.__storage[sku]['quantity'] < quantity:
            raise OutOfStockError(sku, " запасов для отгрузки недостаточно.")
        self.__log.insert(sku, quantity, 'out', place, datetime.datetime.now())
        if self.__storage[sku]['quantity'] == quantity:
            return self.__storage.pop(sku)
        else:
            self.__storage[sku]['quantity'] -= quantity
            return self.__storage[sku]

    def total_quantity(self):
        return reduce(lambda a, x: a + x['quantity'], self.__storage)

    @property
    def logger(self):
        return self.__log


class Equipment(ABC):
    def __init__(self, sku, maker, model, weight, height, width, length):
        if not isinstance(weight, (int, float)):
            raise TypeError('"Вес" содержит неверный тип данных.')
        if not isinstance(width, (int, float)):
            raise TypeError('"Ширина" содержит неверный тип данных.')
        if not isinstance(height, (int, float)):
            raise TypeError('"Высота" содержит неверный тип данных.')
        if not isinstance(length, (int, float)):
            raise TypeError('"Длина" содержит неверный тип данных.')
        self.sku = sku
        self.maker = maker
        self.model = model
        self.weight = weight
        self.height = height
        self.width = width
        self.depth = length

    def __str__(self):
        return f"Manufacturer: {self.maker}, Model: {self.model}, SKU: {self.sku} "


class Printer(Equipment):
    def __init__(self, sku, maker, model, weight, height, width, length, print_res, color=False):
        if not isinstance(color, bool):
            raise TypeError('"Цветность" содержит неверный тип данных.')
        self.print_res = print_res
        self.color = color
        super().__init__(sku, maker, model, weight, height, width, length)


class Scanner(Equipment):
    def __init__(self, sku, maker, model, weight, height, width, length, scan_res, scanner_type):
        self.scan_res = scan_res
        self.scanner_type = scanner_type
        super().__init__(sku, maker, model, weight, height, width, length)


class Copier(Equipment):
    def __init__(self, sku, maker, model, weight, height, width, length, speed):
        self.speed = speed
        super().__init__(sku, maker, model, weight, height, width, length)


logger = Log()
stock = Stock('Главный склад', 'Ленина, 15', logger)
printer = Printer('00-365987', 'Brother', 'HL-5250', 5, 30, 40, 30, '600x600')
print(printer)
copier = Copier('AS-365987', 'Brother', 'MFC-8880', 8, 40, 80, 50, 12)
print(copier)
stock.equipment_in(printer, 'Ситилинк', 3)
stock.equipment_in(copier, 'DNS', 1)
print(stock.logger)
item, quantity = stock.equipment_out('00-365987', 1, 'Шаболовка, 35')
print(stock.logger)
try:
    item, quantity = stock.equipment_out('AS-365987', 2, 'Шаболовка, 35')
except OutOfStockError as err:
    print(err)
except TypeError as err:
    print(err)
