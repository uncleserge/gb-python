while True:
    try:
        km_first_day = float(input("Введите количество км в первый день:"))
        if km_first_day >= 0:
            break
    except ValueError:
        print("Введите положительное число...")
while True:
    try:
        km_needed = float(input("Введите нужное количество км:"))
        if km_needed >= 0:
            break
    except ValueError:
        print("Введите положительное число...")

km_run = km_first_day
days = 1
# побежали
while True:
    print(f" День {days}: {km_run:.2f} км. ")
    if km_run >= km_needed:
        break
    days += 1
    km_run += km_run * 0.1

print(f"На {days} спортсмен достиг результата - не менее {km_needed:.2f}")
