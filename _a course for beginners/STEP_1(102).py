# Список делителей
# На вход программе подается натуральное число n. Напишите программу,
# которая создает список состоящий из делителей введенного числа.
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.

n_for_divide = int(input())
new_list = []
for item in range(1, n_for_divide + 1):
    if n_for_divide % item == 0:
        new_list.append(item)
print(new_list)
