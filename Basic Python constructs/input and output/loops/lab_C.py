"""
Ребята в детском саду учат числа, и мы можем им в этом помочь.
Ребята дают нам два числа — начало и конец последовательности чисел.
Наша задача вывести все числа от начала до конца, заполнив промежуток между ними.

Формат ввода
Два числа в порядке возрастания, каждое с новой строки.

Формат вывода
Все числа от начала до конца (включительно), записанные через пробел.
"""
start_position, end_position = int(input()), int(input())
for i in range(start_position, end_position + 1):
    if i == end_position:
        print(i, end = '')
    else:
        print(i, end = ' ')