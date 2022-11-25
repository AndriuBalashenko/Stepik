"""
You have an 8x8 grid with coordinates ranging from 1 to 8. The origin (1, 1) is in the top left corner. The bottom right corner is (8, 8).

You are given a string as an input which will contain the 2 coordinates in this format: "(x1 y1)(x2 y2)", where (x1 y1) represents point A and (x2 y2) represents point B. In the inputs provided, point A will always be up and to the left of point B. In other words, x1 < x2 and y1 < y2 will be true for every input.

Your goal is to find out the number of different paths you can take to get from point A to point B by moving one cell at a time either down or right.

Example
Given an input of "(2 3)(3 5)", the number of possible paths to get from A to B is 3.

 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  A  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  B  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
Possible paths, marked with x:

A .       A .       A x
x .       x x       . x
x B       . B       . B
"""


def travel_chessboard(s):
    s = s.replace(')(', ',')
    s = s.replace(' ', ',')
    s = s.replace(')', '')
    s = s.replace('(', '')
    string = s.split(',')
    x1 = s[0]
    y1 = s[2]
    x2 = s[4]
    y2 = s[6]
    a = [[0] * 8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            if i == 0:
                a[i][j] = 1
            elif j == 0:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j] + a[i][j - 1]
    print(a)
    return a[int(x2) - int(x1)][int(y2) - int(y1)]
