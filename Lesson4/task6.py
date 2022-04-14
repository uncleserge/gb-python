# Task 6
#
# Реализовать два небольших скрипта:
#
#     итератор, генерирующий целые числа, начиная с указанного;
#     итератор, повторяющий элементы некоторого списка, определённого заранее.
#
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from random import randint
from itertools import count
from itertools import cycle


list_len = 10  # length of list elements
min_value = 0  # range of values
max_value = 20

# initial list
my_list = [randint(min_value, max_value) for i in range(0, list_len)]

# итератор, генерирующий целые числа, начиная с указанного;
print("Итератор count():")
my_count = count(3)

number = 0
while number != 10:
    number = next(my_count)
    print(number, end=" ")
print(end="\n\n")

# итератор, повторяющий элементы некоторого списка, определённого заранее
print("Итератор cycle():")
print(f'Исходный список: {my_list}')

my_cycle = cycle(my_list)
limit = 35
counter = 0
while counter < limit:
    print(next(my_cycle), end=" ")
    counter += 1
print()
