# Максимальный в области 2
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if (i <= j and i >= n - j - 1) or (i >= j and i >= n - j - 1):
            lst.append(matrix[i][j])
print(max(lst))

