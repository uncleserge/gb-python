# Task 1
#
# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

print("Вводите текст. Для завершения введите пустую строку.")

with open('my_file.txt', 'w') as write_f:
    while True:
        line = input(': ')
        if not line:
            break

        write_f.write(line + '\n')

print('Результат работы:\n')
with open('my_file.txt') as read_f:
    for read_line in read_f:
        print(read_line, end='')
