# программа, которая подсчитывает количество чисел
# в диапазоне от a до b включительно, куб которых
# оканчивается на 4 или 9
from math import pow
a = int(input())
b = int(input())
counter = 0
for i in range(a, b + 1):
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
        counter += 1
print(counter)
