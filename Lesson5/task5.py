# Task 5
#
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random
from functools import reduce

# quantity of list elements
quantity = 20
# range of values
min_value = 0
max_value = 120

my_list = [random.randint(min_value, max_value) for i in range(0, quantity)]

sum_of_my_list = reduce(lambda a, b: a + b, my_list)
number_str = ' '.join(str(el) for el in my_list)
print('Набор чисел:', number_str)
print(f'Сумма чисел: {sum_of_my_list}')

try:
    with open('task5.txt', 'w') as write_f:
        print(number_str, file=write_f)
except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()

try:
    with open('task5.txt') as read_f:
        line = read_f.read()
except IOError:
    print("Произошла ошибка ввода-вывода!")
else:
    print('\nНабор чисел из файла:', line, end='')
    sum_from_file = reduce(lambda a, b: a + b, (int(el) for el in line.split()))
    print(f'Сумма чисел из файла: {sum_from_file}')
