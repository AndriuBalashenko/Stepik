# Корни уравнения 🌶️🌶️
# Напишите функцию solve(a, b, c),
# которая принимает в качестве аргументов три целых числа a, b, c
# – коэффициенты квадратного уравнения ax**2+bx+c=0
# и возвращает его корни в порядке возрастания.
# Примечание 1. С подобной задачей мы уже сталкивались.
# Примечание 2. Гарантируется, что квадратное уравнение имеет корни.

from math import pow, sqrt
def solve(a, b, c):
    a, b, c = float(a), float(b), float(c)
    d = pow(b, 2) - (4 * a * c)
    if d == 0:
        x = -b / (2 * a)
        return x, x

    if d > 0:
        x_1 = (- b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
        x_2 = (- b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
        x_3 = min(x_1, x_2)
        x_4 = max(x_1, x_2)
        return x_3, x_4


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
