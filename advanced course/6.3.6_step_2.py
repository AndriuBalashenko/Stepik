# Программист Тимур написал программу для работы с биографическими данными русских поэтов.
# Данные содержатся в кортежах вида (фамилия, год рождения, город рождения).
# В процессе работы программы в некотором кортеже poet_data обнаружилась ошибка:
# ('Пушкин', 1799, 'Санкт-Петербург'), неверно указано место рождения,
# ведь Александр Пушкин родился в Москве.
#
# Дополните приведенный код так, чтобы в переменной poet_data
# находился правильный кортеж (с исправленным значением), а затем выведите его содержимое.

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
l = list(poet_data)
l[2] = 'Москва'
poet_data = tuple(l)
print(poet_data)
