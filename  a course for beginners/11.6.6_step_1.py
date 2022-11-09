# Переставить min и max.
# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел. Напишите программу,
# которая меняет местами минимальный и максимальный элемент этого списка.
#
# Формат входных данных
# На вход программе подается строка текста,
# содержащая различные натуральные числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести строку текста в соответствии с условием задачи.

row_nums = input()
list_digit = [int(item) for item in row_nums.split()]

# или так :
# row_nums = row_nums.split()
# list_digit = []
# for item in row_nums:
#     list_digit.append(int(item))

little = list_digit.index(min(list_digit))
big = list_digit.index(max(list_digit))
list_digit[little], list_digit[big] = list_digit[big], list_digit[little]
print(*list_digit)

