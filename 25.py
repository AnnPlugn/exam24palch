# Функция для проверки, содержит ли столбец только положительные элементы
def is_positive_column(col):
    for elem in col:
        if elem <= 0:
            return False
    return True

# Запрашиваем у пользователя количество строк и столбцов
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

# Создаем пустую матрицу
matrix = []

# Заполняем матрицу введенными значениями
for i in range(m):
    row = [int(input(f"Введите элемент матрицы для строки {i+1}, столбца {j+1}: ")) for j in range(n)]
    matrix.append(row)

# Ищем номер последнего столбца с положительными элементами
last_positive_col = -1
for j in range(n):
    col = [matrix[i][j] for i in range(m)]
    if is_positive_column(col):
        last_positive_col = j

# Если не найден такой столбец, выводим исходную матрицу
if last_positive_col == -1:
    print("Требуемых столбцов нет, выводим исходную матрицу:")
    for row in matrix:
        print(row)
else:
    # Меняем местами первый и последний столбец с положительными элементами
    for i in range(m):
        matrix[i][0], matrix[i][last_positive_col] = matrix[i][last_positive_col], matrix[i][0]

    # Выводим измененную матрицу
    print("Измененная матрица:")
    for row in matrix:
        print(row)
"""". Дана матрица размера M×N. Поменять местами столбец с номером 1 и последний из
столбцов, содержащих только положительные элементы. Если требуемых столбцов
нет, то вывести матрицу без изменений
 """""