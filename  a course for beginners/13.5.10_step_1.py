# Змеиный регистр
# Напишите функцию convert_to_python_case(text),
# которая принимает в качестве аргумента строку
# в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    new_text = text[0].lower()
    for i in text[1:]:
        if i.isupper():
            new_text = new_text + '_' + i.lower()
        else:
            new_text += i

    return new_text

txt = input()

print(convert_to_python_case(txt))