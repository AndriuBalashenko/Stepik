# Снежинка.
# На вход программе подается нечетное натуральное число n. Напишите программу,
# которая создает матрицу размером n×n заполнив её символами . .
# Затем заполните символами * среднюю строку и столбец матрицы,
# главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.
#
# Формат входных данных:
# На вход программе подается нечетное натуральное число n,(n≥3) — количество строк и столбцов в матрице.
#
# Формат выходных данных:
# Программа должна вывести матрицу в соответствии с условием задачи.

n = int(input())
matrix = [['.'] * n for _ in range(n)]
for i in range(n):
    matrix[n // 2][i] = '*'
    matrix[i][n // 2] = '*'
    matrix[i][i] = '*'
    matrix[i][n - i - 1] = '*'

for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]), end=' ')
        print()

# n = int(input())
# matrix = [['.'] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2:
#             matrix[i][j] = '*'
#         elif i == j or i + j + 1 == n:
#             matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)