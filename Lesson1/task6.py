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
is_profit = revenue > costs
if is_profit:
    print("Фирма работает с прибылью.")
    profit = revenue - costs
    profitability = profit / revenue
    print(f"Рентабельность: {profitability * 100:.2f}%")
    while True:
        try:
            quantity = int(input("Введите число сотрудников:"))
            if quantity > 0:
                break
        except ValueError:
            print("Введите положительное число...")
    print(f"Прибыль в расчёте на одного сотрудника составляет {profit / quantity:.2f}")
else:
    print("Фирма работает с убытком.")