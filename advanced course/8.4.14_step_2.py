# Все 10 цифр.
# На вход программе подаются две строки, состоящие из цифр.
# Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?
#
# Формат входных данных:
# На вход подаются две строки, состоящие из цифр.
#
# Формат выходных данных:
# Программа должна вывести YES, если в записи этих двух строк используются все десять цифр, и NO в противном случае.


print('YES' if len(set(input() + input())) == 10 else 'NO')
