# Простой шифр
# На вход программе подается строка текста. Напишите программу,
# которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.

row = input()
for i in row:
    print(ord(i), end=' ')
