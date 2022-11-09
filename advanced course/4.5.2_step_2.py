# Максимум в таблице.
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем n строк по m целых чисел в каждой, отделенных символом пробела.
#
# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.
#
# Формат входных данных:
# На вход программе на разных строках подаются два числа n и m — количество строк и столбцов в матрице,
# затем сами элементы матрицы построчно через пробел.
#
# Формат выходных данных:
# Программа должна вывести два числа: номер строки и номер столбца,
# в которых стоит наибольший элемент таблицы. Если таких элементов несколько,
# то выводится тот, у которого меньше номер строки, а если номера строк равны то тот,
# у которого меньше номер столбца.
#
# Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.

n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
max_matrix = int(matrix[0][0])
a = 0
b = 0
for i in range(n):
    for j in range(m):
        if int(matrix[i][j]) > int(max_matrix):
            a = i
            b = j
            max_matrix = matrix[i][j]

print(a, b)
