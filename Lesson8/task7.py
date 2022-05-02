# Task 7
#
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:
    def __init__(self, real=0, imaginary=0):
        if not isinstance(real, (int, float)):
            raise TypeError("Вещественная часть должна быть числом.")
        if not isinstance(imaginary, (int, float)):
            raise TypeError("Мнимая часть должна быть числом.")
        self.__real = real
        self.__imaginary = imaginary

    def __str__(self):
        con = ''
        if self.__imaginary > 0:
            con = '+'
        return f"{self.real} {con} {self.__imaginary}i"

    def __add__(self, other):
        real = self.__real + other.real
        imaginary = self.__imaginary + other.imaginary
        return Complex(real, imaginary)

    def __mul__(self, other):
        a, b = self.__real, self.__imaginary
        c, d = other.real, other.imaginary
        real = a * c - b * d
        imaginary = b * c + a * d
        return Complex(real, imaginary)

    @property
    def real(self):
        return self.__real

    @property
    def imaginary(self):
        return self.__imaginary


z1 = Complex(-3.6, 8)
z2 = Complex(15, -5)

print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)

