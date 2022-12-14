# Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря
# с сдвигом вправо на 10 символов.
#
# Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).

step = 10
string = 'Блажен, кто верует, тепло ему на свете!'
res = ''
for char in string.lower():
    if ord(char) not in range(1071, 1103):
        res += char
    elif ord(char) + 10 > 1103:
        res += chr(ord(char) + 10 - 32)

    else:
        res += chr(ord(char) + 10)

print(res.capitalize())

""" 1. Создаём пустую строку.
    2. Перебираем каждый символ в строке, переведенной в нижний регистр.
        2.1 Если числового значения Unicode (функция opd()) нет в диапазоне Unicode русского алфавита
            в нижнем регистре: print(ord("а")) = 1072(включительно), print(ord("я")) = 1103, 
            2.1.1 То в созданную строку добавляем все символы(мы в цикле фор), которых нету (в указанном диапазоне)
                В течение фор получается новая строка из всех символов начальной строки, кроме букв.
        2.2 Если числовое значения Unicode (функция opd()) + 10 больше верхнего значения unicode
            (это проверка на нахождение уже "сдвинутых"(зашифрованных) символов вне пределов диапазона unicode)
            2.2.2 То в нашу новую строку добавляем сам символ (chr)(сумма значения символа(ord) плюс сдвиг минус 
                количество букв в русском алфавите (32), чтобы зациклить Unicode
        2.3 В остальных случаях в новую строку добавляем сам символ (chr)(сумма значения символа(ord) плюс сдвиг
    3. Выводим новую строку, используя capitalise()(Возвращает копию строки, переводя первую буквы в верхний регистр,
     а остальные в нижний)
     
     То есть получается, что в течение цикла фор, программа посимвольно проверяет является ли символ буквой или 
     нет, и формирует нашу пустую строку новыми символами, которую потом и выводим.  """