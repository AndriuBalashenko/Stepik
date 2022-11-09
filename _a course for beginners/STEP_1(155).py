# Палиндром 🌶️
# Напишите функцию is_palindrome(text),
# которая принимает в качестве аргумента строку text
# и возвращает значение True
# если указанный текст является палиндромом
# и False в противном случае.
#
# Примечание 1. Палиндром – это строка,
# которая читается одинаково в обоих направлениях
#
# Примечание 2. При проверке считайте большие и
# маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.


def is_palindrome(text):
    audit_text = []
    for i in text.lower():
        if i.isalpha():
            audit_text.append(i)

    if audit_text[:] == audit_text[::-1]:
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))

# audit_text = [i.lower() for i in text if i.isalpha()]
#     return audit_text == audit_text[::-1]