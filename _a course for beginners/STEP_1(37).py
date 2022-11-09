# Дано натуральное число. Напишите программу,
# которая определяет,
# состоит ли указанное число из одинаковых цифр.
num = int(input())
flag = True
l_d = num % 10
while num != 0:
    n = num % 10
    if n != l_d:
        flag = False
    num = num // 10
if flag == False:
    print('NO')
else:
    print('YES')
