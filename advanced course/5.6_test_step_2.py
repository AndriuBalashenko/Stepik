#  Латинский квадрат 🌶️
# Латинским квадратом порядка nn называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица
# латинским квадратом.
#
# Формат входных данных:
# На вход программе подаётся натуральное число n — количество строк
# и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой,
# разделённые пробелами.
#
# Формат выходных данных:
# Программа должна вывести слово YES, если матрица является латинским квадратом,
# и слово NO, если не является.


# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))
# res = 'YES'
# for i in matrix:
#     if set(i) != set(range(1, n+1)):
#         res = 'NO'
#         break
# else:
#     matrix = zip(*matrix)
#     for i in matrix:
#         if set(i) != set(range(1, n+1)):
#             res = 'NO'
#             break
# print(res)

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break

print(result)