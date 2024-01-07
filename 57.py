import random

def generate_matrix(rows, cols, min_val, max_val):
    if rows != cols:
        raise ValueError("Матрица должна быть квадратной")
    matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
    return matrix

def average_above_main_diagonal(matrix):
    total = 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > i:
                total += matrix[i][j]
                count += 1
    if count == 0:
        return 0
    return total / count

def count_even_below_main_diagonal(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i and matrix[i][j] % 2 == 0:
                count += 1
    return count

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

try:
    matrix = generate_matrix(rows, cols, min_val, max_val)
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
    print("Среднее арифметическое элементов над главной диагональю:", average_above_main_diagonal(matrix))
    print("Количество четных элементов под главной диагональю:", count_even_below_main_diagonal(matrix))
except ValueError as e:
    print(e)