#  Секретное слово.
# Напишите программу для расшифровки секретного слова методом частотного анализа.
#
# Формат входных данных:
# В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
# В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.
#
# Формат выходных данных:
# Программа должна вывести дешифрованное слово.
#
# Примечание. Гарантируется, что частоты букв не повторяются.


code_word = input()
amount_letters = int(input())
dct_l = {}
for _ in range(amount_letters):
    letter, num_times = input().split(': ')

    dct_l.update(dict.fromkeys(letter, int(num_times)))
inv_dct_l = {value: key for key, value in dct_l.items()}

dct_s = {}
for i in code_word:
    dct_s[i] = dct_s.get(i, 0) + 1

for i in code_word:
    print(inv_dct_l[dct_s[i]], end='')


# dct, word = {}, {}
# s = input()
# for c in s:
#     word[c] = word.get(c, 0) + 1
# for _ in range(int(input())):
#     a, b = input().split(': ')
#     dct[int(b)] = a
# for c in s:
#     print(dct[word[c]], end='')