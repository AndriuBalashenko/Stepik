# На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран
# произведение цифр введенного числа.
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10
print(product)
