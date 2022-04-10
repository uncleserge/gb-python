# Task 3

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

from calendar import month_name

months = list(month_name)
seasons = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

while True:
    try:
        n = int(input("Введите номер месяца:"))
        if n in range(1, 13):
            break
        else: print("Неверное значение")
    except ValueError:
        print("Ведите число...")

for season in seasons:
    if n in seasons[season]:
        print(f"Month is {months[n]}. Season is {season}.")
        break

