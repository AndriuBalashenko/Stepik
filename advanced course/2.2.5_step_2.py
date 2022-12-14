# Различные элементы.
# На вход программе подается строка текста, содержащая натуральные числа,
# расположенные по неубыванию. Из строки формируется список чисел.
# Напишите программу для подсчета количества разных элементов в списке.

# Формат входных данных:
# На вход программе подается строка текста, содержащая натуральные числа,
# разделенные символом пробела, расположенные по неубыванию.

# Формат выходных данных:
# Программа должна вывести одно число – количество различных элементов списка.

# Примечание. Задачу можно решить без множеств.

lst_nums = [int(_) for _ in input().split()]
count = 1
var = lst_nums[0]
for item in lst_nums:
    if item > var:
        count += 1
    var = item
print(count)
