# Дополните приведенный код так, чтобы он вывел список,
# содержащий средние арифметические значения чисел
# каждого вложенного кортежа в заданном кортеже кортежей numbers.

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
lst = []
for i in numbers:
    var = 0
    for elem in i:
        var += elem
    lst.append(var / len(i))
print(lst)

# print([sum(i) / len(i) for i in numbers])