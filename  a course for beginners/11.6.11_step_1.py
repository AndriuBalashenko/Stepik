# Сортировка чисел.
# На вход программе подается строка текста, содержащая целые числа.
# Из данной строки формируется список чисел. Напишите программу,
# которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести две строки текста в соответствии с условием задачи.

row_text = input().split()
for item in range(len(row_text)):
    row_text[item] = int(row_text[item])
row_text.sort()
print(*row_text)
row_text.sort(reverse=True)
print(*row_text)

