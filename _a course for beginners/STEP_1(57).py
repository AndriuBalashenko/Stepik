# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
# Формат выходных данных:
# Программа должна вывести два числа на одной строке, разделенных пробелом:
# число с максимальной суммой делителей и сумму его делителей.
#
# Примечание. Если таких чисел несколько, то выведите наибольшее из них.
a = int(input())
b = int(input())
sum_digit = 0
max_digit = 0
for n in range(a, b + 1):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += i
            if counter >= sum_digit:
                sum_digit = counter
                max_digit = n
print(max_digit, sum_digit)
