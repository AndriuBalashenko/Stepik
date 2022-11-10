# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных:
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице,
# затем элементы первой матрицы, затем пустая строка. Далее следуют числа m и k
# — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#
# Формат выходных данных:
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

n, m = [int(i) for i in input().split()]
matr_1 = [[int(i) for i in input().split()] for _ in range(n)]
empty = input()
m, k = [int(i) for i in input().split()]
matr_2 = [[int(i) for i in input().split()] for _ in range(m)]
matr_3 = [[0] * k for i in range(n)]
for i in range(n):
    for j in range(k):
        for r in range(m):
            matr_3[i][j] += matr_1[i][r] * matr_2[r][j]

for r in range(n):
    for c in range(k):
        print(matr_3[r][c], end=' ')
    print()


