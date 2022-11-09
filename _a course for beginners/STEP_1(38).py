# Дано натуральное число. Напишите программу,
# которая определяет, является ли последовательность его цифр при просмотре
# справа налево упорядоченной по неубыванию.
num = int(input())
flag = True
l_d = num % 10
while num != 0:
    n = num % 10
    if l_d > n:
        flag = False
    else:
        l_d = n
    num = num // 10
if flag is True:
    print('YES')
else:
    print('NO')



'''"справа налево упорядоченной по неубыванию”
 означает что правая цифра меньше или РАВНА левой'''
