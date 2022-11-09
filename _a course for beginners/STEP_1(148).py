# Merge lists 1.
# Напишите функцию merge(list1, list2),
# которая принимает в качестве
# аргументов два отсортированных по возрастанию списка,
# состоящих из целых чисел,
# и объединяет их в один отсортированный список.
#
# Примечание 1. Списки list1 и list2 могут иметь разную длину.
#
# Примечание 2. Можно использовать списочный метод sort(),
# а можно обойтись и без него 😎.

# def merge(list1, list2):
#     for i in range(len(list1) - 1):
#         minimum_value = list1[i]
#         index_minimum_value = i
#         for i_1 in range(i + 1, len(list1)):
#             if minimum_value > list1[i_1]:
#                 minimum_value = list1[i_1]
#                 index_minimum_value = i_1
#         if index_minimum_value != i:
#             list1[index_minimum_value], list1[i] = list1[i], list1[index_minimum_value]
#
#     for j in range(len(list2) - 1):
#         minimum_value_2 = list2[j]
#         index_minimum_value_2 = j
#         for j_2 in range(j + 1, len(list2)):
#             if minimum_value_2 > list2[j_2]:
#                 minimum_value_2 = list2[j_2]
#                 index_minimum_value_2 = j_2
#         if index_minimum_value_2 != j:
#             list2[index_minimum_value_2], list2[j] = list2[j], list2[index_minimum_value_2]
#
#     list3 = list1 + list2
#     for k in range(len(list3) - 1):
#         minimum_value_3 = list3[k]
#         index_minimum_value_3 = k
#         for k_3 in range(k + 1, len(list3)):
#             if minimum_value_3 > list3[k_3]:
#                 minimum_value_3 = list3[k_3]
#                 index_minimum_value_3 = k_3
#         if index_minimum_value_3 != k:
#             list3[index_minimum_value_3], list3[k] = list3[k], list3[index_minimum_value_3]
#
#     return list3
#
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# print(merge(numbers1, numbers2))

def merge(list1, list2):
    return sorted(list1 + list2)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))