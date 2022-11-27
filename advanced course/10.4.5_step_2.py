# Страны и города.
# На вход программе подается список стран и городов каждой страны. Затем даны названия городов.
# Напишите программу, которая для каждого города выводит, в какой стране он находится.
#
# Формат входных данных:
# Программа получает на вход количество стран n. Далее идет n строк,
# каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число m, далее идут m запросов — названия каких-то m городов,
# из перечисленных выше.
#
# Формат выходных данных:
# Программа должна вывести название страны, в которой находится данный город в соответствии с примером.


n = int(input())
final_dict = {}
for _ in range(n):
    row = input().split()
    key = row[0]
    values = row[1:]
    final_dict.setdefault(key, values)
    final_dict.update(final_dict)

m = int(input())
for _ in range(m):
    city = input()
    for k, v in final_dict.items():
        if city in v:
            print(k)


# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])