# Делители 1
# Напишите функцию get_factors(num),
# принимающую в качестве аргумента
# натуральное число и возвращающую
# список всех делителей данного числа.

def get_factors(num):
    list_divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            list_divisors.append(i)
    return list_divisors

n = int(input())
print(get_factors(n))
