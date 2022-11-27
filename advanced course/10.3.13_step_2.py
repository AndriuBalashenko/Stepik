#  Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s.
#  Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
#  С помощью .split() разбиваем строку на части, используя разделитель, и возвращает эти части списком.
#  Создаём пустой словарь.
result = {}
#  Заполняем словарь. Цикл for перебирает все элементы списка s и для каждого элемента
#  с помощью метода get() мы получаем либо его значение из словаря result,
#  либо значение по умолчанию, равное 0. К данному значению прибавляется единица,
#  и результат записывается обратно в словарь по нужному ключу.
for i in s:
    result[i] = result.get(i, 0) + 1
#  Определяем максимальную цифру среди значений словаря, она равна 12.
max_result = max(result.values())
#  Создаём пустой список, чтобы туда сложить все слова(ключи),
#  соответствующие максимальному значению value словаря. В данном случае
# по значению value 12 у нас получится список из двух слов('barley': 12, 'banana': 12):
# список ['barley', 'banana']
res_lst = []
for key, value in result.items():
    if value == max_result:
        res_lst.append(key)
#  Используя функцию min() выводим на печать меньше в лексикографическом порядке значение списка(banana).
print(min(res_lst))
