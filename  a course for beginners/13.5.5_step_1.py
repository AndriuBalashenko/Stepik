# Good password 🌶️
# Напишите функцию is_password_good(password),
# которая принимает в качестве аргумента строковое значение
# пароля password и возвращает значение True
# если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):

    if len(password) < 8:
        return  False
    flag_A = False
    flag_a = False
    flag_1 = False
    for item in password:
        if item.isupper():
            flag_A = True
        elif item.islower():
            flag_a = True
        elif item.isdigit():
            flag_1 = True
    return flag_A and flag_a and flag_1


txt = input()

print(is_password_good(txt))

#  В цикле пробегаемся по каждой букве. Если выполнится первый if,
#  цикл прервется и флаг станет тру.
#  а если какой то из других elif, то тоже какой то флаг станет трушным
#  и цикл на этой букве прервется,  перейдем проверять другую букву.
# Если соберутся все три тру, то супер, в конце будет выведено тру.
# True = 1, False = 0,
# т.е. если True and True and True то это будет выглядеть так, 1*1*1 = 1, т.е. 1 = True.
# а если хоть где то будет False, пример True and False and True, будет так 1*0*1 = 0, т.е. 0 = False.