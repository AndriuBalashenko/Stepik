# Дополните приведенный код, чтобы он вывел
# сумму квадратов элементов множества numbers.

from math import pow
x = 0
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
for num in numbers:
    num = pow(num, 2)
    x += num
print(int(x))

# print(sum(num * num for num in numbers))