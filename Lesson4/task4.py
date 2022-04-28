# Task 4
#
# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]


import random


quantity = 15  # quantity of list elements
min_value = 0  # range of values
max_value = 20

# initial list
my_list = [random.randint(min_value, max_value) for i in range(0, quantity)]
print(f'Исходный список: {my_list}')

# criteria based list
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Сформированный список: {new_list}')
