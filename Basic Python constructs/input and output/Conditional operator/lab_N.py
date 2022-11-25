"""
Во времена, когда люди верили в великую силу чисел, оказалось, что волшебник Пифуман предал все народы и стал помогать Зерону.

Чтобы посетить башни обоих злодеев одновременно, нам следует разделить магию числа, которое защищало нас в дороге.

Чтобы поделить трёхзначное число, нам нужно составить из него минимально и максимально возможные двухзначные числа.
"""
number = input()
min_figure = min(int(number[0]), int(number[1]), int(number[2]))
max_figure = max(int(number[0]), int(number[1]), int(number[2]))
middle_figure = int(number[0]) + int(number[1]) + int(number[2]) - min_figure - max_figure
if min_figure == 0:
    print(middle_figure * 10 + min_figure, max_figure * 10 + middle_figure)
else:
    print(min_figure * 10 + middle_figure, max_figure * 10 + middle_figure)
