# Количество совпадающих.
# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая определяет количество чисел,
# которые есть как в первой строке, так и во второй.
#
# Формат входных данных:
# На вход программе подаются две строки текста, содержащие числа,
# отделенные символом пробела.
#
# Формат выходных данных:
# Программа должна вывести количество чисел,
# содержащихся одновременно как в первой строке, так и во второй.

print(set([int(i) for i in input()]) & set([int(i) for i in input()]))