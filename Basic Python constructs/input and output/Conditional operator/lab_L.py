"""
Есть много музыкальных инструментов, но Вася обожает треугольник.

У него завалялось немного алюминиевых трубочек разной длины, и он задаётся вопросом, а можно ли из них сделать любимый музыкальный инструмент.

Формат ввода
Три числа — длины трубочек, каждое с новой строки.

Формат вывода
YES — если Васе удастся создать музыкальный треугольник, иначе — NO

Примечание
Обратите внимание, что в треугольнике любая сторона меньше суммы двух других.
"""

first_side, second_side, third_side = int(input()), int(input()), int(input())
max_side = max(first_side, second_side, third_side)
min_side = min(first_side, second_side, third_side)
middle_side = first_side + second_side + third_side - max_side - min_side
if middle_side + min_side > max_side:
    print("YES")
else:
    print("NO")