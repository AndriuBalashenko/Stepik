# Заполнение 3.
# На вход программе подается натуральное число n. Напишите программу,
# которая создает матрицу размером n×n заполнив её в соответствии с образцом.
#
# Формат входных данных:
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.
#
# Формат выходных данных:
# Программа должна вывести указанную матрицу в соответствии с образцом:
# разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
# Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.

n = int(input())
matrix = [['0'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            matrix[i][j] = '1'

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3),end=' ')
    print()


