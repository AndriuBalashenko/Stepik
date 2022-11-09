# программа, которая считывает одну строку,
# после чего выводит «YES», если в введённой строке есть подстрока
# «суббота» или «воскресенье», и «NO» в противном случае.
s = input()
if 'суббота' in s or 'воскресенье' in s:
    print('YES')
else:
    print('NO')

# помним, что оператор имеет приоритет перед оператором or
# поэтому код:  if 'суббота' or 'воскресенье' in s:
# будет неправильным.
# 1/ программа считает воскресенье in s, получит False(если его нет),
# затем будет читать суббота или False in s.


