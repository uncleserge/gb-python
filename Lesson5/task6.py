# Task 6
#
# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re
from functools import reduce

subjects = {}
try:
    with open('task6.txt', encoding='utf-8') as read_f:
        lines = read_f.read().splitlines()
except IOError:
    print("Произошла ошибка ввода-вывода!")
else:
    for line in lines:
        subject, hours = line.split(':')
        # get tuple of hours for current subject
        hours = (int(el[0]) for el in (re.findall(r'\d+', el) for el in re.split(r'\s+', hours.strip())) if len(el) > 0)
        # count total hours
        total_hours = reduce(lambda a, b: a + b, hours, 0)
        print(subject, total_hours)
        # put result to dictionary
        subjects[subject] = total_hours

print(subjects)