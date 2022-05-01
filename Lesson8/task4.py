# Task 4
#
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class Stock:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address} "


class Equipment:
    def __init__(self, maker, model, weight, height, width, depth):
        self.maker = maker
        self.model = model
        self.weight = weight
        self.height = height
        self.width = width
        self.depth = depth

    def __str__(self):
        return f"Name: {self.maker}, Address: {self.model} "


class Printer(Equipment):
    def __init__(self, maker, model, weight, height, width, depth, print_res, color=False):
        self.print_res = print_res
        self.color = color
        super().__init__(maker, model, weight, height, width, depth)


class Scanner(Equipment):
    def __init__(self, maker, model, weight, height, width, depth, scan_res, scanner_type):
        self.scan_res = scan_res
        self.scanner_type = scanner_type
        super().__init__(maker, model, weight, height, width, depth)


class Copier(Equipment):
    def __init__(self, maker, model, weight, height, width, depth, speed):
        self.speed = speed
        super().__init__(maker, model, weight, height, width, depth)