# Ходы ферзя.
# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки,
# которые бьет ферзь. Клетку, где стоит ферзь, отметьте буквой Q,
# клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.
#
# Формат входных данных:
# На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации
# (то есть в виде e4, где сначала записывается номер столбца
# (буква от a до h, слева направо),
# затем номер строки (цифра от 1 до 8, снизу вверх)).
#
# Формат выходных данных:
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

queen = input()
x = ord(queen[0]) - 97
y = 8 - int(queen[1])
chessboard = [['.' for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i == x and j == y:
            chessboard[j][i] = "Q"
        elif (i != x and j == y) or (i == x and j != y):
            chessboard[j][i] = "*"
        elif abs(i - x) == abs(j - y):
            chessboard[j][i] = "*"

for row in chessboard:
    print(*row)
