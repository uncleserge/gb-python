# Task 1
#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date_str):
        if not isinstance(date_str, str):
            raise TypeError("Значение должно быть строкой")
        try:
            d, m, y = self.convert(date_str)
        except:
            raise ValueError("Строка должна быть в формате день-месяц-год.")
        if self.is_valid_date(y, m, d):
            self.__day = d
            self.__month = m
            self.__year = y
        else:
            raise ValueError(f"Неверное значение даты. [{date_str}]")
        pass

    def __str__(self):
        return f'Day: {self.day} Month: {self.month} Year: {self.year}'

    @classmethod
    def convert(cls, date_str):
        return map(int, date_str.split('-'))

    @classmethod
    def from_string(cls, date_str):
        return cls(date_str)

    @staticmethod
    def is_valid_date(year, month, day):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[1] += 1
        return 1 <= month <= 12 and 1 <= day <= days_in_month[month-1]

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day


date1 = Date('30-12-1980')
print(date1)

date2 = Date.from_string('30-12-2020')
print(date2)

try:
    date3 = Date("32-2-1993")
except ValueError as err:
    print(err)
