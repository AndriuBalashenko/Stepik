# Общие цифры.
# На вход программе подается натуральное число n, а затем n различных натуральных чисел,
# каждое на отдельной строке. Напишите программу, которая выводит все общие цифры
# в порядке возрастания у всех введенных чисел.
#
# Формат входных данных:
# На вход программе подаются натуральное число n, n≥1, а затем n различных натуральных чисел,
# каждое на отдельной строке.
#
# Формат выходных данных:
# Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет,
# то ничего выводить не нужно.

n = int(input())
new_set = set(int(i) for i in input())
for _ in range(n - 1):
    my_set = set([int(i) for i in input()])
    new_set.intersection_update(my_set)
print(*sorted(new_set))


