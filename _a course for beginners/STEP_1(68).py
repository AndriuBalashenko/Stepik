# Одинаковые соседи
# На вход программе подается одна строка. Напишите программу,
# которая определяет сколько в ней одинаковых соседних символов.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести количество одинаковых соседних символов.

s = input()
counter = 0
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        counter += 1
print(counter)


