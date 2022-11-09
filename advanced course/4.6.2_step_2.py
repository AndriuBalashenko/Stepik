# Побочная диагональ
# На вход программе подается натуральное число nn. Напишите программу,
# которая создает матрицу размером n × n и заполняет её по следующему правилу:
#
# числа на побочной диагонали равны 1;
# числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.
#
# Формат входных данных:
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.
#
# Формат выходных данных:
# Программа должна вывести матрицу в соответствии с условием задачи.
#
# Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.

n = int(input())
matrix = [['0' for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 > n:
            matrix[i][j] = '2'
        elif i + j + 1 == n:
            matrix[i][j] = '1'

for r in matrix:
    print(*r)