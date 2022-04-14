# Task 5
#
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from functools import reduce

min_value = 100  # range of values
max_value = 1000

# initial list
my_list = [i for i in range(min_value, max_value + 1) if i & 1 == 0]
print(f'Исходный список: {my_list}')

# result
print(f'Результат: {reduce(lambda a, b : a * b, my_list)}')


