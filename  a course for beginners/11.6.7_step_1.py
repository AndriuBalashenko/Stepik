# Количество артиклей.
# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
#
# Формат входных данных
# На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.
#
# Формат выходных данных
# Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с поясняющим текстом.
#
# Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.

text = input().lower().split()

a = text.count('a')
an = text.count('an')
the = text.count('the')
amount_articles = a + an + the

# amount_articles = 0
# for _ in range(len(text)):
#     if 'a' in text or 'an' in text or 'the' in text:
#         amount_articles += 1

print('Общее количество артиклей:', amount_articles)