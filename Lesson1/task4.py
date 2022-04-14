while True:
    try:
        n = int(input("Введите целое положительное число:"))
        if n > 0:
            break
    except ValueError:
        print("Неправильное значение...")
max = 0;
while True:
    r = n % 10;
    if max < r:
        max = r
    n //= 10
    if n == 0:
        break
print(f"Самая большая цифра в числе: {max}")