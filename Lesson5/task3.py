# Task 3
#
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
#
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

from functools import reduce

with open('task3.txt', 'r', encoding="utf-8") as read_f:
    lines = read_f.readlines()

count = len(lines)
xxx = ',\n'.join('{}'.format(surname) for surname, salary in (el.split() for el in lines) if float(salary) > 20000)
print(xxx)


print('Сотрудники с окладом более 20000 у.е.:\n' +
      ',\n'.join('{}'.format(surname) for surname, salary in (el.split() for el in lines) if float(salary) > 20000) +
      '\n')

average_income = reduce(lambda a, b: a + b, {float(salary) for surname, salary in (el.split() for el in lines)})/count
print(f'Среднеяя величина дохода сотрудников: {average_income:.2f} у.е.')
