# Task 4
#
# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

splitter = ' — '
trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

# Returns all file content
def get_text_from_file(filename):
    text = ''
    try:
        with open(filename, encoding='utf-8') as read_f:
            text = read_f.read()
    except IOError:
        print('Произошла ошибка ввода-вывода!')
    return text

# Returns list of lines from file
def get_lines_from_file(filename):
    lines = list()
    try:
        with open(filename, encoding='utf-8') as read_f:
            lines = read_f.read().splitlines()
    except IOError:
        print('Произошла ошибка ввода-вывода!')
    return lines

# Write text to the file
def write_text_to_file(text, filename):
    try:
        with open(filename, 'w', encoding="utf-8") as write_f:
            print(text, file=write_f, end='')
    except IOError:
        print("Произошла ошибка ввода-вывода!")


# try 1
lines = get_lines_from_file('task4.txt')
print(f'Readed from file: {lines}')
new_lines = ''.join(trans_dict[t1] + splitter + t2 + '\n' for t1, t2 in (el.split(splitter) for el in lines))
print(f'Translated: \n{new_lines}')
write_text_to_file(new_lines, 'task4_result_1.txt')

# try 2
text = get_text_from_file('task4.txt')
print(f'Readed from file: \n{text}')
for key, el in trans_dict.items():
    text = text.replace(str(key), el)
print(f'Translated: \n{text}')
write_text_to_file(text, 'task4_result_2.txt')
