# Удалите нечетные индексы
# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу,
# которая создает из указанных чисел список,
# затем удаляет все элементы стоящие по нечетным индексам,
# а затем выводит полученный список.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести список в соответствии с условием задачи.
#
# Примечание. Используйте оператор del.

n_for_range = int(input())
n_list = []
for _ in range(n_for_range):
    n_for_list = int(input())
    n_list.append(n_for_list)
del n_list[1::2]
print(n_list)
