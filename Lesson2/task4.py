# Task 4

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

my_list = input('Введимте значение: ').split()
print('Список значений:', my_list)

for idx, el in enumerate(my_list):
    print(idx, el[0:10])