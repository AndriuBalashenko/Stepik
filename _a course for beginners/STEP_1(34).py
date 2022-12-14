# Дано натуральное число n, n ≥ 10.
# Напишите программу, которая определяет его максимальную и минимальную цифры.

""" 1. Поле ввода.
2. Вводим переменные, с которыми будем сравнивать полученные
в результате num // 10 и num % 10 числа.
3. Чтобы получить минимальное число, надо его сравнивать с бОльшим от 0 до 9, т.е. с 9,
а максимальное - с меньшим, т.е. с 0.
4. Пример:
num = 8954
n_max = 0
n_min = 9
while num != 0:
    if num % 10 (это цифра 5) < n_min(это 9):
        n_min = num % 10 (переприсваиваем переменной n_min(9) полученное значение - цифру 4,
                          теперь у нас n_min = 4)
                          Внизу у нас num = num // 10 - отсекает последнюю цифру 4 (остаётся число 895 )
                           и цикл повторяется заново со слудующей цифрой, т.е.:
                           if num % 10 (это теперь цифра 5) < n_min(это теперь цифра 4):
                           В данном примере цикл условие не выполняется ( 5 не меньше 4),
                           поэтому вложенный блок  n_min = num % 10 не выполняется, и переменная
                           n_min не переназначается, далее num = num // 10 - отсекает следующюю цифру 5,
                          (остаётся число 89), и проверяется 9, а затем 8. Как видно, n_min у нас в примере
                          остаётся = 4, что и выводится на print.

    Аналогично проверяются все цифры числа num на максимальное значение, путём сравнения
    с заданной выше переменной n_max:
    if num % 10 > n_max:
        n_max = num % 10
    num = num // 10
print('Максимальная цифра равна', n_max)
print('Минимальная цифра равна', n_min)
 """


num = int(input())
n_max = 0
n_min = 9
while num != 0:
    if num % 10 < n_min:
        n_min = num % 10
    if num % 10 > n_max:
        n_max = num % 10
    num = num // 10
print('Максимальная цифра равна', n_max)
print('Минимальная цифра равна', n_min)
