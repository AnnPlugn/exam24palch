def sum_diag(n, m):
    try:
        if n != m:
            raise ValueError("Матрица не является квадратной")

        matrix = [[int(input(f"Введите элемент матрицы: ")) for _ in range(n)] for _ in range(m)]
        diagonal_sum = 0
        for i in range(len(matrix)):
            diagonal_sum += matrix[i][i]

        return diagonal_sum
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
print(sum_diag(n, m))