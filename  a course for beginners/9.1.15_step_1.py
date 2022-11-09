# Decimal to Binary
# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести число записанное в двоичной системе счисления.

# n = int(input())
# a = format(n, 'b')
# print(a)

# Решение выше оптимальное.
# Format.
#
# P.S. кто не смог решить можете воспользоваться a = format(a, 'b') , b в этом случае
# и переводит значение нашей переменной в 2-ичную систему.
#
# s - строка, можно не указывать, используется по умолчанию;
# b - двоичный формат;
# с - преобразует целое число в символ Unicode;
# d - десятичный формат;
# e - научный формат, со строчной буквой e;
# E - научный формат, с E верхним регистром;
# f - формат чисел с плавающей запятой;
# F - формат чисел с плавающей запятой, верхний регистр;
# g - общий формат, нижний регистр;
# G - общий формат, верхний регистр;
# o - Восьмеричный формат;
# x - шестнадцатеричный формат, нижний регистр;
# X - шестнадцатеричный формат, верхний регистр;
# n - формат целых чисел;
# %- Процентный формат. Умножает число на 100 и использует f для вывода. В конце ставится %;
# #- альтернативный вариант вывода указанного формата, работает с форматами b, o, x.

n = int(input())
t = ''
while n > 0:
    t = str(n % 2) + t  # при сложении (конкатенации) строк важен порядок.
    # При написаннов в коде варианте число в двоичной системе счисления идёт в нужном порядке,
    # если слагаемые поменять местами так d = d + str(n % 2), то двоичное число окажется записано наоборот, с конца.
    n //= 2
print(t)


# Преобразование десятичных чисел в двоичные:
#
# Допустим, нам нужно перевести число 19 в двоичное. Вы можете воспользоваться следующей процедурой :
#
# 19/2 = 9 с остатком 1
# 9/2 = 4 c остатком 1
# 4/2 = 2 без остатка 0
# 2/2 = 1 без остатка 0
# 1/2 = 0 с остатком 1
#
# Итак, мы делим каждое частное на 2 и записываем остаток в конец двоичной записи.
# Продолжаем деление до тех пор, пока в частном не будет 0. Результат записываем справа налево.
# То есть нижняя цифра (1) будет самой левой и т. д.
# В результате получаем число 19 в двоичной записи: 10011.
