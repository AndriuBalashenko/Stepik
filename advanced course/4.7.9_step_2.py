# Сложение матриц.
# Напишите программу для вычисления суммы двух матриц.
#
# Формат входных данных:
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах,
# затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
#
# Формат выходных данных:
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

n,m = [int(i) for i in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
empty = input()
matrix_2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix_3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

for r in range(n):
    for c in range(m):
        print(matrix_3[r][c], end=" ")
    print()
