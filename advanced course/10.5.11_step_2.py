# Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 11.
#
# Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
#
# result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
# Примечание 2. Выводить содержимое словаря result не нужно.


numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {digit: [divisor for divisor in range(1, digit + 1) if digit % divisor == 0] for digit in numbers}

# result_dict = {}
# for digit in numbers:
#     list_divisors = []
#     for divisor in range(1, digit + 1):
#         if digit % divisor == 0:
#             list_divisors.append(divisor)
#             result_dict[digit] = list_divisors
# #
# print(result_dict)