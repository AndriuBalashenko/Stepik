# Заполнение змейкой.
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n×m заполнив её "змейкой" в соответствии с образцом.
#
# Формат входных данных:
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#
# Формат выходных данных:
# Программа должна вывести указанную матрицу в соответствии с образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
# Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.

n, m = [int(i) for i in input().split()]
matrix = [['*'] * m for _ in range(n)]
index = 0
for r in range(n):
    if r % 2 == 0:
        for c in range(m):
            index += 1
            matrix[r][c] = index
    else:
        for c in reversed(range(m)):
            index += 1
            matrix[r][c] = index

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()