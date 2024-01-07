m = int(input("Число строк: "))
n = int(input("Число колонок: "))
matrix = [[int(input('введите элемент матрицы: ')) for _ in range(n)] for _ in range(m)]

maxi = 0
num_row = 0
for i in range(len(matrix)):
    maxi = max(sum(matrix[i]), maxi)
    if maxi < sum(matrix[i]):
        maxi = sum(matrix[i])
        num_row = i

print(maxi)
print(num_row)


"""". Дана матрица размера M×N. Найти номер ее строки с наибольшей суммой элементов
и вывести данный номер, а также значение наибольшей суммы

 """""