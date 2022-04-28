# Task 3
#
# Реализовать базовый класс Worker (работник).
#
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
#         оклад и премия, например, {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
#         дохода с учётом премии (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
#     проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


position_list = []
position = Position('Jon', 'Doe', 'unknown', 10000, 5000)
position_list.append(position)
position = Position('John', 'Smith', 'administrator', 20000, 3000)
position_list.append(position)
position = Position('Bill', 'Adams', 'slacker', 1000, 0)
position_list.append(position)

for pos in position_list:
    print('Сотрудник: ', pos.get_full_name(), pos.position)
    print('Доход: ', pos.get_total_income())

