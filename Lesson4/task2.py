# Task 2
#
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


import random


quantity = 15  # quantity of list elements
min_value = 0  # range of values
max_value = 120

# initial list
my_list = [random.randint(min_value, max_value) for i in range(0, quantity)]
print(f'Исходный список: {my_list}')

# new list
new_list = [my_list[i] for i in range(1, quantity) if my_list[i-1] < my_list[i]]
print(f'Сформированный список: {new_list}')
