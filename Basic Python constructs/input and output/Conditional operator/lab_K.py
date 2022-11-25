"""
Одно из древних поверий гласит, что трёхзначное число красиво, если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.

Напишите систему определяющую красоту числа.

Формат ввода
Одно трёхзначное число

Формат вывода
YES — если число красивое, иначе — NO
"""

number = int(input())
first_figure = number // 100
second_figure = number // 10 % 10
third_figure = number % 10
max_figure = max(first_figure, second_figure, third_figure)
min_figure = min(first_figure, second_figure, third_figure)
if max_figure + min_figure == 2 * (first_figure + second_figure + third_figure - min_figure - max_figure):
    print("YES")
else:
    print("NO")