# Заполнение спиралью 😈😈
# На вход программе подаются два натуральных числа n и m. Напишите программу,
# которая создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.
#
# Формат входных данных:
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#
# Формат выходных данных:
# Программа должна вывести матрицу в соответствии образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
# Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
counter = 1
rows_passed, columns_passed = 0, 0
current_row, current_column = 0, 0

for k in range(n * m):
    if counter == n * m + 1:
        break
    direction = k % 4
    if direction == 0:
        for j in range(columns_passed, m - columns_passed):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        rows_passed += 1
    elif direction == 1:
        for i in range(rows_passed, n - rows_passed + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        columns_passed += 1
    elif direction == 2:
        for j in range(current_column - 1, columns_passed - 2, -1):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, rows_passed - 1, -1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
