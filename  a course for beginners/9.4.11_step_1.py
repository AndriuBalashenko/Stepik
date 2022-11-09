# Количество цифр.
# На вход программе подается строка текста. Напишите программу,
# которая подсчитывает количество цифр в данной строке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести количество цифр в данной строке.

# row = input()
# counter_of_digits = 0
# for i in row:
#     if i in '0123456789':
#         counter_of_digits += 1
# print(counter_of_digits)

row = input()
counter_of_digits = 0
for digit in '0123456789':
    counter_of_digits += row.count(digit)
print(counter_of_digits)
