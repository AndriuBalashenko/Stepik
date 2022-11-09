# Поворот матрицы.
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.
#
# Формат входных данных:
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.
#
# Формат выходных данных:
# Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    for j in range(n):
        matrix[n - i - 1][j], matrix[i][j] = matrix[i][j], matrix[n - i - 1][j]

for r in range(n):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         result[i][j] = matrix[n - j - 1][i]
#
# for row in result:
#     print(*row)