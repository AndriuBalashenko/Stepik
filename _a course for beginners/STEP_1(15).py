# На вход программе подается натуральное число n,
# а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
#
# Формат входных данных
# На вход программе подаются натуральное число n,
# а затем n целых чисел, каждое на отдельной строке.
n = int(input())
total = 0
for i in range(n):
    n_2 = int(input())
    total += n_2
print(total)