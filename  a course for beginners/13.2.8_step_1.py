# Звездный треугольник.
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.

def draw_triangle(fill, base):
    for i in range(1, (base + 3) // 2):
        print(fill * i)
    for j in range(base // 2, 0, -1):
        print(fill * j)
fill = input()
base = int(input())
draw_triangle(fill, base)




