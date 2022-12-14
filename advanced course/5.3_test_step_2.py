# Транспонирование матрицы.
# Напишите программу, которая транспонирует квадратную матрицу.
#
# Формат входных данных:
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.
#
# Формат выходных данных:
# Программа должна вывести транспонированную матрицу.
#
# Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.
#
# Примечание 2. Задачу можно решить без использования вспомогательного списка.

n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        print (matrix[j][i], end=' ')
    print()


# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
# for i in zip(*matrix):
#     print(*i)
