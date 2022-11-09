# След матрицы
# Следом квадратной матрицы называется сумма элементов главной диагонали.
# Напишите программу, которая выводит след заданной квадратной матрицы.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — след заданной матрицы.

n = int(input())
matrix = []
count = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    count += matrix[i][i]
print(count)
