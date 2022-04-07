while True:
    try:
        revenue = float(input("Введите выручку фирмы:"))
        if revenue >= 0:
            break
    except ValueError:
        print("Введите положительное число...")
while True:
    try:
        costs = float(input("Введите издержки фирмы:"))
        if costs >= 0:
            break
    except ValueError:
        print("Введите положительное число...")
profit = revenue > costs
if profit:
    print("Фирма работает с прибылью.")
else:
    print("Фирма работает с убытком.")