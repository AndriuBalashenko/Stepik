# Возведение матрицы в степень 🌶️
# Напишите программу, которая возводит квадратную матрицу в m-ую степень.
#
# Формат входных данных:
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы, затем натуральное число m.
#
# Формат выходных данных:
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

n = int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]
m = int(input())
doublet = [[i for i in row] for row in matrix]
result = [[0] * n for i in range(n)]
for _ in range(m - 1):
    result = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                result[i][j] += matrix[i][r] * doublet[r][j]
    doublet = result
for r in range(n):
    for c in range(n):
        print(result[r][c], end=' ')
    print()
