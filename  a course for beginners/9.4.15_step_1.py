# Удаление фрагмента.
# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

row = input()
place_1 = row.find('h')
place_2 = row.rfind('h')
print(row.replace(row[place_1:place_2], ''))