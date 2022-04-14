while True:
    try:
        s = abs(int(input("Введите время в секундах:")))
        break
    except ValueError:
        print("Введите число...")

h = s // 3600  # часы
s -= 3600 * h

m = s // 60  # минуты
s -= 60 * m

print(f"Время: {h}:{m:02d}:{s:02d}")
