# Next Prime 🌶️🌶️
# Напишите функцию get_next_prime(num),
# которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


def get_next_prime(num):
    j = num + 1
    while is_prime(j) == False:
        j += 1
    return j


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))