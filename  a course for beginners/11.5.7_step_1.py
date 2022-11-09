# Корректный ip-адрес.
# На вход программе подается строка текста,
# содержащая 4 целых числа разделенных точкой.
# Напишите программу, которая определяет
# является ли введенная строка текста корректным ip-адресом.
#
# Формат входных данных
# На вход программе подается строка текста,
# содержащая 4 целых числа разделенных точкой.
#
# Формат выходных данных
# Программа должна вывести «ДА», если введеная строка является
# корректным ip-адресом, и «НЕТ» — в противном случае.
#
# Примечание. ip-адрес является корректным,
# если все 4 числа находятся в диапазоне от 0 до 255 включительно.



row = input().split('.')
counter = 0
for item in row:
    if 0 <= int(item) <= 255:
        counter += 1
if counter == len(row):
    print('ДА')
else:
    print('НЕТ')


