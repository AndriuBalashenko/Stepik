# Merge lists 2.
# На вход программе подается число n, а затем n строк,
# содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел.
# Напишите программу, которая объединяет указанные списки
# в один отсортированный список с помощью функции quick_merge(),
# а затем выводит его.
#
# Формат входных данных
# На вход программе подается натуральное число n,
# а затем n строк, содержащих целые числа в порядке
# возрастания, разделенные символом пробела.

def quick_merge(list1, list2):

    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

n = int(input())
new_list = []
new_list_2 = []
for _ in range(n):
    new_list_2 = input().split()
    for i in range(len(new_list_2)):
        new_list_2[i] = int(new_list_2[i])
    new_list = quick_merge(new_list, new_list_2)
print(*new_list)


# print(*sorted(sum([list(map(int, input().split())) for _ in range(int(input()))], [])))


