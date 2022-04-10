# Task 1

# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_int = 8
my_float = 1.5
my_str = "my string"
my_list = ['my', 'list']
my_tuple = ('my', 'tuple', 2020)
my_set = set('abrakadabra')
my_dict = {'x': '136', 'y': '18'}
my_none = None

my_super_list = [my_int, my_float, my_str, my_list, my_tuple, my_set, my_dict, my_none]

for i in my_super_list:
    print(f'{i} имеет тип {type(i)}')