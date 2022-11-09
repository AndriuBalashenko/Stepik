# Google search - 2 🌶️🌶️
# На вход программе подается натуральное число n, затем n строк,
# затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки,
# в которых встречаются все поисковые запросы.
#
# Формат входных данных
# На вход программе подаются натуральное число n — количество строк,
# затем сами строки в указанном количестве,
# затем число k, затем сами поисковые запросы.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.

n_range = int(input())
list_row = []
list_search = []
list_final = []
counter_coincidence = 0

for _ in range(n_range):
    row = input()
    list_row.append(row)

amount_search = int(input())
for _ in range(amount_search):
    search_row = input()
    list_search.append(search_row)

for item in list_row:
    for part in list_search:
        if part.lower() in item.lower():
            counter_coincidence += 1
            if counter_coincidence == len(list_search):
                list_final.append(item)
    counter_coincidence = 0

print(*list_final, sep='\n')
