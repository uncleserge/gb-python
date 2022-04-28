# Task 7
#
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import re
import json


def read_line_from_file(file_name):
    with open(file_name, encoding='utf-8') as read_f:
        for line in read_f:
            yield line


try:
    lines = read_line_from_file("task7.txt")
except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()

total_profit = 0
firm_plus_count = 0
average_profit = {}
firms = {}

for line in lines:
    name, firm_type, revenue, costs = re.split(r'\s+', line, 3)
    profit = int(revenue) - int(costs)
    if profit > 0:
        total_profit += profit
        firm_plus_count += 1
    firms[name] = profit
print(f"Фирмы: {firms}")
average_profit['average_profit'] = total_profit / firm_plus_count
print(f"Средняя прибыль: {average_profit}")

data = [firms, average_profit]
print(data)

with open("task7.json", "w") as write_f:
    json.dump(data, write_f)
