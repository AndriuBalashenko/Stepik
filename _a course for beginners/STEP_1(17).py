# На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел
# от 1 до n (включительно) квадрат которых оканчивается на 2, 5 или 8.

from math import pow
n = int(input())
counter = 0
for i in range(1, n + 1):
    if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
        counter += i
print(counter)
