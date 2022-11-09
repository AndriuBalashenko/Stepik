# Напишите программу, которая считывает последовательность
# из 10 целых чисел и определяет является ли каждое
# из них четным или нет.

counter = 0
for _ in range(10):
    n = int(input())
    if n % 2 == 0:
        counter += 1
if counter == 10:
    print('YES')
else:
    print('NO')


# flag = True
# for _ in range(10):
#     n = int(input())
#
#     if n % 2 == 1:
#         flag = False
# if flag is False:
#     print('NO')
# else:
#     print('YES')
