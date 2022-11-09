# Списочное выражение 1
# На вход программе подается натуральное число n. Напишите программу,
# использующую списочное выражение, которая создает список
# содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно,
# то есть каждый на отдельной строке.
#
# Формат входных данных
# На вход программе подается натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Для вывода элементов списка используйте цикл for.

# n_range = int(input())
# new_list = [digit ** 2 for digit in range(1, n_range + 1)]
# print(*new_list, sep='\n')
print(*[digit ** 2 for digit in range(1, int(input()) + 1)], sep='\n')
