while True:
    try:
        n = int(input("Введите число:"))
        break
    except ValueError:
        print("Неправильное значение...")
sum = n + int(2*str(n)) + int(3*str(n))
print(f"Сумма равна: {sum}")