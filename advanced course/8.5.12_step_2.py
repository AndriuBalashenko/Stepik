# Уникальные символы 2.
# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
#
# Формат входных данных:
# На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
#
# Формат выходных данных:
# Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.

n = int(input())
my_list = []
for _ in range(n):
    word = input()
    my_list.append(word.upper())

new_set = set()
for elem in my_list:
    for letter in elem:
        new_set.add(letter)
print(len(new_set))

# n = int(input())
# symbols = set()
#
# for _ in range(n):
#     for c in input().lower():
#         symbols.add(c)
#
# print(len(symbols))
