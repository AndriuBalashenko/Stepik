# Правильная скобочная последовательность 🌶️
# Напишите функцию is_correct_bracket(text),
# которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True
# если поступившая на вход строка является правильной
# скобочной последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью
# называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка.

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return (len(text) == 0)

txt = input()
print(is_correct_bracket(txt))
#
# def is_correct_bracket(text):
#     count = 0
#     for i in text:
#         if i == '(':
#             count += 1
#         if i == ')':
#             count -= 1
#         if count < 0:
#             return False
#     return (count == 0)
#
# txt = input()
# print(is_correct_bracket(txt))


# В способе про count в конце проверок на открытые и закрытые скобки
# делается проверка на count меньше 0, если меньше нуля,
# то возвращаем фолс и дальнейшая работа кода прекращается.
# Почему и для чего? Если прогнать через https://pythontutor.com ,
# то видно, что когда count  = -1, это значит что код считывает ')'
# закрытую скобку перед которой не было парной ей открытой скобки,
# а это значит что если и будет далее парная ей открытая скобка,
# то они будут располагаться по отношению друг к другу вот так )(  ,
# а это противоречит условию задачи. Скобки,
# располагающиеся так по отношению друг к другу не являются парными.
