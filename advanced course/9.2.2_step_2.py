# Домашнее задание.
# Учитель проверяет домашнее задание в классе и получил следующие ответы:
# из n школьников у m домашнее задание съела собака, у k отключили свет,
# а p учеников постигли оба несчастья. Напишите программу, которая определяет
# сколько человек выполнило домашнее задание.
#
# Формат входных данных:
# На вход программе подаются числа n, m, k, p каждое на отдельной строке.
#
# Формат выходных данных:
# Программа должна вывести количество учеников, сделавших домашнее задание.

n = int(input())
m = int(input())
k = int(input())
p = int(input())

print(n - ((m - p) + p + (k - p)))