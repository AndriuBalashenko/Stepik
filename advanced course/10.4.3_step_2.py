# Анаграммы 2.
# На вход программе подаются два предложения. Напишите программу, которая определяет,
# являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов,
# знаки препинания и пробелы.
#
# Формат входных данных:
# На вход программе подаются два предложения, каждое на отдельной строке.
#
# Формат выходных данных:
# Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.
#
# Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-.
# Других символов в тексте нет.

import string
sentence1 = input().lower().split()
new_list1 = [word.strip(string.punctuation) for word in sentence1]
new_str1 = ''.join(new_list1)

sentence2 = input().lower().split()
new_list2 = [word.strip(string.punctuation) for word in sentence2]
new_str2 = ''.join(new_list2)

res_dict1 = {}
for elem in new_str1:
     res_dict1[elem] = res_dict1.get(elem, 0) + 1

res_dict2 = {}
for elem in new_str2:
    res_dict2[elem] = res_dict2.get(elem, 0) + 1

if res_dict1 == res_dict2:
    print('YES')
else:
    print('NO')


# def s(word):
#     res = {}
#     for i in word.lower():
#         if i.isalpha():
#             res[i] = res.get(i, 0) + 1
#     return res
#
#
# print(("NO", "YES")[s(input()) == s(input())])