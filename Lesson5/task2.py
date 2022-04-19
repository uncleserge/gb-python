# Task 2
#
# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


def read_line_from_file(file_name):
    with open(file_name) as read_f:
        for line in read_f:
            yield line


lines = read_line_from_file("task2.txt")
str_count = 0
for el in lines:
    str_count += 1
    print(f'В строка {str_count} кол-во слов {len(el.split())}')

print(f'Количество строк: {str_count}')