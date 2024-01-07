import random

n = int(input("Размер квадратичной матрицы: "))
matrix = [[random.randint(-100,100) for _ in range(n)] for _ in range(n)]

main_diag = []
add_diag = []
for row in range(len(matrix)):
    for el in range(len(matrix[row])):
        if row == el and matrix[row][el] > 0:
            main_diag.append(matrix[row][el])
        if row + el == n and matrix[row][el] <= 0:
            add_diag.append(matrix[row][el])
print(f"Среднее арифметическое положительных элементов главной диагонали: {sum(main_diag)/len(main_diag)}")
print(f"Среднее арифметическое отрицательных элементов побочной диагонали: {sum(add_diag)/len(add_diag)}")
for row in matrix:
    print(row)
"""". В квадратной матрице, элементами которой являются случайные целые числа,
размера n x n найти среднее арифметическое положительных элементов главной
диагонали и среднее арифметическое отрицательных элементов побочной диагонали.
Матрицу вывести на экран.
 """""