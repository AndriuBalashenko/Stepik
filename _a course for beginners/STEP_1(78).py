# Две половинки.
# На вход программе подается строка текста. Напишите программу,
# которая разрежет ее на две равные части, переставит их местами и выведет на экран.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если длина строки нечетная,
# то длина первой части должна быть на один символ больше.

s = input()
n = len(s) // 2 + len(s) % 2
g = s[:n]
t = s[n:]
print(t + g)




