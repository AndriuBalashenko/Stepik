# Арифметические строки
# Вводятся 3 строки в случайном порядке. Напишите программу,
# которая выясняет можно ли из длин этих строк построить возрастающую
# арифметическую прогрессию.

# Формат входных данных
# На вход программе подаются три строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести строку «YES», если из длин введенных слов
# можно построить арифметическую прогрессию, «NO» в ином случае.
s_1 = input()
s_2 = input()
s_3 = input()
ls_1 = len(s_1)
ls_2 = len(s_2)
ls_3 = len(s_3)
long = max(ls_1, ls_2, ls_3)
short = min(ls_1, ls_2, ls_3)
average = ls_1 + ls_2 + ls_3 - (long + short)
if long - average == average - short:
    print('YES')
else:
    print('NO')








