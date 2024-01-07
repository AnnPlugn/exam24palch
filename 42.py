def transp(Matrix):
    transp_matrix = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            transp_matrix[j][i] = Matrix[i][j]
    return transp_matrix


m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = [[int(input(f"Введите элемент матрицы: ")) for _ in range(n)] for _ in range(m)]
for row in matrix:
    print( row)
for row_tr in transp(matrix):
    print( row_tr)
