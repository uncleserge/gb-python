# Task 1

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(dve, dvr):
    return dve / dvr


while True:
    try:
        divisible = abs(int(input("Введите делимое:")))
        break
    except ValueError:
        print("Введите число...")

while True:
    try:
        divider = abs(int(input("Введите делитель:")))
        break
    except ValueError:
        print("Введите число...")

try:
    print(f'Результат деления:  {div(divisible, divider):.4f}')
except ZeroDivisionError:
    print('Ошибка! Деление на ноль!')