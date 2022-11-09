# Делители 2.
# Напишите функцию number_of_factors(num),
# принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
#
# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

def number_of_factors(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    return counter

n = int(input())
print(number_of_factors(n))