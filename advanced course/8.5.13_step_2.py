# Количество слов в тексте
# Напишите программу для определения общего количества различных слов в строке текста.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.
#
# Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или большим числом пробелов.
#
# Примечание 2. Знаками препинания .,;:-?! пренебрегаем.


import string

row = input().lower()

for i in string.punctuation:
    row = row.replace(i, '')

my_set = set()
for elem in row.split():
    my_set.add(elem)

print(len(my_set))

# words = [word.lower().strip('.,;:-?!') for word in input().split()]
# print(len(set(words)))