# Task 1
#
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, param):
        if len(param) == 0 or len(param[0]) == 0:
            raise ValueError("Количество строк или столбцов не должно быть равно нулю.")
        if not isinstance(param, (list, tuple)):
            raise TypeError("Неверный тип данных. Строка должнв содержать список или кортеж.")
        if not all(map(lambda x: isinstance(x, (list, tuple)), param)):
            raise TypeError("Неверный тип данных. Столбец должен содержать список или кортеж.")
        self._num_of_cols = len(param)
        self._num_of_rows = len(param[0])
        if not all(map(lambda x: (len(x) == self._num_of_rows), param)):
            raise ValueError("Все столбцы в матрице должны быть одинаковой размерности.")
        self._elements = param

    def __getitem__(self, item):
        return self._elements[item]

    def __str__(self):
        result = "Матрица: \n"
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                result += f'{self._elements[c][r]:8.2f} '
            result += "\n"
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Матрицу можно складывать только с матрицей.")
        elif not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError("Матрицы должны быть одинаковой размерности.")
        matrix = []
        for a, b in zip(self._elements, other):
            row = []
            for x, y in zip(a, b):
                row.append(x + y)
            matrix.append(row)
        return Matrix(matrix)

    @property
    def rows(self):
        return self._num_of_rows

    @property
    def cols(self):
        return self._num_of_cols


# Пустая матрица

try:
    matr = Matrix([])
except Exception as err:
    print("Ошибка!", err)

# Сложение двух матриц

matr1 = Matrix([[1, 5, 9], [-5, 5, 8], [-6, 7, 54]])
print(matr1)
print(f"Размерность: {matr1.cols} Х {matr1.rows}\n")

matr2 = Matrix([[1, 10, 9], [5, 10, 8], [6, 7, -53]])
print(matr2)
print(f"Размерность: {matr2.cols} Х {matr2.rows}\n")

try:
    print(f'Результат сложения: {matr1 + matr2}')
except Exception as err:
    print("Ошибка!", err)

# Попытка слоджения матриц разных размерностей

matr1 = Matrix([[1, 5, 9], [-5, 5, 8], [-6, 7, 54]])
print(matr1)
print(f"Размерность: {matr1.cols} Х {matr1.rows}\n")

matr2 = Matrix([[1, 10], [5, 8], [6, 7]])
print(matr2)
print(f"Размерность: {matr2.cols} Х {matr2.rows}\n")

try:
    print(f'Результат сложения: {matr1 + matr2}')
except Exception as err:
    print("Ошибка!", err)

# Попытка слоджения не с матрицей

try:
    print(f'Результат сложения: {matr1 + "abc"}')
except Exception as err:
    print("Ошибка!", err)


