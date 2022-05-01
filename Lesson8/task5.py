# Task 5
#
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


class Stock:
    __storage = dict()

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address} "

    def equipment_in(self, equipment, quantity):
        pass

    def equipment_out(self, equipment, quantity):
        pass


class Equipment:
    def __init__(self, sku, maker, model, weight, height, width, depth):
        self.sku = sku
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

