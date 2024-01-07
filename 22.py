m = int(input("Число строк: "))
n = int(input("Число колонок: "))
dm = m//2
dn = n//2
matrix = [[int(input('введите элемент матрицы: ')) for _ in range(n)] for _ in range(m)]
cut1q = [row[:dn] for row in matrix[:dm]]  # Левая верхняя четверть
cut2q = [row[dn:] for row in matrix[dm:]]  # Правая нижняя четверть

# Поменять местами левую верхнюю и правую нижнюю четверти матрицы
for i in range(dm):
    for j in range(dn):
        matrix[i][j], matrix[i+dm][j+dn] = matrix[i+dm][j+dn], matrix[i][j]

print(cut1q)
print(cut2q)
for j in range(len(matrix)):
    print(matrix[j])

"""". Дана матрица размера M×N (M и N – четные числа). Поменять местами левую
верхнюю и правую нижнюю четверти матрицы.
 """""