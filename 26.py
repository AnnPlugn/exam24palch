# Запрашиваем у пользователя количество строк и столбцов
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

# Создаем пустую матрицу
matrix = []

# Заполняем матрицу введенными значениями
for i in range(m):
    row = [int(input(f"Введите элемент матрицы для строки {i+1}, столбца {j+1}: ")) for j in range(n)]
    matrix.append(row)

# Находим максимальный элемент и его столбец
max_value = matrix[0][0]
max_col = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_col = j

# Удаляем столбец с максимальным элементом
for i in range(m):
    del matrix[i][max_col]

# Выводим полученную матрицу
for row in matrix:
    print(row)
"""". Дана матрица размера M×N. Удалить столбец, содержащий максимальный элемент
матрицы
 """""