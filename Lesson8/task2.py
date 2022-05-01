# Task 2
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class MyZeroDivError(Exception):
    def __init__(self, divisible, divider, message="Деление на 0 невозможно."):
        self.__divisible = divisible
        self.__divider = divider
        self.__message = message
        super().__init__(self.__message)

    def __str__(self):
        return f'{self.__message} [{self.__divisible} / {self.__divider}]'


try:
    divle = float(input("Введите делимое:"))
    diver = float(input("Введите делитель:"))
    try:
        if diver == 0:
            raise MyZeroDivError(divle, diver)
        result = divle / diver
        print(f'Результат: {result:.02f}')
    except MyZeroDivError as err:
        print(err)
except ValueError:
    print('Должно быть число.')
