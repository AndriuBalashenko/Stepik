# Построчный вывод
# На вход программе подается строка текста. Напишите программу,
# которая выводит слова введенной строки в столбик.

text = input().split()
# print(text) = ['здесь', 'будет', 'список', 'из', 'введенных', 'слов', 'строки']
print(*text, sep='\n')
# Используем префиксный оператор "*" для распаковки списка на элементы
# и переносим каждый на отдельную строку с помощью параметра sep функции print.