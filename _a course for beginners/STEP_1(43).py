# На обработку поступает последовательность из 7 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10**6.
# Нужно написать программу, которая подсчитывает и выводит сумму
# всех чётных чисел последовательности или 0, если чётных чисел в последовательности нет.
s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)
