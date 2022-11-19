# Онлайн-школа BEEGEEK 5 🌶️
# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику,
# либо оба этих предмета. У руководителя школы есть списки учеников, изучающих каждый предмет.
# Случайно списки всех учеников перемешались.
#
# Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.
#
# Формат входных данных
# На вход программе в первых двух строках подаются числа m и n – количества учеников,
# изучающих математику и информатику соответственно. Далее идут m+n строк — фамилии учеников,
# изучающих математику и информатику, в произвольном порядке.
#
# Формат выходных данных
# Программа должна вывести количество учеников, которые изучают только один предмет.
# Если таких учеников не окажется, то необходимо вывести NO.
#
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m = int(input())
n = int(input())
pupils = {input() for _ in range(m + n)}
only_math = len(pupils) - m
only_inf = len(pupils) - n
if only_math + only_inf == 0:
    print('NO')
else:
    print(only_math + only_inf)


# m, n = int(input()), int(input())
# set_all = {input() for _ in range(m + n)}
# print(['NO', 2 * len(set_all) - (m + n)][2 * len(set_all) != m + n])


