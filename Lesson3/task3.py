# Task3

# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.


def input_number(request):
    while True:
        try:
            return float(input(request))
        except ValueError:
            print("Неверное значение...")


def my_func(a1, a2, a3):
    return a1 + a2 + a3 - min(a1, a2, a3)


arg1 = input_number("Введите число 1:")
arg2 = input_number("Введите число 2:")
arg3 = input_number("Введите число 3:")

print(f"Сумма наибольших двух чисел равна: {my_func(arg1, arg2, arg3):.4f}")
