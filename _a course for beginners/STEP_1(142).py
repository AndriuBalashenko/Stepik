# Сумма цифр.
# Напишите функцию print_digit_sum(),
# которая принимает одно целое число num
# и выводит на печать сумму его цифр.

# объявление функции

def print_digit_sum():
    num = int(input())
    sum_digit = 0
    while num != 0:
        first_digit = num % 10
        sum_digit += first_digit
        num = num // 10
    print(sum_digit)
print_digit_sum()

