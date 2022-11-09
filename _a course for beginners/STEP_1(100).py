# Алфавит.
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Формат выходных данных
# Программа должна вывести указанный список.
#
# Примечание. Последний элемент списка состоит из 26 символов z.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_list = []
multiplier = 1
for item in alphabet:
    item *= multiplier
    multiplier += 1
    new_list.append(item)
print(new_list)






